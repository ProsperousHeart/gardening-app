# Output Format Specification

**Last Updated**: 2025-11-09

This document defines the standard format for execution logs, reports, and AI-generated output files.

## 🎯 Purpose

Standardized output format ensures:

- Consistent logging across all workflow stages
- Easy parsing and analysis
- Complete traceability
- Audit trail for compliance

## 📋 Standard Log Format

All execution logs should follow this template:

```markdown
# Execution Log: {Operation Name}

**Date**: YYYY-MM-DD HH:MM:SS
**Operation**: {Brief description of what was done}
**Input**: {Source documents/files used}
**Output**: {Generated files/artifacts}
**Status**: ✅ Success | 🟡 Partial | ❌ Failed

## Overview

{1-2 paragraph summary of what this operation accomplished}

## Phases Completed

1. ✅ Phase 1: {Description}

   - Details of what was done
   - Key decisions made

2. ✅ Phase 2: {Description}

   - Details of what was done
   - Key decisions made

3. ✅ Phase 3: {Description}
   - Details of what was done
   - Key decisions made

## Status Indicators

Use these special characters throughout logs and documentation:

- ✅ - Complete/Success/Approved
- ❌ - Failed/Rejected/Error
- 🟡 - Partial/In Progress/Warning
- ⏳ - Pending/Waiting
- 📋 - Checklist/Requirements
- 🔒 - Security-related
- 🎯 - Goal/Purpose
- 📝 - Note/Documentation
- 🤖 - AI/Automation
- 🔄 - Process/Workflow
- 📁 - File/Folder
- 🔗 - Link/Reference
- ⚠️ - Warning/Caution
- 💡 - Tip/Suggestion
- 🐛 - Bug/Issue

## CodeGuard Rules Applied

{List each CodeGuard file referenced and why it was relevant}

- **codeguard-0-authentication-mfa.instructions.md**

  - Reason: Implementing user authentication
  - Rules applied: MFA support, secure password hashing, session management

- **codeguard-0-input-validation-injection.instructions.md**
  - Reason: Processing user input
  - Rules applied: Input sanitization, SQL injection prevention

{Repeat for each relevant CodeGuard file}

## Guidelines Followed

{List other instruction files followed}

- **.github/instructions/tdd-workflow.instructions.md** - RED-GREEN-REFACTOR cycle
- **docs/rules/docstring-standards.md** - Docstring formatting
- **.github/instructions/master-workflow.md** - Overall workflow process

## Issues Encountered

{If any issues were encountered, document them here}

### Issue 1: {Brief Description}

- **Error**: {Error message or description}
- **Context**: {When/where it occurred}
- **Resolution**: {How it was fixed}
- **Prevention**: {How to avoid in future}
- **KB Updated**: {Yes/No - if yes, reference docs/rules/error-resolution-kb.md}

### Issue 2: {Brief Description}

{Repeat as needed}

## Test Results

{If applicable, include test output}
```

pytest -v
========================= test session starts =========================
collected 15 items

test/test_auth.py::test_login PASSED [ 6%]
test/test_auth.py::test_logout PASSED [ 13%]
test/test_auth.py::test_invalid_credentials PASSED [ 20%]
...
========================= 15 passed in 2.34s =========================

```

## Quality Checks

{Document quality checks performed}

- ✅ All tests pass
- ✅ Ruff checks pass
- ✅ Security review completed
- ✅ Documentation updated
- ✅ Cross-reference table updated

## Files Created/Modified

{List all files created or modified}

### Created
- `src/auth/login.py`
- `test/test_auth/test_login.py`
- `docs/specifications/spec_auth.md`
- `docs/diagrams/architecture-auth.md`

### Modified
- `docs/SPEC-CROSS-REFERENCE.md`
- `docs/INDEX.md`
- `docs/requirements/req-auth.md` (added link to spec)

## Cross-References

{Link to related documents}

- **Requirement**: [docs/requirements/req-auth.md](../requirements/req-auth.md)
- **Specification**: [docs/specifications/spec_auth.md](../specifications/spec_auth.md)
- **Cross-Reference Table**: [docs/SPEC-CROSS-REFERENCE.md](../SPEC-CROSS-REFERENCE.md)

## Summary

{Brief 2-3 sentence summary of what was accomplished}

---

**Execution Time**: {Duration in minutes/seconds}
**Next Steps**: {What should happen next in the workflow}
```

## 📝 Specific Log Types

### Specification Generation Log

Key sections to emphasize:

- Which requirement(s) were used as input
- CodeGuard files identified as relevant
- Architecture decisions made
- Security considerations

### Code Generation Log (TDD)

Key sections to emphasize:

- TDD cycle documentation (RED-GREEN-REFACTOR)
- Test results at each stage
- CodeGuard rules applied during implementation
- Refactoring decisions

### Threat Modeling Log

Key sections to emphasize:

- STRIDE framework application
- Threats identified
- Mitigations proposed
- CodeGuard files referenced for each threat

### Architecture Diagram Log

Key sections to emphasize:

- Diagram type(s) created
- Component decisions
- Security boundaries marked
- Technology choices

### Security Review Log

Key sections to emphasize:

- CodeGuard compliance verification
- Security findings (if any)
- Recommendations
- Approval status

## ✅ Quality Checklist for Logs

- [ ] All required sections present
- [ ] Date and operation clearly stated
- [ ] Input and output files listed
- [ ] CodeGuard rules documented
- [ ] Issues and resolutions captured
- [ ] Cross-references included
- [ ] Summary is concise and clear
- [ ] Saved to appropriate location (docs/output-logs/)

## 🤖 AI Assistant Usage

When requesting AI assistance, specify output format:

```
Generate code for SPEC-001 following TDD workflow.
Create an execution log in docs/output-logs/ following docs/rules/output-format.md
```

## 🔗 Related Documentation

- [Master Workflow](../../.github/instructions/master-workflow.md)
- [Error Resolution KB](error-resolution-kb.md)
- [Prompts](../../.github/prompts/)

---

**TODO**: Customize this format based on team reporting needs and compliance requirements
