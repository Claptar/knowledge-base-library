---
title: "13. Multiple Linear Regression"
course: "GTPB Psls20"
chapter: 13
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 13. Multiple Linear Regression

## What this covers

Simple linear regression relates one outcome to one predictor. This chapter asks what changes when
several predictors are used at once: how the model and its coefficients are written down, how a
coefficient's meaning changes once other variables are "held fixed," how to test and interpret
several predictors jointly, and how to tell when the fitted model should not be trusted because two
predictors are saying almost the same thing, or because one data point is steering the whole fit. It
assumes the reader already has simple linear regression: least squares, the $\text{SSTot} =
\text{SSR} + \text{SSE}$ decomposition, $R^2$, and the $t$-test on a slope.

The running example throughout is a study of 97 men who had a radical prostatectomy, with prostate
specific antigen (PSA, on the log scale as `lpsa`) as the outcome and a set of clinical variables as
candidate predictors: log tumour volume (`lcavol`), log prostate weight (`lweight`), age, benign
prostate hypertrophy (`lbph`), seminal vesicle invasion (`svi`, present/absent), capsular penetration
(`lcp`), Gleason score, and the percentage of Gleason score 4/5 (`pgg45`).

## Why one predictor is rarely enough

Fitting a separate simple regression of the outcome on each predictor, one at a time, misses three
things that a multiple regression is built to capture:

1. **Confounding.** An association between $X$ and $Y$ can be driven by a third variable connected
   to both. In the prostate data, even if tumour volume were *not* really associated with PSA, men
   with a larger tumour volume can still show a higher PSA because their seminal vesicles are more
   often affected (`svi` status 1) — the tumour volume effect and the SVI effect are entangled
   unless both are in the model at once, so that patients with the *same* SVI status can be
   compared directly.
2. **Which group of variables matters for an outcome.** Assessing several possible drivers of a
   response simultaneously, rather than one at a time, is the only way to see which of them still
   matters once the others are accounted for.
3. **Prediction using several pieces of information at once.** Combining all the predictive
   information available — as is done routinely, for example, when estimating mortality risk in
   intensive care — needs a model that takes several predictors together, not one that is refit
   separately for each.

These three needs motivate extending simple linear regression to multiple predictors.

## The additive multiple linear model

With $p-1$ predictors $X_1,\dots,X_{p-1}$ and outcome $Y$ measured on $n$ subjects, the model is

$$Y_i = \beta_0 + \beta_1 X_{i1} + \dots + \beta_{p-1} X_{i,p-1} + \epsilon_i,$$

with $p$ unknown parameters $\beta_0,\beta_1,\dots,\beta_{p-1}$ and residuals $\epsilon_i$ carrying
whatever the predictors do not explain. As in the single-predictor case, the parameters are
estimated by least squares.

The fitted model does two things:

- **Predicts** the expected outcome for given predictor values,
  $$E[Y\mid X_1=x_1,\dots,X_{p-1}=x_{p-1}] = \hat\beta_0 + \hat\beta_1 x_1 + \dots + \hat\beta_{p-1}x_{p-1}.$$
- **Compares** two groups of subjects that differ by $\delta$ units in one predictor $X_j$ but agree
  on every other predictor $X_k$, $k\neq j$. Subtracting the two expected outcomes, every term but
  the $X_j$ term cancels:
  $$E(Y\mid \dots,X_j=x_j+\delta,\dots) - E(Y\mid\dots,X_j=x_j,\dots) = \beta_j\delta.$$

So $\beta_j$ is the difference in mean outcome between subjects who differ by one unit in $X_j$ but
have the same value of every other predictor in the model — equivalently, **the effect of $X_j$
corrected for the remaining predictors**. In the prostate model this is the effect of tumour volume
corrected for prostate weight and SVI status: comparing patients with the same weight and the same
SVI status, rather than comparing everyone regardless of those two.

Fitting `lpsa ~ lcavol` alone gives one slope for tumour volume; fitting `lpsa ~ lcavol + lweight +
svi` gives a *different* estimate of the tumour-volume slope, because it no longer has to absorb
whatever of the weight and SVI effects happened to travel along with tumour volume in this sample.
Geometrically, the multiple model with SVI included fits two parallel regression planes in
`(lcavol, lweight, lpsa)` — one for SVI absent, one for SVI present, offset from each other by the
SVI coefficient — rather than a single plane that ignores the split.

