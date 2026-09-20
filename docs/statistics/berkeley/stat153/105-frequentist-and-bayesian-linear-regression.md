---
title: "105. Frequentist and Bayesian Linear Regression"
course: "Berkeley Stat 153 Fall 2024"
chapter: 105
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 105. Frequentist and Bayesian Linear Regression

## What this covers

How do you fit a line — or a curve, or an autoregression — to data and say how uncertain the fit
is? This chapter answers that for the multiple linear regression model, from both of the two
standard viewpoints: the frequentist one (least squares and maximum likelihood, giving a point
estimate) and the Bayesian one (a prior on the coefficients and the noise scale, giving a full
posterior distribution). The two meet at the same point estimate, and the chapter's main result is
that the Bayesian posterior can be written down exactly: it is a multivariate $t$-distribution
centred at the least-squares estimate. It assumes simple linear regression and least squares,
matrix algebra (gradients of quadratic forms, matrix inverses), the multivariate normal density,
and the basic Bayesian recipe posterior $\propto$ likelihood $\times$ prior.

## The multiple linear regression model

With one response $y$ and $m$ covariates $x_1,\dots,x_m$, observed on $n$ subjects as
$(y_i,x_{i1},\dots,x_{im})$ for $i=1,\dots,n$, the multiple linear regression model with normal
errors is
$$
y_i = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_m x_{im} + \epsilon_i, \qquad
\epsilon_i \stackrel{\text{i.i.d.}}{\sim} N(0,\sigma^2).
$$
Simple linear regression is the case $m=1$. Two ways this model arises in a time series context:

1. **Regression on functions of time.** To fit a quadratic trend, take $x_{i1}=i$, $x_{i2}=i^2$. To
   fit a simple sinusoid, take $x_{i1}=\cos(2\pi i/12)$, $x_{i2}=\sin(2\pi i/12)$.
2. **Autoregression (AR).** Taking $x_{ij}=y_{i-j}$ gives
   $$
   y_t = \beta_0 + \beta_1 y_{t-1} + \cdots + \beta_m y_{t-m} + \epsilon_t,
   $$
   i.e. using the $m$ most recent values of the series to predict the next one. AR models are used
   constantly in practice and tend to work well.

Writing down the likelihood above treats $x_1,\dots,x_n$ as fixed, known numbers. That is exactly
true when $x_i=i$ (a deterministic function of time) but not strictly true in the AR case, where
$x_i=y_{i-1}$ is itself random. The lecture flags this and promises that it is "still approximately
true" for AR — the argument for that is not in the material covered here. Likewise, everything
below assumes $n$ is much larger than $m$; the regime where $n$ is comparable to or smaller than
$m$ is called high-dimensional linear regression and is a separate topic.

## Two ways to do inference

Given data $(y,X)$, the goal is estimates of $\beta_0,\dots,\beta_m$ together with some measure of
uncertainty about them. There are two standard ways to get there.

**Frequentist.** (1) Construct an estimator — least squares, or more generally maximum likelihood,
which requires writing down a likelihood. (2) Work out, exactly or approximately, the sampling
distribution of the estimator, and use its quantiles for interval estimates. Those quantiles
typically involve other unknown parameters, which then have to be estimated too.

**Bayesian.** Put a prior on all the unknown parameters, and report the posterior distribution
given the data. No separate "point estimate then interval" step is needed — the whole answer is the
posterior, and any point estimate or interval is read off from it afterwards.

## Least squares in matrix form

Collect the data into
$$
y = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}, \qquad
X = \begin{pmatrix} 1 & x_{11} & \cdots & x_{1m} \\ \vdots & \vdots & & \vdots \\ 1 & x_{n1} & \cdots & x_{nm} \end{pmatrix}, \qquad
\beta = \begin{pmatrix} \beta_0 \\ \vdots \\ \beta_m \end{pmatrix},
$$
with $X$ an $n\times(m+1)$ matrix carrying a leading column of ones. This is the notation code uses
too — `sm.OLS(y, X).fit()` in `statsmodels` takes exactly this $y$ and $X$. The sum of squares
becomes
$$
S(\beta) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_{i1} - \cdots - \beta_m x_{im})^2 = \|y - X\beta\|^2.
$$

