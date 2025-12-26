---
title: MkDocs Installation Guide
description: Complete installation guide for MkDocs Material and all required plugins
---

# MkDocs Installation Guide

This guide walks you through installing MkDocs Material theme and all required plugins for this documentation site.

---

## Prerequisites

Before starting, ensure you have:

- [x] **Python 3.8 or higher** installed
- [x] **uv** package manager installed
- [x] **Git** installed (for git-revision-date plugin)
- [x] Virtual environment activated

**Verify your setup:**
```bash
python --version     # Should be 3.8+
uv --version        # Should show uv version
git --version       # Should show git version
```

---

## Installation Steps

### Step 1: Install MkDocs Material Theme

The Material theme is the foundation of this documentation site.

```bash
uv add mkdocs-material
```

**Expected output:**
```
Resolved XX packages in XXXms
Installed X packages in X.XXs
 + mkdocs-material==X.X.X
 + mkdocs==X.X.X
 + ... (other dependencies)
```

**Verify installation:**
```bash
mkdocs --version
```

Should show: `mkdocs, version X.X.X from ... (Python 3.X)`

---

### Step 2: Install Required Plugins

Install all plugins used in `mkdocs.yml`:

#### 2.1 Minify Plugin (HTML/CSS/JS optimization)

```bash
uv add mkdocs-minify-plugin
```

**What it does:** Minifies HTML, CSS, and JavaScript for faster page loading.

#### 2.2 Git Revision Date Plugin (Last updated dates)

```bash
uv add mkdocs-git-revision-date-localized-plugin
```

**What it does:** Shows "last updated" dates on pages based on git commit history.

**Requirement:** Your documentation must be in a git repository.

#### 2.3 Glightbox Plugin (Image lightbox)

```bash
uv add mkdocs-glightbox
```

**What it does:** Adds click-to-zoom functionality and image galleries.

#### 2.4 Material Imaging (Image optimization)

```bash
uv add "mkdocs-material[imaging]"
```

**What it does:** Compresses images, generates WebP versions, optimizes page load.

**Additional requirements:** System dependencies (see Step 3)

---

### Step 3: Install System Dependencies (For Image Optimization)

The Material imaging plugin requires system libraries.

