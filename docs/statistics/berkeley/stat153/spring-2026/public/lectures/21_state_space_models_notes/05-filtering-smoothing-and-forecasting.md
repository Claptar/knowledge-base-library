---
title: Filtering, smoothing, and forecasting
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/21_state_space_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/21_state_space_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Filtering, smoothing, and forecasting

**Source:** [`public/lectures/21_state_space_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/21_state_space_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

For state space models, we want to estimate our underlying unobserved signal $x_t$ given the data $y_{1:s} = {y_1, \dots, y_s}$ to time $s$. In practice, the steps for the state space models include:

1. Filtering, where we estimate $x_t$ using measurements up through time $t$ (here $s$=$t$)
2. Prediction/forecasting, where we have $s<t$ and want to estimate new data
3. Smoothing, where $s>t$. This allows us to estimate $x_t$ using the entire dataset, including observations after $t$. This can be used to better estimate missing values.

---

[← Bone marrow transplant example](04-bone-marrow-transplant-example.md) · [Up: contents](index.md) · [Other examples →](06-other-examples.md)
