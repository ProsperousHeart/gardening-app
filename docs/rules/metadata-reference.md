# Metadata Reference Guide

## Overview

This document provides a complete reference of all YAML front matter metadata fields used across the project's documentation. All metadata is defined in YAML format at the top of markdown files, enclosed in `---` delimiters.

**Purpose**: Metadata enables tracking, organization, automation, and cross-referencing across requirements, specifications, code, tests, and diagrams.

## Document Types Using Metadata

| Document Type | Location | Metadata Required |
|---------------|----------|-------------------|
| **Requirements** | `docs/requirements/*.md` | ✅ Full metadata + cross-reference |
| **Specifications** | `docs/specifications/*.md` | ✅ Full metadata + cross-reference |
| **Diagrams** | `docs/diagrams/*.md` | ⚠️ Optional (recommended for complex diagrams) |
| **General Docs** | `docs/*.md` | ⚠️ Optional (used by MkDocs) |

## Requirement Document Metadata

**Location**: `docs/requirements/REQ-*.md`

### Complete Example

```yaml
---
# Requirement Metadata
title: Plant Database
description: "Plant database with search and filtering capabilities"
req_id: req-general-user-plant-database
priority: CRITICAL
phase: 1
status: approved
created: 2025-01-15
updated: 2025-12-29
author: Kassandra Keeton
show_badges: true
maps_to_req: "System.GenUser.ViewsAndInsights.PlantDatabase"

# Cross-Reference Tracking (see SPEC-CROSS-REFERENCE.md)
cross_ref_table: ../SPEC-CROSS-REFERENCE.md
specification: ../specifications/spec-plant-database.md
source_files: ["src/plants/models.py", "src/plants/views.py"]
test_files: ["tests/test_plant_model.py", "tests/test_plant_views.py"]
diagrams: ["diagrams/architecture-plant-database.md", "diagrams/threat-model-plant-database.md"]
---
```

### Field Definitions

#### Core Metadata Fields

| Field | Type | Required | Values | Description | Example |
|-------|------|----------|--------|-------------|---------|
| **title** | String | ✅ Yes | Any string | Human-readable feature name | `"Plant Database"` |
| **description** | String | ✅ Yes | Quoted string | Brief description for search/metadata | `"Plant database with search capabilities"` |
| **req_id** | String | ✅ Yes | `req-{subsystem}-{component}` | Unique requirement identifier (filename without .md) | `req-general-user-plant-database` |
| **priority** | String | ✅ Yes | `CRITICAL`, `HIGH`, `MEDIUM`, `LOW` | Business priority level | `CRITICAL` |
| **phase** | Integer | ✅ Yes | `0-7` | Implementation phase (0 = foundational) | `1` |
| **status** | String | ✅ Yes | `draft`, `in-review`, `approved`, `implemented` | Current requirement status | `approved` |
| **created** | Date | ✅ Yes | `YYYY-MM-DD` | Creation date | `2025-01-15` |
| **updated** | Date | ✅ Yes | `YYYY-MM-DD` | Last update date | `2025-12-29` |
| **author** | String | ✅ Yes | Name or handle | Primary author | `Kassandra Keeton` |
| **show_badges** | Boolean | ⚠️ Optional | `true`, `false` | Show priority/phase/status badges | `true` |
| **maps_to_req** | String | ⚠️ Optional | REQ-000 reference | Link to REQ-000 series source | `"System.GenUser.ViewsAndInsights.PlantDatabase"` |

#### Cross-Reference Tracking Fields

| Field | Type | Required | Values | Description | Example |
|-------|------|----------|--------|-------------|---------|
| **cross_ref_table** | String | ✅ Yes | Relative path | Link to cross-reference table | `../SPEC-CROSS-REFERENCE.md` |
| **specification** | String | ✅ Yes | Relative path or `TBD` | Path to generated specification | `../specifications/spec-plant-database.md` |
| **source_files** | Array | ✅ Yes | List of paths or `[]` | Implementation file paths | `["src/plants/models.py"]` |
| **test_files** | Array | ✅ Yes | List of paths or `[]` | Test file paths | `["tests/test_plant_model.py"]` |
| **diagrams** | Array | ✅ Yes | List of paths or `[]` | Related diagram file paths | `["diagrams/architecture-plants.md"]` |

