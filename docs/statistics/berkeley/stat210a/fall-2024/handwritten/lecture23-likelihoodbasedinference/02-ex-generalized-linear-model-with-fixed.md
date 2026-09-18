---
title: Ex Generalized linear model with fixed $x$
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture23-likelihoodbasedinference.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture23-likelihoodbasedinference.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture23-likelihoodbasedinference.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture23-likelihoodbasedinference.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Ex Generalized linear model with fixed $x$

$x_1, \dots, x_n \in \mathbb{R}^d$ fixed

$Y_i \overset{\text{ind.}}{\sim} p_{\eta_i}(y) = e^{\eta_i y_i - A(\eta_i)} h(y_i)$

$\eta_i = \beta' x_i$ (**canonical form**)

Let $\mu_i(\beta) = \mathbb{E}_\beta Y_i \quad (= \mu(\eta_i(\beta)))$

(more general: $f(\mu_i) = \beta' x_i$ for link fcn $f$)

Most common examples:
- Logistic regression: $Y_i \overset{\text{ind.}}{\sim} \text{Bern}\left(\frac{e^{x_i' \beta}}{1 + e^{x_i' \beta}}\right)$
- Poisson log-linear model: $Y_i \overset{\text{ind.}}{\sim} \text{Pois}(e^{x_i' \beta})$

$$\ell_n(\beta; Y) = \sum_i (x_i' \beta) y_i - A(x_i' \beta) - \log h(y_i)$$

$$\nabla \ell_n(\beta; Y) = \sum_i y_i x_i - \dot{A}(x_i' \beta) \cdot x_i$$
$$= \sum_i (y_i - \mu_i(\beta)) x_i$$

$$-\nabla^2 \ell_n(\beta; Y) = \sum_i \ddot{A}(x_i' \beta) \cdot x_i x_i'$$
$$= \sum_i \mathrm{Var}_\beta(y_i) \cdot x_i x_i'$$
$$= \mathrm{Var}_\beta(\nabla \ell_n(\beta; Y)) \quad (\text{Not random})$$

---

$$(-\nabla^2 \ell_n(\beta))^{-1/2} \nabla \ell_n(\beta) \sim (0, I_d) \quad \text{in finite samples}$$
$$\overset{*}{\Rightarrow} \mathcal{N}_d(0, I_d)$$

\* Under regularity cond. on $X = \begin{pmatrix} - x_1' - \\ \vdots \\ - x_n' - \end{pmatrix}$

Taylor expansion of $\ell_n$ leads to
$$\hat{J}_n^{1/2} (\hat{\beta}_n - \beta) \Rightarrow \mathcal{N}_d(0, I_d)$$

## Advantages of Wald test:
1) Easy to invert, simple conf. regions
2) Asymptotically correct

## Disadvantages:
1) Have to compute MLE
2) Depends on parameterization
3) Relies on two approximations:
   $\nabla \ell_n \approx \text{Normal}$ and $\ell_n \approx \text{quadratic}$
4) Need MLE to be consistent
5) Confidence interval / ellipsoid might go outside $\Theta$!

---

---

[← Outline](01-outline.md) · [Up: contents](index.md) · [Lecture 23 — likelihoodbasedinference Part 03 — →](03-lecture-23-likelihoodbasedinference-part-03.md)
