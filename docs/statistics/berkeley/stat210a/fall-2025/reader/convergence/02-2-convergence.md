---
title: 2 Convergence
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/convergence.html
source_file: sources/berkeley-stat210a/fall-2025/reader/convergence.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/convergence.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/convergence.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2 Convergence

Let $X_1, X_2, \ldots \in \mathbb{R}^d$ be a sequence of random vectors. We care about two kinds of convergence:

1.  Convergence in probability: $X_n \to$ a constant
2.  Convergence in distribution: $X_n \to N(0, I_d)$ (usually)

### 2.1 Convergence in Probability {.anchored number="2.1" anchor-id="convergence-in-probability"}

We say the sequence converges in probability to $c \in \mathbb{R}^d$ ($X_n \xrightarrow{p} c$) if:

$$
\mathbb{P}(\|X_n - c\| > \epsilon) \to 0 \quad \forall \epsilon > 0
$$

(Could really be any distance on any $\cX$)

Can converge to a r.v. $X$ too, but we don’t need this.

### 2.2 Convergence in Distribution {.anchored number="2.2" anchor-id="convergence-in-distribution"}

We say the sequence converges in distribution to random variable $X$ ($X_n \xrightarrow{d} X$) if:

$$
\mathbb{E}[f(X_n)] \to \mathbb{E}[f(X)] \text{ for all bounded continuous } f: \cX \to \mathbb{R}
$$

Theorem: $X_n, X \in \mathbb{R}$. Fix $\mathbb{P}(X = x) = 0$. Let $F_n(x) = \mathbb{P}(X_n \leq x)$, $F(x) = \mathbb{P}(X \leq x)$. Then $X_n \xrightarrow{d} X$ iff $F_n(x) \to F(x)$ $\forall x: F$ is continuous at $x$.

Also known as weak convergence.

### 2.3 Example {.anchored number="2.3" anchor-id="example"}

If $X_n \xrightarrow{d} X \sim g$, then $X_n \xrightarrow{d} X$:

$$
F_n(x) = \begin{cases}
1 & \text{if } x > 0 \\
1 - \frac{1}{n} & \text{if } x = 0 \\
0 & \text{if } x < 0
\end{cases}
$$

$$
F(x) = \begin{cases}
1 & \text{if } x > 0 \\
0 & \text{if } x \leq 0
\end{cases}
$$

### 2.4 Proof: $X_n \xrightarrow{p} c \implies X_n \xrightarrow{d} c$ {#proof-math28 .anchored number="2.4" anchor-id="proof-x_n-xrightarrowp-c-implies-x_n-xrightarrowd-c"}

Let $f_\epsilon(x) = \max\{1 - \frac{\|x-c\|}{\epsilon}, 0\}$. Then $\forall \epsilon > 0$:

$$
\mathbb{P}(\|X_n - c\| > \epsilon) \leq \mathbb{E}[1 - f_\epsilon(X_n)] \to 0
$$

$f$ bounded continuous. Note $\mathbb{E}[f(c)] = f(c)$.

$\forall \epsilon > 0$, $\exists \delta > 0$ s.t. $\|x - c\| < \delta \implies |f(x) - f(c)| < \epsilon$

$$
|\mathbb{E}[f(X_n)] - f(c)| \leq |\mathbb{E}[f(X_n) - f(c)]1_{\|X_n - c\| < \delta}| + |\mathbb{E}[(f(X_n) - f(c))1_{\|X_n - c\| \geq \delta}]|
$$

$$
\leq \epsilon + 2\sup |f| \cdot \mathbb{P}(\|X_n - c\| \geq \delta)
$$

For sufficiently large $n$. $\square$

In a sequence of statistical models $\cP_n = \{P_{n,\theta}: \theta \in \Theta\}$ with $X_n \sim P_{n,\theta}$, we say $\hat{\theta}_n$ is consistent for $g(\theta)$ if $\hat{\theta}_n \xrightarrow{p} g(\theta)$, meaning:

$$
\mathbb{P}_\theta(|\hat{\theta}_n - g(\theta)| > \epsilon) \to 0
$$

Usually, we omit the index $n$; sequence is implicit.

### 2.5 Law of Large Numbers (LLN) {.anchored number="2.5" anchor-id="law-of-large-numbers-lln"}

Let $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$

If $\mathbb{E}|X_i| < \infty$, $\mathbb{E}X_i = \mu$, then $\bar{X}_n \xrightarrow{p} \mu$

### 2.6 Central Limit Theorem (CLT) {.anchored number="2.6" anchor-id="central-limit-theorem-clt"}

If $\text{Var}(X_i) = \sigma^2 < \infty$, then $\sqrt{n}(\bar{X}_n - \mu) \xrightarrow{d} N(0, \sigma^2)$

There are stronger versions of both the LLN and CLT, but this will generally be enough for us.

## 3 Continuous Mapping Theorem {.anchored number="3" anchor-id="continuous-mapping-theorem"}

Theorem (Continuous Mapping): Let $g$ be continuous, $X_n, X$ r.v.’s.

1.  If $X_n \xrightarrow{d} X$, then $g(X_n) \xrightarrow{d} g(X)$
2.  If $X_n \xrightarrow{p} c$, then $g(X_n) \xrightarrow{p} g(c)$

Proof: $f$ bounded continuous $\implies f \circ g$ bounded continuous If $X_n \xrightarrow{d} X$, then $\mathbb{E}[f(g(X_n))] \to \mathbb{E}[f(g(X))]$ $X_n \xrightarrow{p} c$ special case with $X \equiv c$

## 4 Slutsky’s Theorem {.anchored number="4" anchor-id="slutskys-theorem"}

Theorem (Slutsky): Assume $X_n \xrightarrow{d} X$, $Y_n \xrightarrow{p} c$. Then:

1.  $X_n + Y_n \xrightarrow{d} X + c$
2.  $X_n Y_n \xrightarrow{d} cX$
3.  $X_n / Y_n \xrightarrow{d} X/c$ if $c \neq 0$

Proof: Show $(X_n, Y_n) \xrightarrow{d} (X, c)$, apply continuous mapping.

Wouldn’t normally be true that $X_n \xrightarrow{d} X$, $Y_n \xrightarrow{d} Y$ implies $X_n + Y_n \xrightarrow{d} X + Y$ without specifying joint dist.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [5 Delta Method →](03-5-delta-method.md)
