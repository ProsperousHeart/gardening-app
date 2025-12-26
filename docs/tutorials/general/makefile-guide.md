# Makefile Guide

This project uses a Makefile to standardize common development tasks. All commands are executed using `uv run` to ensure they run within the correct virtual environment with proper dependencies.

## Why Use Make?

- **Consistency**: Everyone on the team uses the same commands
- **Simplicity**: Easy-to-remember shortcuts for complex commands
- **CI/CD Integration**: Same commands work locally and in CI/CD pipelines
- **Documentation**: Self-documenting via `make help`

## Available Commands

### Getting Help

```bash
make help
```

Shows all available commands with descriptions.

### Installing Dependencies

```bash
make install
```

Installs all production and development dependencies using `uv sync --all-groups`.

**Equivalent to:**
```bash
uv sync --all-groups
```

### Linting Code

```bash
make lint
```

Runs flake8 linter on `src/` and `test/` directories to check for code quality issues.

**Equivalent to:**
```bash
uv run flake8 src/ test/
```

**What it checks:**
- PEP 8 style violations
- Syntax errors
- Unused imports
- Undefined variables
- Code complexity warnings

### Formatting Code

```bash
# Format code (modifies files)
make format

# Check formatting without modifying files
make format-check
```

Uses Black to format Python code with consistent style.

**Equivalent to:**
```bash
uv run black src/ test/              # Format
uv run black --check src/ test/      # Check only
```

**CI/CD uses `format-check`** to ensure code is properly formatted before merging.

### Running Tests

```bash
# Run all tests
make test

# Run tests with coverage report
make test-coverage
```

Executes pytest test suite and optionally generates coverage reports.

**Equivalent to:**
```bash
uv run pytest test/                           # Run tests
uv run coverage run -m pytest test/           # With coverage
uv run coverage report                        # Show coverage
uv run coverage html                          # Generate HTML report
```

**Coverage reports:**
- Terminal: `coverage report` shows percentages
- HTML: `htmlcov/index.html` provides detailed line-by-line coverage

### Cleaning Up

```bash
make clean
```

Removes Python cache files, test artifacts, and coverage reports.

**Cleans:**
- `__pycache__/` directories
- `.pytest_cache/` directories
- `.mypy_cache/` directories
- `*.pyc` files
- `htmlcov/` and `.coverage` files

## CI/CD Integration

Our GitHub Actions workflow (`.github/workflows/ci.yml`) uses the same Makefile commands:

```yaml
- name: Install dependencies
  run: uv sync --all-groups

- name: Lint
  run: make lint

- name: Format Check
  run: make format-check

- name: Test
  run: make test
```

This ensures **identical behavior** between local development and CI/CD pipelines.

## Why `uv run`?

All commands in the Makefile use `uv run <command>` instead of running commands directly. This ensures:

1. **Correct Environment**: Commands run in the virtual environment managed by uv
2. **Proper Dependencies**: All required packages are available
3. **Version Consistency**: Uses exact versions from `uv.lock`
4. **No Activation Required**: Don't need to manually activate virtual environment

### Example

```bash
# Without uv run (requires manual activation)
source .venv/bin/activate
flake8 src/ test/
deactivate

# With uv run (automatic)
uv run flake8 src/ test/
```

## Common Workflows

### Before Committing Code

```bash
make format        # Format code
make lint          # Check for issues
make test          # Run tests
```

### Continuous Development

```bash
# Watch for changes and auto-run tests
uv run pytest test/ --watch
```

### Pull Request Review

```bash
make install       # Ensure dependencies are current
make format-check  # Verify formatting
make lint          # Check code quality
make test-coverage # Run tests with coverage
```

## Customizing the Makefile

The Makefile is located at the project root (`Makefile`). You can add custom targets:

```makefile
.PHONY: my-custom-task

my-custom-task:
	uv run python scripts/my-script.py
```

**Best practices:**
1. Always use `uv run` for Python commands
2. Add `.PHONY:` declaration for non-file targets
3. Update `help` target with new command descriptions
4. Keep commands simple and focused

## Troubleshooting

### "make: command not found"

Install Make:

```bash
# Windows (via Chocolatey)
choco install make

# macOS
brew install make

# Linux (usually pre-installed)
sudo apt-get install make    # Debian/Ubuntu
sudo yum install make         # RHEL/CentOS
```

### "uv: command not found"

Install uv:

```bash
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then run `make install` to set up dependencies.

### "No module named 'pytest'" (or similar)

Dependencies not installed. Run:

```bash
make install
```

### Commands fail on Windows

If using Git Bash or WSL, ensure paths use forward slashes. The Makefile uses Unix-style commands which work in Git Bash but may fail in CMD/PowerShell.

**Solutions:**
- Use Git Bash (recommended for Windows)
- Use WSL (Windows Subsystem for Linux)
- Install Unix tools via Chocolatey: `choco install gnuwin32-coreutils.install`

## Related Documentation

- [Dependency Management](dependency-management.md) - Managing Python dependencies with uv
- [CI/CD Workflow](../../.github/workflows/ci.yml) - GitHub Actions configuration
- [pyproject.toml](../../pyproject.toml) - Project dependencies and configuration

## Additional Resources

- [GNU Make Manual](https://www.gnu.org/software/make/manual/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [flake8 Documentation](https://flake8.pycqa.org/)
- [Black Documentation](https://black.readthedocs.io/)
- [pytest Documentation](https://docs.pytest.org/)
