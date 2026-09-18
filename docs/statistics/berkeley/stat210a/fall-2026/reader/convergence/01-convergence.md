---
title: Convergence
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/convergence.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/convergence.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`reader/convergence.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/convergence.qmd) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Convergence

So far, everything has been finite sample, often using special properties of model $\cP$ (e.g., exponential family) to do exact calculations. For generic models, exact calculations may be intractable or impossible. However, we may be able to approximate our problem with a simpler problem in which calculations are easy.

Typically, we approximate by Gaussian by taking the limit as observations $n \to \infty$. But this is only interesting if the approximation is good for reasonable sample sizes.

Let $X_1, X_2, \ldots \in \mathbb{R}^d$ be a sequence of random vectors. We care about two kinds of convergence:

1. Convergence in probability: $X_n \to$ a constant
2. Convergence in distribution: $X_n \to N(0, I_d)$ (usually)

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

## Continuous Mapping Theorem

Theorem (Continuous Mapping): Let $g$ be continuous, $X_n, X$ r.v.'s.

1. If $X_n \xrightarrow{d} X$, then $g(X_n) \xrightarrow{d} g(X)$
2. If $X_n \xrightarrow{p} c$, then $g(X_n) \xrightarrow{p} g(c)$

Proof:
$f$ bounded continuous $\implies f \circ g$ bounded continuous
If $X_n \xrightarrow{d} X$, then $\mathbb{E}[f(g(X_n))] \to \mathbb{E}[f(g(X))]$
$X_n \xrightarrow{p} c$ special case with $X \equiv c$

## Slutsky's Theorem

Theorem (Slutsky): Assume $X_n \xrightarrow{d} X$, $Y_n \xrightarrow{p} c$. Then:

1. $X_n + Y_n \xrightarrow{d} X + c$
2. $X_n Y_n \xrightarrow{d} cX$
3. $X_n / Y_n \xrightarrow{d} X/c$ if $c \neq 0$

Proof: Show $(X_n, Y_n) \xrightarrow{d} (X, c)$, apply continuous mapping.

Wouldn't normally be true that $X_n \xrightarrow{d} X$, $Y_n \xrightarrow{d} Y$ implies $X_n + Y_n \xrightarrow{d} X + Y$ without specifying joint dist.

---

[Up: contents](index.md) · [Delta Method →](02-delta-method.md)
