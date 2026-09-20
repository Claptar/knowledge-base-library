---
title: "72. Ridge Regression as Bayesian Inference"
course: "Berkeley Stat 153 Fall 2024"
chapter: 72
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 72. Ridge Regression as Bayesian Inference

## What this covers

This chapter asks why the ridge penalty on a high-dimensional regression should be trusted, beyond
being an ad hoc fix for overfitting, and how the tuning parameter $\lambda$ might be chosen by
something other than cross-validation. It assumes the piecewise-linear trend model, the
least-squares overfitting problem, and the ridge/LASSO penalties already set up in the previous
lecture; the payoff is a second, Bayesian route to exactly the ridge estimator, and a fully
data-driven way to pick $\lambda$.

## The model, and why least squares overfits

Recall the trend model built from a level, a slope, and a hinge (ReLU) term at every interior time
point:

$$y_t = \beta_0 + \beta_1(t-1) + \beta_2\,\text{ReLU}(t-2) + \dots + \beta_{n-1}\,\text{ReLU}(t-(n-1)) + \varepsilon_t, \qquad t=1,\dots,n.$$

With $n$ data points and $n$ free parameters $\beta_0,\dots,\beta_{n-1}$, this is high-dimensional
linear regression, $y = X\beta+\varepsilon$, with

$$X = \begin{bmatrix} 1&0&0&\dots&0\\ 1&1&0&\dots&0\\ 1&2&1&\dots&0\\ \vdots&\vdots&\vdots&\ddots&\vdots\\ 1&n-1&n-2&\dots&1 \end{bmatrix}.$$

$\beta_0$ is the level and $\beta_1$ the initial slope; each later $\beta_j$ multiplies a hinge
term, so it controls how sharply the fitted trend kinks at time $j$. With as many parameters as
observations, ordinary least squares has exactly enough freedom to reproduce the data:

$$\hat\beta = (X^TX)^{-1}X^Ty, \qquad X\hat\beta = y.$$

Fitted values equal the data — the signature of overfitting.

## Ridge and LASSO, and why penalize only the hinges

Two standard fixes add a penalty on the size of the hinge coefficients only, leaving the level and
slope $\beta_0,\beta_1$ unpenalized so the fit can still follow an arbitrary line:

$$\text{Ridge: } \|y-X\beta\|^2 + \lambda\sum_{j=2}^{n-1}\beta_j^2, \qquad \text{LASSO: } \|y-X\beta\|^2 + \lambda\sum_{j=2}^{n-1}|\beta_j|.$$

The lecture gives two reasons to regularize: wanting a smoother fit without overfitting is
described as "our preference," but the second reason — that regularizing also improves
out-of-sample prediction — is what makes $\lambda$ worth choosing carefully, e.g. by cross-validation.

### Deriving the ridge estimator

Write the penalized objective and minimize over $\beta$. Let $J$ be the diagonal 0/1 matrix that
picks out exactly the penalized coordinates ($J_{jj}=0$ for $j=0,1$ and $J_{jj}=1$ for
$j=2,\dots,n-1$), so the penalty is $\lambda\beta^TJ\beta$. Then

$$\nabla_\beta\Big[\beta^TX^TX\beta - 2\beta^TX^Ty + y^Ty + \lambda\beta^TJ\beta\Big] = 2X^TX\beta - 2X^Ty + 2\lambda J\beta = 0,$$

so the normal equations become $(X^TX+\lambda J)\beta = X^Ty$, giving

$$\hat\beta^{\text{Ridge}}(\lambda) = (X^TX+\lambda J)^{-1}X^Ty,$$

which reduces to the unregularized least-squares estimator at $\lambda=0$.

That is a purely algebraic fix. The rest of the lecture asks whether there is a genuine probability
model over $\beta$ under which this formula falls out as something other than an imposed penalty.

## Setting up a Bayesian version of the same regression

Keep the same likelihood, $\varepsilon_t\overset{\text{iid}}\sim N(0,\sigma^2)$, so

$$f_{\text{data}\mid\beta,\sigma}(\text{data}) = \left(\frac{1}{\sqrt{2\pi}\,\sigma}\right)^n\exp\left\{-\frac{\|y-X\beta\|^2}{2\sigma^2}\right\},$$

