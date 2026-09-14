# VSM Harness Profile

## 1. Status and source boundary

VSM Harness Profile is an implementation-agnostic organizational profile for autonomous AI agent harnesses. It standardizes the organizational model, not its implementation.

This document is the ecosystem's sole authoritative definition of VSM terms. It distinguishes three layers:

1. **VSM basis** — Stafford Beer's model, supported by the sources catalogued in `literature/`.
2. **Harness interpretation** — this profile's application of those functions to autonomous agent harnesses.
3. **Local operationalization** — categorical publication notation, prompts, and workflows owned by `vsm-skills`, `vsm-harness-index`, or `profiles/`. These are not Beer concepts.

## 2. Scope and non-goals

The profile asks whether a declared system-in-focus has the organizational functions and relationships needed to remain coherent and adapt in a changing environment.

It does not define a model provider, agent protocol, RPC, transport, message format, manifest, tool protocol, identity system, telemetry standard, workflow language, runtime API, deployment model, programming language, or required number of agents.

An agent, service, human, policy, evaluator, or distributed combination may perform a VSM function. Component names are never sufficient evidence.

For the harness interpretation, assessment is centered on **agent autonomy**: which AI agent absorbs variety, exercises discretion, and holds bounded decision rights. Deterministic routing, storage, logging, interrupts, and human control may support or constrain that autonomy, but do not by themselves establish agentic enactment of a VSM function.

**Map the organizational function before classifying autonomy.** First establish what VSM function, if any, the observed behavior realizes at the declared system boundary. Only then identify the responsible actor, its decision rights, and how much of that function is agent-owned. A mechanism can support a VSM function without an autonomous agent owning it; conversely, agent autonomy does not make an arbitrary mechanism a VSM function.

Normative words such as `MUST` and `SHOULD` apply only to organizational invariants claimed by this profile, not to implementation mechanisms or certification.

## 3. Frame of analysis

Every application MUST state:

- the **system-in-focus** and recursion level;
- its purpose and identity;
- its relevant environment;
- its operational units;
- the evidence boundary and observation date/ref.

The **environment** includes the people, systems, institutions, constraints, opportunities, and disturbances with which the system must maintain a viable relationship. Moving the boundary can change every mapping.

VSM distinguishes **operations**, which enact the system's primary transformation, from the **metasystem**, which creates cohesion and adaptation. This is a functional distinction, not necessarily a managerial hierarchy.

## 4. System 1 — operations

**VSM basis.** S1 contains the operational units through which the system enacts its identity and purpose. Each unit is coupled to a local environment and may itself be a viable system.

**Harness interpretation.** S1 may be one durable agent loop, several autonomous work cells, human–agent teams, or other units that directly produce outcomes in the relevant environment.

**Invariants.** A viable design MUST contain operational capability. An S1 unit has an outcome, environment, and meaningful local variety—not merely a task label. It SHOULD retain enough autonomy to absorb local variety within constraints needed for cohesion of the whole.

**Not equivalent to.** Every agent process, tool call, microservice, or spawned worker.

## 5. System 2 — coordination

**VSM basis.** S2 dampens oscillation and conflict among S1 units through mutual adjustment, shared constraints, schedules, and other stabilizing channels.

**Harness interpretation.** S2 may use shared work state, reservations, scheduling, negotiated plans, collision detection, or human coordination practices.

**Invariants.** Where several S1 units coexist, enough coordination MUST exist to prevent destructive interference without centralizing decisions the units can absorb locally. A positive S2 mapping therefore needs evidence of a coordination problem among operational units and a mechanism or actor that regulates that interference.

**Not equivalent to.** A message bus, queue, router, workflow edge, task sequence, speaker selector, or parent-to-child delegation merely because it moves or assigns work. Delegation and task decomposition alone do not establish S2.

## 6. System 3 — inside-and-now control

