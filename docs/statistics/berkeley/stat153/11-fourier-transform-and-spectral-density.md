---
title: "11. Fourier Transform and Spectral Density"
course: "Berkeley Stat 153"
chapter: 11
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 11. Fourier Transform and Spectral Density

## What this covers

The previous lecture introduced the periodogram as a way of decomposing a series into sines and
cosines. This chapter asks what population quantity the periodogram is actually estimating. It
defines the discrete Fourier transform (DFT), builds the *spectral density* — the frequency-domain
counterpart of the autocovariance function — from a single worked example, and then computes the
theoretical spectra of white noise and a first-order moving average, along with the general rule
for how linear filtering reshapes a spectrum. It assumes stationary processes, the autocovariance
function, and the periodogram itself.

## From the periodogram to the discrete Fourier transform

Recall the periodogram as a harmonic (Fourier series) fit to a length-$n$ series:

$$y_t = a_0 + \sum_{j=1}^{\lfloor n/2 \rfloor} \left[a_j \cos(2\pi t j/n) + b_j \sin(2\pi t j/n)\right],$$

with coefficients estimated by

$$a_j = \frac{2}{n}\sum_{t=1}^n x_t \cos(2\pi t j/n), \qquad b_j = \frac{2}{n}\sum_{t=1}^n x_t \sin(2\pi t j/n).$$

The **discrete Fourier transform** repackages the same information as a single complex number per
frequency:

$$d(j/n) = \frac{1}{\sqrt{n}}\sum_{t=1}^n x_t e^{-i 2\pi tj/n}, \qquad j = 0, 1, \dots, n-1,$$

where $j/n$ are the *Fourier frequencies*. Using Euler's formula $e^{-i\theta} = \cos\theta - i\sin\theta$,

$$d(j/n) = \frac{1}{\sqrt{n}}\left(\sum_{t=1}^n x_t \cos(2\pi tj/n) - i\sum_{t=1}^n x_t \sin(2\pi tj/n)\right),$$

so $d(j/n)$ is just the cosine and sine sums from the periodogram, packaged as real and imaginary
parts of one number. Taking the squared modulus discards the phase and keeps only the strength of
the frequency component:

$$|d(j/n)|^2 = \frac{1}{n}\left(\sum_{t=1}^n x_t \cos(2\pi tj/n)\right)^2 + \frac{1}{n}\left(\sum_{t=1}^n x_t \sin(2\pi tj/n)\right)^2.$$

Two signals can split the same frequency very differently between its cosine and sine part — but if
the modulus is the same, they carry the same power at that frequency. The *scaled periodogram* is

$$P(j/n) = \frac{4}{n}|d(j/n)|^2,$$

and it satisfies $P(j/n) = P(1 - j/n)$, so only frequencies up to $j/n = 1/2$ need to be computed;
everything above is a mirror image.

The periodogram is a raw, noisy statistic computed from one realization of the data. To say what it
is *estimating*, we need the population object it targets: the spectral density.

## The spectral distribution function

Start from the simplest possible periodic stationary process, with a single fixed frequency
$\omega_0 \in (0, 1/2)$:

$$x_t = U_1 \cos(2\pi\omega_0 t) + U_2 \sin(2\pi\omega_0 t),$$

where $U_1, U_2$ are uncorrelated, mean-zero, and share variance $\sigma^2$. The frequency $\omega_0$
is the fraction of a full cycle the process advances between consecutive time points, so it takes
$1/\omega_0$ time steps to complete one cycle. A short calculation gives the autocovariance function

$$\gamma(h) = \sigma^2\cos(2\pi\omega_0 h) = \frac{\sigma^2}{2}e^{-2\pi i\omega_0 h} + \frac{\sigma^2}{2}e^{2\pi i\omega_0 h}.$$

The right-hand side can be read as an integral against a measure that puts mass $\sigma^2/2$ at
$\omega = -\omega_0$ and mass $\sigma^2/2$ at $\omega = \omega_0$:

$$\gamma(h) = \int_{-1/2}^{1/2} e^{2\pi i \omega h}\, dF(\omega), \qquad
F(\omega) = \begin{cases} 0 & \omega < -\omega_0 \\ \sigma^2/2 & -\omega_0 \le \omega < \omega_0 \\ \sigma^2 & \omega \ge \omega_0. \end{cases}$$

