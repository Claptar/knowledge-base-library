---
title: "11. Fall 2018 Final Examination"
course: "Berkeley Stat 210A"
chapter: 11
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 11. Fall 2018 Final Examination

## What this covers

This chapter is the Fall 2018 final examination for Stat 210A (Theoretical Statistics), written
by Prof. William Fithian. It is not a lecture but a comprehensive problem set covering the
semester's four main strands: sufficiency and completeness in a curved exponential family, the
construction and UMVU/UMPU analysis of a multivariate exponential family, Bayesian and minimax
decision theory under a non-quadratic loss, and finite-sample and nonparametric hypothesis testing
in a location family. It assumes everything the course built up to this point: sufficiency,
completeness and the Lehmann–Scheffé route to UMVU estimators; exponential families and their
natural parameters; Fisher information and the asymptotic behavior of the MLE; optimal testing
(score tests, UMP and UMP-unbiased tests); and Bayes and minimax risk. No solutions are given here,
in keeping with the exam's own instructions.

## About the exam

The exam is organized as four problems worth 15–20 points each, each opening with a short list of
"useful facts" — standard densities and identities the student is expected to already know or is
handed for convenience. The exam's own ground rules, worth keeping in mind when working the
problems below, were:

- Results proved in lecture or on homework may be used without re-derivation, provided it is clear
  which result is being invoked; regularity conditions for named theorems need not be checked
  explicitly.
- Within a multi-part problem, the result of an earlier part may be assumed even if it was not
  itself proved.
- Parts marked with a star (*) are the ones expected to be hardest; they carry no extra points, so
  they are not necessarily worth more time than the unstarred parts.

## Exercises

### 1. A curved Gaussian family (20 points, 4 points per part)

*Useful fact:* the density of $Z \sim N(\mu, \sigma^2)$ is
$$\frac{1}{\sqrt{2\pi\sigma^2}} \exp\left\{ -\frac{(x - \mu)^2}{2\sigma^2} \right\}.$$

Suppose
$$X_1, \ldots, X_n = \begin{pmatrix} X_{1,1} \\ X_{1,2} \end{pmatrix}, \ldots, \begin{pmatrix} X_{n,1} \\ X_{n,2} \end{pmatrix} \stackrel{\text{i.i.d.}}{\sim} N_2(\mu(\theta), I_2),$$
for $\theta \in \mathbb{R}$, where $\mu(\theta) = \begin{pmatrix} \theta \\ \theta^2 \end{pmatrix}$ —
so the mean vector traces out a curve (a parabola) in $\mathbb{R}^2$ rather than the full plane.

(a) Show that $T(X) = \sum_i X_i \in \mathbb{R}^2$ is a minimal sufficient statistic but is *not*
complete sufficient.

(b) Find the Fisher information $J_n(\theta)$ — the information about $\theta$ carried by the
complete sample.

(c) Consider the score test of $H_0: \theta \le \theta_0$ against $H_1: \theta > \theta_0$. Give an
explicit expression for the test statistic and its rejection threshold, and show that the test
achieves finite-sample control of the Type I error rate.

(d) Find the asymptotic distribution of $\hat\mu_2 = \hat\theta^2$, the MLE of the expectation of
$X_{i,2}$, when $\theta \ne 0$. Compare its asymptotic relative efficiency to the "obvious"
estimator $\frac{1}{n}\sum_{i=1}^n X_{i,2}$.

(e) (\*) If $\theta = 0$, find the asymptotic distribution of $\hat\theta^2$, appropriately centered
and scaled (heuristic arguments are acceptable).

### 2. Species abundance (20 points, 5 points per part)

*Useful facts:*

- $X \sim \mathrm{Pois}(\lambda)$ has probability mass function $\dfrac{\lambda^x e^{-\lambda}}{x!}$
  on $x = 0, 1, 2, \ldots$, with mean and variance both $\lambda$.
- $(X_1, \ldots, X_d) \sim \mathrm{Multinom}(n, \pi)$ has probability mass function
  $\dfrac{n!}{\prod_i x_i!}\prod_i \pi_i^{x_i}$.
