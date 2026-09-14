---
title: Family-wise Error Rate (FWER)
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/multiple-testing.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/multiple-testing.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Family-wise Error Rate (FWER)

**Source:** [`reader/multiple-testing.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/multiple-testing.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Problem: Even if all $H_{0i}$ true, might have:

$\mathbb{P}(\text{any } H_{0i} \text{ rejected}) \leq 1 - (1-\alpha)^m \approx m\alpha$

Example: $X_i \sim N(\theta_i, 1)$ iid, $i = 1,\ldots,m$, $H_{0i}: \theta_i = 0$

$\mathbb{P}_0(\text{any } H_{0i} \text{ rejected}) = 1 - (1-\alpha)^m \approx m\alpha$

Is this a problem? Yes, if all attention will be focused on the false rejections and none on the correct non-rejections.

Classical solution is to control the family-wise error rate (FWER):

FWER = $\mathbb{P}_\theta(\text{any false rejections}) = \mathbb{P}_\theta(R \cap H_{0c} \neq \emptyset)$

Want:
$\sup_\theta \text{FWER}(\theta) \leq \alpha$

Typically achieved by correcting marginal p-values: $p_1(X), \ldots, p_m(X)$, $p_i \sim U(0,1)$

e.g., $\phi_i = 1\{\alpha/(2m)|X_i| > \Phi^{-1}(1-\alpha/(2m))\}$ for Gaussian

---

[← Multiple Testing](01-multiple-testing.md) · [Up: contents](index.md) · [Bonferroni Correction →](03-bonferroni-correction.md)
