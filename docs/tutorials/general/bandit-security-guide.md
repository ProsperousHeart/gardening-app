---
title: Bandit Security Guide
description: Tutorial on using Bandit for Python security scanning.
---

# Bandit Security Guide

This project uses [Bandit](https://bandit.readthedocs.io/) to identify common security issues in Python code. Bandit performs static analysis to find security vulnerabilities before they reach production.

## What is Bandit?

Bandit is a security linter designed to find common security issues in Python code. It analyzes your code for patterns that could lead to security vulnerabilities, such as:

- SQL injection vulnerabilities
- Hardcoded passwords and secrets
- Insecure cryptographic functions
- Shell injection vulnerabilities
- Insecure deserialization
- And many more...

## Quick Start

### Running Bandit

```bash
# Run security scan (recommended)
make security

# Alternative command
make bandit
```

### Manual Usage

```bash
# Scan src/ directory with project configuration
uv run bandit -r src/ -c pyproject.toml

# Scan with severity filter (medium and high only)
uv run bandit -r src/ --severity-level medium

# Generate JSON report
uv run bandit -r src/ -f json -o bandit-report.json

# Scan specific file
uv run bandit src/module/file.py
```

## Configuration

This project has Bandit configured in two places. You can use either one:

### Option 1: pyproject.toml (Active Configuration)

Located in `pyproject.toml:53-60`:

```toml
[tool.bandit]
exclude_dirs = ["2024-Django-Attempt", ".venv", "tests", "migrations", ".git", "docs"]
skips = ["B101"]  # Skip assert_used check (common in tests)
severity = ["medium", "high"]  # Only report medium and high severity
confidence = ["medium", "high"]  # Only report medium and high confidence
```

**To use this configuration:**
```bash
uv run bandit -r src/ -c pyproject.toml
```

### Option 2: .bandit YAML File (Alternative)

Located in `.bandit` at project root. This is an alternative configuration format with more detailed comments.

**To use this configuration:**
```bash
uv run bandit -r src/ --configfile .bandit
```

## Understanding Bandit Output

### Severity Levels

- **HIGH**: Critical security issues that should be fixed immediately
- **MEDIUM**: Potential security issues that warrant review
- **LOW**: Minor issues or potential false positives

### Confidence Levels

- **HIGH**: Very likely to be a real security issue
- **MEDIUM**: Could be a security issue, needs review
- **LOW**: Might be a false positive

### Example Output

```
>> Issue: [B105:hardcoded_password_string] Possible hardcoded password: 'my_secret_key'
   Severity: Low   Confidence: Medium
   Location: src/config/settings.py:15
   More Info: https://bandit.readthedocs.io/en/latest/plugins/b105_hardcoded_password_string.html
14
15	SECRET_KEY = 'my_secret_key'  # SECURITY ISSUE!
16
```

## Common Security Issues Detected

### B105: Hardcoded Passwords

**Bad:**
```python
password = "admin123"  # Never hardcode passwords!
API_KEY = "sk-1234567890"  # Never hardcode API keys!
```

**Good:**
```python
import os
password = os.environ.get("DB_PASSWORD")
API_KEY = os.environ.get("API_KEY")
```

### B201: Flask Debug Mode

**Bad:**
```python
app.run(debug=True)  # Never enable debug in production!
```

**Good:**
```python
import os
debug_mode = os.environ.get("FLASK_DEBUG", "False") == "True"
app.run(debug=debug_mode)
```

### B501: Insecure SSL/TLS

**Bad:**
```python
requests.get(url, verify=False)  # Disables certificate verification!
```

**Good:**
```python
requests.get(url)  # Uses default secure settings
# Or explicitly:
requests.get(url, verify=True)
```

### B506: YAML Load

**Bad:**
```python
import yaml
data = yaml.load(user_input)  # Unsafe! Can execute arbitrary code
```

**Good:**
```python
import yaml
data = yaml.safe_load(user_input)  # Safe alternative
```

### B608: SQL Injection

**Bad:**
```python
query = f"SELECT * FROM users WHERE name = '{user_input}'"
cursor.execute(query)  # SQL injection vulnerability!
```

**Good:**
```python
query = "SELECT * FROM users WHERE name = %s"
cursor.execute(query, (user_input,))  # Parameterized query
```

## Skipping False Positives

Sometimes Bandit flags code that is actually safe. You can skip specific warnings:

### Skip Inline (Use Sparingly)

```python
# nosec B101
assert user.is_authenticated  # This is safe in our context
```

### Skip in Configuration

Add to `pyproject.toml`:

```toml
[tool.bandit]
skips = ["B101", "B601"]  # Skip specific test IDs
```

## Integration with Development Workflow

### Pre-commit Hooks (Optional)

If you enable pre-commit hooks (`.pre-commit-config.yaml`), Bandit will run automatically before each commit:

```bash
# Install pre-commit (if not already installed)
uv add --dev pre-commit

# Install the git hooks
uv run pre-commit install

# Now Bandit runs automatically on git commit
git commit -m "Your message"
```

### CI/CD Pipeline

Bandit runs automatically in GitHub Actions via `.github/workflows/security.yml:34-44` on every push and pull request.

## Best Practices

1. **Run Bandit regularly**: Use `make security` before committing code
2. **Fix HIGH severity issues immediately**: These are critical security problems
3. **Review MEDIUM severity issues**: Many are real problems worth addressing
4. **Don't blindly skip warnings**: Understand why Bandit flagged something before using `# nosec`
5. **Keep Bandit updated**: Run `uv add --dev bandit@latest` periodically
6. **Use environment variables**: Never hardcode secrets, passwords, or API keys
7. **Enable in CI/CD**: Already configured in this project
8. **Document exceptions**: If you must skip a warning, add a comment explaining why

## Makefile Integration

The project Makefile (`Makefile:49-52`) includes Bandit:

```makefile
security: bandit

bandit:
	uv run bandit -r src/ -c pyproject.toml --severity-level medium
```

**Available commands:**
```bash
make security  # Run Bandit security scan
make bandit    # Alias for make security
```

## Common Bandit Test IDs

| ID | Name | Description |
|----|------|-------------|
| B101 | assert_used | Use of assert (disabled for tests) |
| B105 | hardcoded_password_string | Hardcoded password string |
| B106 | hardcoded_password_funcarg | Hardcoded password function argument |
| B107 | hardcoded_password_default | Hardcoded password default |
| B201 | flask_debug_true | Flask app with debug=True |
| B301 | pickle | Use of pickle (unsafe deserialization) |
| B303 | md5 | Use of insecure MD5 hash |
| B304 | ciphers | Use of insecure ciphers |
| B501 | request_with_no_cert_validation | SSL certificate verification disabled |
| B502 | ssl_with_bad_version | SSL/TLS protocol version |
| B506 | yaml_load | Use of yaml.load() |
| B608 | hardcoded_sql_expressions | Possible SQL injection |

Full list: [Bandit Plugins Documentation](https://bandit.readthedocs.io/en/latest/plugins/index.html)

## Troubleshooting

### Issue: "Bandit not found"

**Solution:**
```bash
# Ensure dev dependencies are installed
make install

# Or manually sync
uv sync --all-groups
```

### Issue: Too many false positives

**Solution:**
Adjust severity/confidence levels in `pyproject.toml`:

```toml
[tool.bandit]
severity = ["high"]  # Only show high severity
confidence = ["high"]  # Only show high confidence
```

### Issue: Need to exclude specific directories

**Solution:**
Add to `exclude_dirs` in `pyproject.toml`:

```toml
[tool.bandit]
exclude_dirs = ["2024-Django-Attempt", ".venv", "tests", "your_dir_here"]
```

## Further Reading

- [Official Bandit Documentation](https://bandit.readthedocs.io/)
- [Bandit Plugins Reference](https://bandit.readthedocs.io/en/latest/plugins/index.html)
- [Python Security Best Practices](https://python.readthedocs.io/en/latest/library/security_warnings.html)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CodeGuard Security Framework](https://project-codeguard.org/) (integrated in this project)

## Related Documentation

- [Makefile Guide](makefile-guide.md) - Using make commands
- [Dependency Management](dependency-management.md) - Managing dependencies with uv
- [Django Secrets Management](django-secrets-management.md) - Secure configuration practices
- [CodeGuard Plugin](.claude/CLAUDE.md#security-framework) - AI-assisted security practices
