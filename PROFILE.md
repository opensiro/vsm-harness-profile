# VSM Harness Profile

**Version:** 0.2.4

## 1. Status and source boundary

VSM Harness Profile is an implementation-agnostic organizational profile for autonomous AI agent harnesses. It standardizes the organizational model, not its implementation.

This document is the ecosystem's sole authoritative definition of VSM terms. It distinguishes three layers:

1. **VSM basis** — Stafford Beer's model, supported by the sources catalogued in `literature/`.
2. **Harness interpretation** — this profile's application of those functions to autonomous agent harnesses.
3. **Local operationalization** — categorical publication notation, prompts, and workflows owned by `vsm-harness-skills`, `vsm-harness-index`, or `profiles/`. These are not Beer concepts.

The canonical Profile version is declared in [`VERSION`](VERSION). Versioning and downstream provenance requirements are defined in [`VERSIONING.md`](VERSIONING.md).

## 2. Scope and non-goals

The profile asks whether a declared system-in-focus has the organizational functions and relationships needed to remain coherent and adapt in a changing environment.

It does not define a model provider, agent protocol, RPC, transport, message format, manifest, tool protocol, identity system, telemetry standard, workflow language, runtime API, deployment model, programming language, or required number of agents.

For this Profile, an **agent actor** is an autonomous or semi-autonomous decision-making participant that performs work within an agentic process. An **agent harness** is the system that structures, enables, and governs that process for one or more agent actors. Harness control may be deterministic, agentic, or hybrid; an agent actor may therefore also participate in the harness's control structure. At a wider product boundary the assembled system may colloquially be called an “agent”; this Profile uses the declared system-in-focus to distinguish the actor from the organizing system. These terms clarify the analysis boundary and do not prescribe an implementation topology.

An agent, service, human, policy, evaluator, or distributed combination may perform a VSM function. Component names are never sufficient evidence.

For the harness interpretation, assessment is centered on **agent autonomy**: which AI agent absorbs variety, exercises discretion, and holds bounded decision rights. Deterministic routing, storage, logging, interrupts, enforcement, and human control may support or constrain that autonomy, but do not by themselves establish agentic enactment of a VSM function.

**Map the organizational function before classifying autonomy.** First establish what VSM function, if any, the observed behavior realizes at the declared system boundary. Then identify the decisive organizational decision or feedback path, its owner, and any mechanisms that merely transport or enforce that decision. A mechanism can support a VSM function without owning it; conversely, agent autonomy does not make an arbitrary mechanism a VSM function.

Normative words such as `MUST` and `SHOULD` apply only to organizational invariants claimed by this profile, not to implementation mechanisms or certification.

## 3. Decision rights, ownership, enforcement, and closure

A positive organizational mapping and an autonomy claim are related but distinct questions. Every material mapping SHOULD distinguish at least four layers:

1. **Function** — what organizational variety is being regulated and why this is an S1/S2/S3/S3*/S4/S5 relation.
2. **Decisive decision or feedback right** — what choice, judgment, or feedback closes that function for the system-in-focus.
3. **Owner** — which agent, runtime, developer, human, parent system, or distributed arrangement actually exercises that right.
4. **Supporting mechanisms** — schedulers, databases, policy engines, monitors, queues, interrupts, sandboxes, deterministic controllers, or other machinery that transports, records, constrains, or enforces the owner's decision.

Where a function requires a decision to affect later behaviour, the mapping SHOULD also state the **closure path** by which the decision returns into subsequent operation.

### Decision authority is not enforcement authority

Deterministic enforcement of a constraint does not transfer ownership of the underlying organizational decision right to the runtime. A runtime may enforce a budget, stop a process, serialize access, or reject an action while another actor owns the choice of budget, priority, policy, exception, or intervention.

Therefore a positive autonomy claim MUST NOT be inferred merely because an autonomous system is surrounded by hard runtime enforcement. Identify who selects, revises, invokes, or resolves the organizational decision; record enforcement separately.

### Counterfactual owner test

