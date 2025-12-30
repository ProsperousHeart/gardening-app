# Navigation Status Indicators in Material for MkDocs

**Last Updated:** 2025-12-30
**Material for MkDocs Version:** 9.2.0+

## Overview

Material for MkDocs provides a built-in **page status feature** that automatically adds status indicators (icons/badges) to navigation items in the sidebar. This feature helps users quickly identify the status of documentation pages at a glance.

## How It Works

### 1. Configure Status Types in `mkdocs.yml`

Define your status identifiers and descriptions under `extra.status`:

```yaml
extra:
  status:
    draft: Draft - Work in progress
    in-review: In Review - Awaiting approval
    approved: Approved - Ready for implementation
    implemented: Implemented - Complete
```

**Configuration format:**

- **Simple string format**: `identifier: description`
- **Status identifier** (left side): The value used in page front matter (e.g., `draft`, `approved`)
- **Description** (right side): Tooltip text shown when hovering over the status indicator

**IMPORTANT:** Do NOT use dictionary format with `description:` and `icon:` keys. Icons are configured separately in CSS (see step 3 below).

### 2. Add Status to Pages

In your Markdown file's YAML front matter:

```yaml
---
title: Plant Database Requirements
status: approved  # This triggers the status indicator
priority: HIGH
---
```

### 3. Add Custom Icons in CSS (Optional)

If you want custom icons instead of the default indicator, define them in `docs/stylesheets/extra.css`:

```css
/* Define SVG icons using CSS custom properties */
:root {
  /* Draft - Pencil icon (Octicons) */
  --md-status--draft: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M17.263 2.177..."/></svg>');

  /* Approved - Check circle icon (Octicons) */
  --md-status--approved: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M17.28 9.28..."/></svg>');
}

/* Apply icons using mask-image */
.md-status--draft::after {
  mask-image: var(--md-status--draft);
  -webkit-mask-image: var(--md-status--draft);
}

.md-status--approved::after {
  mask-image: var(--md-status--approved);
  -webkit-mask-image: var(--md-status--approved);
}
```

**Why mask-image?**
- Allows icons to inherit theme colors automatically
- Works with dark mode without extra configuration
- SVG data URIs eliminate need for separate image files

