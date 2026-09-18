---
title: 2. ANOVA with random effects (25 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/final2019.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/final2019.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/old-exams/final2019.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/final2019.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2. ANOVA with random effects (25 points, 5 points / part).

Some useful facts for this problem:

• For $\sigma > 0$ and $\mu \in \mathbb{R}$, the Gaussian density for $X \sim N(\mu, \sigma^2)$ is $\frac{1}{\sqrt{2\pi\sigma^2}} \exp\{-\frac{(x-\mu)^2}{2\sigma^2}\}$. If $\sigma^2 = 0$ then $X = 0$ almost surely.

• For a positive integer $k$, the $\chi^2_k$ density for $X \sim \chi^2_k$ is
$$
\frac{1}{2^{k/2}\Gamma(k/2)} x^{k/2-1} e^{-x/2}.
$$
Its mean and variance are $k$ and $2k$, respectively.

Assume we observe $X_{ij}$ for $i = 1, \dots, m$ and $j = 1, \dots, n$, and consider the hierarchical Gaussian model
$$
\begin{aligned}
\alpha_i &\overset{\text{i.i.d.}}{\sim} N(0, \tau^2) \\
X_{ij} \mid \alpha &\overset{\text{ind.}}{\sim} N(\mu + \alpha_i, \sigma^2).
\end{aligned}
$$

Define the following quantities for the purposes of this problem:
$$
\begin{aligned}
\overline{X}_{i\cdot} &= \frac{1}{n} \sum_j X_{ij}, \\
S_i^2 &= \frac{1}{n - 1} \sum_j (X_{ij} - \overline{X}_{i\cdot})^2, \\
\overline{X}_{\cdot\cdot} &= \frac{1}{nm} \sum_{i,j} X_{ij}, \quad \text{and} \\
S_B^2 &= \frac{1}{m - 1} \sum_i (\overline{X}_{i\cdot} - \overline{X}_{\cdot\cdot})^2 \quad \text{(the B stands for "between groups").}
\end{aligned}
$$

The parameters $\mu \in \mathbb{R}$, $\tau^2 \ge 0$, and $\sigma^2 > 0$ are unknown. $\alpha_1, \dots, \alpha_m$ are unobserved random variables but they are not parameters, and the model could be rewritten without them.

In this problem, unless otherwise stated, you do **NOT** need to show tests and confidence intervals are UMP(U) or UMA(U). Where I ask you to give an explicit formula, it is fine for the formula to be in terms of quantiles of one or more distributions from class.

(a) Show that $S_B^2, S_1^2, \dots, S_m^2$ are mutually independent and give their distribution.

---

(b) Find a finite-sample, equal-tailed confidence interval for $\mu$. Give an explicit formula.

(c) Give a finite-sample test of the null hypothesis $H_0 : \tau^2 = 0$ vs $H_1 : \tau^2 > 0$. Give an explicit formula for the test statistic and the critical value.

(d) (*) Find a finite-sample, equal-tailed confidence interval for $\tau^2/\sigma^2$. Give an explicit formula.

(e) (*) Show that the model (with the additional restriction that $\tau^2 > 0$) is a three-parameter exponential family and $(\overline{X}_{\cdot\cdot}, S_B^2, \sum_i S_i^2)$ is a complete sufficient statistic.

---

Problem 2 answers continued (1):

---

Problem 2 answers continued (2):

---

Problem 2 answers continued (3):

---

---

[← 1. Poisson minimax estimation (24 points, 4 points / part).](02-1-poisson-minimax-estimation-24-points-4-points-part.md) · [Up: contents](index.md) · [3. "And if you ever saw it..." (24 points, 6 points / part). →](04-3-and-if-you-ever-saw-it-24-points-6-points-part.md)
