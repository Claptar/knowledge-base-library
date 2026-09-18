---
title: 2 Stein’s Unbiased Risk Estimator
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/empirical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/reader/empirical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/empirical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/empirical-bayes.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2 Stein’s Unbiased Risk Estimator

## 2.1 Stein’s Lemma {.anchored number="2.1" anchor-id="steins-lemma"}

The first ingredient in finding the MSE of $\delta_\text{JS}$ is a lemma called *Stein’s Lemma*:

**Theorem (Stein’s lemma, univariate):** Suppose $X \sim N(\theta, \sigma^2)$, and that $h:\; \RR \to \RR$ is differentiable, with $\EE|\dot{h}(X)| < \infty$. Then we have

$$
\Cov(X, h(X)) = \EE[(X-\theta)h(X)] = \sigma^2\EE[\dot{h}(X)].
$$

*Proof*:

Next, we will do the calculation for $\theta = 0$ and $\sigma^2 = 1$. Then

$$
\EE[Xh(X)] = \int_{-\infty}^\infty xh(x)\phi(x)\,dx = \int_{-\infty}^\infty \dot{h}(x)\phi(x)\,dx,
$$

 where we’ve used integration by parts:

$$
\dot{\phi}(x) = \frac{d}{dx} \frac{1}{\sqrt{2\pi}}e^{-x^2/2} = -x \frac{1}{\sqrt{2\pi}}e^{-x^2/2} = -x\phi(x).
$$

 (A slightly more rigorous version is in the handwritten notes: we can assume wlog $h(0) = 0$ because otherwise we could center it by using $k(X) = h(X) - h(0)$, which has the same covariance with $X$. Then we can break up the integral into an integral from $0$ to $\infty$ and another from $-\infty$ to $0$, and do integration by parts a bit more carefully for each.)

For more general $\theta$, we can write $X = \theta + \sigma Z$, where $Z \sim N(0,1)$. Then applying the result for $k(z) = h(\theta + \sigma z)$, we have

$$
\EE[(X-\theta) h(X)] = \sigma\EE[Zh(\theta + \sigma Z)] = \sigma^2\EE[\dot{h}(\theta + \sigma Z)] = \sigma^2\EE[\dot{h}(X)],
$$

 giving the general result.

We will need the multivariate version of Stein’s lemma. For a function $h:\; \RR^d \to \RR^d$, define the Jacobian matrix $Dh \in \RR^{d\times d}$ by

$$
(Dh(x))_{ij} = \frac{\partial h_i}{\partial x_j}(x).
$$

Define the **Frobenius norm** $A \in \RR^{d\times d}$ as

$$
\|A\|_F = (\sum_{ij} A_{ij}^2)^{1/2}.
$$

Now we can state our theorem:

**Theorem (Stein’s lemma, multivariate):** Assume $X \sim N_d(\theta; \sigma^2 I_d)$, and $h:\;\RR^d \to \RR^d$ is differentiable with $\EE\|Dh(X)\|_F < \infty$. Then

$$
\EE[(X-\theta)'h(X)] = \sigma^2 \EE \text{tr}(Dh(X)) = \sigma^2 \sum_i \EE \frac{\partial h_i}{\partial x_i} (X).
$$

The proof follows easily from the proof of the univariate version, and appears in the handwritten notes.

## 2.2 Stein’s unbaised risk estimator (SURE) {.anchored number="2.2" anchor-id="steins-unbaised-risk-estimator-sure"}

## 2.3 Risk of James-Stein {.anchored number="2.3" anchor-id="risk-of-james-stein"}

---

[← 1 Gaussian sequence model](01-1-gaussian-sequence-model.md) · [Up: contents](index.md) · [3 Empirical Bayes →](03-3-empirical-bayes.md)
