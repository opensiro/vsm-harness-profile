# Versioning

VSM Harness Profile uses Semantic Versioning for the normative harness interpretation.

- **PATCH** — editorial clarification that does not change a conforming mapping.
- **MINOR** — backward-compatible conceptual refinement that may add or refine mapping distinctions.
- **MAJOR** — incompatible change to the profile's organizational model, conformance contract, or meaning of an existing normative concept.

The version in [`VERSION`](VERSION) is the canonical Profile version. Every explicitly versioned Profile release from `v0.2.0` onward must also have an immutable `v<version>` Git tag and a GitHub Release pointing to the same release target.

## Independent Profile versioning

Profile versions identify changes in the **normative organizational model itself**. They are not versions of the general Index, the released assessment Methodology, or any one implementation.

This independence is intentional. Multiple downstream consumers may inherit or track the same Profile version for different purposes, including:

- assessment specifications;
- reference or product implementations;
- derived or domain-specific profiles;
- research protocols;
- compatibility declarations in other formally specified systems.

A consumer SHOULD record the exact Profile version it applies and MAY define its own compatibility or migration policy relative to later Profile releases.

Therefore:

```text
Profile version change
        !=
universal downstream reassessment order
```

The Profile owns the semantic change. Each downstream consumer owns what that change means for its own artifacts.

## Provenance is not freshness

Downstream artifacts SHOULD record the exact Profile version and assessment-procedure version used to produce them. That provenance is historical and MUST NOT be rewritten merely because a later compatible Profile release exists.

A newer Profile version does not automatically invalidate an older artifact and does not automatically make it stale. Consumers determine whether and how review is required under their own declared contract.

This creates two deliberately separate facts:

```text
artifact provenance
= exact Profile used when the artifact was produced

consumer compatibility
= derived by the consumer relative to later Profile releases
```

A bundled or vendored copy of `PROFILE.md` MUST identify the Profile version it represents and SHOULD record an immutable source revision. Generated copies MUST be checked for drift before an assessment procedure or other derived consumer is released.

## Legacy general-assessment release-impact facade

[`RELEASE_IMPACT.json`](RELEASE_IMPACT.json) and [`CONSUMER_CONTRACT.md`](CONSUMER_CONTRACT.md) preserve the release-impact facade introduced for the existing general assessment stack.

That facade remains valid historical compatibility metadata for consumers and frozen work that already rely on it. In particular, old Profile/Methodology/Index provenance and previously completed reassessment rounds are not rewritten by this clarification.

However, `assessment_impact` and its selectors are **not a universal Profile-level reassessment policy for all future consumers**. New assessment specifications, domain-specific indexes, implementations, or derived profiles may track the same Profile releases while defining different compatibility and migration behavior.

The long-term boundary is:

```text
Profile
    → versions normative semantic changes

consumer
    → declares compatibility / migration consequences for its own artifacts
```

The legacy facade may continue to be maintained while current released consumers require it, but new ecosystem architecture must not treat it as authority over unrelated assessment systems.

## Release-impact contract for legacy consumers

Every explicitly versioned Profile transition represented by the current repository state MUST have one entry in `RELEASE_IMPACT.json` while the legacy facade remains supported.

Compatibility and reassessment scope are separate dimensions for those consumers:

- `compatible` means the previous conformance contract remains sufficient;
- `breaking` means an explicit migration decision is required for the affected scope;
- `none` means the Profile transition itself requires no reassessment in the legacy general-assessment contract;
- `targeted` means only artifacts matching declared selectors may need review in that contract;
- `all` means every current artifact in that contract must be considered for review.

The machine-readable facade has no independent semantic-version axis. `VERSION` remains the Profile version.

### SemVer invariants

The Profile's own SemVer meaning is determined by the normative model change above. While the legacy facade remains supported, its existing machine checks additionally require:

- PATCH to remain `compatible` with legacy `assessment_impact: none`;
- MINOR to remain `compatible` and use legacy `none` or `targeted`;
- MAJOR to be `breaking` and use legacy `targeted` or `all`.

These legacy consumer constraints must not be generalized into a rule that every future assessment system has the same reassessment scope.

A PATCH clarification can expose a weak historical assessment without causing a semantic migration. Such a finding is a same-ref correction under the assessment's frozen contract, not reassessment impact caused by the PATCH release itself. Profile `0.2.1` is the reference example: it made the existing S2 witness mechanically explicit while preserving conforming `0.2.0` mappings.

## Targeted selectors

For legacy consumers, a targeted transition declares bounded selectors instead of forcing them to infer review scope from prose alone. Selector syntax and composition rules are defined in `CONSUMER_CONTRACT.md`.

Selectors describe where review may be needed under that consumer contract; they do not define new VSM semantics and do not bind unrelated assessment specifications.

## Release tracking

`.github/workflows/publish-profile.yml` is the persistent Profile release publisher. It is idempotent and derives the default release target from the latest commit that changed `PROFILE.md` or `VERSION`, so release-maintenance commits cannot silently move a semantic release tag forward.

The publisher:

- verifies that the target contains the requested Profile version;
- requires the target to be an ancestor of the current repository state;
- creates `v<version>` only when absent;
- rejects any attempt to move an existing release tag to a different commit;
- creates the GitHub Release from the matching `CHANGELOG.md` section;
- verifies all explicitly versioned releases through `scripts/check_release_tracking.py`.

Manual dispatch exists only for explicit repair/backfill with a version and immutable target SHA. Scheduled validation runs the same tracking check so a future Profile version cannot remain silently present without both release surfaces.

## Frozen work

A downstream reassessment round, research protocol, implementation certification, or other historical work item may freeze a Profile/consumer pair. A later release does not silently upgrade that frozen contract.

Consumers may separately determine that the frozen artifact remains compatible through newer Profile releases. That derived compatibility does not change the artifact's original provenance and does not require rewriting the frozen record.

## Baseline note

`v0.2.0` is the first explicitly versioned Profile revision in the repository. The pre-versioned line that preceded it may be referred to as the **v0.1.0 baseline** for migration discussions, but no historical `v0.1.0` release or tag was published. This distinction avoids inventing provenance that the repository did not previously record.
