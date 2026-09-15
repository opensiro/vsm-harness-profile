# RFC: Organizational Synthesis Model (OSM)

> **Status: non-canonical working extension.** OSM synthesis phases, transformation primitives, and assisted-viability measures are local hypotheses built on VSM. They are not attributable to Stafford Beer and are not requirements of the VSM Harness Profile.

Status: Draft

Extends: Stafford Beer — Viable System Model (VSM)

> This document describes an experimental model of organizational transformation. It is implementation-agnostic and does not prescribe a particular runtime, agent framework, file format, or synthesis engine.

---

# Abstract

Classical Viable System Model (VSM) describes the structural properties required for an organization to remain viable.

This document does not modify the VSM itself.

Instead, it introduces a complementary model describing how organizational systems transform, acquire additional regulatory capacity, and change their recursion structure over time.

A central OSM claim is that organizational functions should appear in response to actual regulatory variety rather than because an implementation is trying to mirror every VSM label. A dedicated S2, S3, S3*, S4, or S5 mechanism may be redundant at a particular boundary when the distinction it would regulate is absent, already absorbed locally, structurally collapsed into another actor, or explicitly supplied by a parent system.

This does **not** mean that arbitrary VSM functions may be removed without consequence. If the relevant variety appears, the organization must either provide the corresponding regulatory function locally or obtain it from another recursion level. Parent-supplied functions indicate assisted rather than fully local viability.

---

# 1. Scope

Classical VSM asks:

> What organizational functions and relationships make a system viable?

This document asks:

> How do organizational systems create, transform, divide, merge, simplify, and mature other organizational systems over time?

OSM is therefore concerned with transitions between organizational configurations rather than with replacing the VSM taxonomy itself.

---

# 2. Axiom of Snapshot

A VSM mapping is defined at a discrete moment in time.

A system is therefore represented as an organizational snapshot: `VSM(t)`.

Organizational change is represented as a transition between snapshots:

```text
VSM(t1) ──Transformation──► VSM(t2)
```

Questions such as these become questions about the transition rather than the snapshot itself:

- Which function became necessary first?
- When did coordination become distinct from operations?
- When did a parent stop supplying policy or adaptation?
- When did a recursive unit acquire enough local regulation to become independently viable?

The model therefore separates **organizational state** from **organizational synthesis**.

---

# 3. Axiom of Recursion

Every viable system contains operational units. Whenever an operational unit itself requires independent viability, it may be represented recursively as its own VSM.

```text
VSM
 ├── S1 (VSM) ──┬── S1 (VSM)
 │              ├── ...
 │              └── metasystem
 ├── S1 (VSM)
 └── S1 (VSM)
```

Recursion represents organizational decomposition, not inheritance and not technical nesting.

A spawned worker, subgraph, process, or child agent does not become a recursive VSM merely because it is nested. It requires its own relevant environment, operations, bounded autonomy, and enough regulatory closure for the variety assigned to it.

---

# 4. Axiom of Existing Viability

Organizational synthesis does not begin from an organizational vacuum. Every transformation starts from at least one already functioning system capable of supplying the initial regulation required for the transition.

In practice, the source of that viability may be:

- a human operator;
- a parent organization;
- an existing autonomous agent organization;
- a human–agent system;
- another viable operational unit.

A child organization may therefore begin with substantial regulatory functions supplied externally by its parent and acquire them locally only when needed.

This is important for agent harnesses: a newly created worker or sub-organization does not need to reproduce six named VSM components immediately. Its parent can temporarily supply coordination, resource regulation, audit, adaptation, or policy closure while the child remains focused on operations.

---

# 5. Organizational Transformations

Let `V` represent the set of organizational systems under analysis. Organizational evolution consists of transformations over elements of `V`.

Primitive transformations include:

## Split

One organizational system becomes multiple recursive systems or candidate recursive systems.

```text
   VSM_a            VSM_a
     │       ──►     ├─ VSM_a1
    ...              └─ VSM_a2
```

## Merge

Multiple systems are reorganized under one shared viable identity and metasystem.

## Intersection

A new organizational unit is formed from a shared mission, capability, or operational domain of multiple existing systems while the parent systems continue to exist.

## Remove

A recursive unit or regulatory mechanism is detached from the organization. The remaining system must still absorb the variety that the removed unit previously handled.

## Reconfigure

Internal responsibilities, channels, decision rights, or recursion boundaries are changed without replacing the organizational identity.

## Collapse

A previously distinct regulatory function is absorbed into another actor or mechanism because maintaining a separate structure is no longer justified by the variety being regulated.

For example, an independent coordination agent may disappear when two operational units are merged into one unit and no longer create cross-unit oscillation.

## Externalize

A function previously performed locally is moved to a parent, human authority, shared platform, or other recursion level.

For example, a child harness may stop maintaining its own S5-like policy authority and instead operate under parent-owned policy boundaries.

