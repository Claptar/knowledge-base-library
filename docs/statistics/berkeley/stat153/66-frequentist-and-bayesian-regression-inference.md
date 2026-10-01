---
title: "66. Frequentist and Bayesian Regression Inference"
course: "Berkeley Stat 153"
chapter: 66
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 66. Frequentist and Bayesian Regression Inference

## What this covers

Given data $(y_i, x_{i1},\dots,x_{im})$, $i=1,\dots,n$, that plausibly follow a linear model, how do we
estimate the coefficients and say how much we trust the estimate? This chapter answers that question
two ways on the same model: the frequentist route (least squares, maximum likelihood, and the sampling
distribution of the estimator) and the Bayesian route (a deliberately noncommittal "flat" prior, updated
by the same likelihood) — and shows that, under a flat prior, the two routes land on the same point
estimate and a closely related spread. It assumes the reader already has ordinary least squares for
simple regression, basic matrix algebra, and the multivariate normal, chi-squared, and $t$-distributions.

## The regression model, in vector and matrix form

$$y=\begin{pmatrix}y_1\\ \vdots \\ y_n\end{pmatrix} \in \mathbb{R}^n,\qquad
X=\begin{pmatrix}1 & x_{11}&\cdots&x_{1m}\\ \vdots& \vdots & &\vdots \\ 1 & x_{n1}&\cdots & x_{nm}\end{pmatrix}\in\mathbb{R}^{n\times(m+1)},\qquad
\beta=\begin{pmatrix}\beta_0\\ \vdots\\ \beta_m\end{pmatrix},$$

with model $y=X\beta+\varepsilon$, $\varepsilon\sim N(0,\sigma^2 I_n)$ — equivalently $y_i$ independent with
$y_i\sim N(\beta_0+\beta_1x_{i1}+\cdots+\beta_mx_{im},\sigma^2)$. This is what `sm.OLS(y, X).fit()` fits.

The columns of $X$ need not be separate measured quantities. Two constructions turn a single time series
$y_1,\dots,y_n$ into a regression problem:

- **Functions of time.** Take $x_{i1}=i$, $x_{i2}=i^2$ to fit a quadratic trend $y_t=\beta_0+\beta_1t+\beta_2t^2+\varepsilon_t$,
  or $x_{i3}=\cos(2\pi i/12)$ (and a matching sine term) to fit a period-12 seasonal cycle.
- **Autoregression.** Take the series' own lagged values as covariates: $x_{i1}=y_{i-1}$, $x_{i2}=y_{i-2}$,
  and so on. With two lags ($m=2$) the regression only makes sense for $i=3,\dots,n$: the response vector
  is $(y_3,\dots,y_n)$ and the design matrix's rows are $(1,y_{i-1},y_{i-2})$, so the first two observations
  are used up just building the earliest row of $X$.

Both are still exactly "$y=X\beta+\varepsilon$"; only the meaning of the columns of $X$ changes, so every
result below applies to either construction unchanged.

## Least squares in matrix form

Write $S(\beta)=\sum_{i=1}^n\big(y_i-\beta_0-\beta_1x_{i1}-\cdots-\beta_mx_{im}\big)^2=\|y-X\beta\|^2$.
Expanding the square,

$$S(\beta) = (y-X\beta)^T(y-X\beta) = y^Ty - 2\beta^TX^Ty+\beta^TX^TX\beta.$$

Differentiating — using $\nabla_\beta(\beta^Ta)=a$ for a constant vector $a$, and $\nabla_\beta(\beta^TA\beta)=2A\beta$
for symmetric $A$ — and setting the gradient to zero gives the **normal equations**:

$$\nabla S(\beta) = -2X^Ty+2X^TX\beta = 0 \quad\Longrightarrow\quad X^TX\beta=X^Ty \quad\Longrightarrow\quad \hat\beta = (X^TX)^{-1}X^Ty.$$

For a single covariate this is exactly the familiar pair $\hat\beta_1=\dfrac{\sum(y_i-\bar y)(x_i-\bar x)}{\sum(x_i-\bar x)^2}$,
$\hat\beta_0=\bar y-\hat\beta_1\bar x$ — the matrix formula is the same least-squares estimator, just
written so it works for any number of covariates.

