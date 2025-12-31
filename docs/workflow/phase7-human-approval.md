---
title: "Phase 7: Human Approval"
description: Final checkpoint before merging or deploying
created: 2025-12-30
updated: 2025-12-31
status: implemented
---

# Phase 7: Human Approval

Final checkpoint before merging or deploying.

## Approval Gates

Before code can be merged, the following gates must pass:

### Automated Gates (Must Pass)

- ✅ All tests pass (`pytest`)
- ✅ Coverage ≥ 90% (`pytest --cov`)
- ✅ Ruff linting passes (`ruff check`)
- ✅ Formatting applied (`ruff format`)
- ✅ Pre-commit hooks pass

### Documentation Gates (Must Complete)

- ✅ Docstrings follow standards
- ✅ SPEC-CROSS-REFERENCE.md updated
- ✅ INDEX.md updated
- ✅ README files updated (if applicable)

### Security Gates (Must Validate)

- ✅ No hardcoded credentials
- ✅ CodeGuard rules applied
- ✅ Security tests pass
- ✅ Threat mitigations implemented

### Human Review Gates (Must Approve)

- ✅ Code review by peer or senior developer
- ✅ Specification requirements met
- ✅ Security review approved (for security-sensitive features)

## Critical Rule

❌ **NEVER use `--no-verify` flag when committing**

```bash
# ❌ WRONG - Bypasses quality checks
git commit --no-verify -m "Quick fix"

# ✅ CORRECT - Runs quality checks
git commit -m "Add plant search feature"
```

The `--no-verify` flag bypasses pre-commit hooks and can introduce broken or non-compliant code into the repository.

## What Happens After Approval

- **Approved** → Merge to main branch, proceed to next feature, or deploy to production
- **Rejected** → Loop back to **Phase 5 (Implementation)** with feedback and make necessary corrections

## CI/CD Integration

This project uses GitHub Actions for continuous integration:

- `.github/workflows/ci.yml` - Lint, format check, tests
- `.github/workflows/codeql.yml` - CodeQL security scanning
- `.github/workflows/security.yml` - Additional security checks

All workflows must pass before merging to main branch.

---

## Related Documentation

### Instructions & Guides

- **[Master Workflow](../../.github/instructions/master-workflow.md)** - Complete workflow overview (Stage 7)
- **[Quality Checklists](../../.github/instructions/quality-checklists.md)** - Pre-approval quality checks
- **[Security Checklist](../../.github/instructions/security-checklist.md)** - Security verification before approval

### Checklists

- **[Pre-Push Checklist](../checklists/pre-push-checklist.md)** - Must complete before git push
- **[Security Checklist](../checklists/security-checklist.md)** - Security validation checklist

### CI/CD Workflows

- **[CI Workflow](../../.github/workflows/ci.yml)** - Automated lint, format, tests
- **[CodeQL Workflow](../../.github/workflows/codeql.yml)** - Security scanning
- **[Security Workflow](../../.github/workflows/security.yml)** - Additional security checks

### Tutorials

- **[Makefile Guide](../tutorials/general/makefile-guide.md)** - Running final checks before commit
- **[Dependency Management](../tutorials/general/dependency-management.md)** - Managing dependencies with UV

## Status

✅ Documented | 🚦 All approval gates defined
