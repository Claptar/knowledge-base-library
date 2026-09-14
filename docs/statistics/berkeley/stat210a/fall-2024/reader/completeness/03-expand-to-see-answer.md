---
title: Expand to see answer
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/completeness.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/completeness.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Expand to see answer

**Source:** [`reader/completeness.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/completeness.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

**No, $S(X)$ is not complete.**

Both the sample median $\text{Med}(S)$ (as defined in Homework 2 Problem XX) and sample mean $\overline{X}(S)$ can be calculated using $S(X)$ alone, and both are unbiased estimators for $\theta$. Hence $f(S) = \text{Med}(S) - \overline{X}(S)$ has expectation zero, but is not almost surely equal to zero because the median and mean are not equal to each other.

:::


**Example 1 (Uniform scale family)**: Let $X_1, \ldots, X_n \simiid U[0, \theta]$, for $\theta > 0$. We showed previously that the maximum $T(X) = X_{(n)}$ is minimal sufficient. Is it complete?

!!! important "Important"

---

[← Completeness](02-completeness.md) · [Up: contents](index.md) · [Expand to see answer →](04-expand-to-see-answer.md)
