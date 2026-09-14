---
title: Mean and variance
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/03_dependence_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/03_dependence_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Mean and variance

**Source:** [`public/lectures/03_dependence_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/03_dependence_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

Last week and in your lab, we saw the concept of how mean and variance differ for a white noise process, a random walk, and a random walk with drift. The *mean* and *variance functions* of a time series are useful descriptors because they helps us determine something about the drift and the spread of the data that we should expect over time.

The *mean function* is defined as $\mu_{xt} = \mathbb{E}(x_t)$

The *variance function* is $\sigma^2_t = \operatorname{Var}(x_t) = \mathbb{E}[(x_t-\mu_t)^2]$.

Let's revisit some examples from before:

## White noise
For a white noise time series, $\mu_{wt} = \mathbb{E}(w_t)=0$ for all $t$. $\operatorname{Var}(w_t) = 1$ (for a Gaussian white noise series).

## Moving average

What if we apply a 3-point moving average? Although this induces some correlation structure, it actually does not change the mean function at all:

$\mu_{vt} = \mathbb{E}(v_t) = \frac{1}{3}[\mathbb{E}(w_{t-1})+\mathbb{E}(w_{t})+\mathbb{E}(w_{t+1})] = 0$

## Random walk with drift

For the random walk with drift, the mean function is just the line $\mu_{xt} = \delta t + \displaystyle\sum_{j=1}^t E(w_j) = \delta t$.

## Signal plus noise

And for a signal plus noise (as an example, we'll use this sinusoid):

$$
\begin{aligned}
\mu_{xt} = \mathbb{E}(x_t) &= \mathbb{E} [A \cos(2\pi \omega t + \phi) + w_t] \\
&= \mathbb{E} [A \cos(2\pi \omega t + \phi)] + \mathbb{E}[w_t] \\
&= \mathbb{E} [A \cos(2\pi \omega t + \phi)]
\end{aligned}
$$

---

[← This week - Measures of dependence](02-this-week---measures-of-dependence.md) · [Up: contents](index.md) · [Autocovariance →](04-autocovariance.md)
