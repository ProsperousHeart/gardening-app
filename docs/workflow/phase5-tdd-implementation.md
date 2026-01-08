---
title: "Phase 5: TDD Implementation"
description: Implement features using Test-Driven Development with shift-left security
created: 2025-12-30
updated: 2025-12-31
status: approved
---

# Phase 5: TDD Implementation

--8<-- "snippets/process/05-tdd-implementation.md"

---

## Related Documentation

### Instructions & Guides

- **[TDD Workflow Instructions](../../.github/instructions/tdd-workflow.instructions.md)** - Test-Driven Development process
- **[Test Planning Instructions](../../.github/instructions/test-planning.instructions.md)** - Test strategy and planning
- **[Master Workflow](../../.github/instructions/master-workflow.md)** - Complete workflow overview (Stage 5)
- **[Security Checklist](../../.github/instructions/security-checklist.md)** - Security review during development

### Commands & Prompts

- **Slash Command**: `.claude/commands/implement-spec.md`
- **Orchestration Workflow**: `.github/prompts/workflow-spec-to-code.prompt.md`
- **Verification Prompt**: `.github/prompts/verify-implementation.prompt.md`
- **Security Review**: `.github/prompts/security-review.prompt.md`

### Tutorials

- **[Makefile Guide](../tutorials/general/makefile-guide.md)** - Running tests (`make test`, `make lint`, `make format`)
- **[Dependency Management](../tutorials/general/dependency-management.md)** - Managing test dependencies with UV
- **[Bandit Security Guide](../tutorials/general/bandit-security-guide.md)** - Security scanning with Bandit

### Security Framework

- **[CodeGuard Plugin](https://github.com/project-codeguard/rules)** - Shift-left security guidelines
- **Plugin Skill**: `/codeguard-security:software-security` - Security skill for code review
