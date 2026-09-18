---
title: 2 Bayesian Regularization
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwelve153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureTwelve153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Bayesian Regularization

We now treat regularization in high-dimensional regression from the Bayesian point of view. Before discussing regularization, let us first recap the basics of Bayesian regression in the model:
$$y = X\beta + \epsilon \quad \text{with } \epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2).$$
The basic prior that we used previously is
$$\beta_j \overset{\text{i.i.d}}{\sim} \text{Unif}(-C, C).$$

for a large positive constant $C$. For this prior, we showed (see e.g., problem 5 in Homework 1) that
$$\beta \mid \text{data}, \sigma \sim N\left((X^T X)^{-1} X^T y, \sigma^2 (X^T X)^{-1}\right) \tag{5}$$
when $C \to \infty$. This fact is not quite true if $C$ is not very large.

A slightly different prior which allows exact formulae even for finite $C$ is the Gaussian prior:
$$\beta_j \overset{\text{i.i.d}}{\sim} N(0, C). \tag{6}$$
Under this prior, it turns out that
$$\beta \mid \text{data}, \sigma \sim N\left(\left(\frac{X^T X}{\sigma^2} + \frac{I}{C}\right)^{-1} \frac{X^T y}{\sigma^2}, \left(\frac{X^T X}{\sigma^2} + \frac{I}{C}\right)^{-1}\right) \tag{7}$$
where $I$ is the identity matrix. It is instructive to compare (5) and (7). Unlike (5) which is only true for large $C$, the fact (7) is true for every $C > 0$. It is also clear that when $C \to \infty$, then (7) is the same as (5). Observe that when $C$ is large, there is not much difference qualitatively between $\text{unif}(-C, C)$ and $N(0, C)$ (they are both uninformative priors).

We shall prove a more general form of (7) later in this lecture.

Now let us specialize to the case of the high dimensional regression (2). If we use the prior (6) with $C \to \infty$, then the posterior mean becomes the unregularized least squares (or unregularized MLE) estimator $(X^T X)^{-1} X^T y$. The fitted values will then perfectly interpolate the data leading to overfitting. From the Bayesian perspective, this is happening because the prior (6) with very large $C$ is not useful for this dataset. The prior needs to be changed for a more meaningful analysis. In the frequentist analysis, the main motivation for the ridge regularization (3) is the need to obtain smaller estimates for $\beta_2, \dots, \beta_{n-1}$ which will lead to a smoother fit to the data. This same effect can be obtained by the following modification of the prior (6):
$$\beta_0, \beta_1 \overset{\text{i.i.d}}{\sim} N(0, C) \quad \text{and} \quad \beta_2 \dots, \beta_{n-1} \overset{\text{i.i.d}}{\sim} N(0, \tau^2) \tag{8}$$
for a small parameter $\tau$ (in the above, we also assume that $\beta_0, \dots, \beta_{n-1}$ are all independent). The prior (8) can be written as
$$\beta \sim N(0, Q) \tag{9}$$
where $Q$ is the diagonal matrix with diagonal entries $C, C, \tau^2, \dots, \tau^2$. Under the prior (9), the posterior of $\beta$ is given by
$$\beta \mid \text{data}, \sigma \sim N\left(\left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2}, \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1}\right) \tag{10}$$
We will prove this result later in this lecture. The posterior mean therefore is given by
$$\left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2} = \left(X^T X + \sigma^2 Q^{-1}\right)^{-1} X^T y. \tag{11}$$
This expression is closely related to the ridge estimator (4). Note that $Q^{-1}$ is diagonal with diagonal entries $1/C, 1/C, 1/\tau^2, \dots, 1/\tau^2$. When $C$ is very large, the first two diagonal entries of $Q^{-1}$ are very close to zero so that
$$Q^{-1} \approx \frac{1}{\tau^2} J.$$

Thus the posterior mean (11) is therefore
$$\left(X^T X + \frac{\sigma^2}{\tau^2} J\right)^{-1} X^T y$$
which matches (4) if
$$\lambda = \frac{\sigma^2}{\tau^2} \quad \text{or, equivalently } \tau = \frac{\sigma}{\sqrt{\lambda}}.$$
Ridge regularization therefore can be understood as Bayesian regression with the prior (8). The precise equivalence is obtained if $\lambda$ is related to $\tau^2$ via $\lambda = \sigma^2/\tau^2$.

---

[← 1 Recap: Ridge Regression](01-1-recap-ridge-regression.md) · [Up: contents](index.md) · [3 Bayesian approach for dealing with unknown $\tau$ and $\sigma$ →](03-3-bayesian-approach-for-dealing-with-unknown-and.md)
