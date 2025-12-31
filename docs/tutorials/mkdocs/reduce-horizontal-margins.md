---
title: Reducing Horizontal Margins in MkDocs Material
description: How to maximize content area by reducing excessive left/right whitespace
created: 2025-12-31
updated: 2025-12-31
status: approved
---

# Reducing Horizontal Margins in MkDocs Material

## Problem

MkDocs Material theme by default adds significant horizontal margins on both sides of the content, creating large empty spaces on the left (before navigation/text) and right (after content). This wastes valuable screen space, especially on wider monitors.

**Symptoms:**
- Large whitespace on left and right sides of page
- Content feels cramped in the middle
- Tables, code blocks, and diagrams don't use full available width
- `.md-sidebar__scrollwrap` shows as a boundary with excessive padding

## Solution

Add custom CSS to reduce horizontal margins and increase content width.

### Implementation

Add to `docs/stylesheets/extra.css`:

```css
/* ========================================
   Reduce Horizontal Margins
   ======================================== */

/* Remove excessive left/right whitespace to maximize content area */

/* Reduce margin on main grid container */
.md-grid {
  max-width: 90rem;  /* Increase from default 61rem (~976px) to 90rem (~1440px) */
  margin-left: 0.5rem;  /* Reduce from default 1rem+ */
  margin-right: 0.5rem;  /* Reduce from default 1rem+ */
}

/* Reduce padding inside content container */
.md-content__inner {
  margin-left: 0.5rem;
  margin-right: 0.5rem;
}

/* Reduce sidebar padding to reclaim space */
.md-sidebar__scrollwrap {
  margin-left: 0.5rem;
  margin-right: 0.5rem;
}
```

### What Each Rule Does

1. **`.md-grid`** - Main container for entire page layout
   - `max-width: 90rem` - Increases max content width to use more screen space on large monitors
   - `margin-left/right: 0.5rem` - Reduces horizontal margins from default (~1rem or more)

2. **`.md-content__inner`** - Inner content container where your markdown renders
   - Reduces left/right margins to minimize wasted space

3. **`.md-sidebar__scrollwrap`** - Navigation sidebar container
   - Reduces padding to bring sidebars closer to edges

## Adjusting Further

If you need **even tighter** spacing:

```css
.md-grid {
  max-width: 100rem;  /* Even wider on large screens */
  margin-left: 0.2rem;  /* Minimal margin */
  margin-right: 0.2rem;
}

.md-content__inner {
  margin-left: 0.2rem;
  margin-right: 0.2rem;
}

.md-sidebar__scrollwrap {
  margin-left: 0;  /* No margin at all */
  margin-right: 0;
}
```

If you need **more breathing room** (less aggressive):

```css
.md-grid {
  max-width: 80rem;  /* More moderate width increase */
  margin-left: 1rem;  /* Keep some margin */
  margin-right: 1rem;
}
```

## Testing

After making changes:

```bash
mkdocs serve
```

Visit `http://127.0.0.1:8000` and check:
- ✅ Less whitespace on left and right sides
- ✅ Content uses more of the available width
- ✅ Tables and code blocks have more room
- ✅ Still readable and not cramped

## Responsive Considerations

The solution works across screen sizes because:
- Uses `rem` units (scales with font size)
- MkDocs Material handles mobile/tablet breakpoints automatically
- On small screens, the margins become even less noticeable

**Optional**: Add media queries for different screen sizes:

```css
/* On very large screens (> 1920px), maximize even more */
@media screen and (min-width: 120em) {
  .md-grid {
    max-width: 110rem;
  }
}

/* On tablets, keep some margin for readability */
@media screen and (max-width: 76.24em) {
  .md-grid {
    margin-left: 1rem;
    margin-right: 1rem;
  }
}
```

## Related Documentation

- **CSS Styling**: `docs/stylesheets/extra.css` - Where custom styles are defined
- **MkDocs Configuration**: `mkdocs.yml` - Theme configuration
- **MkDocs Material Docs**: [Customization Guide](https://squidfunk.github.io/mkdocs-material/customization/)

## Key Classes Reference

MkDocs Material uses these key CSS classes for layout:

| Class | Purpose |
|-------|---------|
| `.md-grid` | Main grid container - controls max width and horizontal margins |
| `.md-content` | Content area wrapper |
| `.md-content__inner` | Inner content container - where markdown renders |
| `.md-sidebar` | Sidebar containers (primary = left nav, secondary = right TOC) |
| `.md-sidebar__scrollwrap` | Scrollable sidebar wrapper - controls sidebar padding |
| `.md-main__inner` | Inner main container - vertical spacing |
| `.md-typeset` | Typography container - text area styling |

## Troubleshooting

**Issue**: Changes don't appear after editing CSS
- **Solution**: Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)
- **Solution**: Clear browser cache
- **Solution**: Check browser DevTools for CSS errors

**Issue**: Content looks too cramped on mobile
- **Solution**: Add media query to restore margins on small screens (see Responsive Considerations above)

**Issue**: Sidebars overlap content
- **Solution**: Reduce `max-width` value (try 80rem or 70rem)
- **Solution**: Check for conflicting CSS rules in browser DevTools

## Summary

**To maximize content space:**
1. Increase `.md-grid` max-width (default 61rem → 90rem)
2. Reduce horizontal margins on `.md-grid`, `.md-content__inner`, and `.md-sidebar__scrollwrap`
3. Test with `mkdocs serve` and adjust values as needed
4. Use browser DevTools to inspect and fine-tune spacing
