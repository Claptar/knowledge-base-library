---
title: "101. AR(p) Estimation and Forecasting (part 2)"
course: "Berkeley Stat 153 Fall 2024"
chapter: 101
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 101. AR(p) Estimation and Forecasting (part 2)

## What this covers

This chapter answers: once you have written down an AR($p$) model, how do you actually estimate
its coefficients and noise variance, attach uncertainty to those estimates, and use the fitted
model to forecast future values together with honest standard errors for the forecasts? It assumes
the AR($p$) model itself, ordinary linear regression (least squares, the MLE, and the flat-prior
Bayesian posterior that produces a $t$-distribution for the regression coefficients), and basic
manipulation of covariance matrices.

## The AR($p$) likelihood, and why it looks like regression

Recall the AR($p$) model,
$$y_t = \phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t,$$
with unknown parameters $\phi_0, \dots, \phi_p$ and $\sigma$, the standard deviation of the noise.
Write $\theta$ for the whole parameter vector. To estimate $\theta$ from data $y_1, \dots, y_n$ we
need its likelihood, and the awkward feature of a time series — each observation depends on the
ones before it — has to be dealt with explicitly.

Split the joint density of all the data using the chain rule, conditioning on the first $p$
observations:
$$f_{y_1,\dots,y_n\mid\theta}(y_1,\dots,y_n) = f_{y_{p+1},\dots,y_n \mid y_1,\dots,y_p,\theta}(y_{p+1},\dots,y_n)\; f_{y_1,\dots,y_p\mid\theta}(y_1,\dots,y_p).$$
The first factor is called the **conditional likelihood**. Because each $y_t$ for $t > p$ is
$\phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \epsilon_t$, and this term-by-term expansion
only uses the model equation for $t = p+1, \dots, n$, the conditional density factors over $t$:
$$f_{y_{p+1},\dots,y_n\mid y_1,\dots,y_p,\theta}(y_{p+1},\dots,y_n) = \prod_{t=p+1}^n f_{\epsilon_t \mid y_{t-1},\dots,y_1,\theta}\bigl(y_t - \phi_0 - \phi_1 y_{t-1} - \dots - \phi_p y_{t-p}\bigr).$$
Assume, as is standard, that $\epsilon_t$ is independent of $y_1,\dots,y_{t-1}$ and
$\epsilon_t \sim N(0,\sigma^2)$, so that
$$\epsilon_t \mid y_{t-1},\dots,y_1 \sim N(0,\sigma^2), \qquad t = p+1,\dots,n.$$
Then the conditional likelihood is an explicit Gaussian product:
$$f_{y_{p+1},\dots,y_n\mid y_1,\dots,y_p,\theta}(y_{p+1},\dots,y_n) = \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^{n-p} \exp\left(-\frac{1}{2\sigma^2}\sum_{t=p+1}^n\bigl(y_t - \phi_0 - \phi_1 y_{t-1} - \dots - \phi_p y_{t-p}\bigr)^2\right).$$

The second factor, $f_{y_1,\dots,y_p\mid\theta}(y_1,\dots,y_p)$, would in principle require running
the model equation backward past $t=1$, which only makes sense under stationarity assumptions on
$\phi_0,\dots,\phi_p$ and is not worth the complication. The standard move is instead to *assume*
this factor does not depend on $\theta$, so that maximizing the full likelihood is the same as
maximizing the conditional likelihood alone. Everything below works with the conditional
likelihood.

Stack the data into matrix form,
$$Y = \begin{pmatrix} y_{p+1} \\ \vdots \\ y_n \end{pmatrix}_{(n-p)\times 1}, \qquad X = \begin{pmatrix} 1 & y_p & y_{p-1} & \cdots & y_1 \\ 1 & y_{p+1} & y_p & \cdots & y_2 \\ \vdots & \vdots & \vdots & & \vdots \\ 1 & y_{n-1} & y_{n-2} & \cdots & y_{n-p} \end{pmatrix}_{(n-p)\times(p+1)}, \qquad \beta = \begin{pmatrix} \phi_0 \\ \vdots \\ \phi_p \end{pmatrix}_{(p+1)\times 1}.$$
Then the conditional likelihood is
$$\text{likelihood} \propto \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^{n-p} \exp\left(-\frac{\|Y-X\beta\|^2}{2\sigma^2}\right),$$
which is *exactly* the likelihood of ordinary linear regression with $n-p$ observations, response
$Y$, design matrix $X$, and coefficient vector $\beta$. Each row of $X$ is a window of $p$ past
values plus the intercept column — the "predictors" for AR regression are just lagged values of
the series itself. This identification is what lets every regression tool be reused for AR
estimation.

