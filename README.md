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

## License

See the main gpt-oss repository for license information.
