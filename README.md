# MCP Python Server

An MCP (Model Context Protocol) server that provides secure Python code execution in Docker containers. This tool allows language models to execute Python code for internal reasoning and computation.

## Features

- **Sandboxed execution**: Runs Python code in isolated Docker containers
- **Stateless execution**: Each execution is independent
- **Standard output capture**: Returns stdout from executed code
- **Internal reasoning**: Designed for LLM internal computation, not user-visible code

## Installation

```bash
cd mcp-python
uv pip install -e .
```

## Requirements

- **Docker**: Must have Docker installed and running
- The server uses the `gpt-oss` PythonTool which manages Docker containers

## Usage

### Running the Server

```bash
python python_server.py
```

The server will start on port **8002**.

### API

#### `python`

Execute Python code in a stateless Docker container.

**Parameters:**
- `code` (string, required): Python code to execute

**Returns:** Standard output from the executed code

**Example:**
```python
# Calculate factorial
result = await python(code="""
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
""")
# Returns: "120"
```

## Use Cases

- Mathematical computations and symbolic math
- Data analysis and statistical calculations
- Algorithm testing and verification
- Internal reasoning that requires computation
- Prototype code execution before showing to users

## Important Notes

- Code execution is **stateless** - variables don't persist between calls
- This tool is for **internal reasoning** only, not for displaying code to users
- Executed code **does not appear** in the user-facing conversation
- Each execution runs in a fresh Docker container

## Dependencies

- mcp
- fastapi>=0.116.1
- uvicorn>=0.35.0
- gpt-oss (for PythonTool implementation)
- docker (system requirement)

## Architecture

The Python server depends on the main `gpt-oss` package for the `PythonTool` implementation, which provides Docker container management and secure code execution.

## Security

Code runs in isolated Docker containers with:
- No network access
- Limited resource usage
- Temporary container lifecycle
- Sandboxed filesystem

## Testing

### Setup

1. Install test dependencies:
```bash
uv pip install -e ".[test]"
```

2. Ensure Docker is installed and running:
```bash
docker --version
docker ps
```

### Running Tests

Run all tests:
```bash
pytest
```

Run with verbose output:
```bash
pytest -v
```

Run specific test file:
```bash
pytest tests/test_python_server.py
```

Run specific test:
```bash
pytest tests/test_python_server.py::test_basic_print -v
```

### Test Coverage

The test suite covers:
- **Basic operations**: Print statements, arithmetic, string manipulation
- **Data structures**: Lists, dictionaries, operations on collections
- **Standard library**: Imports of common modules (math, json, datetime)
- **Functions**: Function definition and recursion
- **Error handling**: Exception capture and syntax errors
- **Output handling**: Single and multiline output
- **Package availability**: Testing for optional packages (e.g., numpy)

**Note**: Tests execute real Python code in Docker containers. Ensure Docker is running before testing. Test execution may be slower due to container startup overhead.

## License

See the main gpt-oss repository for license information.
