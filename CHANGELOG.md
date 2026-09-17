# Changelog

All material changes to the normative VSM Harness Profile are recorded here. Downstream release impact is also represented mechanically in [`RELEASE_IMPACT.json`](RELEASE_IMPACT.json).

## 0.2.2 — 2026-09-17

### Changed

- clarify the terminology boundary between an **agent actor** and an **agent harness**;
- define an agent actor as an autonomous or semi-autonomous decision-making participant that performs work within an agentic process;
- define an agent harness as the system that structures, enables, and governs an agentic work process for one or more agent actors;
- make explicit that harness control may be deterministic, agentic, or hybrid, so an agent actor may also participate in the harness control structure;
- clarify that a wider assembled product may colloquially be called an “agent”, while Profile analysis distinguishes actor and organizing system through the declared system-in-focus.

### Repository contract

- introduce the downstream consumer contract separating exact Profile provenance from later-release compatibility;
- add machine-readable release-impact history so compatible Profile updates do not imply automatic reassessment or provenance rewrites.

### Compatibility

This is a PATCH terminology clarification. It does not change any S1–S5 function, ownership rule, autonomy state, evidence threshold, or existing conforming mapping. It makes the harness interpretation explicit for supervisor/subagent and other agentic-control architectures without prescribing a required topology.

### Assessment impact

`none` — existing conforming assessments do not require reassessment because of this Profile transition. Their original Profile provenance remains unchanged.

## 0.2.1 — 2026-09-16

### Changed

- make the existing S2 evidence threshold mechanically explicit at the declared recursion level;
- require a positive S2 mapping to identify distinct S1 units, a specific actual or structurally evidenced inter-S1 interference/conflict/oscillation, a coordination relation that attenuates it, and a feedback/closure path into subsequent S1 behaviour;
- clarify that generic mailboxes, routing, shared state, task sequencing, speaker selection, or delegation do not establish S2 unless evidence ties them to regulation of a specific inter-S1 disturbance;
- separate S2 function evidence from ownership: deterministic locks, queues, reservations, schedules, turn-taking rules, or similar mechanisms may support/close coordination while agent ownership still requires the decisive coordination discretion to be agent-owned.

### Compatibility

This is a PATCH clarification of requirements already present in Profile 0.2.0 and Methodology 0.2.1: S2 regulates interference/oscillation among operational units, while delegation/routing alone is insufficient. It does not redefine S2 or introduce a new VSM function.

A conforming 0.2.0 mapping should remain conforming under 0.2.1. Existing assessments whose positive S2 state was based only on generic coordination primitives or mediation should be treated as same-ref corrections under their frozen assessment contract rather than as semantic migrations caused by this patch.

### Assessment impact

`none` — the PATCH does not itself require reassessment. Weak historical S2 positives discovered while applying the already-existing frozen evidence contract are same-ref corrections, not migration work caused by Profile 0.2.1.

## 0.2.0 — 2026-09-16

### Changed

- make the evidence pipeline explicitly separate **organizational function**, **decisive decision/feedback right**, **owner**, and **supporting enforcement**;
- state that deterministic enforcement does not transfer ownership of the underlying organizational decision right;
- add a counterfactual owner test for ambiguous hybrid agent/runtime mechanisms;
- require closure-path reasoning for positive mappings where a decision must return into subsequent operation;
- strengthen S3 wording around resource/commitment decisions versus runtime enforcement;
- strengthen S5 wording around legitimate identity/policy closure and parent-authority return paths;
- add category errors for treating enforcement as ownership and generic human approval as S5;
- introduce explicit Profile versioning and downstream provenance guidance.

### Assessment impact

`targeted` — existing assessments whose positive state depends mainly on deterministic enforcement, approval gates, or an unspecified responsible actor should receive targeted reassessment under the Index workflow. The machine-readable selectors additionally identify decision ownership and closure as affected cross-function concepts.

## Pre-versioned baseline

The repository did not previously publish a formal version or release. For migration discussion only, the immediately preceding normative line may be called the **v0.1.0 baseline**. It is not a retroactively asserted Git tag or historical release.
