# Requirements Directory

This directory is where you should save all the requirements documents created for the project.

## Purpose

- Store requirements documents generated using Claude or Copilot with the template from at [`requirements-template.md`](../templates/requirements-template.md)
- Keep all project requirements organized in one location
- Reference during specification and implementation phases

## How to Use

1. When creating a new feature or module, start by creating a requirements document using: `@docs/templates/requirements-template.md`
2. Save the generated requirements document in this directory
3. Use descriptive filenames like `user-authentication.md`, `data-export-module.md`
4. Use these requirements to generate specifications with the `/make-spec-from-req` command

## Workflow

The typical development workflow using requirements:

1. **Create Requirements**: Define what needs to be built using the requirements template
2. **Generate Specification**: Use `/make-spec-from-req [component-name] [req-file]` to create a detailed specification
3. **Implement**: Build the feature based on the specification
4. **Validate**: Verify implementation meets the requirements

## File Naming Convention

Use kebab-case for requirements files:

- `user-authentication.md`
- `data-export-module.md`
- `logging-system.md`
- `api-integration.md`

## What Goes in a Requirements Document

Each requirements document should follow the template structure and include:

- **Context**: Purpose, role in application, users, usage scenarios
- **Functional Requirements**: Core features, business logic, state management
- **Interface Requirements**: API, CLI, UI specifications
- **Data Requirements**: Models, schemas, validation rules
- **Integration Requirements**: Dependencies, external services, data flow
- **Constraints**: Technical stack, performance, security, design constraints
- **Success Criteria**: Validation checklists for functional, technical, testing, and security aspects

## Tips

- Be specific and detailed - more detail in requirements leads to better specifications
- Include code examples and data structure definitions where applicable
- Document security requirements using CodeGuard principles
- Define acceptance criteria clearly with measurable outcomes
- Link related requirements documents in the "Notes & Considerations" section
