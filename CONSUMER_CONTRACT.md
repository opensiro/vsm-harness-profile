# Downstream consumer contract

This document defines the compatibility interface originally introduced between the VSM Harness Profile and the released general assessment stack. It does **not** define VSM functions; [`PROFILE.md`](PROFILE.md) remains the sole normative source for S1, S2, S3, S3*, S4, S5, recursion, variety, escalation, ownership, closure, and evidence boundaries.

## Current status

Profile SemVer is now treated as **consumer-independent normative versioning**. A Profile release records a change in the organizational model; each downstream consumer decides what that change means for its own artifacts.

The machine-readable release-impact facade in this repository remains supported for the existing general Methodology / Index line because released and frozen artifacts already depend on it.

It is therefore a **legacy general-consumer compatibility surface**, not a universal reassessment policy for every assessment specification, implementation, derived profile, or future domain-specific index.

The core distinction remains:

```text
Which exact Profile produced this artifact?
        ↓ provenance

Can this consumer still use the artifact under a later Profile release?
        ↓ consumer-specific compatibility / migration
```

A Profile version is immutable provenance. Compatibility with a later release is derived by the relevant consumer and MUST NOT be represented by rewriting the historical Profile version that produced an assessment or other artifact.

## Core invariant

```text
new Profile version
    != automatic universal reassessment trigger
```

For the released general stack that adopted this facade:

```text
legacy release-impact path
    -> helps determine whether general assessment review is required
```

For another assessment specification or consumer:

```text
Profile semantic change
    -> consumer-owned compatibility / migration rule
```

A downstream artifact produced under an older Profile may remain valid under a newer Profile without being regenerated, reassessed, or relabelled as though it had originally been produced under the newer version.

## Machine-readable legacy facade

[`RELEASE_IMPACT.json`](RELEASE_IMPACT.json) is the machine-readable release-impact history for consumers that adopted the original general-assessment compatibility contract.

Each release entry contains:

- `version` — the Profile version introduced by the transition;
- `previous` — the immediately preceding Profile release, or `baseline` for the first explicitly versioned release;
- `compatibility` — whether the transition preserves the previous Profile conformance contract;
- `assessment_impact` — the maximum reassessment scope for the legacy general-assessment consumer contract;
- `selectors` — a bounded description of legacy general assessments potentially affected when impact is targeted.

The facade has no independent semantic-version axis. `VERSION` remains the Profile version.

`assessment_impact` and `selectors` MUST NOT be interpreted as a universal requirement that unrelated or future assessment systems perform the same reassessment. Such systems may track the same Profile release while defining their own compatibility rules in their owning specification.

## Compatibility

`compatibility` has two values:

- `compatible` — the transition preserves the previous Profile conformance contract;
- `breaking` — at least part of the previous Profile conformance contract is no longer sufficient.

This describes the semantic relationship between Profile versions. A consumer decides what operational migration follows from that fact.

## Legacy assessment impact

For the general assessment stack that adopted this facade, `assessment_impact` has three values:

- `none` — no existing conforming general assessment requires reassessment because of this Profile transition;
- `targeted` — only general assessments matching one or more declared selectors may require review;
- `all` — every current general assessment must be considered for review.

`all` is an explicit exceptional state. Legacy consumers MUST NOT infer corpus-wide reassessment merely from a version number changing.

### Selector syntax

For `targeted` impact, `selectors` contains one or more stable selector tokens:

- `function:S1`, `function:S2`, `function:S3`, `function:S3*`, `function:S4`, `function:S5` — a specific VSM-function mapping may be affected;
- `concept:<kebab-case-id>` — a cross-function Profile concept may be affected;
- `evidence:<kebab-case-id>` — a particular evidence dependency or evidence pattern may be affected.

For `none`, `selectors` MUST be empty. For `all`, `selectors` MUST be exactly `["*"]`.

Selectors bound review scope only for consumers that adopt this legacy facade. They are not additional VSM semantics and do not bind a domain-specific or community assessment specification unless that specification explicitly chooses to adopt them.

