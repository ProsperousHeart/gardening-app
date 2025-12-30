---
title: MkDocs Extensions Guide
description: Comprehensive guide to all markdown extensions used in this documentation
---

# MkDocs Extensions Guide

This guide explains all the markdown extensions enabled in this documentation site and how to use them effectively.

!!! info "Installation Required"
    Before using these extensions, install all required packages: **[MkDocs Installation Guide](mkdocs-installation.md)**

---

## Escaping Syntax in Documentation

!!! tip "Core Concept"
    When writing documentation **about** markdown extensions, you often need to show the raw syntax without MkDocs processing it. This section explains how to display examples that would otherwise be transformed by extensions.

### The Problem

When documenting extensions, you want to show users the **raw syntax** they should type. But MkDocs processes that syntax before rendering!

**Example problem with the Critic extension:**

You want to show this syntax:

<pre><code>This is &#123;--deleted text--&#125;.</code></pre>

But when used in markdown, it renders like this:

```
This is {--deleted text--}.
```

**Result:** Readers see the styled output, not the raw syntax they need to type - regardless of the type you wrap it in (e.g. bash, text, mardown, etc).

### Understanding MkDocs Processing Order

MkDocs processes your documentation in this order:

1. **Markdown extensions** process first (`pymdownx.snippets`, `pymdownx.critic`, etc.)
2. **Plugins** process second (`mkdocs-macros-plugin` for Jinja2 templates)
3. **Rendering** happens last

This means:

- ✅ Markdown extensions see and transform their syntax patterns
- ✅ Plugins see the result after extensions run
- ❌ Standard markdown code blocks don't prevent extension processing

### Solution 1: HTML Entities in `<pre><code>` Blocks

**When to use:** Preventing markdown extensions from processing syntax examples.

**How it works:** HTML entities bypass markdown processing because they're already HTML.

**Common HTML entities:**

| Character | Entity Code | Use Case |
|-----------|-------------|----------|
| `{` | `&#123;` | Critic markup, Jinja2 |
| `}` | `&#125;` | Critic markup, Jinja2 |
| `<` | `&lt;` | Snippets, HTML tags |
| `>` | `&gt;` | Snippets, HTML tags |
| `-` | `&#45;` or `-` | Double dashes (optional) |
| `+` | `&#43;` or `+` | Double plus (optional) |
| `%` | `&#37;` | Jinja2 (optional) |

**Example - Showing Critic Markup Syntax:**

❌ **WRONG - Gets processed by critic extension:**

<pre><code>This is &#123;--deleted text--&#125;.</code></pre>

✅ **CORRECT - Shows raw syntax:**

```html
<pre><code>This is &#123;--deleted text--&#125;.</code></pre>
```

**Renders as:**  what you see above, since I had to use it to show you the example. 💛

**Example - Showing Snippets Syntax:**

❌ **WRONG - Tries to include the file:**

```markdown
--8<-- "snippets/common/example-snippet.md"
```

✅ **CORRECT - Shows raw syntax:**

```html
<pre><code>--8&lt;-- "snippets/common/example-snippet.md"</code></pre>
```

**Renders as:**

<pre><code>--8&lt;-- "snippets/common/example-snippet.md"</code></pre>

### Solution 2: {% raw %}`{% raw %}`{% endraw %} Tags

**When to use:** Preventing Jinja2/macros plugin from processing template syntax (but NOT for markdown extensions).

**How it works:** Tells the macros plugin to skip processing the content between tags.

**Example - Showing Jinja2 Template Syntax:**

✅ **CORRECT - Prevents macros plugin processing:**

The following code:

<pre><code>&#123;% raw %&#125;
&#96;&#96;&#96;markdown
&#123;% if page.meta.priority %&#125;
  Priority: &#123;&#123; page.meta.priority &#125;&#125;
&#123;% endif %&#125;
&#96;&#96;&#96;
&#123;% endraw %&#125;
</code></pre>

... will render this:

{% raw %}
```markdown
{% if page.meta.priority %}
  Priority: {{ page.meta.priority }}
{% endif %}
```
{% endraw %}

