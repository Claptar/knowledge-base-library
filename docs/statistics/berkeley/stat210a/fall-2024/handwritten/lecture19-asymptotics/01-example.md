---
title: Example
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture19-asymptotics.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture19-asymptotics.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture19-asymptotics.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture19-asymptotics.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Example

1) Convergence in Probability and Distribution

2) Continuous Mapping, Slutsky's Theorem

3) Delta method

---

### Logistic Regression (fixed design)

$(x_i, y_i)$ pairs $i = 1, \dots, n$

* $x_i \in \mathbb{R}^d$ Continuous feature vector, fixed ($x_{i,1} = 1$ for intercept)
* $Y_i \overset{\text{ind.}}{\sim} \text{Bern.}(\pi_\beta(x_i))$
* $\text{logit}(\pi_\beta(x_i)) = \log \frac{\pi_\beta}{1 - \pi_\beta} = \beta' x_i$

$$
\begin{aligned}
p_\beta(y \mid x) &= \prod_{i=1}^n \pi_\beta(x_i)^{y_i} (1 - \pi_\beta(x_i))^{1 - y_i} \\
&= \prod_{i=1}^n e^{(\beta' x_i) y_i + \log(1 - \pi_\beta(x_i))} \\
&= e^{\beta' X' y + A(\beta; x_i)} \qquad X = \begin{pmatrix} - x_1' - \\ \vdots \\ - x_n' - \end{pmatrix} \in \mathbb{R}^{n \times d}
\end{aligned}
$$

Sufficient statistics: $T(y) = X'y$

Natural parameter: $\beta$

Idea to test $H_0 : \beta_1 = 0$ : Condition on $X_{-1}' Y$
$\cdots$ but that would condition on $Y$

Ideas to estimate $\beta$: UMVUE? generically doesn't exist
Bayes? need prior on $\beta \in \mathbb{R}^d$

---

Software packages use general purpose asymptotic methods

$$
\begin{aligned}
\hat{\beta}_{\text{MLE}}(x, y) &= \operatorname*{argmax}_{\beta \in \mathbb{R}} p_\beta(y \mid x) = \ell(\beta; x, y) \\
&= \operatorname*{argmax}_{\beta \in \mathbb{R}^d} \underbrace{\beta' X' y - A(\beta; x_i)}_{(\text{concave})}
\end{aligned}
$$

Asymptotically, $\hat{\beta}_{\text{MLE}} \approx N(\beta, \mathcal{J}(\beta)^{-1})$
(large $n$)
$\uparrow$ unbiased $\quad \uparrow$ efficient

$\underset{\text{(Hessian)}}{\nabla^2 \ell(\hat{\beta}; x, y)} \approx \mathbb{E}_\beta[\nabla^2 \ell(\beta; x, y)] = \mathcal{J}(\beta)$

$\hat{\Sigma} = (-\nabla^2 \ell(\hat{\beta}))^{-1} \approx \Sigma(\beta) = \mathcal{J}(\beta)^{-1}$

Test / interval: $Z_j = \frac{\hat{\beta}_j - \beta_j}{\hat{\sigma}_j} \approx N(0, 1) \qquad (\sigma_j^2 = \Sigma_{jj})$

Test $H_0 : \beta_j = 0$ : reject if $\hat{\beta}_j / \hat{\sigma}_j$ large / small / extreme

Invert: $|z_j| < z_{\alpha/2} \iff \beta_j \in \hat{\beta}_j \pm z_{\alpha/2} \hat{\sigma}_j$

---

## Asymptotics

[So far, everything has been finite-sample, often using special properties of model $\mathcal{P}$ (e.g. exp. fam.) to do exact calculations.]

[For "generic" models, exact calculations may be intractable or impossible. But we may be able to approximate our problem with a simpler problem in which calculations are easy]

[Typically approximate by Gaussian, by taking limit as # observations $\to \infty$. But this is only interesting if approx. is good for "reasonable" sample size.]

---

---

[Up: contents](index.md) · [Convergence →](02-convergence.md)
