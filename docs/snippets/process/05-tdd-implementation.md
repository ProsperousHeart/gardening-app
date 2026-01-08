## TDD Implementation with Shift-Left Security

This phase implements features using Test-Driven Development (TDD using RED-GREEN-REFACTOR cycle) with shift-left security integrated from the start.

### Purpose

TDD implementation transforms specifications into working code by:

- Writing tests BEFORE implementation (test-first)
- Following RED-GREEN-REFACTOR cycle
- Integrating security testing from the start (shift-left security)
- Ensuring code meets specifications and security requirements
- Building confidence through comprehensive test coverage

### The `/implement-spec` Workflow

This is a **workflow orchestration command** with built-in **approval gates** to ensure quality implementation.

**Format:**
```bash
/implement-spec <spec-file>
```

**Example:**
```bash
/implement-spec docs/specifications/spec_genuser_plant-search.md
```

### What This Workflow Does (8 Steps)

#### Step 1: Review Specification & Create Test Plan
- Reads specification document
- Reviews threat model and CodeGuard requirements
- Identifies all features to implement
- Creates comprehensive test plan covering:
  - Functional tests (business logic)
  - Security tests (CodeGuard compliance)
  - Edge cases and error handling
  - Integration tests
  - Performance tests (if applicable)

**🚨 APPROVAL GATE**: User must approve test plan before implementation begins.

**Why?** This ensures the implementation approach is correct before writing any code. Catching issues here saves significant rework.

#### Step 2: TDD Implementation (RED-GREEN-REFACTOR)
For each function/method in the specification:

**🔴 RED: Write Failing Tests**
```python
# Write tests FIRST
def test_search_plants_by_zone():
    # Arrange
    search_params = {"zone": "7a"}

    # Act
    results = search_plants(search_params)

    # Assert
    assert all(plant.zone == "7a" for plant in results)
```

**Includes security tests:**
```python
def test_search_prevents_sql_injection():
    # Arrange
    malicious_input = "7a' OR '1'='1"

    # Act
    results = search_plants({"zone": malicious_input})

    # Assert
    assert results == []  # No results, not all results
```