One more identity does the work in both derivations below. Write $S(\beta)=\|(y-X\hat\beta)+(X\hat\beta-X\beta)\|^2$
and expand:

$$S(\beta) = \underbrace{(y-X\hat\beta)^T(y-X\hat\beta)}_{S(\hat\beta)} + (\hat\beta-\beta)^TX^TX(\hat\beta-\beta) + 2(y-X\hat\beta)^TX(\hat\beta-\beta).$$

The cross term vanishes because $\hat\beta$ satisfies the normal equations (Exercise 1), leaving

$$S(\beta) = S(\hat\beta) + (\beta-\hat\beta)^TX^TX(\beta-\hat\beta),$$

where $S(\hat\beta)=\sum_i\big(y_i-\hat\beta_0-\cdots-\hat\beta_mx_{im}\big)^2$ is the **residual sum of
squares**. Since the second term is a nonnegative quadratic form, $S(\beta)\ge S(\hat\beta)$ everywhere,
with equality exactly at $\beta=\hat\beta$ — the decomposition is a Pythagorean statement about how far
any $\beta$ is from the least-squares point.

## Frequentist inference

### Maximum likelihood recovers least squares

Under $\varepsilon_i\overset{iid}\sim N(0,\sigma^2)$ the likelihood is

$$L(\beta,\sigma)=\prod_{i=1}^n\frac{1}{\sqrt{2\pi}\sigma}\exp\left[-\frac{(y_i-\beta_0-\cdots-\beta_mx_{im})^2}{2\sigma^2}\right] = (2\pi)^{-n/2}\sigma^{-n}\exp\left[-\frac{S(\beta)}{2\sigma^2}\right],$$

with log-likelihood $\ell(\beta,\sigma)=-\frac n2\log2\pi - n\log\sigma - \dfrac{S(\beta)}{2\sigma^2}$.
For any fixed $\sigma$, $\ell$ is a decreasing function of $S(\beta)$, so maximizing over $\beta$ is exactly
the problem of minimizing $S(\beta)$, regardless of $\sigma$: $\hat\beta_{MLE}=\hat\beta_{LS}=(X^TX)^{-1}X^Ty$.
Differentiating $\ell$ with respect to $\sigma$, $-n/\sigma+S(\beta)/\sigma^3=0$, gives $\hat\sigma^2_{MLE}=S(\hat\beta)/n$.

### The sampling distribution of $\hat\beta$ and $\hat\sigma^2$

Two facts about the multivariate normal are used repeatedly: (a) its density is
$\frac{1}{(\sqrt{2\pi})^p\sqrt{\det\Sigma}}\exp\!\left(-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu)\right)$; (b) an
affine transform of a multivariate normal vector is normal, $Z\sim N(\mu,\Sigma)\Rightarrow AZ\sim N(A\mu,A\Sigma A^T)$.

The whole response vector is normal, $y\sim N(X\beta,\sigma^2I_n)$, and $\hat\beta=Ay$ with $A=(X^TX)^{-1}X^T$
a fixed matrix (given $X$), so (b) applies directly. The mean transforms to $AX\beta=(X^TX)^{-1}X^TX\beta=\beta$
(so $\hat\beta$ is unbiased for $\beta$) and the covariance to $\sigma^2AA^T=\sigma^2(X^TX)^{-1}$:

$$\hat\beta \sim N\big(\beta,\ \sigma^2(X^TX)^{-1}\big).$$

For $\hat\sigma^2_{MLE}=S(\hat\beta)/n$, the notes state $\hat\sigma^2_{MLE}\sim \dfrac{\sigma^2}{n}\chi^2_{n-m-1}$
directly, without spelling out the argument. Since $E\big[\hat\sigma^2_{MLE}\big]=\dfrac{\sigma^2}{n}(n-m-1)\ne\sigma^2$,
the MLE of $\sigma^2$ is biased downward. Rescaling gives the unbiased estimator

