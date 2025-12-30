# Cross-Reference System Usage Guide

## Overview

This project uses YAML front matter metadata in requirement and specification files to maintain bidirectional traceability between:

- Requirements ↔ Specifications
- Requirements/Specs ↔ Source code
- Requirements/Specs ↔ Tests
- Requirements/Specs ↔ Architecture diagrams

**See**: [SPEC-CROSS-REFERENCE.md](../SPEC-CROSS-REFERENCE.md) for the central tracking table.

## Required Metadata Fields

### Requirement Files (`docs/requirements/*.md`)

```yaml
---
# Standard metadata
title: Feature Name
req_id: req-subsystem-component
priority: CRITICAL | HIGH | MEDIUM | LOW
phase: 1-7
status: draft | in-review | approved | implemented
created: YYYY-MM-DD
updated: YYYY-MM-DD
author: Your Name
maps_to_req000: REQ-000 reference

# Cross-Reference Tracking
cross_ref_table: ../SPEC-CROSS-REFERENCE.md
specification: TBD  # Updated when spec is generated
source_files: []
test_files: []
diagrams: []
---
```

### Specification Files (`docs/specifications/*.md`)

```yaml
---
# Specification metadata
title: Feature Name Specification
spec_id: spec-subsystem-component
status: draft | in-review | approved | implemented
created: YYYY-MM-DD
updated: YYYY-MM-DD
author: Your Name

# Cross-Reference Tracking
cross_ref_table: ../SPEC-CROSS-REFERENCE.md
requirement: ../requirements/req-subsystem-component.md
source_files: []
test_files: []
diagrams: []
---
```

## Workflow: Updating Cross-References

### Phase 1: Create Requirement

**Action**: Create new requirement file

**Update**:
```yaml
cross_ref_table: ../SPEC-CROSS-REFERENCE.md
specification: TBD
source_files: []
test_files: []
diagrams: []
```

**Also update**: `docs/SPEC-CROSS-REFERENCE.md` (add row for this requirement)

### Phase 2: Generate Specification

**Action**: Run `/make-spec-from-req req-file.md`

**Update requirement file**:
```yaml
specification: ../specifications/spec-subsystem-component.md
diagrams: ["diagrams/architecture-subsystem-component.md", "diagrams/threat-model-subsystem-component.md"]
updated: 2025-12-29
```

**Specification file** (auto-generated with):
```yaml
requirement: ../requirements/req-subsystem-component.md
diagrams: ["diagrams/architecture-subsystem-component.md", "diagrams/threat-model-subsystem-component.md"]
```

**Also update**: `docs/SPEC-CROSS-REFERENCE.md` (link spec to requirement)

### Phase 3: Implement Code

**Action**: Write implementation files

**Update both requirement and spec files**:
```yaml
source_files: ["src/module.py", "src/helpers.py"]
updated: 2025-12-29
```

**Also update**: `docs/SPEC-CROSS-REFERENCE.md` (add source files)

### Phase 4: Write Tests

**Action**: Create test files

**Update both requirement and spec files**:
```yaml
test_files: ["tests/test_module.py", "tests/test_helpers.py"]
updated: 2025-12-29
```

**Also update**: `docs/SPEC-CROSS-REFERENCE.md` (add test files)

## Batch Update Script

To add cross-reference fields to existing requirement files:

### Bash Script (Linux/macOS/Git Bash)

```bash
#!/bin/bash
# add-cross-ref-fields.sh
# Adds cross-reference fields to existing requirement files

for file in docs/requirements/REQ-*.md; do
    # Check if file already has cross_ref_table field
    if grep -q "cross_ref_table:" "$file"; then
        echo "Skipping $file (already has cross-reference fields)"
        continue
    fi

    echo "Updating $file..."

    # Find the line number of the closing ---
    line_num=$(grep -n "^---$" "$file" | head -2 | tail -1 | cut -d: -f1)

    # Insert cross-reference fields before the closing ---
    sed -i "${line_num}i\\
\\
# Cross-Reference Tracking (see SPEC-CROSS-REFERENCE.md)\\
cross_ref_table: ../SPEC-CROSS-REFERENCE.md\\
specification: TBD\\
source_files: []\\
test_files: []\\
diagrams: []" "$file"

    # Update the 'updated' field
    TODAY=$(date +%Y-%m-%d)
    sed -i "s/^updated: .*/updated: $TODAY/" "$file"
done

echo "Done!"
```

### PowerShell Script (Windows)

```powershell
# add-cross-ref-fields.ps1
# Adds cross-reference fields to existing requirement files

$files = Get-ChildItem -Path "docs\requirements\REQ-*.md"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw

    # Check if already has cross_ref_table
    if ($content -match "cross_ref_table:") {
        Write-Host "Skipping $($file.Name) (already has cross-reference fields)"
        continue
    }

    Write-Host "Updating $($file.Name)..."

    # Find the second occurrence of ---
    $lines = Get-Content $file.FullName
    $dashCount = 0
    $insertLine = 0

    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -eq "---") {
            $dashCount++
            if ($dashCount -eq 2) {
                $insertLine = $i
                break
            }
        }
    }

    # Create new content array
    $newLines = @()
    $newLines += $lines[0..($insertLine - 1)]
    $newLines += ""
    $newLines += "# Cross-Reference Tracking (see SPEC-CROSS-REFERENCE.md)"
    $newLines += "cross_ref_table: ../SPEC-CROSS-REFERENCE.md"
    $newLines += "specification: TBD"
    $newLines += "source_files: []"
    $newLines += "test_files: []"
    $newLines += "diagrams: []"
    $newLines += $lines[$insertLine..($lines.Count - 1)]

    # Update the 'updated' field
    $today = Get-Date -Format "yyyy-MM-dd"
    $newContent = $newLines -replace "^updated: .*", "updated: $today"

    # Write back to file
    $newContent | Set-Content $file.FullName
}

Write-Host "Done!"
```

