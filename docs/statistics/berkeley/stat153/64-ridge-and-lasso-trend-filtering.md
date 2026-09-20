---
title: "64. Ridge and Lasso Trend Filtering"
course: "Berkeley Stat 153 Fall 2024"
chapter: 64
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 64. Ridge and Lasso Trend Filtering

## What this covers

This chapter asks: if you let a time series trend be an entirely flexible piecewise-linear curve
with as many "kinks" as there are data points, how do you keep the fit from just interpolating the
noise, and what is the real difference between penalizing the kinks with an $\ell_2$ penalty versus
an $\ell_1$ penalty? It assumes the reader already knows ordinary least squares and has met ridge
regression and the LASSO as penalized least-squares problems, just not yet in a time-series
setting.

## A trend with a kink at every time point

For a time series $y_1,\dots,y_n$, model
$$y_t = \mu_t + \varepsilon_t, \qquad \varepsilon_t \overset{\text{iid}}{\sim} N(0,\sigma^2),$$
where $\mu_t$ is a slowly varying trend to be estimated. Build $\mu_t$ out of a piecewise-linear
basis with a possible change of slope ("kink") at every interior time point $2,\dots,n-1$:

$$\mu_t = \beta_0 + \beta_1(t-1) + \beta_2\,\mathrm{ReLU}(t-2) + \beta_3\,\mathrm{ReLU}(t-3) + \dots + \beta_{n-1}\,\mathrm{ReLU}(t-(n-1)),$$

with $\mathrm{ReLU}(x)=\max(x,0)$. Each term $\beta_j\,\mathrm{ReLU}(t-j)$ is zero until $t$ reaches
$j$ and only then starts adding slope, so $\beta_j$ controls how much extra bend the trend picks up
from time $j$ onward. Writing $y = X\beta + \varepsilon$, the design matrix has one column per
basis function, so this model has $n$ parameters $\beta_0,\dots,\beta_{n-1}$ for $n$ observations —
as many free parameters as data points. That is why the lecture calls it "high-dimensional" even
though $p=n$ rather than $p>n$: with a full complement of kinks, ordinary least squares has no
degrees of freedom left over to separate signal from noise.

For $n=4$, for instance, the design matrix is
$$X = \begin{bmatrix} 1&0&0&0\\ 1&1&0&0\\ 1&2&1&0\\ 1&3&2&1 \end{bmatrix},$$
lower triangular with $1$'s on the diagonal, hence invertible — and the same triangular structure
holds for any $n$, so $X\beta = y$ always has an exact solution.

## Unregularized fit: the model just interpolates

Because $X$ is square and invertible, the least-squares fit $\hat\beta = X^{-1}y$ satisfies
$\hat\mu_t = y_t$ exactly at every $t$: the "estimated trend" is just the data back again. The
recursion for $\beta$ makes this concrete. Reading the model off row by row, $\mu_1=\beta_0$,
$\mu_2=\beta_0+\beta_1$, $\mu_3=\beta_0+2\beta_1+\beta_2$, and in general each new $\beta_j$ for
$j\ge2$ is the *change in slope* of $\mu$ at time $j$:
$$\beta_0=\mu_1,\qquad \beta_1=\mu_2-\mu_1,\qquad \beta_j = (\mu_{j+1}-\mu_j)-(\mu_j-\mu_{j-1})\ \ (j=2,\dots,n-1).$$
So $\beta_j$ is the discrete second derivative of the trend at $j$: zero exactly where the trend
keeps going in a straight line through $j$, nonzero exactly where it kinks.

Since unregularized least squares forces $\hat\mu_t=y_t$, plugging the raw data straight into this
same recursion gives the fitted coefficients:
$$\hat\beta_0=y_1,\qquad \hat\beta_1=y_2-y_1,\qquad \hat\beta_j=(y_{j+1}-y_j)-(y_j-y_{j-1}).$$
A trend with a free kink at every point interpolates the data and has no smoothing effect
whatsoever — which is exactly why this basis is only useful once it is regularized.

## Penalizing the kinks: ridge and LASSO

Since $\beta_2,\dots,\beta_{n-1}$ are the changes in slope, penalizing them is exactly penalizing
how much the trend is allowed to bend. Two choices of penalty:

**Ridge** ($\ell_2$ on the kinks):
$$\hat\beta^{\text{ridge}}(\lambda) = \operatorname*{argmin}_\beta \left[\|y-X\beta\|^2 + \lambda\sum_{j=2}^{n-1}\beta_j^2\right].$$

**LASSO** ($\ell_1$ on the kinks):
$$\hat\beta^{\text{LASSO}}(\lambda) = \operatorname*{argmin}_\beta \left[\|y-X\beta\|^2 + \lambda\sum_{j=2}^{n-1}|\beta_j|\right].$$

Neither penalizes $\beta_0$ or $\beta_1$ — the overall level and initial slope stay free; only the
*changes* in slope are shrunk. Both share the same two limits:

