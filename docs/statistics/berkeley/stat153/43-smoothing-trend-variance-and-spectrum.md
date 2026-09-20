---
title: "43. Smoothing Trend, Variance, and Spectrum"
course: "Berkeley Stat 153 Fall 2024"
chapter: 43
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 43. Smoothing Trend, Variance, and Spectrum

## What this covers

This chapter covers three models for extracting a smoothly-varying signal from noisy data: a
smoothly drifting **mean** (Model 1), a smoothly drifting **variance** (Model 2), and a smoothly
varying **spectral density** (Model 3, the "spectrum model"). All three are special cases of one
recipe — reparametrize so the quantity of interest is unconstrained, write its negative
log-likelihood, and penalize the discrete second differences of the reparametrized sequence, either
by their sum of squares (a ridge-type penalty) or their sum of absolute values (a lasso-type
penalty) — solved directly as a convex optimization rather than through an explicit design matrix.
It assumes the ridge/lasso trend-filtering material from previous lectures (in particular the
truncated-power-basis representation of a piecewise-linear trend) and the periodogram, from the
earlier lecture on spectral estimation.

## The recipe common to all three models

Each model below fits the same template. There is a sequence of "natural" parameters
$\theta_1,\dots,\theta_m$ (a mean $\mu_t$, a log-standard-deviation $\alpha_t$, or a log-amplitude
$\alpha_j$ at Fourier frequency $j/n$) that is believed to change gradually rather than jump around.
Fit it by minimizing

$$
-\log(\text{likelihood in } \theta) \;+\; \lambda \sum_k \Big((\theta_{k+1}-\theta_k) - (\theta_k - \theta_{k-1})\Big)^2
$$

or the same expression with the square replaced by an absolute value. The bracketed term is the
discrete second difference of $\theta$ at index $k$ — zero exactly when $\theta$ is locally linear —
so this penalty is a roughness penalty: it punishes curvature, not the level or the slope of
$\theta$. Two choices of penalty, two behaviours: the squared penalty (ridge) shrinks curvature
everywhere a little; the absolute-value penalty (lasso) is willing to leave most of the sequence
exactly linear and concentrate the curvature at a few points, which is why it tends to produce
piecewise-linear-looking fits with a handful of kinks rather than one uniformly smoothed curve.

For the mean model this penalty on $\mu$ is identical to a ridge or lasso penalty on the
coefficients of the truncated-power regression basis

$$
\mu_t = \beta_0 + \beta_1(t-1) + \beta_2(t-2)_+ + \cdots + \beta_{n-1}\big(t-(n-1)\big)_+ ,
$$

covered in an earlier lecture: the term $\beta_k(t-k)_+$ adds a kink to $\mu$ starting at $t=k$, and
its coefficient $\beta_k$ is exactly the change in slope there — the same second difference the
penalty above targets. Penalizing $\sum_k \beta_k^2$ or $\sum_k|\beta_k|$ is therefore the same
optimization as penalizing the sum of squared or absolute second differences of $\mu$ directly. All
three models below are instead solved directly in terms of $\theta$, with `cvxpy`, rather than
through this regression representation.

Without any penalty ($\lambda = 0$), each of these three problems has a trivial, useless solution:
the likelihood alone is maximized by fitting $\theta$ to each observation individually (for Model 1,
$\hat\mu_t = y_t$ — the noisy data itself; for Models 2 and 3, see below). The penalty is what turns
"read off the noise" into "estimate the smooth part."

## Model 1 — smoothing the mean

The model is

$$
y_t \overset{\text{ind}}{\sim} N(\mu_t,\sigma^2), \qquad t = 1,\dots,n,
$$

where $\mu_t$, the trend, is smooth in $t$. The regularized estimators minimize

$$
\sum_{t=1}^n (y_t-\mu_t)^2 + \lambda\sum_{t=2}^{n-1}\Big((\mu_{t+1}-\mu_t)-(\mu_t-\mu_{t-1})\Big)^2
\quad\text{(ridge)}
$$

or the same sum-of-squares term plus $\lambda\sum_t\big|(\mu_{t+1}-\mu_t)-(\mu_t-\mu_{t-1})\big|$
(lasso). Directly in terms of $\mu$, with the second difference written as
`mu[2:] - 2*mu[1:-1] + mu[:-2]`:

