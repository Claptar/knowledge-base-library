---
title: "117. Bayesian Priors and Least Squares"
course: "Berkeley Stat 153"
chapter: 117
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 117. Bayesian Priors and Least Squares

## What this covers

This chapter builds the Bayesian derivation of linear regression from the ground up. It answers a
narrow question: if you refuse to assume anything specific about the parameters of a model and let
the data speak through the likelihood alone, what shape does your resulting belief about those
parameters take? The route is deliberately indirect — it starts from two-number toy problems with
no regression in sight, and only at the end arrives at the regression posterior. It assumes Bayes'
rule for continuous densities, the normal density, and basic calculus (integration by substitution,
the change-of-variables formula for densities), but nothing about regression itself.

## Setting up the machine

Two tools get reused in every example below.

**Bayes' rule for densities.** If $X$ is the unknown and $Y$ is the data, then as a function of $x$
(with $y$ fixed at its observed value),
$$f_{X\mid Y}(x\mid y) \propto f_{Y\mid X}(y\mid x)\, f_X(x),$$
i.e. posterior $\propto$ likelihood $\times$ prior, and the missing normalising constant is whatever
makes the right-hand side integrate to 1.

**Marginalising out a nuisance parameter.** Several of the models below contain a parameter — a
noise scale $\sigma$ — that is needed to write down the model but is not itself the object of
interest. The fix is always the same: write down the *joint* posterior of the interesting parameter
and $\sigma$ together, then integrate $\sigma$ out to get the posterior of the interesting parameter
alone.

Throughout, a "vague" or "flat" prior means $\mathrm{Unif}(-C, C)$ for a location parameter, with
$C$ enormous — a way of saying "no opinion" before seeing the data, while still having a genuine
density to feed into Bayes' rule.

## A question with too little information

Suppose $a$ and $b$ are two numbers and all that is known is $a + b = 7$. What can be said about
$a$? Nothing: for every choice of $a$, setting $b = 7 - a$ satisfies the constraint, so there are
infinitely many possible pairs $(a, b)$. One equation cannot pin down two unknowns, and no amount of
cleverness fixes that — the problem needs another assumption before it has an answer.

## Turning "small" into a distribution

Suppose instead it is known that $b$ is *small in magnitude*. That is a real piece of information,
but only a probabilistic model can turn it into a computation. Assume $a$ and $b$ are independent
with
$$a \sim \mathrm{Unif}(-C, C) \qquad \text{and} \qquad b \sim N(0, \sigma^2),$$
where $C$ is very large (a vague prior — no opinion about the size of $a$) and $\sigma$ is a fixed
number that calibrates what "small" means for $b$.

The quantity of interest is the conditional distribution of $a$ given $a + b = 7$. Write $y = a + b$,
so the target is the density of $a \mid y = 7$. Because $b \sim N(0, \sigma^2)$ independently of $a$,
the conditional distribution of $y$ given $a$ is $N(a, \sigma^2)$. By Bayes' rule,
$$
f_{a \mid y = 7}(a) \propto f_{y\mid a}(7)\, f_a(a)
= \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(7-a)^2}{2\sigma^2}\right) \times \frac{I\{-C<a<C\}}{2C}
\propto \exp\!\left(-\frac{(7-a)^2}{2\sigma^2}\right) I\{-C<a<C\}.
$$
This is a normal density centred at 7 with variance $\sigma^2$, truncated to $(-C, C)$. Since $C$ is
huge, the truncation has essentially no effect, and
$$a \mid a+b = 7 \ \approx\ N(7, \sigma^2).$$
So under the assumption that $b$ is small, the data $a+b=7$ turns into a genuine distribution for
$a$: centred at 7, with $\sigma^2$ controlling how much residual uncertainty is left — the smaller
$\sigma$, the more confidently $a$ is pinned near 7.

## A second observation, and an unknown noise scale

