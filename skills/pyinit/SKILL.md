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

## Type Hint Conventions

All Python code must use type hints following PEP 484 and PEP 604:

### Type Hint Syntax

- **Always use type hints** for function parameters and return values
- **Use `|` union syntax** (PEP 604) instead of `Optional` or `Union`:
  ```python
  # Correct
  def process(data: str | None) -> bool | None:
      ...

  # Incorrect
  from typing import Optional, Union
  def process(data: Optional[str]) -> Optional[bool]:
      ...
  def process(data: Union[str, None]) -> Union[bool, None]:
      ...
  ```

- **Use `|` for multiple types** instead of `Union`:
  ```python
  # Correct
  def handle(value: int | str | float) -> None:
      ...

  # Incorrect
  from typing import Union
  def handle(value: Union[int, str, float]) -> None:
      ...
  ```

### Type Hint Examples

```python
from collections.abc import Callable

def fetch_data(url: str, timeout: int = 30) -> dict[str, object] | None:
    """Fetch data from URL with timeout."""
    ...

def process_items(items: list[str], callback: Callable[[str], bool]) -> list[str]:
    """Process items and return filtered results."""
    ...

class DataProcessor:
    def __init__(self, config: dict[str, object]) -> None:
        self.config: dict[str, object] = config

    def get_value(self, key: str) -> str | int | None:
        """Get value by key, returns None if not found."""
        ...
```

## Usage

When updating or creating Python files:

1. Ensure the file uses UTF-8 encoding with LF line endings
2. Add or verify the standard header (shebang + encoding + blank line)
3. Remove all trailing whitespace from lines
4. Format code according to PEP8 standards
5. Add type hints to all functions and methods using `|` syntax for optional/unions
