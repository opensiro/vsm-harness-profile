# Versioning

VSM Harness Profile uses Semantic Versioning for the normative harness interpretation.

- **PATCH** — editorial clarification that does not change a conforming mapping.
- **MINOR** — backward-compatible conceptual refinement that may add or refine mapping distinctions and may justify targeted reassessment.
- **MAJOR** — incompatible change to the profile's organizational model, conformance contract, or meaning of an existing normative concept.

The version in [`VERSION`](VERSION) is the canonical Profile version. Every explicitly versioned Profile release from `v0.2.0` onward must also have an immutable `v<version>` Git tag and a GitHub Release pointing to the same release target.

## Provenance is not freshness

Downstream assessments SHOULD record the exact Profile version and assessment-procedure version used to produce them. That provenance is historical and MUST NOT be rewritten merely because a later compatible Profile release exists.

A newer Profile version does not automatically invalidate an older assessment and does not automatically make it stale. Whether review is required is determined by the declared release-impact path in [`RELEASE_IMPACT.json`](RELEASE_IMPACT.json), as specified by [`CONSUMER_CONTRACT.md`](CONSUMER_CONTRACT.md).

This creates two deliberately separate facts:

```text
artifact provenance
= exact Profile used when the artifact was produced

current compatibility
= derived from later Profile release-impact transitions
```

A bundled or vendored copy of `PROFILE.md` MUST identify the Profile version it represents and SHOULD record an immutable source revision. Generated copies MUST be checked for drift before an assessment procedure is released.

## Release-impact contract

Every explicitly versioned Profile transition represented by the current repository state MUST have one entry in `RELEASE_IMPACT.json`.

Compatibility and reassessment scope are separate dimensions:

- `compatible` means the previous conformance contract remains sufficient;
- `breaking` means an explicit migration decision is required for the affected scope;
- `none` means the Profile transition itself requires no reassessment;
- `targeted` means only artifacts matching declared selectors may need review;
- `all` means every current assessment must be considered for review.

The machine-readable facade has no independent semantic-version axis. `VERSION` remains the Profile version. The consumer contract and validator define the stable interpretation of release-impact fields.

### SemVer invariants

The following repository rules make SemVer operational for downstream consumers:

- PATCH MUST be `compatible` with `assessment_impact: none`;
- MINOR MUST be `compatible` and MAY use `none` or `targeted`, but MUST NOT require corpus-wide reassessment merely because the minor version changed;
- MAJOR MUST be `breaking` and MUST use `targeted` or `all` impact.

If every current assessment would require review because of a Profile change, that is not a backward-compatible MINOR transition under this contract.

A PATCH clarification can expose a weak historical assessment without causing a semantic migration. Such a finding is a same-ref correction under the assessment's frozen contract, not reassessment impact caused by the PATCH release itself. Profile `0.2.1` is the reference example: it made the existing S2 witness mechanically explicit while preserving conforming `0.2.0` mappings.

## Targeted selectors

A targeted transition MUST declare bounded selectors instead of forcing consumers to infer review scope from prose alone. Selector syntax and composition rules are defined in `CONSUMER_CONTRACT.md`.

Selectors describe where review may be needed; they do not define new VSM semantics. The matching changelog entry remains the human-readable explanation of why the selector applies.

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

A downstream reassessment round or other historical work item may freeze a Profile/Methodology pair. A later release does not silently upgrade that frozen contract.

Consumers may separately determine that the frozen artifact remains compatible through newer Profile releases. That derived compatibility does not change the artifact's original provenance and does not require rewriting the frozen record.

## Baseline note

`v0.2.0` is the first explicitly versioned Profile revision in the repository. The pre-versioned line that preceded it may be referred to as the **v0.1.0 baseline** for migration discussions, but no historical `v0.1.0` release or tag was published. This distinction avoids inventing provenance that the repository did not previously record.