## Specification Document Metadata

**Location**: `docs/specifications/spec-*.md`

### Complete Example

```yaml
---
# Specification Metadata
title: Plant Database Specification
description: "Technical specification for plant database implementation"
spec_id: spec-plant-database
priority: CRITICAL
phase: 1
status: approved
created: 2025-01-20
updated: 2025-12-29
author: Kassandra Keeton
show_badges: true
maps_to_req: ["../requirements/req-general-user-plant-database.md"]

# Cross-Reference Tracking (see SPEC-CROSS-REFERENCE.md)
cross_ref_table: ../SPEC-CROSS-REFERENCE.md
source_files: ["src/plants/models.py", "src/plants/views.py"]
test_files: ["tests/test_plant_model.py", "tests/test_plant_views.py"]
diagrams: ["diagrams/architecture-plant-database.md", "diagrams/threat-model-plant-database.md"]
---
```

### Field Definitions

#### Core Metadata Fields

| Field | Type | Required | Values | Description | Example |
|-------|------|----------|--------|-------------|---------|
| **title** | String | ✅ Yes | Any string | Human-readable specification name | `"Plant Database Specification"` |
| **description** | String | ✅ Yes | Quoted string | Brief description | `"Technical specification for plant database"` |
| **spec_id** | String | ✅ Yes | `spec-{name}` | Unique specification identifier | `spec-plant-database` |
| **priority** | String | ✅ Yes | `CRITICAL`, `HIGH`, `MEDIUM`, `LOW` | Business priority (inherited from requirement) | `CRITICAL` |
| **phase** | Integer | ✅ Yes | `0-7` | Implementation phase | `1` |
| **status** | String | ✅ Yes | `draft`, `in-review`, `approved`, `implemented` | Current specification status | `approved` |
| **created** | Date | ✅ Yes | `YYYY-MM-DD` | Creation date | `2025-01-20` |
| **updated** | Date | ✅ Yes | `YYYY-MM-DD` | Last update date | `2025-12-29` |
| **author** | String | ✅ Yes | Name or handle | Primary author | `Kassandra Keeton` |
| **show_badges** | Boolean | ⚠️ Optional | `true`, `false` | Show priority/phase/status badges | `true` |
| **maps_to_req** | Array | ✅ Yes | List of requirement paths | Links to source requirements | `["../requirements/req-general-user-plant-database.md"]` |

#### Cross-Reference Tracking Fields

| Field | Type | Required | Values | Description | Example |
|-------|------|----------|--------|-------------|---------|
| **cross_ref_table** | String | ✅ Yes | Relative path | Link to cross-reference table | `../SPEC-CROSS-REFERENCE.md` |
| **source_files** | Array | ✅ Yes | List of paths or `[]` | Implementation file paths | `["src/plants/models.py"]` |
| **test_files** | Array | ✅ Yes | List of paths or `[]` | Test file paths | `["tests/test_plant_model.py"]` |
| **diagrams** | Array | ✅ Yes | List of paths or `[]` | Related diagram file paths | `["diagrams/architecture-plants.md"]` |

## Field Value Reference

### Priority Values

| Value | Meaning | Use When |
|-------|---------|----------|
| `CRITICAL` | Must have for MVP, blocks other work | Core functionality, foundational features |
| `HIGH` | Important for initial release | Key features, major improvements |
| `MEDIUM` | Should have but not blocking | Nice-to-have features, enhancements |
| `LOW` | Could have, deferred to later | Future enhancements, edge cases |

### Phase Values

| Phase | Description | Examples |
|-------|-------------|----------|
| `0` | Foundational documents | REQ-000 series (General, Scope, Use Cases, etc.) |
| `1` | Core MVP features | User authentication, plant database |
| `2` | Essential features | Search, filtering, weather integration |
| `3` | Important enhancements | Community garden features |
| `4` | Nice-to-have features | Advanced filtering, recommendations |
| `5` | Future enhancements | Mobile app, offline mode |
| `6` | Optional features | Gamification, social features |
| `7` | Deferred/Research | Experimental features |