```python
def mu_est_ridge(y, lambda_val):
    n = len(y)
    mu = cp.Variable(n)
    neg_likelihood_term = cp.sum((y - mu)**2)
    smoothness_penalty = cp.sum(cp.square(mu[2:] - 2 * mu[1:-1] + mu[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()
    return mu.value

def mu_est_lasso(y, lambda_val):
    n = len(y)
    mu = cp.Variable(n)
    neg_likelihood_term = cp.sum((y - mu)**2)
    smoothness_penalty = cp.sum(cp.abs(mu[2:] - 2 * mu[1:-1] + mu[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()
    return mu.value
```

**Worked example.** Data were simulated as $y_t = \mu_t + \varepsilon_t$ for $t = 1,\dots,2000$,
with $\mu_t$ a genuinely wiggly function of $x \in [0,1]$ on an equally spaced grid —
$\sin(15x) + e^{-x^2/2} + \tfrac12(x-0.5)^2 + 2\log(x+0.1)$ — and $\varepsilon_t \sim N(0,1)$ i.i.d.
Both estimators were fit ($\lambda = 200{,}000$ for ridge, $\lambda = 200$ for lasso — the two
penalties live on different numerical scales, so the same $\lambda$ does not mean the same amount of
smoothing for both) and plotted against the noisy data and the true $\mu_t$ for comparison. The
point of the example is mechanical: it shows that optimizing directly over $\mu$ recovers the same
kind of fit as the regression formulation, without ever building the $n\times n$ design matrix.

## Model 2 — smoothing a time-varying variance

Model 1 assumes constant noise variance and a moving mean. Model 2 is the mirror image: the mean is
fixed at zero and the *variance* moves.

$$
y_t \overset{\text{ind}}{\sim} N(0,\tau_t^2), \qquad t=1,\dots,n.
$$

Because $\tau_t > 0$ must stay positive under optimization, reparametrize with
$\alpha_t = \log\tau_t$. The density of $y_t$ is $\frac{1}{\sqrt{2\pi}\,\tau_t}\exp\!\big(-y_t^2/2\tau_t^2\big)$,
so, dropping the constant $\log\sqrt{2\pi}$ and writing $\tau_t = e^{\alpha_t}$, the negative
log-likelihood is

$$
\sum_{t=1}^n\left(\alpha_t + \frac{y_t^2}{2}e^{-2\alpha_t}\right).
$$

Setting the derivative in $\alpha_t$ to zero shows the unregularized fit is $\hat\alpha_t =
\log|y_t|$ — one noisy observation per parameter, exactly as unhelpful as $\hat\mu_t = y_t$ was in
Model 1. Adding the same second-difference penalty on $\alpha$ (ridge or lasso) gives an estimate
that borrows strength across nearby $t$:

```python
def alpha_est_ridge(y, lambda_val):
    n = len(y)
    alpha = cp.Variable(n)
    neg_likelihood_term = cp.sum(cp.multiply(((y ** 2)/2), cp.exp(-2 * alpha)) + alpha)
    smoothness_penalty = cp.sum(cp.square(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()
    return alpha.value
```

(`alpha_est_lasso` is identical with `cp.abs` in place of `cp.square`.)

**Why look at $y_t^2$.** The likelihood depends on the data only through $y_t^2$, so
$y_1^2,\dots,y_n^2$ is a sufficient statistic. Since $y_t^2 \sim \tau_t^2\chi^2_1$, it has mean
$\tau_t^2$ and variance $2\tau_t^4$ — both the level and the spread of $y_t^2$ move with $\tau_t^2$,
which is why a plot of $y_t^2$ against the fitted $\hat\tau_t^2 = e^{2\hat\alpha_t}$ looks noisy in
exactly the way the model predicts, more so where $\tau_t$ is larger. Taking logs,
$\log(y_t^2) = \log(\tau_t^2) + \log(\chi_1^2)$; since $\mathbb E[\log\chi_1^2] \approx -1.27$, the
log-transformed data sits, on average, visibly *below* $\log\tau_t^2$ rather than scattered around
it symmetrically — worth knowing before reading a log-periodogram plot, since the same offset
reappears in Model 3.

