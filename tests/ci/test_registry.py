"""
Comprehensive tests for the action registry system to ensure backward compatibility
and proper parameter handling for all existing patterns.

Tests cover:
1. Existing parameter patterns (individual params, pydantic models)
2. Special parameter injection (browser_session, page_extraction_llm, etc.)
3. Action-to-action calling scenarios
4. Mixed parameter patterns
5. Registry execution edge cases
"""

import asyncio
import logging

import pytest
from pydantic import Field
from pytest_httpserver import HTTPServer
from pytest_httpserver.httpserver import HandlerType

from browser_use.agent.views import ActionResult
from browser_use.browser import BrowserSession
from browser_use.browser.profile import BrowserProfile
from browser_use.browser.types import Page
from browser_use.controller.registry.service import Registry
from browser_use.controller.registry.views import ActionModel as BaseActionModel
from browser_use.controller.views import (
	ClickElementAction,
	InputTextAction,
	NoParamsAction,
	SearchGoogleAction,
)
from browser_use.llm.messages import UserMessage
from tests.ci.conftest import create_mock_llm

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestContext:
	"""Simple context for testing"""

	pass


# Test parameter models
class SimpleParams(BaseActionModel):
	"""Simple parameter model"""

	value: str = Field(description='Test value')


class ComplexParams(BaseActionModel):
	"""Complex parameter model with multiple fields"""

	text: str = Field(description='Text input')
	number: int = Field(description='Number input', default=42)
	optional_flag: bool = Field(description='Optional boolean', default=False)


# Test fixtures
@pytest.fixture(scope='session')
def http_server():
	"""Create and provide a test HTTP server that serves static content."""
	server = HTTPServer()
	server.start()

	# Add a simple test page that can handle multiple requests
	server.expect_request('/test', handler_type=HandlerType.PERMANENT).respond_with_data(
		'<html><head><title>Test Page</title></head><body><h1>Test Page</h1><p>Hello from test page</p></body></html>',
		content_type='text/html',
	)

	yield server
	server.stop()


@pytest.fixture(scope='session')
def base_url(http_server):
	"""Return the base URL for the test HTTP server."""
	return f'http://{http_server.host}:{http_server.port}'


@pytest.fixture(scope='module')
def mock_llm():
	"""Create a mock LLM"""
	return create_mock_llm()


@pytest.fixture(scope='function')
def registry():
	"""Create a fresh registry for each test"""
	return Registry[TestContext]()


@pytest.fixture(scope='session')
async def browser_session(base_url):
	"""Create a real BrowserSession for testing"""
	browser_session = BrowserSession(
		browser_profile=BrowserProfile(
			headless=True,
			user_data_dir=None,
		)
	)
	await browser_session.start()
	await browser_session.create_new_tab(f'{base_url}/test')
	yield browser_session
	await browser_session.kill()