!!! warning "{% raw %} Does NOT Work for Markdown Extensions"
    The `{% raw %}` tags only prevent **Jinja2/macros plugin** processing (step 2).

    They do NOT prevent **markdown extensions** (step 1) from processing.

    **Why:** Extensions run before plugins see the `{% raw %}` tags.

### Solution 3: Nested Code Blocks (Rare Cases)

For some simple cases, triple backticks inside triple backticks work with `pymdownx.superfences`:

````markdown
```markdown
# This inner markdown won't be processed
```
````

**Limitation:** Only works for basic markdown, not for special extension syntax.

### Decision Guide: Which Method to Use?

```mermaid
flowchart TD
    A[What are you documenting?] --> B{Type of syntax?}
    B -->|"Markdown extension<br>(snippets, critic)"| C["Use HTML entities in pre/code blocks"]
    B -->|"Jinja2 templates<br>(macros plugin)"| D[Use raw tags]
    B -->|"Basic markdown<br>(headings, lists)"| E["Use nested code blocks with superfences"]

    C --> F["Example:<br>#123;--text--#125;"]
    D --> G["Example:<br>#123;% raw %#125;<br>#123;#123; var #125;#125;<br>#123;% endraw #125;"]
    E --> H["Example:<br>````markdown"]
```

### Quick Reference Table

| Extension | Example Syntax | Escape Method | Entity/Code |
|-----------|---------------|---------------|-------------|
| **Critic** | `{--deleted--}` | HTML entities | `&#123;--deleted--&#125;` |
| **Critic** | `{++added++}` | HTML entities | `&#123;++added++&#125;` |
| **Critic** | `{~~old~>new~~}` | HTML entities | `&#123;~~old~&gt;new~~&#125;` |
| **Snippets** | `--8<-- "file:section-name"` | HTML entities | `--8&lt;-- "file:section-name"` |
| **Jinja2** | <code>&#123;&#123; variable &#125;&#125;</code> | {% raw %}`{% raw %}` tags{% endraw %} | N/A - use raw tags |
| **Jinja2** | <code>&#123;% if condition %&#125;</code> | {% raw %}`{% raw %}` tags{% endraw %} | N/A - use raw tags |
| **HTML tags** | `<div>` | HTML entities | `&lt;div&gt;` |

### Real-World Examples from This Guide

Throughout this guide, you'll see these techniques used:

1. **Critic syntax example** (line ~695): Uses `&#123;` and `&#125;` to show `{--deleted--}`
2. **Snippets syntax example** (line ~77): Uses `&lt;` to show `--8<--`
3. **Jinja2 macro example** (line ~358): Uses {% raw %}`{% raw %}` tags{% endraw %} to show <code>&#123;&#123; read_csv() &#125;&#125;</code>

---

## Table of Contents Extensions

### `toc` - Table of Contents

Automatically generates table of contents from page headings.

**Configuration:**
```yaml
- toc:
    permalink: "#"      # Adds clickable anchor links to headings
    toc_depth: 3        # Include h1, h2, h3 in TOC (excludes h4, h5, h6)
```

**Usage:**
```markdown
# Heading 1
## Heading 2
### Heading 3
```

Each heading automatically gets an anchor link you can click to get a direct URL.

---

## Code Highlighting Extensions

### `pymdownx.highlight` - Syntax Highlighting

Provides beautiful syntax highlighting for code blocks.

**Example:**
```python
def calculate_zone(temperature):
    """Calculate USDA hardiness zone from temperature."""
    if temperature < -60:
        return "1a"
    elif temperature < -55:
        return "1b"
    # ... more logic
    return "13b"
```

**Features:**

- Line numbers with `anchor_linenums: true`
- Line highlighting
- Language-specific syntax coloring

### `pymdownx.inlinehilite` - Inline Code Highlighting

Highlight code within text: `:::python print("Hello")` renders as syntax-highlighted inline code.

**Example:**

The function `:::python def my_func():` does something important.

### `pymdownx.snippets` - Code Snippet Inclusion

