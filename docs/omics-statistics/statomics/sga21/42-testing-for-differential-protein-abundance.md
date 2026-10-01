---
title: "42. Testing for Differential Protein Abundance"
course: "StatOmics Sga21"
chapter: 42
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 42. Testing for Differential Protein Abundance

## What this covers

Testing thousands of proteins for differential abundance is not one statistical problem but four,
stacked on top of each other: fit a model to each protein's intensities, fit it in a way that a
few bad measurements cannot dominate, stabilise the resulting variance estimate using information
from all the other proteins, and only then decide which proteins survive being tested many
thousands of times at once. This chapter builds that stack in order, using a heart proteomics case
study (protein intensity modelled by tissue, anatomical location and patient) as the running
example. It assumes the standard linear-model toolkit — least squares, the multivariate normal
distribution of the coefficient estimator, and the $t$- and $F$-tests built from it — together
with the basic vocabulary of hypothesis testing (null hypothesis, $p$-value, Type I error).

## The linear model for a protein's intensities

For a single protein, write the (log-transformed) intensity in sample $i$ as

$$
Y_i = \beta_0 + \sum_{j=1}^{p-1} x_{ij}\beta_j + \epsilon_i, \qquad \epsilon_i \overset{\text{iid}}{\sim} N(0,\sigma^2), \quad i=1,\ldots,n,
$$

where $\mathbf x_i = (x_{i1},\ldots,x_{i,p-1})$ collects the predictors for sample $i$ — in the
running example, indicators built from `location` (left/right heart), `tissue` (atrium/ventriculum)
and `patient`. Stacking the $n$ observations gives the matrix form

$$
\mathbf Y = \mathbf X\boldsymbol\beta + \boldsymbol\epsilon,
$$

with $\mathbf Y$ the $n$-vector of responses, $\mathbf X$ the $n\times p$ design matrix whose first
column is all ones, $\boldsymbol\beta$ the $p$-vector of coefficients, and $\boldsymbol\epsilon$ the
$n$-vector of errors.

### Least squares

The least-squares estimator minimises the residual sum of squares

$$
\mathrm{RSS}(\boldsymbol\beta) = \sum_{i=1}^n \Big(y_i - \beta_0 - \sum_{j=1}^{p-1} x_{ij}\beta_j\Big)^2 = \lVert \mathbf Y - \mathbf X\boldsymbol\beta\rVert^2,
$$

so $\hat{\boldsymbol\beta} = \operatorname*{argmin}_{\boldsymbol\beta}\lVert \mathbf Y - \mathbf X\boldsymbol\beta\rVert^2$.
Setting the derivative of the RSS to zero gives the normal equations and the closed-form solution:

$$
-2\mathbf X^T(\mathbf Y - \mathbf X\boldsymbol\beta) = \mathbf 0
\;\;\Longrightarrow\;\;
\mathbf X^T\mathbf X\boldsymbol\beta = \mathbf X^T\mathbf Y
\;\;\Longrightarrow\;\;
\hat{\boldsymbol\beta} = (\mathbf X^T\mathbf X)^{-1}\mathbf X^T\mathbf Y.
$$

In the heart case study this is checked two ways at once: fitting `lm(y ~ location*tissue + patient)`
and computing `solve(t(X)%*%X) %*% t(X) %*% y` directly from the model matrix `X` returned by
`model.matrix()` — the two give the same coefficients.

### The variance of $\hat{\boldsymbol\beta}$

Because $\hat{\boldsymbol\beta}$ is a linear function of $\mathbf Y$, and $\operatorname{var}(\mathbf Y) = \mathbf I\sigma^2$
(the errors are i.i.d.), the sandwich formula collapses:

$$
\hat{\boldsymbol\Sigma}_{\hat{\boldsymbol\beta}} = \operatorname{var}\!\big[(\mathbf X^T\mathbf X)^{-1}\mathbf X^T\mathbf Y\big]
= (\mathbf X^T\mathbf X)^{-1}\mathbf X^T\big(\mathbf I\sigma^2\big)\mathbf X(\mathbf X^T\mathbf X)^{-1}
= (\mathbf X^T\mathbf X)^{-1}\sigma^2.
$$

$\sigma^2$ is unknown and is estimated by the mean squared error of the residuals,
$\hat\sigma^2 = \mathbf e^T\mathbf e/(n-p)$, giving $\hat{\boldsymbol\Sigma}_{\hat{\boldsymbol\beta}} = (\mathbf X^T\mathbf X)^{-1}\hat\sigma^2$.
This by-hand computation matches `summary(fit)$cov.unscaled * sigma(fit)^2` exactly in the heart
example.

