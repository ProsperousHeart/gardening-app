# Pre-Push Checklist: Preparing Code for Repository

This guide walks you through the essential checks to perform before pushing code to the repository. Following this checklist ensures code quality, security, and consistency.

**Last Updated:** 2025-12-15

---

## Table of Contents

1. [Quick Reference](#quick-reference)
2. [Security Scanning](#security-scanning)
3. [Code Quality](#code-quality)
4. [Testing](#testing)
5. [Documentation](#documentation)
6. [Git Best Practices](#git-best-practices)
7. [Pre-Commit Hooks](#pre-commit-hooks)
8. [Troubleshooting](#troubleshooting)

---

## Quick Reference

**Essential Commands to Run Before Every Push:**

```bash
# 1. Security scan
bandit -x .venv -r .

# 2. Format code
make format

# 3. Lint code
make lint

# 4. Run tests
make test

# 5. Check for secrets
git diff --staged | grep -i -E '(api_key|secret|password|token)='
```

**Django-Specific (if working in `2024-Django-Attempt/`):**

```bash
# Django deployment check
cd 2024-Django-Attempt
python manage.py check --deploy
```

---

## Security Scanning

### 1. Run Bandit Security Scanner

Bandit scans Python code for common security issues.

```bash
# Run bandit from project root, excluding virtual environment
bandit -x .venv -r .
```

**What to Look For:**

- **No HIGH severity issues** - Must be resolved before pushing
- **No MEDIUM severity issues** - Should be resolved or documented
- **LOW severity issues** - Review and address if possible

**Common Findings and Fixes:**

#### B105: Hardcoded Password String

❌ **Bad:**
```python
SECRET_KEY = 'django-insecure-hardcoded-key'
```

✅ **Good:**
```python
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    if DEBUG:
        SECRET_KEY = 'dev-only-key'
    else:
        raise ValueError("DJANGO_SECRET_KEY must be set")
```

#### B608: SQL Injection Risk

❌ **Bad:**
```python
query = f"SELECT * FROM {table_name}"
df = pd.read_sql_query(query, conn)
```

✅ **Good:**
```python
# Validate against schema
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
valid_tables = {row[0] for row in cursor.fetchall()}

if table_name not in valid_tables:
    raise ValueError(f"Invalid table: {table_name}")

# Use identifier quoting
quoted_table = f'"{table_name}"'
df = pd.read_sql_query(f"SELECT * FROM {quoted_table}", conn)
```

#### B201/B301: Pickle Usage

❌ **Bad:**
```python
import pickle
data = pickle.loads(user_input)  # Never unpickle untrusted data!
```

✅ **Good:**
```python
import json
data = json.loads(user_input)  # Use JSON for serialization
```

### 2. Check for Exposed Secrets

Before staging files, scan for accidentally committed secrets:

```bash
# Check unstaged changes
git diff | grep -i -E '(api_key|secret|password|token|aws_access)='

# Check staged changes
git diff --staged | grep -i -E '(api_key|secret|password|token|aws_access)='

# Check for common secret patterns
git diff --staged | grep -E '["\047][A-Za-z0-9]{20,}["\047]'
```

**Common Secrets to Avoid:**

- API keys (weather APIs, Google Maps, etc.)
- Database passwords
- AWS credentials
- Django SECRET_KEY
- OAuth client secrets
- Private encryption keys

**If You Find Secrets:**

1. **Unstage the file:**
   ```bash
   git reset HEAD <file>
   ```

2. **Move secret to environment variable:**
   ```python
   # In code
   API_KEY = os.environ.get('WEATHER_API_KEY')
   ```

3. **Update .env.example:**
   ```bash
   # .env.example
   WEATHER_API_KEY=your-api-key-here
   ```

4. **Ensure .env is in .gitignore:**
   ```bash
   grep -q "^\.env$" .gitignore || echo ".env" >> .gitignore
   ```

### 3. Django Security Check (Django Projects)

Run Django's built-in deployment security checklist:

```bash
cd 2024-Django-Attempt
python manage.py check --deploy
```

**Common Issues:**

- `ALLOWED_HOSTS` not set
- `DEBUG=True` in production
- Missing security headers
- Insecure session cookie settings

---

## Code Quality

### 1. Format Code

Ensure consistent code formatting with Black:

```bash
# Auto-format all Python files
make format

# Or manually:
uv run black .
```

**Expected Output:**
```
All done! ✨ 🍰 ✨
X files reformatted, Y files left unchanged.
```

### 2. Lint Code

Check code quality with flake8:

```bash
# Run linter
make lint

# Or manually:
uv run flake8
```

**Common Linting Issues:**

- **E501**: Line too long (>79 characters) - Break into multiple lines
- **F401**: Imported but unused - Remove unused imports
- **E302**: Expected 2 blank lines - Add blank lines between functions
- **W291**: Trailing whitespace - Remove trailing spaces

**Example Fixes:**

❌ **Bad:**
```python
def very_long_function_with_many_parameters(param1, param2, param3, param4, param5):
    pass
```

✅ **Good:**
```python
def very_long_function_with_many_parameters(
    param1, param2, param3, param4, param5
):
    pass
```

### 3. Type Checking (Optional)

If using type hints, run mypy:

```bash
uv run mypy .
```

---

## Testing

### 1. Run All Tests

```bash
# Run full test suite
make test

# Or manually:
uv run pytest

# With coverage report:
make test-coverage
```

**Required Test Coverage:**

- **Unit tests**: Test individual functions and methods
- **Integration tests**: Test component interactions
- **End-to-end tests**: Test complete user workflows

**Tests MUST pass before pushing!**

### 2. Run Django Tests (Django Projects)

```bash
cd 2024-Django-Attempt
python manage.py test

# Run specific app tests
python manage.py test Plants

# With coverage
uv run coverage run --source='.' manage.py test
uv run coverage report
```

### 3. Verify Test Output

✅ **Good output:**
```
====== 42 passed in 2.34s ======
```

❌ **Bad output (do NOT push):**
```
====== 38 passed, 4 failed in 2.34s ======
```

**If Tests Fail:**

1. Review the failure messages
2. Fix the underlying issues
3. Re-run tests to verify fixes
4. DO NOT use `--no-verify` to skip tests!

---

## Documentation

### 1. Update Documentation

If your changes affect:

- **API endpoints** → Update API documentation
- **User-facing features** → Update user guides
- **Configuration** → Update setup documentation
- **Architecture** → Update architecture diagrams

### 2. Update CHANGELOG

For significant changes, update `CHANGELOG.md`:

```markdown
## [Unreleased]

### Added
- New plant search filtering by multiple characteristics

### Fixed
- SQL injection vulnerability in table name validation

### Changed
- Updated Django SECRET_KEY to use environment variables
```

### 3. Update Docstrings

Ensure all new functions have proper docstrings:

```python
def calculate_planting_date(plant_id: int, location: str) -> datetime:
    """
    Calculate optimal planting date for a plant at a specific location.

    Args:
        plant_id: Database ID of the plant
        location: User's location (city, state or zip code)

    Returns:
        datetime: Recommended planting date

    Raises:
        PlantNotFoundError: If plant_id doesn't exist
        LocationError: If location cannot be geocoded
    """
    pass
```

---

## Git Best Practices

### 1. Review Your Changes

Before committing, review what you're about to push:

```bash
# View all changes
git diff

# View staged changes
git diff --cached

# View changed files
git status
```

### 2. Stage Files Selectively

Don't use `git add .` blindly:

```bash
# Stage specific files
git add path/to/file.py

# Stage interactively (recommended)
git add -p

# Stage all Python files only
git add *.py
```

### 3. Write Good Commit Messages

Follow this format:

```
<type>: <short summary in imperative mood>

<optional detailed description>

<optional footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting (no logic change)
- `refactor`: Code restructuring (no behavior change)
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**

✅ **Good:**
```
fix: resolve SQL injection in plant search query

Added validation to ensure table names are checked against
database schema before constructing queries. Also added
identifier quoting for additional safety.

Fixes bandit issue B608
```

❌ **Bad:**
```
fixed stuff
```

### 4. Commit with Security in Mind

**NEVER use `--no-verify` flag:**

```bash
# ❌ BAD - Bypasses pre-commit hooks
git commit --no-verify -m "quick fix"

# ✅ GOOD - Runs all checks
git commit -m "fix: resolve authentication bug"
```

### 5. Push to Feature Branch

Push to a feature branch, not directly to main:

```bash
# Create feature branch
git checkout -b fix/security-improvements

# Make changes, commit
git add <files>
git commit -m "fix: resolve bandit security findings"

# Push to remote feature branch
git push -u origin fix/security-improvements

# Create pull request on GitHub
```

---

## Pre-Commit Hooks

### What Are Pre-Commit Hooks?

Pre-commit hooks automatically run checks before allowing commits. This project uses pre-commit hooks to ensure code quality.

### Install Pre-Commit Hooks

```bash
# Install pre-commit (if not already installed)
uv add --dev pre-commit

# Install git hook scripts
uv run pre-commit install
```

### Configure Pre-Commit

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.8.0
    hooks:
      - id: black
        language_version: python3.14

  - repo: https://github.com/PyCQA/flake8
    rev: 7.1.1
    hooks:
      - id: flake8
        args: ['--max-line-length=88']

  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.10
    hooks:
      - id: bandit
        args: ['-x', '.venv', '-r', '.']

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: check-yaml
      - id: check-json
      - id: check-added-large-files
      - id: detect-private-key
      - id: trailing-whitespace
      - id: end-of-file-fixer
```

### Run Pre-Commit Manually

```bash
# Run on all files
uv run pre-commit run --all-files

# Run on staged files
uv run pre-commit run
```

---

## Troubleshooting

### Bandit Reports False Positives

If bandit flags safe code, you can suppress specific lines:

```python
# Suppress single line
api_key = get_api_key()  # nosec B106

# Suppress entire function
def safe_function():  # nosec
    pass
```

**Only use `# nosec` if you're absolutely sure the code is safe!**

### Tests Fail in CI but Pass Locally

**Common causes:**

1. **Environment differences** - Missing dependencies in CI
2. **Database state** - CI uses clean database
3. **File paths** - Absolute paths may differ
4. **Time/timezone** - Tests may be timezone-dependent

**Solutions:**

```python
# Use relative paths
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

# Use UTC for tests
from django.utils import timezone
now = timezone.now()  # Timezone-aware

# Use fixtures for consistent test data
@pytest.fixture
def sample_plant():
    return Plant.objects.create(name="Tomato")
```

### Linting Conflicts with Auto-Formatting

Black and flake8 may conflict on line length:

```ini
# In .flake8 or setup.cfg
[flake8]
max-line-length = 88
extend-ignore = E203, W503
```

### Merge Conflicts

If you have merge conflicts:

```bash
# Update your branch with latest main
git fetch origin
git rebase origin/main

# Resolve conflicts in your editor
# Then:
git add <resolved-files>
git rebase --continue
```

---

## Complete Pre-Push Workflow

Here's the complete workflow in one place:

```bash
# 1. Ensure you're on a feature branch
git checkout -b feature/my-feature

# 2. Make your changes
# ... edit files ...

# 3. Run security scan
bandit -x .venv -r .

# 4. Format code
make format

# 5. Lint code
make lint

# 6. Run tests
make test

# 7. Django checks (if applicable)
cd 2024-Django-Attempt && python manage.py check --deploy

# 8. Review changes
git status
git diff

# 9. Check for secrets
git diff | grep -i -E '(api_key|secret|password|token)='

# 10. Stage files
git add <files>

# 11. Commit with good message
git commit -m "feat: add plant search filtering"

# 12. Push to remote branch
git push -u origin feature/my-feature

# 13. Create pull request on GitHub
```

---

## Additional Resources

- [Security Checklist](../../.github/instructions/security-checklist.md)
- [Django Secrets Management](django-secrets-management.md)
- [TDD Workflow](../../.github/instructions/tdd-workflow.instructions.md)
- [Quality Checklists](../../.github/instructions/quality-checklists.md)
- [Makefile Guide](makefile-guide.md)

---

## Summary

**Before EVERY push:**

✅ Security scan passes
✅ Code formatted
✅ Linting passes
✅ All tests pass
✅ No secrets in commits
✅ Documentation updated
✅ Good commit message
✅ Pushed to feature branch

**NEVER:**

❌ Use `git commit --no-verify`
❌ Push directly to main
❌ Commit secrets or API keys
❌ Push failing tests
❌ Skip security scans

Following this checklist ensures high-quality, secure code in the repository!
