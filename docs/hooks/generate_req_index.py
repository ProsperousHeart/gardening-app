"""MkDocs hook to auto-generate requirements index before build."""

import subprocess
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
    script_path = Path("scripts/generate-req-index.py")

    if script_path.exists():
        safe_print("🔄 Generating requirements index...")
        try:
            subprocess.run([sys.executable, str(script_path)], check=True)
            safe_print("✅ Requirements index generated successfully")
        except subprocess.CalledProcessError as e:
            safe_print(f"❌ Failed to generate requirements index: {e}")
            # Don't fail the build, just warn
    else:
        safe_print(f"⚠️  Script not found: {script_path}")
