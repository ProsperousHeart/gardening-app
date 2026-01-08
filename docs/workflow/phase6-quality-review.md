---
title: "Phase 6: Quality Review & Verification"
description: Validate code quality, security, and standards compliance
created: 2025-12-30
updated: 2025-12-31
status: approved
---

# Phase 6: Quality Review & Verification

--8<-- "snippets/process/06-quality-review.md"

---

## Related Documentation

### Instructions & Guides

- **[Quality Checklists](../../.github/instructions/quality-checklists.md)** - Comprehensive quality review checklists
- **[Security Checklist](../../.github/instructions/security-checklist.md)** - Security verification checklist
- **[Master Workflow](../../.github/instructions/master-workflow.md)** - Complete workflow overview (Stage 6)
- **[Docstring Standards](../rules/docstring-standards.md)** - Code documentation standards
- **[Output Format Standards](../rules/output-format.md)** - Output formatting requirements
- **[Error Resolution KB](../rules/error-resolution-kb.md)** - Common errors and solutions

### Commands & Prompts

- **Slash Command (Overall)**: `.claude/commands/quality-review.md`
- **Slash Command (Module)**: `.claude/commands/verify.md`
- **Slash Command (Security)**: `.claude/commands/security-review.md`
- **Verification Prompt**: `.github/prompts/verify-implementation.prompt.md`
- **Security Review Prompt**: `.github/prompts/security-review.prompt.md`

### Tutorials

- **[Makefile Guide](../tutorials/general/makefile-guide.md)** - Running quality commands (`make lint`, `make format`, `make test`)
- **[Bandit Security Guide](../tutorials/general/bandit-security-guide.md)** - Security scanning tools

### Checklists

- **[Pre-Push Checklist](../checklists/pre-push-checklist.md)** - Checklist before pushing code
- **[Security Checklist](../checklists/security-checklist.md)** - Security review checklist
