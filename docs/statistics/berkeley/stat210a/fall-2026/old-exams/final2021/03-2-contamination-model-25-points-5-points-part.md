---
title: 2. Contamination model (25 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2021.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/final2021.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/final2021.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2021.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2. Contamination model (25 points, 5 points / part).

Suppose that we observe $n$ random variables $X_1, \dots, X_n \in [0, 1]$. The observations are supposed to come from a uniform distribution, but we suspect that our sample may be contaminated by a small proportion of observations from another, known distribution with Lebesgue density $q(x)$ ($q$ is not necessarily continuous). Assume that for some $C < \infty$, $0 \le q(x) \le C$ for all $x \in [0, 1]$. That is, we observe
$$X_1, \dots, X_n \overset{\text{i.i.d.}}{\sim} p_\theta(x) = 1 - \theta + \theta q(x).$$
Assume $\theta \in [0, b]$ for some $b < 1$.

(a) Show that the maximum likelihood estimator $\hat{\theta}_n$ is consistent for the true value $\theta_0$ as $n \to \infty$.

(b) Give the asymptotic distribution of the maximum likelihood estimator as $n \to \infty$, for $\theta_0 \in (0, b)$. Give an explicit expression for the asymptotic variance in terms of a definite integral (you don't need to check any regularity conditions for this part).

(c) Find a score test for the null hypothesis that there is no contamination, against the alternative that there is some, i.e. test $H_0 : \theta = 0$ vs. $H_1 : \theta > 0$. Give an explicit expression for your test statistic and your cutoff, in terms of a definite integral and a quantile of a known distribution.

(d) (*) If we expand the parameter space to $[0, 1)$, is the MLE still consistent?

(e) (*) If $\theta_0 = 0$, give the distribution of the MLE as $n \to \infty$.

---

Problem 2 answers continued (1):

---

Problem 2 answers continued (2):

---

Problem 2 answers continued (3):

---

---

[← 1. Regression with correlated errors (25 points, 5 points / part).](02-1-regression-with-correlated-errors-25-points-5-points-part.md) · [Up: contents](index.md) · [3. Two-by-two count table (25 points, 5 points / part). →](04-3-two-by-two-count-table-25-points-5-points-part.md)