## Bayesian inference

Since the likelihood is literally the linear-regression likelihood, Bayesian inference for AR($p$)
is *identical* to Bayesian inference for linear regression, because Bayesian inference only cares
about the likelihood. Using the same flat prior as before,
$$\phi_0,\phi_1,\dots,\phi_p,\log\sigma \overset{\text{i.i.d.}}{\sim}\text{unif}(-C,C),$$
and integrating the joint posterior of $(\beta,\sigma)$ over $\sigma$ gives the posterior of $\beta$
alone as a multivariate $t$:
$$\beta \mid \text{data} \sim t_{n-2p-1,\,p+1}\bigl(\hat\beta,\ \hat\sigma^2 (X^TX)^{-1}\bigr),$$
where
$$\hat\beta := (X^TX)^{-1}X^TY, \qquad \hat\sigma := \sqrt{\frac{\|Y-X\hat\beta\|^2}{n-2p-1}}.$$
The degrees of freedom is $n - 2p - 1$: there are $n-p$ effective observations and $p+1$ fitted
coefficients, so the usual "observations minus parameters minus one" count is
$(n-p) - (p+1) - 1 + 1$... concretely, $n-p$ observations and $p+1$ regression coefficients give
$(n-p)-(p+1) = n-2p-1$ residual degrees of freedom. If inference on $\sigma$ itself is wanted,
$$\frac{\|Y-X\hat\beta\|^2}{\sigma^2}\ \middle|\ \text{data} \sim \chi^2_{n-2p-1}.$$

## Frequentist inference — where the analogy with regression breaks

The MLE of $\beta$ is the same $\hat\beta = (X^TX)^{-1}X^TY$ as above, and the MLE of $\sigma$ is
$$\hat\sigma_{\text{MLE}} = \sqrt{\frac{\|Y-X\hat\beta\|^2}{n-p}}$$
(dividing by $n-p$, the number of effective observations, rather than by $n-2p-1$).

Here the parallel with ordinary regression stops. To build a frequentist confidence interval for a
coefficient $\phi_i$ one needs the *sampling* distribution of $\hat\beta$, and for AR models this
is genuinely different from the regression case — the rows of $X$ are not independent of $Y$ the
way regression assumes, since each row of $X$ is built from the same series whose future values
are being regressed on. The correct derivation (see Section 3.5 of Shumway and Stoffer's *Time
Series Analysis and its Applications*) is asymptotic and more involved than the regression
argument, and it produces **normal** limiting distributions for the $\hat\phi_i$, not
$t$-distributions — so inference uses $z$-scores, not $t$-scores, even though the point estimates
are computed by literally running OLS. In practice the numerical results from the Bayesian
$t$-based interval and the frequentist normal-based interval end up close.

## Doing it on the computer

Two equivalent routes to the point estimates:

1. Build $Y$ and $X$ by hand as above and run ordinary least squares.
2. Use the `AutoReg` function in `statsmodels`, which does the same regression internally.

Both give the same $\hat\phi_0,\dots,\hat\phi_p$. They differ in the reported $\hat\sigma$ and
standard errors, because they use different divisors:

| | $\hat\sigma$ | standard errors from | coefficient inference |
|---|---|---|---|
| OLS | $\sqrt{\text{RSS}/(n-2p-1)}$ | $\hat\sigma^2_{\text{OLS}}(X^TX)^{-1}$ | $t_{n-2p-1}$ |
| `AutoReg` | $\sqrt{\text{RSS}/(n-p)}$ (the MLE) | $\hat\sigma^2_{\text{MLE}}(X^TX)^{-1}$ | normal |

`AutoReg`'s choices are the ones justified by the correct AR asymptotics described above; OLS is
just reusing the regression machinery, which is a convenient approximation rather than the
theoretically correct procedure for this model.

## Point prediction

