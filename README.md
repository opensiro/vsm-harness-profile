# VSM Harness Profile

**Current Profile version: `0.2.0`**

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
| [VERSIONING.md](VERSIONING.md) | Versioning, release, and downstream provenance contract. |
| [CHANGELOG.md](CHANGELOG.md) | Material normative changes and assessment impact. |
| [literature/](literature/README.md) | Provenance separated into primary sources, secondary sources, and explicit adaptations. |
| [profiles/](profiles/README.md) | Non-normative MIN/MAX implementation examples derived from the profile. |
| [examples/](examples/) | Short conceptual examples at different boundaries and recursion levels. |

Evidence collection and standalone repository assessments belong to [`assess-vsm-harness`](https://github.com/opensiro/vsm-harness-skills/tree/main/skills/assess-vsm-harness). Cohort-relative synthesis belongs to `vsm-harness-skills`, while the published assessment corpus and derived tables belong to [vsm-harness-index](https://github.com/opensiro/vsm-harness-index).

## Versioning

The Profile follows the policy in [VERSIONING.md](VERSIONING.md). `v0.2.0` is the first explicitly versioned repository revision. The immediately preceding pre-versioned line can be referred to as the `v0.1.0` baseline for migration discussion, but no historical `v0.1.0` tag/release was published.

Downstream assessments should preserve which Profile and assessment-procedure versions they used so semantic revisions can trigger targeted, traceable reassessment rather than silent reinterpretation.

## Boundary

The profile defines organizational functions and relationships. It does not define protocols, transports, manifests, runtimes, deployment models, message formats, a required agent topology, or a numerical maturity model.

## License

Original profile documentation, examples, and implementation profiles are licensed under [CC BY 4.0](LICENSE). Third-party literature is excluded and retains its stated license or copyright status; see [literature/README.md](literature/README.md). The bundled article is separately covered by [CC BY-NC-ND 4.0](LICENSES/CC-BY-NC-ND-4.0.txt) and its companion attribution record.
