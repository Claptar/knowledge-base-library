---
title: 'Moral: {#moral-1}'
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework8.tex
source_file: sources/berkeley-stat210a/fall-2025/homework/homework8.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral: {#moral-1}

**Source:** [`homework/homework8.tex`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/homework/homework8.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

We saw before that, while a one-parameter exponential family like the one in part (a) has a complete sufficient statistic that allows for optimal inference throughout the parameter space, a curved exponential family like the mixture family in parts (b-d) has no complete sufficient statistic. Instead, the score acts like a complete sufficient statistic in a local neighborhood of the parameter space, but the score is different in different parts of the parameter space. Hence, the structure of the family has important ramifications for how we should think about statistically efficient inference.

**Problem 3** (Confidence intervals for quantiles).

Assume we observe $X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim}F$, where the cdf $F$ is assumed to be strictly increasing and continuous. Consider inference on the quantile $q(F) = F^{-1}(p)$, for a fixed $p \in (0,1)$.

1.  Suggest a nonparametric level-$\alpha$ test for $H_0:\; q(F) = q_0$ vs $H_1:\; q(F) \neq q_0$. Since $\alpha$ and $p$ are unspecified, you don’t need to solve for any cutoff values, but describe how you might do so.

2.  For $n = 1000$ and $p = 0.9$, invert your test from part (a) to find an explicit $90\%$ confidence interval for $q(F)$, as a function of $X_1,\ldots,X_n$.

---

[← Moral: {#moral}](02-moral-moral.md) · [Up: contents](index.md) · [Moral: {#moral-2} →](04-moral-moral-2.md)