Once $\theta = (\phi_0,\dots,\phi_p,\sigma)$ is fixed (in practice, replaced by its conditional
MLE $\hat\theta$), the natural point prediction for a future value $y_{n+i}$ is its conditional
expectation given everything observed:
$$\hat y_{n+i}(\theta) := \mathbb{E}(y_{n+i}\mid y_1,\dots,y_n,\theta).$$
These are computed recursively. Initialize with the observed values themselves,
$$\hat y_j(\theta) = y_j \quad\text{for } j = n, n-1,\dots, n+1-p,$$
and then, for $i = 1, 2, \dots$, apply the model equation with the noise term dropped (since
$\mathbb E[\epsilon_{n+i}\mid \text{data}] = 0$):
$$\hat y_{n+i}(\theta) = \phi_0 + \phi_1\hat y_{n+i-1}(\theta) + \phi_2 \hat y_{n+i-2}(\theta) + \dots + \phi_p \hat y_{n+i-p}(\theta).$$
Each forecast plugs in previously *forecast* values once it runs past the observed data, which is
exactly what makes multi-step-ahead forecasts progressively less certain — the subject of the rest
of the chapter.

## Prediction standard errors

The natural companion to a point forecast is
$$V_i(\theta) := \operatorname{var}(y_{n+i}\mid y_1,\dots,y_n,\theta),$$
with the reported standard error for $\hat y_{n+i}$ taken as $\sqrt{V_i(\hat\theta)}$.

**A direct recursion in the $V_i$ alone does not exist.** Working out the first few terms shows
why. For $i=1$, $y_{n+1} = \phi_0 + \phi_1 y_n + \dots + \phi_p y_{n+1-p} + \epsilon_{n+1}$, and
every term except $\epsilon_{n+1}$ is part of the conditioning, so
$$V_1(\theta) = \operatorname{var}(\epsilon_{n+1}\mid\text{data},\theta) = \sigma^2.$$
For $i=2$, $y_{n+2} = \phi_0 + \phi_1 y_{n+1} + \phi_2 y_n + \dots + \epsilon_{n+2}$, and now $y_n$
is still data (variance $0$) but $y_{n+1}$ is itself random given the data, so
$$V_2(\theta) = \phi_1^2 \operatorname{var}(y_{n+1}\mid\text{data},\theta) + \sigma^2 = \sigma^2(1+\phi_1^2),$$
which *is* expressible through $V_1$. But at $i=3$,
$$y_{n+3} = \phi_0 + \phi_1 y_{n+2} + \phi_2 y_{n+1} + \dots + \epsilon_{n+3},$$
so
$$V_3(\theta) = \operatorname{var}(\phi_1 y_{n+2} + \phi_2 y_{n+1}\mid \text{data}) + \sigma^2,$$
and expanding the first term brings in $\operatorname{Cov}(y_{n+1},y_{n+2}\mid\text{data})$ — a
quantity that is not one of $V_1, V_2$ and has to be tracked separately. So the variances alone do
not close under the recursion; the *covariances* between not-yet-observed future values have to be
carried along too.

### Covariance matrix facts needed

For a random vector $Y = (Y_1,\dots,Y_n)^T$, $\operatorname{Cov}(Y)$ is the $n\times n$ matrix whose
$(i,j)$ entry is $\operatorname{Cov}(Y_i,Y_j)$; its diagonal holds the variances, and it is
symmetric. For two random vectors $Y$ ($p\times 1$) and $W$ ($q\times 1$),
$\operatorname{Cov}(Y,W)$ is the $p\times q$ matrix of pairwise covariances, so
$\operatorname{Cov}(Y) = \operatorname{Cov}(Y,Y)$. The two facts that drive the derivation are, for
deterministic matrices $A, B$ and vectors $c, d$,
$$\mathbb{E}(AY+c) = A\,\mathbb E(Y) + c, \qquad \operatorname{Cov}(AY+c,\,BW+d) = A\,\operatorname{Cov}(Y,W)\,B^T,$$
and specializing the second to a single linear combination $a^TY$ gives
$$\operatorname{var}(a^TY) = a^T\operatorname{Cov}(Y)\,a.$$

### The covariance recursion

Define, for $k=1,2,\dots$,
$$\Gamma_k(\theta) := \operatorname{Cov}\!\left(\begin{pmatrix} y_{n+1}\\ \vdots \\ y_{n+k}\end{pmatrix}\ \middle|\ \theta, y_1,\dots,y_n\right),$$
whose diagonal entries are exactly $V_1(\theta),\dots,V_k(\theta)$. Initialize with
$\Gamma_1(\theta) = V_1(\theta) = \sigma^2$, matching the computation above.

