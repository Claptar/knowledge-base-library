---
title: 2. Inverse gamma prior (20 points, 5 points / part). Some useful facts for
  this problem
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2024.pdf
source_file: sources/berkeley-stat210a/fall-2025/old-exams/final2024.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/final2024.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/old-exams/final2024.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2. Inverse gamma prior (20 points, 5 points / part). Some useful facts for this problem

• A $\chi^2_d$ random variable has mean $d$ and variance $2d$.

• If $Y$ is a $\text{Gamma}(\alpha, \beta)$ random variable (in its “rate parameterization”) then it has density
$$
\frac{\beta^\alpha}{\Gamma(\alpha)} y^{\alpha-1} \exp\{-\beta y\},
$$
on $(0, \infty)$. $Y$ has mean $\alpha/\beta$ and variance $\alpha/\beta^2$. This distribution is defined for $\alpha, \beta > 0$.

• The inverse-gamma distribution (denoted $\text{IG}(\alpha, \beta)$) is the distribution of $W = 1/Y$ where $Y \sim \text{Gamma}(\alpha, \beta)$. Then $W \in (0, \infty)$ has the density
$$
\frac{\beta^\alpha}{\Gamma(\alpha)} w^{-\alpha-1} \exp\{-\beta/w\}.
$$
Note that $\beta$ is a scale parameter for $W$. $W$ has mean $\frac{\beta}{\alpha-1}$ provided $\alpha > 1$, and variance $\frac{\beta^2}{(\alpha-1)^2(\alpha-2)}$ provided $\alpha > 2$. This distribution is likewise defined for $\alpha, \beta > 0$.

• Define the squared relative error loss function
$$
L_{\text{rel}}(d, \theta) = \left( \frac{d - \theta}{\theta} \right)^2 = \left( \frac{d}{\theta} - 1 \right)^2,
$$
and define the corresponding risk function $R_{\text{rel}}(\delta(\cdot), \theta) = \mathbb{E}_\theta[L_{\text{rel}}(\delta(X), \theta)]$.

Consider the Bayesian model with
\$\$
\theta \sim \text

---

[← 1. Six Gaussians (20 points, 5 points / part).](02-1-six-gaussians-20-points-5-points-part.md) · [Up: contents](index.md)
