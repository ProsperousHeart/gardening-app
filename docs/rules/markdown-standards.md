# Markdown Standards

## Purpose

This document defines markdown authoring standards for this project to ensure documentation is portable, maintainable, and easy to navigate.

## Platform-Agnostic Markdown

**Default Principle**: Write markdown using standard CommonMark syntax that works everywhere.

### Standard Features (Always Safe)

Use these features freely - they work in all markdown renderers:

- Headers (`#`, `##`, `###`)
- Lists (ordered and unordered)
- Code blocks with language tags (` ```python `)
- Links and images
- Tables (basic GitHub Flavored Markdown)
- Blockquotes (`>`)
- Bold (`**text**`) and italic (`*text*`)
- Horizontal rules (`---`)

### Tool-Specific Features

**Use tool-specific features ONLY when**:

1. Explicitly configured in `mkdocs.yml`, `docusaurus.config.js`, or similar
2. The document is in a tool-specific directory (e.g., `docs/mkdocs-only/`)
3. The file includes a header comment indicating tool requirements

**Common tool-specific features to avoid by default**:

- Admonitions/callouts (mkdocs: `!!! note`, GitHub: `> [!NOTE]`)
- Custom containers
- Mermaid diagrams without fallback (see exception below)
- Table of contents directives
- Include/import statements

### Exception: Mermaid Diagrams

Mermaid diagrams ARE allowed but MUST follow the three-format rule (see Architecture Diagram Requirements below).

### Making Your Docs Tool-Specific Later

To customize for your documentation tool, add a header comment:

```markdown
<!-- DOCS-TOOL: mkdocs -->
<!-- This file uses MkDocs-specific features -->

# Your Document Title
```

Then enable tool-specific features like:

```markdown
!!! note "MkDocs Admonition"
This uses MkDocs syntax for callouts.

[TOC] <!-- MkDocs table of contents -->
```

## README File Standards

README files serve as **navigation hubs**, not comprehensive documentation.

### README Purpose

1. **Explain the local folder**: What is this directory for?
2. **Link to detailed docs**: Point readers to where they can learn more
3. **Provide quick orientation**: Help readers find what they need fast

### What README Files Should Contain

**✓ DO Include**:

- Brief 1-2 sentence folder purpose
- Directory structure overview (tree or list)
- Links to key documents in the folder
- Links to related documentation elsewhere
- Quick reference tables or lists

**✗ DON'T Include**:

- Detailed explanations (link to docs instead)
- Duplicated content from other files
- Step-by-step tutorials (link to them)
- Full specifications (summarize and link)

### README Template

```markdown
# [Directory Name]

[1-2 sentence description of this directory's purpose]

## Contents

- `file1.md` - [Brief description]
- `file2.md` - [Brief description]
- `subdir/` - [Brief description]

## Key Documents

- **[Document Name](./path/to/doc.md)**: [One-line description]
- **[External Doc](../other/doc.md)**: [One-line description]

## Related Documentation

- See [Project Index](../INDEX.md) for all documentation
- See [Other Relevant Doc](../path/to/doc.md) for [topic]
```

### Example: Good README

```markdown
# Requirements

This directory contains requirement documents that define WHAT to build (not HOW).

## Contents

- `req_user-auth.md` - User authentication system requirements
- `req_api-gateway.md` - API gateway requirements

## Workflow

1. Create requirements using [templates](../templates/requirements-template.md)
2. Generate specifications with `/make-spec-from-req`
3. See [Master Workflow](../../.github/instructions/master-workflow.md) for complete process

## Related

- [Specifications](../specifications/) - Generated from these requirements
- [Template](../templates/requirements-template.md) - For creating new requirements
```

### Example: Bad README (Too Much Detail)

```markdown
# Requirements

Requirements define what to build. They are created by stakeholders...
[500 words of explanation that should be in master-workflow.md]

## How to Write Good Requirements

Requirements should follow these principles:

1. Clear and testable...
   [300 words duplicating content from requirements-template.md]

## Creating a Requirement

First, copy the template...
[Detailed step-by-step that duplicates slash command docs]
```

## Information Architecture

### Single Source of Truth (SSoT)

**Rule**: Every piece of information should have ONE authoritative location.

**How to implement**:

1. **Define the canonical location** for each type of information
2. **Link to it** from everywhere else
3. **Never duplicate** explanatory content

### When to Link vs. Duplicate

**Link when**:

- Explaining a concept or process
- Providing detailed instructions
- Referencing standards or rules
- Pointing to examples

**Duplicate (sparingly) when**:

- Quick reference data (e.g., a 3-row table)
- File paths or names that aid navigation
- Status indicators or metadata
- Information is truly context-dependent

### Cross-Referencing Strategies

**Inline links** for concepts:

```markdown
Follow the [TDD workflow](.github/instructions/tdd-workflow.instructions.md) when implementing.
```

**Reference sections** for multiple related docs:

```markdown
## Related Documentation

- [Master Workflow](../instructions/master-workflow.md) - Complete development process
- [Quality Checklists](../instructions/quality-checklists.md) - Validation criteria
```

**Index files** for comprehensive navigation:

```markdown
See [Documentation Index](./docs/INDEX.md) for all available documentation.
```

### Keeping Documentation Synchronized

**The Problem**: When you update information in one location, related documents may become outdated if they reference that information.

**The Solution**: Follow these practices to maintain consistency:

#### 1. Use Links Instead of Duplication (Primary Strategy)

When information exists in one canonical location, **always link to it** rather than copying it:

```markdown
<!-- ❌ BAD: Duplicating content -->

## Installation

First, install uv:
curl -LsSf https://astral.sh/uv/install.sh | sh

Then activate the environment:
source .venv/bin/activate

<!-- ✅ GOOD: Linking to canonical source -->

## Installation

See [UV Environment Setup](.github/instructions/uv-environment-setup.instructions.md) for installation and activation instructions.
```

**Why this works**: When you update the canonical source, all references automatically point to the latest information.

#### 2. Maintain a Cross-Reference Table

For complex projects, track relationships between documents in a central table:

**Example**: See `docs/SPEC-CROSS-REFERENCE.md` in this project

| Requirement      | Specification     | Code Files | Tests                  | Diagrams                  |
| ---------------- | ----------------- | ---------- | ---------------------- | ------------------------- |
| req_user-auth.md | spec_user-auth.md | src/auth/  | test/test_user-auth.py | architecture_user-auth.md |

**When to update**:

- Adding new requirements → Update table with new row
- Creating specifications → Link to requirement
- Implementing code → Link spec to code files
- Adding diagrams → Link to related spec

**Update checklist** (keep in your table document):

```markdown
## Update Checklist

When updating documentation:

- [ ] Update the canonical source document
- [ ] Check cross-reference table for related documents
- [ ] Update or add cross-reference entry
- [ ] Verify links in related documents still work
- [ ] Update INDEX.md if adding new documents
```

#### 3. Use Automation Where Possible

**Manual approach** (for small projects):

- Keep a checklist in your cross-reference document
- Review related docs when making changes

**Semi-automated approach** (recommended):

- Use `markdown-link-check` to find broken links
- Run link checker in CI/CD pipeline
- Get alerts when links break

**Fully automated approach** (for large projects):

- Use documentation build tools (MkDocs, Docusaurus) that validate links
- Create scripts to update cross-references
- Use git hooks to check documentation consistency

**Example CI check** (`.github/workflows/docs.yml`):

```yaml
name: Documentation Check
on: [push, pull_request]
jobs:
  link-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Check links
        uses: gaurav-nelson/github-action-markdown-link-check@v1
        with:
          config-file: ".markdown-link-check.json"
```

#### 4. Document Update Triggers

In your README files or documentation index, specify when documents need updating:

**Example**:

```markdown
## Maintenance

This document should be updated when:

- New requirements are added to `docs/requirements/`
- Specifications are created or modified
- Code implementation changes architecture
- New diagrams are created

Related documents that may need updates:

- [INDEX.md](./INDEX.md) - Add new document entries
- [SPEC-CROSS-REFERENCE.md](./SPEC-CROSS-REFERENCE.md) - Add relationships
- [Master Workflow](../.github/instructions/master-workflow.md) - If process changes
```

#### 5. Version Control Best Practices

**Commit related documentation together**:

```bash
# ❌ BAD: Update spec without updating related docs
git add docs/specifications/spec-auth.md
git commit -m "Update auth spec"

# ✅ GOOD: Update all related documents in one commit
git add docs/specifications/spec_user-auth.md \
        docs/diagrams/architecture_user-auth.md \
        docs/SPEC-CROSS-REFERENCE.md
git commit -m "Update auth spec and related documentation"
```

**Why**: Atomic commits ensure documentation stays synchronized in version control.

#### 6. Use Templates with Placeholders

Create templates that force you to consider related documents:

**Example template section**:

```markdown
## Related Documentation

<!-- REQUIRED: Update these links when creating this document -->

- **Requirement**: [Link to requirement doc](../requirements/req_REQ-NAME.md)
- **Architecture**: [Link to architecture diagram](../diagrams/architecture_REQ-NAME.md)
- **Threat Model**: [Link to threat model](../diagrams/threat-model_REQ-NAME.md)

<!-- REQUIRED: Add this document to the index -->

- [ ] Added to docs/INDEX.md
- [ ] Added to docs/SPEC-CROSS-REFERENCE.md
```

#### 7. Regular Documentation Audits

Schedule periodic reviews to catch drift:

**Monthly checklist**:

- [ ] Run link checker on all documentation
- [ ] Review cross-reference table for completeness
- [ ] Check for orphaned documents (not linked from anywhere)
- [ ] Verify recent code changes have updated specs
- [ ] Update "Last Updated" dates in index files

**Tools to help**:

- `find docs/ -name "*.md" -mtime +90` - Find docs not modified in 90 days
- `grep -r "TODO" docs/` - Find unfinished documentation
- Link checker tools (see Tools and Linting section)

#### Quick Reference: Update Cascades

When you update X, also check Y:

| You Updated           | Also Check                                       |
| --------------------- | ------------------------------------------------ |
| Requirement           | Specification, Cross-reference table             |
| Specification         | Architecture diagram, Threat model, Related code |
| Code                  | Specification, Tests, Docstrings                 |
| Architecture diagram  | Specification, Threat model                      |
| Workflow instructions | INDEX.md, Related slash commands                 |
| File/folder structure | All README files, INDEX.md                       |

## Architecture Diagram Requirements

**CRITICAL**: All architecture diagrams MUST include THREE formats:

1. **Text Description** - Accessible, search-friendly bullet points or tables
2. **ASCII Diagram** - Platform-agnostic visual using box-drawing characters
3. **Mermaid Code** - In a collapsible `<details>` block for GitHub rendering

### Why Three Formats?

- **Text**: Works everywhere, searchable, accessible to screen readers
- **ASCII**: Visual but platform-agnostic, renders in plain text viewers
- **Mermaid**: Rich visual for tools that support it (GitHub, mkdocs, etc.)

### Format Structure

````markdown
## Architecture Diagram

### Text Description

[Bullet points, tables, or numbered lists describing the architecture]

### ASCII Diagram

[Box-drawing character diagram]

### Mermaid Diagram

<details>
<summary>Click to view Mermaid diagram</summary>

```mermaid
[Mermaid code]
```
````

</details>
```

**See** `.github/instructions/architecture-diagrams.instructions.md` for complete examples and guidance.

## File Organization Best Practices

### Naming Conventions

- Use lowercase with hyphens: `my-document.md` (not `My_Document.md`)
- Prefix related files: `req_feature-name.md`, `spec_feature-name.md`
- Use descriptive names: `user-authentication.md` (not `doc1.md`)

### Directory Structure

```
docs/
├── README.md           # Hub for entire docs/ folder
├── INDEX.md            # Comprehensive documentation index
├── requirements/
│   ├── README.md       # Hub for requirements folder
│   └── req_*.md        # Individual requirements
├── specifications/
│   ├── README.md       # Hub for specifications folder
│   └── spec_*.md       # Individual specifications
└── rules/
    ├── README.md       # Hub for rules folder
    └── *.md            # Individual rule documents (like this file)
```

### Front Matter (Optional)

**What is Front Matter?**

Front matter is metadata placed at the beginning of a markdown file, enclosed in triple dashes (`---`). It provides information about the document to static site generators like Jekyll, Hugo, MkDocs, or Docusaurus.

**Common uses**:

- Page titles and descriptions
- Author information and dates
- Tags and categories for organization
- Custom variables for templates
- SEO metadata

**Example front matter**:

```markdown
---
title: Document Title
description: Brief description for search engines
author: Your Name
date: 2025-11-10
category: Guide
tags: [tag1, tag2]
draft: false
---

# Document Title

Your content here...
```

**Format**: Front matter typically uses YAML syntax, but some tools support JSON or TOML.

**Learn more**:

- [Jekyll Front Matter Guide](https://jekyllrb.com/docs/front-matter/)
- [MkDocs Meta-Data](https://www.mkdocs.org/user-guide/writing-your-docs/#meta-data)
- [Hugo Front Matter](https://gohugo.io/content-management/front-matter/)

**Important**: Front matter is tool-specific! If you use it, mark your file:

```markdown
## <!-- DOCS-TOOL: mkdocs -->

## title: Document Title

# Document Title
```

**Default behavior**: Do NOT add front matter unless you have configured a static site generator for your project.

## Maintenance

### Periodic Review

- Check for broken links (use `markdown-link-check` or similar)
- Identify duplicated content and consolidate
- Update README files when directory structure changes
- Verify cross-references remain accurate

### Deprecation

When retiring a document:

1. Add deprecation notice at the top
2. Link to the replacement document
3. Update all references to point to new location
4. Archive or delete after grace period

```markdown
# [Document Title]

> **DEPRECATED**: This document has been replaced by [New Document](./new-document.md).
> This file will be removed on [DATE].
```

## Tools and Linting

### Recommended Tools

- **Markdown linter**: markdownlint (configurable via `.markdownlint.json`)
- **Link checker**: markdown-link-check
- **Spell checker**: cspell or Vale
- **Formatter**: Prettier with markdown plugin

### Configuration Example

`.markdownlint.json`:

```json
{
  "default": true,
  "line-length": false,
  "no-inline-html": {
    "allowed_elements": ["details", "summary"]
  }
}
```

## Summary

1. **Write platform-agnostic markdown** unless tool-specific features are required
2. **README files are hubs** - link, don't duplicate
3. **Single source of truth** - one canonical location per concept
4. **Keep documentation synchronized** - use links, cross-reference tables, and automation
5. **Three diagram formats** - text, ASCII, and Mermaid (collapsible)
6. **Make it easy to customize** - use comments to mark tool-specific sections

By following these standards, documentation remains portable, maintainable, and accessible across all tools and platforms.