class TestActionRegistryParameterPatterns:
	"""Test different parameter patterns that should all continue to work"""

	async def test_individual_parameters_no_browser(self, registry):
		"""Test action with individual parameters, no special injection"""

		@registry.action('Simple action with individual params')
		async def simple_action(text: str, number: int = 10):
			return ActionResult(extracted_content=f'Text: {text}, Number: {number}')

		# Test execution
		result = await registry.execute_action('simple_action', {'text': 'hello', 'number': 42})

		assert isinstance(result, ActionResult)
		assert result.extracted_content is not None
		assert 'Text: hello, Number: 42' in result.extracted_content

	async def test_individual_parameters_with_browser(self, registry, browser_session, base_url):
		"""Test action with individual parameters plus browser_session injection"""

		@registry.action('Action with individual params and browser')
		async def action_with_browser(text: str, browser_session: BrowserSession):
			page = await browser_session.get_current_page()
			return ActionResult(extracted_content=f'Text: {text}, URL: {page.url}')

		# Navigate to test page first
		await browser_session.create_new_tab(f'{base_url}/test')

		# Test execution
		result = await registry.execute_action('action_with_browser', {'text': 'hello'}, browser_session=browser_session)

		assert isinstance(result, ActionResult)
		assert result.extracted_content is not None
		assert 'Text: hello, URL:' in result.extracted_content
		assert base_url in result.extracted_content

	async def test_page_parameter_injection(self, registry, browser_session, base_url):
		"""Test action with direct Page parameter injection"""

		@registry.action('Action with page parameter')
		async def action_with_page(text: str, page: Page):
			title = await page.title()
			return ActionResult(extracted_content=f'Text: {text}, Page Title: {title}')

		# Navigate to test page first
		await browser_session.create_new_tab(f'{base_url}/test')

		# Test execution
		result = await registry.execute_action('action_with_page', {'text': 'hello'}, browser_session=browser_session)

		assert isinstance(result, ActionResult)
		assert result.extracted_content is not None
		assert 'Text: hello, Page Title: Test Page' in result.extracted_content

	async def test_pydantic_model_with_page_parameter(self, registry, browser_session, base_url):
		"""Test pydantic model action with page parameter injection"""

		@registry.action('Pydantic action with page', param_model=ComplexParams)
		async def pydantic_action_with_page(params: ComplexParams, page: Page):
			title = await page.title()
			return ActionResult(extracted_content=f'Text: {params.text}, Number: {params.number}, Page Title: {title}')

		# Navigate to test page first
		await browser_session.create_new_tab(f'{base_url}/test')

		# Test execution
		result = await registry.execute_action(
			'pydantic_action_with_page', {'text': 'test', 'number': 100}, browser_session=browser_session
		)

		assert isinstance(result, ActionResult)
		assert result.extracted_content is not None
		assert 'Text: test, Number: 100, Page Title: Test Page' in result.extracted_content

	async def test_pydantic_model_parameters(self, registry, browser_session, base_url):
		"""Test action that takes a pydantic model as first parameter"""

		@registry.action('Action with pydantic model', param_model=ComplexParams)
		async def pydantic_action(params: ComplexParams, browser_session: BrowserSession):
			page = await browser_session.get_current_page()
			return ActionResult(
				extracted_content=f'Text: {params.text}, Number: {params.number}, Flag: {params.optional_flag}, URL: {page.url}'
			)

		# Navigate to test page first
		await browser_session.create_new_tab(f'{base_url}/test')

		# Test execution
		result = await registry.execute_action(
			'pydantic_action', {'text': 'test', 'number': 100, 'optional_flag': True}, browser_session=browser_session
		)

		assert isinstance(result, ActionResult)
		assert result.extracted_content is not None
		assert 'Text: test, Number: 100, Flag: True' in result.extracted_content
		assert base_url in result.extracted_content

	async def test_mixed_special_parameters(self, registry, browser_session, base_url, mock_llm):
		"""Test action with multiple special injected parameters"""

		from browser_use.llm.base import BaseChatModel

		@registry.action('Action with multiple special params')
		async def multi_special_action(
			text: str,
			page: Page,
			page_extraction_llm: BaseChatModel,
			available_file_paths: list,
		):
			llm_response = await page_extraction_llm.ainvoke([UserMessage(content='test')])
			files = available_file_paths or []

			return ActionResult(
				extracted_content=f'Text: {text}, URL: {page.url}, LLM: {llm_response.completion}, Files: {len(files)}'
			)

		# Navigate to test page first
		await browser_session.create_new_tab(f'{base_url}/test')

		# Test execution
		result = await registry.execute_action(
			'multi_special_action',
			{'text': 'hello'},
			browser_session=browser_session,
			page_extraction_llm=mock_llm,
			available_file_paths=['file1.txt', 'file2.txt'],
		)

		assert isinstance(result, ActionResult)
		assert result.extracted_content is not None
		assert 'Text: hello' in result.extracted_content
		assert base_url in result.extracted_content
		# The mock LLM returns a JSON response
		assert '"Task completed successfully"' in result.extracted_content
		assert 'Files: 2' in result.extracted_content

	async def test_no_params_action(self, registry, browser_session):
		"""Test action with NoParamsAction model"""

		@registry.action('No params action', param_model=NoParamsAction)
		async def no_params_action(params: NoParamsAction, page: Page):
			return ActionResult(extracted_content=f'No params action executed on {page.url}')

		# Test execution with any parameters (should be ignored)
		result = await registry.execute_action(
			'no_params_action', {'random': 'data', 'should': 'be', 'ignored': True}, browser_session=browser_session
		)

		assert isinstance(result, ActionResult)
		assert result.extracted_content is not None
		assert 'No params action executed on' in result.extracted_content
		assert '/test' in result.extracted_content

	async def test_legacy_browser_parameter_names(self, registry, browser_session):
		"""Test that legacy browser parameter names still work"""

		@registry.action('Action with legacy browser param')
		async def legacy_browser_action(text: str, browser: BrowserSession):
			page = await browser.get_current_page()
			return ActionResult(extracted_content=f'Legacy browser: {text}, URL: {page.url}')

		@registry.action('Action with legacy browser_context param')
		async def legacy_context_action(text: str, browser_context: BrowserSession):
			page = await browser_context.get_current_page()
			return ActionResult(extracted_content=f'Legacy context: {text}, URL: {page.url}')

		# Test legacy browser parameter
		result1 = await registry.execute_action('legacy_browser_action', {'text': 'test1'}, browser_session=browser_session)
		assert result1.extracted_content is not None
		assert 'Legacy browser: test1, URL:' in result1.extracted_content
		assert '/test' in result1.extracted_content

		# Test legacy browser_context parameter
		result2 = await registry.execute_action('legacy_context_action', {'text': 'test2'}, browser_session=browser_session)
		assert result2.extracted_content is not None
		assert 'Legacy context: test2, URL:' in result2.extracted_content
		assert '/test' in result2.extracted_content

	async def test_page_parameter_optimization(self, browser_session: BrowserSession, httpserver: HTTPServer):
		"""Test that actions can use page: Page parameter directly instead of browser_session"""
		registry = Registry()

		httpserver.expect_request('/test').respond_with_data('<html><body>Test Page</body></html>')
		page = await browser_session.get_current_page()
		await page.goto(httpserver.url_for('/test'))

		# Action that takes page directly (optimized pattern)
		@registry.action('Action with direct page parameter')
		async def direct_page_action(text: str, page: Page):
			# This is the optimized pattern - no need to call get_current_page()
			return ActionResult(extracted_content=f'Direct page: {text}, URL: {page.url}')

		# Action that takes browser_session and calls get_current_page (old pattern)
		@registry.action('Action with browser_session parameter')
		async def browser_session_action(text: str, browser_session: BrowserSession):
			page = await browser_session.get_current_page()
			return ActionResult(extracted_content=f'Browser session: {text}, URL: {page.url}')

		# Test direct page parameter
		result1 = await registry.execute_action('direct_page_action', {'text': 'optimized'}, browser_session=browser_session)
		assert result1.extracted_content is not None
		assert 'Direct page: optimized, URL:' in result1.extracted_content
		assert '/test' in result1.extracted_content

		# Test browser_session parameter (should still work)
		result2 = await registry.execute_action('browser_session_action', {'text': 'legacy'}, browser_session=browser_session)
		assert result2.extracted_content is not None
		assert 'Browser session: legacy, URL:' in result2.extracted_content
		assert '/test' in result2.extracted_content

		# Verify both patterns work with pydantic models too
		class PageActionParams(BaseActionModel):
			message: str = Field(..., description='Test message')

		@registry.action('Pydantic action with page', param_model=PageActionParams)
		async def pydantic_page_action(params: PageActionParams, page: Page):
			return ActionResult(extracted_content=f'Pydantic page: {params.message}, URL: {page.url}')

		result3 = await registry.execute_action('pydantic_page_action', {'message': 'pydantic'}, browser_session=browser_session)
		assert result3.extracted_content is not None
		assert 'Pydantic page: pydantic, URL:' in result3.extracted_content
		assert '/test' in result3.extracted_content


