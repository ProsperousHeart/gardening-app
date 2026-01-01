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
            result = subprocess.run([sys.executable, str(script_path)], check=True, capture_output=True, text=True)  # nosec B603
            output = result.stdout

            # Parse output lines to categorize results
            generated_files = []
            skipped_files = []

            for line in output.split('\n'):
                line = line.strip()
                # Match "Generated" regardless of emoji encoding issues
                if 'Generated' in line and not line.startswith(('=', 'Requirements')):
                    # Extract filename - handle both "✅ Generated {path}" and fallback ASCII
                    # Remove common prefixes
                    for prefix in ['✅ Generated', 'Generated']:
                        if prefix in line:
                            filename = line.split(prefix, 1)[1].strip()
                            if filename:  # Only add if we extracted something
                                generated_files.append(filename)
                            break
                elif 'unchanged' in line and 'skipping write' in line:
                    # Extract filename from "ℹ️  {name} unchanged, skipping write" or ASCII variant
                    # Remove "unchanged, skipping write" and any emoji prefix
                    filename = line.replace('unchanged, skipping write', '').strip()
                    # Remove emoji if present
                    filename = filename.replace('ℹ️', '').strip()
                    if filename:  # Only add if we extracted something
                        skipped_files.append(filename)

            # Display categorized results
            if generated_files:
                safe_print(f"   ✅ Generated/Updated ({len(generated_files)} file{'s' if len(generated_files) != 1 else ''}):")
                for filename in generated_files:
                    safe_print(f"      • {filename}")

            if skipped_files:
                safe_print(f"   ℹ️  Skipped ({len(skipped_files)} file{'s' if len(skipped_files) != 1 else ''}, unchanged):")
                for filename in skipped_files:
                    safe_print(f"      • {filename}")

            # Summary
            total_count = len(generated_files) + len(skipped_files)
            if total_count > 0:
                safe_print(f"✅ Requirements index complete: {len(generated_files)} generated/updated, {len(skipped_files)} unchanged")
            else:
                safe_print(f"⚠️  No requirement files processed")
        except subprocess.CalledProcessError as e:
            safe_print(f"❌ Failed to generate requirements index: {e}")
            # Don't fail the build, just warn
    else:
        safe_print(f"⚠️  Script not found: {script_path}")
