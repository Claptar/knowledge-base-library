---
title: "22. Breast Cancer Dataset"
course: "GTPB Psls20"
chapter: 22
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 22. Breast Cancer Dataset

## What this covers

A worked case study in simple linear regression: is the expression of the gene *S100A8* associated
with expression of *ESR1* in breast cancer tumours? It assumes the reader already has simple linear
regression — the model $Y_i \mid X_i \sim N(\beta_0+\beta_1X_i,\sigma^2)$, the t-test and confidence
interval on the slope, and the residual diagnostics for checking the model's assumptions — and shows
how those pieces are actually used on a real, noisy, biological dataset: why the data get
transformed before fitting, how the assumptions are checked rather than assumed, and how a
regression coefficient on a transformed scale gets turned back into a statement about fold changes.

## The dataset and the question

The data are a subset of a published study of 32 breast cancer patients, all with an
estrogen-receptor-positive (ER+) tumour treated with the hormone therapy tamoxifen. For each
patient the data record the tumour's histological grade (1 or 3), lymph node status (affected and
removed, or not), tumour size, and the expression of two genes measured in the tumour biopsy by
microarray: *ESR1* and *S100A8*.

The two genes matter for different reasons:

- *ESR1* encodes the estrogen receptor and is active in around 75% of breast cancer tumours.
  A tumour that expresses ER is one that responds to hormone therapy, because tamoxifen works by
  interacting with the estrogen receptor and modulating the genes it controls.
- *S100A8* is a member of the S100 protein family, which is frequently dysregulated in cancer.
  S100A8 expression is thought to suppress the local immune response and create an inflammatory
  environment that promotes tumour growth.

Both genes are biologically implicated in the tumour, but by different mechanisms. That raises a
question that is purely statistical once it is posed: **is the expression of *S100A8* associated
with the expression of *ESR1*** in these tumours, and how strong is that association?

## Looking at the data before modelling

Before fitting anything, the data are plotted. With several variables recorded, a scatterplot
matrix (a grid of pairwise scatterplots, `ggpairs`) gives a first look at all the pairwise
relationships at once. Attention then narrows to the pair of interest: *S100A8* expression against
*ESR1* expression.

Plotted on the raw scale, the relationship is visibly there but **not linear** — it curves. A
straight line fitted through the points does not track the trend that a smooth curve (a loess fit)
picks out. This matters because Pearson correlation and simple linear regression are both built to
detect *linear* association; a real but curved relationship can look weak to them even when it is
strong.

Gene expression concentrations are typically right-skewed, and a standard remedy is a **log
transform**. Taking $\log_2$ of both *ESR1* and *S100A8* expression and re-plotting, the
relationship becomes linear: the curve and the straight line now agree closely.

