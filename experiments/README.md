# Profile experiments

This directory contains **non-normative** experiments for possible future VSM Harness Profile semantics.

Nothing under `experiments/` changes the current Profile, the meaning of `PROFILE.md`, the value in `VERSION`, the release-impact chain, or any downstream canonical assessment. Consumers MUST NOT treat an experimental state, symbol, test, or fixture as part of the active VSM Harness Profile unless it has been promoted through a released Profile/Methodology pair.

The normative source remains [`../PROFILE.md`](../PROFILE.md).

## Why this directory exists

Some semantic hypotheses need a fixture corpus and reproducibility work before they are safe to place in the normative Profile. Keeping that work here allows the repository to develop those hypotheses in public without silently changing historical assessments.

The expected lifecycle is:

```text
issue / hypothesis
        ↓
experimental draft
        ↓
fixture corpus + counterexamples
        ↓
independent reproducibility review
        ↓
stable experimental specification
        ↓
explicit normative adoption release
        ↓
downstream migration / reassessment / reindex
```

`stable` in this directory means the experimental contract is frozen enough to prepare adoption. It does **not** itself make the experiment normative.

## Promotion rule

An experiment may move toward normative adoption only when its own stability gates are satisfied and the change is carried through the repository's ordinary release/versioning contract.

Promotion MUST NOT:

- rewrite historical assessment provenance;
- silently reinterpret an existing state;
- mutate `PROFILE.md`, `VERSION`, `RELEASE_IMPACT.json`, Skills, or Index artifacts from inside the experiment;
- make downstream consumers infer migration scope from prose alone.

When an experiment reaches `stable`, the next step is an explicit adoption transaction that determines the released Profile/Methodology pair and release impact. Canonical Index reindexing or reassessment begins only against that released contract.

## Current experiments

- [`self-organizing-autonomy/`](self-organizing-autonomy/) — candidate `S` capability for endogenous reconstruction of organizational/regulatory repertoire; source discussion: [#13](https://github.com/opensiro/vsm-harness-profile/issues/13).
