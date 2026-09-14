---
title: Multiple Testing
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/multiple-testing.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/multiple-testing.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Multiple Testing

**Source:** [`reader/multiple-testing.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/multiple-testing.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

In many testing problems, we want to test many hypotheses at a time, e.g.:

- Test $H_0: \beta_j = 0$ for $j = 1,\ldots,d$ in linear regression
- Test whether each of 20K single nucleotide polymorphisms (SNPs) is associated with a given phenotype (e.g., diabetes, schizophrenia)
- Test whether each of 2000 website tweaks affect user engagement

### Setup

$X \sim P_\theta \in \cP$, $H_{0i}: \theta \in \Theta_i$, $i = 1,\ldots,m$

Commonly, $H_{0i}: \theta_i = 0$

Goal: Return accept/reject decision for each $i$

Let $R = \{i: H_{0i} \text{ rejected}\}$, $|R| \leq m$

$H_{0c} = \{i: H_{0i} \text{ true}\}$, $|H_{0c}| = m_0 \leq m$

$R \cap H_{0c}$ = false rejections

---

[Up: contents](index.md) · [Family-wise Error Rate (FWER) →](02-family-wise-error-rate-fwer.md)
