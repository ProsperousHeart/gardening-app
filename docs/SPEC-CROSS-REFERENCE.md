# Specification Cross-Reference Table

**Last Updated**: 2025-11-09

This table tracks relationships between requirements, specifications, source code, tests, and diagrams. It serves as the central navigation hub for understanding how requirements are implemented throughout the codebase.

## Purpose

- **Traceability**: Follow a requirement from concept through implementation
- **Coverage**: Ensure all requirements have specifications and implementations
- **Testing**: Verify all specifications have corresponding tests
- **Documentation**: Link specifications to relevant diagrams and documentation

## How to Use This Table

- **Links are bidirectional**: Each linked file should reference back to this table
- **Status values**: Not Started, In Progress, In Review, Approved, Implemented, Tested
- **Multiple entries**: Separate multiple files with `<br>` in the table cell

## Cross-Reference Table

| Requirement | Specification | Source Files | Test Files | Diagrams | Status |
| ----------- | --------------|--------------|------------|----------|--------|
| Example: [example-req](requirements/example-req.md) | [example-spec](specifications/example-spec.md) | [src/example.py](../src/example.py) | [test/test_example.py](../test/test_example.py) | [architecture-example.md](diagrams/architecture-example.md)<br>[threat-model-example.md](diagrams/threat-model-example.md) | Example |
| [REQ-000a_General](requirements/REQ-000a_General.md) (General) | TBD | N/A | N/A | [context-main](./diagrams/context-general.md#main-all-users)<br>[context-community](./diagrams/context-general.md#community-gardener-special-user-access) | IN PROGRESS |
| [REQ-000b_Scope](requirements/REQ-000b_Scope.md) (Scope) | TBD | N/A | N/A | TBD | IN PROGRESS |
| [REQ-000c_UseCases](requirements/REQ-000c_UseCases.md) (Use Cases) | TBD | N/A | N/A | Multiple - see MD | IN PROGRESS |
| [REQ-000d_UCBDs](requirements/REQ-000d_UCBDs.md) (Use Case Behavior Diagrams) | TBD | N/A | N/A | Multiple - see MD | IN PROGRESS |
| [REQ-000e_Requirements](requirements/REQ-000e_Requirements.md) (Requirements Specs) | Multiple | TBD | TBD | Multiple | IN PROGRESS |
| [REQ-000f_FBDs](requirements/REQ-000f_FBDs.md) (Functional Flow Block Diagrams) | Multiple | TBD | TBD | Multiple | IN PROGRESS |
| [REQ-000g_Decisions](requirements/REQ-000g_Decisions.md) (Decision Diagrams) | Multiple | TBD | TBD | Multiple | IN PROGRESS |

## Adding New Entries

When creating new requirements or specifications:

1. Add a new row to the table
2. Link to the requirement document in `requirements/`
3. Link to the specification document in `specifications/`
4. As implementation progresses, add links to source files, tests, and diagrams
5. Update the status column
6. Update the "Last Updated" date at the top of this file

## Automation

This table can be automatically updated using:
- GitHub Actions (see `.github/workflows/`)
- Pre-commit hooks
- Manual update scripts

See [.github/instructions/automation-setup.instructions.md](../.github/instructions/automation-setup.instructions.md) for details.

## Header Template for Linked Files

Each file referenced in this table should include a header section linking back:

```markdown
---
**Cross-Reference**: See [SPEC-CROSS-REFERENCE.md](../SPEC-CROSS-REFERENCE.md) for implementation tracking
**Requirement**: [REQ-XXX](../requirements/req_xxx.md)
**Specification**: [SPEC-XXX](../specifications/spec_xxx.md)
---
```

Adjust paths as needed based on file location.

## Related Documentation

- [Master Index](INDEX.md) - Complete documentation overview
- [Master Workflow](../.github/instructions/master-workflow.md) - Development process documentation
