---
title: "70. Bayesian Shrinkage and Variance Models"
course: "Berkeley Stat 153"
chapter: 70
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 70. Bayesian Shrinkage and Variance Models

## What this covers

This chapter answers a question about regularized regression: when a ridge penalty is used to
smooth a spline fit, where does the penalty strength come from, and can it be set by the data
itself rather than tuned by cross-validation? The answer is a fully Bayesian version of ridge
regression, worked out for a piecewise-linear spline. It assumes regression splines built from a
truncated-power basis, ridge regression as penalized least squares, and the mechanics of Bayesian
updating — prior times likelihood gives posterior — for a linear-Gaussian model. The notes pick up
the spline model mid-stream, so its construction is taken here exactly as given; the chapter ends
with a short transition into a different class of model, one where it is the variance rather than
the mean that moves over time.

## The spline model and its knots

The model under study is a piecewise-linear curve built from a truncated-power basis, with a knot
at every interior time point:

$$y_t = \beta_0 + \beta_1(t-1)_+ + \beta_2(t-2)_+ + \dots + \beta_{n-1}\bigl(t-(n-1)\bigr)_+ + \varepsilon_t.$$

Here $(t-j)_+$ means $t-j$ when $t \ge j$ and $0$ otherwise. The term $\beta_0$ sets the overall
level, $\beta_1(t-1)_+$ contributes the baseline linear trend, and each further term
$\beta_j(t-j)_+$ for $j \ge 2$ does nothing before $t=j$ and adds $\beta_j$ to the slope from $t=j$
onward. So $\beta_j$ is exactly the change in slope at the knot $j$: a curve with all these
coefficients equal to zero is a straight line, and turning one on puts a kink in the line at that
knot.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="A piecewise-linear curve bending at a knot, showing that one truncated-power term changes only the slope after its knot.">
  <line x1="30" y1="170" x2="320" y2="170" stroke="currentColor" stroke-width="1"/>
  <text x="320" y="188" font-size="12" text-anchor="end" fill="currentColor">t</text>
  <line x1="40" y1="150" x2="180" y2="105" stroke="currentColor" stroke-width="2"/>
  <line x1="180" y1="105" x2="300" y2="60" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.55"/>
  <line x1="180" y1="105" x2="300" y2="30" stroke="currentColor" stroke-width="2"/>
  <circle cx="180" cy="105" r="3" fill="currentColor"/>
  <text x="180" y="188" font-size="12" text-anchor="middle" fill="currentColor">knot at t = j</text>
  <text x="250" y="45" font-size="11" fill="currentColor">slope + &#946;&#8320;</text>
  <text x="285" y="80" font-size="11" fill="currentColor" opacity="0.6">slope without &#946;&#8320;</text>
</svg>
<figcaption>Adding the term $\beta_j(t-j)_+$ leaves the curve unchanged before $t=j$ and adds
$\beta_j$ to the slope after it. A knot coefficient near zero keeps the curve smooth there; letting
every knot coefficient move freely lets the curve bend at every single time point and interpolate
the data.</figcaption>
</figure>

Because there is a knot at every interior point, fitting this model by ordinary least squares would
simply interpolate the data — as many parameters as points to fit. The rest of the lecture is about
controlling that flexibility with priors instead of by hand-picking which knots to keep.

## Priors: flat on the trend, shrinkage on the kinks

The coefficients are split into two groups and given different priors:

$$\beta_0, \beta_1 \overset{\text{i.i.d.}}{\sim} N(0, C) \ \text{ (or } \mathrm{Unif}(-C,C)\text{)}, \qquad \beta_2, \dots, \beta_{n-1} \overset{\text{i.i.d.}}{\sim} N(0, \tau^2),$$

with $C$ taken very large, and diffuse priors on the log scale for the two remaining hyperparameters:

$$\log \tau \sim \mathrm{Unif}(-C, C), \qquad \log \sigma \sim \mathrm{Unif}(-C, C).$$

The asymmetry is deliberate. The level and the baseline trend, $\beta_0$ and $\beta_1$, are given an
essentially flat prior — there is no reason to shrink the overall straight-line fit toward zero. The
knot coefficients $\beta_2,\dots,\beta_{n-1}$ are given a common Gaussian prior with variance
$\tau^2$: this expresses the belief that most kinks should be small, i.e. that the true curve is
close to smooth, and $\tau$ controls how much curvature is tolerated. Small $\tau$ says "expect
almost no kinks"; large $\tau$ says "kinks of any size are plausible."

