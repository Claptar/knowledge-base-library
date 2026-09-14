---
title: Autoregression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/02_characteristics_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/02_characteristics_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Autoregression

**Source:** [`public/lectures/02_characteristics_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/02_characteristics_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Another flavor of dataset we might see is data that comes from an autoregressive process. Autoregression = regression or prediction based on past values of the same time series ("auto").

This might look something like:

$x_t = 1.5 x_{t-1} - 0.75 x_{t-2} + w_t$

You will see what this looks like in Lab 1. Because the data at $t$ relies on $t-1$ and $t-2$ (the prior two data points), this is an AR(2) process. Generating data in this way can result in oscillatory behavior.

---

[← Moving average](04-moving-average.md) · [Up: contents](index.md) · [Random Walk →](06-random-walk.md)
