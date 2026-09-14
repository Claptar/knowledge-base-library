---
title: Theoretical spectra of different processes
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/13_spectral_analysis_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/13_spectral_analysis_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Theoretical spectra of different processes

**Source:** [`public/lectures/13_spectral_analysis_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/13_spectral_analysis_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

We have discussed a number of types of processes in this class, so let's look at their theoretical power spectra.

![Examples of spectra of white noise, moving average, and second-order autoregressive process](https://raw.githubusercontent.com/berkeley-stat153/spring-2026/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/images/13_spectra.png)

## White noise

Recall that a white noise process consists of uncorrelated random variables $w_t$ with variance $\sigma_w^2$. The autocovariance of a white noise process is $\gamma_w(h)=\sigma_w^2$ for $h=0$ and $0$ otherwise. Thus it follows that the spectral density function is:

$$f(\omega) = \sum_{h=-\infty}^{h=\infty} \gamma(h)e^{-2\pi i \omega h} = \sigma_w^2$$

for $-1/2 \leq \omega \leq 1/2$. This means that white noise contains equal power at all frequencies. In fact, we spoke before about how the term "white noise" is related to the analogy to white light, which contains all colors (frequencies). In fact, we can think of spectral analysis like separating our signals like a prism into different colors (spectra).

### Linear filtering

An important tool in time series analysis is the concept of linear filtering, where we may want to amplify or attentuate different frequencies in our signal. In general, a linear filter uses a set of specified coefficients $a_j$ for $j=0,\pm 1, \pm2, \dots$, to transform an input series $x_t$ into an output $y_t$:

$$y_t = \sum_{j=-\infty}^{\infty} a_j x_{t-j}, \quad \sum_{j=-\infty}^{\infty} |a_j| < \infty$$

Sometimes this is also written as a convolution: $y_t = (a * x)_t$

Here the frequency behavior is hidden inside of the pattern of the weights $a_j$ - we can't immediately see what these are doing because they're time domain weights. However, we can look at the Fourier transform of these weights (the frequency response function):

$$A(\omega) = \sum_{j=-\infty}^{\infty} a_j e^{-2\pi i \omega j}$$

After applying a filter like this, we can connect this to the output spectrum for our new signal $y_t$, and we have:

$$f_y(\omega) = |A(\omega)|^2 f_x(\omega)$$

For a proof, you can look at Chapter 4 of Shumway and Stoffer (Property 4.3).

One thing that's very nice about this is that convolution in the time domain becomes multiplication in the frequency domain, which makes this representation much more convenient in many time series problems.

Note that this also looks like the property of variances where if $Y=aX$, then $\text{var}(Y)=a^2\text{var}(X)$ assuming $\text{var}(X)$ exists.

## Moving Average

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

Next week we will talk about how to deal with noisiness in the DFT and periodogram through a few different techniques, and we will extend our conversation to time-frequency analysis, where we care about how frequency coefficients change over time.

---

[← Autocovariance vs. spectral distribution functions](03-autocovariance-vs-spectral-distribution-functions.md) · [Up: contents](index.md)
