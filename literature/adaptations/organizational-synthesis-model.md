# RFC: Organizational Synthesis Model (OSM)

> **Status: non-canonical development methodology.** OSM is a local working method built on the VSM Harness Profile. Its phases, gates, transformations, and autonomy language are not Stafford Beer concepts and are not conformance requirements.

Status: Draft

Depends on:
- [VSM Harness Profile](../../PROFILE.md) — organizational semantics;
- [Agent VSM Extension](agent-vsm-extension.md) — conditional regulatory load and redundancy.

---

# Abstract

The profile defines **what** S1, S2, S3, S3*, S4, and S5 mean. The Agent VSM Extension asks **when** they carry active regulatory load. OSM asks:

> How should an agent organization be progressively built as new regulatory demands appear?

Default construction order:

```text
Intent
  ↓
S1 — useful operations
  ↓
S2 — coordination, if demanded
  ↓
S3 — present-time whole-system control, if demanded
  ↓
S3* — complementary verification, if demanded
  ↓
S4 — environmental / future adaptation, if demanded
  ↓
S5 — local policy / identity closure, if delegated
```

This is a **development heuristic**, not a mandatory final topology. Every step after S1 has a gate.

---

# 1. Separation of concerns

```text
PROFILE.md
    What does each VSM function mean?

Agent VSM Extension
    Why and when is each function demanded?

OSM
    In what order should we build or transform it?
```

An organizational snapshot and a development path are different things. A function may be unnecessary or parent-supplied in the final snapshot even though OSM still checks its gate during development.

---

# 2. Snapshots and transformations

OSM represents development as explicit transitions:

```text
VSM(t1) ──Transformation──► VSM(t2)
```

A transformation may add an operational unit, expose a regulatory problem, move authority from parent to child, collapse a responsibility into another actor, or change the recursion boundary.

The basic loop is:

```text
observe current organization
        ↓
identify new / uncovered variety
        ↓
identify the responsible VSM function
        ↓
apply the minimum transformation
        ↓
validate regulation
        ↓
record the next snapshot
        ↺
```

---

# 3. Existing and assisted viability

A new child starts inside an already functioning context: a human, parent harness, organization, or other recursive VSM. The parent can initially supply coordination, budgets, verification, adaptation, policy, and escalation.

Therefore OSM starts with the minimum useful S1 and internalizes additional functions only when the child needs and is authorized to own them.

---

# 4. Default maturity path

## Phase 0 — Intent

Declare purpose, boundary, environment, expected operational outcome, and authority retained by the parent.

## Phase 1 — Operational formation (S1)

Build the minimum operational capability that can produce useful work.

**Exit:** useful outcomes exist and failures can be observed.

## Phase 2 — Coordination gate (S2)

Ask:

> Do multiple operations create interference, oscillation, contention, duplication, or instability they cannot absorb locally?

If yes, introduce the minimum coordination mechanism. If no, keep S2 collapsed or not locally demanded.

## Phase 3 — Present-time control gate (S3)

Ask:

> Are locally reasonable decisions diverging from whole-system interests, shared constraints, or resource priorities?

If yes, add whole-system current regulation: budgets, WIP limits, priority negotiation, resource bargaining, or intervention. If no, keep S3 collapsed or parent-supplied.

## Phase 4 — Verification gate (S3*)

Ask:

> Is routine operational reporting trustworthy enough for the relevant risk?

If no, add complementary access to operational reality such as replay, raw-artifact inspection, independent evaluation, adversarial probes, or external ground truth. If yes, a distinct S3* path is unnecessary.

## Phase 5 — Adaptation gate (S4)

Ask:

> Must the child itself model environmental or future change and alter present capability in response?

If yes, add local environmental intelligence and a path back into present organization. If no, S4 may remain parent-supplied.

## Phase 6 — Policy and identity gate (S5)

Ask:

> Is the child authorized and required to resolve policy, identity, ultimate constraints, or unresolved S3–S4 tension locally?

