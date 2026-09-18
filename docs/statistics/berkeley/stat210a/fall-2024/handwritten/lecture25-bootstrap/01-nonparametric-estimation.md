---
title: Nonparametric Estimation
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture25-bootstrap.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture25-bootstrap.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture25-bootstrap.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture25-bootstrap.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Nonparametric Estimation

1) Nonparametric Estimation
2) Plug-in estimator
3) Bootstrap standard errors
4) Bootstrap bias estimator / correction
5) Bootstrap confidence intervals
6) Double bootstrap

---

**Setting** Nonparametric iid sampling model
$$X_1, \dots, X_n \overset{\text{iid}}{\sim} P, \quad P \text{ unknown}$$

Want to do inference on some "parameter" $\theta(P)$ (functional)

**Ex**
a) $\theta(P) = \text{median}(P) \quad (X \in \mathbb{R})$
b) $\theta(P) = \lambda_{\max}(\text{Var}_P(X_i)) \quad (X \in \mathbb{R}^d)$
c) $\theta(P) = \underset{\theta \in \mathbb{R}^d}{\text{argmin}} \ \mathbb{E}_P \left[ (Y_i - \theta' X_i)^2 \right] \quad ((X_i, Y_i) \overset{\text{iid}}{\sim} P)$
d) $\theta(P) = \underset{\theta \in \Theta}{\text{argmin}} \ D_{\text{KL}}(P \parallel P_\theta) \quad (\text{best-fitting model even if misspec.})$
$$= \underset{\theta}{\text{argmax}} \ \mathbb{E}_P [\ell(\theta; X_i)]$$

**Recall** the empirical dist. of $X_1, \dots, X_n$ is
$$\hat{P}_n = \frac{1}{n} \sum_{i=1}^n \delta_{X_i} \quad \left( \hat{P}_n(A) = \frac{#\{i : X_i \in A\}}{n} \right)$$

The **plug-in estimator** of $\theta(P)$ is $\hat{\theta} = \theta(\hat{P}_n)$
a) Sample median
b) $\lambda_{\max}(\text{sample var})$
c) OLS estimator
d) MLE for $\{P_\theta : \theta \in \Theta\}$

---

Does plug-in estimator work? Depends.

$\hat{P}_n \overset{p}{\to} P$? Dep. on what sense of convergence

$\hat{P}_n(A) \overset{p}{\to} P(A)$ for all $A$ $\checkmark$

$\sup_A |\hat{P}_n(A) - P(A)| \overset{p}{\not\to} 0$ if $P$ cts $\times$ (TV)
(use $A_n = \{X_1, \dots, X_n\}$)

$\sup_x |\hat{P}_n((-\infty, x]) - P((-\infty, x])| \overset{p}{\to} 0$ for $X \in \mathbb{R}$ $\checkmark$ (Glivenko-Cantelli)

Want $\theta(P)$ to be cts wrt some topology in which $\hat{P}_n \overset{p}{\to} P$, then $\theta(\hat{P}_n) \overset{p}{\to} \theta(P)$

**Counterexamples**
$\theta(P) = \mathbf{1}\{P \text{ is absolutely cts}\} \quad (P \ll \text{Lebesgue})$
$\theta(P) = \mathbf{1}\{P \text{ is integrable}\} \quad (\mathbb{E}_P |X| < \infty)$

$\hat{P}_n$ always integrable, never abs. cts., for all $n$.

---

## Bootstrap standard errors

Suppose $\hat{\theta}_n(X)$ is an estimator for $\theta(P)$ (maybe plug-in, maybe not)

What is its standard error? Use plug-in:

$$\widehat{\text{s.e.}}(\hat{\theta}_n) = \sqrt{\text{Var}_{\hat{P}_n}(\hat{\theta}_n^*)} \quad \left[\text{use } \hat{\theta}_n^* \text{ to indicate new sample } X^*, \text{ not } X\right]$$

$$\text{Var}_{\hat{P}_n}(\hat{\theta}_n^*) = \text{Var}_{X_1^*, \dots, X_n^* \overset{\text{iid}}{\sim} \hat{P}_n} (\hat{\theta}_n(X_1^*, \dots, X_n^*))$$

How to compute? Monte Carlo:

For $b = 1, \dots, B$:
$$\text{Sample } X_1^{*b}, \dots, X_n^{*b} \overset{\text{iid}}{\sim} \hat{P}_n \quad \leftarrow \left[\text{Sample } n \text{ points with replacement from original sample}\right]$$
$$\hat{\theta}^{*b} = \hat{\theta}(X_1^{*b}, \dots, X_n^{*b})$$

$$\overline{\theta^*} = \frac{1}{B} \sum_{b=1}^B \hat{\theta}^{*b}$$

$$\widehat{\text{s.e.}}(\hat{\theta}_n) = \sqrt{\frac{1}{B} \sum_b (\hat{\theta}^{*b} - \overline{\theta^*})^2}$$

Note this is a Monte Carlo numerical approx. to the idealized Bootstrap estimator, which we could compute by iterating over all $n^n$ possible $X^* = (X_1^*, \dots, X_n^*)$ vectors.

---

---

[Up: contents](index.md) · [Bootstrap Bias Correction →](02-bootstrap-bias-correction.md)
