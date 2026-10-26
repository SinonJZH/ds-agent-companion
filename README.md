# ds-agent-companion

[English](README_en.md) | 简体中文

基于 DeepSeek API 的本地单用户 AI 角色扮演陪伴应用：模型扮演的角色拥有长期记忆和自己的日程，会主动找你聊天、发帖。引擎本地常驻，桌面、移动端浏览器与
headless 部署均可接入。

> **状态**：项目处于设计阶段，架构与 UI 设计已定稿，代码尚未开始编写。

## 规划特性

- **长期记忆**：四层滚动笔记 + 向量库 + 状态卡，公开/隐私分区注入，append-only 存储。
- **主动陪伴**：调度层承接定时/条件触发，角色会主动发起私聊、发布 SNS 帖子。
- **人设包**：人设、世界观、性格池、出身记忆打包为可导入导出的目录包。
- **多端接入**：单一引擎进程服务多前端（pywebview 桌面壳、移动端浏览器 / PWA、headless）。

## 技术栈

Python (asyncio) · DeepSeek API · SQLite (sqlite-vec) · fastembed · Angular · ConnectRPC

## 文档

- [架构设计](doc/ARCHITECTURE.md)
- [UI 设计规范](doc/ui_design.md)
- [测试设计](doc/testing.md)
- [文档修订记录](doc/revisions.md)

## 许可

本项目采用 [AGPL-3.0](LICENSE) 协议。
