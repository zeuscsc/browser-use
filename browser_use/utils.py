import asyncio
import logging
import os
import platform
import signal
import time
from collections.abc import Callable, Coroutine
from fnmatch import fnmatch
from functools import cache, wraps
from pathlib import Path
from sys import stderr
from typing import Any, ParamSpec, TypeVar
from urllib.parse import urlparse

from dotenv import load_dotenv

load_dotenv()


logger = logging.getLogger(__name__)

# Import error types - these may need to be adjusted based on actual import paths
try:
	from openai import BadRequestError as OpenAIBadRequestError
except ImportError:
	OpenAIBadRequestError = None

try:
	from groq import BadRequestError as GroqBadRequestError  # type: ignore[import-not-found]
except ImportError:
	GroqBadRequestError = None


# Global flag to prevent duplicate exit messages
_exiting = False

# Define generic type variables for return type and parameters
R = TypeVar('R')
T = TypeVar('T')
P = ParamSpec('P')


class SignalHandler:
	"""
	A modular and reusable signal handling system for managing SIGINT (Ctrl+C), SIGTERM,
	and other signals in asyncio applications.

	This class provides:
	- Configurable signal handling for SIGINT and SIGTERM
	- Support for custom pause/resume callbacks
	- Management of event loop state across signals
	- Standardized handling of first and second Ctrl+C presses
	- Cross-platform compatibility (with simplified behavior on Windows)
	"""

	def __init__(
		self,
		loop: asyncio.AbstractEventLoop | None = None,
		pause_callback: Callable[[], None] | None = None,
		resume_callback: Callable[[], None] | None = None,
		custom_exit_callback: Callable[[], None] | None = None,
		exit_on_second_int: bool = True,
		interruptible_task_patterns: list[str] | None = None,
	):
		"""
		Initialize the signal handler.

		Args:
			loop: The asyncio event loop to use. Defaults to current event loop.
			pause_callback: Function to call when system is paused (first Ctrl+C)
			resume_callback: Function to call when system is resumed
			custom_exit_callback: Function to call on exit (second Ctrl+C or SIGTERM)
			exit_on_second_int: Whether to exit on second SIGINT (Ctrl+C)
			interruptible_task_patterns: List of patterns to match task names that should be
										 canceled on first Ctrl+C (default: ['step', 'multi_act', 'get_next_action'])
		"""
		self.loop = loop or asyncio.get_event_loop()
		self.pause_callback = pause_callback
		self.resume_callback = resume_callback
		self.custom_exit_callback = custom_exit_callback
		self.exit_on_second_int = exit_on_second_int
		self.interruptible_task_patterns = interruptible_task_patterns or ['step', 'multi_act', 'get_next_action']
		self.is_windows = platform.system() == 'Windows'

		# Initialize loop state attributes
		self._initialize_loop_state()

		# Store original signal handlers to restore them later if needed
		self.original_sigint_handler = None
		self.original_sigterm_handler = None

	def _initialize_loop_state(self) -> None:
		"""Initialize loop state attributes used for signal handling."""
		setattr(self.loop, 'ctrl_c_pressed', False)
		setattr(self.loop, 'waiting_for_input', False)

	def register(self) -> None:
		"""Register signal handlers for SIGINT and SIGTERM."""
		try:
			if self.is_windows:
				# On Windows, use simple signal handling with immediate exit on Ctrl+C
				def windows_handler(sig, frame):
					print('\n\n🛑 Got Ctrl+C. Exiting immediately on Windows...\n', file=stderr)
					# Run the custom exit callback if provided
					if self.custom_exit_callback:
						self.custom_exit_callback()
					os._exit(0)

				self.original_sigint_handler = signal.signal(signal.SIGINT, windows_handler)
			else:
				# On Unix-like systems, use asyncio's signal handling for smoother experience
				self.original_sigint_handler = self.loop.add_signal_handler(signal.SIGINT, lambda: self.sigint_handler())
				self.original_sigterm_handler = self.loop.add_signal_handler(signal.SIGTERM, lambda: self.sigterm_handler())

		except Exception:
			# there are situations where signal handlers are not supported, e.g.
			# - when running in a thread other than the main thread
			# - some operating systems
			# - inside jupyter notebooks
			pass

	def unregister(self) -> None:
		"""Unregister signal handlers and restore original handlers if possible."""
		try:
			if self.is_windows:
				# On Windows, just restore the original SIGINT handler
				if self.original_sigint_handler:
					signal.signal(signal.SIGINT, self.original_sigint_handler)
			else:
				# On Unix-like systems, use asyncio's signal handler removal
				self.loop.remove_signal_handler(signal.SIGINT)
				self.loop.remove_signal_handler(signal.SIGTERM)

				# Restore original handlers if available
				if self.original_sigint_handler:
					signal.signal(signal.SIGINT, self.original_sigint_handler)
				if self.original_sigterm_handler:
					signal.signal(signal.SIGTERM, self.original_sigterm_handler)
		except Exception as e:
			logger.warning(f'Error while unregistering signal handlers: {e}')

	def _handle_second_ctrl_c(self) -> None:
		"""
		Handle a second Ctrl+C press by performing cleanup and exiting.
		This is shared logic used by both sigint_handler and wait_for_resume.
		"""
		global _exiting

		if not _exiting:
			_exiting = True

			# Call custom exit callback if provided
			if self.custom_exit_callback:
				try:
					self.custom_exit_callback()
				except Exception as e:
					logger.error(f'Error in exit callback: {e}')

		# Force immediate exit - more reliable than sys.exit()
		print('\n\n🛑  Got second Ctrl+C. Exiting immediately...\n', file=stderr)

		# Reset terminal to a clean state by sending multiple escape sequences
		# Order matters for terminal resets - we try different approaches

		# Reset terminal modes for both stdout and stderr
		print('\033[?25h', end='', flush=True, file=stderr)  # Show cursor
		print('\033[?25h', end='', flush=True)  # Show cursor

		# Reset text attributes and terminal modes
		print('\033[0m', end='', flush=True, file=stderr)  # Reset text attributes
		print('\033[0m', end='', flush=True)  # Reset text attributes

		# Disable special input modes that may cause arrow keys to output control chars
		print('\033[?1l', end='', flush=True, file=stderr)  # Reset cursor keys to normal mode
		print('\033[?1l', end='', flush=True)  # Reset cursor keys to normal mode

		# Disable bracketed paste mode
		print('\033[?2004l', end='', flush=True, file=stderr)
		print('\033[?2004l', end='', flush=True)

		# Carriage return helps ensure a clean line
		print('\r', end='', flush=True, file=stderr)
		print('\r', end='', flush=True)

		# these ^^ attempts dont work as far as we can tell
		# we still dont know what causes the broken input, if you know how to fix it, please let us know
		print('(tip: press [Enter] once to fix escape codes appearing after chrome exit)', file=stderr)

		os._exit(0)

	def sigint_handler(self) -> None:
		"""
		SIGINT (Ctrl+C) handler.

		First Ctrl+C: Cancel current step and pause.
		Second Ctrl+C: Exit immediately if exit_on_second_int is True.
		"""
		global _exiting

		if _exiting:
			# Already exiting, force exit immediately
			os._exit(0)

		if getattr(self.loop, 'ctrl_c_pressed', False):
			# If we're in the waiting for input state, let the pause method handle it
			if getattr(self.loop, 'waiting_for_input', False):
				return

			# Second Ctrl+C - exit immediately if configured to do so
			if self.exit_on_second_int:
				self._handle_second_ctrl_c()

		# Mark that Ctrl+C was pressed
		setattr(self.loop, 'ctrl_c_pressed', True)

		# Cancel current tasks that should be interruptible - this is crucial for immediate pausing
		self._cancel_interruptible_tasks()

		# Call pause callback if provided - this sets the paused flag
		if self.pause_callback:
			try:
				self.pause_callback()
			except Exception as e:
				logger.error(f'Error in pause callback: {e}')

		# Log pause message after pause_callback is called (not before)
		print('----------------------------------------------------------------------', file=stderr)

	def sigterm_handler(self) -> None:
		"""
		SIGTERM handler.

		Always exits the program completely.
		"""
		global _exiting
		if not _exiting:
			_exiting = True
			print('\n\n🛑 SIGTERM received. Exiting immediately...\n\n', file=stderr)

			# Call custom exit callback if provided
			if self.custom_exit_callback:
				self.custom_exit_callback()

		os._exit(0)

	def _cancel_interruptible_tasks(self) -> None:
		"""Cancel current tasks that should be interruptible."""
		current_task = asyncio.current_task(self.loop)
		for task in asyncio.all_tasks(self.loop):
			if task != current_task and not task.done():
				task_name = task.get_name() if hasattr(task, 'get_name') else str(task)
				# Cancel tasks that match certain patterns
				if any(pattern in task_name for pattern in self.interruptible_task_patterns):
					logger.debug(f'Cancelling task: {task_name}')
					task.cancel()
					# Add exception handler to silence "Task exception was never retrieved" warnings
					task.add_done_callback(lambda t: t.exception() if t.cancelled() else None)

		# Also cancel the current task if it's interruptible
		if current_task and not current_task.done():
			task_name = current_task.get_name() if hasattr(current_task, 'get_name') else str(current_task)
			if any(pattern in task_name for pattern in self.interruptible_task_patterns):
				logger.debug(f'Cancelling current task: {task_name}')
				current_task.cancel()

	def wait_for_resume(self) -> None:
		"""
		Wait for user input to resume or exit.

		This method should be called after handling the first Ctrl+C.
		It temporarily restores default signal handling to allow catching
		a second Ctrl+C directly.
		"""
		# Set flag to indicate we're waiting for input
		setattr(self.loop, 'waiting_for_input', True)

		# Temporarily restore default signal handling for SIGINT
		# This ensures KeyboardInterrupt will be raised during input()
		original_handler = signal.getsignal(signal.SIGINT)
		try:
			signal.signal(signal.SIGINT, signal.default_int_handler)
		except ValueError:
			# we are running in a thread other than the main thread
			# or signal handlers are not supported for some other reason
			pass

		green = '\x1b[32;1m'
		red = '\x1b[31m'
		blink = '\033[33;5m'
		unblink = '\033[0m'
		reset = '\x1b[0m'

		try:  # escape code is to blink the ...
			print(
				f'➡️  Press {green}[Enter]{reset} to resume or {red}[Ctrl+C]{reset} again to exit{blink}...{unblink} ',
				end='',
				flush=True,
				file=stderr,
			)
			input()  # This will raise KeyboardInterrupt on Ctrl+C

			# Call resume callback if provided
			if self.resume_callback:
				self.resume_callback()
		except KeyboardInterrupt:
			# Use the shared method to handle second Ctrl+C
			self._handle_second_ctrl_c()
		finally:
			try:
				# Restore our signal handler
				signal.signal(signal.SIGINT, original_handler)
				setattr(self.loop, 'waiting_for_input', False)
			except Exception:
				pass

	def reset(self) -> None:
		"""Reset state after resuming."""
		# Clear the flags
		if hasattr(self.loop, 'ctrl_c_pressed'):
			setattr(self.loop, 'ctrl_c_pressed', False)
		if hasattr(self.loop, 'waiting_for_input'):
			setattr(self.loop, 'waiting_for_input', False)


