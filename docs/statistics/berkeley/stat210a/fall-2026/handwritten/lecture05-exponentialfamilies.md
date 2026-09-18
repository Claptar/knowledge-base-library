---
title: Exponential families
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture05-exponentialfamilies.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture05-exponentialfamilies.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture05-exponentialfamilies.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture05-exponentialfamilies.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Exponential families

## Outline

1) Exponential families
2) Differential identities
3) MGF

---

An **$s$-parameter exponential family** is a family $\mathcal{P} = \{P_\eta : \eta \in \Xi\}$ with densities of the form
$$p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x)$$
wrt base measure $\mu$ on sample space $\mathcal{X}$

## Components of $p_\eta$:

- $\eta \in \Xi \subseteq \mathbb{R}^s$ called **natural parameter**
- $T(x)$ is $s$-dimensional **sufficient statistic**
  $$\text{factorization theorem}: \quad g_\eta(T(x)) = e^{\eta' T(x) - A(\eta)}$$
- \$

---

[Up: contents](../index.md)
