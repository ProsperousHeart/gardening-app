## Quality Review & Verification

This phase validates code quality, security, and standards compliance before merging or deployment.

### Purpose

Quality review ensures:
- All tests pass with pristine output
- Code meets quality standards
- Security requirements are met
- Documentation is complete
- Code is ready for production

### Quality Review Commands

This project provides **three complementary commands** for comprehensive quality validation:

#### 1. `/quality-review` - Comprehensive Project Review

Runs full quality check across the entire project.

**Usage:**

```bash
/quality-review
```

**What it checks:**

- ✅ All tests pass (`pytest`)
- ✅ Coverage ≥ 90% (`pytest --cov`)
- ✅ Ruff linting passes (`ruff check`)
- ✅ Ruff formatting applied (`ruff format`)
- ✅ Docstrings follow standards
- ✅ No hardcoded credentials
- ✅ CodeGuard compliance
- ✅ Documentation updated

**Output:**

- Quality report in terminal
- Coverage report: `htmlcov/index.html`
- List of issues and recommendations

#### 2. `/verify <module-path>` - Module Verification

Runs comprehensive verification of specific module or file.

**Usage:**

```bash
/verify src/plants/search.py
/verify src/api/
```

**What it checks:**

1. **Import Validation**: All dependencies declared in `pyproject.toml`
2. **Type Checking**: If mypy/pyright configured
3. **Test Structure**: Tests exist, follow AAA pattern
4. **Test Quality**: Meaningful assertions, good coverage
5. **Test Execution**: All tests pass
6. **Code Quality**: Ruff linting and formatting
7. **Documentation**: Docstrings, type hints present
8. **Security**: No secrets, CodeGuard compliance
9. **Platform Independence**: Path handling, test isolation
10. **Integration**: Imports work, no breaking changes

**Output:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VERIFICATION REPORT: src/plants/search.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Import Validation: PASS
✅ Test Structure: PASS (10 tests found)
✅ Test Execution: PASS (all passing)
✅ Code Coverage: PASS (94% coverage)
✅ Code Quality: PASS (ruff)
✅ Documentation: PASS (all functions documented)
✅ Security: PASS (no issues)
✅ Platform Independence: PASS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OVERALL VERDICT: ✅ PASS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ready for review and merge.
```

If issues found:

```
❌ Security: FAIL
  Line 45: Hardcoded API key detected
  Line 82: SQL query not parameterized

OVERALL VERDICT: ❌ FAIL - Address issues before proceeding
```

#### 3. `/security-review <module-path>` - Security Focus

Conducts deep security review of implementation.

**Usage:**

```bash
/security-review src/plants/search.py
/security-review src/api/
```

**What it checks:**

1. **Security Context**: Reviews spec and threat model
2. **CodeGuard Rules**: Validates compliance with applicable rules
3. **OWASP Top 10**: Checks for common vulnerabilities
    - Injection (SQL, Command, XSS)
    - Broken Authentication
    - Sensitive Data Exposure
    - XML External Entities (XXE)
    - Broken Access Control
    - Security Misconfiguration
    - Cross-Site Scripting (XSS)
    - Insecure Deserialization
    - Using Components with Known Vulnerabilities
    - Insufficient Logging & Monitoring
4. **Security Test Coverage**: Validates security tests exist
5. **Hardcoded Secrets**: Scans for credentials, keys, tokens

**Output:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECURITY REVIEW: src/plants/search.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 CRITICAL ISSUES (Must Fix):
  None

🟡 WARNINGS (Should Address):
  Line 67: Consider rate limiting for search endpoint
  Line 103: Add input length validation

🔵 RECOMMENDATIONS (Best Practices):
  Add security headers to API responses
  Consider implementing request logging

CodeGuard Compliance:
  ✅ input-validation/sql-injection-prevention.md
  ✅ api-security/rate-limiting.md (WARNING: not fully implemented)
  ✅ authentication/session-management.md

Security Test Coverage: 87% (8 of 9 threats tested)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OVERALL VERDICT: ⚠️ NEEDS FIXES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Address warnings before deployment.
```

### Automated Quality Checks

#### Pytest (Test Execution)

```bash
# Run all tests
make test

# Run with verbose output
make test-v

# Run specific test file
pytest test/plants/test_search.py -v

# Run specific test function
pytest test/plants/test_search.py::test_search_by_zone -v
```

**Requirements:**

- All tests must pass
- Output must be pristine (no warnings, no print statements)
- Tests must be platform-independent

#### Coverage (Test Coverage)

```bash
# Run tests with coverage
make test-coverage

# Open coverage report
# Windows
start htmlcov/index.html

# macOS
open htmlcov/index.html

# Linux
xdg-open htmlcov/index.html
```

**Requirements:**

