---
title: "51. Bayesian Regularization and Variance Models"
course: "Berkeley Stat 153"
chapter: 51
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 51. Bayesian Regularization and Variance Models

## What this covers

This chapter follows STAT 153's high-dimensional regression machinery in two directions it is pushed
once ridge and LASSO are already available. First, it makes the choice of the ridge tuning parameter
$\lambda$ fully Bayesian, rather than picked by cross-validation, by putting a prior on $\lambda$ itself
and computing its posterior. Second, it asks what to do once a *single* unknown variance is not enough —
once the thing that needs to vary smoothly is the variance itself, either from one frequency to the next
(the **spectrum** of a time series) or from one time point to the next (**heteroscedasticity**). It assumes
the ridge/LASSO regularization and cross-validation from Lecture 11, the closed-form ridge estimator and
posterior from Lecture 12, and the sinusoidal regression model and RSS-based frequency estimation used on
the sunspots data in Lecture 8.

## The running example: a high-dimensional regression model

The recurring dataset is the monthly global temperature-anomaly series. To let the trend be as flexible
as the data demand, the model is a **piecewise-linear (broken-stick) regression** with a kink at every
time point:
$$
y_t = \beta_0 + \beta_1(t-1) + \beta_2(t-2)_+ + \cdots + \beta_{n-1}\big(t-(n-1)\big)_+ + \epsilon_t,
$$
where $(x)_+ = \max(x,0)$. Written as $y = X\beta + \epsilon$, the design matrix $X$ has one column of
ones, one column for the overall linear slope, and one column per kink location — as many columns as
there are data points, which is exactly the high-dimensional regime that forces regularization.

## Recap: ridge and cross-validation

The ridge estimator minimizes
$$
\|y - X\beta\|^2 + \lambda \sum_{j=2}^{n-1} \beta_j^2,
$$
penalizing every coefficient from $\beta_2$ onward but leaving the intercept $\beta_0$ and the overall
slope $\beta_1$ unpenalized — they describe the trend itself, not a deviation from it. Equivalently,
$\hat\beta_{\text{ridge}} = (X^TX + \lambda J)^{-1}X^Ty$ for the diagonal matrix $J$ with a $0$ in the
first two diagonal slots and a $1$ everywhere else. Small $\lambda$ lets the fit hug the data (overfitting);
large $\lambda$ flattens it toward a straight line (underfitting).

$\lambda$ was chosen by 5-fold cross-validation over a log-spaced grid from $10^{-2}$ to $10^{8}$. The
cross-validated error is U-shaped in $\log\lambda$, exactly as the bias–variance story predicts:

| $\lambda$ | $10^{-2}$ | $1$ | $10^{2}$ | $10^{3}$ | $10^{4}$ | $10^{6}$ | $10^{8}$ |
|---|---|---|---|---|---|---|---|
| CV error | 20.47 | 2.26 | 0.126 | **0.0446** | 0.0482 | 0.105 | 0.168 |

the minimum sits at $\hat\lambda_{\text{CV}} = 1000$. This is the benchmark the rest of the chapter's
Bayesian estimate of $\lambda$ is measured against.

## Making the prior fully Bayesian

Cross-validation treats $\lambda$ as a single number to be searched for. The Bayesian alternative treats
it as an unknown parameter with its own posterior distribution, computed from a prior rather than a grid
search over held-out error.

### The prior, and the posterior of $\beta$ given $(\tau,\sigma)$

Give the unpenalized coefficients a vague, symmetric prior and the penalized ones a Gaussian prior sharing
one unknown scale $\tau$:
$$
\beta_0,\beta_1 \overset{\text{i.i.d.}}{\sim} \text{unif}(-C,C), \qquad
\beta_2,\dots,\beta_{n-1} \overset{\text{i.i.d.}}{\sim} N(0,\tau^2),
$$
and treat both $\tau$ and the noise scale $\sigma$ as unknown, with $\log\tau,\log\sigma \overset{\text{i.i.d.}}{\sim}\text{unif}(-C,C)$.
Conditional on $(\tau,\sigma)$, the posterior of $\beta$ is Gaussian:
$$
\beta \mid \text{data},\sigma,\tau \sim N\!\left(\Big(\tfrac{X^TX}{\sigma^2}+Q^{-1}\Big)^{-1}\tfrac{X^Ty}{\sigma^2},\;
\Big(\tfrac{X^TX}{\sigma^2}+Q^{-1}\Big)^{-1}\right),
$$
where $Q = \text{diag}(C,C,\tau^2,\dots,\tau^2)$. This is exactly the ridge estimator in disguise — the
prior precision $Q^{-1}$ plays the role that $\lambda J$ plays in the frequentist formula — with the
tuning parameter now identified as $\lambda = \sigma^2/\tau^2$.

