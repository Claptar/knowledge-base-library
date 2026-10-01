---
title: "106. Mean, Variance, and Spectrum Models"
course: "Berkeley Stat 153"
chapter: 106
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 106. Mean, Variance, and Spectrum Models

## What this covers

This chapter lays out three high-dimensional models for a time series $y_1, \dots, y_n$: a **mean
model**, already met the previous week as trend filtering, and two **variance models** — one that
models the raw data directly, one that models its discrete Fourier transform (DFT). The point of
walking through the three together is that the second is deliberately the simplest version of the
idea, so that the more useful third model — a smoothed periodogram — is nothing but the second
model applied to the right coordinates. It assumes ridge and lasso trend filtering (from the
previous lecture), the DFT and periodogram, and the chi-squared distribution.

## Model one: the mean model (recap)

The first model treats $\mu_t$, the mean of $y_t$, as the object of interest:

$$y_t \overset{\text{ind}}{\sim} N(\mu_t, \sigma^2).$$

Writing "ind" rather than "i.i.d." matters: the right-hand side depends on $t$, so the $y_t$ are
independent but not identically distributed. The parameters are $\mu_1, \dots, \mu_n$ together with
$\sigma^2$ — as many mean parameters as data points, which is what makes the model
high-dimensional. Maximizing the likelihood with no constraint gives $\hat\mu_t = y_t$ and
$\hat\sigma^2 = 0$: the model interpolates the data exactly, which is overfitting, not estimation.

Getting something useful requires regularizing $\mu_t$ toward smoothness. Penalizing closeness of
*slopes* (the discrete second difference), rather than just closeness of neighbouring values, gives
more smoothness. This yields the ridge and lasso trend-filtering estimators $\hat\mu_t^{\text{ridge}}(\lambda)$
and $\hat\mu_t^{\text{lasso}}(\lambda)$ minimizing

$$\sum_{t=1}^n (y_t - \mu_t)^2 + \lambda \sum_{t=2}^{n-1} \big((\mu_{t+1} - \mu_t) - (\mu_t - \mu_{t-1})\big)^2$$

and

$$\sum_{t=1}^n (y_t - \mu_t)^2 + \lambda \sum_{t=2}^{n-1} \big|(\mu_{t+1} - \mu_t) - (\mu_t - \mu_{t-1})\big|$$

respectively. As covered the previous week, both can be rewritten as linear-model penalized
regressions $\hat\mu_t = X\hat\beta$, where

