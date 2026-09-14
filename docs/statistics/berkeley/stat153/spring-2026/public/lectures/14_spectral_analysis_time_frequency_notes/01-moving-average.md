---
title: Moving Average
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/14_spectral_analysis_time_frequency_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/14_spectral_analysis_time_frequency_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Moving Average

**Source:** [`public/lectures/14_spectral_analysis_time_frequency_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/14_spectral_analysis_time_frequency_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

![Examples of spectra of white noise, moving average, and second-order autoregressive process](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/13_spectra.png)

For the moving average, let's consider a causal moving average (remember, this is the version where we only consider values from the past in our moving average):

$$x_t = w_t + \theta w_{t-1}$$

The autocovariance function for this is:

$$
\gamma(h) = \begin{cases}
(1+\theta^2)\sigma^2 & h=0\\
\theta\sigma^2 & |h|=1\\
0 & |h| > 1
\end{cases}
$$

The spectral density is therefore:

$$
\begin{aligned}
f(\omega) &= (1+\theta^2)\sigma^2 + \theta\sigma^2(e^{-2\pi i \omega}+e^{2\pi i \omega}) \\
&= \sigma^2(1+\theta^2+2\theta\cos(2\pi\omega))
\end{aligned}
$$

in the second line, we used $\cos(\theta) = (e^{i\theta}+e^{-i\theta})/2$ from Euler's formula $e^{i\theta}=\cos(\theta)+i\sin(\theta)$.

What results here is that the MA process has a spectral density that decays from zero, with larger $\theta$ corresponding to a steeper decay from $\omega=0$ to $\omega=1/2$.

---

[Up: contents](index.md) · [An overview of the DFT and periodogram →](02-an-overview-of-the-dft-and-periodogram.md)
