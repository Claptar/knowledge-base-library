---
title: "95. Inference in Nonlinear Regression Models"
course: "Berkeley Stat 153"
chapter: 95
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 95. Inference in Nonlinear Regression Models

## What this covers

Three models in this chapter share a shape: linear in most of their parameters, but nonlinear in
one scalar — an unknown frequency, an unknown time at which a series changes level or slope. The
chapter answers how to get both a point estimate of that scalar and an honest picture of the
uncertainty in it, using one recipe applied three times: a sinusoid with unknown frequency, a
step change in level, and a change of slope in a real time series. It assumes ordinary least
squares and maximum likelihood, and enough Bayesian machinery to recognize a posterior density, a
$\chi^2$ distribution, and a multivariate normal. It builds directly on an earlier lab (not
included here) that first set up the sinusoid model and estimated its frequency from a
periodogram.

## Models that are linear once one number is fixed

The three models are

$$y_t = \beta_0 + \beta_1\cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t \qquad \text{(sinusoid, unknown frequency $f$)}$$

$$y_t = \beta_0 + \beta_1 I\{t>c\} + \epsilon_t \qquad \text{(change-point, unknown time $c$)}$$

$$y_t = \beta_0 + \beta_1 t + \beta_2 (t-c)_+ + \epsilon_t, \quad (t-c)_+ := \max(t-c,0) \qquad \text{(change of slope, unknown time $c$)}$$

Call the scalar that enters nonlinearly $\theta$ — it is $f$ in the first model, $c$ in the other
two. For a *fixed* value of $\theta$, each equation is an ordinary linear regression: write
$X_\theta$ for the design matrix built from that value (columns $1,\cos(2\pi ft),\sin(2\pi ft)$ for
the sinusoid; $1, I\{t>c\}$ for the step; $1, t, (t-c)_+$ for the broken stick). All of the
nonlinearity in the model lives in $\theta$ — once $\theta$ is known, $\beta$ and $\sigma$ are
estimated by ordinary least squares.

## Profiling out $\beta$: the RSS curve

Define the **profile residual sum of squares**

$$\mathrm{RSS}(\theta) = \min_\beta \sum_{t=1}^n \big(y_t - x_t(\theta)^\top \beta\big)^2,$$

i.e. run OLS with design matrix $X_\theta$ and record the residual sum of squares it leaves behind.
Because $\beta$ has already been minimized out, $\mathrm{RSS}(\theta)$ is a function of $\theta$
alone, and

$$\hat\theta = \arg\min_\theta \mathrm{RSS}(\theta)$$

is the maximum likelihood estimate of $\theta$: minimizing over $\theta$ after already minimizing
over $\beta$ is the same computation as jointly maximizing the Gaussian likelihood over both. In
practice $\hat\theta$ is found by evaluating $\mathrm{RSS}(\theta)$ on a grid and taking the
minimizer — there is no closed form because $\theta$ enters nonlinearly. Once $\hat\theta$ is in
hand, plugging it into the design and running OLS once more gives $\hat\beta$, and the residual sum
of squares at $\hat\theta$ gives two estimates of $\sigma$: the MLE
$\hat\sigma = \sqrt{\mathrm{RSS}(\hat\theta)/n}$, and the usual unbiased version with $n-p$ in the
denominator, $p$ being the number of columns of $X_\theta$.

## Worked example: an unknown frequency

Data were simulated with $f = 0.2035$, $n=400$, $(\beta_0,\beta_1,\beta_2) = (0,3,5)$ and
$\sigma = 10$. Minimizing $\mathrm{RSS}(f)$ over a dense grid of $100{,}000$ points on $[0, 0.5]$
gives $\hat f = 0.20355$, extremely close to the truth. There is a cheaper alternative: evaluate
the periodogram only at the $n/2$ **Fourier frequencies** $f_j = j/n$, computed in a single FFT
rather than as $n/2$ separate regressions, and take the maximizer. Here that gives
$\hat f_{\text{fft}} = 0.2025$ — visibly worse, because the true frequency does not happen to sit
exactly on the Fourier grid. Except in the rare case where it does, the dense-grid MLE is more
accurate; the Fourier-frequency estimate is far cheaper to compute. Plugging $\hat f = 0.20355$
into OLS recovers $(\hat\beta_0,\hat\beta_1,\hat\beta_2) \approx (-0.053,\, 3.00,\, 5.64)$ against
the true $(0,3,5)$, and $\hat\sigma \approx 9.50$ (MLE) or $9.54$ (unbiased) against the true
$\sigma=10$.

## A posterior for the nonlinear parameter

A point estimate says nothing about how far $\hat\theta$ could plausibly be off. The lab states,
without re-deriving it here, a marginal posterior density for $\theta$ alone, after integrating
$\beta$ and $\sigma$ out:

$$\pi(\theta \mid \text{data}) \;\propto\; \mathbb{1}\{\theta \in \Theta\}\cdot |X_\theta^\top
X_\theta|^{-1/2} \cdot \Big(\frac{1}{\mathrm{RSS}(\theta)}\Big)^{(n-p)/2}.$$

