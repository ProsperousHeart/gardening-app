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

## Planned Process Snippets

### Phase 2: Specification Generation (Detailed)

**File**: `02-specification-generation.md`
**Should Cover**:

- Deep dive into specification generation process
- Architecture decisions documentation
- Data flow specifications
- Integration requirements
- CodeGuard security considerations

**Status**: ⏳ Pending

### Phase 3: Architecture Diagram Creation

**File**: `03-architecture-diagrams.md`
**Should Cover**:

- `/create-architecture` command
- Three required formats (Text, ASCII, Mermaid)
- Component relationship mapping
- System boundary definition
- Integration points visualization

**Status**: ⏳ Pending

### Phase 4: Threat Modeling

**File**: `04-threat-modeling.md`
**Should Cover**:

- `/create-threat-model` command
- STRIDE framework application
- Threat model scopes (per-requirement, high-level-aggregate, grouped-by-feature)
- Security risk identification
- Mitigation strategies
- CodeGuard compliance

**Status**: ⏳ Pending

### Phase 5: TDD Implementation

**File**: `05-tdd-implementation.md`
**Should Cover**:

- `/implement-spec` command
- RED-GREEN-REFACTOR cycle
- Test-first development
- Code generation from specifications
- Security implementation (CodeGuard rules)
- Quality validation

**Status**: ⏳ Pending

### Phase 6: Quality Review & Verification

**File**: `06-quality-review.md`
**Should Cover**:

- `/quality-review` command
- `/verify` command
- `/security-review` command
- Automated checks (pytest, coverage, ruff)
- Manual review checklists
- Documentation validation

**Status**: ⏳ Pending

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
5. **Include in Process.md**: Add `{% include 'process/XX-phase-name.md' %}` at appropriate location
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