## The posterior of $\beta$, and why it is ridge regression

Writing $Q$ for the prior covariance of the full coefficient vector $\beta$ — the diagonal matrix
with $C, C, \tau^2,\dots,\tau^2$ down the diagonal — the likelihood is Gaussian in $\beta$ and the
prior is Gaussian in $\beta$, so the posterior is Gaussian too, by the usual conjugate-normal
updating (precision adds, and the mean is the precision-weighted combination):

$$\beta \mid \text{data}, \sigma, \tau \sim N\!\left(\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\frac{X^Ty}{\sigma^2},\ \left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\right).$$

As $C \to \infty$, the prior on $\beta_0,\beta_1$ becomes flat, so its contribution to the precision
$Q^{-1}$ vanishes, leaving

$$Q^{-1} \approx \frac{1}{\tau^2}J, \qquad J = \mathrm{diag}(0,0,1,1,\dots,1),$$

the matrix that zeroes out the first two coordinates and picks out the rest. Substituting gives

$$\beta \mid \text{data}, \sigma, \tau \sim N\!\left(\left(X^TX+\frac{\sigma^2}{\tau^2}J\right)^{-1}X^Ty,\ \sigma^2\left(X^TX+\frac{\sigma^2}{\tau^2}J\right)^{-1}\right).$$

Compare this with ridge regression, minimizing squared error plus a penalty on the knot
coefficients only:

$$\|y-X\beta\|^2 + \lambda\sum_{j=2}^{n-1}\beta_j^2 \qquad\Longrightarrow\qquad \hat\beta_{\text{ridge}}(\lambda) = (X^TX+\lambda J)^{-1}X^Ty.$$

The two formulas match term for term: the posterior mean of $\beta$ *is* the ridge estimate,
provided

$$\lambda = \frac{\sigma^2}{\tau^2}.$$

This is the standard Bayesian reading of a ridge penalty: penalizing $\sum \beta_j^2$ is, up to a
constant, the same as putting an independent Gaussian prior on those coefficients, and the
regularization strength $\lambda$ is exactly the ratio of the noise variance to the prior variance.
A tight prior on the kinks (small $\tau$) means strong shrinkage (large $\lambda$); a loose prior
(large $\tau$) means weak shrinkage (small $\lambda$).

## Choosing $\tau$ and $\sigma$ from the data

Ordinary ridge regression leaves $\lambda$ to be chosen separately, typically by cross-validation.
The Bayesian version instead gives $(\tau,\sigma)$ their own posterior,

$$f(\tau,\sigma\mid\text{data}) \propto f(\text{data}\mid\tau,\sigma)\, f(\tau,\sigma),$$

with prior $f(\tau,\sigma)\propto \dfrac{1}{\tau\sigma}$, the density implied by taking $\log\tau$
and $\log\sigma$ independently flat — an "uninformative" prior that treats no order of magnitude of
either scale as more likely than another.

The likelihood term $f(\text{data}\mid\tau,\sigma)$ here is the *integrated*, or *marginal*,
likelihood: the ordinary likelihood $f(\text{data}\mid\beta,\sigma)$ with $\beta$ averaged out
against its prior rather than maximized over,

$$f(\text{data}\mid\tau,\sigma) = \int f(\text{data}\mid\beta,\sigma)\, f(\beta\mid\tau)\, d\beta, \qquad f(\text{data}\mid\beta,\sigma) = \left(\frac{1}{\sqrt{2\pi}\,\sigma}\right)^n \exp\left(-\frac{\|y-X\beta\|^2}{2\sigma^2}\right).$$

Integrating out $\beta$ rather than maximizing over it matters, because the ordinary likelihood
maximized over $\beta$ is always largest for whichever $\beta$ overfits the data — exactly what
happens when there are as many knots as data points. Averaging the likelihood against the *whole*
prior spread of $\beta$, at a given $\tau$, measures how well that whole range of plausible curves
explains the data, not just the single best-fitting one, and this builds in a penalty at both
extremes of $\tau$:

