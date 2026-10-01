---
title: "18. Time-Lagged Regression and the STRF"
course: "Berkeley Stat 153"
chapter: 18
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 18. Time-Lagged Regression and the STRF

## What this covers

This chapter covers **time-lagged regression**: extending ordinary multiple regression so that an
output series can depend on an input series at many different time delays, not just at the same
time point. It works through the one running example the lecture used — reconstructing the
**spectrotemporal receptive field (STRF)** of a set of brain electrodes from an intracranial
recording made while a patient listened to speech and movie clips — and uses that example to show
why the resulting design matrix has strongly correlated columns, and why that breaks ordinary least
squares. It assumes multiple linear regression, ridge regression, cross-validation, and the idea of
a spectrogram from earlier in the course.

## The model: regression across time lags

Every regression model seen so far has predicted $y_t$ from covariates measured *at* time $t$.
Time-lagged regression drops that restriction and lets $y_t$ depend on an input series $x_t$ at a
whole range of lags:

$$y_t = \sum_{r=-\infty}^\infty \beta_r x_{t-r} + v_t$$

Shumway and Stoffer write it with an infinite sum (their eqn 4.115) because that form makes the
Fourier arguments work out cleanly; in practice one uses a finite series and a finite, theoretically
motivated set of lags. Their book's example is the SOI and Recruitment series: the Southern
Oscillation Index — which tracks El Niño-related weather — as a candidate input $x_t$ driving fish
recruitment $y_t$ as the output, at some range of lags rather than only at lag zero.

The rest of this lecture builds one worked example that pulls together several strands from the
course at once — multiple regression, regularization, cross-validation, and spectral analysis — and
applies them to a neuroscience problem called **spectrotemporal receptive field estimation**.

## The STRF: time-lagged regression as a model of the brain

In this application, the input $x$ is a sound stimulus and the output $y$ is a neural time series
recorded while a person listens to it:

$$y_t = \sum_\tau \beta_\tau x_{t-\tau}$$

where $\tau$ is the time delay. Models of this shape have been used to identify which features of a
stimulus drive neural activity in a given brain area — frequency content from a spectrogram,
phoneme identity, word onsets, visual features, and so on. When the input is a spectrogram
specifically, the model is called a **spectrotemporal receptive field (STRF)**: the term refers to
the fitted $\beta$ coefficients themselves, which act as a linear filter describing which
combinations of frequency and time delay increase or decrease activity in the recorded brain area.
The same technique, and the same coefficients under the names **TRF** or **mTRF weights**
(temporal response function), has been applied to EEG, intracranial EEG, MEG, and fMRI recordings.

The lecture's key references for this framing: Aertsen & Johannesma (1981), who introduced the STRF;
Theunissen, David, Singh et al. (2001) and Wu, David & Gallant (2006), on estimating receptive
fields from natural stimuli; and Holdgraf et al. (2017), *Encoding and Decoding Models in Cognitive
Electrophysiology*, which is also this lecture's assigned reading alongside Shumway & Stoffer §4.8.

### Writing the STRF as a matrix regression

For a single output time series, $F$ frequency bins in the spectrogram, and $D$ delays:

$$y_t = \sum_{f=1}^{F} \sum_{d=0}^{D-1} \beta_{f,d}\, x_{f,\, t-d}$$

The response at $t$ is a weighted sum, over every (frequency, delay) pair, of the spectrogram values
at the corresponding earlier time points. $\beta_{f,d}$ *is* the STRF: how much frequency $f$ at
delay $d$ contributes to the response.

Collect the weights into a matrix $B \in \mathbb{R}^{F \times D}$ and the relevant slice of stimulus
history into a matrix $X_t \in \mathbb{R}^{F \times D}$ — the spectrogram columns from $t$ back to
$t-D+1$. Then

$$y_t = \sum_{f,d} B_{f,d}\, (X_t)_{f,d} = \langle B, X_t \rangle_F,$$

the Frobenius inner product of the STRF kernel with the recent stimulus history — the "2D filter"
view of the model.

To fit it, flatten $B$ into a column vector $\beta \in \mathbb{R}^{FD}$ and each $X_t$ into a row
vector $\mathbf{x}_t^T$, so that $y_t = \mathbf{x}_t^T \beta$ for every $t$. Stacking the rows over
all $T$ time points gives a design matrix $\mathbf{X} \in \mathbb{R}^{T \times FD}$ and the ordinary
regression form

$$\mathbf{y} = \mathbf{X}\beta.$$

