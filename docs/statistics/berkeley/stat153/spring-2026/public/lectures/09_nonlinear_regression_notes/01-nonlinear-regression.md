---
title: Nonlinear regression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nonlinear_regression_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/09_nonlinear_regression_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Nonlinear regression

**Source:** [`public/lectures/09_nonlinear_regression_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nonlinear_regression_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Recall last time we spoke about *Multiple Linear Regression*:

$$y_i = \beta_0 + \beta_1 x_{i_1} + \beta_2 x_{i_2} + \cdots + \beta_n x_{i_p} + w_i $$

In this case, we assumed a linear relationship between $y$ and our $\beta$ estimates. However, in many real datasets and models, certain parameters are related to our output in a nonlinear fashion. One example is seen in the sunspots dataset, in which the time series data show strong periodicity.

![Smoothed 12-month sunspot numbers sampled twice per year](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/09_sunspots.png)

## When might this type of problem come up?

* Climate data (El Nino/SOI)
* Astronomy
  * Variable stars - brightness fluctations that can be used to estimate the period ($1/f$), which relates to the intrinsic luminosity of a star. This can then be used to estimate the distance to the star. Edwin Hubble in the 1920s measured the distance to the Andromeda galaxy and showed they were too far to be inside the Milky Way, which suggested we are in just one galaxy among many.
* Signal processing - speech and audio
  * Estimating the pitch and formants of a person's voice is part of ASR (automatic speech recognition)
* Economics - but generally less stable

For example, we might have:

```math
:label: eq2
y_t = \beta_0 + \beta_1 \cos (2\pi ft) + \beta_2 \sin (2\pi ft ) + \epsilon_t \quad \text{where } \epsilon_t \overset{i.i.d}\sim N(0, \sigma^2)\label{eq2}
```

The parameters we will fit here include $\beta_0, \beta_1, \beta_2, \sigma$ and frequency parameter $f$. If $f$ is already known, then {eq}`eq2` reduces to multiple linear regression: $y=X_f\beta + \epsilon$ with:

$$
  y = \begin{pmatrix}
    y_1 \\ \vdots \\ y_n
  \end{pmatrix},
  X_f = \begin{pmatrix}
    1 & \cos(2\pi f(1)) & \sin(2\pi f(1)) \\
    \vdots & \vdots & \vdots \\
    1 & \cos(2\pi f(n)) & \sin(2\pi f(n)) \\
    \end{pmatrix},
  \beta = \begin{pmatrix}
    \beta_0 \\ \beta_1 \\ \beta_2
    \end{pmatrix} \quad \text{and }
  \epsilon = \begin{pmatrix}
    \epsilon_1 \\ \vdots \\ \epsilon_n
    \end{pmatrix}
$$

And we can proceed as before. If $f$ is *not* known, then this is a nonlinear regression model.

This particular type of model $y_t = \beta_0 + \beta_1 \cos (2\pi ft) + \beta_2 \sin (2\pi ft ) + \epsilon_t$ is called a sinusoid, which has some special properties (later we'll revisit this when we talk about power spectral analysis).

---

[Up: contents](index.md) · [About Sinusoids →](02-about-sinusoids.md)
