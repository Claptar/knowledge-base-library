---
title: 3. Two-by-two count table (25 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/final2021.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/final2021.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/old-exams/final2021.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/final2021.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3. Two-by-two count table (25 points, 5 points / part).

Some useful facts for this problem:
- For $\theta > 0$, the Poisson density for $X \sim \text{Pois}(\theta)$ is $\frac{\theta^x e^{-\theta}}{x!}$ on $x = 0, 1, \dots$. The mean and variance are both $\theta$.
- For $\pi_1, \dots, \pi_d \ge 0$ with $\sum_{i=1}^d \pi_i = 1$, the multinomial density for $X \sim \text{Multinom}(n, \pi)$ is
$$p_{n,\pi}(x) = n! \cdot \prod_{i=1}^d \frac{\pi_i^{x_i}}{x_i!},$$
on $x \in \{0, \dots, n\}^d$ with $\sum_i x_i = n$.
- Suppose $X_i \sim \text{Pois}(\theta_i)$ with $\theta_i > 0$, independently for $i = 1, \dots, d$, and let $X_+ = \sum_{i=1}^d X_i$ and $\theta_+ = \sum_{i=1}^d \theta_i$. Then, conditional on $X_+ = n$,
$$(X_1, \dots, X_d) \sim \text{Multinom}(n, (\theta_1, \dots, \theta_d)/\theta_+)$$

Assume that $X_{ij} \sim \text{Pois}(\lambda_{ij})$, independently for $i, j \in \{0, 1\}$. We will consider the model with $\lambda_{ij} = \lambda_0 \rho^{i+j}$, for $\lambda_0, \rho > 0$. Except when otherwise specified, assume both parameters are unknown.

(a) Give a complete sufficient statistic for the model and show it is complete.

(b) Assume (for this part only) that $\lambda_0$ is known, but $\rho$ is unknown. Suggest a UMP test of $H_0 : \rho = \rho_0$ vs. $H_1 : \rho > \rho_0$. You do not need to give an explicit cutoff for your test but give an explicit formula for the test statistic, explain how you would find the cutoff, and explain why your test is UMP.

(c) Assuming again that both parameters are unknown, suggest a UMPU test of $H_0 : \rho = 1$ against $H_1 : \rho > 1$. You do not need to give an explicit cutoff for your test but explain how you would calculate it. If the data are $X_{00} = X_{01} = 0$ and $X_{10} = X_{11} = 1$, calculate the (conservative, non-randomized) p-value for your test.

(d) For the same data set, $X_{00} = X_{01} = 0$ and $X_{10} = X_{11} = 1$, find the maximum likelihood estimators for $\lambda_0$ and $\rho$. Give your answers as explicit numbers.

(e) (*) Now suppose we consider a relaxed model $\lambda_{ij} = f(i + j)$, for any strictly positive real-valued function $f$ on $\{0, 1, 2\}$. This includes our previous parametric model as a special case since we could have $f(i + j) = \lambda_0 \rho^{i+j}$. Does there exist a UMPU test of the null hypothesis that our previous model was correctly specified, against the alternative that it was misspecified but the relaxed model is correct? Explain why or why not. (If you say yes you only need to give enough details to establish that such a test exists).

---

Problem 3 answers continued (1):

---

Problem 3 answers continued (2):

---

Problem 3 answers continued (3):

---

---

[← 2. Contamination model (25 points, 5 points / part).](03-2-contamination-model-25-points-5-points-part.md) · [Up: contents](index.md) · [4. Change point problem (25 points, 5 points / part). →](05-4-change-point-problem-25-points-5-points-part.md)