**A STRF is fundamentally a linear regression.** The "spectrotemporal" language is only there for
interpretation — reshaping the flat $\beta$ vector back into an $F \times D$ grid so it can be read
as a filter over frequency and delay — the estimation itself is regression on the flattened design
matrix. With $E$ electrodes recorded at once, replace $\mathbf{y}$ by $\mathbf{Y} \in
\mathbb{R}^{T \times E}$ and $\beta$ by $\mathbf{B} \in \mathbb{R}^{FD \times E}$, giving
$\mathbf{Y} = \mathbf{X}\mathbf{B}$: the same design matrix, $E$ regressions solved side by side.

## The dataset

The worked example uses electrocorticography (ECoG) recordings from a patient with epilepsy who
listened to a set of movie clips, looking at three example electrodes. The inputs are two competing
descriptions of the sound: an 80-bin spectrogram, and a 14-feature phoneme representation. Training
and test sets are pre-split (161{,}034 and 13{,}563 time points respectively), and every series —
the neural responses and both stimulus representations — is z-scored to mean 0 and standard
deviation 1 before fitting.

## Choosing the lags

Before building the design matrix you have to decide what range of lags to include. Two ways to do
that: prior knowledge about the brain area (if responses in this area are known to occur within,
say, 500 ms, there is no point searching beyond that), or the empirical **cross-correlation
function (CCF)** between stimulus and response, computed directly from the data.

The lecture did the second: for every electrode and every spectrogram frequency, it computed the
cross-correlation between the neural series and that stimulus feature over a window of lags from
$-0.6$ to $+0.6$ seconds, then averaged the absolute CCF across frequency features to get one
lead–lag curve per electrode.

<figure>
<svg viewBox="0 0 380 220" role="img" aria-label="Cross-correlation envelope between spectrogram and neural response, peaking at a positive lag, with the delay window used for the design matrix shaded">
  <line x1="30" y1="170" x2="350" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="190" y1="20" x2="190" y2="170" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <rect x="190" y="20" width="80" height="150" fill="currentColor" fill-opacity="0.15"/>
  <polyline points="30,160 70,158 110,150 150,130 190,100 210,70 230,45 250,55 270,75 290,100 310,125 330,145 350,155"
            fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="190" y="188" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <text x="350" y="188" text-anchor="end" font-size="12" fill="currentColor">lag (s)</text>
  <text x="30" y="18" font-size="12" fill="currentColor">|CCF|, averaged over spec. features</text>
  <text x="230" y="205" text-anchor="middle" font-size="11" fill="currentColor">spectrogram leads neural response</text>
</svg>
<figcaption>The cross-correlation envelope between the sound spectrogram and one electrode's
response, averaged across frequency features. It peaks just after zero lag — the response follows
the sound, not the reverse — and the shaded window of positive lags is what gets embedded into the
design matrix.</figcaption>
</figure>

Positive lag here means the spectrogram leads the neural signal, which is the causally sensible
direction: the sound arrives before the brain responds to it. Reading off where this envelope is
concentrated is what fixes the embedding window; the lecture used delays running from 0 up to 0.4
seconds forward (`delay_min = 0`, `delay_max = 0.4`), which came out as 40 discrete integer delay
steps — $0, 1, \dots, 39$. (Forty samples covering 0.4 seconds pins the recording's sampling rate at
100 Hz, though the notebook never states that number directly — it only appears through this
arithmetic.)

## Building the delay-embedded design matrix

Turning a stimulus matrix into a lagged design matrix means stacking shifted copies of it side by
side. For a toy spectrogram with $n$ time points and 3 frequencies,

$$
\begin{bmatrix}
x_{1,1} & x_{1,2} & x_{1,3} \\
x_{2,1} & x_{2,2} & x_{2,3} \\
x_{3,1} & x_{3,2} & x_{3,3} \\
\vdots & \vdots & \vdots \\
x_{n,1} & x_{n,2} & x_{n,3}
\end{bmatrix}
$$

becomes a stacked delay matrix whose rows contain the current stimulus values together with
progressively older ones, zero-padded at the start:

$$
\begin{bmatrix}
x_{1,1} & x_{1,2} & x_{1,3} & 0 & 0 & 0 & \cdots & 0 \\
x_{2,1} & x_{2,2} & x_{2,3} & x_{1,1} & x_{1,2} & x_{1,3} & \cdots & 0 \\
x_{3,1} & x_{3,2} & x_{3,3} & x_{2,1} & x_{2,2} & x_{2,3} & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
x_{n,1} & x_{n,2} & x_{n,3} & x_{n-1,1} & x_{n-1,2} & x_{n-1,3} & \cdots & x_{n-d+1,3}
\end{bmatrix}
$$

