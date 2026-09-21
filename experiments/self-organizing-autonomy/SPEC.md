# Experimental specification: self-organizing autonomy (`S`)

**Status:** experimental draft  
**Source issue:** [#13 — Recursive self-organizing autonomy as a state beyond A/C](https://github.com/opensiro/vsm-harness-profile/issues/13)  
**Normative effect:** none

## 1. Purpose

This experiment tests whether the ecosystem needs a capability distinction beyond ordinary autonomous closure.

The candidate distinction is:

```text
C — material new in-domain organizational variety still requires an external
    constructor/composer to supply missing organizational logic.

A — the system can autonomously absorb novel in-domain variety using its
    existing organizational/regulatory repertoire and close the function.

S — the system includes A-level closure and can additionally reconstruct or
    extend that repertoire when it becomes insufficient, within the substrate,
    resources, channels, and legitimate authority actually available to it.
```

`S` is provisional. This document does not add `S` to the active publication state set.

## 2. Function-first rule remains mandatory

The experiment does not weaken the current Profile discipline.

For every candidate witness:

1. establish the VSM function at the declared system boundary;
2. identify the disturbance / variety being regulated;
3. identify the decisive decision or feedback right and its owner;
4. separate supporting/enforcement machinery from ownership;
5. establish closure into subsequent operation;
6. establish ordinary `A` before considering an experimental `S` witness.

A component name, self-modification feature, agent count, workflow generator, or recursive-looking topology is not evidence by itself.

## 3. Candidate `S` test

A per-function candidate supports the `S` hypothesis only if all of the following can be reconstructed from primary evidence at one declared boundary and operating mode.

### 3.1 A-level prerequisite

The function already satisfies ordinary autonomous closure: an autonomous agent owns the relevant discretionary organizational decision/feedback right and the loop closes through the first-party operating boundary.

### 3.2 Repertoire insufficiency

There is a material disturbance that remains inside the declared operating domain but cannot be adequately absorbed by the currently available organizational/regulatory repertoire.

The evidence must distinguish **repertoire insufficiency** from an ordinary hard task, transient failure, missing data, lack of compute, or a case already supported by an existing mechanism.

### 3.3 Endogenous reconstruction

The system itself identifies the insufficiency and forms a materially new or altered organizational/regulatory response without an external constructor supplying the missing organizational logic.

The reconstructed element must change the repertoire used to regulate the function, not merely select another pre-authored branch of ordinary operation.

### 3.4 Legitimate authorization

The reconstruction stays within the authority available at the declared recursion. If parent or higher-recursion authority is required, the experiment must identify that boundary explicitly rather than treating permission as autonomous ownership.

### 3.5 Integration and closure

The reconstructed repertoire is integrated into the operating organization and changes subsequent regulation or operation. A generated proposal, patch, prompt, workflow, agent, or configuration that is never integrated does not close the witness.

### 3.6 Continued operation

After integration, the function can actually absorb the target variety through the reconstructed repertoire. The witness must therefore include evidence of post-change operation, not only evidence that the organization can modify itself.

## 4. Strong recursive witness

The strongest system-level witness is recursive self-organization. It shows that the organization can:

1. recognize that its current organizational variety is insufficient;
2. define a new bounded operational purpose/domain for the unresolved variety;
3. create or reorganize an operational unit for that domain;
4. establish enough local coordination, control, audit, adaptation, and policy relations for that unit to remain viable for the delegated purpose;
5. grant the unit bounded autonomy;
6. connect the new recursion to the parent without duplicate authority;
7. demonstrate that the new recursion actually absorbs the variety that the prior organization could not.

The generated subsystem need not contain literal components named S1-S5. The requirement is functional viability at the new recursion.

## 5. Per-function interpretation

The experiment may be evaluated per function, but each function needs its own reconstruction witness.

- **S1:** reconstruct the operational process, tooling, or local organization when the existing operational repertoire cannot absorb in-domain variety.
- **S2:** reconstruct the coordination regime when the existing anti-interference/anti-oscillation repertoire is inadequate.
- **S3:** reconstruct current-control, resource-allocation, accountability, or escalation organization when its existing repertoire lacks requisite variety.
- **S3\*:** reconstruct audit strategy, probes, sampling, evidence access, or auditor composition while preserving complementary independence.
- **S4:** reconstruct how the organization senses/model external or future distinctions, develops adaptation options, or experiments when the existing adaptation repertoire is inadequate.
- **S5:** reconstruct identity / ultimate-policy machinery or legitimate rules for self-revision. This is the hardest case because unconstrained self-change may instead reveal that ultimate authority resides at a higher recursion.

A positive witness for one function does not transitively establish `S` for another function.

## 6. Parent governance

`P` answers a different question: where legitimate decisive authority resides.

The experiment therefore does not assume `S(P)` as publication notation. A lower-level function may potentially satisfy the `S` hypothesis while S5 remains fixed or parent-governed, provided the constitutional envelope already authorizes the reconstruction.

Likewise, a future `S5=S` would be a constitutional capability, not proof that S1-S4 or S3* can reconstruct themselves.

Any eventual composition rule between `S` and parent-governed modes must be specified before normative adoption.

## 7. Non-evidence

None of the following establishes `S` by itself:

- self-editing code;
- modifying prompts or configuration;
- adding or selecting tools;
- generating a workflow;
- spawning or nesting agents/subagents;
- choosing among pre-authored organizational templates;
- ordinary retry/recovery;
- ordinary S4 learning/adaptation;
- ordinary `A` discretion over a case already supported by the existing repertoire;
- human approval of a generated organizational change;
- repository-development/dogfood behavior outside the assessed operating boundary.

The experiment specifically tests **endogenous increase or reconstruction of regulatory variety with organizational closure**.

## 8. Experimental findings notation

While this specification is non-normative, fixture reviews MUST NOT write `S` into canonical Index assessment vectors.

Experimental reports should use one of these findings instead:

- `supports-S-hypothesis` — the candidate test is positively reconstructed;
- `does-not-support-S` — evidence shows the candidate remains within ordinary `A`, `C`, or another existing distinction;
- `inconclusive` — the evidence boundary is insufficient to decide.

A report may separately note whether the witness is a **strong recursive witness**.

These findings are experimental evidence, not autonomy states.

## 9. Evidence contract

A positive experimental report should record at least:

- repository and pinned revision;
- system-in-focus, recursion, purpose, environment, and operating/deployment mode;
- baseline VSM function and current canonical state;
- the material in-domain disturbance;
- evidence that the prior repertoire was insufficient;
- who recognized the insufficiency;
- what organizational/regulatory repertoire was reconstructed;
- who authorized the change and under what authority;
- supporting/enforcement mechanisms separately;
- integration path;
- post-change closure evidence;
- whether an external constructor supplied any material missing organizational logic;
- caveats and alternative interpretation under existing Profile concepts.

The report must make it possible for an independent reviewer to distinguish endogenous reconstruction from ordinary autonomy, S4 adaptation, recursion, and software self-modification.

## 10. Stability gates

This experimental specification may be marked `stable` only when all of the following are complete:

1. the fixture corpus contains the required positive and negative cases described in [`FIXTURES.md`](FIXTURES.md);
2. at least one candidate supplies a strong positive witness or the experiment explicitly concludes that the strong form is not empirically supported;
3. self-modification-without-self-organization and generated-structure-without-viable-recursion counterexamples are demonstrated;
4. S3* independence and S5 legitimate-authority counterexamples are demonstrated;
5. two independent reviewers can apply the candidate test to the fixture corpus with materially reproducible results;
6. the experiment demonstrates information not already captured by existing Profile concepts of autonomy, recursion, S4, ownership, and closure;
7. per-function versus system-level semantics are resolved;
8. composition with parent-governed modes is resolved or normatively restricted;
9. a normative adoption and downstream migration plan is ready.

Reaching `stable` freezes the experimental contract for adoption work. It does not itself alter the normative Profile.

## 11. Promotion boundary

Promotion follows [`PROMOTION.md`](PROMOTION.md).

In particular, canonical assessments remain on the released Profile/Methodology state set until an explicit normative release adopts the new distinction. Historical provenance remains unchanged. Any downstream reindex/reassessment round must run against the released adopting contract rather than this experiment directory.
