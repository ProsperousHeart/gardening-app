---
title: Green Coding Practices
description: "Currently a page outlining how to be more aware of ways to make your coding more efficient & the lessons learned when incorporating it into this project."
---
# Green Coding Practices: Build Optimization Case Study

!!! warning
    This has not yet been reviewed and confirmed. It is a side project that affected one piece.

**Topic:** Sustainable Software Engineering, Build Optimization
**Related Files:** `scripts/generate-req-index.py`, `docs/hooks/generate_req_index.py`

---

## Summary

This guide teaches green coding principles through a real optimization case study - improving the requirements index generation system to minimize computational waste and energy consumption. You'll learn how to measure code efficiency, identify wasteful patterns, and implement sustainable solutions.

---

## The Problem

### Initial Issue

When moving `docs/requirements/GenUser/req-genuser-example.md` to `docs/requirements/CommunityMember/req-genuser-example.md`, the file disappeared from the generated index and triggered regeneration of multiple files on every MkDocs build.

### Root Cause Analysis

**Issue 1: Missing Subdirectory Support**
```python
# Original code (line 34)
for req_file in req_dir.glob("req-*.md"):  # Only searches top-level directory
```

The glob pattern `req-*.md` only searches the immediate `docs/requirements/` directory, not subdirectories like `CommunityMember/` or `GenUser/`.

**Issue 2: Unnecessary Build Cycles**

The MkDocs hook (`docs/hooks/generate_req_index.py`) runs the index generation script on **every build**, even when requirement files haven't changed. While the script has change detection to prevent writing unchanged files, it still:
- Reads all requirement files
- Parses YAML front matter
- Regenerates HTML in memory
- Compares with existing file

This wastes CPU cycles and energy, especially in development with live reload.

---

## The Solution

### Phase 1: Fix Subdirectory Support (Implemented ✅)

**Changed glob pattern to search recursively:**
```python
# Updated code (line 34)
for req_file in req_dir.glob("**/req-*.md"):  # Searches all subdirectories
```

**Added relative path tracking:**
```python
# Get relative path from requirements directory
relative_path = req_file.relative_to(req_dir)

requirements.append({
    "file": req_file.name,
    "relative_path": str(relative_path).replace("\\", "/"),  # URL-safe paths
    # ... other metadata
})
```

**Fixed link generation for subdirectories:**
```python
# Use relative_path for links to handle subdirectories
link_path = req["relative_path"].replace(".md", "")  # Remove .md for MkDocs
output.append(f'<a href="../{link_path}">{title_clean}</a>')
```

### Phase 1.5: Smart Filtering Logic (Implemented ✅)

**Problem:** After fixing subdirectory scanning, files in the "wrong" folder didn't appear in their expected subsystem indexes.

**Example scenario:**
- File: `req-genuser-example.md`
- Expected location: `GenUser/` folder
- Actual location: `CommunityMember/` folder (moved for testing)
- Original behavior: Only appeared in CommunityMember index (wrong!)
- Desired behavior: Appear in BOTH indexes (filename suggests GenUser, location is CommunityMember)

**Solution: OR Filtering Logic**

Files appear in a subsystem index if **EITHER** condition is true:
1. Subsystem name is in the **filename** (req-**genuser**-example.md), OR
2. Subsystem name matches the **parent folder** (CommunityMember/)

**Implementation in `generate-req-index_UPDATE.py`:**

```python
# Always scan entire requirements directory (line 182-184)
scan_dir = base_dir  # Not limited to one subdirectory

# Extract subsystems from filename and folder (lines 222-235)
if req_id and "-" in req_id:
    filename_subsystem = req_id.split("-")[1].lower()
elif "-" in req_file.stem:
    filename_subsystem = req_file.stem.split("-")[1].lower()
else:
    filename_subsystem = ""

# Extract actual subsystem from parent folder
try:
    parent_rel = req_file.parent.relative_to(base_dir)
    folder_subsystem = str(parent_rel).lower() if str(parent_rel) != "." else ""
except ValueError:
    folder_subsystem = ""

# Expected filter subsystem (e.g., "req-genuser" -> "genuser")
filter_subsystem = req_id_filter.split("-")[1].lower() if "-" in req_id_filter else ""

# Include if subsystem matches filename OR folder (OR logic)
matches_filename = filename_subsystem == filter_subsystem
matches_folder = folder_subsystem == filter_subsystem

if not (matches_filename or matches_folder):
    continue  # Skip if doesn't match either
```

**Link Path Fix:**

Since files can now be in different folders, we needed to fix relative link depths:

