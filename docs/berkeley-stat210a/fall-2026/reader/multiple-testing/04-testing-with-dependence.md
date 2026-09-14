---
title: Testing with Dependence
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/multiple-testing.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/multiple-testing.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Testing with Dependence

**Source:** [`reader/multiple-testing.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/multiple-testing.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Bonferroni isn't much worse than Šidák
e.g., $\alpha = 0.05$, $m = 20$: $0.0025$ vs $0.00256$

But when tests are highly dependent, can often do much better

### Example: Scheffé's S-method

$X \sim N(\theta, I_d)$, $\theta \in \mathbb{R}^d$
$H_0: a_j^T \theta = 0$ for $j = 1,\ldots,m$, $\|a_j\| = 1$

Reject $H_{0j}$ if $|a_j^T X| > \sqrt{d F_{d,\infty,1-\alpha}}$

Controls FWER:

$\mathbb{P}(\|X - \theta\|^2 \leq dF_{d,\infty,1-\alpha}) = 1-\alpha$

Can view as deduction from confidence region:
$C(X) = \{\theta: \|X - \theta\|^2 \leq dF_{d,\infty,1-\alpha}\}$

---

[← Bonferroni Correction](03-bonferroni-correction.md) · [Up: contents](index.md) · [Deduced Inference →](05-deduced-inference.md)
