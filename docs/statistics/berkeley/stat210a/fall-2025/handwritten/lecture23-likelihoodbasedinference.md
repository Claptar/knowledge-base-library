---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture23-likelihoodbasedinference.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture23-likelihoodbasedinference.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture23-likelihoodbasedinference.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture23-likelihoodbasedinference.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

1) Wald test
2) Score test
3) Generalized likelihood ratio test
4) Asymptotic Relative Efficiency

---

## Likelihood-Based Inference

**Setting** $\quad X_1, \dots, X_n \overset{iid}{\sim} p_\theta(x)$, $p_\theta(x)$ "smooth" in $\Theta$

Assume $\mathbb{E}_\theta \nabla \ell(\theta; X_i) = 0$,

$$\mathrm{Var}_\theta [\nabla \ell(\theta; X_i)] = -\mathbb{E}_\theta \nabla^2 \ell(\theta; X_i) = J_1(\theta) \succ 0,$$

$$\hat{\theta}_{\mathrm{MLE}} \xrightarrow{\mathbb{P}_\theta} \theta \quad (\text{consistent})$$

Then, if $\theta = \theta_0$:

$$\frac{1}{\sqrt{n}} \nabla \ell_n(\theta_0; X) \Rightarrow N(0, J_1(\theta_0))$$

$$\frac{1}{n} \nabla^2 J_n(\theta_0; X) \xrightarrow{\mathbb{P}} J_1(\theta_0)$$

Used $0 = \nabla \ell(\hat{\theta}_n) \approx \nabla \ell_n(\theta_0) + \nabla^2 \ell_n(\theta_0) (\hat{\theta}_n - \theta_0)$

to get $\sqrt{n}(\hat{\theta}_n - \theta_0) \Rightarrow N_d(0, J_1(\theta_0)^{-1})$

Can use this for inference on $\theta_0$!

---

## Wald-Type Confidence Regions

Assume we have some estimator $\hat{J}_n \succ 0$ s.t. $\frac{1}{n} \hat{J}_n \xrightarrow{\mathbb{P}} J_1(\theta_0) \succ 0$. Then we can plug in:

If $\sqrt{n}(\hat{\theta}_n - \theta_0) \Rightarrow N_d(0, J_1(\theta_0)^{-1})$

then $(J_1(\theta_0))^{1/2} \sqrt{n} (\hat{\theta}_n - \theta_0) \Rightarrow N_d(0, I_d)$

so $\hat{J}_n^{1/2} (\hat{\theta}_n - \theta_0) \Rightarrow N_d(0, I_d) \quad (\text{Slutsky})$

Leads to test of $H_0: \theta = \theta_0$:

$$\|\hat{J}_n^{1/2} (\hat{\theta}_n - \theta_0)\|^2 \Rightarrow \chi_d^2 \quad (\text{Reject if large})$$

So, $\mathbb{P}_{\theta_0} \left( \hat{J}_n^{1/2} (\hat{\theta}_n - \theta_0) \ge \chi_d^2(\alpha) \right) \to \alpha$
where $\chi_d^2(\alpha)$ is the $1-\alpha$ quantile.

Note we reject $\theta_0$ iff $\|\hat{J}_n^{1/2}(\hat{\theta}_n - \theta_0)\|^2 > \chi_d^2(\alpha)$

$\Leftrightarrow$ reject $\theta_0$ iff $\theta_0 \notin \underbrace{\hat{\theta}_n + \hat{J}_n^{-1/2} B_{\chi_d^2(\alpha)}(0)}_{\text{confidence ellipsoid}}$

<!-- Hand-drawn diagram: an ellipse representing the region, centered near \hat{\theta}_n -->

More info $\Leftrightarrow$ smaller ellipse (shrinks like $1/\sqrt{n}$)

---

## Options for $\hat{J}_n$:

1) Most obvious is to "plug in" the MLE:
   $$\hat{J}_n = J_n(\hat{\theta}_n) \qquad (\text{MLE for } J_n(\theta))$$
   $$= \mathrm{Var}_\theta (\nabla \ell_n(\theta; X)) \Big|_{\theta = \hat{\theta}_n}$$
   $$(\text{NB}) \ne \mathrm{Var}_{\hat{\theta}_n} (\nabla \ell_n(\hat{\theta}_n(X); X)) = 0$$

   Or, $\hat{J}_n = -\mathbb{E}_\theta \nabla^2 \ell_n(\theta) \Big|_{\theta = \hat{\theta}_n}$

2) Observed Fisher info:
   $$\hat{J}_n = -\nabla^2 \ell_n(\hat{\theta}_n; X)$$

**Remarks**:
- Both have $\frac{1}{n} \hat{J}_n \xrightarrow{\mathbb{P}} J_1(\theta_0)$ in "nice" iid sampling setting
- Both make sense outside of iid setting
- Heuristically, plug-in measures info about $\theta$ in "typical" data set but obs. info. measures info about $\theta$ in "this" data set

---

## Wald interval for $\theta_j$:

If $\hat{\theta}_n \approx N_d(\theta_0, J_n(\theta_0)^{-1})$

then $\hat{\theta}_{n,j} \approx N_1(\theta_{0,j}, \underbrace{(J_n(\theta_0)^{-1})_{jj}}_{\mathrm{s.e.}(\hat{\theta}_{n,j})^2})$

Leads to univariate interval:
$$C_j = \hat{\theta}_{nj} \pm \widehat{\mathrm{s.e.}}(\hat{\theta}_{n,j}) \cdot z_{\alpha/2}$$
$$= \hat{\theta}_{nj} \pm \sqrt{(\hat{J}_n^{-1})_{jj}} \cdot z_{\alpha/2}$$

`glm` function in R uses these intervals / p-values, with $\hat{J}_n = -\nabla^2 \ell(\hat{\theta}_n)$

Conf. ellipsoid for $\theta_{0,S} = (\theta_{0,j})_{j \in S}$ : ($|S| = k$)
$$\hat{\theta}_{n,S} \approx N_k(\theta_{0,S}, (J_n(\theta_0)^{-1})_{SS})$$
$$\leadsto C_S = \hat{\theta}_{n,S} + ((\hat{J}_n^{-1})_{SS})^{1/2} B_{\chi_k^2(\alpha)}(0)$$

More generally, if $\sqrt{n}(\hat{\theta}_n - \theta_0) \Rightarrow N(0, \Sigma(\theta_0))$
and $\frac{1}{n}\hat{\Sigma}_n \xrightarrow{\mathbb{P}_\theta} \Sigma(\theta_0)$ ($\hat{\theta}_n$ not nec. MLE)
then we can do the same things

---

## Ex

---

[Up: contents](../index.md)
