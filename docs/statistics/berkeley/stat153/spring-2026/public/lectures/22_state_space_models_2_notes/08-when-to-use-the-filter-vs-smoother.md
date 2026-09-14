---
title: When to use the filter vs. smoother
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/22_state_space_models_2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# When to use the filter vs. smoother

**Source:** [`public/lectures/22_state_space_models_2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

It's helpful to use the Kalman filter for real-time estimates where you can't use future data because it doesn't exist yet. Computationally, the Kalman filter is also very cheap, because you only need data from the previous time step for your estimates.

On the other hand, the Kalman smoother is helpful for post hoc analyses where getting the best possible estimate at each time point is your goal. For example, in the bone marrow transplant data, if we are trying to look at platelet, WBC, and hematocrit data after the fact to make some claims about patient outcomes, we may want to use the smoother to get better estimates.

---

[← The Kalman Smoother](07-the-kalman-smoother.md) · [Up: contents](index.md) · [Examples →](09-examples.md)
