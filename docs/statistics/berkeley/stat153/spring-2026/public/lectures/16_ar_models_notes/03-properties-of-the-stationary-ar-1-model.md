---
title: Properties of the stationary AR(1) model
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/16_ar_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/16_ar_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Properties of the stationary AR(1) model

**Source:** [`public/lectures/16_ar_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/16_ar_models_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

When $|\phi| < 1$, we can derive closed-form expressions (see the derivations of these in your book, Ch 3 example 3.1):

| Property       | Formula                                                        |
|----------------|----------------------------------------------------------------|
| Mean           | $\mu_x = 0$ (assuming zero-mean)                               |
| Variance       | $\gamma(0) = \frac{\sigma_w^2}{1 - \phi^2}$                    |
| Autocovariance | $\gamma(h) = \frac{\sigma_w^2\phi^h}{1 - \phi^2}$ for $h\geq 0$|
| ACF            | $\rho(h) = \frac{\gamma(h)}{\gamma(0)} = \phi^{h}$             |

Note that the ACF of an AR(1) process decays exponentially! We can also see here that $|\phi| < 1$ is needed for stationarity, because the denominator in the variance equation goes to zero as $|\phi| \to 1$. Let's look at an example for the ACF in the notebook.

![Example ACF for AR(1) process with phi=0.9](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/16_acf.png)

---

[← AR(1) process](02-ar-1-process.md) · [Up: contents](index.md) · [The backshift operator →](04-the-backshift-operator.md)
