---
title: Image Processing Setup Guide
description: Complete guide to setting up image optimization and lightbox features for MkDocs
---

# Image Processing Setup Guide

This guide shows you how to set up both image processing plugins for optimal image handling in your MkDocs documentation.

---

## Overview

We use **two complementary plugins** for complete image handling:

| Plugin | Purpose | Features |
|--------|---------|----------|
| **Material's optimize** | Image optimization | Compression, WebP conversion, responsive sizes |
| **glightbox** | Interactive viewing | Click-to-zoom, galleries, lightbox, navigation |

**Both plugins are FREE** and work together seamlessly.

---

## Prerequisites

Before starting, ensure you have:

- [x] Python 3.8 or higher installed
- [x] `uv` package manager installed
- [x] MkDocs Material theme installed
- [x] Virtual environment activated

```bash
# Verify your setup
python --version
uv --version
```

---

## Installation Overview

**Quick Summary:**
```bash
# 1. Install Python packages
uv add "mkdocs-material[imaging]"
uv add mkdocs-glightbox

# 2. Install system dependencies (see platform-specific sections below)
# Windows: Use MSYS2
# macOS: Use Homebrew
# Linux: Use apt/yum/zypper

# 3. Verify installation
mkdocs build
```

---

## Part 1: Material's Image Optimization

### Step 1: Install Python Package

The Material imaging extra includes **Pillow** and **CairoSVG**:

```bash
uv add "mkdocs-material[imaging]"
```

**Expected output:**
```
Resolved XX packages in XXXms
Installed 3 packages in X.XXs
 + pillow==X.X.X
 + cairosvg==X.X.X
 + cssselect2==X.X.X
```

### Step 2: Install System Dependencies

Material's optimize plugin requires two system libraries:

1. **Cairo Graphics** - Image rendering and processing
2. **pngquant** - PNG compression

Installation varies by platform:

