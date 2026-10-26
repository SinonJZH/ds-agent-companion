# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 SinonJZH
"""骨架冒烟测试：全部子包可导入且带身份 docstring。"""

import importlib

import pytest

SUBPACKAGES = [
    "companion",
    "companion.api",
    "companion.engine",
    "companion.llm",
    "companion.memory",
    "companion.plugins",
    "companion.prompt",
    "companion.scheduler",
    "companion.storage",
]


@pytest.mark.parametrize("name", SUBPACKAGES)
def test_import_subpackage(name: str) -> None:
    module = importlib.import_module(name)
    assert module.__doc__
