---
title: "118. Bayesian View of Ridge Regression"
course: "Berkeley Stat 153"
chapter: 118
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 118. Bayesian View of Ridge Regression

## What this covers

This chapter answers: what does ridge regression *mean* if you think of it as a Bayesian
calculation rather than as a penalized least-squares problem, and what changes if the smoothing
parameter is itself treated as unknown and inferred from the data? It assumes the piecewise-linear
trend model built from an intercept, a slope, and a run of $\mathrm{ReLU}$ basis functions (the
subject of the two lectures before this one), the ridge estimator for that model, and the basic
mechanics of Bayesian linear regression — a prior on $\beta$, a Gaussian likelihood, a normal
posterior — from an earlier lecture.

## Ridge regression, recap

The working model for the trend of a time series $y_1, \dots, y_n$ is

$$y_t = \beta_0 + \beta_1(t-1) + \beta_2\,\mathrm{ReLU}(t-2) + \dots + \beta_{n-1}\,\mathrm{ReLU}\big(t-(n-1)\big) + \epsilon_t,$$

with $\epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2)$ and $\mathrm{ReLU}(t-c) = (t-c)_+$, equal to
$0$ for $t \le c$ and to $t - c$ for $t > c$. The unknown parameters are $\beta_0, \dots,
\beta_{n-1}$ and $\sigma$. Writing this in matrix form, $y = X\beta + \epsilon$, where the columns
of $X$ are the intercept, the linear term, and the successive $\mathrm{ReLU}$ kinks evaluated at
$t = 1, \dots, n$, and $\beta = (\beta_0, \dots, \beta_{n-1})^T$.

Fitting this model by ordinary least squares interpolates the data exactly once $n$ is the number
of observations, because there are as many basis functions as data points — every kink is free to
place itself wherever it wants. Ridge regression controls this by penalizing the kink coefficients,
leaving the intercept and the overall slope alone: $\hat\beta_{\mathrm{ridge}}(\lambda)$ minimizes

$$\|y - X\beta\|^2 + \lambda \sum_{j=2}^{n-1} \beta_j^2.$$

Only $\beta_2, \dots, \beta_{n-1}$ — the coefficients that let the fit bend — are shrunk; $\beta_0$
and $\beta_1$, which only set the level and the overall trend, are not. Differentiating and setting
the gradient to zero, with $J$ the $n\times n$ diagonal matrix whose first two diagonal entries are
$0$ and whose remaining entries are $1$ (so that $J\beta$ zeroes out $\beta_0,\beta_1$ and keeps the
rest), gives

$$-2X^Ty + 2X^TX\beta + 2\lambda J\beta = 0 \quad\Longrightarrow\quad \hat\beta_{\mathrm{ridge}}(\lambda) = \big(X^TX + \lambda J\big)^{-1}X^Ty.$$

This is the ordinary least-squares formula $(X^TX)^{-1}X^Ty$ with $\lambda J$ added inside the
inverse — the only change is the extra term that penalizes the kinks.

## Bayesian regression with two different priors

Bayesian regression puts a prior on $\beta$ and asks for the posterior given the data and $\sigma$.
The prior used earlier in the course was flat: $\beta_j \overset{\text{i.i.d.}}{\sim}
\mathrm{Unif}(-C,C)$ for a large constant $C$. Under that prior, as $C \to \infty$,

$$\beta \mid \text{data}, \sigma \;\sim\; N\Big((X^TX)^{-1}X^Ty,\; \sigma^2(X^TX)^{-1}\Big),$$

recovering the ordinary least-squares estimate as the posterior mean. The catch is the phrase "as
$C \to \infty$": this is only approximately true for finite $C$.

A Gaussian prior fixes that. If $\beta_j \overset{\text{i.i.d.}}{\sim} N(0,C)$, then for *every*
$C>0$ (not just in a limit),

