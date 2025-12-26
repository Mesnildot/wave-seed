\# Wave-Seed – Experimental Summary (Gemini)



\## Protocol

\- Same Wave-Seed core prompt

\- Multiple conversations treated as independent conditions

\- Outputs cleaned using separator: <<<END\_OF\_OUTPUT>>>

\- CollapseRate computed with collapse\_rate\_eoo.py



\## Results (N≈19)



| Condition | CollapseRate |

|---------|---------------|

| Control (Wave-Seed, conversation A) | 0.104 |

| Delay (Wave-Seed + temporal friction) | 0.124 |

| B3 (Contradiction maintained) | 0.145 |

| Baseline (Wave-Seed, conversation B) | 0.235 |



\## Key Observation

Despite identical prompts, baseline and control show large divergence.

This indicates that \*\*conversation state acts as a hidden variable\*\* affecting convergence.



\## Interpretation

\- Prompt alone is not the unit of regulation

\- Temporal structure and interaction history modulate collapse

\- Wave-Seed behaves as an interaction protocol, not a static text



\## Conclusion

Regulation emerges from coupling (human ↔ model ↔ time), not from content alone.