- **$\tau$ too large:** the prior $N(0,\tau^2)$ on each knot coefficient is spread thin — its peak
  height is $\propto 1/\tau$ — so even though some $\beta$ drawn from that wide prior would overfit
  and match the data closely, most of the prior's mass does not, and the average likelihood
  $f(\text{data}\mid\tau,\sigma)$ comes out small. This is the mechanism that lets the posterior
  disfavor $\tau$ that is too large, i.e. avoid overfitting.
- **$\tau$ too small:** the prior forces every knot coefficient near zero, so the fitted curve is
  nearly a straight line regardless of the data; unless the true curve really is close to a
  straight line, the fit is poor and $f(\text{data}\mid\tau,\sigma)$ is again small. This is what
  lets the posterior disfavor $\tau$ that is too small, i.e. avoid underfitting.

So $f(\tau,\sigma\mid\text{data})$, viewed as a function of $\tau$ at fixed $\sigma$, tends to peak
at an intermediate value that trades flexibility against fit — the same trade-off cross-validation
is used for, obtained here directly from the probability model. The lecture illustrated the
comparison with two candidate values at a fixed $\sigma=2$: $f(\tau=0.5,\sigma=2\mid\text{data})=17$
against $f(\tau=0.05,\sigma=2\mid\text{data})=25$, one pair of numbers showing that the posterior
distinguishes between candidate values of $\tau$ rather than being flat in it.

Carrying out the Gaussian integral over $\beta$ (a standard multivariate-normal identity: it
completes the square, contributing a determinant factor and an exponential evaluated at the
posterior mean) gives the explicit joint posterior

$$f(\sigma,\tau\mid\text{data}) \propto \frac{\sigma^{-n-1}\tau^{-1}}{\sqrt{\det Q}}\sqrt{\det\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}}\ \exp\left(-\frac{y^Ty}{2\sigma^2}\right)\exp\left(\frac{y^TX\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}X^Ty}{2\sigma^2}\right),$$

using $\det Q = C^2(\tau^2)^{n-2} \propto (\tau^2)^{n-2}$ (the factor of $C^2$ is a fixed constant
and drops out of the proportionality). In principle this can be evaluated over a grid of
$(\tau,\sigma)$ values, and posterior samples of $(\tau,\sigma)$ drawn from that grid, with $\beta$
then generated conditional on each sampled pair.

## A reparametrization that makes $\sigma$ integrate out

Working directly with $(\tau,\sigma)$ on a two-dimensional grid is workable but wasteful, since the
formula above still needs $\sigma$ integrated out separately to summarize $\tau$ alone. The lecture
used a change of coordinates: set

$$\gamma = \frac{\tau}{\sigma} \qquad\text{so that}\qquad \tau = \sigma\gamma, \qquad \lambda = \frac{\sigma^2}{\tau^2} = \frac{1}{\gamma^2},$$

and move the flat prior from $(\log\tau,\log\sigma)$ onto $(\log\gamma,\log\sigma)$:

$$\log\tau,\log\sigma \overset{\text{i.i.d.}}{\sim}\mathrm{Unif}(-C,C) \quad\longrightarrow\quad \log\gamma,\log\sigma\overset{\text{i.i.d.}}{\sim}\mathrm{Unif}(-C,C).$$

This is the same model — $\lambda$, and hence the ridge penalty, is unchanged — just re-expressed
in a pair of coordinates in which $\sigma$ can be integrated out of the joint posterior in closed
form. What remains is a marginal posterior for $\gamma$ alone,

$$f(\gamma\mid\text{data}) \propto \gamma^{-n+1}\,\bigl|X^TX+\gamma^{-2}J\bigr|^{-1/2}\left(y^Ty - y^TX(X^TX+\gamma^{-2}J)^{-1}X^Ty\right)^{-\left(\frac n2 -1\right)},$$

and a conditional posterior for $\sigma$ given $\gamma$ that is (in terms of the precision
$1/\sigma^2$) a Gamma distribution:

$$\frac{1}{\sigma^2}\ \Big|\ \gamma,\text{data} \ \sim\ \mathrm{Gamma}\!\left(\frac n2 - 1,\ \frac{y^Ty - y^TX(X^TX+\gamma^{-2}J)^{-1}X^Ty}{2}\right).$$

## Sampling the full posterior

The point of the reparametrization is that the joint posterior now factors cleanly,

