---
title: Nonparametric Estimation
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture25-bootstrap.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture25-bootstrap.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture25-bootstrap.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture25-bootstrap.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Nonparametric Estimation

1) Nonparametric Estimation
2) Plug-in estimator
3) Bootstrap standard errors
4) Bootstrap bias estimator / correction
5) Bootstrap confidence intervals
6) Double bootstrap

---

**Setting** Nonparametric iid sampling model
$$X_1, \dots, X_n \overset{iid}{\sim} P, \quad P \text{ unknown}$$

Want to do inference on some "parameter" $\theta(P)$ (functional)

**Ex**
a) $\theta(P) = \text{median}(P) \quad (X \in \mathbb{R})$
b) $\theta(P) = \lambda_{\max}(\text{Var}_P(X_i)) \quad (X \in \mathbb{R}^d)$
c) $\theta(P) = \underset{\theta \in \mathbb{R}^d}{\text{argmin}} \, \mathbb{E}_P \left[(Y_i - \theta' X_i)^2\right] \quad (X_i, Y_i) \overset{iid}{\sim} P$
d) $\theta(P) = \underset{\theta \in \Theta}{\text{argmin}} \, D_{\text{KL}}(P \parallel P_\theta) \quad (\text{best-fitting model even if misspec.})$
$$= \underset{\theta}{\text{argmax}} \, \mathbb{E}_P[\ell(\theta; X_i)]$$

Recall the **empirical dist.** of $X_1, \dots, X_n$ is
$$\hat{P}_n = \frac{1}{n} \sum \delta_{X_i} \quad \left(\hat{P}_n(A) = \frac{#\{i : X_i \in A\}}{n}\right)$$

The **plug-in estimator** of $\theta(P)$ is $\hat{\theta} = \theta(\hat{P}_n)$
a) Sample median
b) $\lambda_{\max}(\text{sample var})$
c) OLS estimator
d) MLE for $\{P_\theta : \theta \in \Theta\}$

---

Does plug-in estimator work? Depends

$\hat{P}_n \overset{P}{\to} P$? Dep. on what sense of convergence

$\hat{P}_n(A) \overset{P}{\to} P(A)$ for all $A \quad \checkmark$

(TV) $\sup_A |\hat{P}_n(A) - P(A)| \overset{P}{\not\to} 0$ if $P$ cts $\quad \times$
(use $A_n = \{X_1, \dots, X_n\}$)

$\sup_x |\hat{P}_n((-\infty, x]) - P((-\infty, x])| \overset{P}{\to} 0$ for $X \in \mathbb{R} \quad \checkmark$ (Glivenko-Cantelli)

Want $\theta(P)$ to be cts wrt some topology in which $\hat{P}_n \overset{P}{\to} P$, then $\theta(\hat{P}_n) \overset{P}{\to} \theta(P)$

**Counterexamples**
$\theta(P) = \mathbf{1}\{P \text{ is absolutely cts}\} \quad (P \ll \text{Lebesgue})$
$\theta(P) = \mathbf{1}\{P \text{ is integrable}\} \quad (\mathbb{E}_P|X| < \infty)$

$\hat{P}_n$ always integrable, never abs. cts., for all $n$.

---

---

[Up: contents](index.md) · [Bootstrap standard errors →](02-bootstrap-standard-errors.md)
