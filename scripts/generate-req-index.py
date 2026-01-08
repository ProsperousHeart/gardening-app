#!/usr/bin/env python3
"""Generate requirements index from YAML front matter."""

import re
import yaml
from pathlib import Path


def safe_print(message):
    """Print with encoding error handling for Windows console."""
    try:
        print(message)
    except UnicodeEncodeError:
        # Fallback to ASCII-safe output if console doesn't support Unicode
        print(message.encode('ascii', errors='replace').decode('ascii'))


def generate_index():
    req_dir = Path("docs/requirements")
    requirements = []

    # Read all requirement files
    for req_file in req_dir.glob("req-*.md"):
        with open(req_file, "r", encoding="utf-8") as f:
            content = f.read()

            # Extract YAML front matter
            if content.startswith("---"):
                yaml_end = content.find("---", 3)
                yaml_content = content[3:yaml_end]
                metadata = yaml.safe_load(yaml_content)

                requirements.append({
                    "file": req_file.name,
                    "title": metadata.get("title"),
                    "priority": metadata.get("priority"),
                    "phase": metadata.get("phase"),
                    "status": metadata.get("status"),
                    "req_id": metadata.get("req_id", ""),
                })

    # Sort by phase, then priority
    priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    requirements.sort(
        key=lambda r: (int(r["phase"]), priority_order.get(r["priority"], 4))
    )

    # Generate markdown with interactive table
    output = ["# Requirements Index\n\n"]

    # Add filter controls
    output.append('<div class="req-index-controls" markdown="1">\n')
    output.append('  <div class="req-filters">\n')
    output.append('    <input type="text" id="req-search" placeholder="Search requirements..." />\n')
    output.append('    <select id="phase-filter">\n')
    output.append('      <option value="">All Phases</option>\n')

    # Get unique phases for dropdown
    phases = sorted(set(req["phase"] for req in requirements))
    for phase in phases:
        output.append(f'      <option value="{phase}">Phase {phase}</option>\n')

    output.append('    </select>\n')
    output.append('    <select id="priority-filter">\n')
    output.append('      <option value="">All Priorities</option>\n')
    output.append('      <option value="CRITICAL">Critical</option>\n')
    output.append('      <option value="HIGH">High</option>\n')
    output.append('      <option value="MEDIUM">Medium</option>\n')
    output.append('      <option value="LOW">Low</option>\n')
    output.append('    </select>\n')
    output.append('  </div>\n')
    output.append('</div>\n\n')

    # Add single table with all requirements
    output.append('<table id="requirements-table" class="requirements-table">\n')
    output.append('  <thead>\n')
    output.append('    <tr>\n')
    output.append('      <th class="sortable" data-sort="priority">Priority <span class="sort-icon">⇅</span></th>\n')
    output.append('      <th class="sortable" data-sort="phase">Phase <span class="sort-icon">⇅</span></th>\n')
    output.append('      <th class="sortable" data-sort="docnum">Doc Number <span class="sort-icon">⇅</span></th>\n')
    output.append('      <th class="sortable" data-sort="title">Title <span class="sort-icon">⇅</span></th>\n')
    output.append('    </tr>\n')
    output.append('  </thead>\n')
    output.append('  <tbody>\n')

    for req in requirements:
        # Create priority badge
        priority_badge = (
            f'<span class="priority-badge priority-{req["priority"].lower()}">'
            f'{req["priority"]}</span>'
        )

        # Get doc number
        doc_number = req["req_id"] if req["req_id"] else req["file"].replace(".md", "").upper()

        # Remove doc number from title if it appears in parentheses (DRY principle)
        title = req["title"]
        # Match (doc_number) or (DOC_NUMBER) in title
        pattern = r'\s*\(' + re.escape(doc_number) + r'\)'
        title_clean = re.sub(pattern, '', title, flags=re.IGNORECASE).strip()

        # Add table row with data attributes for filtering
        output.append(
            f'    <tr data-phase="{req["phase"]}" data-priority="{req["priority"]}" '
            f'data-docnum="{doc_number}" data-title="{title_clean}">\n'
            f'      <td style="text-align: center;">{priority_badge}</td>\n'
            f'      <td style="text-align: center;">{req["phase"]}</td>\n'
            f'      <td style="text-align: center;">{doc_number}</td>\n'
            f'      <td><a href="{req["file"]}">{title_clean}</a></td>\n'
            f'    </tr>\n'
        )

    output.append('  </tbody>\n')
    output.append('</table>\n')

    # Generate new content
    new_content = "".join(output)
    output_file = Path("docs/requirements/req-index.md")

    # Only write if content changed (prevents infinite rebuild loop)
    should_write = True
    if output_file.exists():
        with open(output_file, "r", encoding="utf-8") as f:
            old_content = f.read()
        if old_content == new_content:
            should_write = False
            safe_print("ℹ️  Requirements index unchanged, skipping write")

    if should_write:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        safe_print("✅ Generated docs/requirements/req-index.md")
    else:
        safe_print("✅ Requirements index up to date")

if __name__ == "__main__":
    generate_index()