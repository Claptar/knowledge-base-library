---
title: Part b.
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/problem-sets/ps5.md
source_file: sources/berkeley-stat158/spring-2026/problem-sets/ps5.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Part b.

**Source:** [`problem-sets/ps5.md`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/problem-sets/ps5.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

Under CO, define $W_i = Y_i(A) - Y_i(B) = \tau + \varepsilon_{iA} - \varepsilon_{iB}$ for each subject. The subject effect $s_i$ cancels out. The estimator is $\hat{\tau}_{CO} = \bar{W} = \frac{1}{2n}\sum_{i=1}^{2n} W_i$.

Each $W_i$ has variance $\text{Var}(\varepsilon_{iA} - \varepsilon_{iB}) = 2\sigma_\varepsilon^2$ (since $\varepsilon_{iA}$ and $\varepsilon_{iB}$ are independent). Therefore:

$$
\text{Var}(\hat{\tau}_{CO}) = \frac{2\sigma_\varepsilon^2}{2n} = \frac{\sigma_\varepsilon^2}{n}
$$

---

[← Part a.](02-part-a.md) · [Up: contents](index.md) · [Part c. →](04-part-c.md)
