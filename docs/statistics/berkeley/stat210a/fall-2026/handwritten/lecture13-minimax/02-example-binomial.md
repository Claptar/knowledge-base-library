---
title: Example (Binomial)
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture13-minimax.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture13-minimax.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture13-minimax.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture13-minimax.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Example (Binomial)

$X \sim \text{Binom}(n, \theta)$, estimate $\theta$, sq. err.

Try $\text{Beta}(\alpha, \beta)$, hope to get one with const. risk

Try $\alpha = \beta$: $\delta_\alpha(X) = \frac{X + \alpha}{n + 2\alpha}$ (symmetric)

$$
\mathbb{E}_\theta \delta_\alpha(X) = \frac{n\theta + \alpha}{n + 2\alpha} \implies \text{Bias}(\theta; \delta_\alpha) = \frac{\alpha(1 - 2\theta)}{n + 2\alpha}
$$

$$
\text{Var}_\theta \delta_\alpha(X) = \frac{\text{Var}_\theta(X)}{(n + 2\alpha)^2} = \frac{n\theta(1 - \theta)}{(n + 2\alpha)^2}
$$

$$
\begin{aligned}
\text{MSE}(\theta; \delta_\alpha) &= (2\alpha + n)^{-2} \left[ \alpha^2(1 - 2\theta)^2 + n\theta(1 - \theta) \right] \\
&= (2\alpha + n)^{-2} \left[ \alpha^2 + (n - 4\alpha^2)\theta(1 - \theta) \right]
\end{aligned}
$$

$$
\alpha^* = \sqrt{n}/2
$$

$$
\text{MSE}(\theta; \delta_{\alpha^*}) \equiv \frac{n/4}{(n + \sqrt{n})^2} = r^*
$$

$$
\Rightarrow \delta_{\alpha^*}(X) = \frac{\frac{\sqrt{n}}{2} + X}{\sqrt{n} + n} \quad \text{minimax}
$$

Q: Why concentrated at $\theta = 1/2$?

$\Lambda^* = \text{Beta}(\sqrt{n}/2, \sqrt{n}/2)$ LF:

```
        /\ Lambda*
       /  \
      /    \
     /      \
    /        \
  -+----------+-
   0         1
```

---

## Least Favorable Sequence

Sometimes there is no least favorable prior

**Def**: A sequence $\Lambda_1, \Lambda_2, \ldots$ is LF if

$$
r_{\Lambda_n} \to \sup_\Lambda r_\Lambda
$$

**Thm**: Suppose $\Lambda_1, \Lambda_2, \ldots$ is a prior sequence and $\delta$ satisfies $\sup_\theta R(\theta; \delta) = \lim_n r_{\Lambda_n}$

Then $\delta$ is minimax and $\Lambda_1, \Lambda_2, \ldots$ is LF

### Proof

Other est. $\tilde{\delta}$, $\forall n$,

$$
\begin{aligned}
\sup_\theta R(\theta; \tilde{\delta}) &\ge \int R(\theta; \tilde{\delta}) \, d\Lambda_n(\theta) \\
&\ge r_{\Lambda_n} \\
\Rightarrow \sup_\theta R(\theta; \tilde{\delta}) &\ge \sup_n r_{\Lambda_n} \\
&\ge \lim_n r_{\Lambda_n} \\
&= \sup_\theta R(\theta; \delta)
\end{aligned}
$$

Hence $\lim_n r_{\Lambda_n} \le r^* \le \sup_\theta R(\theta; \delta) = \lim_n r_{\Lambda_n}$ $\quad \blacksquare$

---

## Ex

$X \sim N_d(\theta, I_d)$. Est. $\theta$, use MSE

$\delta_0(X) = X \quad \text{unbiased}, \quad \text{MSE} = d$

Prior $\Lambda_n = N_d(0, n I_d) \rightsquigarrow \delta_{\zeta_n}(X) = (1 - \zeta_n)X \qquad \zeta_n = \frac{1}{n+1}$

$\text{MSE}(\theta; \delta_{\zeta_n}) = \zeta_n^2 \|\theta\|^2 + (1 - \zeta_n)^2 d$

$$
\begin{aligned}
r_{\Lambda_n} &= \mathbb{E} \, \text{MSE}(\theta) \\
&= \zeta_n^2 n d + (1 - \zeta_n)^2 d \\
&= d \left( \frac{n}{(1+n)^2} + \frac{n^2}{(1+n)^2} \right) \\
&\to d
\end{aligned}
$$

So $\Lambda_1, \Lambda_2, \ldots$ is LF,

$\delta_0(X)$ is minimax (but inadmissible?)

$r^* = d$

---

## Bounding minimax risk

Our theorem gives an idea of how to bound $r^*$ for a problem:

**Upper bound**: If $\delta$ is any estimator then

$$
r^* \le \sup_\theta R(\theta; \delta) \qquad (= \text{if } \delta \text{ minimax})
$$

**Lower bound**: If $\Lambda$ is any prior then

$$
r^* \ge \int R(\theta; \delta_\Lambda) \, d\Lambda(\theta) \qquad (= \text{if } \Lambda \text{ LF})
$$

Minimax estimators are very hard to find but minimax bounds are often used in stat theory to characterize hardness (esp. lower)

**Ex**: Propose practical estimator $\delta$, find $\Lambda$ for which $r_\Lambda$ close to $\sup_\theta R(\theta; \delta)$ (or same rate, or cvgs asymptotically)
$\Rightarrow$ Conclude $\delta$ can't be improved "much" (*)

**Ex**: Quantify hardness of a problem by its minimax rate in some asy. regime.

**Caveat**: A problem might be easy throughout most of par. space but very hard in some bizarre corner you never encounter in practice!

---

[← Minimax Estimation](01-minimax-estimation.md) · [Up: contents](index.md)