$$\beta \mid \text{data},\sigma \;\sim\; N\!\left(\left(\frac{X^TX}{\sigma^2}+\frac{I}{C}\right)^{-1}\frac{X^Ty}{\sigma^2},\; \left(\frac{X^TX}{\sigma^2}+\frac{I}{C}\right)^{-1}\right).$$

As $C \to \infty$ this reduces to the flat-prior posterior above, which makes sense: a very wide
Gaussian and a very wide uniform prior are both saying "I have no real preference among values of
$\beta$," and the two priors become interchangeable in that limit. The derivation of this posterior
is given in general form below.

## A prior that regularizes

Used with a huge $C$, the Gaussian prior is uninformative and the posterior mean is again the
unregularized least-squares fit — which interpolates the data and overfits, for the same reason
plain least squares does on this model. The fix mirrors the ridge penalty exactly: give the
unpenalized coefficients a wide prior and the kink coefficients a narrow one,

$$\beta_0, \beta_1 \overset{\text{i.i.d.}}{\sim} N(0,C), \qquad \beta_2, \dots, \beta_{n-1} \overset{\text{i.i.d.}}{\sim} N(0,\tau^2),$$

all independent, for some small $\tau$. Writing $\beta \sim N(0,Q)$ with $Q$ the diagonal matrix
$\mathrm{diag}(C, C, \tau^2, \dots, \tau^2)$, the posterior (proved below for general $Q$) is

$$\beta \mid \text{data}, \sigma \;\sim\; N\!\left(\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\frac{X^Ty}{\sigma^2},\; \left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\right),$$

with posterior mean $\big(X^TX + \sigma^2 Q^{-1}\big)^{-1}X^Ty$. Since $Q^{-1}$ has diagonal entries
$1/C, 1/C, 1/\tau^2, \dots, 1/\tau^2$, letting $C \to \infty$ sends the first two entries to $0$, so
$Q^{-1} \approx \tau^{-2} J$, and the posterior mean becomes

$$\left(X^TX + \frac{\sigma^2}{\tau^2}J\right)^{-1}X^Ty.$$

This is exactly the ridge estimator, with

$$\lambda = \frac{\sigma^2}{\tau^2}, \qquad\text{equivalently}\qquad \tau = \frac{\sigma}{\sqrt\lambda}.$$

So ridge regularization *is* Bayesian regression under a prior that treats the kink coefficients as
draws from a tight $N(0,\tau^2)$: shrinking $\lambda$ up in the frequentist picture is the same
move as shrinking the prior variance $\tau^2$ down in the Bayesian one, and the two are precisely
interchangeable once $\lambda$ and $\tau$ are related by $\lambda = \sigma^2/\tau^2$.

## Deriving the posterior: completing the square

Both posterior formulas above are instances of one calculation, for a general prior covariance
$Q$ on $\beta$ (diagonal or not). The log-posterior density of $\beta$, up to an additive constant,
combines the Gaussian log-likelihood and the Gaussian log-prior:

$$\frac{1}{\sigma^2}\|y - X\beta\|^2 + \beta^TQ^{-1}\beta.$$

Expanding the squared norm and collecting terms in $\beta$,

$$\frac{1}{\sigma^2}\|y-X\beta\|^2 + \beta^TQ^{-1}\beta = \frac{y^Ty}{\sigma^2} - \frac{2\beta^TX^Ty}{\sigma^2} + \beta^T\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)\beta,$$

which is a quadratic form in $\beta$ and can be completed to a square around

$$\mu := \left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\frac{X^Ty}{\sigma^2}:$$

$$\frac{1}{\sigma^2}\|y-X\beta\|^2 + \beta^TQ^{-1}\beta = (\beta-\mu)^T\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)(\beta-\mu) + \Big(\text{terms not involving }\beta\Big).$$

Exponentiating, the posterior density factors into a piece depending on $\beta$ through the
quadratic $(\beta-\mu)^T(\cdots)(\beta-\mu)$ and a piece that does not depend on $\beta$ at all —
which is exactly the shape of a Gaussian density in $\beta$ centered at $\mu$. Hence

