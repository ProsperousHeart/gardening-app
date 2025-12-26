# Project-Specific Claude Instructions

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This project also uses the CodeGuard plugin for AI-assisted secure code generation.

## Table of Contents

- [Project Specific Details](#project-specific-details)
    - [Project Overview](#project-overview)
    - [Project Status & Development Approach](#project-status--development-approach)
    - [Architecture](#architecture)
        - [Key Architecture Patterns](#key-architecture-patterns)
        - [Documentation Structure](#documentation-structure)
        - [Key System Features](#key-system-features)
        - [Key Architecture Concepts](#key-architecture-concepts)
- [Development Workflow](#development-workflow)
    - [Orchestration Workflow Prompts](#orchestration-workflow-prompts)
    - [CI/CD](#cicd)
    - [Slash Commands](#slash-commands)
        - [Relationship to Prompts](#relationship-to-prompts)
        - [Development Workflow Commands](#development-workflow-commands)
        - [Individual Operation Commands](#individual-operation-commands)
- [Development Commands](#development-commands)
    - [Linting and Formatting](#linting-and-formatting)
    - [Testing](#testing)
    - [Quick Start with Makefile](#quick-start-with-makefile)
    - [MkDocs Documentation](#mkdocs-documentation)
    - [Environment Setup](#environment-setup)
- [Security Framework](#security-framework)
    - [About CodeGuard](#about-codeguard)
    - [Security Coverage](#security-coverage)
- [Critical Operational Notes](#critical-operational-notes)
    - [Code Standards](#code-standards)
    - [Always Use UV Package Manager](#always-use-uv-package-manager)
    - [Diagram Format Requirements](#diagram-format-requirements)
    - [Threat Modeling Order](#threat-modeling-order)
    - [Working on This Project](#working-on-this-project)
    - [Documentation Best Practices](#documentation-best-practices)
- [Related Documentation](#related-documentation)
    - [Django Application Architecture (2024-Django-Attempt - Reference Only)](#django-application-architecture-2024-django-attempt---reference-only)

## Project Specific Details

### Project Overview

This is a gardening application designed to help new gardeners and community gardeners determine what to plant in their yard. The project uses Django and follows a **specification-driven development workflow** through Cornell's Systems Design certification program.

**Key Context:**

- The project originated from a community garden that grows food for local food pantries
- Users range from budding gardeners to master gardeners, including community garden apprentices, supporters, and plot managers
- The system aims to provide plant information, garden planning, weather notifications, and secure collaboration tools for community gardening

**Project Characteristics:**

- **Specification-driven workflow**: Requirements → Specifications → Code using Test Driven Development
- **Security-first approach**: Integrated [CodeGuard](https://github.com/project-codeguard) security guidelines
- **Systems design methodology**: Formal requirements analysis with context diagrams, FFBDs, UCBDs via Cornell's Systems Design certification program
- **AI-assisted development**: Structured workflows for Claude Code and GitHub Copilot

### Project Status & Development Approach

**IMPORTANT:** The `2024-Django-Attempt/` folder contains an original Django implementation that will likely be removed soon. This is **reference only** for understanding existing data models.

**Current focus** is on **systems requirements documentation** in the `gardening-docs/` folder using MkDocs. The documentation represents formal systems design including:

- Context diagrams defining system boundaries and stakeholders
- Use cases and scenarios (23+ scenarios identified)
- Functional Flow Block Diagrams (FFBDs) for architecture
- Use Case Behavior Diagrams (UCBDs)
- Requirements tables and scope trees

**New development should follow the specifications-based approach**, not the legacy Django implementation.

### Architecture

**Key Architecture Patterns:**
- **Hardiness Zone System**: Plant compatibility by USDA zones (1a-13b)
- **Plant Characteristics as Boolean Flags**: Extensive use for filtering
- **Exposure Categories**: Five-level categorization from Full Sun to Shade
- **Range-based Physical Attributes**: Min/max fields for spacing and height

#### Documentation Structure

Currently, there are 2 locations for documentation:
1. Used for mkdocs
2. Used for program architecture planning and specification driven development

Documentation for mkdocs needs is located in `docs/`:

- `index.md` - Project description, stakeholders, original scenarios
- `scope.md` - Context diagrams, use cases, scenarios, scope tree
- `system-requirements.md` - Requirements documentation (in progress)
- `architecture.md` - Functional Flow Block Diagrams (TBD)
- `progress.md` - Current status and next steps
- `resources.md` - Resources used in development

mkdocs Configuration: `mkdocs.yml`

The project uses a comprehensive documentation system for specification driven development in `docs/`:

```
docs/
├── INDEX.md                    # Documentation master index
├── SPEC-CROSS-REFERENCE.md     # Tracks requirements→specs→code→tests
├── requirements/               # What to build
├── specifications/             # How to build it
├── diagrams/                   # Architecture diagrams
├── templates/                  # Templates for docs creation
├── rules/                      # Project standards
└── history/                    # Decision logs
```

**Key Documentation Standards:**
- **Diagram formats**: See `.github/instructions/architecture-diagrams.instructions.md`
- **Markdown standards**: See `docs/rules/markdown-standards.md`
- **Docstring standards**: See `docs/rules/docstring-standards.md`

#### Key System Features

**User Roles:**

- **System Users** (general gardeners)
- **Admin** (system administrators)
- **Community Lead** (manages community garden groups)
- **Community Members** (general members, team/chore assigned)
- **Apprentices** (in training program)
- **Supporters** (non-gardeners who help with tasks)

**Core Features:**

1. **General User Functions:**
   - Plant search and filtering by zone, type, season, characteristics
   - View plant data (common/scientific name, hardiness zone, spacing, height, container size, companion plants, medicinal benefits)
   - Weather component with alerts and historical data
   - Moon planning for planting
   - Sun angle visualization for bed planning
   - Personal settings (USDA location manual/automated)
   - User plant collections and personal settings
   - Feedback submission and error reporting
   - 

2. **Admin Functions:**
   - Create/manage community leads
   - Account management
   - System permissions

3. **Community Member Functions:**
   - Plot management
   - Team/chore assignments
   - Training modules and progress tracking (for apprentices)
   - Collaboration tools

#### Key Architecture Concepts

**USDA Hardiness Zones**: Plants are categorized by temperature tolerance zones (1a-13b) which determine what can grow in a location.

**Plant Characteristics**: System tracks extensive attributes including:
- Exposure requirements (Full Sun 6+hrs, Partial Sun/Shade, Shade)
- Plant types (Annual, Biennial, Perennial, Shrub, Tree, Vine)
- Growing attributes (drought tolerant, heat tolerant, deer resistant, pollinator friendly, etc.)
- Timing (germination days, days to maturity)
- Physical dimensions (spacing, height, container size)

**Weather Integration**: System will provide location-based weather data and alerts to protect plants.

**Resource Links**: Plants can have associated resources (academic articles, blogs, books, master gardener info, nursery info, YouTube videos).

## Development Workflow

This project follows a structured specification-driven workflow:

1. **Requirements**: Define what to build using `docs/templates/requirements-template.md`
2. **Specifications**: Generate detailed specs from requirements with architecture decisions
3. **Architecture Diagrams**: Create visual diagrams based on specifications (see `.github/instructions/architecture-diagrams.instructions.md`)
4. **Threat Modeling**: Identify security risks based on specifications & architecture (see `.github/instructions/threat-modeling.instructions.md`)
5. **TDD Implementation**: Write tests first, then code (see `.github/instructions/tdd-workflow.instructions.md`)
6. **Quality Review**: Validate against checklists (see `.github/instructions/quality-checklists.md`)

**Note**: Threat modeling comes AFTER specifications because you need to know the system architecture, data flows, and integrations before identifying threats.

See `.github/instructions/master-workflow.md` for complete details.

### Orchestration Workflow Prompts

Use orchestration prompts to automate multi-step workflows:

**Requirements → Specification:**
```
# Option 1
Execute .github/prompts/workflow-requirements-to-spec.prompt.md for docs/requirements/req-{name}.md

# Option 2
Execute the workflow-requirements-to-spec prompt for docs/requirements/req-{name}.md
```
- Generates spec, architecture diagram, threat model (in correct order), runs quality review

**Specification → Code:**
```
# Option 1
Execute .github/prompts/workflow-spec-to-code.prompt.md for docs/specifications/spec-{name}.md

# Option 2
Execute the workflow-spec-to-code prompt for docs/specifications/spec-{name}.md
```
- Implements with TDD, runs security review, quality validation

See `docs/history/2025-11-09-workflow-usage-guide.md` for step-by-step examples.

### CI/CD

GitHub Actions workflows:
- `.github/workflows/ci.yml` - Lint, format check, tests
- `.github/workflows/codeql.yml` - CodeQL security scanning
- `.github/workflows/security.yml` - Additional security checks

### Slash Commands

Claude Code provides custom slash commands for common workflows.

**IMPORTANT**: These slash commands are the primary way to interact with this repository's workflow system.

### Relationship to Prompts

- Slash commands delegate to workflow prompts in `.github/prompts/`
- Prompts are tool-agnostic (work with Copilot too)

**GitHub Copilot users**: See `.github/instructions/copilot-usage.instructions.md`

#### Development Workflow Commands

| Command | Purpose | Delegates To |
|---------|---------|-------------|
| `/setup-env` | Set up UV virtual environment | `.github/instructions/uv-environment-setup.instructions.md` |
| `/create-requirement <name>` | Create new requirement document | `.github/prompts/create-requirement.prompt.md` |
| `/make-spec-from-req <req-file> [scope]` | Generate specification from requirement | `.github/prompts/workflow-requirements-to-spec.prompt.md` |
| `/implement-spec <spec-file>` | Implement specification using TDD | `.github/prompts/workflow-spec-to-code.prompt.md` |
| `/quality-review` | Run comprehensive quality checks | `.github/instructions/quality-checklists.md` |

**See `.claude/commands/README.md` for detailed usage.**

#### Individual Operation Commands

| Command | Purpose | Delegates To |
|---------|---------|-------------|
| `/create-architecture <spec-or-name>` | Generate architecture diagram | `.github/prompts/create-architecture-diagram.prompt.md` |
| `/create-threat-model <spec> [scope]` | Create security threat model (STRIDE) | `.github/prompts/create-threat-model.prompt.md` |
| `/verify <module-path>` | Comprehensive verification of implementation | `.github/prompts/verify-implementation.prompt.md` |
| `/security-review <module-path>` | Security review with CodeGuard | `.github/prompts/security-review.prompt.md` |
| `/update-docs <type> <files>` | Update documentation indexes | `.github/prompts/update-documentation.prompt.md` |

**Note**: These commands are thin wrappers that delegate to tool-agnostic workflow prompts in `.github/prompts/`. See `.claude/commands/README.md` for detailed usage.

## Development Commands

### Linting and Formatting

```bash
make lint      # Run flake8
make format    # Run black
```

Configuration in `.flake8` (max line length: 88).

### Testing

**See `.github/instructions/tdd-workflow.instructions.md` for complete TDD workflow and testing requirements.**

**Quick commands:**
```bash
make test      # Run all tests
pytest -v      # Run with verbose output
```

**IMPORTANT:** Never commit with `--no-verify` flag.

### Quick Start with Makefile

This project uses a Makefile for common development tasks. All commands use `uv run` to ensure proper virtual environment execution.

```bash
# Show all available commands
make help

# Install dependencies
make install

# Development workflow (run before committing)
make lint          # Check code quality with flake8
make format        # Auto-format code with Black
make test          # Run tests with pytest

# Additional commands
make format-check  # Check formatting without modifying
make test-coverage # Run tests with coverage report
make clean         # Remove cache and temporary files
```

See `docs/tutorials/general/makefile-guide.md` for detailed documentation.

For linting, update configuration in `.flake8` (max line length: 88).

### MkDocs Documentation

```bash
# Build static site
cd gardening-docs
mkdocs build

# Serve documentation locally (auto-reload on changes)
cd gardening-docs
mkdocs serve

# Deploy to GitHub Pages
cd gardening-docs
mkdocs gh-deploy
```

### Environment Setup

**See [Dependency Management Guide](docs/tutorials/general/dependency-management.md) for complete installation and usage instructions.** (Original [uvx setup guide](docs/tutorials/general/archive/uvx-setup-guide.md) archived for reference.)

This project uses `uv` for dependency management with `pyproject.toml`.

```bash
# Create virtual environment
uv venv

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Activate virtual environment (Unix/macOS)
source .venv/bin/activate

# Install all dependencies from pyproject.toml
uv sync

# Add new production dependencies
uv add <package-name>

# Add new development dependencies
uv add --dev <package-name>
```

For detailed setup instructions, see `docs/tutorials/general/dependency-management.md`.

## Security Framework

**Plugin:** `codeguard-security@project-codeguard`
**Update command:** `/plugin update codeguard-security@project-codeguard`
**Source:** https://github.com/project-codeguard/rules
**Documentation:** https://project-codeguard.org/

### About CodeGuard

Project CodeGuard is an open-source security framework from Cisco that embeds secure-by-default practices into AI coding workflows. It provides comprehensive security rules across 8 domains that guide AI assistants to generate more secure code automatically.

### Security Coverage

- Cryptography (algorithms, key management, certificate validation)
- Input validation (SQL injection, XSS, command injection prevention)
- Authentication (MFA, OAuth/OIDC, session management)
- Authorization (RBAC/ABAC, access control)
- Supply chain security
- Cloud security
- Platform security
- Data protection

## Critical Operational Notes

### Code Standards

- **Docstrings**: See `docs/rules/docstring-standards.md`
- **Python version**: Python 3.14+

#### Testing Requirements

**See `.github/instructions/tdd-workflow.instructions.md` for complete requirements.**

Key points:
- Follow TDD workflow: Red → Green → Refactor
- Test output must be pristine
- Tests must be platform independent
- **NO EXCEPTIONS POLICY**: Must have unit, integration, AND end-to-end tests

#### AI Assistant Workflows

- `.github/instructions/claude-usage.instructions.md` - Claude Code workflows
- `.github/instructions/copilot-usage.instructions.md` - GitHub Copilot workflows
- `.github/instructions/master-workflow.md` - Master workflow document

### Always Use UV Package Manager

**CRITICAL**: This project uses `uv` for dependency management. NEVER use `pip` or `pip install`.

```bash
# ✅ CORRECT
uv add <package-name>
uv add --dev <package-name>
uv sync

# ❌ WRONG
pip install <package-name>
uv pip install <package-name>
```

### Diagram Format Requirements

**CRITICAL**: All architecture diagrams MUST include THREE formats:

1. **Text Description** - Human-readable bullet points, tables, or numbered lists
2. **ASCII Diagram** - Text-based visual using box-drawing characters (┌ ─ ┐ │ └ ┘ ├ ┤ ┬ ┴ ┼ → ↓ ↑ ← ═)
3. **Mermaid Diagram** - Collapsible Mermaid code block

See `.github/instructions/architecture-diagrams.instructions.md` for complete format structure and examples.

### Threat Modeling Order

**IMPORTANT**: Threat modeling comes AFTER specifications because you need to know the system architecture, data flows, and integrations before identifying threats.

### Working on This Project

1. **Follow specification-driven workflow** - See `.github/instructions/master-workflow.md`
2. **Focus on documentation work** - The application code will be rebuilt based on these specs
3. **Follow systems design methodology** - Reference the documentation structure when discussing features
4. **Understand user diversity** - System must serve both novice gardeners to experienced community garden managers
5. **Consider community garden workflows** - Features like plot tracking, team assignments, and training are critical
6. **2024-Django-Attempt is reference only** - Use it for understanding existing data models but new development follows the specifications-based approach. Do not use this to plan new work, as it may not be efficient
7. **Use slash commands** - `/make-spec-from-req` and `/implement-spec` for automated workflows
8. **Always include three diagram formats** - See `.github/instructions/architecture-diagrams.instructions.md`
9. **Security first** - Apply CodeGuard guidelines and include threat modeling
10. **Link to canonical documentation** - Maintain Single Source of Truth

### Documentation Best Practices

**See `docs/rules/markdown-standards.md` for complete standards.**

Key principles:
- **Single Source of Truth** - one canonical location per concept
- **Link, don't duplicate** - reference canonical documentation
- **README files are navigation hubs** - they link to detailed docs

## Related Documentation

- **Master Workflow**: `.github/instructions/master-workflow.md`
- **Slash Commands**: `.claude/commands/README.md`
- **Workflow Prompts**: `.github/prompts/`
- **CodeGuard Security**: `.claude/CLAUDE.md`
- **Project Documentation**: https://prosperousheart.github.io/gardening-app/
- **Miro Board**: https://miro.com/app/board/uXjVLFJo2wg=/

### Django Application Architecture (2024-Django-Attempt - Reference Only)

**Django Configuration:**
- **Project Name**: `config`
- **Database**: SQLite3 (development)
- **Installed Apps**: Standard Django apps + local `Plants` app

**Directory Structure:**
- `2024-Django-Attempt/config/` - Django project configuration (settings, URLs, WSGI/ASGI)
- `2024-Django-Attempt/Plants/` - Main Django app containing plant models and logic
- `gardening-docs/` - MkDocs system requirements documentation
- `specs/` - Application specifications (new specifications go here)

**Core Data Models** (in `2024-Django-Attempt/Plants/models.py`):

1. **Plant Model** (`2024-Django-Attempt/Plants/models.py:21-104`):
   - Comprehensive plant information including common/scientific names, USDA (or related country's hardiness) zones, exposure requirements, physical dimensions, and special attributes
   - Uses Django choices for `EXPOSURE_CHOICES`, `TYPE_CHOICES`, and `HARDINESS_ZONES` (1a-13b)
   - Boolean flags for plant characteristics (drought tolerant, deer resistant, pollinator friendly, etc.)
   - Related to `PlantLink` via many-to-many relationship

2. **Profile Model** (`2024-Django-Attempt/Plants/models.py:112-121`):
   - OneToOne with Django User model
   - Many-to-many with Plant for user collections
   - Methods: `add_plant()`, `remove_plant()`

3. **PlantLink Model** (`2024-Django-Attempt/Plants/models.py:123-166`):
   - Represents external resources linked to plants (articles, videos, books, nursery info)
   - Choice field for link types
   - Link types: Academic Article, Blog, Book, Master Gardener, Nursery, YouTube, Other

4. **Nursery Model** (`2024-Django-Attempt/Plants/models.py:9-18`):
   - Stores nursery information with many-to-many to Plant

**Key Architecture Patterns:**
- **Hardiness Zone System**: Plant compatibility by USDA zones (1a-13b)
- **Plant Characteristics as Boolean Flags**: Extensive use of boolean fields for filtering
- **Exposure Categories**: Five-level categorization from Full Sun to Shade
- **Range-based Physical Attributes**: Min/max fields for spacing and height
