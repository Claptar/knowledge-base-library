---
title: 2 The Sinusoid
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeven153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureSeven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 The Sinusoid

When we say sinusoid, we refer to the following function of time $t$:
$$s(t) := \beta_0 + R \cos(2\pi f t + \phi) \tag{2}$$
Here
* $R$ is called the *amplitude*. It represents the height of the oscillation from its center line.
* $f$ is called the *frequency*. It represents the number of oscillations in unit time. If time is measured in seconds, then the unit of $f$ is Hertz (Hz).
* $1/f$ is called the *period*. It is the length of time to complete one full oscillation.
* $\phi$ is called the *phase*. Without $\phi$ (i.e., if $\phi = 0$), then the above sinusoid becomes $\beta_0 + R \cos(2\pi f t)$ so it starts at its maximum value at $t = 0$. Adding $\phi$ shifts the wave left or right in time. This captures the fact that different oscillations might 'start' at different points in their cycle.
* $2\pi f$ is called the *angular frequency*. Sometimes we use the notation $\omega = 2\pi f$ for the angular frequency. It measures the rate of change of the angle inside the cosine.

Using the formula $\cos(\alpha + \beta) = (\cos \alpha)(\cos \beta) - (\sin \alpha)(\sin \beta)$, we can represent the sinusoid (2) in the following equivalent alternative form:
$$s(t) = \beta_0 + \beta_1 \cos 2\pi f t + \beta_2 \sin 2\pi f t. \tag{3}$$
The parameters $\beta_1, \beta_2$ in (3) are related to $R, \phi$ in (2) via $\beta_1 = R \cos \phi$ and $\beta_2 = R \sin \phi$. While working with models involving sinusoids, we use the representation (3) because the parameters $\beta_1$ and $\beta_2$ appear linearly in (3).

---

← 1 The Sinusoidal Model · [Up: contents](index.md) · [3 Discrete sampling and restricting $f$ to $[0, 1/2]$ →](03-3-discrete-sampling-and-restricting-to.md)
