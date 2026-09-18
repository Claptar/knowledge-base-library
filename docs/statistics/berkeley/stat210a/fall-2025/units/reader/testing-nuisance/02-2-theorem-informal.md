---
title: 2 Theorem (Informal)
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-nuisance.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-nuisance.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/testing-nuisance.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-nuisance.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2 Theorem (Informal)

Let $\cP$ be full rank exp. fam. with densities $p_{\theta, \lambda}(x) = e^{\theta \cdot T(x) + \lambda \cdot U(x) - A(\theta, \lambda)}h(x)$

$\theta \in \mathbb{R}^s$, $\lambda \in \mathbb{R}^r$, $(\theta_0, \lambda_0)$ possible

1.  To test $H_0: \theta = \theta_0$ vs $H_1: \theta \neq \theta_0$, there is a UMPU test $\phi(x) = \psi(T(x), U(x))$ where

$$
\psi(t, u) = \begin{cases}
1 & \text{if } t > c_2(u) \\
\gamma_2(u) & \text{if } t = c_2(u) \\
0 & \text{if } c_1(u) < t < c_2(u) \\
\gamma_1(u) & \text{if } t = c_1(u) \\
1 & \text{if } t < c_1(u)
\end{cases}
$$

```
with $\gamma_1, \gamma_2, c_1, c_2$ chosen to make $\mathbb{E}_{\theta_0}[\phi] = \alpha$ and $\mathbb{E}_{\theta_0}[T\phi] = \theta_0$
```

2.  To test $H_0: \theta \leq \theta_0$ vs $H_1: \theta > \theta_0$, there is a UMPU test $\phi(x) = \psi(T(x), U(x))$ where

$$
\psi(t, u) = \begin{cases}
1 & \text{if } t > c(u) \\
\gamma(u) & \text{if } t = c(u) \\
0 & \text{if } t < c(u)
\end{cases}
$$

```
with $\gamma, c$ chosen to make $\mathbb{E}_{\theta_0}[\phi] = \alpha$
```

Note: $h$ has disappeared from the problem.

## 2.1 Example: Poisson Ratio {.anchored number="2.1" anchor-id="example-poisson-ratio"}

$X_i \sim \text{iid Poisson}(\mu_i)$, $i=1,2$

$H_0: \mu_1 = \mu_2$ vs $H_1: \mu_1 \neq \mu_2$

$$
p(x) = \frac{\mu_1^{x_1} e^{-\mu_1}}{x_1!} \cdot \frac{\mu_2^{x_2} e^{-\mu_2}}{x_2!} = e^{x_1 \log \mu_1 + x_2 \log \mu_2 - \mu_1 - \mu_2}
$$

Let $\theta = \log \frac{\mu_1}{\mu_2}$, $\lambda = \log \mu_2$

$H_0: \theta = 0$ vs $H_1: \theta \neq 0$

Reject for conditionally large values of $X_1$ given $X_1 + X_2 = u$:

$$
P_\theta(X_1 = x_1 | X_1 + X_2 = u) = \frac{e^{\theta x_1}}{\sum_{i=0}^u e^{\theta i}} = \binom{u}{x_1} \left(\frac{e^\theta}{1+e^\theta}\right)^{x_1} \left(\frac{1}{1+e^\theta}\right)^{u-x_1}
$$

$X_1 | X_1 + X_2 \sim \text{Binom}(u, \frac{e^\theta}{1+e^\theta})$

So in the end, we do a Binomial test.

---

[← 1 Nuisance Parameters](01-1-nuisance-parameters.md) · [Up: contents](index.md) · [3 Proof Sketch →](03-3-proof-sketch.md)