The joint posterior of the hyperparameters $(\tau,\sigma)$ is
$$
f_{\tau,\sigma\mid\text{data}}(\tau,\sigma) \;\propto\;
\frac{\sigma^{-n-1}\tau^{-1}}{\sqrt{\det Q}}\sqrt{\det\Big(\tfrac{X^TX}{\sigma^2}+Q^{-1}\Big)^{-1}}\,
\exp\!\Big(-\tfrac{y^Ty}{2\sigma^2}\Big)
\exp\!\Big(\tfrac{y^TX}{2\sigma^2}\Big(\tfrac{X^TX}{\sigma^2}+Q^{-1}\Big)^{-1}\tfrac{X^Ty}{\sigma^2}\Big).
$$
This still depends on the bound $C$ through $Q$ — but only in a way that disappears as $C\to\infty$.
Write $J$ for the same $0/0/1/\dots/1$ diagonal matrix as before. As $C\to\infty$,
$$
Q^{-1} = \text{diag}(1/C,1/C,1/\tau^2,\dots,1/\tau^2) \;\longrightarrow\; \text{diag}(0,0,1/\tau^2,\dots,1/\tau^2) = J/\tau^2,
$$
and $\det Q = C^2\tau^{2(n-2)}$, whose factor of $C^2$ is common to every value of $(\tau,\sigma)$ and
cancels once the posterior is normalized. So the vague bound $C$ never has to be chosen numerically; the
"unpenalize the first two coordinates" convention from the ridge code re-appears here as a limit of the
prior. Substituting gives the simplified posterior that the code actually evaluates:
$$
f_{\tau,\sigma\mid\text{data}}(\tau,\sigma) \;\propto\;
\sigma^{-n-1}\tau^{-n+1}\sqrt{\det\Big(\tfrac{X^TX}{\sigma^2}+\tfrac{J}{\tau^2}\Big)^{-1}}\,
\exp\!\Big(-\tfrac{y^Ty}{2\sigma^2}\Big)
\exp\!\Big(\tfrac{y^TX}{2\sigma^2}\Big(\tfrac{X^TX}{\sigma^2}+\tfrac{J}{\tau^2}\Big)^{-1}\tfrac{X^Ty}{\sigma^2}\Big).
$$

### The posterior of $(\tau,\sigma)$, and how the code samples from it

The determinant in this expression rules out a closed-form normalizing constant, so the posterior is
approximated numerically: evaluate its logarithm on a $100\times 100$ grid of $(\tau,\sigma)$ pairs
(log-spaced, $\tau\in[10^{-4},1]$, $\sigma\in[0.1,1]$), re-centre by subtracting the maximum for numerical
stability, exponentiate, and normalize so the grid weights sum to one. This turns the messy density into
a discrete distribution over the grid that can be sampled directly.

Posterior draws of the *whole* parameter vector $(\beta,\tau,\sigma)$ are then produced in two steps —
draw the hyperparameters first, then the parameters given them — which is valid because the joint
posterior factors as $p(\beta,\tau,\sigma\mid\text{data}) = p(\beta\mid\text{data},\tau,\sigma)\,p(\tau,\sigma\mid\text{data})$:

1. Resample $N=1000$ pairs $(\tau,\sigma)$ from the grid, with probability equal to the normalized
   weights just computed.
2. For each drawn $(\tau,\sigma)$, draw $\beta$ from its exact Gaussian conditional posterior above.

