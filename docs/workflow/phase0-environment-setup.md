---
title: "Phase 0: Environment Setup"
description: Set up the development environment with UV package manager
created: 2025-12-30
updated: 2025-12-31
status: implemented
---

# Phase 0: Environment Setup

Set up the development environment with UV package manager.

## Command

```bash
/setup-env
```

## What it does

- Creates UV virtual environment (`.venv/`)
- Installs dependencies from `pyproject.toml`
- Verifies installation

## Related Documentation

### Instructions

- **UV Environment Setup**: `.github/instructions/uv-environment-setup.instructions.md`

### Tutorials

- **[Dependency Management Guide](../tutorials/general/dependency-management.md)** - Complete guide to using UV for package management
- **[Makefile Guide](../tutorials/general/makefile-guide.md)** - Development workflow commands (`make install`, `make test`, etc.)
- **[MkDocs Installation](../tutorials/mkdocs/mkdocs-installation.md)** - Setting up documentation environment

### Archived References

- **[UVX Setup Guide](../tutorials/general/archive/uvx-setup-guide.md)** - Original setup approach (archived for reference)

## Status

✅ Documented | 🎯 All setup tools and workflows documented
