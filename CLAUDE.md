# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a gardening application designed to help new gardeners and community gardeners determine what to plant in their yard. The project is built with Django and is intended to be hosted on Render.

**Key Context:**
- The project originated from a community garden that grows food for local food pantries
- Users range from budding gardeners to master gardeners, including community garden apprentices, supporters, and plot managers
- The system aims to provide plant information, garden planning, weather notifications, and secure collaboration tools for community gardening

## Project Status & Development Approach

**Important:** The `2024-Django-Attempt/` folder contains an original attempt at building the application but will likely be removed soon. The project is now following **specifications-based development** through Cornell's Systems Design certification program.

Current focus is on **systems requirements documentation** in the `gardening-docs/` folder using MkDocs. The documentation represents formal systems design including:
- Context diagrams defining system boundaries and stakeholders
- Use cases and scenarios (23+ scenarios identified)
- Functional Flow Block Diagrams (FFBDs) for architecture
- Use Case Behavior Diagrams (UCBDs)
- Requirements tables and scope trees

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
- Project uses Python dependencies listed in `requirements.txt` (MkDocs-related)
- Context diagrams and visuals are linked to Miro board: https://miro.com/app/board/uXjVLFJo2wg=/

## When Working on This Project

1. **Focus on documentation work** - The application code will be rebuilt based on these specs
2. **Follow systems design methodology** - Reference the documentation structure when discussing features
3. **Understand user diversity** - System must serve both novice gardeners and experienced community garden managers
4. **Consider community garden workflows** - Features like plot tracking, team assignments, and training are critical for community members