but now also put a prior distribution on $\beta$ (and, later, on $\sigma$ itself). The question in
each case is: what is the posterior mean of $\beta$ given the data, and does it match one of the two
point estimates above?

## A flat prior reproduces least squares

Take $\beta_0,\dots,\beta_{n-1}\overset{\text{iid}}\sim\text{Unif}(-C,C)$ and let $C\to\infty$ — a
prior that says nothing at all about where $\beta$ should lie. As $C\to\infty$ the posterior
converges to

$$\beta\mid\text{data},\sigma \;\sim\; N\Big((X^TX)^{-1}X^Ty,\ \sigma^2(X^TX)^{-1}\Big),$$

an $n$-variate normal centered exactly at the least-squares estimate (left as an exercise below,
where the lecture also leaves it).

The same conclusion follows from a different, easier-to-integrate prior:
$\beta_0,\dots,\beta_{n-1}\overset{\text{iid}}\sim N(0,C)$ with $C$ large. Over any bounded range of
$\beta_j$, the density $\frac{1}{\sqrt{2\pi C}}\exp(-\beta_j^2/2C)$ barely changes, so a
large-variance Gaussian behaves like a constant — like a flat prior — and is "very similar" to
$\text{Unif}(-C,C)$ for most values of $\beta_j$. Working out the exact posterior for *any* $C$ (not
only large $C$) gives the standard Bayesian-linear-regression formula

$$\beta\mid\text{data},\sigma \;\sim\; N\left(\left(\frac{X^TX}{\sigma^2}+\frac{I}{C}\right)^{-1}\frac{X^Ty}{\sigma^2},\ \left(\frac{X^TX}{\sigma^2}+\frac{I}{C}\right)^{-1}\right),$$

and letting $C\to\infty$ removes the $I/C$ term and recovers exactly the uniform-prior posterior
above. For example, with $C=10^{10}$, over the range where $\beta_j$'s posterior mass actually sits
— say $\beta_j\in(-10,10)$ — $\text{Unif}(-C,C)$ and $N(0,C)$ put essentially the same, essentially
flat, density.

Conclusion: with no real prior information — flat over a wide range, whether uniform or Gaussian —
the Bayesian posterior mean coincides with the frequentist unregularized least-squares estimator.

## A tight prior on the hinge terms reproduces ridge

Now use a general zero-mean Gaussian prior, $\beta\sim N(0,Q)$ for a (here diagonal) covariance
matrix $Q$. Repeating the same computation gives the posterior

$$\beta\mid\text{data},\sigma \;\sim\; N\left(\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\frac{X^Ty}{\sigma^2},\ \left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\right).$$

Choose $Q$ to mirror the ridge split exactly: give the level and slope a flat, large-variance prior
(so they are not shrunk), and give every hinge coefficient a *tight* zero-mean prior with a small
shared variance $\tau^2$:

$$\beta_0,\beta_1\overset{\text{iid}}\sim N(0,C), \ C \text{ large}, \qquad \beta_j\overset{\text{iid}}\sim N(0,\tau^2), \ j=2,\dots,n-1,\ \tau \text{ small}.$$

Then $Q^{-1}=\text{diag}(1/C,\,1/C,\,1/\tau^2,\dots,1/\tau^2)$, and since $C$ is large, $1/C\approx0$:

$$Q^{-1}\approx \text{diag}(0,0,1/\tau^2,\dots,1/\tau^2) = \frac{1}{\tau^2}J,$$

exactly the same 0/1 matrix $J$ that picked out the penalized coordinates in the ridge derivation.
Substituting into the posterior mean,

$$\left(\frac{X^TX}{\sigma^2}+\frac{1}{\tau^2}J\right)^{-1}\frac{X^Ty}{\sigma^2} = \left(X^TX+\frac{\sigma^2}{\tau^2}J\right)^{-1}X^Ty,$$

which is exactly $\hat\beta^{\text{Ridge}}(\lambda)$ with

$$\lambda = \frac{\sigma^2}{\tau^2}.$$

So: **frequentist ridge regression is the posterior mean of a Bayesian model in which the level and
slope have an uninformative prior and the hinge coefficients share a tight, zero-mean Gaussian
prior** — a large $\lambda$ corresponds to a small $\tau$, i.e. a strong prior belief that the trend
has few, small kinks.

This prior is restrictive in one respect: $\tau$ (equivalently $\lambda$) still has to be fixed by
hand before seeing the data, exactly as $\lambda$ had to be chosen by hand or by cross-validation on
the frequentist side.

