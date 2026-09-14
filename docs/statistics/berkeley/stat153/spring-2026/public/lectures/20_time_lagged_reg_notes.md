---
title: Lecture 20 Notes - Time Lagged Regression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/20_time_lagged_reg_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/20_time_lagged_reg_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Lecture 20 Notes - Time Lagged Regression

**Source:** [`public/lectures/20_time_lagged_reg_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/20_time_lagged_reg_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

* **Reading**: Ch 4.8 - Shumway and Stoffer, [Holdgraf et al. Encoding and Decoding Models in Cognitive Electrophysiology](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2017.00061/full)

# Time-lagged Regression Models

Up until now, we've spoken about simple linear regression, multiple linear regression, nonlinear/sinusoidal regression, and various flavors of autoregressive models. Time-lagged regression is another extension of multiple linear regression that allows us to estimate an output time series $y_t$ from a weighted sum of another input time series $x_t$ at different time lags.

$$y_t = \sum_{r=-\infty}^\infty \beta_r x_{t-r} + v_t$$

Note here that in Shumway and Stoffer (eqn 4.115), this is written with infinite lag values to make the Fourier math work out cleanly, but typically we will use a finite time series and finite, theoretically motivated lags.

As an example in your book, we have the SOI and Recruitment series. We can relate these two time series to motivate showing that the SOI (reflecting El Ni\~{n}o related weather patterns) may be an input $x_t$ that drives fish recruitment $y_t$ as the output. Today, we're going to pull together several concepts from class including multiple linear regression, regularization, cross-validation, and spectral analysis and use these on a neuroscience problem, referred to in the field as "spectrotemporal receptive field estimation".

For the rest of this lecture, we'll refer to the accompanying [Lecture20.ipynb notebook](Lecture20/index.md)

---

[Up: contents](../../index.md)
