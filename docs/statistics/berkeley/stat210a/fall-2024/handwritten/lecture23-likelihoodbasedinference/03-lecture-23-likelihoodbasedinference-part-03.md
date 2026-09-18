---
title: Lecture 23 — likelihoodbasedinference Part 03 —
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture23-likelihoodbasedinference.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture23-likelihoodbasedinference.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture23-likelihoodbasedinference.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture23-likelihoodbasedinference.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture 23 — likelihoodbasedinference Part 03 —

Test $H_0: \theta = \theta_0 \quad \text{vs.} \quad H_1: \theta \ne \theta_0$

We can bypass quadratic approximation entirely by using score as test stat

$$\frac{1}{\sqrt{n}} \nabla \ell_n(\theta_0; X) \overset{P_{\theta_0}}{\Longrightarrow} \mathcal{N}_d(0, J_1(\theta_0))$$

$$\left( \text{or } J_n(\theta_0)^{-1/2} \nabla \ell_n(\theta_0; X) \overset{P_{\theta_0}}{\Longrightarrow} \mathcal{N}_d(0, I_d) \right)$$

So, we can reject $H_0: \theta = \theta_0$ if
$$\|J_n(\theta_0)^{-1/2} \nabla \ell_n(\theta_0; X)\|_2^2 \ge \chi^2_d(\alpha)$$

$d=1$:
$$\frac{\dot{\ell}_n(\theta_0)}{\sqrt{J_n(\theta_0)}} \Rightarrow \mathcal{N}(0, 1),$$
can do 1-sided tests

## Remarks
- No quadratic approx., no MLE
- No need to estimate Fisher info at $\theta_0$

Can be generalized to case with nuisance params. Typically estimate via MLE on $\Theta_0$.

---

Score test is invariant to reparameterization*

Assume $d=1$, $\theta = g(\zeta)$, $\dot{g}(\zeta) > 0 \;\forall \zeta$

$$q_\zeta(x) = p_{g(\zeta)}(x)$$

$$\dot{\ell}^{(\zeta)}(\zeta; x) = \frac{d}{d\zeta} \log p_{g(\zeta)}(x)$$
$$= \dot{\ell}^{(\theta)}(g(\zeta); x) \cdot \dot{g}(\zeta)$$

$$J^{(\zeta)}(\zeta) = J^{(\theta)}(g(\zeta)) \cdot \dot{g}(\zeta)^2$$

So $\frac{\dot{\ell}^{(\zeta)}(\zeta_0; x)}{\sqrt{J^{(\zeta)}(\zeta_0)}} \overset{\text{a.s.}}{=} \frac{\dot{\ell}^{(\theta)}(\theta_0; x)}{\sqrt{J^{(\theta)}(\theta_0)}}$

if $\theta_0 = g(\zeta_0)$

## **Ex** $s$-parameter exp. fam:

$$X_1, \dots, X_n \overset{\text{iid}}{\sim} e^{\eta' T(x) - A(\eta)} h(x)$$

$$\nabla \ell(\eta; X) = \sum T(X_i) - n \mu(\eta)$$

$$\|J_n(\eta_0)^{-1/2} (\sum T(X_i) - n\mu(\eta_0))\|^2 \Rightarrow \chi^2_d$$

$$\frac{\sum T(X_i) - n\mu(\eta_0)}{\sqrt{n \mathrm{Var}_{\eta_0}(T(X_i))}} \overset{P_{\eta_0}}{\Longrightarrow} \mathcal{N}(0, 1)$$

---

## **Ex** Pearson's $\chi^2$ test (goodness of fit)

$$N = (N_1, \dots, N_d) \sim \mathrm{Multinom}(n, (\pi_1, \dots, \pi_d))$$
$$= \frac{n! \, \pi_1^{N_1} \cdots \pi_d^{N_d}}{N_1! \cdots N_d!} \mathbf{1}\{\sum N_i = n\}$$

Note $\sum \pi_j = 1$ so this is a full-rank $(d-1)$-parameter exp. family, e.g.

$$\pi_j = \begin{cases} \frac{1}{1 + \sum_{k>1} e^{\eta_k}} & j = 1 \\ \frac{e^{\eta_j}}{1 + \sum_{k>1} e^{\eta_k}} & j > 1 \end{cases}$$

$$\nabla \ell(\eta; N) = (N_2, \dots, N_d) - (n\pi_2, \dots, n\pi_d)$$

$$\mathrm{Var}_\eta(\nabla \ell(\eta)) = \begin{pmatrix} n\pi_2(1-\pi_2) & & -n\pi_i\pi_j \\ & \ddots & \\ -n\pi_i\pi_j & & n\pi_d(1-\pi_d) \end{pmatrix}$$
$$= n \left( \mathrm{diag}(\pi_{2:d}) - \pi_{2:d} \pi_{2:d}' \right)$$

$$\Rightarrow J_n(\eta)^{-1} = \frac{1}{n} \cdot \left( (\mathrm{diag}(\pi_{2:d}))^{-1} - \pi_1^{-1} \mathbf{1}\mathbf{1}' \right)$$
$$(\text{uses } (A + uv')^{-1} = A^{-1} - \frac{A^{-1}uv'A^{-1}}{1 + v'A^{-1}u})$$

Score test of $H_0: \pi = \pi_0$:
$$\nabla \ell_n(\eta_0) J_n^{-1}(\eta_0) \nabla \ell_n(\eta_0) \overset{(\text{algebra})}{\underset{\downarrow}{=}} \sum_{j=1}^d \frac{(N_j - n\pi_{0,j})^2}{n\pi_{0,j}} \overset{P_{\pi_0}}{\Longrightarrow} \chi^2_{d-1}$$
(don't really need asy. approx)

---

---

[← Ex Generalized linear model with fixed $x$](02-ex-generalized-linear-model-with-fixed.md) · [Up: contents](index.md) · [Generalized LRT →](04-generalized-lrt.md)