<figure>
<svg viewBox="0 0 620 230" role="img" aria-label="Schematic scatterplots showing a curved relationship between S100A8 and ESR1 expression on the raw scale that becomes linear after log2 transformation">
  <text x="150" y="14" text-anchor="middle" font-size="12" fill="currentColor">raw scale</text>
  <line x1="40" y1="200" x2="260" y2="200" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="20" x2="40" y2="200" stroke="currentColor" stroke-width="1"/>
  <text x="150" y="218" text-anchor="middle" font-size="11" fill="currentColor">ESR1</text>
  <text x="14" y="110" text-anchor="middle" font-size="11" fill="currentColor" transform="rotate(-90 14 110)">S100A8</text>
  <path d="M40,20 C90,140 150,175 260,191" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="60" x2="260" y2="160" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
  <g fill="currentColor">
    <circle cx="50" cy="45" r="2.5"/>
    <circle cx="75" cy="95" r="2.5"/>
    <circle cx="100" cy="118" r="2.5"/>
    <circle cx="125" cy="148" r="2.5"/>
    <circle cx="150" cy="152" r="2.5"/>
    <circle cx="175" cy="168" r="2.5"/>
    <circle cx="200" cy="182" r="2.5"/>
    <circle cx="225" cy="190" r="2.5"/>
    <circle cx="245" cy="185" r="2.5"/>
    <circle cx="258" cy="193" r="2.5"/>
  </g>
  <text x="470" y="14" text-anchor="middle" font-size="12" fill="currentColor">log2 scale</text>
  <line x1="360" y1="200" x2="580" y2="200" stroke="currentColor" stroke-width="1"/>
  <line x1="360" y1="20" x2="360" y2="200" stroke="currentColor" stroke-width="1"/>
  <text x="470" y="218" text-anchor="middle" font-size="11" fill="currentColor">log2 ESR1</text>
  <text x="334" y="110" text-anchor="middle" font-size="11" fill="currentColor" transform="rotate(-90 334 110)">log2 S100A8</text>
  <line x1="360" y1="30" x2="580" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <g fill="currentColor">
    <circle cx="380" cy="50" r="2.5"/>
    <circle cx="395" cy="58" r="2.5"/>
    <circle cx="410" cy="60" r="2.5"/>
    <circle cx="440" cy="95" r="2.5"/>
    <circle cx="470" cy="105" r="2.5"/>
    <circle cx="500" cy="140" r="2.5"/>
    <circle cx="520" cy="138" r="2.5"/>
    <circle cx="530" cy="148" r="2.5"/>
    <circle cx="560" cy="170" r="2.5"/>
    <circle cx="575" cy="182" r="2.5"/>
  </g>
</svg>
<figcaption>Schematic of the shape seen in the exploratory plots: on the raw scale (left) the
smooth trend (curve) and the straight-line fit (dashed) disagree, because the true relationship is
convex, not linear. After log2-transforming both genes (right), the smooth trend and the straight
line coincide.</figcaption>
</figure>

## Pearson and Spearman correlation

Two correlation coefficients are computed, on both the raw and the log2-transformed data:

- **Pearson correlation** measures the strength of a *linear* association.
- **Spearman correlation** is Pearson correlation applied to the *ranks* of the data, so it
  measures the strength of any *monotonic* association, linear or not, and is unaffected by a
  monotonic transformation such as $\log_2$.

Both correlations come out negative, consistent with the visual impression that higher *ESR1*
goes with lower *S100A8*. The instructive part is how they compare:

- On the **raw scale**, the Spearman correlation is much larger in absolute value than the
  Pearson correlation. Pearson correlation is penalised by the curvature: a real monotonic
  relationship that is not linear is not fully captured by a coefficient that only measures linear
  association.
- On the **log2 scale**, the Pearson correlation rises to match the Spearman correlation, because
  log-transforming has made the relationship linear. The Spearman correlation itself barely
  changes between the two scales — it cannot, since $\log_2$ is a monotonic transformation and rank
  correlation depends only on the ordering of the values, not the scale they are measured on.

This is the diagnostic that justifies working on the log2 scale from here on: it is the scale on
which the association is (close to) linear, so it is the scale on which a linear-regression model,
and the Pearson correlation that goes with it, are appropriate tools.

## The regression model

Having decided to work on the log2 scale, the association is modelled as simple linear regression:

$$Y_i \mid X_i \sim N(\beta_0 + \beta_1 X_i, \sigma^2)$$

where $Y_i$ is the $\log_2$-transformed *S100A8* expression of subject $i$ and $X_i$ is the
$\log_2$-transformed *ESR1* expression of subject $i$.

Fitting this model (`lm`) requires its assumptions to hold, and they are not simply assumed —
they are checked:

1. **Independence.** The subjects were sampled at random from the population, so their outcomes
   are treated as independent. This one is a property of the study design, not something read off
   a plot.
2. **Linearity.** Checked by plotting the residuals against the fitted values: if the model is
   missing curvature that is really in the data, the residuals will show a trend rather than being
   scattered evenly around zero.
3. **Equal variance (homoscedasticity).** Checked from the same residuals-vs-fitted plot: the
   spread of the residuals should stay roughly constant across the range of fitted values, not
   fan out or narrow.