### Manual Update Process

If you prefer manual updates:

1. Open each requirement file in `docs/requirements/`
2. Find the second `---` line (closing the YAML front matter)
3. Add these lines **before** the closing `---`:

```yaml

# Cross-Reference Tracking (see SPEC-CROSS-REFERENCE.md)
cross_ref_table: ../SPEC-CROSS-REFERENCE.md
specification: TBD
source_files: []
test_files: []
diagrams: []
```

4. Update the `updated:` field to today's date
5. Save the file

## Querying Cross-References

### Find Requirements Without Specs

```bash
grep -l "specification: TBD" docs/requirements/REQ-*.md
```

### Find Requirements With Implementations

```bash
grep -l "source_files: \[.*\]" docs/requirements/REQ-*.md | \
  grep -v "source_files: \[\]"
```

### List All Diagrams for a Requirement

```bash
grep "diagrams:" docs/requirements/REQ-000a_General.md
```

### Generate Cross-Reference Report

```bash
#!/bin/bash
echo "=== Cross-Reference Coverage Report ==="
echo ""

total=0
with_spec=0
with_code=0
with_tests=0

for file in docs/requirements/REQ-*.md; do
    ((total++))

    if ! grep -q "specification: TBD" "$file"; then
        ((with_spec++))
    fi

    if grep -q "source_files: \[.*\]" "$file" && \
       ! grep -q "source_files: \[\]" "$file"; then
        ((with_code++))
    fi

    if grep -q "test_files: \[.*\]" "$file" && \
       ! grep -q "test_files: \[\]" "$file"; then
        ((with_tests++))
    fi
done

echo "Total requirements: $total"
echo "With specifications: $with_spec ($((with_spec * 100 / total))%)"
echo "With implementations: $with_code ($((with_code * 100 / total))%)"
echo "With tests: $with_tests ($((with_tests * 100 / total))%)"
```

## MkDocs Integration

### Display Cross-References in Documents

You can add this snippet to requirement/spec files to display cross-references:

```markdown
{% if page.meta.specification and page.meta.specification != "TBD" %}
## Related Documentation

**Specification**: [{{ page.meta.specification }}]({{ page.meta.specification }})

{% if page.meta.source_files %}
**Implementation Files**:
{% for file in page.meta.source_files %}
- `{{ file }}`
{% endfor %}
{% endif %}

{% if page.meta.test_files %}
**Test Files**:
{% for file in page.meta.test_files %}
- `{{ file }}`
{% endfor %}
{% endif %}

{% if page.meta.diagrams %}
**Diagrams**:
{% for diagram in page.meta.diagrams %}
- [{{ diagram }}](../{{ diagram }})
{% endfor %}
{% endif %}
{% endif %}
```

### Create Custom MkDocs Plugin

For advanced usage, create a plugin to:
- Auto-generate cross-reference tables
- Validate bi-directional links
- Highlight incomplete requirements
- Generate coverage reports

## Best Practices

### 1. Always Update Both Directions

When linking requirement → spec, also update spec → requirement.

### 2. Use Relative Paths

Always use relative paths for portability:
- ✅ `../specifications/spec-feature.md`
- ❌ `/docs/specifications/spec-feature.md`

### 3. Keep Lists Updated

Add to lists, don't replace:
```yaml
# Before
diagrams: ["diagrams/architecture.md"]

# After adding threat model
diagrams: ["diagrams/architecture.md", "diagrams/threat-model.md"]
```

### 4. Update the 'updated' Field

Always update `updated: YYYY-MM-DD` when modifying cross-references.

### 5. Maintain SPEC-CROSS-REFERENCE.md

The central table should always reflect the metadata:
- Add rows when creating requirements
- Update cells when generating specs
- Link to diagrams when creating them

## Troubleshooting

### Missing Cross-Reference Fields

**Symptom**: Old requirement files don't have cross-reference fields

**Solution**: Run the batch update script (see above)

### Broken Links

**Symptom**: Links in metadata point to non-existent files

**Solution**:
1. Run `markdown-link-check` on docs/
2. Update paths in YAML front matter
3. Verify file names match exactly (case-sensitive)

### Inconsistent Cross-References

**Symptom**: Requirement says spec is TBD, but spec file exists

**Solution**:
1. Find the spec file
2. Update requirement's `specification:` field
3. Verify spec's `requirement:` field points back
4. Update `docs/SPEC-CROSS-REFERENCE.md`

## Related Documentation

- [SPEC-CROSS-REFERENCE.md](../SPEC-CROSS-REFERENCE.md) - Central tracking table
- [Requirement Metadata Guide](./requirement-metadata-guide.md) - Detailed metadata documentation
- [Markdown Standards](./markdown-standards.md) - Documentation standards
- [Master Workflow](../../.github/instructions/master-workflow.md) - Development process
