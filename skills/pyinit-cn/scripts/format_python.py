#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
根据项目 PEP8 标准格式化 Python 文件。

此脚本确保 Python 文件遵循项目约定：
- UTF-8 编码，使用 LF 换行符
- 标准文件头（shebang + 编码声明 + 空行）
- 无尾随空格
- PEP8 格式化
"""

import os
import re
import sys


def has_shebang(line):
    """检查行是否为 shebang。"""
    return line.startswith("#!")


def has_encoding_declaration(line):
    """检查行是否为编码声明。"""
    return re.match(r"^#.*?coding[:=]\s*([-\w.]+)", line)


def add_header(content):
    """为 Python 文件内容添加标准头部。"""
    lines = content.split('\n')
    header = [
        "#!/usr/bin/env python",
        "# -*- coding: UTF-8 -*-",
        "",
    ]

    # 如果文件已有 shebang/编码声明，跳过它们
    start_idx = 0
    if lines and has_shebang(lines[0]):
        start_idx = 1
        if len(lines) > 1 and has_encoding_declaration(lines[1]):
            start_idx = 2
            if len(lines) > 2 and lines[2].strip() == "":
                start_idx = 3

    # 移除头部后的现有空行
    while start_idx < len(lines) and lines[start_idx].strip() == "":
        start_idx += 1

    return '\n'.join(header + lines[start_idx:])


def trim_trailing_whitespace(content):
    """移除所有行的尾随空格。"""
    lines = content.split('\n')
    return '\n'.join(line.rstrip() for line in lines)


def ensure_utf8_lf(content):
    """确保内容使用 UTF-8 编码和 LF 换行符。"""
    # 将任何 Windows 换行符转换为 Unix 格式
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    return content


def format_python_file(file_path):
    """格式化单个 Python 文件。"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 应用转换
        content = ensure_utf8_lf(content)
        content = trim_trailing_whitespace(content)
        content = add_header(content)

        # 确保文件以换行符结尾
        if content and not content.endswith('\n'):
            content += '\n'

        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)

        return True
    except Exception as e:
        print(f"格式化 {file_path} 时出错: {e}", file=sys.stderr)
        return False


def main():
    """主入口点。"""
    if len(sys.argv) < 2:
        print("用法: python format_python.py <文件.py> [文件2.py] ...")
        sys.exit(1)

    files = sys.argv[1:]
    success_count = 0

    for file_path in files:
        if not file_path.endswith('.py'):
            print(f"跳过非 Python 文件: {file_path}")
            continue

        if not os.path.isfile(file_path):
            print(f"未找到文件: {file_path}", file=sys.stderr)
            continue

        if format_python_file(file_path):
            print(f"已格式化: {file_path}")
            success_count += 1

    print(f"\n已格式化 {success_count}/{len(files)} 个文件")


if __name__ == "__main__":
    main()
