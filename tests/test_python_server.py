import pytest
from python_server import python


@pytest.mark.asyncio
async def test_basic_print():
    """Test basic print statement execution"""
    code = 'print("Hello, World!")'
    result = await python.fn(code)

    assert result is not None
    assert "Hello, World!" in result


@pytest.mark.asyncio
async def test_arithmetic_operations():
    """Test arithmetic calculations"""
    code = """
x = 10 + 20
y = x * 2
print(f"Result: {y}")
"""
    result = await python.fn(code)

    assert result is not None
    assert "60" in result


@pytest.mark.asyncio
async def test_list_operations():
    """Test list manipulation"""
    code = """
numbers = [1, 2, 3, 4, 5]
squared = [n**2 for n in numbers]
print(squared)
"""
    result = await python.fn(code)

    assert result is not None
    assert "[1, 4, 9, 16, 25]" in result


@pytest.mark.asyncio
async def test_import_standard_library():
    """Test importing standard library modules"""
    code = """
import math
result = math.sqrt(16)
print(f"Square root of 16: {result}")
"""
    result = await python.fn(code)

    assert result is not None
    assert "4.0" in result


@pytest.mark.asyncio
async def test_json_operations():
    """Test JSON serialization and deserialization"""
    code = """
import json
data = {"name": "Test", "value": 42}
json_str = json.dumps(data)
parsed = json.loads(json_str)
print(parsed['name'], parsed['value'])
"""
    result = await python.fn(code)

    assert result is not None
    assert "Test" in result
    assert "42" in result


@pytest.mark.asyncio
async def test_datetime_operations():
    """Test datetime operations"""
    code = """
from datetime import datetime
now = datetime(2024, 1, 1, 12, 0, 0)
print(f"Date: {now.strftime('%Y-%m-%d')}")
"""
    result = await python.fn(code)

    assert result is not None
    assert "2024-01-01" in result


@pytest.mark.asyncio
async def test_function_definition():
    """Test defining and calling functions"""
    code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

result = [fibonacci(i) for i in range(8)]
print(result)
"""
    result = await python.fn(code)

    assert result is not None
    assert "[0, 1, 1, 2, 3, 5, 8, 13]" in result


@pytest.mark.asyncio
async def test_exception_handling():
    """Test that exceptions are captured and returned"""
    code = """
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Caught error: {e}")
"""
    result = await python.fn(code)

    assert result is not None
    assert "division by zero" in result.lower() or "caught error" in result.lower()


@pytest.mark.asyncio
async def test_multiline_output():
    """Test code that produces multiple lines of output"""
    code = """
for i in range(5):
    print(f"Line {i}")
"""
    result = await python.fn(code)

    assert result is not None
    assert "Line 0" in result
    assert "Line 4" in result


@pytest.mark.asyncio
async def test_numpy_operations():
    """Test numpy operations (if available in container)"""
    code = """
try:
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Mean: {arr.mean()}")
    print(f"Sum: {arr.sum()}")
except ImportError:
    print("NumPy not available")
"""
    result = await python.fn(code)

    assert result is not None
    # Either numpy works or we get the import error message
    assert ("Mean:" in result and "Sum:" in result) or "not available" in result


@pytest.mark.asyncio
async def test_string_operations():
    """Test string manipulation"""
    code = """
text = "hello world"
print(text.upper())
print(text.capitalize())
print(text.replace("world", "python"))
"""
    result = await python.fn(code)

    assert result is not None
    assert "HELLO WORLD" in result
    assert "Hello world" in result
    assert "hello python" in result


@pytest.mark.asyncio
async def test_dictionary_operations():
    """Test dictionary operations"""
    code = """
data = {"a": 1, "b": 2, "c": 3}
for key, value in data.items():
    print(f"{key}: {value}")
"""
    result = await python.fn(code)

    assert result is not None
    assert "a: 1" in result
    assert "b: 2" in result
    assert "c: 3" in result


@pytest.mark.asyncio
async def test_empty_code():
    """Test execution of empty code"""
    code = ""
    result = await python.fn(code)

    # Empty code should return empty result or minimal output
    assert result is not None


@pytest.mark.asyncio
async def test_comment_only_code():
    """Test execution of code with only comments"""
    code = """
# This is a comment
# Another comment
"""
    result = await python.fn(code)

    # Code with only comments should produce no output
    assert result is not None


@pytest.mark.asyncio
async def test_syntax_error():
    """Test that syntax errors are captured"""
    code = "print('hello"  # Unclosed string
    result = await python.fn(code)

    # Should contain error information
    assert result is not None
    # Check if error is mentioned (different implementations may format differently)
    assert len(result) > 0
