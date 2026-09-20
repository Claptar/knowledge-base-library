---
title: "92. Change of Variables and MLE"
course: "Berkeley Stat 153 Fall 2024"
chapter: 92
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 92. Change of Variables and MLE

## What this covers

Two self-contained calculations from an early lab in the course: evaluating an integral over
$(0,\infty)$ by a substitution that turns it into the Gamma function, and deriving the maximum
likelihood estimators of the mean and variance of an i.i.d. normal sample, together with a
rigorous argument that each is the *unique* maximizer. Assumes single-variable calculus
(integration by substitution, first- and second-derivative tests) and the definitions of the
Gamma function and the normal density.

## A change of variables that produces the Gamma function

Recall the Gamma function, defined for $\alpha>0$ by

$$\Gamma(\alpha)=\int_0^\infty u^{\alpha-1}e^{-u}\,du.$$

The exercise starts from a function on $(0,\infty)$ that does not look at all like this,

$$g_n(s)=s^{-n-1}\exp\Big(-\frac{1}{2s^2}\Big),\qquad n>0,$$

and asks for a closed form for

$$I=\int_0^\infty s^{-n-1}\exp\Big(-\frac{1}{2s^2}\Big)\,ds.$$

The hint is the substitution $u=\dfrac{1}{2s^2}$, which is the standard move whenever the exponent
contains $1/s^2$: it converts the decay $e^{-1/(2s^2)}$ into a plain $e^{-u}$.

Solving for $s$ gives $s=(2u)^{-1/2}$, so

$$ds=-(2u)^{-3/2}\,du.$$

Multiplying together the two pieces that involve $s$,

$$s^{-(n+1)}\,ds=\big((2u)^{-1/2}\big)^{-(n+1)}\big(-(2u)^{-3/2}\big)\,du=-(2u)^{\frac{n-2}{2}}\,du.$$

The substitution also reverses the limits of integration: as $s$ runs from $0$ to $\infty$,
$u=1/(2s^2)$ runs from $\infty$ down to $0$. Flipping the limits absorbs the minus sign:

$$I=\int_\infty^0 e^{-u}\Big(-(2u)^{\frac{n}{2}-1}\Big)\,du=\int_0^\infty e^{-u}(2u)^{\frac{n}{2}-1}\,du
=2^{\frac{n}{2}-1}\int_0^\infty u^{\frac{n}{2}-1}e^{-u}\,du.$$

The remaining integral is exactly the Gamma function evaluated at $\alpha=n/2$. Two ways to see
that, both present in the solution:

- **Directly**, it is the definition of $\Gamma$ with $\alpha = n/2$.
- **Via a recognizable density.** The $\mathrm{Gamma}(\alpha,\beta)$ density in the shape–rate
  parameterization is $f(u)=\dfrac{\beta^\alpha}{\Gamma(\alpha)}u^{\alpha-1}e^{-\beta u}$. The
  integrand $u^{n/2-1}e^{-u}$ is exactly this kernel with $\alpha=n/2,\ \beta=1$, stripped of its
  normalizing constant. Since a genuine probability density must integrate to $1$, the missing
  constant is forced to be $1/\Gamma(\alpha)$ — which is the same statement as
  $\int_0^\infty u^{\alpha-1}e^{-u}\,du=\Gamma(\alpha)$. This is a useful general trick: to
  evaluate an integral, recognize it as the *un-normalized kernel* of a known density and read off
  its normalizing constant, rather than integrating by hand.

Putting the pieces together,

$$\boxed{\int_0^\infty s^{-n-1}\exp\Big(-\frac{1}{2s^2}\Big)\,ds=2^{\frac{n}{2}-1}\Gamma\Big(\frac{n}{2}\Big).}$$

## Maximum likelihood for the normal distribution

The second exercise: given data $y_1,\dots,y_n$ modeled as
$y_i \overset{\text{i.i.d.}}\sim \mathcal N(\mu,\sigma^2)$ with both $\mu\in\mathbb R$ and $\sigma>0$
unknown, find the MLEs $\hat\mu,\hat\sigma$ — and show they are the *unique interior* maximizers of
the likelihood, not merely critical points of it.

### Likelihood and log-likelihood

$$L(\mu,\sigma)=\prod_{i=1}^n\frac{1}{\sqrt{2\pi}\,\sigma}\exp\Big\{-\frac{(y_i-\mu)^2}{2\sigma^2}\Big\}
=(2\pi\sigma^2)^{-n/2}\exp\Big\{-\frac{1}{2\sigma^2}\sum_{i=1}^n(y_i-\mu)^2\Big\},$$

so

$$\ell(\mu,\sigma)=-\frac n2\log(2\pi)-n\log\sigma-\frac{1}{2\sigma^2}\sum_{i=1}^n(y_i-\mu)^2.$$