**The least squares estimator.** The minimiser $\hat\beta$ of $S(\beta)$ is
$$
\hat\beta = (X^TX)^{-1}X^Ty.
$$
This follows by setting the gradient of $S$ to zero:
$$
\nabla S(\beta) = \nabla\big[(y-X\beta)^T(y-X\beta)\big]
= \nabla\big[y^Ty - \beta^TX^Ty - y^TX\beta + \beta^TX^TX\beta\big] = 2X^Ty - 2X^TX\beta.
$$
At $\beta=\hat\beta$ this must vanish, so $X^T(y-X\hat\beta)=0$, i.e. $X^TX\hat\beta = X^Ty$ — the
normal equations — which rearrange to $\hat\beta=(X^TX)^{-1}X^Ty$.

## Maximum likelihood coincides with least squares

Under the normal-error assumption, $y_i$ are independent with $y_i \sim N(\beta_0+\beta_1x_{i1}+\cdots+\beta_mx_{im},\ \sigma^2)$, so the likelihood is
$$
f(y_1,\dots,y_n \mid \beta,\sigma) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\,\sigma}
\exp\!\left(-\frac{(y_i-\beta_0-\cdots-\beta_mx_{im})^2}{2\sigma^2}\right)
= (2\pi)^{-n/2}\sigma^{-n}\exp\!\left(-\frac{S(\beta)}{2\sigma^2}\right).
$$
Equivalently, in vector form, $y \sim N_n(X\beta,\ \sigma^2 I_n)$. The likelihood depends on $\beta$
only through $-S(\beta)/(2\sigma^2)$, and for any fixed $\sigma$ this is maximised exactly where
$S(\beta)$ is minimised. So the maximum likelihood estimate of $\beta$ is the same as the
least-squares estimate $\hat\beta$ — the normal-errors assumption doesn't change the point estimate
for the coefficients, only adds a likelihood that also identifies $\sigma$. (The lecture material
available here states that maximum likelihood also gives an estimate of $\sigma$, but breaks off
before carrying that derivation out.)

## The Pythagorean identity

One more algebraic fact about $S$ does the work of turning the Bayesian posterior, later, into a
recognisable distribution:
$$
S(\beta) = S(\hat\beta) + (\beta-\hat\beta)^TX^TX(\beta-\hat\beta).
$$
To see this, write $y - X\beta = (y-X\hat\beta) + (X\hat\beta - X\beta)$, so
$$
S(\beta) = \|y-X\beta\|^2 = \|y-X\hat\beta\|^2 + \|X\hat\beta-X\beta\|^2 + 2\langle y-X\hat\beta,\ X\hat\beta-X\beta\rangle.
$$
The cross term vanishes:
$$
\langle y-X\hat\beta,\ X\hat\beta-X\beta\rangle = (\hat\beta-\beta)^TX^T(y-X\hat\beta)
= (\hat\beta-\beta)^T(X^Ty - X^TX\hat\beta) = 0,
$$
using the normal equations $X^TX\hat\beta=X^Ty$ from the previous section. What's left is exactly
the claimed identity, since $\|X\hat\beta-X\beta\|^2 = (\beta-\hat\beta)^TX^TX(\beta-\hat\beta)$.

## The Bayesian model: prior and posterior

