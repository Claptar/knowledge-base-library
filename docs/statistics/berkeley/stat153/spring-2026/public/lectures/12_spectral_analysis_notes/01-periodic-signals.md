---
title: Periodic signals
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/12_spectral_analysis_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/12_spectral_analysis_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Periodic signals

**Source:** [`public/lectures/12_spectral_analysis_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/12_spectral_analysis_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

We spoke previously about periodic signals

$$y(t) := \beta_0 + R \cos (2\pi f t + \phi)$$

which can also be re-parameterized as

$$y(t) = \beta_0 + U_1 \cos 2\pi ft + U_2 \sin 2\pi ft$$

where $U_1=A\cos\phi$ and $U_2=-R\sin\phi$, and $U_1$ and $U_2$ are taken to be normally distributed random variables. The amplitude is $A=\sqrt{U_1^2+U_2^2}$ and the phase is $\phi=\arctan (U_2/U_1)$. If we assume that $U_1$ and $U_2$ are uncorrelated random variables with mean 0 and variance $\sigma^2$, then we also can show that $$y(t)$$ is stationary because $\mathbb{E}(y_t)=0$ and $\lambda = 2\pi f$:

$$
\begin{aligned}
\gamma_y(t,s) &= \text{cov}(y_t, y_s)\\
&= \text{cov} (U_1 \cos(\lambda t) + U_2 \sin (\lambda t), U_1 \cos(\lambda s) + U_2 \sin (\lambda s))\\
&= \text{cov} (U_1 \cos(\lambda t),U_1 \cos(\lambda s)) + \text{cov} (U_1 \cos(\lambda t),U_2 \sin(\lambda s)) + \\
& \quad \text{cov} (U_2 \sin(\lambda t),U_1 \cos(\lambda s)) +\\
& \quad \text{cov} (U_2 \sin(\lambda t),U_2 \sin(\lambda s))\\
&= \sigma^2 \cos (\lambda t) \cos (\lambda s) + 0 + 0 + \sigma^2 \sin (\lambda t) \sin(\lambda s)\\
&= \sigma^2 [\cos (\lambda t) \cos (\lambda s) + \sin (\lambda t) \sin (\lambda s)]\\
&= \sigma^2 \cos (\lambda(t-s))
\end{aligned}
$$

Because this quantity depends only on the time lag $t-s$. We can create a generalization of this signal that allows mixtures of periodic signals with multiple freqauencies and amplitudes:

$$y_t = \sum_{k=1}^q [U_{k1}\cos(2\pi f_k t) + U_{k2}\sin(2\pi f_k t)]$$

where $U_{k1},U_{k2}$ for $k=1,2,\dots,q$ are uncorrelated zero-mean random variables with variances $\sigma^2_k$ and $f_k$ are distinct frequencies.

Let's look at some examples of these mixtures of frequencies in the accompanying jupyter notebook.

---

[Up: contents](index.md) · [Periodogram →](02-periodogram.md)
