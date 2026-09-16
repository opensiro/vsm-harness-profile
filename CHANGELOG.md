# Changelog

All material changes to the normative VSM Harness Profile are recorded here.

## 0.2.1 — 2026-09-16

### Changed

- make the existing S2 evidence threshold mechanically explicit at the declared recursion level;
- require a positive S2 mapping to identify distinct S1 units, a specific actual or structurally evidenced inter-S1 interference/conflict/oscillation, a coordination relation that attenuates it, and a feedback/closure path into subsequent S1 behaviour;
- clarify that generic mailboxes, routing, shared state, task sequencing, speaker selection, or delegation do not establish S2 unless evidence ties them to regulation of a specific inter-S1 disturbance;
- separate S2 function evidence from ownership: deterministic locks, queues, reservations, schedules, turn-taking rules, or similar mechanisms may support/close coordination while agent ownership still requires the decisive coordination discretion to be agent-owned.

### Compatibility

This is a PATCH clarification of requirements already present in Profile 0.2.0 and Methodology 0.2.1: S2 regulates interference/oscillation among operational units, while delegation/routing alone is insufficient. It does not redefine S2 or introduce a new VSM function.

A conforming 0.2.0 mapping should remain conforming under 0.2.1. Existing assessments whose positive S2 state was based only on generic coordination primitives or mediation should be treated as same-ref corrections under their frozen assessment contract rather than as semantic migrations caused by this patch.

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

This revision is intended to reduce false-positive autonomy classifications without redefining Stafford Beer's functions. Existing assessments whose positive state depends mainly on deterministic enforcement, approval gates, or an unspecified responsible actor should receive targeted reassessment under the Index workflow.

## Pre-versioned baseline

The repository did not previously publish a formal version or release. For migration discussion only, the immediately preceding normative line may be called the **v0.1.0 baseline**. It is not a retroactively asserted Git tag or historical release.
