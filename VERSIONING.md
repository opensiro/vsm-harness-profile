# Versioning

VSM Harness Profile uses Semantic Versioning for the normative harness interpretation.

- **PATCH** — editorial clarification that should not change a conforming mapping.
- **MINOR** — backward-compatible conceptual refinement that may change how evidence, ownership, or a VSM function is mapped and therefore may trigger targeted reassessment.
- **MAJOR** — incompatible change to the profile's organizational model, conformance contract, or meaning of an existing normative concept.

The version in [`VERSION`](VERSION) is the canonical profile version. A release should also be represented by a Git tag/release when the change is accepted.

## Assessment provenance

Downstream assessments SHOULD record the Profile version and the assessment-procedure version used to produce them. A newer Profile version does not automatically invalidate an older assessment, but any semantic change that can affect an existing mapping SHOULD be evaluated through the Index reassessment process.

A bundled or vendored copy of `PROFILE.md` MUST identify the Profile version it represents and SHOULD record an immutable source revision. Generated copies MUST be checked for drift before an assessment procedure is released.

## Baseline note

`v0.2.0` is the first explicitly versioned Profile revision in the repository. The pre-versioned line that preceded it may be referred to as the **v0.1.0 baseline** for migration discussions, but no historical `v0.1.0` release or tag was published. This distinction avoids inventing provenance that the repository did not previously record.
