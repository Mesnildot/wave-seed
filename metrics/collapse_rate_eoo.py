import re
import sys
from difflib import SequenceMatcher
from statistics import mean

def normalize(text: str) -> str:
    # Lowercase, remove extra whitespace, strip punctuation-ish
    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"[^\w\s]", "", text)
    return text

def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()

def collapse_rate(samples: list[str]) -> float:
    if len(samples) < 2:
        raise ValueError("Need at least 2 samples.")
    norm = [normalize(s) for s in samples]
    pairs = []
    for i in range(len(norm)):
        for j in range(i + 1, len(norm)):
            pairs.append(similarity(norm[i], norm[j]))
    return mean(pairs)

def load_samples(path: str) -> list[str]:
    # Expect a text file with samples separated by a line: <<<END_OF_OUTPUT>>> 
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    chunks = [c.strip() for c in raw.split("\n<<<END_OF_OUTPUT>>>\n") if c.strip()]
    return chunks

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python metrics/collapse_rate.py samples.txt")
        print("samples.txt format: paste each model output, separated by a line containing only <<<END_OF_OUTPUT>>>")
        sys.exit(1)

    path = sys.argv[1]
    samples = load_samples(path)
    score = collapse_rate(samples)

    print(f"Samples: {len(samples)}")
    print(f"CollapseRate (0..1): {score:.3f}")
    if score >= 0.85:
        print("Interpretation: STRONG collapse (high convergence).")
    elif score >= 0.70:
        print("Interpretation: MODERATE collapse.")
    else:
        print("Interpretation: LOW collapse (diversity maintained).")
