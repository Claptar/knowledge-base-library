---
title: White noise
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/02_characteristics_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/02_characteristics_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# White noise

**Source:** [`public/lectures/02_characteristics_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/02_characteristics_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Many real-world time series are a combination of underlying signal $s_t$ plus noise $w_t$. In some (nice) cases, $w_t$ is _white noise_.

White noise is a special case of uncorrelated variables in sequence, e.g. $x_t$ where $t=1,2,3,...$. White noise, unlike most real time series, *is* iid, with mean $0$ and variance $\sigma^2_w$.  One very useful case is white noise from a Gaussian distribution, where we can write: $w_t \sim \mbox{iid } \mathcal{N}(0,\sigma^2_w)$.

If all time series could be described in this way, classical statistics would suffice.

What does white noise look like?

![White noise time series](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/Lec2_white_noise.png)

---

[← Stochastic process](02-stochastic-process.md) · [Up: contents](index.md) · [Moving average →](04-moving-average.md)