Averaging the resulting fitted curves $X\hat\beta$ over all $N$ draws gives the **posterior mean fit**,
which tracks the temperature-anomaly data closely; plotting all $N$ individual fitted curves alongside it
shows the spread of plausible curves the data leave open — something a single cross-validated ridge fit
does not report. Summarizing the $\tau$ and $\sigma$ draws themselves gives posterior means of roughly
$\bar\tau \approx 0.0024$ and $\bar\sigma \approx 0.173$ for this dataset.

## A second parametrization: $\gamma$ instead of $\tau$, and back to $\lambda$

Re-parametrize the same prior in terms of $\gamma := \tau/\sigma$ instead of $\tau$ directly:
$$
\beta_2,\dots,\beta_{n-1} \overset{\text{i.i.d.}}{\sim} N(0,\gamma^2\sigma^2), \qquad
\log\gamma,\log\sigma \overset{\text{i.i.d.}}{\sim} \text{unif}(-C,C).
$$
This looks like relabeling, but it is genuinely a **different prior**: under the first model $\tau$ and
$\sigma$ were assigned independent log-uniform priors, but here $\tau = \gamma\sigma$ is now a *dependent*
function of two independent log-uniform variables, so the induced prior on $\tau$ is no longer independent
of $\sigma$.

The payoff is that the conditional posterior of $\sigma$ given $\gamma$ is now available in closed form —
no grid needed for that dimension:
$$
\frac{1}{\sigma^2}\Bigm| \text{data},\gamma \;\sim\; \text{Gamma}\!\left(\frac{n}{2}-1,\;
\frac{y^Ty - y^TX(X^TX+\gamma^{-2}J)^{-1}X^Ty}{2}\right),
$$
and the marginal posterior of $\gamma$ alone is
$$
f_{\gamma\mid\text{data}}(\gamma) \;\propto\; \gamma^{-n+1}\sqrt{\det(X^TX+\gamma^{-2}J)^{-1}}\,
\Big(y^Ty - y^TX(X^TX+\gamma^{-2}J)^{-1}X^Ty\Big)^{-(n/2-1)}.
$$
Only $\gamma$ needs to be gridded — a 1-D grid rather than the earlier 2-D grid over $(\tau,\sigma)$ — and
$\sigma$ and $\beta$ can then be drawn exactly, conditionally, without approximation.

This parametrization also reconnects to $\lambda$ directly: since $\lambda = \sigma^2/\tau^2$ and
$\tau=\gamma\sigma$, $\lambda = 1/\gamma^2$, i.e. $\gamma = 1/\sqrt{\lambda}$. Computing the posterior mean
over a grid of $10^3$ values of $\gamma$ from $10^{-6}$ to $10^4$ gives $\bar\gamma \approx 0.01388$, hence
a Bayesian point estimate $\hat\lambda = 1/\bar\gamma^2 \approx 5190$. Both this figure and the earlier
cross-validated $\hat\lambda_{\text{CV}} = 1000$ land in the same broad range (hundreds to thousands) but
do not agree exactly — a reminder that cross-validation and a fully Bayesian treatment are two different
principled ways of answering the same question, not two routes to the same number. From the $\gamma$ draws
one also gets a histogram of implied $\lambda = 1/\gamma^2$ values directly, i.e. a full posterior over the
tuning parameter rather than one chosen point.

## Beyond a single shared variance

Both priors above still share **one** unknown scale ($\tau^2$, or $\gamma^2\sigma^2$) across every
regularized coefficient. The rest of the chapter asks what happens once that scale is itself allowed to
vary smoothly — across time, or across frequency — instead of being one shared number. As a first,
deliberately simple illustration of the idea, consider data with no regression structure at all, just
independent, mean-zero, unequal variances:
$$
y_t \overset{\text{independent}}{\sim} N(0,\tau_t^2), \qquad t=1,\dots,n,
$$
where $\tau_1,\dots,\tau_n$ are assumed to vary smoothly in $t$. (Estimating them is left for a later
lecture; here the point is only to see what such data look like.)

## Variance that changes over time: heteroscedasticity

