---
title: "47. AR(p) Estimation and Forecasting (part 1)"
course: "Berkeley Stat 153"
chapter: 47
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 47. AR(p) Estimation and Forecasting (part 1)

## What this covers

Given a fitted AR($p$) model, two practical questions remain: how do we actually get the
coefficient estimates and their standard errors out of a computer, and what do the resulting
forecasts look like? This chapter works through both, using four real and simulated datasets. It
assumes the reader already has the AR($p$) model itself,
$$y_t = \phi_0 + \phi_1 y_{t-1} + \cdots + \phi_p y_{t-p} + \epsilon_t, \qquad \epsilon_t \overset{iid}{\sim} N(0,\sigma^2),$$
knows what stationarity of such a process means, and has seen ordinary least squares regression.

## The AR($p$) regression setup

An AR($p$) model can be fit by ordinary regression once the data is arranged correctly. From
$y_1,\dots,y_n$, build the response vector and design matrix
$$Y = \begin{pmatrix} y_{p+1}\\ y_{p+2}\\ \vdots\\ y_n\end{pmatrix}, \qquad
X = \begin{pmatrix} 1 & y_p & y_{p-1} & \cdots & y_1\\
1 & y_{p+1} & y_p & \cdots & y_2\\
\vdots & \vdots & \vdots & & \vdots\\
1 & y_{n-1} & y_{n-2} & \cdots & y_{n-p}\end{pmatrix},$$
so that row $t-p$ of $X$ holds $(1, y_{t-1}, \dots, y_{t-p})$ for $t = p+1,\dots,n$. Ordinary least
squares of $Y$ on $X$, $\hat\phi = (X^\top X)^{-1}X^\top Y$, gives estimates
$\hat\phi_0,\hat\phi_1,\dots,\hat\phi_p$. These are called **conditional least squares** or
**conditional MLE** estimates — "conditional" because the first $p$ observations $y_1,\dots,y_p$
are treated as fixed rather than as data contributing their own likelihood term.

## Fitting AR(1) to US population: two routes to the same numbers

The first worked example fits an AR(1) to the FRED monthly US population series (`POPTHM`), $n=799$
months. Building $X$ and $Y$ by hand as above and running `statsmodels`' `OLS` gives
$$\hat\phi_0 = 227.606, \qquad \hat\phi_1 = 0.99993.$$
The estimated $\hat\phi_1$ is essentially $1$: population is close to following a random walk with
a small positive drift $\hat\phi_0$, which is exactly what steady month-on-month growth looks like.

`statsmodels` also has a purpose-built function, `AutoReg`, that fits AR($p$) models directly
without the user constructing $X$ and $Y$. Run on the same series it returns the *same* point
estimates, $\hat\phi_0 = 227.606$, $\hat\phi_1 = 0.99993$ — unsurprising, since both routes solve
the same least-squares problem — but its label for the fitting method is "Conditional MLE" rather
than "OLS", and its reported standard errors are slightly different from the OLS ones. That gap is
worth pinning down exactly, because it is easy to fit a model two ways, get numbers that nearly but
not quite agree, and not know whether that is a bug or is expected.

## Two estimates of $\sigma$, two sets of standard errors

Both routes compute standard errors as square roots of the diagonal of $\hat\sigma^2(X^\top X)^{-1}$
— the only difference is which $\hat\sigma$ they plug in.

- **OLS** uses the usual unbiased regression estimate, dividing the residual sum of squares by the
  residual degrees of freedom. With $n-p$ observations in the regression and $p+1$ estimated
  coefficients, that is
  $$\hat\sigma_{\text{OLS}} = \sqrt{\frac{\mathrm{RSS}}{(n-p)-(p+1)}} = \sqrt{\frac{\mathrm{RSS}}{n-2p-1}}.$$
  For the population data ($p=1$), $\hat\sigma_{\text{OLS}} = 51.229$, and the corresponding
  standard errors are $(9.7277,\ 3.678\times10^{-5})$ for $(\hat\phi_0,\hat\phi_1)$ — this is what
  `OLS.bse` reports, and inference off it uses a $t$-distribution, exactly as in ordinary linear
  regression. (The lecture notes in passing that this $t$-based inference for the AR model can be
  justified through a Bayesian argument that treats $y_1$ as a fixed constant; that argument is not
  worked out here.)