$$\beta \mid \text{data}, \sigma \;\sim\; N\!\left(\mu, \left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\right)$$

for *any* prior covariance $Q$ — the $Q = CI$ case gives the uninformative-Gaussian-prior posterior,
and the $Q = \mathrm{diag}(C,C,\tau^2,\dots,\tau^2)$ case gives the ridge-equivalent posterior. Both
are the same computation with a different $Q$ plugged in.

## Letting the data choose the smoothing parameter

The prior in the previous section still requires picking $\tau$ by hand, exactly as the frequentist
ridge estimator requires picking $\lambda$. The distinctively Bayesian move is to put a prior on
$\tau$ (and, while at it, on $\sigma$) as well, and let the posterior decide what values of $\tau$
and $\sigma$ the data support. Use a prior that is flat on the log scale,

$$\log\tau, \log\sigma \overset{\text{i.i.d.}}{\sim} \mathrm{Unif}(-C,C),$$

together with $\beta \mid \tau,\sigma \sim N(0,Q)$, $Q$ as before. A flat prior on $\log\tau$ treats
all *orders of magnitude* of $\tau$ as equally likely a priori, so it does not rule out large $\tau$
just because a wiggly fit looks unappealing before seeing the data. Converting to a density on $\tau$
itself contributes a factor $1/\tau$ (and likewise $1/\sigma$ for $\sigma$), so the prior density is

$$f_{\beta,\tau,\sigma}(\beta,\tau,\sigma) \;\propto\; \frac{1}{\tau\sigma}\,\frac{1}{\sqrt{\det Q}}\exp\!\left(-\tfrac12\beta^TQ^{-1}\beta\right)$$

once the (very wide) indicator on $\tau,\sigma$ is dropped. Multiplying by the usual Gaussian
likelihood $\sigma^{-n}\exp\!\left(-\frac{1}{2\sigma^2}\|y-X\beta\|^2\right)$ gives the joint
posterior

$$f_{\beta,\tau,\sigma\mid\text{data}}(\beta,\tau,\sigma) \;\propto\; \frac{\sigma^{-n-1}\tau^{-1}}{\sqrt{\det Q}}\exp\left(-\frac12\left(\frac{1}{\sigma^2}\|y-X\beta\|^2 + \beta^TQ^{-1}\beta\right)\right).$$

Note that $Q$ now depends on $\tau$, but the exponent is still exactly the quadratic form completed
in the previous section — the calculation carries over unchanged, conditional on $\tau,\sigma$. So

$$\beta \mid \text{data},\sigma,\tau \;\sim\; N\!\left(\mu, \left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\right), \qquad \mu = \left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\frac{X^Ty}{\sigma^2},$$

confirming the earlier formulas as the special case with $\tau,\sigma$ fixed. Integrating $\beta$
out of the joint posterior (the completed-square form makes this a standard Gaussian integral)
leaves the marginal posterior of $\tau,\sigma$ alone:

$$f_{\tau,\sigma\mid\text{data}}(\tau,\sigma) \;\propto\; \frac{\sigma^{-n-1}\tau^{-1}}{\sqrt{\det Q}}\sqrt{\det\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}}\exp\left(-\frac{y^Ty}{2\sigma^2}\right)\exp\left(\frac{y^TX}{2\sigma^2}\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\frac{X^Ty}{\sigma^2}\right).$$

In practice this is evaluated on a grid of $(\sigma,\tau)$ values (on the log scale, to keep the
arithmetic stable), which gives either point estimates — the posterior maximizer — or posterior
samples, by resampling grid points with weights proportional to the posterior. For each sampled
$(\sigma,\tau)$, a sample of $\beta$ follows from the conditional normal above. This grid search can
be replaced by MCMC methods such as a Gibbs sampler, which the lecture mentions but does not work
through.

