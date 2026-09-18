---
title: 4. Nonlinear regression (24 points, 6 points / part).
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2019.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/final2019.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/final2019.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2019.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4. Nonlinear regression (24 points, 6 points / part).

Note the Gaussian density is printed in the preamble of Problem 2.
We are given a sample of $n$ pairs $(x_i, Y_i)$ where $x_1, \dots, x_n \in \mathbb{R}$ are fixed real numbers and
$$
Y_i = g(\alpha + \beta x_i) + \varepsilon_i, \quad \text{where } \varepsilon_i \overset{\text{ind.}}{\sim} N(0, \sigma^2 h(x_i)).
$$
Assume (except where otherwise specified) that:
• $g : \mathbb{R} \to \mathbb{R}$ is a known function which is strictly increasing and infinitely differentiable.
• $h : \mathbb{R} \to (0, \infty)$ is a known continuous function.
• $\alpha, \beta \in \mathbb{R}$ and $\sigma^2 > 0$ are unknown

Finally, let $r_i = Y_i - g(\hat{\alpha} + \hat{\beta} x_i)$ denote the $i$th residual. Throughout the problem, assume we are estimating the parameter vector $(\alpha, \beta, \sigma^2)$ jointly by maximum likelihood; let $(\hat{\alpha}, \hat{\beta}, \hat{\sigma}^2)$ denote the joint MLE.

(a) Show that the MLE for $\alpha$ and $\beta$ is found by setting weighted averages of the residuals to 0:
$$
\sum_{i=1}^n w_i r_i = \sum_{i=1}^n w_i r_i x_i = 0,
$$
and give explicit expressions for the weights $w_i$ in terms of the data, the functions $g$ and $h$, and the maximum likelihood estimators $\hat{\alpha}, \hat{\beta}, \hat{\sigma}^2$.

(b) Give an explicit expression for the MLE for $\sigma^2$, i.e. $\hat{\sigma}^2$, in terms of the data, the functions $g$ and $h$, and the maximum likelihood estimators $\hat{\alpha}, \hat{\beta}$.

(c) (*) Now assume (for this part **ONLY**) that instead of fixed numbers we observe i.i.d. random variables $X_1, \dots, X_n$, which are continuous and bounded random variables ($|X_i| \le B$ almost surely, for some $B > 0$.)
Give the asymptotic distribution of the maximum likelihood estimators $(\hat{\alpha}, \hat{\beta})$ in terms of the functions $g$ and $h$, and expectations of suitable random variables. The limit is taken as $n \to \infty$ with the other parameters fixed.

You may assume without proof that $(\hat{\alpha}, \hat{\beta}, \hat{\sigma}^2)$ are consistent for the true population values, and that all of the regularity conditions from class

---

for our theorem on the asymptotic distribution of the MLE hold (the log-likelihood and its derivatives are well-behaved in the required sense). You do not need to write down what the conditions are, either.

(Hint: it might be easier to do the problem assuming $\sigma^2$ is known, and then explain why the answer doesn't change when $\sigma^2$ is unknown.)

(d) (*) We now go back to assuming the $x_i$ values are fixed. Now assume $h(z) \equiv 1$ but $g$ is completely unknown (apart from the restrictions described in the preamble: strictly increasing and infinitely differentiable).
Give a finite-sample test of $H_0 : \beta \le 0$ vs $H_1 : \beta > 0$. You should provide a test statistic and describe how to calculate the critical value.
For full credit you must show your test controls the rejection probability throughout the composite null hypothesis (that is, for all valid choices of $g$, $\alpha$, and $\sigma^2$.)

Since we are already using the letter $\alpha$ for the intercept, I suggest using $a$ to denote the significance level in your answer.

---

Problem 4 answers continued (1):

---

Problem 4 answers continued (2):

---

Problem 4 answers continued (3):

---

[← 3. "And if you ever saw it..." (24 points, 6 points / part).](04-3-and-if-you-ever-saw-it-24-points-6-points-part.md) · [Up: contents](index.md)