=== "Windows"

    ### Windows Installation (MSYS2)

    **Install MSYS2** (if not already installed):

    1. Download installer from [msys2.org](https://www.msys2.org/)
    2. Run installer and follow default options
    3. Open **MSYS2 UCRT64** terminal (NOT MinGW or MSYS)

    !!! warning "Important: Use UCRT64 Terminal"
        Make sure you use the **MSYS2 UCRT64** terminal (blue icon), not the MinGW64 (purple) or MSYS (brown) terminals. The package names are different for each environment.

    **Update MSYS2:**
    ```bash
    pacman -Syu
    ```

    If terminal closes, reopen and run again:
    ```bash
    pacman -Su
    ```

    **Install Cairo Graphics and pngquant:**
    ```bash
    pacman -S mingw-w64-ucrt-x86_64-cairo mingw-w64-ucrt-x86_64-pngquant
    ```

    !!! note "Dependencies Installed Automatically"
        The `cairo` package automatically installs: freetype, libffi, libjpeg-turbo, libpng, and zlib.

    **Add to PATH (Critical!):**

    1. Find MSYS2 bin directory (usually `C:\msys64\ucrt64\bin`)
    2. Open Windows Settings → System → About → Advanced system settings
    3. Click "Environment Variables"
    4. Under "User variables", find "Path" and click "Edit"
    5. Click "New" and add: `C:\msys64\ucrt64\bin`
    6. Click OK on all dialogs
    7. **Restart your terminal/VS Code** for PATH changes to take effect

    **Verify installation:**

    Open a **new** Command Prompt or PowerShell window:
    ```bash
    pngquant --version
    ```

    Expected output: `2.X.X (XXXX)`

    !!! tip "Troubleshooting Windows Installation"
        **Problem**: `pngquant: command not found`

        **Solutions**:
        1. Verify you added `C:\msys64\ucrt64\bin` to PATH
        2. Restart your terminal/VS Code completely
        3. Check the path exists: `dir C:\msys64\ucrt64\bin\pngquant.exe`
        4. Try running with full path: `C:\msys64\ucrt64\bin\pngquant.exe --version`

=== "macOS"

    ### macOS Installation (Homebrew)

    **Install Homebrew** (if not already installed):
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

    **Install Cairo Graphics:**
    ```bash
    brew install cairo freetype libffi libjpeg libpng zlib
    ```

    **Install pngquant:**
    ```bash
    brew install pngquant
    ```

    **Verify installation:**
    ```bash
    pngquant --version
    ```

=== "Linux (Ubuntu/Debian)"

    ### Linux Installation (apt)

    **Update package list:**
    ```bash
    sudo apt-get update
    ```

    **Install image processing libraries:**
    ```bash
    sudo apt-get install libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev pngquant
    ```

    **Verify installation:**
    ```bash
    pngquant --version
    ```

=== "Linux (RHEL/CentOS/Fedora)"

    ### Linux Installation (yum)

    **Install image processing libraries:**
    ```bash
    sudo yum install cairo-devel freetype-devel libffi-devel libjpeg-devel libpng-devel zlib-devel pngquant
    ```

    **Verify installation:**
    ```bash
    pngquant --version
    ```

### Step 3: Configure in mkdocs.yml

The optimize plugin is already configured in your `mkdocs.yml`:

```yaml
plugins:
  - optimize:
      enabled: true
      cache: true
      cache_dir: .cache/plugins/optimize
      optimize_png: true           # Compress PNG images
      optimize_png_speed: 4        # 1 (slow/best) to 10 (fast/ok)
      optimize_png_strip: true     # Remove metadata
      optimize_jpg: true           # Compress JPG images
      optimize_jpg_quality: 85     # Quality 0-100
      optimize_jpg_progressive: true
```

**Configuration Options:**

| Option | Default | Description |
|--------|---------|-------------|
| `enabled` | `true` | Enable/disable plugin |
| `cache` | `true` | Cache optimized images |
| `cache_dir` | `.cache/plugins/optimize` | Cache location |
| `optimize_png` | `true` | Enable PNG compression |
| `optimize_png_speed` | `4` | Compression speed (1-10) |
| `optimize_png_strip` | `true` | Remove PNG metadata |
| `optimize_jpg` | `true` | Enable JPG compression |
| `optimize_jpg_quality` | `60` | JPG quality (0-100) |
| `optimize_jpg_progressive` | `true` | Progressive JPG |

### Step 4: Test Image Optimization

Create a test page with images:

```markdown
# Test Image Optimization

![Large Test Image](img/test-large.png)

This image will be automatically:
- Compressed
- Converted to WebP (if supported by browser)
- Stripped of metadata
```

**Build and verify:**
```bash
cd gardening-docs
mkdocs build
```

Check the `site/img/` directory - you should see optimized versions of your images.

---

## Part 2: Glightbox Interactive Lightbox

### Step 1: Install Glightbox Plugin

```bash
uv add mkdocs-glightbox
```

**Expected output:**
```
Resolved XX packages in XXXms
Installed 1 package in X.XXs
 + mkdocs-glightbox==X.X.X
```

### Step 2: Configure in mkdocs.yml

The glightbox plugin is already configured:

```yaml
plugins:
  - glightbox:
      touchNavigation: true        # Swipe to navigate on mobile
      loop: false                  # Don't loop through gallery
      effect: zoom                 # Zoom animation effect
      slide_effect: slide          # Slide between images
      width: 100%
      height: auto
      zoomable: true               # Allow zoom controls
      draggable: true              # Drag to pan zoomed images
      auto_caption: false          # Don't auto-generate captions
      caption_position: bottom     # Caption position if enabled
```

**Configuration Options:**

| Option | Default | Description |
|--------|---------|-------------|
| `touchNavigation` | `true` | Swipe on mobile |
| `loop` | `false` | Loop through images |
| `effect` | `zoom` | Open animation (zoom/fade/none) |
| `slide_effect` | `slide` | Navigation effect |
| `zoomable` | `true` | Enable zoom controls |
| `draggable` | `true` | Drag zoomed images |
| `auto_caption` | `false` | Auto-generate captions from alt text |

### Step 3: Use Lightbox in Documentation

**Basic image (auto-enabled):**
```markdown
![Plant Image](img/plant.jpg)
```

Click the image to open lightbox view.

**Image with caption:**
```markdown
![Tomato plant showing healthy growth](img/tomato.jpg)
```

When `auto_caption: true`, the alt text becomes the caption.

**Disable lightbox for specific image:**
```markdown
![Icon](img/icon.png){ .skip-lightbox }
```

**Create image gallery:**
```markdown
![Plant 1](img/plant1.jpg)
![Plant 2](img/plant2.jpg)
![Plant 3](img/plant3.jpg)
```

Images on the same page become a navigable gallery.

---

## Verification & Testing

### Test Both Plugins Together

Create `docs/test-images.md`:

```markdown
---
title: Image Processing Test
---

# Image Processing Test

## Test 1: Single Image

![USDA Hardiness Zone Map](./diagrams/REQ000/context-main.jpg)

Click the image above to test lightbox functionality.

## Test 2: Image Gallery

![Context Diagram 1](../../diagrams/REQ000/context-main.jpg)
![Context Diagram 2](img/context-diagrams/community-gardener.jpg)

Click images and use arrow keys or swipe to navigate.

## Test 3: Optimized Small Images

![Favicon](img/favicon.ico){ .skip-lightbox }

Small images can skip lightbox with the `.skip-lightbox` class.
```

### Build and Test

```bash
cd gardening-docs
mkdocs build
mkdocs serve
```

Open browser to `http://127.0.0.1:8000/test-images/`

**Verify:**
- [x] Images load quickly (optimization working)
- [x] Clicking images opens lightbox (glightbox working)
- [x] Can zoom in/out on images
- [x] Arrow keys navigate between images
- [x] Mobile: Swipe gestures work

---

## Troubleshooting

### Common Issues

??? question "Build fails with 'cairo' error"
    **Problem**: Cairo Graphics not installed or not in PATH

    **Solution**:

    === "Windows"
        1. Verify MSYS2 UCRT64 terminal was used for installation
        2. Check PATH includes `C:\msys64\ucrt64\bin`
        3. Restart terminal/VS Code
        4. Reinstall: `pacman -S mingw-w64-ucrt-x86_64-cairo`

    === "macOS"
        ```bash
        brew reinstall cairo
        ```

    === "Linux"
        ```bash
        sudo apt-get install --reinstall libcairo2-dev
        ```

??? question "Build fails with 'pngquant' error"
    **Problem**: pngquant not installed or not in PATH

    **Solution**:

    === "Windows"
        ```bash
        # In MSYS2 UCRT64 terminal
        pacman -S mingw-w64-ucrt-x86_64-pngquant

        # Verify in Command Prompt
        pngquant --version
        ```

    === "macOS"
        ```bash
        brew install pngquant
        pngquant --version
        ```

    === "Linux"
        ```bash
        sudo apt-get install pngquant
        pngquant --version
        ```

??? question "Images not optimizing"
    **Problem**: Optimize plugin not processing images

    **Checks**:
    1. Verify plugin is enabled: `enabled: true`
    2. Clear cache: `rm -rf .cache/plugins/optimize`
    3. Rebuild: `mkdocs build --clean`
    4. Check build output for optimization messages

??? question "Lightbox not working"
    **Problem**: Clicking images doesn't open lightbox

    **Solutions**:
    1. Verify glightbox is installed: `uv pip list | grep glightbox`
    2. Check browser console for JavaScript errors
    3. Clear browser cache (Ctrl+Shift+R)
    4. Verify image has proper markdown syntax (not HTML `<img>` tag)

??? question "Images load slowly"
    **Problem**: Optimization not reducing file size enough

    **Solutions**:
    1. Lower `optimize_png_speed` to 1 (slower but better compression)
    2. Lower `optimize_jpg_quality` to 75 or 80
    3. Manually resize large images before adding to docs
    4. Use WebP format for new images

---

## Performance Tips

### Image Size Guidelines

| Image Type | Recommended Max Size | Format |
|------------|---------------------|--------|
| Screenshots | 1920x1080 | PNG → WebP |
| Photos | 1600x1200 | JPG (quality 85) |
| Diagrams | 1200x800 | PNG → WebP |
| Icons | 128x128 | PNG or SVG |
| Thumbnails | 400x300 | JPG (quality 80) |

### Optimization Best Practices

1. **Resize before adding**: Don't upload 4K images if you only need 1080p
2. **Choose right format**:
   - Photos/screenshots → JPG
   - Diagrams/logos → PNG
   - Icons → SVG (no optimization needed)
3. **Use descriptive alt text**: Good for accessibility and SEO
4. **Enable caching**: Speeds up repeated builds
5. **Test on mobile**: Verify images look good and load fast on mobile

### Cache Management

**Clear optimization cache:**
```bash
rm -rf gardening-docs/.cache/plugins/optimize
```

**Cache location in .gitignore:**
```
.cache/
```

The cache directory should already be in your `.gitignore`.

---

## Advanced Configuration

### Conditional Optimization

Only optimize in production builds:

```yaml
plugins:
  - optimize:
      enabled: !ENV [PRODUCTION, false]
```

Set when building for production:
```bash
PRODUCTION=true mkdocs build
```

### Custom Image Classes

Skip optimization for specific images:

```markdown
![Logo](img/logo.png){ .no-optimize }
```

Configure in mkdocs.yml:
```yaml
plugins:
  - optimize:
      exclude:
        - "*.svg"
        - "img/logos/*"
```

### Multiple Image Sizes

For responsive images, the optimize plugin automatically generates multiple sizes when using Material's image processing features.

---

## Next Steps

Now that image processing is set up:

1. ✅ Add images to your documentation
2. ✅ Test lightbox and optimization
3. ✅ Monitor build times (caching should help)
4. ✅ Check file sizes in `site/img/` directory

**Related Guides:**
- [MkDocs Extensions Guide](mkdocs-extensions-guide.md)
- [Material for MkDocs Documentation](https://squidfunk.github.io/mkdocs-material/)
- [Glightbox Documentation](https://github.com/blueswen/mkdocs-glightbox)

---

## Reference Commands

```bash
# Install both plugins
uv add "mkdocs-material[imaging]"
uv add mkdocs-glightbox

# Build with clean cache
mkdocs build --clean

# Serve locally
mkdocs serve

# Clear optimization cache
rm -rf .cache/plugins/optimize

# Verify system dependencies
pngquant --version
```

---

**Last Updated:** 2025-12-12
**Maintained By:** Gardening App Documentation Team
