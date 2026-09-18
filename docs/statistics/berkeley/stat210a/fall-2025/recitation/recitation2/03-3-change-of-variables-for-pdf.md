---
title: (3) Change of variables for pdf
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation/recitation2.pdf
source_file: sources/berkeley-stat210a/fall-2025/recitation/recitation2.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`recitation/recitation2.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation/recitation2.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# (3) Change of variables for pdf

$X$: a random variable, $Y = u(X)$

(i) $X$: discrete
$$p_Y(y) = \sum_{x: u(x)=y} p_X(x)$$

(ii) $X$: continuous
$$p_Y(y) = \sum_{x: u(x)=y} p_X(x) \left|\frac{dy}{dx}\right|^{-1} \quad \text{(determinant)}$$

$$\left(\begin{aligned}
&\text{not rigorous:} \\
&\mathbb{P}(Y \in (y-dy, y+dy)) = \mathbb{P}(u(X) \in (y-dy, y+dy)) \\
&\quad = \sum_{x: u(x)=y} \mathbb{P}(X \in (x-dx, x+dx)) \\
&\implies p_Y(y)|dy| = \sum_{x: u(x)=y} p_X(x)|dx|
\end{aligned}\right)$$

**Example) 1** $X_1 \sim \text{Poisson}(\lambda_1)$, $X_2 \sim \text{Poisson}(\lambda_2)$ independent
$$Y = X_1 + X_2$$

$$\begin{aligned}
p_Y(y) &= \sum_{x_1+x_2=y} \frac{e^{-\lambda_1} \lambda_1^{x_1}}{x_1!} \times \frac{e^{-\lambda_2} \lambda_2^{x_2}}{x_2!} \\
&= \frac{e^{-\lambda_1-\lambda_2}}{y!} \sum_{x_1=0}^y \binom{y}{x_1} \lambda_1^{x_1} \lambda_2^{y-x_1} \\
&= \frac{e^{-\lambda_1-\lambda_2}(\lambda_1+\lambda_2)^y}{y!} \quad \text{for } y = 0, 1, 2, \dots \\
\implies Y &\sim \text{Poisson}(\lambda_1 + \lambda_2)
\end{aligned}$$

**2** $X \sim N(0, 1)$, $Y = X^2$

$$p_X(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}x^2}$$

$$\begin{aligned}
p_Y(y) &= \sum_{x: x^2=y} p_X(x) \left|\frac{dy}{dx}\right|^{-1} \\
&= \sum_{x: x^2=y} p_X(x) \times \frac{1}{2|x|} \\
&= \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}y} \times \frac{1}{\sqrt{y}} = \frac{1}{\sqrt{2\pi}} y^{-\frac{1}{2}} e^{-\frac{1}{2}y} \quad \text{for } y > 0
\end{aligned}$$

$$\left(\begin{aligned}
&X \sim \text{Gamma}(k, \theta) \quad (k, \theta > 0) \\
&\text{the pdf of } X \text{ is } f(x) = \frac{1}{\Gamma(k)\theta^k} x^{k-1} e^{-\frac{x}{\theta}}, \quad x > 0 \\
&\implies Y \sim \text{Gamma}\left(\frac{1}{2}, 2\right) \\
&\quad \left(\chi^2(1) \equiv \text{Gamma}\left(\frac{1}{2}, 2\right)\right)
\end{aligned}\right)$$

---

---

[← (2) Moment generating function](02-2-moment-generating-function.md) · [Up: contents](index.md) · (4) Order statistics →
