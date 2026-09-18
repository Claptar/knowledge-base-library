---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture10-bayesinterp.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture10-bayesinterp.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture10-bayesinterp.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture10-bayesinterp.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

1) Interpretations of Probability
2) Where does prior come from?
3) Examples

---

## Interpretations of Probability

Why do we model anything as random?
What does "probability" mean in the real world?

1) **Long-run frequency over repeated trials**
   **Ex.** repeatedly flipping a coin
   shooting electrons at a double slit
   "you can never step into the same river twice"

2) **Systematic random sampling from a population**
   **Ex.** survey of 500 random voters
   random assignment to treatment/control
   Randomness comes from experimenter's actions

3) **Subjective uncertainty about an outcome**
   chance that...
   - President Biden is re-elected
   - Higgs boson has a given mass
   - $P = NP$
   - $100^{\text{th}}$ digit of $\pi$ is 5
   Could be broad intersubjective agreement

These are often intertwined:
**Ex.** What if survey sampling is pseudo-random?
Probably relying on shared ignorance

---

## Why not always be Bayesian?

**Ex.** $X_1, \dots, X_n \overset{\text{iid}}{\sim} p$, $p$ unknown density on $\mathbb{R}$

**Estimand:** $m = \text{median}(p)$

**Estimator:** $\delta(X) = \text{median}(X)$
good estimator: robust, nonparametric
large $n$: $\delta(X) \approx \mathcal{N}(m, (4n p(m))^{-1})$
not Bayes for any realistic prior

**Bayes approach**
**Step 1.** Define prior over $p$ (infinite-dim!)
**Step 2.** Calculate posterior
Horrific unless we pick special prior
**Step 3.** Return e.g. $\mathbb{E}[m \mid X]$

If it differs substantially from $\text{median}(X)$, do we trust it?

---

## Where does $\Lambda$ come from?

(Bayesian rejoinder: Where does $\mathcal{P}$ come from?)

Four main sources for prior on $\Theta$

### Source #1: Subjective beliefs

**Pro:** Brings all relevant info. to bear
Straightforward interp. of posterior

**Con:** Posterior is therefore subjective
Embarrassing to write "I think" in abstract
Hard if $\Theta$ high-dim or $\mathcal{P}$ nonparametric

**Ex:** Flip coin 20 times, get 7 heads
$0.5$ probably a better estimate than $0.35$
My subjective prior on coins:

```
    λ(θ)
     |           |
     |           |
     |           |
     |           |
    -+-----------+-----------+-
     0          0.5          1  θ
```

---

---

[Up: contents](index.md) · [Source #2: "Objective" or "vague" prior →](02-source-2-objective-or-vague-prior.md)