$$f(\beta,\sigma,\gamma\mid\text{data}) = f(\gamma\mid\text{data})\, f(\sigma\mid\gamma,\text{data})\, f(\beta\mid\sigma,\gamma,\text{data}),$$

and every factor on the right is now something that can be sampled directly rather than iteratively.
This gives a three-step recipe for drawing a posterior sample of the whole model:

1. Lay a grid over $\gamma$, evaluate $f(\gamma\mid\text{data})$ on it, and draw a sample of
   $\gamma$ from the resulting (grid-approximated) distribution.
2. Given that $\gamma$, draw $\sigma$ from its Gamma-based conditional.
3. Given $\gamma$ and $\sigma$ — and hence $\tau=\sigma\gamma$ — draw $\beta$ from the Gaussian
   posterior derived earlier.

Because each step draws exactly from the correct conditional distribution given what came before,
this is direct composition sampling, not an iterative chain: there is no burn-in and nothing to
check for convergence, unlike a Markov chain Monte Carlo scheme.

## From mean models to variance models

Every model examined up to this point — the spline above, and more generally any model of the form

$$\sum_{t=1}^n (y_t-\mu_t)^2 + \lambda\sum_{t=2}^{n-1}\Bigl((\mu_t-\mu_{t-1})-(\mu_{t-1}-\mu_{t-2})\Bigr)^2 \quad\text{or}\quad \lambda\sum_{t=2}^{n-1}\Bigl|(\mu_t-\mu_{t-1})-(\mu_{t-1}-\mu_{t-2})\Bigr|$$

— is a **mean model**: the data $y_t$ are modeled as independent $N(\mu_t,\sigma^2)$ with a fixed
noise variance, and the object being estimated is the mean sequence $\mu_1,\dots,\mu_n$, recovered
by trading off fit against smoothness. The two penalty forms shown are both on the discrete second
difference $(\mu_t-\mu_{t-1})-(\mu_{t-1}-\mu_{t-2})$ — the discrete analogue of curvature — squared
in one case and in absolute value in the other, mirroring the same ridge-versus-absolute-value
choice already seen for the spline coefficients above.

A **variance model** turns this around: the data $y_1,\dots,y_n$ are modeled as independent

$$y_t \sim N(0,\sigma_t^2), \qquad t=1,\dots,n,$$

with a fixed (here zero) mean, and it is the *variance* $\sigma_t^2$ that is allowed to change with
$t$ and is the object of interest. To model $\sigma_t$ as a free quantity without needing to enforce
positivity directly, write

$$\sigma_t = \exp(\alpha_t),$$

and work with $\alpha_t$ — a real-valued sequence, plotted against $t$ in the same way the mean
sequence $\mu_t$ would be — as the quantity to be estimated. This reframes a variance model as a
level-estimation problem for $\alpha_t$, and is where the lecture's material on spectral analysis
of variance begins; the notes end at this point of the introduction.

## Sources

All of this chapter comes from a single supplied source: the handwritten lecture notes for
Berkeley Stat 153, Fall 2025, Lecture Thirteen
(`docs/statistics/berkeley/stat153/fall-2025/HandwrittenNotesLectureThirteen153248Fall2025.md` in
the library repository, CC BY 4.0). No slide deck, transcript, or exercise set was supplied for
this lecture, so no `## Exercises` section is included.

The source file itself is flagged as a **model reconstruction** of a handwritten PDF with no text
layer: the prose is a paraphrase in places and every equation in it is marked unverified against
the original scan. This chapter follows that source's structure and formulas exactly — the spline
model and its priors, the ridge-regression identity, the marginal-likelihood argument for choosing
$\tau$ and $\sigma$, the $\gamma$-reparametrization, the sampling recipe, and the closing contrast
between mean models and variance models — without adding derivations, examples, or results beyond
what the notes contain. A reader who needs the equations checked should go back to the original PDF
linked in the source file's header. The notes also open mid-model (the spline construction is
presented without an introduction) and close mid-topic (variance models are only introduced, not
developed); both boundaries are inherited from the source rather than supplied here.

---

[← 69. Autoregression and Yule's AR(2)](69-autoregression-and-yule-s-ar-2.md) · [Contents](index.md) · [71. Bayesian Reasoning for Noisy Measurements →](71-bayesian-reasoning-for-noisy-measurements.md)