Include code from external files directly into documentation.

**Example:**

<pre><code>--8&lt;-- "path/to/code.py"
</code></pre>

SOME EXAMPLE SHOULD BE ABOVE

From [here](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippet-sections) you can also specify sections:

<pre><code>--8&lt;-- "include.md:name"

--8&lt;--
include.md:name
--8&lt;--
</code></pre>

!!! danger "Snippets + Jinja2 Templates DON'T WORK"
    **Problem:** You CANNOT use snippets to include Jinja2 template code!

    **Why:** Execution order:

    1. ✅ Markdown extensions (including `pymdownx.snippets`) run FIRST
    2. ✅ Plugins (including `mkdocs-macros-plugin`) run SECOND

    **What happens:**

    ```markdown
    <!-- ❌ WRONG - Shows raw Jinja2 code -->
    --8<-- "snippets/common/my-template.md"
    ```

    The snippet includes Jinja2 code as **literal text** BEFORE the macros plugin can process it.
    You'll see raw {% raw %}`{% if page.meta.priority %}`{% endraw %} on the rendered page.

    **Solution - Put Jinja2 code directly in files:**

    {% raw %}
    ```markdown
    <!-- ✅ CORRECT - Macros plugin processes this -->
    {% if page.meta.priority %}
    <div class="badge">{{ page.meta.priority }}</div>
    {% endif %}
    ```
    {% endraw %}

    **When to use snippets:**

    - ✅ Regular markdown content
    - ✅ Code examples
    - ✅ Static content that doesn't need processing

    **When NOT to use snippets:**

    - ❌ Jinja2 templates (use direct code instead)
    - ❌ Dynamic content that needs plugin processing

### `pymdownx.superfences` - Advanced Code Blocks

Enables nested code blocks and custom fences like Mermaid diagrams.

---

## Diagram Support

