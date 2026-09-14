---
title: Signal in noise
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/02_characteristics_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/02_characteristics_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Signal in noise

**Source:** [`public/lectures/02_characteristics_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/02_characteristics_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

More generally, we can see other examples of periodic signals contaminated by white noise. For example:

$x_t = A*\cos(2\pi\omega t+\phi) + w_t$

Where $A$ is the amplitude of the signal, $\omega$ is the frequency of the oscillation, and $\phi$ is a phase shift.

The ratio of the amplitude of the signal to the standard deviation of the noise determines the SNR - signal to noise ratio. The larger the SNR, the easier it is to recover our signal.

Later, we will use various forms of regression to try to recover these signals!

---

[← Random Walk](06-random-walk.md) · [Up: contents](index.md) · [Next week →](08-next-week.md)