$$X = \begin{pmatrix}
1 & 0 & 0 & \cdot & \cdot & 0 \\
1 & 1 & 0 & \cdot & \cdot & 0 \\
1 & 2 & 1 & \cdot & \cdot & 0 \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
1 & n-1 & n-2 & \cdot & \cdot & 1
\end{pmatrix}, \qquad
\beta = \begin{pmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \\ \cdot \\ \cdot \\ \beta_{n-1} \end{pmatrix},$$

and $\hat\beta^{\text{ridge}}(\lambda)$, $\hat\beta^{\text{lasso}}(\lambda)$ minimize
$\|y - X\beta\|^2 + \sum_{t=2}^{n-1}\beta_t^2$ and $\|y - X\beta\|^2 + \sum_{t=2}^{n-1}|\beta_t|$.

Model One is an example of a **mean model**: the target is $\mu_t$. The remaining two models are
**variance models** — the target is a variance parameter instead, and the same overfitting-then-
regularize pattern reappears in a new coordinate.

## Model two: a variance model for the raw data

Now suppose the mean is known to be zero and interest is in how the *scale* of $y_t$ changes over
time:

$$y_t \overset{\text{ind}}{\sim} N(0, \tau_t^2). \tag{2}$$

The parameters are $\tau_1^2, \dots, \tau_n^2$ — again as many as data points, so again
high-dimensional. $\tau_t$ is the magnitude of $y_t$; this model is the right one when only the size
of the observations matters, not their sign.

**Finding the sufficient statistic.** The likelihood is proportional to

$$\prod_{t=1}^n \frac{1}{\tau_t}\exp\left(-\frac{y_t^2}{2\tau_t^2}\right), \tag{3}$$

which depends on the data only through the squares $y_1^2, \dots, y_n^2$ — these are the
**sufficient statistic**. That this is the right way to see it can be checked directly: under (2),
$y_t^2 \overset{\text{ind}}{\sim} \tau_t^2 \chi_1^2$, and rewriting the density of $\tau_t^2\chi_1^2$
in terms of $x = y_t^2$ gives

$$\frac{1}{\tau_t^2}\left(\frac{x}{\tau_t^2}\right)^{-1/2}\exp\left(-\frac{x}{2\tau_t^2}\right)
= x^{-1/2}\,\frac{1}{\tau_t}\exp\left(-\frac{x}{2\tau_t^2}\right).$$

The factor $x^{-1/2} = (y_t^2)^{-1/2}$ does not involve $\tau_t$, so dropping it recovers (3)
exactly — the likelihood computed from the squares alone agrees with the likelihood computed from
the raw data.

**Overfitting again, and the log-scale reparametrization.** The negative log-likelihood is

$$\sum_{t=1}^n \left(\log \tau_t + \frac{y_t^2}{2\tau_t^2}\right).$$

Since $\tau_t > 0$ is constrained, it is more convenient to optimize over $\alpha_t = \log \tau_t$
instead, which is unconstrained. This reparametrization is worth doing for two reasons: it turns a
constrained problem into an unconstrained one, which is more numerically stable to optimize; and
because variance parameters can range over several orders of magnitude, working on the log scale
avoids the precision problems that come with that range. (This is also why stochastic volatility
models are typically written in log-variance form.) In terms of $\alpha_t$, the negative
log-likelihood is

$$\sum_{t=1}^n \left(\alpha_t + \frac{y_t^2}{2}e^{-2\alpha_t}\right).$$

Minimizing this with no further constraint gives $\alpha_t = \log|y_t|$, i.e. $\tau_t^2 = y_t^2$:
exactly the overfitting seen in Model One, now happening to the sufficient statistic instead of to
the raw data.

**Regularizing.** Assuming $\alpha_t$ varies smoothly in $t$, the same second-difference penalty as
in Model One gives ridge and lasso estimators $\hat\alpha_t^{\text{ridge}}(\lambda)$,
$\hat\alpha_t^{\text{lasso}}(\lambda)$ minimizing

$$\sum_{t=1}^n \left(\alpha_t + \frac{y_t^2}{2}e^{-2\alpha_t}\right) + \lambda \sum_{t=2}^{n-1}\big((\alpha_{t+1}-\alpha_t)-(\alpha_t-\alpha_{t-1})\big)^2$$

and the corresponding sum of absolute values. Both objectives are convex in $\alpha$, so they can
be handed to a general convex solver — `cvxpy`, the same tool used for the mean-model estimators.

## Model three: a variance model for the spectrum

Model Three reuses Model Two exactly, but applied to the DFT of the series rather than to the
series itself. Recall the DFT: given $y_0, \dots, y_{n-1}$, its transform is $b_0, \dots, b_{n-1}$
with

$$b_j = \sum_{t=0}^{n-1} y_t \exp\left(-\frac{2\pi i jt}{n}\right), \qquad
\mathrm{Re}(b_j) = \sum_{t=0}^{n-1} y_t\cos\left(\frac{2\pi jt}{n}\right), \qquad
\mathrm{Im}(b_j) = -\sum_{t=0}^{n-1} y_t\sin\left(\frac{2\pi jt}{n}\right).$$

Two facts about the DFT do the organizing work here. First, $b_0 = \sum_t y_t$ has zero imaginary
part and carries no information about cycles — it is just the sum of the data. Second,
$b_{n-j} = \bar{b}_j$: the second half of the coefficients is the complex conjugate of the first
half, hence redundant. So the *informative* coefficients are $b_1, \dots, b_m$, where $m = (n-1)/2$
if $n$ is odd, and $m = (n-2)/2$ (plus the single real coefficient $b_{n/2}$) if $n$ is even. What
follows takes $n$ odd, with $m = (n-1)/2$, for simplicity.

**The model.** Apply Model Two to the real and imaginary parts of each informative DFT coefficient:

$$\mathrm{Re}(b_j), \mathrm{Im}(b_j) \overset{\text{i.i.d.}}{\sim} N(0, \gamma_j^2), \qquad j = 1, \dots, m, \tag{4}$$

with the $b_j$ independent across $j$. The parameters are $\gamma_1, \dots, \gamma_m$, and $\gamma_j$
is the strength of the sinusoid at frequency $j/n$.

**The sufficient statistic is the periodogram.** The likelihood for (4) is

$$\prod_{j=1}^m \frac{1}{\gamma_j}\exp\left(-\frac{\mathrm{Re}(b_j)^2}{2\gamma_j^2}\right)\frac{1}{\gamma_j}\exp\left(-\frac{\mathrm{Im}(b_j)^2}{2\gamma_j^2}\right)
= \prod_{j=1}^m \frac{1}{\gamma_j^2}\exp\left(-\frac{|b_j|^2}{2\gamma_j^2}\right),$$

which depends on the data only through $|b_j|^2$. Recalling the periodogram $I(j/n) := |b_j|^2/n$,
the likelihood is

$$\prod_{j=1}^m \frac{1}{\gamma_j^2}\exp\left(-\frac{nI(j/n)}{2\gamma_j^2}\right), \tag{5}$$

so the periodogram ordinates $I(j/n)$, $j=1,\dots,m$, are the sufficient statistic — the exact
counterpart of the squares $y_t^2$ in Model Two. Since $\mathrm{Re}(b_j)$ and $\mathrm{Im}(b_j)$ are
independent $N(0,\gamma_j^2)$, their sum of squares satisfies $|b_j|^2 \sim \gamma_j^2 \chi_2^2$, so

$$I(j/n) \overset{\text{ind}}{\sim} \frac{\gamma_j^2}{n}\chi_2^2, \qquad j = 1,\dots, m.$$

(A useful side fact: $\chi_2^2$ is the same distribution as an exponential with rate $1/2$.) Model
Three intentionally does not care about the individual coefficients $b_j$, only their magnitude —
which is exactly the periodogram.

**Overfitting and regularizing, again.** The negative log-likelihood for (5), reparametrized with
$\alpha_j = \log\gamma_j$, is

$$\sum_{j=1}^m \left(2\alpha_j + \frac{nI(j/n)}{2}e^{-2\alpha_j}\right).$$

Unconstrained minimization gives $\alpha_j = \log\sqrt{nI(j/n)/2}$, i.e.
$\gamma_j^2 = nI(j/n)/2$: the estimate interpolates the periodogram exactly, the same overfitting
seen twice already. Assuming $\alpha_j$ varies smoothly across frequency $j$, the same
second-difference penalty gives ridge and lasso estimators minimizing

$$\sum_{j=1}^m \left(2\alpha_j + \frac{nI(j/n)}{2}e^{-2\alpha_j}\right) + \lambda \sum_{j=2}^{m-1}\big((\alpha_{j+1}-\alpha_j)-(\alpha_j-\alpha_{j-1})\big)^2$$

and the corresponding absolute-value penalty. The result is a smoothed estimate of $\gamma_j^2$
across frequencies — a regularized version of the periodogram — obtained by exactly the same
convex-optimization recipe as Model Two.

## The pattern common to both variance models

Laid side by side, Model Two and Model Three follow one recipe, differing only in which quantity
plays the role of "the data":

1. Write down a model in which the raw quantity of interest ($y_t$, or $\mathrm{Re}(b_j)$ and
   $\mathrm{Im}(b_j)$) is mean-zero Gaussian with an unknown, time- or frequency-varying variance.
2. Observe that the likelihood collapses onto a low-dimensional sufficient statistic — the squared
   observations $y_t^2$ for Model Two, the periodogram $I(j/n)$ for Model Three — because a sum of
   squares of independent Gaussians is chi-squared.
3. The unregularized MLE reproduces the sufficient statistic exactly: $\hat\tau_t^2 = y_t^2$, or
   $\hat\gamma_j^2 = nI(j/n)/2$. This is overfitting, just as $\hat\mu_t = y_t$ was in Model One.
4. Reparametrize the variance on the log scale ($\alpha = \log\tau$ or $\log\gamma$) to make the
   optimization unconstrained and numerically stable.
5. Penalize the discrete second difference of $\alpha$ (ridge or lasso) to obtain a smooth,
   non-overfit estimate. Both penalized objectives stay convex, so the same solver (`cvxpy`) that
   handled the mean model handles both variance models.

This is why the lecture introduces Model Two before Model Three: Model Three is Model Two applied
coordinate-by-coordinate to the DFT rather than to the series itself, and every step of the
derivation goes through unchanged once $y_t^2$ is replaced by $I(j/n)$.

## Sources

- Berkeley Stat 153, Spring 2025, Lecture Fourteen (Aditya Guntuboyina, March 6, 2025) —
  `docs/statistics/berkeley/stat153/spring-2025/LectureFourteen153248Spring2025/01-1-model-one.md`,
  `.../02-2-model-two.md`, `.../03-3-model-three.md` in the knowledge-base-library. These three
  files are a model's reconstruction of a PDF slide deck with no extractable text layer; the
  original slides and any spoken commentary were not supplied, so nothing beyond what is written in
  these three files is reflected here, and every equation should be treated as unverified against
  the original.
- The lecture explicitly builds on material not included in these files: "last week's" derivation
  of the ridge/lasso trend-filtering estimators and their linear-model representation (Model One),
  and "last lecture's" spectrum model, which Model Three is stated to be equivalent to but the
  equivalence is deferred to the next lecture and is not shown here.
- No transcript, problem set, or additional notes were supplied for this lecture.

---

[← 105. Frequentist and Bayesian Linear Regression](105-frequentist-and-bayesian-linear-regression.md) · [Contents](index.md) · [107. Multiple Frequencies and Change-of-Slope Models →](107-multiple-frequencies-and-change-of-slope-models.md)
