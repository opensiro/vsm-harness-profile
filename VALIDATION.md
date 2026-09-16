# Repository validation

This repository keeps the VSM Harness Profile's semantic authority in [`PROFILE.md`](PROFILE.md). Validation closes deterministic repository-maintenance invariants around that source; it does not decide whether a VSM statement is conceptually correct.

## Completion signals

Before this validator, repository closure relied on separately reviewable signals:

- [`VERSION`](VERSION) for the canonical Profile version;
- the version declaration in [`PROFILE.md`](PROFILE.md);
- [`CHANGELOG.md`](CHANGELOG.md) and [`VERSIONING.md`](VERSIONING.md) for change/release policy;
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

1. `PROFILE.md`, `VERSION`, `VERSIONING.md`, `CHANGELOG.md`, `README.md`, and `LICENSE` exist;
2. `VERSION` is a Semantic Version and matches the explicit current-version declarations in `PROFILE.md` and `README.md`;
3. the newest version heading in `CHANGELOG.md` matches `VERSION`;
4. repository-local Markdown links resolve to paths inside the repository;
5. no second Markdown document independently declares a `**Version:**` Profile version, so `PROFILE.md` remains the sole versioned Profile source;
6. every existing SemVer-style `v*` Git tag records the same version in its tagged `VERSION` and `PROFILE.md`, and that released version remains represented in the current changelog.

Git tag checks run when the repository is available as a Git worktree. CI uses full history so those checks are active there. The validator does not require a tag for an unreleased version bump; a tag/release is an acceptance artifact created after the corresponding revision is accepted.

## Downstream direction

`vsm-harness-skills` may bundle a generated Profile snapshot for portable assessment. Its sync tooling reads this repository's `PROFILE.md` and `VERSION` and records immutable source provenance. That consumer-side drift check is intentionally not reimplemented here, and a downstream copy is never treated as a normative input to this validator.

## Reviewer judgment remains necessary

The oracle intentionally does **not** determine:

- whether an S1/S2/S3/S3*/S4/S5 definition or interpretation is conceptually correct;
- whether repository evidence really establishes an organizational function or ownership relation;
- whether a semantic change should be classified PATCH, MINOR, or MAJOR;
- whether release notes adequately explain semantic impact;
- whether a proposed normative change should be accepted.

Those remain evidence and review questions. The validator only makes ordinary mechanical closure failures explicit and reproducible.