def time_execution_sync(additional_text: str = '') -> Callable[[Callable[P, R]], Callable[P, R]]:
	def decorator(func: Callable[P, R]) -> Callable[P, R]:
		@wraps(func)
		def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
			start_time = time.time()
			result = func(*args, **kwargs)
			execution_time = time.time() - start_time
			# Only log if execution takes more than 0.25 seconds
			if execution_time > 0.25:
				self_has_logger = args and getattr(args[0], 'logger', None)
				if self_has_logger:
					logger = getattr(args[0], 'logger')
				elif 'agent' in kwargs:
					logger = getattr(kwargs['agent'], 'logger')
				elif 'browser_session' in kwargs:
					logger = getattr(kwargs['browser_session'], 'logger')
				else:
					logger = logging.getLogger(__name__)
				logger.debug(f'⏳ {additional_text.strip("-")}() took {execution_time:.2f}s')
			return result

		return wrapper

	return decorator


def time_execution_async(
	additional_text: str = '',
) -> Callable[[Callable[P, Coroutine[Any, Any, R]]], Callable[P, Coroutine[Any, Any, R]]]:
	def decorator(func: Callable[P, Coroutine[Any, Any, R]]) -> Callable[P, Coroutine[Any, Any, R]]:
		@wraps(func)
		async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
			start_time = time.time()
			result = await func(*args, **kwargs)
			execution_time = time.time() - start_time
			# Only log if execution takes more than 0.25 seconds to avoid spamming the logs
			# you can lower this threshold locally when you're doing dev work to performance optimize stuff
			if execution_time > 0.25:
				self_has_logger = args and getattr(args[0], 'logger', None)
				if self_has_logger:
					logger = getattr(args[0], 'logger')
				elif 'agent' in kwargs:
					logger = getattr(kwargs['agent'], 'logger')
				elif 'browser_session' in kwargs:
					logger = getattr(kwargs['browser_session'], 'logger')
				else:
					logger = logging.getLogger(__name__)
				logger.debug(f'⏳ {additional_text.strip("-")}() took {execution_time:.2f}s')
			return result

		return wrapper

	return decorator


