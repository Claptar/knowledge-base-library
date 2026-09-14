---
title: Testing with one real parameter
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-one-parameter.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-one-parameter.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Testing with one real parameter

**Source:** [`reader/testing-one-parameter.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-one-parameter.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

This lecture concerns the general problem of testing with one real parameter. We observe $X \sim P_\theta$ for $\theta \in \Theta \subseteq \RR$, and we might want to test a *one-sided alternative* like $H_0:\; \theta \leq \theta_0$ vs the one-sided alternative $H_1:\; \theta > \theta_0$, or a *point null* hypothesis like $H_0:\; \theta = \theta_0$ against a *two-sided alternative* $H_1:\; \theta \neq \theta_0$. Or, we could test an *interval null* $H_0:\; |\theta - \theta_0| \leq \delta$ vs the two-sided alternative $H_1:\; |\theta-\theta_0|>\delta$, for $\delta \geq 0$ (which reduces to the point null if $\delta = 0$).

---

[Up: contents](index.md) · [One-sided testing →](02-one-sided-testing.md)
