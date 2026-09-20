---
title: "8. Improving upon the linear model"
course: "Berkeley Stat 153 Fall 2024"
chapter: 8
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 8. Improving upon the linear model

## What this covers

Ordinary least squares assumes there are many more observations than parameters. This chapter
asks what happens as that stops being true — when a model has almost as many parameters as data
points — and what "overfitting" concretely looks like when it happens. It then covers the standard
remedy, cross-validation, including the specific ways it has to be done differently for time series
data, and closes by naming (without yet deriving) the alternative the next lecture takes up:
shrinking coefficients instead of choosing a subset of them. It assumes multiple linear regression
and least squares, and familiarity with fitting a sinusoid of unknown frequency by grid search plus
OLS, as used in the worked examples below.

## When does least squares break down?

For multiple linear regression, $Y = \beta_0 + \beta_1 X_1 + \cdots + \beta_p X_p + \epsilon$. If the
true relationship is approximately linear, the least squares estimates have low bias. If, in
addition, $n \gg p$ — many more observations than parameters — the estimates also tend to have low
variance, so the fitted model should perform well on new data.

Two things go wrong as $p$ grows relative to $n$:

- If $n$ is not much larger than $p$, the least squares fit can have a lot of variability, which
  shows up as **overfitting**: the fitted model does not predict new observations well.
- If $p > n$, there are more coefficients to estimate than there are observations to estimate them
  from. Least squares no longer has a unique minimizer — there are infinitely many solutions that
  achieve zero error on the training data. Any of them can look perfect on the data used to fit it
  and still perform very poorly on new data, because it has fit the noise rather than the signal.

**Overfitting** is what happens when a model learns to predict the data it was fit on almost
perfectly but does not generalize — it follows the noise too closely. As model flexibility (and the
number of parameters) grows, the model can pick up patterns that are there by chance in this
particular sample, rather than because they reflect a real relationship.

## Overfitting, made concrete

The lecture's running example is a sinusoid observed with noise: $y = \beta_0 + R\cos(2\pi f t +
\phi) + \epsilon$, sampled at 500 Hz for two seconds ($n = 1000$ points), with $\beta_0 = 2$,
$R = 2.5$, $f = 2.3$, $\phi = 0$, and noise variance $0.2$. The frequency $f$ is unknown, so it is
found by a grid search: for each candidate $\hat f$, fit the three-parameter model

$$
X_{\hat f} = \begin{pmatrix}
1 & \cos(2\pi \hat f t_0) & \sin(2\pi \hat f t_0) \\
\vdots & \vdots & \vdots \\
1 & \cos(2\pi \hat f t_n) & \sin(2\pi \hat f t_n)
\end{pmatrix}
$$

by OLS and record its RSS; take the $\hat f$ with the smallest RSS. This gives a sensible
three-parameter fit.

Now push it further: instead of estimating one frequency, put a whole grid of candidate
frequencies — one cosine/sine pair each, up to the Nyquist limit ($f_s/2 = 250$ Hz) — into the same
regression. With $500$ candidate frequencies this produces about as many predictor columns
($1 + 2\times 500 = 1001$) as there are observations ($n=1000$): essentially $p \approx n$, the
pathological case above.

The fit reports $R^2 = 0.993$ — it looks superb — but the *adjusted* $R^2$, which is penalized for
the number of parameters used, is $-2.336$: strongly negative. Almost every individual coefficient
is statistically indistinguishable from zero (large p-values), while the first couple of
coefficients — the intercept and the near-zero-frequency terms — have enormous point estimates and
standard errors, on the order of $10^8$ to $10^{10}$, that very nearly cancel against each other.
That is what "infinitely many solutions" looks like in practice: the fitted values can still look
reasonable while the individual coefficients are wild and numerically unstable, because the design
matrix is (near-)singular.

The real test is generalization. Generate genuinely new data from the same underlying sinusoid, at
time points *after* the training window (a further second, fresh noise draw), and compare training
and test root-mean-squared error:

| model | train RMSE | test RMSE |
|---|---|---|
| overfit, $p \approx n$ | 0.151 | 4.41 |
| well-specified, 3 parameters | 0.445 | 0.442 |

The overfit model's training error is far smaller — it interpolates the training noise almost
exactly — but its test error is nearly thirty times worse than the well-specified model's. The
well-specified model's train and test errors are close to each other: that closeness is what
generalizing looks like, since it means the error the model achieves on the data it was fit to is a
fair estimate of what it will do on data it hasn't seen.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Schematic of training error falling steadily with model complexity while test error is U-shaped and blows up once the number of parameters approaches the number of observations">
  <line x1="40" y1="185" x2="320" y2="185" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="185" x2="40" y2="15" stroke="currentColor" stroke-width="1.5"/>
  <text x="180" y="207" text-anchor="middle" font-size="12" fill="currentColor">number of parameters</text>
  <text x="18" y="100" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 18 100)">error</text>

  <polyline points="55,50 100,75 150,110 200,140 250,162 310,180" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="228" y="152" font-size="11" fill="currentColor">training error</text>

  <polyline points="55,140 90,90 130,62 170,58 210,80 250,130 305,20" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="120" y="46" font-size="11" fill="currentColor">test error</text>

  <circle cx="170" cy="58" r="3.5" fill="currentColor"/>
  <line x1="170" y1="58" x2="170" y2="185" stroke="currentColor" stroke-width="1" stroke-dasharray="2 3"/>
  <text x="170" y="200" text-anchor="middle" font-size="11" fill="currentColor">best model</text>

  <text x="315" y="15" text-anchor="end" font-size="11" fill="currentColor">p ≈ n</text>
</svg>
<figcaption>Schematic of the relationship the two fitted models above sit on: training error keeps
falling as parameters are added, but test error is minimized at some intermediate complexity and
then rises sharply — catastrophically, in the $p \approx n$ case above.</figcaption>
</figure>

## Cross-validation: judging a model on data it hasn't seen

Training error alone cannot distinguish the two models above from each other in advance, because
training error only improves (or stays flat) as parameters are added — it is being computed on the
same data used to fit the model. The fix is to evaluate the fit on data that was withheld from
fitting: choose the model that minimizes an estimate of mean squared error on **held-out** data.

The general recipe is **$k$-fold cross-validation**: split the data into $k$ chunks, fit on $k-1$ of
them, and compute the error on the remaining held-out fold; repeat over each fold in turn and
average the errors.

## Cross-validation and time series

Two features of time series break the usual recipe:

- We typically want to predict the future from the past, so randomly permuting time before
  splitting does not make sense.
- Observations are autocorrelated, so choosing a random subset of individual time points as the
  test set does not isolate genuinely unseen information — a training point next to a test point
  can be nearly the same value.