class TestActionToActionCalling:
	"""Test scenarios where actions call other actions"""

	async def test_action_calling_action_with_kwargs(self, registry, browser_session):
		"""Test action calling another action using kwargs (current problematic pattern)"""

		# Helper function that actions can call
		async def helper_function(browser_session: BrowserSession, data: str):
			page = await browser_session.get_current_page()
			return f'Helper processed: {data} on {page.url}'

		@registry.action('First action')
		async def first_action(text: str, browser_session: BrowserSession):
			# This should work without parameter conflicts
			result = await helper_function(browser_session=browser_session, data=text)
			return ActionResult(extracted_content=f'First: {result}')

		@registry.action('Calling action')
		async def calling_action(message: str, browser_session: BrowserSession):
			# Call the first action through the registry (simulates action-to-action calling)
			intermediate_result = await registry.execute_action(
				'first_action', {'text': message}, browser_session=browser_session
			)
			return ActionResult(extracted_content=f'Called result: {intermediate_result.extracted_content}')

		# Test the calling chain
		result = await registry.execute_action('calling_action', {'message': 'test'}, browser_session=browser_session)

		assert isinstance(result, ActionResult)
		assert result.extracted_content is not None
		assert 'Called result: First: Helper processed: test on' in result.extracted_content
		assert '/test' in result.extracted_content

	async def test_google_sheets_style_calling_pattern(self, registry, browser_session):
		"""Test the specific pattern from Google Sheets actions that causes the error"""

		# Simulate the _select_cell_or_range helper function
		async def _select_cell_or_range(browser_session: BrowserSession, cell_or_range: str):
			page = await browser_session.get_current_page()
			return ActionResult(extracted_content=f'Selected cell {cell_or_range} on {page.url}')

		@registry.action('Select cell or range')
		async def select_cell_or_range(cell_or_range: str, browser_session: BrowserSession):
			# This pattern now works with kwargs
			return await _select_cell_or_range(browser_session=browser_session, cell_or_range=cell_or_range)

		@registry.action('Select cell or range (fixed)')
		async def select_cell_or_range_fixed(cell_or_range: str, browser_session: BrowserSession):
			# This pattern also works
			return await _select_cell_or_range(browser_session, cell_or_range)

		@registry.action('Update range contents')
		async def update_range_contents(range_name: str, new_contents: str, browser_session: BrowserSession):
			# This action calls select_cell_or_range, simulating the real Google Sheets pattern
			# Get the action's param model to call it properly
			action = registry.registry.actions['select_cell_or_range_fixed']
			params = action.param_model(cell_or_range=range_name)
			await select_cell_or_range_fixed(cell_or_range=range_name, browser_session=browser_session)
			return ActionResult(extracted_content=f'Updated range {range_name} with {new_contents}')

		# Test the fixed version (should work)
		result_fixed = await registry.execute_action(
			'select_cell_or_range_fixed', {'cell_or_range': 'A1:F100'}, browser_session=browser_session
		)
		assert result_fixed.extracted_content is not None
		assert 'Selected cell A1:F100 on' in result_fixed.extracted_content
		assert '/test' in result_fixed.extracted_content

		# Test the chained calling pattern
		result_chain = await registry.execute_action(
			'update_range_contents', {'range_name': 'B2:D4', 'new_contents': 'test data'}, browser_session=browser_session
		)
		assert result_chain.extracted_content is not None
		assert 'Updated range B2:D4 with test data' in result_chain.extracted_content

		# Test the problematic version (should work with enhanced registry)
		result_problematic = await registry.execute_action(
			'select_cell_or_range', {'cell_or_range': 'A1:F100'}, browser_session=browser_session
		)
		# With the enhanced registry, this should succeed
		assert result_problematic.extracted_content is not None
		assert 'Selected cell A1:F100 on' in result_problematic.extracted_content
		assert '/test' in result_problematic.extracted_content

	async def test_complex_action_chain(self, registry, browser_session):
		"""Test a complex chain of actions calling other actions"""

		@registry.action('Base action')
		async def base_action(value: str, browser_session: BrowserSession):
			page = await browser_session.get_current_page()
			return ActionResult(extracted_content=f'Base: {value} on {page.url}')

		@registry.action('Middle action')
		async def middle_action(input_val: str, browser_session: BrowserSession):
			# Call base action
			base_result = await registry.execute_action(
				'base_action', {'value': f'processed-{input_val}'}, browser_session=browser_session
			)
			return ActionResult(extracted_content=f'Middle: {base_result.extracted_content}')

		@registry.action('Top action')
		async def top_action(original: str, browser_session: BrowserSession):
			# Call middle action
			middle_result = await registry.execute_action(
				'middle_action', {'input_val': f'enhanced-{original}'}, browser_session=browser_session
			)
			return ActionResult(extracted_content=f'Top: {middle_result.extracted_content}')

		# Test the full chain
		result = await registry.execute_action('top_action', {'original': 'test'}, browser_session=browser_session)

		assert isinstance(result, ActionResult)
		assert result.extracted_content is not None
		assert 'Top: Middle: Base: processed-enhanced-test on' in result.extracted_content
		assert '/test' in result.extracted_content