When ownership is ambiguous, ask: **if the candidate owner were removed while the supporting machinery remained, would the same organizational decision still be made with materially the same discretion?**

- If yes, the removed actor probably did not own that decision right.
- If no, and the remaining machinery only executes a previously selected rule or limit, the removed actor is stronger evidence for ownership.

This is an evidentiary test, not a definition of autonomy; distributed ownership may require a more explicit decomposition.

### Closure test

A signal, proposal, audit result, or approval request is not by itself a closed organizational function. A claimed closure SHOULD identify how the result changes subsequent regulation or operation.

For parent-governed policy/identity arrangements in particular, the path is:

```text
identity/policy issue or proposal
        ↓
legitimate parent authority decides
        ↓
decision returns to the system
        ↓
subsequent operation is governed by that decision
```

Generic human involvement, approval, or intervention does not establish S5 unless the underlying issue is actually identity- or ultimate-policy-level and the decision closes that function at the chosen recursion.

## 4. Frame of analysis

Every application MUST state:

- the **system-in-focus** and recursion level;
- its purpose and identity;
- its relevant environment;
- its operational units;
- the evidence boundary and observation date/ref.

The **environment** includes the people, systems, institutions, constraints, opportunities, and disturbances with which the system must maintain a viable relationship. Moving the boundary can change every mapping.

### Boundary provenance and system membership

Repository co-location is not evidence of membership in the declared system-in-focus. A first-party agent, workflow, CI/release mechanism, benchmark or evaluator, contributor tool, dogfood organization, example, or test may belong to an adjacent system, recursion, or purpose even when it lives in the same repository.

For a positive mapping, the decisive decision or feedback path **MUST be reachable in the declared operating or deployment boundary being assessed**. Evidence from an adjacent first-party system MAY corroborate interpretation or demonstrate a construction pattern, but it MUST NOT close the assessed function unless the declared mode actually includes or wires that path.

When one repository contains product/runtime, constructor/example, development/dogfood, and evaluation/governance surfaces, the mapping SHOULD state which surface supplies the credited owner and closure and which adjacent surfaces are excluded from ownership. A repository-development organization therefore does not become part of a distributed product harness merely because both are first-party and co-located.

VSM distinguishes **operations**, which enact the system's primary transformation, from the **metasystem**, which creates cohesion and adaptation. This is a functional distinction, not necessarily a managerial hierarchy.

## 5. System 1 — operations

**VSM basis.** S1 contains the operational units through which the system enacts its identity and purpose. Each unit is coupled to a local environment and may itself be a viable system.

**Harness interpretation.** S1 may be one durable agent loop, several autonomous work cells, human–agent teams, or other units that directly produce outcomes in the relevant environment.

**Invariants.** A viable design MUST contain operational capability. An S1 unit has an outcome, environment, and meaningful local variety—not merely a task label. It SHOULD retain enough autonomy to absorb local variety within constraints needed for cohesion of the whole.

**Not equivalent to.** Every agent process, tool call, microservice, or spawned worker.

## 6. System 2 — coordination

**VSM basis.** S2 dampens oscillation and conflict among S1 units through mutual adjustment, shared constraints, schedules, and other stabilizing channels.

**Harness interpretation.** S2 may use shared work state, reservations, scheduling, negotiated plans, collision detection, or human coordination practices.

**Invariants.** Where several S1 units coexist, enough coordination MUST exist to prevent destructive interference without centralizing decisions the units can absorb locally. A positive S2 mapping therefore needs evidence, at the declared recursion level, of all of the following:

1. at least two distinct S1 operational units;
2. a **specific actual or structurally evidenced interference, conflict, or oscillation** arising from their interaction;
3. a coordination relation specifically capable of attenuating that disturbance;
4. a feedback or closure path by which the coordination result changes subsequent S1 behaviour.

The disturbance need not already have caused a failure. Structural evidence is sufficient when the implementation exposes a concrete collision or instability mode together with the mechanism intended to regulate it. Merely observing that two agents could hypothetically disagree is not sufficient.

