---
title: Periodogram
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/12_spectral_analysis_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/12_spectral_analysis_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Periodogram

**Source:** [`public/lectures/12_spectral_analysis_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/12_spectral_analysis_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Now let's say we wanted to estimate the component frequencies of a signal like this, where we didn't know what the underlying components were. One way to do this is using the *periodogram*.

For any time series, we can write:

$$y_t = a_0 + \sum_{j=1}^{\lfloor n/2 \rfloor} [a_j \cos(2\pi t j/n) + b_j \sin(2\pi t j/n)]$$

for $t=1,\dots,n$ and coefficients $a_j$ and $b_j$. $\lfloor \rfloor$ is the greatest integer function (also called the "floor"), which rounds numbers down to the nearest integer. If $n$ is even, we have $a_{n/2} \cos(2\pi t \frac{1}{2})=a_{n/2}(-1)^t$ and $b_{n/2}=0$.

Here the values of $j$ correspond to frequencies indices. Each $j$ represents a different frequency component in the decomposition. $j/n$ is the frequency in cycles per sample. As $j$ goes from 1 to $\lfloor n/2 \rfloor$, we sweep up through all distinguishable frequencies from the slowest oscillation up to the Nyquist frequency. For example, let's say we have $n=100$ data points:

* $j=1$ means the wave completes exactly 1 full cycle over the n samples, which is the slowest possible oscillation that fits in your data window.
* $j = 2$ completes exactly 2 full cycles, $j = 3$ completes 3, and so on.
* $j = 50 (= n/2)$ completes 50 cycles, the fastest oscillation you can resolve, alternating up-down-up-down every sample.

We can now use regression to get the coefficients:

$a_j = \frac{2}{n}\sum_{t=1}^n x_t \cos(2\pi t j/n)$ and $b_j = \frac{2}{n}\sum_{t=1}^n x_t \sin(2\pi t j/n)$

Here $a_j$ and $b_j$ represent how much of a particular frequency is present in our signal, with $a_j$ and $b_j$ together controlling the amplitude and phase at frequency $j$. These are free parameters and set independently, but jointly contribute to $A$ and $\phi$.

From this, we can then define the *scaled periodogram*:

$$P(j/n) = a_j^2+b_j^2$$

for $j/n \neq 0, 1/2$. The scaled periodogram is the sample variance at each frequency component and is an estimate of $\sigma_j^2$ corresponding to a sinusoid at frequency $f_j = j/n$. These frequencies are called the *Fourier frequencies*. Large values of $P(j/n)$ indicate which frequencies dominate the series, small values may represent noise.

Next time we will relate this to the Discrete Fourier Transform (DFT) of a signal.

---

[← Periodic signals](01-periodic-signals.md) · [Up: contents](index.md)