- If $X_i \stackrel{\text{ind.}}{\sim} \mathrm{Pois}(\lambda_i)$ for $i = 1, \ldots, d$, and
  $X_+ = \sum_i X_i$, $\lambda_+ = \sum_i \lambda_i$, then conditional on $X_+ = x_+$,
  $$(X_1, \ldots, X_d) \sim \mathrm{Multinomial}\big(x_+, (\lambda_1, \ldots, \lambda_d)/\lambda_+\big).$$

Consider an ecological sampling problem: we visit $m$ sites and, for each of $s$ species, count the
number of individuals present. Let $N_j^{(i)}$ be the count of species $j$ at site $i$, so the data
form a table

| | Species $1$ | $\cdots$ | Species $s$ |
| :---: | :---: | :---: | :---: |
| Site $1$ | $N_1^{(1)}$ | $\cdots$ | $N_s^{(1)}$ |
| $\vdots$ | $\vdots$ | $N_j^{(i)}$ | $\vdots$ |
| Site $m$ | $N_1^{(m)}$ | $\cdots$ | $N_s^{(m)}$ |

Assume throughout that the rows $N^{(1)}, \ldots, N^{(m)}$ are i.i.d. vectors in $\mathbb{R}^s$
(the coordinates *within* a row need not be i.i.d.).

(a) First suppose $N_j^{(i)} \stackrel{\text{ind.}}{\sim} \mathrm{Pois}(\lambda_j)$ across species,
independent within a site, i.e.
$$N^{(i)} \stackrel{\text{i.i.d.}}{\sim} p_\lambda(n) = \prod_{j=1}^s \frac{\lambda_j^{n_j} e^{-\lambda_j}}{n_j!}.$$
Find a complete sufficient statistic for the whole data table, and give a UMVU estimator for
$\lambda_j$ — the average abundance of species $j$ — explaining why it is UMVU.

(b) Now suppose we have, from outside data, a fixed and known dissimilarity measure
$d(j,k) \in [0,\infty)$ for each pair of species $1 \le j < k \le s$ (for instance, how long ago the
two species diverged). We conjecture that latent habitat characteristics at a site make similar
species more or less common together, and test this by enriching the model to
$$N^{(i)} \stackrel{\text{i.i.d.}}{\sim} p_{\lambda,\beta}(n) \propto \prod_{j=1}^s \frac{\lambda_j^{n_j} e^{-\lambda_j}}{n_j!} \times \prod_{1 \le j < k \le s} \exp\{\beta\, e^{-d(j,k)}\, n_j n_k\}.$$
Show that this is an exponential family with $s+1$ sufficient statistics, and identify the natural
parameter corresponding to each (there is more than one valid way to write these). You need not
find the normalizing constant.

(c) Find a UMP-unbiased test of $H_0: \beta = 0$ (independence across species) against
$H_1: \beta > 0$ (positive correlation between similar species), and explain how to find its
critical value.

(d) (\*) Now make the test more robust by dropping the Poisson assumption: under $H_0$ the species
counts are still independent but with unknown distributions (still supported on the non-negative
integers),
$$N^{(i)} \stackrel{\text{i.i.d.}}{\sim} \prod_{j=1}^s F_j(n_j) \quad (\text{under } H_0),$$
while under the alternative similar species remain more correlated. Modify the test from part (b)
so that it controls the Type I error rate in finite samples, in this nonparametric model.

### 3. Inverse gamma prior (20 points, 4 points per part)

*Useful facts:*

- The density of $Z \sim N(\mu,\sigma^2)$ is as in Problem 1.
- A $\chi^2_d$ random variable has mean $d$ and variance $2d$.
- If $Y \sim \mathrm{Gamma}(\alpha,\beta)$ (rate parametrization) then $Y$ has density
  $\dfrac{\beta^\alpha}{\Gamma(\alpha)} y^{\alpha-1} e^{-\beta y}$ on $(0,\infty)$, with mean
  $\alpha/\beta$ and variance $\alpha/\beta^2$ (defined for $\alpha,\beta>0$).
- The inverse-gamma distribution $IG(\alpha,\beta)$ is the law of $W = 1/Y$ for
  $Y \sim \mathrm{Gamma}(\alpha,\beta)$; $W$ has density
  $\dfrac{\beta^\alpha}{\Gamma(\alpha)} w^{-\alpha-1} e^{-\beta/w}$ on $(0,\infty)$, with $\beta$ a
  scale parameter, mean $\dfrac{\beta}{\alpha-1}$ (for $\alpha>1$) and variance
  $\dfrac{\beta^2}{(\alpha-1)^2(\alpha-2)}$ (for $\alpha>2$).
