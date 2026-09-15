# RFC: Organizational Synthesis Model (OSM)

> **Status: non-canonical working extension.** OSM transformation primitives, regulatory-load interpretation, and assisted-viability concepts are local hypotheses built on VSM. They are not attributable to Stafford Beer and are not requirements of the VSM Harness Profile.

Status: Draft

Extends: Stafford Beer — Viable System Model (VSM)

> This document describes an experimental model of organizational transformation. It is implementation-agnostic and does not prescribe a particular runtime, agent framework, file format, or synthesis engine.

---

# Abstract

Classical Viable System Model (VSM) describes the functional organization required for viability.

This document does not modify the VSM itself.

Instead, it introduces a complementary model for reasoning about how organizational configurations change over time: how regulatory functions become active, separate, collapse, move across recursion boundaries, and are supplied by parent systems.

The central OSM hypothesis is that the observable need for distinct metasystemic regulation is driven by the regulatory problems present at a declared boundary.

In an idealized limiting case where:

- the environment does not change;
- information is perfect;
- operations are fully mutually compatible;
- local optimization always produces the correct whole-system result;
- purpose, policy, and identity never require choice or reinterpretation;

there is almost no active metasystemic regulatory workload. The organizational picture approaches:

```text
Environment ⇄ S1
```

This is not a claim that VSM systems can be arbitrarily deleted. It is a thought experiment about **regulatory load**: as the class of disturbance that a function compensates for approaches zero, the need for a distinct active implementation of that function also approaches zero.

Conversely, when the relevant disturbance appears, the organization must absorb it somewhere — locally, through a combined mechanism, through another recursion level, or through an external authority.

---

# 1. Scope

Classical VSM asks:

> What organizational functions and relationships make a system viable?

This document asks:

> How and why does an organizational system move from one configuration of those functions to another?

OSM focuses on transitions, emergence of regulatory load, redistribution of decision rights, and changes in recursion boundaries.

It does not replace the VSM taxonomy and does not define new canonical VSM systems.

---

# 2. Axiom of Snapshot

A VSM mapping is defined at a discrete moment in time.

A system is therefore represented as an organizational snapshot: `VSM(t)`.

Organizational change is represented as a transition between snapshots:

```text
VSM(t1) ──Transformation──► VSM(t2)
```

The snapshot says what organizational responsibilities exist and where they are carried at time `t`.

The transition explains what changed, for example:

- a second operational unit introduced coordination problems;
- local optimization began to conflict with whole-system constraints;
- ordinary reporting stopped being trustworthy enough;
- the environment became materially dynamic;
- policy or identity became ambiguous;
- a parent delegated a previously retained decision right;
- several responsibilities collapsed into one actor after complexity decreased.

OSM therefore separates **organizational state** from **organizational synthesis**.

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

A spawned worker, subgraph, process, or child agent does not become a recursive VSM merely because it is nested. It requires its own relevant environment, operations, bounded autonomy, and sufficient regulatory closure for the variety assigned to it.

---

# 4. Axiom of Existing Viability

Organizational synthesis does not begin from an organizational vacuum. Every transformation starts from at least one already functioning system capable of supplying the initial regulation required for the transition.

In practice, the source of that viability may be:

- a human operator;
- a parent organization;
- an existing autonomous agent organization;
- a human–agent system;
- another viable operational unit.

A child organization may therefore begin with substantial regulatory responsibilities supplied externally by its parent and acquire them locally only when required or delegated.

This matters for agent harnesses: creating a worker or sub-organization does not imply that six named VSM components should immediately be instantiated around it.

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

A recursive unit or regulatory mechanism is detached from the organization. The remaining organization must still absorb any relevant variety that the removed unit previously handled.

## Reconfigure

Responsibilities, channels, decision rights, or recursion boundaries are changed without replacing the organizational identity.

## Collapse

A previously distinct regulatory responsibility is absorbed into another actor or mechanism because a separate implementation no longer adds useful regulatory capacity.

Example: an independent coordination mechanism may disappear after several interacting operational units are merged into one unit and cross-unit oscillation disappears.

## Externalize

A responsibility previously performed locally is moved to a parent, human authority, shared platform, or another recursion level.

Example: a child harness may stop maintaining local policy authority and instead operate under parent-owned identity and policy boundaries.

---

# 6. Regulatory Load

OSM models metasystemic structure as a response to classes of organizational difficulty.

The following table is a conceptual interpretation for synthesis. It is not a replacement definition of the VSM systems.

