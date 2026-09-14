---
title: Bonferroni Correction
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/multiple-testing.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/multiple-testing.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Bonferroni Correction

**Source:** [`reader/multiple-testing.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/multiple-testing.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Assume $p_1,\ldots,p_m$ are p-values for $H_{01},\ldots,H_{0m}$ with $p_i \sim U(0,1)$ under $H_{0i}$

For general dependence, can guarantee control by rejecting $H_{0i}$ iff $p_i \leq \alpha/m$:

$\mathbb{P}_\theta(\text{any false rejections}) \leq \mathbb{P}_\theta(\text{any } H_{0i} \text{ rejected}) \leq \sum_{i \in H_{0c}} \mathbb{P}_\theta(H_{0i} \text{ rejected}) \leq m_0\alpha/m \leq \alpha$

If p-values independent, can improve to $1-(1-\alpha)^{1/m}$ (Šidák correction)

Then $\mathbb{P}_\theta(\text{no false rejections}) = \prod_{i \in H_{0c}} \mathbb{P}_\theta(p_i > (1-(1-\alpha)^{1/m})) \geq (1-\alpha)^{m_0/m} \geq 1-\alpha$

For small $\alpha$: $1-(1-\alpha)^{1/m} \approx \alpha/m$

Šidák doesn't improve much on Bonferroni

---

[← Family-wise Error Rate (FWER)](02-family-wise-error-rate-fwer.md) · [Up: contents](index.md) · [Testing with Dependence →](04-testing-with-dependence.md)