class TestRegistryEdgeCases:
	"""Test edge cases and error conditions"""

	async def test_decorated_action_rejects_positional_args(self, registry, browser_session):
		"""Test that decorated actions reject positional arguments"""

		@registry.action('Action that should reject positional args')
		async def test_action(cell_or_range: str, browser_session: BrowserSession):
			page = await browser_session.get_current_page()
			return ActionResult(extracted_content=f'Selected cell {cell_or_range} on {page.url}')

		# Test that calling with positional arguments raises TypeError
		with pytest.raises(
			TypeError, match='test_action\\(\\) does not accept positional arguments, only keyword arguments are allowed'
		):
			await test_action('A1:B2', browser_session)

		# Test that calling with keyword arguments works
		result = await test_action(browser_session=browser_session, cell_or_range='A1:B2')
		assert isinstance(result, ActionResult)
		assert result.extracted_content is not None
		assert 'Selected cell A1:B2 on' in result.extracted_content

	async def test_missing_required_browser_session(self, registry):
		"""Test that actions requiring browser_session fail appropriately when not provided"""

		@registry.action('Requires browser')
		async def requires_browser(text: str, browser_session: BrowserSession):
			page = await browser_session.get_current_page()
			return ActionResult(extracted_content=f'Text: {text}, URL: {page.url}')

		# Should raise RuntimeError when browser_session is required but not provided
		with pytest.raises(RuntimeError, match='requires browser_session but none provided'):
			await registry.execute_action(
				'requires_browser',
				{'text': 'test'},
				# No browser_session provided
			)

	async def test_missing_required_llm(self, registry, browser_session):
		"""Test that actions requiring page_extraction_llm fail appropriately when not provided"""

		from browser_use.llm.base import BaseChatModel

		@registry.action('Requires LLM')
		async def requires_llm(text: str, browser_session: BrowserSession, page_extraction_llm: BaseChatModel):
			page = await browser_session.get_current_page()
			llm_response = await page_extraction_llm.ainvoke([UserMessage(content='test')])
			return ActionResult(extracted_content=f'Text: {text}, LLM: {llm_response.completion}')

		# Should raise RuntimeError when page_extraction_llm is required but not provided
		with pytest.raises(RuntimeError, match='requires page_extraction_llm but none provided'):
			await registry.execute_action(
				'requires_llm',
				{'text': 'test'},
				browser_session=browser_session,
				# No page_extraction_llm provided
			)

	async def test_invalid_parameters(self, registry, browser_session):
		"""Test handling of invalid parameters"""

		@registry.action('Typed action')
		async def typed_action(number: int, browser_session: BrowserSession):
			return ActionResult(extracted_content=f'Number: {number}')

		# Should raise RuntimeError when parameter validation fails
		with pytest.raises(RuntimeError, match='Invalid parameters'):
			await registry.execute_action(
				'typed_action',
				{'number': 'not a number'},  # Invalid type
				browser_session=browser_session,
			)

	async def test_nonexistent_action(self, registry, browser_session):
		"""Test calling a non-existent action"""

		with pytest.raises(ValueError, match='Action nonexistent_action not found'):
			await registry.execute_action('nonexistent_action', {'param': 'value'}, browser_session=browser_session)

	async def test_sync_action_wrapper(self, registry, browser_session):
		"""Test that sync functions are properly wrapped to be async"""

		@registry.action('Sync action')
		def sync_action(text: str, browser_session: BrowserSession):
			# This is a sync function that should be wrapped
			return ActionResult(extracted_content=f'Sync: {text}')

		# Should work even though the original function is sync
		result = await registry.execute_action('sync_action', {'text': 'test'}, browser_session=browser_session)

		assert isinstance(result, ActionResult)
		assert result.extracted_content is not None
		assert 'Sync: test' in result.extracted_content

	async def test_excluded_actions(self, browser_session):
		"""Test that excluded actions are not registered"""

		registry_with_exclusions = Registry[TestContext](exclude_actions=['excluded_action'])

		@registry_with_exclusions.action('Excluded action')
		async def excluded_action(text: str):
			return ActionResult(extracted_content=f'Should not execute: {text}')

		@registry_with_exclusions.action('Included action')
		async def included_action(text: str):
			return ActionResult(extracted_content=f'Should execute: {text}')

		# Excluded action should not be in registry
		assert 'excluded_action' not in registry_with_exclusions.registry.actions
		assert 'included_action' in registry_with_exclusions.registry.actions

		# Should raise error when trying to execute excluded action
		with pytest.raises(ValueError, match='Action excluded_action not found'):
			await registry_with_exclusions.execute_action('excluded_action', {'text': 'test'})

		# Included action should work
		result = await registry_with_exclusions.execute_action('included_action', {'text': 'test'})
		assert result.extracted_content is not None
		assert 'Should execute: test' in result.extracted_content


