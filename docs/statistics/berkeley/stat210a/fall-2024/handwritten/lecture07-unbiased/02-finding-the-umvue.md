---
title: Finding the UMVUE
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture07-unbiased.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture07-unbiased.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture07-unbiased.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture07-unbiased.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Finding the UMVUE

2 methods for finding UMVUE:
1) Find any unbiased estimator based on $T$
2) Find any unbiased estimator at all, then R-B'ize it.

**Ex.** $X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} \text{Pois}(\theta)$, $g(\theta) = \theta^2$

$$p_\theta^{(1)}(x) = \frac{\theta^x e^{-\theta}}{x!} \quad \theta > 0, \quad x = 0, 1, \ldots$$

Complete suff. stat $T(X) = \sum X_i \sim \text{Pois}(n\theta)$

$$p_\theta^T(t) = \frac{(n\theta)^t e^{-n\theta}}{t!}$$

$\delta(T)$ unbiased
$$\iff \sum_{t=0}^\infty \delta(t) p_\theta^T(t) = \theta^2, \quad \forall \theta$$
$$\iff \sum_{t=0}^\infty \delta(t) \frac{n^t}{t!} \theta^t = e^{n\theta} \theta^2 = \sum_{k=0}^\infty \frac{n^k}{k!} \theta^{k+2}, \quad \forall \theta$$

Match terms in power series:
$$\delta(0) = \delta(1) = 0, \quad \delta(t) = \frac{n^{t-2}}{(t-2)!} \cdot \frac{t!}{n^t} \quad t \ge 2$$
$$\implies \delta(T) = \frac{T(T-1)}{n^2} \quad \left( \approx \left(\frac{T}{n}\right)^2 \text{ for large } t \right)$$

---

Alternatively, we could R-B'ize $\delta_0(X) = X_1 X_2$

$$\mathbb{E}_\theta X_1 X_2 = (\mathbb{E}_\theta X_1)(\mathbb{E}_\theta X_2) = \theta^2$$

What is $\delta^*(T) = \mathbb{E}[X_1 X_2 \mid T]$?

$$X \mid T = t \sim \text{Multinom}\left(n, \frac{1}{n} \mathbf{1}_n\right)$$
$$X_1 \mid T = t \sim \text{Binom}\left(n, \frac{1}{n}\right)$$

$$\implies \mathbb{E}[X_1 \mid T] = T/n$$
$$\text{Var}(X_1 \mid T) = T \cdot \frac{1}{n}\left(1 - \frac{1}{n}\right) = \frac{T(n-1)}{n^2}$$
$$\mathbb{E}[X_2 \mid T, X_1] = \frac{T - X_1}{n-1}$$

$$\begin{aligned}
\mathbb{E}[X_1 X_2 \mid T] &= \mathbb{E} \left[ X_1 \mathbb{E}[X_2 \mid T, X_1] \mid T \right] \\
&= \mathbb{E} \left[ \left. \frac{T}{n-1} X_1 - \frac{1}{n-1} X_1^2 \right| T \right] \\
&= \frac{T^2}{n(n-1)} - \frac{1}{n-1} \left( \frac{T^2}{n^2} + \frac{T(n-1)}{n^2} \right) \\
&= \frac{1}{n^2(n-1)} \left( T^2 n - T^2 - T(n-1) \right) \\
&= \frac{T(T-1)}{n^2}
\end{aligned}$$

---

**Ex** $X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} U[0, \theta] \quad \theta > 0$

$T = X_{(n)}$ complete suff.

$$p_\theta^T = \frac{n}{\theta^n} t^{n-1} \mathbf{1}\{t \le \theta\}$$

$$\mathbb{E}_\theta T = \int_0^\theta t \frac{n}{\theta^n} t^{n-1} dt = \frac{n}{n+1} \theta$$

$$\implies \frac{n+1}{n} T \quad \text{is UMVU}$$

**Alternate** $2X_1$ is unbiased

$$X_1 \mid T \sim \begin{cases} T & \text{wp } \frac{1}{n} \\ U[0, T] & \text{wp } \frac{n-1}{n} \end{cases}$$

$$\implies \mathbb{E}[2X_1 \mid T] = 2T \cdot \frac{1}{n} + T \cdot \frac{n-1}{n}$$
$$= \frac{n+1}{n} T$$

Actually, $\frac{n+1}{n} T$ is inadmissible too!

Keener shows $\frac{n+2}{n+1} T$ has best MSE for any estimator $c \cdot T$.

**Raises question:** why do we require 0 bias?

---

## Doubts about unbiasedness

The UMVUE might be very inefficient, or inadmissible, or just dumb, in cases where another approach makes much more sense

**Ex.** $X \sim \text{Bin}(1000, \theta)$

Estimate $g(\theta) = \mathbb{P}_\theta(X \ge 500)$

UMVUE is $\mathbf{1}\{X \ge 500\}$ (why?)

$$\implies X = 500 \text{? Conclude } g(\theta) = 100\%$$
$$X = 499 \text{? Conclude } g(\theta) = 0\%$$

This is not epistemically reasonable!!

Could do much better with e.g. MLE or a Bayes estimator.

In fact, our theorem should make us suspicious of UMVUE's: every idiotic function of $T$ is a UMVUE (of its own expectation)

---

## Gaussian Sequence Model

$X_i \stackrel{\text{iid}}{\sim} N(\mu_i, 1) \quad i = 1, \ldots, d \quad \text{indep.}$

or $X \sim N_d(\mu, I_d) \quad \mu \in \mathbb{R}^d$, estimate $g = \|\mu\|^2$

$X$ is complete sufficient

$$\begin{aligned}
\mathbb{E}_\mu \|X\|^2 &= \mathbb{E}_0 [\|\mu + X\|^2] \\
&= \|\mu\|^2 + \mathbb{E}_0 \|X\|^2 + 2 \mathbb{E}_0 [\mu^T X] \quad (\to 0) \\
&= \|\mu\|^2 + d
\end{aligned}$$

$$\implies \delta(X) = \|X\|^2 - d$$

If $\mu = 0$, $\delta(X) < 0$ about half the time!

$$(\|X\|^2 - d)_+ = \max\left(0, \|X\|^2 - d\right)$$
strictly dominates UMVU

---

[← Outline](01-outline.md) · [Up: contents](index.md)
