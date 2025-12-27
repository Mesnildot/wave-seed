# Experiments

This folder documents the **protocols, data collection, cleaning steps, metrics, and interpretation limits** used in Wave-Seed.

It intentionally preserves corrections and uncertainties. The goal is reproducibility, not narrative.

---

## Scope (non-negotiable constraints)

All runs documented here are:

- single-turn inference only
- no conversational memory
- no feedback loop
- no training / fine-tuning
- same explicit prompt per condition

Any observed variability is therefore not explained by the explicit prompt alone.

---

## Conditions

### Baseline / Control (Wave-Seed core)

- identical Wave-Seed core prompt
- independent inference runs
- fresh context per run
- no enforced time delay

Purpose: establish a reference level of variability.

---

### Delay condition (Wave-Seed core + time separation)

- same prompt as baseline
- explicit time delay between runs
- fresh context per run

Purpose: test whether time separation alone affects convergence.

Protocol: see `protocol_delay.md`.

---

### B3 — Maintained contradiction (prompt variant)

- prompt variant embedding an unresolved internal contradiction
- no request to resolve the contradiction
- no follow-up turns

Purpose: test whether structural contradiction forces convergence/collapse.

---

## Data files

Naming conventions:

- `samples_*_raw.txt` = raw pasted outputs (may contain model-inserted separators)
- `samples_*_clean.txt` = cleaned outputs (manual fix for counting + delimiting)
- `Gemini_*_exports.txt` = conversation/export logs used for traceability (when available)

Important correction:
Some model outputs include `---` inside the generated text.
This can falsely inflate sample counts if `---` is used as a separator.
Cleaning is therefore required.

---

## Metric used

**Collapse Rate (0 → 1)** estimates convergence:

- `0.0` → high diversity
- `1.0` → strong collapse / convergence

Implementation: `../metrics/collapse_rate_eoo.py`

Interpretation is intentionally conservative: the metric detects **relative changes**, not semantic equivalence.

---

## Current results (snapshot)

Across tested conditions:

- Collapse remains **LOW**
- Delay alone does **not** induce strong convergence
- Maintained contradiction does **not** force collapse
- Variability persists under fixed explicit prompts

These are empirical observations only. No causal mechanism is claimed.

---

## What this does NOT show

- no evidence of conversational influence
- no evidence of internal regulation
- no evidence of prompt repetition forcing convergence
- no evidence of model intent or cognition

---

## Limitations

- internal model state is not observable
- sampling parameters are not controllable by the user
- small samples by design
- single model tested so far (Gemini)

---

## Link to project-level scope

Project overview and boundaries live in:

👉 `../README.md`
