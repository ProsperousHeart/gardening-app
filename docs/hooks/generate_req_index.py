"""MkDocs hook to auto-generate requirements index before build."""

import subprocess  # nosec B404 - subprocess used safely with hardcoded, controlled inputs only
import sys
from pathlib import Path


def safe_print(message):
    """Print with encoding error handling for Windows console."""
    try:
        print(message)
    except UnicodeEncodeError:
        # Fallback to ASCII-safe output if console doesn't support Unicode
        print(message.encode('ascii', errors='replace').decode('ascii'))


def on_pre_build(config):
    """Run before MkDocs build starts."""
    # script_path = Path("scripts/generate-req-index.py")  # Original
    script_path = Path("scripts/generate-req-index_UPDATE.py")  # TEMP: Testing updated version

    if script_path.exists():
        safe_print("🔄 Generating requirements index...")
        try:
            # Safe: script_path is hardcoded, sys.executable is controlled, no user input
            subprocess.run([sys.executable, str(script_path)], check=True)  # nosec B603
            safe_print("✅ Requirements index generated successfully")
        except subprocess.CalledProcessError as e:
            safe_print(f"❌ Failed to generate requirements index: {e}")
            # Don't fail the build, just warn
    else:
        safe_print(f"⚠️  Script not found: {script_path}")