This has a name: it is a [Toeplitz matrix](http://en.wikipedia.org/wiki/Toeplitz_matrix), since
every diagonal is constant. In the STRF example, embedding the 80-frequency spectrogram at 40 delays
gives $80 \times 40 = 3200$ predictor columns, confirmed directly by the code (`xtraind.shape[1] ==
xtrain.shape[1] * len(delays)` returns `True`): the training design matrix is $161{,}034 \times
3200$ and the test design matrix is $13{,}563 \times 3200$. Appending an intercept column of ones
brings the final count to 3201 predictors.

## Correlated predictors: the covariance matrix

Before fitting anything, the lecture computed the covariance matrix of the delay-embedded stimulus,
$\mathbf{X}^T\mathbf{X}$. The point of looking at it is to see, up front, how strongly the columns
of the design matrix covary — both because nearby frequencies in a spectrogram tend to rise and
fall together, and because a slowly varying signal is strongly correlated with shifted copies of
itself. This covariance structure is the thing that determines whether ordinary least squares will
behave well, and it is examined *before* fitting for exactly that reason.

## Fitting by ordinary least squares

With the design matrix and intercept in hand, OLS is a single call: `beta, SSE, rank, s =
np.linalg.lstsq(xtraind_int, ytrain, rcond=None)`. With $\mathbf{X}$ of shape $161{,}034 \times
3201$ and $\mathbf{Y}$ of shape $161{,}034 \times 3$ (one column per electrode), $\hat\beta$ comes
out as $3201 \times 3$ — an independent set of weights per electrode, fit by ordinary least squares
without pooling information across electrodes.

**Cross-validation performance.** Predictions on the held-out test set are $\hat{\mathbf{y}} =
\mathbf{X}_{\text{test}}\hat\beta$, and performance is measured as the Pearson correlation between
$\hat{\mathbf{y}}$ and the true $\mathbf{y}_{\text{test}}$ for each electrode. The OLS fit reaches
correlations up to about 0.5 on held-out data — for neural recordings, given measurement and
physiological noise, that counts as a good result.

**Residuals.** The residuals $\mathbf{y}_{\text{test}} - \hat{\mathbf{y}}$ still show structure in
their autocorrelation function. This is typical of this kind of model: the stimulus usually does
*not* account for most of the variance in a neural recording, because other ongoing oscillatory
brain processes dominate the signal and regression on stimulus features alone cannot remove them.
That is a real limitation, but the lecture's stance is pragmatic — if the model still predicts new,
unseen data usefully, it is worth having even though it does not explain every source of variance.

**Reading the fitted weights as a filter.** Reshaping $\hat\beta$ for one electrode (dropping the
intercept) back into a delay-by-frequency grid, `beta[1:, c].reshape(len(delays), -1)`, recovers the
STRF itself — the picture that is supposed to show which past frequency/delay combinations push the
response up or down.

## Why OLS breaks down, and the fix

Even with correlations up to 0.5, the recovered weight matrices are not easy to interpret. The hope
is to read a large positive value as "this frequency at this delay drives the response up" — but
that is not what the raw OLS weights show, because the stimulus features are highly correlated: a
spectrogram does not vary independently from one time bin to the next, or from one frequency to the
next, and delay-embedding compounds this by adding shifted copies of an already-smooth signal as
extra, strongly correlated columns. Highly correlated columns are exactly the setting in which
ordinary least squares becomes unstable — small changes in the data can swing $\hat\beta$
substantially, without much affecting the fitted values.

The fix is **ridge regression**: regularizing the fit stabilizes the estimated weights when the
design matrix's columns are correlated, at the cost of some bias. This is precisely the situation
autocorrelated, delay-embedded stimuli create, so it is the natural next step here.

### Cross-validated ridge

The lecture's ridge fit (`cv_ridge`) makes several choices explicit:

- `alphas = np.logspace(2, 8, 15)` — 15 candidate regularization strengths spanning $10^2$ to
  $10^8$, evenly spaced on a log scale.
- `use_corr = True` — select $\alpha$ to maximize the correlation between predicted and held-out
  responses, rather than by squared error.
- `single_alpha = False` — fit a separate best $\alpha$ per electrode rather than one shared value;
  the lecture calls this "usually what you should do", since different electrodes can tolerate
  different amounts of regularization.
- `nfolds = 3` — a fairly small number of cross-validation folds.
- `chunklen = 4 * len(delays)` — the training data is split into contiguous chunks of this length,
  not shuffled point by point, before being assigned to folds. Randomly permuting individual time
  points would destroy the temporal correlation structure the delay embedding is built to capture,
  so the resampling has to respect blocks of consecutive time instead.

Sweeping $\alpha$ shows the pattern ridge regression is supposed to produce: as $\alpha$ increases
from $10^2$, the mean held-out correlation across folds first rises — regularization is helping,
because it is damping the instability from correlated columns — then falls sharply beyond roughly
$10^7$–$10^8$, once the penalty is strong enough to shrink the fitted weights toward zero and destroy
the signal along with the instability. The practical diagnostic (`check_alphas`) is to plot
correlation against $\alpha$ on a log axis and check that the curve peaks somewhere in the middle of
the chosen range; if the best $\alpha$ keeps landing at one end of the range, the fix is to widen
the range and refit, not to accept an edge value.

The final fit uses each electrode's own best $\alpha$, applied to the full training set, giving
ridge STRF weights, held-out correlations, and held-out predictions for every electrode. Visually,
the ridge-regularized STRFs come out smoother and easier to read as frequency-by-delay filters than
the raw OLS ones.

### How the STRF's shape depends on $\alpha$

As a purely illustrative exercise (not something you would normally do in an analysis), the lecture
refit the ridge weights at *every* candidate $\alpha$, for every electrode, rather than only the
electrode-specific best one. Two things fall out of comparing them side by side:

1. As $\alpha$ grows, the estimated STRF becomes visibly broader and smoother — more of the
   original signal has been shrunk away.
2. The held-out correlation, plotted against $\alpha$, traces the same inverted-U shape as before,
   for every electrode individually: too little regularization leaves the fit unstable because of
   the correlated columns; too much regularization erases the real structure along with the
   instability; the useful fit sits at an intermediate value that the cross-validation search finds
   automatically.

## Putting it together

The STRF example was chosen to combine, in one worked model, several ideas that had each shown up
separately earlier in the course:

1. **Spectral analysis** — using the spectrogram of a sound as a covariate in a regression.
2. **Multiple linear regression with time lags** — the STRF itself, once vectorized.
3. **Cross-validation** — both for choosing the delay window and for selecting the ridge penalty.
4. **Dealing with autocorrelated predictors** — recognizing why the delay-embedded design matrix has
   highly correlated columns, and why that specifically breaks OLS.
5. **OLS vs. ridge** — seeing the failure mode directly, then seeing regularization fix it.

## Sources

- `20_time_lagged_reg_notes.md` (Lecture 20 notes) — the general time-lagged regression model,
  the reference to Shumway & Stoffer §4.8 (eqn 4.115) and the SOI/Recruitment example, and the
  framing of the STRF as combining regression, regularization, cross-validation and spectral
  analysis.
- `Lecture20/01-stat-153-248-lecture-20.md` — the STRF model definition, its matrix form ($B$,
  $X_t$, Frobenius inner product), the vectorized regression form $\mathbf{y} = \mathbf{X}\beta$ and
  its multi-electrode extension, the reference list (Aertsen & Johannesma 1981; Theunissen et al.
  2001; Wu et al. 2006; Holdgraf et al. 2017), the dataset description, and the cross-correlation
  computation used to choose the lag window.
- `Lecture20/02-plotting-lag-relationships.md` — the cross-correlation envelope plot, the Toeplitz
  delay-matrix construction and its toy example, the resulting design-matrix shapes, and the
  stimulus covariance matrix.
- `Lecture20/03-ols.md` — the OLS fit and its held-out performance, the residual autocorrelation
  discussion, the STRF-as-filter visualization, the motivation for ridge regression, the
  cross-validated ridge procedure (`cv_ridge`) and its parameters, the alpha-sweep diagnostic, and
  the closing summary of the five course topics combined in this example.
- Named but not contained in the supplied material: Shumway & Stoffer, *Time Series Analysis and
  Its Applications*, §4.8 (the textbook treatment of time-lagged/transfer-function regression);
  the four neuroscience references listed above (Aertsen & Johannesma 1981; Theunissen, David, Singh
  et al. 2001; Wu, David & Gallant 2006; Holdgraf et al. 2017); and the `Lecture20.ipynb` notebook's
  omitted figures, described in the source but not reproduced as images.

---

[← 17. Fitting and Diagnosing ARIMA Models](17-fitting-and-diagnosing-arima-models.md) · [Contents](index.md) · [19. State Space Models →](19-state-space-models.md)