- $\lambda=0$: no penalty, so both reduce to the unregularized fit — the trend interpolating every
  data point, with $\hat\beta_j$ the raw second differences of $y$ derived above.
- $\lambda\to\infty$: the penalty forces every $\beta_j$ ($j\ge2$) to zero, leaving only $\beta_0$
  and $\beta_1$ — the trend collapses to a single straight line, and $(\hat\beta_0,\hat\beta_1)$ is
  exactly the ordinary simple linear regression of $y$ on the time index $t$:
  $$\left(\bar y - \hat\beta_1\bar t,\ \ \frac{\sum_i (y_i-\bar y)(t_i-\bar t)}{\sum_i(t_i-\bar t)^2}\right).$$

So $\lambda$ interpolates between "fit every wiggle" and "fit a single line," and in either case the
fitted trend is $\hat\mu(\lambda) = X\hat\beta(\lambda)$.

## Rewriting the penalty in terms of the trend itself

Because $\beta_j$ is the second difference of $\mu$, both problems can be restated directly in
terms of the trend values $\{\mu_t\}$ instead of the basis coefficients — the more transparent way
to see what each one is actually doing:

$$\hat\mu^{\text{ridge}}(\lambda) = \operatorname*{argmin}_{\{\mu_t\}} \left[\sum_t (y_t-\mu_t)^2 + \lambda\sum_{j=2}^{n-1}\big((\mu_{j+1}-\mu_j)-(\mu_j-\mu_{j-1})\big)^2\right],$$

$$\hat\mu^{\text{LASSO}}(\lambda) = \operatorname*{argmin}_{\{\mu_t\}} \left[\sum_t (y_t-\mu_t)^2 + \lambda\sum_{j=2}^{n-1}\big|(\mu_{j+1}-\mu_j)-(\mu_j-\mu_{j-1})\big|\right].$$

Both trade off fit to the data against a roughness penalty on the discrete second derivative of the
trend — i.e., against how far the trend departs from growing "at a constant rate on average,"
$\mu_{t+1}-\mu_t \approx \mu_t-\mu_{t-1}$. They differ only in whether that roughness penalty is
$\ell_2$ or $\ell_1$, and the difference turns out to matter a great deal.

- The **ridge** version penalizes the *sum of squares* of the second differences — the discrete
  analogue of penalizing curvature everywhere. The same optimization goes by other names elsewhere:
  the **Hodrick–Prescott filter** used to extract business-cycle trends in economics, and (in
  continuous time) **cubic spline smoothing**. It has a closed form, since the objective is
  quadratic in $\mu$.
- The **LASSO** version penalizes the *sum of absolute values* of the second differences, known as
  **trend filtering**. It has no closed form — the objective is still convex, but piecewise-linear
  rather than quadratic — and is solved numerically, e.g. with a convex-optimization package such as
  `cvxpy`.

## Choosing $\lambda$ by cross-validation

$\lambda$ is chosen the same way as in ordinary regularized regression, with one adjustment for
time order: since the data form a sequence, the train/test split is not a random shuffle but
respects time — e.g. the first 80% of the series as $T_{\text{train}}$ and the last 20% as
$T_{\text{test}}$.

For each candidate $\lambda$: fit $\hat\beta^{\text{ridge, train}}(\lambda)$ by minimizing the ridge
objective using only the residuals at $t\in T_{\text{train}}$ (still with the full penalty on
$\beta_2,\dots,\beta_{n-1}$), then use the fitted coefficients to predict every held-out time
$t\in T_{\text{test}}$:
$$\hat y_t(\lambda) = \hat\beta_0^{\text{ridge,train}}(\lambda) + \hat\beta_1^{\text{ridge,train}}(\lambda)(t-1) + \dots + \hat\beta_{n-1}^{\text{ridge,train}}(\lambda)\,\mathrm{ReLU}(t-(n-1)),$$
$$\mathrm{MSE}(\lambda,\text{split}) = \sum_{t\in T_{\text{test}}}\big(y_t-\hat y_t(\lambda)\big)^2.$$

Repeating this over several splits $\text{split}_1,\dots,\text{split}_S$ and summing,
$$\mathrm{MSE}(\lambda,\text{all splits}) = \sum_{i=1}^S \mathrm{MSE}(\lambda,\text{split}_i),$$
gives one number per candidate $\lambda$. The notes suggest scanning a wide log-spaced grid,
$\lambda \in \{10^{-6},10^{-5},\dots,10^{6},10^{7}\}$, and picking whichever minimizes total
held-out error. The same procedure applies to LASSO trend filtering.

## Why LASSO can zero out a coefficient and ridge cannot

The trend-filtering objective is complicated, but the reason an $\ell_1$ penalty produces
genuinely sparse second differences — a few real kinks — while an $\ell_2$ penalty only shrinks all
of them a little, is already visible in the single-coordinate case: one observation
$y\in\mathbb{R}$, one parameter $\beta$.

