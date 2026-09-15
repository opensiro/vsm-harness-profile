# Terminology normalization across agent harnesses

> **Supplementary, non-normative evidence for the [VSM Harness Profile](../PROFILE.md).**

> **One term can describe different responsibilities. Different terms can describe the same responsibility.**

This note gives concrete examples from popular agent harnesses and orchestration frameworks. Its purpose is not to claim that the upstream projects implement the Viable System Model (VSM). It demonstrates why a cross-harness profile cannot infer organizational responsibility from framework vocabulary alone.

OpenSiro VSM therefore normalizes **observable organizational function and relationships first**, and only then asks whether the behavior maps to S1, S2, S3, S3*, S4, S5, or to a technical/external mechanism that does not establish a VSM function by itself.

## Reading the VSM maps

The mappings below follow the repository's [PROFILE.md](../PROFILE.md), especially these rules:

- component names are never sufficient evidence;
- a router, workflow edge, task sequence, speaker selector, or parent-to-child delegation is **not S2 merely because it moves or assigns work**;
- a manager, orchestrator, controller, supervisor, task allocator, or result aggregator is **not S3 without whole-system current regulation and relevant authority**;
- a checker, critic, validator, or verifier is **not S3\*** without a sufficiently independent complementary path to operational reality;
- an `Agent` is **not automatically S1**: an S1 mapping needs an operational outcome, a relevant local environment, and meaningful local autonomy.

Accordingly, `not sufficient for S2/S3` is a positive result of the mapping process, not a missing classification.

---

## A. One term can describe different responsibilities