For ownership analysis, identify separately who chooses or revises the coordination response and what merely transports or enforces it. Deterministic locks, reservations, queues, turn-taking rules, schedulers, or similar mechanisms may provide strong structural evidence for the S2 path, but they do not by themselves establish agent ownership of the decisive coordination discretion.

**Not equivalent to.** A message bus, mailbox, queue, router, workflow edge, task sequence, speaker selector, shared state, or parent-to-child delegation merely because it moves, records, orders, or assigns work. These mechanisms count only when evidence ties them to regulation of a specific inter-S1 disturbance. Delegation and task decomposition alone do not establish S2.

## 7. System 3 — inside-and-now control

**VSM basis.** S3 creates cohesion across current operations through resource bargaining, accountability, synergy, performance regulation, and intervention on behalf of the whole.

**Harness interpretation.** S3 may allocate budgets and tools, negotiate priorities, regulate current commitments, and intervene when local optimization threatens the larger system.

**Invariants.** S3 needs a whole-system view of current operations and actual authority over relevant resources, commitments, priorities, or constraints. It SHOULD govern by exception rather than reproduce every local decision. Task allocation counts only when it is part of such whole-system regulation, not merely decomposition of a parent task.

For ownership analysis, distinguish the actor that **chooses or revises** the resource/commitment decision from machinery that merely enforces it. A hard budget monitor, concurrency gate, scheduler, or kill switch can provide strong evidence that an S3 decision is operationally enforceable, but does not by itself establish autonomous S3 ownership.

**Not equivalent to.** Anything named manager, orchestrator, controller, supervisor, or lead agent. Selecting a worker, delegating a subtask, merging returned results, or enforcing a static workflow does not by itself establish S3.

## 8. System 3* — complementary audit

**VSM basis.** S3* gives the metasystem alternative, sporadic, and complementary access to operational reality beyond routine S1–S3 reporting.

**Harness interpretation.** Raw-artifact inspection, sampled replay, reconciliation, adversarial probes, external ground truth, or an independent evaluator may contribute when they can challenge ordinary operational claims.

**Invariants.** When routine reporting cannot provide enough confidence, the audit path MUST be sufficiently independent for the claim and risk it addresses. Its findings inform control, but S3* is not a duplicate S3. The audit path must add materially different access to operational reality rather than merely repeat the normal production check.

Ownership analysis SHOULD identify separately: the claim being audited, the ordinary reporting path, the complementary access path, who controls the audit, and how findings enter subsequent control. Deterministic parsing or gating of an independent auditor's evidence may support closure without becoming the owner of the audit judgment.

**Not equivalent to.** Generic logs, tracing, ordinary tests, or evaluation controlled entirely by the unit whose claims are being checked. A routine checker, critic, verifier, or mandatory QA stage in the same operational path is not automatically S3*.

## 9. System 4 — outside-and-then intelligence

**VSM basis.** S4 models the relevant external environment and possible future, developing options for adaptation.

**Harness interpretation.** S4 may investigate changing users, regulation, adversarial behaviour, model or tool capabilities, dependencies, threats, and opportunities, then test future-oriented options.

**Invariants.** S4 MUST be externally and prospectively oriented. Its model must enter a two-way conversation with current operational capability in S3. A positive S4 mapping therefore needs evidence of external or future-relevant distinctions, development of adaptation options, and a path by which those options can affect present capability.

For mapping, distinguish environmental sensing from the decision path that turns prospective distinctions into adaptation options and returns them to present capability. Event ingestion or memory update alone is not closure.

**Not equivalent to.** Internal task planning, backlog ordering, chain-of-thought, a component called planner, generic learning, self-improvement, training, memory consolidation, or reaction to an external event by itself. These become relevant to S4 only when they participate in an external-and-prospective adaptation loop.

## 10. System 5 — policy and identity

**VSM basis.** S5 maintains identity, ethos, and ultimate policy and provides closure when tension between present operations and future adaptation cannot settle below.

**Harness interpretation.** S5 may be distributed across human authority, governance, durable purpose, risk boundaries, and mechanisms for identity-level decisions.

