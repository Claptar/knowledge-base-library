---
title: Mean and variance {#mean-and-variance}
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec03_Notes.tex
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lec03_Notes.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Mean and variance {#mean-and-variance}

**Source:** [`public/lectures/Lec03_Notes.tex`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec03_Notes.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Last week and in your lab, we saw the concept of how mean and variance differ for a white noise process, a random walk, and a random walk with drift. The *mean* and *variance functions* of a time series are useful descriptors because they helps us determine something about the drift and the spread of the data that we should expect over time.

The *mean function* is defined as $\mu_{xt} = \mathbb{E}(x_t)$

The *variance function* is $\sigma^2_t = \operatorname{Var}(x_t) = \mathbb{E}[(x_t -\mu_t)^2]$.

Let’s revisit some examples from before:

## White noise {#white-noise}

For a white noise time series, $\mu_{wt} = \mathbb{E}(w_t)=0$ for all $t$. $\operatorname{Var}(w_t) = 1$ (for a Gaussian white noise series).

## Moving average {#moving-average}

What if we apply a 3-point moving average? Although this induces some correlation structure, it actually does not change the mean function at all:

$\mu_{vt} = \mathbb{E}(v_t) = \frac{1}{3}[\mathbb{E}(w_{t -1})+\mathbb{E}(w_{t})+\mathbb{E}(w_{t+1})] = 0$

## Random walk with drift {#random-walk-with-drift}

For the random walk with drift, the mean function is just the line $\mu_{xt} = \delta t + \displaystyle\sum_{j=1}^t E(w_j) = \delta t$.

## Signal plus noise {#signal-plus-noise}

And for a signal plus noise (as an example, we’ll use this sinusoid):

$$\begin{equation}
\begin{aligned}
\mu_{xt} = \mathbb{E}(x_t) &= \mathbb{E} [A \cos(2\pi \omega t + \phi) + w_t] \\
&= \mathbb{E} [A \cos(2\pi \omega t + \phi)] + \mathbb{E}[w_t] \\
&= \mathbb{E} [A \cos(2\pi \omega t + \phi)]
\end{aligned}
\end{equation}$$

## Autocovariance {#autocovariance}

What if we instead want to know something about the dependence between two points $s$ and $t$ within the same time series. We’ll call this *autocovariance*, $\gamma$.

$\gamma_x(s,t) = \operatorname{cov}(x_s,x_t) = \mathbb{E}[(x_s -\mu_s)(x_t -\mu_t)]$

When $s=t$, we have:

$\gamma_x(t,t) = \mathbb{E}[(x_t -\mu_t)^2] = \operatorname{Var}(x_t)$

For white noise, there should be no dependence between differing time points. By definition, $\mathbb{E}(w_t)=0$ and:

$$\begin{equation}
\gamma_w(s,t) = \operatorname{cov}(w_s,w_t) =
\begin{cases}
\sigma^2_w, & \text{if } s=t, \\
0, & s \neq t
\end{cases}
\end{equation}$$

## Covariance of linear combinations {#covariance-of-linear-combinations}

If we have random variables $U=\displaystyle\sum_{j=1}^m a_j X_j$ and $V=\displaystyle\sum_{k=1}^r b_k Y_k$ that are linear combinations of (finite variance) random variables ${X_j}$ and ${Y_k}$, then the covariance of these is:

$\operatorname{cov}(U,V) = \displaystyle\sum_{j=1}^m \displaystyle\sum_{k=1}^r a_j b_k \operatorname{cov}(X_j, Y_k)$

Also, $\operatorname{var}(U) = \operatorname{cov}(U,U)$.

So how can we use this? Now we can try this for the moving average example.

$$\begin{equation}
\begin{aligned}
\gamma_v(s,t) = \operatorname{cov}(v_s, v_t) &= \operatorname{cov}(\tfrac{1}{3}(w_{s-1}+w_s+w_{s+1}), \tfrac{1}{3}(w_{t-1}+w_t+w_{t+1})) \\
&= \tfrac{1}{9} \operatorname{cov}(w_{s-1}+w_s+w_{s+1}, w_{t-1}+w_t+w_{t+1})
\end{aligned}
\end{equation}$$

When $s=t$, we have: $$\begin{equation}
\begin{aligned}
\gamma_v(t,t) &= \operatorname{cov}(v_t, v_t) \\
&= \operatorname{cov}(\tfrac{1}{3}(w_{t-1}+w_t+w_{t+1}), \tfrac{1}{3}(w_{t-1}+w_t+w_{t+1})) \\
&= \tfrac{1}{9} (\operatorname{cov}(w_{t-1},w_{t-1}) + \operatorname{cov}(w_{t},w_{t}) + \operatorname{cov}(w_{t+1},w_{t+1}) \\
&\quad + 2\operatorname{cov}(w_{t-1}, w_t)) + 2\operatorname{cov}(w_{t}, w_{t+1})) + 2\operatorname{cov}(w_{t-1}, w_{t+1}))\\
&= \tfrac{1}{9} (\sigma_w^2 + \sigma_w^2 + \sigma_w^2 + 0 +0 +0)\\
&= \tfrac{3}{9} \sigma_w^2 \\
&= \tfrac{1}{3} \sigma_w^2
\end{aligned}
\end{equation}$$

When $s=t+1$, we have: $$\begin{equation}
\begin{aligned}
\gamma_v(t+1,t) &= \operatorname{cov}(\tfrac{1}{3}(w_{t}+w_{t+1}+w_{t+2}), \tfrac{1}{3}(w_{t-1}+w_t+w_{t+1})) \\
&= \tfrac{1}{9}(\operatorname{cov}(w_t,w_t)+\operatorname{cov}(w_{t+1},w_{t+1}))\\
&= \tfrac{2}{9}\sigma^2_w
\end{aligned}
\end{equation}$$

If we then follow this for more lags, we get:

$$\begin{equation}
\gamma_v(s,t) =
\begin{cases}
\tfrac{3}{9}\sigma^2_w, & \text{if } s=t, \\
\tfrac{2}{9}\sigma^2_w, & \text{if } |s-t|=1, \\
\tfrac{1}{9}\sigma^2_w, & \text{if } |s-t|=2, \\
0, & \text{if } |s-t|>2
\end{cases}
\end{equation}$$

Why is this interesting? The autocovariance depends only on the *lag* between $s$ and $t$ and not on the absolute location of these time points. We’ll come back to this when we talk about *stationarity*.

## Autocovariance of a random walk {#autocovariance-of-a-random-walk}

Recall that a random walk (with or without drift) is:

$x_t = \delta t + \displaystyle\sum_{i=1}^t w_i$

So, $$\begin{equation}
\begin{aligned}
\gamma(s,t) &= \operatorname{cov}(x_s, x_t) \\
&= \operatorname{cov}(\delta s + \displaystyle\sum_{i=1}^s w_i, \delta t + \displaystyle\sum_{i=1}^t w_i)\\
&= \sigma^2 \min(s,t)
\end{aligned}
\end{equation}$$

In this case, the autocovariance *does* depend on the particular $s$ and $t$ chosen.

What if we want a bounded measure?

## Autocorrelation function {#autocorrelation-function}

We can calculate the autocorrelation function (ACF) as:

$\rho(s,t) = \frac{\gamma(s,t)}{\sqrt{\gamma(s,s)\gamma(t,t)}}$

This measures the linear predictability of the time series at time $t$ ($x_t$) using $x_s$. We can also extend this to looking at the linear predictability of one time series to another, by extending into the concepts of *cross-covariance* and *cross-correlation*.

## Cross-covariance {#cross-covariance}

Between two time series $x_t$ and $y_t$:

$\gamma_xy(s,t) = \operatorname{cov}(x_s,y_t) = \mathbb{E}[(x_s -\mu_{xs})(y_t -\mu_{yt})]$

This tells us how the values in $y$ relate to the values in $x$ over time.

Let’s think about a simple example:

$y_t = x_{t -2}$

What is $\gamma_{xy}(k)$ (for lag $k$)? At what lag is $\gamma_{xy}$ maximized?

We can also have the normalized version:

## Cross-correlation {#cross-correlation}

$\rho_{xy}(s,t) = \frac{\gamma_xy(s,t)}{\sqrt{\gamma_x(s,s)\gamma_y(t,t)}}$

This is bounded such that $-1 \leq \rho(s,t) \leq 1$

*Poll example*

---

[← This week - Measures of dependence {#this-week---measures-of-dependence}](02-this-week---measures-of-dependence-this-week---measures-of-d.md) · [Up: contents](index.md) · [Next time: {#next-time} →](04-next-time-next-time.md)