---

# 6. Conditional Emergence of VSM Functions

OSM treats synthesis as **demand-driven acquisition of regulatory capacity**, not as a mandatory sequence in which every system must instantiate S1, S2, S3, S3*, S4, and S5 as separate components.

The phase numbers below are a useful ordering heuristic. They are not a requirement that every organizational snapshot contain a dedicated implementation of every phase.

## Phase 0 — Intent

An existing viable system determines that a new organizational capability or recursive unit is useful.

## Phase 1 — Operational Formation

Operational capability is established.

From the parent's perspective, this becomes a candidate S1 unit. Operational capability is the only function that cannot be omitted from a system that is claimed to perform work in its environment.

## Phase 2 — Coordination

S2 becomes necessary when multiple operational units can interfere, oscillate, duplicate work, contend for shared state, or otherwise require mutual stabilization.

A dedicated S2 mechanism may be redundant when:

- there is only one operational unit at the declared boundary;
- operational units are independent and cannot materially interfere;
- coordination is completely absorbed by local protocols without a distinct organizational responsibility.

If interference later appears, coordination must emerge somewhere in the organization.

## Phase 3 — Inside-and-now regulation

S3 becomes distinct when the system requires whole-system current regulation such as shared resource bargaining, cross-unit prioritization, accountability, synergy, or intervention on behalf of the whole.

A dedicated S3 mechanism may be redundant when:

- no shared resources or cross-unit commitments require whole-system regulation;
- current control is small enough to be absorbed directly by the operational unit;
- the parent system explicitly retains this authority.

Parent-owned current regulation means the child has not yet acquired full local control at that recursion level.

## Phase 4 — Complementary audit

S3* becomes necessary when routine operational reporting is insufficiently trustworthy, complete, independent, or timely for the relevant risk.

A separate S3* path may be redundant when:

- ordinary reporting already provides the required confidence;
- the cost or risk of reporting error is negligible;
- an independent audit path is supplied by the parent or surrounding institution.

S3* should not be created merely to satisfy a diagram. It becomes useful when information asymmetry or verification risk justifies a materially different route to operational reality.

## Phase 5 — Adaptation

S4 becomes distinct when the system must model external change, future possibilities, threats, opportunities, or capability transitions and feed those distinctions back into present organization.

A local S4 mechanism may be absent when:

- the relevant environment and task horizon are intentionally fixed;
- the child is not expected to adapt its own organization;
- environmental intelligence and future-oriented adaptation are supplied by a parent system.

Such absence is acceptable for a bounded child organization, but a child that depends indefinitely on parent-owned adaptation should not be described as independently adaptive at that recursion level.

## Phase 6 — Policy and identity closure

S5 becomes distinct when the organization needs legitimate local authority over identity, policy, ultimate boundaries, or unresolved tension between current operations and future adaptation.

A local S5 mechanism may be absent when:

- identity and policy are intentionally fixed by the parent;
- the child has no delegated authority to redefine its purpose or ultimate constraints;
- no unresolved S3–S4 tension is delegated to the child.

This is common for subordinate agent organizations: they can be highly autonomous operationally while remaining parent-governed at the policy level.

---

# 7. Redundancy, Collapse, and Acceptable Absence

OSM distinguishes three situations that are often conflated.

## 7.1 Redundant component

The **organizational function exists**, but a dedicated component would add no useful regulatory capacity.

Example: one agent both performs work and applies a small fixed resource budget. Creating a separate "S3 agent" solely for naming symmetry would add structure without adding requisite variety.

## 7.2 Function not currently demanded

The triggering organizational distinction is absent at the declared boundary.

Example: one isolated operational unit has no peer unit with which it can oscillate, so there is no current S2 coordination problem.

This is a conditional absence. If the organizational variety changes, the missing function may become necessary.

## 7.3 Function supplied by a parent

The function is real and necessary, but the child does not own it locally.

Example: a child coding organization performs planning and execution while a human parent retains final policy, budget, and escalation authority.

This is **assisted viability**. It should be recorded as parent-supplied rather than misclassified as local autonomy.

## 7.4 What is not allowed

A function is not safely absent merely because:

- no component has its VSM name;
- the implementation would be simpler without it;
- a framework has no primitive for it;
- the function exists in theory but no actor has the information or authority to perform it.

The correct test is always whether the relevant variety exists and, if it does, where that variety is actually absorbed.

---

# 8. Assisted Viability

A newly synthesized recursive system rarely begins fully autonomous. Missing regulatory functions may be temporarily supplied by its parent organization.

Assistance can include:

- coordination between child operations;
- current resource regulation;
- independent verification;
- environmental intelligence and adaptation;
- policy, identity, and escalation closure.

As the child acquires decision rights, information channels, and regulatory capacity, selected functions may move from the parent into the child.

Let `A(t)` represent local organizational autonomy only as an informal abstraction:

```text
A = 0          Parent-controlled
0 < A < 1      Shared / assisted viability
A = 1          Locally closed for the relevant delegated variety
```

`A = 1` does **not** require six separate agents or six separately deployed components. It means that the child can locally absorb the relevant variety delegated to it, including the VSM functions that are actually required at that boundary.

A child whose policy or adaptation is intentionally parent-owned can still be operationally autonomous, but should be described as parent-governed rather than fully locally closed.

---

# 9. Examples

These examples illustrate conditional emergence rather than prescribe canonical architectures.

## Example A — Single coding agent under a fixed task

```text
Parent / human
  ├─ policy, budget, escalation
  └─ Coding agent
       └─ tools + repository
```

Possible interpretation:

- **S1:** present — the coding agent performs the primary work.
- **S2:** locally redundant — there is no second operational unit to coordinate with.
- **S3:** mostly parent-supplied — the parent owns budget and whole-task intervention.
- **S3*:** absent unless independent verification is required.
- **S4:** absent locally if the task and environment are intentionally fixed.
- **S5:** parent-supplied — the child cannot redefine mission or policy.

Creating separate S2, S3, S4, and S5 agents here would usually be organizational over-modeling.

## Example B — Parallel coding swarm with shared repository state

```text
                 Parent policy
                     │
             current regulation
                     │
        ┌────────────┼────────────┐
      S1-A          S1-B         S1-C
        \             |            /
         └──── coordination ──────┘
```

Possible interpretation:

- **S1:** several coding units operate concurrently.
- **S2:** required because branches, files, locks, tests, or shared plans can conflict.
- **S3:** useful when budgets, priorities, WIP, or shared resources require whole-system regulation.
- **S3*:** useful only if ordinary unit reports cannot provide enough confidence; an independent replay or evaluator could supply it.
- **S4:** not automatically present merely because workers plan tasks. It appears only if the organization models external/future change and adapts itself accordingly.
- **S5:** may remain parent-owned.

Here S2 emerges because the organization acquired interaction variety that did not exist in Example A.

## Example C — Parent-governed domain harness

Consider a scientific or government-domain harness whose operational agents can act autonomously inside a tightly defined mandate, while mission, legal boundaries, and final policy remain external.

Possible interpretation:

- operational S1 units can be highly autonomous;
- S2 and S3 may be local because the units share data, resources, schedules, or commitments;
- S3* may become important when independent evidence is required for safety, compliance, or accountability;
- S4 may be local if the harness is expected to track changing regulation, literature, threats, or capabilities;
- S5 can remain parent-governed if the harness is not authorized to redefine the mandate.

The absence of local S5 is therefore not an implementation defect. It is a statement about the recursion boundary and retained parent authority.

## Example D — When a system becomes redundant after reconfiguration

Suppose a harness originally contains three workers plus a coordination agent. Later the workers are merged into one durable operational agent with one work state and no concurrent peer operations.

```text
Before:  S1-A + S1-B + S1-C + coordination
After:   one S1
```

The previous dedicated S2 component can now be removed without losing a required organizational function because the coordination problem itself disappeared at that boundary.

If parallel operations are introduced again, S2 may need to re-emerge.

---

# 10. Relationship with Classical VSM

Classical Stafford Beer VSM defines the functional organization of viable systems. OSM describes hypothetical transformations between organizational configurations and the progressive or conditional acquisition of those functions.

Therefore:

- Classical VSM asks: *What organizational functions make a system viable?*
- OSM asks: *How does an organizational system move from one configuration of those functions to another?*

OSM does not redefine S1–S5 and does not claim that Beer described the phases, primitives, autonomy notation, or redundancy rules in this document.

The VSM Harness Profile remains authoritative for the repository's engineering interpretation of each VSM function.

---

# 11. Design Principles

1. Organizational synthesis starts from existing regulatory capacity rather than an empty organizational state.
2. Every organizational state can be represented as a discrete snapshot for analysis.
3. Organizational evolution is a sequence of transformations between snapshots.
4. Recursive viability is organizational, not merely technical nesting.
5. Regulatory functions should emerge in response to actual variety rather than naming symmetry.
6. A dedicated component may be redundant even when the organizational function it contributes to remains necessary.
7. A locally absent function must be either not demanded at the declared boundary or supplied elsewhere.
8. Parent-supplied functions imply assisted or parent-governed viability rather than full local closure.
9. Removing a function is valid only if the organization still absorbs the variety that function previously handled.
10. Full local closure does not require one agent or service per VSM system.

---

# Future Work

This document intentionally leaves undefined:

- algebra of organizational transformations;
- formal invariants preserved during transformations;
- formal criteria for when a function becomes necessary;
- measurable thresholds for collapse versus separation of functions;
- complexity and autonomy metrics;
- machine-readable transformation semantics;
- empirical tests for assisted versus local viability.

These constitute the next layer of formalization.
