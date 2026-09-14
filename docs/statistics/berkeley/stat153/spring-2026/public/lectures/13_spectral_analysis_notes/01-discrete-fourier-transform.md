---
title: Discrete Fourier Transform
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/13_spectral_analysis_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/13_spectral_analysis_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Discrete Fourier Transform

**Source:** [`public/lectures/13_spectral_analysis_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/13_spectral_analysis_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

We ended last lecture talking about the *periodogram*, which was defined as:

$$y_t = a_0 + \sum_{j=1}^{\lfloor n/2 \rfloor} [a_j \cos(2\pi t j/n) + b_j \sin(2\pi t j/n)]$$

with $a_j = \frac{2}{n}\sum_{t=1}^n x_t \cos(2\pi t j/n)$ and $b_j = \frac{2}{n}\sum_{t=1}^n x_t \sin(2\pi t j/n)$.

Today we will relate this to the *Discrete Fourier Transform*, which is defined as:

$$d(j/n) = \frac{1}{\sqrt{n}}\sum_{t=1}^n x_t e^{-i 2\pi tj/n}$$

Recalling Euler's formula $e^{-i\theta} = \cos \theta - i \sin \theta$ .

$$ d(j/n) = \frac{1}{\sqrt{n}}\left (\sum_{t=1}^n x_t \cos(2\pi t j/n) - i \sum_{t=1}^n x_t \sin(2\pi t j/n)\right)$$

for $j=0,1,\dots, n-1$ where the frequencies $j/n$ are the Fourier frequencies. We can then compute the squared modulus of the transform, which represents the total strength of a frequency component regardless of the phase. For example, two signals could have very different mixes of sines and cosines for a frequency $j$, but if their moduli are the same, they have the same power at that frequency.

$$|d(j/n)|^2 = \frac{1}{n}\left(\sum_{t=1}^{n} x_t \cos(2\pi t j/n)\right)^2 + \frac{1}{n}\left(\sum_{t=1}^n x_t \sin (2\pi t j/n)\right)^2$$

the scaled periodogram is then

$$P(j/n) = \frac{4}{n} |d(j/n)|^2$$

Note also that $P(j/n) = P(1-j/n)$ for $j=0,1,\dots,n-1$ so we only have to calculate up to $1/2$.

As we saw, the periodogram is a raw, noisy estimate computed from sample data. However, we'd also like to have a way to estimate the true underlying spectral structure, so we need learn about the theoretical quantity that the periodogram is estimating. This is the *spectral density*.

---

[Up: contents](index.md) · [Spectral Density →](02-spectral-density.md)
