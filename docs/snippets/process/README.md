# Process Snippets

This folder contains modular documentation snippets for each phase of the Specification-Driven Development (SDD) process. These snippets are included in `docs/Process.md` to maintain a clean, organized workflow documentation.

## Purpose

- **Modularity**: Each SDD phase is documented in its own file
- **Reusability**: Snippets can be included in multiple documents
- **Maintainability**: Update once, changes reflect everywhere
- **Organization**: Clear progression through the SDD workflow

## Naming Convention

Files are numbered sequentially to reflect the SDD workflow order:

```
01-{phase-name}.md
02-{phase-name}.md
03-{phase-name}.md
...
```

## Current Process Snippets

### Phase 1: Requirement Creation

**File**: `01-automated-requirement-creation.md`
**Covers**:

- `/create-requirement` command
- `/make-spec-from-req` command
- Difference between the two
- Complete workflow example
- Directory structure and organization

**Status**: ✅ Complete

### Phase 2: Specification Generation

This phase is a deep dive into specification generation process.

**File**: `02-specification-generation.md`

**Covers**:

- `/make-spec-from-req` workflow orchestration
- Specification generation process
- Architecture diagram creation (automatic)
- Threat model generation (automatic and includes data flow specifications)
- Threat model scopes (per-requirement, high-level-aggregate, grouped-by-feature)
- Historical context of workflow development
- Integration requirements
- CodeGuard security integration

**Status**: ✅ Complete

### Phase 3: Architecture Diagram Creation

**File**: `03-architecture-diagrams.md`

**Covers**:

- `/create-architecture` command
- Three required formats (Text, ASCII, Mermaid)
- ASCII box-drawing characters guide
- Diagram types (System, Component, Sequence, ERD, Deployment) and relationship mapping
- When diagrams are created (AFTER specifications)
- Diagram versioning strategies
- Integration with workflow

**Status**: ✅ Complete

### Phase 4: Threat Modeling

**File**: `04-threat-modeling.md`

**Covers**:

- `/create-threat-model` command
- STRIDE framework (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation of Privilege)
- Why threat modeling comes AFTER specifications
- Threat model scopes explained (per-requirement, high-level-aggregate, grouped-by-feature)
- security risk identification & mitigation strategies
- CodeGuard integration and mapping
- Example threat model output

**Status**: ✅ Complete

### Phase 5: TDD Implementation

**File**: `05-tdd-implementation.md`

**Covers**:

- `/implement-spec` workflow orchestration
- RED-GREEN-REFACTOR cycle explained
- Shift-left security approach with implementation of CodeGuard rules
- Security test examples
- Test structure standards (AAA pattern)
- Quality validation and requirements (≥90% coverage)
- Approval gate before implementation

**Status**: ✅ Complete

### Phase 6: Quality Review & Verification

**File**: `06-quality-review.md`

**Covers**:

- `/quality-review` command
- `/verify <module-path>` command
- `/security-review <module-path>` command
- Automated checks (pytest, coverage, ruff)
- Quality gates
- Pre-commit hooks (NEVER use --no-verify)
- Post-test review checklist

**Status**: ✅ Complete

## Usage in Process.md

Snippets are included using MkDocs macro syntax:

```markdown
{% include 'process/01-automated-requirement-creation.md' %}
```

## Creating New Process Snippets

When documenting a new SDD phase:

1. **Create numbered file**: Follow naming convention (e.g., `02-specification-generation.md`)
2. **Document thoroughly**: Include commands, examples, workflow steps, and insights
3. **Add cross-references**: Link to related documentation (prompts, instructions, templates)
4. **Update this README**: Add entry under "Current Process Snippets"
5. **Include in Process.md**: Add {% raw %}`{% include 'process/XX-phase-name.md' %}`{% endraw %} at appropriate location
6. **Test rendering**: Run `mkdocs serve` to verify snippet displays correctly

## Template Structure

Each process snippet should follow this structure:

```markdown
## {Phase Name}

### Background
[Why this phase exists, what problem it solves]

### Commands Used
[List of slash commands relevant to this phase]

### Workflow Steps
[Step-by-step process with examples]

### Key Insights
[Important lessons learned, common mistakes, best practices]

### Refinements Made
[Document iterations and improvements]

### Related Documentation
[Links to templates, prompts, instructions]
```

## Related Documentation

- **Process Overview**: `docs/Process.md` (includes these snippets)
- **Master Workflow**: `.github/instructions/master-workflow.md`
- **Slash Commands**: `.claude/commands/README.md`
- **Workflow Prompts**: `.github/prompts/README.md`
- **Common Snippets**: `docs/snippets/common/`
- **Technical Snippets**: `docs/snippets/technical/`

## Notes

- Keep snippets focused on ONE phase of the SDD process
- Include practical examples and real command usage
- Document both successes and failures (lessons learned)
- Cross-reference related phases where appropriate
- Update regularly as the process evolves
