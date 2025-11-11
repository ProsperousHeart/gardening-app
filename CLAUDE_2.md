# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Table of Contents

- [Project Overview](#project-overview)
- [Development Workflow](#development-workflow)
- [Development Commands](#development-commands)
  - [Environment Setup](#environment-setup)
  - [Linting and Formatting](#linting-and-formatting)
  - [Testing](#testing)
  - [Pre-commit Hooks](#pre-commit-hooks)
  - [Running the Application](#running-the-application)
- [Slash Commands](#slash-commands)
- [Architecture](#architecture)
  - [Documentation Structure](#documentation-structure)
  - [Logging System](#logging-system)
  - [Testing Pattern](#testing-pattern)
- [CI/CD](#cicd)
- [Important Notes](#important-notes)

## Project Overview

This is a Python project template designed for specification-driven development with AI assistance. The repository demonstrates:

- **Production-ready patterns**: Custom logging with decorators, comprehensive testing
- **Specification-driven workflow**: Requirements → Specifications → Code using Test Driven Development
- **Security-first approach**: Integrated [CodeGuard](https://github.com/project-codeguard) security guidelines
- **AI-assisted development**: Structured workflows for Claude Code and GitHub Copilot
- **Educational framework**: Templates, examples, and best practices for teaching

## Development Workflow

This project follows a structured specification-driven workflow:

1. **Requirements**: Define what to build using `docs/templates/requirements-template.md`
2. **Specifications**: Generate detailed specs from requirements with architecture decisions
3. **Architecture Diagrams**: Create visual diagrams based on specifications (see `.github/instructions/architecture-diagrams.instructions.md`)
4. **Threat Modeling**: Identify security risks based on specifications and architecture (see `.github/instructions/threat-modeling.instructions.md`)
5. **TDD Implementation**: Write tests first, then code (see `.github/instructions/tdd-workflow.instructions.md`)
6. **Quality Review**: Validate against checklists (see `.github/instructions/quality-checklists.md`)

**Note**: Threat modeling comes AFTER specifications because you need to know the system architecture, data flows, and integrations before identifying threats.

See `.github/instructions/master-workflow.md` for complete details.

### Quick Start with Workflow Prompts

Use orchestration prompts to automate multi-step workflows:

- **Requirements → Specification**: Execute `.github/prompts/workflow-requirements-to-spec.prompt.md`

  - Generates spec, architecture diagram, threat model (in correct order), runs quality review
  - Usage: `Execute the workflow-requirements-to-spec prompt for docs/requirements/req-{name}.md`

- **Specification → Code**: Execute `.github/prompts/workflow-spec-to-code.prompt.md`
  - Implements with TDD, runs security review, quality validation
  - Usage: `Execute the workflow-spec-to-code prompt for docs/specifications/spec-{name}.md`

See `docs/history/2025-11-09-workflow-usage-guide.md` for step-by-step examples.

## Development Commands

### Environment Setup

This project uses `uv` for dependency management (faster than pip):

```bash
# Install uv (if not already installed)
# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows:
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Create virtual environment
uv venv

# Activate environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Install dependencies
uv add -r requirements.txt
uv add --dev -r requirements-dev.txt
```

See `.github/instructions/uv-environment-setup.instructions.md` for detailed guidance.

### Linting and Formatting

```bash
# Lint code (checks style and programming errors)
make lint
# Or directly: flake8 src/ test/

# Format code (auto-formats to Black style)
make format
# Or directly: black src/ test/

# Check formatting without modifying files
black --check src/ test/
```

Flake8 configuration in `.flake8`:

- Max line length: 88 (matches Black)
- Excludes: `__pycache__`, `.git`, `.venv`

### Testing

```bash
# Run all tests with detailed output
make test
# Or directly: pytest -v

# Run a specific test file
pytest test/test_tmp.py -s -v

# Run a specific test function
pytest test/test_tmp.py -k test_print_hi -s -v
```

### Pre-commit Hooks

The repository uses pre-commit hooks for Black and flake8. To set up:

```bash
pip install pre-commit
pre-commit install
```

This will automatically run Black and flake8 checks before each commit.

### Running the Application

```bash
python -m src.tmp
```

## Slash Commands

Claude Code provides custom slash commands for common workflows. These are convenience wrappers around tool-agnostic prompts in `.github/prompts/`.

### Available Commands

| Command                                  | Purpose                                                 |
| ---------------------------------------- | ------------------------------------------------------- |
| `/setup-env`                             | Set up UV virtual environment                           |
| `/create-requirement <name>`             | Create new requirement document                         |
| `/make-spec-from-req <req-file> [scope]` | Generate specification from requirement (full workflow) |
| `/implement-spec <spec-file>`            | Implement specification using TDD (full workflow)       |
| `/quality-review`                        | Run comprehensive quality checks                        |

### Primary Workflow Commands

**`/make-spec-from-req [req-file] [scope]`**: Generate a specification from a requirements document

This command creates a detailed technical specification in `docs/specifications/` based on the requirements document, including threat model, architecture diagram, and quality review.

**Example:**

```bash
/make-spec-from-req docs/requirements/req_user-auth.md
/make-spec-from-req docs/requirements/req_user-auth.md high-level-aggregate
```

**Output:**

- `docs/specifications/spec_{name}.md`
- `docs/diagrams/threat-model_{name}.md`
- `docs/diagrams/architecture_{name}.md`
- Updates to cross-reference table and index

**`/implement-spec [spec-file]`**: Implement specification using Test-Driven Development

This command implements the specification using TDD (RED-GREEN-REFACTOR), applies CodeGuard security rules, and runs comprehensive quality checks.

**Example:**

```bash
/implement-spec docs/specifications/spec_user-auth.md
```

**See `.claude/commands/README.md` for detailed usage of all commands.**

### Relationship to Prompts

These slash commands delegate to workflow prompts in `.github/prompts/`:

- Commands provide Claude-specific convenience
- Prompts are tool-agnostic (work with Copilot too)
- Same workflow logic for all tools

**GitHub Copilot users**: See `.github/instructions/copilot-usage.instructions.md` for how to use prompts directly with `@workspace`.

## Architecture

### Documentation Structure

The project uses a comprehensive documentation system organized in `docs/`:

```
docs/
├── INDEX.md                    # Documentation master index
├── SPEC-CROSS-REFERENCE.md     # Tracks requirements→specs→code→tests
├── requirements/               # What to build
├── specifications/             # How to build it
├── diagrams/                   # Architecture diagrams (Mermaid)
├── templates/                  # Templates for docs creation
├── rules/                      # Project standards
│   ├── docstring-standards.md
│   ├── output-format.md
│   └── error-resolution-kb.md
└── history/                    # Decision logs
```

**Workflows:**

- Requirements are created using `docs/templates/requirements-template.md`
- Specifications are generated from requirements using `/make-spec-from-req`
- **All diagrams MUST include three formats**: Text description, ASCII diagram, and Mermaid code (collapsible)
- Cross-references are tracked in `SPEC-CROSS-REFERENCE.md`

**Diagram Format Requirements:**
- Text descriptions for accessibility
- ASCII diagrams for portability (work everywhere)
- Mermaid diagrams for visual rendering
- See `.github/instructions/architecture-diagrams.instructions.md` for format details

**Key Documentation:**

- `.github/instructions/` contains AI assistant workflows and CodeGuard security guidelines
- `docs/` contains project-specific documentation
- All Python code follows Google-style docstrings (see `docs/rules/docstring-standards.md`)

### Logging System

The project uses a custom logger utility (`src/utils/logger.py`) with the following characteristics:

- **RotatingFileHandler**: Logs rotate at 1MB with 5 backup files
- **Dual output**: Both file and console logging with different formats and levels
- **Default file location**: `logs/` directory (auto-created if missing)
- **Log naming**: `YYYY-MM-DD_{file_name}.log`

**Decorators:**

- `@func_wrapper(logger)`: Logs function start/end and handles exceptions
- `@sol_wrapper(logger)`: Logs entire solution/script execution (use once per script)

**Key pattern**: Functions store `__wrapped__` attribute to access undecorated versions, enabling test isolation by redecorating with test-specific loggers.

### Testing Pattern

Tests use `unittest` framework (pytest-compatible) with a critical logging isolation pattern:

```python
# In tests, redecorate functions with test logger to avoid log pollution
test_logger = create_logger(file_name="Test_File_Test", file_mode="w")
decorated_func = func_wrapper(test_logger)(original_func.__wrapped__)
```

This ensures test logs are separate from production logs.

## CI/CD

GitHub Actions workflow (`.github/workflows/ci.yml`) runs on push/PR to main:

1. Lint with flake8
2. Format check with Black
3. Run all tests with pytest

Additional workflows: `codeql.yml`, `security.yml` for security scanning.

## Project Structure

### Code Organization

```
src/
  utils/
    logger.py         # Custom logging utilities and decorators
  tmp.py              # Example script demonstrating logging patterns
test/
  test_tmp.py         # Tests with logger isolation pattern
logs/                 # Auto-generated log files (gitignored)
.github/
  instructions/       # AI workflows and CodeGuard security guidelines
  prompts/           # AI prompt templates
docs/                # Project documentation (see Documentation Structure above)
```

### Key Directories

- **`src/`**: Production source code
- **`test/`**: Test files (mirrors `src/` structure)
- **`logs/`**: Auto-generated rotating log files (gitignored)
- **`docs/`**: Requirements, specifications, diagrams, and project rules
- **`.github/instructions/`**: Workflow instructions for AI assistants and CodeGuard security guidelines
- **`.github/prompts/`**: Prompt templates for orchestrating workflows

## Important Notes

### Code Standards

- **ABOUTME comments**: All code files must start with 2-line ABOUTME comments describing the file's purpose
- **Docstrings**: Follow Google-style docstrings (see `docs/rules/docstring-standards.md`)
- **Python version**: Python 3.14+ (managed via `pyproject.toml`)
- **Dependencies**: Use `uv add` for production packages, `uv add --dev` for development tools

### Testing Requirements

- Tests MUST use the decorator unwrapping pattern (`func.__wrapped__`) to maintain log isolation
- Follow TDD workflow: Red (write failing test) → Green (make it pass) → Refactor
- Test output must be pristine - no unexpected errors or warnings
- must be platform independent so no errors when run on linux or windows

### Security

- CodeGuard security guidelines are integrated in `.github/instructions/codeguard-*.instructions.md`
- Security reviews required for authentication, cryptography, and data handling features
- Never commit with `--no-verify` flag (bypasses pre-commit hooks)

### AI Assistant Workflows

- `.github/instructions/claude-usage.instructions.md` - Claude Code workflows
- `.github/instructions/copilot-usage.instructions.md` - GitHub Copilot workflows
- Use `/make-spec-from-req` to generate specifications from requirements
- Follow master workflow in `.github/instructions/master-workflow.md`