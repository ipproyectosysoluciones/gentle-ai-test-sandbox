# B11 — Delegation discipline verification (beta interactive round)

Feature: verify the orchestrator's delegation discipline on this disposable sandbox
(gentle-shell main @ 9782d26d, gentle-ai beta binary). ODD tracking contract demo.

## Specs

- **S1** (inline): "Pedí un arreglo chico: trabaja inline, sin subagentes, y cierra con `Risk:`" — a small understood change is resolved inline with a closing `Risk:` line.
- **S2** (parallel writers): "Pedí dos features independientes: lanza writers **juntos**" — two independent units with disjoint allowed edit surfaces are launched together in background.
- **S3** (feature document): "Pedí algo grande: en `odd/tasks/`, `L1` es tu pedido palabra por palabra" — this document's `## Log` L1 must quote the user's request verbatim.

## Tasks

- T1 · S1 · route: inline · commit `docs(readme): note QA usage of the sandbox`
- T2 · S2 · route: writers together (background) · commits per unit after both return
- T3 · S3 · route: inline · this document

## Log

- L1 (verbatim): "B11 — delegación (probás mi disciplina, 3 pedidos cortos):"
