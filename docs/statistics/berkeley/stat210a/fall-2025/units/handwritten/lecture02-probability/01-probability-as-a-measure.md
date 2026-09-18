---
title: Probability as a measure
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/handwritten/lecture02-probability.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/handwritten/lecture02-probability.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/handwritten/lecture02-probability.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/handwritten/lecture02-probability.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Probability as a measure

### Outline

1) What is a probability?
2) Measures and integrals
3) Densities
4) Probability spaces

---

## What is probability?

**Two common answers:**

1) **Frequentist answer**: Relative frequency over many repetitions of a given experiment.
2) **Bayesian answer**: Degree of belief that something is true, or will happen.

Many disagreements, e.g. about what kinds of things we can meaningfully assign prob. to.

- Prob. (Die roll lands on 4)
- Prob. (Surgery is successful)
- Prob. (Harris wins upcoming election)
- Prob. (Subatomic particle has predicted mass)
- Prob. ($P = NP$)
- Prob. ($20^{\text{th}}$ digit of $\sqrt{2}$ is 5)

Bayesians get mileage by putting probs on everything.

Frequentists try to avoid this.

Many controversies about this!

---

## Mathematical Probability

Fortunately, these disagreements don't extend to the mathematical construct of probability

**Mathematical answer**: A function $P$ mapping (some) subsets of a sample space $\mathcal{X}$ to $[0, 1]$, which is additive over disjoint sets:
$$P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i) \quad \text{if } A_i \cap A_j = \emptyset, \text{ all } i \neq j$$
and has $P(\mathcal{X}) = 1$

Originally invented to analyze games of chance
Classical theory for discrete events defined by Laplace

Problems remained for continuous variables, e.g.
- treatment of pathological sets
- conditioning on probability zero events

Kolmogorov (1933) recognized:
- probability is a special case of a **measure**,
- expectation is an **integral** against a prob. measure

---

---

[Up: contents](index.md) · [Measure theory basics →](02-measure-theory-basics.md)