Now suppose there are three unknowns $a, b_1, b_2$, both $b_1$ and $b_2$ are small, and
$$a + b_1 = 7 \qquad \text{and} \qquad a + b_2 = 10.$$
Three unknowns and two equations is again logically unanswerable without assumptions — the same
obstruction as the first question. The natural model is
$$a \sim \mathrm{Unif}(-C, C), \qquad b_1, b_2 \mid \sigma \overset{\mathrm{iid}}{\sim} N(0, \sigma^2),
\qquad \log\sigma \sim \mathrm{Unif}(-C, C).$$
Three choices are packed into this: no opinion about $a$; a common but unknown scale $\sigma$ for
the two small noise terms; and, since the *order of magnitude* of $\sigma$ is unknown, a flat prior
not on $\sigma$ itself but on $\log \sigma$ — the one range over which "no opinion" makes sense,
because $\log\sigma$ can be any real number while $\sigma$ must be positive. By the change-of-
variables formula this induces
$$f_\sigma(\sigma) = f_{\log\sigma}(\log\sigma)\left|\frac{d}{d\sigma}\log\sigma\right|
= \frac{I\{-C<\log\sigma<C\}}{2C\,\sigma},$$
i.e. $f_\sigma(\sigma) \propto 1/\sigma$ on a huge range of positive values.

The target is $a \mid y_1 = 7, y_2 = 10$, where $y_1 = a+b_1$ and $y_2 = a+b_2$. Since $\sigma$ is a
nuisance parameter here, first find the *joint* posterior of $(a, \sigma)$, using
$y_1, y_2 \mid a, \sigma \sim N(a, \sigma^2)$ independently:
$$
f_{a,\sigma \mid y_1,y_2}(a,\sigma) \propto \left\{\prod_{j=1}^2 \frac{1}{\sqrt{2\pi}\,\sigma}
\exp\!\left(-\frac{(y_j-a)^2}{2\sigma^2}\right)\right\} \frac{I\{-C<a<C\}}{2C}\cdot\frac{I\{-C<\log\sigma<C\}}{2C\sigma}
\propto \sigma^{-3} \exp\!\left(-\frac{S(a)}{2\sigma^2}\right),
$$
dropping the two indicators (both are 1 for all reasonable $a$ and $\sigma>0$ once $C$ is large), and
writing $S(a) = (y_1-a)^2 + (y_2-a)^2$ for the **sum of squares**. The likelihood contributes
$\sigma^{-2}$ from the two normal factors and the prior on $\sigma$ contributes one more factor of
$1/\sigma$, for $\sigma^{-3}$ overall.

Now integrate out $\sigma$:
$$f_{a\mid y_1,y_2}(a) \propto \int_0^\infty \sigma^{-3}\exp\!\left(-\frac{S(a)}{2\sigma^2}\right)d\sigma.$$
Substitute $\sigma = t\sqrt{S(a)}$, so $d\sigma = \sqrt{S(a)}\,dt$:
$$
\int_0^\infty \sigma^{-3}\exp\!\left(-\frac{S(a)}{2\sigma^2}\right)d\sigma
= \frac{1}{S(a)}\int_0^\infty t^{-3}\exp\!\left(-\frac{1}{2t^2}\right)dt \ \propto\ \frac{1}{S(a)},
$$
because the remaining integral is a constant that does not depend on $a$. So
$$f_{a\mid y_1,y_2}(a) \propto \frac{1}{(y_1-a)^2 + (y_2-a)^2}.$$
Completing the square,
$$(y_1-a)^2+(y_2-a)^2 = 2\left(a - \frac{y_1+y_2}{2}\right)^2 + 2\left(\frac{|y_1-y_2|}{2}\right)^2,$$
so
$$f_{a\mid y_1,y_2}(a) \propto \frac{1}{\left(a - \frac{y_1+y_2}{2}\right)^2 + \left(\frac{|y_1-y_2|}{2}\right)^2}.$$
This is exactly the shape of a **Cauchy density** with location $\mu$ and scale $\tau$,
$$\mathrm{Cauchy}(\mu,\tau):\quad \frac{1}{\pi\tau}\cdot\frac{1}{1+\left(\frac{x-\mu}{\tau}\right)^2}
\propto \frac{1}{\tau^2 + (x-\mu)^2},$$
matched by $\mu = (y_1+y_2)/2$ and $\tau = |y_1-y_2|/2$. So
$$a \mid y_1, y_2 \ \sim\ \mathrm{Cauchy}\!\left(\frac{y_1+y_2}{2}, \frac{|y_1-y_2|}{2}\right),$$
and for $y_1=7,\ y_2=10$ this is $\mathrm{Cauchy}(8.5, 1.5)$. The appearance of a Cauchy distribution
here is a direct consequence of the modelling assumptions above — in particular, of treating the
noise scale $\sigma$ as unknown and integrating it out — not something imposed by hand.

