# INT-01 | PUBLIC_PATTERN_SUMMARY

section: Introduction
function: PLAN_TO_PROSE_LEAKAGE
reference_category: BAD_TO_GOOD

公开版仅保留编辑模式，不提供原段、改稿或原文的替代文本。模式不是待写论文的研究事实；实际编辑必须取得用户自己的输入与上下文。

**pattern_summary**：删除段末对前两句的再次归类；保留核心关系和所有分支。

**why_it_works**：删除段末对前两句的再次归类；保留核心关系和所有分支。

**when_to_use**：同一缺陷与给定基线存在时，仅作已列改动。

**when_not_to_use**：不改前文文献Gap，不把各工况统一成同条件验证。

**material_issue_scope**：只修复明确组织或语义缺陷；不认证其他研究内容。

**recommended_action**：MINIMAL_EDIT

**preserve**：不改前文文献Gap，不把各工况统一成同条件验证。

linked_rules: K-02, B-01

未公开来源内容与身份已移除；只保留通用写作动作。

## 来源表示

```json
{
  "case_id": "INT-01",
  "section": "Introduction",
  "case_type": "PUBLIC_PATTERN_SUMMARY",
  "reference_category": "BAD_TO_GOOD",
  "function": "PLAN_TO_PROSE_LEAKAGE",
  "linked_rules": [
    "K-02",
    "B-01"
  ],
  "text_representation": "EDITORIAL_PATTERN_SUMMARY_NOT_ORIGINAL_TEXT",
  "original_text_included": false,
  "edited_text_included": false,
  "source_scope": "UNPUBLISHED_SOURCE_WITHHELD",
  "source_locator": null
}
```
