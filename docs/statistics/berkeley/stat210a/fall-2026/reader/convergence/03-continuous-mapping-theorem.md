---
title: Continuous Mapping Theorem
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/convergence.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/convergence.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Continuous Mapping Theorem

**Source:** [`reader/convergence.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/convergence.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Theorem (Continuous Mapping): Let $g$ be continuous, $X_n, X$ r.v.'s.

1. If $X_n \xrightarrow{d} X$, then $g(X_n) \xrightarrow{d} g(X)$
2. If $X_n \xrightarrow{p} c$, then $g(X_n) \xrightarrow{p} g(c)$

Proof:
$f$ bounded continuous $\implies f \circ g$ bounded continuous
If $X_n \xrightarrow{d} X$, then $\mathbb{E}[f(g(X_n))] \to \mathbb{E}[f(g(X))]$
$X_n \xrightarrow{p} c$ special case with $X \equiv c$

---

[← Convergence](02-convergence.md) · [Up: contents](index.md) · [Slutsky's Theorem →](04-slutsky-s-theorem.md)
