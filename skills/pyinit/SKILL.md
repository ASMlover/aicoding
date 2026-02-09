---
name: pyinit
description: Update Python file headers and formatting according to PEP8 standards with specific conventions - UTF-8 encoding, LF line endings, trim trailing whitespace, and standardized file header format. Use when working with Python files that need proper initialization or formatting updates.
---

# Python File Initialization

## Overview

Standardize Python files with consistent formatting and headers. This skill ensures all Python files follow the project's PEP8-based conventions.

## File Format Standards

All Python files must follow these conventions:

### Encoding and Line Endings
- **File encoding**: UTF-8
- **Line endings**: LF (Unix-style, not CRLF)
- **Trailing whitespace**: Automatically removed from all lines

### File Header Format

Every Python file must start with the following three lines:

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

```

- Line 1: Shebang `#!/usr/bin/env python`
- Line 2: Encoding declaration `# -*- coding: UTF-8 -*-`
- Line 3: Empty line

## PEP8 Conventions

Follow PEP8 style guidelines:
- 4 spaces per indentation level (no tabs)
- Maximum line length of 79 characters
- Two blank lines between top-level function/class definitions
- One blank line between method definitions
- Imports on separate lines at the top of the file (after header)

## Usage

When updating or creating Python files:

1. Ensure the file uses UTF-8 encoding with LF line endings
2. Add or verify the standard header (shebang + encoding + blank line)
3. Remove all trailing whitespace from lines
4. Format code according to PEP8 standards
