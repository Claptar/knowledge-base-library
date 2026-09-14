---
title: A note on dealing with sampling
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nonlinear_regression_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/09_nonlinear_regression_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# A note on dealing with sampling

**Source:** [`public/lectures/09_nonlinear_regression_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nonlinear_regression_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

The sinusoidal model is written above in continuous time, but usually we are collecting data in discrete time samples. If our sampling rate is $f_s$ (in samples per second, or Hz), then our actual observations are occuring at times $t_n = \frac{n}{f_s}$ for $n=0, 1, \dots$, so we are actually fitting:

$$y_n = \beta_0 + R \cos \left( \frac{2\pi f n}{f_s} + \phi \right) + \epsilon_n$$

This sampling rate $f_s$ fundamentally constrains what frequencies you can estimate. This has a special name:

## The Nyquist limit

You can only reliably estimate frequencies up to half of the sampling rate:

$$f_\text{max} = \frac{f_s}{2}$$

This $f_\text{max}$ is also called the **Nyquist Frequency**. If the true signal contains a component at frequency $f$ and your sampling rate is too low ($f > f_s/2$), then that component doesn't vanish -- rather, induces **aliasing**, which is where you will get an estimate of $f$ that is $| f - n f_s|$ for any integer $n$. We'll come back to this when we talk about power spectral analysis, but for now, just remember that if you want to estimate a particular sinusoidal component with frequency $f$, that frequency must be no more than one half of the sampling rate.

Also, this becomes important when we are trying to estimate $f$ via least squares, because if framed in this way we only have to test $f \sim \text{unif}[0, 1/2]$

See a demo of [how the Nyquist Limit works](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nyquist.html)

---

[← About Sinusoids](02-about-sinusoids.md) · [Up: contents](index.md) · [Least squares estimation of $\beta, f, \sigma$ →](04-least-squares-estimation-of.md)
