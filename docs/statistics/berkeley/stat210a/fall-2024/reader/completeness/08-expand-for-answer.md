---
title: Expand for answer
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/completeness.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/completeness.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Expand for answer

**Source:** [`reader/completeness.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/completeness.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Consider the model $\cP$ with *known* $\sigma^2 > 0$ and unknown $\mu\in \RR$. This $\cP$ is a one-parameter full-rank exponential family with complete sufficient statistic $\overline{X}$. Moreover, $S^2$ is ancillary, since we can write
$$
S^2 = \sum_{i=1}^n (Z_i - \overline{Z})^2, \quad \text{ for } Z_i = X_i - \mu.
$$
Because the distribution of $Z_1,\ldots,Z_n \simiid N(0,\sigma^2)$ is known, it follows that the distribution of $S^2$ is known as well (specifically, $S^2/\sigma^2$ is a $\chi^2$ random variable with $n-1$ degrees of freedom). Since $\mu$ is the only unknown parameter, $S^2$ is therefore ancillary in $\cP$. Applying Basu's theorem, we have $\overline{X} \indep S^2$ for any $\mu \in \RR$. But $\sigma^2$ was arbitrary, so we have the result for all $\mu$ and $\sigma^2$.

:::

---

[← Basu's Theorem](07-basu-s-theorem.md) · [Up: contents](index.md)
