# VSM Harness Profile

VSM Harness Profile is the implementation-agnostic organizational reference used by [vsm-skills](https://github.com/opensiro/vsm-skills) and [vsm-harness-index](https://github.com/opensiro/vsm-harness-index).

Start with [PROFILE.md](PROFILE.md). It is the only authoritative definition of VSM functions in this ecosystem.

## Repository structure

| Path | Responsibility |
| --- | --- |
| [PROFILE.md](PROFILE.md) | Consolidated VSM basis, harness interpretation, invariants, evidence rules, and category errors. |
| [literature/](literature/README.md) | Provenance separated into primary sources, secondary sources, and explicit adaptations. |
| [profiles/](profiles/README.md) | Non-normative MIN/MAX implementation examples derived from the profile. |
| [examples/](examples/) | Short conceptual examples at different boundaries and recursion levels. |

Harness evidence collection and categorical TL;DR reconstruction belong to [`assess-vsm-harness`](https://github.com/opensiro/vsm-skills/tree/main/skills/assess-vsm-harness); the published catalog belongs to [vsm-harness-index](https://github.com/opensiro/vsm-harness-index).

## Boundary

The profile defines organizational functions and relationships. It does not define protocols, transports, manifests, runtimes, deployment models, message formats, or a required agent topology.

## License

Original profile documentation, examples, and implementation profiles are licensed under [CC BY 4.0](LICENSE). Third-party literature is excluded and retains its stated license or copyright status; see [literature/README.md](literature/README.md). The bundled article is separately covered by [CC BY-NC-ND 4.0](LICENSES/CC-BY-NC-ND-4.0.txt) and its companion attribution record.