```python
# Component indexes need to go up 2 levels (lines 248-257)
if req_id_filter:
    # From /requirements/GenUser/genuser-index/ to /requirements/CommunityMember/req-example/
    file_path = "../../" + file_path  # Go up 2 levels
else:
    # From /requirements/req-index/ to /requirements/GenUser/req-example/
    file_path = "../" + file_path  # Go up 1 level
```

**Result:**
- ✅ Files in "wrong" folder appear in both expected and actual subsystem indexes
- ✅ Links work correctly regardless of folder location
- ✅ Moving file back to correct folder removes it from "wrong" index
- ✅ Main index always shows all files regardless of location

**Benefits:**
1. **Fault tolerance** - Misplaced files still appear where expected
2. **Flexibility** - Files can be organized by folder OR naming convention
3. **Discoverability** - Users find files in multiple relevant places
4. **No broken links** - Correct relative paths regardless of file location

### Phase 2: Conditional Hook Execution (Future 🔄)

**Current behavior:**
- Hook runs on every `mkdocs serve` reload (every file save)
- Script processes all requirement files every time
- Only skips writing if content unchanged

**Planned optimization:**
- Track modification timestamps of requirement files
- Only run script when `.md` files in `docs/requirements/` changed
- Cache the last scan time to avoid redundant processing

**Implementation approach:**
```python
def on_pre_build(config):
    """Run before MkDocs build starts."""
    req_dir = Path("docs/requirements")
    cache_file = Path(".req_index_cache")

    # Get latest modification time of any requirement file
    req_files = list(req_dir.glob("**/req-*.md"))
    if not req_files:
        return

    latest_mod = max(f.stat().st_mtime for f in req_files)

    # Check if we need to regenerate
    should_regenerate = True
    if cache_file.exists():
        cached_time = float(cache_file.read_text())
        should_regenerate = latest_mod > cached_time

    if should_regenerate:
        # Run the generation script
        result = subprocess.run([sys.executable, str(script_path)], ...)
        # Update cache
        cache_file.write_text(str(latest_mod))
    else:
        print("✅ Requirements index up to date (no changes detected)")
```

---

## Green Coding Principles

### What is Green Coding?

**Green coding** (also called sustainable software engineering) is the practice of writing software that minimizes:

- **Energy consumption** (CPU cycles, memory usage, network traffic)
- **Carbon footprint** (data center energy, user device battery drain)
- **Computational waste** (redundant processing, inefficient algorithms)

### Why It Matters

**Energy Impact:**

- Global data centers consume ~200 TWh/year (1% of global electricity)
- Software inefficiency contributes to unnecessary energy use
- Each unnecessary file scan/build wastes CPU cycles = energy

**Developer Impact:**

- Faster builds = faster development cycles
- Less CPU usage = longer laptop battery life
- Reduced cloud costs in CI/CD pipelines

**Environmental Impact:**

- Less energy = reduced carbon emissions
- Sustainable practices compound across all users
- Sets good patterns for scaling applications

### Core Principles Applied to This Project

1. **Lazy Evaluation** - Don't process what hasn't changed

   - ✅ Change detection before writing files
   - 🔄 Timestamp checking before processing (planned)

2. **Efficient Data Structures** - Use appropriate algorithms

   - ✅ Single pass through files
   - ✅ Sorted requirements list (O(n log n) once vs O(n²) filtering)

3. **Caching** - Store results to avoid recomputation

   - ✅ File content comparison to skip unchanged writes
   - 🔄 Modification time caching (planned)

4. **Minimize I/O** - File operations are expensive

   - ✅ Read files only when needed
   - ✅ Write only when content changed
   - 🔄 Skip reading entirely if timestamps unchanged (planned)

5. **Right-Sized Processing** - Match tool to task

   - ✅ Client-side filtering (JavaScript) vs server-side regeneration
   - ✅ Static HTML generation vs dynamic database queries

---

## Measuring Green Code

### Metrics to Track

#### 1. **Build Time Metrics**

**What to measure:**

- Total build time (MkDocs)
- Index generation time (scripts/generate-req-index.py)
- File I/O operations count

**How to measure:**

```bash
# Time the full build
time mkdocs build

# Time just the index generation
time python scripts/generate-req-index.py

# Profile Python script performance
python -m cProfile -o profile.stats scripts/generate-req-index.py
python -m pstats profile.stats
```

**Baseline (pre-optimization):**

- TBD: Need to run benchmarks

**Target (post-optimization):**

- 50% reduction in build time when no files changed
- Zero file processing when timestamps unchanged

#### 2. **CPU & Memory Usage**

**Tools:**

- **Windows:** Task Manager, `wmic` command
- **Linux/Mac:** `top`, `htop`, `time -v`
- **Python:** `memory_profiler`, `psutil`

**Example with memory_profiler:**

```bash
pip install memory_profiler
python -m memory_profiler scripts/generate-req-index.py
```

