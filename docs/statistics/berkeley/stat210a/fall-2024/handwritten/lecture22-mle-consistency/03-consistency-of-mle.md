---
title: Consistency of MLE
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture22-mle-consistency.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture22-mle-consistency.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture22-mle-consistency.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture22-mle-consistency.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Consistency of MLE

$$X_1, \ldots, X_n \overset{\text{iid}}{\sim} P_{\theta_0}, \qquad \hat{\theta}_n \in \underset{\theta \in \Theta}{\operatorname{argmax}} \, l_n(\theta; X)$$

$$\left[ \text{Will be ok if } \hat{\theta}_n \text{ comes close to maximizing } l_n \right]$$

Question: When does $\hat{\theta}_n \overset{P}{\to} \theta_0$?

Assume model identifiable ($P_\theta \neq P_{\theta_0}$ for $\theta \neq \theta_0$)

Recall KL Divergence:

$$D_{\text{KL}}(\theta_0 \,\|\, \theta) = \mathbb{E}_{\theta_0} \log \frac{p_{\theta_0}(X_i)}{p_\theta(X_i)}$$

$$-D_{\text{KL}}(\theta_0 \,\|\, \theta) \overset{\text{(Jensen)}}{\le} \log \mathbb{E}_{\theta_0} \frac{p_\theta(X_i)}{p_{\theta_0}(X_i)} \qquad \leftarrow \text{(note switch)}$$

$$= \log \int_{x: p_{\theta_0}(x) > 0} \frac{p_\theta(x)}{p_{\theta_0}(x)} p_{\theta_0}(x) \, d\mu(x)$$

$$\le \log 1 = 0$$

strict ineq unless $\frac{p_\theta}{p_{\theta_0}} = \text{const.}$ (i.e., unless $P_\theta = P_{\theta_0}$)

Let $W_i(\theta) = l(\theta; X_i) - l(\theta_0; X_i)$, $\bar{W}_n = \frac{1}{n}\sum W_i$

Note $\hat{\theta}_n \in \underset{\theta \in \Theta}{\operatorname{argmax}} \, \bar{W}_n(\theta)$ too

---

$$\bar{W}_n(\theta) \overset{P}{\to} \mathbb{E}_{\theta_0} W_1(\theta)$$

$$= -D_{\text{KL}}(\theta_0 \,\|\, \theta)$$

$$\le 0, \quad \text{equality iff } \theta = \theta_0$$

**But not enough:**
- MLE $\hat{\theta}_n$ depends on entire function $\bar{W}_n(\cdot)$
- need uniform convergence in $\theta$

**Def** For compact $K$ let $C(K) = \{f: K \to \mathbb{R}, \text{ cts}\}$

For $f \in C(K)$ let $\|f\|_\infty = \sup_{t \in K} |f(t)|$

$f_n \to f$ in this norm if $\|f_n - f\|_\infty \to 0$ ($\overset{P}{\to}$)

**Thm (LLN for random functions)**

Assume $K$ compact, $W_1, W_2, \ldots \in C(K)$ iid.

$\mathbb{E}\|W_1\|_\infty < \infty$, $\mu(t) = \mathbb{E} W_1(t)$

Then $\mu(t) \in C(K)$

and $\mathbb{P}\left(\left\|\frac{1}{n} \sum W_i - \mu\right\|_\infty > \varepsilon\right) \to 0$

(i.e., $\bar{W}_n \overset{P}{\to} \mu$ in $\|\cdot\|_\infty$, or $\|\bar{W}_n - \mu\|_\infty \overset{P}{\to} 0$)

---

---

← Asymptotic Picture ($d=1$) · [Up: contents](index.md) · [Theorem (Consistency of MLE for compact $\Theta$) →](04-theorem-consistency-of-mle-for-compact.md)
