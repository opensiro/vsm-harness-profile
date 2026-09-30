# VSM Harness Profile

**Current Profile version: `0.2.4`**

## I'm human

- **Web overview:** [opensiro.com](https://opensiro.com)
- **How do I contribute?** [Contribute to OpenSiro with AI](https://github.com/opensiro/vsm-oss-organization/blob/main/CONTRIBUTE_WITH_AI.md)

You can read and use the Profile directly without first learning the OpenSiro control structure. The contribution guide gives you a copy-paste route for handing an idea, issue, or open-ended contribution to an AI agent.

## I'm AI

Treat this README as the public handoff surface, then continue with the current shared [`START_HERE.md`](https://github.com/opensiro/vsm-oss-organization/blob/main/START_HERE.md). For already tracked work use the shared [`TODO.md`](https://github.com/opensiro/vsm-oss-organization/blob/main/TODO.md); for new, unclassified, cross-repository, or authority-sensitive work use [`CONTRIBUTOR_START.md`](https://github.com/opensiro/vsm-oss-organization/blob/main/CONTRIBUTOR_START.md).

If the bootstrap resolves Profile work to this repository, repository-local Profile semantics, normative wording, versioning, validation, evidence, and acceptance remain authoritative here.

VSM Harness Profile is the implementation-agnostic organizational reference for autonomous AI agent harnesses.

Start with [PROFILE.md](PROFILE.md). It is the only authoritative definition of VSM functions in this ecosystem.

```text
Beer / cybernetics
        ↓
VSM Harness Profile
        ↓
vsm-harness-skills assessment specifications
        ↓
general / domain-specific assessment indexes
```

The profile defines **organizational semantics**: S1, S2, S3, S3*, S4, S5, recursion, autonomy, variety, escalation, evidence boundaries, and common category errors. It does not define repository assessments, autonomy scores, comparative signatures, rankings, manifests, protocols, runtime APIs, or a universal reassessment policy for downstream consumers.

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
downstream classification under an assessment specification
```

## Repository structure

| Path | Responsibility |
| --- | --- |
| [PROFILE.md](PROFILE.md) | Normative VSM basis, harness interpretation, invariants, ownership/evidence rules, and category errors. |
| [VERSION](VERSION) | Canonical Profile version. |
| [VERSIONING.md](VERSIONING.md) | Profile SemVer, immutable releases, provenance, and consumer-independent version tracking. |
| [CONSUMER_CONTRACT.md](CONSUMER_CONTRACT.md) | Legacy compatibility facade for the released general assessment stack; not a universal reassessment policy. |
| [RELEASE_IMPACT.json](RELEASE_IMPACT.json) | Machine-readable legacy release-impact chain retained for existing consumers and frozen work. |
| [CHANGELOG.md](CHANGELOG.md) | Human-readable material Profile changes. |
| [VALIDATION.md](VALIDATION.md) | Deterministic completion-oracle checks and the boundary with semantic review. |
| [literature/](literature/README.md) | Provenance separated into primary sources, secondary sources, and explicit adaptations. |
| [profiles/](profiles/README.md) | Non-normative MIN/MAX implementation examples derived from the profile. |
| [examples/](examples/) | Short conceptual examples at different boundaries and recursion levels. |

Evidence collection and assessment specifications belong to [`vsm-harness-skills`](https://github.com/opensiro/vsm-harness-skills). The released [`assess-vsm-harness`](https://github.com/opensiro/vsm-harness-skills/tree/main/skills/assess-vsm-harness) skill is the canonical general assessment used by [`vsm-harness-index`](https://github.com/opensiro/vsm-harness-index). Future domain-specific assessment specifications may track the same Profile version while maintaining their own evidence and migration contracts.

## Versioning and downstream compatibility

The Profile follows the policy in [VERSIONING.md](VERSIONING.md). `v0.2.0` is the first explicitly versioned repository revision. The immediately preceding pre-versioned line can be referred to as the `v0.1.0` baseline for migration discussion, but no historical `v0.1.0` tag/release was published.

A Profile version identifies the normative organizational model independently of any one assessment corpus or implementation. Implementations, assessment specifications, derived profiles, and research protocols may pin or track that version for their own compatibility purposes.

Downstream artifacts preserve the exact Profile and procedure versions that produced them. A later Profile version does **not** by itself require reassessment, regeneration, or provenance rewrites. Each downstream consumer owns how Profile changes affect its artifacts.

The existing `RELEASE_IMPACT.json` / `CONSUMER_CONTRACT.md` surface remains supported for historical and released general-assessment consumers that already rely on it. Its `assessment_impact` metadata must not be generalized into a universal rule for future domain-specific or community assessment systems.

## Validation

Ordinary repository-maintenance invariants can be checked locally with:

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -v
```

See [VALIDATION.md](VALIDATION.md) for the machine-checkable boundary. These checks intentionally do not judge whether VSM semantics or a maintainer's semantic impact judgment is conceptually correct.

## Boundary

The profile defines organizational functions and relationships. It does not define protocols, transports, manifests, runtimes, deployment models, message formats, a required agent topology, or a numerical maturity model.

A harness does not need to have been designed as VSM for an assessment to map VSM functions that emerge at a declared system boundary. Conversely, an implementation that intentionally claims to realize this Profile can be assessed for whether those functions and relationships are actually present.

The Profile versions the model; downstream assessment specifications version how they test or classify systems against that model.

## Contributing and organization

Contribute Profile semantics, normative wording, versioning, examples, and repository-local maintenance here.

The shared bootstrap/current-work/routing links are kept near the top of this README so they remain directly discoverable without duplicating Organization policy here. `TODO.md` owns current selection/order only; this repository remains authoritative for Profile task scope, evidence and acceptance.

For questions or proposals about **how the OpenSiro VSM Harness OSS repositories are organized as a system** — contributor roles, authority boundaries, cross-repository control, escalation, milestone sequencing, or the shared contribution control plane — use [`opensiro/vsm-oss-organization`](https://github.com/opensiro/vsm-oss-organization). That repository applies this Profile as an intentional reference realization track; it does not replace this repository as the normative source of VSM semantics.

## License

Licensing follows repository function rather than applying a software license to the normative specification:

- original Profile documentation, examples, implementation profiles, and machine-readable semantic/release metadata are licensed under [CC BY 4.0](LICENSE);
- repository-maintenance software in `scripts/` and `tests/`, plus CI workflow configuration under `.github/workflows/`, is licensed under [Apache License 2.0](LICENSES/Apache-2.0.txt);
- third-party literature is excluded from both grants and retains its stated license or copyright status; see [literature/README.md](literature/README.md);
- the bundled article is separately covered by [CC BY-NC-ND 4.0](LICENSES/CC-BY-NC-ND-4.0.txt) and its companion attribution record.

This licensing clarification does not change the Profile version or normative semantics.
