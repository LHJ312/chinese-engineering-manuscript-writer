# chinese-engineering-manuscript-writer

**v1.0.0 · ACCEPTED_WITH_NOTES · DEVELOPMENT_FROZEN**

公开署名：**LHJ312**。项目仓库：[https://github.com/LHJ312/chinese-engineering-manuscript-writer](https://github.com/LHJ312/chinese-engineering-manuscript-writer)。本地发布包已定稿，尚未自动上传GitHub。

面向中文土木工程、结构工程与工程力学期刊论文的章节规划、辅助起草、最小必要编辑和写作诊断 Skill。将作者已经确认的研究事实与认识组织成具有明确科学论点的中文正文。

本次发布状态由项目维护方接受已知注记后确定；**预注册的严格留出验收门槛未完全满足**。发布没有改写历史测试结论，也不代表自动终稿生成能力得到认证。

## 功能与适用范围

- 依据章节科学功能组织信息，形成问题、判断与支撑的对应。
- 起草前建立必要Plan，按已确认输入完成局部辅助稿。
- 精简数据播报、研究操作流水账和重复组织说明。
- 按分句判断Results中的观察、就近解释与机制论证职责。
- 保留关键条件、反例、数字口径、引用职责与论断强度。
- 无实质问题时输出 `NO MATERIAL ISSUE`，保留正常表达。

适用于纯试验、纯数值、试验＋数值、理论＋数值及参数分析。用户应提供研究对象、章节目标、已确认事实/解释、正文与必要图表上下文。Skill运行无需网络；可选读取器只依赖Python 3.9及以上的标准库。

## 非适用范围

不承担事实审计、文献检索、科研推断、补算数据、机制发现或投稿格式认证。不自动解决研究输入冲突，不以案例事实补全新稿。Title / Keywords尚无专用Playbook；不提供保证优于作者原稿的自动终稿生成器。

## 六个章节Playbook

| 章节 | 主要职责 |
| --- | --- |
| Introduction | 工程问题、已有知识、具体缺口、科学综合与RQ层级；定位为PLANNING + ASSISTED DRAFTING。 |
| Methods | 按对象、配置、加载/边界、指标与说明依赖组织足以理解和复现的条件。 |
| Results | 报告已确认的响应、对比、阶段、转折和异常，按用途选取数字。 |
| Discussion | 围绕结果锚点建立有依据的解释增量、条件关系和机制比较。 |
| Conclusion | 提炼正文已成立的认识和方法贡献，保留必要条件。 |
| Abstract | 从正文命题与证据链压缩出研究问题、方法职责、关键结果与意义。 |

Scientific Synthesis是Introduction补充模块，**不是第七个章节**。入口见[运行清单](skills/chinese-engineering-manuscript-writer/runtime_manifest.md)。

## 31条横向规则：三级体系

| 强度 | 数量 | 执行方式 |
| --- | ---: | --- |
| LEVEL_1_HARD | 9 | 仅识别有具体依据的逻辑、语义、口径或证据不一致；不猜填事实。 |
| LEVEL_2_STRONG | 16 | 通常遵循，先检查上下文、用途与合理例外，再作最小修改。 |
| LEVEL_3_HEURISTIC | 6 | 可选的风格或组织启发，不凭形式自动判错或重写。 |

31条规则正文沿用批准版本。D-01→C-01、L-03→G-02为别名；METHODS-IMPL-01属于Methods实施原则，不计入31条。案例和风格卡按需读取，不默认把全部规则与Playbook加载进上下文。

公开包包含24个案例ID的**模式摘要**与14张Style Cards。摘要不是论文原文，也不是新造的真实正例；原稿、完整改稿、受控长文本及内部溯源材料不随包发布。

## Codex本地安装

下载本仓库或发布ZIP，在仓库根目录打开PowerShell。将完整Skill子目录复制到Codex的skills目录；已有同名目录时停止，避免覆盖本地修改：

```powershell
$skillName = 'chinese-engineering-manuscript-writer'
$skillRoot = if ($env:CODEX_HOME) {
    Join-Path $env:CODEX_HOME 'skills'
} else {
    Join-Path $HOME '.codex/skills'
}
$skillDestination = Join-Path $skillRoot $skillName
if (Test-Path -LiteralPath $skillDestination) {
    throw '同名Skill已存在，请先自行确认备份或更新方式。'
}
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath (Join-Path 'skills' $skillName) -Destination $skillDestination -Recurse
```

安装后下一轮对话可调用。也可将 `skills/chinese-engineering-manuscript-writer` 整个文件夹手动复制到自己的Codex skills目录。不要只复制SKILL.md。

## 使用 $skill-installer 从GitHub安装

维护者将本包上传至下述仓库并提供main分支后，在Codex中发送：

```text
$skill-installer 从 GitHub 仓库 LHJ312/chinese-engineering-manuscript-writer 安装
路径 skills/chinese-engineering-manuscript-writer，使用 main 分支。
```

对应installer参数为：

```text
--repo LHJ312/chinese-engineering-manuscript-writer --path skills/chinese-engineering-manuscript-writer --ref main
```

维护者创建 `v1.0.0` 标签后，可将 `--ref main` 改为 `--ref v1.0.0` 固定版本。当前包未自动创建GitHub仓库或标签，也未联网验证目标仓库已发布。installer会拒绝覆盖已存在的目标目录。

## 快速使用

```text
$chinese-engineering-manuscript-writer
请根据下面已确认的研究对象、文献认识与研究设计，生成Introduction的
Scientific Synthesis和RQ层级Plan。暂不写完整引言，不新增文献空白。
```

```text
$chinese-engineering-manuscript-writer
请对以下Results段落作最小编辑。保留数字、比较口径、反例和必要限定。
如无实质问题，请输出NO MATERIAL ISSUE；待确认项与正文分开。
```

```text
$chinese-engineering-manuscript-writer
请依据我提供的Results与已确认物理解释，判断哪些分句可留在Results、
哪些需要承担Discussion功能。只作局部组织判断，不补机制。
```

```text
$chinese-engineering-manuscript-writer
请从以下正文已成立的认识辅助起草摘要，列出关键命题的正文依据。
不要新增正文不存在的结论，不把不同指标概括成全面改善。
```

可选资产读取命令（在Skill目录执行）：

```text
python scripts/read_runtime_asset.py rules --ids C-01,F-02
python scripts/read_runtime_asset.py list --kind case --section Results
python scripts/read_runtime_asset.py read --kind case --id RES-03
python scripts/read_runtime_asset.py read --kind style --id SC-09
```

无Python时仍可使用Markdown文件；按JSON规则索引的相应行号读取。

## 验证方法与Holdout结果

采用冻结语料的分层开发与验证，按真实章节功能检查适用性、误伤、证据边界和最小修改。最终留出测试锁定运行包与六项任务，由两个独立上下文执行，再由第三个未参与起草的上下文一次性评价；测试中不修包、不改答案。评价属于模型会话评价，不冒充人工或不同模型验证。

**任务级Holdout结果：3 PASS + 3 PASS_WITH_NOTE + 0 FAIL**，NOT_ASSESSABLE为0。

| 论文级综合 | 结果 |
| --- | --- |
| H14：覆冰导线 | PASS_WITH_NOTE |
| H15：藏式木梁柱节点 | PASS_WITH_NOTE |

预注册要求两篇均不FAIL、**至少一篇综合PASS**，并要求无结构性缺口或系统性补造、能够保护正常表达。两篇均有注记，因此严格门槛**未完全满足**。本轮没有发现STRUCTURAL_SKILL_GAP或系统性事实/机制补造；H15的正常结论段合理输出NO MATERIAL ISSUE。

详见[验证说明](docs/validation.md)。该结果来自脱敏前的冻结运行包；公开包经过路径迁移和案例摘要化，**没有重新运行行为测试**。公开包检查仅验证结构、兼容性、脱敏与完整性。

## 已知限制

- 输入缺少百分比基准或解释前提时，仍需作者补充上下文；不自动补定。
- 文本与图表存在阶段或指标冲突时，草稿可能仍附作者确认项。
- 留出执行曾出现一次无依据的符号疑问；不存在“零误伤”承诺。
- 两篇六项局部任务不证明全部工程对象、章节或研究类型的广泛泛化。
- 公开摘要化案例不能替代原始语料作逐字复核；原始留出文本不公开。
- 不继续为细小风格差异开发新版本；后续重复性的跨论文问题才可累计为v1.1依据。

## 仓库与发布检查

运行Skill位于 `skills/chinese-engineering-manuscript-writer/`，所有运行依赖均在其内部。`scripts/`提供正式运行所需的轻量读取器；子目录LICENSE和NOTICE保证通过installer只安装Skill时仍携带许可和必要版权声明。

- [方法说明](docs/methodology.md)
- [核心语料设计](docs/corpus_design.md)
- [发布包检查](docs/package_checks.md)
- [文件清单](FILE_MANIFEST.json)与[SHA-256清单](SHA256SUMS)

## License

本项目采用[PolyForm Noncommercial License 1.0.0](LICENSE)，公开署名与版权声明见[NOTICE](NOTICE)。这是允许非商业用途的源码公开许可，不是允许任意商业使用的开源许可。

| 用途 | 授权范围 |
| --- | --- |
| 修改代码或Skill | 允许，限许可证允许的用途。 |
| 二次发布 | 允许，限许可证允许的用途；随副本保留许可条款或其URL及全部Required Notice声明。 |
| 科研和论文写作 | 允许，须符合许可证的允许用途条款。 |
| 商业使用 | 本包不授予商业使用许可。 |

以上为便于阅读的摘要，不更改许可证正文；具体允许用途包括其Noncommercial Purposes、Personal Uses及Noncommercial Organizations条款，以[完整条款](LICENSE)为准。[官方许可证来源](https://github.com/polyformproject/polyform-licenses/blob/1.0.0/PolyForm-Noncommercial-1.0.0.md)。

书目信息与外部链接不意味着取得原论文再分发许可；论文正文、图表和其他第三方材料的权利仍属于各自权利人，本包不附这些材料。

## Citation

可按项目名、公开署名和使用版本引用：

> LHJ312. chinese-engineering-manuscript-writer, v1.0.0. https://github.com/LHJ312/chinese-engineering-manuscript-writer

按维护者要求，当前不提供CITATION.cff，不公开联系邮箱、姓名拆分字段或ORCID，也不虚构DOI。
