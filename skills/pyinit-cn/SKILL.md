---
name: pyinit-cn
description: 根据 PEP8 标准更新 Python 文件头部和格式化 - UTF-8 编码、LF 换行符、移除行尾空格、标准化文件头格式。当需要为 Python 文件进行初始化或格式化更新时使用。
---

# Python 文件初始化

## 概述

使用一致的格式化和头部来标准化 Python 文件。此技能确保所有 Python 文件遵循基于 PEP8 的项目约定。

## 文件格式标准

所有 Python 文件必须遵循以下约定：

### 编码和换行
- **文件编码**: UTF-8
- **换行符**: LF（Unix 风格，非 CRLF）
- **行尾空格**: 自动移除所有行的尾随空格

### 文件头格式

每个 Python 文件必须以以下三行开头：

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

```

- 第1行: Shebang `#!/usr/bin/env python`
- 第2行: 编码声明 `# -*- coding: UTF-8 -*-`
- 第3行: 空行

## PEP8 约定

遵循 PEP8 风格指南：
- 每个缩进级别使用 4 个空格（不使用制表符）
- 最大行长度为 79 个字符
- 顶级函数/类定义之间保留两个空行
- 方法定义之间保留一个空行
- 导入语句位于文件顶部的单独行（头部之后）

## 类型提示约定

所有 Python 代码必须使用类型提示，遵循 PEP 484 和 PEP 604：

### 类型提示语法

- **始终使用类型提示**标注函数参数和返回值
- **使用 `|` 联合语法**（PEP 604）代替 `Optional` 或 `Union`：
  ```python
  # 正确
  def process(data: str | None) -> bool | None:
      ...

  # 错误
  from typing import Optional, Union
  def process(data: Optional[str]) -> Optional[bool]:
      ...
  def process(data: Union[str, None]) -> Union[bool, None]:
      ...
  ```

- **使用 `|` 表示多类型**代替 `Union`：
  ```python
  # 正确
  def handle(value: int | str | float) -> None:
      ...

  # 错误
  from typing import Union
  def handle(value: Union[int, str, float]) -> None:
      ...
  ```

### 类型提示示例

```python
from collections.abc import Callable

def fetch_data(url: str, timeout: int = 30) -> dict[str, object] | None:
    """使用超时从 URL 获取数据。"""
    ...

def process_items(items: list[str], callback: Callable[[str], bool]) -> list[str]:
    """处理项目并返回筛选结果。"""
    ...

class DataProcessor:
    def __init__(self, config: dict[str, object]) -> None:
        self.config: dict[str, object] = config

    def get_value(self, key: str) -> str | int | None:
        """按键获取值，未找到时返回 None。"""
        ...
```

## 使用方法

当更新或创建 Python 文件时：

1. 确保文件使用 UTF-8 编码和 LF 换行符
2. 添加或验证标准头部（shebang + 编码声明 + 空行）
3. 移除所有行的尾随空格
4. 按照 PEP8 标准格式化代码
5. 为所有函数和方法添加类型提示，使用 `|` 语法表示可选/联合类型

## 脚本

使用 `scripts/format_python.py` 脚本来自动格式化 Python 文件：

```bash
python scripts/format_python.py <file.py> [file2.py] ...
```

该脚本会：
- 确保文件使用 UTF-8 编码和 LF 换行符
- 添加或更新标准文件头
- 移除所有行的尾随空格
- 确保文件以换行符结尾
