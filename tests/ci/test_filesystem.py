"""Tests for the FileSystem class and related file operations."""

import asyncio
import tempfile
from pathlib import Path

import pytest

from browser_use.filesystem.file_system import (
	DEFAULT_FILE_SYSTEM_PATH,
	INVALID_FILENAME_ERROR_MESSAGE,
	CsvFile,
	FileSystem,
	FileSystemState,
	JsonFile,
	MarkdownFile,
	TxtFile,
)


class TestBaseFile:
	"""Test the BaseFile abstract base class and its implementations."""

	def test_markdown_file_creation(self):
		"""Test MarkdownFile creation and basic properties."""
		md_file = MarkdownFile(name='test', content='# Hello World')

		assert md_file.name == 'test'
		assert md_file.content == '# Hello World'
		assert md_file.extension == 'md'
		assert md_file.full_name == 'test.md'
		assert md_file.get_size == 13
		assert md_file.get_line_count == 1

	def test_txt_file_creation(self):
		"""Test TxtFile creation and basic properties."""
		txt_file = TxtFile(name='notes', content='Hello\nWorld')

		assert txt_file.name == 'notes'
		assert txt_file.content == 'Hello\nWorld'
		assert txt_file.extension == 'txt'
		assert txt_file.full_name == 'notes.txt'
		assert txt_file.get_size == 11
		assert txt_file.get_line_count == 2

	def test_json_file_creation(self):
		"""Test JsonFile creation and basic properties."""
		json_content = '{"name": "John", "age": 30, "city": "New York"}'
		json_file = JsonFile(name='data', content=json_content)

		assert json_file.name == 'data'
		assert json_file.content == json_content
		assert json_file.extension == 'json'
		assert json_file.full_name == 'data.json'
		assert json_file.get_size == len(json_content)
		assert json_file.get_line_count == 1

	def test_csv_file_creation(self):
		"""Test CsvFile creation and basic properties."""
		csv_content = 'name,age,city\nJohn,30,New York\nJane,25,London'
		csv_file = CsvFile(name='users', content=csv_content)

		assert csv_file.name == 'users'
		assert csv_file.content == csv_content
		assert csv_file.extension == 'csv'
		assert csv_file.full_name == 'users.csv'
		assert csv_file.get_size == len(csv_content)
		assert csv_file.get_line_count == 3

	def test_file_content_operations(self):
		"""Test content update and append operations."""
		file_obj = TxtFile(name='test')

		# Initial content
		assert file_obj.content == ''
		assert file_obj.get_size == 0

		# Write content
		file_obj.write_file_content('First line')
		assert file_obj.content == 'First line'
		assert file_obj.get_size == 10

		# Append content
		file_obj.append_file_content('\nSecond line')
		assert file_obj.content == 'First line\nSecond line'
		assert file_obj.get_line_count == 2

		# Update content
		file_obj.update_content('New content')
		assert file_obj.content == 'New content'

	async def test_file_disk_operations(self):
		"""Test file sync to disk operations."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			tmp_path = Path(tmp_dir)
			file_obj = MarkdownFile(name='test', content='# Test Content')

			# Test sync to disk
			await file_obj.sync_to_disk(tmp_path)

			# Verify file was created on disk
			file_path = tmp_path / 'test.md'
			assert file_path.exists()
			assert file_path.read_text() == '# Test Content'

			# Test write operation
			await file_obj.write('# New Content', tmp_path)
			assert file_path.read_text() == '# New Content'
			assert file_obj.content == '# New Content'

			# Test append operation
			await file_obj.append('\n## Section 2', tmp_path)
			expected_content = '# New Content\n## Section 2'
			assert file_path.read_text() == expected_content
			assert file_obj.content == expected_content

	async def test_json_file_disk_operations(self):
		"""Test JSON file sync to disk operations."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			tmp_path = Path(tmp_dir)
			json_content = '{"users": [{"name": "John", "age": 30}]}'
			json_file = JsonFile(name='data', content=json_content)

			# Test sync to disk
			await json_file.sync_to_disk(tmp_path)

			# Verify file was created on disk
			file_path = tmp_path / 'data.json'
			assert file_path.exists()
			assert file_path.read_text() == json_content

			# Test write operation
			new_content = '{"users": [{"name": "Jane", "age": 25}]}'
			await json_file.write(new_content, tmp_path)
			assert file_path.read_text() == new_content
			assert json_file.content == new_content

			# Test append operation
			await json_file.append(', {"name": "Bob", "age": 35}', tmp_path)
			expected_content = new_content + ', {"name": "Bob", "age": 35}'
			assert file_path.read_text() == expected_content
			assert json_file.content == expected_content

	async def test_csv_file_disk_operations(self):
		"""Test CSV file sync to disk operations."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			tmp_path = Path(tmp_dir)
			csv_content = 'name,age,city\nJohn,30,New York'
			csv_file = CsvFile(name='users', content=csv_content)

			# Test sync to disk
			await csv_file.sync_to_disk(tmp_path)

			# Verify file was created on disk
			file_path = tmp_path / 'users.csv'
			assert file_path.exists()
			assert file_path.read_text() == csv_content

			# Test write operation
			new_content = 'name,age,city\nJane,25,London'
			await csv_file.write(new_content, tmp_path)
			assert file_path.read_text() == new_content
			assert csv_file.content == new_content

			# Test append operation
			await csv_file.append('\nBob,35,Paris', tmp_path)
			expected_content = new_content + '\nBob,35,Paris'
			assert file_path.read_text() == expected_content
			assert csv_file.content == expected_content

	def test_file_sync_to_disk_sync(self):
		"""Test synchronous disk sync operation."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			tmp_path = Path(tmp_dir)
			file_obj = TxtFile(name='sync_test', content='Sync content')

			# Test synchronous sync
			file_obj.sync_to_disk_sync(tmp_path)

			# Verify file was created
			file_path = tmp_path / 'sync_test.txt'
			assert file_path.exists()
			assert file_path.read_text() == 'Sync content'