- **`AutoReg`**, following the (conditional) maximum-likelihood route, divides by the number of
  residuals with no correction for the estimated parameters:
  $$\hat\sigma_{\text{MLE}} = \sqrt{\frac{\mathrm{RSS}}{n-p}}.$$
  For the population data this gives $\hat\sigma_{\text{MLE}} = 51.165$, and standard errors
  $(9.7155,\ 3.674\times10^{-5})$ — close to the OLS values but not identical, because $n-p$ is a
  slightly smaller denominator's reciprocal effect than $n-2p-1$... in this case $n - p = 798$
  versus $n-2p-1 = 796$, so $\hat\sigma_{\text{MLE}} < \hat\sigma_{\text{OLS}}$ and the MLE-based
  standard errors are slightly smaller. `AutoReg` inference is based on the normal distribution
  (an asymptotic argument) rather than the $t$-distribution.

So: identical point estimates $\hat\phi$ from both routes, because both solve the same
least-squares problem; standard errors that agree to two or three significant figures but not
exactly, because the two conventions divide the same residual sum of squares by different
denominators. Knowing this in advance saves the confusion of thinking two model fits disagree when
they only used two conventions for the noise variance.

## Generating multi-step forecasts by recursion

Once $\hat\phi_0,\dots,\hat\phi_p$ are in hand, a $k$-step-ahead forecast is produced by
plugging the model's own point forecasts back into the recursion:
$$\hat y_{n+i} = \hat\phi_0 + \sum_{j=1}^{p} \hat\phi_j\, \hat y_{n+i-j}, \qquad i = 1,\dots,k,$$
where $\hat y_{n+i-j}$ is the observed value $y_{n+i-j}$ whenever $n+i-j \le n$, and a previously
computed forecast otherwise. This is exactly what `AutoReg`'s `.predict()` method does internally;
the lecture verifies this directly by coding the recursion by hand and checking that the two sets
of forecasts coincide.

Applied to the FRED annual California population series (`CAPOP`, $n=125$, 1900 onward), an AR(1)
fit gives $\hat\phi_0 = 236.66$, $\hat\phi_1 = 1.0038$ — again close to, but now just over, $1$.
Because $\hat\phi_1 > 1$, the recursion is explosive: extending the forecast $k=100$ steps ahead
shows visibly exponential growth. With a short horizon the curve looks nearly linear, and the
exponential shape only becomes obvious once $k$ is made large — a caution about eyeballing a short
forecast plot and concluding a trend is linear.

## Order matters: an overfit AR(25)

Refitting the same California series with $p=25$ instead of $p=1$ raises the log-likelihood sharply
(from $-828.9$ at $p=1$ to $-601.6$ at $p=25$), which is expected: 26 free parameters fit 125 data
points far more closely than 2 do. But most of the 25 lag coefficients are individually far from
significant, several of the model's estimated characteristic roots sit almost exactly on the unit
circle (modulus $0.9987$, for instance), and the resulting forecasts *decrease* into the future
rather than growing — the opposite of the AR(1) fit on the same data. With $n=125$ and $p=25$, the
model is overfitting, and its extrapolations should not be trusted even though its in-sample fit is
far better.

## Why $\hat\phi_1$ matters so much: three forecast regimes

The California example landed on $\hat\phi_1$ slightly above $1$ almost by chance. To see how much
that placement matters, the lecture simulates data explicitly from an AR(1) recursion with
$\phi_0 = 0.1$, $\phi_1 = 1$ exactly (a random walk with drift) and Gaussian noise of scale
$\sigma=0.5$, $n=400$, run twice with different random seeds.

- With seed 43, the fitted model gives $\hat\phi_1 = 1.0021$ — just over $1$ — and forecasting
  $k=1000$ steps ahead produces the same exponential blow-up seen in the population data.
- With seed 123 (same true $\phi_1=1$, same generating process), the fitted model instead gives
  $\hat\phi_1 = 0.9974$ — just under $1$ — and now the $1000$-step forecast *converges to a
  constant* instead of exploding. (The fixed point of $y = \hat\phi_0 + \hat\phi_1 y$ is
  $\hat\phi_0/(1-\hat\phi_1)$, which is where the recursion settles once $|\hat\phi_1|<1$.)

Both datasets were generated with the *same* true $\phi_1 = 1$; only sampling noise decided which
side of $1$ the estimate landed on. Near the unit root, an estimation error of a few thousandths
in $\hat\phi_1$ is the difference between a forecast that diverges, one that grows linearly forever,
and one that flattens out — three qualitatively different long-run pictures from what looks, on a
$t$-statistic, like a very precisely estimated coefficient. Forcing $\hat\phi_1$ to its true value
of exactly $1$ in the recursion (keeping the estimated $\hat\phi_0$) restores linear forecasts in
both simulated datasets, confirming that the divergence in shape came entirely from which side of
the unit root the point estimate fell on, not from any other feature of the fit.