| System | Regulatory problem that creates active load |
| --- | --- |
| **S2** | Dynamic interference, oscillation, or conflict between operational units. |
| **S3** | Divergence between local optimization and the needs of the whole; shared-resource and current-control problems. |
| **S3\*** | Imperfect, incomplete, delayed, strategically filtered, or otherwise insufficient routine information about operational reality. |
| **S4** | Environmental change, future uncertainty, threats, opportunities, or capability transitions requiring adaptation. |
| **S5** | Ambiguity or conflict concerning identity, policy, ultimate constraints, or the balance between present and future. |

This can be expressed informally as:

```text
Need(S2)  ∝ operational interference
Need(S3)  ∝ local/global optimization gap
Need(S3*) ∝ information uncertainty or asymmetry
Need(S4)  ∝ environmental and future change
Need(S5)  ∝ policy or identity ambiguity
```

The notation is conceptual, not a numerical metric.

The important claim is directional: when a regulatory problem grows, the organization requires more capacity to absorb it. When that problem disappears, a previously distinct regulatory mechanism may become redundant or collapse into another role.

A VSM function is therefore not equivalent to a permanently active named component.

---

# 7. Idealized Limiting Case

Consider an intentionally unrealistic boundary with all of the following conditions:

1. **Static environment** — no relevant external condition changes over time.
2. **Perfect information** — operational reality is fully observable with no delay, distortion, concealment, or uncertainty relevant to regulation.
3. **Perfect operational compatibility** — operational units never oscillate, collide, duplicate, or interfere.
4. **Perfect local/global alignment** — every locally optimal decision is also correct for the whole organization; there are no scarce shared resources or cross-unit trade-offs requiring current whole-system intervention.
5. **Fixed and unambiguous identity** — purpose, policy, boundaries, and ultimate constraints never conflict and never require reinterpretation.

Under those assumptions:

```text
operational interference        → 0  ⇒ active S2 load  → 0
local/global optimization gap   → 0  ⇒ active S3 load  → 0
information imperfection        → 0  ⇒ active S3* load → 0
environmental/future change     → 0  ⇒ active S4 load  → 0
identity/policy ambiguity       → 0  ⇒ active S5 load  → 0
```

The organizational picture approaches:

```text
Environment ⇄ S1
```

This is a **limiting case of zero regulatory load**, not a recommendation to build organizations as `S1` only.

Two qualifications matter:

- A system still requires a declared identity and boundary for us to call it the same system at all. In the limiting case, that identity is assumed fixed and unproblematic rather than continuously decided by an active S5 mechanism.
- A function can have near-zero active workload without being represented by a separate agent, process, or service. OSM is about regulatory necessity, not component count.

Real organizations depart from the limiting case precisely because one or more assumptions fail.

---

# 8. Trigger-Based Emergence

OSM does **not** prescribe a maturity sequence such as:

```text
S1 → S2 → S3 → S3* → S4 → S5
```

There is no requirement that functions become organizationally distinct in that order.

Instead, synthesis is trigger-based.

```text
S1 encounters additional regulatory variety
        │
        ├─ interference between operations  → S2 load
        ├─ local/global optimization gap    → S3 load
        ├─ insufficient routine information → S3* load
        ├─ environmental/future change      → S4 load
        └─ identity/policy ambiguity        → S5 load
```

Several loads may appear simultaneously. Some may disappear later. A previously external responsibility may move into the child. A previously separate component may collapse into another actor.

The synthesis question is therefore not:

> Which VSM system must be created next?

but:

> What new variety can no longer be absorbed by the current organization, and where should the corresponding regulatory capacity live?

## 8.1 S2 trigger — operational interference

S2 load appears when multiple operational units can create destructive interaction: oscillation, collision, duplication, contention, incompatible timing, or mutually destabilizing behavior.

A distinct coordination mechanism may be unnecessary when there is one S1 unit or when units are genuinely independent at the declared boundary.

## 8.2 S3 trigger — whole-system current regulation

S3 load appears when local decisions alone cannot preserve current cohesion of the whole: scarce shared resources, cross-unit priorities, commitments, performance trade-offs, or intervention on behalf of the whole become material.

If every local optimum is also a whole-system optimum and no shared trade-off exists, distinct S3 workload can approach zero.

## 8.3 S3* trigger — information imperfection

S3* load appears when routine S1–S3 reporting cannot provide sufficient confidence about operational reality.

The trigger is not merely the existence of logs or tests. It is the possibility that ordinary information is incomplete, delayed, filtered, mistaken, or otherwise insufficient for the relevant risk.

## 8.4 S4 trigger — change and future uncertainty

S4 load appears when the environment, threat model, user needs, regulation, capabilities, dependencies, or other future-relevant conditions can change enough that the organization must adapt.

In a truly static environment with no meaningful future distinction, active S4 workload approaches zero.

## 8.5 S5 trigger — policy and identity ambiguity