class TestFileSystem:
	"""Test the FileSystem class functionality."""

	@pytest.fixture
	def temp_filesystem(self):
		"""Create a temporary FileSystem for testing."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			fs = FileSystem(base_dir=tmp_dir, create_default_files=True)
			yield fs
			try:
				fs.nuke()
			except Exception:
				pass  # Directory might already be cleaned up

	@pytest.fixture
	def empty_filesystem(self):
		"""Create a temporary FileSystem without default files."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			fs = FileSystem(base_dir=tmp_dir, create_default_files=False)
			yield fs
			try:
				fs.nuke()
			except Exception:
				pass

	def test_filesystem_initialization(self, temp_filesystem):
		"""Test FileSystem initialization with default files."""
		fs = temp_filesystem

		# Check that base directory and data directory exist
		assert fs.base_dir.exists()
		assert fs.data_dir.exists()
		assert fs.data_dir.name == DEFAULT_FILE_SYSTEM_PATH

		# Check default files are created
		assert 'todo.md' in fs.files
		assert len(fs.files) == 1

		# Check files exist on disk
		todo_path = fs.data_dir / 'todo.md'
		assert todo_path.exists()

	def test_filesystem_without_default_files(self, empty_filesystem):
		"""Test FileSystem initialization without default files."""
		fs = empty_filesystem

		assert fs.base_dir.exists()
		assert fs.data_dir.exists()
		assert len(fs.files) == 0

	def test_get_allowed_extensions(self, temp_filesystem):
		"""Test getting allowed file extensions."""
		fs = temp_filesystem
		extensions = fs.get_allowed_extensions()

		assert 'md' in extensions
		assert 'txt' in extensions
		assert 'json' in extensions
		assert 'csv' in extensions

	def test_filename_validation(self, temp_filesystem):
		"""Test filename validation."""
		fs = temp_filesystem

		# Valid filenames
		assert fs._is_valid_filename('test.md') is True
		assert fs._is_valid_filename('my_file.txt') is True
		assert fs._is_valid_filename('file-name.md') is True
		assert fs._is_valid_filename('file123.txt') is True
		assert fs._is_valid_filename('data.json') is True
		assert fs._is_valid_filename('users.csv') is True

		# Invalid filenames
		assert fs._is_valid_filename('test.doc') is False  # wrong extension
		assert fs._is_valid_filename('test') is False  # no extension
		assert fs._is_valid_filename('test.md.txt') is False  # multiple extensions
		assert fs._is_valid_filename('test with spaces.md') is False  # spaces
		assert fs._is_valid_filename('test@file.md') is False  # special chars
		assert fs._is_valid_filename('.md') is False  # no name
		assert fs._is_valid_filename('.json') is False  # no name
		assert fs._is_valid_filename('.csv') is False  # no name

	def test_filename_parsing(self, temp_filesystem):
		"""Test filename parsing into name and extension."""
		fs = temp_filesystem

		name, ext = fs._parse_filename('test.md')
		assert name == 'test'
		assert ext == 'md'

		name, ext = fs._parse_filename('my_file.TXT')
		assert name == 'my_file'
		assert ext == 'txt'  # Should be lowercased

		name, ext = fs._parse_filename('data.json')
		assert name == 'data'
		assert ext == 'json'

		name, ext = fs._parse_filename('users.CSV')
		assert name == 'users'
		assert ext == 'csv'  # Should be lowercased

	def test_get_file(self, temp_filesystem):
		"""Test getting files from the filesystem."""
		fs = temp_filesystem

		# Get non-existent file
		non_existent = fs.get_file('nonexistent.md')
		assert non_existent is None

		# Get file with invalid name
		invalid = fs.get_file('invalid@name.md')
		assert invalid is None

	def test_list_files(self, temp_filesystem):
		"""Test listing files in the filesystem."""
		fs = temp_filesystem
		files = fs.list_files()

		assert 'todo.md' in files
		assert len(files) == 1

	def test_display_file(self, temp_filesystem):
		"""Test displaying file content."""
		fs = temp_filesystem

		# Display existing file
		content = fs.display_file('todo.md')
		assert content == ''  # Default files are empty

		# Display non-existent file
		content = fs.display_file('nonexistent.md')
		assert content is None

		# Display file with invalid name
		content = fs.display_file('invalid@name.md')
		assert content is None

	async def test_read_file(self, temp_filesystem: FileSystem):
		"""Test reading file content with proper formatting."""
		fs: FileSystem = temp_filesystem

		# Read existing empty file
		result = await fs.read_file('todo.md')
		expected = 'Read from file todo.md.\n<content>\n\n</content>'
		assert result == expected

		# Read non-existent file
		result = await fs.read_file('nonexistent.md')
		assert result == "File 'nonexistent.md' not found."

		# Read file with invalid name
		result = await fs.read_file('invalid@name.md')
		assert result == INVALID_FILENAME_ERROR_MESSAGE

	async def test_write_file(self, temp_filesystem):
		"""Test writing content to files."""
		fs = temp_filesystem

		# Write to existing file
		result = await fs.write_file('results.md', '# Test Results\nThis is a test.')
		assert result == 'Data written to file results.md successfully.'

		# Verify content was written
		content = await fs.read_file('results.md')
		assert '# Test Results\nThis is a test.' in content

		# Write to new file
		result = await fs.write_file('new_file.txt', 'New file content')
		assert result == 'Data written to file new_file.txt successfully.'
		assert 'new_file.txt' in fs.files
		assert fs.get_file('new_file.txt').content == 'New file content'

		# Write with invalid filename
		result = await fs.write_file('invalid@name.md', 'content')
		assert result == INVALID_FILENAME_ERROR_MESSAGE

		# Write with invalid extension
		result = await fs.write_file('test.doc', 'content')
		assert result == INVALID_FILENAME_ERROR_MESSAGE

	async def test_write_json_file(self, temp_filesystem):
		"""Test writing JSON files."""
		fs = temp_filesystem

		# Write valid JSON content
		json_content = '{"users": [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]}'
		result = await fs.write_file('data.json', json_content)
		assert result == 'Data written to file data.json successfully.'

		# Verify content was written
		content = await fs.read_file('data.json')
		assert json_content in content

		# Verify file object was created
		assert 'data.json' in fs.files
		file_obj = fs.get_file('data.json')
		assert file_obj is not None
		assert isinstance(file_obj, JsonFile)
		assert file_obj.content == json_content

		# Write to new JSON file
		result = await fs.write_file('config.json', '{"debug": true, "port": 8080}')
		assert result == 'Data written to file config.json successfully.'
		assert 'config.json' in fs.files

	async def test_write_csv_file(self, temp_filesystem):
		"""Test writing CSV files."""
		fs = temp_filesystem

		# Write valid CSV content
		csv_content = 'name,age,city\nJohn,30,New York\nJane,25,London\nBob,35,Paris'
		result = await fs.write_file('users.csv', csv_content)
		assert result == 'Data written to file users.csv successfully.'

		# Verify content was written
		content = await fs.read_file('users.csv')
		assert csv_content in content

		# Verify file object was created
		assert 'users.csv' in fs.files
		file_obj = fs.get_file('users.csv')
		assert file_obj is not None
		assert isinstance(file_obj, CsvFile)
		assert file_obj.content == csv_content

		# Write to new CSV file
		result = await fs.write_file('products.csv', 'id,name,price\n1,Laptop,999.99\n2,Mouse,29.99')
		assert result == 'Data written to file products.csv successfully.'
		assert 'products.csv' in fs.files

	async def test_append_file(self, temp_filesystem):
		"""Test appending content to files."""
		fs = temp_filesystem

		# First write some content
		await fs.write_file('test.md', '# Title')

		# Append content
		result = await fs.append_file('test.md', '\n## Section 1')
		assert result == 'Data appended to file test.md successfully.'

		# Verify content was appended
		content = fs.get_file('test.md').content
		assert content == '# Title\n## Section 1'

		# Append to non-existent file
		result = await fs.append_file('nonexistent.md', 'content')
		assert result == "File 'nonexistent.md' not found."

		# Append with invalid filename
		result = await fs.append_file('invalid@name.md', 'content')
		assert result == INVALID_FILENAME_ERROR_MESSAGE

	async def test_append_json_file(self, temp_filesystem):
		"""Test appending content to JSON files."""
		fs = temp_filesystem

		# First write some JSON content
		await fs.write_file('data.json', '{"users": [{"name": "John", "age": 30}]}')

		# Append additional JSON content (note: this creates invalid JSON, but tests the append functionality)
		result = await fs.append_file('data.json', ', {"name": "Jane", "age": 25}')
		assert result == 'Data appended to file data.json successfully.'

		# Verify content was appended
		file_obj = fs.get_file('data.json')
		assert file_obj is not None
		expected_content = '{"users": [{"name": "John", "age": 30}]}, {"name": "Jane", "age": 25}'
		assert file_obj.content == expected_content

	async def test_append_csv_file(self, temp_filesystem):
		"""Test appending content to CSV files."""
		fs = temp_filesystem

		# First write some CSV content
		await fs.write_file('users.csv', 'name,age,city\nJohn,30,New York')

		# Append additional CSV row
		result = await fs.append_file('users.csv', '\nJane,25,London')
		assert result == 'Data appended to file users.csv successfully.'

		# Verify content was appended
		file_obj = fs.get_file('users.csv')
		assert file_obj is not None
		expected_content = 'name,age,city\nJohn,30,New York\nJane,25,London'
		assert file_obj.content == expected_content

		# Append another row
		await fs.append_file('users.csv', '\nBob,35,Paris')
		expected_content = 'name,age,city\nJohn,30,New York\nJane,25,London\nBob,35,Paris'
		assert file_obj.content == expected_content

	async def test_save_extracted_content(self, temp_filesystem):
		"""Test saving extracted content with auto-numbering."""
		fs = temp_filesystem

		# Save first extracted content
		result = await fs.save_extracted_content('First extracted content')
		assert result == 'Extracted content saved to file extracted_content_0.md successfully.'
		assert 'extracted_content_0.md' in fs.files
		assert fs.extracted_content_count == 1

		# Save second extracted content
		result = await fs.save_extracted_content('Second extracted content')
		assert result == 'Extracted content saved to file extracted_content_1.md successfully.'
		assert 'extracted_content_1.md' in fs.files
		assert fs.extracted_content_count == 2

		# Verify content
		content1 = fs.get_file('extracted_content_0.md').content
		content2 = fs.get_file('extracted_content_1.md').content
		assert content1 == 'First extracted content'
		assert content2 == 'Second extracted content'

	async def test_describe_with_content(self, temp_filesystem):
		"""Test describing filesystem with files containing content."""
		fs = temp_filesystem

		# Add content to files
		await fs.write_file('results.md', '# Results\nTest results here.')
		await fs.write_file('notes.txt', 'These are my notes.')

		description = fs.describe()

		# Should contain file information
		assert 'results.md' in description
		assert 'notes.txt' in description
		assert '# Results' in description
		assert 'These are my notes.' in description
		assert 'lines' in description

	async def test_describe_large_files(self, temp_filesystem):
		"""Test describing filesystem with large files (truncated content)."""
		fs = temp_filesystem

		# Create a large file
		large_content = '\n'.join([f'Line {i}' for i in range(100)])
		await fs.write_file('large.md', large_content)

		description = fs.describe()

		# Should be truncated with "more lines" indicator
		assert 'large.md' in description
		assert 'more lines' in description
		assert 'Line 0' in description  # Start should be shown
		assert 'Line 99' in description  # End should be shown

	def test_get_todo_contents(self, temp_filesystem):
		"""Test getting todo file contents."""
		fs = temp_filesystem

		# Initially empty
		todo_content = fs.get_todo_contents()
		assert todo_content == ''

		# Add content to todo
		fs.get_file('todo.md').update_content('- [ ] Task 1\n- [ ] Task 2')
		todo_content = fs.get_todo_contents()
		assert '- [ ] Task 1' in todo_content

	def test_get_state(self, temp_filesystem):
		"""Test getting filesystem state."""
		fs = temp_filesystem

		state = fs.get_state()

		assert isinstance(state, FileSystemState)
		assert state.base_dir == str(fs.base_dir)
		assert state.extracted_content_count == 0
		assert 'todo.md' in state.files

	async def test_from_state(self, temp_filesystem):
		"""Test restoring filesystem from state."""
		fs = temp_filesystem

		# Add some content
		await fs.write_file('results.md', '# Original Results')
		await fs.write_file('custom.txt', 'Custom content')
		await fs.save_extracted_content('Extracted data')

		# Get state
		state = fs.get_state()

		# Create new filesystem from state
		fs2 = FileSystem.from_state(state)

		# Verify restoration
		assert fs2.base_dir == fs.base_dir
		assert fs2.extracted_content_count == fs.extracted_content_count
		assert len(fs2.files) == len(fs.files)

		# Verify file contents
		file_obj = fs2.get_file('results.md')
		assert file_obj is not None
		assert file_obj.content == '# Original Results'
		file_obj = fs2.get_file('custom.txt')
		assert file_obj is not None
		assert file_obj.content == 'Custom content'
		file_obj = fs2.get_file('extracted_content_0.md')
		assert file_obj is not None
		assert file_obj.content == 'Extracted data'

		# Verify files exist on disk
		assert (fs2.data_dir / 'results.md').exists()
		assert (fs2.data_dir / 'custom.txt').exists()
		assert (fs2.data_dir / 'extracted_content_0.md').exists()

		# Clean up second filesystem
		fs2.nuke()

	async def test_complete_workflow_with_json_csv(self):
		"""Test a complete filesystem workflow with JSON and CSV files."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			# Create filesystem
			fs = FileSystem(base_dir=tmp_dir, create_default_files=True)

			# Write JSON configuration file
			config_json = '{"app": {"name": "TestApp", "version": "1.0"}, "database": {"host": "localhost", "port": 5432}}'
			await fs.write_file('config.json', config_json)

			# Write CSV data file
			users_csv = 'id,name,email,age\n1,John Doe,john@example.com,30\n2,Jane Smith,jane@example.com,25'
			await fs.write_file('users.csv', users_csv)

			# Append more data to CSV
			await fs.append_file('users.csv', '\n3,Bob Johnson,bob@example.com,35')

			# Update JSON configuration
			updated_config = '{"app": {"name": "TestApp", "version": "1.1"}, "database": {"host": "localhost", "port": 5432}, "features": {"logging": true}}'
			await fs.write_file('config.json', updated_config)

			# Create another JSON file for API responses
			api_response = '{"status": "success", "data": [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]}'
			await fs.write_file('api_response.json', api_response)

			# Create a products CSV file
			products_csv = (
				'sku,name,price,category\nLAP001,Gaming Laptop,1299.99,Electronics\nMOU001,Wireless Mouse,29.99,Accessories'
			)
			await fs.write_file('products.csv', products_csv)

			# Verify file listing
			files = fs.list_files()
			expected_files = ['todo.md', 'config.json', 'users.csv', 'api_response.json', 'products.csv']
			assert len(files) == len(expected_files)
			for expected_file in expected_files:
				assert expected_file in files

			# Verify JSON file contents
			config_file = fs.get_file('config.json')
			assert config_file is not None
			assert isinstance(config_file, JsonFile)
			assert config_file.content == updated_config

			api_file = fs.get_file('api_response.json')
			assert api_file is not None
			assert isinstance(api_file, JsonFile)
			assert api_file.content == api_response

			# Verify CSV file contents
			users_file = fs.get_file('users.csv')
			assert users_file is not None
			assert isinstance(users_file, CsvFile)
			expected_users_content = 'id,name,email,age\n1,John Doe,john@example.com,30\n2,Jane Smith,jane@example.com,25\n3,Bob Johnson,bob@example.com,35'
			assert users_file.content == expected_users_content

			products_file = fs.get_file('products.csv')
			assert products_file is not None
			assert isinstance(products_file, CsvFile)
			assert products_file.content == products_csv

			# Test state persistence with JSON and CSV files
			state = fs.get_state()
			fs.nuke()

			# Restore from state
			fs2 = FileSystem.from_state(state)

			# Verify restoration
			assert len(fs2.files) == len(expected_files)

			# Verify JSON files were restored correctly
			restored_config = fs2.get_file('config.json')
			assert restored_config is not None
			assert isinstance(restored_config, JsonFile)
			assert restored_config.content == updated_config

			restored_api = fs2.get_file('api_response.json')
			assert restored_api is not None
			assert isinstance(restored_api, JsonFile)
			assert restored_api.content == api_response

			# Verify CSV files were restored correctly
			restored_users = fs2.get_file('users.csv')
			assert restored_users is not None
			assert isinstance(restored_users, CsvFile)
			assert restored_users.content == expected_users_content

			restored_products = fs2.get_file('products.csv')
			assert restored_products is not None
			assert isinstance(restored_products, CsvFile)
			assert restored_products.content == products_csv

			# Verify files exist on disk
			for filename in expected_files:
				if filename != 'todo.md':  # Skip todo.md as it's already tested
					assert (fs2.data_dir / filename).exists()

			fs2.nuke()

	async def test_from_state_with_json_csv_files(self, temp_filesystem):
		"""Test restoring filesystem from state with JSON and CSV files."""
		fs = temp_filesystem

		# Add JSON and CSV content
		await fs.write_file('data.json', '{"version": "1.0", "users": [{"name": "John", "age": 30}]}')
		await fs.write_file('users.csv', 'name,age,city\nJohn,30,New York\nJane,25,London')
		await fs.write_file('config.json', '{"debug": true, "port": 8080}')
		await fs.write_file('products.csv', 'id,name,price\n1,Laptop,999.99\n2,Mouse,29.99')

		# Get state
		state = fs.get_state()

		# Create new filesystem from state
		fs2 = FileSystem.from_state(state)

		# Verify restoration
		assert fs2.base_dir == fs.base_dir
		assert len(fs2.files) == len(fs.files)

		# Verify JSON file contents
		json_file = fs2.get_file('data.json')
		assert json_file is not None
		assert isinstance(json_file, JsonFile)
		assert json_file.content == '{"version": "1.0", "users": [{"name": "John", "age": 30}]}'

		config_file = fs2.get_file('config.json')
		assert config_file is not None
		assert isinstance(config_file, JsonFile)
		assert config_file.content == '{"debug": true, "port": 8080}'

		# Verify CSV file contents
		csv_file = fs2.get_file('users.csv')
		assert csv_file is not None
		assert isinstance(csv_file, CsvFile)
		assert csv_file.content == 'name,age,city\nJohn,30,New York\nJane,25,London'

		products_file = fs2.get_file('products.csv')
		assert products_file is not None
		assert isinstance(products_file, CsvFile)
		assert products_file.content == 'id,name,price\n1,Laptop,999.99\n2,Mouse,29.99'

		# Verify files exist on disk
		assert (fs2.data_dir / 'data.json').exists()
		assert (fs2.data_dir / 'users.csv').exists()
		assert (fs2.data_dir / 'config.json').exists()
		assert (fs2.data_dir / 'products.csv').exists()

		# Verify disk contents match
		assert (fs2.data_dir / 'data.json').read_text() == '{"version": "1.0", "users": [{"name": "John", "age": 30}]}'
		assert (fs2.data_dir / 'users.csv').read_text() == 'name,age,city\nJohn,30,New York\nJane,25,London'

		# Clean up second filesystem
		fs2.nuke()

	def test_nuke(self, empty_filesystem):
		"""Test filesystem destruction."""
		fs = empty_filesystem

		# Create a file to ensure directory has content
		fs.data_dir.mkdir(exist_ok=True)
		test_file = fs.data_dir / 'test.txt'
		test_file.write_text('test')
		assert test_file.exists()

		# Nuke the filesystem
		fs.nuke()

		# Verify directory is removed
		assert not fs.data_dir.exists()

	def test_get_dir(self, temp_filesystem):
		"""Test getting the filesystem directory."""
		fs = temp_filesystem

		directory = fs.get_dir()
		assert directory == fs.data_dir
		assert directory.exists()
		assert directory.name == DEFAULT_FILE_SYSTEM_PATH


class TestFileSystemEdgeCases:
	"""Test edge cases and error handling."""

	def test_filesystem_with_string_path(self):
		"""Test FileSystem creation with string path."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			fs = FileSystem(base_dir=tmp_dir, create_default_files=False)
			assert isinstance(fs.base_dir, Path)
			assert fs.base_dir.exists()
			fs.nuke()

	def test_filesystem_with_path_object(self):
		"""Test FileSystem creation with Path object."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			path_obj = Path(tmp_dir)
			fs = FileSystem(base_dir=path_obj, create_default_files=False)
			assert isinstance(fs.base_dir, Path)
			assert fs.base_dir == path_obj
			fs.nuke()

	def test_filesystem_recreates_data_dir(self):
		"""Test that FileSystem recreates data directory if it exists."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			# Create filesystem
			fs1 = FileSystem(base_dir=tmp_dir, create_default_files=True)
			data_dir = fs1.data_dir

			# Add a custom file
			custom_file = data_dir / 'custom.txt'
			custom_file.write_text('custom content')
			assert custom_file.exists()

			# Create another filesystem with same base_dir (should clean data_dir)
			fs2 = FileSystem(base_dir=tmp_dir, create_default_files=True)

			# Custom file should be gone, default files should exist
			assert not custom_file.exists()
			assert (fs2.data_dir / 'todo.md').exists()

			fs2.nuke()

	async def test_write_file_exception_handling(self):
		"""Test exception handling in write_file."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			fs = FileSystem(base_dir=tmp_dir, create_default_files=False)

			# Test with invalid extension
			result = await fs.write_file('test.invalid', 'content')
			assert result == INVALID_FILENAME_ERROR_MESSAGE

			fs.nuke()

	def test_from_state_with_unknown_file_type(self):
		"""Test restoring state with unknown file types (should skip them)."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			# Create a state with unknown file type
			state = FileSystemState(
				files={
					'test.md': {'type': 'MarkdownFile', 'data': {'name': 'test', 'content': 'test content'}},
					'unknown.txt': {'type': 'UnknownFileType', 'data': {'name': 'unknown', 'content': 'unknown content'}},
				},
				base_dir=tmp_dir,
				extracted_content_count=0,
			)

			# Restore from state
			fs = FileSystem.from_state(state)

			# Should only have the known file type
			assert 'test.md' in fs.files
			assert 'unknown.txt' not in fs.files
			assert len(fs.files) == 1

			fs.nuke()