## Contrasts: testing a linear combination of coefficients

Most questions of interest are not about a single coefficient but about a combination of them —
e.g. "is the tissue effect the same in the left and right heart region?" A **contrast** packages
this as

$$
H_0:\ \mathbf L^T\boldsymbol\beta = 0 \quad\text{vs}\quad H_1:\ \mathbf L^T\boldsymbol\beta \neq 0,
$$

with estimator $\mathbf L^T\hat{\boldsymbol\beta}$ and, since $\mathbf L$ is a fixed vector,
variance $\boldsymbol\Sigma_{\mathbf L^T\hat{\boldsymbol\beta}} = \mathbf L^T\boldsymbol\Sigma_{\hat{\boldsymbol\beta}}\mathbf L$.

The heart example builds four such contrasts from the fitted model `~ location*tissue + patient`
(coefficients `tissueV` for the tissue effect and `locationR:tissueV` for its interaction with
location):

1. $\mathbf L_1$: `tissueV = 0` — the tissue effect in the left region,
2. $\mathbf L_2$: `tissueV + locationR:tissueV = 0` — the tissue effect in the right region,
3. $\mathbf L_3$: `tissueV + 0.5·locationR:tissueV = 0` — the tissue effect averaged over both regions,
4. $\mathbf L_4$: `locationR:tissueV = 0` — the interaction itself, i.e. whether the tissue effect differs between regions.

Comparing the standard errors of these four contrasts is a clean illustration of where statistical
power comes from. Write $a$ for the left-region effect and $b$ for the right-region effect, each
estimated from disjoint sets of samples and so (approximately) independent with the same variance
$v$. Then $\mathbf L_3$ estimates the average $(a+b)/2$, with variance $v/2$ — an $\sqrt 2$ smaller
standard error than either $a$ or $b$ alone, because averaging pools information from twice as many
samples. $\mathbf L_4$ estimates the difference $b-a$, with variance $2v$ — a $\sqrt2$ *larger*
standard error than $a$ or $b$ alone, and exactly twice the standard error of $\mathbf L_3$. This
matches what the fitted model actually returns: $\mathrm{se}(\mathbf L_1)=\mathrm{se}(\mathbf L_2)$,
$\mathrm{se}(\mathbf L_3) = \mathrm{se}(\mathbf L_1)/\sqrt2$, and $\mathrm{se}(\mathbf L_4) = \sqrt2\,\mathrm{se}(\mathbf L_1) = 2\,\mathrm{se}(\mathbf L_3)$.
The general point: an interaction is a difference of two noisy quantities and is always harder to
detect than either quantity on its own, while an average pools samples and is always easier.

### $t$-tests for a single contrast

Under the model assumptions,

$$
\hat{\boldsymbol\beta} \sim \mathrm{MVN}\!\left[\boldsymbol\beta,\ (\mathbf X^T\mathbf X)^{-1}\sigma^2\right]
\quad\Longrightarrow\quad
\mathbf L^T\hat{\boldsymbol\beta} \sim \mathrm{MVN}\!\left[\mathbf L^T\boldsymbol\beta,\ \mathbf L^T(\mathbf X^T\mathbf X)^{-1}\sigma^2\,\mathbf L\right].
$$

Testing one contrast $\mathbf L_k$ at a time, with $\sigma^2$ replaced by its MSE estimate, gives

$$
T = \frac{\mathbf L_k^T\hat{\boldsymbol\beta}}{\sqrt{\mathbf L_k^T\hat{\boldsymbol\Sigma}_{\hat{\boldsymbol\beta}}\mathbf L_k}} \underset{H_0}{\sim} t_{n-p}
\qquad\text{under } H_0:\ \mathbf L_k^T\boldsymbol\beta = 0.
$$

Computed by hand from `betas` and `SigmaBeta`, this reproduces the $t$-statistics and $p$-values
that `glht` (from the `multcomp` package) reports for the same contrasts.

### The omnibus test

Several contrasts can also be tested jointly, with the vector null hypothesis $H_0: \mathbf L^T\boldsymbol\beta = \mathbf 0$
and statistic