S5 load appears when legitimate choice is required about organizational identity, policy, ultimate constraints, or unresolved tension between present capability and future adaptation.

If those matters are perfectly fixed and never become ambiguous, active S5 decision workload can approach zero. The identity boundary remains conceptually present; what disappears is the need for recurrent identity-level choice.

---

# 9. Where a Required Function Lives

Only after establishing that a regulatory problem exists should OSM ask how that function is implemented.

This is a second-order question.

## 9.1 Local and distinct

The responsibility is implemented by a dedicated local actor or mechanism.

Example: a coordination agent arbitrates conflicting claims on shared repository state.

## 9.2 Local and collapsed

The responsibility is real but is absorbed by an actor that also performs another function.

Example: one durable operational agent enforces a small fixed resource budget on itself. Creating a separate "S3 agent" would not add useful regulatory variety.

## 9.3 Parent-supplied

The responsibility is required but retained by the parent organization.

Example: a child coding organization executes autonomously while a human or parent harness retains ultimate budget, adaptation, or policy authority.

This is **assisted / parent-governed viability** rather than local closure for that responsibility.

## 9.4 Externalized

The responsibility is performed by a shared external institution, platform, evaluator, regulator, or service outside the child organization.

Whether that still counts as part of the system-in-focus depends on the declared boundary and decision rights.

## 9.5 Not currently demanded

The triggering regulatory problem is absent at the declared boundary.

Example: a single isolated S1 has no peer operation with which to oscillate, so current S2 load is zero.

This is categorically different from a required function that nobody performs.

---

# 10. Acceptable Absence and Redundancy

OSM distinguishes four cases that should not be conflated:

| Case | Meaning |
| --- | --- |
| **Zero / negligible load** | The triggering regulatory problem is absent or negligible at the declared boundary. |
| **Collapsed implementation** | The function is required, but a separate component adds no useful capacity because another actor absorbs it. |
| **Parent/external supply** | The function is required, but decision rights or capacity live outside the child. |
| **Uncovered variety** | The function is required, but no actor has sufficient information, authority, or capacity to perform it. This is a viability problem, not acceptable absence. |

A VSM-named component is never required merely for diagrammatic symmetry.

But absence is not justified merely because:

- no component carries the VSM name;
- the implementation would be simpler without it;
- the framework has no primitive for it;
- the function is assumed to "happen somewhere" without evidence of information and authority.

The correct order of analysis is:

1. identify the regulatory problem;
2. determine whether its load is material at the declared boundary;
3. if material, identify where the corresponding function is carried;
4. determine who owns the necessary information and decision rights;
5. only then evaluate local autonomy.

---

# 11. Assisted Viability

A newly synthesized recursive system rarely begins fully autonomous. Regulatory responsibilities may initially be supplied by its parent organization.

Assistance can include:

- coordination between child operations;
- current resource regulation;
- independent verification;
- environmental intelligence and adaptation;
- policy, identity, and escalation closure.

As the child acquires decision rights, information channels, and regulatory capacity, selected responsibilities may move from the parent into the child.

Let `A(t)` represent local organizational autonomy only as an informal abstraction:

```text
A = 0          Parent-controlled
0 < A < 1      Shared / assisted viability
A = 1          Locally closed for the relevant delegated variety
```

`A = 1` does **not** require six separate agents or six separately deployed components.

It means that the child can locally absorb the regulatory variety delegated to it. A child whose policy or adaptation is intentionally parent-owned can still be highly operationally autonomous while remaining parent-governed at those higher-order decisions.

---

# 12. Examples

These examples illustrate regulatory load and transformation. They are not canonical architectures.

## Example A — Idealized perfect world

Assume one operational unit in a static environment, perfect information, no resource contention, no conflicting goals, and immutable identity.

```text
Environment ⇄ S1
```

Interpretation:

- **S2 load:** approximately zero because there is no operational interference.
- **S3 load:** approximately zero because local action is assumed globally correct and no shared current trade-off exists.
- **S3* load:** approximately zero because information is assumed perfect.
- **S4 load:** approximately zero because the relevant environment does not change.
- **S5 active decision load:** approximately zero because identity and policy never become ambiguous.

This is a theoretical limit used to expose what each metasystemic function compensates for. It is not an empirical description of realistic organizations.

## Example B — Single coding agent under a fixed task

```text
Parent / human
  ├─ policy, budget, escalation
  └─ Coding agent
       └─ tools + repository
```

Possible interpretation:

