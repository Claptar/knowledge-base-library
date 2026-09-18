---
title: $p$-Values, Confidence Regions
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture16-pconf.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture16-pconf.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture16-pconf.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture16-pconf.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# $p$-Values, Confidence Regions

### Outline

1) $p$-Values
2) Confidence regions
3) (Mis-)interpreting tests

---

## $p$-Values

Informal definition: Suppose $\phi(x)$ rejects for large values of $T(x)$.

$$p(x) = \text{``Null probability that } T(X) \text{ is as large or larger than what we observed''}$$

$$= \text{``}\mathbb{P}_{H_0}(T(X) \ge T(x))\text{''}$$

$$= \sup_{\theta \in \Theta_0} \mathbb{P}_\theta(T(X) \ge T(x))$$

**Ex** $X \sim \text{Binom}(n, \theta) \quad H_0: \theta \le 0.5 \quad \text{vs} \quad H_1: \theta > 0.5$

One-sided test rejects for large $X$

$$p(x) = \mathbb{P}_{0.5}(X \ge x) = \sup_{\theta \le 0.5} \mathbb{P}_\theta(X \ge x)$$

**Ex** $X \sim N(\theta, 1) \quad H_0: \theta = 0 \quad \text{vs.} \quad H_1: \theta \ne 0$

Two-sided test rejects for large $T(X) = |X|$

$$(\iff \phi(x) = \mathbf{1}\{|X| > z_{\alpha/2}\})$$

The two-sided $p$-value is $p(x)$ where

$$p(x) = \mathbb{P}_0(|X| > |x|)$$
$$= 2(1 - \Phi(|x|))$$

---

### Formal definition: $\mathcal{P}$, $\Theta_0$, $\Theta_1$

Not all tests reject for large $T(X)$
(e.g. UMPU two-sided test)

Assume we have a test $\phi_\alpha$ for each significance level, $\sup_{\theta \in \Theta_0} \mathbb{E}_\theta \phi_\alpha(X) \le \alpha$ with $\phi_\alpha(x) \nearrow$ in $\alpha$

Then $p(x) = \sup\{\alpha: \phi_\alpha(x) < 1\} = \inf\{\alpha: \phi_\alpha(x) = 1\}$

These definitions coincide if $\phi$ rejects for large $T$

### Prop

If $\phi_\alpha$ rejects for large $T(x)$ with tight cutoffs:
$$c_\alpha = \min\{c : \mathbb{P}_\theta(T > c) \le \alpha, \text{ all } \theta \in \Theta_0\}$$
Then $p(x) = \sup_{\theta \in \Theta_0} \mathbb{P}_\theta(T(X) \ge T(x))$

#### Proof
Let $p_1(x) = \sup_{\theta \in \Theta_0} \mathbb{P}_\theta(T(X) \ge T(x))$, $p_2(x) = \sup\{\alpha : \phi_\alpha(x) < 1\}$

$$p_1(x) > \alpha \iff \mathbb{P}_\theta(T(X) \ge T(x)) > \alpha, \text{ for some } \theta \in \Theta_0$$
$$\iff x < c_\alpha, \text{ or } c_\alpha = x \text{ and } \gamma_\alpha < 1$$
$$\iff \phi_\alpha(x) < 1$$

Therefore, $p_2(x) = \sup\{\alpha: p_1(x) > \alpha\} = p_1(x)$ $\blacksquare$

---

## Super-Uniformity

Under $H_0$, the $p$-value is **super-uniform**
(stochastically larger than $\text{Unif}[0,1]$)

### Prop
For $\theta \in \Theta_0$, $\mathbb{P}_\theta(p(X) \le \alpha) \le \alpha$

#### Proof
$p(x) \le \alpha \iff \phi_{\alpha+\varepsilon}(x) = 1$, all $\varepsilon > 0$

$$\mathbb{P}_\theta(p(X) \le \alpha) = \mathbb{P}_\theta(\phi_{\alpha+\varepsilon}(X) = 1, \text{ all } \varepsilon > 0)$$
$$= \lim_{\varepsilon \downarrow 0} \mathbb{P}_\theta(\phi_{\alpha+\varepsilon}(X) = 1)$$
\$\$\le \lim_{\varepsilon \downarrow 0} \mathbb{E}_\theta \phi_{\alpha+\varepsilon

---

[Up: contents](../index.md)
