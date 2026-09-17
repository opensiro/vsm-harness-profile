# Repository validation

This repository keeps the VSM Harness Profile's semantic authority in [`PROFILE.md`](PROFILE.md). Validation closes deterministic repository-maintenance invariants around that source; it does not decide whether a VSM statement or a maintainer's semantic-impact judgment is conceptually correct.

## Completion signals

Repository closure uses separately reviewable signals:

- [`VERSION`](VERSION) for the canonical Profile version;
- the version declaration in [`PROFILE.md`](PROFILE.md);
- [`VERSIONING.md`](VERSIONING.md) for SemVer and release policy;
- [`CONSUMER_CONTRACT.md`](CONSUMER_CONTRACT.md) for the stable downstream compatibility/reassessment interface;
- [`RELEASE_IMPACT.json`](RELEASE_IMPACT.json) for machine-readable release-impact history;
- [`CHANGELOG.md`](CHANGELOG.md) for human-readable change and impact rationale;
- Git tags and GitHub Releases for accepted immutable release identity;
- the downstream `vsm-harness-skills` sync check, which consumes Profile artifacts and verifies its generated snapshot against this repository.

The local oracle makes the repository-internal subset executable without moving normative authority downstream.

## Deterministic checks

Run:

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -v
```

The validator checks that:

1. `PROFILE.md`, `VERSION`, `VERSIONING.md`, `CHANGELOG.md`, `README.md`, `CONSUMER_CONTRACT.md`, `RELEASE_IMPACT.json`, and `LICENSE` exist;
2. `VERSION` is a Semantic Version and matches the explicit current-version declarations in `PROFILE.md` and `README.md`;
3. the newest version heading in `CHANGELOG.md` matches `VERSION`;
4. `RELEASE_IMPACT.json` is valid JSON, identifies this Profile, and forms one contiguous release chain through the current `VERSION`;
5. release-impact versions match version headings in the changelog;
6. impact values and selectors satisfy the machine-readable contract;
7. PATCH transitions are `compatible + none`, MINOR transitions are `compatible + none|targeted`, and MAJOR transitions are `breaking + targeted|all`;
8. repository-local Markdown links resolve to paths inside the repository;
9. no second Markdown document independently declares a `**Version:**` Profile version, so `PROFILE.md` remains the sole versioned Profile source;
10. every existing SemVer-style `v*` Git tag records the same version in its tagged `VERSION` and `PROFILE.md`, and that released version remains represented in the current changelog.

Git tag checks run when the repository is available as a Git worktree. CI uses full history so those checks are active there. The validator does not require a tag for an unreleased version bump; a tag/release is an acceptance artifact created after the corresponding revision is accepted.

## Release-impact boundary

The validator makes the declared downstream contract mechanically coherent; it does not decide whether maintainers chose the correct impact classification.

For example, it can prove that a PATCH was declared `compatible + none`, that a targeted transition has bounded selectors, and that the release chain is complete. It cannot prove that a semantic change truly deserved PATCH rather than MINOR, or that a selected function/concept is the only affected scope.

That distinction is deliberate: impact **declaration and consistency** are completion-oracle concerns; impact **truth** remains a semantic/evidence review concern.

## Downstream direction

`vsm-harness-skills` may bundle a generated Profile snapshot for portable assessment. Its sync tooling reads this repository's `PROFILE.md` and `VERSION` and records immutable source provenance. A consumer may additionally use `RELEASE_IMPACT.json` to determine whether an older assessment requires review before use with a later Profile.

Consumer-side compatibility state is intentionally not written back into Profile provenance. A downstream copy is never treated as a normative input to this validator.

`vsm-oss-organization` can eventually consume the same facade to distinguish an upstream release that requires no local semantic migration from targeted/breaking work. That downstream integration remains separate from this repository's semantic authority.

## Reviewer judgment remains necessary

The oracle intentionally does **not** determine:

- whether an S1/S2/S3/S3*/S4/S5 definition or interpretation is conceptually correct;
- whether repository evidence really establishes an organizational function or ownership relation;
- whether a semantic change should be classified PATCH, MINOR, or MAJOR;
- whether `compatible` vs `breaking` is semantically correct for a proposed change;
- whether `none`, `targeted`, or `all` is the correct real-world reassessment scope;
- whether the chosen targeted selectors are semantically complete;
- whether release notes adequately explain semantic impact;
- whether a proposed normative change should be accepted.

Those remain evidence and review questions. The validator only makes ordinary mechanical closure failures explicit and reproducible.