**Two simulated settings.** In the first, $\tau_t = \sqrt{1+\theta^2+2\theta\cos(2\pi t/n)}$ with
$\theta=-0.8$, a smooth periodic variance over $n=400$ points. In the second, $\alpha_t$ is set to
the same wiggly `smoothfun` used for $\mu_t$ in Model 1, so $\tau_t = e^{\alpha_t}$ — checking the
same estimator on a variance surface with the same shape used to test the mean estimator.

**A real example: S&P 500 returns.** Daily closing prices of the S&P 500 (2000–2024, via
`yfinance`) were converted to percentage log-returns, $y = 100\times\text{diff}(\log(\text{price}))$.
Financial returns are close to mean zero but visibly go through calmer and more turbulent stretches
— exactly the pattern Model 2 targets, since it treats the mean as fixed and lets only the variance
drift. Ridge and lasso estimates of $\alpha_t$ were fit ($\lambda=4\times10^7$ ridge, $\lambda=2000$
lasso) and compared to $y_t^2$ directly and on the log scale.

## Model 3 — smoothing the spectrum

Model 3 reuses the same machinery in the frequency domain, and is the same *spectrum model*
introduced in an earlier lecture, applied here to a real dataset. Recall the periodogram at Fourier
frequency $j/n$,

$$
I(j/n) := \frac{|b_j|^2}{n},
$$

where $b_j$ is the $j$-th coefficient of the discrete Fourier transform of $y_1,\dots,y_n$, computed
for $j/n$ between $0$ and $\tfrac12$.

**A motivating dataset.** EEG recordings (64-channel, from the PhysioNet EEG Motor Movement/Imagery
database) were compared for one subject and one channel across two conditions: eyes open and eyes
closed. Cognitive neuroscience predicts that the power of the occipital alpha rhythm (about 10 Hz)
rises when the eyes are closed (Hohaia et al., 2022). The raw time series for the two conditions
look similar by eye; the periodogram makes the difference visible, and its logarithm makes it
sharper still (recall from Model 2 that the periodogram, like $y_t^2$, is noisy in proportion to its
own level, so working on a log scale is the natural fix).

**The model.** For $j=1,\dots,m$,

$$
\operatorname{Re}(b_j),\ \operatorname{Im}(b_j) \overset{\text{i.i.d.}}{\sim} N(0,\gamma_j^2).
$$

Since $I(j/n) = \big(\operatorname{Re}(b_j)^2+\operatorname{Im}(b_j)^2\big)/n$ is, up to scale, a sum
of two independent squared normals, $I(j/n) \sim \frac{\gamma_j^2}{n}\chi^2_2$, and the likelihood in
terms of the periodogram is

$$
\prod_{j=1}^m \frac{n}{\gamma_j^2}\exp\!\left(-\frac{nI(j/n)}{2\gamma_j^2}\right)
\quad\Longrightarrow\quad
-\log(\text{lik}) = \sum_{j=1}^m\left(\frac{nI(j/n)}{2\gamma_j^2}+2\log\gamma_j\right).
$$

With $\alpha_j=\log\gamma_j$ this is $\sum_j\big(\tfrac{n}{2}I(j/n)e^{-2\alpha_j}+2\alpha_j\big)$ —
exactly Model 2's negative log-likelihood with $y_t^2$ replaced by $I(j/n)$ and an extra factor of
$2$ (because $I(j/n)$ is $\chi^2_2$, with two degrees of freedom, rather than $\chi^2_1$). Minimizing
without any penalty gives, by the same calculation as in Model 2,

$$
\alpha_j = \log\sqrt{\frac{nI(j/n)}{2}}, \qquad \gamma_j^2 = e^{2\alpha_j} = \frac{nI(j/n)}{2} ,
$$

i.e. the unregularized "estimate" is just the periodogram itself, unsmoothed. Adding the ridge or
lasso second-difference penalty on $\{\alpha_j\}$ — this time smoothing across *frequency* $j$
rather than across *time* $t$ — produces a smoothed estimate of the power spectrum:

```python
def alpha_estimator_ridge(y, lambda_val):
    freq, I = periodogram(y)
    m, n = len(freq), len(y)
    alpha = cp.Variable(m)
    neg_likelihood_term = cp.sum(cp.multiply((n * I / 2), cp.exp(-2 * alpha)) + 2*alpha)
    smoothness_penalty = cp.sum(cp.square(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()
    return alpha.value, freq
```