$$\hat\sigma^2_{unbiased} = \frac{S(\hat\beta)}{n-m-1} = \frac{n}{n-m-1}\,\hat\sigma^2_{MLE}.$$

### Confidence intervals

Each coordinate of $\hat\beta$ is marginally normal, $\hat\beta_j\sim N\big(\beta_j,\ \sigma^2\big((X^TX)^{-1}\big)_{j+1,j+1}\big)$.
If $\sigma$ were known this would give $\hat\beta_j\pm z_{\alpha/2}\,\sigma\sqrt{(X^TX)^{-1}_{j+1,j+1}}$. Since
$\sigma$ must itself be estimated, replacing it with $\hat\sigma_{unbiased}$ adds extra uncertainty, which is
exactly what swapping the normal quantile for a $t$ quantile accounts for:

$$\hat\beta_j \pm t_{n-m-1,\,\alpha/2}\;\hat\sigma_{unbiased}\sqrt{\big((X^TX)^{-1}\big)_{j+1,j+1}},$$

with $n-m-1$ degrees of freedom — what is left of the $n$ observations after $m+1$ coefficients have been
fit.

## Bayesian inference with a flat prior

### Setting up the posterior for simple linear regression

The argument is easiest to see first with a single covariate, $y_i=\beta_0+\beta_1x_i+\varepsilon_i$. The
prior is made deliberately as noncommittal as possible:

$$\beta_0,\beta_1,\log\sigma \overset{iid}\sim \mathrm{Unif}(-C,C), \qquad \text{think of } C\to\infty.$$

Flat priors on $\beta_0$ and $\beta_1$ say every value is equally plausible in advance; flat on $\log\sigma$
rather than on $\sigma$ itself says every *order of magnitude* of the noise is equally plausible. Changing
variables from $\log\sigma$ to $\sigma$ turns the flat density on $(-C,C)$ into a $1/\sigma$ density on
$(e^{-C},e^C)$, so the joint prior is

$$f(\beta_0,\beta_1,\sigma) = \frac{I\{-C<\beta_0<C\}}{2C}\cdot\frac{I\{-C<\beta_1<C\}}{2C}\cdot\frac{I\{e^{-C}<\sigma<e^C\}}{2C\sigma} \;\propto\; \frac{I\{-C<\beta_0,\beta_1,\log\sigma<C\}}{\sigma}.$$

Multiplying by the likelihood $\propto \sigma^{-n}\exp[-S(\beta_0,\beta_1)/2\sigma^2]$ gives the joint
posterior

$$f_{\beta_0,\beta_1,\sigma\mid\text{data}}(\beta_0,\beta_1,\sigma)\;\propto\; I\{-C<\beta_0,\beta_1,\log\sigma<C\}\;\sigma^{-(n+1)}\exp\left[-\frac{S(\beta_0,\beta_1)}{2\sigma^2}\right].$$

### Integrating out $\sigma$

$\beta_0,\beta_1$ are the parameters of interest here; $\sigma$ is a nuisance parameter, and the law of
total probability says its marginal posterior comes from integrating $\sigma$ out:

$$f_{\beta_0,\beta_1\mid\text{data}}(\beta_0,\beta_1) = \int_{-\infty}^\infty f_{\beta_0,\beta_1,\sigma\mid\text{data}}(\beta_0,\beta_1,\sigma)\,d\sigma \;\propto\; I\{-C<\beta_0,\beta_1<C\}\int_{e^{-C}}^{e^C} \sigma^{-(n+1)}\exp\left[-\frac{S(\beta_0,\beta_1)}{2\sigma^2}\right]d\sigma.$$

Letting $C\to\infty$ and substituting $s=\sigma/\sqrt{S(\beta_0,\beta_1)}$ (so $d\sigma=\sqrt{S}\,ds$):

$$\int_0^\infty \sigma^{-(n+1)}e^{-S/2\sigma^2}\,d\sigma = S(\beta_0,\beta_1)^{-n/2}\int_0^\infty s^{-(n+1)}e^{-1/2s^2}\,ds,$$

and the remaining integral no longer involves $\beta_0,\beta_1$ at all — it is absorbed into the
proportionality constant. So