### Status Values

| Value | Meaning | Requirement Stage | Specification Stage | Implementation Stage |
|-------|---------|-------------------|---------------------|----------------------|
| `draft` | Work in progress | Initial draft | Spec being written | Not started |
| `in-review` | Under review | Stakeholder review | Tech review | Code review |
| `approved` | Ready for next stage | Ready for spec | Ready to implement | Ready to deploy |
| `implemented` | Complete | N/A (stays approved) | Code written | Deployed |

## Metadata Lifecycle

### Requirement Lifecycle

1. **Creation** (status: `draft`)
   ```yaml
   status: draft
   specification: TBD
   source_files: []
   test_files: []
   diagrams: []
   ```

2. **After Review** (status: `in-review` → `approved`)
   ```yaml
   status: approved
   updated: 2025-12-29
   ```

3. **After Spec Generation** (`/make-spec-from-req`)
   ```yaml
   specification: ../specifications/spec-feature.md
   diagrams: ["diagrams/architecture-feature.md", "diagrams/threat-model-feature.md"]
   updated: 2025-12-29
   ```

4. **After Implementation**
   ```yaml
   source_files: ["src/feature.py"]
   test_files: ["tests/test_feature.py"]
   updated: 2025-12-29
   ```

### Specification Lifecycle

1. **Creation** (generated from requirement)
   ```yaml
   status: draft
   maps_to_req: ["../requirements/req-feature.md"]
   source_files: []
   test_files: []
   diagrams: ["diagrams/architecture-feature.md", "diagrams/threat-model-feature.md"]
   ```

2. **After Review** (status: `approved`)
   ```yaml
   status: approved
   updated: 2025-12-29
   ```

3. **After Implementation** (status: `implemented`)
   ```yaml
   status: implemented
   source_files: ["src/feature.py"]
   test_files: ["tests/test_feature.py"]
   updated: 2025-12-29
   ```

## Best Practices

### 1. Always Update `updated` Field

When making ANY change to a document:
```yaml
updated: 2025-12-29  # Today's date
```

### 2. Keep Cross-References Bidirectional

When requirement links to spec, spec must link back:

**Requirement**:
```yaml
specification: ../specifications/spec-feature.md
```

**Specification**:
```yaml
maps_to_req: ["../requirements/req-feature.md"]
```

### 3. Use Relative Paths

Always use relative paths for portability:
- ✅ `../specifications/spec-feature.md`
- ❌ `/docs/specifications/spec-feature.md`
- ❌ `D:\Programming\Code\gardening-app\docs\specifications\spec-feature.md`

### 4. Maintain Empty Arrays vs TBD

- Use `TBD` for single-value fields that will be filled later:
  ```yaml
  specification: TBD
  ```

- Use empty arrays `[]` for list fields:
  ```yaml
  source_files: []
  diagrams: []
  ```

### 5. Quote String Values

Always quote string values to avoid YAML parsing issues:
```yaml
description: "This is a description"  # ✅ Good
title: "Plant Database"                # ✅ Good
```

### 6. Comment Changes

Add comments to explain priority/status changes:
```yaml
priority: HIGH  # Changed from CRITICAL on 2025-12-29 (plant database completed)
```

## Querying Metadata

### Find Requirements by Priority

```bash
# Find all CRITICAL requirements
grep -l 'priority: CRITICAL' docs/requirements/REQ-*.md

# Find all HIGH priority requirements
grep -l 'priority: HIGH' docs/requirements/REQ-*.md
```

### Find Requirements by Phase

```bash
# Find all Phase 1 requirements
grep -l 'phase: 1' docs/requirements/REQ-*.md
```

### Find Requirements by Status

```bash
# Find all approved requirements
grep -l 'status: approved' docs/requirements/REQ-*.md

# Find all draft requirements
grep -l 'status: draft' docs/requirements/REQ-*.md
```

### Find Requirements Without Specs

