# Requirement Metadata Management Guide

## Overview

All requirement files use **YAML front matter** to track metadata like priority, phase, and status. This metadata is separate from the file content, making it safe to update independently.

## Metadata Structure

```yaml
---
title: "Plant Database"
req_id: "req-general-user-plant-database"
priority: "CRITICAL"
phase: "1"
status: "approved"
created: "2025-01-15"
updated: "2025-01-20"
author: "Your Name"
maps_to_req000: "System.GenUser.ViewsAndInsights.PlantDatabase"
---
```

## Metadata Fields

| Field | Description | Values | Example |
|-------|-------------|--------|---------|
| **title** | Human-readable feature name | Any string | `"Plant Database"` |
| **req_id** | Filename without .md extension | `req-{subsystem}-{component}` | `req-general-user-plant-database` |
| **priority** | Business priority level | `CRITICAL`, `HIGH`, `MEDIUM`, `LOW` | `CRITICAL` |
| **phase** | Implementation phase (1-7) | `1` through `7` | `1` |
| **status** | Current requirement status | `draft`, `in-review`, `approved`, `implemented` | `approved` |
| **created** | Creation date | `YYYY-MM-DD` | `2025-01-15` |
| **updated** | Last update date | `YYYY-MM-DD` | `2025-01-20` |
| **author** | Primary author | Name or handle | `Kassandra Keeton` |
| **maps_to_req000** | Link to REQ-000b scope | REQ-000b reference | `System.GenUser.ViewsAndInsights.PlantDatabase` |

### Cross-Reference Tracking Fields

| Field | Description | Values | Example |
|-------|-------------|--------|---------|
| **cross_ref_table** | Link to cross-reference table | Relative path | `../SPEC-CROSS-REFERENCE.md` |
| **specification** | Path to generated spec file | Relative path or `TBD` | `../specifications/spec-plant-database.md` |
| **source_files** | Implementation file paths | YAML list | `["src/plants/models.py"]` |
| **test_files** | Test file paths | YAML list | `["tests/test_plant_model.py"]` |
| **diagrams** | Related diagram file paths | YAML list | `["diagrams/architecture-plants.md"]` |

## Cross-Reference Tracking Usage

### Purpose

Cross-reference fields enable bidirectional traceability between requirements, specifications, code, tests, and diagrams. This ensures:
- **Traceability**: Follow a requirement from concept through implementation
- **Completeness**: Verify all requirements have specs, code, and tests
- **Maintenance**: Update related documents when changes occur

### When to Update Cross-Reference Fields

