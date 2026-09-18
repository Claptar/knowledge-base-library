---
title: Least Favorable Sequence
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture12-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture12-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture12-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture12-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Least Favorable Sequence

Sometimes there is no least favorable prior, e.g. if par. space isn't compact.

$X \sim N(\theta, 1)$: LF prior should spread mass everywhere, but that is not a proper prior.

**Def**: A sequence $\Lambda_1, \Lambda_2, \dots$ is LF if

$$r_{\Lambda_n} \to \sup_\Lambda r_\Lambda$$

**Thm**: Suppose $\Lambda_1, \Lambda_2, \dots$ is a prior sequence and $\delta$ satisfies

$$\sup_\theta R(\theta; \delta) = \lim_n r_{\Lambda_n}$$

Then
a) $\delta$ is minimax
b) $\Lambda_1, \Lambda_2, \dots$ is LF

**Proof**

a) Other est. $\tilde{\delta}$. Then $\forall n$,

$$\begin{aligned}
\sup_\theta R(\theta; \tilde{\delta}) &\ge \int R(\theta; \tilde{\delta}) \, d\Lambda_n(\theta) \\
&\ge r_{\Lambda_n}
\end{aligned}$$

$$\begin{aligned}
\Rightarrow \sup_\theta R(\theta; \tilde{\delta}) &\ge \sup_n r_{\Lambda_n} \\
&\ge \lim_n r_{\Lambda_n} \\
&= \sup_\theta R(\theta; \delta)
\end{aligned}$$

---

b) Prior $\Lambda$

$$\begin{aligned}
r_\Lambda &= \int R(\theta; \delta_\Lambda) \, d\Lambda(\theta) \\
&\le \int R(\theta; \delta) \, d\Lambda(\theta) \\
&\le \sup_\theta R(\theta; \delta) \\
&= \lim_n r_{\Lambda_n} \qquad \blacksquare
\end{aligned}$$

### **Basic Picture**:

$$\begin{array}{lcl}
\sup_\theta R(\theta; \delta) & & \text{generic } \delta \\
\ge & & \\
\inf_\delta \sup_\theta R(\theta; \delta) & & \left(= \sup_\theta R(\theta; \delta^*) \quad \text{if minimax est. exists}\right) \\
\ge & & \\
\sup_\Lambda r_\Lambda & & \left(= r_{\Lambda^*} \quad \text{if LF prior exists}\right) \\
\ge & & \\
r_\Lambda & & \text{generic } \Lambda
\end{array}$$

---

## Bounding minimax risk

Our theorem gives an idea of how to bound $r^*$ for a problem:

**Upper bound**: If $\delta$ is any estimator then

$$r^* \le \sup_\theta R(\theta; \delta) \qquad (= \text{if } \delta \text{ minimax})$$

**Lower bound**: If $\Lambda$ is any prior then

$$r^* \ge \int R(\theta; \delta_\Lambda) \, d\Lambda(\theta) \qquad (= \text{if } \Lambda \text{ LF})$$

Minimax estimators are very hard to find but minimax bounds are often used in stat theory to characterize hardness (esp. lower)

**Ex**: Propose practical estimator $\delta$, find $\Lambda$ for which $r_\Lambda$ close to $\sup_\theta R(\theta; \delta)$ (or same rate, or cvgs asymptotically)
$\Rightarrow$ Conclude $\delta$ can't be improved "much" ($*$)

**Ex**: Quantify hardness of a problem by its minimax rate in some asy. regime.

**Caveat**: A problem might be easy throughout most of par. space but very hard in some bizarre corner you never encounter in practice!

---

[← Example (Binomial)](03-example-binomial.md) · [Up: contents](index.md)
