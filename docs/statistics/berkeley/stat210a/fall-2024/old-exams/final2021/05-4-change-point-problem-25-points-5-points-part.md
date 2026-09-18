---
title: 4. Change point problem (25 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/final2021.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/final2021.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/final2021.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/final2021.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4. Change point problem (25 points, 5 points / part).

Some useful facts for this problem:
- The Beta distribution $\text{Beta}(\alpha, \beta)$ with parameters $\alpha, \beta > 0$ has density
$$\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)}, \quad \text{where } B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}$$
with respect to the Lebesgue measure on $(0, 1)$. Its mean and variance are
$$\mathbb{E}_{\alpha,\beta}[X] = \frac{\alpha}{\alpha + \beta}, \quad \text{Var}_{\alpha,\beta}(X) = \frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}.$$
- The negative binomial distribution $\text{NB}(m, \theta)$ with parameters $m \in \{1, 2, \dots\}, \theta \in (0, 1)$ has probability mass function
$$p_{m,\theta}(x) = \binom{x + m - 1}{x} \theta^x (1 - \theta)^m, \quad \text{for } x \in \{0, 1, 2, \dots\}.$$
Its mean and variance are
$$\mathbb{E}_{m,\theta}[X] = \frac{m\theta}{1 - \theta}, \quad \text{Var}_{m,\theta}(X) = \frac{m\theta}{(1 - \theta)^2}.$$

Assume we observe independent random variables $X_i \sim \text{NB}(m, \theta_i)$ for $i = 1, \dots, n$. Assume also that the $\theta_i$ values are constant except at some integer $k \in \{1, \dots, n - 1\}$ where they change. That is,
$$\theta_i = \begin{cases} \gamma_0 & \text{if } i \le k \\ \gamma_1 & \text{if } i > k \end{cases},$$
for $\gamma_0, \gamma_1 \in (0, 1)$.
Until otherwise specified, assume $k$ is known. Throughout the problem, we will assume $m$ is known.

(a) Calculate the maximum likelihood estimator for $\gamma_0$ and find its asymptotic distribution if $k, n \to \infty$. You do not need to check regularity conditions.

(b) Next assume we introduce a prior distribution that $\gamma_0, \gamma_1 \overset{\text{i.i.d.}}{\sim} \text{Beta}(\alpha, \beta)$. Give the posterior distribution for $(\gamma_0, \gamma_1)$ given $X_1, \dots, X_n$, and give the Bayes estimator for squared error loss.

(c) (*) Find the asymptotic distribution of the Bayes estimator for $\gamma_0$, holding $\gamma_0$ and $\gamma_1$ fixed and sending $k, n \to \infty$.

(d) Next, we relax the assumption that $k$ is known. Instead assume $n = 10$ and all we know is that $k \in \{4, 5, 6\}$. Find a minimal sufficient statistic for the three-parameter model with $\gamma_0, \gamma_1 \in (0, 1)$ and $k \in \{4, 5, 6\}$. You do not need to prove it is minimal, as long as you give the right answer.

(e) Continuing with the three-parameter model above, consider a Bayesian approach where we assign priors $k \sim \text{Unif}(\{4, 5, 6\})$ independently of $\gamma_0, \gamma_1 \overset{\text{i.i.d.}}{\sim} \text{Beta}(\alpha, \beta)$. Give a Gibbs sampler algorithm to sample from the posterior distribution of $(k, \gamma_0, \gamma_1)$.

---

Problem 4 answers continued (1):

---

Problem 4 answers continued (2):

---

Problem 4 answers continued (3):

---

[← 3. Two-by-two count table (25 points, 5 points / part).](04-3-two-by-two-count-table-25-points-5-points-part.md) · [Up: contents](index.md)
