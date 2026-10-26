# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 SinonJZH
"""依赖方向契约：import-linter 机械执行 doc/ARCHITECTURE.md 的约束。

契约定义在 pyproject.toml 的 [tool.importlinter]，import-linter 未提供
pytest 插件，故经 CLI 程序化调用纳入默认套件。
"""

from pathlib import Path

from click.testing import CliRunner
from importlinter.cli import lint_imports_command

_REPO_ROOT = Path(__file__).resolve().parents[1]


def test_architecture_dependency_contracts() -> None:
    result = CliRunner().invoke(
        lint_imports_command, ["--config", str(_REPO_ROOT / "pyproject.toml")]
    )
    assert result.exit_code == 0, result.output
