# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Table of Contents

- [Project Overview](#project-overview)
- [Development Workflow](#development-workflow)
- [Development Commands](#development-commands)
  - [Environment Setup](#environment-setup)
  - [Linting and Formatting](#linting-and-formatting)
  - [Testing](#testing)
  - [Pre-commit Hooks](#pre-commit-hooks)
  - [MkDocs Documentation](#mkdocs-documentation)
  - [Django Application](#django-application)
- [Slash Commands](#slash-commands)
- [Architecture](#architecture)
  - [Documentation Structure](#documentation-structure)
  - [Testing Pattern](#testing-pattern)
  - [Django Application Architecture](#django-application-architecture)
- [CI/CD](#cicd)
- [Project Structure](#project-structure)
- [Important Notes](#important-notes)

## Project Overview

This is a gardening application designed to help new gardeners and community gardeners determine what to plant in their yard. The project is built with Django and is intended to be hosted on Render.

**Key Context:**

- The project originated from a community garden that grows food for local food pantries
- Users range from budding gardeners to master gardeners, including community garden apprentices, supporters, and plot managers
- The system aims to provide plant information, garden planning, weather notifications, and secure collaboration tools for community gardening

### Project Characteristics

This project demonstrates:

- **Production-ready patterns**: Django models, comprehensive testing, secure authentication
- **Specification-driven workflow**: Requirements → Specifications → Code using Test Driven Development
- **Security-first approach**: Integrated [CodeGuard](https://github.com/project-codeguard) security guidelines
- **AI-assisted development**: Structured workflows for Claude Code and GitHub Copilot
- **Systems design methodology**: Formal requirements analysis through Cornell's Systems Design certification program

## Project Status & Development Approach

**Important:** The `2024-Django-Attempt/` folder contains an original attempt at building the application but will likely be removed soon. The project is now following **specifications-based development** through Cornell's Systems Design certification program.

Current focus is on **systems requirements documentation** in the `gardening-docs/` folder using MkDocs. The documentation represents formal systems design including:

- Context diagrams defining system boundaries and stakeholders
- Use cases and scenarios (23+ scenarios identified)
- Functional Flow Block Diagrams (FFBDs) for architecture
- Use Case Behavior Diagrams (UCBDs)
- Requirements tables and scope trees

## Development Workflow

This project follows a structured specification-driven workflow:

1. **Requirements**: Define what to build using `docs/templates/requirements-template.md`
2. **Specifications**: Generate detailed specs from requirements with architecture decisions
3. **Architecture Diagrams**: Create visual diagrams based on specifications (see `.github/instructions/architecture-diagrams.instructions.md`)
4. **Threat Modeling**: Identify security risks based on specifications and architecture (see `.github/instructions/threat-modeling.instructions.md`)
5. **TDD Implementation**: Write tests first, then code (see `.github/instructions/tdd-workflow.instructions.md`)
6. **Quality Review**: Validate against checklists (see `.github/instructions/quality-checklists.md`)

**Note**: Threat modeling comes AFTER specifications because you need to know the system architecture, data flows, and integrations before identifying threats.

See `.github/instructions/master-workflow.md` for complete details.

### Quick Start with Workflow Prompts

Use orchestration prompts to automate multi-step workflows:

- **Requirements → Specification**: Execute `.github/prompts/workflow-requirements-to-spec.prompt.md`

  - Generates spec, architecture diagram, threat model (in correct order), runs quality review
  - Usage: `Execute the workflow-requirements-to-spec prompt for docs/requirements/req-{name}.md`

- **Specification → Code**: Execute `.github/prompts/workflow-spec-to-code.prompt.md`
  - Implements with TDD, runs security review, quality validation
  - Usage: `Execute the workflow-spec-to-code prompt for docs/specifications/spec-{name}.md`

See `docs/history/2025-11-09-workflow-usage-guide.md` for step-by-step examples.

## Documentation Commands

The documentation site uses MkDocs and is located in `gardening-docs/`.

### Serve documentation locally

```bash
cd gardening-docs
mkdocs serve
```

### Build documentation site

```bash
cd gardening-docs
mkdocs build
```

### Deploy documentation to GitHub Pages

```bash
cd gardening-docs
mkdocs gh-deploy
```

## Documentation Structure

Located in `gardening-docs/docs/`:

- `index.md` - Project description, stakeholders, original scenarios
- `scope.md` - Context diagrams, use cases, scenarios, scope tree
- `system-requirements.md` - Requirements documentation (in progress)
- `architecture.md` - Functional Flow Block Diagrams (TBD)
- `progress.md` - Current status and next steps
- `resources.md` - Resources used in development

### Key System Features (from requirements)

1. **General User Functions:**

   - Plant search and filtering by zone, type, season, characteristics
   - View plant data (common/scientific name, hardiness zone, spacing, height, container size, companion plants, medicinal benefits)
   - Weather component with alerts and historical data
   - Moon planning for planting
   - Sun angle visualization for bed planning
   - Personal settings (USDA location manual/automated)
   - User plant collections
   - Feedback submission and error reporting

2. **Admin Functions:**

   - Create/manage community leads
   - Account management
   - System permissions

3. **Community Member Functions:**
   - Plot management
   - Team/chore assignments
   - Training modules and progress tracking (for apprentices)
   - Collaboration tools

### User Roles

- **System Users** (general gardeners)
- **Admin** (system administrators)
- **Community Lead** (manages community garden groups)
- **Community Members** (general members, team/chore assigned)
- **Apprentices** (in training program)
- **Supporters** (non-gardeners who help with tasks)

## Key Architecture Concepts

**USDA Hardiness Zones:** Plants are categorized by temperature tolerance zones (1a-13b) which determine what can grow in a location.

**Plant Characteristics:** System tracks extensive plant attributes including:

- Exposure requirements (Full Sun 6+hrs, Partial Sun/Shade, Shade)
- Plant types (Annual, Biennial, Perennial, Shrub, Tree, Vine)
- Growing attributes (drought tolerant, heat tolerant, deer resistant, pollinator friendly, etc.)
- Timing (germination days, days to maturity)
- Physical dimensions (spacing, height, container size)

**Weather Integration:** System will provide location-based weather data and alerts to protect plants.

**Resource Links:** Plants can have associated resources (academic articles, blogs, books, master gardener info, nursery info, YouTube videos).

## Development Notes

- MkDocs configuration in `gardening-docs/mkdocs.yml`
- Documentation references external Google Docs for "full & updated versions" - these are being migrated to MkDocs incrementally
- Current branch is `mkdocs` (main branch is `main`)
- Project uses `pyproject.toml` for dependency management (uv-based ... originally used Python dependencies listed in `requirements.txt`)
- Context diagrams and visuals are linked to Miro board: https://miro.com/app/board/uXjVLFJo2wg=/

## Django Application Architecture (2024-Django-Attempt)

### Directory Structure

- `2024-Django-Attempt/` - Original Django implementation (may be deprecated soon)
  - `config/` - Django project configuration (settings, URLs, WSGI/ASGI)
  - `Plants/` - Main Django app containing plant models and logic
  - `manage.py` - Django management command interface
- `gardening-docs/` - MkDocs system requirements documentation
- `specs/` - Application specifications (new specifications go here)
- `templates/` - Template files for future development

### Core Data Models

The `Plants` app contains the primary data models:

**Plant Model** (`2024-Django-Attempt/Plants/models.py:21-104`):

- Stores comprehensive plant information including common/scientific names, hardiness zones, exposure requirements, physical dimensions, and special attributes
- Uses Django choices for `EXPOSURE_CHOICES`, `TYPE_CHOICES`, and `HARDINESS_ZONES` (1a-13b)
- Boolean flags for plant characteristics (drought tolerant, deer resistant, pollinator friendly, etc.)
- Related to `PlantLink` via many-to-many relationship
- Tracks germination and maturity days

**Profile Model** (`2024-Django-Attempt/Plants/models.py:112-121`):

- OneToOne relationship with Django's User model
- Many-to-many relationship with Plant for user collections
- Methods: `add_plant()`, `remove_plant()`

**PlantLink Model** (`2024-Django-Attempt/Plants/models.py:123-166`):

- Represents external resources linked to plants (articles, videos, books, nursery info)
- Choice field for link types: Academic Article, Blog, Book, Master Gardener, Nursery, YouTube, Other
- Many-to-many relationship with Plant

**Nursery Model** (`2024-Django-Attempt/Plants/models.py:9-18`):

- Stores nursery information with many-to-many to Plant

### Key Architecture Patterns

1. **Hardiness Zone System**: Plant compatibility determined by USDA zones (1a-13b), stored as CharField choices with temperature ranges in both Fahrenheit and Celsius

2. **Plant Characteristics as Boolean Flags**: Extensive use of boolean fields for filtering (is_drought_tolerant, is_deer_resistant, is_pollinator_friendly, etc.)

3. **Exposure Categories**: Five-level categorization from Full Sun (6+ hours) to Shade, stored as 2-character codes

4. **Range-based Physical Attributes**: Min/max fields for spacing and height to accommodate variation

### Django Configuration

- **Project Name**: `config`
- **Database**: SQLite3 (development)
- **Static Files**: Configured for `/static/` URL path
- **Media Files**: Configured for `/media/` URL path
- **Installed Apps**: Standard Django apps + local `Plants` app

## Development Commands

### MkDocs Documentation

```bash
# Serve documentation locally (auto-reload on changes)
cd gardening-docs
mkdocs serve

# Build static site
cd gardening-docs
mkdocs build

# Deploy to GitHub Pages
cd gardening-docs
mkdocs gh-deploy
```

### Django Application (2024-Django-Attempt)

```bash
# Run development server
cd 2024-Django-Attempt
python manage.py runserver

# Create migrations after model changes
cd 2024-Django-Attempt
python manage.py makemigrations

# Apply migrations to database
cd 2024-Django-Attempt
python manage.py migrate

# Create superuser for admin access
cd 2024-Django-Attempt
python manage.py createsuperuser

# Run tests
cd 2024-Django-Attempt
python manage.py test

# Run specific app tests
cd 2024-Django-Attempt
python manage.py test Plants

# Django shell (interactive Python with Django environment)
cd 2024-Django-Attempt
python manage.py shell

# Collect static files for production
cd 2024-Django-Attempt
python manage.py collectstatic
```

### Environment Setup

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

# Deactivate virtual environment
deactivate
```

For detailed setup instructions, see [docs/uvx-setup-guide.md](docs/uvx-setup-guide.md).

## When Working on This Project

1. **Focus on documentation work** - The application code will be rebuilt based on these specs
2. **Follow systems design methodology** - Reference the documentation structure when discussing features
3. **Understand user diversity** - System must serve both novice gardeners and experienced community garden managers
4. **Consider community garden workflows** - Features like plot tracking, team assignments, and training are critical for community members
5. **2024-Django-Attempt is reference only** - This folder contains the original implementation and may be deprecated; use it for understanding existing data models but new development should follow the specifications-based approach