**Example with psutil:**

```python
import psutil
import os

process = psutil.Process(os.getpid())
start_mem = process.memory_info().rss / 1024 / 1024  # MB

# ... your code ...

end_mem = process.memory_info().rss / 1024 / 1024
print(f"Memory used: {end_mem - start_mem:.2f} MB")
```

#### 3. **File I/O Operations**

**What to track:**

- Number of files read
- Number of files written
- Total bytes read/written

**Implementation:**

```python
# Add counters to the script
files_read = 0
files_written = 0
files_skipped = 0

for req_file in req_dir.glob("**/req-*.md"):
    files_read += 1
    # ... processing ...

if should_write:
    files_written += 1
else:
    files_skipped += 1

print(f"📊 I/O Stats: {files_read} read, {files_written} written, {files_skipped} skipped")
```

#### 4. **Carbon Footprint Estimation**

**Tools:**

- [Green Software Foundation - Carbon Aware SDK](https://github.com/Green-Software-Foundation/carbon-aware-sdk)
- [Cloud Carbon Footprint](https://www.cloudcarbonfootprint.org/)
- [Code Carbon](https://codecarbon.io/) - Python library for tracking emissions

**Example with Code Carbon:**

```bash
pip install codecarbon
```

```python
from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()

# Run your script
generate_index()

emissions = tracker.stop()
print(f"🌍 CO2 emissions: {emissions:.6f} kg")
```

### Benchmarking Process

#### Before Optimization

```bash
# 1. Clear all caches
rm -rf site/ .cache/ .req_index_cache

# 2. Run baseline benchmark
time mkdocs build

# 3. Run with profiling
python -m cProfile -o baseline.stats scripts/generate-req-index.py

# 4. Track file operations
# (Add counters to script and run)
```

#### After Optimization

```bash
# 1. Run with no changes (should be fastest)
time mkdocs build

# 2. Run with one file changed (should skip most processing)
touch docs/requirements/CommunityMember/req-genuser-example.md
time mkdocs build

# 3. Run with all files changed (should be similar to baseline)
find docs/requirements -name "*.md" -exec touch {} +
time mkdocs build
```

#### Comparison Metrics

| Scenario | Before | After | Improvement |
|----------|--------|-------|-------------|
| No changes | TBD | TBD | TBD |
| One file changed | TBD | TBD | TBD |
| All files changed | TBD | TBD | TBD |
| Files read | TBD | TBD | TBD |
| Files written | TBD | TBD | TBD |
| CPU time | TBD | TBD | TBD |
| Memory peak | TBD | TBD | TBD |

---

## Green Coding Resources

### Organizations & Standards

- [Green Software Foundation](https://greensoftware.foundation/) - Industry standards for sustainable software
- [Climate Action.tech](https://climateaction.tech/) - Community for climate-conscious technologists
- [The Green Web Foundation](https://www.thegreenwebfoundation.org/) - Tools for greener web hosting

### Tools & Libraries

**Carbon Measurement:**
- [Code Carbon](https://codecarbon.io/) - Track CO2 emissions from code execution
- [Cloud Carbon Footprint](https://www.cloudcarbonfootprint.org/) - Measure cloud provider emissions
- [Green Metrics Tool](https://github.com/green-coding-berlin/green-metrics-tool) - Energy consumption measurement

**Performance Profiling:**
- [Python cProfile](https://docs.python.org/3/library/profile.html) - Built-in profiling
- [memory_profiler](https://pypi.org/project/memory-profiler/) - Line-by-line memory usage
- [py-spy](https://github.com/benfred/py-spy) - Sampling profiler for Python

**Build Optimization:**
- [MkDocs Optimization Plugin](https://github.com/byrnereese/mkdocs-optimize-plugin) - Minify HTML/CSS/JS
- [Git Hook Tools](https://pre-commit.com/) - Run checks only on changed files

### Reading & Learning

**Articles:**
- [Principles of Green Software Engineering](https://learn.greensoftware.foundation/)
- [The Green Software Practitioner Guide](https://learn.greensoftware.foundation/)
- [Sustainable Web Design](https://sustainablewebdesign.org/)

**Books:**
- *Building Green Software* by Anne Currie, Sarah Hsu, Sara Bergman (O'Reilly, 2024)
- *Designing Data-Intensive Applications* by Martin Kleppmann (includes efficiency patterns)

**Podcasts:**
- [Environment Variables](https://podcast.greensoftware.foundation/) - Green Software Foundation podcast

---

## Action Items

### Immediate (Phase 1) - ✅ Complete

- [x] Fix glob pattern to search subdirectories (`**/req-*.md`)
- [x] Add relative path tracking for correct link generation
- [x] Test with files in subdirectories
- [x] Document green coding principles

### Phase 1.5: Smart Filtering - ✅ Complete

- [x] Implement OR filtering logic (filename OR folder location)
- [x] Scan entire directory tree for all component indexes
- [x] Fix link depths for cross-folder references (`../../` vs `../`)
- [x] Test with misplaced files appearing in multiple indexes
- [x] Verify correct behavior when file is moved back to proper location
- [x] Document filtering logic and benefits

### Short-term (Phase 2) - 🔄 Planned

- [ ] Implement timestamp-based change detection in hook
- [ ] Add file I/O counters and reporting
- [ ] Run baseline benchmarks (build time, CPU, memory)
- [ ] Compare before/after metrics
- [ ] Add cache file for modification times

### Long-term Considerations

- [ ] Evaluate JSON-based approach for larger scale
- [ ] Consider using SQLite for metadata caching (if >100 req files)
- [ ] Implement parallel processing for large requirement sets
- [ ] Add `--skip-index` flag for faster development builds
- [ ] Create pre-commit hook to regenerate index only when req files change

---

## Testing Checklist

To verify the optimization works:

**Phase 1: Subdirectory Support**
- [x] File in subdirectory appears in index (`CommunityMember/req-genuser-example.md`)
- [x] Links to subdirectory files work correctly
- [x] Files in root directory still work (`req-index.md`)
- [x] All existing requirement files still appear in index

**Phase 1.5: Smart Filtering**
- [x] Misplaced file appears in BOTH indexes (filename match + folder match)
  - `req-genuser-example.md` in `CommunityMember/` → shows in GenUser AND CommunityMember indexes
- [x] Links work correctly for cross-folder files
  - GenUser index links to file in CommunityMember folder use `../../CommunityMember/...`
- [x] Moving file back to correct folder removes it from "wrong" index
  - `req-genuser-example.md` moved to `GenUser/` → only shows in GenUser index
- [x] Main index always shows all files regardless of location

**Phase 2: Build Optimization (Pending)**
- [ ] No files are regenerated when content unchanged
- [ ] Build time is measurably faster with no changes (after Phase 2)
- [ ] Filters and search still work in the HTML table

---

## Lessons for Future Development

### Design Patterns for Efficiency

1. **Change Detection First**
   - Always check if work is needed before doing it
   - Timestamp comparison is cheaper than file reading
   - Content hashing is cheaper than full parsing

2. **Incremental Processing**
   - Process only what changed, not everything
   - Cache intermediate results
   - Use dependency graphs to minimize work

3. **Right-Sized Tools**
   - Static generation for rarely-changing data
   - Client-side filtering for user interactions
   - Server-side processing for complex calculations

4. **Measure, Don't Guess**
   - Profile before optimizing
   - Benchmark before and after changes
   - Track metrics over time

### Questions to Ask Before Writing Code

- **Does this need to run every time?** (Lazy evaluation)
- **Can I cache this result?** (Memoization)
- **Am I processing unchanged data?** (Change detection)
- **Is there a more efficient algorithm?** (Big-O analysis)
- **Can this run in parallel?** (Concurrency)
- **Will this scale with more files?** (Scalability testing)

### Code Review Checklist for Green Coding

- [ ] Are we reading files multiple times unnecessarily?
- [ ] Are we regenerating data that hasn't changed?
- [ ] Could we use caching to avoid repeated work?
- [ ] Are we using efficient data structures?
- [ ] Have we profiled to find bottlenecks?
- [ ] Does this scale well with more data?
- [ ] Are we doing work in tight loops that could be done once?
- [ ] Could this run conditionally instead of always?

---

## Conclusion

This optimization demonstrates that **green coding isn't just about algorithms** - it's about thoughtful system design:

- **Understand your build system** - Know when code runs and why
- **Measure before optimizing** - Profile to find real bottlenecks
- **Cache and skip when possible** - The fastest code is code that doesn't run
- **Think incrementally** - Process changes, not everything
- **Document your reasoning** - Help future developers understand trade-offs

**Key Takeaway:** Every unnecessary file read, every redundant build step, every wasted CPU cycle adds up across all developers, all builds, all deployments. Small optimizations compound into significant energy savings.

---

## Related Documentation

- **Architecture Diagrams:** `.github/instructions/architecture-diagrams.instructions.md`
- **MkDocs Guide:** `docs/tutorials/mkdocs/mkdocs-reference.md`
- **Dependency Management:** `docs/tutorials/general/dependency-management.md`
- **Code Standards:** `docs/rules/docstring-standards.md`

---

**Status:** 🔄 In Progress (Phase 1 complete, Phase 2 planned)
**Next Review:** After implementing timestamp-based change detection
**Benchmark Date:** TBD
