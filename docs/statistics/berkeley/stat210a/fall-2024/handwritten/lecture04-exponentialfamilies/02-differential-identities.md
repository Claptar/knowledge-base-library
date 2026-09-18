---
title: Differential Identities
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture04-exponentialfamilies.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture04-exponentialfamilies.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture04-exponentialfamilies.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture04-exponentialfamilies.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Differential Identities

Write
$$e^{A(\eta)} = \int e^{\eta' T(x)} h(x) d\mu(x) \qquad (*)$$

We can derive lots of useful identities by differentiating $(*)$ on both sides, pulling derivative inside $\int$ [not always allowed]

**Keener Thm 2.4** For $f : \mathcal{X} \to \mathbb{R}$, let
$$\Xi_f = \left\{ \eta \in \mathbb{R}^s : \int |f| e^{\eta' T} h d\mu < \infty \right\}$$
Then $g(\eta) = \int f e^{\eta' T} h d\mu$ has cts partial derivatives of all orders for $\eta \in \Xi_f^\circ$, & we can get them by differentiating under the $\int$ sign.
$$\Rightarrow \text{ on } \Xi_1^\circ, \quad A(\eta) \text{ has all partial derivatives}$$

**Differentiate once:**
$$\frac{\partial}{\partial \eta_j} e^{A(\eta)} = \frac{\partial}{\partial \eta_j} \int e^{\eta' T(x)} h(x) d\mu(x)$$
$$e^{A(\eta)} \frac{\partial A}{\partial \eta_j}(\eta) = \int T_j(x) e^{\eta' T(x) - A(\eta)} h(x) d\mu(x)$$
$$\Rightarrow \frac{\partial A}{\partial \eta_j}(\eta) = \mathbb{E}_\eta[T_j(X)]$$
$$\nabla A(\eta) = \mathbb{E}_\eta[T(X)]$$

---

**Diff twice:**
$$\frac{\partial^2}{\partial \eta_j \partial \eta_k} e^{A(\eta)} = \frac{\partial^2}{\partial \eta_j \partial \eta_k} \int e^{\eta' T} h d\mu$$
$$e^{A(\eta)} \left( \frac{\partial^2 A}{\partial \eta_j \partial \eta_k} + \underbrace{\frac{\partial A}{\partial \eta_j}}_{\mathbb{E}[T_j]} \underbrace{\frac{\partial A}{\partial \eta_k}}_{\mathbb{E}[T_k]} \right) = \underbrace{\int T_j T_k e^{\eta' T - A(\eta)} h d\mu}_{\mathbb{E}[T_j T_k]}$$
$$\frac{\partial^2 A}{\partial \eta_j \partial \eta_k}(\eta) = \text{Cov}_\eta(T_j, T_k)$$
$$\nabla^2 A(\eta) = \text{Var}_\eta(T(X)) \in \mathbb{R}^{s \times s}$$

### Example: Poisson:
$$T(X) = X, \quad A(\eta) = e^\eta \ (= \lambda)$$
$$\mathbb{E}_\eta[X] = \frac{d}{d\eta} e^\eta = e^\eta = \lambda$$
$$\text{Var}_\eta(X) = \frac{d^2}{d\eta^2} e^\eta = e^\eta = \lambda$$

**NB:** We would get wrong answer by differentiating wrt $\lambda$

---

## Moment-generating function

We can get $k^{\text{th}}$ order moments of $T(X)$ by
1) Differentiating $(*)$ $k$ times, then
2) Dividing by $e^{A(\eta)}$

That is because $M_\eta^T(u) = e^{A(\eta + u) - A(\eta)}$ is the **moment-generating function** (**mgf**) of $T(X)$ when $X \sim P_\eta$

$$\begin{aligned}
M_\eta^{T(X)}(u) &= \mathbb{E}_\eta\left[ e^{u' T(X)} \right] \\
&= \int e^{u' T} e^{\eta' T - A(\eta)} h d\mu \\
&= e^{A(\eta + u) - A(\eta)} \underbrace{\int e^{(\eta + u)' T - A(\eta + u)} h d\mu}_{= 1}
\end{aligned}$$

**Useful for**
- finding moments
- finding dist. of sums of indep. RVs

### Cumulant-generating function
$$K_\eta^T(u) = \log M_\eta^T(u) = A(\eta + u) - A(\eta) \qquad (A \text{ is sometimes called cgf})$$

---

## Other Parameterizations

Sometimes it is more convenient to use a different parameterization:
$$p_\theta(x) = e^{\eta(\theta)' T(x) - B(\theta)} h(x)$$
$$B(\theta) = A(\eta(\theta))$$

Many, many examples, sometimes requires massaging to see that they are exp. fam.s:

### Ex: Normal
$$X \sim N(\mu, \sigma^2) \qquad \mu \in \mathbb{R} \qquad \sigma^2 > 0$$

Let $\theta = (\mu, \sigma^2)$
\$\$\begin{aligned}
p

---

[← Canonical Form](01-canonical-form.md) · [Up: contents](index.md)
