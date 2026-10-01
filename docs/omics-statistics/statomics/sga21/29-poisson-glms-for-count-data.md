---
title: "29. Poisson GLMs for Count Data"
course: "StatOmics Sga21"
chapter: 29
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 29. Poisson GLMs for Count Data

## What this covers

This chapter answers two connected questions: why an ordinary linear model is the wrong tool for
count data such as RNA-seq read counts or hourly bike-rental tallies, and what to put in its place.
It introduces the Poisson distribution as the natural model for counts, shows why counts carry a
built-in **mean-variance relationship** that a linear model cannot represent, and then builds the
generalized linear model (GLM) machinery needed to fit, interpret, test and diagnose a Poisson
regression. It assumes the reader is comfortable with linear regression in matrix form, ordinary
least squares, and the basics of maximum likelihood (likelihood, log-likelihood, score function).

## The Poisson distribution and the mean-variance relationship

The Poisson distribution is the standard model for count data: it is popular, easy to work with,
and defined by a single parameter, its mean $\mu$. For a Poisson random variable $Y_i \sim Poi(\mu)$,

$$E(Y_i) = Var(Y_i) = \mu.$$

Mean and variance are forced to be equal. This is already the most important fact about count
data in general: whatever distribution you use for counts, the variance will be some function of
the mean, because a count cannot spread out independently of how large it typically is. This is
the **mean-variance relationship**, and it is the single feature that separates count data from
the data a linear model was built for.

The idea is intuitive before it is a formula. Imagine two bird cages, one holding $10$ birds and
the other $100$. Ask a room of people to estimate, by eye, how many birds are in each cage. It is
easy to picture someone at the $10$-bird cage guessing $5$ — off by $5$ — but hard to picture
someone at the $100$-bird cage guessing $95$, even though that is also off by $5$. The *absolute*
error people tolerate scales with the *size* of the count. A quick simulation of $Poi(10)$ and
$Poi(100)$ makes the same point on histograms: the spread of the $Poi(100)$ sample is larger in
absolute terms, but relative to its own mean it looks far tighter than the $Poi(10)$ sample.

