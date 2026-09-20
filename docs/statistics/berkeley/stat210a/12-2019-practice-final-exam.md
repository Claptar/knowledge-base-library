---
title: "12. 2019 Practice Final Exam"
course: "Berkeley Stat 210A Fall 2024"
chapter: 12
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 12. 2019 Practice Final Exam

## What this covers

This chapter is not a lecture but the department's own record of use for one: Berkeley's Stat 210A
final examination question booklet (filed as `final2019.pdf`; the booklet itself is headed "Fall
2020," an inconsistency in the archive rather than in the mathematics). It is reproduced here as a
practice exam rather than as exposition, since that is what the source is. The four problems range
across the semester's core topics in point estimation and testing — decision-theoretic risk and
minimax analysis, sufficiency and completeness in exponential families, and the asymptotic theory
of the MLE — so working them assumes all of that machinery is already available, not being taught
here. Two general rules apply throughout, as stated in the booklet: any result proved in lecture or
homework may be used without re-derivation, provided it is clearly identified, and results from an
earlier part of a multi-part problem may be assumed even if that part was not itself solved. Parts
marked with a star ($*$) are the ones the instructor flagged as the hardest; they carry no extra
points, so the advice given alongside them is to leave them until the rest of a problem is solid.

## The exam's four models

Each problem sets up its own model and states, in a preamble, whichever densities and moment
facts it needs. Those preambles are collected below, since they are the material the exercises
draw on; the exercises themselves are the actual questions asked, deliberately left unsolved.

### 1. A weighted-loss Poisson decision problem

A single observation $X \sim \text{Pois}(\theta)$, $\theta > 0$, is used to estimate $\theta$
under the loss
$$
L(d, \theta) = \frac{(d - \theta)^2}{\theta},
$$
rather than ordinary squared error — dividing by $\theta$ rescales the loss to compensate for the
fact that $\text{Pois}(\theta)$ becomes harder to pin down as $\theta$ grows (its variance is
$\theta$ itself). Unless stated otherwise, "risk" in this problem always means risk under $L$.

The preamble supplies three facts: the Poisson density $\theta^x e^{-\theta}/x!$ on
$x = 0, 1, \dots$, with mean and variance both $\theta$; the Gamma density, in the rate
parametrization $X \sim \text{Gamma}(k, \beta)$,
$$
\frac{\beta^k}{\Gamma(k)} x^{k-1} e^{-\beta x}, \qquad x > 0,
$$
with mean $k/\beta$ and variance $k/\beta^2$; and, for $X \sim \text{Gamma}(k,\beta)$ with $k > 1$,
the moment identity $\mathbb{E}[X^{-1}] = \beta/(k-1)$.

### 2. A Gaussian one-way random effects model

Data $X_{ij}$, $i = 1,\dots,m$, $j = 1,\dots,n$, follow the hierarchical model
$$
\alpha_i \overset{\text{i.i.d.}}{\sim} N(0,\tau^2), \qquad
X_{ij} \mid \alpha \overset{\text{ind.}}{\sim} N(\mu + \alpha_i, \sigma^2).
$$
The unknown parameters are $\mu \in \mathbb{R}$, $\tau^2 \ge 0$, and $\sigma^2 > 0$; the $\alpha_i$
are unobserved random effects, not parameters, and could in principle be integrated out of the
model. The exam fixes notation for the group means and the within- and between-group sums of
squares:
$$
\overline{X}_{i\cdot} = \frac{1}{n}\sum_j X_{ij}, \qquad
S_i^2 = \frac{1}{n-1}\sum_j (X_{ij} - \overline{X}_{i\cdot})^2, \qquad
\overline{X}_{\cdot\cdot} = \frac{1}{nm}\sum_{i,j} X_{ij},
$$
$$
S_B^2 = \frac{1}{m-1}\sum_i (\overline{X}_{i\cdot} - \overline{X}_{\cdot\cdot})^2 \quad
\text{(the $B$ is for "between groups").}
$$
The needed facts are the Gaussian density (with the convention that $\sigma^2 = 0$ means $X = 0$
almost surely) and the $\chi^2_k$ density
$$
\frac{1}{2^{k/2}\Gamma(k/2)} x^{k/2-1} e^{-x/2},
$$
with mean $k$ and variance $2k$. Except where a part says otherwise, the problem does not ask for
UMP(U)/UMA(U) optimality of any test or interval, and an explicit formula is allowed to be stated
in terms of quantiles of distributions covered in the course.

### 3. A capture–recapture model

An ecologist visits a wildlife preserve on two consecutive days looking for reindeer, tagging each
one she finds so that a reindeer seen on both days can be recognized. The population of $n$
reindeer is the same on both days, and each reindeer is seen on a given day with probability
$\pi \in (0,1)$, independently across reindeer and across days — so detections behave like $2n$
i.i.d. coin flips with success probability $\pi$. Here $n$ is the parameter of interest and $\pi$
is a nuisance parameter. Write $N_{11}$ for the number of reindeer seen on both days, $N_{10}$ for
the number seen only on day one, and $N_{01}$ for the number seen only on day two; $N_{00}$, the
number seen on neither day, is not observed. The only distributional fact supplied is the
multinomial density: for $X \sim \text{Multinom}(n,p)$ with $p \in [0,1]^d$, $\sum_i p_i = 1$,
$$
p_1^{x_1}\cdots p_d^{x_d}\,\frac{n!}{x_1!\cdots x_d!}, \qquad x \in \{0,\dots,n\}^d,\ \textstyle\sum_i x_i = n.
$$

### 4. A heteroscedastic nonlinear regression model

Fixed real numbers $x_1,\dots,x_n$ and observations $Y_i$ satisfy
$$
Y_i = g(\alpha + \beta x_i) + \varepsilon_i, \qquad \varepsilon_i \overset{\text{ind.}}{\sim} N(0,\sigma^2 h(x_i)),
$$
where $g: \mathbb{R}\to\mathbb{R}$ is known, strictly increasing, and infinitely differentiable,
and $h: \mathbb{R} \to (0,\infty)$ is known and continuous; $\alpha,\beta \in \mathbb{R}$ and
$\sigma^2 > 0$ are unknown and estimated jointly by maximum likelihood, giving
$(\hat\alpha,\hat\beta,\hat\sigma^2)$. The $i$th residual is
$r_i = Y_i - g(\hat\alpha + \hat\beta x_i)$. The Gaussian density needed here is the one already
given for Problem 2.

## Exercises

Each problem below is reproduced from the exam, with its own point value and the star convention
described above. None are solved here.

### 1. Poisson minimax estimation (24 points, 4 points per part)

Work in the model of §"A weighted-loss Poisson decision problem" above.

(a) Find the MLE of $\theta$ and calculate its risk function.

(b) Show that $\theta \sim \text{Gamma}(k,\beta)$ is a conjugate prior for this problem, and give
the posterior distribution.

(c) Find the Bayes estimator for the prior of part (b) under the loss $L$.

(d) $(*)$ Show that the Bayes risk of the Bayes estimator from part (c) is $1/(1+\beta)$.

(e) Show that the MLE is minimax relative to the loss $L$.

(f) Show that the minimax risk under ordinary squared error loss,
$L_{\text{SE}}(d,\theta) = (d-\theta)^2$, is infinite — this is the fact that motivates using the
rescaled loss $L$ instead.

### 2. ANOVA with random effects (25 points, 5 points per part)

Work in the model of §"A Gaussian one-way random effects model" above.

(a) Show that $S_B^2, S_1^2,\dots,S_m^2$ are mutually independent, and give their distributions.

(b) Find a finite-sample, equal-tailed confidence interval for $\mu$, with an explicit formula.

(c) Give a finite-sample test of $H_0: \tau^2 = 0$ against $H_1: \tau^2 > 0$, with an explicit test
statistic and critical value.

(d) $(*)$ Find a finite-sample, equal-tailed confidence interval for $\tau^2/\sigma^2$, with an
explicit formula.

(e) $(*)$ Show that the model, restricted to $\tau^2 > 0$, is a three-parameter exponential family,
and that $(\overline{X}_{\cdot\cdot},\, S_B^2,\, \sum_i S_i^2)$ is a complete sufficient statistic.

### 3. "And if you ever saw it..." (24 points, 6 points per part)

Work in the capture–recapture model above. You need not derive the reduction from individual
reindeer-day Bernoulli outcomes to $(N_{01}, N_{10}, N_{11})$ — since the undetected reindeer are
never observed, start directly from $N_{01}, N_{10}, N_{11}$ as the data and $(n,\pi)$ as the
parameters.

(a) Write the likelihood as a function of $N_{01}, N_{10}, N_{11}$, and show that
$T = (N_{01}+N_{10},\, N_{11})$ is sufficient for the model.

(b) $(*)$ Show that $T$ is minimal sufficient (you may take sufficiency, from part (a), as given).

(c) Consider the estimator
$$
\hat n = \frac{(N_{01}+N_{10}+2N_{11})^2}{4N_{11}}.
$$
Show that $\hat n$ is consistent in the sense that $\hat n / n \overset{p}{\to} 1$ as $n\to\infty$
with $\pi$ fixed.

(d) Find the asymptotic distribution of $\hat n$ from part (c) as $n \to \infty$ with $\pi$ fixed,
centering and scaling so that the limit is non-degenerate.

### 4. Nonlinear regression (24 points, 6 points per part)

Work in the model of §"A heteroscedastic nonlinear regression model" above.

(a) Show that the MLE for $\alpha$ and $\beta$ is found by setting weighted averages of the
residuals to zero,
$$
\sum_{i=1}^n w_i r_i = \sum_{i=1}^n w_i r_i x_i = 0,
$$
and give explicit expressions for the weights $w_i$ in terms of the data, $g$, $h$, and
$\hat\alpha,\hat\beta,\hat\sigma^2$.

(b) Give an explicit expression for the MLE $\hat\sigma^2$ in terms of the data, $g$, $h$, and
$\hat\alpha,\hat\beta$.

(c) $(*)$ For this part only, suppose $X_1,\dots,X_n$ are i.i.d. continuous random variables
instead of fixed numbers, bounded by $|X_i|\le B$ a.s. for some $B > 0$. Give the asymptotic
distribution of $(\hat\alpha,\hat\beta)$ in terms of $g$, $h$, and expectations of suitable random
variables, as $n\to\infty$ with the other parameters fixed. You may take consistency of
$(\hat\alpha,\hat\beta,\hat\sigma^2)$ and the regularity conditions behind the course's MLE
asymptotic-normality theorem as given, without needing to state what those conditions are. (Hint:
it may be easier to first assume $\sigma^2$ is known, then argue the answer is unchanged when it
is not.)

(d) $(*)$ Now return to fixed $x_i$, assume $h \equiv 1$, and let $g$ be completely unknown apart
from being strictly increasing and infinitely differentiable. Give a finite-sample test of
$H_0: \beta \le 0$ against $H_1: \beta > 0$, with a test statistic and a description of how to
compute the critical value, and show it controls the rejection probability throughout the
composite null (i.e., for every valid choice of $g$, $\alpha$, $\sigma^2$). Since $\alpha$ already
names the intercept, use $a$ for the significance level.

## Sources

All content in this chapter comes from one document: the Berkeley Stat 210A Fall 2019 final
examination question booklet (Prof. Will Fithian), filed in the library as `final2019.pdf` and
converted to markdown across five files —
`old-exams/final2019/01-introduction.md` through `05-4-nonlinear-regression-24-points-6-points-part.md`.
Identical copies of this conversion are filed under four course instances
(`fall-2024`, `fall-2025`, `fall-2025/units`, `fall-2026`); only one copy's text was used here,
since all four are the same exam. The conversion notice on each file records that the original PDF
has no text layer, that a model reconstructed the markdown from the scanned pages, that the prose
is a paraphrase in places, and that **every equation is unverified** — that caveat applies to every
formula reproduced above. No slides, transcript, or separate problem set were supplied for this
chapter; the exam supplies both its own setup and its own exercises, and no solutions are given in
the source or reproduced here.

---

[← 11. Fall 2018 Final Examination](11-fall-2018-final-examination.md) · [Contents](index.md) · [13. Final Exam Review Problems →](13-final-exam-review-problems.md)