$$f_{\beta_0,\beta_1\mid\text{data}}(\beta_0,\beta_1) \;\propto\; \left[\frac{1}{S(\beta_0,\beta_1)}\right]^{n/2} \;=\;\left[\frac{S(\hat\beta_0,\hat\beta_1)}{S(\beta_0,\beta_1)}\right]^{n/2}$$

(the second form just multiplies by $1=S(\hat\beta_0,\hat\beta_1)^{-n/2}/S(\hat\beta_0,\hat\beta_1)^{-n/2}$,
to compare the posterior directly against its value at the least-squares point).

### The posterior concentrates at the least-squares estimate

Since $S(\beta)\ge S(\hat\beta)$ everywhere, the ratio $S(\hat\beta)/S(\beta)\le1$ with equality exactly at
$\beta=\hat\beta$: **the posterior mode is the least-squares estimator**, for any $C$ and any data. The
exponent $n/2$ makes the posterior fall off fast as $S(\beta)$ moves away from its minimum:

- if $S(\beta_0,\beta_1)$ is $10\%$ larger than $S(\hat\beta_0,\hat\beta_1)$, the posterior there is only
  $(1/1.1)^{n/2}$ of its peak value;
- if it is just $1\%$ larger, the posterior there is $(1/1.01)^{n/2}$ of its peak.

Both ratios shrink toward $0$ as $n$ grows, so for realistic sample sizes the posterior mass is squeezed
tightly around $\hat\beta_0,\hat\beta_1$: a flat prior does not stop the data from pinning down the
coefficients once $n$ is large enough. What remains, $[S(\hat\beta)/S(\beta)]^{n/2}$, is (up to
normalization) a bivariate $t$-density.

### Generalizing: the multivariate $t$ posterior

The same argument runs unchanged for $m+1$ coefficients $\beta_0,\dots,\beta_m$ with a flat prior on each
of them and on $\log\sigma$: the joint posterior is $\propto \sigma^{-n-1}\exp[-S(\beta)/2\sigma^2]$, and
integrating out $\sigma$ the same way gives

$$f_{\beta\mid\text{data}}(\beta) \;\propto\; \left[\frac{1}{S(\beta)}\right]^{n/2} \;\propto\; \left[\frac{S(\hat\beta)}{S(\beta)}\right]^{n/2}.$$

Now bring in the decomposition $S(\beta)=S(\hat\beta)+(\beta-\hat\beta)^TX^TX(\beta-\hat\beta)$ from the
least-squares section:

$$f_{\beta\mid\text{data}}(\beta)\;\propto\;\left\{\frac{S(\hat\beta)}{S(\hat\beta)+(\beta-\hat\beta)^TX^TX(\beta-\hat\beta)}\right\}^{n/2} = \left\{1+\frac{(\beta-\hat\beta)^TX^TX(\beta-\hat\beta)}{S(\hat\beta)}\right\}^{-n/2}.$$

This is exactly the shape of a $p$-dimensional multivariate $t$-density with location $\mu$, scale matrix
$\Sigma$, and $\nu$ degrees of freedom,

$$\left[1+\frac1\nu(x-\mu)^T\Sigma^{-1}(x-\mu)\right]^{-(\nu+p)/2},$$

matched term by term: $p=m+1$ (the number of coefficients), $\mu=\hat\beta$; matching exponents
$\nu+p=n\Rightarrow \nu=n-p=n-m-1$; matching the quadratic forms $\frac1\nu\Sigma^{-1}=\dfrac{X^TX}{S(\hat\beta)}
\Rightarrow \Sigma=\dfrac{S(\hat\beta)}{n-m-1}(X^TX)^{-1}$. So

$$\big(\beta_0,\dots,\beta_m\big)\mid\text{data} \;\sim\; t_{m+1}\!\left(\hat\beta,\ \frac{S(\hat\beta)}{n-m-1}(X^TX)^{-1},\ n-m-1\right).$$