In RNA-seq, this is not just a toy story. Technical replicates — repeated sequencing runs of
aliquots from the same sample — should have the same true underlying expression for a given gene,
so any variation across replicates is measurement noise rather than biology. [Marioni *et al.*
(2008)](https://genome.cshlp.org/content/18/9/1509) showed that for most genes, the distribution of
counts across technical replicates does follow a Poisson distribution. A small fraction of genes
(around $0.5\%$) do not: they show *extra-Poisson variation*, more spread than the Poisson model
predicts — a preview of the overdispersion discussed later in this chapter.

## Relative uncertainty: the coefficient of variation

The mean-variance relationship has a consequence that looks paradoxical at first, and it matters
directly for differential expression analysis.

Suppose we have three technical replicates of a solid tumour sample and of the surrounding healthy
tissue. Write $Y_{grt}$ for the count of gene $g$ in replicate $r \in \{1,2,3\}$ of tissue
$t \in \{0,1\}$ (healthy, tumoral), each Poisson distributed, and estimate the mean in each tissue
by the replicate average $\bar Y_{g0}$, $\bar Y_{g1}$. Do the same for a second gene $k$. Now
suppose both genes have the same fold-change between tumour and healthy tissue,
$\beta_g = \bar Y_{g1}/\bar Y_{g0} = \beta_k = \bar Y_{k1}/\bar Y_{k0} = 5$, but gene $k$ is much
more highly expressed: $\bar Y_{k1} = 100$, $\bar Y_{k0} = 20$, versus $\bar Y_{g1} = 10$,
$\bar Y_{g0} = 2$ for gene $g$. **Which fold-change would you trust more?**

Simulating this directly — drawing $3$ Poisson counts at each of the four means, many times over,
and recomputing the ratio of averages each time — shows that the estimated $\beta_k$ clusters
tightly around $5$, while the estimated $\beta_g$ is spread out much more widely, even though the
*raw* variance of gene $k$'s counts ($\mu=100$) is far larger than gene $g$'s ($\mu=10$). The
absolute noise on gene $k$ is bigger, but the ratio it produces is more trustworthy.

The resolution is that fold-change depends on *relative*, not absolute, precision. Relative
uncertainty is captured by the **coefficient of variation**,

$$CV = \frac{\sigma}{\mu},$$

the standard deviation as a fraction of the mean. Because a Poisson variable has $\sigma =
\sqrt{\mu}$,

$$CV = \frac{\sqrt{\mu}}{\mu} = \frac{1}{\sqrt{\mu}},$$

which *decreases* as $\mu$ grows. For gene $k$ ($\mu = 100$), $CV = \sqrt{100}/100 = 0.1$; for gene
$g$ ($\mu = 10$), $CV = \sqrt{10}/10 \approx 0.316$. Gene $k$'s mean is estimated with three times
less relative noise than gene $g$'s, and that lower relative uncertainty propagates through the
ratio to give a more precise fold-change estimate. This is the basic result behind why
highly-expressed genes give tighter differential-expression calls than lowly-expressed genes at
the same fold-change: it is essential for reading the results of any differential expression
analysis built on count data.

## Why a linear model will not do

A linear model for a response $Y_i$ against a covariate $X_i$ is

$$Y_i = \beta_0 + \beta_1 X_i + \epsilon_i, \qquad Y_i \mid X_i \sim N(\beta_0 + \beta_1 X_i, \sigma^2),$$

or, in matrix form with design matrix $\mathbf{X}$,

$$Y_i = \mathbf{X}_i^T\beta + \epsilon_i, \qquad Y_i \mid \mathbf{X}_i \sim N(\mathbf{X}_i^T\beta, \sigma^2\mathbf{I}).$$

The variance-covariance matrix of $\mathbf Y$ here is diagonal with the *same* $\sigma^2$
everywhere — every observation is assumed equally noisy, a property called **homoscedasticity**.
That assumption is exactly what the mean-variance relationship rules out for count data: two counts
with different means cannot have the same variance if the underlying distribution is Poisson (or
any other genuine count distribution). A linear model, in its basic form, has no way to let the
variance track the mean.

There is a second problem. Counts are non-negative, but a linear model's fitted values,
$\hat Y_i = \mathbf{X}_i^T\hat\beta$, can be any real number, $]-\infty, \infty[$. Nothing in the
model stops a fitted count from going negative.

## Generalized linear models

Generalized linear models (GLMs) extend the linear model along exactly the two axes that broke
above.

- The **conditional distribution** of $Y_i \mid X_i$ is allowed to be any member of the
  **exponential family** of distributions — which includes the Gaussian, but also the Binomial,
  Gamma and Poisson distributions.
- Instead of assuming $E(Y_i\mid X_i) = \mathbf{X}_i^T\beta$ directly, a **link function** $g(\cdot)$
  connects the conditional mean to the linear predictor:

$$g\big(E(Y_i \mid X_i)\big) = \mathbf{X}_i^T\beta.$$

Each family has a **canonical link**: the identity, $g(\mu) = \mu$, for the Gaussian (recovering
the ordinary linear model); the log link, $g(\mu) = \log\mu$, for the Poisson; and the logit link,
$g(\mu) = \log\frac{\mu}{1-\mu}$, for the Binomial.

### A Poisson GLM

A Poisson GLM is defined by

$$Y_i \sim Poi(\mu_i), \qquad \log\mu_i = \eta_i, \qquad \eta_i = \mathbf{X}_i^T\beta,$$

where $\eta_i$ is called the **linear predictor**, $\mathbf X$ is the $n \times p$ model matrix and
$\beta$ the $p \times 1$ vector of coefficients being estimated.

It is worth comparing this to the tempting alternative of just log-transforming $Y_i$ and fitting a
linear model to $\log Y_i$. The Poisson GLM models $\log E(Y_i)$; the log-linear model models
$E(\log Y_i)$. These are not the same quantity — $E(\log Y_i) \ne \log E(Y_i)$ — so only the GLM
lets you translate the fit back into a statement about the *mean* of the response after
exponentiating. The log-linear model's fit, once back-transformed, has to be read as a statement
about a geometric mean instead, which is a real cost of the shortcut.

The log link also solves the negativity problem for free: $\mathbf{X}_i^T\beta$ can be any real
number, but $\exp(\mathbf{X}_i^T\beta) \in [0, \infty[$ always, so the fitted mean is automatically
non-negative.

## Fitting a GLM: maximum likelihood

Maximum likelihood estimation chooses the parameter values that maximize the likelihood of the
observed data under the assumed model — equivalently, the point where the **score function** (the
derivative of the log-likelihood) is zero. For a non-convex likelihood this could be a merely local
maximum, but the GLM likelihood is convex, so the root found is guaranteed to be the global maximum.

### Recovering least squares from likelihood, for a linear model

As a sanity check, apply maximum likelihood to $Y_i \sim N(\mu_i, \sigma^2)$, $\mu_i =
\mathbf{X}_i\beta$. The likelihood is a product of Gaussian densities,

$$L(\mathbf Y;\beta,\sigma) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left\{-\frac{(Y_i - \mathbf{X}_i\beta)^2}{2\sigma^2}\right\},$$

with log-likelihood

$$\ell(\mathbf Y;\beta,\sigma) = \sum_{i=1}^n \left\{-\tfrac12\log(2\pi\sigma^2) - \tfrac{1}{2\sigma^2}(Y_i-\mathbf X_i\beta)^2\right\}.$$

Differentiating with respect to $\beta$ gives the score function

$$S(\beta) = \sum_{i=1}^n \frac{1}{\sigma^2}\mathbf X_i(Y_i - \mathbf X_i \beta),$$

and setting $S(\beta) = 0$ gives $\mathbf X^T\mathbf Y - \mathbf X^T\mathbf X\beta = 0$, so

$$\hat\beta = (\mathbf X^T\mathbf X)^{-1}\mathbf X^T\mathbf Y$$

— exactly the ordinary least squares estimator. Maximum likelihood and least squares agree for the
Gaussian case; this is the template the Poisson case will not quite live up to.

### Maximum likelihood for a Poisson GLM

For $Y_i \sim Poi(\mu_i)$ with $\mu_i = \exp(\mathbf X_i \beta)$, the likelihood is

$$L(Y_i;\mu) = \prod_{i=1}^n \frac{e^{-\mu}\mu^{Y_i}}{Y_i!},$$

with log-likelihood, written as a function of $\beta$ once $\mu_i = \exp(\mathbf X_i\beta)$ is
substituted in,

$$\ell(Y_i;\beta) = \sum_{i=1}^n \Big\{ -\exp(\mathbf X_i\beta) + Y_i(\mathbf X_i\beta) - \log(Y_i!)\Big\}.$$

The score function is

$$S(\beta) = -\mathbf X^T\exp(\mathbf X\beta) + \mathbf X^T \mathbf Y.$$

Setting this to zero gives

$$\mathbf X^T\mathbf Y = \mathbf X^T\exp(\mathbf X\beta),$$

or, written out coordinate by coordinate, $\sum_i\sum_p x_{ip}\exp(x_{ip}\beta_p) = \sum_i\sum_p
x_{ip}Y_i$. This is **non-linear in $\beta$**: there is no closed-form solution analogous to the
normal equations. Fitting a GLM is genuinely harder than fitting a linear model for exactly this
reason.

### Solving the score equation: iteratively reweighted least squares

The standard fitting algorithm is **iteratively reweighted least squares (IRLS)**. It is a form of
Newton–Raphson root-finding applied to the score function: at the current estimate $\beta^{(k)}$,
take the tangent line to $S(\beta)$ (using the second derivative of the log-likelihood, i.e. the
first derivative of the score), and move to wherever that tangent line crosses zero to get
$\beta^{(k+1)}$. Repeating this reweights each observation, at every iteration, according to its
currently-estimated variance under the assumed mean-variance relationship — observations with high
estimated variance are down-weighted, and vice versa — until $\beta$ stops moving.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Newton-Raphson step in fitting a GLM: the tangent to the score function at the current estimate crosses zero at the next estimate">
  <defs>
    <marker id="arrow29" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="30" y1="200" x2="30" y2="20" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow29)"/>
  <line x1="30" y1="200" x2="310" y2="200" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow29)"/>
  <text x="10" y="30" font-size="12" fill="currentColor">S(&#946;)</text>
  <text x="298" y="214" font-size="12" fill="currentColor">&#946;</text>
  <line x1="30" y1="140" x2="310" y2="140" stroke="currentColor" stroke-width="0.8" stroke-dasharray="3,3"/>
  <text x="34" y="134" font-size="11" fill="currentColor">S(&#946;) = 0</text>
  <path d="M95,55 Q115,70 140,95 Q160,115 180,140 Q200,158 220,176 Q250,190 280,205" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <circle cx="220" cy="176" r="3.2" fill="currentColor"/>
  <line x1="220" y1="176" x2="220" y2="200" stroke="currentColor" stroke-width="0.8" stroke-dasharray="2,2"/>
  <text x="220" y="214" text-anchor="middle" font-size="11" fill="currentColor">&#946; = 2.25</text>
  <line x1="100" y1="113" x2="245" y2="189" stroke="currentColor" stroke-width="1.1" stroke-dasharray="5,3"/>
  <circle cx="152" cy="140" r="3.2" fill="currentColor"/>
  <line x1="152" y1="140" x2="152" y2="200" stroke="currentColor" stroke-width="0.8" stroke-dasharray="2,2"/>
  <text x="152" y="214" text-anchor="middle" font-size="11" fill="currentColor">&#946; = 1.4</text>
  <text x="150" y="118" font-size="11" fill="currentColor">tangent at current &#946;</text>
</svg>
<figcaption>One Newton-Raphson step in fitting a Poisson GLM by iteratively reweighted least
squares: from a current estimate &#946; = 2.25, the tangent to the score function crosses zero at
&#946; = 1.4, the next estimate. The curve's own root (where it actually crosses zero) still lies
elsewhere, which is why this is repeated until the estimate stops moving.</figcaption>
</figure>

## A worked example: bike-sharing counts

To get hands-on with a Poisson GLM, the lecture used the `Bikeshare` dataset (`ISLR2` package),
which records how many bikes were in use, `bikers`, in every hour of a full year, together with
`hum` (normalized humidity, continuous, $0$ to $1$), `hr` (hour of day, $0$–$23$, treated as
categorical because its effect is not remotely linear) and `weathersit` (a four-level ordered
category from clear to severe weather/snow).

Exploring the data first showed three things: more bikes are used in better weather; ridership is a
non-linear function of humidity, low at both extremes and highest around moderate humidity
(plausibly reflecting very hot and very wet days at the two ends); and ridership has a clear
non-linear pattern across the hours of the day, with peaks at the typical commuting hours (roughly
6–8h and 17–19h). (A caveat noted at the time: there are likely interactions between these
variables — better weather probably encourages more commuting by bike — which this particular
model does not attempt to capture.)

The fitted model regressed `bikers` on `weathersit`, a *centered* humidity variable `humc = hum -
mean(hum)` together with its square and cube (to capture the non-linear, non-monotonic humidity
effect while avoiding multicollinearity between the linear, quadratic and cubic terms), and `hr` as
a categorical variable — using `family = "poisson"`, which defaults to the canonical log link.

### Reading off the coefficients

Because of the log link, coefficients in a Poisson GLM are **multiplicative**, not additive, on the
scale of the mean response. That single fact governs every interpretation below.

*The intercept.* The reference level is hour $0$, clear weather (`weathersit` level $1$), average
humidity (`humc` $=0$). Since $\log\mu_i = \beta_0$ at that reference point, $\mu_i =
\exp(\beta_0)$: the estimated intercept exponentiates to the model's predicted average number of
bikes in use under those reference conditions.

*The weather effect.* Let $\beta_1$ be the coefficient for `weathersit = cloudy/misty`. Holding
everything else fixed, the linear predictors at the two weather levels differ by exactly $\beta_1$,
so $\beta_1 = \log\mu_{w2} - \log\mu_{w1} = \log(\mu_{w2}/\mu_{w1})$, and $\exp(\beta_1) =
\mu_{w2}/\mu_{w1}$. Here $\exp(\hat\beta_1) = 0.85$: all else equal, average ridership in cloudy/misty
weather is $85\%$ of ridership in clear weather. A handy rule of thumb for reading these numbers
off in your head: $\exp(1) \approx 2.72 \approx 3$, so a difference of $1$ ($-1$) on the linear
predictor scale corresponds to roughly tripling (or a third) of the average response.

*The humidity effect.* With linear, quadratic and cubic terms in `humc`, the three coefficients
must be read together, and the rate of change is not constant across the humidity range — no single
number summarizes "the" humidity effect. As one concrete slice: comparing humidity $0.2$ above
average to average humidity gives

$$\log\frac{\hat\mu_{0.2}}{\hat\mu_0} = \hat\beta_4(0.2) + \hat\beta_5(0.2)^2 + \hat\beta_6(0.2)^3 = 0.0918(0.2) - 2.234(0.04) - 1.823(0.008) \approx -0.0856,$$

so $\hat\mu_{0.2}/\hat\mu_0 \approx 0.92$: at humidity $0.2$ above average, predicted ridership is
about $92\%$ of ridership at average humidity, all else equal. The full curve — obtained by
predicting on the response scale (`type = "response"`, as opposed to the default linear-predictor
scale) across a grid of humidity values — peaks around average humidity and falls off at both
extremes, matching the exploratory plot.

### Building a contrast

Suppose the question is: are there more bikers at (A) maximum humidity ($0.357$ above average),
hour $17$, in `light rain/snow` weather, than at (B) average humidity, hour $8$, in `clear`
weather? This is a **contrast** — a linear combination of the fitted coefficients.

By hand, using the fitted coefficients $\hat\beta_0=3.894$, $\hat\beta_{rainSnow}=-0.556$,
$\hat\beta_{humc}=0.092$, $\hat\beta_{humc^2}=-2.234$, $\hat\beta_{humc^3}=-1.823$,
$\hat\beta_{hr17}=2.140$, $\hat\beta_{hr8}=1.830$:

$$\log\hat\mu_A = 3.894 - 0.556 + 0.092(0.357) - 2.234(0.357)^2 - 1.823(0.357)^3 + 2.140 = 5.143,$$
$$\log\hat\mu_B = 3.894 + 1.830 = 5.724,$$
$$\frac{\hat\mu_A}{\hat\mu_B} = \exp(5.143 - 5.724) = \exp(-0.581) \approx 0.559.$$

So predicted ridership under scenario A is about $56\%$ of ridership under scenario B — despite the
hour-$17$ coefficient on its own being *larger* than the hour-$8$ coefficient ($2.140 > 1.830$,
meaning the evening commute is intrinsically busier than the morning one); the combination of worse
weather and near-maximum humidity in scenario A more than cancels that out.

The same number can be obtained two other ways that generalize better than hand algebra: (i)
writing the contrast as a row vector $\mathbf C$ (with a $1$ in the `light rain/snow` position, the
appropriate humidity powers, a $+1$ at `hr17` and a $-1$ at `hr8`, everything else $0$) and
computing $\exp(\mathbf C\hat\beta)$ directly; or (ii) constructing two data frames representing
scenarios A and B and calling `predict(..., type = "response")` on each, then taking the ratio.
All three routes — hand calculation, an explicit contrast matrix, and `predict` — must agree, and
checking that they do is a good way to be sure a contrast has been set up correctly.

## Testing hypotheses about GLM coefficients

Interpreting a coefficient is not the same as knowing whether it is statistically different from
zero. Two tests do that job for GLMs, and in genomics they are the standard machinery for testing
differential expression — asking, for each gene, whether a (combination of) coefficient(s) equals
zero.

### The Wald test

The Wald test is the GLM analogue of the $t$-test in a linear model. It relies on the asymptotic
result $\hat\beta \mid \beta \sim N(\beta, Var(\hat\beta))$. For a single coefficient,

$$W = \frac{\hat\beta}{\widehat{SE}(\hat\beta)} \sim N(0,1) \ \big|\ H_0,$$

and more generally, for a $1\times p$ contrast $\mathbf C$ and estimated variance-covariance matrix
$\hat\Sigma_{\hat\beta}$,

$$W = (\mathbf C\hat\beta)^T\big(\mathbf C\hat\Sigma_{\hat\beta}\mathbf C^T\big)^{-1}(\mathbf C\hat\beta) \sim \chi^2_1 \ \big|\ H_0: \mathbf C\beta = 0.$$

Testing $c \ge 1$ contrasts simultaneously gives $W \sim \chi^2_c$ under $H_0$, provided the $c$
contrasts are linearly independent (the contrast matrix is full rank — see below for what happens
when it is not).

### The likelihood ratio test

The likelihood ratio test (LRT) compares the log-likelihood of a full model to that of a reduced
model **nested** inside it (the reduced model must be obtainable by dropping parameters from the
full one). Adding covariates always improves the fit somewhat; the LRT asks whether the improvement
is more than chance. The test statistic is

$$L = 2\Big\{\ell(\hat\beta_{full}) - \ell(\hat\beta_{reduced})\Big\} \sim \chi^2_c \ \big|\ H_0,$$

with $c$ the number of parameters dropped going from the full model to the reduced one, and the
same null hypothesis $H_0: \mathbf C\beta = 0$ as the Wald test. As a concrete case: to test
whether ridership differs between working days and weekends, fit `bikers ~ workingday` (full model)
against `bikers ~ 1` (reduced model), both Poisson; the LRT statistic $L$ and the Wald statistic
$W^2$ need not be numerically identical (they are two different asymptotic approximations to the
same test), but both test the same null hypothesis and both are provided directly by standard GLM
software (the Wald test in a model summary; the LRT via an analysis-of-deviance comparison of the
two fitted models).

### A caveat about contrasts, and about the asymptotics

If a contrast matrix contains linearly dependent rows — for instance, testing the intercept, testing
`workingday`, and testing their sum, all in the same matrix — the implied variance-covariance matrix
$\mathbf C\hat\Sigma_{\hat\beta}\mathbf C^T$ is singular and cannot be inverted, so the joint Wald
test breaks down. The fix is to extract a linearly independent subset of the rows first (in
practice, via a QR decomposition of $\mathbf C^T$, keeping the pivoted columns up to the matrix's
rank) and test that reduced contrast instead.

More fundamentally, both tests are **asymptotic in the sample size $n$**: they need enough data
points, and correct distributional and independence assumptions, before the stated null
distributions are trustworthy. Bulk RNA-seq experiments often have very few samples, so asymptotic
theory should not be expected to hold exactly. In single-cell RNA-seq, several preprocessing steps
typically precede $p$-value calculation for every gene, which amounts to using the same data more
than once. The pragmatic stance is to treat GLM $p$-values in genomics as **useful numerical
rankings** for prioritizing genes for further inspection, rather than as exact probabilistic
statements.

## Deviance, residuals and goodness of fit

Ordinary residuals $e_i = y_i - \hat\mu_i$, useful in linear models for checking linearity and
homoscedasticity, are no longer appropriate for a GLM: because $Var(\epsilon_i)$ depends on
$\mu_i$, a residual of the same absolute size means something different depending on where the
fitted mean sits.

Instead, GLM diagnostics are built from the log-likelihood itself. For the Poisson GLM,

$$\ell(\mathbf Y;\beta) = \sum_{i=1}^n \Big\{ Y_i(\mathbf X_i^T\beta) - \exp(\mathbf X_i^T\beta) - \log Y_i!\Big\}.$$

The **residual deviance** $D$ is twice the gap in log-likelihood between the current model and the
**saturated model** — the (uninformative but perfectly-fitting) model with one parameter per data
point, so that $\hat\mu_i = y_i$ exactly:

$$D = 2\Big\{ \ell(\mathbf Y;\beta \mid \hat\mu_i = y_i) - \ell(\mathbf Y;\beta \mid \hat\mu_i = \exp(\mathbf X_i^T\beta))\Big\}.$$

This is, by construction, a likelihood ratio test statistic — a low deviance means the current
model's log-likelihood is close to the best any model could do on this data, i.e. a good fit. The
corresponding **deviance residual** for observation $i$ is

$$D_i = \text{sign}(Y_i - \hat\mu_i)\sqrt{2\Big\{\ell(Y_i;\beta\mid\hat\mu_i=y_i) - \ell(Y_i;\beta\mid\hat\mu_i=\exp(\mathbf X_i^T\beta))\Big\}}.$$

A second kind of residual, the **Pearson residual**,

$$e_i = \frac{y_i - E(y_i)}{\sqrt{Var(y_i)}},$$

has the familiar shape of an ordinary residual but is normalized by the (mean-dependent) standard
deviation, correcting exactly for the mean-variance relationship.

For **goodness of fit**, the residual deviance directly tests $H_0$: the current model fits about
as well as the saturated model, against $H_1$: it fits significantly worse. A second discrepancy
measure, the generalized Pearson $\chi^2$ statistic,

$$X^2 = \sum_{i=1}^n \frac{(y_i-\hat\mu_i)^2}{Var(y_i)} = \sum_{i=1}^n e_i^2,$$

targets the same question. Asymptotic theory gives $D \sim \chi^2_{n-p}$ and $X^2 \sim
\chi^2_{n-p}$ under $H_0$, with $n$ observations and $p$ fitted parameters.

## Overdispersion

Everything above assumed the Poisson mean-variance relationship, $Var = E$, actually holds. It
often does not: when the variance exceeds the mean, this is **overdispersion** (the reverse,
underdispersion, is much rarer).

Overdispersion can be measured directly from Pearson residuals. If the Poisson GLM is correctly
specified, $Var(Y_i \mid X,\hat\beta) = \hat\mu_i$, so $Var(Y_i - \hat\mu_i) = \hat\mu_i$ too
(variance is unaffected by shifting), and dividing through by $\sqrt{\hat\mu_i}$,

$$Var\!\left(\frac{Y_i - \hat\mu_i}{\sqrt{\hat\mu_i}}\right) = \frac{\hat\mu_i}{\hat\mu_i} = 1.$$

The quantity being varied here is exactly the Pearson residual $E_i$, so under a correctly
specified Poisson model $Var(E_i) = 1$ — a testable prediction. If the empirical variance of the
Pearson residuals is much larger than $1$ (as a rough rule of thumb, above roughly $1.3$, though
this threshold is arbitrary and context-dependent), that is evidence of overdispersion. In the
`Bikeshare` example, this diagnostic comes out enormous — the lecturer's own comment on the
computed value was simply "HUGE!" — which means the standard errors and $p$-values reported by the
naive Poisson fit cannot be trusted.

### Remedies: negative binomial and quasi-Poisson

Two distributions are commonly used to accommodate overdispersion, and choosing between them is
not always straightforward.

The **negative binomial (NB)** distribution belongs to the exponential family and so fits into
standard GLM machinery. If $Y_i \sim NB(\mu_i,\phi)$, then

$$E(Y_i) = \mu_i, \qquad Var(Y_i) = \mu_i + \phi\mu_i^2, \qquad \phi \ge 0.$$

Because $\phi \ge 0$, the NB variance is always at least the Poisson variance, and it is now a
*quadratic* function of the mean rather than linear; at $\phi = 0$ the NB reduces exactly to the
Poisson. Refitting the `Bikeshare` model as a negative binomial removes the overdispersion problem
entirely (the mean squared Pearson residual returns to about $1$).

The **quasi-Poisson** model, from the quasi-likelihood framework of [Wedderburn
(1974)](https://www.jstor.org/stable/2334725), specifies only the first two moments — mean and
variance — leaving higher moments unspecified: $E(Y_i) = \mu_i$, $Var(Y_i) = \phi\mu_i$, with
dispersion parameter $\phi \ge 0$. The variance is again at least the Poisson variance, but the
mean-variance relationship stays *linear* rather than becoming quadratic as in the NB. Fitting a
quasi-Poisson model estimates $\phi$ as exactly the same overdispersion diagnostic computed above
from the Pearson residuals — that is precisely how its dispersion parameter is defined.

[ver Hoef *et al.* (2007)](https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1141&context=usdeptcommercepub)
give a practical diagnostic for choosing empirically between a quasi-Poisson and a negative
binomial fit for a given dataset.

A final word on scope: this chapter covers estimation, interpretation, inference and some
goodness-of-fit diagnostics for Poisson GLMs, but not model selection, nor how to decide in the
first place whether a GLM is the right tool for a given dataset — both real questions the lecture
flagged as out of scope for the time available.

## Exercises

1. Using the fitted `Bikeshare` Poisson GLM (`bikers ~ weathersit + humc + humc^2 + humc^3 + hr`),
   derive the change in average number of bikers between (a) humidity $0.1$ above average, clear
   weather, hour $10$, and (b) humidity $0.1$ below average, cloudy/misty weather, hour $20$. Do
   this three ways: by hand from the fitted coefficients, via an explicit contrast matrix and
   $\exp(\mathbf C\hat\beta)$, and via `predict(..., type = "response")` on two constructed data
   frames — and check that all three agree.

2. For the same fitted model: verify the residual deviance reported in its summary by recomputing
   it directly from the log-likelihoods of the current and saturated models. Recover the deviance
   residuals and the Pearson residuals from first principles, and check them against the model's
   built-in residual extraction. Does this model fit significantly worse than the saturated model?

## Sources

- [`01-the-poisson-distribution.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd)
  — the Poisson distribution and mean-variance relationship, the bird-cage intuition, the Marioni
  *et al.* (2008) RNA-seq result, and the tumour/healthy relative-uncertainty (coefficient of
  variation) example, including its simulation.
- [`02-modeling-count-data-generalized-linear-models.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd)
  — why linear models fail for counts; the GLM framework and the Poisson GLM; maximum likelihood
  and IRLS; the `Bikeshare` worked example (data, fit, coefficient interpretation, contrasts); the
  Wald and likelihood ratio tests; deviance, residuals and goodness of fit; overdispersion and its
  remedies.
- Both files are the same converted `sequencing_countData.Rmd` from the statOmics SGA21 course
  (CC BY-NC-SA 4.0), split into two parts.
- The source material referred to, but this chapter does not reproduce, three embedded figures
  (a Marioni *et al.* replicate-count figure, a schematic of the Newton–Raphson/IRLS update, and a
  figure contrasting the Wald and likelihood ratio tests) and a closing xkcd comic; the
  Newton–Raphson figure above is redrawn from the numeric description given in the text (initial
  estimate $\beta=2.25$, updated estimate $\beta=1.4$), not from the original image.
- Also referenced: [Marioni *et al.* (2008)](https://genome.cshlp.org/content/18/9/1509);
  [Wedderburn (1974)](https://www.jstor.org/stable/2334725); [ver Hoef *et al.*
  (2007)](https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1141&context=usdeptcommercepub);
  the `Bikeshare` dataset documentation at the [UCI bike-sharing
  dataset](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset) page; and the count-data
  chapter of *Modern Statistics for Modern Biology* by Wolfgang Huber and Susan Holmes
  (https://www.huber.embl.de/msmb/Chap-CountData.html) — named in the lecture as further reading,
  not reproduced here.

---

[← 28. Gene-level quantification](28-gene-level-quantification.md) · [Contents](index.md) · [30. Bulk RNA-seq DE Homework →](30-bulk-rna-seq-de-homework.md)