## Generalising to $n$ measurements of one quantity

A scientist makes $n=6$ measurements of an unknown physical quantity $\theta$:
$$y_1=26.6,\ \ y_2=38.5,\ \ y_3=34.4,\ \ y_4=34.0,\ \ y_5=31.0,\ \ y_6=23.6.$$
Write each as signal plus noise, $y_i = \theta + \epsilon_i$ for $i=1,\dots,n$: this is exactly the
previous setup with $n=6$ instead of $n=2$, and $\theta, \epsilon_i$ in place of $a, b_i$. Assume
$$\theta \sim \mathrm{Unif}(-C,C), \qquad \epsilon_1,\dots,\epsilon_n \mid \sigma
\overset{\mathrm{iid}}{\sim} N(0,\sigma^2), \qquad \log\sigma \sim \mathrm{Unif}(-C,C).$$
Exactly the same argument — joint posterior of $(\theta,\sigma)$, then marginalise $\sigma$ — but now
with $n$ likelihood factors instead of 2 gives
$$f_{\theta,\sigma\mid y_1,\dots,y_n}(\theta,\sigma) \propto \sigma^{-n-1}
\exp\!\left(-\frac{S(\theta)}{2\sigma^2}\right), \qquad S(\theta) = \sum_{i=1}^n (y_i-\theta)^2.$$
The same substitution $\sigma = t\sqrt{S(\theta)}$ turns the $\sigma$-integral into
$$
\int_0^\infty \sigma^{-n-1}\exp\!\left(-\frac{S(\theta)}{2\sigma^2}\right)d\sigma
= S(\theta)^{-n/2}\int_0^\infty t^{-n-1}\exp\!\left(-\frac{1}{2t^2}\right)dt \ \propto\ S(\theta)^{-n/2},
$$
since the leftover power of $S(\theta)$ from the substitution is $S(\theta)^{-(n+1)/2 + 1/2} =
S(\theta)^{-n/2}$, and the remaining $t$-integral is again a constant. So
$$f_{\theta \mid y_1,\dots,y_n}(\theta) \ \propto\ \left(\frac{1}{S(\theta)}\right)^{n/2}.$$
(Setting $n=2$ recovers exactly the sum-of-squares kernel found for the Cauchy case above.) This is
stated to be a $t$-density with $n-1$ degrees of freedom, though that identification is deferred to
a later lecture and is not derived here. What can already be read off is the *location* of this
density: $S(\theta)$ is minimised at the sample mean
$$\bar y = \frac{y_1 + \cdots + y_n}{n},$$
and since $1/S(\theta)$ is largest exactly where $S(\theta)$ is smallest, the posterior density of
$\theta$ given the data is maximised at the sample mean.

## Adding a covariate: linear regression

