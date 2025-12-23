# Documentation Hub

Welcome to the central documentation hub for this project. All requirements, specifications, diagrams, and related documentation are organized here.

## 📋 Master Index

**Start here**: [INDEX.md](INDEX.md) - Complete documentation overview and navigation

## 🔗 Quick Links

- **[Specification Cross-Reference Table](SPEC-CROSS-REFERENCE.md)** - Track implementation progress
- **[Requirements](requirements/)** - What needs to be built
- **[Specifications](specifications/)** - How it will be built
- **[Diagrams](diagrams/)** - Visual documentation (architecture, threat models, etc.)
- **[Rules](rules/)** - Project standards and conventions
- **[Templates](templates/)** - Starting point for new documentation
- **[History](history/)** - Decision logs and important conversations

## 🚀 Getting Started

### For New Team Members

1. Read the [Master Index](INDEX.md) to understand the documentation structure
2. Review existing [Requirements](requirements/) to understand project goals
3. Check the [Specification Cross-Reference Table](SPEC-CROSS-REFERENCE.md) to see what's implemented
4. Familiarize yourself with [Rules](rules/) to understand coding standards

### For Adding New Features

**Quick Start**: Use workflow orchestration prompts:
- [Requirements → Specification Workflow](../.github/prompts/workflow-requirements-to-spec.prompt.md) - Generates spec, threat model, architecture diagram with quality review
- [Specification → Code Workflow](../.github/prompts/workflow-spec-to-code.prompt.md) - TDD implementation with security and quality reviews

**Or step-by-step**:
1. **Requirements**: Create a new requirement in `requirements/` using the [template](templates/requirements-template.md)
2. **Specifications**: Generate or write a specification in `specifications/` using the [template](templates/spec-template.md)
3. **Diagrams**: Create architecture diagrams and threat models in `diagrams/`
4. **Implementation**: Follow the TDD workflow in [.github/instructions/master-workflow.md](../.github/instructions/master-workflow.md)
5. **Quality Gates**: Validate against [quality checklists](../.github/instructions/quality-checklists.md)
6. **Cross-Reference**: Update [SPEC-CROSS-REFERENCE.md](SPEC-CROSS-REFERENCE.md) to track your work

**Practical Examples**: See [Workflow Usage Guide](history/2025-11-09-workflow-usage-guide.md) for step-by-step examples

## 🤖 AI Assistant Integration

This documentation structure works with both **Claude Code** and **GitHub Copilot**:

- **Claude Code**: See [.github/instructions/claude-usage.instructions.md](../.github/instructions/claude-usage.instructions.md)
- **GitHub Copilot**: See [.github/instructions/copilot-usage.instructions.md](../.github/instructions/copilot-usage.instructions.md)

## 📁 Folder Structure

```
docs/
├── INDEX.md                      # Master index (start here!)
├── SPEC-CROSS-REFERENCE.md       # Implementation tracking table
├── README.md                     # This file
├── requirements/                 # Feature requirements
├── specifications/               # Technical specifications
├── diagrams/                     # Architecture, threat models, etc.
├── rules/                        # Standards and conventions
├── templates/                    # Documentation templates
├── history/                      # Decision logs
└── output-logs/                  # Workflow execution logs
```

## 🔄 Documentation Workflow

This project follows a **specification-driven development** approach:

```
Requirements → Specifications → Code Generation (TDD) → Quality Review → Approval
```

Each stage has human approval gates and automated quality checks. See the [Master Workflow](../.github/instructions/master-workflow.md) for complete details.

## 🛠️ Automation

Documentation can be automatically updated using:
- GitHub Actions
- Pre-commit hooks
- Manual scripts

See [.github/instructions/](../.github/instructions/) for automation setup guides.

## 📚 Additional Resources

- **[Master Workflow](../.github/instructions/master-workflow.md)** - Complete development process
- **[CodeGuard Security](../.github/instructions/)** - Security guidelines for code generation
- **[Error Resolution KB](rules/error-resolution-kb.md)** - Common issues and solutions

---

**Note**: This is a template repository. When you use this template for a new project, start by creating your first requirement in `requirements/` and following the workflow from there.
