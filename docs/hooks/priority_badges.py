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
    # Only process requirement files
    if not page.file.src_path.startswith("requirements/req-"):
        return markdown

    # Extract metadata from page
    meta = page.meta

    # Check if we have the required metadata
    if not meta.get("priority"):
        return markdown

    # Build badge HTML
    badges_html = build_badges_html(meta)

    # Find the first h1 heading and insert badges after it
    # Pattern: # Heading text
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
    # Only process requirement files
    if not page.file.src_path.startswith("requirements/req-"):
        return context

    # Add metadata to context
    context["priority"] = page.meta.get("priority")
    context["phase"] = page.meta.get("phase")
    context["status"] = page.meta.get("status")
    context["req_id"] = page.meta.get("req_id")
    context["maps_to_req000"] = page.meta.get("maps_to_req000")

    return context