- The squared relative error loss is
  $$L_{\mathrm{rel}}(d,\theta) = \left(\frac{d-\theta}{\theta}\right)^2 = \left(\frac{d}{\theta}-1\right)^2,$$
  with risk $R_{\mathrm{rel}}(\delta(\cdot),\theta) = \mathbb{E}_\theta[L_{\mathrm{rel}}(\delta(X),\theta)]$.

Consider the Bayesian model
$$\theta \sim IG(\alpha,\beta), \qquad X_1,\ldots,X_n \mid \theta \stackrel{\text{i.i.d.}}{\sim} N(0,\theta),$$
where the variance is $\theta$ itself (not $\theta^2$); assume $n \ge 2$.

(a) Find the posterior distribution of $\theta$ given $X = (X_1,\ldots,X_n)$, and the Bayes
estimator for $\theta$ under squared error loss.

(b) Give the mean squared error of the estimator from (a), as a function of $\theta$ (it need not be
simplified fully).

(c) Find the Bayes estimator for $\theta$ under the squared relative error loss $L_{\mathrm{rel}}$.

(d) (\*) For the estimator in (c), find the risk function $R_{\mathrm{rel}}(\delta(\cdot),\theta)$ as
a function of $\theta$, and show that the Bayes risk equals $\dfrac{2}{n+2(\alpha+1)}$.

(e) For the relative squared error risk, find a linear estimator of the form
$\delta(X) = a\sum_{i=1}^n X_i^2$ that is minimax, and prove that it is minimax.

### 4. Inference in the Laplace family (15 points, 5 points per part)

*Useful facts:*

- The Laplace location family with location $\theta$ has density $p_\theta(x) = f(x-\theta)$, where
  $f(x) = \frac{1}{2}e^{-|x|}$.
- $\mathrm{sign}(x) = -1$ for $x<0$, $0$ for $x=0$, $1$ for $x>0$.

Assume $X_1,\ldots,X_n \stackrel{\text{i.i.d.}}{\sim} \mathrm{Laplace}(\theta)$.

(a) Find the score test of $H_0: \theta = 0$ against $H_1: \theta > 0$. Give the test statistic and
its threshold in terms of a quantile of a binomial distribution (assume $\alpha$ is chosen so this
quantile is exact, so the test need not be randomized; note $\mathbb{P}_\theta(X=0)=0$ for all
$\theta$, so ties need not be worried about).

(b) Suppose instead we only believe the data come from a symmetric location family — that is,
$p_\theta(x) = f(x-\theta)$ for some unknown density $f$ that is symmetric about the origin (so the
family is parametrized by $(\theta,f)$). Show that the test from (a) remains a valid, finite-sample
test of $H_0: \theta = 0$ against $H_1: \theta > 0$ in this larger, nonparametric family.

(c) Now consider testing $H_0: \theta \le 0$ against $H_1: \theta > 0$ (so the null now includes
negative $\theta$). Show that the test from (a) is a valid and unbiased level-$\alpha$ test for the
nonparametric family of part (b).

## Sources

- Both supplied notes are the same document: the Fall 2018 final examination for Berkeley Stat
  210A, Prof. William Fithian, as mirrored in the `old-exams/` folder of two later course
  offerings —
  [`fall-2024/old-exams/final2018.md`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/final2018.pdf)
  and
  [`fall-2026/old-exams/final2018.md`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2018.pdf).
  Both are machine reconstructions of a PDF with no text layer; the source markdown flags every
  equation as unverified, so the statements above should be checked against the original PDF before
  being treated as exact.
- No slides, transcript, or separate problem set were supplied for this chapter — the exam booklet
  is the entire source, and its "answer continued" pages were blank in the original, so no solutions
  are recorded anywhere in the source material.
- The exam's own reference facts (Gaussian, Poisson, multinomial, gamma/inverse-gamma densities,
  the Poisson-conditional-on-sum-is-multinomial identity, and the relative-error loss definition)
  are reproduced above exactly as printed on the exam, since the exam supplies them for use without
  proof.

---

[← 10. The Factorization Theorem](10-the-factorization-theorem.md) · [Contents](index.md) · [12. 2019 Practice Final Exam →](12-2019-practice-final-exam.md)