```bash
# Find requirements that don't have specs yet
grep -l "specification: TBD" docs/requirements/REQ-*.md
```

### Find Implemented Features

```bash
# Find specifications with implementations
grep -l "status: implemented" docs/specifications/spec-*.md
```

## MkDocs Integration

### Accessing Metadata in Templates

MkDocs makes metadata available via `page.meta`:

```jinja
<!-- Display priority badge -->
{% if page.meta.priority %}
<span class="priority-{{ page.meta.priority | lower }}">
  {{ page.meta.priority }}
</span>
{% endif %}

<!-- Display specification link -->
{% if page.meta.specification and page.meta.specification != "TBD" %}
**Specification**: [View Spec]({{ page.meta.specification }})
{% endif %}

<!-- List implementation files -->
{% if page.meta.source_files %}
**Implementation**:
{% for file in page.meta.source_files %}
- `{{ file }}`
{% endfor %}
{% endif %}
```

### Custom Macros

You can create MkDocs macros to display metadata:

```python
# In mkdocs.yml or custom plugin
def render_metadata(page):
    if not page.meta:
        return ""

    html = "<div class='metadata'>"
    html += f"<p><strong>Priority:</strong> {page.meta.get('priority', 'N/A')}</p>"
    html += f"<p><strong>Phase:</strong> {page.meta.get('phase', 'N/A')}</p>"
    html += f"<p><strong>Status:</strong> {page.meta.get('status', 'N/A')}</p>"
    html += "</div>"
    return html
```

## Validation

### Required Field Checklist

Before committing a requirement or specification, verify:

- [ ] `title` is descriptive and unique
- [ ] `description` is clear and concise
- [ ] `req_id` or `spec_id` matches filename
- [ ] `priority` is one of: CRITICAL, HIGH, MEDIUM, LOW
- [ ] `phase` is between 0-7
- [ ] `status` is one of: draft, in-review, approved, implemented
- [ ] `created` date is in YYYY-MM-DD format
- [ ] `updated` date is today's date (if modified)
- [ ] `cross_ref_table` points to ../SPEC-CROSS-REFERENCE.md
- [ ] All array fields use `[]` not empty strings

### Automated Validation (Future)

Consider creating a pre-commit hook to validate metadata:

```bash
#!/bin/bash
# .git/hooks/pre-commit

for file in docs/requirements/REQ-*.md docs/specifications/spec-*.md; do
    # Check for required fields
    if ! grep -q "^title:" "$file"; then
        echo "ERROR: $file missing 'title' field"
        exit 1
    fi
    # Add more validation checks...
done
```

## Related Documentation

- **[Cross-Reference Usage Guide](./cross-reference-usage-guide.md)** - How to use cross-reference fields
- **[Requirement Metadata Guide](./requirement-metadata-guide.md)** - Detailed guide for requirements
- **[Markdown Standards](./markdown-standards.md)** - Documentation standards
- **[SPEC-CROSS-REFERENCE.md](../SPEC-CROSS-REFERENCE.md)** - Central tracking table

## Quick Reference Card

### Requirement Template

```yaml
---
title: Feature Name
description: "Brief description"
req_id: req-subsystem-component
priority: CRITICAL | HIGH | MEDIUM | LOW
phase: 1-7
status: draft | in-review | approved | implemented
created: YYYY-MM-DD
updated: YYYY-MM-DD
author: Your Name
show_badges: true
maps_to_req: "REQ-000 reference"

cross_ref_table: ../SPEC-CROSS-REFERENCE.md
specification: TBD
source_files: []
test_files: []
diagrams: []
---
```

### Specification Template

```yaml
---
title: Feature Specification
description: "Brief description"
spec_id: spec-feature-name
priority: CRITICAL | HIGH | MEDIUM | LOW
phase: 1-7
status: draft | in-review | approved | implemented
created: YYYY-MM-DD
updated: YYYY-MM-DD
author: Your Name
show_badges: true
maps_to_req: ["../requirements/req-feature.md"]

cross_ref_table: ../SPEC-CROSS-REFERENCE.md
source_files: []
test_files: []
diagrams: []
---
```