- **S1:** present — the coding agent performs the primary work.
- **S2:** no current local load if there is no peer S1 to coordinate with.
- **S3:** some current-control responsibility may be collapsed into the agent, while budget authority remains parent-owned.
- **S3*:** becomes relevant only if ordinary execution reports are insufficiently trustworthy for the risk.
- **S4:** can remain parent-owned if the task and environment are intentionally fixed for the child.
- **S5:** parent-owned if the child cannot redefine mission or policy.

The absence of several dedicated VSM-named components is not itself a defect.

## Example C — Parallel coding swarm

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

New regulatory loads appear:

- shared files, branches, locks, tests, or plans can conflict → **S2 load**;
- budgets, WIP, priorities, and shared resources create whole-system trade-offs → **S3 load**;
- workers may overstate completion or miss failures → potentially **S3* load**;
- changing dependencies, tools, or requirements can require future-oriented adaptation → potentially **S4 load**;
- the mandate can still remain fixed by the parent → **S5 parent-owned**.

The metasystem grows because the organization acquired new regulatory problems, not because it advanced to a predetermined maturity stage.

## Example D — Parent-governed domain harness

Consider a scientific or government-domain harness whose operational agents act autonomously inside a tightly defined mandate while legal boundaries, mission, and ultimate policy remain external.

Possible interpretation:

- operational S1 units may be highly autonomous;
- S2 and S3 may be local because units share data, resources, schedules, or commitments;
- S3* may be material because independent evidence is required for safety, compliance, or accountability;
- S4 may be local if the harness must track changing regulation, literature, threats, or capabilities;
- S5 may remain parent-owned because the harness is not authorized to redefine its mandate.

The absence of local S5 authority is therefore a statement about recursion and delegated decision rights, not automatically a missing implementation feature.

## Example E — S2 disappears after reconfiguration

Suppose a harness initially contains three concurrent workers plus a coordination mechanism. Later the workers are merged into one durable operational agent with one work state and no concurrent peer operations.

```text
Before:  S1-A + S1-B + S1-C + coordination
After:   one S1
```

Cross-unit interference disappears, so the dedicated S2 mechanism can become redundant and be removed.

If parallel operations are introduced again, the S2 regulatory load can reappear.

## Example F — S4 appears without adding more S1 units

A single long-running operational agent initially works against a stable API and fixed requirements. Later the API, model capabilities, regulation, and user needs begin changing quickly.

The number of S1 units has not changed, but environmental and future uncertainty has increased. S4 load therefore appears even though no split or additional worker was introduced.

This demonstrates why OSM synthesis cannot be reduced to a fixed sequence tied to organization size.

---

# 13. Relationship with Classical VSM

Classical Stafford Beer VSM defines the functional organization of viable systems. OSM describes a local hypothesis about why the active regulatory burden associated with those functions changes and how organizational configurations transform in response.

Therefore:

- Classical VSM asks: *What organizational functions make a system viable?*
- OSM asks: *What regulatory problem makes a function actively necessary here, and how does responsibility for that function move as the organization changes?*

OSM does not claim that Beer defined:

- the regulatory-load table;
- the limiting-case thought experiment;
- the transformation primitives;
- the autonomy notation;
- the trigger-based synthesis model.

Those are explicit local extensions.

The VSM Harness Profile remains authoritative for this repository's engineering interpretation of S1–S5.

---

# 14. Design Principles

1. Organizational synthesis starts from existing regulatory capacity rather than an empty organizational state.
2. Every organizational state can be represented as a discrete snapshot for analysis.
3. Organizational evolution is a sequence of transformations between snapshots.
4. Recursive viability is organizational, not merely technical nesting.
5. Metasystemic regulatory load is driven by the disturbances and ambiguities present at the declared boundary.
6. OSM does not prescribe an `S1 → S2 → S3 → S3* → S4 → S5` maturity sequence.
7. A VSM function is not equivalent to a dedicated agent, service, or permanently active component.
8. As the regulatory problem associated with a function approaches zero, the need for a distinct active implementation can also approach zero.
9. If material regulatory variety exists, it must be absorbed somewhere: locally, in a collapsed role, by a parent, or externally.
10. Parent-supplied functions indicate assisted or parent-governed viability rather than local closure for those decision rights.
11. Removing a mechanism is valid only when its regulatory load disappeared or sufficient capacity exists elsewhere.
12. Uncovered regulatory variety is a viability problem, not acceptable absence.

---

# Future Work

This document intentionally leaves undefined:

- a formal algebra of organizational transformations;
- measurable definitions of regulatory load for S2–S5;
- thresholds for when responsibilities should separate or collapse;
- invariants preserved during Split, Merge, Collapse, and Externalize;
- formal criteria for assisted versus locally closed viability;
- complexity and autonomy metrics;
- machine-readable transformation semantics;
- empirical tests of whether a regulatory load is actually near zero.

These constitute the next layer of formalization.
