---
title: Flexibility of Bayes
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture10-bayesinterp.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture10-bayesinterp.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture10-bayesinterp.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture10-bayesinterp.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Flexibility of Bayes

Any $\Lambda$, $\mathcal{P}$, $L$, $g(\theta)$: $\delta_\Lambda$ defined straightforwardly

$$
\delta_\Lambda(x) = \operatorname{argmin}_d \int L(\theta, d) \lambda(\theta \mid x) \, d\theta
$$

Problem reduced to (possibly hard) computation
Posterior is "one stop shop" for all answers

No need for:
- special family structure (exp. fam. / complete s.s.)
- special estimator ($U$-estimable)
- convex or nice $L$

$\Rightarrow$ Highly expressive modeling & estimation

**Caveat**: Limited by ability to do computations
(Topic of next lecture)

## Source #4: Convenience Priors

Choosing conjugate or other "nice" priors
$\rightsquigarrow$ much faster computations esp. in high-dim.
(But what does the posterior mean?)

---

**Ex**. $X_1, \dots, X_n \overset{\text{iid}}{\sim} p$, $p$ unknown density on $\mathbb{R}$

**Estimand**: $m = \text{median}(p)$

**Estimator** $\delta(X) = \text{median}(X)$
good estimator: robust, nonparametric
large $n$: $\delta(X) \approx N(m, (4n p(m))^{-1})$
not Bayes for any realistic prior

**Bayes approach**
**Step 1**. Define prior over $p$ (infinite-dim!)
**Step 2**. Calculate posterior
Horrific unless we pick special prior
**Step 3**. Return e.g. $\mathbb{E}[m \mid X]$

If it differs substantially from $\text{median}(X)$, do we trust it?

---

---

[← Gaussian sequence model](02-gaussian-sequence-model.md) · [Up: contents](index.md) · [Gaussian Hierarchical Model →](04-gaussian-hierarchical-model.md)