Two simulations illustrate the model. In the first, $\tau_t = \sqrt{1+\theta^2+2\theta\cos(2\pi t/n)}$
with $\theta=-0.8$ traces out one smooth cycle of variance across the whole series. In the second, a
genuinely wiggly function
$$
\alpha_t = \sin(15x) + e^{-x^2/2} + 0.5(x-0.5)^2 + 2\log(x+0.1), \qquad x = t/n \in [0,1],
$$
defines $\tau_t = e^{\alpha_t}$, and $y_t \sim N(0,\tau_t^2)$ independently as before. Both simulations
share two features, which are exactly what the model was built to produce:

1. the data oscillate around zero, with clusters of small values where $\tau_t$ is small and bursts of
   large values where $\tau_t$ is large;
2. because $\log\tau_t = \alpha_t$ is smooth, the standard deviation changes *gradually* rather than
   abruptly — periods of calm and periods of volatility, but with slow transitions between them, rather
   than a sudden jump.

Nothing here is autocorrelated: each $y_t$ is drawn independently of its neighbors. What is smooth is only
the instantaneous variance, not the value itself.

### A real instance: S&P 500 daily returns

Real data with exactly this texture exist, particularly in finance. Downloading S&P 500 closing prices
from 2000–2024 and converting to percentage log-returns,
$$
y_t = 100\big(\log P_t - \log P_{t-1}\big),
$$
produces a series that visibly shares both features above: it oscillates around zero, and it alternates
between calm stretches and bursts of large swings (volatility clustering) with the same gradual, rather
than abrupt, transitions between them. Estimating $\tau_t$ from data like this — the natural next
question — is left to the following lecture.

## Why a handful of sinusoids cannot fit the sunspots cycle

The same idea — replace one number by a smoothly varying profile — is what eventually fixes a long-standing
gap in the sunspots model. Recall the sinusoidal regression fit to the sunspots counts,
$$
y_t = \beta_0 + \sum_{j=1}^k \big(\beta_{1j}\cos(2\pi f_j t) + \beta_{2j}\sin(2\pi f_j t)\big) + \epsilon_t,
$$
with $(\beta, f, \sigma)$ estimated by minimizing the residual sum of squares over $f$. For $k=1$, the RSS
is minimized at $\hat f \approx 1/11$, correctly recovering the famous 11-year solar cycle.

But the raw data show more structure than a single fixed period can capture: the peaks of the series are
not evenly spaced. Finding the peaks directly and measuring the gaps between them gives values mostly
around 11 but ranging from as small as 8 up to 14 (occasional gaps of 2 are attributed to noise rather
than genuine short cycles). A model with one exact, constant period cannot reproduce that variability. The
mismatch is visible directly: simulate several synthetic datasets from the fitted single-sinusoid model
(same $\hat f,\hat\beta,\hat\sigma$, fresh Gaussian noise), plot them in a grid alongside the real sunspots
series, and the real data is easy to spot as the odd one out — the simulated series are too wiggly and lack
the sharply defined peaks of the original.

Adding more sinusoids at fixed, previously estimated frequencies helps only a little. With two components
($f_1=0.0908$, $f_2=0.0099$) the residual scale drops from $\hat\sigma\approx 51.6$ to $\approx 48.3$; with
three ($f_1=0.0907$, $f_2=0.01$, $f_3=0.0998$) it drops further to $\approx 42.8$. The fits get visually
closer, but simulated data from even the three-sinusoid model is still noticeably more wiggly, without
clearly defined peaks, than the real series. A small number of exact frequencies with fixed amplitudes is
the wrong kind of object for this data, no matter how many are added.

## Regularizing all the Fourier frequencies at once

The natural next attempt is to stop choosing which frequencies to include and instead include **all** of
them — every Fourier frequency $j/n$ for $j=1,\dots,m=(n-1)/2$ — and let regularization decide which
matter:
$$
y_t = \beta_0 + \sum_{j=1}^m \big(\beta_{1j}\cos(2\pi (j/n) t) + \beta_{2j}\sin(2\pi (j/n) t)\big) + \epsilon_t.
$$
For the sunspots series $n=325$ (odd), so this model has as many coefficients as data points: the
unregularized fit ($\lambda=0$) interpolates the data exactly, which is exactly the high-dimensional
regime ridge and LASSO were built for. Only the intercept $\beta_0$ is left unpenalized this time (there
is no separate linear-trend term to protect, unlike the temperature-anomaly model).