If yes, delegate legitimate local closure. If no, S5 remains parent-owned.

---

# 5. Gate outcomes

Each phase after S1 records one outcome:

| Outcome | Meaning |
| --- | --- |
| `local-distinct` | demanded and implemented distinctly in the child |
| `local-collapsed` | demanded but absorbed by another local actor |
| `parent-supplied` | demanded but retained by the parent |
| `externalized` | demanded but supplied outside the child |
| `not-demanded` | triggering variety is absent |
| `missing` | triggering variety exists and remains uncovered |

Only `missing` is an unresolved organizational defect by definition.

---

# 6. Why the order matters

The sequence remains useful even with conditional gates:

```text
S1 gives us operations to observe.
S2 appears when operations interact.
S3 appears when local and whole-system interests diverge.
S3* appears when routine reports are insufficient.
S4 appears when the organization must adapt to external/future change.
S5 appears when identity or policy closure is delegated locally.
```

Building later functions before their regulatory problem exists tends to create cargo-cult structure rather than requisite regulation.

---

# 7. Assisted autonomy

A child rarely begins fully locally closed. OSM models progressive transfer of selected responsibilities from parent to child.

```text
A = 0          parent-controlled
0 < A < 1      shared / assisted viability
A = 1          locally closed for delegated variety
```

This is an informal abstraction, not a score. `A = 1` does not require six dedicated components.

---

# 8. Transformation vocabulary

- **Split** — one unit becomes several organizational units.
- **Merge** — several units become one organizational system.
- **Intersection** — a new unit forms around shared mission or capability while parents remain.
- **Reconfigure** — responsibilities, channels, decision rights, or boundaries change.
- **Collapse** — a distinct responsibility is absorbed into another actor.
- **Externalize** — responsibility moves out of the child.
- **Internalize** — externally supplied responsibility moves into the child.
- **Remove** — a unit or mechanism is detached after its variety disappears or remains regulated elsewhere.

---

# 9. Worked example: Terminal-Bench VSM

[`terminal-bench-vsm`](https://github.com/opensiro/terminal-bench-vsm) contains an earlier concrete version of this evolutionary construction method in [`vsmlite-tb/osm.md`](https://github.com/opensiro/terminal-bench-vsm/blob/main/vsmlite-tb/osm.md).

It describes organizational synthesis as **progressive acquisition of viability** through:

```text
Intent
→ Operational Formation
→ Coordination
→ Executive Regulation
→ Verification
→ Adaptation
→ Identity
```

It is referenced as a **worked historical example of the method**, not as theoretical authority or the canonical OSM definition.

The current OSM refines that experiment by adding explicit gates and allowing later functions to remain collapsed, parent-supplied, externalized, or not demanded.

---

# 10. Relationship to Agent VSM Extension

The extension describes regulatory demand:

```text
interference                → S2 demand
local/global divergence     → S3 demand
information uncertainty     → S3* demand
environmental change        → S4 demand
identity/policy ambiguity   → S5 demand
```

OSM turns that into a development rule:

```text
observe demand
→ add minimum regulatory capacity
→ validate
→ continue when new variety justifies another transformation
```

The extension explains **why** regulation is needed. OSM explains **when and how to add it**.

---

# 11. Design principles

1. Start from useful operations, not from a complete diagram.
2. Keep S1 → S5 as a development heuristic, not a mandatory final topology.
3. Gate every new regulatory function by the variety that makes it necessary.
4. Prefer the minimum transformation that restores requisite regulation.
5. Keep functions parent-supplied until there is reason and authority to internalize them.
6. Validate after every material transformation.
7. Distinguish a missing function from a legitimately skipped or collapsed phase.
8. Allow reverse evolution when regulatory load falls.

---

# Future Work

Formal gate thresholds, automated demand detection, transformation invariants, cost models, rollback semantics, empirical maturity benchmarks, and machine-readable snapshot formats remain open.
