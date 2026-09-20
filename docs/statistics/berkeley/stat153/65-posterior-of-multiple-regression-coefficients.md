---
title: "65. Posterior of Multiple Regression Coefficients"
course: "Berkeley Stat 153 Fall 2024"
chapter: 65
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 65. Posterior of Multiple Regression Coefficients

## What this covers

This chapter sets up multiple linear regression in the Bayesian framework used earlier in the
course for the one-covariate case, and asks the same question: given data, what does the posterior
distribution over the regression coefficients look like? The answer turns out to have exactly the
algebraic shape of a multivariate $t$-density, so most of the chapter is spent building the
background needed to say that precisely — the multivariate normal distribution, the multivariate
$t$ distribution, and the fact that a single coordinate of a multivariate $t$ vector is itself a
univariate $t$. It assumes the reader already has simple (one-covariate) Bayesian regression, the
least-squares estimate, and the univariate normal and $t$ distributions.

## Setting up multiple regression

The data now carries several covariates per observation instead of one:
$$y_i, \quad x_{i1}, x_{i2}, \dots, x_{im}, \qquad i = 1, \dots, n,$$
and the model is the direct extension of simple linear regression to $m$ covariates:
$$y_i = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_m x_{im} + \varepsilon_i, \qquad
\varepsilon_i \overset{\text{iid}}{\sim} N(0, \sigma^2).$$

## The Bayesian model: flat priors on the coefficients and on $\log\sigma$

As in the one-covariate case, each coefficient is given an (improper, in the limit) flat prior:
$$\beta_0, \beta_1, \dots, \beta_m \overset{\text{iid}}{\sim} \text{Unif}(-C, C), \qquad C \to \infty,$$
and the noise standard deviation is given a prior that is flat on the *log* scale rather than on
$\sigma$ itself:
$$\log \sigma \sim \text{Unif}(-C, C), \qquad C \to \infty.$$
Neither of these is a genuine probability distribution in the limit $C \to \infty$ — they carry
essentially no information about where $\beta$ or $\sigma$ lie — but they are the priors that make
the posterior come out in closed form, and (as below) make it peak exactly at the least-squares
estimate.

Given data $y_1, \dots, y_n$, the object of interest is the posterior over $(\beta_0, \dots,
\beta_m, \sigma)$, and from it the marginal posterior over the coefficients alone:
$$f_{\beta_0 \dots \beta_m \mid y_1 \dots y_n}(\beta_0, \dots, \beta_m)
= \int_0^\infty f_{\beta_0 \dots \beta_m, \sigma \mid y_1 \dots y_n}(\beta_0, \dots, \beta_m, \sigma)
\, d\sigma.$$

## Integrating out $\sigma$: the posterior depends on $\beta$ only through the residual sum of squares

With the flat priors above, the integral over $\sigma$ can be carried out explicitly (in the limit
$C \to \infty$), and it collapses to
$$f(\beta_0, \dots, \beta_m \mid \text{data}) \;\propto\; \left[\frac{1}{S(\beta)}\right]^{n/2},
\qquad
S(\beta) = S(\beta_0, \dots, \beta_m) = \sum_{i=1}^n \bigl(y_i - \beta_0 - \beta_1 x_{i1} - \cdots
- \beta_m x_{im}\bigr)^2.$$
$S(\beta)$ is exactly the residual sum of squares — the same quantity ordinary least squares
minimizes. So the whole posterior over the coefficients is a function of $\beta$ through $S(\beta)$
alone, and nothing else about the data matters once $S(\beta)$ is known as a function of $\beta$.

Let $\hat\beta = (\hat\beta_0, \dots, \hat\beta_m)$ minimize $S(\beta)$: this is exactly the
least-squares estimate. Since $1/S(\beta)$ is largest exactly where $S(\beta)$ is smallest, the
posterior is maximized at $\hat\beta$. Dividing numerator and denominator by the constant
$S(\hat\beta)$ turns this into an equivalent (still proportional) expression that is normalized to
equal $1$ at the mode:
$$f(\beta \mid \text{data}) \;\propto\; \left[\frac{S(\hat\beta)}{S(\beta)}\right]^{n/2}.$$

