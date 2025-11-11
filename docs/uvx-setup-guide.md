# uvx Setup Guide

This guide explains how to set up and use `uvx` for managing Python virtual environments in this project.

## What is uvx?

`uvx` is a tool from the `uv` project by Astral, designed to run Python tools in isolated environments. It's significantly faster than traditional virtual environment tools and provides better dependency management.

## Prerequisites

- Python 3.8 or higher
- pip (comes with Python)

## Installation

### Installing uv (includes uvx)

#### macOS and Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Alternative: Using pip

```bash
pip install uv
```

After installation, verify that `uvx` is available:

```bash
uvx --version
```

## Using uvx with This Project

### Initializing a New Project with uv

If you're starting a brand new Python project from scratch, `uv` can set up the project structure for you:

```bash
# Create a new project directory with pyproject.toml
uv init my-project

# Create a new project in the current directory
uv init

# Initialize without creating a workspace
uv init --no-workspace

# Initialize with a specific Python version
uv init --python 3.12
```

This creates:
- `pyproject.toml` - Modern Python project configuration
- `README.md` - Basic project documentation
- `.python-version` - Specifies Python version
- Basic project structure

**Note**: This template project uses `requirements.txt` files instead of `pyproject.toml` for compatibility with traditional workflows. New projects may prefer the `pyproject.toml` approach.

### Running Tools with uvx

Instead of creating a traditional virtual environment, you can run Python tools directly with `uvx`:

```bash
# Run pytest
uvx pytest

# Run black formatter
uvx black src/ test/

# Run flake8 linter
uvx flake8 src/ test/
```

### Creating a Virtual Environment with uv

If you need a traditional virtual environment, use `uv venv`:

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### Installing Dependencies

**Important**: `uv add` requires a `pyproject.toml` file. This project currently uses `requirements.txt` files instead.

#### If you have a pyproject.toml file:

```bash
# Add a single package
uv add requests

# Add a development dependency
uv add --dev pytest

# Sync all dependencies from pyproject.toml
uv sync
```

#### For projects using requirements.txt (like this one):

```bash
# Create and activate virtual environment first
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install from requirements files using pip
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Or use uv pip for faster installation
uv pip install -r requirements.txt
uv pip install -r requirements-dev.txt
```

#### Converting to pyproject.toml (optional):

If you want to use `uv add` commands, you'll need to migrate to `pyproject.toml`:

```bash
# Initialize a new pyproject.toml
uv init --no-workspace

# Then manually add your dependencies or convert from requirements.txt
# See: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
```

## Common Development Workflows

### Running Tests

```bash
# With uvx (no virtual environment needed)
uvx pytest -v

# With activated virtual environment
pytest -v

# Run specific test file
uvx pytest test/test_tmp.py -s -v

# Run specific test function
uvx pytest test/test_tmp.py -k test_print_hi -s -v
```

### Code Formatting and Linting

```bash
# Format code with Black
uvx black src/ test/

# Check formatting without changes
uvx black --check src/ test/

# Lint with flake8
uvx flake8 src/ test/

# Run all quality checks
uvx black src/ test/ && uvx flake8 src/ test/ && uvx pytest -v
```

### Using Make Commands with uv

If you prefer the Makefile commands, ensure your virtual environment is activated first:

```bash
# Create and activate environment
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
uv add -r requirements.txt
uv add --dev -r requirements-dev.txt

# Now you can use Make commands
make lint
make format
make test
```

## Advantages of uvx

1. **Speed**: Much faster than pip and traditional virtual environment tools
2. **Isolation**: Each tool runs in its own isolated environment
3. **No Activation Required**: Use `uvx` to run tools without activating a virtual environment
4. **Consistency**: Ensures everyone uses the same tool versions
5. **Simplicity**: Fewer steps to get started with development

## Cleanup

### Removing a Virtual Environment

If you created a virtual environment with `uv venv` and want to remove it:

```bash
# First, deactivate if currently activated
deactivate

# Then remove the .venv directory
# On macOS/Linux:
rm -rf .venv

# On Windows (PowerShell):
Remove-Item -Recurse -Force .venv

# On Windows (Command Prompt):
rmdir /s /q .venv
```

### Clearing uv Cache

To free up disk space or resolve dependency issues:

```bash
# Clear all cached packages and environments
uv cache clean

# View cache location and size
uv cache dir
```

## Troubleshooting

### uvx command not found

Make sure `uv` is properly installed and in your PATH. Try reinstalling:

```bash
pip install --upgrade uv
```

### Tool not found with uvx

If `uvx` can't find a tool, try specifying the package explicitly:

```bash
uvx --from pytest pytest -v
```

### Dependency conflicts

If you encounter dependency conflicts, try removing the cache:

```bash
uv cache clean
```

## Additional Resources

- [uv Documentation](https://github.com/astral-sh/uv)
- [uv Installation Guide](https://github.com/astral-sh/uv#installation)
- [uv GitHub Repository](https://github.com/astral-sh/uv)

## Support

For issues specific to this project's setup, please file an issue in the repository. For uvx/uv issues, refer to the [uv GitHub Issues](https://github.com/astral-sh/uv/issues).
