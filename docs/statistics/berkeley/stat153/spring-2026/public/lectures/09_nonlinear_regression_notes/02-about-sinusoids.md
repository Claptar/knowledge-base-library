---
title: About Sinusoids
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nonlinear_regression_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/09_nonlinear_regression_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# About Sinusoids

**Source:** [`public/lectures/09_nonlinear_regression_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nonlinear_regression_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

A sinusoid can be given by the following function at time $t$:

$$s(t) := \beta_0 + R \cos (2\pi f t + \phi)$$

Where:

* $R$ is the *amplitude* of the sinusoid, which represents the height of the oscillation from the center line.
* $f$ is the *frequency* of the sinusoid, which represents how many cycles (oscillations) are observed per unit time. If time is measured in seconds, then $f$ is given in units of Hertz (Hz).
* $1/f$ is the *period* of the oscillation, which is the length of time it takes to complete one full oscillation (one up peak and down peak)
* $\phi$ is the *phase* of the oscillation. If $\phi=0$, the sinusoid is at its maximum value at $t=0$. The $\phi$ value allows us to account for leftward or rightward shifts of the whole oscillation in time.
* $2\pi f$ is called the angular frequency. Sometimes we also write this as $\omega=2\pi f$. This measures the rate of change of the angle inside the cosine.

You may have noticed here that this sinusoid doesn't look exactly like the equation we started with earlier {eq}`eq2`. However, we can use the trigonometric identity $\cos(a + b) = (\cos a)(\cos b) - (\sin a)(\sin b)$ to rewrite the equation as:

$$a &= 2\pi ft, \quad b=\phi$$

$$
\begin{aligned}
s(t) &= \beta_0 + R ( (\cos 2\pi ft \cos \phi) - (\sin 2\pi ft \sin \phi))\\
&= \beta_0 + R \cos \phi \cos 2\pi ft - R \sin \phi \sin 2\pi ft
\end{aligned}
$$

We can now express $\beta_1=R\cos\phi$ and $\beta_2=-R\sin\phi$, then we have the equation we discussed before:

$$s(t) = \beta_0 + \beta_1 \cos 2\pi ft + \beta_2 \sin 2\pi ft$$

We can also always rederive $R$ or $\phi$ if we want them:

$$R=\sqrt{\beta_1^2+ \beta_2^2}, \quad \phi = \arctan\left(-\frac{\beta_2}{\beta_1}\right)$$

---

[← Nonlinear regression](01-nonlinear-regression.md) · [Up: contents](index.md) · [A note on dealing with sampling →](03-a-note-on-dealing-with-sampling.md)
