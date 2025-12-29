---
title: Image Styling Guide
description: How to add borders, shadows, and custom styling to images in MkDocs
---

# Image Styling Guide

This guide shows you how to add custom CSS styling to images in your MkDocs documentation, including borders, shadows, and other visual enhancements.

!!! info "Prerequisites"
    - MkDocs with Material theme installed
    - `attr_list` markdown extension enabled
    - Custom CSS file configured in `mkdocs.yml`

---

## Table of Contents

- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [CSS Class Reference](#css-class-reference)
- [Creating Custom Image Styles](#creating-custom-image-styles)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)

---

## Quick Start

### Add a Border to an Image

Use the `{ .bordered }` class on any image:

```markdown
![Example Image](path/to/image.png){ .bordered }
```

**Result:** Image with a 2px border, rounded corners, padding, and subtle shadow.

---

## How It Works

### 1. MkDocs Configuration

The `attr_list` extension must be enabled in `mkdocs.yml`:

```yaml
markdown_extensions:
  - attr_list  # Add CSS classes to elements
  - md_in_html # Use markdown inside HTML blocks
```

**File:** `mkdocs.yml:179-180`

### 2. Custom CSS File

Custom CSS must be loaded in `mkdocs.yml`:

```yaml
extra_css:
  - stylesheets/extra.css
  - stylesheets/priority-badges.css
```

**File:** `mkdocs.yml:323-325`

### 3. CSS Class Definition

Define image styles in your CSS file:

```css
/* Bordered image - adds border and subtle shadow */
img.bordered {
  border: 2px solid var(--md-default-fg-color--lightest);
  border-radius: 8px;
  padding: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Dark mode border adjustment */
[data-md-color-scheme="slate"] img.bordered {
  border-color: rgba(255, 255, 255, 0.2);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}
```

**File:** `docs/stylesheets/extra.css:243-254`

### 4. Apply Class to Image

Use the `attr_list` syntax to add the class:

```markdown
![Alt Text](image-path){ .class-name }
```

**Syntax:**
- Image must be in markdown format: `![Alt](path)`
- Class attribute comes immediately after, no space
- Use curly braces with a leading dot: `{ .class-name }`

---

## CSS Class Reference

### Available Image Classes

| Class | Description | Dark Mode Support |
|-------|-------------|-------------------|
| `.bordered` | 2px border, rounded corners, padding, shadow | ✅ Yes |

### Available Code Block Classes

| Class | Description | Use Case |
|-------|-------------|----------|
| `.ascii-art` | Forces monospace rendering for ASCII art | Box-drawing characters, diagrams |

There may come a time where it makes more sense to have an ASCII diagram than mermaid.

If you do not add the CSS class as outlined above, you will see something like this:

```text
┌─────────────────────────────────────────────────────────┐
│ Plant Database              [CRITICAL] [Phase 1]        │
├─────────────────────────────────────────────────────────┤
│ Plant data model, storage, and basic display.           │
│ Foundation for entire system.                           │
│                                                         │
│ View Requirement →                                      │
└─────────────────────────────────────────────────────────┘
```

... instead of this:

<div class="ascii-art">

```text
┌─────────────────────────────────────────────────────────┐
│ Plant Database              [CRITICAL] [Phase 1]        │
├─────────────────────────────────────────────────────────┤
│ Plant data model, storage, and basic display.           │
│ Foundation for entire system.                           │
│                                                         │
│ View Requirement →                                      │
└─────────────────────────────────────────────────────────┘
```

</div>

### Creating Your Own Classes

You can create additional image styling classes in `docs/stylesheets/extra.css`.

---

## Creating Custom Image Styles

### Step 1: Define CSS Class

Add to `docs/stylesheets/extra.css`:

```css
/* Example: Thick red border */
img.alert-border {
  border: 4px solid #dc2626;
  border-radius: 12px;
  padding: 8px;
  box-shadow: 0 4px 8px rgba(220, 38, 38, 0.3);
}
```

### Step 2: Use in Markdown

```markdown
![Warning Image](path/to/image.png){ .alert-border }
```

### Step 3: Test Locally

```bash
mkdocs serve
```

Visit your page to see the styled image.

---

## Examples

### Example 1: Bordered Screenshot

**Use Case:** Distinguish example screenshots from page background

**Markdown:**

```markdown
![Priority Badge Example](../../img/Examples/example-PRI-badge.png){ .bordered }
```

**Result:** Screenshot with subtle border and shadow

**File:** `docs/tutorials/mkdocs/priority-badges-setup.md:29`

---

### Example 2: Multiple Classes

**Use Case:** Combine multiple CSS classes

**Markdown:**

```markdown
![Diagram](path/to/diagram.png){ .bordered .center }
```

**CSS:**
```css
img.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
```

**Result:** Bordered image centered on page

---

### Example 3: Inline Attributes

**Use Case:** One-off custom styling without creating CSS class

**Markdown:**

```markdown
![Small Icon](path/to/icon.png){ width="100px" style="border: 2px solid blue;" }
```

**Result:** 100px wide image with blue border

!!! warning "Prefer CSS Classes"
    Inline styles are harder to maintain. Create reusable CSS classes instead.

---

### Example 4: Rounded Profile Images

**CSS:**

```css
img.profile {
  border-radius: 50%;
  width: 150px;
  height: 150px;
  object-fit: cover;
  border: 3px solid var(--md-primary-fg-color);
}
```

**Markdown:**

```markdown
![User Avatar](images/avatar.jpg){ .profile }
```

**Result:** Circular profile picture with colored border

---

### Example 5: Floating Images with Text Wrap

**CSS:**

```css
img.float-right {
  float: right;
  margin-left: 1rem;
  margin-bottom: 1rem;
  max-width: 300px;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 4px;
}
```

**Markdown:**

```markdown
![Diagram](diagram.png){ .float-right }

This text will wrap around the image on the left side. The image floats to the right
with appropriate spacing. This is useful for integrating images into flowing text content.
```

---

### Example 6: ASCII Art Alignment Fix

**Use Case:** Box-drawing characters not aligning properly in rendered output

**Problem:** When using ASCII art diagrams with box-drawing characters (┌ ─ ┐ │ └ ┘), the Material theme CSS can override monospace fonts, causing misalignment where some lines appear far to the right.

**CSS:**

```css
/* Ensures proper monospace rendering for ASCII art and box-drawing characters */
.ascii-art pre,
pre.ascii-art {
  font-family: 'Courier New', Courier, 'Lucida Console', Monaco, monospace !important;
  font-size: 14px !important;
  line-height: 1.2 !important;
  letter-spacing: 0 !important;
  white-space: pre !important;
  tab-size: 4 !important;
  -moz-tab-size: 4 !important;
}

.ascii-art code,
pre.ascii-art code {
  font-family: inherit !important;
  font-size: inherit !important;
  line-height: inherit !important;
  letter-spacing: inherit !important;
}
```

**File:** `docs/stylesheets/extra.css:260-278`

**Markdown:**

<pre><code>&lt;div class="ascii-art"&gt;

&#96;&#96;&#96;text
┌─────────────────────────────────────────────────────────┐
│ Plant Database              [CRITICAL] [Phase 1]   │
├─────────────────────────────────────────────────────────┤
│ Plant data model, storage, and basic display.      │
└─────────────────────────────────────────────────────────┘
&#96;&#96;&#96;

&lt;/div&gt;
</code></pre>

**Why `!important` is needed:**

- Material theme applies its own font styles to code blocks
- Without `!important`, theme CSS takes precedence
- Box-drawing characters require exact monospace spacing to align
- Forces consistent font across all browsers

**Result:** Perfect alignment of box-drawing characters in all rendered views

**See also:** The CSS Class Reference section above shows a visual comparison of ASCII art with and without this class.

---

## Technical Details

### attr_list Extension

The `attr_list` extension allows adding HTML attributes to markdown elements:

**Supported attributes:**

- `.class-name` - CSS classes
- `#element-id` - HTML ID
- `key="value"` - Custom attributes (width, height, alt, title, etc.)

**Syntax:**

```markdown
![Image](path){ .class1 .class2 #image-id width="500px" }
```

### Material Theme Variables

Use Material theme CSS variables for consistent styling:

```css
/* Colors */
--md-primary-fg-color          /* Primary theme color */
--md-accent-fg-color           /* Accent color */
--md-default-fg-color--lightest /* Light border color */

/* Spacing */
--md-typeset-table--spacing    /* Table spacing */
```

**Benefits:**

- Automatic dark mode support
- Consistent with site theme
- Adapts if user changes theme colors

### Dark Mode Support

Always provide dark mode styling:

```css
/* Light mode */
img.bordered {
  border: 2px solid var(--md-default-fg-color--lightest);
}

/* Dark mode */
[data-md-color-scheme="slate"] img.bordered {
  border-color: rgba(255, 255, 255, 0.2);
}
```

---

## Troubleshooting

### Image Border Not Showing

**Problem:** Added `{ .bordered }` but no border appears

**Solutions:**

1. **Check CSS file is loaded:**

   - Open browser DevTools (F12)
   - Go to Network tab
   - Look for `extra.css` with 200 status code

2. **Verify attr_list extension:**

   ```yaml
   # mkdocs.yml
   markdown_extensions:
     - attr_list  # Must be present
   ```

3. **Check syntax:**

   ```markdown
   # ✅ CORRECT
   ![Image](path){ .bordered }

   # ❌ WRONG - space between image and class
   ![Image](path) { .bordered }

   # ❌ WRONG - no leading dot
   ![Image](path){ bordered }
   ```

4. **Clear browser cache:**

   - Windows/Linux: `Ctrl + Shift + R`
   - Mac: `Cmd + Shift + R`

5. **Restart MkDocs server:**

   ```bash
   # Stop server (Ctrl+C)
   mkdocs serve
   ```

---

### CSS Not Updating

**Problem:** Changed CSS but don't see updates

**Solutions:**

1. **Hard refresh browser:** `Ctrl + Shift + R` (or `Cmd + Shift + R` on Mac)

2. **Check MkDocs cache:**

   ```bash
   # Delete cache and rebuild
   rm -rf .cache
   mkdocs build
   ```

3. **Verify file paths:**

   ```yaml
   # mkdocs.yml - paths relative to mkdocs.yml location
   extra_css:
     - stylesheets/extra.css  # ✅ CORRECT
     - docs/stylesheets/extra.css  # ❌ WRONG
   ```

---

### Dark Mode Border Looks Wrong

**Problem:** Border is invisible or too bright in dark mode

**Solution:** Add dark mode specific styling:

```css
[data-md-color-scheme="slate"] img.bordered {
  border-color: rgba(255, 255, 255, 0.2);  /* Lighter border */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5); /* Darker shadow */
}
```

**Test both modes:**
- Click theme toggle in header (sun/moon icon)
- Verify border is visible in both light and dark mode

---

### Image Stretching or Distorted

**Problem:** Image aspect ratio is wrong

**Solution:** Use `object-fit` CSS property:

```css
img.fixed-size {
  width: 200px;
  height: 200px;
  object-fit: cover;  /* Crop to fit */
  /* OR */
  object-fit: contain; /* Shrink to fit */
}
```

---

## Best Practices

### 1. Use Semantic Class Names

```css
/* ✅ GOOD - describes purpose */
img.screenshot { }
img.diagram { }
img.profile-photo { }

/* ❌ BAD - describes style */
img.red-border { }
img.big-shadow { }
```

### 2. Create Reusable Classes

Don't duplicate styles. Create one class and reuse it:

```markdown
![Image 1](path1){ .bordered }
![Image 2](path2){ .bordered }
![Image 3](path3){ .bordered }
```

### 3. Provide Dark Mode Support

Always test in both light and dark mode.

### 4. Use Theme Variables

Prefer `var(--md-primary-fg-color)` over hardcoded colors like `#4caf50`.

### 5. Keep Styles Simple

Avoid overly complex styling. Simple borders and shadows are usually enough.

---

## Related Documentation

- **MkDocs Extensions Guide:** [mkdocs-extensions-guide.md](mkdocs-extensions-guide.md)
- **Material Theme CSS Variables:** [Material for MkDocs - Customization](https://squidfunk.github.io/mkdocs-material/customization/)
- **attr_list Extension:** [Python-Markdown Attr List](https://python-markdown.github.io/extensions/attr_list/)

---

## Real-World Example

**Original request:** Add border to priority badge example image

**Implementation:**

1. **CSS Class** (`docs/stylesheets/extra.css:243-254`):
   ```css
   img.bordered {
     border: 2px solid var(--md-default-fg-color--lightest);
     border-radius: 8px;
     padding: 4px;
     box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
   }

   [data-md-color-scheme="slate"] img.bordered {
     border-color: rgba(255, 255, 255, 0.2);
     box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
   }
   ```

2. **Markdown** (`docs/tutorials/mkdocs/priority-badges-setup.md:29`):
   ```markdown
   ![Priority Badge Example](../../img/Examples/example-PRI-badge.png){ .bordered }
   ```

3. **Result:** Screenshot now has visible border distinguishing it from page background

---

**Questions?** Check the [MkDocs Extensions Guide](mkdocs-extensions-guide.md) for more customization options.
