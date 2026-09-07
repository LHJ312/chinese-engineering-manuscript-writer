# Task Router

先确定用户要起草、编辑、诊断还是计划，再选章节。章节标题与实际功能不一致时按功能判断；Results/Discussion合章可同时调用相邻接口。不要因用户只发了一段就启动全文审查。

下表“规则”是候选调用范围，不是要求全部读取。按具体问题从中选择ID，用[按需读取器](../scripts/read_runtime_asset.py)或[行号索引](../criteria/rule_index_v2.json)只取对应规则。强度沿用批准版本，D-01→C-01、L-03→G-02。

| task_type | Playbook入口（位于sections） | 按问题选择规则 | 案例 | Plan要求 | 允许输出 |
| --- | --- | --- | --- | --- | --- |
| INTRODUCTION_DRAFT | introduction.md + scientific_synthesis.md | B/I/L；必要时G-02、J-01、K-02 | 可选INT-01—04 | 必须Map与必要段落Plan；复用有效已有Plan | 授权范围内计划及辅助稿，不能承诺自动终稿 |
| METHODS_DRAFT | methods.md | E/N/M；必要时C-03、L-01/L-02 | 可选MET-01—04 | 必须说明依赖Plan | 方法草稿与无法恢复的必要输入项 |
| RESULTS_DRAFT | results.md | C/F/O；数值M，试验N-02；必要时I-01/L-01 | 可选RES-01—04 | 必须发现—指标—图表Plan | 结果草稿；不补未确认解释 |
| DISCUSSION_DRAFT | discussion.md | G/F-02/A-01/B/L；必要时M-02 | 可选DIS-01—04 | 必须解释—前提Plan | 已支持的讨论；缺前提留编辑说明 |
| CONCLUSION_DRAFT | conclusion.md | H/C-02/L-01/G-02/O-02 | 可选CON-01—04 | 必须正文命题映射，可简短 | 条件化结论；不首次添加认识 |
| ABSTRACT_DRAFT | abstract.md | C/I-01/G-02/L-01；必要时M-02/O-02 | 可选ABS-01—04 | 必须摘要命题与正文映射 | 摘要及必要待答项，不补PARTIAL链 |
| SECTION_EDIT | 对应章节 | 按实际问题选该章规则 | 不默认；有歧义时取1个对照 | 默认不另建正式Plan；结构改动需局部Plan | 最小修改稿或NO MATERIAL ISSUE |
| PARAGRAPH_EDIT | 对应功能章节的相关小节 | 只选命中的规则 | 不默认；可取边界/无问题案例 | 通常不需要；内部识别功能与保留项即可 | 修改的最小单元或原文保留 |
| FULL_MANUSCRIPT_EDIT | 先manuscript_review_workflow，再逐章加载 | 按章节问题渐进调用 | 不默认 | 先诊断及改动Plan，已有授权下继续执行 | 在用户范围内全文修改稿、关键差异与待答项 |
| MANUSCRIPT_DIAGNOSIS | manuscript_review_workflow，再按问题调用章节 | 按已定位问题调用 | 只解决边界歧义时需要 | 章节职责图即可，不写草稿 | 有位置/依据/级别的诊断，不自动改文 |
| OUTLINE_OR_PLAN | 只读目标章节 | B/I/L及该章必要规则 | 可选 | 任务本身为Plan | 功能图、提纲或段落计划；不越权正文 |
| RESULT_TO_DISCUSSION | results.md + discussion.md | F-02/G/A-01/L-01 | 可选SC-09/10与相应案例 | 必须最小解释前提表 | 观察/就近解释/机制分层及可支持的讨论 |
| EVIDENCE_CONSTRAINED_REWRITE | 对应章节 + editing_workflow | G-02/L-01/I-01及特定口径规则 | 不默认 | 先短列受保护命题与允许改动，复用已有清单 | 受约束最小改稿；冲突或缺项单列 |

起草：[drafting_workflow](drafting_workflow.md)。编辑：[editing_workflow](editing_workflow.md)。诊断：[manuscript_review_workflow](manuscript_review_workflow.md)。小任务不因路由而增加无用途文件或审批步骤。

明确要求Title/Keywords、文献检索、事实审计或期刊格式核查时，说明本包没有对应专用Playbook；按用户另行授权的能力处理，不假称已由本Skill验证，也不自动扩库。