Ridge regularization ($\lambda=200$) shrinks the huge unregularized coefficients toward zero and produces
a fitted curve that closely tracks the data, shrunk toward the overall mean — visually reasonable, but with
no obvious interpretation, and data simulated from it (with $\hat\sigma\approx 34.1$) is still distinguishable
from the real sunspots series in the same odd-one-out comparison. LASSO regularization ($\lambda=2000$)
instead sets most of the coefficients to exactly zero — comparing the LASSO coefficients to the
unregularized ones shows the small coefficients disappearing entirely, leaving effectively a handful of
active frequencies. The resulting fit looks similar to the three-sinusoid fit above, for the same reason:
LASSO is implicitly *selecting* a small set of frequencies, just automatically. Data simulated from it
(with $\hat\sigma\approx 33.5$) is, unsurprisingly, still wiggly and without well-defined peaks — the same
qualitative failure as before. Regularization changes *how many* frequencies are active or *how much* they
are shrunk, but as long as each active frequency still gets one fixed amplitude, the irregular timing of
the real peaks is out of reach.

## The spectrum model

The fix is to stop trying to pin down the amplitude at each frequency and instead give every frequency's
amplitude a **distribution**. Drop the noise term and write
$$
y_t = \beta_0 + \sum_{j=1}^m \big(\beta_{1j}\cos(2\pi (j/n)t) + \beta_{2j}\sin(2\pi(j/n)t)\big),
\qquad \beta_{1j},\beta_{2j} \overset{\text{i.i.d.}}{\sim} N(0,\tau_j^2).
$$
The sequence $\tau_1^2,\dots,\tau_m^2$ is the **spectrum** of the model: $\tau_j^2$ measures how much the
frequency $j/n$ contributes to the overall variability of $y_t$ — large where that frequency is important,
near zero where it is not. Because the sinusoidal basis functions are orthogonal, the total variance
decomposes additively across frequencies,
$$
\text{var}(y_t) = \sum_{j=1}^m \tau_j^2,
$$
so the spectrum literally is a description of how the variance of the series is distributed across
frequencies — a **spectral representation** of the time series. Nothing about a specific $\beta_{1j},\beta_{2j}$
pair is fixed any more; instead each simulated draw of the coefficients from these Gaussians produces a
*different* realization with the same overall spectral shape, which is exactly the freedom needed to let
peak spacing vary from cycle to cycle while the dominant period stays roughly fixed.

Four choices of spectrum illustrate this.

**Example one.** Let $\tau_j^2$ be constant for $j/n$ between $1/13$ and $1/9$, and zero elsewhere — all
the variance concentrated in a narrow band around the solar cycle. The simulated series looks smooth, with
well-defined peaks; measuring the gaps between them gives values "reminiscent of the sunspots dataset,"
i.e. clustered but not identical. Fitting a single sinusoid by RSS to this *simulated* data (the same
procedure used on the real data) gives $\widehat{1/f} \approx 9.6$ — close to, but not exactly, the true
band, since a single point estimate is a coarse summary of variance spread over a whole band of frequencies
rather than concentrated at one point.

**Example two.** Split the same total variance across two disjoint bands, one near $1/13$–$1/9$ and one
near $1/25$–$1/22$. The resulting simulated data looks visually more like the real sunspots series than
example one, and the peak spacing again varies across the series, matching what the real data shows.

**Example three.** Instead of a flat band, let $\tau_j^2$ decay (or grow) smoothly across frequency using
$$
\tau_j = \sqrt{1+\theta^2 + 2\theta\cos(2\pi (j/n))}, \qquad \theta = -0.8,
$$
which is the *same* formula, with the *same* value of $\theta$, used earlier for the smoothly time-varying
$\tau_t$ in the heteroscedasticity simulation — only there the index was time, and here it is frequency.
That coincidence is a genuine feature of the model, not just of the example: a smoothly changing profile
is the object of interest whether it sits over time or over frequency, and the same functional shape can
illustrate either.

**Example four.** Concentrate $\tau_j^2$ in a narrow peak centered at $j/n \approx 1/11$ that drops off
quickly on either side — a sharper, more localized version of example one's flat band, still tied directly
to the known 11-year period.