| Lifecycle Event | Update These Fields | Example |
|----------------|---------------------|---------|
| **Creating requirement** | `cross_ref_table` (always `../SPEC-CROSS-REFERENCE.md`) | Initial file creation |
| **Generating specification** | `specification` (path to generated spec) | After `/make-spec-from-req` |
| **Creating diagrams** | `diagrams` (add diagram path to list) | After architecture/threat model creation |
| **Implementing code** | `source_files` (add implementation paths) | When writing actual code |
| **Writing tests** | `test_files` (add test file paths) | When creating test files |
| **Any update** | `updated` (today's date) | Every change to the file |

### Updating Cross-Reference Fields

**Example workflow**:

```yaml
# Initial requirement (newly created)
specification: TBD
source_files: []
test_files: []
diagrams: []

# After running /make-spec-from-req
specification: ../specifications/spec-plant-database.md
diagrams: ["diagrams/architecture-plant-database.md", "diagrams/threat-model-plant-database.md"]

# After implementation
specification: ../specifications/spec-plant-database.md
source_files: ["src/plants/models.py", "src/plants/views.py"]
test_files: ["tests/test_plant_model.py", "tests/test_plant_views.py"]
diagrams: ["diagrams/architecture-plant-database.md", "diagrams/threat-model-plant-database.md"]
```

### Accessing Cross-Reference Data in MkDocs

You can use these fields in MkDocs templates:

```jinja
<!-- Display related specification -->
{% if page.meta.specification and page.meta.specification != "TBD" %}
**Specification**: [{{ page.meta.specification }}]({{ page.meta.specification }})
{% endif %}

<!-- List implementation files -->
{% if page.meta.source_files %}
**Implementation**:
{% for file in page.meta.source_files %}
- `{{ file }}`
{% endfor %}
{% endif %}
```

## How to Update Priority Safely

### Method 1: Edit Only the YAML Section

When updating priority, **only modify lines 1-15** (the YAML front matter):

```yaml
---
# Change this line only:
priority: "HIGH"  # Changed from CRITICAL to HIGH
# Leave everything else unchanged
---
```

The rest of the document (lines 16+) remains untouched.

### Method 2: Use Search & Replace

To change priority across multiple files:

```bash
# Find all files with CRITICAL priority
grep -r "priority: \"CRITICAL\"" docs/requirements/req-*.md

# Replace priority in specific file
sed -i 's/priority: "CRITICAL"/priority: "HIGH"/' docs/requirements/req-general-user-weather.md
```

### Method 3: Use a Script

Create a script to update priority systematically:

```bash
#!/bin/bash
# update-priority.sh
REQ_FILE=$1
NEW_PRIORITY=$2

# Update only the priority line
sed -i "s/^priority: \".*\"/priority: \"$NEW_PRIORITY\"/" "$REQ_FILE"

# Update the 'updated' field
TODAY=$(date +%Y-%m-%d)
sed -i "s/^updated: \".*\"/updated: \"$TODAY\"/" "$REQ_FILE"

echo "Updated $REQ_FILE to priority: $NEW_PRIORITY"
```

Usage:
```bash
./update-priority.sh docs/requirements/req-general-user-weather.md HIGH
```

## Protection Against Overwrites

### Why This Prevents Accidental Overwrites

1. **Metadata is isolated**: Lines 1-15 contain ONLY metadata
2. **Content is separate**: Lines 16+ contain the actual requirements
3. **Visual separation**: The `---` markers make it obvious where metadata ends
4. **Editor support**: Most editors highlight YAML front matter differently

### Example: Updating Content Without Touching Priority

```markdown
---
priority: "CRITICAL"  # ← THIS LINE STAYS UNCHANGED
updated: "2025-01-20" # ← Update this when content changes
---

# Requirements Template

## Context
### Purpose
- [UPDATE YOUR CONTENT HERE]  # ← Content changes happen here
```

When you edit content (lines 16+), the priority (line 8) remains unchanged unless you specifically modify it.

## Querying Metadata

### Find All Requirements by Priority

```bash
# Find all CRITICAL requirements
grep -l 'priority: "CRITICAL"' docs/requirements/req-*.md

# Find all HIGH priority requirements
grep -l 'priority: "HIGH"' docs/requirements/req-*.md
```

### List Requirements by Phase

```bash
# Find all Phase 1 requirements
grep -l 'phase: "1"' docs/requirements/req-*.md
```

### Generate Priority Report

```bash
#!/bin/bash
# priority-report.sh

echo "=== Requirement Priority Report ==="
echo ""

for priority in CRITICAL HIGH MEDIUM LOW; do
    echo "### $priority Priority:"
    grep -l "priority: \"$priority\"" docs/requirements/req-*.md | while read file; do
        title=$(grep "^title:" "$file" | cut -d'"' -f2)
        echo "  - $title ($(basename $file))"
    done
    echo ""
done
```

## MkDocs Integration

MkDocs automatically reads YAML front matter and makes it available in templates:

```jinja
<!-- In MkDocs template -->
<h1>{{ page.meta.title }}</h1>
<div class="priority priority-{{ page.meta.priority | lower }}">
    Priority: {{ page.meta.priority }}
</div>
```

You can even create a plugin to:
- Show priority badges on pages
- Filter requirements by priority
- Generate priority-sorted lists

## Best Practices

### 1. Always Update the `updated` Field

When making ANY change to a requirement file, update the `updated` field:

```yaml
updated: "2025-01-27"  # Today's date
```

### 2. Use Comments to Track Priority Changes

Add comments in the metadata to track why priority changed:

```yaml
priority: "HIGH"  # Changed from CRITICAL on 2025-01-27 (plant database completed)
```

### 3. Review Priority During Sprint Planning

Create a habit of reviewing priority during sprint/phase planning:

```bash
# Generate priority report before sprint planning
./priority-report.sh > sprint-priorities.md
```

### 4. Link Priority to Phase

Keep priority and phase aligned:

- **Phase 1-2**: Usually `CRITICAL` or `HIGH` priority
- **Phase 3-4**: Usually `HIGH` or `MEDIUM` priority
- **Phase 5-6**: Usually `MEDIUM` priority
- **Phase 7**: Usually `LOW` priority (deferred)

### 5. Document Priority Decisions

Add a note in the requirement explaining why it has its priority:

```markdown
## Context

### Priority Justification

This requirement has **CRITICAL** priority because:
- All other features depend on plant data existing
- Provides immediate value to users
- Required for MVP
```

## Version Control Tips

### Git Diff Shows Metadata Changes Clearly

```diff
--- a/docs/requirements/req-general-user-weather.md
+++ b/docs/requirements/req-general-user-weather.md
@@ -1,7 +1,7 @@
 ---
 title: "Weather Integration"
 req_id: "req-general-user-weather"
-priority: "CRITICAL"
+priority: "HIGH"
 phase: "3"
-updated: "2025-01-15"
+updated: "2025-01-27"
 ---
```

### Commit Message Convention

When changing priority:

```bash
git commit -m "docs: Update req-general-user-weather priority to HIGH

Plant database is now complete, so weather integration is no longer
blocking other work. Reduced from CRITICAL to HIGH priority."
```

## Automation Opportunities

### Pre-commit Hook

Create a pre-commit hook to validate metadata:

```bash
#!/bin/bash
# .git/hooks/pre-commit

for file in docs/requirements/req-*.md; do
    if ! grep -q "^priority: " "$file"; then
        echo "ERROR: $file missing priority field"
        exit 1
    fi

    if ! grep -q "^updated: " "$file"; then
        echo "ERROR: $file missing updated field"
        exit 1
    fi
done
```

### GitHub Action

Create an action to generate priority reports on PR:

```yaml
name: Priority Report
on: [pull_request]
jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Generate Report
        run: |
          ./scripts/priority-report.sh > priority-report.md
          gh pr comment ${{ github.event.number }} --body-file priority-report.md
```

## Summary

✅ **Metadata is isolated** - Priority lives in YAML front matter (lines 1-15)
✅ **Content is separate** - Requirements content starts at line 16+
✅ **Easy to query** - Use grep/sed to find and update priorities
✅ **Version control friendly** - Changes show clearly in git diff
✅ **MkDocs compatible** - Automatic integration with documentation site
✅ **No overwrites** - Update priority independently of content

**Key Takeaway**: When you update requirement content, the priority metadata stays safe in the YAML front matter unless you explicitly change it.