def singleton(cls):
	instance = [None]

	def wrapper(*args, **kwargs):
		if instance[0] is None:
			instance[0] = cls(*args, **kwargs)
		return instance[0]

	return wrapper


def check_env_variables(keys: list[str], any_or_all=all) -> bool:
	"""Check if all required environment variables are set"""
	return any_or_all(os.getenv(key, '').strip() for key in keys)


def is_unsafe_pattern(pattern: str) -> bool:
	"""
	Check if a domain pattern has complex wildcards that could match too many domains.

	Args:
		pattern: The domain pattern to check

	Returns:
		bool: True if the pattern has unsafe wildcards, False otherwise
	"""
	# Extract domain part if there's a scheme
	if '://' in pattern:
		_, pattern = pattern.split('://', 1)

	# Remove safe patterns (*.domain and domain.*)
	bare_domain = pattern.replace('.*', '').replace('*.', '')

	# If there are still wildcards, it's potentially unsafe
	return '*' in bare_domain


def is_new_tab_page(url: str) -> bool:
	"""
	Check if a URL is a new tab page (about:blank or chrome://new-tab-page).

	Args:
		url: The URL to check

	Returns:
		bool: True if the URL is a new tab page, False otherwise
	"""
	return url in ('about:blank', 'chrome://new-tab-page/', 'chrome://new-tab-page')