For the Bayesian route, put
$$
\beta_0,\beta_1,\dots,\beta_m,\ \log\sigma \stackrel{\text{i.i.d.}}{\sim} \text{Unif}(-C,C)
$$
for some very large constant $C$ (its exact value won't matter). Since $\sigma$ must be positive,
the "no information" assumption is put on $\log\sigma$ rather than on $\sigma$ itself; by the
change-of-variables formula the implied density of $\sigma$ is
$$
f_\sigma(x) = f_{\log\sigma}(\log x)\cdot\frac1x = \frac{I\{-C<\log x<C\}}{2Cx} = \frac{I\{e^{-C}<x<e^C\}}{2Cx},
$$
i.e. $\sigma$ is uniform on a (very wide) range on the *log* scale, not the linear one. The prior
density for all the parameters together is then
$$
f(\beta_0,\dots,\beta_m,\sigma) = f(\beta_0)\cdots f(\beta_m)f(\sigma) \propto \frac1\sigma\, I\{-C<\beta_0,\dots,\beta_m,\log\sigma<C\}.
$$
Multiplying this by the likelihood from two sections above gives the joint posterior over every
unknown parameter:
$$
f(\beta,\sigma \mid \text{data}) \propto \sigma^{-n-1}\exp\!\left(-\frac{S(\beta)}{2\sigma^2}\right) I\{-C<\beta_0,\dots,\beta_m,\log\sigma<C\}.
$$

## Marginalizing out $\sigma$

Only $\beta$ is of primary interest, so integrate $\sigma$ out. For large $C$ the range
$(e^{-C},e^C)$ is essentially $(0,\infty)$, and the substitution $s = \sigma/\sqrt{S(\beta)}$ turns
the integral into
$$
\int_0^\infty \sigma^{-n-1}\exp\!\left(-\frac{S(\beta)}{2\sigma^2}\right)d\sigma
= S(\beta)^{-n/2}\int_0^\infty s^{-n-1}\exp\!\left(-\frac{1}{2s^2}\right)ds \ \propto\ S(\beta)^{-n/2},
$$
where the remaining integral over $s$ is a fixed number that does not involve $\beta$ at all. So
$$
f(\beta \mid \text{data}) \propto I\{-C<\beta_0,\dots,\beta_m<C\}\cdot S(\beta)^{-n/2}.
$$
Since $S(\beta)^{n/2}\cdot S(\hat\beta)^{-n/2}$ is just a constant multiple (it doesn't depend on
$\beta$), this is the same density as
$$
f(\beta \mid \text{data}) \propto \left(\frac{S(\hat\beta)}{S(\beta)}\right)^{n/2} I\{-C<\beta_0,\dots,\beta_m<C\}.
$$
The posterior is inversely proportional to $S(\beta)^{n/2}$, and $S$ is minimised at $\hat\beta$, so
the **posterior mode is exactly the least-squares estimate** — the same point the frequentist route
landed on.

## Where the posterior concentrates

The ratio $\big(S(\hat\beta)/S(\beta)\big)^{n/2}$ is not just maximised at $\hat\beta$, it collapses
to almost nothing away from it once $n$ is at all large, because the exponent $n/2$ amplifies any
relative gap between $S(\beta)$ and $S(\hat\beta)$. Concretely, with $n=791$:

- if $S(\beta) = 1.1\, S(\hat\beta)$, the ratio is $(1/1.1)^{395.5} \approx 4.26\times 10^{-17}$ —
  negligible;
- if $S(\beta) = 1.01\, S(\hat\beta)$ — ten times closer — the ratio is only $(1/1.01)^{395.5}
  \approx 0.02$, still fairly small.

So for large $n$ the posterior puts essentially all its mass on $\beta$ close to $\hat\beta$, and
correspondingly the bound $-C<\beta_0,\dots,\beta_m<C$ has no practical effect once $C$ is large,
because the density is already negligible before it reaches the bound. From here on the indicator
is dropped and the posterior is written simply as
$$
f(\beta \mid \text{data}) \propto \left(\frac{S(\hat\beta)}{S(\beta)}\right)^{n/2}.
$$

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="Posterior density as a function of distance from the least-squares estimate, sharper for larger n">
  <line x1="40" y1="180" x2="320" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="180" y1="180" x2="180" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <path d="M40,178 C90,178 130,128 180,128 C230,128 270,178 320,178" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M40,179 L150,179 C165,179 170,30 180,30 C190,30 195,179 210,179 L320,179" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M40,179 L150,179 C165,179 170,30 180,30 C190,30 195,179 210,179 L320,179 L320,180 L40,180 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <text x="180" y="198" text-anchor="middle" font-size="12" fill="currentColor">beta-hat</text>
  <text x="255" y="150" text-anchor="middle" font-size="12" fill="currentColor">small n</text>
  <text x="222" y="55" text-anchor="middle" font-size="12" fill="currentColor">large n</text>
</svg>
<figcaption>The posterior of beta as a function of distance from the least-squares estimate: both
curves peak at beta-hat, but the peak sharpens rapidly as n grows, because S(beta-hat)/S(beta) is
raised to the power n/2.</figcaption>
</figure>

## The posterior is a multivariate $t$-distribution

The multivariate $t$-distribution, in the parametrisation the lecture takes from the standard
reference (Wikipedia's page on the multivariate $t$-distribution), has density
$$
f(x) = \frac{\Gamma((\nu+p)/2)}{\Gamma(\nu/2)\,\nu^{p/2}\pi^{p/2}\sqrt{\det\Sigma}}
\left[1+\frac1\nu(x-\mu)^T\Sigma^{-1}(x-\mu)\right]^{-(\nu+p)/2}
\ \propto\ \left[1+\frac1\nu(x-\mu)^T\Sigma^{-1}(x-\mu)\right]^{-(\nu+p)/2},
$$
written $t_p(\mu,\Sigma,\nu)$, where $p$ is the dimension, $\mu$ the ($p\times 1$) location, $\Sigma$
the ($p\times p$) scale matrix, and $\nu>0$ the degrees of freedom.

To see that the posterior above is a special case, apply the Pythagorean identity to rewrite
$S(\beta)$ in the denominator:
$$
f(\beta\mid\text{data}) \propto \left(\frac{S(\hat\beta)}{S(\hat\beta)+(\beta-\hat\beta)^TX^TX(\beta-\hat\beta)}\right)^{n/2}
= \left[1+(\beta-\hat\beta)^T\frac{X^TX}{S(\hat\beta)}(\beta-\hat\beta)\right]^{-n/2}.
$$
Matching this term by term against the $t$-density above — $x=\beta$, $p=m+1$, $\mu=\hat\beta$,
$\nu+p=n$, $\Sigma^{-1}/\nu = X^TX/S(\hat\beta)$ — gives $\nu=n-m-1$ and
$\Sigma = \dfrac{S(\hat\beta)}{n-m-1}(X^TX)^{-1}$. So the Bayesian posterior for the regression
coefficients is, exactly,
$$
\beta \mid \text{data} \ \sim\ t_{m+1}\!\left(\hat\beta,\ \frac{S(\hat\beta)}{n-m-1}(X^TX)^{-1},\ n-m-1\right).
$$
This is a genuinely useful closed form: it says the posterior is centred at the least-squares
estimate, its spread is governed by $(X^TX)^{-1}$ scaled by the residual sum of squares, and its
tails are those of a $t$-distribution with $n-m-1$ degrees of freedom rather than of a normal.
Uncertainty about the coefficients — or about fitted values built from them — can be quantified
directly by drawing samples from this $t_{m+1}$ distribution and looking at the spread of the
resulting curves.

## Sources

- Multiple linear regression model, its two time-series uses (regression on functions of time,
  autoregression), and the "two broad principles" framing of frequentist vs. Bayesian inference:
  Fall 2026, Lecture Four (8 Sept 2026), `01-1-multiple-linear-regression.md`; the same model and
  applications also appear in Fall 2025, Lecture Four (9 Sept 2025),
  `02-2-multiple-linear-regression.md`.
- Frequentist recipe, least-squares-as-MLE derivation, and the $y\sim N_n(X\beta,\sigma^2I_n)$
  form of the likelihood: Fall 2026, Lecture Four, `02-2-frequentist-inference-for-linear-regression.md`.
  This document is truncated mid-derivation in the source conversion — it promises an MLE for
  $\sigma$ that is not shown, and the note above flags that gap rather than supplying it.
- Least-squares estimator in matrix form, the normal equations, and the Pythagorean identity:
  Fall 2025, Lecture Four, `03-4-matrix-notation-for-multiple-linear-regression.md`.
  The high-dimensional-regression aside and the "$n \gg m$" assumption come from Spring 2025,
  Lecture Four, `LectureFour153248Spring2025.md`, which otherwise duplicates the opening of the
  Fall 2025 treatment and is cut off before doing the marginalization.
  The AR caveat about $x_i=y_{i-1}$ not being exactly fixed is from Fall 2026,
  `02-2-frequentist-inference-for-linear-regression.md`; the lecture explicitly defers the
  justification to a later lecture not included in this material.
- Uniform-on-log-$\sigma$ prior, joint posterior, marginalization over $\sigma$, the posterior
  mode/concentration argument (including the $n=791$ numerical example), and the identification of
  the posterior with the multivariate $t$-distribution: Fall 2025, Lecture Four,
  `01-1-bayesian-inference-for-simple-linear-regression.md` (worked for simple regression, $m=1$)
  and `02-2-multiple-linear-regression.md` (generalized to $m$ covariates), with the final matrix
  form in `03-4-matrix-notation-for-multiple-linear-regression.md`. The multivariate $t$-density
  formula itself is quoted from Wikipedia's "Multivariate t-distribution" page, as the lecture does.
- All of the above documents are machine reconstructions of PDF slides with no extractable text
  layer (course: UC Berkeley STAT 153/248, instructor Aditya Guntuboyina); no separate transcript
  or problem set was supplied for this lecture, and none is referenced here.

---

[← 104. The Posterior t-Distribution in Regression](104-the-posterior-t-distribution-in-regression.md) · [Contents](index.md) · [106. Mean, Variance, and Spectrum Models →](106-mean-variance-and-spectrum-models.md)
