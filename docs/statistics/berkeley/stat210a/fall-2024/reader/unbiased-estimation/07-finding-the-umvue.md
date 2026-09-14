---
title: Finding the UMVUE
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/unbiased-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/unbiased-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Finding the UMVUE

**Source:** [`reader/unbiased-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/unbiased-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Theorem XXX suggests two strategies for finding the UMVUE:

1.  Solve directly for an unbiased estimator based on $T$
2.  Find any unbiased estimator at all, then Rao-Blackwellize it

We give examples of both strategies below:

**Example (Poisson):** Let $X_1, \ldots, X_n \sim \text{Pois}(\theta)$, $g(\theta) = e^{-\theta}$ and consider unbiased estimation for $g(\theta) = \theta^2$.

The complete sufficient statistic for the model is

$$T(X) = \sum X_i \sim \text{Pois}(n\theta),$$
and its probability mass function for $t \geq 0$ is
$$
p_\theta(t) = \frac{e^{-n\theta} (n\theta)^t}{t!}
$$
**Strategy 1**

If there is some unbiased estimator $\delta(t)$, we can try to solve for it by setting its expectation equal to $\theta^2$:
$$
\theta^2 = \EE_\theta \delta(T) = \sum_{t=0}^\infty \delta(t) \frac{e^{-n\theta} (n\theta)^t}{t!}.
$$
Rearranging factors, we obtain matching power series:
$$
\sum_{t=0}^\infty \delta(t) \frac{n^t \theta^t}{t!} = e^{n\theta}\theta^2 =  \sum_{k=0}^\infty \frac{n^k\theta^{k+2}}{k!}.
$$
We will choose the coefficients on the left-hand side to match terms. First, change the index for the left-hand sum to $t = k+2$:
$$
\sum_{t=0}^\infty \delta(t) \frac{n^t \theta^t}{t!} = e^{n\theta}\theta^2 =  \sum_{t=2}^\infty \frac{n^{t-2}\theta^{t}}{(t-2)!}.
$$
To match the terms, we can set $\delta(0)=\delta(1)=0$, and for $t\geq 2$, set $\delta(t)=\frac{t!}{n^2(t-2)!}=\frac{t(t-1)}{n^2}$. The same expression works for both, so we obtain the estimator
$$
\delta(T) = \frac{T(T-1)}{n^2}
$$

**Strategy 2:**

Alternatively, we can find an unbiased estimator and Rao-Blackwellize it. If $n\geq $, we can use the fact that

$$
\EE_\theta [X_1 X_2] = \EE_\theta [X_1] \;\cdot\; \EE_\theta [X_2] = \theta^2
$$
to obtain an initial unbiased estimator $\delta_0(X) = X_1X_2$, which we will Rao-Blackwellize.

Conditional on $

to match the terms


$\delta(T) = (1 - 1/n)^T$ unbiased:

$$\begin{aligned}
\EE_\theta \delta(T) &= \sum_{t=0}^\infty (1-1/n)^t e^{-n\theta} (n\theta)^t / t! \\
&= e^{-n\theta} \sum_{t=0}^\infty ((n-1)\theta)^t / t! \\
&= e^{-n\theta} e^{(n-1)\theta} = e^{-\theta}
\end{aligned}$$

Alternatively, we could Rao-Blackwellize $\delta_0(X) = I(X_1 = 0)$:

$$\begin{aligned}
\EE[I(X_1 = 0) | T] &= \PP(X_1 = 0 | T) \\
&= \frac{\PP(X_1 = 0, X_2 + \cdots + X_n = T)}{\PP(X_2 + \cdots + X_n = T-1) + \PP(X_2 + \cdots + X_n = T)} \\
&= \frac{\binom{n-1}{T} (1/n)^0 (1-1/n)^T}{\binom{n-1}{T-1} (1/n) (1-1/n)^{T-1} + \binom{n-1}{T} (1-1/n)^T} \\
&= \frac{(1-1/n)^T}{T/n + (1-1/n)^T} \\
&= (1-1/n)^T
\end{aligned}$$

**Example:** $X_1, \ldots, X_n \sim U[0, \theta]$, $\theta > 0$

$T = X_{(n)}$ complete sufficient

$p_\theta(t) = n t^{n-1} / \theta^n \cdot I(0 < t < \theta)$

$\EE_\theta[T] = \frac{n}{n+1} \theta$

$T \cdot \frac{n+1}{n}$ is UMVUE

Alternatively, $2X_1$ is unbiased:

$$\EE[2X_1 | T] = 2T \cdot \frac{n+1}{2n} = T \cdot \frac{n+1}{n}$$

Actually, $T$ is inadmissible too! Keener shows $\frac{n-1}{n} T$ has better MSE for any estimator $c \cdot T$.

This raises the question: why do we require zero bias?

The UMVUE is often inefficient, inadmissible, or just dumb in cases where another approach makes much more sense.

**Example:** $X \sim \text{Bin}(1000, \theta)$

Estimate $g(\theta) = I(\theta > 0.5)$

UMVUE is $I(X > 500)$. Why?

-   $X = 500$: Conclude $g(\theta) = 1$
-   $X = 499$: Conclude $g(\theta) = 0$

This is not epistemically reasonable. Could do much better with e.g. MLE or a Bayes estimator.

In fact, our theorem should make us suspicious of UMVUEs: every idiotic function of $T$ is a UMVUE of its own expectation!

**Example:** $X_1, \ldots, X_n \sim N(\mu, 1)$, estimate $g(\mu) = \|\mu\|$

$\bar{X}$ is complete sufficient

$\|\bar{X}\|$ is unbiased: $\EE[\|\bar{X}\|] = \EE[\|N(\mu, 1/n)\|] = \|\mu\|$

So $\|\bar{X}\|$ is UMVUE

If $\mu = 0$, $\delta(\bar{X}) = 0$ about half the time

$\|\bar{X}\| + d \cdot \max(0, \|\bar{X}\| - d)$ strictly dominates UMVUE

---

[← UMVU estimators](06-umvu-estimators.md) · [Up: contents](index.md)