<figure>
<svg viewBox="0 0 420 220" role="img" aria-label="Three qualitatively different AR(1) forecast shapes depending on the estimated phi one, all extending from the same observed history">
  <line x1="40" y1="190" x2="400" y2="190" stroke="currentColor" stroke-width="1.2"/>
  <text x="400" y="205" text-anchor="end" font-size="12" fill="currentColor">time</text>
  <polyline points="40,150 70,130 100,145 130,120 160,135 190,110 220,120" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="220" y1="30" x2="220" y2="190" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="220" y="20" text-anchor="middle" font-size="11" fill="currentColor">forecast start</text>
  <path d="M220,120 C280,105 320,80 380,15" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <text x="384" y="18" font-size="12" fill="currentColor">phi&#770;&#8321; &#62; 1</text>
  <line x1="220" y1="120" x2="380" y2="78" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5,3"/>
  <text x="384" y="80" font-size="12" fill="currentColor">phi&#770;&#8321; = 1</text>
  <path d="M220,120 C260,133 320,140 380,141" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <text x="384" y="145" font-size="12" fill="currentColor">phi&#770;&#8321; &#60; 1</text>
  <text x="34" y="14" font-size="11" fill="currentColor" text-anchor="start">observed data</text>
</svg>
<figcaption>Three AR(1) fits to data generated from the same unit-root process, differing only in
which side of $\hat\phi_1 = 1$ the estimate fell on: forecasts that explode, grow linearly forever,
or converge to a constant.</figcaption>
</figure>

## AR(2) can oscillate

An AR(1) forecast, whatever its long-run shape, moves monotonically once past the last observed
values — it grows, decays, or holds steady, but it never swings up and down. An AR(2) forecast can.
Fitting AR(2) to an annual sunspot count series (`SN_y_tot_V2.0.csv`, $n=325$) gives
$$\hat\phi_0 = 24.456, \qquad \hat\phi_1 = 1.388, \qquad \hat\phi_2 = -0.6965,$$
with estimated characteristic roots $0.9965 \pm 0.6655i$ — a complex-conjugate pair, modulus
$1.1983$ and reported frequency $0.0937$ (so a cycle roughly every $1/0.0937 \approx 10.7$ time
steps). Forecasting forward from this fit produces predictions that visibly oscillate, something
no AR(1) fit can do since it has only ever a single, real characteristic root. (For contrast, the
non-stationary California AR(1) fit above had a real root of modulus $0.9962$, just inside the unit
circle — no oscillation, only monotone explosion.)

The lecture flags the oscillation as a phenomenon to explain rather than explaining it fully here:
the formulas for AR(2) predictions that account for the oscillating behaviour — presumably relating
it to the complex roots — are deferred to the next lecture and are not derived in this one.

## Sources

- Berkeley STAT 153, Fall 2025, *Code Lecture 17* — `CodeLectureSeventeen153248Fall2025.ipynb`
  (converted notebook, CC BY 4.0):
  `docs/statistics/berkeley/stat153/fall-2025/CodeLectureSeventeen153248Fall2025.md`.
  Source of the US population AR(1) fit, the OLS-versus-`AutoReg` comparison, and the two
  standard-error formulas.
- Berkeley STAT 153, Spring 2025, same code lecture (a different year's pass over the same
  material), split into three notebook sections:
  `01-dataset-one-california-population.md`
  (California population: OLS/`AutoReg` fitting, recursive forecasting, the AR(25) overfitting
  example),
  `02-dataset-two-simulated-dataset.md`
  (the two seeded simulations illustrating the three forecast regimes near $\phi_1=1$), and
  `03-dataset-three-sunspots.md`
  (the AR(2) sunspots example and its oscillating forecasts).
- No slides or spoken transcript were supplied for this lecture; the notebooks are the only
  material. No problem set was supplied, so no Exercises section is included.
- Both notebooks refer to a "next lecture" that will give formulas explaining AR(2) oscillating
  predictions in more depth, and the Bayesian justification for treating AR(1) regression inference
  as $t$-distributed; neither is contained in the material supplied here.

---

[← 46. Sinusoidal Regression and the DFT](46-sinusoidal-regression-and-the-dft.md) · [Contents](index.md) · [48. Profile RSS: Changepoints and the Periodogram →](48-profile-rss-changepoints-and-the-periodogram.md)