To go from $\Gamma_{k-1}$ to $\Gamma_k$, write $\Gamma_k$ in block form,
$$\Gamma_k(\theta) = \begin{pmatrix} \Gamma_{k-1}(\theta) & \gamma_{k1}(\theta) \\ \gamma_{k1}(\theta)^T & V_k(\theta)\end{pmatrix}, \qquad \gamma_{k1}(\theta) := \operatorname{Cov}\!\left(\begin{pmatrix} y_{n+1}\\ \vdots \\ y_{n+k-1}\end{pmatrix},\, y_{n+k}\ \middle|\ \theta,\text{data}\right).$$
Since $y_{n+k} = \phi_0 + \phi_1 y_{n+k-1} + \dots + \phi_p y_{n+k-p} + \epsilon_{n+k}$ and
$\epsilon_{n+k}$ has zero covariance with anything in the conditioning, $y_{n+k}$ can be replaced
by $\phi_1 y_{n+k-1} + \dots + \phi_p y_{n+k-p}$ inside the covariance. Writing this linear
combination as $a^T(y_{n+1},\dots,y_{n+k-1})^T$ for the $(k-1)\times 1$ vector $a$ with
$$a_i = \begin{cases}\phi_{k-i} & \text{if } k-p \le i \le k-1 \\ 0 & \text{otherwise,}\end{cases}$$
(i.e. $a$ places the coefficients $\phi_1,\dots,\phi_p$ against the $p$ most recent entries and
zero elsewhere), the covariance identities above give
$$\gamma_{k1}(\theta) = \Gamma_{k-1}(\theta)\,a, \qquad V_k(\theta) = a^T\Gamma_{k-1}(\theta)\,a + \sigma^2.$$
So the full block update is
$$\Gamma_k(\theta) = \begin{pmatrix} \Gamma_{k-1}(\theta) & \Gamma_{k-1}(\theta)a \\ a^T\Gamma_{k-1}(\theta) & a^T\Gamma_{k-1}(\theta)a+\sigma^2 \end{pmatrix}.$$

This gives a complete algorithm for the prediction standard errors up to horizon $K$:

1. Initialize $\Gamma_1(\theta) = V_1(\theta) = \sigma^2$.
2. For $k = 2,\dots,K$: form the vector $a$ (length $k-1$) with $a_i = \phi_{k-i}$ for
   $k-p\le i\le k-1$ and $a_i=0$ otherwise, then compute $\Gamma_k(\theta)$ from $\Gamma_{k-1}(\theta)$
   and $a$ by the block formula above.
3. Read $V_1(\theta),\dots,V_K(\theta)$ off the diagonal of $\Gamma_K(\theta)$.

As with the point forecasts, $\theta$ is replaced by the conditional MLE $\hat\theta$ in practice,
and the prediction standard error at horizon $i$ is $\sqrt{V_i(\hat\theta)}$. These numbers agree
with what `statsmodels`' `get_prediction` function reports.

## Sources

- Lecture 18, Fall 2025, UC Berkeley Stat 153 (Aditya Guntuboyina, 2025-10-30), converted notes
  `docs/statistics/berkeley/stat153/fall-2025/LectureEighteen153248Fall2025/01-1-ar-models-estimation-inference-and-prediction.md`
  (§§ 1–2 of the lecture: the likelihood derivation, Bayesian and frequentist inference, the
  OLS/`AutoReg` comparison, and point prediction) and
  `.../02-3-prediction-standard-errors.md` (§ 3: the failure of a direct variance recursion, the
  covariance-matrix review, and the $\Gamma_k$ recursion).
- Both source files are machine-reconstructed from a PDF slide deck with no text layer
  (`route: llm`, `fidelity: reconstructed`); the equations here follow that reconstruction and have
  not been independently re-derived from the original PDF.
- The lecture refers to, but does not itself contain, "Lecture 4" of the same course (for the
  flat-prior derivation of the regression $t$-posterior) and Section 3.5 of Shumway and Stoffer,
  *Time Series Analysis and its Applications* (4th edition), for the asymptotic sampling
  distribution behind frequentist AR inference. Neither is reproduced here.

---

[← 100. Discrete Fourier Transform and Periodogram](100-discrete-fourier-transform-and-periodogram.md) · [Contents](index.md) · [102. Ridge and LASSO Trend Filtering →](102-ridge-and-lasso-trend-filtering.md)