$$
F = \frac{\hat{\boldsymbol\beta}^T\mathbf L\left(\mathbf L^T\hat{\boldsymbol\Sigma}_{\hat{\boldsymbol\beta}}\mathbf L\right)^{-1}\mathbf L^T\hat{\boldsymbol\beta}}{n_c} \underset{H_0}{\sim} F_{n_c,\,n-p},
$$

where $n_c$ is the number of contrasts, provided $\mathbf L$ has full column rank.

If $\mathbf L$ only has rank $r<n_c$ — some contrasts are linear combinations of the others — the
$n_c\times n_c$ covariance matrix of the contrasts is singular and cannot be inverted. The fix is
to replace $\mathbf L$ by $r$ orthonormal contrasts $\mathbf Q$ spanning the same space
($\mathbf Q_j^T\mathbf Q_k = \delta_{jk}$), obtained by a QR decomposition of $\mathbf L$, and test

$$
F = \frac{\hat{\boldsymbol\beta}^T\mathbf Q\left(\mathbf Q^T\hat{\boldsymbol\Sigma}_{\hat{\boldsymbol\beta}}\mathbf Q\right)^{-1}\mathbf Q^T\hat{\boldsymbol\beta}}{r} \underset{H_0}{\sim} F_{r,\,n-p}.
$$

This is exactly the situation in the heart example: the four contrasts above are all built from
just two free parameters (`tissueV` and `locationR:tissueV`), so $\mathbf L$ has rank 2 and its
$4\times4$ contrast-covariance matrix cannot be inverted. Decomposing it with `qr()` gives two
orthonormal contrasts, and testing the omnibus hypothesis with them is equivalent to testing
$H_0: \beta_{\text{tissue}} = \beta_{\text{tissue:location}} = 0$ jointly. As a check, the same
question can be asked by comparing the full model against a reduced model that drops `tissue` and
the interaction (keeping `location + patient`): the nested-model $F$-test (`anova(fit, fit0)`)
returns the same $F$-statistic and $p$-value as the by-hand computation.

## Robust regression

Ordinary least squares is a maximum-likelihood estimator only when the errors really are Gaussian,
and it is not robust: a single badly-behaved measurement can move $\hat{\boldsymbol\beta}$ a long
way. **M-estimation** replaces the squared-error loss with a general loss $\rho$, chosen to be
symmetric ($\rho(z)=\rho(-z)$), zero and minimal at $z=0$, and increasing in $|z|$:

$$
\hat{\boldsymbol\beta} = \operatorname*{argmin}_{\boldsymbol\beta} \sum_{i=1}^n \rho\!\left(y_i - \mathbf x_i^T\boldsymbol\beta\right).
$$

Differentiating, the estimator solves $\sum_i \Psi(y_i-\mathbf x_i^T\boldsymbol\beta)\,\mathbf x_i = \mathbf 0$,
where $\Psi=\rho'$. For $\hat{\boldsymbol\beta}$ to be robust, $\Psi$ must be **bounded**: it caps
how much a single, arbitrarily bad observation can pull the estimating equation. Ordinary least
squares is the special case $\rho(z)=z^2$, so $\Psi(z)=2z$ — unbounded, hence not robust — and the
estimating equation reduces to the usual normal equations, $\hat{\boldsymbol\beta}=(\mathbf X^T\mathbf X)^{-1}\mathbf X^T\mathbf y$.

Several common choices of $\rho$, its derivative $\Psi$, and the associated weight function
$w(z)=\Psi(z)/z$ (the table shown in the lecture, from Bolstad's 2004 PhD thesis):

| Name | $\rho(z)$ | $\Psi(z)$ | $w(z)$ |
| --- | --- | --- | --- |
| Huber | $z^2/2$ if $\lvert z\rvert\le k$; $k(\lvert z\rvert - k/2)$ if $\lvert z\rvert>k$ | $z$ if $\lvert z\rvert\le k$; $k\,\mathrm{sgn}(z)$ if $\lvert z\rvert>k$ | $1$ if $\lvert z\rvert\le k$; $k/\lvert z\rvert$ if $\lvert z\rvert>k$ |
| Cauchy | $\tfrac{c^2}{2}\log\!\big(1+(z/c)^2\big)$ | $\dfrac{z}{1+(z/c)^2}$ | $\dfrac{1}{1+(z/c)^2}$ |
| Tukey (biweight) | $\tfrac{c^2}{6}\big[1-(1-(z/c)^2)^3\big]$ if $\lvert z\rvert\le c$; $c^2/6$ otherwise | $z(1-(z/c)^2)^2$ if $\lvert z\rvert\le c$; $0$ otherwise | $(1-(z/c)^2)^2$ if $\lvert z\rvert\le c$; $0$ otherwise |

Huber's $\Psi$ behaves exactly like least squares for small residuals ($\Psi(z)=z$, full weight
$w=1$) but flattens out to $\pm k$ beyond the threshold $k$, so a residual's influence stops growing
once it is large enough to look like an outlier; Tukey's biweight goes further and gives residuals
past $c$ a weight of exactly zero.

