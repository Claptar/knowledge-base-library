---
title: Convergence
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture19-asymptotics.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture19-asymptotics.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture19-asymptotics.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture19-asymptotics.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Convergence

Let $X_1, X_2, \dots \in \mathbb{R}^d$ sequence of random vectors

We care about 2 kinds of convergence:
1) cvg. in probability ($X_n \approx \text{constant}$)
2) cvg. in distribution ($X_n \approx N_d(0, I_d)$, usually)

We say the sequence **converges in probability** to $c \in \mathbb{R}^d$ ($X_n \overset{P}{\to} c$) if
$$
\mathbb{P}(\|X_n - c\| > \varepsilon) \to 0, \quad \forall \varepsilon > 0
$$
(could really be any distance on any $\mathcal{X}$)

[Can converge to a r.v. $X$ too, but we don't need this]

We say the sequence **converges in distribution** to random variable $X$ ($X_n \Rightarrow X$, $X_n \overset{d}{\to} X$) if
$$
\mathbb{E} f(X_n) \to \mathbb{E} f(X) \quad \text{for all bdd, cts } f : \mathcal{X} \to \mathbb{R}
$$

**Thm** $X_1, X_2, \dots \in \mathbb{R}$, $F_n(x) = \mathbb{P}(X_n \le x)$, $F(x) = \mathbb{P}(X \le x)$
Then $X_n \Rightarrow X$ iff $F_n(x) \to F(x) \quad \forall x : F \text{ cts at } x$

Also known as **weak convergence**

---

**Ex**: If $X_n \sim \delta_{\frac{1}{n}}$ ($X_n \overset{\text{a.s.}}{=} \frac{1}{n}$), $X \sim \delta_0$, then $X_n \Rightarrow X$
$F_n(x) = \mathbf{1}\{\frac{1}{n} \le x\} \to \mathbf{1}\{0 \le x\}$ except $x = 0$

**Prop** $X_n \overset{P}{\to} c \iff X_n \Rightarrow \delta_c$

**Proof**
($\Leftarrow$) Let $f_\varepsilon(x) = \max\left(1, \frac{\|x-c\|}{\varepsilon}\right) \ge \mathbf{1}\{\|x-c\| > \varepsilon\}$
$\mathbb{P}(\|X_n - c\| > \varepsilon) \le \mathbb{E} f_\varepsilon(X_n) \to 0$

($\Rightarrow$) $f$ bdd, cts, note $\mathbb{E} f(X) = f(c)$
$\forall \varepsilon > 0$, $\exists d(\varepsilon) > 0$ s.t. $\|x - c\| \le d(\varepsilon) \implies |f(x) - f(c)| \le \varepsilon$

$$
\begin{aligned}
\mathbb{E} f(X_n) - f(c) &\le \mathbb{E}[|f(X_n) - f(c)| \cdot (\mathbf{1}\{\|X_n - c\| \le d(\varepsilon)\} + \mathbf{1}\{\|\cdot\| > d\})] \\
&\le \varepsilon + \mathbb{P}(\|X_n - c\| > d(\varepsilon)) \cdot \sup |f(x) - f(c)| \\
&\le 2\varepsilon \cdot \sup |f| \quad \text{for suff. large } n \quad \boxtimes
\end{aligned}
$$

In a sequence of statistical models $\mathcal{P}_n = \{P_{n,\theta} : \theta \in \Theta\}$ with $X_n \sim P_{n,\theta}$, we say $\delta_n(X_n)$ is **consistent** for $g(\theta)$ if $\delta_n(X_n) \overset{P_\theta}{\to} g(\theta)$, meaning
$$
\mathbb{P}_\theta(\|\delta_n(X_n) - g(\theta)\| > \varepsilon) \to 0
$$

Usually we omit the index $n$; sequence is implicit.

---

## Limit Theorems

Let $X_1, X_2, \dots$ iid random vectors
$\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$

### Law of large numbers (LLN)
If $\mathbb{E}|X_i| < \infty$, $\mathbb{E} X_i = \mu$, then $\bar{X}_n \overset{P}{\to} \mu \quad (\bar{X}_n \overset{\text{a.s.}}{\to} \mu)$

### Central limit theorem (CLT)
If $\mathbb{E} X = \mu \in \mathbb{R}^d$, $\operatorname{Var}(X_n) = \Sigma$ (finite)
Then $\sqrt{n}(\bar{X}_n - \mu) \Rightarrow N(0, \Sigma)$

[There are stronger versions of both the LLN & CLT, but this will generally be enough for us]

---

## Continuous Mapping

**Theorem (Cts Mapping)** $g$ cts; $X_1, X_2, \dots$ r.v.s
If $X_n \Rightarrow X$ then $g(X_n) \Rightarrow g(X)$
If $X_n \overset{P}{\to} c$ then $g(X_n) \overset{P}{\to} g(c)$

**Proof** $f$ bdd, cts $\implies f \circ g$ bdd, cts
If $X_n \Rightarrow X$ then $\mathbb{E} f(g(X_n)) \to \mathbb{E} f(g(X))$
$X_n \overset{P}{\to} c$ special case with $X \sim \delta_c$ $\boxtimes$

**Theorem (Slutsky)** Assume $X_n \Rightarrow X$, $Y_n \overset{P}{\to} c$
Then:
$$
\begin{aligned}
X_n + Y_n &\Rightarrow X + c \\
X_n \cdot Y_n &\Rightarrow c X \\
X_n / Y_n &\Rightarrow X / c \quad \text{if } c \ne 0
\end{aligned}
$$

**Proof** Show $(X_n, Y_n) \Rightarrow (X, c)$, apply cts mapping.

[Wouldn't normally be true that $X_n \Rightarrow X$, $Y_n \Rightarrow Y$ implies $(X_n, Y_n) \Rightarrow (X, Y)$ without specifying joint dist.]

---

## Theorem (Delta Method)

If
* $\sqrt{n}(X_n - \mu) \Rightarrow N(0, \sigma^2)$
* $f(x)$ differentiable at $x = \mu$

Then $\sqrt{n}(f(X_n) - f(\mu)) \Rightarrow N(0, \dot{f}(\mu)^2 \sigma^2)$

**Informal statement:**
$$
X_n \approx N(\mu, \sigma^2 / n) \implies f(X_n) \approx N(f(\mu), \dot{f}(\mu) \sigma^2 / n)
$$

**Proof**
$$
\begin{aligned}
f(X_n) &= f(\mu) + \dot{f}(\mu)(X_n - \mu) + o(X_n - \mu) \\
\sqrt{n}(f(X_n) - f(\mu)) &= \dot{f}(\mu) \cdot \sqrt{n}(X_n - \mu) + \underbrace{\sqrt{n} \cdot o(X_n - \mu)}_{\overset{P}{\to} 0} \\
&= N(0, \dot{f}(\mu)^2 \sigma^2)
\end{aligned}
$$

**Multivariate:** $\sqrt{n}(X_n - \mu) \Rightarrow N_d(0, \Sigma)$, $f : \mathbb{R}^d \to \mathbb{R}^k$
Derivative $Df(x) = \begin{pmatrix} - \nabla f_1(x) - \\ \vdots \\ - \nabla f_k(x) - \end{pmatrix}$ exists at $\mu$

Then
$$
\begin{aligned}
\sqrt{n}(f(X_n) - f(\mu)) &\approx \sqrt{n} Df(\mu)(X_n - \mu) \\
&\approx N(0, Df(\mu) \Sigma Df(\mu)') \\
&= N(0, \nabla f(\mu)' \Sigma \nabla f(\mu)) \quad \text{if } k = 1
\end{aligned}
$$

---

---

[← Example](01-example.md) · [Up: contents](index.md) · [Delta Method →](03-delta-method.md)