## Letting the data set the scale: a hierarchical prior

The natural next step is to stop fixing $\tau$ and $\sigma$ and instead put a prior on them too, so
the posterior determines them from the data. Keep the same conditional structure —
$\beta_0,\beta_1\sim N(0,C)$ with $C$ large, $\beta_j\sim N(0,\tau^2)$ for $j\ge2$, i.e.
$\beta\sim N(0,Q)$ — but now also put flat priors on $\log\tau$ and $\log\sigma$, the standard
non-informative choice for a positive scale parameter:

$$\log\tau\sim\text{Unif}(-C,C), \qquad \log\sigma\sim\text{Unif}(-C,C).$$

The joint prior density is

$$f_{\beta,\sigma,\tau}(\beta,\sigma,\tau) \propto \frac{1}{\sqrt{\det Q}}\exp\left(-\frac{\beta^TQ^{-1}\beta}{2}\right)\cdot\frac{1}{\tau}I\{-C<\log\tau<C\}\cdot\frac1\sigma I\{-C<\log\sigma<C\},$$

and with the Gaussian likelihood $f_{\text{data}\mid\beta,\sigma}\propto\sigma^{-n}\exp(-\|y-X\beta\|^2/2\sigma^2)$,
the joint posterior of $(\beta,\tau,\sigma)$ is

$$f_{\beta,\tau,\sigma\mid\text{data}} \;\propto\; \frac{\sigma^{-n-1}\tau^{-1}}{\sqrt{\det Q}}\exp\left\{-\frac12\left(\frac{\|y-X\beta\|^2}{\sigma^2}+\beta^TQ^{-1}\beta\right)\right\}.$$

### Integrating $\beta$ out

For fixed $\sigma,\tau$, the exponent is quadratic in $\beta$, so it completes to a square — the
same trick as $x^2-4x+6=(x-2)^2+2$ for a scalar:

$$\frac{\|y-X\beta\|^2}{\sigma^2}+\beta^TQ^{-1}\beta = (\beta-b)^T\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)(\beta-b) + \left[\frac{y^Ty}{\sigma^2} - b^T\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)b\right],$$

$$b = \left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\frac{X^Ty}{\sigma^2},$$

exactly the posterior mean of $\beta$ given $(\sigma,\tau)$ computed above. The first term, as a
function of $\beta$, integrates to a Gaussian normalizing constant; what remains is the marginal
posterior of $(\sigma,\tau)$ alone:

$$f_{\sigma,\tau\mid\text{data}}(\sigma,\tau) \;\propto\; \frac{\sigma^{-n-1}\tau^{-1}}{\sqrt{\det Q}}\left[\det\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\right]^{1/2}\exp\left(-\frac{y^Ty}{2\sigma^2}\right)\exp\left\{\frac{y^TX}{2\sigma^2}\left(\frac{X^TX}{\sigma^2}+Q^{-1}\right)^{-1}\frac{X^Ty}{\sigma^2}\right\}.$$

### The resulting procedure

<figure>
<svg viewBox="0 0 680 160" role="img" aria-label="A four-step procedure moving from a grid of noise and prior-scale values to a sampled beta.">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="10" y="50" width="140" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="80" y="75" text-anchor="middle" font-size="12" fill="currentColor">grid of</text>
  <text x="80" y="91" text-anchor="middle" font-size="12" fill="currentColor">(σ, τ) values</text>

  <line x1="150" y1="80" x2="188" y2="80" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>

  <rect x="190" y="40" width="160" height="80" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="270" y="65" text-anchor="middle" font-size="12" fill="currentColor">weigh each point</text>
  <text x="270" y="81" text-anchor="middle" font-size="12" fill="currentColor">by</text>
  <text x="270" y="97" text-anchor="middle" font-size="12" fill="currentColor">f(σ,τ ∣ data)</text>

  <line x1="350" y1="80" x2="388" y2="80" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>

  <rect x="390" y="50" width="140" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="460" y="75" text-anchor="middle" font-size="12" fill="currentColor">mean/mode, or</text>
  <text x="460" y="91" text-anchor="middle" font-size="12" fill="currentColor">a sampled (σ, τ)</text>

  <line x1="530" y1="80" x2="568" y2="80" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>

  <rect x="570" y="50" width="100" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="620" y="75" text-anchor="middle" font-size="12" fill="currentColor">sample β from</text>
  <text x="620" y="91" text-anchor="middle" font-size="12" fill="currentColor">N(b, ·)</text>