<figure>
<svg viewBox="0 0 340 175" role="img" aria-label="A random split scatters test points among correlated neighbours in time, unlike a chunked split that puts the whole test block after the training block">
  <text x="170" y="14" text-anchor="middle" font-size="12" fill="currentColor">time →</text>

  <text x="24" y="42" font-size="11" fill="currentColor">random split</text>
  <line x1="26" y1="50" x2="300" y2="50" stroke="currentColor" stroke-width="0.5" stroke-opacity="0.3"/>
  <circle cx="30" cy="50" r="4" fill="currentColor"/>
  <circle cx="44" cy="50" r="4" fill="currentColor"/>
  <circle cx="58" cy="50" r="4" fill="currentColor"/>
  <circle cx="72" cy="50" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="86" cy="50" r="4" fill="currentColor"/>
  <circle cx="100" cy="50" r="4" fill="currentColor"/>
  <circle cx="114" cy="50" r="4" fill="currentColor"/>
  <circle cx="128" cy="50" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="142" cy="50" r="4" fill="currentColor"/>
  <circle cx="156" cy="50" r="4" fill="currentColor"/>
  <circle cx="170" cy="50" r="4" fill="currentColor"/>
  <circle cx="184" cy="50" r="4" fill="currentColor"/>
  <circle cx="198" cy="50" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="212" cy="50" r="4" fill="currentColor"/>
  <circle cx="226" cy="50" r="4" fill="currentColor"/>
  <circle cx="240" cy="50" r="4" fill="currentColor"/>
  <circle cx="254" cy="50" r="4" fill="currentColor"/>
  <circle cx="268" cy="50" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="282" cy="50" r="4" fill="currentColor"/>
  <circle cx="296" cy="50" r="4" fill="currentColor"/>
  <path d="M58,44 Q65,26 72,44" fill="none" stroke="currentColor" stroke-width="1"/>
  <text x="60" y="22" font-size="11" fill="currentColor">neighbours are correlated</text>

  <text x="10" y="113" font-size="11" fill="currentColor">chunked split</text>
  <line x1="26" y1="120" x2="300" y2="120" stroke="currentColor" stroke-width="0.5" stroke-opacity="0.3"/>
  <circle cx="30" cy="120" r="4" fill="currentColor"/>
  <circle cx="44" cy="120" r="4" fill="currentColor"/>
  <circle cx="58" cy="120" r="4" fill="currentColor"/>
  <circle cx="72" cy="120" r="4" fill="currentColor"/>
  <circle cx="86" cy="120" r="4" fill="currentColor"/>
  <circle cx="100" cy="120" r="4" fill="currentColor"/>
  <circle cx="114" cy="120" r="4" fill="currentColor"/>
  <circle cx="128" cy="120" r="4" fill="currentColor"/>
  <circle cx="142" cy="120" r="4" fill="currentColor"/>
  <circle cx="156" cy="120" r="4" fill="currentColor"/>
  <circle cx="170" cy="120" r="4" fill="currentColor"/>
  <circle cx="184" cy="120" r="4" fill="currentColor"/>
  <circle cx="198" cy="120" r="4" fill="currentColor"/>
  <circle cx="212" cy="120" r="4" fill="currentColor"/>
  <circle cx="226" cy="120" r="4" fill="currentColor"/>
  <circle cx="240" cy="120" r="4" fill="currentColor"/>
  <line x1="247" y1="103" x2="247" y2="137" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <circle cx="254" cy="120" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="268" cy="120" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="282" cy="120" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="296" cy="120" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>

  <circle cx="235" cy="153" r="4" fill="currentColor"/>
  <text x="243" y="157" font-size="11" fill="currentColor">train</text>
  <circle cx="278" cy="153" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="286" y="157" font-size="11" fill="currentColor">test</text>
</svg>
<figcaption>Splitting 80/20 at random scatters test points next to highly correlated training
neighbours, inflating apparent accuracy for reasons that have nothing to do with generalizing;
training on the first 80% of time points and testing on the last 20% avoids this.</figcaption>
</figure>

This is exactly the comparison the lecture works through: with the sinusoid data, choosing 80% of
the individual time points at random for training (and the rest for testing) is "cheating" because
neighbouring points in an autocorrelated series carry almost the same information, so nearby train
and test points aren't independent. Splitting by contiguous chunk instead — training on the first
80% of the time points, testing on the last 20% — makes the test period genuinely unseen at the
point the model was fit.

## Cross-validation versus AIC and BIC

Cross-validation used to be too computationally expensive to try many possible splits, which is why
parametric alternatives such as AIC and BIC were preferred. That is no longer true, and
cross-validation has become the more common choice because it needs none of:

- normally distributed errors,
- homoscedasticity,
- correct model specification,
- a known number of parameters.

It works for essentially any model, using only predictive accuracy on held-out data, whereas AIC
and BIC are built on an assumption of Gaussian errors.

## Choosing how many frequencies to keep

