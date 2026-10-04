# Approve all of them.And add some ui imporvements Proceed Level L

## Goal
Approve all of them.And add some ui imporvements Proceed Level L

## Deliverable
The user-requested outcome described in the full goal, with supporting evidence appropriate to that outcome

## Constraints
- Do not bypass the fixed six-stage governed runtime.
- Do not widen scope silently beyond the frozen requirement document.

## Acceptance Criteria
- Requirement document is frozen before execution.
- Execution plan exists before task execution.
- Verification evidence exists before completion claims.
- Phase cleanup receipt is produced.

## Product Acceptance Criteria
- Requirement document is frozen before execution.
- Execution plan exists before task execution.
- Verification evidence exists before completion claims.
- Phase cleanup receipt is produced.
- The delivered output must satisfy observable behavior implied by the frozen goal and deliverable, not only internal runtime progress.
- Full completion wording is allowed only after downstream delivery truth is passing.

## Manual Spot Checks
- None required beyond automated verification for this task unless the execution scope expands to a user-visible or interactive flow.

## Completion Language Policy
- Full completion wording is allowed only when governance truth, engineering verification truth, workflow completion truth, and product acceptance truth are all passing.
- `completed_with_failures`, degraded execution, or pending manual actions must be reported as non-complete states.
- If manual spot checks remain pending, the run must be described as requiring manual review rather than fully ready.

## Delivery Truth Contract
- Governance truth: requirement, plan, execution, and cleanup artifacts remain traceable and authoritative.
- Engineering verification truth: targeted verification passes or fails explicitly; silence does not count as success.
- Workflow completion truth: planned units, delegated lanes, and specialist outputs reconcile back into the governed plan.
- Product acceptance truth: observable deliverable behavior satisfies frozen acceptance criteria before full completion language is allowed.

## Code Task TDD Mode
TDD mode: required
Decision source: runtime_inference
Reason: The task includes implementation or defect-correction intent that requires code-task TDD evidence.

## Code Task TDD Evidence Requirements
- Record failing-first evidence for the changed behavior before implementation or defect correction.
- Record the green rerun that proves the targeted behavior passed after implementation.
- Map the changed behavior to targeted verification evidence; generic suite success alone is insufficient.
- If automated failing-first evidence is not appropriate, freeze and honor an explicit code-task TDD exception instead of silently skipping the requirement.

Non-goals:
- Do not create separate M/L/XL entry commands.
- Do not introduce a second router or control plane.

## Skill Search Guide
- 先拆任务，再拆模块
- 会按模块搜索本地 skills
- 每个模块单独搜索本地 skills
- 会先看候选 skill 名和短描述，再打开并阅读候选 `SKILL.md`
- 每个模块最多保留 3 个候选，避免上下文污染
- 以候选 `SKILL.md` 的真实用途为准，不按词面碰撞判断
- 会给出 `L` / `XL` 两套 skills 组织方案，并说明每个 skill 的职责
- 优先选择真正负责该模块的 owner，不选只沾边的 helper
- 一个 skill 可以覆盖多个模块
- explicit_only skills 只有在用户明确点名时才可入选
- 不得跨越候选 skill 声明的负边界或适用限制
- 没有 owner 时必须报缺口，不得伪装覆盖
- 没有 owner 的模块会明确标出缺口
- requirement 阶段公开搜索办法，并在请用户选择前由 Agent 分别给出 L / XL 的具体工作流和候选 skill 名称；这些名称必须标为尚未正式选定或使用，不得公开程序候选排名或预选结果
- xl_plan 阶段公开模块、候选、最终采用和缺口
- execute 阶段公开本次实际启用的 skills

## Workflow Level Confirmation
- User-visible: True
- Recommended level: L
- Recommendation reason: 当前任务更像单主线交付：先冻结需求和计划，再让 Agent 按模块组织一个较轻量的 skills 方案，通常比一开始就上分波次协作更省沟通成本。
- Why this decision matters: L 和 XL 会直接改变后续的协作深度、是否进入分波次执行，以及证据和回归边界的强度。
- Before asking the user to choose L or XL, explain each task-specific workflow and list its task-specific candidate skill names. Label those names as candidates that are not yet selected or used.
- L: L 级适合多步骤但主要串行的工作：会确认需求和计划，证据要求完整，但一般由一个主流程推进。
- L workflow: 先冻结需求和计划，再由一个主流程串行推进 Agent 组织出的方案。
- L skills: 会先按模块搜索本地 skills、阅读候选 `SKILL.md`，再给出较轻量的 L 级组织方案；涉及代码改动或缺陷修复时，会补充 `tdd` 这类 failure-first 验证 skill，但不默认拆成多代理。
- L rationale: 适合仍然是一个主交付物、依赖链较短、并行收益不高的任务，可以把沟通成本压低，同时保留完整的冻结与验证边界。
- L confirm reply: 如果你认可这个较轻量但证据完整的流程，请回复：`走 L 级`。
- XL: XL 级适合研究交付、多产物、多技能协作或风险更高的任务：会有更严格的需求冻结、计划冻结、分阶段执行、证据清单和收尾检查。
- XL workflow: 先冻结需求和计划，再把 Agent 组织出的方案拆成分波次执行；只有在依赖安全时才允许小步并行，最后统一回到验证和收尾。
- XL skills: 会先按模块组织更完整的本地 Skills；确需多代理时，由当前 Agent 依据已冻结计划分波次协调，不额外假定一个协调 Skill。
- XL rationale: 适合多产物、多技能协作、研究交付或高风险改动，因为它能先讲清分工、阶段边界和证据清单，再进入执行。
- XL confirm reply: 如果你希望先把分工和波次讲清楚，再进入更重的执行流程，请回复：`走 XL 级`。
- Question: 先确认任务级别：这次任务走 L 级还是 XL 级？
- Selection prompt: 请根据上面的说明选择并确认这次任务级别。

## Assumptions
- Interactive clarification is allowed if unresolved ambiguity materially changes the requested outcome.
