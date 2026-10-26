# ds-agent-companion

通过调用 DeepSeek API 让模型进行角色扮演、陪伴用户的 Python 项目。

## 运行环境

- Python 虚拟环境固定使用项目根目录下的 `./.venv`，所有 python / pip 命令一律通过该环境执行（如 `./.venv/bin/python`、
  `./.venv/bin/pip`），不使用系统 Python 或全局环境。
- 依赖清单分两个文件：`requirements.txt`（运行时依赖）与 `requirements-test.txt`（测试依赖，首行 `-r requirements.txt`
  ，其余为运行时清单之外的测试专属包）。每次新增或更新依赖后，用 `./.venv/bin/pip freeze`
  重新生成对应清单（两文件均逐包精确钉版本）；未改动依赖时不要随意重新生成。

## 文档体系

本文件（AGENTS.md）只记载通用信息与文档索引，详细内容一律放在 `./doc/` 下：

| 文档                                       | 内容                                     |
|--------------------------------------------|------------------------------------------|
| [doc/ARCHITECTURE.md](doc/ARCHITECTURE.md) | 项目总体架构                             |
| [doc/ui_design.md](doc/ui_design.md)       | UI 设计规范与要求                        |
| [doc/testing.md](doc/testing.md)           | 测试设计与 CI 策略                       |
| [doc/revisions.md](doc/revisions.md)       | 每次文档修订的决策与改动记录（时间倒序） |

文档编写规则（对所有文档生效，包括本文件）：

- 除 `doc/revisions.md` 外，任何文档只描述当前最新状态，严格禁止记录修订信息（如"某日更新""原先……现在……"之类的内容）；历史一律通过
  `doc/revisions.md` 和 git 历史查询。
- 每次修订文档（含新增文档）后，必须在 `doc/revisions.md` 追加一条记录，写明本次修订的决策与改动内容；`revisions.md`
  只记修订记录，不记现状。
- 后续随开发需要再新增文档；新文档加入后须同步更新本索引。

## 代码风格

- 遵循 Google 开源项目风格指南（Google Python Style Guide）。
- 行尾统一 LF，由根目录 `.gitattributes` 在 git 侧强制（入库与检出均 LF）。
- 编辑器约定见根目录 `.editorconfig`：UTF-8、文末保留换行、缩进一律使用空格——Python 4 空格，TypeScript / HTML / SCSS / JSON
  及其余文件默认 2 空格。
- 注释要求：只保留必要的、简短的 docstring；尽量少用块注释和行注释，只在代码确实比较复杂的地方加简短注释。

## 许可声明

- 项目采用 AGPL-3.0 协议（协议全文见根目录 `LICENSE`）。
- 所有自研源码文件开头必须加以下两行声明（年份取文件创建年份；如有 shebang / 编码声明则置于其后）：

  ```python
  # SPDX-License-Identifier: AGPL-3.0-or-later
  # Copyright (C) 2026 SinonJZH
  ```

- 第三方依赖与工具生成的代码文件不加此声明。
