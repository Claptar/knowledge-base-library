---
title: Finding the UMVUE
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/unbiased-estimation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/unbiased-estimation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Finding the UMVUE

**Source:** [`reader/unbiased-estimation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/unbiased-estimation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

We have two strategies for finding the UMVUE:

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

Alternatively, we can find an unbiased estimator and Rao-Blackwellize it. If $n\geq 2$, we can use the fact that

$$
\EE_\theta [X_1 X_2] = \EE_\theta [X_1] \;\cdot\; \EE_\theta [X_2] = \theta^2
$$
to obtain an initial unbiased estimator $\delta_0(X) = X_1X_2$, which we will Rao-Blackwellize.

Our calculation begins by recalling that, conditional on $T$, we have
$$
(X_1,\ldots,X_n) \mid T=t \sim \text{Multinom}\left(t, \frac{1}{n}1_n\right),
$$
so that, in particular, $X_1 \mid T=t \sim \text{Binom}(t, \frac{1}{n})$, which has mean $t/n$ and variance $t\frac{1}{n}\cdot (1-\frac{1}{n}) = \frac{(n-1)t}{n^2}$ Likewise, conditional on $X_1$ and $T$, we have
$$
(X_2,\ldots,X_n) \mid T=t, X_1=x_1 \sim \text{Multinom}\left(t-x_1, \frac{1}{n-1}1_{n-1}\right),
$$
where $1_n = (1,\ldots,1) \in \RR^n$, so we likewise have $X_2 \mid T=t, X_1=x_1 \sim \text{Binom}(t-x_1, \frac{1}{n-1})$.

Hence, we can write
$$
\begin{aligned}
\EE\left[\, X_1 X_2 \mid T \,\right]
&= \EE\left[\, X_1 \EE[X_2 \mid T, X_1] \mid T\,\right]\\[5pt]
&= \EE\left[\, X_1 \frac{T-X_1}{n-1} \mid T\,\right]\\[5pt]
&= \frac{1}{n-1}\cdot\EE[X_1 T - X_1^2 \mid T]\\[5pt]
&= \frac{1}{n-1}\cdot\left(T^2/n - \left[\frac{T (n-1)}{n^2}+\left(T/n\right)^2\right]\right)\\[5pt]
&= \frac{T(T-1)}{n^2},
\end{aligned}
$$
giving  us the same answer as above (as we knew it had to).


**Example:** $X_1, \ldots, X_n \sim U[0, \theta]$, $\theta > 0$

The complete sufficient statistic for the model is $T = X_{(n)}$, and its pdf is
$$
p_\theta(t) = n t^{n-1} / \theta^n \cdot 1\{0 < t < \theta\}
$$

**Strategy 1**

We can start by just checking how far off $T$ is from being an unbiased estimator, and see if we can correct it. From the density above we can recognize that $T/\theta$ follows a $\text{Beta}(n,1)$ distribution, which has mean $\frac{n}{n+1}$ and variance $\frac{n}{(n+1)^2(n+2)}$ (we could also compute these easily enough by integration).

As a result, we have $\EE_\theta[T] = \frac{n}{n+1} \theta$, so $\frac{n+1}{n} T$ is unbiased, and therefore UMVU.

**Strategy 2**

Alternatively, we could observe that $2X_1$ is unbiased and try to Rao-Blackwellize it. To do this we need to find the conditional distribution of $X$ given that $X_{(n)}=t$. To warm up, let's just condition on $X_{(n)} = t$ *and* $X_n$ is the maximum. This is equivalent to conditioning on $X_n = t$ and $X_1,\ldots,X_{n-1} \leq t$. In that case, $X_n$ is deterministically $t$ and we have
$$
X_1,\ldots,X_{n-1} \mid \max_{i\leq n} X_i \leq t, X_n =t \simiid \text{Unif}[0,t].
$$
More generally, define $I^*(X)$ to be the maximizing index. We've just calculated the distribution of $T(X)$ given $I^*(X)=n$ and $T(X)=t$. Since the data are exchangeable (or by Basu's theorem) $I^*(X)$ is also independent of $T(X)$. So the conditional distribution of $X_1$ is that its $t$ if $I^*(X)=1$, which happens with probability $1/n$, and it's $\text{Unif}[0,t]$ otherwise. Wrapping up, we have

$$
\begin{aligned}
\EE[X_1 \mid T=t]
&= \frac{1}{n}\EE[X_1 \mid T=t, I^*=1] + \frac{n-1}{n}\EE[X_1 \mid T=t, I^* \neq 1]\\
&= \frac{t}{n} + \frac{t(n-1)}{2n}\\
&= \frac{t(n+1)}{2n}
\end{aligned}
$$
Hence $\EE[2X_1 \mid T] = \frac{n+1}{n} T$, giving the same estimator as we saw before.

**A better estimator**

Unfortunately, the estimator we just calculated twice is inadmissible.

For any estimator $cT$, we can calculate its MSE as the squared bias plus the variance

$$
\begin{aligned}
\text{MSE}(\theta; cT)
&= (\EE_\theta [cT] - \theta)^2 + \Var_\theta(cT)\\
&= (c \EE_\theta [T] - \theta)^2 + c^2\Var_\theta(T)\\
&= \theta^2\left[(c \EE_\theta [T/\theta] - 1)^2 + c^2\Var_\theta(T/\theta)\right]\\
&= \theta^2\left[\left(\frac{cn}{n+1}-1\right)^2 + \frac{c^2n}{(n+1)^2(n+2)}\right].
\end{aligned}
$$
The final expression is a quadratic in $c$, which is minimized at $c^* = \frac{n+2}{n+1}$. Thus, $\frac{n+2}{n+1}T$ has a lower MSE than $\frac{n+1}{n}T$ *for every value of $\theta$*. By scaling down our estimator a bit, we reduce its variance enough to compensate for the bias we have introduced.

Thus, we see that by introducing the unbiasedness constraint we have ruled out *all admissible estimators* and are left only with inadmissible ones, the best of which is $\frac{n+1}{n}T$.

---

[← UMVU estimators](04-umvu-estimators.md) · [Up: contents](index.md) · [Doubts about unbiasedness →](06-doubts-about-unbiasedness.md)