**Learn More:** [Mermaid Documentation](https://mermaid.js.org/)

### Mermaid Diagrams

Create diagrams directly in markdown using Mermaid syntax.

**Example - Flowchart:**

```mermaid
graph LR
    A[Gardener] --> B{Check Zone}
    B -->|Zone 6a| C[Select Plants]
    B -->|Zone 7b| D[Select Plants]
    C --> E[Add to Garden]
    D --> E
```

**Example - Sequence Diagram:**

```mermaid
sequenceDiagram
    User->>System: Search for tomato
    System->>Database: Query plants
    Database-->>System: Return results
    System-->>User: Display plants
```

**Example - Class Diagram:**

```mermaid
classDiagram
    class Plant {
        +String commonName
        +String scientificName
        +String hardinessZone
        +Boolean isDroughtTolerant
        +getPlantInfo()
    }
    class Profile {
        +User user
        +List plants
        +addPlant()
        +removePlant()
    }
    Profile --> Plant : contains
```

**Supported Diagram Types:**

- Flowcharts (`graph`)
- Sequence diagrams (`sequenceDiagram`)
- Class diagrams (`classDiagram`)
- State diagrams (`stateDiagram`)
- Entity Relationship diagrams (`erDiagram`)
- Gantt charts (`gantt`)
- Pie charts (`pie`)
- Git graphs (`gitGraph`)

---

## Content Organization Extensions

### `pymdownx.tabbed` - Tabbed Content

Create tabbed content blocks for organizing related information.

**Example:**

```markdown
=== "Web Interface"
    Access the plant search from the main navigation menu.

=== "Mobile App"
    Tap the search icon in the bottom navigation bar.

=== "API"
    ```bash
    curl https://api.example.com/plants?zone=6a
    ```
```

**Renders as:**

=== "Web Interface"
    Access the plant search from the main navigation menu.

=== "Mobile App"
    Tap the search icon in the bottom navigation bar.

=== "API"
    ```bash
    curl https://api.example.com/plants?zone=6a
    ```

---

## Admonitions & Callouts

### `admonition` - Callout Boxes

Create attention-grabbing callout boxes as per [here](https://squidfunk.github.io/mkdocs-material/reference/admonitions).

**Available Types:**

!!! note "Note"
    This is a note - use for general information.

!!! tip "Tip"
    This is a tip - use for helpful suggestions.

!!! warning "Warning"
    This is a warning - use for important caveats.

!!! danger "Danger"
    This is a danger alert - use for critical warnings.

!!! example "Example"
    This is an example - use for code examples or demonstrations.

!!! quote "Quote"
    This is a quote - use for citations or references.

!!! success "Success"
    This is a success message - use for confirmations.

!!! info "Information"
    This is an info box - use for supplementary information.

!!! question "Question"
    This is a question - use for FAQs or clarifications.

!!! bug "Bug"
    This is a bug alert - use for known issues.

**Syntax:**
```markdown
!!! note "Custom Title"
    Content goes here.
    Can be multiple paragraphs.
```

**Custom Plant Tip** (with custom CSS):
```markdown
!!! plant-tip "Plant Tip"
    Tomatoes need 6-8 hours of full sun daily.
```

### `pymdownx.details` - Collapsible Admonitions

Make admonitions collapsible to save space.

**Example:**
```markdown
??? question "How do I determine my USDA zone?"
    Click here to expand and see the answer.

    Your USDA hardiness zone is based on your location's average annual minimum temperature.
```

**Renders as:**

??? question "How do I determine my USDA zone?"
    Click here to expand and see the answer.

    Your USDA hardiness zone is based on your location's average annual minimum temperature.

**Start Expanded:**

```markdown
???+ tip "Pro Tip"
    This starts open but can be collapsed.
```


**Renders as:**

???+ tip "Pro Tip"
    This starts open but can be collapsed.

---

## Table Extensions

### `tables` - Enhanced Tables

Create beautiful, responsive tables.

**Example:**
```markdown
| Plant | Zone | Sun | Water |
|-------|------|-----|-------|
| Tomato | 3-11 | Full | Medium |
| Lettuce | 2-11 | Partial | High |
| Basil | 10-11 | Full | Medium |
```

**Renders as:**

| Plant | Zone | Sun | Water |
|-------|------|-----|-------|
| Tomato | 3-11 | Full | Medium |
| Lettuce | 2-11 | Partial | High |
| Basil | 10-11 | Full | Medium |

**Alignment:**
```markdown
| Left-aligned | Center-aligned | Right-aligned |
|:-------------|:--------------:|--------------:|
| Content      | Content        | Content       |
```

### `mkdocs-table-reader-plugin` - Import Tables from External Files

Note that even after installing `mkdocs-table-reader-plugin` you may still be asked to install:

- `openpyxl`
- `xlrd`

View this extension's documentation [here](https://timvink.github.io/mkdocs-table-reader-plugin/). Learn how to use it to create reproducible reports via [here](https://timvink.nl/blog/reproducible-reports-with-mkdocs/).

Include tables directly from CSV, Excel, or other data files into your documentation.

**Installation:**

```bash
uv add mkdocs-table-reader-plugin
```

**Configuration in mkdocs.yml:**

```yaml
plugins:
  - table-reader
```

**Basic Usage - CSV Files:**

{% raw %}
```markdown
{{ read_csv('path/to/data.csv') }}
```
{% endraw %}

**Basic Usage - Excel Files:**

{% raw %}
```markdown
{{ read_excel('path/to/spreadsheet.xlsx') }}
```
{% endraw %}

**Read Specific Excel Sheet:**

{% raw %}
```markdown
{{ read_excel('path/to/spreadsheet.xlsx', sheet_name='Sheet1') }}
```
{% endraw %}

**Advanced Options:**

{% raw %}
```markdown
<!-- Include only specific columns -->
{{ read_csv('data.csv', usecols=['Name', 'Zone', 'Type']) }}

<!-- Skip rows -->
{{ read_csv('data.csv', skiprows=2) }}

<!-- Use specific encoding -->
{{ read_csv('data.csv', encoding='utf-8') }}

<!-- Read Excel with specific range -->
{{ read_excel('data.xlsx', sheet_name='Plants', usecols='A:D') }}
```
{% endraw %}

**Example - Decision Matrix:**

{% raw %}
```markdown
## Project Decisions

The following decision matrix was used to evaluate our options:

{{ read_excel('../../decisions/CESYS524_decision-matrix.xlsx') }}
```
{% endraw %}

**Features:**

- Automatically converts CSV/Excel to markdown tables
- Supports pandas DataFrame operations
- Updates automatically when source files change
- No need to manually maintain duplicate table data
- Supports filtering, column selection, and formatting

**Use Cases:**

- Decision matrices and trade-off analyses
- Quality Function Deployment (QFD) matrices
- FMEA (Failure Mode and Effects Analysis) tables
- N-squared charts and interface matrices
- Any tabular data stored in external files

**Learn More:** [mkdocs-table-reader-plugin Documentation](https://timvink.github.io/mkdocs-table-reader-plugin/)

---

## Styling Extensions

### `attr_list` - Add CSS Classes

Add custom CSS classes and attributes to elements.

**Example:**

```markdown
![Plant Image](path/to/image.jpg){ .plant-image }

{.zone-badge}
Zone 6a
```

### `md_in_html` - Markdown Inside HTML

Use markdown syntax inside HTML blocks.

!!! warning "CRITICAL: Must Add `markdown` Attribute"
    By default, markdown is **NOT** processed inside HTML block elements like `<div>`.
    You MUST add the `markdown` attribute to enable processing.

**❌ WRONG - Markdown not processed:**

```html
<div style="border: 2px solid gray;">
# This Won't Render as H1
**This won't be bold**
</div>
```

**✅ CORRECT - Add `markdown` attribute:**

```html
<div markdown style="border: 2px solid gray;">

# This Renders as H1

**This is bold**

</div>
```

**Requirements:**

1. Add `markdown` attribute to the opening tag
2. Add blank line after opening tag
3. Add blank line before closing tag
4. Markdown content must be properly formatted

**Example with Classes:**

```html
<div markdown class="feature-card custom-style">

## Feature Title

- Markdown list item
- Another item

</div>
```

**Inline vs Block Markdown:**

```html
<!-- Block-level markdown (headings, lists, paragraphs) -->
<div markdown style="padding: 20px;">

## Heading

Paragraph with **bold** and *italic*.

</div>

<!-- Inline markdown only -->
<div markdown="span">This is **inline** markdown only.</div>
```

**Real-world example:**

```html
<div markdown style="border: 2px solid #e5e7eb; border-radius: 8px; padding: 20px;">

# Plant Database

**Purpose:** Plant data model and storage

**Status:** Approved

</div>
```

### `pymdownx.emoji` - Emoji Support

Use emojis via shortcodes.

**Examples:**
- `:seedling:` → 🌱
- `:sunflower:` → 🌻
- `:cactus:` → 🌵
- `:herb:` → 🌿
- `:bouquet:` → 💐
- `:cherry_blossom:` → 🌸

**Search emojis:** [Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet)

---

## Task List Extensions

### `pymdownx.tasklist` - Interactive Checkboxes

Create task lists with checkboxes.

**Example:**
```markdown
- [x] Choose planting location
- [x] Test soil pH
- [ ] Purchase seeds
- [ ] Plant seeds
- [ ] Water regularly
```

**Renders as:**

- [x] Choose planting location
- [x] Test soil pH
- [ ] Purchase seeds
- [ ] Plant seeds
- [ ] Water regularly

---

## List Extensions

### `def_list` - Definition Lists

Create glossary-style definition lists.

**Example:**

```markdown
USDA Hardiness Zone
:   A geographic area defined by average annual minimum temperature, used to determine which plants can survive in a location.

Full Sun
:   6 or more hours of direct sunlight per day.

Partial Shade
:   3-6 hours of direct sunlight per day.
```

**Renders as:**

USDA Hardiness Zone
:   A geographic area defined by average annual minimum temperature, used to determine which plants can survive in a location. (See [abbreviations](#abbr---abbreviations) to see why USDA is special here.)

Full Sun
:   6 or more hours of direct sunlight per day.

Partial Shade
:   3-6 hours of direct sunlight per day.

---

## Reference Extensions

### `abbr` - Abbreviations

Define abbreviations with tooltips.

**Example:**
```markdown
The USDA defines plant hardiness zones.

*[USDA]: United States Department of Agriculture
```

When you hover over "USDA", you'll see the full definition like in this line.
*[USDA]: United States Department of Agriculture

Should you decide to do this, remember it might be best to put them at the bottom. It is untested about if the last definition updates all or only the most recent. (If you have them all at the end, you can alphabetize to know what ones you do have.)

### `footnotes` - Footnotes

Add footnotes to content. (They will appear at the bottom of your document - just like gootnotes.)

**Example:**
```markdown
Plants in zone 6a can survive temperatures down to -10°F[^1].

[^1]: USDA Plant Hardiness Zone Map, 2012 revision
```

**Renders as:**

Plants in zone 6a can survive temperatures down to -10°F[^1].

[^1]: USDA Plant Hardiness Zone Map, 2012 revision

---

## Typography Extensions

### `pymdownx.smartsymbols` - Smart Symbols

Automatically converts text to proper symbols.

**Conversions:**

- `(c)` → ©
- `(r)` → ®
- `(tm)` → ™
- `c/o` → ℅
- `+/-` → ±
- `-->` → →
- `<--` → ←
- `<-->` → ↔
- `=/=` → ≠

### `pymdownx.keys` - Keyboard Keys

Display keyboard shortcuts beautifully.

**Example:**

```markdown
Press ++ctrl+alt+delete++ to restart.
Press ++cmd+s++ to save.
```

**Renders as:**

Press ++ctrl+alt+delete++ to restart.

---

## Review Extensions

### `pymdownx.critic` - Track Changes

Mark up content for review with track-changes style markup.

**Syntax:**

<pre><code>This is &#123;--deleted text--&#125;.
This is &#123;++added text++&#125;.
This is &#123;~~old~&gt;new~~&#125; text.
This is &#123;==highlighted==&#125; text.
&#123;&gt;&gt;This is a comment&lt;&lt;&#125;
</code></pre>

**Renders as:**

```markdown
This is {--deleted text--}.
This is {++added text++}.
This is {~~old~>new~~} text.
This is {==highlighted==} text.
{>>This is a comment<<}
```

---

## Math Extensions

### `pymdownx.arithmatex` - Mathematical Expressions

Write mathematical formulas using LaTeX syntax.

**Inline Math:**
```markdown
The area of a circle is $A = \pi r^2$.
```

**Block Math:**
```markdown
$$
\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$
```

**Example - Growing Calculations:**
```markdown
Plant spacing: $S = \frac{L}{n-1}$ where L is length and n is number of plants.
```

---

## Best Practices

### When to Use Each Extension

**Admonitions:**

- Use `note` for general information
- Use `warning` for important caveats
- Use `tip` for helpful suggestions
- Use `example` for code demonstrations

**Diagrams:**

- Use flowcharts for process flows
- Use sequence diagrams for API interactions
- Use class diagrams for data models
- Use entity-relationship diagrams for database schemas

**Tabs:**

- Use for multiple implementations (web vs mobile)
- Use for different user roles (admin vs user)
- Use for multiple code examples (Python vs JavaScript)

**Tables:**

- Use for structured data (plant characteristics)
- Use for comparison (feature matrices)
- Keep tables simple - complex tables are hard to read on mobile

### Accessibility Considerations

1. **Always provide alt text for images:**

   ```markdown
   ![USDA Hardiness Zone Map showing zones 1a through 13b](path/to/image.jpg)
   ```

2. **Use semantic heading structure:**

    - Don't skip heading levels (h1 → h3)
    - Use h1 only once per page

3. **Make link text descriptive:**

    - ❌ `[Click here](link)` for more information
    - ✅ `[Learn about USDA zones](link)` for detailed information

4. **Use proper table headers:**

   ```markdown
   | Plant Name | Zone | Spacing |
   |------------|------|---------|
   | Tomato     | 3-11 | 24-36"  |
   ```

---

## Image Processing (Quick Reference)

This documentation uses two plugins for optimal image handling.

### Automatic Image Optimization

All images are automatically compressed during build - no special syntax needed.

**Just add images normally:**

```markdown
![Plant Diagram](img/plant-structure.png)
```

The optimize plugin automatically:

- Compresses PNG/JPG files (30-70% size reduction)
- Strips metadata
- Generates WebP versions
- Caches results for faster rebuilds

### Click-to-Zoom Lightbox

All images automatically get click-to-zoom functionality.

**Basic usage (auto-enabled):**

```markdown
![Tomato Plant](img/tomato.jpg)
```

Click image to open lightbox. Use arrow keys or swipe to navigate.

**Disable lightbox for specific images:**

```markdown
![Small Icon](img/icon.png){ .skip-lightbox }
```

<!-- **Create image gallery:**

```markdown
![Stage 1](img/stage1.jpg)
![Stage 2](img/stage2.jpg)
![Stage 3](img/stage3.jpg)
```

Multiple images become a navigable gallery. Click any image, then use ← → arrows or swipe.

For example, here is the gallery of the FFBDs as of Dec 2025:

![F.0 - Overall System Operations](../../img/FFBDs/F.0-Overall_System_Ops.png)
![F.1 - System Initialization](../../img/FFBDs/F.1-Sys_Init.png)
![F.2 - User Choice Loop](../../img/FFBDs/F.2-Usr_Choice_Loop.png)
![F.2.1 - General User Functions](../../img/FFBDs/F.2.1-Gen_Usr_Funcs.png)
![F.2.1.1](../../img/FFBDs/F.2.1.1-Access_Plant_Search.png)
![F.2.1.1.4 - Select Plant](../../img/FFBDs/F.2.1.1.4-Select_Plant.png)
![F.F.2.1.5 - Access Settings](../../img/FFBDs/F.2.1.5-Access_Settings.png)
![F.2.1c.1 - Plant Search & Filter](../../img/FFBDs/F.2.1c.1-Plant_SearchFilter.png) -->

**Keyboard shortcuts in lightbox:**

- `←` / `→` - Navigate gallery
- `Esc` - Close
- `+` / `-` - Zoom in/out

!!! info "Installation & Configuration"
    For setup instructions, system dependencies, and troubleshooting, see:
    **[Image Processing Setup Guide](image-processing-setup.md)**

---

## Custom Extensions (Project-Specific)

### Zone Badges

Use custom CSS class for zone badges:

```html
<span class="zone-badge">Zone 6a</span>
```

### Status Badges

Use for requirement/specification status:

```html
<div class="status-badge draft">Draft</div>
<div class="status-badge review">In Review</div>
<div class="status-badge approved">Approved</div>
<div class="status-badge implemented">Implemented</div>
```

### Feature Cards

Use for highlighting features:

```html
<div class="feature-card">

## Plant Search

Search thousands of plants by name, zone, characteristics, and more.

</div>
```

See more with the [requirements index example](../../requirements/requirements-index-example.md).

---

## Additional Resources

- [Material for MkDocs Reference](https://squidfunk.github.io/mkdocs-material/reference/)
- [PyMdown Extensions Documentation](https://facelessuser.github.io/pymdown-extensions/)
- [Python Markdown Documentation](https://python-markdown.github.io/)
- [Mermaid Live Editor](https://mermaid.live/) - Test diagrams

---

## Need Help?

If you're unsure which extension to use, refer to this decision tree:

```mermaid
flowchart TD
    A["What do you need?"] --> B{"Content Type"}
    B -->|"Diagram"| C["Use Mermaid"]
    B -->|"Code"| D["Use highlight or superfences"]
    B -->|"Important Info"| E["Use admonition"]
    B -->|"Organize Options"| F["Use tabs"]
    B -->|"Structured Data"| G["Use table"]
    B -->|"Definition"| H["Use def_list"]
    B -->|"Track Changes"| I["Use critic"]
```

---

**Maintained By:** Gardening App Documentation Team