### Iteratively reweighted least squares

When a scale parameter $\sigma$ must be estimated alongside $\boldsymbol\beta$, write
$u_i = (y_i-\mathbf x_i^T\boldsymbol\beta)/\sigma$; the estimating equation for $\boldsymbol\beta$
becomes $\sum_i w(u_i)\,u_i\,\mathbf x_i = 0$ with $w(u)=\Psi(u)/u$ — precisely the form solved by
**iteratively reweighted least squares (IRWLS)**: at iteration $k$, compute weights $w\big(u_i^{(k-1)}\big)$
from the *previous* residuals, then re-fit by weighted least squares,

$$
\big(\hat{\boldsymbol\beta},\hat\sigma\big)^{(k)} = \operatorname*{argmin}_{\boldsymbol\beta,\sigma} \sum_{i=1}^n w\big(u_i^{(k-1)}\big)\big(u_i^{(k)}\big)^2,
$$

and repeat until the weights stop changing. `msqrob2` fits protein-level models this way; `rlm()`
in R's `MASS` package does the same with a Huber loss by default.

### A worked example: one outlier at high leverage

The lecture simulated 20 points from $y = 10+5x+\varepsilon$, $\varepsilon\sim N(0,1)$, with $x$
evenly spaced on $[0,1]$, then corrupted the *last* point — the one at the largest $x$, i.e. the
point farthest from the average covariate value and therefore with the most leverage on the slope
— setting its $y$ far below the line. Fitting `lm()` (OLS) and `rlm()` (M-estimation) to the same
data and overlaying both fitted lines makes the effect visible directly: the OLS line is pulled
down toward the outlier, while the robust fit stays close to the other 19 points.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A high-leverage outlier pulls the ordinary least-squares line toward it, while the robust fit, having given the outlier a small weight, tracks the rest of the points.">
  <line x1="40" y1="185" x2="320" y2="185" stroke="currentColor" stroke-width="1"/>
  <circle cx="55" cy="150" r="4" fill="currentColor"/>
  <circle cx="85" cy="138" r="4" fill="currentColor"/>
  <circle cx="115" cy="122" r="4" fill="currentColor"/>
  <circle cx="145" cy="108" r="4" fill="currentColor"/>
  <circle cx="175" cy="95" r="4" fill="currentColor"/>
  <circle cx="205" cy="80" r="4" fill="currentColor"/>
  <circle cx="235" cy="65" r="4" fill="currentColor"/>
  <circle cx="270" cy="150" r="9" fill="#d9534f" fill-opacity="0.15" stroke="#d9534f" stroke-width="1"/>
  <circle cx="270" cy="150" r="3" fill="#d9534f"/>
  <line x1="45" y1="158" x2="295" y2="52" stroke="currentColor" stroke-width="1.8"/>
  <line x1="45" y1="150" x2="295" y2="103" stroke="currentColor" stroke-width="1.8" stroke-dasharray="5,4"/>
  <text x="252" y="48" font-size="12" fill="currentColor">robust fit</text>
  <text x="252" y="118" font-size="12" fill="currentColor">OLS</text>
  <text x="215" y="172" font-size="11" fill="#d9534f">outlier, small weight</text>
</svg>
<figcaption>Ordinary least squares is dragged toward the high-leverage outlier; the robust fit down-weights it and stays close to the bulk of the points.</figcaption>
</figure>

The lecture then rebuilt `rlm()`'s answer by hand, which is the clearest way to see what IRWLS is
actually doing:

```r
res <- lmMod$res                       # residuals from the current (OLS) fit
stdev <- mad(res)                      # robust scale: median(|res - median(res)|) * 1.4826
z <- res / stdev                       # standardised residuals
w <- psi.huber(z)                      # Huber weights: 1 for small |z|, shrinking for large |z|
lmMod <- lm(ysim ~ xsim, weights = w)  # re-fit, weighted
```

