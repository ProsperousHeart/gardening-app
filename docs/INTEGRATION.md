# Integration Guide: Adding to Existing Projects

This guide explains how to integrate the Python Development Toolkit into your existing project with minimal disruption.

## Table of Contents

- [Quick Start](#quick-start)
- [Installation Methods](#installation-methods)
- [Component Breakdown](#component-breakdown)
- [Post-Installation Steps](#post-installation-steps)
- [Manual Integration](#manual-integration)
- [Troubleshooting](#troubleshooting)

## Quick Start

### For Existing Projects

```bash
# 1. Download the toolkit
git clone https://github.com/yourusername/repo-template-python /tmp/python-toolkit

# 2. Run the installer in your project directory
cd /path/to/your/project
python /tmp/python-toolkit/install.py

# 3. Follow the interactive prompts to select components

# 4. Clean up
rm -rf /tmp/python-toolkit
```

The installer will:
- ✅ Detect existing files before overwriting
- ✅ Prompt for confirmation on conflicts
- ✅ Merge compatible files (dependencies, .gitignore)
- ✅ Install only what you need

## Installation Methods

### Method 1: Interactive Installation (Recommended)

**Best for:** First-time users, selective adoption

```bash
python install.py
```

You'll be prompted to:
1. Select components (by number or "all")
2. Review conflicts
3. Confirm installation
4. Handle overwrites individually

**Example session:**
```
Available components:

1. AI Workflow System
   Claude/Copilot instructions, prompts, and slash commands

2. Documentation Structure
   Requirements, specifications, templates, and rules

...

Select components to install: 1,2,4

Will install:
  - AI Workflow System
  - Documentation Structure
  - Code Quality Tools

⚠️  Code Quality Tools has conflicts:
   - .gitignore

Proceed with installation? [y/N]: y
```

### Method 2: Non-Interactive Installation

**Best for:** Automation, CI/CD, specific component needs

```bash
# Install specific components
python install.py --component ai-workflows --component docs

# Install with auto-overwrite (use with caution!)
python install.py --component quality-tools --force

# Install to different directory
python install.py --target /path/to/project --component ci-cd
```

### Method 3: Manual Selective Copy

**Best for:** Maximum control, cherry-picking specific files

See [Manual Integration](#manual-integration) section below.

## Component Breakdown

### 1. AI Workflow System

**What it adds:**
```
.github/instructions/     # Workflow guides for Claude/Copilot
.github/prompts/          # Reusable prompt templates
.claude/commands/         # Custom slash commands
.claude/CLAUDE.md         # Project-specific AI instructions
```

**Impact:** Zero - These are pure documentation files
**Dependencies:** None
**Use if:** You use Claude Code or GitHub Copilot

**Customization needed:**
- Update `.claude/CLAUDE.md` with your project details
- Review slash commands, remove unused ones
- Customize prompts for your workflow

### 2. Documentation Structure

**What it adds:**
```
docs/templates/           # Requirements, specification templates
docs/rules/              # Docstring standards, output formats
docs/INDEX.md            # Documentation master index
docs/SPEC-CROSS-REFERENCE.md  # Requirements → specs → code tracking
```

**Impact:** Zero - Pure documentation
**Dependencies:** None
**Use if:** You want structured specification-driven development

**Customization needed:**
- Remove example templates if not needed
- Add your existing docs to INDEX.md
- Customize templates for your domain

### 3. CI/CD Workflows

**What it adds:**
```
.github/workflows/ci.yml        # Linting, testing, build
.github/workflows/codeql.yml    # Security scanning
.github/workflows/security.yml  # Dependency scanning
```

**Impact:** Runs on push/PR to main branch
**Dependencies:** `quality-tools` (requires flake8, black, pytest)
**Use if:** You use GitHub and want automated testing

**Customization needed:**
- Update Python version in workflows
- Modify test commands for your project
- Adjust trigger branches

### 4. Code Quality Tools

**What it adds:**
```
.flake8                   # Linting configuration
.pre-commit-config.yaml   # Git hooks for black + flake8
```

**Merges:**
- `.gitignore` (adds logs/, .pytest_cache/, etc.)

**Impact:** Medium - Adds pre-commit hooks
**Dependencies:** None
**Use if:** You want automated code formatting and linting

**Post-install:**
```bash
pip install pre-commit black flake8
pre-commit install
```

**Customization needed:**
- Adjust `.flake8` max line length
- Modify `.pre-commit-config.yaml` hooks
- May need to format existing code: `black .`

### 5. Logging Utilities

**What it adds:**
```
src/utils/logger.py       # Custom logger with decorators
```

**Impact:** Zero until you use it
**Dependencies:** None
**Use if:** You want structured logging with rotation

**Integration:**
```python
from src.utils.logger import create_logger, func_wrapper

logger = create_logger(file_name="my_module")

@func_wrapper(logger)
def my_function():
    logger.info("Function called")
```

**Customization needed:**
- Change log directory in logger.py if desired
- Adjust rotation settings (max bytes, backup count)

### 6. Testing Patterns

**What it adds:**
```
pytest.ini                # Pytest configuration
```

**Merges:**
- `requirements-dev.txt` (adds pytest, pytest-cov)

**Impact:** Zero until you run tests
**Dependencies:** None
**Use if:** You use pytest for testing

**Customization needed:**
- Update `testpaths` in pytest.ini
- Adjust coverage settings

### 7. Development Tools

**What it adds:**
```
Makefile                  # Common dev commands (lint, test, format)
```

**Merges:**
- `pyproject.toml` (adds project metadata template)

**Impact:** Low - Just convenience commands
**Dependencies:** None
**Use if:** You want quick dev commands

**Customization needed:**
- Update Makefile paths for your project structure
- Merge pyproject.toml carefully (has template values)

## Post-Installation Steps

### 1. Update Project-Specific Files

**Required:**
- [ ] Update `CLAUDE.md` and `.claude/CLAUDE.md` with your project details
- [ ] Update `pyproject.toml` (if merged) with correct project name, author, version
- [ ] Review and customize slash commands in `.claude/commands/`

**Optional:**
- [ ] Customize documentation templates in `docs/templates/`
- [ ] Update CI/CD workflows for your Python version and test commands
- [ ] Adjust linting rules in `.flake8`

### 2. Install Dependencies

If you installed quality tools or testing:

```bash
# Using pip
pip install -r requirements-dev.txt

# Using uv (faster)
uv add --dev -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### 3. Handle Existing Code

**If you have existing code:**

```bash
# Format existing code with black
black src/ test/

# Fix linting issues
flake8 src/ test/

# Or auto-fix what's possible
autopep8 --in-place --recursive src/ test/
```

**Note:** You may want to create a commit before formatting:
```bash
git add .
git commit -m "chore: add development toolkit"
git add .
git commit -m "style: format code with black"
```

### 4. Test the Integration

```bash
# Run linting
make lint

# Run tests
make test

# Verify CI/CD (if installed)
git push  # Check GitHub Actions
```

### 5. Update Team Documentation

Add to your README.md or CONTRIBUTING.md:

```markdown
## Development Setup

This project uses the Python Development Toolkit for structured workflows.

See:
- `CLAUDE.md` - Project overview and development commands
- `.github/instructions/` - AI-assisted development workflows
- `docs/templates/` - Templates for requirements and specifications
```

## Manual Integration

If you prefer manual control, here's how to cherry-pick components:

### AI Workflows Only

```bash
# Copy AI instruction files
cp -r .github/instructions/ your-project/.github/
cp -r .github/prompts/ your-project/.github/
cp -r .claude/ your-project/

# Customize
vim your-project/CLAUDE.md
vim your-project/.claude/CLAUDE.md
```

### Documentation Structure Only

```bash
# Copy documentation templates
cp -r docs/templates/ your-project/docs/
cp -r docs/rules/ your-project/docs/
cp docs/INDEX.md your-project/docs/
cp docs/SPEC-CROSS-REFERENCE.md your-project/docs/
```

### Logging Utilities Only

```bash
# Copy logger utility
mkdir -p your-project/src/utils/
cp src/utils/logger.py your-project/src/utils/
```

### Quality Tools Only

```bash
# Copy configuration files
cp .flake8 your-project/
cp .pre-commit-config.yaml your-project/

# Merge .gitignore
cat .gitignore >> your-project/.gitignore

# Install tools
cd your-project
pip install black flake8 pre-commit
pre-commit install
```

## Troubleshooting

### Pre-commit Hook Failures

**Problem:** `pre-commit` fails on first commit after installation

**Solution:**
```bash
# Format all code first
black .

# Or skip hooks for initial formatting commit
git commit -m "style: format code with black" --no-verify

# Then reinstall hooks
pre-commit install
```

### CI/CD Workflow Failures

**Problem:** GitHub Actions fail after installing CI/CD component

**Solution:**
1. Check Python version in `.github/workflows/ci.yml` matches your project
2. Update test commands if you use different testing tools
3. Verify all dependencies are in `requirements.txt` and `requirements-dev.txt`

### Merge Conflicts in pyproject.toml

**Problem:** Installer merged template values into your existing `pyproject.toml`

**Solution:**
```bash
# Review the file
git diff pyproject.toml

# Remove template sections manually
vim pyproject.toml

# Keep your project's values, remove duplicates
```

### Logger Module Import Errors

**Problem:** `ModuleNotFoundError: No module named 'src.utils.logger'`

**Solution:**
1. Ensure your project structure has `src/utils/` directory
2. Add `__init__.py` files:
   ```bash
   touch src/__init__.py
   touch src/utils/__init__.py
   ```
3. Or adjust import path in your code

### Documentation Templates Not Rendering

**Problem:** Slash commands or prompts reference files that don't exist

**Solution:**
1. Create missing directories: `mkdir -p docs/requirements docs/specifications`
2. Review `.claude/commands/` and update file paths
3. Customize prompts in `.github/prompts/` for your project structure

## Gradual Adoption Strategy

You don't need to adopt everything at once! Here's a recommended progression:

### Phase 1: Non-Invasive Components (Week 1)
- ✅ Install AI Workflow System
- ✅ Install Documentation Structure
- ✅ Review and customize for your project

**Impact:** Zero - just documentation

### Phase 2: Development Tools (Week 2)
- ✅ Install Quality Tools
- ✅ Format existing code with `black`
- ✅ Fix linting issues with `flake8`
- ✅ Install pre-commit hooks

**Impact:** Medium - requires code formatting

### Phase 3: Testing & CI/CD (Week 3)
- ✅ Install Testing Patterns
- ✅ Install CI/CD Workflows
- ✅ Verify workflows run successfully

**Impact:** High - runs automatically on commits

### Phase 4: Utilities (Ongoing)
- ✅ Install Logging Utilities
- ✅ Gradually refactor code to use new logger
- ✅ Install Development Tools (Makefile)

**Impact:** Low - use as needed

## Getting Help

- **Installation issues:** Open an issue with the installer output
- **Integration questions:** See project CLAUDE.md for detailed component documentation
- **Customization help:** Review `.github/instructions/` for detailed workflow guides

## Uninstalling Components

To remove a component:

```bash
# Manual removal
rm -rf .github/instructions/  # AI Workflows
rm -rf docs/templates/         # Documentation
rm -f .flake8 .pre-commit-config.yaml  # Quality Tools

# Uninstall pre-commit hooks
pre-commit uninstall
```

There's no automatic uninstaller (yet), but components are independent and can be safely deleted.