Because $S(\beta) \ge S(\hat\beta)$ everywhere, this ratio is at most $1$, and equals $1$ only at
$\beta = \hat\beta$. Raising it to the power $n/2$ makes it fall off sharply away from $\hat\beta$
once $n$ is at all large: any $\beta$ for which $S(\beta)$ is even a little larger than
$S(\hat\beta)$ gets its ratio pushed toward $0$ as $n$ grows. So, exactly as in the one-covariate
case, the posterior over $\beta$ becomes highly concentrated around the least-squares estimator as
the sample size grows.

## Recognizing the shape: the multivariate $t$-density

The general multivariate $t$ density, for a $p$-vector $x$ with location $\mu$, scale matrix
$\Sigma$, and degrees of freedom $\nu$, has kernel
$$t_p(\mu, \Sigma, \nu): \qquad f(x) \;\propto\; \left[1 + \frac{1}{\nu}(x - \mu)^T \Sigma^{-1}
(x - \mu)\right]^{-\frac{\nu + p}{2}}.$$
The posterior kernel $\bigl[S(\hat\beta)/S(\beta)\bigr]^{n/2}$ has the same shape: it is a ratio,
raised to a power built from the sample size, that equals $1$ at a center point and decreases as a
function of how far the argument is from that center. Once $S(\beta)$ is expanded as a quadratic
function of $\beta$ around its minimizer $\hat\beta$, the ratio $S(\beta)/S(\hat\beta)$ becomes
$1$ plus a quadratic form in $(\beta - \hat\beta)$, matching the $t_p$ kernel term for term, with
$p = m+1$ (one coordinate per coefficient $\beta_0, \dots, \beta_m$). This is why, in multiple
regression, the natural distribution for describing how far the posterior could stray from the
least-squares estimate is a *multivariate* $t$ — the direct generalization of the univariate $t$
that shows up for a single coefficient in simple regression.

The rest of the lecture builds exactly the background needed to use this identification: what a
multivariate normal and multivariate $t$ distribution are, how the $t$ is built from the normal,
and — the fact the lecture ends on — that a single coordinate of a multivariate $t$ vector is again
a univariate $t$. That last fact is what is actually needed to say anything about one coefficient
$\beta_j$ at a time.

## Background: the multivariate normal

A $p$-dimensional normal vector $X = (X_1, \dots, X_p) \sim N_p(\mu, \Sigma)$ has density
$$f(x) \;\propto\; \exp\left[-\frac{(x-\mu)^T \Sigma^{-1} (x - \mu)}{2}\right],$$
the direct generalization of the univariate "$\exp[-\text{square}]$" shape. Here:

- $\mu = (\mathbb{E}X_1, \dots, \mathbb{E}X_p)^T$ is the vector of means, and
- $\Sigma$ is the covariance matrix, with $\Sigma(i,j) = \text{Cov}(X_i, X_j)$; in particular the
  diagonal entries are the ordinary variances, $\Sigma(j,j) = \text{Var}(X_j)$.

Two properties of the multivariate normal are used without further proof:

- **Every subvector is normal.** If $X \sim N_p(\mu, \Sigma)$, then every individual component is
  normal, $X_j \sim N(\mu_j, \Sigma(j,j))$, and more generally any subset of the components — e.g.
  $(X_1, X_2)$ — is jointly normal, with mean vector and covariance matrix given by the
  corresponding entries of $\mu$ and $\Sigma$.
- **Every linear combination is normal.** Any linear combination of $X_1, \dots, X_p$ is itself a
  normal random variable.

## Background: chi-squared, and building the $t$ distribution from the normal

