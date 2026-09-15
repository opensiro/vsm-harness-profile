# Literature map

This directory records what the profile is based on and what is a later modification. Files are grouped by epistemic role, not convenience.

## 1. Primary basis

Primary-author sources define the theoretical orientation.

| Source | Local status | Rights |
| --- | --- | --- |
| Stafford Beer, *Brain of the Firm*, 2nd ed., Wiley, ISBN 978-0-471-94839-1 | [English bibliographic record](primary/brain-of-the-firm.md); full text not vendored | Copyrighted and commercially available; no open redistribution license found. |
| Stafford Beer, *The Heart of Enterprise* | Bibliographic reference only | Copyrighted; obtain from an authorized source. |
| Stafford Beer, *Diagnosing the System for Organizations* | Bibliographic reference only | Copyrighted; obtain from an authorized source. |
| W. Ross Ashby, *An Introduction to Cybernetics* | External reference in the profile | Consult the rights statement of the authorized edition used. |

No full-text edition of *Brain of the Firm* is vendored. A lawfully obtained copy may be used privately, but it must not be committed unless its exact edition permits repository redistribution.

## 2. Secondary explanatory source

| Source | Local status | Rights |
| --- | --- | --- |
| Angela Espinosa, Jon Walker, Andrea Martinez-Lozada, “The Viable System Model: An Introduction to Theory and Practice,” *Journal of Systems Thinking* 3(1), 2023, DOI 10.54120/jost.000004 | [Unmodified PDF](secondary/the-viable-system-model-an-introduction-to-theory-and-practice.pdf) and [license record](secondary/the-viable-system-model-an-introduction-to-theory-and-practice.LICENSE.md) | CC BY-NC-ND; attribution required, commercial use and derivatives prohibited. |
| Jon Walker, *The Viable Systems Model Guide*, v3.2 | External reference: <https://vsmg.lrc.org.uk/> | CC BY-NC-SA 4.0 on the publisher site. |

Secondary sources explain VSM but do not override Beer or the explicit boundary of [PROFILE.md](../PROFILE.md).

## 3. Adaptations and modifications

- [Agent VSM Extension](adaptations/agent-vsm-extension.md) is a local descriptive extension for agent harnesses. It studies conditional regulatory load, redundancy, collapse, parent-supplied functions, and limiting cases such as `Environment ⇄ S1`. These claims are not Beer concepts and do not redefine the canonical S1–S5 meanings in `PROFILE.md`.
- [Organizational Synthesis Model](adaptations/organizational-synthesis-model.md) is a local prescriptive development methodology. It describes progressive organizational development and transformation, including a practical `S1 → S2 → S3 → S3* → S4 → S5` construction path with conditional gates. Its phases, transformations, and assisted-viability measures are not Beer concepts.
- [`opensiro/terminal-bench-vsm`](https://github.com/opensiro/terminal-bench-vsm) is a worked historical example of evolutionary VSM development. In particular, [`vsmlite-tb/osm.md`](https://github.com/opensiro/terminal-bench-vsm/blob/main/vsmlite-tb/osm.md) records an earlier progressive-acquisition approach. It is implementation evidence, not theoretical authority.
- [`../profiles/`](../profiles/) contains MIN/MAX agent-harness implementation profiles. They are examples, not literature and not conformance levels.
- [`vsm-skills`](https://github.com/opensiro/vsm-skills) owns evidence collection, token-cost methods, and categorical TL;DR rules. Those are operationalizations of the profile.

## Authority rule

When claims conflict, use this order:

1. authorized primary Beer sources;
2. attributed scholarly interpretation;
3. the declared engineering choices in [PROFILE.md](../PROFILE.md);
4. local adaptations, profiles, skills, and index methods.

A GitHub implementation is evidence of its own design, not theoretical authority for VSM.
