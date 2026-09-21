# Promotion and downstream reindex contract for experimental `S`

**Status:** experimental process contract  
**Normative effect:** none

This file defines how the self-organizing-autonomy experiment may leave `experiments/` without silently changing the released VSM Harness ecosystem.

## 1. Separation of states

The experiment has three materially different lifecycle states:

```text
draft experiment
      ↓
stable experiment
      ↓
released normative adoption
```

### Draft experiment

Semantics are still being tested. No downstream canonical artifact changes.

### Stable experiment

The experimental contract has passed the stability gates in `SPEC.md` and is frozen enough to prepare adoption. `stable` is **not** a Profile release and does not change the active assessment state set.

The stable transition MUST trigger preparation of an explicit downstream migration/reindex work item so the adoption impact is known before release.

### Released normative adoption

The distinction becomes normative only through an explicit Profile/Methodology release transaction. Only that released pair may be used for canonical assessment migration and Index publication.

## 2. Normative adoption transaction

A promotion PR must explicitly decide at least:

1. the final name and notation (`S` may still be renamed);
2. whether the capability is per-function, system-level, or both;
3. its exact relationship to existing `A`, `C`, and `P` publication semantics;
4. any allowed parent-governed composition such as a future `S(P)`;
5. the minimum positive witness and required negative/counterfactual checks;
6. whether strong recursive viability is required or only a stronger system-level witness;
7. Profile version and compatibility classification;
8. Methodology version and assessment artifact changes;
9. machine-readable release impact and migration scope;
10. Index regeneration/reassessment procedure.

The adoption must follow the existing `VERSIONING.md`, `CONSUMER_CONTRACT.md`, `RELEASE_IMPACT.json`, release tags, and downstream provenance rules. The experiment itself does not preselect a SemVer number or release-impact value.

## 3. Index reindex boundary

The desired downstream sequence is:

```text
experimental S reaches stable
        ↓
freeze experimental semantics
        ↓
open/prepare explicit adoption + migration round
        ↓
release adopting Profile/Methodology pair
        ↓
pin migration contract in vsm-harness-index
        ↓
reassess/reindex against released semantics
        ↓
regenerate derived views
        ↓
validate corpus consistency
```

Canonical Index vectors MUST NOT acquire `S` from the experimental directory alone.

## 4. Historical assessments

Adoption must preserve historical provenance.

An older assessment that recorded `A` under its original Profile/Methodology remains a valid historical artifact under that contract. A later migration may determine that the same pinned repository revision also satisfies the new distinction, but it must do so through an explicit same-ref migration/revalidation or a new-ref reassessment as appropriate.

Do not rewrite generation provenance to make an old artifact appear to have been produced under the future `S` contract.

## 5. Reindex strategy

The migration round should separate two questions:

1. **compatibility:** does the historical assessment remain valid under the released transition?
2. **enrichment:** has the evidence needed to distinguish ordinary `A` from the new self-organizing capability actually been reviewed?

A missing experimental/new-state review must not automatically downgrade an existing `A` or be represented as `—`. If the future Methodology needs an explicit not-reviewed representation for the new distinction, that representation must be designed before corpus migration.

A complete public `S` view should not pretend that unreviewed historical `A` rows were tested. The migration should therefore track coverage explicitly until all in-scope candidates have been reviewed.

## 6. Candidate selection for migration

If the adopted semantics require ordinary `A` as a prerequisite, existing autonomous rows are the natural first review cohort. However, the released Profile/Methodology and release-impact contract—not this experiment—must define the authoritative migration scope.

The migration procedure should inspect upstream changes first and avoid re-proving unchanged baseline claims when a same-ref assessment already establishes the function, owner, boundary, and closure required as prerequisites. The new work should focus on evidence unique to the new distinction: repertoire insufficiency, endogenous reconstruction, authority, integration, and post-change absorption.

## 7. Derived views

No `FULL_S.md`, ranking, signature field, website badge, or similar derived projection should be canonical before normative adoption and sufficient migration coverage.

If an experimental comparison is useful before adoption, it must remain clearly under an experimental path and use the non-normative findings from `SPEC.md` rather than writing `S` into canonical autonomy vectors.

After adoption, derived views remain deterministic projections of canonical assessment states/evidence, not subjective product-quality scores or maturity rankings.

## 8. Rollback

If the experiment fails its reproducibility or information-value tests, close it as a documented negative result. No canonical rollback is needed because draft/stable experimental work has no normative effect.

If problems are discovered after normative adoption, repair must follow the ordinary versioning and release-impact contract rather than editing the experiment to retroactively change released semantics.
