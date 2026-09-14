---
title: Spectral Density
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/13_spectral_analysis_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/13_spectral_analysis_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Spectral Density

**Source:** [`public/lectures/13_spectral_analysis_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/13_spectral_analysis_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Consider a periodic stationary process with fixed frequency $\omega_0 \in (0, 1/2)$:

$$x_t = U_1 \cos(2\pi\omega_0 t) + U_2 \sin(2\pi\omega_0 t)$$

with $U_1$ and $U_2$ as uncorrelated zero-mean random variables with equal variance $\sigma^2$. The frequency $\omega_0$ tells us what fraction of a complete cycle the process completes between consecutive time points. Equivalently, the process requires $1/\omega_0$ time periods to complete one full cycle. We can then calculate the covariance function as:

$$
\begin{aligned}
\gamma(h) &=\sigma^2 \cos(2\pi \omega_0 h) = \frac{\sigma^2}{2}e^{-2\pi i \omega_0 h} + \frac{\sigma^2}{2}e^{2\pi i \omega_0 h}\\
&= \int_{-\frac{1}{2}}^{\frac{1}{2}} e^{2\pi i \omega h} dF(\omega)\\
\end{aligned}
$$

where $F(\omega)$ is the *spectral distribution function* defined by:

$$F(\omega) = \begin{cases}
0 & \omega < -\omega_0\\
\sigma^2/2 & -\omega_0 \leq \omega < \omega_0\\
\sigma^2 & \omega \geq \omega_0
\end{cases}$$

For details of this integration, your book has a longer explanation and proof in Section C.4.1.

An important property of this spectral distribution function is that if ${x_t}$ is stationary with autocovariance $\gamma(h) = \text{cov}(x_{t+h}, x_t)$, then there exists a unique monotonically increasing function $F(\omega)$ such that the relationship described above in (7) applies.

We can think of $F$ here as being analogous to a cumulative distribition function (CDF), so the integral above is analogous to an expectation defined with respect to the distribution governing $F$. The total mass is $\gamma(0)$ rather than 1. In the case where the autocovariance function is absolutely summable, we have $dF(\omega) = f(\omega)d\omega$, where we call $f(\omega)$ the *spectral density*.

that is, we rewrite this as:

$$
\begin{aligned}
\gamma(h) &= \int_{-\frac{1}{2}}^{\frac{1}{2}} e^{2\pi i \omega h} f(\omega)d\omega\\
\end{aligned}
$$

This is then the inverse transform of the *spectral density function*:

$$f(\omega) = \sum_{h=-\infty}^{h=\infty} \gamma(h)e^{-2\pi i \omega h}\quad -1/2 \leq \omega \leq 1/2$$

This is very cool because the spectral density is then the analog of the probability density function. The fact that $\gamma(h)$ is nonnegative ensures that we always have positive values for each frequency: $f(\omega) \geq 0$ for all $\omega$. We also have $f(\omega)=f(-\omega)$, so typically we only plot $f(\omega)$ for values less than 1/2. For $h=0$ we also have:

$$\gamma(0) = \text{var}(x_t) = \int_{-\frac{1}{2}}^{\frac{1}{2}} f(\omega)d\omega$$

This quantity expresses the total variance as the integrated spectral density over all frequencies.

---

[← Discrete Fourier Transform](01-discrete-fourier-transform.md) · [Up: contents](index.md) · [Autocovariance vs. spectral distribution functions →](03-autocovariance-vs-spectral-distribution-functions.md)
