---
title: Finding Your Extra Python Processes
description: Things learned in Windows processes to find python loop while troubleshooting this project.
---
# Finding Your Extra Python Processes

The lessons learned in this page were part of the troubleshooting process for learning how to built this site.

Sometimes you may start a process that never ends, even when your IDE closes. Linux has a similar system, but in Windows you can see what processes are running and make informed decisions about which ones to stop.

### The Problem: Identifying Running Python Processes

When you have multiple Python processes running, you need to identify which ones are important (IDE tools) vs. which ones you want to stop (like a stuck development server).

### Command 1: List All Python Processes

**Basic listing (shows only process names and IDs):**

```cmd
tasklist /FI "IMAGENAME eq python.exe"
```

**Output example:**
```
Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
python.exe                   27776 Console                    1     45,632 K
python.exe                   65964 Console                    1     42,108 K
python.exe                   52860 Console                    1     38,944 K
python.exe                    2416 Console                    1     41,220 K
```

**Problem:** You can't tell which process is which! They all look the same.

### Command 2: Show What Each Process Is Actually Running

**Advanced listing (shows full command line):**

```cmd
wmic process where "name='python.exe'" get CommandLine,ProcessId
```

**Output example:**
```
CommandLine                                                                                                                                             ProcessId
"c:\Program Files\Python\Python314\python.exe" c:\Users\gradu\.vscode\extensions\ms-python.black-formatter-2025.2.0\bundled\tool\lsp_server.py --stdio  27776
"c:\Program Files\Python\Python314\python.exe" c:\Users\gradu\.vscode\extensions\ms-python.flake8-2025.2.0\bundled\tool\lsp_server.py                   65964
"c:\Program Files\Python\Python314\python.exe" c:\Users\gradu\.vscode\extensions\ms-python.pylint-2025.2.0\bundled\tool\lsp_server.py                   52860
"c:\Program Files\Python\Python314\python.exe" c:\Users\gradu\.vscode\extensions\ms-python.mypy-type-checker-2025.2.0\bundled\tool\lsp_server.py        2416
```

**Now you can identify each process:**

- **PID 27776**: Black formatter (VS Code extension) ✅ Keep running
- **PID 65964**: Flake8 linter (VS Code extension) ✅ Keep running
- **PID 52860**: Pylint linter (VS Code extension) ✅ Keep running
- **PID 2416**: Mypy type checker (VS Code extension) ✅ Keep running

### Command 3: Find Specific Processes

**Search for a specific program (like MkDocs):**

```cmd
wmic process where "CommandLine like '%mkdocs%'" get CommandLine,ProcessId
```

This helps you find only the processes you're looking for, avoiding unnecessary noise.

### Critical Thinking: When to Kill Processes

**❌ DON'T blindly kill all Python processes:**

```cmd
REM BAD - Kills everything, including IDE tools!
taskkill /F /IM python.exe
```

**✅ DO investigate first, then selectively kill:**

1. **Identify** what each process is doing
2. **Decide** which ones are safe to stop
3. **Kill selectively** by PID:

```cmd
taskkill /F /PID 12345
```

Or better yet, **stop it gracefully** in the terminal where you started it (Ctrl+C).

---

## Case Study: MkDocs Infinite Refresh Loop

### The Problem

When running `mkdocs serve` with build hooks that modify watched files, you can get stuck in an infinite refresh loop:

1. **Hook runs** during build → modifies a file in `docs/`
2. **MkDocs sees** the file change → triggers rebuild
3. **Hook runs again** → modifies file again
4. **Loop repeats** forever! 🔄

### The Investigation

**Step 1: Recognize the symptom**
- Browser page constantly refreshes
- Terminal shows continuous rebuild messages
- Changes don't settle

**Step 2: Check your configuration**

Look at `mkdocs.yml` for hooks:

```yaml
hooks:
  - docs/hooks/priority_badges.py
  - docs/hooks/generate_req_index.py  # ⚠️ Generates files during build!
```

**Root cause:** The `generate_req_index.py` hook creates/modifies `docs/requirements/req-index.md` during every build, which triggers another build.

**Step 3: Verify MkDocs is running**

```cmd
REM Search for MkDocs process
wmic process where "CommandLine like '%mkdocs%'" get CommandLine,ProcessId
```

If found, you know it's running and causing the loop.

### The Solution

**Option 1: Stop auto-reload during development**

```cmd
mkdocs serve --no-livereload
```

- Prevents automatic page refresh
- Hooks still run on each manual build
- You manually refresh browser to see changes

**Option 2: Dirty builds (skip unchanged files)**

```cmd
mkdocs serve --dirty --no-livereload
```

- Faster builds
- Only rebuilds changed files
- Best for rapid development

**Option 3: Fix the hook (advanced)**

Modify the hook to only write if content actually changed:

```python
# Before writing
if new_content != old_content:
    file.write(new_content)  # Only write if different
```

This prevents unnecessary file modifications that trigger rebuilds.

### Lessons Learned

1. **Investigate before acting** - Don't kill all Python processes blindly
2. **Use detailed commands** - `wmic` with `CommandLine` shows what's really running
3. **Understand the system** - Know how MkDocs watches files and triggers rebuilds
4. **Choose the right tool** - Use `--no-livereload` when hooks modify watched files
5. **Document solutions** - Future you will thank present you! 📝

---

## Command 4: Clean MkDocs Build Directory

**Purpose:** Remove the `site/` directory to force a fresh build and clear any cached content.

**Command:**

```cmd
if exist site rmdir /s /q site
```

**Breakdown:**

- `if exist site` - Check if the `site` directory exists before trying to delete it
- `rmdir` - Remove directory command
- `/s` - Remove all subdirectories and files recursively (like `rm -rf` on Linux)
- `/q` - Quiet mode - don't prompt for confirmation
- `site` - The directory name (MkDocs default build output)

**When to use this:**

- ✅ Status indicators not updating after config changes
- ✅ CSS/JavaScript changes not appearing on deployment
- ✅ Stale content showing up
- ✅ Before deploying to ensure clean build
- ✅ Troubleshooting rendering issues

**Best practice:**

```cmd
REM Clean build directory, then rebuild
if exist site rmdir /s /q site && mkdocs build

REM But really it's the same as:
mkdocs build --clean

REM You should not do this because you cannot serve without site:
if exist site rmdir /s /q site && mkdocs serve
```

---

## Quick Reference

| Task | Command | Use Case |
|------|---------|----------|
| **List Python processes** | `tasklist /FI "IMAGENAME eq python.exe"` | See PIDs only |
| **Show what's running** | `wmic process where "name='python.exe'" get CommandLine,ProcessId` | Identify processes |
| **Find specific program** | `wmic process where "CommandLine like '%mkdocs%'" get CommandLine,ProcessId` | Target search |
| **Kill by PID** | `taskkill /F /PID 12345` | Stop specific process |
| **[Clean build](#command-4-clean-mkdocs-build-directory)** | `if exist site rmdir /s /q site` or `mkdocs build --clean` | Remove build cache |
| **MkDocs no reload** | `mkdocs serve --no-livereload` | Prevent refresh loop |
| **MkDocs dirty build** | `mkdocs serve --dirty --no-livereload` | Fast development |

---

## Additional Resources

- [Windows Task Manager](https://learn.microsoft.com/en-us/shows/inside/task-manager) - Microsoft's guide to Task Manager
- [WMIC Command Reference](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmic) - Complete WMIC documentation
- [MkDocs Serve Options](https://www.mkdocs.org/user-guide/cli/#mkdocs-serve) - Official MkDocs CLI reference