## Why the data-driven $\tau$ lands in the middle

Empirically, the posterior over $\tau$ (given $\sigma$) favors values that are neither too small nor
too large — it does the job that hand-tuning $\lambda$ by trial and error would otherwise have to
do. The reason is visible in the marginal likelihood. Since the prior $f_{\tau,\sigma}(\tau,\sigma)$
is nearly flat, the posterior shape is driven almost entirely by the likelihood
$f_{\text{data}\mid\tau,\sigma}(\text{data})$, which is a genuinely different object from the
likelihood $f_{\text{data}\mid\beta,\sigma}(\text{data})$ used in ordinary maximum likelihood.
Maximizing the latter over $\beta$ gives the unregularized (interpolating) fit; maximizing the
former over $\tau$ typically gives a small $\hat\tau$ and hence a smooth fit. The two disagree
because the $\tau$-likelihood is an average of the $\beta$-likelihood over the prior on $\beta$:

$$f_{\text{data}\mid\tau,\sigma}(\text{data}) = \int f_{\text{data}\mid\beta,\sigma}(\text{data})\, f_{\beta\mid\tau}(\beta)\, d\beta.$$

If $\tau$ is large, the prior density $f_{\beta\mid\tau}(\beta)$ is spread thin over a huge range of
$\beta$ values, so it is small everywhere, including at the $\beta$ that fits the data best — the
average is dragged down by all the implausible values of $\beta$ the wide prior takes seriously. If
$\tau$ is very small, the prior concentrates its mass on smooth $\beta$'s, but those $\beta$'s fit
the data poorly, so $f_{\text{data}\mid\beta,\sigma}(\text{data})$ itself is small at the points
where the prior actually puts weight. A moderate $\tau$ is the compromise that keeps both factors
from collapsing at once, which is exactly why the marginal likelihood — and hence the posterior —
peaks somewhere in between.

## Sources

- Ridge regression recap, the model, the design matrix, the penalized objective, the gradient
  calculation and the closed-form ridge estimator: Fall 2025 Lecture Twelve (Aditya Guntuboyina,
  October 6, 2025), file `01-1-recap-ridge-regression.md`. No equivalent file was supplied from
  Spring 2025 for this section.
- The two Bayesian regression priors (uniform vs. Gaussian), the regularizing prior
  $N(0,\mathrm{diag}(C,C,\tau^2,\dots,\tau^2))$, and the $\lambda=\sigma^2/\tau^2$ equivalence:
  Fall 2025 `02-2-bayesian-regularization.md`, matching Spring 2025
  `02-2-bayesian-regularization.md` (same content in both offerings; Fall cites this as "problem 5
  in Homework 1", Spring as "problem 4 in Homework 1" — that homework is referred to but not
  supplied here).
- The general completing-the-square derivation of the posterior of $\beta$, the hierarchical prior
  on $\tau,\sigma$, the joint and marginal posteriors, and the grid/MCMC remark on inference: Fall
  2025 `03-3-bayesian-approach-for-dealing-with-unknown-and.md`, matching Spring 2025
  `03-3-bayesian-approach-for-dealing-with-unknown-and.md`.
- The marginal-likelihood argument for why moderate $\tau$ is favored: Fall 2025
  `04-4-comments-on-bayesian-regularization.md`, matching Spring 2025
  `04-4-comments-on-bayesian-regularization.md`.
- All of the above are model reconstructions of PDF slide decks with no extractable text layer
  (route: llm, fidelity: reconstructed); the equations are flagged unverified in the source files
  and are reproduced here as given, with one silent notational fix (the ridge penalty's summation
  index, given inconsistently as $t$ in the source, is written as $j$ throughout for consistency
  with $\beta_j$).

---

[← 117. Bayesian Priors and Least Squares](117-bayesian-priors-and-least-squares.md) · [Contents](index.md) · [119. MA Models and AR(p) Stationarity →](119-ma-models-and-ar-p-stationarity.md)
