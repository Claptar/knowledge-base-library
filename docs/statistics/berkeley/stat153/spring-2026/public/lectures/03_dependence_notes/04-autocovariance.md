---
title: Autocovariance
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/03_dependence_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/03_dependence_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Autocovariance

**Source:** [`public/lectures/03_dependence_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/03_dependence_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

What if we instead want to know something about the dependence between two points $s$ and $t$ within the same time series. We'll call this *autocovariance*, $\gamma$.

$\gamma_x(s,t) = \operatorname{cov}(x_s,x_t) = \mathbb{E}[(x_s-\mu_s)(x_t-\mu_t)]$

When $s=t$, we have:

$\gamma_x(t,t) = \mathbb{E}[(x_t-\mu_t)^2] = \operatorname{Var}(x_t)$

For white noise, there should be no dependence between differing time points. By definition, $\mathbb{E}(w_t)=0$ and:


$$
\gamma_w(s,t) = \operatorname{cov}(w_s,w_t) =
\begin{cases}
\sigma^2_w, & \text{if } s=t, \\
0, & s \neq t
\end{cases}
$$

## Covariance of linear combinations

If we have random variables $U=\displaystyle\sum_{j=1}^m a_j X_j$ and $V=\displaystyle\sum_{k=1}^r b_k Y_k$ that are linear combinations of (finite variance) random variables ${X_j}$ and ${Y_k}$, then the covariance of these is:

$\operatorname{cov}(U,V) = \displaystyle\sum_{j=1}^m \displaystyle\sum_{k=1}^r a_j b_k \operatorname{cov}(X_j, Y_k)$

Also, $\operatorname{var}(U) = \operatorname{cov}(U,U)$.

So how can we use this? Now we can try this for the moving average example.

$$
\begin{aligned}
\gamma_v(s,t) = \operatorname{cov}(v_s, v_t) &= \operatorname{cov}(\tfrac{1}{3}(w_{s-1}+w_s+w_{s+1}), \tfrac{1}{3}(w_{t-1}+w_t+w_{t+1})) \\
&= \tfrac{1}{9} \operatorname{cov}(w_{s-1}+w_s+w_{s+1}, w_{t-1}+w_t+w_{t+1})
\end{aligned}
$$

When $s=t$, we have:
$$
\begin{aligned}
\gamma_v(t,t) &= \operatorname{cov}(v_t, v_t) \\
&= \operatorname{cov}(\tfrac{1}{3}(w_{t-1}+w_t+w_{t+1}), \tfrac{1}{3}(w_{t-1}+w_t+w_{t+1})) \\
&= \tfrac{1}{9} (\operatorname{cov}(w_{t-1},w_{t-1}) + \operatorname{cov}(w_{t},w_{t}) + \operatorname{cov}(w_{t+1},w_{t+1}) \\
&\quad + 2\operatorname{cov}(w_{t-1}, w_t)) + 2\operatorname{cov}(w_{t}, w_{t+1})) + 2\operatorname{cov}(w_{t-1}, w_{t+1}))\\
&= \tfrac{1}{9} (\sigma_w^2 + \sigma_w^2 + \sigma_w^2 + 0 +0 +0)\\
&= \tfrac{3}{9} \sigma_w^2 \\
&= \tfrac{1}{3} \sigma_w^2
\end{aligned}
$$

When $s=t+1$, we have:
$$
\begin{aligned}
\gamma_v(t+1,t) &= \operatorname{cov}(\tfrac{1}{3}(w_{t}+w_{t+1}+w_{t+2}), \tfrac{1}{3}(w_{t-1}+w_t+w_{t+1})) \\
&= \tfrac{1}{9}(\operatorname{cov}(w_t,w_t)\\
	&\quad +\operatorname{cov}(w_{t+1},w_{t+1}))\\
	&\quad +\operatorname{cov}(w_{t},w_{t-1})\\
	&\quad +\operatorname{cov}(w_{t},w_{t+1})\\
	&\quad +\operatorname{cov}(w_{t+1},w_{t-1})\\
	&\quad +\operatorname{cov}(w_{t+1},w_{t})\\
	&\quad +\operatorname{cov}(w_{t+2},w_{t-1})\\
	&\quad +\operatorname{cov}(w_{t+2},w_{t})\\
	&\quad +\operatorname{cov}(w_{t+2},w_{t+1}))\\
&= \tfrac{1}{9}(\operatorname{cov}(w_t,w_t)+\operatorname{cov}(w_{t+1},w_{t+1}))\\
&= \tfrac{2}{9}\sigma^2_w
\end{aligned}
$$

If we then follow this for more lags, we get:

$$
\gamma_v(s,t) =
\begin{cases}
\tfrac{3}{9}\sigma^2_w, & \text{if } s=t, \\
\tfrac{2}{9}\sigma^2_w, & \text{if } |s-t|=1, \\
\tfrac{1}{9}\sigma^2_w, & \text{if } |s-t|=2, \\
0, & \text{if } |s-t|>2
\end{cases}
$$

Why is this interesting? The autocovariance depends only on the *lag* between $s$ and $t$ and not on the absolute location of these time points. We'll come back to this when we talk about *stationarity*.

---

[← Mean and variance](03-mean-and-variance.md) · [Up: contents](index.md)
