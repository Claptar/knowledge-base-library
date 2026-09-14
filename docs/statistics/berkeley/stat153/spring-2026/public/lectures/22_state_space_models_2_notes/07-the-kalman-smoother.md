---
title: The Kalman Smoother
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/22_state_space_models_2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# The Kalman Smoother

**Source:** [`public/lectures/22_state_space_models_2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

The Kalman Smoother (in the accompanying notebook this is implemented using the Rauch-Tung-Striebel/RTS algorithm, published in 1965). This can be used *post hoc* to refine state estimates retrospectively, using all data (including future data)!

In practice, this runs using a forward pass (the Kalman filter), followed by a backward pass, which modifies earlier estimates based on the filter's stored outputs.

---

[← Running the Kalman Filter](06-running-the-kalman-filter.md) · [Up: contents](index.md) · [When to use the filter vs. smoother →](08-when-to-use-the-filter-vs-smoother.md)
