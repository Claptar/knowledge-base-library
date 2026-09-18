---
title: Risk of James-Stein
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture11-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture11-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture11-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture11-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Risk of James-Stein

$$
\delta^{\text{JS}}(X) = \left(1 - \frac{d-2}{\|X\|^2}\right) X
$$

$$
\implies h(X) = \frac{d-2}{\|X\|^2} X
$$

$$
\|h(X)\|^2 = \frac{(d-2)^2}{\|X\|^2}
$$

$$
\frac{\partial h_i}{\partial x_i}(X) &= \frac{\partial}{\partial x_i} \frac{(d-2)X_i}{\sum_j X_j^2} \\
&= (d-2) \frac{\|X\|^2 - 2X_i^2}{\|X\|^4}
$$

$$
\implies \text{tr}(Dh(X)) &= \frac{d-2}{\|X\|^4} \sum_i (\|X\|^2 - 2X_i^2) \\
&= \frac{(d-2)^2}{\|X\|^2}
$$

$$
\hat{R} &= d + \frac{(d-2)^2}{\|X\|^2} - 2\frac{(d-2)^2}{\|X\|^2} \\
&= d - \frac{(d-2)^2}{\|X\|^2}
$$

$$
R(\theta; \delta_{\text{JS}}) &= d - (d-2)^2 \overbrace{\mathbb{E}\left[\frac{1}{\|X\|^2}\right]}^{> 0} \\
&< d \\
&= R(\theta; X)
$$

---

If $\theta = 0$ then $\mathbb{E}_0\left[\frac{1}{\|X\|^2}\right] = \frac{1}{d-2}$

$$
\implies R(\theta; \delta_{\text{JS}}) = d - (d-2) = 2
$$

Possibly $\ll d$ !

$\theta \to \infty$ then $\mathbb{E}_\theta\left[\frac{1}{\|X\|^2}\right] \approx \frac{1}{\|\theta\|^2}$

$$
\implies R(\theta; \delta_{\text{JS}}) &\approx d - \frac{(d-2)^2}{\|\theta\|^2} \\
&\to d
$$

Smaller and smaller advantage but always better.

**Note** $\delta_{\text{JS}}(X)$ also inadmissible:

$$
\delta_{\text{JS}+}(X) = \left(1 - \frac{d-2}{\|X\|^2}\right)_+ X \quad \text{is strictly better}
$$

**Practically more useful version:**

$$
\delta_{\text{JS}, 2}(X) = \bar{X} + \left(1 - \frac{d-3}{\|X - \bar{X}\mathbf{1}_d\|^2}\right)(X - \bar{X}\mathbf{1}_d)
$$

Dominates $\delta(X) = X$ for $d \ge 4$

Taken to logical extreme, suggestion seems dumb: should everyone @ Berkeley pool their estimates?

**Note** $\mathbb{E}\|\cdot\|^2$ is improved, but $\mathbb{E}(X_i - \theta_i)^2$ may get worse for individual coordinates.

---

[← Stein's Lemma](02-stein-s-lemma.md) · [Up: contents](index.md)
