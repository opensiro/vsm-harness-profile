# VSM Harness Profile

**Current Profile version: `0.2.4`**

VSM Harness Profile is the implementation-agnostic organizational reference for autonomous AI agent harnesses.

Start with [PROFILE.md](PROFILE.md). It is the only authoritative definition of VSM functions in this ecosystem.

```text
Beer / cybernetics
        ↓
VSM Harness Profile
        ↓
vsm-harness-skills assessment procedure
        ↓
vsm-harness-index assessments and derived comparisons
```

The profile defines **organizational semantics**: S1, S2, S3, S3*, S4, S5, recursion, autonomy, variety, escalation, evidence boundaries, and common category errors. It does not define repository assessments, autonomy scores, comparative signatures, rankings, manifests, protocols, or runtime APIs.

A core rule is to **map the VSM function before classifying autonomy**. A router, manager, verifier, planner, learning loop, prompt, or subagent is never sufficient evidence from its name or existence alone. Version `0.2.0` makes the next distinction explicit as well: after the function is established, identify the **decisive decision/feedback right and its owner**, and record deterministic enforcement/support separately.

```text
repository evidence
        ↓
organizational function
        ↓
decisive decision / feedback right
        ↓
owner
        ↓
supporting enforcement / transport
        ↓
downstream autonomy classification
```

## Repository structure

| Path | Responsibility |
| --- | --- |
| [PROFILE.md](PROFILE.md) | Normative VSM basis, harness interpretation, invariants, ownership/evidence rules, and category errors. |
| [VERSION](VERSION) | Canonical Profile version. |
| [VERSIONING.md](VERSIONING.md) | SemVer, release, provenance, and reassessment-impact policy. |
| [CONSUMER_CONTRACT.md](CONSUMER_CONTRACT.md) | Stable downstream facade: provenance vs compatibility, release-impact composition, and consumer obligations. |
| [RELEASE_IMPACT.json](RELEASE_IMPACT.json) | Machine-readable Profile release-impact chain for deterministic downstream selection. |
| [CHANGELOG.md](CHANGELOG.md) | Human-readable material changes, compatibility, and assessment impact. |
| [VALIDATION.md](VALIDATION.md) | Deterministic completion-oracle checks and the boundary with semantic review. |
| [literature/](literature/README.md) | Provenance separated into primary sources, secondary sources, and explicit adaptations. |
| [profiles/](profiles/README.md) | Non-normative MIN/MAX implementation examples derived from the profile. |
| [examples/](examples/) | Short conceptual examples at different boundaries and recursion levels. |

Evidence collection and standalone repository assessments belong to [`assess-vsm-harness`](https://github.com/opensiro/vsm-harness-skills/tree/main/skills/assess-vsm-harness). Cohort-relative synthesis belongs to `vsm-harness-skills`, while the published assessment corpus and derived tables belong to [vsm-harness-index](https://github.com/opensiro/vsm-harness-index).

## Versioning and downstream compatibility

The Profile follows the policy in [VERSIONING.md](VERSIONING.md). `v0.2.0` is the first explicitly versioned repository revision. The immediately preceding pre-versioned line can be referred to as the `v0.1.0` baseline for migration discussion, but no historical `v0.1.0` tag/release was published.

Downstream artifacts preserve the exact Profile and assessment-procedure versions that produced them. A later Profile version does **not** by itself require reassessment or provenance rewrites. Consumers determine whether review is needed from the release-impact path defined by [CONSUMER_CONTRACT.md](CONSUMER_CONTRACT.md) and represented in [RELEASE_IMPACT.json](RELEASE_IMPACT.json).

In particular, a compatible PATCH with `assessment_impact: none` can become the active Profile without touching every historical harness assessment. Targeted or breaking changes remain explicit and traceable.

## Validation

Ordinary repository-maintenance invariants can be checked locally with:

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -v
```

See [VALIDATION.md](VALIDATION.md) for the machine-checkable boundary. These checks intentionally do not judge whether VSM semantics or a maintainer's impact classification are conceptually correct.

## Boundary

The profile defines organizational functions and relationships. It does not define protocols, transports, manifests, runtimes, deployment models, message formats, a required agent topology, or a numerical maturity model.

The downstream facade similarly does not define a second semantic model. It only tells consumers how to preserve exact Profile provenance and reason about later release compatibility without treating every version bump as a corpus migration.

## Contributing and organization

Contribute Profile semantics, normative wording, release-impact metadata, examples, and repository-local maintenance here.

For **currently tracked work across the bounded VSM Harness OSS group**, start with the shared [`OpenSiro VSM OSS TODO`](https://github.com/opensiro/vsm-oss-organization/blob/main/TODO.md), then return here when the selected task is Profile-owned. `TODO.md` owns current selection/order only; this repository remains authoritative for Profile task scope, evidence and acceptance.

For questions or proposals about **how the OpenSiro VSM Harness OSS repositories are organized as a system** — contributor roles, authority boundaries, cross-repository control, escalation, milestone sequencing, or the shared contribution control plane — use [`opensiro/vsm-oss-organization`](https://github.com/opensiro/vsm-oss-organization). That repository applies this Profile to the OSS organization; it does not replace this repository as the normative source of VSM semantics.

## License

Licensing follows repository function rather than applying a software license to the normative specification:

- original Profile documentation, examples, implementation profiles, and machine-readable semantic/release metadata are licensed under [CC BY 4.0](LICENSE);
- repository-maintenance software in `scripts/` and `tests/`, plus CI workflow configuration under `.github/workflows/`, is licensed under [Apache License 2.0](LICENSES/Apache-2.0.txt);
- third-party literature is excluded from both grants and retains its stated license or copyright status; see [literature/README.md](literature/README.md);
- the bundled article is separately covered by [CC BY-NC-ND 4.0](LICENSES/CC-BY-NC-ND-4.0.txt) and its companion attribution record.

This licensing clarification does not change the Profile version or normative semantics.