The degrees of freedom $n-m-1$ that fall out of matching exponents are exactly the residual degrees of
freedom from the frequentist section, and the scale matrix is $\hat\sigma^2_{unbiased}(X^TX)^{-1}$ — the
same matrix that appears as $\hat\beta$'s frequentist covariance once $\sigma^2$ is replaced by its
unbiased estimate. That is the sense in which, as the notes put it, "Bayesian inference is also based on
the least-squares estimator": mode, location, and scale all agree with the frequentist answer, and the
heavier ($t$, rather than normal) tail of the posterior is exactly what accounts for not knowing $\sigma$
— in parallel with why the frequentist confidence interval also switches from a $z$- to a $t$-quantile.
The lecture also notes that one can *simulate* draws $\beta^{(1)},\beta^{(2)},\dots,\beta^{(N)}$ from this
$t$-posterior directly, rather than working with its density in closed form.

## Frequentist and Bayesian answers, side by side

| | Frequentist | Bayesian (flat prior) |
|---|---|---|
| Point estimate | $\hat\beta=(X^TX)^{-1}X^Ty$ (least squares $=$ MLE) | posterior mode $=\hat\beta$ |
| Spread | $\hat\beta\sim N\big(\beta,\sigma^2(X^TX)^{-1}\big)$; $\sigma$ estimated by $\hat\sigma_{unbiased}$ | $\beta\mid\text{data}\sim t_{m+1}\big(\hat\beta,\ \hat\sigma^2_{unbiased}(X^TX)^{-1},\ n-m-1\big)$ |
| Where the heavier tail comes from | swapping $z_{\alpha/2}$ for $t_{n-m-1,\alpha/2}$ because $\sigma$ is estimated | integrating $\sigma$ out of the joint posterior instead of plugging in an estimate |

## Exercises

1. In the identity $S(\beta) = S(\hat\beta) + (\hat\beta-\beta)^TX^TX(\hat\beta-\beta) + 2(y-X\hat\beta)^TX(\hat\beta-\beta)$,
   show that the cross term vanishes, using the normal equations $X^Ty=X^TX\hat\beta$.

2. Verify $\nabla_\beta(\beta^TX^Ty)=X^Ty$ and $\nabla_\beta(\beta^TX^TX\beta)=2X^TX\beta$ (the second using
   $\nabla(\beta^TA\beta)=2A\beta$ for symmetric $A$), and check that setting $\nabla S(\beta)=0$ reproduces
   the normal equations $X^TX\beta=X^Ty$.

## Sources

- Handwritten lecture notes, Berkeley STAT 153, "Lecture Four", fall 2025 offering — reconstructed by a
  model from a PDF with no text layer (`route: llm`, `fidelity: reconstructed`); every equation is
  unverified against the original scan. Source PDF:
  [`HandwrittenNotesLectureFour153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureFour153248Fall2025.pdf).
  Converted pages used: `01-bayesian-inference-for-simple-linear-regression.md` (single-covariate Bayesian
  derivation and the posterior-concentration argument), `02-multiple-linear-regression.md` (covariate
  constructions from time and from lags; multivariate-$t$ statement), `03-matrix-notation-for-regression.md`
  (matrix least-squares derivation, the $S(\beta)$ decomposition, and the $t$-posterior parameter matching).
- Handwritten lecture notes, Berkeley STAT 153, "Lecture Four", fall 2026 offering — same reconstruction
  route and caveats. Source PDF:
  [`HandwrittenNotesLectureFour153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureFour153248Fall2026.pdf).
  Converted pages used: `01-multiple-linear-regression.md` (model setup and covariate construction),
  `02-frequentist-inference.md` (MLE derivation and the least-squares/MLE equivalence), `03-step-2.md`
  (sampling distribution of $\hat\beta$ and $\hat\sigma^2$, confidence intervals), `04-bayesian-approach.md`
  (direct multivariate Bayesian derivation).
- No slides, transcript, or problem set were supplied for this chapter. The two exercises above are the
  checks the notes explicitly leave to the reader (marked "Exercise" and "Check" in the source).

---

[← 65. Posterior of Multiple Regression Coefficients](65-posterior-of-multiple-regression-coefficients.md) · [Contents](index.md) · [67. Frequency and Breakpoint Estimation →](67-frequency-and-breakpoint-estimation.md)
