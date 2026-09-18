---
title: Gaussian sequence model
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture10-bayesinterp.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture10-bayesinterp.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture10-bayesinterp.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture10-bayesinterp.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Gaussian sequence model

$X \mid \theta \sim N_d(\mu, I_d) \qquad \mu \in \mathbb{R}^d$

Jeffreys prior is flat: $\lambda(\mu) \propto_\mu 1$

$$
\lambda(\mu \mid X) = N_d(X, I_d) \implies \mathbb{E}[\mu \mid X] = X
$$
(Same as UMVU)

What about $\rho^2 = \|\mu\|^2$? Recall
$$
\mu \sim N_d(X, I_d) \implies \mathbb{E}[\|\mu\|^2 \mid X] = \|X\|^2 + d
$$

Note $\delta_{\text{umvu}}(X) = \|X\|^2 - d \implies \delta_\lambda(X) = \delta_{\text{umvu}}(X) + 2d$

$$
\begin{aligned}
\text{MSE}(\theta; \delta_\lambda) &= \text{Var}_\theta(\delta_\lambda) + \text{Bias}_\theta(\delta_\lambda)^2 \\
&= \text{Var}_\theta(\delta_{\text{umvu}}) + 4d^2
\end{aligned}
$$

What went wrong? Examine Jeffreys prior:
$$
\begin{aligned}
\mathbb{P}(\rho^2 \le t) &= \text{Vol}(\text{Ball of radius } \sqrt{t}) \\
&= \text{const}(d) \cdot t^{d/2}
\end{aligned}
$$

$$
\Rightarrow \lambda(\rho^2) \propto_{\rho^2} (\rho^2)^{\frac{d}{2}-1} = \rho^{d-2}
$$

Grows rapidly! Prior "expects" $\rho^2$ to be huge

---

## Source #3: Prior or concurrent experience

May have many "copies" of same problem
Assume corresp. $\Theta$ values drawn from a population
$\rightsquigarrow$ Hierarchical Bayes / empirical Bayes

Can be hard to choose right reference class

**Ex**. Estimate same-side bias for $m = 48$ coin flippers
Flipper $i$ has $n_i$ trials, "true" same-side prob $\theta_i$

Hierarchical model: flippers $i = 1, \dots, m$
"hyperparameters" $\alpha, \beta \sim \lambda$ $\leftarrow$ "hyperprior"
$\theta_i \mid \alpha, \beta \overset{\text{iid}}{\sim} \text{Beta}(\alpha, \beta)$
$X_i \mid \alpha, \beta, \theta \overset{\text{ind.}}{\sim} \text{Binom}(n_i, \theta_i)$

$$
\mathbb{E}[\theta_i \mid X, \alpha, \beta] = \frac{X_i + \alpha}{n_i + \alpha + \beta}
$$

$$
\begin{aligned}
\mathbb{E}[\theta_i \mid X] &= \mathbb{E}\left[ \mathbb{E}[\theta_i \mid X, \alpha, \beta] \mid X \right] \\
&= \iint \frac{X_i + \alpha}{n_i + \alpha + \beta} \lambda(\alpha, \beta \mid X) \, d\alpha \, d\beta
\end{aligned}
$$

If $m$ large, $\alpha, \beta$ may be "almost known"
$\rightsquigarrow$ choice of $\lambda$ doesn't matter much

---

---

[← Where does $\Lambda$ come from?](01-where-does-come-from.md) · [Up: contents](index.md) · [Flexibility of Bayes →](03-flexibility-of-bayes.md)
