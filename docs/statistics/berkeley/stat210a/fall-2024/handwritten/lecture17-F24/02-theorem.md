---
title: Theorem
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture17-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture17-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture17-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture17-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Theorem

Let $\mathcal{P}$ be full rank exp. fam. with densities
$$p_{\theta, \lambda}(x) = e^{\theta T(x) + \lambda' U(x) - A(\theta, \lambda)} h(x)$$
$\theta \in \mathbb{R}$, $\lambda \in \mathbb{R}^r$, $(\theta, \lambda) \in \Omega$ open, $\theta_0$ possible

a) To test $H_0 : \theta \le \theta_0$ vs. $H_1 : \theta > \theta_0$, there is a UMPU test $\phi^*(x) = \psi(T(x); U(x))$ where
$$\psi(t; u) = \begin{cases}
1 & t > c(u) \\
\gamma(u) & t = c(u) \\
0 & t < c(u)
\end{cases}$$
with $c(u)$, $\gamma(u)$ chosen to make
$$\mathbb{E}_{\theta_0} [\phi^*(x) \mid U(x) = u] = \alpha$$

b) To test $H_0 : \theta = \theta_0$ vs. $H_1 : \theta \ne \theta_0$, there is a UMPU test $\phi^*(x) = \psi(T(x); U(x))$ where
$$\psi(t; u) = \begin{cases}
1 & t < c_1(u) \text{ or } t > c_2(u) \\
\gamma_i(u) & t = c_i(u) \\
0 & t \in (c_1(u), c_2(u))
\end{cases}$$
with $c_i(u)$, $\gamma_i(u)$ chosen to make
$$\mathbb{E}_{\theta_0} [\phi^*(x) \mid U(x) = u] = \alpha$$
$$\mathbb{E}_{\theta_0} [T(x)(\phi^*(x) - \alpha) \mid U(x) = u] = 0$$

[**Note** $\lambda$ has disappeared from the problem.]

---

**Ex:** $X_i \overset{\text{ind.}}{\sim} \text{Pois}(\mu_i) \quad i = 1, 2$

$H_0 : \mu_1 \le \mu_2$ vs. $H_1 : \mu_1 > \mu_2$

$$p_\mu(x) = \prod_{i=1}^2 \frac{\mu_i^{X_i} e^{-\mu_i}}{X_i!}$$
$$= e^{X_1 \eta_1 + X_2 \eta_2 - (e^{\eta_1} + e^{\eta_2})} \frac{1}{X_1! X_2!}$$

(where $\eta_i = \log \mu_i$. $H_0 : \eta_1 \le \eta_2 \quad H_1 : \eta_1 > \eta_2$)

$$= e^{\overbrace{X_1}^{T(X)} \overbrace{(\eta_1 - \eta_2)}^\theta + \overbrace{(X_1 + X_2)}^{u(x)} \overbrace{\eta_2}^\lambda - A(\eta)} \frac{1}{X_1! X_2!}$$

$H_0 : \theta \le 0$ vs $H_1 : \theta > 0$

Reject for **conditionally** large values of $X_1$, given $X_1 + X_2 = u$

$$\begin{aligned}
P_\theta(X_1 = x_1 \mid U = u) &= \left. e^{x_1 \theta + u \lambda - A(\cdot)} \frac{1}{x_1! (u - x_1)!} \middle/ \sum_{x_1=0}^u (\cdot) \right. \\
&\propto_{x_1} e^{x_1 \theta} \frac{u!}{x_1! (u - x_1)!} \\
&= \text{Binom}\left(u, \frac{e^\theta}{1 + e^\theta}\right) \qquad e^\theta = \mu_1 / \mu_2 \\
&= \text{Binom}\left(u, \frac{\mu_1}{\mu_1 + \mu_2}\right)
\end{aligned}$$

So in the end we do a Binomial test.

---

## Proof Sketch

```
  λ ^                Ω
    |           .---------.
    |          /           \
    |         /             \
    |        |   θ = θ₀:     \     θ > θ₀:
    |        |   Power ≤ α    |    Power ≥ α
    |        |  (Boundary)    |
    |        |                |
    |         \              /
    |          \            /
    |           '----------'
    |                 :
    +-----------------+-------------> θ
                      θ₀
```

1) Any unbiased test has $\beta(\theta_0, \lambda) = \alpha \quad \forall \lambda$ (continuity)

2) $\text{Power} \equiv \alpha \text{ on boundary} \Rightarrow \mathbb{E}_{\theta_0} [\phi \mid U] \overset{\text{a.s.}}{=} \alpha$
($U(X)$ complete sufficient on boundary submodel)

3) $\phi^*$ optimal among all tests with conditional level $\alpha$ (by reduction to univariate model)

---

---

[← Outline](01-outline.md) · [Up: contents](index.md) · [Proof →](03-proof.md)
