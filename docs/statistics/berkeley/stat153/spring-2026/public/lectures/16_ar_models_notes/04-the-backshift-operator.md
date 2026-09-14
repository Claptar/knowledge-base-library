---
title: The backshift operator
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/16_ar_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/16_ar_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# The backshift operator

**Source:** [`public/lectures/16_ar_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/16_ar_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Next, to look into the properties of the AR models, we're going to define the *backshift operator* $B$:

$B x_t = x_{t-1}$

Then we can rewrite the AR(1) model as:

$$\begin{aligned}
x_t - \phi x_{t-1} &= w_t\\
x_t - \phi B x_t &= w_t\\
(1 - \phi B) x_t &= w_t
\end{aligned}
$$

or the AR(p) model:

$$(1 - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p) x_t = w_t$$

---

[← Properties of the stationary AR(1) model](03-properties-of-the-stationary-ar-1-model.md) · [Up: contents](index.md) · [The autoregressive operator/characteristic polynomial →](05-the-autoregressive-operator-characteristic-polynomial.md)