**Where to get SVG icons:**
- [Octicons](https://primer.style/foundations/icons) (GitHub's icon set)
- [Material Design Icons](https://fonts.google.com/icons)
- [FontAwesome](https://fontawesome.com/icons)
- [Heroicons](https://heroicons.com/)

### 4. Automatic Display

Material for MkDocs will automatically:

- ✅ Detect the `status` field in page metadata
- ✅ Add a status indicator icon next to the page title in navigation
- ✅ Show the configured description as a tooltip on hover
- ✅ Apply custom icons from CSS (if configured)

## What You See

### In the Navigation Sidebar

```
📁 System Requirements
  ├─ 📄 General Requirements ✅  ← Status indicator appears here
  ├─ 📄 Scope Document 👀
  └─ 📄 Use Cases 📝
```

### On Hover

When you hover over the status indicator, you'll see the tooltip:

```
✅ Approved - Ready for implementation
```

## Status Indicators vs. Priority Badges

This project uses **two separate systems** for showing metadata:

| Feature | Location | Technology | Purpose |
|---------|----------|------------|---------|
| **Status Indicators** | Navigation sidebar | Material for MkDocs built-in | Show page status in navigation |
| **Priority Badges** | Page content (below title) | Custom CSS + Python hook | Show priority/phase/status on the page itself |

### Status Indicators (Navigation)

- **Where:** Left sidebar navigation menu
- **How:** Configured in `mkdocs.yml` under `extra.status`
- **Styling:** Uses `docs/stylesheets/extra.css` (`.md-status` classes)
- **Emojis:** Defined via Material's emoji extension in `mkdocs.yml`

### Priority Badges (Page Content)

- **Where:** Below the H1 heading on the page
- **How:** Python hook (`docs/hooks/priority_badges.py`) injects HTML
- **Styling:** Uses `docs/stylesheets/priority-badges.css`
- **Content:** Shows priority, phase, and status together

## Emoji Configuration

For status indicators to display emojis properly, ensure you have the emoji extension configured:

```yaml
markdown_extensions:
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
```

**This is already configured** in this project's `mkdocs.yml` (lines 197-199).

## How to Get SVG Icon Data

To add custom icons, you need SVG code converted to a data URI. Here's how:

### Method 1: From Octicons (Used in this project)

1. Visit [Octicons](https://primer.style/foundations/icons)
2. Find your icon (e.g., "pencil-24")
3. Click "Copy SVG"
4. Wrap in data URI format:
   ```css
   --md-status--draft: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="..."/></svg>');
   ```

### Method 2: From Material Icons

1. Visit [Material Icons](https://fonts.google.com/icons)
2. Select icon → Copy SVG
3. Convert to data URI format (same as above)

### Method 3: From Any SVG

```css
/* 1. Get SVG code */
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path d="..."/>
</svg>

/* 2. Convert to CSS custom property */
--md-status--custom: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="..."/></svg>');

/* 3. Apply with mask-image */
.md-status--custom::after {
  mask-image: var(--md-status--custom);
  -webkit-mask-image: var(--md-status--custom);
}
```

### Complete Example

See `docs/stylesheets/extra.css` (lines 131-171) for the complete implementation used in this project.

## Custom Styling

This project uses **custom Octicon icons** defined in `docs/stylesheets/extra.css`.

**Default behavior (no custom CSS):**
- Material for MkDocs shows a generic "i" icon
- Tooltips work correctly
- Basic theme-consistent styling

**With custom icons (this project):**
- Octicon SVG icons (pencil, eye, check-circle, rocket)
- Icons inherit theme colors via `mask-image`
- Automatic dark mode support
- Professional appearance matching GitHub's design

**See the implementation:** `docs/stylesheets/extra.css` lines 131-171

## Troubleshooting

### Icons Show as "i" in a Circle

**Problem:** Status indicators appear as a generic "i" icon.

**Cause:** No custom icons defined in CSS. This is actually **normal behavior** for Material for MkDocs!

**Solutions:**

**Option 1: Accept the default** - The "i" icon is Material's default and works fine
- ✅ Tooltips work correctly
- ✅ Theme-consistent
- ✅ No additional CSS needed

**Option 2: Add custom icons** - Define icons in CSS (see [How to Get SVG Icon Data](#how-to-get-svg-icon-data))

```css
/* In docs/stylesheets/extra.css */
:root {
  --md-status--draft: url('data:image/svg+xml;charset=utf-8,<svg>...</svg>');
}

.md-status--draft::after {
  mask-image: var(--md-status--draft);
  -webkit-mask-image: var(--md-status--draft);
}
```

### Tooltip Shows Dictionary/Object

**Problem:** Tooltip displays `{'description': '...', 'icon': '...'}` instead of just the description.

**Cause:** Using incorrect YAML format with dictionary syntax.

**Solution:** Use simple string format:

```yaml
# ❌ WRONG - Dictionary format (not supported)
extra:
  status:
    draft:
      description: Draft - Work in progress
      icon: octicons/pencil-24

# ✅ CORRECT - Simple string format
extra:
  status:
    draft: Draft - Work in progress
```

Icons must be configured in CSS, not in `mkdocs.yml`!

### Status Indicators Don't Match Between Local and Deployment

**Problem:** Status indicators look different locally vs. on GitHub Pages.

**Cause:** Usually caching issues or Material for MkDocs version mismatch.

**Solution:**
1. Clear browser cache and rebuild: `mkdocs build --clean`
2. Verify same Material for MkDocs version locally and in deployment
3. Check that emoji extension is configured in `mkdocs.yml`

### Status Indicator Doesn't Appear

**Problem:** No status indicator in navigation even with `status:` in front matter.

**Checklist:**
- ✅ Material for MkDocs version 9.2.0 or higher
- ✅ `extra.status` configured in `mkdocs.yml`
- ✅ Page has `status: <value>` in YAML front matter
- ✅ Status value matches a configured identifier (e.g., `draft`, `approved`)
- ✅ Page is in the `nav:` configuration

## Complete Example

### 1. Configure in `mkdocs.yml`

```yaml
extra:
  status:
    draft: Draft - Work in progress
    approved: Approved - Ready for implementation
```

### 2. Add Custom Icons in CSS (Optional)

```css
/* In docs/stylesheets/extra.css */
:root {
  --md-status--approved: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M17.28 9.28a.75.75 0 0 0-1.06-1.06l-5.97 5.97-2.47-2.47a.75.75 0 0 0-1.06 1.06l3 3a.75.75 0 0 0 1.06 0l6.5-6.5Z"/><path d="M12 1c6.075 0 11 4.925 11 11s-4.925 11-11 11S1 18.075 1 12 5.925 1 12 1ZM2.5 12a9.5 9.5 0 0 0 9.5 9.5 9.5 9.5 0 0 0 9.5-9.5A9.5 9.5 0 0 0 12 2.5 9.5 9.5 0 0 0 2.5 12Z"/></svg>');
}

.md-status--approved::after {
  mask-image: var(--md-status--approved);
  -webkit-mask-image: var(--md-status--approved);
}
```

### 3. Add Status to Page

```yaml
---
title: Plant Database Requirements
req_id: req-general-user-plant-database
priority: HIGH
phase: 1
status: approved  # ← This adds the status indicator
created: 2025-01-15
updated: 2025-01-27
author: Kassandra Keeton
---

# Plant Database Requirements

This document defines requirements for the plant database...
```

### 4. Result in Navigation

```
📁 System Requirements
  └─ 📄 Plant Database Requirements ✓ ← Check circle icon with tooltip
```

Hover over the icon to see: "Approved - Ready for implementation"

### 5. Result on Page Content

Below the H1 heading, you'll see priority badges (from the Python hook - separate feature):

```
HIGH  Phase 1  Approved
```

## Best Practices

1. **Use descriptive tooltip text** - Help users understand what each status means
   ```yaml
   approved: Approved - Ready for implementation  # Good
   approved: Approved                             # Less helpful
   ```

2. **Keep status values lowercase** - Matches Material for MkDocs conventions
   ```yaml
   status: approved    # Good
   status: Approved    # Works but inconsistent
   ```

3. **Align with your workflow** - Define statuses that match your development process
   ```yaml
   extra:
     status:
       draft: Initial draft
       review: Under review
       approved: Approved
       implemented: Implemented
       archived: Archived
   ```

4. **Document your status workflow** - Create a guide explaining when to use each status

## Related Documentation

- **Priority Badges Setup:** `docs/tutorials/mkdocs/priority-badges-setup.md` - In-page badges (separate from navigation indicators)
- **Requirement Metadata Guide:** `docs/rules/requirement-metadata-guide.md` - YAML front matter standards
- **Custom CSS:** `docs/stylesheets/extra.css` (lines 131-171) - Icon implementation

## External Resources

- [Material for MkDocs - Page Status Reference](https://squidfunk.github.io/mkdocs-material/reference/#setting-the-page-status) - Official documentation
- [Material for MkDocs - Page Status Example](https://mkdocs-material.github.io/examples/page-status/) - Live example project
- [GitHub Examples Repository](https://github.com/mkdocs-material/examples/tree/master/examples/page-status) - Source code for example
- [Octicons](https://primer.style/foundations/icons) - GitHub's icon set (used in this project)
- [CSS mask-image](https://developer.mozilla.org/en-US/docs/Web/CSS/mask-image) - How SVG masking works