$F$ is the **spectral distribution function**. It behaves like a CDF — monotone increasing — except
that its total mass is $\gamma(0)$ rather than $1$; the analogy is to an expectation taken against
the "distribution" $F$ rather than to a probability. (The full derivation of the integral is in
Shumway and Stoffer, Section C.4.1.) The general fact behind this example: for *any* stationary
process with autocovariance $\gamma(h)$, there exists a unique, monotonically increasing $F(\omega)$
satisfying the same relationship.

When $\gamma(h)$ is absolutely summable, $F$ has a derivative: $dF(\omega) = f(\omega)\,d\omega$,
and $f$ is the **spectral density**. The relationship becomes an ordinary Fourier transform pair:

$$\gamma(h) = \int_{-1/2}^{1/2} e^{2\pi i\omega h} f(\omega)\, d\omega
\qquad\Longleftrightarrow\qquad
f(\omega) = \sum_{h=-\infty}^{\infty} \gamma(h) e^{-2\pi i \omega h}, \quad -\tfrac12 \le \omega \le \tfrac12.$$

$f(\omega)$ is the direct analogue of a probability density: it is nonnegative for every $\omega$
(this follows from $\gamma$ being a nonnegative-definite sequence), it is symmetric,
$f(\omega) = f(-\omega)$ — so in practice only $\omega \in [0, 1/2]$ is plotted — and setting $h = 0$
recovers the total variance as the area under the density,

$$\gamma(0) = \operatorname{Var}(x_t) = \int_{-1/2}^{1/2} f(\omega)\, d\omega.$$

## Time domain versus frequency domain

The autocovariance function and the spectral distribution carry the *same* information about a
stationary process, organized differently:

- the autocovariance function expresses it in terms of **lags**;
- the spectral distribution expresses it in terms of **cycles / frequencies**.

Some questions are easier to answer from lagged information; others — anything with periodic
structure — are easier to see once the series has been broken into frequencies.

## Theoretical spectra of specific processes

### White noise

A white noise process $w_t$ has uncorrelated entries with variance $\sigma_w^2$, so
$\gamma_w(h) = \sigma_w^2$ at $h=0$ and $0$ otherwise. Plugging into the transform,

$$f(\omega) = \sum_{h=-\infty}^{\infty}\gamma(h)e^{-2\pi i\omega h} = \sigma_w^2, \qquad -\tfrac12 \le \omega \le \tfrac12:$$

white noise carries **equal power at every frequency** — the same sense in which white light
contains all colors. Spectral analysis plays the role of a prism: it splits a signal into the
frequency components ("colors") it is made of.

### Linear filtering

A **linear filter** turns an input series $x_t$ into an output $y_t$ using fixed weights $a_j$:

$$y_t = \sum_{j=-\infty}^{\infty} a_j x_{t-j}, \qquad \sum_{j=-\infty}^{\infty}|a_j| < \infty,$$

also written as a convolution $y_t = (a * x)_t$. The weights $a_j$ live in the time domain, so their
effect on frequency content is not visible directly; the **frequency response function** is their
own Fourier transform,

$$A(\omega) = \sum_{j=-\infty}^{\infty} a_j e^{-2\pi i \omega j}.$$

The payoff is a clean relationship between input and output spectra:

$$f_y(\omega) = |A(\omega)|^2 f_x(\omega)$$

(proved in Shumway and Stoffer, Property 4.3 — not reproduced in the lecture). Convolution in the
time domain becomes multiplication in the frequency domain, which is why the frequency-domain view
is often the convenient one. The relation is the spectral analogue of $\operatorname{Var}(aX) = a^2\operatorname{Var}(X)$
for a linear rescaling of a random variable.

### Moving average

Take a causal $MA(1)$ process, $x_t = w_t + \theta w_{t-1}$, with $w_t$ white noise of variance
$\sigma^2$. Its autocovariance function is

$$\gamma(h) = \begin{cases} (1+\theta^2)\sigma^2 & h = 0 \\ \theta\sigma^2 & |h| = 1 \\ 0 & |h| > 1. \end{cases}$$

