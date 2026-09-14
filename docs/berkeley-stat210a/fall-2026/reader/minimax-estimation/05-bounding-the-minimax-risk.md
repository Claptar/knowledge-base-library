---
title: Bounding the minimax risk
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/minimax-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/minimax-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Bounding the minimax risk

**Source:** [`reader/minimax-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/minimax-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Outside of simple examples, it's often difficult to find minimax estimators in finite samples, but minimax bounds are very commonly used in statistical theory to characterize the hardness of a problem.

### Application 1: near-optimal estimators.
As one application, we might exhibit an estimator that has other nice properties such as ease of calculation, unbiasedness, an appealing functional form, or a natural inductive bias that we expect to make it perform well in certain settings of interest. It is also nice if we can show that the estimator is not far from minimax optimal.

We can do this by calculating our estimator's sup-risk and comparing it to the Bayes risk of any Bayes estimator. If (say) the former is only $10\%$ greater than the latter, then we can say our estimator is within $10\%$ of minimax optimality.

### Application 2: Problem Hardness.
Another common application of minimaxity is to quantify the difficulty of a problem in some asymptotic regime; i.e. the hardness of a sequence of problems indexed by an asymptotic parameter $n$ (commonly the sample size). If we can find an upper bound by calculating or bounding the sup-risk of an estimator $\delta_n$, and also a lower bound by calculating or bounding the Bayes risk for a prior $\Lambda_n$, then we can sandwich the minimax risk $r_n^*$ as
$$
r_{\Lambda_n} \leq r_n^* \leq \sup_\theta R_n(\theta; \delta_n).
$$
If the upper and lower bounds shrink (or grow) at the same rate in $n$, then $r_n^*$ must also shrink (or grow) at that rate. This rate is called the problem's **minimax rate**.

A caveat for this approach is that calculating a problem's minimax risk may inappropriately focus attention on a small corner of the parameter space where the problem is especially hard. It's possible that it matters more what is happening elsewhere.


Caveat: A problem might be easy throughout most of parameter space but very hard in some bizarre corner we never encounter in practice.

---

[← Least Favorable Sequence](04-least-favorable-sequence.md) · [Up: contents](index.md)
