#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 SinonJZH
"""检测并为自研源码文件补写 AGPL SPDX 文件头。

扫描 git 跟踪与未忽略的 .py / .ts / .scss 文件，默认仅检测：缺头的文件
列出清单并以退出码 1 结束（供 CI 把关）；加 --fix 实际写入。年份取文件
入库时间（git 首次加入的提交年份），未入库的新文件取当前年份。工具生成
的代码目录（如后续 connect-es 生成物）加入 EXCLUDED_PARTS 后跳过。
"""

import argparse
import datetime
import subprocess
import sys
from pathlib import Path

SPDX_ID = "AGPL-3.0-or-later"
HOLDER = "SinonJZH"

COMMENT_STYLES = {".py": "#", ".ts": "//", ".scss": "//"}

EXCLUDED_PARTS = ("node_modules", "dist", ".venv")


def _git(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=True
    ).stdout


def repo_root() -> Path:
    return Path(_git(Path.cwd(), "rev-parse", "--show-toplevel").strip())


def candidates(root: Path) -> list[Path]:
    """返回待检查文件：git 可见、扩展名受支持、不在排除目录内。"""
    listed = _git(root, "ls-files", "--cached", "--others", "--exclude-standard")
    files = []
    for line in listed.splitlines():
        path = Path(line)
        if path.suffix not in COMMENT_STYLES:
            continue
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        files.append(root / path)
    return files


def has_spdx(text: str) -> bool:
    return any("SPDX-License-Identifier:" in line for line in text.splitlines()[:5])


def creation_year(root: Path, path: Path) -> int:
    dates = _git(
        root, "log", "--diff-filter=A", "--format=%as", "--",
        path.relative_to(root).as_posix(),
    )
    lines = dates.splitlines()
    return int(lines[-1].split("-")[0]) if lines else datetime.date.today().year


def _is_declaration(line: str) -> bool:
    """Python shebang 或编码声明行，文件头须置于其后。"""
    return line.startswith("#!") or (
        line.startswith("#") and "coding" in line and "-*-" in line
    )


def insert_header(path: Path, year: int) -> None:
    comment = COMMENT_STYLES[path.suffix]
    header = "\n".join(
        [
            f"{comment} SPDX-License-Identifier: {SPDX_ID}",
            f"{comment} Copyright (C) {year} {HOLDER}",
        ]
    ) + "\n"
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    skip = 0
    if path.suffix == ".py":
        while skip < len(lines) and _is_declaration(lines[skip]):
            skip += 1
    body = "".join(lines[skip:])
    text = "".join(lines[:skip]) + header + (f"\n{body}" if body else "")
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fix", action="store_true", help="写入缺失的文件头（默认仅检测）"
    )
    args = parser.parse_args()
    root = repo_root()
    missing = [
        p for p in candidates(root) if not has_spdx(p.read_text(encoding="utf-8"))
    ]
    for path in missing:
        if args.fix:
            year = creation_year(root, path)
            insert_header(path, year)
            print(f"added:   {path.relative_to(root)} ({year})")
        else:
            print(f"missing: {path.relative_to(root)}")
    if missing and not args.fix:
        print(f"{len(missing)} 个文件缺 SPDX 文件头，运行 --fix 补写", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