</svg>
<figcaption>The grid procedure: lay a grid of (σ, τ), weigh each point by its marginal posterior
density, take a summary (or a draw) of (σ, τ), then draw β from its Gaussian posterior conditional
on that (σ, τ). This is the fully Bayesian counterpart to choosing λ by cross-validation.</figcaption>
</figure>

Concretely: (1) lay a grid of candidate $(\sigma,\tau)$ pairs; (2) evaluate
$f_{\sigma,\tau\mid\text{data}}$ at every grid point; (3) take the posterior mean or mode of
$(\sigma,\tau)$ over the grid, or sample $(\sigma,\tau)$ from it; (4) sample $\beta$ from its normal
posterior given the data and that $(\sigma,\tau)$. Where the frequentist route chooses $\lambda$ by
splitting the data and minimizing held-out MSE over a grid of $\lambda$, this route places a grid
over $(\sigma,\tau)$ — equivalently over $\lambda=\sigma^2/\tau^2$ — and weighs each grid point by
how probable it is given the *whole* data set.

## Why the hierarchical model does not just overfit again

Something has to explain why this route avoids the overfitting that ordinary least squares fell
into, since it is built on the same $n$-parameter model. The failure case would be maximizing the
joint likelihood over $\beta$ and $\sigma$ directly: that likelihood is maximized by the
unregularized least-squares $\hat\beta$ (fitted values equal to the data) together with
$\hat\sigma=0$ — the same degenerate answer as before.

The hierarchical model never does that. It works instead with

$$f_{\text{data}\mid\tau,\sigma} = \int f_{\text{data}\mid\beta,\sigma}(\text{data})\, f_{\beta\mid\tau}(\beta)\, d\beta,$$

the likelihood *averaged over* $\beta$ under its prior, rather than maximized over $\beta$, and only
then combines it with the hyperprior, $f_{\tau,\sigma\mid\text{data}}\propto f_{\text{data}\mid\tau,\sigma}\,f_{\tau,\sigma}$.
A value of $\tau$ large enough to let $\beta$ wiggle freely enough to reproduce the data exactly
spreads its prior mass over an enormous range of $\beta$ values, most of which fit the data badly;
averaging over all of them, rather than reporting only the best one, pulls this marginal likelihood
back down. It is exactly this averaging step — present in $f_{\text{data}\mid\tau,\sigma}$ and
absent from a plain joint maximization over $(\beta,\sigma)$ — that keeps the hierarchical posterior
from being dragged to the degenerate, zero-noise, perfect-interpolation answer.

## Exercises

1. Under the prior $\beta_j\overset{\text{iid}}\sim\text{Unif}(-C,C)$, $j=0,\dots,n-1$, show that as
   $C\to\infty$ the posterior of $\beta$ given the data and $\sigma$ converges to
   $N\big((X^TX)^{-1}X^Ty,\ \sigma^2(X^TX)^{-1}\big)$.

## Sources

Berkeley STAT 153 (fall 2025), Lecture Twelve handwritten notes, reconstructed by a model from a
handwritten PDF with no text layer (fidelity: reconstructed; the source itself flags every equation
as unverified against the original scan):

- Model recap and the ridge-estimator derivation — `01-model.md`.
- The Bayesian setup, the likelihood, and the uniform- and Gaussian-flat-prior cases —
  `02-bayesian-regularization.md`.
- The ridge-reproducing prior, the hierarchical prior on $(\tau,\sigma)$, the completing-the-square
  marginalization, the grid procedure, and the overfitting argument — `03-summarize.md`.

The exercise above is the derivation the source notes mark "Homework" without working it, in
`02-bayesian-regularization.md`. No slides, transcript, or separate problem set were supplied for
this lecture. The cross-validation procedure for choosing $\lambda$, referred to here only for
contrast, belongs to the preceding lecture and is not reproduced in this chapter.

---

[← 71. Bayesian Reasoning for Noisy Measurements](71-bayesian-reasoning-for-noisy-measurements.md) · [Contents](index.md) · [73. Stationary MA and AR Processes →](73-stationary-ma-and-ar-processes.md)
