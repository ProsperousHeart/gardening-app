# Requirements Directory

This directory is where you should save all the requirements documents created for the project.

!!! info "Full Version Available"

Current full & updated version of this page is currently in the works & can be found <a href="https://docs.google.com/document/d/1decYpeZlxtQeLBvPupJ2VFWPRHVlUZnn/edit?usp=sharing&ouid=114844884846337292418&rtpof=true&sd=true" target="_blank">here</a>. And as of 20251226, this should be converted in it's entirety to this site. You are welcome to peruse this to see it's original documentation state, but it is a much better experience viewing it through this site instead.

<!-- <iframe src="https://docs.google.com/document/d/1decYpeZlxtQeLBvPupJ2VFWPRHVlUZnn/edit?usp=sharing&ouid=114844884846337292418&rtpof=true&sd=true" width="100%" height="600px"></iframe> -->

## Purpose

- Store requirements crafted by humans (all **REQ-000** files) as machine readable markdown files
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

**IMPORTANT**: All new requirement files must follow this naming pattern:

```
req-{subsystem}-{component}.md
```

**Examples:**
- `req-general-user-plant-database.md`
- `req-general-user-weather.md`
- `req-community-member-announcements.md`
- `req-admin-account-management.md`

**Why this format:**
- ✅ Clear subsystem identification (general-user, community-member, admin)
- ✅ Component name describes functionality
- ✅ **No priority in filename** - priority is tracked in YAML front matter (see below)
- ✅ Allows priorities to change without renaming files

**Old naming patterns** (deprecated):
- ~~`user-authentication.md`~~ ❌ Use `req-general-user-authentication.md` ✅
- ~~`req-01-plant-database.md`~~ ❌ Priority should not be in filename

## YAML Front Matter (Required)

**CRITICAL**: Every requirement file MUST start with YAML front matter containing metadata:

```yaml
---
# Requirement Metadata
title: "Plant Database"
req_id: "req-general-user-plant-database"
priority: "CRITICAL | HIGH | MEDIUM | LOW"
phase: "1-7"
status: "draft | in-review | approved | implemented"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
author: "Your Name"
maps_to_req000: "[REQ-000b section reference]"
---
```

**This metadata enables:**
- 🎨 **Priority badges** on the documentation site (color-coded by priority)
- 📊 **Automatic sorting** and filtering of requirements
- 📈 **Progress tracking** by phase and status
- 🔍 **Quick searches** by priority, phase, or status

**See:**
- [Requirement Metadata Management Guide](../rules/requirement-metadata-guide.md) - Complete guide
- [Priority Badges Visual Demo](../tutorials/mkdocs/priority-badges-visual-demo.md) - See how badges look
- [Priority Badges Setup](../tutorials/mkdocs/priority-badges-setup.md) - Technical details

## What Goes in a Requirements Document

Each requirements document should follow the template structure and include:

- **YAML Front Matter** (REQUIRED - see above)
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