## Statistical inference for the coefficients

The least squares estimators are unbiased whenever the sample is representative, $E[\hat\beta_j] =
\beta_j$ for every $j$, with no further assumptions. Turning that into confidence intervals and
tests, however, needs the same four assumptions as simple regression:

1. **Linearity** of the mean outcome in the predictors.
2. **Independence** of the observations.
3. **Homoscedasticity**: the residual variance $\sigma^2$ is the same for every combination of
   predictor values.
4. **Normality**: $\epsilon_i \sim N(0,\sigma^2)$.

Under all four, $Y_i \sim N(\beta_0+\beta_1X_{i1}+\dots+\beta_{p-1}X_{i,p-1},\,\sigma^2)$, and the
residual variance is estimated by the mean squared error, now with $n-p$ degrees of freedom because
$p$ parameters had to be estimated first:

$$\hat\sigma^2 = \text{MSE} = \frac{\sum_{i=1}^n\left(y_i-\hat\beta_0-\hat\beta_1X_{i1}-\dots-\hat\beta_{p-1}X_{i,p-1}\right)^2}{n-p} = \frac{\sum_{i=1}^n e_i^2}{n-p}.$$

As before, each coefficient gets a standardised statistic

$$T_k = \frac{\hat\beta_k - \beta_k}{\text{SE}(\hat\beta_k)}, \qquad k=0,\dots,p-1,$$

which is $t$-distributed on $n-p$ degrees of freedom when all four assumptions hold, giving
confidence intervals $[\hat\beta_j - t_{n-p,\alpha/2}\text{SE}_{\hat\beta_j},\ \hat\beta_j +
t_{n-p,\alpha/2}\text{SE}_{\hat\beta_j}]$ and the usual test of $H_0:\beta_j=0$ against
$H_1:\beta_j\neq0$. If normality fails but linearity, independence and homoscedasticity hold, $T_k$
is still approximately normal in large samples by the central limit theorem, so the machinery
degrades gracefully rather than breaking outright. Fitting the residual diagnostics (`plot(lm)`)
against these assumptions is exactly the check to run before trusting any of the intervals or tests.

## When the model is not additive: interaction

The model above is called **additive** because the contribution of each predictor to the mean
outcome does not depend on the value of any other predictor — the slope for `lcavol` is the same
whatever `lweight` and `svi` happen to be. Algebraically, this is exactly the cancellation used
above to get $\beta_j\delta$: nothing about $x_w$ or $x_s$ survives in the difference.

But it is entirely possible that the association between tumour volume and PSA genuinely *depends*
on prostate weight — that the difference in PSA for a one-unit change in log tumour volume is larger
for men with heavy prostates than for men with light ones. To let the model say that, add a *product
term* of the two predictors:

$$Y_i = \beta_0 + \beta_v x_{iv} + \beta_w x_{iw} + \beta_s x_{is} + \beta_{vw}x_{iv}x_{iw} + \epsilon_i.$$

Recomputing the same subtraction as before, but now for a one-unit change in $X_v$ holding $X_w$ and
$X_s$ fixed, the product term no longer cancels:

$$E(Y\mid X_v{=}x_v{+}1,\dots) - E(Y\mid X_v{=}x_v,\dots) = \beta_v + \beta_{vw}x_w.$$

The effect of tumour volume is now $\beta_v + \beta_{vw}x_w$ — it *depends on* $x_w$, exactly the
dependence the additive model ruled out. $\beta_{vw}$ is the **interaction** (or effect
modification) coefficient, and $\beta_vx_{iv}$, $\beta_wx_{iw}$ are called the **main effects** of
the two predictors involved in the interaction. Fitted on the prostate data, the estimated
`lcavol:lweight` interaction was not statistically significant — and because the main effects that
enter an interaction term cannot be interpreted on their own once that term is in the model, the
practical rule is to drop non-significant interaction terms first, and only then read off the main
effects.

An interaction between a continuous predictor and a binary factor works the same way. Adding
`svi:lcavol` and `svi:lweight` to the prostate model gives

