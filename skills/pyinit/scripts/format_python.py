#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Format Python files according to project PEP8 standards.

This script ensures Python files follow the project's conventions:
- UTF-8 encoding with LF line endings
- Standard file header (shebang + encoding + blank line)
- No trailing whitespace
- PEP8 formatting
"""

import os
import re
import sys


def has_shebang(line):
    """Check if line is a shebang."""
    return line.startswith("#!")


def has_encoding_declaration(line):
    """Check if line is an encoding declaration."""
    return re.match(r"^#.*?coding[:=]\s*([-\w.]+)", line)


def add_header(content):
    """Add standard header to Python file content."""
    lines = content.split('\n')
    header = [
        "#!/usr/bin/env python",
        "# -*- coding: UTF-8 -*-",
        "",
    ]

    # If file already has shebang/encoding, skip them
    start_idx = 0
    if lines and has_shebang(lines[0]):
        start_idx = 1
        if len(lines) > 1 and has_encoding_declaration(lines[1]):
            start_idx = 2
            if len(lines) > 2 and lines[2].strip() == "":
                start_idx = 3

    # Remove existing blank lines after header
    while start_idx < len(lines) and lines[start_idx].strip() == "":
        start_idx += 1

    return '\n'.join(header + lines[start_idx:])


def trim_trailing_whitespace(content):
    """Remove trailing whitespace from all lines."""
    lines = content.split('\n')
    return '\n'.join(line.rstrip() for line in lines)


def ensure_utf8_lf(content):
    """Ensure content is UTF-8 with LF line endings."""
    # Convert any Windows line endings to Unix
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    return content


def format_python_file(file_path):
    """Format a single Python file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Apply transformations
        content = ensure_utf8_lf(content)
        content = trim_trailing_whitespace(content)
        content = add_header(content)

        # Ensure file ends with newline
        if content and not content.endswith('\n'):
            content += '\n'

        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)

        return True
    except Exception as e:
        print(f"Error formatting {file_path}: {e}", file=sys.stderr)
        return False


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python format_python.py <file.py> [file2.py] ...")
        sys.exit(1)

    files = sys.argv[1:]
    success_count = 0

    for file_path in files:
        if not file_path.endswith('.py'):
            print(f"Skipping non-Python file: {file_path}")
            continue

        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}", file=sys.stderr)
            continue

        if format_python_file(file_path):
            print(f"Formatted: {file_path}")
            success_count += 1

    print(f"\nFormatted {success_count}/{len(files)} files")


if __name__ == "__main__":
    main()