class TestFileSystemIntegration:
	"""Integration tests for FileSystem with real file operations."""

	async def test_complete_workflow(self):
		"""Test a complete filesystem workflow."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			# Create filesystem
			fs = FileSystem(base_dir=tmp_dir, create_default_files=True)

			# Write to results file
			await fs.write_file('results.md', '# Test Results\n## Section 1\nInitial results.')

			# Append more content
			await fs.append_file('results.md', '\n## Section 2\nAdditional findings.')

			# Create a notes file
			await fs.write_file('notes.txt', 'Important notes:\n- Note 1\n- Note 2')

			# Save extracted content
			await fs.save_extracted_content('Extracted data from web page')
			await fs.save_extracted_content('Second extraction')

			# Verify file listing
			files = fs.list_files()
			assert len(files) == 5  # results.md, todo.md, notes.txt, 2 extracted files

			# Verify content
			file_obj = fs.get_file('results.md')
			assert file_obj is not None
			results_content = file_obj.content
			assert '# Test Results' in results_content
			assert '## Section 1' in results_content
			assert '## Section 2' in results_content
			assert 'Additional findings.' in results_content

			# Test state persistence
			state = fs.get_state()
			fs.nuke()

			# Restore from state
			fs2 = FileSystem.from_state(state)

			# Verify restoration
			assert len(fs2.files) == 5
			file_obj = fs2.get_file('results.md')
			assert file_obj is not None
			assert file_obj.content == results_content
			file_obj = fs2.get_file('notes.txt')
			assert file_obj is not None
			assert file_obj.content == 'Important notes:\n- Note 1\n- Note 2'
			assert fs2.extracted_content_count == 2

			# Verify files exist on disk
			for filename in files:
				assert (fs2.data_dir / filename).exists()

			fs2.nuke()

	async def test_concurrent_operations(self):
		"""Test concurrent file operations."""
		with tempfile.TemporaryDirectory() as tmp_dir:
			fs = FileSystem(base_dir=tmp_dir, create_default_files=False)

			# Create multiple files concurrently
			tasks = []
			for i in range(5):
				tasks.append(fs.write_file(f'file_{i}.md', f'Content for file {i}'))

			# Wait for all operations to complete
			results = await asyncio.gather(*tasks)

			# Verify all operations succeeded
			for result in results:
				assert 'successfully' in result

			# Verify all files were created
			assert len(fs.files) == 5
			for i in range(5):
				assert f'file_{i}.md' in fs.files
				file_obj = fs.get_file(f'file_{i}.md')
				assert file_obj is not None
				assert file_obj.content == f'Content for file {i}'

			fs.nuke()