Now let $y_1, \dots, y_n$ be a time series, and decompose it as
$$y_i = \beta_0 + \beta_1 x_i + \epsilon_i,$$
where $x_i$ is *known*. The simplest case is $x_i = i$ — regression with time itself as the
covariate. (The same analysis also applies when $x_i = y_{i-1}$, lagged regression, but that is
taken up in a later lecture.) There are now $n+2$ unknowns — $\beta_0, \beta_1$, and
$\epsilon_1,\dots,\epsilon_n$ — and the goal is to recover $\beta_0,\beta_1$ from the $n$ observed
$y_i$. The assumptions are the direct extension of the previous section, with *two* location
parameters sharing one noise scale:
$$\beta_0 \sim \mathrm{Unif}(-C,C), \qquad \beta_1 \sim \mathrm{Unif}(-C,C), \qquad
\epsilon_1,\dots,\epsilon_n \mid \sigma \overset{\mathrm{iid}}{\sim} N(0,\sigma^2), \qquad
\log\sigma \sim \mathrm{Unif}(-C,C).$$
The joint posterior of $(\beta_0,\beta_1,\sigma)$ given the data works out, by exactly the same
Bayes' rule computation as before, to
$$f_{\beta_0,\beta_1,\sigma \mid y_1,\dots,y_n}(\beta_0,\beta_1,\sigma) \propto \sigma^{-n-1}
\exp\!\left(-\frac{S(\beta_0,\beta_1)}{2\sigma^2}\right), \qquad
S(\beta_0,\beta_1) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2,$$
the sum of squared residuals from the line $\beta_0+\beta_1 x_i$. Nothing about the $\sigma$-integral
changes when there are two location parameters sharing $\sigma$ instead of one — the substitution
$\sigma = t\sqrt{S}$ goes through exactly as before, treating $S(\beta_0,\beta_1)$ as a single number
for fixed $\beta_0,\beta_1$ — so integrating $\sigma$ out gives
$$f_{\beta_0,\beta_1 \mid y_1,\dots,y_n}(\beta_0,\beta_1) \ \propto\ \left(\frac{1}{S(\beta_0,\beta_1)}\right)^{n/2}.$$
This is stated to be a multivariate $t$-distribution with $n-2$ degrees of freedom, centred at the
least-squares estimators $(\hat\beta_0, \hat\beta_1)$ that minimise $S(\beta_0,\beta_1)$ — again, the
derivation of that fact is left for a later lecture. What matters immediately is the shape of the
argument: the entire chain — toy problem, unknown-scale toy problem, $n$ measurements, regression —
is the same computation with the location parameter changed from a single number to a pair, because
the $\sigma$-marginalisation step never looks at how many location parameters there are.

## Why the posterior concentrates at the least-squares fit

The proportionality $f(\beta_0,\beta_1\mid\text{data}) \propto S(\beta_0,\beta_1)^{-n/2}$ is
awkward to work with directly: in a real dataset $S(\beta_0,\beta_1)$ can be astronomically large
(sums of squared residuals in the billions, say), so $S(\beta_0,\beta_1)^{-n/2}$ is a minute number
everywhere, with the normalising constant correspondingly huge. Dividing through by the same power
of $S(\hat\beta_0,\hat\beta_1)$ — the minimum value — changes nothing, since that quantity does not
depend on $(\beta_0,\beta_1)$ and is exactly the missing constant factor:
$$f_{\beta_0,\beta_1\mid\text{data}}(\beta_0,\beta_1) \ \propto\
\left(\frac{S(\hat\beta_0,\hat\beta_1)}{S(\beta_0,\beta_1)}\right)^{n/2}.$$
Written this way, the ratio equals 1 exactly at the least-squares estimate and shrinks below 1
everywhere else — and the exponent $n/2$ is what makes the posterior *concentrate* there once $n$ is
large: any $(\beta_0,\beta_1)$ with $S(\beta_0,\beta_1)$ even a little larger than
$S(\hat\beta_0,\hat\beta_1)$ gets a ratio below 1 raised to a large power, which collapses toward 0.

