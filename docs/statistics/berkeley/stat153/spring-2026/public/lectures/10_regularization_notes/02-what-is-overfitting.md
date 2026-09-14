---
title: What is overfitting?
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/10_regularization_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/10_regularization_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# What is overfitting?

**Source:** [`public/lectures/10_regularization_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/10_regularization_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Overfitting is seen when we fit a model that learns to predict our data perfectly, but does not generalize to new data. It follows the *noise* too closely. As model flexibility (and number of parameters) increases, we can pick up patterns in the data by random chance rather than by some true relationship.

We can look at an example in the notebook that accompanies this lecture.

---

[← Improving upon the linear model](01-improving-upon-the-linear-model.md) · [Up: contents](index.md) · [Cross-validation →](03-cross-validation.md)
