---
title: Dynamic Index Generation Tutorial
author: Kassandra Keeton
description:  "Tutorial on how to automatically generate an index of requirement or specification files."
created: 2025-12-30
updated: 2025-12-30
phase: 0
status: draft
show_badges: false  # set to "false" to disable badges
---
# Dynamic Index Generation for MkDocs

**Purpose:** Automatically generate and update requirement/specification index pages

## Overview

This tutorial explains how to set up dynamic index generation for documentation using [MkDocs hooks](https://www.mkdocs.org/user-guide/configuration/#hooks), [Python](https://www.python.org/) scripts, and [Jinja2](https://jinja.palletsprojects.com/en/stable/) templates. This system automatically regenerates index pages whenever you build your MkDocs site, ensuring your documentation stays synchronized with your requirement files.

### What You'll Learn

- How to create MkDocs hooks that run before builds
- How to extract YAML front matter from markdown files
- How to generate markdown files from Jinja2 templates
- How to create component-specific filtered indexes
- Common pitfalls and how to avoid them

### Use Cases

- **Requirements indexes**: Auto-generate tables of all requirements
- **Specification indexes**: Auto-generate lists of technical specs
- **API documentation**: Auto-generate API reference pages
- **Any structured documentation**: Automatically build navigation pages from front matter

## Architecture

<div class="ascii-art">
```
┌─────────────────────────────────────────────────────────────┐
│                    MkDocs Build Process                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   MkDocs Hook (on_pre_build)                │
│              docs/hooks/generate_req_index.py               │
│   • Triggered before MkDocs processes files                 │
│   • Calls the generation script                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              Generation Script (Python)                     │
│          scripts/generate-req-index_UPDATE.py               │
│   • Scans directories for markdown files                    │
│   • Extracts YAML front matter                              │
│   • Validates metadata                                      │
│   • Sorts and filters requirements                          │
│   • Renders Jinja2 templates                                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              Jinja2 Template                                │
│      scripts/templates/requirements-index.jinja2            │
│   • Defines structure of generated pages                    │
│   • Handles empty states                                    │
│   • Includes filtering UI                                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌────────────────────────────────────────────────────────────────┐
│              Generated Index Files                             │
│   • docs/requirements/req-index.md (main)                      │
│   • docs/requirements/GenUser/genuser-index.md                 │
│   • docs/requirements/UserMgmt/usermgmt-index.md               │
│   • docs/requirements/CommunityMember/communitymember-index.md │
└────────────────────────────────────────────────────────────────┘
```
</div>

## Implementation Steps

### Step 1: Create the MkDocs Hook

MkDocs hooks run at specific points in the build process. We use [`on_pre_build`](https://www.mkdocs.org/dev-guide/plugins/#config) to generate indexes before MkDocs processes the files.

**File:** `docs/hooks/generate_req_index.py`

```python
"""MkDocs hook to auto-generate requirements index before build."""

import subprocess  # nosec B404 - subprocess used safely with hardcoded, controlled inputs only
import sys
from pathlib import Path


def safe_print(message):
    """Print with encoding error handling for Windows console."""
    try:
        print(message)
    except UnicodeEncodeError:
        # Fallback to ASCII-safe output if console doesn't support Unicode
        print(message.encode('ascii', errors='replace').decode('ascii'))


def on_pre_build(config):
    """Run before MkDocs build starts."""
    script_path = Path("scripts/generate-req-index_UPDATE.py")

    if script_path.exists():
        safe_print("🔄 Generating requirements index...")
        try:
            # Safe: script_path is hardcoded, sys.executable is controlled, no user input
            subprocess.run([sys.executable, str(script_path)], check=True)  # nosec B603
            safe_print("✅ Requirements index generated successfully")
        except subprocess.CalledProcessError as e:
            safe_print(f"❌ Failed to generate requirements index: {e}")
            # Don't fail the build, just warn
    else:
        safe_print(f"⚠️  Script not found: {script_path}")
```

**Register the hook in `mkdocs.yml`:**

```yaml
# Hooks for custom processing
hooks:
  - docs/hooks/priority_badges.py
  - docs/hooks/generate_req_index.py  # Auto-generate requirements index before build
```

### Step 2: Create the Generation Script

The script scans directories, extracts metadata, and generates indexes.

**File:** `scripts/generate-req-index_UPDATE.py`

Key functions:

```python
def extract_metadata_from_file(file_path: Path) -> Optional[Dict]:
    """Extract and validate YAML front matter from a requirement file."""
    # Read file
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract YAML front matter (content between --- markers)
    if not content.startswith("---"):
        return None

    yaml_end = content.find("---", 3)
    if yaml_end == -1:
        return None

    yaml_content = content[3:yaml_end]

    # Parse YAML safely
    metadata = yaml.safe_load(yaml_content)

    # Validate metadata
    if not validate_requirement_metadata(metadata):
        return None

    return metadata
```

```python
def scan_requirements(base_dir: Path, req_id_filter: Optional[str] = None) -> List[Dict]:
    """Scan directory for requirement files and extract metadata.

    Args:
        base_dir: Base directory to scan
        req_id_filter: Optional filter (e.g., "req-genuser") to only include
                      requirements where req_id starts with this value
    """
    requirements = []

    for req_file in scan_dir.rglob("*.md"):
        # Skip index files and examples
        if req_file.name.lower() in ("index.md", "readme.md", "req-index.md"):
            continue

        # Extract metadata
        metadata = extract_metadata_from_file(req_file)
        if not metadata:
            continue

        # Apply filter if specified
        req_id = metadata.get("req_id", "")
        if req_id_filter and not req_id.startswith(req_id_filter):
            continue

        requirements.append({
            "file_path": str(req_file.relative_to(link_base)),
            "title_clean": clean_title(metadata.get("title")),
            "priority": metadata.get("priority"),
            "phase": int(metadata.get("phase")),
            "status": metadata.get("status"),
            "req_id": req_id,
        })

    # Sort by phase, then priority
    priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    requirements.sort(
        key=lambda r: (r["phase"], priority_order.get(r["priority"], 4))
    )

    return requirements
```

```python
def generate_component_indexes() -> bool:
    """Generate component-specific requirement indexes."""
    base_dir = Path("docs/requirements")

    # Find component subdirectories
    for component_dir in base_dir.iterdir():
        if not component_dir.is_dir():
            continue

        # Skip hidden/special directories
        if component_dir.name.startswith((".", "_")) or component_dir.name in ("for-sdd",):
            continue

        # Determine filter (e.g., "req-genuser")
        component_name = component_dir.name.lower()
        req_id_filter = f"req-{component_name}"

        # Scan for matching requirements
        requirements = scan_requirements(base_dir, req_id_filter=req_id_filter)

        # Generate index (even if empty)
        index_path = component_dir / f"{component_name}-index.md"
        generate_index_from_template(
            output_path=index_path,
            title=f"{component_dir.name} Requirements",
            requirements=requirements,
            component_name=component_dir.name,  # Preserve CamelCase
        )
```

### Step 3: Create the Jinja2 Template

Templates define the structure of generated pages.

**File:** `scripts/templates/requirements-index.jinja2`

{% raw %}
```jinja2
---
hide:
  - toc
---

# {{ title | trim }}

{% if component_name %}
## About {{ component_name }} Component

This section contains requirements specific to the **{{ component_name }}** subsystem.

**Naming Convention:**

- **File name**: `req-{{ component_name | lower }}-[component-name].md`
- **req_id**: `req-{{ component_name | lower }}-[component-name]`
- **Example**: `req-{{ component_name | lower }}-plant-database.md`

## Related Requirements

See [Main Requirements Index](../req-index.md) for all project requirements.
{% endif %}

## Requirements Table

<div class="req-index-controls" markdown="1">
  <div class="req-filters">
    <input type="text" id="req-search" placeholder="Search requirements..." />
    <select id="phase-filter">
      <option value="">All Phases</option>
{%- for phase in phases | sort %}
      <option value="{{ phase }}">Phase {{ phase }}</option>
{%- endfor %}
    </select>
    <select id="priority-filter">
      <option value="">All Priorities</option>
      <option value="CRITICAL">Critical</option>
      <option value="HIGH">High</option>
      <option value="MEDIUM">Medium</option>
      <option value="LOW">Low</option>
    </select>
  </div>
</div>

<table id="requirements-table" class="requirements-table">
  <thead>
    <tr>
      <th class="sortable" data-sort="priority">Priority</th>
      <th class="sortable" data-sort="phase">Phase</th>
      <th class="sortable" data-sort="docnum">Doc Number</th>
      <th class="sortable" data-sort="title">Title</th>
    </tr>
  </thead>
  <tbody>
{%- for req in requirements %}
    <tr data-phase="{{ req.phase }}" data-priority="{{ req.priority }}">
      <td><span class="priority-badge priority-{{ req.priority | lower }}">{{ req.priority }}</span></td>
      <td>{{ req.phase }}</td>
      <td>{{ req.doc_number }}</td>
      <td><a href="{{ req.file_path }}">{{ req.title_clean }}</a></td>
    </tr>
{%- endfor %}
  </tbody>
</table>

{% if requirements | length == 0 %}
!!! info "No Requirements Found"
    No requirements matching the filter criteria were found. Requirements will appear here once they are created.
{% endif %}
```
{% endraw %}

### Step 4: Update Navigation

**In `mkdocs.yml`:**

```yaml
nav:
  - System Requirements:
    - Requirements by Subsystem:
      - requirements/req-by-subsys-idx.md
      - General User Access: requirements/GenUser/genuser-index.md
      - User Management: requirements/UserMgmt/usermgmt-index.md
      - Community Garden Member Access: requirements/CommunityMember/communitymember-index.md
```

**In `docs/requirements/req-by-subsys-idx.md`:**

```markdown
# Requirements by Subsystem

1. General User ([GenUser](./GenUser/genuser-index.md))
2. Elevated Privileges ([UserMgmt](./UserMgmt/usermgmt-index.md))
3. Community Garden Member ([CommunityMember](./CommunityMember/communitymember-index.md))
```

## Common Pitfalls and Solutions

### ❌ Pitfall 1: Checking if Index Exists Before Generating

**Problem:**

```python
# BAD: Only generates if index already exists
if not index_path.exists():
    continue  # Skip generation
```

**Why it's wrong:** If someone deletes the index file, it will never be regenerated (chicken-and-egg problem).

**Solution:**

```python
# GOOD: Generate based on whether requirements exist
requirements = scan_requirements(base_dir, req_id_filter)

if not requirements:
    print(f"No requirements found for {component_name}, generating empty index...")

# Always generate the index
generate_index_from_template(...)
```

### ❌ Pitfall 2: Incorrect Case Handling

**Problem:**

{% raw %}
```jinja2
{# BAD: title filter converts to "Genuser" instead of "GenUser" #}
{{ component_name | title }}
```
{% endraw %}

**Why it's wrong:** The `title` filter capitalizes the first letter of each word but lowercases the rest.

**Solution:**

```python
# Pass the CamelCase directory name directly
generate_index_from_template(
    component_name=component_dir.name,  # "GenUser" not "genuser"
)
```

{% raw %}
```jinja2
{# GOOD: Preserve original case #}
{{ component_name }}
```
{% endraw %}

### ❌ Pitfall 3: Generic Index File Names

**Problem:**

```
docs/requirements/GenUser/index.md
docs/requirements/UserMgmt/index.md
```

**Why it's problematic:** Hard to search for, not descriptive, conflicts with MkDocs section indexes.

**Solution:**

```
docs/requirements/GenUser/genuser-index.md
docs/requirements/UserMgmt/usermgmt-index.md
```

Benefits:

- More descriptive and searchable
- Easier to automate
- No naming conflicts
- Clear purpose

### ❌ Pitfall 4: Not Handling Empty States

**Problem:** Generated index crashes or shows empty table when no requirements exist.

**Solution:**

{% raw %}
```jinja2
{% if requirements | length == 0 %}
!!! info "No Requirements Found"
    No requirements matching the filter criteria were found.
    Requirements will appear here once they are created.
{% endif %}
```
{% endraw %}

## Testing Your Implementation

### Manual Test

```bash
# Generate indexes manually
python scripts/generate-req-index_UPDATE.py

# Build MkDocs site
mkdocs build --clean

# Serve locally
mkdocs serve
```

**Example of expected output:**

```
============================================================
Requirements Index Generator
============================================================
🔄 Generating main requirements index...
✅ Generated docs/requirements/req-index.md
🔄 Generating component-specific indexes...
   Processing genuser component...
✅ Generated GenUser/genuser-index.md
   Processing usermgmt component...
   No requirements found for usermgmt, generating empty index...
✅ Generated UserMgmt/usermgmt-index.md
```

### Verify Generated Files

**Check file exists:**

```bash
ls -la docs/requirements/GenUser/genuser-index.md
```

**Check content:**

```bash
head -20 docs/requirements/GenUser/genuser-index.md
```

**Verify navigation:**

- Navigate to "Requirements by Subsystem" in MkDocs site
- Click on "General User Access"
- Verify page loads with correct component name
- Verify table displays requirements (or "No Requirements Found")

## Extending to Specifications

You can reuse this pattern for specifications:

1. **Create specification hook:** `docs/hooks/generate_spec_index.py`
2. **Create specification script:** `scripts/generate-spec-index.py`
3. **Reuse template:** `scripts/templates/requirements-index.jinja2` (or create spec-specific template)
4. **Update mkdocs.yml navigation**

**Key changes for specifications:**

```python
# In generate-spec-index.py
def scan_specifications(base_dir: Path, spec_id_filter: Optional[str] = None):
    """Scan for spec-*.md files instead of req-*.md"""
    for spec_file in scan_dir.rglob("spec-*.md"):
        # Extract metadata from specifications
        ...
```

## Benefits of This Approach

✅ **Automatic Updates**: Indexes regenerate on every build
✅ **No Manual Maintenance**: Add a requirement file, index updates automatically
✅ **Consistency**: All indexes follow the same format
✅ **Filtering**: Component-specific views using req_id prefixes
✅ **Empty State Handling**: Clear messages when no requirements exist
✅ **Extensible**: Easy to add new components or adapt for specifications
✅ **Security**: Input validation, path validation, YAML safe loading

## Best Practices

1. **Always validate metadata** before processing
2. **Use explicit encoding** (`encoding="utf-8"`) when reading/writing files
3. **Handle empty states gracefully** with informative messages
4. **Log what's happening** so users understand the process
5. **Don't fail the build** if index generation fails (warn instead)
6. **Use relative paths** for links (portability across environments)
7. **Preserve case** when displaying component names
8. **Check if content changed** before writing (prevents infinite rebuild loops)

## Troubleshooting

### Hook Not Running

**Symptom:** Index files not generated during `mkdocs build`

**Check:**

1. Is hook registered in `mkdocs.yml`?
2. Does hook file exist at `docs/hooks/generate_req_index.py`?
3. Does script exist at `scripts/generate-req-index_UPDATE.py`?
4. Run with `--verbose` to see if hook errors occur

**Debug:**

```bash
mkdocs build --clean --verbose 2>&1 | grep -i "generating requirements"
```

### Files Not Appearing in Navigation

**Symptom:** Index files generated but don't show in MkDocs navigation

**Check:**

1. File paths in `mkdocs.yml` match generated file names
2. Files exist at expected paths
3. YAML syntax in `mkdocs.yml` is correct (proper indentation)

### Wrong Component Name Case

**Symptom:** Seeing "Genuser" instead of "GenUser"

**Fix:** Pass `component_dir.name` (CamelCase) instead of `component_name` (lowercase) to template

### Infinite Rebuild Loop

**Symptom:** MkDocs keeps rebuilding when using `mkdocs serve`

**Cause:** Script writes file even when content hasn't changed

**Fix:** Check if content changed before writing:
```python
if output_path.exists():
    with open(output_path, "r", encoding="utf-8") as f:
        old_content = f.read()
    if old_content == new_content:
        return  # Don't write, content unchanged
```

## Related Documentation

- [MkDocs Hooks Documentation](https://www.mkdocs.org/dev-guide/plugins/#on_pre_build)
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/)
- [YAML Front Matter](https://jekyllrb.com/docs/front-matter/)
- [Project Requirement Metadata Guide](../../rules/requirement-metadata-guide.md)

## Summary

You've learned how to:

✅ Create MkDocs hooks that run during the build process
✅ Extract and validate YAML front matter from markdown files
✅ Generate markdown files from Jinja2 templates
✅ Create filtered, component-specific indexes
✅ Handle edge cases (empty states, case preservation, file naming)
✅ Debug common issues with dynamic index generation

This pattern is highly reusable for any structured documentation that uses YAML front matter!