class TestExistingControllerActions:
	"""Test that existing controller actions continue to work"""

	async def test_existing_action_models(self, registry, browser_session):
		"""Test that existing action parameter models work correctly"""

		@registry.action('Test search', param_model=SearchGoogleAction)
		async def test_search(params: SearchGoogleAction, browser_session: BrowserSession):
			return ActionResult(extracted_content=f'Searched for: {params.query}')

		@registry.action('Test click', param_model=ClickElementAction)
		async def test_click(params: ClickElementAction, browser_session: BrowserSession):
			return ActionResult(extracted_content=f'Clicked element: {params.index}')

		@registry.action('Test input', param_model=InputTextAction)
		async def test_input(params: InputTextAction, browser_session: BrowserSession):
			return ActionResult(extracted_content=f'Input text: {params.text} at index: {params.index}')

		# Test SearchGoogleAction
		result1 = await registry.execute_action('test_search', {'query': 'python testing'}, browser_session=browser_session)
		assert result1.extracted_content is not None
		assert 'Searched for: python testing' in result1.extracted_content

		# Test ClickElementAction
		result2 = await registry.execute_action('test_click', {'index': 42}, browser_session=browser_session)
		assert result2.extracted_content is not None
		assert 'Clicked element: 42' in result2.extracted_content

		# Test InputTextAction
		result3 = await registry.execute_action('test_input', {'index': 5, 'text': 'test input'}, browser_session=browser_session)
		assert result3.extracted_content is not None
		assert 'Input text: test input at index: 5' in result3.extracted_content

	async def test_pydantic_vs_individual_params_consistency(self, registry, browser_session):
		"""Test that pydantic and individual parameter patterns produce consistent results"""

		# Action using individual parameters
		@registry.action('Individual params')
		async def individual_params_action(text: str, number: int, browser_session: BrowserSession):
			return ActionResult(extracted_content=f'Individual: {text}-{number}')

		# Action using pydantic model
		class TestParams(BaseActionModel):
			text: str
			number: int

		@registry.action('Pydantic params', param_model=TestParams)
		async def pydantic_params_action(params: TestParams, browser_session: BrowserSession):
			return ActionResult(extracted_content=f'Pydantic: {params.text}-{params.number}')

		# Both should produce similar results
		test_data = {'text': 'hello', 'number': 42}

		result1 = await registry.execute_action('individual_params_action', test_data, browser_session=browser_session)

		result2 = await registry.execute_action('pydantic_params_action', test_data, browser_session=browser_session)

		# Both should extract the same content (just different prefixes)
		assert result1.extracted_content is not None
		assert 'hello-42' in result1.extracted_content
		assert result2.extracted_content is not None
		assert 'hello-42' in result2.extracted_content
		assert 'Individual:' in result1.extracted_content
		assert 'Pydantic:' in result2.extracted_content


class TestType1Pattern:
	"""Test Type 1 Pattern: Pydantic model first (from normalization tests)"""

	def test_type1_with_param_model(self):
		"""Type 1: action(params: Model, special_args...) should work"""
		registry = Registry()

		class ClickAction(BaseActionModel):
			index: int
			delay: float = 0.0

		@registry.action('Click element', param_model=ClickAction)
		async def click_element(params: ClickAction, browser_session: BrowserSession):
			return ActionResult(extracted_content=f'Clicked {params.index}')

		# Verify registration
		assert 'click_element' in registry.registry.actions
		action = registry.registry.actions['click_element']
		assert action.param_model == ClickAction

		# Verify decorated function signature (should be kwargs-only)
		import inspect

		sig = inspect.signature(click_element)
		params = list(sig.parameters.values())

		# Should have no positional-only or positional-or-keyword params
		for param in params:
			assert param.kind in (inspect.Parameter.KEYWORD_ONLY, inspect.Parameter.VAR_KEYWORD)

	def test_type1_with_multiple_special_params(self):
		"""Type 1 with multiple special params should work"""
		registry = Registry()

		class ExtractAction(BaseActionModel):
			goal: str
			include_links: bool = False

		from browser_use.llm.base import BaseChatModel

		@registry.action('Extract content', param_model=ExtractAction)
		async def extract_content(
			params: ExtractAction, browser_session: BrowserSession, page: Page, page_extraction_llm: BaseChatModel
		):
			return ActionResult(extracted_content=params.goal)

		assert 'extract_content' in registry.registry.actions


