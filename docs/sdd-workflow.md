---
title: SDD Workflow Guide
description: Complete guide to the Specification-Driven Development workflow used in this project.
created: 2025-12-30
updated: 2025-12-30
author: Kassandra Keeton
---
# Specification-Driven Development (SDD) Workflow

This guide provides comprehensive documentation for the SDD workflow used in this project, from requirements through deployment.

**Quick Reference**: See [Master Workflow](../.github/instructions/master-workflow.md) for the complete overview.

---

## SDD Workflow Overview

This project follows a **7-phase specification-driven development workflow**:

1. **Phase 0**: Environment Setup
2. **Phase 1**: Requirements Creation
3. **Phase 2**: Specification Generation
4. **Phase 3**: Architecture Diagrams
5. **Phase 4**: Threat Modeling
6. **Phase 5**: TDD Implementation
7. **Phase 6**: Quality Review & Verification
8. **Phase 7**: Human Approval

Each phase is documented below with commands, examples, and best practices.

### Workflow Visual

<div class="ascii-art">
```
┌─────────────┐      ┌─────────────┐     ┌─────────────┐      ┌─────────────┐     ┌─────────────┐
│   Phase 0   │      │   Phase 1   │     │   Phase 2   │      │   Phase 3   │     │   Phase 4   │
│     ENV     │────▶│ REQ Create  │────▶│SPEC Generate│────▶│Architecture │────▶│Threat Model │
│    Setup    │      │  Template   │     │  +Diagrams  │      │  Diagrams   │     │  (STRIDE)   │
└─────────────┘      └─────────────┘     └─────────────┘      └─────────────┘     └─────────────┘
                                                │
                                                ▼
┌─────────────┐      ┌─────────────┐     ┌─────────────┐
│   Phase 7   │      │   Phase 6   │     │   Phase 5   │
│   Human     │◀────│   Quality   │◀────│     TDD     │
│  Approval   │      │   Review    │     │  Implement  │
│   (Gates)   │      │(3 Commands) │     │  RED-GREEN  │
│             │      │             │     │  -REFACTOR  │
└─────────────┘      └─────────────┘     └─────────────┘
```
</div>

??? note "Click to expand interactive Mermaid diagram"

    ```mermaid
    flowchart TD
        P0[Phase 0: Environment Setup] --> P1[Phase 1: Requirements Creation]
        P1 --> P2{Phase 2: /make-spec-from-req req-file<br/>Orchestration Command}

        P2 -->|Generates| SPEC[Specification Document]
        SPEC -->|Auto-generates| P3[Phase 3: Architecture Diagrams]
        SPEC -->|Auto-generates| P4[Phase 4: Threat Model STRIDE]

        SPEC -->|Primary input| P5[Phase 5: TDD Implementation<br/>RED-GREEN-REFACTOR]
        P3 -->|Design context| P5
        P4 -->|Security requirements| P5

        P5 --> P6[Phase 6: Quality Review]
        P6 --> P7[Phase 7: Human Approval]

        P3 -.->|Can run independently| P3_ALT["/create-architecture spec-or-name"]
        P4 -.->|Can run independently| P4_ALT["/create-threat-model spec scope"]

        style P2 fill:#e1f5ff,stroke:#0066cc,stroke-width:3px
        style SPEC fill:#fff4e6,stroke:#ff9800,stroke-width:2px
        style P3 fill:#e8f5e9,stroke:#4caf50,stroke-width:2px
        style P4 fill:#fce4ec,stroke:#e91e63,stroke-width:2px
        style P5 fill:#f3e5f5,stroke:#9c27b0,stroke-width:2px
    ```

    **Key Points:**

    - **Phase 2 (blue)** is an orchestration command that automates multiple steps
    - **Specification (orange)** is the central hub that:
        - Auto-generates Architecture Diagrams (Phase 3) and Threat Model (Phase 4)
        - Serves as the primary input to Phase 5 implementation
    - **Architecture Diagrams (green)** provide design context to implementation
    - **Threat Model (pink)** provides security requirements to implementation
    - **Phase 5 (purple)** receives inputs from spec, architecture, and threat model
    - Phases 3 & 4 can also be run independently if needed

---

## Phase 0: [Environment Setup](workflow/phase0-environment-setup.md)

Set up the development environment with UV package manager.

**Command**: `/setup-env`

**[→ View detailed Phase 0 documentation](workflow/phase0-environment-setup.md)**

---

## Phase 1: [Requirements Creation](workflow/phase1-requirements-creation.md)