<figure>
<svg viewBox="0 0 380 220" role="img" aria-label="Two example spectra, a flat band and a narrow peak, both concentrated near the 1/11 sunspot frequency">
  <line x1="40" y1="180" x2="340" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <rect x="86" y="140" width="21" height="40" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2"/>
  <path d="M80,180 C85,180 90,65 94.5,60 C99,65 105,180 110,180 Z" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
  <line x1="94.5" y1="180" x2="94.5" y2="186" stroke="currentColor" stroke-width="1"/>
  <text x="94.5" y="199" text-anchor="middle" font-size="11" fill="currentColor">1/11</text>
  <text x="40" y="199" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="340" y="199" text-anchor="middle" font-size="11" fill="currentColor">0.5</text>
  <text x="190" y="213" text-anchor="middle" font-size="12" fill="currentColor">frequency f = j/n</text>
  <text x="46" y="55" font-size="12" fill="currentColor">τⱼ²</text>
  <rect x="210" y="25" width="14" height="10" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="228" y="34" font-size="11" fill="currentColor">flat band (Example 1)</text>
  <path d="M210,58 h14" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
  <text x="228" y="61" font-size="11" fill="currentColor">peak (Example 4)</text>
</svg>
<figcaption>Two of the four example spectra: a flat band and a sharper peak, both putting nearly all the
variance of the simulated series into frequencies close to the known 1/11 solar-cycle frequency. A single
fixed-amplitude sinusoid puts all the variance at one exact point instead — the spectrum model spreads it
over a shape, which is what lets simulated peak spacing vary the way the real sunspots data's does.</figcaption>
</figure>

Estimating an unknown spectrum from data — rather than fixing it by hand, as in these four illustrations —
is the natural next question, and is left for a later lecture (the sunspots material points ahead to
"estimating the spectrum by smoothing the periodogram").

## Sources

**Berkeley STAT 153, "Lecture Thirteen" code notebooks**, two offerings, both CC BY 4.0, converted
losslessly from Jupyter notebooks (so section titles below are the notebook's own markdown headings):

- Fall 2025 (`CodeLectureThirteen153248Fall2025.ipynb`): `01-introduction.md` (the piecewise-linear
  high-dimensional model on the temperature-anomaly data); `02-quick-recap-ridge-regularization-lecture-11.md`
  (ridge estimator and 5-fold cross-validation, quoting the closed-form estimator "derived in Lecture 12");
  `03-bayesian-regularization-from-lecture-12.md` (the $(\tau,\sigma)$ prior, its posterior, and grid/resampling
  computation); `04-bayesian-regularization-with-a-slightly-different-prior.md` (the $(\gamma,\sigma)$
  reparametrization, the link to $\lambda$, and the transition into "Variance Models" with Simulation 1);
  `05-simulation-2.md` (the second heteroscedasticity simulation and its two stated features);
  `06-a-real-dataset-from-finance-for-which-this-variance-model-is.md` (the S&P 500 example).
- Spring 2025 (`CodeLectureThirteen153248Spring2025.ipynb`): `02-sunspots-dataset.md` (peak-gap analysis
  and the one/two/three-sinusoid RSS fits, building on the frequency-estimation method used in Lecture 8);
  `03-ridge-and-lasso-regression-with-sinusoids.md` (ridge and LASSO on the full set of Fourier frequencies);
  `04-the-spectrum-model.md` (the spectrum model and its four worked examples).

Lectures 8, 11 and 12 are referred to throughout (for the sunspots frequency-estimation method, the ridge
estimator, and its closed-form Bayesian posterior respectively) but were not among the material supplied
for this chapter. The estimation of an unknown spectrum by periodogram smoothing, and the estimation of a
time-varying $\tau_t$ from data such as the S&P 500 returns, are both explicitly deferred to later lectures
not included here. No slides, transcript, or exercises were supplied for this chapter; all of it is drawn
from the notebooks' own markdown and code-cell commentary.

---

[← 50. Broken-Stick Regression and Regularization](50-broken-stick-regression-and-regularization.md) · [Contents](index.md) · [52. Trend and Seasonal Regression →](52-trend-and-seasonal-regression.md)