$$Y = \beta_0 + \beta_vX_v + \beta_wX_w + \beta_sX_s + \beta_{vs}X_vX_s + \beta_{ws}X_wX_s + \epsilon,$$

and because $X_s\in\{0,1\}$ is a dummy variable, this single equation is really two separate
regression planes:

- **SVI absent** ($X_s=0$): $Y = \beta_0 + \beta_vX_v + \beta_wX_w + \epsilon$.
- **SVI present** ($X_s=1$): $Y = (\beta_0+\beta_s) + (\beta_v+\beta_{vs})X_v + (\beta_w+\beta_{ws})X_w + \epsilon$.

So the interaction terms let the intercept **and both slopes** differ between the two SVI groups,
rather than just shifting one plane up or down as the additive model does.

<figure>
<svg viewBox="0 0 460 220" role="img" aria-label="Two regression lines for two groups: parallel under an additive model, non-parallel once an interaction term is added">
  <line x1="40" y1="190" x2="230" y2="190" stroke="currentColor" stroke-width="1.2"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.2"/>
  <text x="135" y="208" text-anchor="middle" font-size="12" fill="currentColor">lcavol</text>
  <text x="20" y="105" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 20 105)">lpsa</text>
  <line x1="40" y1="160" x2="220" y2="70" stroke="currentColor" stroke-width="1.6"/>
  <line x1="40" y1="120" x2="220" y2="30" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/>
  <text x="228" y="72" font-size="11" fill="currentColor">svi = 0</text>
  <text x="228" y="32" font-size="11" fill="currentColor">svi = 1</text>
  <text x="135" y="14" text-anchor="middle" font-size="12" fill="currentColor">additive: same slope</text>

  <line x1="270" y1="190" x2="440" y2="190" stroke="currentColor" stroke-width="1.2"/>
  <line x1="270" y1="190" x2="270" y2="20" stroke="currentColor" stroke-width="1.2"/>
  <text x="355" y="208" text-anchor="middle" font-size="12" fill="currentColor">lcavol</text>
  <line x1="270" y1="150" x2="440" y2="100" stroke="currentColor" stroke-width="1.6"/>
  <line x1="270" y1="60" x2="440" y2="160" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 4"/>
  <text x="444" y="102" font-size="11" fill="currentColor">svi = 0</text>
  <text x="444" y="162" font-size="11" fill="currentColor">svi = 1</text>
  <text x="355" y="14" text-anchor="middle" font-size="12" fill="currentColor">with interaction: slopes differ</text>
</svg>
<figcaption>Left: an additive model forces the two SVI groups' regression lines to be parallel — the
SVI effect is only a vertical shift. Right: adding an lcavol&#215;svi interaction lets the slope
itself differ between groups, so the tumour-volume effect depends on SVI status.</figcaption>
</figure>

## Partitioning variance: the ANOVA table for multiple regression

The sum-of-squares decomposition carries over unchanged in form:

$$\text{SSTot} = \sum_{i=1}^n(Y_i-\bar Y)^2, \qquad \text{SSE} = \sum_{i=1}^n(Y_i-\hat Y_i)^2, \qquad \text{SSR} = \sum_{i=1}^n(\hat Y_i-\bar Y)^2, \qquad \text{SSTot}=\text{SSR}+\text{SSE}.$$

Only the degrees of freedom change, because $p$ parameters are now estimated instead of two:

| Source | df | Mean square |
|---|---|---|
| Regression | $p-1$ | $\text{MSR}=\text{SSR}/(p-1)$ |
| Error | $n-p$ | $\text{MSE}=\text{SSE}/(n-p)$ |
| Total | $n-1$ | $\text{SSTot}/(n-1)$ |

$\text{SSTot}/(n-1)$ estimates the total (marginal) variance of $Y$; $\text{MSE}$ estimates the
residual variance $\sigma^2$ left after conditioning on all $p-1$ predictors. $R^2$ is unchanged in
form, $R^2 = 1-\text{SSE}/\text{SSTot} = \text{SSR}/\text{SSTot}$, still the fraction of total
variability the model explains. The global test that *none* of the predictors matter,
$$H_0:\beta_1=\dots=\beta_{p-1}=0,$$
uses $F=\text{MSR}/\text{MSE}$, which under $H_0$ follows an $F_{p-1,n-p}$ distribution — one test
for the whole set of predictors at once, rather than $p-1$ separate $t$-tests.

