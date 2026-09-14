---
title: Part a.
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/problem-sets/ps5.md
source_file: sources/berkeley-stat158/spring-2026/problem-sets/ps5.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Part a.

**Source:** [`problem-sets/ps5.md`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/problem-sets/ps5.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

Under CRD, $\hat{\tau}_{CRD} = \bar{Y}_A - \bar{Y}_B$ where $\bar{Y}_A = \frac{1}{n}\sum_{i \in A} Y_i(A)$ and $\bar{Y}_B = \frac{1}{n}\sum_{i \in B} Y_i(B)$.

Since subjects in group $A$ are different from subjects in group $B$ (between-subjects comparison), the two group means are independent. Each individual observation has variance $\sigma_s^2 + \sigma_\varepsilon^2$, so:

$$
\text{Var}(\bar{Y}_A) = \frac{\sigma_s^2 + \sigma_\varepsilon^2}{n}, \quad \text{Var}(\bar{Y}_B) = \frac{\sigma_s^2 + \sigma_\varepsilon^2}{n}
$$

$$
\text{Var}(\hat{\tau}_{CRD}) = \text{Var}(\bar{Y}_A) + \text{Var}(\bar{Y}_B) = \frac{2(\sigma_s^2 + \sigma_\varepsilon^2)}{n}
$$

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Part b. →](03-part-b.md)