- Coverage ≥ 90% for all modules
- All branches covered where possible
- No untested code paths

#### Ruff (Linting & Formatting)

```bash
# Check code quality
make lint

# Auto-format code
make format

# Check formatting without changes
make format-check
```

**Configuration:**

- `.flake8` - Linting rules
- `pyproject.toml` - Ruff and Black configuration
- Max line length: 88 characters (Black default)

**Requirements:**

- No linting errors
- Code formatted with Black/Ruff
- Consistent style throughout

### Quality Gates

Before code can be merged:

#### Automated Gates (Must Pass)

- ✅ All tests pass (`pytest`)
- ✅ Coverage ≥ 90% (`pytest --cov`)
- ✅ Ruff linting passes (`ruff check`)
- ✅ Formatting applied (`ruff format`)
- ✅ Pre-commit hooks pass

#### Documentation Gates (Must Complete)

- ✅ Docstrings follow standards
- ✅ SPEC-CROSS-REFERENCE.md updated
- ✅ INDEX.md updated
- ✅ README files updated (if applicable)

#### Security Gates (Must Validate)

- ✅ No hardcoded credentials
- ✅ CodeGuard rules applied
- ✅ Security tests pass
- ✅ Threat mitigations implemented

#### Human Review Gates (Must Approve)

- ✅ Code review by peer or senior developer
- ✅ Specification requirements met
- ✅ Security review approved (for security-sensitive features)

### Pre-Commit Hooks

This project uses git pre-commit hooks to enforce quality standards automatically.

**What runs on `git commit`:**

1. Ruff linting
2. Ruff formatting
3. Test execution
4. Coverage check

**CRITICAL**: ❌ **NEVER use `--no-verify` flag**

```bash
# ❌ WRONG - Bypasses quality checks
git commit --no-verify -m "Quick fix"

# ✅ CORRECT - Runs quality checks
git commit -m "Add plant search feature"
```

The `--no-verify` flag bypasses pre-commit hooks and can introduce broken or non-compliant code.

### Post-Test Review

After implementation and automated checks, conduct manual review:

#### Code Quality Review

- [ ] Code is readable and maintainable
- [ ] Functions are appropriately sized
- [ ] Naming is clear and consistent
- [ ] Comments explain "why", not "what"
- [ ] No code duplication
- [ ] Proper error handling

#### Specification Compliance

- [ ] All requirements implemented
- [ ] Acceptance criteria met
- [ ] Edge cases handled
- [ ] Integration points working

#### Security Review

- [ ] All threats from threat model addressed
- [ ] Security tests cover all threats
- [ ] CodeGuard patterns applied
- [ ] No security shortcuts taken

#### Documentation Review

- [ ] Docstrings accurate and complete
- [ ] README files updated
- [ ] API documentation generated
- [ ] Examples provided

### Integration with Workflow

Quality review is **automatically included** in the `/implement-spec` workflow:

```bash
/implement-spec docs/specifications/spec_genuser_plant-search.md
```

This includes:
1. TDD implementation
2. **Security review** ← Automatic
3. **Quality validation** ← Automatic
4. **Implementation verification** ← Optional
5. **Post-test review** ← Automatic
6. Documentation updates

You can also run quality checks independently:

```bash
/quality-review
/verify src/plants/search.py
/security-review src/plants/search.py
```

### Error Resolution

When quality checks fail, reference the **Error Resolution Knowledge Base**:

**Location:** `docs/rules/error-resolution-kb.md`

**Contains:**

- Common errors and solutions
- Platform-specific fixes
- Dependency conflicts
- Test failures and debugging

Add new errors to the KB as you encounter them.

### Delegates To

- **Quality Review Command**: `.claude/commands/quality-review.md`
- **Verify Prompt**: `.github/prompts/verify-implementation.prompt.md`
- **Security Review Prompt**: `.github/prompts/security-review.prompt.md`
- **Quality Checklist**: `.github/instructions/quality-checklists.md`
- **Post-Test Review**: `.github/instructions/post-test-review.instructions.md`
- **Security Review Instructions**: `.github/instructions/security-review.instructions.md`

### Related Documentation

- **Quality Checklists**: `.github/instructions/quality-checklists.md` (all stages)
- **Post-Test Review**: `.github/instructions/post-test-review.instructions.md`
- **Security Review**: `.github/instructions/security-review.instructions.md`
- **Error Resolution**: `docs/rules/error-resolution-kb.md`
- **Master Workflow**: `.github/instructions/master-workflow.md` (Stage 6)

### Next Steps After Quality Review

1. **All Checks Pass**: Proceed to human approval and merge
2. **Issues Found**: Address issues and re-run quality review
3. **Critical Security Issues**: Loop back to implementation (**Phase 5**)
4. **Documentation Issues**: Update documentation and re-verify
