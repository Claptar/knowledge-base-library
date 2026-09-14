---
title: Practical Applications
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/minimax-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/minimax-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Practical Applications

**Source:** [`reader/minimax-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/minimax-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Minimax estimators are very hard to find, but minimax bounds are often used in statistical theory to characterize hardness, especially lower bounds.

### Approach 1: Near-optimal Estimators

1. Propose practical estimator $\delta$
2. Find $\pi$ for which $r(\pi)$ close to $\sup_\theta R(\theta, \delta)$ (or same rate, or asymptotically)
3. Conclude $\delta$ can't be improved much

### Approach 2: Problem Hardness

Quantify hardness of a problem by its minimax rate in some asymptotic regime.

Caveat: A problem might be easy throughout most of parameter space but very hard in some bizarre corner we never encounter in practice.

---

[← Least Favorable Sequence](03-least-favorable-sequence.md) · [Up: contents](index.md)