def match_url_with_domain_pattern(url: str, domain_pattern: str, log_warnings: bool = False) -> bool:
	"""
	Check if a URL matches a domain pattern. SECURITY CRITICAL.

	Supports optional glob patterns and schemes:
	- *.example.com will match sub.example.com and example.com
	- *google.com will match google.com, agoogle.com, and www.google.com
	- http*://example.com will match http://example.com, https://example.com
	- chrome-extension://* will match chrome-extension://aaaaaaaaaaaa and chrome-extension://bbbbbbbbbbbbb

	When no scheme is specified, https is used by default for security.
	For example, 'example.com' will match 'https://example.com' but not 'http://example.com'.

	Note: New tab pages (about:blank, chrome://new-tab-page) must be handled at the callsite, not inside this function.

	Args:
		url: The URL to check
		domain_pattern: Domain pattern to match against
		log_warnings: Whether to log warnings about unsafe patterns

	Returns:
		bool: True if the URL matches the pattern, False otherwise
	"""
	try:
		# Note: new tab pages should be handled at the callsite, not here
		if is_new_tab_page(url):
			return False

		parsed_url = urlparse(url)

		# Extract only the hostname and scheme components
		scheme = parsed_url.scheme.lower() if parsed_url.scheme else ''
		domain = parsed_url.hostname.lower() if parsed_url.hostname else ''

		if not scheme or not domain:
			return False

		# Normalize the domain pattern
		domain_pattern = domain_pattern.lower()

		# Handle pattern with scheme
		if '://' in domain_pattern:
			pattern_scheme, pattern_domain = domain_pattern.split('://', 1)
		else:
			pattern_scheme = 'https'  # Default to matching only https for security
			pattern_domain = domain_pattern

		# Handle port in pattern (we strip ports from patterns since we already
		# extracted only the hostname from the URL)
		if ':' in pattern_domain and not pattern_domain.startswith(':'):
			pattern_domain = pattern_domain.split(':', 1)[0]

		# If scheme doesn't match, return False
		if not fnmatch(scheme, pattern_scheme):
			return False

		# Check for exact match
		if pattern_domain == '*' or domain == pattern_domain:
			return True

		# Handle glob patterns
		if '*' in pattern_domain:
			# Check for unsafe glob patterns
			# First, check for patterns like *.*.domain which are unsafe
			if pattern_domain.count('*.') > 1 or pattern_domain.count('.*') > 1:
				if log_warnings:
					logger = logging.getLogger(__name__)
					logger.error(f'⛔️ Multiple wildcards in pattern=[{domain_pattern}] are not supported')
				return False  # Don't match unsafe patterns

			# Check for wildcards in TLD part (example.*)
			if pattern_domain.endswith('.*'):
				if log_warnings:
					logger = logging.getLogger(__name__)
					logger.error(f'⛔️ Wildcard TLDs like in pattern=[{domain_pattern}] are not supported for security')
				return False  # Don't match unsafe patterns

			# Then check for embedded wildcards
			bare_domain = pattern_domain.replace('*.', '')
			if '*' in bare_domain:
				if log_warnings:
					logger = logging.getLogger(__name__)
					logger.error(f'⛔️ Only *.domain style patterns are supported, ignoring pattern=[{domain_pattern}]')
				return False  # Don't match unsafe patterns

			# Special handling so that *.google.com also matches bare google.com
			if pattern_domain.startswith('*.'):
				parent_domain = pattern_domain[2:]
				if domain == parent_domain or fnmatch(domain, parent_domain):
					return True

			# Normal case: match domain against pattern
			if fnmatch(domain, pattern_domain):
				return True

		return False
	except Exception as e:
		logger = logging.getLogger(__name__)
		logger.error(f'⛔️ Error matching URL {url} with pattern {domain_pattern}: {type(e).__name__}: {e}')
		return False


