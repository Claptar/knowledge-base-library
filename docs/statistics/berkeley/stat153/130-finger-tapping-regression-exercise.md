---
title: "130. Finger Tapping Regression Exercise"
course: "Berkeley Stat 153"
chapter: 130
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 130. Finger Tapping Regression Exercise

## What this covers

This chapter works through an in-class data-collection exercise from Stat153/248: each student
taps a finger for 60 seconds while software logs every tap, and the class fits ordinary least
squares (OLS) models to the results. It assumes the reader already has least squares regression and
the normal equations, and shows how a categorical predictor becomes a numeric one in a design
matrix, how to compare competing encodings of the same experimental factor, and how a stream of
event times gets turned into a time series by binning — the same move needed whenever a time series
has to be built out of irregularly spaced events.

## The experiment and the raw data

Each of 101 subjects tapped one finger — index or pinky — with one hand, for 60 seconds, while an
app recorded the time of every tap, `t_seconds`. From consecutive tap times the notebook computes
the inter-tap gap, `dt_seconds`. Two more variables describe each subject: `handedness`, which hand
they consider dominant, and `hand`, which hand they actually tapped with; a derived boolean,
`dominant_hand`, records whether the two agree.

The first two plots in the notebook set up the question the rest of the lecture answers
numerically:

- a line plot of `t_seconds` against `tap_index`, split by finger, shows how fast each finger
  accumulates taps over the minute;
- a violin plot of `dt_seconds` against `dominant_hand`, split by finger, shows the distribution of
  the gap between taps for each of the four combinations of hand dominance and finger.

Both plots raise the same question: do finger and hand dominance actually change how many taps
someone can produce, or are the visual differences just noise? That is what the regression models
below answer.

The subject-level summary collapses each of the 101 sessions into one row: subject id, hand,
finger, handedness, dominant_hand, and the total tap count in 60 seconds, `ntaps` — ranging, in the
sample shown, from the high 200s to the high 300s.

## Coding a categorical predictor: dummy variables and the design matrix

OLS needs a numeric design matrix, so a categorical predictor like finger (index/pinky) or hand
(left/right) has to become one or more 0/1 columns before it can enter $X$. With $k$ levels this
takes $k-1$ indicator columns once one level is fixed as the reference; `pd.get_dummies(...,
drop_first=True)` does exactly this, turning finger into a single column `finger_pinky` (1 if
pinky, 0 if index) and hand into `hand_right`. Adding a constant column gives the design matrix

$$X = [\,\mathbf{1} \mid \text{finger\_pinky} \mid \text{dominant\_hand}\,],$$

against which `ntaps` is regressed:

$$\text{ntaps} = \beta_0 + \beta_1\cdot\text{finger\_pinky} + \beta_2\cdot\text{dominant\_hand} + \varepsilon.$$

The reference case — the row where every indicator is 0 — is tapping with the index finger on the
non-dominant hand; $\beta_0$ is the predicted tap count for that case, and each $\beta_j$ is the
shift in tap count from switching that one indicator on.

## Three ways to fit the same model

The notebook fits this model three separate ways and gets the identical answer each time, which is
worth pausing on because it is the reason a formula interface can be trusted rather than treated as
a black box.

1. **By the normal equations directly**, $\hat\beta = (X^\top X)^{-1}X^\top y$, computed with
   `np.linalg.inv`.
2. **By `sm.OLS(y, X).fit()`** on the same hand-built dummy-coded matrix.
3. **By the formula interface**, `smf.ols("ntaps ~ C(dominant_hand) + C(finger)", data=summary_df)`,
   which builds the same dummy-coded matrix from the raw categorical columns internally — `C()`
   marks a column as categorical, and the reference level is whichever one sorts first (`index`
   before `pinky`, `False` before `True`).

All three return

$$\hat\beta = (323.517,\ -28.250,\ 46.707),$$

i.e. the OLS estimator does not care how the design matrix was assembled, only what it contains —
the formula interface is a convenience for building exactly the matrix in step 1, not a different
computation.

Reading the fitted model: on the index finger with the non-dominant hand, it predicts about 323.5
taps in 60 seconds. Using the pinky costs about 28.25 taps ($p = 0.004$); using the dominant hand
instead of the non-dominant one gains about 46.7 taps ($p < 0.001$). Both effects are large
relative to their standard errors, and together they account for about a quarter of the variance in
tap counts ($R^2 = 0.262$).