4. **Normally distributed residuals.** Checked with a normal QQ-plot of the residuals: points
   should fall close to the diagonal, with no substantial systematic curve or heavy tail.

For this fit, the residuals are spread evenly around zero with no visible trend and roughly
constant spread, and the QQ-plot shows no substantial deviation from a straight line. The
assumptions hold well enough on the log2 scale to trust the inference that follows — which is
exactly why the earlier step of finding the right scale mattered: the same diagnostics would have
flagged a problem had the model been fit on the untransformed data.

## Testing the association: the slope

The biological question — is there an association between the two genes' expression — translates
into a statement about the slope of the fitted line. If $\beta_1=0$, expression of *ESR1* carries
no linear information about expression of *S100A8*; if $\beta_1\neq0$, it does. So the hypotheses
are

$$H_0:\ \beta_1 = 0 \qquad\text{vs.}\qquad H_1:\ \beta_1\neq 0.$$

The logic runs in the direction of falsification, not confirmation: data can never *prove* the
alternative that an association exists, so instead the model tests whether the no-association
null can be rejected. The two standard tools for this are the same ones used for any slope in
simple linear regression:

- a **t-test** on $\hat\beta_1$, read off the regression summary, and
- a **confidence interval** for $\beta_1$, which adds information the test alone does not give:
  not just whether the association is detectable, but how large it plausibly is.

Both the test and the interval here point the same way: the association is extremely significant,
and the interval is far enough from zero, and narrow enough, to say the association is not only
statistically detectable but large enough to matter biologically.

## Reading the coefficient as a fold change

The model was fit on the log2 scale, so $\hat\beta_1$ is a slope in log2 units — not directly an
interpretable biological quantity on its own. Exponentiating base 2 undoes the transform and turns
the coefficient into a **fold change**: $2^{\hat\beta_1}$ is the multiplicative change in
(untransformed) *S100A8* expression associated with a doubling of *ESR1* expression, and applying
the same transform to the endpoints of the confidence interval for $\beta_1$ gives a confidence
interval for that fold change.

This is the general move for interpreting a coefficient estimated on a log2 scale: additive on the
log scale becomes **multiplicative** on the original scale, and the natural unit of $X$ becomes "a
doubling of $X$" rather than "one unit of $X$".

## Conclusion

There is an extremely significant negative association between *S100A8* expression and *ESR1*
expression. In fold-change terms: a patient whose *ESR1* expression is twice that of another
patient has, on average, a lower *S100A8* expression by a factor read off from $2^{\hat\beta_1}$,
with the corresponding confidence interval giving the plausible range for that factor. The result
is consistent with the biological picture that motivated the question: a tumour with an active
estrogen receptor pathway (high *ESR1*, responsive to tamoxifen) tends to have less of the
inflammation-promoting *S100A8* signal.

## Sources

This chapter is built entirely from the converted tutorial notes for this exercise; no slide deck
or lecture transcript was supplied for it.

- Data, biological background, exploratory plots, log2 transform, and Pearson/Spearman
  correlation: `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/06_linearRegression/breastcancerExample/01-breast-cancer-dataset.md`.
- Regression model, assumption checking, hypothesis test on the slope, and back-transformation to
  fold change: `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/06_linearRegression/breastcancerExample/02-model.md`.
- The dataset is a subset of the study at https://doi.org/10.1093/jnci/djj052, cited in the notes
  but not otherwise described there.
- The notes give the R code that produces the scatterplots, residual and QQ diagnostic plots, and
  the numerical output of `summary(lm)`, `confint(lm)`, and the back-transformed coefficients, but
  the underlying `.Rmd` file was not executed as part of this material, so no rendered plots or
  numeric estimates (coefficients, $p$-value, confidence interval bounds) were available to quote;
  the discussion above reports only the qualitative conclusions the notes themselves state.

---

[← 21. One-Way ANOVA Worked Example](21-one-way-anova-worked-example.md) · [Contents](index.md) · [23. Smelly Armpit Data Exploration →](23-smelly-armpit-data-exploration.md)