For the sinusoid $\Theta = [0, 1/2]$; for the other two models $\Theta$ is the interior of the
observed time range. Two computational points recur across all three examples.

**Work with the log posterior.** Raising a residual sum of squares to the power $(n-p)/2$, with $n$
in the hundreds or thousands, overflows or underflows in floating point long before it becomes
informative. The lab instead computes
$\log\pi(\theta) = \tfrac{p-n}{2}\log\mathrm{RSS}(\theta) - \tfrac12\log|X_\theta^\top X_\theta|$
on the grid, subtracts its maximum, and only then exponentiates and normalizes — a log-sum-exp
trick that never has to exponentiate a number larger than $1$.

**Exclude $\theta$ near the edge of $\Theta$.** Wherever $\theta$ pushes the design toward
collinearity, $|X_\theta^\top X_\theta|\to 0$ and $|X_\theta^\top X_\theta|^{-1/2}$ blows up,
producing spurious posterior mass that has nothing to do with the fit. For the sinusoid this
happens exactly at $f=0$, where $\cos(2\pi f t)\equiv 1$ duplicates the intercept column, and at
$f=1/2$, where $\sin(\pi t)\equiv 0$ for every integer $t$; the lab therefore grids over
$f\in[0.05, 0.35]$, guided by where the periodogram peaks, rather than over all of $[0,1/2]$. The
change-point and broken-stick grids trim a handful of points from each end of the series in the
same way, running from $5$ to $n-4$ rather than over the full range — the notebook does not spell
out why, but the risk being guarded against is the same one: too close to either edge, a column of
$X_c$ becomes (nearly) constant on the remaining data and $X_c^\top X_c$ is again close to
singular.

Given a grid of posterior values normalized to sum to one, a posterior sample of $\theta$ is a
weighted draw from that grid. Two more draws complete a full posterior sample of every parameter,
chained together using two standard facts about the Gaussian linear model — the first is the
result proved in Problem 4 of Homework 1, not included in this lab:

$$\frac{\mathrm{RSS}(\theta)}{\sigma^2}\ \Big|\ \text{data},\theta \;\sim\; \chi^2_{n-p},
\qquad
\beta \mid \text{data}, \sigma, \theta \;\sim\; N_p\big(\hat\beta_\theta,\, \sigma^2
(X_\theta^\top X_\theta)^{-1}\big).$$

So each posterior draw is built in sequence: draw $\theta$ from the grid, draw $\sigma$ from the
scaled inverse-$\chi^2$ conditional on that $\theta$, then draw $\beta$ from the normal conditional
on both $\theta$ and $\sigma$. Repeating this a few thousand times and overlaying the resulting
fitted curves on the data turns a single best-fit curve into a band of plausible curves — a direct
picture of how much the fit could vary given the noise.

For the sinusoid, $2000$ such draws give a posterior for $f$ with mean $\approx 0.2036$ and
standard deviation $\approx 0.00015$ — the frequency is pinned down extremely tightly — while
$\beta_1,\beta_2,\sigma$ show the wider spread expected from ordinary regression noise (posterior
means $\approx (-0.05,\,2.93,\,5.49)$ for $\beta_0,\beta_1,\beta_2$ and $\approx 9.57$ for
$\sigma$, close to the true $(0,3,5,10)$).

## Two shapes for a change: level jump and slope change

The change-point and broken-stick models use exactly the same machinery above but pivot the mean
function differently at the unknown time $c$. The step model holds the series at level $\beta_0$
until $c$ and jumps it to $\beta_0+\beta_1$ immediately after; the broken-stick model keeps the
series continuous but bends it, with slope $\beta_1$ up to $c$ and slope $\beta_1+\beta_2$ after.

<figure>
<svg viewBox="0 0 620 240" role="img" aria-label="A step change in level next to a change in slope, each pivoting at an unknown time c">
  <line x1="30" y1="210" x2="290" y2="210" stroke="currentColor" stroke-width="1"/>
  <line x1="30" y1="150" x2="150" y2="150" stroke="currentColor" stroke-width="2"/>
  <line x1="150" y1="70" x2="290" y2="70" stroke="currentColor" stroke-width="2"/>
  <line x1="150" y1="150" x2="150" y2="70" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="150" y1="210" x2="150" y2="216" stroke="currentColor" stroke-width="1"/>
  <text x="150" y="230" text-anchor="middle" font-size="12" fill="currentColor">c</text>
  <text x="34" y="142" font-size="12" fill="currentColor">&#946;&#8320;</text>
  <text x="248" y="62" font-size="12" fill="currentColor">&#946;&#8320;+&#946;&#8321;</text>
  <text x="160" y="18" text-anchor="middle" font-size="12" fill="currentColor">change-point</text>

  <line x1="340" y1="210" x2="600" y2="210" stroke="currentColor" stroke-width="1"/>
  <line x1="340" y1="180" x2="465" y2="110" stroke="currentColor" stroke-width="2"/>
  <line x1="465" y1="110" x2="600" y2="30" stroke="currentColor" stroke-width="2"/>
  <line x1="465" y1="210" x2="465" y2="216" stroke="currentColor" stroke-width="1"/>
  <text x="465" y="230" text-anchor="middle" font-size="12" fill="currentColor">c</text>
  <text x="345" y="172" font-size="12" fill="currentColor">slope &#946;&#8321;</text>
  <text x="495" y="58" font-size="12" fill="currentColor">slope &#946;&#8321;+&#946;&#8322;</text>
  <text x="470" y="18" text-anchor="middle" font-size="12" fill="currentColor">change of slope</text>