**Ridge.** Minimize $(y-\beta)^2 + \lambda\beta^2$. Differentiating and setting the result to zero,
$-2(y-\beta) + 2\lambda\beta = 0$, so
$$\hat\beta = \frac{y}{1+\lambda}.$$
This is a straight-line shrinkage: $\hat\beta$ is always a fixed fraction of $y$, and it is zero
only when $y$ itself is.

**LASSO.** Minimize $(y-\beta)^2 + \lambda|\beta|$. The penalty is not differentiable at $\beta=0$,
so split into cases. For $\beta>0$ the derivative is $2\beta - 2y + \lambda$, giving
$\beta = y-\lambda/2$, valid only when this is actually positive, i.e. $y>\lambda/2$. Symmetrically,
for $\beta<0$, $\beta = y+\lambda/2$ is valid when $y<-\lambda/2$. In between, $\beta=0$ is itself
the minimizer whenever $0$ lies in the subdifferential of the objective there, which works out to
$-\lambda/2 \le y \le \lambda/2$. Altogether,
$$\hat\beta = \begin{cases} y-\dfrac{\lambda}{2} & y>\dfrac{\lambda}{2}\\[4pt] 0 & -\dfrac{\lambda}{2}\le y\le \dfrac{\lambda}{2}\\[4pt] y+\dfrac{\lambda}{2} & y<-\dfrac{\lambda}{2}\end{cases}$$
— the **soft-thresholding** operator, written $S_{\lambda/2}(y)$.

<figure>
<svg viewBox="0 0 320 240" role="img" aria-label="Ridge shrinkage and LASSO soft-thresholding as functions of a single input, compared to the unregularized line">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="40" y1="130" x2="290" y2="130" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="160" y1="230" x2="160" y2="20" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="296" y="134" font-size="12" fill="currentColor">y</text>
  <text x="140" y="16" font-size="12" fill="currentColor">&#946;</text>
  <line x1="60" y1="230" x2="260" y2="30" stroke="currentColor" stroke-width="1.1" stroke-dasharray="4 3"/>
  <line x1="60" y1="165" x2="260" y2="95" stroke="currentColor" stroke-width="1.5"/>
  <polyline points="60,205 135,130 185,130 260,55" stroke="currentColor" stroke-width="2.2" fill="none"/>
  <line x1="135" y1="127" x2="135" y2="133" stroke="currentColor" stroke-width="1"/>
  <line x1="185" y1="127" x2="185" y2="133" stroke="currentColor" stroke-width="1"/>
  <text x="135" y="146" text-anchor="middle" font-size="11" fill="currentColor">-&#955;/2</text>
  <text x="185" y="146" text-anchor="middle" font-size="11" fill="currentColor">&#955;/2</text>
  <text x="160" y="160" text-anchor="middle" font-size="11" fill="currentColor">&#946; = 0 here</text>
  <text x="264" y="26" font-size="11" fill="currentColor">unregularized</text>
  <text x="264" y="53" font-size="11" fill="currentColor">LASSO</text>
  <text x="264" y="95" font-size="11" fill="currentColor">ridge</text>
</svg>
<figcaption>Ridge's shrinkage rule is a straight line through the origin: it reaches $\hat\beta=0$
only at the single point $y=0$. LASSO's soft-threshold is flat on the whole interval
$|y|\le\lambda/2$, mapping a range of inputs to exactly zero. That flat interval is what lets an
$\ell_1$ penalty on the trend's second differences kill a kink outright at a finite $\lambda$,
where an $\ell_2$ (ridge) penalty only ever shrinks it.</figcaption>
</figure>

Carrying this back to trend filtering: an $\ell_1$ penalty on the second differences of $\mu$ sends
whole ranges of them to exactly zero at a finite $\lambda$, producing a trend that is genuinely
piecewise linear with a sparse set of real kinks. The ridge/Hodrick–Prescott penalty, built from
the same shrinkage rule coordinate by coordinate, only ever shrinks every second difference
continuously and never removes a kink outright.

## Sources

- Handwritten lecture notes, Berkeley STAT 153, Fall 2025, "Lecture Eleven":
  `docs/statistics/berkeley/stat153/fall-2025/HandwrittenNotesLectureEleven153248Fall2025.md`
  in the library repository. This was the only material supplied for this chapter — no slide deck,
  transcript, or problem set accompanied it. The source file is itself a model's reconstruction of
  a handwritten PDF with no text layer, and its header flags the prose as paraphrase and every
  equation as unverified; the worked additions here (the $n=4$ design matrix, the derivation of the
  soft-thresholding formula) are standard completions of the results the notes state, not drawn
  from any further source.
- The notes mention a proof of the soft-thresholding formula as being available "in notes" without
  reproducing it; the case-by-case derivation given above reconstructs that argument, since the
  original proof was referred to but not part of the supplied material.

---

[← 63. AR(p) Estimation and Multistep Forecasting](63-ar-p-estimation-and-multistep-forecasting.md) · [Contents](index.md) · [65. Posterior of Multiple Regression Coefficients →](65-posterior-of-multiple-regression-coefficients.md)
