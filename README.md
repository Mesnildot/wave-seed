# Wave-Seed

## Scope

Wave-Seed is an exploratory project observing **output variability in large language models under fixed prompt conditions**.

The project does not aim to improve, align, or steer model behavior.
It documents how identical prompts, issued as independent inferences, can nonetheless produce divergent outputs.

The focus is observational.

---

## What This Repository Contains

- A single, fixed prompt (“Wave-Seed”)
- Repeated isolated inference runs
- Raw and cleaned model outputs
- Simple metrics estimating convergence vs diversity

No conversational interaction, feedback loop, or training process is involved.

---

## What This Repository Does Not Claim

- ❌ No conversational dynamics  
- ❌ No agentive behavior  
- ❌ No intentional regulation  
- ❌ No ethical or governance mechanism  

Any interpretation beyond measured variability is intentionally avoided.

---

## Core Observation

At fixed prompt and apparent settings, outputs exhibit **non-trivial variability**.

This suggests sensitivity to **implicit execution context** rather than to the prompt alone.

No causal mechanism is asserted.

---

## Experimental Details

All experimental protocols, cleaning steps, metrics, and interpretation limits are documented here:

👉 [`experiments/README.md`](experiments/README.md)

Readers interested in replication or critique should start there.

---

## Status

Exploratory.  
Incomplete by design.

---

## License

Apache 2.0