**Additional (partial) sums of squares.** Compare a smaller model with only $X_1$ to a larger model
adding $X_2$:
$$Y_i=\beta_0+\beta_1X_{i1}+\epsilon_i \qquad\text{vs.}\qquad Y_i=\beta_0+\beta_1X_{i1}+\beta_2X_{i2}+\epsilon_i.$$
$\text{SSTot}$ is identical for both, since it only depends on the response, so each model gives its
own decomposition $\text{SSTot}=\text{SSR}_1+\text{SSE}_1=\text{SSR}_2+\text{SSE}_2$. The
**additional sum of squares** of $X_2$ over the model that already has $X_1$ is defined as
$$\text{SSR}_{2\mid1} = \text{SSE}_1-\text{SSE}_2 = \text{SSR}_2-\text{SSR}_1$$
(the two expressions agree automatically, by the shared decomposition), and it is read as the extra
variability that adding $X_2$ explains once $X_1$ is already in the model. It refines the three-way
split of total variability into
$$\text{SSTot} = \text{SSR}_1 + \text{SSR}_{2\mid1} + \text{SSE},$$
which follows directly from the definition — this is the tool for asking whether one particular
predictor (or block of predictors) is pulling its weight once the others are already accounted for.

## Multicollinearity

Adding predictors only helps if they carry somewhat separate information. When two or more
predictors are strongly correlated with each other, the model cannot tell their effects apart —
each coefficient becomes far less precise, even though the model as a whole may predict well. This
is diagnosed with the **variance inflation factor (VIF)**, computed per predictor; the rule of thumb
used in the lecture is that a VIF above about 10 signals strong multicollinearity.

The point is made directly with a body-fat dataset, where body fat is regressed on triceps skinfold,
thigh circumference and mid-arm circumference. Regressing `Midarm` on `Triceps` and `Thigh` alone
shows that mid-arm circumference is itself almost fully predictable from the other two measurements
— exactly the situation VIF is built to catch: one predictor is nearly a linear combination of the
others, so including all three buys little extra information at the cost of very unstable
coefficient estimates.

The same diagnostic applied to the prostate models shows VIFs rising once the `lcavol:lweight`
interaction term is added. This inflation is a different phenomenon from the body-fat case: it is
not that `lcavol` and `lweight` are newly collinear, but that a main effect's *meaning* has changed
once an interaction term involving it is in the model, which is a further reason to drop
non-significant interaction terms rather than leave them in.

## Influential observations

A regression fit should not be dictated by a single data point. Two separate diagnostics are used to
spot problem observations: **studentized residuals** flag points whose outcome is unusual given the
fitted model, and **leverage** flags points whose *predictor* values are unusual compared to the
rest of the data. Neither on its own says a point actually changes the fit — that needs both at
once, which is exactly what **Cook's distance** measures. For observation $i$,

$$D_i = \frac{\sum_{j=1}^n(\hat Y_j - \hat Y_{j(i)})^2}{p\,\text{MSE}},$$