</svg>
<figcaption>Left: the change-point model — the level jumps from &#946;&#8320; to &#946;&#8320;+&#946;&#8321;
at the unknown time c. Right: the change-of-slope (broken-stick) model — the series stays
continuous, but its slope changes from &#946;&#8321; to &#946;&#8321;+&#946;&#8322; at the same
kind of unknown c.</figcaption>
</figure>

### A jump in level

Data were simulated with $n=10{,}000$, level $\mu_1=0$ for the first half of the series and
$\mu_2=0.4$ for the second half (so $\beta_0=0,\beta_1=0.4$), and $\sigma=1$. Minimizing
$\mathrm{RSS}(c)$ over integers $c=5,\dots,n-4$ gives $\hat c = 4981$, close to the true change at
$t=5000$. Plugging that in: $\hat\beta_0\approx 0.0197$, $\hat\beta_1\approx 0.4087$ (true $0,\,0.4$),
$\hat\sigma\approx 1.003$ (true $1$).

Applying the same Bayesian recipe (here $p=2$) and drawing $N=1000$ posterior samples gives a
posterior for $c$ with mean $4990.7$ and standard deviation $10.0$ — the change-point is located to
within about ten time steps out of ten thousand — while $\beta_0,\beta_1,\sigma$ show the spread
expected from noisy data (posterior means $\approx (-0.007,\,0.413,\,1.003)$).

### A change of slope in a real series

The same idea applied to a real series — monthly US population — rather than simulated data, so
there is no "true" change-point to check against. Minimizing $\mathrm{RSS}(c)$ over the grid gives
$\hat c = 298$; plugging that in, the fitted slope is $\hat\beta_1\approx 191.2$ before the change
and $\hat\beta_1+\hat\beta_2\approx 223.5$ after it — population growth accelerated around that
point in the series — with $\hat\sigma$ between $2214$ and $2219$ depending on which of the two
estimators is used. A broken-stick fit tracks the curvature in the series visibly better than a
single straight line fit over the whole range, which the lab plots alongside it for comparison.

The Bayesian posterior for $c$ (here $p=3$) again mirrors the shape of the RSS curve; $2000$
posterior draws give mean $\hat c\approx 297.4$, standard deviation $\approx 9.2$, and posterior
means for $(\beta_0,\beta_1,\beta_2,\sigma)\approx (178342,\,191.1,\,32.4,\,2222)$ — close to the
plug-in estimates, as expected once $n$ is large enough that the plug-in MLE and the posterior mean
essentially agree.

## What carries across all three examples

- The recipe is always the same two steps: profile out the linear part to get
  $\mathrm{RSS}(\theta)$, minimize it over a grid for a point estimate, then reuse that same
  $\mathrm{RSS}(\theta)$ together with $|X_\theta^\top X_\theta|$ to build a posterior over
  $\theta$, and finally chain draws $\theta \to \sigma \to \beta$ into a full posterior sample.
- The Fourier-frequency shortcut is special to the sinusoid case, where a single FFT hands back the
  periodogram at all $n/2$ candidate frequencies at once. The step and broken-stick models have no
  analogous transform, so their grid search is genuinely over every candidate integer time point.
- Near-singularity of $X_\theta^\top X_\theta$ is the generic hazard whenever $\theta$ is pushed
  toward a value that makes the design degenerate — the frequency boundary for the sinusoid, the
  first or last handful of time points for a change-point — and it always shows up the same way: an
  exploding $|X_\theta^\top X_\theta|^{-1/2}$ term that has to be trimmed from the grid by hand.

## Sources

- `01-inference-in-sinusoid-models.md`, `02-change-point-model.md`,
  `03-change-of-slope-or-broken-stick-regression.md` — berkeley-stat153, spring 2025, `Lab4.ipynb`,
  CC BY 4.0. All equations, numerical results, and posterior summaries in this chapter come from
  these three notebook sections.
- Referred to but not supplied here: the earlier lab that first set up the sinusoid model and
  estimated $f$ from the periodogram alone (opening paragraph of `01-inference-in-sinusoid-models.md`);
  the derivation of the marginal posterior $\pi(\theta\mid\text{data})$ itself, which the lab states
  but does not re-derive; and Problem 4 of Homework 1, which proves
  $\mathrm{RSS}(\theta)/\sigma^2 \mid \text{data},\theta \sim \chi^2_{n-p}$.

---

[← 94. Frequency Estimation and Aliasing](94-frequency-estimation-and-aliasing.md) · [Contents](index.md) · [96. Change-point model →](96-change-point-model.md)
