---
title: 1. Six Gaussians (20 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2024.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/final2024.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/final2024.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2024.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1. Six Gaussians (20 points, 5 points / part).

Some useful facts for this problem:
• Recall that the Gaussian density function for $Z \sim N(\theta, \sigma^2)$ is
$$
\frac{1}{\sqrt{2\pi\sigma^2}} \exp\left\{ -\frac{(x - \theta)^2}{2\sigma^2} \right\}
$$

Assume that we observe Gaussian random variables $X_1, \ldots, X_6$ where $X_i \sim N(\theta_i, \sigma^2)$, independently. Different parts of the question will assume $\sigma^2 > 0$ is known or unknown.

(a) Assume it is known that $\sigma^2 = 1$. Suppose we want to test the null hypothesis:
$$
H_0 : \theta_2 = \theta_3 \text{ and } \theta_4 = \theta_5 = \theta_6,
$$
against the alternative that $\theta$ is any other vector in $\mathbb{R}^6$. Suggest a $\chi^2$ test statistic and specify the degrees of freedom.

(b) Continue to assume $\sigma^2 = 1$ and consider the following estimator for $\theta$:
$$
\delta(X) = \gamma \cdot \left( X_1, \overline{X}_{23}, \overline{X}_{23}, \overline{X}_{456}, \overline{X}_{456}, \overline{X}_{456} \right),
$$
where $\gamma \in [0, 1]$ is a fixed constant, $\overline{X}_{23} = \frac{X_2+X_3}{2}$, and $\overline{X}_{456} = \frac{X_4+X_5+X_6}{3}$. Give an unbiased estimator for the MSE of $\delta(X)$.

(c) Now, assume that $\sigma^2$ is unknown, but it is known that $\theta_2 = \theta_3$ and $\theta_4 = \theta_5 = \theta_6$. That is, what in part (a) was a null hypothesis to be tested is now a modeling assumption. Suggest a confidence interval based on the Student's $t$-distribution for the parameter $g(\theta) = \theta_4 - \theta_3$. Specify the degrees of freedom.

(d) Under the same assumptions as part (b), now suppose that we want to test the null hypothesis $H_0 : \theta_1 = \theta_2 = \dots = \theta_6$ against the alternative that $\theta$ is any other vector in $\mathbb{R}^6$ with $\theta_2 = \theta_3$ and $\theta_4 = \theta_5 = \theta_6$. Suggest an $F$ test statistic and specify the degrees of freedom.

---

Problem 1 answers continued (1):

---

Problem 1 answers continued (2):

---

Problem 1 answers continued (3):

---

---

[← Final Examination: QUESTION BOOKLET](01-final-examination-question-booklet.md) · [Up: contents](index.md) · [2. Inverse gamma prior (20 points, 5 points / part). Some useful facts for this problem →](03-2-inverse-gamma-prior-20-points-5-points-part-some-useful-fa.md)