## Which encoding of hand dominance fits better?

The notebook then compares three specifications that differ only in how hand dominance enters:

| Model | Predictors | $R^2$ |
|---|---|---|
| A | `C(dominant_hand)` alone | 0.196 |
| B | `C(dominant_hand) + C(finger)` | 0.262 |
| C | `C(hand) + C(finger)` | 0.306 |

Model C replaces the *derived* indicator "was this your dominant hand" with the *raw* fact of which
hand was used, and fits noticeably better: tapping with the right hand adds about 51.9 taps, the
pinky penalty is about 30.9, and both are significant at $p < 0.005$. B and C use different
predictors for the same underlying idea, so this is not a nested-model comparison; it is a reminder
that two variables can tell "the same story" — hand dominance — and still not carry the same
information once a line is actually fit through the data, because whichever hand happens to be more
common in the sample can absorb variation that the more abstract dominance label does not.

## Bringing in outside covariates

A second, independent dataset comes from a self-reported Google Form (65 respondents), carrying the
same finger/hand/handedness fields plus hours of sleep, whether the respondent plays video games,
and a sport variable. Three specifications, each adding one extra predictor to
`C(finger) + C(dominant_hand)`, are fit in turn:

| Added predictor | $R^2$ | coefficient | $p$-value |
|---|---|---|---|
| `sleep_hrs` | 0.326 | $-9.40$ per hour | 0.134 |
| `sport` | 0.308 | $+1.20$ | 0.405 |
| `C(gamer)` | 0.384 | $+58.56$ (Yes) | 0.005 |

Only the gaming indicator clears conventional significance in this sample of 65; sleep and sport,
despite showing sizeable-looking coefficients, do not. With three separate candidate additions
tried and only one significant, that is a result to hold loosely rather than treat as established —
unlike `finger` and `dominant_hand`, which come out significant, in the same direction, in both this
dataset and the first one.

## From an event stream to a time series: binning taps into windows

The subject-level totals throw away *when* within the minute each tap happened. The full per-tap
table, `df_all`, keeps every tap's timestamp for all 101 subjects (34,113 taps in total) and lets
the notebook ask a different question: does the tapping rate change over the course of the 60
seconds?

To answer it, each tap's time is assigned to a 10-second window, $\text{time\_bin} = \lfloor
t_{\text{seconds}} / 10 \rfloor$, and taps are counted within each (subject, window) pair to give
`taps_bin`. This is the general move needed whenever irregular event times — taps, arrivals, spikes
— have to become a regularly spaced count series before a regression, or later a proper time series
model, can be fit to them.

<figure>
<svg viewBox="0 0 340 240" role="img" aria-label="Individual tap times over one minute collapsed into 10-second bins, with bar height showing the declining tap count per bin">
  <line x1="20" y1="40" x2="320" y2="40" stroke="currentColor" stroke-width="1.2"/>
  <g stroke="currentColor" stroke-width="1">
    <line x1="28" y1="34" x2="28" y2="46"/>
    <line x1="41" y1="34" x2="41" y2="46"/>
    <line x1="55" y1="34" x2="55" y2="46"/>
    <line x1="70" y1="34" x2="70" y2="46"/>
    <line x1="88" y1="34" x2="88" y2="46"/>
    <line x1="108" y1="34" x2="108" y2="46"/>
    <line x1="128" y1="34" x2="128" y2="46"/>
    <line x1="150" y1="34" x2="150" y2="46"/>
    <line x1="172" y1="34" x2="172" y2="46"/>
    <line x1="196" y1="34" x2="196" y2="46"/>
    <line x1="220" y1="34" x2="220" y2="46"/>
    <line x1="246" y1="34" x2="246" y2="46"/>
    <line x1="272" y1="34" x2="272" y2="46"/>
    <line x1="298" y1="34" x2="298" y2="46"/>
  </g>
  <text x="170" y="20" text-anchor="middle" font-size="12" fill="currentColor">raw tap times (illustrative spacing)</text>

  <line x1="20" y1="200" x2="320" y2="200" stroke="currentColor" stroke-width="1.2"/>
  <g fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1">
    <rect x="30" y="68" width="44" height="132"/>
    <rect x="90" y="92" width="44" height="108"/>
    <rect x="150" y="100" width="44" height="100"/>
    <rect x="210" y="90" width="44" height="110"/>
    <rect x="270" y="104" width="44" height="96"/>
  </g>
  <text x="52" y="215" text-anchor="middle" font-size="11" fill="currentColor">0-10s</text>
  <text x="112" y="215" text-anchor="middle" font-size="11" fill="currentColor">10-20s</text>
  <text x="172" y="215" text-anchor="middle" font-size="11" fill="currentColor">20-30s</text>
  <text x="232" y="215" text-anchor="middle" font-size="11" fill="currentColor">30-40s</text>
  <text x="292" y="215" text-anchor="middle" font-size="11" fill="currentColor">40-50s</text>
  <text x="52" y="62" text-anchor="middle" font-size="11" fill="currentColor">66</text>
  <text x="112" y="86" text-anchor="middle" font-size="11" fill="currentColor">54</text>
  <text x="172" y="94" text-anchor="middle" font-size="11" fill="currentColor">52</text>
  <text x="232" y="84" text-anchor="middle" font-size="11" fill="currentColor">55</text>
  <text x="292" y="98" text-anchor="middle" font-size="11" fill="currentColor">50</text>