The second worked example makes the number of parameters itself the thing to be chosen. The signal
now has three sinusoidal components — frequencies $2.3$, $5.55$ and $12.5$, with amplitudes $2.5$,
$1$ and $1.25$ on top of an intercept of $2$ — and a much larger noise variance ($5$, versus $0.2$
before). This time the number of frequencies genuinely in the signal is not something you'd want to
assume you know.

The strategy:

1. Fit each candidate frequency in the search grid **on its own**, as a three-parameter model, as
   before, and rank all candidates by their individual RSS. The ten best individually-fit
   frequencies (in Hz) came out as:

   $$2.505,\ 2.004,\ 12.525,\ 5.511,\ 3.006,\ 3.507,\ 1.503,\ 4.008,\ 5.010,\ 93.687$$

   These cluster near the three true frequencies ($2.3$, $5.55$, $12.5$) but don't recover them
   exactly: several neighbouring grid points near a true frequency score almost as well, since a
   nearby frequency still explains much of a short, noisy sinusoid, and one clear outlier
   ($93.687$) makes the top ten purely from noise. Ranking by RSS alone does not cleanly separate
   signal from noise once the data is this noisy.

2. Rather than picking a cutoff by eye, build a nested sequence of models — the single best
   frequency, the best two, the best three, and so on up to the best 29 — and use cross-validation
   to choose how many to keep. The splitting has to respect time order at each fold (an expanding
   training window moving forward through the series, via `TimeSeriesSplit`), for the same reason
   as above. The number of frequencies is then chosen to minimize the cross-validated MSE, not the
   training RSS — which, following the overfitting story above, would simply keep falling as more
   (increasingly noise-fitting) frequencies are added.

## Looking ahead: shrinkage instead of selection

An alternative to *selecting* a subset of predictors, as in the frequency-selection procedure just
described, is to keep all of them but **constrain or shrink** their coefficients — trading a little
bias for a large reduction in variance, and, as a side benefit, making the model easier to interpret
if some coefficients shrink close to zero. The two standard versions of this are ridge regression
($L_2$ regularization) and LASSO regression ($L_1$ regularization). Those are the subject of the
next lecture, not this one.

## Sources

- Slide notes, `10_regularization_notes/01-improving-upon-the-linear-model.md`: the bias/variance
  setup for least squares, the $n \gg p$, $n \approx p$ and $p > n$ cases, and the definition of
  overfitting. That page names its assigned reading — *An Introduction to Statistical Learning*,
  Chapter 6 (and §6.2) — which was not itself supplied and so is not covered here.
- Slide notes, `10_regularization_notes/02-cross-validation.md`: the general $k$-fold recipe, the
  time-series-specific complications, the historical note on CV's computational cost versus
  AIC/BIC, and the transition into shrinkage methods (ridge/LASSO, $L_2$/$L_1$), which the notes
  explicitly defer to the following lecture.
- Lecture notebook, `Lecture10/01-lecture-10---regularization.md`: the sinusoid worked example —
  grid search for $f$, the three-parameter fit, the $p \approx n$ "perfect model" overfitting
  demonstration (including the regression summary's $R^2$, adjusted $R^2$, and coefficient
  instability), the train/test RMSE comparison on genuinely new data, and the random-versus-chunked
  split demonstration for time series cross-validation.
- Lecture notebook, `Lecture10/02-what-about-choosing-the-number-of-parameters.md`: the
  three-frequency, higher-noise example — ranking candidate frequencies by individual RSS, and
  setting up cross-validation (via `TimeSeriesSplit`) over how many top-ranked frequencies to
  include. The notebook code computes but does not print the resulting CV-error-versus-number-of-
  frequencies curve, so that specific result is not reported here.
- No transcript, written notes, or problem set were supplied for this lecture.

---

[← 7. Sinusoidal Nonlinear Regression](07-sinusoidal-nonlinear-regression.md) · [Contents](index.md) · [9. Cross-Validation and Regularization →](09-cross-validation-and-regularization.md)
