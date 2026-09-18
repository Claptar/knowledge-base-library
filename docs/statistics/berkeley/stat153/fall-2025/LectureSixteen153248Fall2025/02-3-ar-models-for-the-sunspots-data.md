---
title: 3 AR Models for the Sunspots Data
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSixteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSixteen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureSixteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSixteen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 AR Models for the Sunspots Data

For the sunspots dataset, we previously employed the model
$$y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t \quad \text{for } t = 1, \dots, n \tag{2}$$
We used a Bayesian method to infer the frequency parameter $f$ (which is the main parameter of interest) and this led to an estimated period of close to 11 years (which is often cited as the period of the solar cycle). Note however that (2) is not ideal for the sunspots dataset for at least two reasons: (a) the fit to the data is not very good (some of the oscillations have a much higher amplitude than that explained by the single sinusoid), (b) data generated from the model (2) look much more "noisy" compared to the actual sunspots data. Starting with these observations, Yule [1] proposed an alternative model that is also based on a single sinuosoid. This alternative model is based on the idea of AR modeling.

Yule started with the following basic observation. Let $s_t$ denote the sinusoid:
$$s_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) \tag{3}$$
The same sinusoid can be understood as the solution to a specific *difference equation*. To derive the difference equation, let us first note that, in continuous time, $s(t)$ satisfies
$$s''(t) = -(2\pi f)^2 (\beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t)) = -(2\pi f)^2 (s(t) - \beta_0). \tag{4}$$
In discrete time (where $t \in \{\dots, -2, -1, 0, 1, 2, \dots\}$), the sequence (3) satisfies the following difference equation that is analogous to (4):
$$s_t - 2s_{t-1} + s_{t-2} = 2(\cos(2\pi f) - 1) (s_{t-1} - \beta_0). \tag{5}$$

To see this, note that (below we take $\omega = 2\pi f$ for notational simplicity)
$$s_t - 2s_{t-1} + s_{t-2} = \beta_1 (\cos(\omega t) - 2\cos(\omega(t - 1)) + \cos(\omega(t - 2))) + \beta_2 (\sin(\omega t) - 2\sin(\omega(t - 1)) + \sin(\omega(t - 2)))$$
Writing $A = \omega(t - 1)$ and $B = \omega$, we get
$$\begin{aligned}
\cos(\omega t) - 2\cos(\omega(t - 1)) + \cos(\omega(t - 2)) &= \cos(A + B) - 2\cos A + \cos(A - B) \\
&= 2\cos A(\cos B - 1) \\
&= 2(\cos \omega - 1)\cos(\omega(t - 1))
\end{aligned}$$
and similarly
$$\sin(\omega t) - 2\sin(\omega(t - 1)) + \sin(\omega(t - 2)) = 2(\cos \omega - 1)\sin(\omega(t - 1)).$$
This proves
$$\begin{aligned}
s_t - 2s_{t-1} + s_{t-2} &= 2(\cos \omega - 1)(\beta_1 \cos(\omega(t - 1)) + \beta_2 \sin(\omega(t - 1))) \\
&= 2(\cos \omega - 1)(s_{t-1} - \beta_0)
\end{aligned}$$
thereby establishing (5).

The converse is also true in the sense that every solution $\{s_t\}$ to the difference equation (5) say, for $t = 1, 2, 3, \dots$, with given values of $s_1$ and $s_2$ (initial conditions) is of the form (3) for some $\beta_1$ and $\beta_2$. To see this, let $g_t = s_t - \beta_0$ and note that $\{g_t\}$ satisfies
$$g_t - 2g_{t-1} + g_{t-2} = 2(\cos \omega - 1)g_{t-1}.$$
We find $\beta_1$ and $\beta_2$ such that (note again that $\omega = 2\pi f$)
$$h_t := \beta_1 \cos(\omega t) + \beta_2 \sin(\omega t)$$
matches $g_t$ for $t = 1, 2$. Now if $g_{t-1} = h_{t-1}$ and $g_{t-2} = h_{t-2}$, then
$$\begin{aligned}
g_t &= (2\cos \omega)g_{t-1} - g_{t-2} \\
&= (2\cos \omega)h_{t-1} - h_{t-2} \\
&= (2\cos \omega)(\beta_1 \cos(\omega(t - 1)) + \beta_2 \sin(\omega(t - 1))) - (\beta_1 \cos(\omega(t - 2)) + \beta_2 \sin(\omega(t - 2))) \\
&= \beta_1 (2\cos \omega \cos(\omega(t - 1)) - \cos(\omega(t - 2))) + \beta_2 (2\cos \omega \sin(\omega(t - 1)) - \sin(\omega(t - 2))).
\end{aligned}$$
Verify that
$$2\cos \omega \cos(\omega(t - 1)) - \cos(\omega(t - 2)) = \cos(\omega t)$$
and
$$2\cos \omega \sin(\omega(t - 1)) - \sin(\omega(t - 2)) = \sin(\omega t),$$
which gives
$$g_t = \beta_1 \cos(\omega t) + \beta_2 \sin(\omega t) = h_t.$$
We thus proved that if $g_{t-1} = h_{t-1}$ and $g_{t-2} = h_{t-2}$, then $g_t = h_t$. Using this for $t = 1, 2, \dots$ proves that (3) is the unique solution to (5).

To summarize, an alternative way of describing a sinusoid of frequency $\omega = 2\pi f$ is via the difference equation (5) which is equivalent to
$$s_t = (2\cos \omega)s_{t-1} - s_{t-2} + 2(1 - \cos \omega)\beta_0.$$

Based on this equation, Yule proposed the model:
$$y_t = \phi_0 + \phi_1 y_{t-1} - y_{t-2} + \epsilon_t \tag{6}$$
with two parameters $\phi_0$ and $\phi_1$ (and the additional noise parameter $\sigma$ in $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$). Note that (6) is also a single sinusoid plus noise model but now the noise is in a different place.

To better understand the difference between (6) and the earlier model (2), consider the following physical situation where sinusoids naturally arise (see e.g., page 2 of the Fourier Analysis book by Stein and Shakarchi). Consider a mass $m$ that is attached to a horizontal spring, which itself is attached to fixed wall, and assume that the system lies on a frictionless surface. Suppose that $\beta_0$ is the location of the center of the mass when the spring is neither compressed or stretched. When the spring is compressed or stretched and released, the mass undergoes simple harmonic motion.

Let \$s(

---

[← 2 AR (Auto-Regressive) Models](01-2-ar-auto-regressive-models.md) · [Up: contents](index.md)
