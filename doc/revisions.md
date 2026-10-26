# 文档修订记录

记录每次文档修订时的决策与改动内容，不记录现状。新记录追加在最上方（按时间倒序）。

## 2026-10-26 SPDX 文件头自动检测与补写

- 决策：SPDX 文件头改由脚本机械把关——`scripts/add_license_headers.py` 默认仅检测（缺头即非零退出），`--fix`
  自动补写；年份取文件入库时间（git 首次加入的提交年份），未入库新文件取当年；Python 文件头置于 shebang /
  编码声明之后；覆盖 `.py` / `.ts` / `.scss`，只扫 git 可见文件（忽略清单自动生效），工具生成代码目录在脚本
  `EXCLUDED_PARTS` 排除。CI backend job 增加检测步骤。
- 改动：`AGENTS.md` 许可声明一节补脚本用法一条；新增 `scripts/add_license_headers.py`；CI 增加检测步骤；补写了
  `frontend/src/app/app.scss` 遗漏的文件头。

## 2026-10-26 前端技术栈钉版与 Angular 22 编码规范入册

- 决策：前端技术栈钉版——Angular 22、包管理器 pnpm、样式表 SCSS（工程位于 `frontend/` 目录）。
- 改动：`doc/ui_design.md` 技术选型一条补钉版本信息；新增「Angular 编码规范（v22）」章节——TypeScript strict
  （禁 `any`）、standalone 与 OnPush 走默认不显式声明、signals 状态（禁 `mutate`）、函数式输入输出（`input()` /
  `output()` / `model()`）、Signal Forms 优先、原生控制流与 `class` / `style` 绑定（禁结构性指令旧语法与
  `ngClass` / `ngStyle`、不导入 `CommonModule`）、host 对象、`inject()` 注入、`NgOptimizedImage`、WCAG AA
  无障碍（AXE 全过）。

## 2026-10-26 AI 记忆工具定位为记忆模块内置插件

Python 骨架落地阶段的首个补充决策（骨架本身为代码改动，不入本记录）。

- 决策：AI 记忆工具（按日期查笔记、语义检索、存/改向量条目、改状态卡）实现于记忆模块内，定位为内置插件——代码内置、不走启动扫描，
  与外部插件同样经引擎注册分发。
- 改动：`doc/ARCHITECTURE.md` 记忆模块「注入与检索」与插件模块加载方式两处补充上述定位；`pyproject.toml` 相应新增
  import-linter
  契约「记忆模块仅被引擎、提示词、调度层访问」（api / llm / plugins / storage 禁止依赖 memory）。

## 2026-10-26 项目初始化与设计定稿

项目创建阶段的一次性定稿：以下决策已全部落在当前各文档中，本阶段无代码。