Repeating these four lines a handful of times (recomputing residuals, weights, and the weighted fit
each time) converges to essentially the same line that `rlm()` returns directly.

## Borrowing strength across proteins: empirical Bayes variance moderation

With only a handful of replicates per protein, the per-protein variance estimate $s_p^2$ is itself
noisy — small by chance for some proteins, large for others, regardless of the true underlying
variance. A naive fix is to stabilise the denominator of the $t$-statistic by simply adding a small
constant, $\tilde s_p = s_p + s_0$. **Empirical Bayes** theory, as implemented in the `limma`
package, turns this ad hoc trick into a principled shrinkage estimator that borrows information
across all the proteins in the experiment.

### A Bayesian intermezzo

A frequentist treats the data as random and the population parameters as fixed but unknown. A
Bayesian instead represents uncertainty about a parameter $\theta$ with a probability distribution
— a **prior**, $g(\theta)$, reflecting prior belief about plausible values — and updates it by
confronting the model with data via Bayes' theorem, producing a **posterior**:

$$
g(\theta\mid \mathbf Y) = \frac{f(\mathbf Y\mid\theta)\,g(\theta)}{\int f(\mathbf Y\mid\theta)\,g(\theta)\,d\theta}
\qquad\Big(\text{posterior} = \frac{\text{prior}\times\text{likelihood}}{\text{marginal}}\Big).
$$

### The limma hierarchical model

For protein (gene) $g$, `limma` places a prior directly on the *variance*: the precision
$1/\sigma_g^2$ is assumed to follow a scaled inverse chi-squared distribution with prior scale
$s_0^2$ and prior degrees of freedom $d_0$,

$$
\frac{1}{\sigma_g^2} \sim s_0^2\,\frac{\chi^2_{d_0}}{d_0},
$$

