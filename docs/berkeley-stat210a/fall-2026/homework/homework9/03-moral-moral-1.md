---
title: 'Moral: {#moral-1}'
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework9.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework9.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral-1}

**Source:** [`homework/homework9.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework9.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

The $t$-test of $\mu=0$ that we are familiar with can be derived from the theory of UMPU conditional testing, but we need to additionally use the location family structure to get a conditional interval.

**Problem 3** (McNemar’s test). Suppose we have paired binary data: for $i=1,\ldots,n$ we observe $(X_i,Y_i)\in \{0,1\}^2$. The pairs are i.i.d. with $$\mathbb{P}\left[(X_i,Y_i) = (a,b)\right] = \pi_{a,b} \quad a,b\in \{0,1\}.$$ This model could describe the performance of two prediction models on a test set, where $X_i$ and $Y_i$ represent respectively whether each model gets the $i$th prediction right. Or it could represent binary outcomes in a matched-pairs clinical trial, where similar patients are matched into pairs and then within each pair a coin is flipped to see who gets the treatment and who gets the placebo.

Write $\pi_X = \mathbb{P}(X_i=1) = \pi_{1,0}+\pi_{1,1}$ and $\pi_Y = \mathbb{P}(Y_i=1) = \pi_{0,1}+\pi_{1,1}$, and let $N_{a,b} = \sum_{i=1}^n 1\{X_i=a,Y_i=b\}$.

1.  Find the UMPU test of $H_0:\; \pi_X \leq \pi_Y$ vs. $H_1:\; \pi_X > \pi_Y$, giving the cutoffs $c(u), \gamma(u)$ in terms of solutions to integral equalities for a binomial distribution. (Hint: it may help to first reframe the hypothesis in terms of the $\pi_{a,b}$ parameters.)

2.  Suppose $N_{0,0} = N_{1,1} = 1000$, $N_{0,1} = 5$ and $N_{1,0}=25$. Compute $95\%$ confidence intervals for $\pi_X$ and $\pi_Y$ (invert the two-sided equal-tailed test but without randomizing). Then compute a $p$-value for $H_0:\; \pi_X\leq\pi_Y$ (do not randomize). Does anything about the respective answers surprise you?

(Note: This test is called McNemar’s test; it is very useful for clinical trials with matched pairs of subjects, and also for comparing the performance of different classifiers on a held-out sample.)

---

[← Moral: {#moral}](02-moral-moral.md) · [Up: contents](index.md) · [Moral: {#moral-2} →](04-moral-moral-2.md)