comparing every fitted value with and without observation $i$ in the data. $D_i$ is considered
extreme once it exceeds the 50% quantile of the $F_{p+1,\,n-(p+1)}$ distribution — that is, once
leaving observation $i$ out would move the fitted surface further than would be expected from chance
alone.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Three ways to add one point to a trend, only one of which noticeably rotates the fitted line">
  <line x1="40" y1="185" x2="310" y2="185" stroke="currentColor" stroke-width="1.2"/>
  <line x1="40" y1="185" x2="40" y2="20" stroke="currentColor" stroke-width="1.2"/>
  <text x="175" y="205" text-anchor="middle" font-size="12" fill="currentColor">x</text>
  <text x="18" y="105" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 18 105)">y</text>

  <circle cx="60" cy="168" r="2.5" fill="currentColor"/>
  <circle cx="85" cy="158" r="2.5" fill="currentColor"/>
  <circle cx="105" cy="150" r="2.5" fill="currentColor"/>
  <circle cx="130" cy="140" r="2.5" fill="currentColor"/>
  <circle cx="150" cy="132" r="2.5" fill="currentColor"/>
  <circle cx="175" cy="118" r="2.5" fill="currentColor"/>
  <circle cx="195" cy="108" r="2.5" fill="currentColor"/>
  <circle cx="215" cy="98" r="2.5" fill="currentColor"/>

  <line x1="40" y1="178" x2="300" y2="55" stroke="currentColor" stroke-width="1.6"/>

  <circle cx="150" cy="60" r="3.5" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="150" y="48" text-anchor="middle" font-size="10" fill="currentColor">outlier, ordinary x</text>

  <circle cx="295" cy="60" r="3.5" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="295" y="48" text-anchor="middle" font-size="10" fill="currentColor">extreme x, on trend</text>

  <circle cx="295" cy="150" r="3.5" fill="currentColor"/>
  <text x="270" y="168" text-anchor="middle" font-size="10" fill="currentColor">extreme x, off trend</text>

  <line x1="40" y1="170" x2="300" y2="140" stroke="currentColor" stroke-width="1.4" stroke-dasharray="5 4"/>
  <text x="230" y="128" text-anchor="middle" font-size="10" fill="currentColor">refit with that point</text>
</svg>
<figcaption>Adding one extra point to the same trend. An outlier at an ordinary predictor value, or
an extreme predictor value that still lies on the trend, barely moves the fitted line. Only the
point that is both extreme in x and off the trend (filled circle) has high leverage and a large
residual together, and it visibly rotates the line — this is what a large Cook's distance is
catching.</figcaption>
</figure>

Once an observation is flagged as influential overall, **DFBETAS** breaks the influence down
parameter by parameter:
$$\text{DFBETAS}_{j(i)} = \frac{\hat\beta_j - \hat\beta_{j(i)}}{\text{SD}(\hat\beta_j)},$$
the standardised change in coefficient $j$ when observation $i$ is dropped. A DFBETAS is considered
extreme once it exceeds 1 in small to moderate datasets, or $2/\sqrt n$ in large ones. Together, Cook's
distance says *whether* a point matters and DFBETAS says *for which coefficient* it matters — useful,
for instance, for tracing an inflated interaction-term VIF or an unexpectedly large slope back to one
or two specific patients.

## Sources

- `docs/omics-statistics/gtpb/psls20/theory/08-MultipleRegression/01-intro.md` — motivation for
  multiple predictors and the prostate cancer dataset.
- `docs/omics-statistics/gtpb/psls20/theory/08-MultipleRegression/02-additive-multiple-linair-model.md`
  — the additive model, coefficient interpretation, and the confounding argument.
- `docs/omics-statistics/gtpb/psls20/theory/08-MultipleRegression/03-inference-in-multiple-linear-models.md`
  — inference assumptions, tests and confidence intervals, and interaction models (continuous&times;continuous
  and continuous&times;factor).
- `docs/omics-statistics/gtpb/psls20/theory/08-MultipleRegression/04-anova-tabel.md` — the ANOVA
  decomposition, additional sums of squares, multicollinearity/VIF and the body-fat example, and
  influential-observation diagnostics (Cook's distance, DFBETAS, the synthetic leverage example).

All four files are converted slides from GTPB PSLS20, `theory/08-MultipleRegression.Rmd` (CC BY
4.0); no separate transcript or problem set was supplied for this lecture. The chapter reuses the
$\text{SSTot}$/$\text{SSE}$/$\text{SSR}$/MSE/$R^2$ notation established in the course's simple linear
regression lecture (`theory/06-linearRegression`), which this chapter builds on directly. The R code
chunks embedded in the source (data loading, `lm()` calls, `plot3D` surfaces, `vif()`, `cooks.distance()`,
`dfbetasPlots()`) are not reproduced verbatim here; what each one was demonstrating is described in
the relevant section instead.

---

[← 12. ANOVA Case Studies](12-anova-case-studies.md) · [Contents](index.md) · [14. Kruskal-Wallis Test for g Groups →](14-kruskal-wallis-test-for-g-groups.md)