</svg>
<figcaption>Subject 0's first five 10-second bins: individual tap timestamps (top) collapse into a
count per window (bars), the object the trend regression below is fit to.</figcaption>
</figure>

## Fitting a trend to the binned counts

With `taps_bin` as the response and `time_bin` (0 through 5, the six 10-second windows in a minute)
as the predictor, the simplest model,

$$\text{taps\_bin} = \beta_0 + \beta_1\cdot\text{time\_bin} + \varepsilon,$$

gives $\hat\beta_0 = 60.46$ and $\hat\beta_1 = -1.56$ ($p < 0.001$): the average subject taps about
1.56 fewer times in each successive 10-second window. Over the five steps from the first bin to the
last, that is a predicted decline of about 7.8 taps — roughly 13% of the starting rate. $R^2$ is
small here (0.062) because this model ignores every between-subject difference — finger, hand —
established earlier.

Adding those back in, with an interaction between the time trend and finger,

$$\text{taps\_bin} = \beta_0 + \beta_1\cdot\text{time\_bin} + \beta_2\cdot\text{pinky} +
\beta_3\cdot\text{dominant\_hand} + \beta_4\cdot(\text{time\_bin}\times\text{pinky}) + \varepsilon,$$

raises $R^2$ to 0.282. The main effects repeat the earlier story — pinky taps about 6.3 fewer per
bin ($p<0.001$), the dominant hand taps about 8.3 more ($p<0.001$) — and the time trend for the
index finger is $-1.75$ per bin ($p<0.001$). The interaction term, $+0.45$, is not significant
($p = 0.305$): there is no detectable evidence in this data that the pinky fatigues at a different
rate than the index finger — it is simply slower throughout, at roughly the same rate of decline.

## Sources

- Notebook `TippyTaps.md` (converted from `TippyTaps.ipynb`), Stat153/248, Berkeley, Spring 2026,
  "Lecture 7 and 8 Finger Tapping Exercise" — the sole input for this chapter. Every coefficient,
  $p$-value, $R^2$, and sample size above is read directly from the code and printed `statsmodels`
  output in that notebook.
- The notebook is explicitly marked "in progress" and carries no narrative markdown beyond its
  title; the exposition above is built from the code, the variable names, and the regression output,
  not from a lecturer's commentary — no transcript was supplied for this lecture.
- Four plots in the notebook (`t_seconds` vs. `tap_index` by finger; `dt_seconds` by `dominant_hand`
  and finger; `hand` counts by `dominant_hand`; `ntaps` by `dominant_hand` and gamer, as a boxplot)
  are referenced above by their axes only — the rendered images were not part of the converted
  source.
- No transcript, written notes, or problem set were supplied for this lecture; no exercises section
  follows as a result.

---

[← 129. Stat 153 Course Syllabus](129-stat-153-course-syllabus.md) · [Contents](index.md)
