#!/usr/bin/env python3
"""Generate requirements index from YAML front matter.

This script generates two types of index files:
1. Main requirements index (docs/requirements/req-index.md)
2. Component-specific indexes (e.g., docs/requirements/GenUser/index.md)

Security:
- Input validation on all file paths (prevent path traversal)
- YAML safe loading (prevent code execution)
- HTML escaping via Jinja2 auto-escape
- Controlled file operations with explicit encoding
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Set

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


# Security: Define allowed base directories (prevent path traversal)
ALLOWED_BASE_DIR = Path("docs/requirements").resolve()
TEMPLATE_DIR = Path("scripts/templates").resolve()

# Valid priority levels (for validation)
VALID_PRIORITIES = {"CRITICAL", "HIGH", "MEDIUM", "LOW"}

# Valid status values (for validation)
VALID_STATUSES = {"draft", "in-review", "approved", "implemented"}


def safe_print(message: str) -> None:
    """Print with encoding error handling for Windows console.

    Args:
        message: The message to print

    Security: Prevents encoding errors that could crash the script
    """
    try:
        print(message)
    except UnicodeEncodeError:
        # Fallback to ASCII-safe output if console doesn't support Unicode
        print(message.encode("ascii", errors="replace").decode("ascii"))


def validate_path(file_path: Path, base_dir: Path) -> bool:
    """Validate that a path is within the allowed base directory.

    Args:
        file_path: The path to validate
        base_dir: The base directory that must contain file_path

    Returns:
        True if path is valid and within base_dir, False otherwise

    Security: Prevents path traversal attacks
    """
    try:
        resolved_path = file_path.resolve()
        resolved_base = base_dir.resolve()
        return resolved_path.is_relative_to(resolved_base)
    except (ValueError, OSError):
        return False


def validate_requirement_metadata(metadata: Dict) -> bool:
    """Validate requirement metadata fields.

    Args:
        metadata: Dictionary of metadata from YAML front matter

    Returns:
        True if metadata is valid, False otherwise

    Security: Validates data types and values before processing
    """
    # Check required fields exist
    required_fields = {"title", "req_id", "priority", "phase", "status"}
    if not all(field in metadata for field in required_fields):
        return False

    # Validate priority is in allowed set
    priority = metadata.get("priority")
    if priority not in VALID_PRIORITIES:
        safe_print(f"⚠️  Invalid priority: {priority}")
        return False

    # Validate phase is a non-negative integer
    try:
        phase = int(metadata.get("phase"))
        if phase < 0:
            return False
    except (ValueError, TypeError):
        return False

    # Validate status is in allowed set (required field)
    status = metadata.get("status")
    if status not in VALID_STATUSES:
        safe_print(f"⚠️  Invalid status: {status}")
        return False

    return True


def extract_metadata_from_file(file_path: Path) -> Optional[Dict]:
    """Extract and validate YAML front matter from a requirement file.

    Args:
        file_path: Path to the requirement file

    Returns:
        Dictionary of metadata if valid, None otherwise

    Security:
    - Uses yaml.safe_load to prevent code execution
    - Validates file path before reading
    - Validates metadata after extraction
    """
    # Security: Validate path is within allowed directory
    if not validate_path(file_path, ALLOWED_BASE_DIR):
        safe_print(f"⚠️  Skipping file outside allowed directory: {file_path}")
        return None

    # Security: Use explicit UTF-8 encoding
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError) as e:
        safe_print(f"⚠️  Error reading {file_path}: {e}")
        return None

    # Extract YAML front matter
    if not content.startswith("---"):
        return None

    yaml_end = content.find("---", 3)
    if yaml_end == -1:
        return None

    yaml_content = content[3:yaml_end]

    # Security: Use safe_load to prevent code execution
    try:
        metadata = yaml.safe_load(yaml_content)
    except yaml.YAMLError as e:
        safe_print(f"⚠️  Invalid YAML in {file_path}: {e}")
        return None

    # Validate metadata
    if not validate_requirement_metadata(metadata):
        safe_print(f"⚠️  Invalid metadata in {file_path}")
        return None

    return metadata


def scan_requirements(
    base_dir: Path, req_id_filter: Optional[str] = None
) -> List[Dict]:
    """Scan directory for requirement files and extract metadata.

    Args:
        base_dir: Base directory to scan for requirements
        req_id_filter: Optional filter - only include requirements where
                      req_id starts with this value (e.g., "req-genuser")

    Returns:
        List of requirement metadata dictionaries

    Security: Uses validate_path and extract_metadata_from_file for safety
    """
    requirements = []

    # Security: Validate base directory
    if not validate_path(base_dir, ALLOWED_BASE_DIR):
        safe_print(f"⚠️  Invalid base directory: {base_dir}")
        return requirements

    # Always scan entire requirements directory
    # Filtering happens later based on req_id_filter (filename OR folder matching)
    scan_dir = base_dir

    # Find all requirement markdown files
    # Note: Using rglob to support subdirectories, but with path validation
    for req_file in scan_dir.rglob("*.md"):
        # Skip index files and example/documentation files
        if req_file.name.lower() in (
            "index.md",
            "readme.md",
            "requirements-index-example.md",
            "req-index.md",  # Main requirements index (auto-generated)
            "req-by-subsys-idx.md",  # Subsystem index
        ):
            continue

        # Skip files that don't follow req-* naming pattern
        if not req_file.stem.lower().startswith("req-"):
            continue

        # Extract metadata
        metadata = extract_metadata_from_file(req_file)
        if not metadata:
            continue

        # Get req_id for cross-referencing
        req_id = metadata.get("req_id", "")

        # Apply component filter if specified (OR logic: filename OR folder)
        if req_id_filter:
            # Extract expected subsystem from req_id/filename
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

        # Calculate relative path for links
        try:
            # Get relative path from the requirements base directory
            rel_path = req_file.relative_to(base_dir)
            file_path = str(rel_path).replace("\\", "/")

            # Remove .md extension (MkDocs converts file.md to file/)
            if file_path.endswith(".md"):
                file_path = file_path[:-3]

            # Add correct ../ prefix based on index depth
            # MkDocs creates subdirectories from .md files:
            #   - Main index at /requirements/req-index/ needs ../ (1 level up)
            #   - Component index at /requirements/GenUser/genuser-index/ needs ../../ (2 levels up)
            if req_id_filter:
                # Component index: need to go up 2 levels
                file_path = "../../" + file_path
            else:
                # Main index: need to go up 1 level
                file_path = "../" + file_path
        except ValueError:
            # If we can't compute relative path, use filename without extension
            file_path = "../" + req_file.stem

        # Clean title (remove doc number in parentheses if present)
        title = metadata.get("title", "")
        doc_number = req_id if req_id else req_file.stem.upper()
        pattern = r"\s*\(" + re.escape(doc_number) + r"\)"
        title_clean = re.sub(pattern, "", title, flags=re.IGNORECASE).strip()

        requirements.append(
            {
                "file": req_file.name,
                "file_path": file_path,
                "title": title,
                "title_clean": title_clean,
                "priority": metadata.get("priority"),
                "phase": int(metadata.get("phase")),
                "status": metadata.get("status", ""),
                "req_id": req_id,
                "doc_number": doc_number,
                "exclude": metadata.get("exclude", False),
            }
        )

    # Sort by phase, then priority
    priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    requirements.sort(
        key=lambda r: (r["phase"], priority_order.get(r["priority"], 4))
    )

    return requirements


def generate_index_from_template(
    output_path: Path,
    title: str,
    requirements: List[Dict],
    description: Optional[str] = None,
    component_name: Optional[str] = None,
) -> bool:
    """Generate index file using Jinja2 template.

    Args:
        output_path: Path where index file will be written
        title: Page title
        requirements: List of requirement metadata
        description: Optional page description
        component_name: Optional component name for filtered views

    Returns:
        True if successful, False otherwise

    Security:
    - Jinja2 autoescape prevents XSS
    - Path validation before writing
    - UTF-8 encoding explicitly specified
    """
    # Security: Validate output path
    if not validate_path(output_path, ALLOWED_BASE_DIR):
        safe_print(f"⚠️  Invalid output path: {output_path}")
        return False

    # Get unique phases for dropdown
    phases: Set[int] = set(req["phase"] for req in requirements)

    # Setup Jinja2 environment with security settings
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html", "xml"]),  # Security: Auto-escape HTML
        trim_blocks=True,
        lstrip_blocks=True,
    )

    # Load template
    try:
        template = env.get_template("requirements-index.jinja2")
    except Exception as e:
        safe_print(f"❌ Error loading template: {e}")
        return False

    # Render template
    try:
        content = template.render(
            title=title,
            description=description,
            component_name=component_name,
            requirements=requirements,
            phases=sorted(phases),
        )
    except Exception as e:
        safe_print(f"❌ Error rendering template: {e}")
        return False

    # Write to file (only if content changed)
    should_write = True
    if output_path.exists():
        try:
            with open(output_path, "r", encoding="utf-8") as f:
                old_content = f.read()
            if old_content == content:
                should_write = False
        except (OSError, UnicodeDecodeError):
            pass  # If we can't read old file, write anyway

    if should_write:
        try:
            # Security: Explicit UTF-8 encoding
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
            safe_print(f"✅ Generated {output_path}")
            return True
        except OSError as e:
            safe_print(f"❌ Error writing {output_path}: {e}")
            return False
    else:
        safe_print(f"ℹ️  {output_path.name} unchanged, skipping write")
        return True


def generate_main_index() -> bool:
    """Generate the main requirements index.

    Returns:
        True if successful, False otherwise
    """
    safe_print("🔄 Generating main requirements index...")

    base_dir = ALLOWED_BASE_DIR
    requirements = scan_requirements(base_dir)

    output_path = base_dir / "req-index.md"
    return generate_index_from_template(
        output_path=output_path,
        title="Requirements Index",
        requirements=requirements,
        description=None,
        component_name=None,
    )


def generate_component_indexes() -> bool:
    """Generate component-specific requirement indexes.

    Scans for subdirectories in docs/requirements/ and generates
    an index for each component that has requirements.

    Returns:
        True if all successful, False if any failed
    """
    safe_print("🔄 Generating component-specific indexes...")

    base_dir = ALLOWED_BASE_DIR
    success = True

    # Find component subdirectories
    for component_dir in base_dir.iterdir():
        if not component_dir.is_dir():
            continue

        # Skip hidden directories and special directories
        if component_dir.name.startswith((".", "_")) or component_dir.name in (
            "for-sdd",
        ):
            continue

        # Determine req_id filter (e.g., "req-genuser")
        component_name = component_dir.name.lower()
        req_id_filter = f"req-{component_name}"

        safe_print(f"   Processing {component_name} component...")

        # Scan for requirements matching this component
        requirements = scan_requirements(base_dir, req_id_filter=req_id_filter)

        # Log if no requirements found (but still generate the index)
        if not requirements:
            safe_print(f"   No requirements found for {component_name}, generating empty index...")

        # Set output path for component index (e.g., genuser-index.md)
        index_path = component_dir / f"{component_name}-index.md"

        # Generate index
        result = generate_index_from_template(
            output_path=index_path,
            title=f"{component_dir.name} Requirements",
            requirements=requirements,
            description=None,
            component_name=component_dir.name,  # Use CamelCase directory name, not lowercased version
        )

        if not result:
            success = False

    return success


def main() -> int:
    """Main entry point.

    Returns:
        0 on success, 1 on failure
    """
    safe_print("=" * 60)
    safe_print("Requirements Index Generator")
    safe_print("=" * 60)

    # Generate main index
    main_success = generate_main_index()

    # Generate component-specific indexes
    component_success = generate_component_indexes()

    # Overall result
    if main_success and component_success:
        safe_print("=" * 60)
        safe_print("✅ All indexes generated successfully")
        safe_print("=" * 60)
        return 0
    else:
        safe_print("=" * 60)
        safe_print("❌ Some indexes failed to generate")
        safe_print("=" * 60)
        return 1


if __name__ == "__main__":
    exit(main())
