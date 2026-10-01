---
title: "13. Final Exam Review Problems"
course: "Berkeley Stat 210A"
chapter: 13
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 13. Final Exam Review Problems

## What this covers

This is the question booklet for the Fall 2021 final examination in STAT210A (Prof. Will Fithian) — four
independent problems drawing on material from across the semester: exponential families and sufficiency,
maximum likelihood estimation and its large-sample behavior, uniformly most powerful (and unbiased) testing,
and Bayesian point estimation together with Gibbs sampling. The exam supplies its own toolkit of facts for
each problem, and this chapter is organized the same way: each section below sets up one scenario and states
the facts the exam hands you for working it, and the lettered parts themselves are collected at the end as
exercises. It assumes the reader has already met sufficiency and completeness, the exponential family, the
Neyman–Pearson and UMP/UMPU testing framework, asymptotic normality of the MLE, and Bayesian conjugate priors
— the exam's own instructions say exactly this: any result "from lecture or homework" may be used and cited
without re-derivation.

## Exam conventions

A few rules from the booklet are worth keeping in mind while reading the problems, because they tell you how
much machinery you are meant to bring to each part:

- Any result from lecture or homework can be used and cited without re-deriving it, and you do not need to
  check regularity conditions for theorems from class that required them.
- Within a multi-part problem, you may treat the result of an earlier part as given even if you did not prove
  it, and use it to solve a later part.
- Parts marked with a star (*) are flagged as the hardest in each problem. They are not worth extra points —
  the star is there so you know where to spend time only after the unstarred parts are solid.

## Problem 1: regression with correlated errors

For $i=1,\dots,n$ we observe fixed covariates $x_i\in\mathbb R^d$ and a random response
$$Y_i = x_i'\beta+\varepsilon_i,$$
for a coefficient vector $\beta\in\mathbb R^d$. Stacking observations, with $X$ the $n\times d$ design matrix
with $i$th row $x_i'$ and $\Sigma\in\mathbb R^{n\times n}$ positive definite,
$$Y = X\beta+\varepsilon,\qquad \varepsilon\sim N_n(0,\Sigma).$$
Assume $n\ge d\ge1$ and $X$ has full column rank. The problem supplies two standard multivariate-normal facts:

- the density of $Z\sim N_n(\mu,\Sigma)$ is $p_{\mu,\Sigma}(z)=|2\pi\Sigma|^{-1/2}\exp\{-\tfrac12(z-\mu)'\Sigma^{-1}(z-\mu)\}$
  (the exponent on the determinant is $-\tfrac12$, not $-n/2$);
- affine images of Gaussians are Gaussian: if $Z\sim N_n(\mu,\Sigma)$ and $A\in\mathbb R^{k\times n}$,
  $b\in\mathbb R^k$ are fixed, then $AZ+b\sim N_k(A\mu+b, A\Sigma A')$.

Parts (a)–(b) treat $\Sigma$ as known and ask you to recognize the distribution of $Y$ as an exponential
family in $\beta$ and to find the MLE. Parts (c)–(e) drop that assumption: $\Sigma$ is now unknown, so it has
to be estimated from $m$ i.i.d. replicate response vectors sharing the same $X$ and $\beta$,
$$Y^{(k)}=X\beta+\varepsilon^{(k)},\qquad \varepsilon^{(k)}\overset{\text{i.i.d.}}\sim N_n(0,\Sigma),\quad k=1,\dots,m.$$
From these replicates, form the sample mean and the sample covariance
$$\overline Y=\frac1m\sum_{k=1}^m Y^{(k)},\qquad
\widehat\Sigma=\frac1{m-1}\sum_{k=1}^m(Y^{(k)}-\overline Y)(Y^{(k)}-\overline Y)'.$$
This is the multivariate, matrix-valued analogue of the familiar fact that a Gaussian sample's mean and sample
variance are independent — the independence, unbiasedness, and (in)efficiency of $\widehat\Sigma$ are exactly
what parts (c)–(e) ask about. Part (e) specializes to $n=d$, where $X$ is square and invertible, and asks
whether $\widehat\Sigma$ is UMVU in that case.

## Problem 2: contamination model

$X_1,\dots,X_n\in[0,1]$ are i.i.d. from
$$p_\theta(x) = 1-\theta+\theta q(x),$$
a mixture of the $\mathrm{Unif}(0,1)$ density and a known, bounded contaminating density $q$ (a Lebesgue
density, not necessarily continuous, with $0\le q(x)\le C<\infty$), with mixing weight $\theta\in[0,b]$ for
some $b<1$. The question throughout is how well the contamination fraction $\theta$ can be detected and
estimated.

Parts (a)–(c) are the standard sequence for a regular parametric model: consistency of the MLE $\hat\theta_n$,
its asymptotic normal distribution (with the asymptotic variance an explicit integral against $q$ — a Fisher
information computation), and a score test of $H_0:\theta=0$ against $H_1:\theta>0$. What makes the two
starred parts, (d) and (e), genuinely harder is that $\theta=0$ sits at the *boundary* of the parameter space
$[0,b]$: the usual argument for asymptotic normality of the MLE assumes the true parameter is an interior
point, and that assumption fails exactly at the null value being tested in part (c). Part (d) asks whether
consistency survives once the parameter space is enlarged to $[0,1)$, and part (e) asks for the limiting
distribution of the MLE precisely at the boundary point $\theta_0=0$.

## Problem 3: two-by-two count table

Independent counts $X_{ij}\sim\mathrm{Pois}(\lambda_{ij})$ for $i,j\in\{0,1\}$ follow
$$\lambda_{ij} = \lambda_0\rho^{\,i+j},$$
so $\lambda_{00}=\lambda_0$, $\lambda_{01}=\lambda_{10}=\lambda_0\rho$, $\lambda_{11}=\lambda_0\rho^2$. Read
this as a $2\times2$ table with a baseline rate $\lambda_0$ and a single multiplicative "interaction"
parameter $\rho$: $\rho=1$ means the two factors act additively on the log scale, and departures from $\rho=1$
are what the hypothesis tests in (b)–(c) are built to detect. Three facts are supplied:

- the Poisson pmf and its mean/variance;
- the multinomial pmf $p_{n,\pi}(x)=n!\prod_{i=1}^d \pi_i^{x_i}/x_i!$ on $\{0,\dots,n\}^d$ with $\sum_i x_i=n$;
- if $X_i\sim\mathrm{Pois}(\theta_i)$ independently for $i=1,\dots,d$, with $X_+=\sum_i X_i$ and
  $\theta_+=\sum_i\theta_i$, then conditionally on $X_+=n$, $(X_1,\dots,X_d)\sim\mathrm{Multinom}(n,\theta/\theta_+)$.

That last fact is the key tool for (b) and (c): conditioning on the total count removes the nuisance
parameter $\lambda_0$ (which enters only through $\theta_+$), leaving a multinomial model in which $\rho$
alone determines the cell probabilities. That is the standard route to a UMP test of a one-sided hypothesis on
$\rho$ when $\lambda_0$ is known (part (b)), and to a UMPU test when it is not (part (c)) — conditioning on a
complete sufficient statistic for the nuisance parameter to reduce to a one-parameter exponential family. Part
(d) asks for the MLEs of $\lambda_0,\rho$ on a specific small data set, and part (e) asks whether the same
conditioning idea still yields a UMPU test once the model is relaxed to an arbitrary $\lambda_{ij}=f(i+j)$.

## Problem 4: change-point problem

Independent observations $X_i\sim\mathrm{NB}(m,\theta_i)$ for $i=1,\dots,n$, with $m$ known throughout, have a
single unknown change point $k\in\{1,\dots,n-1\}$ after which the success probability shifts:
$$\theta_i = \begin{cases}\gamma_0 & i\le k\\ \gamma_1 & i>k\end{cases},\qquad \gamma_0,\gamma_1\in(0,1).$$

<figure>
<svg viewBox="0 0 320 150" role="img" aria-label="Index axis split at the change point k into a gamma-zero segment and a gamma-one segment">
  <line x1="30" y1="70" x2="290" y2="70" stroke="currentColor" stroke-width="1.5"/>
  <rect x="30" y="55" width="140" height="30" fill="currentColor" fill-opacity="0.15"/>
  <rect x="170" y="55" width="120" height="30" fill="currentColor" fill-opacity="0.07"/>
  <line x1="170" y1="48" x2="170" y2="92" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="100" y="45" text-anchor="middle" font-size="12" fill="currentColor">θᵢ = γ₀</text>
  <text x="230" y="45" text-anchor="middle" font-size="12" fill="currentColor">θᵢ = γ₁</text>
  <text x="30" y="103" text-anchor="middle" font-size="12" fill="currentColor">i = 1</text>
  <text x="170" y="103" text-anchor="middle" font-size="12" fill="currentColor">i = k</text>
  <text x="290" y="103" text-anchor="middle" font-size="12" fill="currentColor">i = n</text>
  <line x1="140" y1="122" x2="200" y2="122" stroke="currentColor" stroke-width="1.5"/>
  <line x1="140" y1="117" x2="140" y2="122" stroke="currentColor" stroke-width="1.5"/>
  <line x1="200" y1="117" x2="200" y2="122" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="138" text-anchor="middle" font-size="12" fill="currentColor">k ∈ {4, 5, 6} in parts (d)-(e)</text>
</svg>
<figcaption>Observations up to the unknown change point k have negative-binomial success probability γ₀, those
after have γ₁; later parts of the problem treat k itself as unknown, restricted to {4, 5, 6}.</figcaption>
</figure>

The supplied facts are the $\mathrm{Beta}(\alpha,\beta)$ density and moments, and the $\mathrm{NB}(m,\theta)$
pmf $p_{m,\theta}(x)=\binom{x+m-1}{x}\theta^x(1-\theta)^m$ and moments. As a function of $\theta$, the NB pmf
is proportional to $\theta^x(1-\theta)^m$ — exactly the kernel of a Beta density — so a
$\mathrm{Beta}(\alpha,\beta)$ prior on $\theta$ is conjugate to the negative-binomial likelihood, which is what
makes the posterior in part (b) tractable in closed form.

The problem builds up in stages: (a)–(c) fix $k$ and ask about the MLE of $\gamma_0$, the Bayes estimator
under the Beta prior, and the asymptotics of both as $k,n\to\infty$. Parts (d)–(e) then take $k$ itself to be
unknown — restricted to a small set $\{4,5,6\}$ with $n=10$ — turning the model into a three-parameter model
$(\gamma_0,\gamma_1,k)$, for which (d) asks for a minimal sufficient statistic and (e) asks for a Gibbs sampler
targeting the joint posterior of $(k,\gamma_0,\gamma_1)$ under independent priors
$k\sim\mathrm{Unif}\{4,5,6\}$ and $\gamma_0,\gamma_1\overset{\text{i.i.d.}}\sim\mathrm{Beta}(\alpha,\beta)$.

## Exercises

### 1. Regression with correlated errors (25 points, 5 points / part)

(a) Show that $Y$ follows a full-rank exponential family model and identify its complete sufficient statistic.

(b) Find the maximum likelihood estimator of $\beta$ and give its distribution.

(c) Show that $\overline Y$ and $\widehat\Sigma$ are independent of each other.

(d) Show that $\widehat\Sigma$ is an unbiased estimator of $\Sigma$.

(e) Now assume $n=d$. Is $\widehat\Sigma$ UMVU? Why or why not?

### 2. Contamination model (25 points, 5 points / part)

(a) Show that the maximum likelihood estimator $\hat\theta_n$ is consistent for the true value $\theta_0$ as
$n\to\infty$.

(b) Give the asymptotic distribution of the maximum likelihood estimator as $n\to\infty$, for
$\theta_0\in(0,b)$, with an explicit expression for the asymptotic variance as a definite integral. (No need
to check regularity conditions.)

(c) Find a score test of $H_0:\theta=0$ against $H_1:\theta>0$. Give an explicit test statistic and cutoff, in
terms of a definite integral and a quantile of a known distribution.

(d) (*) If the parameter space is enlarged to $[0,1)$, is the MLE still consistent?

(e) (*) If $\theta_0=0$, give the limiting distribution of the MLE as $n\to\infty$.

### 3. Two-by-two count table (25 points, 5 points / part)

(a) Give a complete sufficient statistic for the model and show it is complete.

(b) Suppose, for this part only, that $\lambda_0$ is known but $\rho$ is unknown. Propose a UMP test of
$H_0:\rho=\rho_0$ against $H_1:\rho>\rho_0$: give an explicit test statistic, explain how to find the cutoff,
and explain why the test is UMP. (An explicit cutoff is not required.)

(c) Now suppose both parameters are unknown. Propose a UMPU test of $H_0:\rho=1$ against $H_1:\rho>1$,
explaining how the cutoff would be calculated. For the data $X_{00}=X_{01}=0$, $X_{10}=X_{11}=1$, compute the
conservative (non-randomized) p-value.

(d) For the same data, find the maximum likelihood estimators of $\lambda_0$ and $\rho$ as explicit numbers.

(e) (*) Suppose the model is relaxed to $\lambda_{ij}=f(i+j)$ for an arbitrary strictly positive function $f$
on $\{0,1,2\}$ (this includes $\lambda_0\rho^{i+j}$ as a special case). Does a UMPU test exist for the null
hypothesis that the original model is correctly specified, against the alternative that only the relaxed model
holds? Justify your answer. (If the answer is yes, it suffices to establish that such a test exists, without
fully constructing it.)

### 4. Change-point problem (25 points, 5 points / part)

(a) With $k$ known, find the MLE of $\gamma_0$ and its asymptotic distribution as $k,n\to\infty$. (No need to
check regularity conditions.)

(b) Now put independent priors $\gamma_0,\gamma_1\overset{\text{i.i.d.}}\sim\mathrm{Beta}(\alpha,\beta)$. Give
the posterior distribution of $(\gamma_0,\gamma_1)$ given $X_1,\dots,X_n$, and the Bayes estimator under
squared-error loss.

(c) (*) Holding $\gamma_0,\gamma_1$ fixed and sending $k,n\to\infty$, find the asymptotic distribution of the
Bayes estimator of $\gamma_0$.

(d) Now suppose $k$ is unknown, $n=10$, and all that is known is $k\in\{4,5,6\}$. Find a minimal sufficient
statistic for the three-parameter model with $\gamma_0,\gamma_1\in(0,1)$ and $k\in\{4,5,6\}$. (No need to
prove minimality, provided the answer is correct.)

(e) Continuing with the three-parameter model, put a prior $k\sim\mathrm{Unif}\{4,5,6\}$ independent of
$\gamma_0,\gamma_1\overset{\text{i.i.d.}}\sim\mathrm{Beta}(\alpha,\beta)$. Describe a Gibbs sampler that
samples from the posterior distribution of $(k,\gamma_0,\gamma_1)$.

## Sources

All content is from the reconstructed question booklet for the Fall 2021 STAT210A final exam (Prof. Will
Fithian), converted by a model from a PDF with no text layer — the source itself flags that "every equation is
unverified," so the display equations here should be checked against the original PDF rather than cited
directly:

- `01-final-examination-question-booklet.md` — cover page and exam-wide instructions.
- `02-1-regression-with-correlated-errors-25-points-5-points-part.md` — Problem 1 and its supplied facts.
- `03-2-contamination-model-25-points-5-points-part.md` — Problem 2.
- `04-3-two-by-two-count-table-25-points-5-points-part.md` — Problem 3 and its supplied facts.
- `05-4-change-point-problem-25-points-5-points-part.md` — Problem 4 and its supplied facts.

Identical copies of this booklet exist under the `fall-2024`, `fall-2025`, `fall-2025/units`, and `fall-2026`
trees of the library's `statistics/berkeley/stat210a` course (only the source metadata differs); the
`fall-2024` copy was used as the text above. No slide deck, transcript, or answer key was supplied: the
booklet's own "Problem N answers continued" pages are blank, and no worked solutions appear anywhere in the
input.

---

[← 12. 2019 Practice Final Exam](12-2019-practice-final-exam.md) · [Contents](index.md) · [14. Fall 2024 Final Examination →](14-fall-2024-final-examination.md)
