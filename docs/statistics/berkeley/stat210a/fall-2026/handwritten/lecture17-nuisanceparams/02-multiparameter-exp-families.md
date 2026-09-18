---
title: Multiparameter Exp. Families
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture17-nuisanceparams.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture17-nuisanceparams.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture17-nuisanceparams.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture17-nuisanceparams.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Multiparameter Exp. Families

Assume $X \sim p_{\theta, \lambda}(x) = e^{\theta' T(x) + \lambda' U(x) - A(\theta, \lambda)} h(x)$

$\theta \in \mathbb{R}^s, \ \lambda \in \mathbb{R}^r$, both unknown

How to test $H_0: \theta \in \Theta_0 \quad$ vs $\quad H_1: \theta \in \Theta_1$?

**Idea**: Condition on $U(X)$ to eliminate dep. on $\lambda$

1) **Sufficiency reduction to $(T(X), U(X))$**

$$(T, U) \sim p_{\theta, \lambda}(t, u) = e^{\theta' t + \lambda' u - A(\theta, \lambda)} g(t, u)$$

density wrt e.g. Lebesgue on $\mathbb{R}^{s+r}$

$$\left[ g(t, u) \, dt \, du = \text{push-forward of } h(x) \, d\mu(x) \right]$$

2) **Condition on $U$:**

$$\begin{aligned}
q_\theta(t \mid u) &= \frac{p_{\theta, \lambda}(t, u)}{\int p_{\theta, \lambda}(z, u) \, dz} \\
&= \frac{e^{\theta' t + \lambda' u - A(\theta, \lambda)} g(t, u)}{\textcolor{red}{e^{B_u(\theta)}} \int e^{\theta' z + \lambda' u - A(\theta, \lambda)} g(z, u) \, dz} \\
&= e^{\theta' t - B_u(\theta)} g(t, u)
\end{aligned}$$

---

3) **Conditional test:**

Test $H_0: \theta \in \Theta_0 \quad$ vs. $\quad H_1: \theta \in \Theta_1$ in

$s$-parameter model $\mathcal{Q}_u = \{ q_\theta(t \mid u) : \theta \in \Theta \}$

**Note** if $s = 1$, this family has MLR in $T$

Even if $s > 1$, we still have gotten rid of $\lambda$

**Ex (Comparing Poissons, Cont'd)**

$$X \sim \text{Pois}(\mu) \qquad Y \sim \text{Pois}(\nu), \qquad X \perp\!\!\!\perp Y$$

$$H_0: \mu \leq \nu \quad \text{vs} \quad H_1: \mu > \nu$$

$$p_{\mu, \nu}(x, y) = \frac{\mu^x e^{-\mu}}{x!} \cdot \frac{\nu^y e^{-\nu}}{y!}$$

$$= e^{x \log \mu + y \log \nu - (\mu + \nu)} \cdot \frac{1}{x! y!}$$

want $T = X, \ u = X + Y$

$$= e^{x(\log \mu - \log \nu) + (x + y) \log \nu - (\mu + \nu)} \frac{1}{x! y!}$$

$$H_0: \mu \leq \nu \iff \log \frac{\mu}{\nu} \leq 0 \quad \left( \iff \frac{\mu}{\mu + \nu} \leq \frac{1}{2} \right)$$

$\rightsquigarrow$ Condition on $U = X + Y$, reject for large $X$

---

## Theorem

Let $\mathcal{P}$ be full rank exp. fam. with densities

$$p_{\theta, \lambda}(x) = e^{\theta T(x) + \lambda' U(x) - A(\theta, \lambda)} h(x)$$

$\theta \in \mathbb{R}, \ \lambda \in \mathbb{R}^r, \ (\theta, \lambda) \in \Omega \text{ open}, \ \Theta_0 \text{ possible}$

a) To test $H_0: \theta \leq \theta_0 \ \text{vs.} \ H_1: \theta > \theta_0$, there is a UMPU test $\phi^*(x) = \psi(T(x); U(x))$ where

$$\psi(t; u) = \begin{cases}
1 & t > c(u) \\
\gamma(u) & t = c(u) \\
0 & t < c(u)
\end{cases}$$

with $c(u), \ \gamma(u)$ chosen to make

$$\mathbb{E}_{\theta_0} [\phi^*(X) \mid U(X) = u] = \alpha$$

b) To test $H_0: \theta = \theta_0 \ \text{vs.} \ H_1: \theta \neq \theta_0$ there is a UMPU test $\phi^*(x) = \psi(T(x); U(x))$ where

$$\psi(t; u) = \begin{cases}
1 & t < c_1(u) \quad \text{or} \quad t > c_2(u) \\
\gamma_i(u) & t = c_i(u) \\
0 & t \in (c_1(u), c_2(u))
\end{cases}$$

with $c_i(u), \ \gamma_i(u)$ chosen to make

$$\mathbb{E}_{\theta_0} [\phi^*(X) \mid U(X) = u] = \alpha$$

$$\mathbb{E}_{\theta_0} [T(X)(\phi^*(X) - \alpha) \mid U(X) = u] = 0$$

[**Note** $\lambda$ has disappeared from the problem.]

---

## Proof Sketch

```
  λ ^
    |       Ω
    |    .---------.
    |   /     |     \
    |  /      |      \
    | |   θ=θ₀|  θ>θ₀:|
    | |Power≤α|Power≥α|
    | |(Bndry)|       |
    |  \      |      /
    |   \     |     /
    |    '----+----'
    |         |
    +---------+---------> θ
             θ₀
```

1) Any unbiased test has $\beta(\theta_0, \lambda) = \alpha \quad \forall \lambda$

   (continuity of $\beta(\theta, \lambda)$)

2) $\text{Power} \equiv \alpha \text{ on boundary} \Rightarrow \mathbb{E}_{\theta_0} [\phi \mid U] \overset{\text{a.s.}}{=} \alpha$

   ($U(X)$ complete sufficient on boundary submodel)

3) $\phi^*$ optimal among all tests with conditional level $\alpha$

   (by reduction to univariate model)

---

---

[← Outline](01-outline.md) · [Up: contents](index.md) · [Proof →](03-proof.md)
