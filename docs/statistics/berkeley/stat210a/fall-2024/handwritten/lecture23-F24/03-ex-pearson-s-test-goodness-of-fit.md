---
title: Ex Pearson's $\chi^2$ test (goodness of fit)
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture23-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture23-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture23-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture23-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Ex Pearson's $\chi^2$ test (goodness of fit)

$$N = (N_1, \ldots, N_d) \sim \text{Multinom}(n, (\pi_1, \ldots, \pi_d))$$
$$= \frac{n! \, \pi_1^{N_1} \cdots \pi_d^{N_d}}{N_1! \cdots N_d!} \mathbf{1}\{\sum N_i = n\}$$

Note $\sum \pi_j = 1$ so this is a full-rank $(d-1)$-parameter exp. family, e.g.

$$\pi_j = \begin{cases} \frac{1}{1 + \sum_{k > 1} e^{\eta_k}} & j = 1 \\ \frac{e^{\eta_j}}{1 + \sum_{k > 1} e^{\eta_k}} & j > 1 \end{cases}$$

$$\nabla \ell(\eta; N) = (N_2, \ldots, N_d) - (n\pi_2, \ldots, n\pi_d)$$

$$\operatorname{Var}_\eta(\nabla \ell(\eta)) = \begin{pmatrix} n\pi_2(1-\pi_2) & & -n\pi_i\pi_j \\ & \ddots & \\ -n\pi_i\pi_j & & n\pi_d(1-\pi_d) \end{pmatrix}$$
$$= n \left( \operatorname{diag}(\pi_{2:d}) - \pi_{2:d} \, \pi_{2:d}' \right)$$

$$\Rightarrow J_n(\eta)^{-1} = \frac{1}{n} \cdot \left( \operatorname{diag}(\pi_{2:d})^{-1} - \pi_1^{-1} \mathbf{1} \mathbf{1}' \right)$$
$$(\text{uses } (A + uv')^{-1} = A^{-1} - \frac{A^{-1}uv'A^{-1}}{1 + v'A^{-1}u})$$

Score test of $H_0: \pi = \pi_0$: (don't really need asy. approx)

$$\nabla \ell_n(\eta_0)' J_n^{-1}(\eta_0) \nabla \ell_n(\eta_0) \overset{\text{(algebra)}}{\downarrow} \sum_{j=1}^d \frac{(N_j - n\pi_{0,j})^2}{n\pi_{0,j}} \xrightarrow{P_{\pi_0}} \chi_{d-1}^2$$

---

## Generalized LRT

Test $H_0: \theta = \theta_0$ vs. $H_1: \theta \neq \theta_0$

Taylor expand around $\hat{\theta}_n$:

$$\ell_n(\theta_0) - \ell_n(\hat{\theta}_n) = \underbrace{\nabla \ell(\hat{\theta}_n)^0}_{0} + \frac{1}{2}(\theta_0 - \hat{\theta}_n)' \nabla^2 \ell_n(\tilde{\theta}_n)(\theta_0 - \hat{\theta}_n)$$
$$= -\frac{1}{2} \cdot \|\underbrace{\left(-\frac{1}{n} \nabla^2 \ell_n(\tilde{\theta}_n)\right)^{1/2}}_{\xrightarrow{P} J_1(\theta_0)} \underbrace{(\sqrt{n}(\theta_0 - \hat{\theta}_n))}_{\Rightarrow N(0, J_1(\theta_0)^{-1})}\|_2^2$$
$$\Rightarrow -\frac{1}{2} \chi_d^2$$

**Test stat:** $2(\ell_n(\hat{\theta}_n; X) - \ell_n(\theta_0; X)) \xrightarrow{P_{\theta_0}} \chi_d^2$

---

## Composite vs. Composite:

$$H_0: \theta \in \Theta_0 \quad \text{vs} \quad H_1: \theta \in \Theta \setminus \Theta_0,$$

Assume
- $\Theta = \mathbb{R}^d$, $\Theta_0$ $d_0$-dim manifold
- $\theta_0 \in \operatorname{relint}(\Theta_0)$
- $\hat{\theta}_n \xrightarrow{P_{\theta_0}} \theta_0$
- Likelihood "smooth"

Then $2(\ell_n(\hat{\theta}_n) - \ell_n(\hat{\theta}_0)) \Rightarrow \chi_{d-d_0}^2$

where $\hat{\theta}_0 = \operatorname{argmin}_{\theta \in \Theta_0} \ell_n(\theta; X)$

**Why?** Assume wlog $\theta_0 = 0$, $J_1(0) = I_d$ (reparam.)

Then $\hat{\theta}_n \approx N_d(\theta_0, \frac{1}{n} I_d)$

And locally, $\nabla^2 \ell_n(\theta) \approx n I_d$ near $\theta_0$

$$\ell_n(\theta) - \ell_n(\hat{\theta}_n) \approx \frac{n}{2} \|\theta - \hat{\theta}_n\|^2$$

$$\hat{\theta}_0 \approx \operatorname{argmin}_{\theta \in \Theta_0} \|\theta - \hat{\theta}_n\| = \operatorname{Proj}_{\Theta_0}(\hat{\theta}_n)$$

$$2(\ell(\hat{\theta}_n) - \ell_n(\hat{\theta}_0)) \approx n \|\hat{\theta}_n - \operatorname{Proj}_{\Theta_0}(\hat{\theta}_n)\|^2$$
$$= n \|\operatorname{Proj}_{\Theta_0}^\perp(\hat{\theta}_n)\|^2$$
$$\Rightarrow \chi_{d-d_0}^2$$

---

## Asymptotic Equivalence

Recall quadratic approx. picture $(d=1)$:

$$\ell_n(\theta) - \ell_n(\theta_0) \approx \dot{\ell}(\theta_0)(\theta - \theta_0) + \frac{1}{2} J_n(\theta_0)(\theta - \theta_0)^2$$

- GLRT: $\ell_n(\hat{\theta}_n) - \ell_n(\theta_0) \approx \frac{1}{2} J_n^{-1} \dot{\ell}(\theta_0)^2$
- Wald: $\hat{\theta}_n - \theta_0 \approx J_n^{-1} \dot{\ell}(\theta_0)$
- Score: $\dot{\ell}_n(\theta_0)$ (slope at $\theta_0$)

For large $n$,

$$\underbrace{\ell_n(\hat{\theta}_n) - \ell_n(\theta_0)}_{\text{(GLRT)}} \approx \|J_n(\theta_0)^{1/2}(\hat{\theta}_n - \theta_0)\|^2 \approx \underbrace{\|J_n(\theta_0)^{-1/2} \nabla \ell_n(\theta_0)\|^2}_{\text{(Score)}}$$

$$\approx \underbrace{\|\hat{J}_n^{1/2}(\hat{\theta}_n - \theta_0)\|^2}_{\text{(Wald)}}$$

---

## Asymptotic Relative Efficiency (ARE)

Suppose $\hat{\theta}_n^{(i)}$, $i = 1, 2$ are two asy. Normal estimators of $\theta_0 \in \mathbb{R}$, with

$$\sqrt{n}(\hat{\theta}_n^{(i)} - \theta_0) \Rightarrow N(0, \sigma_i^2)$$

The ARE of $\hat{\theta}^{(2)}$ wrt $\hat{\theta}^{(1)}$ is $\sigma_1^2 / \sigma_2^2$

e.g. if $\sigma_2^2 = 2\sigma_1^2$ then $\hat{\theta}^{(2)}$ is $50\%$ as efficient

## Interpretation:

Suppose $\sigma_1^2 / \sigma_2^2 = \gamma \in (0, 1)$

Then for large $n$,

$$\hat{\theta}_{\lfloor\gamma n\rfloor}^{(1)}(X_1, \ldots, X_{\lfloor\gamma n\rfloor}) \overset{D}{\approx} \hat{\theta}_n^{(2)}(X_1, \ldots, X_n) \approx N(\theta, \frac{\sigma_2^2}{n})$$

Using $\hat{\theta}^{(2)}$ is like throwing away $100(1-\gamma)\%$ of the data and then using $\hat{\theta}^{(1)}$

---

[← Ex Generalized linear model with fixed $x$](02-ex-generalized-linear-model-with-fixed.md) · [Up: contents](index.md)