Automated requirement creation workflow for streamlined requirement management.

**Key Commands**:

- `/create-requirement <subsystem> <component>` - Create new requirement document
- `/make-spec-from-req <req-file>` - Generate specification from requirement

**[→ View detailed Phase 1 documentation](workflow/phase1-requirements-creation.md)**

---

## Phase 2: [Specification Generation](workflow/phase2-specification-generation.md)

Convert completed requirements into detailed technical specifications with architecture decisions and security considerations.

**Orchestration Workflow**: Generates spec + architecture diagram + threat model + quality review

**[→ View detailed Phase 2 documentation](workflow/phase2-specification-generation.md)**

---

## Phase 3: [Architecture Diagrams](workflow/phase3-architecture-diagrams.md)

Create visual representations of system design with three required formats (Text, ASCII, Mermaid).

**Command**: `/create-architecture <spec-or-name>`

**[→ View detailed Phase 3 documentation](workflow/phase3-architecture-diagrams.md)**

---

## Phase 4: [Threat Modeling](workflow/phase4-threat-modeling.md)

Identify security risks and vulnerabilities using STRIDE framework before implementation.

**Command**: `/create-threat-model <spec> [scope]`

**[→ View detailed Phase 4 documentation](workflow/phase4-threat-modeling.md)**

---

## Phase 5: [TDD Implementation](workflow/phase5-tdd-implementation.md)

Implement features using Test-Driven Development with shift-left security (RED-GREEN-REFACTOR cycle).

**Command**: `/implement-spec <spec-file>`

**[→ View detailed Phase 5 documentation](workflow/phase5-tdd-implementation.md)**

---

## Phase 6: [Quality Review & Verification](workflow/phase6-quality-review.md)

Validate code quality, security, and standards compliance before merging.

**Key Commands**:
- `/quality-review` - Comprehensive project review
- `/verify <module-path>` - Module verification
- `/security-review <module-path>` - Security focus

**[→ View detailed Phase 6 documentation](workflow/phase6-quality-review.md)**

---

## Phase 7: [Human Approval](workflow/phase7-human-approval.md)

Final checkpoint before merging or deploying with automated and human review gates.

**Critical Rule**: ❌ Never use `--no-verify` flag

**[→ View detailed Phase 7 documentation](workflow/phase7-human-approval.md)**

---

## Quick Command Reference

### Development Workflow Commands

| Phase | Type | Command | Purpose |
|-------|------|---------|---------|
| 0 | Setup | `/setup-env` | Set up UV virtual environment |
| 1 | Individual | `/create-requirement <subsystem> <component>` | Create new requirement document |
| 2 | **Orchestration** | `/make-spec-from-req <req-file> [scope]` | Generate specification + architecture + threat model + quality review |
| 3 | Individual | `/create-architecture <spec-or-name>` | Generate architecture diagram (Text, ASCII, Mermaid) |
| 4 | Individual | `/create-threat-model <spec> [scope]` | Create security threat model (STRIDE) |
| 5 | **Orchestration** | `/implement-spec <spec-file>` | Implement using TDD + security review + quality validation |
| 6a | Individual | `/verify <module-path>` | Comprehensive verification |
| 6b | Individual | `/security-review <module-path>` | Security review with CodeGuard |
| 6c | Individual | `/quality-review` | Run quality checks |
| 7 | Individual | `/update-docs <type> <files>` | Update documentation indexes |