class TestType2Pattern:
	"""Test Type 2 Pattern: loose parameters (from normalization tests)"""

	def test_type2_simple_action(self):
		"""Type 2: action(arg1, arg2, special_args...) should work"""
		registry = Registry()

		@registry.action('Fill field')
		async def fill_field(index: int, text: str, page: Page):
			return ActionResult(extracted_content=f'Filled {index} with {text}')

		# Verify registration
		assert 'fill_field' in registry.registry.actions
		action = registry.registry.actions['fill_field']

		# Should auto-generate param model
		assert action.param_model is not None
		assert 'index' in action.param_model.model_fields
		assert 'text' in action.param_model.model_fields

	def test_type2_with_defaults(self):
		"""Type 2 with default values should preserve defaults"""
		registry = Registry()

		@registry.action('Scroll page')
		async def scroll_page(direction: str = 'down', amount: int = 100, browser_session: BrowserSession = None):  # type: ignore
			return ActionResult(extracted_content=f'Scrolled {direction} by {amount}')

		action = registry.registry.actions['scroll_page']
		# Check that defaults are preserved in generated model
		schema = action.param_model.model_json_schema()
		assert schema['properties']['direction']['default'] == 'down'
		assert schema['properties']['amount']['default'] == 100

	def test_type2_no_action_params(self):
		"""Type 2 with only special params should work"""
		registry = Registry()

		@registry.action('Save PDF')
		async def save_pdf(browser_session: BrowserSession, page: Page):
			return ActionResult(extracted_content='Saved PDF')

		action = registry.registry.actions['save_pdf']
		# Should have empty or minimal param model
		fields = action.param_model.model_fields
		assert len(fields) == 0 or all(f in ['title'] for f in fields)

	def test_no_special_params_action(self):
		"""Test action with no special params (like wait action in Controller)"""
		registry = Registry()

		@registry.action('Wait for x seconds default 3')
		async def wait(seconds: int = 3):
			await asyncio.sleep(seconds)
			return ActionResult(extracted_content=f'Waited {seconds} seconds')

		# Should register successfully
		assert 'wait' in registry.registry.actions
		action = registry.registry.actions['wait']

		# Should have seconds in param model
		assert 'seconds' in action.param_model.model_fields

		# Should preserve default value
		schema = action.param_model.model_json_schema()
		assert schema['properties']['seconds']['default'] == 3


class TestValidationRules:
	"""Test validation rules for action registration (from normalization tests)"""

	def test_error_on_kwargs_in_original_function(self):
		"""Should error if original function has kwargs"""
		registry = Registry()

		with pytest.raises(ValueError, match='kwargs.*not allowed'):

			@registry.action('Bad action')
			async def bad_action(index: int, page: Page, **kwargs):
				pass

	def test_error_on_special_param_name_with_wrong_type(self):
		"""Should error if special param name used with wrong type"""
		registry = Registry()

		# Using 'page' with str type should error
		with pytest.raises(ValueError, match=rf'conflicts with special argument.*page: {repr(Page)}'):

			@registry.action('Navigate')
			async def navigate_to_page(page: str, browser_session: BrowserSession):
				pass

		# Using 'browser_session' with wrong type should error
		with pytest.raises(ValueError, match='conflicts with special argument.*browser_session: BrowserSession'):

			@registry.action('Bad session')
			async def bad_session(browser_session: str):
				pass

	def test_special_params_must_match_type(self):
		"""Special params with correct types should work"""
		registry = Registry()

		@registry.action('Good action')
		async def good_action(
			index: int,
			page: Page,  # Correct type
			browser_session: BrowserSession,  # Correct type
		):
			return ActionResult()

		assert 'good_action' in registry.registry.actions


class TestDecoratedFunctionBehavior:
	"""Test behavior of decorated action functions (from normalization tests)"""

	async def test_decorated_function_only_accepts_kwargs(self):
		"""Decorated functions should only accept kwargs, no positional args"""
		registry = Registry()

		class MockBrowserSession:
			async def get_current_page(self):
				return None

		@registry.action('Click')
		async def click(index: int, browser_session: BrowserSession):
			return ActionResult()

		# Should raise error when called with positional args
		with pytest.raises(TypeError, match='positional arguments'):
			await click(5, MockBrowserSession())

	async def test_decorated_function_accepts_params_model(self):
		"""Decorated function should accept params as model"""
		registry = Registry()

		class MockBrowserSession:
			async def get_current_page(self):
				return None

		@registry.action('Input text')
		async def input_text(index: int, text: str, browser_session: BrowserSession):
			return ActionResult(extracted_content=f'{index}:{text}')

		# Get the generated param model class
		action = registry.registry.actions['input_text']
		ParamsModel = action.param_model

		# Should work with params model
		result = await input_text(params=ParamsModel(index=5, text='hello'), browser_session=MockBrowserSession())
		assert result.extracted_content == '5:hello'

	async def test_decorated_function_ignores_extra_kwargs(self):
		"""Decorated function should ignore extra kwargs for easy unpacking"""
		registry = Registry()

		class MockPage:
			pass

		@registry.action('Simple action')
		async def simple_action(value: int, page: Page):
			return ActionResult(extracted_content=str(value))

		# Should work even with extra kwargs
		special_context = {
			'page': MockPage(),
			'browser_session': None,
			'page_extraction_llm': create_mock_llm(),
			'context': {'extra': 'data'},
			'unknown_param': 'ignored',
		}

		action = registry.registry.actions['simple_action']
		ParamsModel = action.param_model

		result = await simple_action(params=ParamsModel(value=42), **special_context)
		assert result.extracted_content == '42'


class TestParamsModelGeneration:
	"""Test automatic parameter model generation (from normalization tests)"""

	def test_generates_model_from_non_special_args(self):
		"""Should generate param model from non-special positional args"""
		registry = Registry()

		@registry.action('Complex action')
		async def complex_action(
			query: str,
			max_results: int,
			include_images: bool = True,
			page: Page = None,  # type: ignore
			browser_session: BrowserSession = None,  # type: ignore
		):
			return ActionResult()

		action = registry.registry.actions['complex_action']
		model_fields = action.param_model.model_fields

		# Should include only non-special params
		assert 'query' in model_fields
		assert 'max_results' in model_fields
		assert 'include_images' in model_fields

		# Should NOT include special params
		assert 'page' not in model_fields
		assert 'browser_session' not in model_fields

	def test_preserves_type_annotations(self):
		"""Generated model should preserve type annotations"""
		registry = Registry()

		@registry.action('Typed action')
		async def typed_action(
			count: int,
			rate: float,
			enabled: bool,
			name: str | None = None,
			browser_session: BrowserSession = None,  # type: ignore
		):
			return ActionResult()

		action = registry.registry.actions['typed_action']
		schema = action.param_model.model_json_schema()

		# Check types are preserved
		assert schema['properties']['count']['type'] == 'integer'
		assert schema['properties']['rate']['type'] == 'number'
		assert schema['properties']['enabled']['type'] == 'boolean'
		# Optional should allow null
		assert 'null' in schema['properties']['name']['anyOf'][1]['type']