while the data contribute the usual sampling distribution of the per-protein variance estimate,
$s_g^2 \sim \sigma_g^2\,\chi^2_{d_g}/d_g$ (with $d_g$ the residual degrees of freedom of protein
$g$'s own regression fit). Because this prior is conjugate to that sampling distribution, the two
combine analytically. The posterior mean of the variance is a **precision-weighted average** of
the protein's own estimate and the prior:

$$
\tilde s_p^2 = \mathrm E\!\left[\sigma_p^2 \mid s_p^2\right] = \frac{d_0 s_0^2 + d_p s_p^2}{d_0+d_p},
$$

and plugging this moderated variance into the earlier $t$-statistic, with $\mathbf W$ the weights
from the robust fit,

$$
\tilde T_p = \frac{\mathbf L_k^T\hat{\boldsymbol\beta}_p}{\sqrt{\mathbf L_k^T(\mathbf X^T\mathbf W\mathbf X)^{-1}\mathbf L_k\;\tilde s_p^2}},
$$

gives a statistic that is exactly $t$-distributed on $d_0+d_p$ degrees of freedom under
$H_0:\mathbf L^T\boldsymbol\beta=0$ — *more* degrees of freedom than the plain per-protein test,
because information has genuinely been borrowed from the rest of the dataset.

This is what makes the earlier ad hoc fix ($\tilde s_p = s_p+s_0$) more than a hack: the correct
combination is not additive but a weighted average by degrees of freedom, and the payoff for doing
it properly is the extra degrees of freedom, i.e. extra statistical power.

**Empirical** Bayes, as distinct from a fully Bayesian analysis, is specifically about where $s_0$
and $d_0$ come from. A fully Bayesian analysis would fix the prior parameters from genuine external
knowledge and then work with the whole posterior. `limma` instead *estimates* $s_0$ and $d_0$ from
the data itself — using moment estimators built from the ensemble of all the proteins' own
$(s_g^2, d_g)$ pairs (`limma::squeezeVar()`) — and, rather than propagating the full posterior
distribution of $\sigma_g^2$, uses only its posterior mean (equivalently, the maximum a posteriori
point estimate).

### Checking the shrinkage

Plotting each protein's raw $\hat\sigma_p$ (`getSigma`) against its posterior $\tilde\sigma_p$
(`getSigmaPosterior`) in the heart data shows the shrinkage directly: large standard deviations
are pulled down, small ones are pulled up, all toward the estimated prior standard deviation
$\sqrt{s_0^2}$.

A simulation makes the point sharply. Take the real fitted coefficients from the heart model, but
simulate every protein with the *same* true $\sigma=1$ — i.e. by construction there is no genuine
between-protein variance heterogeneity. Refitting and comparing raw versus posterior standard
deviations shows: the raw per-protein estimates still scatter widely around 1, simply because a
single protein's own $s_p^2$ is a very noisy estimate with so few residual degrees of freedom; but
the posterior estimates are pulled tightly to 1 for essentially every protein, and the estimated
prior degrees of freedom come out enormous (effectively infinite). The empirical Bayes procedure
has correctly detected that there is no real heterogeneity to preserve, and borrows (almost)
complete strength across proteins — exactly the behaviour a correct procedure should have on data
simulated with a genuinely shared variance.

## $p$-values: null and real behaviour

The lecture checked the testing procedure by simulating data **under the null**: take the fitted
heart model, set the tissue effect in the left region to exactly zero (leaving every other
parameter, and each protein's own $\hat\sigma$, at its fitted value), simulate fresh intensities
from this null model, refit, and test the same tissue contrast. The resulting $p$-values are
(flat) uniform on $[0,1]$: under $H_0$, every $p$-value threshold is equally likely to be crossed
by chance, which is exactly the definition of a correctly calibrated test. The direct consequence:
applying a fixed cutoff such as $0.05$ to thousands of truly null proteins returns, in expectation,
5% of them as false positives — with no correction, a large absolute number of false discoveries
whenever many proteins are tested.

The $p$-value histogram from the *real* heart data is not flat. It is a **mixture**: a uniform
component from the (large majority of) genuinely non-differential proteins, plus an enrichment of
small $p$-values from the genuinely differentially abundant ones. Separating that small-$p$-value
excess from the uniform background, while controlling how many of the returned proteins are false
positives, is exactly the problem multiple-testing correction solves.

## Correction for multiple testing

### Family-wise error rate

The **family-wise error rate** is the probability of making *at least one* false positive decision
across the whole list of tests, $\mathrm{FWER} = P(\mathrm{FP}\ge1)$ — a returned list is
considered wrong as soon as it contains even one truly non-differential protein.

**Bonferroni.** Test each of $m$ hypotheses at level $\alpha/m$. By the union bound,

$$
\mathrm{FWER} \le \sum_{p=1}^m P\big(\text{reject } H_{0p}\mid H_{0p}\text{ true}\big) = m\cdot\frac{\alpha}{m} = \alpha,
$$

so Bonferroni provides strong control of the FWER for *any* dependence structure between the
tests — but at the cost of being very conservative. The adjusted $p$-value is
$\tilde p_p = \min(m\,p_p,\,1)$. Applied to the null simulation, Bonferroni (correctly) returns
zero false positives; applied to the real heart data, it returns very few significant proteins.

**Holm's step-down method.** More powerful than Bonferroni while still controlling the FWER
strongly. Order the $p$-values from smallest to largest, $p_{(1)}\le\cdots\le p_{(m)}$. Test
$p_{(1)}$ against $\alpha/m$; if it is rejected, test $p_{(2)}$ against $\alpha/(m-1)$; if that is
rejected, test $p_{(3)}$ against $\alpha/(m-2)$; and so on, testing the $k$-th smallest against
$\alpha/(m-k+1)$ — stopping the first time a test fails to reject. At each step Holm corrects only
for the hypotheses still in play, rather than for all $m$ at once, which is what buys the extra
power over Bonferroni.

The naive adjusted $p$-value is $\tilde p_{(k)} = \min\big(p_{(k)}(m-k+1),\,1\big)$, but applied
rank by rank this can break monotonicity: with two tests and $p_{(1)}=0.001$, $p_{(2)}=0.0015$, the
naive formula gives $\tilde p_{(1)}=0.002$ but $\tilde p_{(2)}=0.0015$ — the *more* significant
original $p$-value ending up with a *larger* adjusted one. The fix is a running maximum,

$$
\tilde p_{(k)} = \max_{h=1,\ldots,k}\ \min\big(p_{(h)}(m-h+1),\,1\big),
$$

which is what a by-hand implementation does explicitly: order the $p$-values, multiply each by
$(m-\text{rank}+1)$, cap at 1, then sweep through enforcing that each value is at least as large as
the one before it. On the null simulation Holm, like Bonferroni, returns no false positives; on the
real data it returns slightly more proteins than Bonferroni, but is still conservative.

### False discovery rate

The FWER controls the chance of *any* false positive at all, which is an increasingly harsh
standard as $m$ grows. The **false discovery rate (FDR)** instead controls the *expected
proportion* of false positives among the proteins actually returned:

$$
\mathrm{FDR}(p_0) = \mathrm E\!\left[\frac{\mathrm{FP}}{\mathrm{FP}+\mathrm{TP}}\right] \approx \frac{p_0\, m}{\#\{p_p\le p_0\}}
$$

— under a uniform null, $p_0\, m$ estimates how many truly null $p$-values are expected to fall
below the threshold $p_0$ by chance alone; dividing by however many proteins were actually called
significant at that threshold estimates the fraction of the returned list that is false. The
**Benjamini–Hochberg** adjusted $p$-value for protein $j$ is this quantity, capped at 1 and made
monotone in the original $p$-values:

$$
\tilde p_j = \min_{k:\, p_k\ge p_j}\ \min\!\left[\frac{p_{0,k}\, m}{\#\{p_p\le p_{0,k}\}},\,1\right].
$$

The by-hand computation orders the $p$-values ascending, rescales the $k$-th smallest by $m/k$,
caps at 1, and then enforces monotonicity by sweeping from the *largest* rank down to the smallest,
keeping a running minimum (the mirror image of Holm's running maximum, and in the opposite
direction, because BH's correction must be non-decreasing in the original $p$-value while Holm's
correction is non-increasing in significance rank).

On the null simulation, BH again returns no false positives — and it can be shown that the FDR
method controls the FWER whenever $H_0$ is true for *every* feature, which is exactly that case.
On the real heart data, BH returns a substantially longer list of differentially abundant proteins
than Bonferroni or Holm, at the price of tolerating some false positives: at $\alpha=0.05$, the
guarantee is that on average 5% of the *returned list* is expected to be false, not that the whole
experiment has only a 5% chance of any false positive at all. That relaxation — trading a
guarantee about the whole experiment for a guarantee about the proportion of the returned list — is
what makes FDR control the practical choice whenever the list itself, not just its correctness, is
the object of interest.

## Sources

All material in this chapter comes from the five converted slide files of the `technicalDetailsProteomics.Rmd`
lecture source (statOmics SGA21, licensed CC BY-NC-SA 4.0; no separate slide deck, transcript, or
problem set was supplied for this lecture — the markdown files themselves are a lossless conversion
of the R Markdown slides and are the only material available):

- `01-linear-regression.md` — the linear model, matrix notation, least squares, the variance of
  $\hat{\boldsymbol\beta}$, contrasts, the heart case-study power comparison, $t$-tests, the omnibus
  $F$-test and its rank-deficient case (QR decomposition), all worked on the heart proteomics
  dataset (`~ location*tissue + patient`).
- `02-robust-regression.md` — M-estimation, the $\Psi$-function robustness condition, IRWLS, and
  the simulated one-outlier / high-leverage worked example, including the by-hand Huber-weighted
  refit. The table of $\rho$, $\Psi$ and $w$ for Huber, Cauchy and Tukey's biweight is reproduced
  from the image `TableRobust.PNG` embedded in that slide (credited there to Bolstad's 2004 PhD
  thesis); two further images in the same slide (`RhoRobust.PNG`, and the `robustRegressionPsi.png`
  / `robustRegressionWeights.png` pair) show plots of the same families of functions and are not
  reproduced here.
- `03-empirical-bayes-moderated--test.md` — the Bayesian intermezzo, the `limma` hierarchical
  model, the posterior-mean variance and moderated $t$-statistic, the empirical-vs-fully-Bayesian
  distinction, and both the heart-data shrinkage plot and the equal-true-variance simulation check.
- `04-p-values.md` — the under-$H_0$ simulation (setting the left-region tissue effect to zero) and
  the comparison between the resulting uniform $p$-value histogram and the mixture histogram from
  the real heart data.
- `05-correction-for-multiple-testing.md` — FWER, Bonferroni, Holm's step-down method (including the
  worked two-test monotonicity example), and the false discovery rate / Benjamini–Hochberg
  correction, each illustrated on both the null simulation and the real heart data.

---

[← 41. Stage-wise Omnibus and Post-hoc Testing](41-stage-wise-omnibus-and-post-hoc-testing.md) · [Contents](index.md) · [43. Mass Spectrometry & Bioinformatics for Proteomics →](43-mass-spectrometry-bioinformatics-for-proteomics.md)