(`alpha_estimator_lasso` again just swaps in `cp.abs`.) The fitted mean of the periodogram under the
model is $\mathbb E[I(j/n)] = 2\gamma_j^2/n = \tfrac{2}{n}e^{2\alpha_j}$, which is what gets plotted
against the raw, very noisy, periodogram.

**Reading off the alpha rhythm.** Locating the peaks of the smoothed lasso log-spectrum for the
eyes-closed recording finds candidates at frequency (as a fraction of $n$) $\approx 0.0627$,
$0.108$, and $0.245$; the first, converted to Hertz by multiplying by the 160 Hz sampling rate, gives
$0.0627 \times 160 \approx 10.03\text{ Hz}$ — squarely inside the 8–12 Hz band conventionally called
the alpha rhythm. The smoothed spectra for the two conditions are visibly different in exactly that
band, matching the neuroscience prediction that motivated looking at the data this way in the first
place.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Smoothed log-periodogram comparing eyes-open and eyes-closed EEG, with elevated power in the 8-12 Hz alpha band for eyes closed">
  <rect x="112" y="15" width="36" height="150" fill="currentColor" fill-opacity="0.15"/>
  <line x1="40" y1="170" x2="315" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <line x1="40" y1="15" x2="40" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <text x="177" y="188" text-anchor="middle" font-size="12" fill="currentColor">frequency (Hz)</text>
  <text x="130" y="12" text-anchor="middle" font-size="11" fill="currentColor">8&#8211;12 Hz</text>
  <polyline points="40,60 80,95 120,115 160,128 200,136 240,142 280,147 310,150"
            fill="none" stroke="currentColor" stroke-width="1.6"/>
  <text x="315" y="153" font-size="11" fill="currentColor">eyes open</text>
  <polyline points="40,58 80,93 100,108 112,100 130,80 148,102 160,126 200,135 240,141 280,146 310,149"
            fill="none" stroke="darkorange" stroke-width="1.8"/>
  <text x="230" y="72" font-size="11" fill="darkorange">eyes closed</text>
</svg>
<figcaption>Schematic of the finding: the smoothed log-periodogram for eyes-closed EEG rises above the
eyes-open spectrum specifically in the 8-12 Hz alpha band, the signature the model was used to
recover from the raw, noisy periodogram.</figcaption>
</figure>

The same method was also applied, in the same lecture, to a yearly sunspot-count series in place of
the EEG data: the periodogram of the sunspot series was computed and smoothed the same way. The
model and code are identical; only the dataset changes.

## Sources

- **Model 1**: `spring-2025/CodeLectureFourteen153248Spring2025/01-model-one.md` (introductory
  framing, "Three High-Dimensional Models for Time Series") and the parallel
  `fall-2025/CodeLectureFourteen153248Fall2025/02-model-one.md` — the two notebooks are essentially
  identical for this section; this chapter draws on both.
- **Model 2**: `fall-2025/.../03-model-two.md` and `spring-2025/.../02-model-two.md`, identical in
  content (the derivation, both simulated settings, and the S&P 500 example agree word-for-word
  between the two semesters).
- **Model 3**: `fall-2025/.../04-model-three.md` (the EEG eyes-open/eyes-closed worked example, used
  here in full) and `spring-2025/.../03-model-three.md` (the same model applied instead to a
  sunspot-count series, mentioned briefly rather than reproduced in full, since the mathematical
  content duplicates the fall notebook and only the dataset differs).
- Referred to but not contained in these notebooks: the trend-filtering / truncated-power-basis
  regression representation of $\mu_t$, and the definition and derivation of the periodogram, both
  described as covered in earlier lectures of the course; Hohaia et al. (2022), "Occipital
  alpha-band brain waves when the eyes are closed are shaped by ongoing visual processes," cited for
  the alpha-rhythm claim; the PhysioNet EEG Motor Movement/Imagery Database
  (physionet.org/content/eegmmidb/1.0.0/) and the yearly sunspot-count dataset (`SN_y_tot_V2.0.csv`),
  both used as data sources but not included in the converted notebooks.

---

[← 42. Time Series Regression and Uncertainty](42-time-series-regression-and-uncertainty.md) · [Contents](index.md) · [44. Multiple Sinusoids and Change-Points →](44-multiple-sinusoids-and-change-points.md)