- 决策：
    - 文档体系：AGENTS.md 只记通用信息与文档索引，详细内容一律置于 `doc/` 下；除本文件外所有文档只描述当前最新状态、严禁记录修订信息，历史由本文件与
      git 历史承载。
    - 许可：AGPL-3.0，`LICENSE` 保存协议官方全文；自研源码文件开头统一加 SPDX 标识与版权两行声明（约定见 AGENTS.md）。
    - 总体架构：对话引擎为编排核心（agent loop、会话开始取记忆快照、上下文按整轮裁剪）；主调度层统一承接定时/条件触发与全部后台任务（用户/LLM/插件三方共用
      CRUD 接口、持久化可审计、设数量与频率上限、无时效任务排谷价时段）；交互层为薄前端；全部运行数据收敛到单一 SQLite。
    - 提示词模块：块三级归属（全局层不可卸载 / 场景默认层 / 人设包层）+ 槽位场景变体；`build(scene, context)`
      纯函数组装，后台任务走第二入口 `build_task(task, data)`（不进场景枚举契约）；场景枚举初版三场景（private_chat /
      sns_post / sns_reply）；组装顺序按变动频率稳定在前（配合 DeepSeek
      前缀缓存），环境状态随会话快照冻结、精确当前时刻归尾部块；场景严格度由分区注入规则、场景默认层变体、场景级模型配置三机制组合表达，不设独立等级；心境状态化（每日抽取落状态区、组装只读）；人设包含性格池。
    - 记忆模块：分区（公开/隐私）不变式贯穿会话历史、笔记、向量库、状态区与 AI 检索工具返回，条目默认继承产生会话的分区；状态卡分区标签落到条目级（sns
      场景角色知道关系存在但不谈隐私细节）；四层笔记为 24h 滚动日记视图（平滑遗忘）+ 周/月/年压缩（anchored_to
      锚点下钻、重要度只决定压缩存活、上限初版固定），append-only 永不删除；持久事实唯一权威在状态卡，压缩与记忆卫生各设侧向沉淀/晋升出口；向量库纯拉取式检索（AI
      经工具自构查询、不自动注入 top-k），排序合成相关度 × 新近度衰减 × 重要度，命中即强化；查重为阈值判定 + 灰区带 LLM
      仲裁，以固定基线问题集重放校准。
    - 向量与嵌入：sqlite-vec（钉 0.1.9，vec0 虚拟表 + cosine 距离，精确暴力 top-k 不用 ANN）；fastembed 运行
      jinaai/jina-embeddings-v2-base-zh（768 维），为全项目单一嵌入模型、不更换（红线）；该嵌入模型许可为
      CC-BY-NC-4.0，商业化需换模型或购买授权。
    - LLM 模块：DeepSeek V4 现役模型（deepseek-flash / deepseek-v4-pro）；不引入 LangChain 等 agent 框架（agent loop
      归对话引擎自研），自写薄封装 + openai SDK 传输（base_url 指向 DeepSeek，SDK 版本钉死）；API 面走 Chat Completions，不采用
      Responses API 与 Anthropic 兼容端点（理由与重议条件见 ARCHITECTURE.md）；对引擎暴露自有事件流接口，引擎不感知 SDK
      类型；场景级配置（模型 × thinking × effort × tools），后台任务独立配置组；带 tools 会话必须全量回传
      reasoning_content；利用前缀缓存与峰谷计费；OpenAI 兼容协议为本地模型逃生通道。
    - 存储与人设包：单一 SQLite 存全部运行数据（UTC epoch 存储 + IANA 配置时区渲染、WAL、append-only、备份走 VACUUM
      INTO）；主要表建表即带 persona_id，切换人设整套数据随 persona 隔离；人设包权威存储为文件系统目录包
      personas/&lt;id&gt;/（manifest.yaml + core.md + worldview/*.md + corpus/*.md + memories.yaml，zip
      导入导出），引擎启动全量加载进内存、UI 编辑经引擎 API 写穿，SQLite
      只存激活指针；记忆槽位定义为角色出身记忆：常驻注入（人设块之后、状态卡之前）、不进记忆系统；完整提示词组装日志独立存储不进主库。
    - 调度层：内置触发类型含回忆触发（条目关联日期周年/纪念日或高重要度久未访问 → 以该条目为上下文发起 private_chat
      主动会话）与主动发帖（定期/按条件触发 sns_post、产出发布到时间线，SNS 场景唯一主动入口）。
    - 接口层：引擎与前端的接口以 protobuf 为契约、ConnectRPC 承载（服务端 connect-python，前端 connect-es 生成强类型客户端）；浏览器走
      Connect 协议（普通 HTTP POST + JSON，无需 gRPC-Web 代理）；对话流式输出走 server-streaming；不采用裸 gRPC 与 FastAPI +
      OpenAPI 生成。
    - UI：单一 web 前端（Angular）桌面移动同构，「引擎进程 + 多前端客户端」形态——pywebview 桌面壳、移动端浏览器 /
      PWA（后续）、NAS / 服务器 headless 常驻；桌面集成收窄为快捷键与系统通知；深色暗蓝主题，颜色一律经 token
      引用，对比度按内容分级（阅读型正文 ≥7:1、界面短文本 ≥4.5:
      1）并有校验脚本纳入测试；页面集七页（聊天、人设包管理、提示词设置、记忆管理、调度与后台任务、插件管理、系统设置）；图片输入、系统托盘、PWA
      封装与推送通知列范围外（初版不做）。
    - 测试与 CI：按确定性分层——确定性逻辑与 asyncio 并发进默认离线套件，真实依赖（SQLite /
      sqlite-vec、fastembed、ConnectRPC）真实现离线测试，LLM 质量类隔离为独立 eval runner（基线问题集重放、阈值校准）不进
      pytest 与 CI；时钟、LLM 客户端（httpx）、嵌入函数、数据库路径四注入点一律构造函数注入（时钟禁用 datetime.now()）；FakeLLM
      为一等测试设施；「架构不变式必须有对应测试」替代覆盖率硬指标；前端测试守组件单测（mock transport）、markdown 安全（LLM
      输出按不可信输入）、token 对比度断言三件事，E2E 仅 Playwright 冒烟；CI 默认工作流完全无 secrets，live_api 本地按需、eval
      纯本地；测试 fixture 与基线问题集一律合成内容，禁止真实个人数据。
    - 工程配置：行尾统一 LF，由 `.gitattributes` 强制（入库与检出均 LF）；编辑器约定收敛到 `.editorconfig`
      （UTF-8、文末换行、缩进空格：Python 4 空格、其余默认 2 空格）；依赖清单拆为 `requirements.txt`（运行时）与
      `requirements-test.txt`（测试）双文件，均由 pip freeze 生成、逐包精确钉版本。
    - README：新增中英双语最简 README（README.md 中文 / README_en.md
      英文，顶部互链），仅含定位描述、状态、规划特性、技术栈、文档索引与许可声明，不含安装使用章节，待代码落地后补充；README 不入
      AGENTS.md 文档索引（索引只收录 `doc/` 下文档）。
- 改动：创建 `AGENTS.md`、`LICENSE`、`.gitattributes`、`.editorconfig`、`requirements.txt`、`requirements-test.txt`、
  `README.md`、`README_en.md` 与 `doc/` 下 `ARCHITECTURE.md`、`ui_design.md`、`testing.md` 及本文件。