| # | Shared term | Harness A / observed responsibility | VSM map A | Harness B / observed responsibility | VSM map B | Normalization point |
|---|---|---|---|---|---|---|
| **1** | `manager` | [**OpenAI Agents SDK — Manager pattern**](https://github.com/openai/openai-agents-python/blob/main/docs/agents.md#manager-agents-as-tools): a central LLM agent invokes specialists as tools and retains control of the conversation. | The manager can itself be an **S1** operational unit if it directly owns an outcome and local variety at the chosen boundary. The manager pattern **does not establish S3 by itself**; calling specialists is task decomposition unless whole-system current regulation and authority are also present. | [**AutoGen — `SwarmGroupChatManager`**](https://github.com/microsoft/autogen/blob/main/python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_swarm_group_chat.py): runtime component that selects the next speaker from handoff messages and maintains group-chat state. | Primarily a **technical control-flow / speaker-selection mechanism**. It is **not S2 merely because it selects a speaker**, and it is not S3 without whole-system regulatory authority. | The label `manager` covers an acting delegator in one harness and a runtime conversation coordinator in another. |
| **2** | `manager` | [**CrewAI — hierarchical manager agent**](https://github.com/crewAIInc/crewAI/blob/main/docs/v1.15.0/en/learn/hierarchical-process.mdx): allocates tasks among crew members, coordinates workflow, and validates outcomes. | **Potential S3 contribution, conditional.** Allocation and validation can participate in inside-and-now control only when the manager has a whole-system view and authority over relevant shared resources/constraints. Delegation alone is not S3; routine validation alone is not S3*. | [**Semantic Kernel — `GroupChatManager`**](https://github.com/microsoft/semantic-kernel/blob/main/docs/decisions/0071-multi-agent-orchestration.md): governs group-chat progression, including next-agent selection and orchestration state. | Primarily **conversation-flow arbitration**. It does not establish S2 unless it regulates actual interference among S1 units, and does not establish S3 without current whole-system regulation and authority. | Same word, but CrewAI bundles supervisory task management while Semantic Kernel uses a manager as an orchestration actor for conversation flow. |
| **3** | `handoff` | [**OpenAI Agents SDK — handoff**](https://github.com/openai/openai-agents-python/blob/main/docs/handoffs.md): a peer agent transfers the conversation to a specialist, which takes over. | A **control-transfer relation/channel**. If the participants qualify as S1 units, the handoff can connect operational units, but **handoff is not S2 by itself** because transfer does not prove conflict/oscillation damping. | [**Pydantic AI — programmatic agent hand-off**](https://github.com/pydantic/pydantic-ai/blob/main/docs/multi-agent-applications.md#programmatic-agent-hand-off): multiple agents are called in succession while application code and/or a human decides which agent runs next. | **External / parent-owned control-plane sequencing.** The decision right is application/human-owned rather than necessarily agent-owned. It does not establish S2 or S3 by itself. | `handoff` can mean agent-to-agent active-control transfer or application-level sequencing between separate runs. |
| **4** | `agent` | [**OpenAI Agents SDK — `Agent`**](https://github.com/openai/openai-agents-python/blob/main/docs/agents.md): an LLM configured with instructions, tools, handoffs, guardrails, and runtime behavior. | **Candidate S1, conditional on boundary and behavior.** It maps to S1 only when it directly enacts the system's purpose in a local environment with meaningful discretion; the class name is not evidence by itself. | [**Google ADK — workflow agents**](https://github.com/google/adk-docs/blob/main/docs/agents/workflow-agents/index.md): `SequentialAgent`, `ParallelAgent`, and `LoopAgent` control sub-agent execution using predefined deterministic logic without consulting an AI model for orchestration. | Primarily **technical orchestration / execution control**, not S1 merely because the component is named `Agent`. Sequential or parallel execution also does not establish S2 without evidence of interference regulation among S1 units. | `agent` may denote an LLM-driven operational actor or a deterministic workflow controller. |
| **5** | `delegation` | [**Pydantic AI — agent delegation / `SubAgents`**](https://github.com/pydantic/pydantic-ai/blob/main/docs/multi-agent-applications.md#agent-delegation): a parent calls a delegate as a bounded subtask and takes control back when it finishes. | **Task decomposition / retained parent authority.** Delegation itself is neither S2 nor S3. A delegate can qualify as S1 only if it has its own operational outcome, relevant environment, and meaningful autonomy at the chosen recursion level. | [**CrewAI — hierarchical task delegation**](https://github.com/crewAIInc/crewAI/blob/main/docs/v1.15.0/en/learn/hierarchical-process.mdx): a manager assigns work to crew members and validates results as part of the hierarchical process. | **Potential S3 contribution, conditional** on whole-system current view plus actual authority over shared constraints/resources. The delegation act alone is not S3 and does not establish S2. | Both call the behavior delegation, but one is explicitly a nested call-return relation while the other is embedded in a broader managerial role. |

---

## B. Different terms can describe the same responsibility

| # | Normalized responsibility | Harness A / term | VSM map A | Harness B / term | VSM map B | Normalization point |
|---|---|---|---|---|---|---|
| **6** | **Transfer active control to another specialist** | [**OpenAI Agents SDK — `handoff`**](https://github.com/openai/openai-agents-python/blob/main/docs/handoffs.md) | A control-transfer channel between actors. If both actors are S1 units, this is a relation between operations; **not S2 merely because control moves**. | [**Google ADK — `transfer_to_agent`**](https://github.com/google/adk-python/blob/main/src/google/adk/flows/llm_flows/agent_transfer.py) | A model-visible transfer mechanism to another eligible agent. Same VSM treatment: **control transfer does not itself establish S2/S3**; map the responsibilities of the source and target separately. | Different API terms expose essentially the same control-transfer responsibility. |
| **7** | **A central actor chooses specialists and assigns work** | [**LangGraph Supervisor — `supervisor` / `create_supervisor`**](https://github.com/langchain-ai/langgraph-supervisor-py/blob/main/README.md): central supervisor controls communication flow and task delegation. | **Not automatically S3.** It becomes S3 only if the supervisor regulates current operations on behalf of the whole with relevant shared-resource/constraint authority. Otherwise this is centralized task decomposition; specialists may separately qualify as S1. | [**CrewAI — `manager_agent`**](https://github.com/crewAIInc/crewAI/blob/main/docs/v1.15.0/en/learn/hierarchical-process.mdx): central manager strategically assigns tasks to crew members. | Same VSM rule: **conditional S3 at most from delegation evidence alone**. Need whole-system regulation and authority before making a positive S3 mapping. | `supervisor` and `manager` can implement the same centralized work-allocation responsibility. |
| **8** | **Invoke a specialist as a bounded subtask and retain caller authority** | [**OpenAI Agents SDK — `Agent.as_tool()` / agents-as-tools**](https://github.com/openai/openai-agents-python/blob/main/docs/agents.md#manager-agents-as-tools) | **Parent-owned task decomposition.** The caller retains conversational authority. This is not S2/S3 by itself; the specialist is S1 only if it independently meets the S1 criteria at the declared boundary. | [**Pydantic AI — `SubAgents` / `delegate_task(...)`**](https://github.com/pydantic/pydantic-ai/blob/main/docs/multi-agent-applications.md#agent-delegation) | Same map: **bounded delegation with retained parent control**, not a VSM metasystem function by itself. | `as_tool()` and `delegate_task()` use different vocabulary but expose the same parent-calls-specialist-and-returns pattern. |
| **9** | **A leader delegates work to named specialist agents** | [**smolagents — `managed_agents` / manager agent**](https://github.com/huggingface/smolagents/blob/main/docs/source/en/examples/multiagents.md): specialist agents are made callable by a manager agent. | **Centralized delegation; not automatically S3.** The manager may be an S1 actor or may contribute to S3 depending on system boundary, whole-system view, and actual regulatory authority. Managed workers are not automatically recursive S1s merely because they are agents. | [**Agno — `Team` leader with `members`**](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/team/team.py): a team model can choose/delegate work to member agents or teams. | Same VSM treatment: **delegation mechanism first, S3 only conditionally**; individual members require separate S1 evidence. | `managed_agents` and `Team.members` provide different object models for the same leader-to-specialist allocation responsibility. |
| **10** | **Fan out independent work to multiple execution units** | [**LangGraph — `Send`**](https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/langgraph/types.py): sends packets/state to specific graph nodes and is commonly used for dynamic fan-out. | **Execution-routing mechanism.** Parallel fan-out alone is not S2; S2 requires evidence that the mechanism regulates interference or oscillation among operational units. | [**Google ADK — `ParallelAgent`**](https://github.com/google/adk-docs/blob/main/docs/agents/workflow-agents/parallel-agents.md): executes multiple sub-agents in parallel under predefined workflow logic. | **Deterministic parallel orchestration.** Not S2 merely because multiple agents run concurrently; positive S2 requires a coordination problem among S1s plus regulation of that interference. | `Send` and `ParallelAgent` differ in abstraction and naming but both can implement fan-out execution without thereby implementing organizational coordination in the VSM sense. |

---

## What the examples demonstrate

Framework vocabulary is not a stable ontology.

A classifier based on names such as `manager`, `agent`, `handoff`, `supervisor`, `team`, `delegation`, `parallel`, `critic`, or `planner` will systematically make two kinds of error:

1. **false equivalence** — treating components with the same name as if they carried the same organizational responsibility;
2. **false difference** — treating equivalent responsibilities as different because frameworks expose them under different names or APIs.

The VSM Harness Profile avoids both errors by using this sequence:

```text
implementation / primitive
        ↓
observed behavior + decision rights + relationships
        ↓
normalized organizational responsibility
        ↓
VSM function, support mechanism, or no positive VSM mapping
        ↓
autonomy ownership at the declared system boundary
```

The practical rule is therefore:

> **Never infer a VSM responsibility from a framework term alone. Classify runtime behavior, relationships, authority, and boundary first; then map the result to the VSM profile.**

This is also why an honest mapping may conclude that a familiar multi-agent primitive is **not sufficient evidence for any S2/S3/S3*/S4/S5 function**. VSM normalization is useful precisely because it distinguishes organizational responsibility from implementation vocabulary.

## Scope and caveat

These examples are snapshots of documented behavior, not complete assessments of the listed harnesses. A full assessment can produce a different mapping when the system-in-focus, recursion level, configuration, or surrounding application changes. Upstream projects do not endorse the OpenSiro VSM interpretation unless explicitly stated by them.
