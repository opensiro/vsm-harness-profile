# Downstream consumer contract

This document defines the stable interface between the VSM Harness Profile and downstream consumers. It does **not** define VSM functions; [`PROFILE.md`](PROFILE.md) remains the sole normative source for S1, S2, S3, S3*, S4, S5, recursion, variety, escalation, ownership, closure, and evidence boundaries.

The purpose of this contract is to separate two questions that downstream systems must not collapse:

```text
Which exact Profile produced this artifact?
        ↓ provenance

Can this artifact still be used under a later Profile release?
        ↓ compatibility / reassessment impact
```

A Profile version is immutable provenance. Compatibility with a later release is a derived property and MUST NOT be represented by rewriting the historical Profile version that produced an assessment or other artifact.

## Core invariant

```text
new Profile version
    != automatic reassessment trigger

release-impact path
    -> determines whether review is required
```

A downstream artifact produced under an older Profile may remain valid under a newer compatible Profile without being regenerated, reassessed, or relabelled as though it had originally been produced under the newer version.

## Machine-readable facade

[`RELEASE_IMPACT.json`](RELEASE_IMPACT.json) is the machine-readable release-impact history. It records one linear transition for each explicitly versioned Profile release known to the current repository state.

Each release entry contains:

- `version` — the Profile version introduced by the transition;
- `previous` — the immediately preceding Profile release, or `baseline` for the first explicitly versioned release;
- `compatibility` — whether the transition preserves the previous conformance contract;
- `assessment_impact` — the maximum reassessment scope caused by the Profile change itself;
- `selectors` — a bounded description of the assessments potentially affected when impact is targeted.

The facade has no independent semantic-version axis. `VERSION` remains the Profile version. Additive machine-readable fields may be introduced compatibly; an incompatible change to required field meaning or consumer interpretation must not be silently introduced inside the same Profile major line.

## Compatibility

`compatibility` has two values:

- `compatible` — the transition preserves the previous conformance contract;
- `breaking` — at least part of the previous conformance contract is no longer sufficient under the new Profile and an explicit migration decision is required.

Compatibility is deliberately separate from reassessment scope. A breaking change may affect only one bounded function or concept; conversely, a compatible conceptual refinement may still justify targeted review of artifacts that depend on a specific affected distinction.

## Assessment impact

`assessment_impact` has three values:

- `none` — no existing conforming assessment requires reassessment because of this Profile transition;
- `targeted` — only assessments matching one or more declared selectors may require review;
- `all` — every current assessment must be considered for review.

`all` is an explicit exceptional state. Consumers MUST NOT infer corpus-wide reassessment merely from a version number changing.

### Selector syntax

For `targeted` impact, `selectors` contains one or more stable selector tokens:

- `function:S1`, `function:S2`, `function:S3`, `function:S3*`, `function:S4`, `function:S5` — a specific VSM-function mapping may be affected;
- `concept:<kebab-case-id>` — a cross-function Profile concept may be affected;
- `evidence:<kebab-case-id>` — a particular evidence dependency or evidence pattern may be affected.

For `none`, `selectors` MUST be empty. For `all`, `selectors` MUST be exactly `["*"]`.

Selectors bound review scope; they are not additional VSM semantics. Their meaning must be explained by the corresponding changelog entry. A downstream system may use structured selector metadata when available or route only the targeted subset for human/evidence review when it cannot mechanically resolve a selector.

## SemVer relationship

The release-impact contract makes the repository's SemVer policy operational:

- **PATCH** transitions MUST be `compatible` with `assessment_impact: none`;
- **MINOR** transitions MUST be `compatible` and may declare `none` or `targeted`, but never `all` merely because the minor version changed;
- **MAJOR** transitions MUST be `breaking` and must declare `targeted` or `all` impact.

A same-ref correction discovered while reviewing historical evidence is not automatically release impact. For example, Profile `0.2.1` made the existing S2 evidence witness more explicit; weak historical positives can still be corrected under their frozen contract without treating the PATCH release as a semantic migration.

## Compatibility composition

To determine whether an artifact produced under Profile `P` needs review before use under later Profile `T`:

1. preserve `P` as the artifact's provenance;
2. follow the ordered release transitions after `P` through `T` in `RELEASE_IMPACT.json`;
3. if every transition has `assessment_impact: none`, no reassessment is required because of the Profile version change;
4. if one or more transitions are `targeted`, review only artifacts that may match the union of those selectors;
5. if any transition is `all`, review the corpus;
6. if any transition is `breaking`, require an explicit migration decision for the affected scope even when that scope is targeted rather than global;
7. if the transition path cannot be established from the declared facade, report insufficient compatibility evidence rather than assuming either compatibility or incompatibility.

This composition rule lets consumers advance their active Profile without mutating historical assessment provenance.

## Consumer obligations

Downstream consumers SHOULD:

- record the exact Profile version and, where appropriate, immutable source revision used to produce an artifact;
- keep assessment-procedure provenance separate from Profile provenance;
- evaluate later Profile compatibility from the release-impact chain instead of comparing version strings alone;
- preserve frozen reassessment-round contracts unless the round explicitly adopts a newer contract;
- avoid copying VSM definitions into local compatibility logic.

A consumer may additionally record a derived statement such as “compatible through Profile X”, but that statement is not a replacement for the original Profile version and should be reproducible from the release-impact chain.

## `vsm-oss-organization`

`opensiro/vsm-oss-organization` may consume this facade as part of its released semantic boundary and may later produce Profile changes through ordinary bounded OSS work. That does not transfer semantic authority: a proposed change becomes Profile semantics only after it is accepted in this repository and represented by the Profile's release process.

The organization should therefore be able to distinguish an upstream Profile release that requires no local semantic migration from one that requires targeted or breaking work, without hard-coding “every newer Profile version means update everything.”

## Release identity

Git tags/releases remain the immutable identity of accepted Profile releases. `RELEASE_IMPACT.json` on `main` may describe the current not-yet-tagged version while it is being prepared; consumers that require released semantics should resolve the facade from an accepted release or otherwise verify the release state.

Historical tags are not rewritten when this facade gains information about earlier transitions. The current release-impact history is the forward consumer interface; tagged historical artifacts remain immutable provenance.

## Non-goals

This contract does not:

- define or reinterpret S1-S5;
- define autonomy-state notation owned by downstream Methodology;
- decide whether a maintainer's semantic impact judgment is correct;
- create a second assessment database;
- create a second compatibility-version hierarchy;
- require a frozen Index round to upgrade in place;
- make `vsm-oss-organization` or any other consumer a normative Profile authority.