??? example "Click to expand command flow diagram (using plant-search example)"

    ```mermaid
    flowchart TD
        START([Start New Feature]) --> P0

        subgraph P0["Phase 0: Environment Setup"]
            CMD0["/setup-env"]
        end

        subgraph P1["Phase 1: Requirements Creation"]
            CMD1["/create-requirement<br/>GenUser plant-search"]
            REQ["req_genuser_plant-search.md"]
            CMD1 --> REQ
        end

        subgraph P2["Phase 2: Specification Orchestration<br/>/make-spec-from-req (AUTO)"]
            CMD2["/make-spec-from-req docs/requirements/GenUser/req_genuser_plant-search.md"]
            SPEC["spec_genuser_plant-search.md"]
            CMD3["/create-architecture spec_genuser_plant-search"]
            CMD4["/create-threat-model spec_genuser_plant-search per-requirement"]
            QR1["Quality Review:<br/>Validate Spec, Architecture, Threat Model"]

            CMD2 --> SPEC
            SPEC --> CMD3
            SPEC --> CMD4
            SPEC --> QR1
            CMD3 --> QR1
            CMD4 --> QR1
        end

        subgraph P5["Phase 5: Implementation Orchestration<br/>/implement-spec (AUTO)"]
            CMD5["/implement-spec docs/specifications/spec_genuser_plant-search.md"]
            TDD["TDD Implementation<br/>RED-GREEN-REFACTOR"]
            CMD6B["/security-review src/plants/search.py"]
            CMD6A["/verify src/plants/search.py"]
            QR2["Quality Validation:<br/>Code, Tests, Security"]

            CMD5 --> TDD
            TDD --> CMD6B
            TDD --> CMD6A
            CMD6B --> QR2
            CMD6A --> QR2
            TDD --> QR2
        end

        subgraph P6["Phase 6: Quality Review (Manual)"]
            CMD6C["/quality-review"]
        end

        subgraph P7["Phase 7: Documentation Updates"]
            CMD7["/update-docs requirements docs/requirements/"]
        end

        P0 --> P1
        P1 --> P2
        P2 --> P5
        P5 --> P6
        P6 --> P7
        P7 --> END([Ready for Human Approval])

        CMD3 -.->|"Can run independently"| INDEP3["/create-architecture spec_genuser_plant-search"]
        CMD4 -.->|"Can run independently"| INDEP4["/create-threat-model spec_genuser_plant-search per-requirement"]

        style P0 fill:#f5f5f5,stroke:#666,stroke-width:2px
        style P1 fill:#fff9c4,stroke:#f57f17,stroke-width:2px
        style P2 fill:#e1f5ff,stroke:#0066cc,stroke-width:3px
        style P5 fill:#e1f5ff,stroke:#0066cc,stroke-width:3px
        style P6 fill:#e3f2fd,stroke:#2196f3,stroke-width:2px
        style P7 fill:#fff3e0,stroke:#ff6f00,stroke-width:2px
    ```

    **Legend:**

    - **Blue (thick border)**: Orchestration phases that run multiple commands automatically
    - **Yellow**: Requirements creation
    - **Light Blue**: Manual quality review
    - **Orange**: Documentation updates
    - **Gray**: Environment setup
    - **Solid lines**: Automatic workflow progression
    - **Dotted lines**: Optional independent execution

### Workflow Orchestration

**Requirements → Specification** (Automated):

```bash
/make-spec-from-req docs/requirements/<subsystem>/req_<subsystem>_<component>.md
```

Generates: specification + architecture diagram + threat model + quality review

**Specification → Code** (Automated with approval gate):

```bash
/implement-spec docs/specifications/spec_<name>.md
```

Generates: TDD implementation + security review + quality validation + documentation updates

---

## Related Documentation

### Workflow Documentation

- **Master Workflow**: `.github/instructions/master-workflow.md` - Complete workflow overview
- **Workflow Usage Guide**: `docs/history/2025-11-09-workflow-usage-guide.md` - Step-by-step examples
- **Process History**: `docs/Process.md` - How this workflow was developed
- **Slash Commands**: `.claude/commands/README.md` - Command reference
- **Workflow Prompts**: `.github/prompts/README.md` - Prompt catalog

### Templates

- **Requirements Template**: `docs/templates/requirements-template.md`
- **Specification Template**: `docs/templates/spec-template.md`

### Standards

- **Markdown Standards**: `docs/rules/markdown-standards.md`
- **Docstring Standards**: `docs/rules/docstring-standards.md`
- **Output Format**: `docs/rules/output-format.md`
- **Error Resolution KB**: `docs/rules/error-resolution-kb.md`

### Security

- **CodeGuard Plugin**: `codeguard-security@project-codeguard`
- **Security Checklist**: `.github/instructions/security-checklist.md`
- **Threat Modeling Instructions**: `.github/instructions/threat-modeling.instructions.md`

### Quality

- **Quality Checklists**: `.github/instructions/quality-checklists.md`
- **TDD Workflow**: `.github/instructions/tdd-workflow.instructions.md`
- **Test Planning**: `.github/instructions/test-planning.instructions.md`

---

## For New Team Members

If you're new to this project:

1. **Start here**: Read this document to understand the workflow
2. **Set up environment**: Run `/setup-env`
3. **Study examples**: Review `docs/history/2025-11-09-workflow-usage-guide.md`
4. **Practice**: Try creating a simple requirement with `/create-requirement`
5. **Ask questions**: Reference the related documentation above

**Remember**: This workflow is designed to ensure quality, security, and maintainability. Don't skip phases!
