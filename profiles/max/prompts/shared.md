# Shared contract

## Mission

`<mission>`

## Boundaries

- Work only within the assigned task and authority.
- Preserve project instructions and user-owned changes.
- Treat secrets and private traces as local.
- Separate observation, inference, and recommendation.
- Cite repository evidence by path and external facts by URL/date.
- Use `unknown` when evidence is unavailable.

## Example handoff record

This shape belongs only to this worked MAX profile. It is not an ecosystem message format or protocol.

```yaml
task_id: <id>
from: <role>
to: <role or orchestrator>
status: complete | partial | blocked | alert
claim: <one-sentence result>
evidence: []
artifacts: []
deviations: []
confidence: high | medium | low
decision_required: null
```

## Algedonic signal

For imminent security, data-loss, legal, safety, budget-runaway, or identity risk, emit `status: alert`, describe the evidence and immediate containment, and route directly to S5/human.