## SemVer relationship

Profile SemVer itself is defined in [`VERSIONING.md`](VERSIONING.md) from the normative model change.

While the legacy facade remains supported, its compatibility checks retain the historical constraints expected by existing consumers:

- **PATCH** transitions remain `compatible` with legacy `assessment_impact: none`;
- **MINOR** transitions remain `compatible` and may declare legacy `none` or `targeted`;
- **MAJOR** transitions are `breaking` and declare legacy `targeted` or `all`.

These constraints preserve existing released tooling. They do not make general-Index reassessment semantics part of the VSM model.

A same-ref correction discovered while reviewing historical evidence is not automatically release impact. For example, Profile `0.2.1` made the existing S2 evidence witness more explicit; weak historical positives can still be corrected under their frozen contract without treating the PATCH release as a semantic migration.

## Compatibility composition for legacy consumers

For a legacy consumer that explicitly adopted this facade, determining whether an artifact produced under Profile `P` needs review before use under later Profile `T` remains:

1. preserve `P` as the artifact's provenance;
2. follow the ordered release transitions after `P` through `T` in `RELEASE_IMPACT.json`;
3. if every transition has legacy `assessment_impact: none`, no reassessment is required because of the Profile version change;
4. if one or more transitions are `targeted`, review only artifacts that may match the union of those selectors;
5. if any transition is `all`, review that consumer's corpus;
6. if any transition is `breaking`, require an explicit migration decision for the affected scope;
7. if the transition path cannot be established, report insufficient compatibility evidence rather than inventing it.

A new assessment specification SHOULD instead state its own compatibility contract explicitly. It may reuse this facade, partially reuse it, or define a different migration model.

## Consumer obligations

All downstream consumers SHOULD:

- record the exact Profile version and, where appropriate, immutable source revision used to produce an artifact;
- keep their own procedure/version provenance separate from Profile provenance;
- preserve frozen work contracts unless that work explicitly adopts a newer contract;
- avoid copying VSM definitions into local compatibility logic;
- declare how Profile changes affect their own artifacts rather than assuming another consumer's reassessment policy applies.

A consumer may additionally record a derived statement such as “compatible through Profile X”, but that statement is not a replacement for the original Profile version and should be reproducible under that consumer's declared compatibility rule.

## Assessment specifications

`opensiro/vsm-harness-skills` owns assessment specifications. The released `assess-vsm-harness` Methodology is the canonical general assessment used by `opensiro/vsm-harness-index`.

Future domain-specific or community assessment specifications may depend on the same Profile while defining different evidence, admission, capability, or migration requirements. Their compatibility rules belong with those specifications, not in the Profile.

## `vsm-oss-organization`

`opensiro/vsm-oss-organization` may consume a pinned Profile as a reference realization track and may later produce Profile-change proposals through ordinary bounded OSS work. That does not transfer semantic authority: a proposed change becomes Profile semantics only after it is accepted in this repository and represented by the Profile's release process.

Its implementation status also does not determine the Profile version by itself. Reference realization evidence may support a release decision, while the Profile repository remains the normative authority.

## Release identity

Git tags/releases remain the immutable identity of accepted Profile releases. `RELEASE_IMPACT.json` on `main` may describe the current not-yet-tagged version while it is being prepared; legacy consumers that require released semantics should resolve the facade from an accepted release or otherwise verify the release state.

Historical tags are not rewritten when this facade gains information about earlier transitions. Tagged historical artifacts remain immutable provenance.

## Non-goals

This contract does not:

- define or reinterpret S1-S5;
- define autonomy-state notation owned by downstream Methodology;
- make general-Index reassessment policy a VSM semantic concept;
- impose one migration policy on domain-specific or community assessments;
- create a second assessment database;
- create a second Profile version hierarchy;
- require frozen work to upgrade in place;
- make `vsm-oss-organization` or any other consumer a normative Profile authority.