**VSM basis.** S3 creates cohesion across current operations through resource bargaining, accountability, synergy, performance regulation, and intervention on behalf of the whole.

**Harness interpretation.** S3 may allocate budgets and tools, negotiate priorities, regulate current commitments, and intervene when local optimization threatens the larger system.

**Invariants.** S3 needs a whole-system view of current operations and actual authority over relevant resources or constraints. It SHOULD govern by exception rather than reproduce every local decision. Task allocation counts only when it is part of such whole-system regulation, not merely decomposition of a parent task.

**Not equivalent to.** Anything named manager, orchestrator, controller, supervisor, or lead agent. Selecting a worker, delegating a subtask, merging returned results, or enforcing a static workflow does not by itself establish S3.

## 7. System 3* — complementary audit

**VSM basis.** S3* gives the metasystem alternative, sporadic, and complementary access to operational reality beyond routine S1–S3 reporting.

**Harness interpretation.** Raw-artifact inspection, sampled replay, reconciliation, adversarial probes, external ground truth, or an independent evaluator may contribute when they can challenge ordinary operational claims.

**Invariants.** When routine reporting cannot provide enough confidence, the audit path MUST be sufficiently independent for the claim and risk it addresses. Its findings inform control, but S3* is not a duplicate S3. The audit path must add materially different access to operational reality rather than merely repeat the normal production check.

**Not equivalent to.** Generic logs, tracing, ordinary tests, or evaluation controlled entirely by the unit whose claims are being checked. A routine checker, critic, verifier, or mandatory QA stage in the same operational path is not automatically S3*.

## 8. System 4 — outside-and-then intelligence

**VSM basis.** S4 models the relevant external environment and possible future, developing options for adaptation.

**Harness interpretation.** S4 may investigate changing users, regulation, adversarial behaviour, model or tool capabilities, dependencies, threats, and opportunities, then test future-oriented options.

**Invariants.** S4 MUST be externally and prospectively oriented. Its model must enter a two-way conversation with current operational capability in S3. A positive S4 mapping therefore needs evidence of external or future-relevant distinctions, development of adaptation options, and a path by which those options can affect present capability.

**Not equivalent to.** Internal task planning, backlog ordering, chain-of-thought, a component called planner, generic learning, self-improvement, training, memory consolidation, or reaction to an external event by itself. These become relevant to S4 only when they participate in an external-and-prospective adaptation loop.

## 9. System 5 — policy and identity

**VSM basis.** S5 maintains identity, ethos, and ultimate policy and provides closure when tension between present operations and future adaptation cannot settle below.

**Harness interpretation.** S5 may be distributed across human authority, governance, durable purpose, risk boundaries, and mechanisms for identity-level decisions.

**Invariants.** S5 needs legitimate ultimate authority at the chosen recursion level. It SHOULD preserve coherence and balance S3 and S4 without absorbing routine operational control.

**Not equivalent to.** A system prompt, policy file, safety filter, approval gate, static constitution, or executive agent by name alone. Constraints and policy text may bound autonomy without themselves providing runtime identity or ultimate-policy closure.

## 10. Recursion and autonomy

VSM recurs because an S1 unit may itself be a viable system. A claimed recursive unit SHOULD have:

- a durable contribution to its parent system;
- a relevant local environment and identity;
- distinguishable operations;
- meaningful autonomy and local regulatory capacity;
- the metasystemic functions required for its own viability;
- channels connecting local and parent levels without duplicate authority.

Spawning a worker, nesting a graph, or creating a subagent proves task decomposition, not recursive viability.

Autonomy is the capacity to regulate local variety within constraints protecting the larger system. Centralizing locally absorbable variety overloads S3; delegating identity-level or cross-unit variety without constraints fragments the whole.

## 11. Variety and channels

**Variety** is the range of distinguishable states relevant to regulation. Requisite variety means the regulatory arrangement must be able to distinguish and respond to the disturbances for which it is responsible.

Analyze:

