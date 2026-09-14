# VSM Harness Profile

VSM Harness Profile is the implementation-agnostic organizational reference for autonomous AI agent harnesses.

Start with [PROFILE.md](PROFILE.md). It is the only authoritative definition of VSM functions in this ecosystem.

```text
Beer / cybernetics
        ↓
VSM Harness Profile
        ↓
vsm-skills assessment procedure
        ↓
vsm-harness-index assessments and derived comparisons
```

The profile defines **organizational semantics**: S1, S2, S3, S3*, S4, S5, recursion, autonomy, variety, escalation, evidence boundaries, and common category errors. It does not define repository assessments, autonomy scores, comparative signatures, rankings, manifests, protocols, or runtime APIs.

A core rule is to **map the VSM function before classifying autonomy**. A router, manager, verifier, planner, learning loop, prompt, or subagent is never sufficient evidence from its name or existence alone. The mapping must first establish the organizational function at the declared system boundary, then identify who owns the relevant decision right.

## Repository structure

| Path | Responsibility |
| --- | --- |
| [PROFILE.md](PROFILE.md) | Consolidated VSM basis, harness interpretation, invariants, evidence rules, and category errors. |
| [literature/](literature/README.md) | Provenance separated into primary sources, secondary sources, and explicit adaptations. |
| [profiles/](profiles/README.md) | Non-normative MIN/MAX implementation examples derived from the profile. |
| [examples/](examples/) | Short conceptual examples at different boundaries and recursion levels. |

Evidence collection and standalone repository assessments belong to [`assess-vsm-harness`](https://github.com/opensiro/vsm-skills/tree/main/skills/assess-vsm-harness). Cohort-relative synthesis belongs to `vsm-skills`, while the published assessment corpus and derived tables belong to [vsm-harness-index](https://github.com/opensiro/vsm-harness-index).

## Boundary

The profile defines organizational functions and relationships. It does not define protocols, transports, manifests, runtimes, deployment models, message formats, a required agent topology, or a numerical maturity model.

## License

Original profile documentation, examples, and implementation profiles are licensed under [CC BY 4.0](LICENSE). Third-party literature is excluded and retains its stated license or copyright status; see [literature/README.md](literature/README.md). The bundled article is separately covered by [CC BY-NC-ND 4.0](LICENSES/CC-BY-NC-ND-4.0.txt) and its companion attribution record.