Run tests: `pytest -v` → **Tests MUST FAIL** (code doesn't exist yet)

**🟢 GREEN: Write Minimal Code to Pass**
```python
def search_plants(params):
    # Implement minimal code to pass ALL tests
    # Apply CodeGuard secure coding patterns
    # Use parameterized queries, input validation, etc.
    zone = validate_zone(params.get("zone"))
    return Plant.objects.filter(zone=zone)
```

Run tests: `pytest -v` → **Tests MUST PASS**

**🔵 REFACTOR: Improve Code Quality**
```python
def search_plants(params):
    # Clean up, extract functions, improve readability
    # Keep security measures in place
    zone = validate_zone(params.get("zone"))
    queryset = Plant.objects.filter(zone=zone)
    return optimize_query(queryset)
```

Run tests: `pytest -v` → **Tests MUST STILL PASS**

Repeat for next function...

#### Step 3: Security Review
- Runs comprehensive security check using CodeGuard rules
- Validates security tests exist for each threat identified
- Checks for common vulnerabilities (OWASP Top 10)
- Ensures CodeGuard compliance
- Reviews for hardcoded secrets, insecure patterns

See **Phase 6: Quality Review** for details.

#### Step 4: Quality Validation
Runs automated quality checks:
- **Pytest**: All tests must pass (pristine output)
- **Coverage**: ≥90% code coverage required
- **Ruff**: Linting and formatting checks
- **Docstrings**: Standards compliance
- **Type Hints**: Proper type annotations

#### Step 5: Implementation Verification (Optional but Recommended)
Runs `/verify` command for comprehensive validation:
- Import validation
- Test structure quality
- Code quality standards
- Security compliance
- Platform independence
- Documentation completeness

#### Step 6: Post-Test Review
Reviews implementation for:
- Specification compliance
- Security requirements met
- Code quality standards
- Documentation accuracy
- Integration concerns

#### Step 7: Documentation Updates
- Updates `docs/SPEC-CROSS-REFERENCE.md` (status: ✅ Complete)
- Links code files to specification
- Links test files to code
- Updates `docs/INDEX.md`

#### Step 8: Execution Logging
- Saves log to `docs/output-logs/{timestamp}-code-workflow.md`
- Documents decisions made
- Records any issues encountered
- Provides summary report

### The RED-GREEN-REFACTOR Cycle

```
┌─────────────────────────────────────────────────┐
│  For Each Function in Specification             │
└──────────────────┬──────────────────────────────┘
                   │
                   ↓
         ┌─────────────────┐
         │  🔴 RED Phase   │
         │  Write Test     │
         │  (It MUST Fail) │
         └────────┬────────┘
                  │
                  ↓
         ┌─────────────────┐
         │ 🟢 GREEN Phase  │
         │ Write Code      │
         │ (Test MUST Pass)│
         └────────┬────────┘
                  │
                  ↓
         ┌─────────────────┐
         │ 🔵 REFACTOR     │
         │ Improve Code    │
         │ (Keep Tests     │
         │  Passing)       │
         └────────┬────────┘
                  │
                  ↓
         ┌─────────────────┐
         │ More Functions? │
         └────────┬────────┘
                  │
        ┌─────────┴─────────┐
        │                   │
       Yes                 No
        │                   │
        └──────► Loop       │
                            ↓
                   ┌─────────────────┐
                   │ Implementation  │
                   │   Complete      │
                   └─────────────────┘
```

### Shift-Left Security

**"Shift-left"** means moving security testing earlier in the development process.

**Traditional Approach** (Security at the end):
```
Code → Test → Security Review → 😱 Find vulnerabilities → Rewrite
```

**Shift-Left Approach** (Security from the start):
```
🔴 RED: Write Security Tests
         ↓
🟢 GREEN: Implement Securely (CodeGuard patterns)
         ↓
🔵 REFACTOR: Maintain Security
         ↓
😊 Security Built-In
```

**Benefits:**
- Vulnerabilities caught early (cheaper to fix)
- Security tests document requirements
- Developers learn secure patterns
- No security surprises at end
- CodeGuard compliance built-in

### Security Test Examples

From threat model threats, write security tests:

**SQL Injection Prevention:**
```python
def test_prevents_sql_injection_in_plant_search():
    malicious = "7a' OR '1'='1"
    results = search_plants({"zone": malicious})
    assert len(results) == 0  # No results, not bypass
```

**XSS Prevention:**
```python
def test_escapes_html_in_plant_names():
    malicious = "<script>alert('xss')</script>"
    plant = create_plant(name=malicious)
    html = render_plant_card(plant)
    assert "<script>" not in html
    assert "&lt;script&gt;" in html  # Escaped
```

**Authorization Check:**
```python
def test_requires_admin_for_plant_deletion():
    regular_user = create_user(role="user")
    plant = create_plant()

    with pytest.raises(PermissionDenied):
        delete_plant(plant.id, user=regular_user)
```

### Test Structure Standards

**Directory Structure:**
```
src/
├── plants/
│   ├── __init__.py
│   ├── models.py
│   ├── search.py
│   └── validation.py

test/
├── plants/          # Mirrors src/plants/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_search.py
│   └── test_validation.py
```

**Test Naming:**
- File: `test_{module_name}.py`
- Function: `test_{what_it_tests}()`
- Class: `Test{ClassName}`

**AAA Pattern (Arrange-Act-Assert):**
```python
def test_function_name():
    # Arrange: Set up test data
    user = create_user()

    # Act: Execute the function
    result = do_something(user)

    # Assert: Verify the outcome
    assert result.status == "success"
```

### Quality Requirements

**Coverage Threshold:** ≥90%
```bash
pytest --cov=src --cov-report=html
# Open htmlcov/index.html to view coverage
```

**Test Output Must Be Pristine:**
- No warnings
- No deprecation notices
- No print statements in tests
- Clear pass/fail results

**Platform Independence:**
- Use `pathlib.Path` for file paths (not string concatenation)
- No hardcoded OS-specific paths
- Tests run on Windows, macOS, Linux

### Delegates To

- **Slash Command**: `.claude/commands/implement-spec.md`
- **Orchestration Prompt**: `.github/prompts/workflow-spec-to-code.prompt.md`
- **Individual Prompt**: `.github/prompts/generate-code-from-spec.prompt.md`
- **TDD Instructions**: `.github/instructions/tdd-workflow.instructions.md`
- **Test Planning**: `.github/instructions/test-planning.instructions.md`

### Related Documentation

- **TDD Workflow**: `.github/instructions/tdd-workflow.instructions.md` (detailed TDD guidance)
- **Test Planning**: `.github/instructions/test-planning.instructions.md`
- **CodeGuard Rules**: `.github/instructions/codeguard-security/` (25+ security files)
- **Quality Checklist**: `.github/instructions/quality-checklists.md` (Code Generation Stage)
- **Master Workflow**: `.github/instructions/master-workflow.md` (Stage 5)

### Next Steps After Implementation

1. **Human Code Review**: Review implementation for correctness and quality
2. **Integration Testing**: Verify integration with other components
3. **Security Sign-Off**: Security expert reviews threat mitigations
4. **Proceed to Next Feature**: Continue to next requirement or deploy