1. which disturbances operations and environment can produce;
2. which distinctions change the correct response;
3. which distinctions reach the regulator, with what delay or distortion;
4. which response repertoire and authority the regulator has;
5. where variety is attenuated, amplified, or lost in transduction.

Attenuation reduces presented variety; amplification increases regulatory capacity; transduction changes representation across a boundary. None is inherently good. A summary that removes a decisive distinction or additional agents that create uncoordinated noise both reduce viability.

The profile does not prescribe a channel topology or transport. Channels MUST have enough capacity, timeliness, and fidelity for the organizational conversations they carry.

## 12. Homeostasis, escalation, and algedonic signals

Homeostasis is dynamic regulation around viable bounds, not a fixed state. A central example is the S3–S4 relation:

- S3 brings current capability, commitments, and constraints;
- S4 brings environmental change, possible futures, and adaptation options;
- S5 supplies identity and policy and closes unresolved tension.

S3 dominance produces strategic myopia; S4 dominance produces novelty without operational grounding.

Routine exceptions SHOULD remain at the lowest level with requisite information and authority. Exceptions move when their variety exceeds local authority, capability, risk allowance, or time horizon.

An **algedonic signal** communicates exceptional pain or opportunity without waiting for normal reporting compression. It SHOULD reach an authority able to respond, preserve enough evidence for judgment, and remain exceptional rather than becoming a second routine channel. No severity schema or event protocol is required.

## 13. Evidence and mapping

Use these evidence bases:

| Basis | Meaning |
| --- | --- |
| `explicit` | Maintainer material deliberately assigns the organizational responsibility. |
| `structural` | Architecture or observed behaviour directly realizes it without VSM terminology. |
| `inferred` | The mapping depends on stated assumptions. |
| `unknown` | Evidence is insufficient to establish presence or absence. |

For each material mapping record function, responsible actors or mechanisms, decision rights, evidence, basis, confidence, boundary, and caveat.

Apply the evidence in this order:

1. establish the organizational function from behavior and relationships at the declared system boundary;
2. identify the actor or mechanism that carries it;
3. determine whether an autonomous agent owns the relevant decision right or whether the function remains runtime-, developer-, human-, or parent-owned;
4. only then apply any local autonomy notation defined outside this profile.

Absence of documentation is not proof of absence. Conversely, labels such as “manager”, “planner”, “auditor”, and “policy agent” are not proof of function.

## 14. Frequent category errors

- **Component-name mapping:** equating labels with S-functions.
- **Delegation as coordination:** task decomposition or parent-child delegation is counted as S2 without evidence of interference regulation among operations.
- **Manager as control:** task assignment or result aggregation is counted as S3 without a whole-system current view and authority over shared constraints or resources.
- **Centralized pseudo-viability:** a supervisor absorbs variety that belongs in autonomous S1 units.
- **Coordination as command:** S2 becomes another top-down controller.
- **Audit as observability:** the same path produces the action, success claim, metric, and evaluation.
- **Verifier as audit:** routine checking is counted as S3* without complementary and sufficiently independent access to operational reality.
- **Planning as intelligence:** internal task planning is counted as S4 without external/future coupling.
- **Learning as intelligence:** training, self-improvement, memory, or event reaction is counted as S4 without an external-and-prospective adaptation loop.
- **Prompt as policy:** policy text exists without legitimate authority or S3–S4 closure.
- **Nesting as recursion:** a technical child lacks its own environment, autonomy, and metasystem.
- **Cargo-cult completeness:** six named actors are created solely to mirror VSM labels.
- **Variety destruction:** summaries or routing rules remove distinctions required for control.

## 15. Conformance claim

A mapping conforms to this profile when it declares its boundary, uses the functions and relationships above, separates evidence from inference, exposes uncertainty, and avoids imposing implementation mechanisms as VSM requirements.

The profile does not certify that a harness is viable. Viability is an empirical organizational property that must be tested over time in relation to an environment.