class TestErrorMessages:
	"""Test error messages for validation failures (from normalization tests)"""

	def test_clear_error_for_kwargs(self):
		"""Error message for kwargs should be clear"""
		registry = Registry()

		try:

			@registry.action('Bad')
			async def bad(x: int, **kwargs):
				pass

			pytest.fail('Should have raised ValueError')
		except ValueError as e:
			assert 'kwargs' in str(e).lower()
			assert 'not allowed' in str(e).lower()
			assert 'bad' in str(e).lower()  # Should mention function name

	def test_clear_error_for_param_conflicts(self):
		"""Error message for param conflicts should be helpful"""
		registry = Registry()

		try:

			@registry.action('Bad')
			async def bad(page: str):
				pass

			pytest.fail('Should have raised ValueError')
		except ValueError as e:
			error_msg = str(e)
			assert 'page: str' in error_msg
			assert 'conflicts' in error_msg
			assert f'page: {repr(Page)}' in error_msg  # Show expected type
			assert 'bad' in error_msg.lower()  # Show function name


class TestParameterOrdering:
	"""Test mixed ordering of parameters (from normalization tests)"""

	def test_mixed_param_ordering(self):
		"""Should handle any ordering of action params and special params"""
		registry = Registry()
		from browser_use.llm.base import BaseChatModel

		# Special params mixed throughout
		@registry.action('Mixed params')
		async def mixed_action(
			first: str,
			browser_session: BrowserSession,
			second: int,
			page: Page,
			third: bool = True,
			page_extraction_llm: BaseChatModel = None,  # type: ignore
		):
			return ActionResult()

		action = registry.registry.actions['mixed_action']
		model_fields = action.param_model.model_fields

		# Only action params in model
		assert set(model_fields.keys()) == {'first', 'second', 'third'}
		assert model_fields['third'].default is True

	def test_all_params_at_end(self):
		"""Should work with all action params at the end"""
		registry = Registry()

		@registry.action('Params at end')
		async def params_at_end(page: Page, query: str, limit: int = 10):
			return ActionResult()

		action = registry.registry.actions['params_at_end']
		assert set(action.param_model.model_fields.keys()) == {'query', 'limit'}

	def test_extract_content_pattern_registration(self):
		"""Test that the extract_content pattern with mixed params registers correctly"""
		registry = Registry()

		# This is the problematic pattern: positional arg, then special args, then kwargs with defaults
		@registry.action('Extract content from page')
		async def extract_content(
			goal: str,
			page: Page,
			page_extraction_llm,
			include_links: bool = False,
		):
			return ActionResult(extracted_content=f'Goal: {goal}, include_links: {include_links}')

		# Verify registration
		assert 'extract_content' in registry.registry.actions
		action = registry.registry.actions['extract_content']

		# Check that the param model only includes user-facing params
		model_fields = action.param_model.model_fields
		assert 'goal' in model_fields
		assert 'include_links' in model_fields
		assert model_fields['include_links'].default is False

		# Special params should NOT be in the model
		assert 'page' not in model_fields
		assert 'page_extraction_llm' not in model_fields

		# Verify the action was properly registered
		assert action.name == 'extract_content'
		assert action.description == 'Extract content from page'


