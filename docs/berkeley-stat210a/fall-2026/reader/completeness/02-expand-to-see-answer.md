---
title: Expand to see answer
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/completeness.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/completeness.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Expand to see answer

**Source:** [`reader/completeness.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/completeness.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

**No, $S(X)$ is not complete.**

One simple way to see this is that $X_{(n)}-X_{(1)}$ has the same distribution for every $\theta$, because we can write $X_i = \theta + Z_i$ for $Z_1,\ldots,Z_n \simiid \text{Lap}(0)$ and then $X_{(n)}-X_{(1)} = Z_{(n)}-Z_{(1)}$.

Another evocative counterexample is that both the sample median $\text{Med}(X)$ and sample mean $\overline{X}$ can be calculated using $S(X)$ alone, and both are unbiased estimators for $\theta$ (since the distribution is symmetric for $\theta=0$ and $\text{Med}(X) = \theta + \text{Med}(Z)$). Hence $f(S) = \text{Med}(X) - \overline{X}$ has expectation zero, but is not almost surely equal to zero because the median and mean are a.s. unequal for $n>2$.

:::


**Example 1 (Uniform scale family)**: Let $X_1, \ldots, X_n \simiid U[0, \theta]$, for $\theta > 0$. We showed previously that the maximum $T(X) = X_{(n)}$ is minimal sufficient. Is it complete?

!!! important "Important"

---

[← Completeness](01-completeness.md) · [Up: contents](index.md) · [Expand to see answer →](03-expand-to-see-answer.md)
