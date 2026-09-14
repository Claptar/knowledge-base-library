---
title: Convergence
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/asymptotics.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/asymptotics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Convergence

**Source:** [`reader/asymptotics.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/asymptotics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

There are two main approximations we will be interested in making: approximating a random variable as a limiting constant, and approximating it as having some limiting distribution, usually a multivariate Gaussian distribution. To make these approximations precise, we need to introduce two types of convergence: convergence in probability, and convergence in distribution.

Let $X_1, X_2, \ldots$ be a sequence of random variables on a sample space $\cX$, which we assume is endowed with a distance $d(x,y)$. Because we are primarily interested in $\cX \subseteq \RR^d$, we will write $d(x,y)$ as $\|x-y\|$, and it will not matter which norm we choose, but

We say the sequence *converges in probability* to a limiting constant $c \in \cX$, written as $X \toProb c$ if
$$
\mathbb{P}(\|X_n - c\| > \epsilon) \to 0 \quad \forall \epsilon > 0.
$$
In writing the norm we are implicitly assuming $

### Convergence in Probability

We say the sequence converges in probability to $c \in \mathbb{R}^d$ ($X_n \xrightarrow{p} c$) if:

$$\mathbb{P}(\|X_n - c\| > \epsilon) \to 0 \quad \forall \epsilon > 0$$

(Could really be any distance on any $\cX$)

Can converge to a r.v. $X$ too, but we don't need this.

### Convergence in Distribution

We say the sequence converges in distribution to random variable $X$ ($X_n \xrightarrow{d} X$) if:

$$\mathbb{E}[f(X_n)] \to \mathbb{E}[f(X)] \text{ for all bounded continuous } f: \cX \to \mathbb{R}$$

Theorem: $X_n, X \in \mathbb{R}$. Fix $\mathbb{P}(X = x) = 0$. Let $F_n(x) = \mathbb{P}(X_n \leq x)$, $F(x) = \mathbb{P}(X \leq x)$.
Then $X_n \xrightarrow{d} X$ iff $F_n(x) \to F(x)$ $\forall x: F$ is continuous at $x$.

Also known as weak convergence.

### Example

If $X_n \xrightarrow{d} X \sim g$, then $X_n \xrightarrow{d} X$:

$$F_n(x) = \begin{cases}
1 & \text{if } x > 0 \\
1 - \frac{1}{n} & \text{if } x = 0 \\
0 & \text{if } x < 0
\end{cases}$$

$$F(x) = \begin{cases}
1 & \text{if } x > 0 \\
0 & \text{if } x \leq 0
\end{cases}$$

### Proof: $X_n \xrightarrow{p} c \implies X_n \xrightarrow{d} c$

Let $f_\epsilon(x) = \max\{1 - \frac{\|x-c\|}{\epsilon}, 0\}$. Then $\forall \epsilon > 0$:

$$\mathbb{P}(\|X_n - c\| > \epsilon) \leq \mathbb{E}[1 - f_\epsilon(X_n)] \to 0$$

$f$ bounded continuous. Note $\mathbb{E}[f(c)] = f(c)$.

$\forall \epsilon > 0$, $\exists \delta > 0$ s.t. $\|x - c\| < \delta \implies |f(x) - f(c)| < \epsilon$

$$|\mathbb{E}[f(X_n)] - f(c)| \leq |\mathbb{E}[f(X_n) - f(c)]1_{\|X_n - c\| < \delta}| + |\mathbb{E}[(f(X_n) - f(c))1_{\|X_n - c\| \geq \delta}]|$$
$$\leq \epsilon + 2\sup |f| \cdot \mathbb{P}(\|X_n - c\| \geq \delta)$$

For sufficiently large $n$. $\square$

In a sequence of statistical models $\cP_n = \{P_{n,\theta}: \theta \in \Theta\}$ with $X_n \sim P_{n,\theta}$, we say $\hat{\theta}_n$ is consistent for $g(\theta)$ if $\hat{\theta}_n \xrightarrow{p} g(\theta)$, meaning:

$$\mathbb{P}_\theta(|\hat{\theta}_n - g(\theta)| > \epsilon) \to 0$$

Usually, we omit the index $n$; sequence is implicit.

### Law of Large Numbers (LLN)

Let $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$

If $\mathbb{E}|X_i| < \infty$, $\mathbb{E}X_i = \mu$, then $\bar{X}_n \xrightarrow{p} \mu$

### Central Limit Theorem (CLT)

If $\text{Var}(X_i) = \sigma^2 < \infty$, then $\sqrt{n}(\bar{X}_n - \mu) \xrightarrow{d} N(0, \sigma^2)$

There are stronger versions of both the LLN and CLT, but this will generally be enough for us.

---

[← "True" Fisher information](02-true-fisher-information.md) · [Up: contents](index.md) · [Continuous Mapping Theorem →](04-continuous-mapping-theorem.md)