Feeding this into the transform and using $\cos\theta = (e^{i\theta}+e^{-i\theta})/2$,

$$f(\omega) = (1+\theta^2)\sigma^2 + \theta\sigma^2\left(e^{-2\pi i\omega} + e^{2\pi i \omega}\right)
= \sigma^2\left(1 + \theta^2 + 2\theta\cos(2\pi\omega)\right).$$

For $\theta > 0$ this is largest at $\omega = 0$ and decays monotonically to its minimum at
$\omega = 1/2$; the larger $\theta$ is, the steeper the decay. Unlike white noise, an $MA(1)$
concentrates its power at low frequencies — smoothing the series suppresses the fast, high-frequency
wiggles, and the spectral density says exactly how much.

<figure>
<svg viewBox="0 0 320 210" role="img" aria-label="Spectral density of white noise, a flat line, against the decaying spectral density of a causal MA(1) process with theta = 0.5">
  <line x1="40" y1="180" x2="312" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <polygon points="312,180 302,176 302,184" fill="currentColor"/>
  <line x1="40" y1="185" x2="40" y2="10" stroke="currentColor" stroke-width="1.5"/>
  <polygon points="40,10 36,20 44,20" fill="currentColor"/>
  <text x="308" y="198" text-anchor="middle" font-size="12" fill="currentColor">&#969;</text>
  <text x="18" y="20" text-anchor="middle" font-size="12" fill="currentColor">f(&#969;)</text>
  <text x="40" y="196" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="170" y="196" text-anchor="middle" font-size="11" fill="currentColor">0.25</text>
  <text x="300" y="196" text-anchor="middle" font-size="11" fill="currentColor">0.5</text>
  <line x1="40" y1="116" x2="300" y2="116" stroke="currentColor" stroke-width="2"/>
  <text x="235" y="108" font-size="12" fill="currentColor">white noise, flat</text>
  <polyline points="40,36 66,39.1 92,48.2 118,62.4 144,80.2 170,100 196,119.8 222,137.6 248,151.8 274,160.9 300,164"
            fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="90" y="52" font-size="12" fill="currentColor">MA(1), &#952; = 0.5</text>
</svg>
<figcaption>Theoretical spectral density of white noise (constant) against a causal MA(1) process
with &#952; = 0.5, computed from f(&#969;) = &#963;&#178;(1 + &#952;&#178; + 2&#952;cos 2&#960;&#969;):
power concentrated near &#969; = 0 rather than spread evenly.</figcaption>
</figure>

The lecture's own figure additionally plots the spectrum of a second-order autoregressive process
alongside white noise and the moving average, but only the white-noise and moving-average cases are
derived in the accompanying text.

The next lecture turns to two extensions: how to tame the noisiness of the DFT and periodogram as
estimators of $f(\omega)$, and time-frequency analysis, where the question becomes how the frequency
content of a series changes over time.

## Sources

- Berkeley STAT 153, spring 2026, lecture 13 ("Spectral analysis"), split into three linked pages,
  all CC BY 4.0:
  - [Discrete Fourier Transform](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/13_spectral_analysis_notes.md) — periodogram recap, DFT definition, squared modulus, scaled
    periodogram.
  - Spectral Density — the periodic-process example, spectral distribution function $F$, spectral
    density $f$ and its properties.
  - Theoretical spectra of different processes — white noise, linear filtering, and the causal
    $MA(1)$ spectral density.
- Referred to but not contained in the supplied material: Shumway and Stoffer, *Time Series
  Analysis*, Ch. 4 (assigned reading), Section C.4.1 (derivation of the spectral distribution
  integral for the periodic example), and Property 4.3 (proof that $f_y(\omega) = |A(\omega)|^2 f_x(\omega)$).
  The lecture image `13_spectra.png` also shows the theoretical spectrum of a second-order
  autoregressive process, which is not worked out in the text.
- No transcript, written notes, or exercises were supplied for this lecture.

---

[← 10. Periodic Signals and the Periodogram](10-periodic-signals-and-the-periodogram.md) · [Contents](index.md) · [12. Smoothing the Periodogram (part 1) →](12-smoothing-the-periodogram-part-1.md)
