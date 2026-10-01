---
title: "9. Simple Linear Regression"
course: "GTPB Psls20"
chapter: 9
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 9. Simple Linear Regression

## What this covers

This chapter builds simple linear regression from the ground up: how a straight-line model for a
conditional mean is fit by least squares, what extra assumptions turn that fit into something you
can attach a confidence interval or p-value to, how to check those assumptions and what to do when
they fail, and how the same machinery gives prediction intervals, the sum-of-squares decomposition
behind $R^2$ and the F-test, and the two-sample t-test as a special case. It assumes you already
have expectation and conditional expectation, the normal and $t$ distributions, and confidence
intervals and hypothesis tests for a single mean. The running example is a set of 32 breast-cancer
patients whose tumour biopsies were profiled for gene expression.

## The breast cancer dataset

The data are a subset of a published study (<https://doi.org/10.1093/jnci/djj052>): 32 patients
with an estrogen-receptor-positive tumour who were treated with tamoxifen chemotherapy. For each
patient the dataset records the histological grade of the tumour (grade 1 vs. grade 3), lymph node
status (node = 0 if unaffected, 1 if lymph nodes were affected and removed), tumour size, and the
expression level of two genes, **ESR1** and **S100A8**, measured in the tumour biopsy by microarray.

The biology motivates the question. ESR1 (the estrogen receptor gene) is expressed in roughly 75%
of breast tumours; a tumour that expresses it responds to hormone therapy, and tamoxifen works by
interacting with the receptor and modulating gene expression. Proteins of the S100 family are often
dysregulated in cancer, and S100A8 in particular represses the immune system in the tumour and
creates an inflammatory environment that promotes tumour growth. So it is natural to ask whether
ESR1 and S100A8 expression are associated in this sample — and, if so, how strongly.

For didactic reasons the first pass through the analysis removes three outliers in the S100A8
measurements and works with this trimmed subset; the chapter returns later to how to handle the
full data properly, without throwing points away.

## The linear regression model

Linear regression is a way to assess the association between two variables $(X_i, Y_i)$, measured
on each of $n$ subjects $i = 1, \dots, n$ — here $X$ is ESR1 expression and $Y$ is S100A8
expression. For a fixed value of $X$, $Y$ does not have to take the same value every time: there is
signal and there is noise,
$$Y_i = g(X_i) + \epsilon_i,$$
where $g(x)$ is defined as the expected outcome for subjects with $X_i = x$,
$$E[Y_i \mid X_i = x] = g(x).$$
It follows that $\epsilon_i$ averages to zero among subjects who share the same $X_i$:
$E[\epsilon_i \mid X_i] = 0$.

To get results that are both *accurate* and *interpretable*, $g(x)$ is usually chosen to be linear
in an unknown intercept and slope:
$$E(Y \mid X = x) = \beta_0 + \beta_1 x.$$
This is a genuine *assumption* about the joint distribution of $X$ and $Y$, and it can be wrong. Its
payoff is that it is an efficient way to analyse the data, because every observation contributes to
learning the single line rather than to a separate estimate at each value of $x$.

The model supports two uses. For **prediction**, once the line is fit, $Y$ can be forecast from $X$
via $E(Y \mid X=x) = \beta_0 + \beta_1 x$. For **association**, the parameters have a direct
biological reading: the intercept is the mean response at $X=0$, $E(Y\mid X=0) = \beta_0$, and the
slope is the effect of a unit increase in the predictor,
$$E(Y \mid X = x+\delta) - E(Y \mid X = x) = \beta_0 + \beta_1(x+\delta) - \beta_0 - \beta_1 x = \beta_1 \delta.$$
So $\beta_1$ is the difference in mean outcome between subjects whose predictor differs by one unit.

## Parameter estimation: least squares

$\beta_0$ and $\beta_1$ are unknown population parameters and have to be estimated from the sample.
The natural criterion is to choose the line that fits best: for a given $x_i$, the point on the
line $(x_i, \beta_0+\beta_1 x_i)$ should sit as close as possible to the observed $(x_i, y_i)$.
Concretely, choose $\beta_0, \beta_1$ to minimise the sum of squared vertical distances between the
observations and the fitted line,
$$SSE = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2 = \sum_{i=1}^n e_i^2,$$
where the **residuals** $e_i$ are exactly those vertical distances. Minimising $SSE$ gives closed-form
estimators,
$$\hat\beta_1 = \frac{\sum_{i=1}^n (y_i-\bar y)(x_i-\bar x)}{\sum_{i=1}^n (x_i-\bar x)^2} = \frac{\mathrm{cor}(x,y)\, s_y}{s_x}, \qquad \hat\beta_0 = \bar y - \hat\beta_1 \bar x.$$
Notice that the least-squares slope is proportional to the correlation between response and
predictor — regression and correlation are two views of the same fact. Once fitted, the line can be
used exactly as before, with hats on the parameters: to predict the response at a given $x$, or to
compare the mean response between two groups that differ by $\delta$ in the predictor,
$$E[Y\mid X=x+\delta] - E[Y \mid X=x] = \hat\beta_1 \delta.$$

Fitting `lm(S100A8 ~ ESR1, brcaSubset)` on the outlier-trimmed data gives a negative $\hat\beta_1$:
expected S100A8 expression falls as ESR1 expression rises. Two cautions come with the fitted line.
First, extrapolation is dangerous: the linearity assumption can only be checked within the range of
the observed data, so predictions for ESR1 values far outside that range are not justified by
anything the fit has shown. Second — and this is the subject of the next two sections — a fitted
line is not yet evidence of an association; that requires a statistical model on top of the
geometry of least squares.

## Statistical inference: what has to be assumed

Least squares gives a best-fitting line for *any* data, whether or not there is a real association.
To draw conclusions — how much the estimators would vary from sample to sample, and how they behave
under the null hypothesis of no association — requires an explicit statistical model for the
distribution of $Y$ given $X$. Besides **linearity**, this needs three further assumptions:

- **Independence**: the pairs $(X_1,Y_1),\dots,(X_n,Y_n)$ come from $n$ independent subjects. This
  is needed to estimate the variance at all.
- **Homoscedasticity** (equal variances): observations vary with the same spread around the
  regression line everywhere — $\mathrm{var}(Y\mid X=x) = \sigma^2$ for every $x$, where $\sigma$ is
  called the *residual standard deviation*.
- **Normality**: the residuals $\epsilon_i$ are normally distributed.

Given independence, homoscedasticity and normality, $\epsilon_i$ are i.i.d. $N(0,\sigma^2)$; together
with linearity this means
$$Y_i \mid X_i \sim N(\beta_0 + \beta_1 X_i,\ \sigma^2).$$

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="Regression line with normal conditional distributions of equal spread centred on the line at three x-values">
  <line x1="30" y1="170" x2="300" y2="170" stroke="currentColor" stroke-width="1"/>
  <line x1="30" y1="170" x2="30" y2="20" stroke="currentColor" stroke-width="1"/>
  <line x1="45" y1="55" x2="290" y2="130" stroke="currentColor" stroke-width="1.5"/>
  <path d="M 90,25 Q 118,45 118,75 Q 118,105 90,125 Q 100,100 100,75 Q 100,50 90,25 Z" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <path d="M 170,45 Q 198,65 198,95 Q 198,125 170,145 Q 180,120 180,95 Q 180,70 170,45 Z" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <path d="M 250,65 Q 278,85 278,115 Q 278,145 250,165 Q 260,140 260,115 Q 260,90 250,65 Z" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="150" y="185" font-size="12" fill="currentColor">predictor X</text>
  <text x="10" y="95" font-size="12" fill="currentColor" transform="rotate(-90 10 95)">response Y</text>
</svg>
<figcaption>The four assumptions pictured together: each bump is a normal density of $Y$ at a fixed $x$,
of equal width (homoscedasticity), symmetric (normality), and centred exactly on the fitted line
(the mean function is correctly linear). Independence is not visible in a single picture — it is
about how the points were sampled, not about their shape.</figcaption>
</figure>

Under these assumptions one can show that the parameter estimators are themselves normally
distributed, with variances
$$\sigma^2_{\hat\beta_0} = \frac{\sum_{i=1}^n X_i^2}{\sum_{i=1}^n (X_i-\bar X)^2} \times \frac{\sigma^2}{n}, \qquad \sigma^2_{\hat\beta_1} = \frac{\sigma^2}{\sum_{i=1}^n (X_i-\bar X)^2},$$
$$\hat\beta_0 \sim N\!\left(\beta_0, \sigma^2_{\hat\beta_0}\right), \qquad \hat\beta_1 \sim N\!\left(\beta_1, \sigma^2_{\hat\beta_1}\right).$$

The formula for $\sigma^2_{\hat\beta_1}$ says something useful on its own: the more spread out the
$X$ values are, the larger $\sum(X_i-\bar X)^2$ is, and the smaller the variance of the slope
estimator — a widely spread predictor pins the slope down much more precisely than a tightly
clustered one.

<figure>
<svg viewBox="0 0 340 190" role="img" aria-label="Comparison of a narrow spread of X, where several slopes fit almost equally well, against a wide spread, where the slope is well determined">
  <text x="95" y="15" font-size="12" fill="currentColor" text-anchor="middle">narrow spread of X</text>
  <circle cx="90" cy="95" r="3" fill="currentColor"/>
  <circle cx="97" cy="88" r="3" fill="currentColor"/>
  <circle cx="84" cy="102" r="3" fill="currentColor"/>
  <circle cx="94" cy="108" r="3" fill="currentColor"/>
  <circle cx="88" cy="85" r="3" fill="currentColor"/>
  <line x1="20" y1="150" x2="170" y2="40" stroke="currentColor" stroke-width="1" stroke-opacity="0.5"/>
  <line x1="20" y1="60" x2="170" y2="150" stroke="currentColor" stroke-width="1" stroke-opacity="0.5"/>
  <line x1="20" y1="105" x2="170" y2="90" stroke="currentColor" stroke-width="1.5"/>
  <text x="95" y="172" font-size="11" fill="currentColor" text-anchor="middle">many slopes fit</text>
  <line x1="190" y1="0" x2="190" y2="190" stroke="currentColor" stroke-width="0.5" stroke-opacity="0.3"/>
  <text x="255" y="15" font-size="12" fill="currentColor" text-anchor="middle">wide spread of X</text>
  <circle cx="210" cy="70" r="3" fill="currentColor"/>
  <circle cx="235" cy="90" r="3" fill="currentColor"/>
  <circle cx="260" cy="105" r="3" fill="currentColor"/>
  <circle cx="285" cy="118" r="3" fill="currentColor"/>
  <circle cx="310" cy="135" r="3" fill="currentColor"/>
  <line x1="205" y1="62" x2="315" y2="140" stroke="currentColor" stroke-width="1" stroke-opacity="0.5"/>
  <line x1="205" y1="68" x2="315" y2="132" stroke="currentColor" stroke-width="1.5"/>
  <line x1="205" y1="74" x2="315" y2="126" stroke="currentColor" stroke-width="1" stroke-opacity="0.5"/>
  <text x="260" y="172" font-size="11" fill="currentColor" text-anchor="middle">slope pinned down</text>
</svg>
<figcaption>Since $\sigma^2_{\hat\beta_1} = \sigma^2/\sum_i(X_i-\bar X)^2$, a predictor that only
takes values close together (left) leaves many different slopes almost equally consistent with the
data, while the same noise spread over widely separated $X$ values (right) leaves much less room for
the slope to vary.</figcaption>
</figure>

The conditional variance $\sigma^2$ is itself unknown and is estimated by the **mean squared error**,
$$\hat\sigma^2 = MSE = \frac{\sum_{i=1}^n (y_i - \hat\beta_0 - \hat\beta_1 x_i)^2}{n-2} = \frac{\sum_{i=1}^n e_i^2}{n-2}.$$
This estimator relies on independence and equal variance, and it divides by $n-2$ rather than $n$
because two parameters, $\beta_0$ and $\beta_1$, were already estimated from the same data. Plugging
$MSE$ into the formulas above gives standard errors,
$$\mathrm{SE}_{\hat\beta_0} = \sqrt{\frac{\sum_i X_i^2}{\sum_i (X_i-\bar X)^2}\times\frac{MSE}{n}}, \qquad \mathrm{SE}_{\hat\beta_1} = \sqrt{\frac{MSE}{\sum_i(X_i-\bar X)^2}},$$
and confidence intervals and tests follow the familiar pattern,
$$T = \frac{\hat\beta_k - \beta_k}{\mathrm{SE}(\hat\beta_k)}, \qquad k=0,1.$$
If all four assumptions hold, $T$ follows a $t$-distribution with $n-2$ degrees of freedom. If
normality fails but independence, linearity and equal variance hold and the sample is large, the
central limit theorem rescues the same conclusion approximately.

**Breast cancer example.** The regression of S100A8 on ESR1 shows a negative association. A 95%
confidence interval for $\beta_1$,
$$\left[\hat\beta_1 - t_{n-2,\alpha/2}\,\mathrm{SE}_{\hat\beta_1},\ \hat\beta_1 + t_{n-2,\alpha/2}\,\mathrm{SE}_{\hat\beta_1}\right],$$
obtained in R with `confint(lm1)`, excludes zero: the negative association is significant at the 5%
level.

## The hypothesis test

The research question — is there an association between S100A8 and ESR1 expression — translates
into a statement about $\beta_1$. Under the null hypothesis of no association, $H_0: \beta_1 = 0$;
under the alternative, $H_1: \beta_1 \neq 0$. The test statistic is
$$T = \frac{\hat\beta_1 - 0}{\mathrm{SE}(\hat\beta_1)},$$
which, under $H_0$, follows a $t$-distribution with $n-2$ degrees of freedom. For the brca dataset,
`summary(lm1)` shows the association between S100A8 and ESR1 expression is extremely significant
($p \ll 0.001$). But a significant test is only as trustworthy as the assumptions it rests on — they
have to be checked before the conclusion is believed.

## Checking the assumptions

Four things need checking: independence is a property of how the data were collected (a matter of
design, not something visible in a plot), linearity, homoscedasticity, and normality.

**Linearity** is assessed with a *residual plot*: put the fitted values $\hat\beta_0+\hat\beta_1 x$
on the horizontal axis and the residuals
$$e_i = y_i - \hat g(x_i) = y_i - \hat\beta_0 - \hat\beta_1 x_i$$
on the vertical axis (`plot(lm1)` in R). A residual plot is especially important once the model has
more than one covariate, where a simple scatterplot of $Y$ against $X$ no longer shows the whole
picture directly.

**Homoscedasticity** is checked the same way: residuals and squared residuals carry information
about how variable the response is, so any association between the (squared) residuals and the
predictor or the fitted values is a sign of heteroscedasticity.

**Normality** matters least when the sample is large — the central limit theorem makes the
estimators approximately normal even when the observations themselves are not, though exactly how
large "large" needs to be depends on the shape and size of the departure from normality. The
assumption to check is that $Y_i \mid X_i \sim N(\beta_0+\beta_1 X_i, \sigma^2)$ — note that a
QQ-plot of the raw response $Y$ is misleading and useless here, because the $Y_i$ genuinely have
different distributions (they have different conditional means at different $X_i$) even when the
model is exactly right. The assumption is about the *residuals*, so the QQ-plot has to be of the
residuals $e_i$, not of $Y$ itself.

A useful calibration when reading a residual plot on a small sample: simulate several batches of
pure, independent normal noise against the same predictor and look at what *those* residual plots
look like. With only $n=32$ observations, apparently patterned scatter can appear in plots of noise
that has no structure at all, so a real diagnostic plot is only worth acting on if it shows more
than this baseline level of apparent pattern.

## When the assumptions fail: transformations

Transforming the *predictor* does not change the distribution of $Y$ given $X$ — it is not useful
for fixing homoscedasticity or non-normality — but it can fix non-linearity, when normality and
homoscedasticity already hold, typically by adding higher-order terms $X^2, X^3,\dots$,
$$Y_i = \beta_0 + \beta_1 X_i + \beta_2 X_i^2 + \cdots + \epsilon_i.$$
Transforming the *response* $Y$, by contrast, can fix both non-normality and heteroscedasticity —
common choices are $\sqrt{Y}$, $\log(Y)$, or $1/Y$.

**Breast cancer example.** The straightforward linear model has problems on several fronts:
heteroscedasticity, a right-skewed departure from normality, predictions that can theoretically go
negative even though a gene expression level cannot, and non-linearity. This combination is typical
of concentration and intensity measurements, which are often log-normally distributed — normal once
log-transformed. In gene expression this is standard practice, using a base-2 logarithm, because
then differences on the log scale are exactly fold changes on the original scale. Rather than
discarding the three outlying points as in the first pass, fitting
$$\log_2(\text{S100A8}) \sim \log_2(\text{ESR1})$$
on the *full* dataset (not the trimmed subset) handles the skew, the impossible negative
predictions, and much of the heteroscedasticity in one move — this is the promised "properly dealing
with all the data" that the outlier removal at the start of the chapter deferred.

Fitting this model (`lm2`) gives $\hat\beta_0 = 23.401$ and $\hat\beta_1 = -1.615$, so
$$\log_2\hat\mu = 23.401 - 1.615 \times \log_2(\text{ESR1}).$$
This coefficient admits three different, complementary readings.

**Interpretation 1 (log scale, direct).** A patient whose ESR1 expression is one unit higher on the
$\log_2$ scale than another's has, on average, a $\log_2$ S100A8 expression that is $1.615$ units
lower — this is just the slope read directly off the fitted line, since
$$\log_2\hat\mu_2 - \log_2\hat\mu_1 = -1.615(\log_2\text{ESR1}_2 - \log_2\text{ESR1}_1).$$

**Interpretation 2 (back-transformed, geometric mean).** A model fit on the log scale, once
back-transformed, describes *geometric* means, because
$$\frac{1}{n}\sum_{i=1}^n \log x_i = \frac{\log x_1 + \cdots + \log x_n}{n} = \frac{\log(x_1\times\cdots\times x_n)}{n} = \log\left(\sqrt[n]{\textstyle\prod_i x_i}\right).$$
The population mean $\mu$ is therefore estimated as a geometric mean, and because the logarithm is
monotone, confidence intervals can be back-transformed too. Taking $2$ to the power of the fitted
slope gives $2^{-1.615} = 0.326$ (equivalently $2^{1.615} = 3.06$): a patient whose ESR1 expression
is double another's has, on average, an S100A8 expression that is $0.326$ times as large — about a
threefold decrease.

**Interpretation 3 (percentage change).** For a small relative change in the predictor, the effect
translates into an approximate percentage change in the response. A 1% higher ESR1 expression is
associated with an S100A8 expression that is $1.01^{-1.615} = 0.984$, i.e. about $1.6\%$ lower. More
generally, for $-10 < \beta_1 < 10$,
$$1.01^{\beta_1} - 1 \approx \frac{\beta_1}{100},$$
which is why "$\beta_1$ percent" is a serviceable shorthand for moderate slopes on the log scale.

## Inference on the mean outcome vs. prediction for a new observation

The fitted line can be used to estimate the *average* response at a given predictor value, or to
*predict* the actual response of one new, as-yet-unobserved subject. These are numerically the same
quantity, $\hat g(x) = \hat\beta_0 + \hat\beta_1 x$, but their sampling distributions are different,
and conflating them understates uncertainty about a single future patient.

**The mean.** $\hat g(x)$ estimates the conditional mean $E[Y\mid X=x]$; since the parameter
estimators are unbiased and normal, so is $\hat g(x)$, with
$$\mathrm{SE}_{\hat g(x)} = \sqrt{MSE\left\{\frac{1}{n} + \frac{(x-\bar X)^2}{\sum_i(X_i-\bar X)^2}\right\}}, \qquad T = \frac{\hat g(x) - g(x)}{\mathrm{SE}_{\hat g(x)}} \sim t_{n-2}.$$
In R, `predict(model, newdata=..., interval="confidence")` returns exactly this — the mean response
and its confidence interval at chosen predictor values.

**A new observation.** For an independent new observation $Y^* = g(x) + \epsilon^*$, with
$\epsilon^* \sim N(0,\sigma^2)$ independent of the sample, the uncertainty has two sources rather
than one: uncertainty about the estimated model parameters, exactly as before, *plus* the
irreducible extra spread of any individual observation around its own mean. This gives a larger
standard error,
$$\mathrm{SE}_{\hat Y(x)} = \sqrt{\hat\sigma^2 + \hat\sigma^2_{\hat g(x)}} = \sqrt{MSE\left\{1 + \frac{1}{n} + \frac{(x-\bar X)^2}{\sum_i(X_i-\bar X)^2}\right\}}, \qquad \frac{\hat Y(x) - Y}{\mathrm{SE}_{\hat Y(x)}} \sim t_{n-2}.$$
A **prediction interval**, obtained with `predict(model, newdata=..., interval="prediction")`, is
exactly this wider interval — an improved version of a plain reference interval that additionally
accounts for the fact that the model's own parameters are estimated, not known.

**NHANES cholesterol example.** Compare a reference interval for direct cholesterol built from a
large sample of women, $\exp\!\left(\overline{\log(\text{DirectChol})} \pm z_{0.975}\, sd(\log(\text{DirectChol}))\right)$,
against the prediction interval from `predict(lmChol, interval="prediction")` on the same data. With
a large sample the two intervals are almost identical, because the model parameters are estimated
precisely enough that the extra term contributes little. Repeating the comparison on a subsample of
only 10 women changes this: the prediction interval becomes much wider than the naive reference
interval, especially at the upper limit once back-transformed, because now the uncertainty in the
mean and standard deviation is no longer negligible. In small samples, ignoring parameter
uncertainty and using a plain reference interval understates how uncertain a single new
observation really is.

## Sum of squares and the ANOVA table

Three sums of squares organise how much of the variability in $Y$ the model explains.

The **total sum of squares**,
$$SSTot = \sum_{i=1}^n (Y_i - \bar Y)^2,$$
estimates the variance of the *marginal* distribution of the response — ignoring $X$ altogether —
whereas the chapter has otherwise been about the *conditional* distribution $f(Y\mid X=x)$, whose
variance $MSE$ estimates.

The **regression sum of squares**,
$$SSR = \sum_{i=1}^n (\hat Y_i - \bar Y)^2 = \sum_{i=1}^n (\hat g(x_i) - \bar Y)^2,$$
measures how far the fitted predictions move away from the overall mean. Equivalently, it compares
the fitted model $\hat g(x) = \hat\beta_0+\hat\beta_1 x$ against the model with no predictor at all,
$g(x)=\beta_0$ — in which case $\beta_0$ would just equal $\bar Y$ — so $SSR$ measures the size of
the predictor's effect.

The **error sum of squares**,
$$SSE = \sum_{i=1}^n (Y_i - \hat Y_i)^2 = \sum_{i=1}^n \{Y_i - \hat g(x_i)\}^2,$$
is exactly the least-squares criterion from before: the smaller $SSE$, the better the fit.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="One observation's deviation from the sample mean split into the part explained by the regression line and the residual left over">
  <circle cx="70" cy="115" r="3" fill="currentColor" fill-opacity="0.3"/>
  <circle cx="100" cy="128" r="3" fill="currentColor" fill-opacity="0.3"/>
  <circle cx="130" cy="105" r="3" fill="currentColor" fill-opacity="0.3"/>
  <circle cx="190" cy="150" r="3" fill="currentColor" fill-opacity="0.3"/>
  <circle cx="220" cy="160" r="3" fill="currentColor" fill-opacity="0.3"/>
  <circle cx="250" cy="145" r="3" fill="currentColor" fill-opacity="0.3"/>
  <line x1="40" y1="150" x2="290" y2="150" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="240" y="144" font-size="11" fill="currentColor">mean $\bar Y$</text>
  <line x1="40" y1="100" x2="290" y2="172" stroke="currentColor" stroke-width="1.5"/>
  <text x="225" y="178" font-size="11" fill="currentColor">fitted line</text>
  <line x1="160" y1="90" x2="160" y2="135" stroke="currentColor" stroke-width="2"/>
  <line x1="160" y1="135" x2="160" y2="150" stroke="currentColor" stroke-width="2" stroke-dasharray="2 2"/>
  <circle cx="160" cy="90" r="4" fill="currentColor"/>
  <circle cx="160" cy="135" r="3" fill="currentColor" fill-opacity="0.6"/>
  <text x="168" y="112" font-size="12" fill="currentColor">SSE</text>
  <text x="168" y="146" font-size="12" fill="currentColor">SSR</text>
  <text x="112" y="82" font-size="12" fill="currentColor">observation</text>
</svg>
<figcaption>For one observation, the total deviation from the sample mean (bottom dashed segment up
to the solid point) splits into the part explained by the regression line — from the mean up to the
fitted value ($SSR$) — and the residual left over — from the fitted value up to the point ($SSE$).
Summing the squares of each of these three segments over all $n$ points gives $SSTot$, $SSR$ and
$SSE$.</figcaption>
</figure>

Squaring and summing the decomposition shown in the figure over every observation gives
$$SSTot = \sum_i (Y_i - \bar Y)^2 = \sum_i (Y_i - \hat Y_i + \hat Y_i - \bar Y)^2 = \sum_i(Y_i-\hat Y_i)^2 + \sum_i(\hat Y_i - \bar Y)^2 = SSE + SSR.$$
The total variability in the data is partly explained by the predictor ($SSR$) and partly left over
as residual variability that the regression model cannot account for ($SSE$).

The **coefficient of determination**,
$$R^2 = 1 - \frac{SSE}{SSTot} = \frac{SSR}{SSTot},$$
is the fraction of the total variability in the sample explained by the model. A large $R^2$ means
the model has the potential to make good predictions (small $SSE$ relative to the total spread), but
$R^2$ is not a good guide to the p-value of the test $H_0: \beta_1=0$: the p-value is driven mainly
by $SSE$ and the sample size $n$, but not by $SSTot$, while $R^2$ is driven by $SSE$ and $SSTot$ but
not by $n$. A model with a low $R^2$ can still be the right, useful way to study an association, as
long as the association is modelled correctly.

Sums of squares are also the basis of an **F-test**. Define
$$MSR = \frac{SSR}{1}, \qquad MSE = \frac{SSE}{n-2}, \qquad F = \frac{MSR}{MSE},$$
where the denominators $1$ and $n-2$ are the degrees of freedom of $SSR$ and $SSE$ respectively.
Under $H_0: \beta_1 = 0$, $F = MSR/MSE \sim F_{1,n-2}$, and the F-test is always a two-sided test of
exactly the same null hypothesis, $H_1: \beta_1 \neq 0$, that the t-test above addressed, with
p-value $p = P_0[F \geq f] = 1 - F_F(f; 1, n-2)$. These pieces are usually collected into an
**ANOVA table**:

| |Df|Sum Sq|Mean Sq|F value|Pr(>F)|
|---|---|---|---|---|---|
|Regression|degrees of freedom of $SSR$|$SSR$|$MSR$|$f$-statistic|p-value|
|Error|degrees of freedom of $SSE$|$SSE$|$MSE$| | |

produced in R with `anova(lm2)`.

## Dummy variables: regression as a two-sample comparison

Linear regression can also be used to compare the means of two groups — for instance, whether
average age differs between the brca patients with unaffected and with affected lymph nodes. Define
a **dummy variable**
$$x_i = \begin{cases} 1 & \text{affected lymph nodes} \\ 0 & \text{unaffected lymph nodes} \end{cases}$$
and the group coded $x_i=0$ is the **reference group**. The regression model is unchanged,
$Y_i = \beta_0 + \beta_1 x_i + \epsilon_i$ with $\epsilon_i$ i.i.d. $N(0,\sigma^2)$, but since $x_i$
can only take two values, the model splits into two separate statements:
$$Y_i = \beta_0 + \epsilon_i \ \ (x_i=0), \qquad Y_i = \beta_0 + \beta_1 + \epsilon_i \ \ (x_i=1),$$
so that $E[Y_i\mid x_i=0] = \beta_0 = \mu_0$ and $E[Y_i\mid x_i=1] = \beta_0+\beta_1 = \mu_1$, and
hence
$$\beta_1 = E[Y_i \mid x_i=1] - E[Y_i \mid x_i=0] = \mu_1 - \mu_0.$$
The least-squares estimators turn out to be exactly the familiar two-sample quantities: $\hat\beta_0$
is the sample mean of the reference group, $\hat\beta_1$ is the difference between the two group
means, and $MSE$ is the pooled sample variance $S_p^2$. Testing $H_0: \beta_1 = 0$ against
$H_1: \beta_1 \neq 0$ in this regression is therefore exactly the two-sample $t$-test of
$H_0: \mu_0 = \mu_1$ under equal variances — in R, `t.test(age ~ node, brca, var.equal=TRUE)` and
`summary(lm(age ~ node, brca))` give the same test.

## Association is not causation

The brca data are observational, not experimental, and that limits what can be concluded from
either regression in this chapter. Patients were not randomly assigned to have affected or
unaffected lymph nodes, so an age difference between the two groups cannot be read as age *causing*
a higher risk of node involvement — the groups may differ in other, unmeasured ways too
(**confounding**). The most that can be said is that lymph node status and age are associated.

The same caveat applies to the ESR1–S100A8 model. ESR1 expression was not experimentally
manipulated, so the negative association cannot be read as ESR1 expression causing a decrease in
S100A8 expression — only that the two are negatively associated. Establishing that one gene's
expression actually causes a change in another's typically requires an experimental intervention,
such as a knockout mutant in the lab, rather than an observational regression.

## Sources

All of this chapter comes from the GTPB PSLS20 course, theory unit 6, "Simple linear regression"
(`theory/06-linearRegression.Rmd`, CC BY 4.0), converted losslessly into the eight linked notes
files:

- `01-breast-cancer-dataset.md` — the dataset, its biological motivation, and the outlier-trimming
  step.
- `02-lineair-regression.md` — the model, $g(x)$, and the interpretation of intercept and slope.
- `03-parameter-estimation.md` — least squares, the closed-form estimators, and the first fitted
  model on the trimmed data.
- `04-statistical-inference.md` — the four assumptions, the sampling distribution of the
  estimators, standard errors, confidence intervals, and the hypothesis test.
- `05-assess-assumptions.md` — residual analysis for linearity, homoscedasticity, and normality.
- `06-invalid-assumptions.md` — transformations, the log-log model on the full data, and the three
  interpretations of a log-scale slope.
- `07-prediction-intervals.md` — confidence intervals for the mean response vs. prediction
  intervals for a new observation, and the NHANES cholesterol comparison.
- `08-sum-of-squares-and-anova-table.md` — the sum-of-squares decomposition, $R^2$, the F-test, the
  ANOVA table, dummy-variable coding, and the closing note on confounding.

No slide deck, transcript, or problem set was supplied for this lecture; the notes above are the
only source. Two figures referenced in the original slides (an image of the model's assumptions,
`RegModel3.png`, and an image about the effect of the spread of $X$ on precision, `spread.png`) were
not included in the conversion and are redrawn here from the surrounding text rather than copied.
The underlying dataset (`breastcancer.csv`) and the original study
(<https://doi.org/10.1093/jnci/djj052>) are referenced by the notes but were not supplied or used
directly — no numeric results beyond those stated in the notes are reported here.

---

[← 8. Hypothesis-Testing Case Studies](08-hypothesis-testing-case-studies.md) · [Contents](index.md) · [10. Linear Regression Case Studies →](10-linear-regression-case-studies.md)