class TestParamsModelArgsAndKwargs:
	async def test_browser_session_double_kwarg(self):
		"""Run the test to diagnose browser_session parameter issue

		This test demonstrates the problem and our fix. The issue happens because:

		1. In controller/service.py, we have:
		```python
		@registry.action('Google Sheets: Select a specific cell or range of cells')
		async def select_cell_or_range(browser_session: BrowserSession, cell_or_range: str):
		    return await _select_cell_or_range(browser_session=browser_session, cell_or_range=cell_or_range)
		```

		2. When registry.execute_action calls this function, it adds browser_session to extra_args:
		```python
		# In registry/service.py
		if 'browser_session' in parameter_names:
		    extra_args['browser_session'] = browser_session
		```

		3. Then later, when calling action.function:
		```python
		return await action.function(**params_dict, **extra_args)
		```

		4. This effectively means browser_session is passed twice:
		- Once through extra_args['browser_session']
		- And again through params_dict['browser_session'] (from the original function)

		The fix is to pass browser_session positionally in select_cell_or_range:
		```python
		return await _select_cell_or_range(browser_session, cell_or_range)
		```

		This test confirms that this approach works.
		"""

		from browser_use.controller.registry.service import Registry
		from browser_use.controller.registry.views import ActionModel

		# Simple context for testing
		class TestContext:
			pass

		class MockBrowserSession:
			async def get_current_page(self):
				return None

		browser_session = MockBrowserSession()

		# Create registry
		registry = Registry[TestContext]()

		# Model that doesn't include browser_session (renamed to avoid pytest collecting it)
		class CellActionParams(ActionModel):
			value: str = Field(description='Test value')

		# Model that includes browser_session
		class ModelWithBrowser(ActionModel):
			value: str = Field(description='Test value')
			browser_session: BrowserSession = None  # type: ignore

		# Create a custom param model for select_cell_or_range
		class CellRangeParams(ActionModel):
			cell_or_range: str = Field(description='Cell or range to select')

		# Use the provided real browser session

		# Test with the real issue: select_cell_or_range
		# logger.info('\n\n=== Test: Simulating select_cell_or_range issue with correct model ===')

		# Define the function without using our registry - this will be a helper function
		async def _select_cell_or_range(browser_session, cell_or_range):
			"""Helper function for select_cell_or_range"""
			return f'Selected cell {cell_or_range}'

		# This simulates the actual issue we're seeing in the real code
		# The browser_session parameter is in both the function signature and passed as a named arg
		@registry.action('Google Sheets: Select a cell or range', param_model=CellRangeParams)
		async def select_cell_or_range(browser_session: BrowserSession, cell_or_range: str):
			# logger.info(f'select_cell_or_range called with browser_session={browser_session}, cell_or_range={cell_or_range}')

			# PROBLEMATIC LINE: browser_session is passed by name, matching the parameter name
			# This is what causes the "got multiple values" error in the real code
			return await _select_cell_or_range(browser_session=browser_session, cell_or_range=cell_or_range)

		# Fix attempt: Register a version that uses positional args instead
		@registry.action('Google Sheets: Select a cell or range (fixed)', param_model=CellRangeParams)
		async def select_cell_or_range_fixed(browser_session: BrowserSession, cell_or_range: str):
			# logger.info(f'select_cell_or_range_fixed called with browser_session={browser_session}, cell_or_range={cell_or_range}')

			# FIXED LINE: browser_session is passed positionally, avoiding the parameter name conflict
			return await _select_cell_or_range(browser_session, cell_or_range)

		# Another attempt: explicitly call using **kwargs to simulate what the registry does
		@registry.action('Google Sheets: Select with kwargs', param_model=CellRangeParams)
		async def select_with_kwargs(browser_session: BrowserSession, cell_or_range: str):
			# logger.info(f'select_with_kwargs called with browser_session={browser_session}, cell_or_range={cell_or_range}')

			# Get params and extra_args, like in Registry.execute_action
			params = {'cell_or_range': cell_or_range, 'browser_session': browser_session}
			extra_args = {'browser_session': browser_session}

			# Try to call _select_cell_or_range with both params and extra_args
			# This will fail with "got multiple values for keyword argument 'browser_session'"
			try:
				# logger.info('Attempting to call with both params and extra_args (should fail):')
				await _select_cell_or_range(**params, **extra_args)
			except TypeError as e:
				# logger.info(f'Expected error: {e}')

				# Remove browser_session from params to avoid the conflict
				params_fixed = dict(params)
				del params_fixed['browser_session']

				# logger.info(f'Fixed params: {params_fixed}')

				# This should work
				result = await _select_cell_or_range(**params_fixed, **extra_args)
				# logger.info(f'Success after fix: {result}')
				return result

		# Test the original problematic version
		# logger.info('\n--- Testing original problematic version ---')
		try:
			result1 = await registry.execute_action(
				'select_cell_or_range',
				{'cell_or_range': 'A1:F100'},
				browser_session=browser_session,  # type: ignore
			)
			# logger.info(f'Success! Result: {result1}')
		except Exception as e:
			logger.error(f'Error: {str(e)}')

		# Test the fixed version (using positional args)
		# logger.info('\n--- Testing fixed version (positional args) ---')
		try:
			result2 = await registry.execute_action(
				'select_cell_or_range_fixed',
				{'cell_or_range': 'A1:F100'},
				browser_session=browser_session,  # type: ignore
			)
			# logger.info(f'Success! Result: {result2}')
		except Exception as e:
			logger.error(f'Error: {str(e)}')

		# Test with kwargs version that simulates what Registry.execute_action does
		# logger.info('\n--- Testing kwargs simulation version ---')
		try:
			result3 = await registry.execute_action(
				'select_with_kwargs',
				{'cell_or_range': 'A1:F100'},
				browser_session=browser_session,  # type: ignore
			)
			# logger.info(f'Success! Result: {result3}')
		except Exception as e:
			logger.error(f'Error: {str(e)}')

		# Manual test of our theory: browser_session is passed twice
		# logger.info('\n--- Direct test of our theory ---')
		try:
			# Create the model instance
			params = CellRangeParams(cell_or_range='A1:F100')

			# First check if the extra_args approach works
			# logger.info('Checking if extra_args approach works:')
			extra_args = {'browser_session': browser_session}

			# If we were to modify Registry.execute_action:
			# 1. Check if the function parameter needs browser_session
			parameter_names = ['browser_session', 'cell_or_range']
			browser_keys = ['browser_session', 'browser', 'browser_context']

			# Create params dict
			param_dict = params.model_dump()
			# logger.info(f'params dict before: {param_dict}')

			# Apply our fix: remove browser_session from params dict
			for key in browser_keys:
				if key in param_dict and key in extra_args:
					# logger.info(f'Removing {key} from params dict')
					del param_dict[key]

			# logger.info(f'params dict after: {param_dict}')
			# logger.info(f'extra_args: {extra_args}')

			# This would be the fixed code:
			# return await action.function(**param_dict, **extra_args)

			# Call directly to test
			result3 = await select_cell_or_range(**param_dict, **extra_args)
			# logger.info(f'Success with our fix! Result: {result3}')
		except Exception as e:
			logger.error(f'Error with our manual test: {str(e)}')
