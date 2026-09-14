# RFC: Organizational Synthesis Model (OSM)

> **Status: non-canonical working extension.** OSM synthesis phases, transformation primitives, and assisted-viability measures are local hypotheses built on VSM. They are not attributable to Stafford Beer and are not requirements of the VSM Harness Profile.

Status: Draft

Extends: Stafford Beer — Viable System Model (VSM)

> In its original repository this document governed local `primitives.yaml` and `phases.yaml` files. Those implementation files are not part of the current profile; the RFC is retained for research provenance.

---

# Abstract

Classical Viable System Model (VSM) describes the structural properties required
for an organization to remain viable.

This document does not modify the VSM itself.

Instead, it introduces a complementary model describing how viable systems
transform into other viable systems.

The model is intended as a formal foundation for organizational synthesis within
vsmforge.

---

# 1. Scope

Classical VSM answers:

> What structure must a viable organization contain?

This document answers:

> How do viable organizations create, transform, divide, merge and evolve other
> viable organizations?

---

# 2. Axiom of Snapshot

A VSM is defined only at a discrete moment in time.

A system is therefore represented as a complete organizational snapshot: `VSM(t)`.

The model intentionally ignores continuous evolution. Organizational change is
represented only as a transition between snapshots:

```
VSM(t1) ──Transformation──► VSM(t2)
```

Consequently, questions such as

- Which System appeared first?
- Does S5 create S3?
- When does recursion emerge?

are outside the scope of the model.

Instead, the model studies transformations between complete organizational
configurations.

---

# 3. Axiom of Recursion

Every viable system consists of operational units. Whenever an operational unit
itself requires independent viability, it may be represented recursively as its
own VSM.

```
VSM
 ├── S1 (VSM) ──┬── S1 (VSM)
 │              ├── ...
 │              └── S5
 ├── S1 (VSM)
 └── S1 (VSM)
```

Recursion therefore represents organizational decomposition rather than
inheritance. The complete organization forms a recursive tree of viable systems.

---

# 4. Axiom of Existing Viability

Organizational synthesis never begins from an empty state. Every transformation
starts from at least one already viable system.

The minimal practical example of such a system is a human. A human already
possesses the essential functions required for viability:

- operations;
- coordination;
- executive regulation;
- self-observation;
- adaptation;
- identity.

Therefore, organizational synthesis always operates on existing viable systems
rather than creating viability from nothing.

> **vsmlite extension (pragmatic):** in the applied setting, vsmlite permits a
> `Create` primitive — but **only in Initial State**, to bootstrap the child
> `../vsm/`. This avoids forcing vsmlite itself to become a factory (recursive
> factory of organizations), which is out of scope. The original implementation referred to a local `primitives.yaml` file that is not retained here.

---

# 5. Organizational Transformations

Let `V` represent the set of all viable systems. Organizational evolution
consists only of transformations over elements of `V`.

Primitive transformations are:

## Split

One viable system becomes multiple recursive viable systems.

```
   VSM_a            VSM_a
     │       ──►     ├─ VSM_a1
    ...              └─ VSM_a2
```

## Merge

Multiple viable systems become one shared viable system.

## Intersection

A new viable system is formed from the shared mission, capabilities or
operational domain of multiple existing systems. Parent systems continue to
exist.

## Remove

A viable system is detached from a recursive structure. The remaining
organization must still satisfy viability.

## Reconfigure

Internal relationships are modified without changing organizational identity.

---

No primitive `Create` operation exists in the canonical model: every viable
system originates from one or more existing viable systems.

> **vsmlite extension:** `Create` is admitted, restricted to Initial State (see §4).

---

# 6. Organizational Synthesis

Creation of a new organizational unit is represented as progressive acquisition
of viability.

## Phase 0 — Intent

A parent VSM determines that an additional viable system is required.

## Phase 1 — Operational Formation

Operational units are established. From the parent's perspective these become
candidate S1 units. Whenever necessary, each operational unit may recursively
become a VSM.

## Phase 2 — Coordination

Interactions between operational units require coordination. S2 functions emerge.

## Phase 3 — Executive Regulation

Resource allocation and organizational optimization emerge. S3 functions emerge.

## Phase 4 — Verification

When information asymmetry becomes significant, independent observation
mechanisms emerge. S3* functions emerge.

## Phase 5 — Adaptation

Interaction with a changing environment requires strategic adaptation. S4
functions emerge.

## Phase 6 — Identity

When conflicts cannot be resolved by S3 and S4 alone, organizational policy,
identity and autonomy boundaries become necessary. S5 functions emerge.

At this point the organization is considered a fully viable VSM.

---

# 7. Assisted Viability

A newly synthesized VSM rarely begins fully autonomous. Missing functions are
temporarily compensated by its parent organization.

Support is performed by dedicated operational units (S1) of the parent VSM whose
mission is organizational synthesis and maturation.

> **This is precisely the role of vsmlite.** vsmlite is that dedicated S1: it
> applies OSM primitives and walks the phases to mature the child `../vsm/`.

As autonomy increases, these functions are progressively transferred to the child
system.

Let `A(t)` represent organizational autonomy:

```
A = 0          Parent-controlled
0 < A < 1      Shared viability
A = 1          Fully autonomous VSM
```

> **vsmlite operationalization of A(t):** four behavioral signs, forward-
> compatible with the (unbuilt) vsmforge autonomy engine — see the original, non-retained `vsmlite.yaml` and `scripts/autonomy.py` implementation files.

---

# 8. Relationship with Classical VSM

Classical Stafford Beer VSM defines the invariant structure of a viable
organization. This document defines transformations over viable organizations.

Therefore:

- Classical VSM answers: *What makes an organization viable?*
- Organizational Synthesis Model answers: *How do viable organizations synthesize
  other viable organizations?*

The two models are complementary rather than competing.

---

# 9. Design Principles

1. Viability cannot emerge from an empty state.
2. Every organizational state is represented as a discrete snapshot.
3. Organizational evolution is a sequence of transformations between snapshots.
4. Every sufficiently complex operational unit may recursively become a VSM.
5. Organizational synthesis is the progressive acquisition of viability rather
   than instantaneous creation.

---

# Future Work

This document intentionally leaves undefined:

- algebra of organizational transformations;
- formal invariants preserved during transformations;
- complexity metrics;
- autonomy metrics;
- compiler semantics for vsmforge.

These constitute the next layer of formalization.