### Step 1: maximize over $\mu$, holding $\sigma$ fixed

$$\frac{\partial\ell}{\partial\mu}=\frac1{\sigma^2}\sum_{i=1}^n(y_i-\mu)=\frac n{\sigma^2}(\bar y-\mu),
\qquad \frac{\partial^2\ell}{\partial\mu^2}=-\frac n{\sigma^2}<0.$$

The first derivative vanishes at $\hat\mu=\bar y$, and the second derivative is negative for every
$\sigma$, so $\ell(\mu,\sigma)$ is strictly concave in $\mu$ for each fixed $\sigma$: $\hat\mu=\bar y$
is the unique maximizer over $\mu$. Equivalently, maximizing $\ell$ over $\mu$ is the same as
minimizing $\sum_i(y_i-\mu)^2$, a strictly convex quadratic whose unique minimizer is the sample
mean — the same computation as least squares with a single constant regressor.

### Step 2: maximize over $\sigma$, at $\mu=\bar y$

This is a **profile likelihood** argument: having solved for the optimal $\mu$ as a function of
$\sigma$ (here it does not even depend on $\sigma$), substitute it back in and maximize what
remains over the one parameter left. Let $S=\sum_{i=1}^n(y_i-\bar y)^2$; the profile log-likelihood
is

$$\ell(\bar y,\sigma)=-\frac n2\log(2\pi)-n\log\sigma-\frac{S}{2\sigma^2},\qquad \sigma>0.$$

Differentiating,

$$\frac{d}{d\sigma}\ell(\bar y,\sigma)=-\frac n\sigma+\frac S{\sigma^3}=\frac{S-n\sigma^2}{\sigma^3}.$$

Setting this to zero gives $\hat\sigma^2=S/n$, i.e. $\hat\sigma=\sqrt{S/n}$.

### Step 3: this critical point really is the unique maximum

A vanishing derivative only produces a *candidate*; the exercise explicitly asks for an argument
that it is the unique maximizer on $\sigma>0$. Two checks close the gap:

- **Boundary behavior.** As $\sigma\to0^+$, the term $-S/(2\sigma^2)\to-\infty$ dominates
  $-n\log\sigma\to+\infty$, so $\ell(\bar y,\sigma)\to-\infty$; as $\sigma\to\infty$,
  $-n\log\sigma\to-\infty$ as well, so again $\ell(\bar y,\sigma)\to-\infty$. The profile
  log-likelihood is $-\infty$ at both ends of $(0,\infty)$.
- **Sign of the derivative.** From $\dfrac{d\ell}{d\sigma}=\dfrac{S-n\sigma^2}{\sigma^3}$, the
  denominator $\sigma^3$ is always positive, and the numerator $S-n\sigma^2$ is positive for
  $\sigma<\sqrt{S/n}$ and negative for $\sigma>\sqrt{S/n}$. So $\ell(\bar y,\cdot)$ strictly
  increases on $(0,\hat\sigma)$ and strictly decreases on $(\hat\sigma,\infty)$.

A function that tends to $-\infty$ at both ends of an interval, rises the whole way to a single
critical point, and falls the whole way afterward, attains its maximum only at that point. Hence
$\hat\sigma$ is the unique interior maximizer.

### Conclusion

$$\boxed{\hat\mu=\bar y,\qquad \hat\sigma^2=\frac1n\sum_{i=1}^n(y_i-\bar y)^2,
\qquad \hat\sigma=\sqrt{\frac1n\sum_{i=1}^n(y_i-\bar y)^2}.}$$

These jointly form the unique interior maximizer of $\ell(\mu,\sigma)$ over $\mu\in\mathbb R,\
\sigma>0$.

## Sources

Both worked examples come from the lab 1 solutions for Berkeley STAT 153, Fall 2025
(`lab1_Shana_solution.pdf`, dated September 8, 2025):

- **Change of variables / Gamma function** — Exercise 1 of the solution set, reproduced in
  `01-exercise-1---change-of-variables.md`.
- **Normal MLE** — Exercise 2 of the solution set, reproduced in `02-exercise-2---mle.md`.

No slides or transcript were supplied for this item, and the lab handout itself (the statement of
the exercises as originally posed) was not among the inputs, only the worked solutions — so both
problems are presented above as worked examples rather than restated and left unsolved. The source
markdown carries its own caveat, worth repeating here: the original PDF has no extractable text
layer, so the conversion was done by a model reading page images, and every equation in it is
flagged as unverified. The derivations above were checked internally for consistency (each step
follows from the one before it) but have not been checked against the original PDF pages.

---

[← 91. LSTM Forecasting for Time Series](91-lstm-forecasting-for-time-series.md) · [Contents](index.md) · [93. Anatomy of a Regression Fit (part 2) →](93-anatomy-of-a-regression-fit-part-2.md)