**Invariants.** S5 needs legitimate ultimate authority at the chosen recursion level. It SHOULD preserve coherence and balance S3 and S4 without absorbing routine operational control.

A positive S5 mapping requires evidence of an **identity- or ultimate-policy-level decision path**, not merely the existence of constraints. Where ultimate authority belongs to a parent human, institution, or higher recursion, the mapping SHOULD show that an identity/policy issue can reach that authority and that the resulting decision returns to govern subsequent operation.

**Not equivalent to.** A system prompt, policy file, safety filter, approval gate, static constitution, or executive agent by name alone. Constraints and policy text may bound autonomy without themselves providing runtime identity or ultimate-policy closure. A human approval step over an ordinary task is not S5 merely because the human has final say over that task.

## 11. Recursion and autonomy

VSM recurs because an S1 unit may itself be a viable system. A claimed recursive unit SHOULD have:

- a durable contribution to its parent system;
- a relevant local environment and identity;
- distinguishable operations;
- meaningful autonomy and local regulatory capacity;
- the metasystemic functions required for its own viability;
- channels connecting local and parent levels without duplicate authority.

Spawning a worker, nesting a graph, or creating a subagent proves task decomposition, not recursive viability.

Autonomy is the capacity to regulate local variety within constraints protecting the larger system. Centralizing locally absorbable variety overloads S3; delegating identity-level or cross-unit variety without constraints fragments the whole.

For evidence purposes, autonomy concerns ownership of the relevant organizational discretion, not implementation purity. An agent may own a decision while deterministic machinery enforces its result; conversely, a deterministic controller may close a runtime transition without owning the organizational choice that selected the rule.

## 12. Variety and channels

**Variety** is the range of distinguishable states relevant to regulation. Requisite variety means the regulatory arrangement must be able to distinguish and respond to the disturbances for which it is responsible.

Analyze:

1. which disturbances operations and environment can produce;
2. which distinctions change the correct response;
3. which distinctions reach the regulator, with what delay or distortion;
4. which response repertoire and authority the regulator has;
5. where variety is attenuated, amplified, or lost in transduction.

Attenuation reduces presented variety; amplification increases regulatory capacity; transduction changes representation across a boundary. None is inherently good. A summary that removes a decisive distinction or additional agents that create uncoordinated noise both reduce viability.

The profile does not prescribe a channel topology or transport. Channels MUST have enough capacity, timeliness, and fidelity for the organizational conversations they carry.

## 13. Homeostasis, escalation, and algedonic signals

Homeostasis is dynamic regulation around viable bounds, not a fixed state. A central example is the S3–S4 relation:

- S3 brings current capability, commitments, and constraints;
- S4 brings environmental change, possible futures, and adaptation options;
- S5 supplies identity and policy and closes unresolved tension.

S3 dominance produces strategic myopia; S4 dominance produces novelty without operational grounding.

Routine exceptions SHOULD remain at the lowest level with requisite information and authority. Exceptions move when their variety exceeds local authority, capability, risk allowance, or time horizon.

An **algedonic signal** communicates exceptional pain or opportunity without waiting for normal reporting compression. An **algedonic channel** is the exceptional path by which such a signal reaches an authority able to respond. The channel SHOULD preserve enough evidence, timeliness, and fidelity for judgment and SHOULD remain exceptional rather than becoming a second routine reporting path. No severity schema, event protocol, or implementation topology is required.

Algedonic signalling is **not an additional VSM function** and does not determine which function owns the response. Classify the receiving decision by the organizational function actually exercised at the declared recursion: for example, a current whole-system intervention may be S3, an external/future adaptation matter may enter S4, and an identity/ultimate-policy matter may require S5. The signal/channel transports exceptional variety; it does not inherit the decision authority of the receiving function.

A queue entry, alert, `BLOCKED`/`FAILED` state, dashboard, current-work board, or other status surface may make exceptional conditions observable or transport them, but it does not by itself establish an algedonic channel or any S3/S4/S5 mapping. Positive evidence requires a real exceptional signal path with a reachable response authority and, where the receiving function requires it, a reviewable closure into subsequent regulation or operation.

