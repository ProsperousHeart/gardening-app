"""
MkDocs hook to automatically add priority badges to requirement pages.

This hook reads the YAML front matter from requirement files and injects
priority, phase, and status badges into the page content.
"""

import re
from pathlib import Path


def on_page_markdown(markdown, page, config, files):
    """
    MkDocs hook that processes markdown before rendering.

    Adds priority badges to requirement pages based on YAML front matter.
    """
    # Only process requirement files (both req- and REQ- patterns)
    src_path = page.file.src_path
    if not (src_path.startswith("requirements/req-") or src_path.startswith("requirements/REQ-")):
        return markdown

    # Extract metadata from page
    meta = page.meta

    # Check if we have the required metadata
    if page.meta.get("show_badges") == False or not meta.get("priority"):
        return markdown

    # Build badge HTML
    badges_html = build_badges_html(meta)

    # Remove YAML front matter first (if present) so we don't match # comments in it
    # Find the end of YAML front matter (second occurrence of ---)
    yaml_end_pattern = r"^---\s*\n.*?\n^---\s*\n"
    yaml_match = re.search(yaml_end_pattern, markdown, flags=re.MULTILINE | re.DOTALL)

    if yaml_match:
        # Split markdown into YAML and content
        yaml_section = markdown[:yaml_match.end()]
        content_section = markdown[yaml_match.end():]

        # Find the first h1 heading in the content section (not in YAML)
        h1_pattern = r"(^#\s+.+$)"
        content_modified = re.sub(h1_pattern, rf"\1\n\n{badges_html}\n", content_section, count=1, flags=re.MULTILINE)

        return yaml_section + content_modified
    else:
        # No YAML front matter, use original approach
        pattern = r"(^#\s+.+$)"
        replacement = rf"\1\n\n{badges_html}\n"
        modified_markdown = re.sub(pattern, replacement, markdown, count=1, flags=re.MULTILINE)
        return modified_markdown


def build_badges_html(meta):
    """
    Build HTML for priority, phase, and status badges.

    Args:
        meta: Dictionary of page metadata from YAML front matter

    Returns:
        HTML string with badges
    """
    badges = []

    # Priority badge
    priority = meta.get("priority", "").upper()
    if priority:
        priority_class = f"priority-{priority.lower()}"
        badges.append(
            f'<span class="priority-badge {priority_class}">{priority}</span>'
        )

    # Phase badge
    phase = meta.get("phase")
    if phase:
        badges.append(
            f'<span class="phase-badge">Phase {phase}</span>'
        )

    # Status badge
    status = meta.get("status", "").lower()
    if status:
        status_class = f"status-{status}"
        status_display = status.replace("-", " ").title()
        badges.append(
            f'<span class="status-badge {status_class}">{status_display}</span>'
        )

    # Combine all badges
    if badges:
        return f'<div class="requirement-badges">{" ".join(badges)}</div>'

    return ""


def on_page_context(context, page, config, nav):
    """
    Add metadata to page context for use in templates.

    This allows templates to access priority data for custom layouts.
    """
    # Only process requirement files (both req- and REQ- patterns)
    src_path = page.file.src_path
    if not (src_path.startswith("requirements/req-") or src_path.startswith("requirements/REQ-")):
        return context

    # Add metadata to context
    context["priority"] = page.meta.get("priority")
    context["phase"] = page.meta.get("phase")
    context["status"] = page.meta.get("status")
    context["req_id"] = page.meta.get("req_id")
    context["maps_to_req000"] = page.meta.get("maps_to_req000")

    return context