=== "Windows"

    **Install MSYS2:**

    1. Download from [msys2.org](https://www.msys2.org/)
    2. Run installer with default options
    3. Open **MSYS2 UCRT64** terminal (blue icon)

    **Update MSYS2:**
    ```bash
    pacman -Syu
    ```

    If terminal closes, reopen and run:
    ```bash
    pacman -Su
    ```

    **Install Cairo Graphics and pngquant:**
    ```bash
    pacman -S mingw-w64-ucrt-x86_64-cairo mingw-w64-ucrt-x86_64-pngquant
    ```

    !!! note "Dependencies Installed Automatically"
        The `cairo` package automatically installs: freetype, libffi, libjpeg-turbo, libpng, and zlib as dependencies.

    **Add to PATH:**
    1. Open Windows Settings → System → About → Advanced system settings
    2. Environment Variables → Edit "Path" under User variables
    3. Add: `C:\msys64\ucrt64\bin`
    4. **Restart terminal/VS Code**

    **Verify:**
    ```bash
    pngquant --version
    ```

=== "macOS"

    **Install Homebrew** (if not installed):
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

    **Install image processing libraries:**
    ```bash
    brew install cairo freetype libffi libjpeg libpng zlib pngquant
    ```

    **Verify:**
    ```bash
    pngquant --version
    ```

=== "Linux (Ubuntu/Debian)"

    **Update package list:**
    ```bash
    sudo apt-get update
    ```

    **Install image processing libraries:**
    ```bash
    sudo apt-get install libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev pngquant
    ```

    **Verify:**
    ```bash
    pngquant --version
    ```

=== "Linux (RHEL/CentOS/Fedora)"

    **Install image processing libraries:**
    ```bash
    sudo yum install cairo-devel freetype-devel libffi-devel libjpeg-devel libpng-devel zlib-devel pngquant
    ```

    **Verify:**
    ```bash
    pngquant --version
    ```

---

### Step 4: Create Custom CSS File

The configuration references a custom stylesheet that needs to exist.

```bash
# Create directories
mkdir -p docs/stylesheets

# Create empty CSS file (we'll add styles later)
touch docs/stylesheets/extra.css
```

Or on Windows (PowerShell):
```powershell
New-Item -Path "gardening-docs\docs\stylesheets" -ItemType Directory -Force
New-Item -Path "gardening-docs\docs\stylesheets\extra.css" -ItemType File
```

---

### Step 5: Verify Installation

Test that everything is installed correctly:

```bash
cd gardening-docs
mkdocs build
```

**Expected output:**
```
INFO    -  Cleaning site directory
INFO    -  Building documentation to directory: D:\...\site
INFO    -  Documentation built in X.XX seconds
```

**If successful, serve locally:**
```bash
mkdocs serve
```

**Expected output:**
```
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Documentation built in X.XX seconds
INFO    -  [XX:XX:XX] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [XX:XX:XX] Serving on http://127.0.0.1:8000/
```

Open browser to `http://127.0.0.1:8000/` to view the documentation.

---

## Complete Installation Command List

For quick reference, here are all installation commands:

```bash
# Python packages
uv add mkdocs-material
uv add mkdocs-minify-plugin
uv add mkdocs-git-revision-date-localized-plugin
uv add mkdocs-glightbox
uv add "mkdocs-material[imaging]"

# Create CSS directory and file
mkdir -p docs/stylesheets
touch docs/stylesheets/extra.css

# System dependencies (platform-specific - see Step 3 above)

# Verify
cd gardening-docs
mkdocs build
mkdocs serve
```

---

## Troubleshooting

### Common Installation Issues

??? question "ERROR: 'minify' plugin not found"
    **Problem:** mkdocs-minify-plugin not installed

    **Solution:**
    ```bash
    uv add mkdocs-minify-plugin
    ```

??? question "ERROR: 'git-revision-date-localized' plugin not found"
    **Problem:** Git revision date plugin not installed

    **Solution:**
    ```bash
    uv add mkdocs-git-revision-date-localized-plugin
    ```

??? question "ERROR: 'glightbox' plugin not found"
    **Problem:** Glightbox plugin not installed

    **Solution:**
    ```bash
    uv add mkdocs-glightbox
    ```

??? question "ERROR: 'optimize' plugin not found"
    **Problem:** Material imaging extra not installed

    **Solution:**
    ```bash
    uv add "mkdocs-material[imaging]"
    ```

??? question "Build fails with 'cairo' error"
    **Problem:** Cairo Graphics not installed or not in PATH

    **Solution:** See Step 3 for platform-specific Cairo installation

??? question "ERROR: Config file 'stylesheets/extra.css' does not exist"
    **Problem:** Custom CSS file doesn't exist

    **Solution:**
    ```bash
    mkdir -p docs/stylesheets
    touch docs/stylesheets/extra.css
    ```

??? question "uv: command not found"
    **Problem:** uv package manager not installed

    **Solution:**
    ```bash
    # Install uv
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # Or on Windows (PowerShell):
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

??? question "Git revision dates not showing"
    **Problem:** Not in a git repository or no commits

    **Solution:**
    ```bash
    # Initialize git if needed
    git init

    # Make initial commit
    git add .
    git commit -m "Initial commit"
    ```

---

## Optional Enhancements

### Install Mike for Version Management

If you want to host multiple documentation versions (v1.0, v2.0, etc.):

```bash
uv add mike
```

**Usage:**
```bash
# Deploy version 1.0
mike deploy 1.0 latest --update-aliases

# Deploy version 2.0
mike deploy 2.0 latest --update-aliases

# Serve versioned docs
mike serve
```

### Install Additional Extensions

Add more functionality as needed:

```bash
# PDF export
uv add mkdocs-pdf-export-plugin

# Macros for variables in markdown
uv add mkdocs-macros-plugin

# Include markdown files
uv add mkdocs-include-markdown-plugin
```

---

## Development Workflow

Once installed, your typical workflow:

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Unix/Mac

# 2. Navigate to docs directory
cd gardening-docs

# 3. Start development server
mkdocs serve

# 4. Edit documentation files
# Server auto-reloads on file changes

# 5. Build for production
mkdocs build

# 6. Deploy to GitHub Pages (optional)
mkdocs gh-deploy
```

---

## Keeping Dependencies Updated

Update all packages periodically:

```bash
# Update all packages
uv sync --upgrade

# Or update specific package
uv add --upgrade mkdocs-material
```

**Check for outdated packages:**
```bash
uv pip list --outdated
```

---

## Package Reference

| Package | Purpose | Required? |
|---------|---------|-----------|
| `mkdocs-material` | Material theme | ✅ Required |
| `mkdocs-minify-plugin` | Minify HTML/CSS/JS | ✅ Required |
| `mkdocs-git-revision-date-localized-plugin` | Show update dates | ✅ Required |
| `mkdocs-glightbox` | Image lightbox | ✅ Required |
| `mkdocs-material[imaging]` | Image optimization | ✅ Required |
| Cairo Graphics (system) | Image processing | ✅ Required |
| pngquant (system) | PNG compression | ✅ Required |
| `mike` | Version management | ⚪ Optional |

---

## Next Steps

After successful installation:

1. ✅ **Read the extensions guide:** [MkDocs Extensions Guide](mkdocs-extensions-guide.md)
2. ✅ **Set up image processing:** [Image Processing Setup](image-processing-setup.md)
3. ✅ **Start writing documentation:** Edit files in `docs/`
4. ✅ **Customize styling:** Edit `docs/stylesheets/extra.css`
5. ✅ **Configure theme:** Modify `mkdocs.yml`

---

## Additional Resources

- [MkDocs Official Documentation](https://www.mkdocs.org/)
- [Material for MkDocs Documentation](https://squidfunk.github.io/mkdocs-material/)
- [UV Package Manager Documentation](https://github.com/astral-sh/uv)
- [MSYS2 Documentation](https://www.msys2.org/) (Windows users)
- [Homebrew Documentation](https://brew.sh/) (macOS users)

---

**Last Updated:** 2025-12-12
**Maintained By:** Gardening App Documentation Team