The chi-squared distribution with $\nu$ degrees of freedom is the distribution of a sum of $\nu$
squared independent standard normals:
$$\chi^2_\nu \;\overset{d}{=}\; Z_1^2 + \cdots + Z_\nu^2, \qquad Z_j \overset{\text{iid}}{\sim}
N(0,1).$$
Since $\mathbb{E}(Z_j^2) = 1$ for each $j$, $\mathbb{E}(\chi^2_\nu) = \nu$.

The multivariate $t$ is built from a multivariate normal exactly as the univariate $t$ is built
from a univariate normal: take $X \sim N_p(\mu, \Sigma)$ and, independently, $V \sim \chi^2_\nu$,
and define
$$T = \mu + \frac{X - \mu}{\sqrt{V/\nu}}.$$
Every coordinate of $X$ is centered at $\mu$ and then divided by the *same* random scale factor
$\sqrt{V/\nu}$. The stated fact is that $T \sim t_p(\mu, \Sigma, \nu)$.

## Why a single coordinate of a multivariate $t$ is a univariate $t$

Write out the $j$-th coordinate of $T$:
$$T_j = \mu_j + \frac{X_j - \mu_j}{\sqrt{V/\nu}}.$$
By the marginal property of the multivariate normal, $X_j \sim N(\mu_j, \Sigma(j,j))$, and $V$ is
the same $\chi^2_\nu$ variable used to build every coordinate of $T$. So $T_j$ is built from a
univariate normal and an independent $\chi^2_\nu$ in exactly the way a univariate $t$ variable is
defined, giving
$$T_j \sim t_1\bigl(\mu_j, \Sigma(j,j), \nu\bigr).$$
In words: **a single component of a multivariate $t$ vector is a univariate $t$**, with the same
location $\mu_j$ and the same degrees of freedom $\nu$, and with scale taken from the matching
diagonal entry of $\Sigma$.

This is exactly the tool needed to talk about one regression coefficient at a time. If the joint
posterior of $(\beta_0, \dots, \beta_m)$ is (once $\Sigma$ and $\nu$ are identified from the
quadratic expansion of $S(\beta)$ above) a multivariate $t$ centered at the least-squares estimate
$\hat\beta$, then the posterior of any single $\beta_j$ falls out as a univariate $t$ centered at
$\hat\beta_j$ — the same kind of distribution used for the one coefficient in simple regression,
now justified when there are several covariates at once.

## Sources

- Multiple-regression setup, the flat/improper priors, integrating out $\sigma$, the posterior
  $\propto [S(\hat\beta)/S(\beta)]^{n/2}$, and its identification with the multivariate $t$ kernel:
  `docs/statistics/berkeley/stat153/fall-2026/HandwrittenNotesLectureFive153248Fall2026/01-multiple-regression.md`
  ("Multiple Regression" through "Connection to the multivariate $t$-density"). The same material,
  as far as the definition of $S(\beta)$ before the page is cut off, is corroborated by
  `docs/statistics/berkeley/stat153/fall-2025/HandwrittenNotesLectureFive153248Fall2025.md`.
- The multivariate normal, the chi-squared construction of the multivariate $t$, and the fact that
  its coordinates are univariate $t$: the same fall-2026 file, sections "Normal Density" and
  "$t$ & Normal".
- No slide deck, transcript, or problem set was supplied for this lecture. Both note files are
  themselves reconstructions: the source PDFs have no text layer, a model transcribed the
  handwritten pages, and every equation in them is flagged unverified by the conversion — so the
  algebra above should be checked against the original PDFs linked in each file's front matter
  before it is relied on as a citation.

---

[← 64. Ridge and Lasso Trend Filtering](64-ridge-and-lasso-trend-filtering.md) · [Contents](index.md) · [66. Frequentist and Bayesian Regression Inference →](66-frequentist-and-bayesian-regression-inference.md)
