# v1.0.0 公开包检查

软件状态：ACCEPTED_WITH_NOTES / DEVELOPMENT_FROZEN。

公开发布元数据：COMPLETE。署名LHJ312，仓库LHJ312/chinese-engineering-manuscript-writer，采用PolyForm Noncommercial License 1.0.0。按维护者要求不提供CITATION.cff、邮箱、姓名拆分字段或ORCID。PUBLICATION_READY = YES仅表示本地发布包完成，不表示GitHub已经上线。

## 检查范围与结果

| 检查 | 结果与边界 |
| --- | --- |
| 冻结项目保护 | 原项目595个文件逐一SHA-256比较，未改动、未增加原项目文件。 |
| 正式运行清单 | 原runtime清单60项对应公开运行文件；另有安装子目录LICENSE、NOTICE版权声明、最小agents配置和公开书目索引，共64项。无开发历史、PDF、候选库或留出原文。 |
| 路径与引用 | 检查Markdown本地文件引用、runtime清单、规则/案例/Style索引；所有运行文件留在Skill子目录，源码路径仅作公开包迁移。外部出版方链接不是运行依赖，本轮不重新联网核验。 |
| SKILL frontmatter | name、description两个纯量字段通过严格结构与长度检查。官方quick_validate依赖PyYAML，本环境缺少该依赖，未宣称官方脚本通过。 |
| 安装兼容性 | 使用本地skill-installer实际路径检查、Skill检查及复制函数作离线安装；64项复制哈希一致，拒绝目录穿越与覆盖既有目标。未执行GitHub网络安装。 |
| runtime读取 | 从隔离安装副本、以Skill目录之外为工作目录进行43次调用；31规则、合并别名、Methods实施原则、24案例、14 Style Cards、筛选和未知ID拒绝均通过。 |
| 规则保护 | 31条规则正文块与批准源逐字相同；9 HARD / 16 STRONG / 6 HEURISTIC。外层路径与发布说明变化不改变规则正文。 |
| 隐私与密钥 | 对文本执行本地绝对路径、工作区身份、邮箱、常见密钥前缀、私钥块和敏感赋值模式扫描，未发现未授权匹配；仅精确放行用户明确授权的公开署名LHJ312。匹配项仅记录文件和位置，不输出秘密值。 |
| 第三方及未公开文本 | 24案例均不含原段或改稿，保留模式摘要与公开定位。对既有78个文本单元建立连续文本重合筛查，第三方采用80个规范化字符，未公开作者案例采用40个字符，未发现匹配。此阈值不是版权许可或全面法律认证，也不等同对全部论文全文逐字扫描。 |
| 文件与归档完整性 | 文件清单、文件SHA-256清单以及ZIP外部SHA-256分层记录。ZIP仅包含repository内文件，不带本地checks、隔离安装副本或构建脚本。 |

许可证全文从PolyForm官方仓库1.0.0版本下载，仓库根目录和Skill子目录LICENSE均与下载内容逐字节一致；NOTICE独立保存版权声明，不修改标准许可条款。许可证文本属于获准复用的法律文本，不属于待移除的论文原文。

## 可复核范围

[FILE_MANIFEST.json](../FILE_MANIFEST.json)逐项记录运行和仓库文件的大小及SHA-256，不收录其自身与SHA256SUMS，避免循环依赖。[SHA256SUMS](../SHA256SUMS)覆盖除自身外的所有仓库文件，包括FILE_MANIFEST.json。ZIP的SHA-256放在压缩包旁，覆盖整个归档。

完整本地扫描记录留在公开仓库之外，避免把机器路径、内部文件名及原语料带入公开包。公开检查说明只保留统计、方法和限制。

这些检查不重跑留出任务，不证明公开摘要化案例与原运行包行为完全等价。历史结果仍为3 PASS + 3 PASS_WITH_NOTE + 0 FAIL，两篇论文均PASS_WITH_NOTE，预注册严格门槛未完全满足。
