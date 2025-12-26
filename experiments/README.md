# Wave-Seed  
**Measuring Output Variability Under Fixed Prompt Conditions**

---

## Overview

**Wave-Seed** is an exploratory experimental framework designed to measure **output variability** in large language models when the **explicit prompt is held constant**.

The project investigates whether identical prompts, issued as isolated inferences, produce convergent or divergent outputs — and what this reveals about **implicit contextual sensitivity** in generative systems.

This repository prioritizes **methodological transparency**, **reproducibility**, and **negative results**.

---

## What This Project Is

- A **prompt-controlled experimental setup**
- A collection of **raw and cleaned model outputs**
- A simple, transparent **diversity / collapse metric**
- A record of **failed, partial, and exploratory hypotheses**

---

## What This Project Is NOT

- ❌ Not a benchmark  
- ❌ Not a conversational or memory experiment  
- ❌ Not a performance evaluation  
- ❌ Not a claim about model cognition or intent  

Each run consists of a **single, isolated inference**.  
No feedback, no dialogue, no learning loop is involved.

---

## Core Question

> **Do identical prompts, issued as independent inferences, converge toward similar outputs — or do they remain diverse?**

If diversity persists, the variability must originate from **implicit system-level or contextual factors**, not from the prompt itself.

---

## Experimental Conditions

All experiments share the same **Wave-Seed core prompt**, with variations only in **external conditions**:

- **Baseline / Control**  
  Identical prompt, independent runs

- **Delay condition**  
  Same prompt, time delay between runs

- **B3 – Maintained contradiction**  
  Prompt variant embedding an unresolved internal contradiction

No conversational turns are used in any condition.

---

## Metrics

### Collapse Rate (0 → 1)

A simple metric estimating **output convergence**:

- `0.0` → high diversity  
- `1.0` → strong collapse / convergence  

Implemented in:

# Wave-Seed  
**Measuring Output Variability Under Fixed Prompt Conditions**

---

## Overview

**Wave-Seed** is an exploratory experimental framework designed to measure **output variability** in large language models when the **explicit prompt is held constant**.

The project investigates whether identical prompts, issued as isolated inferences, produce convergent or divergent outputs — and what this reveals about **implicit contextual sensitivity** in generative systems.

This repository prioritizes **methodological transparency**, **reproducibility**, and **negative results**.

---

## What This Project Is

- A **prompt-controlled experimental setup**
- A collection of **raw and cleaned model outputs**
- A simple, transparent **diversity / collapse metric**
- A record of **failed, partial, and exploratory hypotheses**

---

## What This Project Is NOT

- ❌ Not a benchmark  
- ❌ Not a conversational or memory experiment  
- ❌ Not a performance evaluation  
- ❌ Not a claim about model cognition or intent  

Each run consists of a **single, isolated inference**.  
No feedback, no dialogue, no learning loop is involved.

---

## Core Question

> **Do identical prompts, issued as independent inferences, converge toward similar outputs — or do they remain diverse?**

If diversity persists, the variability must originate from **implicit system-level or contextual factors**, not from the prompt itself.

---

## Experimental Conditions

All experiments share the same **Wave-Seed core prompt**, with variations only in **external conditions**:

- **Baseline / Control**  
  Identical prompt, independent runs

- **Delay condition**  
  Same prompt, time delay between runs

- **B3 – Maintained contradiction**  
  Prompt variant embedding an unresolved internal contradiction

No conversational turns are used in any condition.

---

## Metrics

### Collapse Rate (0 → 1)

A simple metric estimating **output convergence**:

- `0.0` → high diversity  
- `1.0` → strong collapse / convergence  

Implemented in:metrics/collapse_rate_eoo.py

Interpretation is intentionally conservative.

---

## Key Observations (Current State)

- Collapse remains **LOW** across all tested conditions
- Time delay alone does **not** produce meaningful convergence
- Maintained contradiction does **not** force collapse
- Variability persists despite fixed prompts

👉 This falsifies the hypothesis that **prompt repetition alone** induces convergence.

---

## What Is Actually Observed

The data suggests sensitivity to **implicit context**, potentially including:

- session or account state
- internal initialization noise
- system-level framing not exposed to the user

These factors are **not directly observable**, but their effects are measurable.

---

## Repository Structure

wave-seed/
├── README.md
├── LICENSE
├── analysis/
│ └── RESULTS_SUMMARY.md
├── experiments/
│ ├── README.md
│ ├── protocol_delay.md
│ ├── samples_raw.txt
│ ├── samplesclean.txt
│ └── Gemini*_exports.txt
├── metrics/
│ └── collapse_rate_eoo.py
├── prompts/
│ ├── wave_seed_core.md
│ ├── wave_seed_B3_contradiction.md
│ └── variants.md


---

## Methodological Position

This project embraces:

- incomplete results
- null effects
- hypothesis revision

**Not concluding** is considered a valid and valuable outcome.

---

## Current Limitations

- No control over internal model state
- No access to system-level randomness parameters
- Small sample sizes (by design)

---

## Next Possible Directions

- Controlled session reuse vs fresh sessions
- Minimal two-turn interaction tests
- Cross-model comparison under identical protocol

These are **not yet implemented**.

---

## License

Apache 2.0 — see `LICENSE`.

---

## Citation

If you reference this work: Wave-Seed Project.
Measuring Output Variability Under Fixed Prompt Conditions.
GitHub repository.

A `CITATION.cff` file is provided.

---

### Final note

This repository documents **what happened**, not what we hoped would happen.

That is the point.