A worked size for this: with $n=791$ observations, a point $(\beta_0,\beta_1)$ whose sum of squares
is 10% worse than the optimum, $S(\beta_0,\beta_1) = 1.1\, S(\hat\beta_0,\hat\beta_1)$, gets
$$\left(\frac{1}{1.1}\right)^{395.5} \approx 4.26\times 10^{-17},$$
essentially zero posterior weight. Even a point only 1% worse than optimal, $S(\beta_0,\beta_1) =
1.01\, S(\hat\beta_0,\hat\beta_1)$, gets
$$\left(\frac{1}{1.01}\right)^{395.5} \approx 0.02,$$
still small. So for large $n$ the posterior mass sits in an extremely narrow neighbourhood of the
least-squares fit, and — retroactively — this is why the vague-prior indicator
$I\{-C<\beta_0,\beta_1<C\}$ could be dropped along the way without changing anything: whatever
enormous range $C$ was chosen to allow, the data has already concentrated the answer into a region
minuscule by comparison. The chain that began with an admission of total ignorance about $a$ in
"$a+b=7$" ends, once enough data accumulates, in a posterior that is for practical purposes a point
mass at the least-squares estimator.

## Sources

- Fall 2026 lecture notes (converted from LaTeX, high fidelity), *Simple Question 2* — the intro
  motivating Bayesian over frequentist regression, and Simple Questions 1–2 (the underdetermined
  $a+b=7$ problem and its resolution with $b$ small and $\sigma$ known):
  `docs/statistics/berkeley/stat153/fall-2026/LectureThree153248Fall2026/01-simple-question-2.md`.
- Same lecture, *Simple Question 3* — the two-equation, unknown-$\sigma$ problem, the log-uniform
  prior on $\sigma$, and the marginalisation to a Cauchy posterior:
  `docs/statistics/berkeley/stat153/fall-2026/LectureThree153248Fall2026/02-simple-question-3.md`.
- Same lecture, *Question 4: Several Measurements of One Quantity* — the $n$-measurement
  generalisation, the numeric dataset, and the sample-mean-as-mode observation:
  `docs/statistics/berkeley/stat153/fall-2026/LectureThree153248Fall2026/03-question-4-several-measurements-of-one-quantity.md`.
- Same lecture, *Linear Regression with Time as a Covariate* — the regression setup and posterior:
  `docs/statistics/berkeley/stat153/fall-2026/LectureThree153248Fall2026/04-linear-regression-with-time-as-a-covariate.md`.
  This page's source has a rendering gap in the prior/indicator terms of the joint posterior
  display; the missing indicator factors ($I\{-C<\beta_0<C\}$, $I\{-C<\beta_1<C\}$,
  $I\{e^{-C}<\sigma<e^C\}$) were reconstructed here by the identical pattern used two sections
  earlier in the same lecture for Simple Question 3 and Question 4.
- Spring 2025 slides (model-reconstructed from a PDF with no text layer; fidelity marked
  "reconstructed", every equation there unverified against the original) —
  `docs/statistics/berkeley/stat153/spring-2025/LectureThree153248Spring2025.md`. Used only for the
  rewriting of the posterior around the least-squares estimator and the numerical concentration
  example ($n=791$, the "US population dataset" mentioned there); the arithmetic in that example
  was checked independently and is consistent. The regression posterior derivation itself is not
  duplicated from this source, since the Fall 2026 notes give the clearer version of the same
  computation.
- Referred to but not contained in the supplied material: the frequentist treatment of linear
  regression, promised for "the next lecture" in the Fall 2026 notes; the derivation that the
  $\theta$-posterior is a $t$-density with $n-1$ degrees of freedom and that the
  $(\beta_0,\beta_1)$-posterior is a multivariate $t$-distribution with $n-2$ degrees of freedom,
  both stated but deferred; and lagged regression ($x_i = y_{i-1}$), mentioned as a later topic.

---

[← 116. Sinusoidal Models for Sunspots](116-sinusoidal-models-for-sunspots.md) · [Contents](index.md) · [118. Bayesian View of Ridge Regression →](118-bayesian-view-of-ridge-regression.md)