def merge_dicts(a: dict, b: dict, path: tuple[str, ...] = ()):
	for key in b:
		if key in a:
			if isinstance(a[key], dict) and isinstance(b[key], dict):
				merge_dicts(a[key], b[key], path + (str(key),))
			elif isinstance(a[key], list) and isinstance(b[key], list):
				a[key] = a[key] + b[key]
			elif a[key] != b[key]:
				raise Exception('Conflict at ' + '.'.join(path + (str(key),)))
		else:
			a[key] = b[key]
	return a


@cache
def get_browser_use_version() -> str:
	"""Get the browser-use package version using the same logic as Agent._set_browser_use_version_and_source"""
	try:
		package_root = Path(__file__).parent.parent
		pyproject_path = package_root / 'pyproject.toml'

		# Try to read version from pyproject.toml
		if pyproject_path.exists():
			import re

			with open(pyproject_path, encoding='utf-8') as f:
				content = f.read()
				match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', content)
				if match:
					version = f'{match.group(1)}'
					os.environ['LIBRARY_VERSION'] = version  # used by bubus event_schema so all Event schemas include versioning
					return version

		# If pyproject.toml doesn't exist, try getting version from pip
		from importlib.metadata import version as get_version

		version = str(get_version('browser-use'))
		os.environ['LIBRARY_VERSION'] = version
		return version

	except Exception as e:
		logger.debug(f'Error detecting browser-use version: {type(e).__name__}: {e}')
		return 'unknown'


def _log_pretty_path(path: str | Path | None) -> str:
	"""Pretty-print a path, shorten home dir to ~ and cwd to ."""

	if not path or not str(path).strip():
		return ''  # always falsy in -> falsy out so it can be used in ternaries

	# dont print anything thats not a path
	if not isinstance(path, (str, Path)):
		# no other types are safe to just str(path) and log to terminal unless we know what they are
		# e.g. what if we get storage_date=dict | Path and the dict version could contain real cookies
		return f'<{type(path).__name__}>'

	# replace home dir and cwd with ~ and .
	pretty_path = str(path).replace(str(Path.home()), '~').replace(str(Path.cwd().resolve()), '.')

	# wrap in quotes if it contains spaces
	if pretty_path.strip() and ' ' in pretty_path:
		pretty_path = f'"{pretty_path}"'

	return pretty_path


def _log_pretty_url(s: str, max_len: int | None = 22) -> str:
	"""Truncate/pretty-print a URL with a maximum length, removing the protocol and www. prefix"""
	s = s.replace('https://', '').replace('http://', '').replace('www.', '')
	if max_len is not None and len(s) > max_len:
		return s[:max_len] + '…'
	return s