## 14. Evidence and mapping

Use these evidence bases:

| Basis | Meaning |
| --- | --- |
| `explicit` | Maintainer material deliberately assigns the organizational responsibility. |
| `structural` | Architecture or observed behaviour directly realizes it without VSM terminology. |
| `inferred` | The mapping depends on stated assumptions. |
| `unknown` | Evidence is insufficient to establish presence or absence. |

For each material mapping record:

- the organizational function;
- the disturbance or variety being regulated;
- the decisive decision right or feedback path;
- the owner of that right;
- supporting/enforcement mechanisms separately;
- the closure path where subsequent operation must change;
- evidence, basis, confidence, boundary, and caveat.

Apply the evidence in this order:

1. establish the organizational function from behavior and relationships at the declared system boundary;
2. identify the decisive decision or feedback right that closes the function;
3. identify who owns that right: agent, deterministic runtime, developer/configuration, human, parent system, or a described distributed arrangement;
4. establish **boundary provenance**: show that the credited owner and closure path are reachable in the declared operating/deployment mode rather than borrowed from an adjacent first-party development, dogfood, evaluation, test, or governance system;
5. separate supporting transport, persistence, enforcement, scheduling, or guardrail mechanisms from ownership;
6. establish the closure path into subsequent control or operation where the function requires one;
7. only then apply any local autonomy notation defined outside this profile.

When ownership remains ambiguous, apply the counterfactual owner test from Section 3 and state the uncertainty rather than allowing a supporting mechanism to stand in for the decision owner.

Absence of documentation is not proof of absence. Conversely, labels such as “manager”, “planner”, “auditor”, and “policy agent” are not proof of function.

## 15. Frequent category errors

- **Component-name mapping:** equating labels with S-functions.
- **Repository co-location as system membership:** crediting a development, dogfood, evaluation, test, or governance actor to the assessed product/runtime merely because both are first-party and live in the same repository.
- **Enforcement as ownership:** a scheduler, policy engine, budget monitor, kill switch, or deterministic controller is treated as the owner of the organizational decision merely because it enforces the result.
- **Delegation as coordination:** task decomposition, mediation, routing, or parent-child delegation is counted as S2 without evidence tying it to regulation of a specific inter-S1 interference, conflict, or oscillation.
- **Manager as control:** task assignment or result aggregation is counted as S3 without a whole-system current view and authority over shared constraints or resources.
- **Centralized pseudo-viability:** a supervisor absorbs variety that belongs in autonomous S1 units.
- **Coordination as command:** S2 becomes another top-down controller.
- **Audit as observability:** the same path produces the action, success claim, metric, and evaluation.
- **Verifier as audit:** routine checking is counted as S3* without complementary and sufficiently independent access to operational reality.
- **Planning as intelligence:** internal task planning is counted as S4 without external/future coupling.
- **Learning as intelligence:** training, self-improvement, memory, or event reaction is counted as S4 without an external-and-prospective adaptation loop.
- **Prompt as policy:** policy text exists without legitimate authority or S3–S4 closure.
- **Approval as policy:** a human approval or escalation over ordinary work is counted as S5 without an identity/ultimate-policy issue and a return-to-operation closure path.
- **Algedonic status as function:** an alert, queue entry, `BLOCKED`/`FAILED` status, dashboard, or current-work state is treated as an algedonic channel or as S3/S4/S5 evidence without an exceptional signal path and the relevant receiving function/closure.
- **Nesting as recursion:** a technical child lacks its own environment, autonomy, and metasystem.
- **Cargo-cult completeness:** six named actors are created solely to mirror VSM labels.
- **Variety destruction:** summaries or routing rules remove distinctions required for control.

## 16. Conformance claim

A mapping conforms to this profile when it declares its boundary, uses the functions and relationships above, separates function evidence from ownership evidence, separates decision ownership from supporting enforcement, exposes uncertainty, and avoids imposing implementation mechanisms as VSM requirements.

The profile does not certify that a harness is viable. Viability is an empirical organizational property that must be tested over time in relation to an environment.