---
title: "27. Recap: The General Linear Model"
course: "StatOmics Sga21"
chapter: 27
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 27. Recap: The General Linear Model

## What this covers

The chapter answers a single practical question: how do you go from "does gene expression differ
between two groups" to a model that can hold several factors — and their interaction — at once,
and what do the numbers that come out of that model actually mean? It works through one running
example, a breast-cancer microarray study, from a two-sample comparison up to the matrix form of
the general linear model, least squares, and testing a composite hypothesis with a contrast. It
assumes familiarity with basic hypothesis testing (the $t$-test, $p$-values) and with matrix
algebra (transpose, matrix product, inverse).

## The motivating study

The running example is a breast-cancer study (Sotiriou et al., [doi:10.1093/jnci/djj052](https://doi.org/10.1093/jnci/djj052)).
Histologic grade is a clinically established prognostic factor in breast cancer, and the question
is whether it is associated with the expression of *KPNA2*, a gene already linked to poor
prognosis. The population of interest is "all current and future breast cancer patients" — the
sample in hand is only a stand-in for that population, which is why everything downstream is
phrased as inference rather than as a description of the data at hand.

The measured quantity, `gene`, is a background-corrected, normalized intensity from a microarray
platform. It is not itself the gene expression level; after a log transform it is treated as a
good proxy for the log-transformed concentration of the KPNA2 expression product.

## A first test: one factor at a time

### Setting up the hypotheses

The direct question — "are grade 1 and grade 3 patients different, on average, in KPNA2 expression"
— is not attacked head on. Instead, the analysis starts from the alternative hypothesis $H_A$ (the
thing you actually want to show: the means differ) and tries to falsify its opposite, the null
hypothesis

$$
H_0:\ \text{average KPNA2 expression is equal for grade 1 and grade 3 patients.}
$$

A $p$-value answers a precise question about $H_0$: *how likely is it to see an association at
least as extreme as the one observed in this sample, if $H_0$ were true?* Quantifying that
probability requires an assumption about the distribution of the test statistic. If the $p$-value
falls below a chosen significance level $\alpha$, $H_0$ is rejected, and $\alpha$ is exactly the
rate of false positives (Type I errors) this procedure is willing to tolerate in the long run. The
one condition that makes the whole argument work is easy to lose sight of: **the $p$-value is only
correct if the assumptions behind it hold.**

### Why log the data

Raw microarray intensities are usually not normally distributed, and, worse, their variance tends
to grow with their mean — a *mean–variance relationship* that violates the equal-variance
assumption a simple two-sample $t$-test relies on. The standard fix is a $\log_2$ transform, which
has a second, very useful property: a difference on the log scale is a fold change,

$$
\log_2(B) - \log_2(A) = \log_2\frac{B}{A} = \log_2 FC_{B/A}.
$$

On the raw scale, `t.test(gene ~ grade, data = gene)` defaults to a Welch test that does not assume
equal variances — visible in the fractional degrees of freedom it reports (a Satterthwaite
approximation, not an integer), which is itself evidence that the two groups' variances were not
being treated as equal. After the $\log_2$ transform, the variances of the two grade groups become
plausible to treat as equal, and the analysis switches to a pooled two-sample $t$-test
(`var.equal = TRUE`).

### Conclusion

The log-scale test finds an extremely significant association between histologic grade and KPNA2
expression: on average, grade 3 patients express the gene some multiplicative factor $2^{\log_2 FC}$
higher than grade 1 patients, with a 95% confidence interval obtained by back-transforming the
confidence interval on the log scale, and $p \ll 0.001$. (The slide leaves the fold change and its
interval as inline computations — `2^log2FC` and a back-transformed `conf.int` — rather than
printed numbers, so no specific value is repeated here.)

That single comparison, though, is not the whole story: the same patients also differ in their
lymph-node status. Treating grade in isolation throws that information away, and raises the
question of how to test more than one factor — and any interaction between them — in one model.

## Two factors together: the general linear model

The fix is to fold both factors into a single linear model. With two dummy variables,

$$
x_{i,1}=\begin{cases}0 & \text{grade 1}\\ 1 & \text{grade 3}\end{cases}
\qquad
x_{i,2}=\begin{cases}0 & \text{lymph nodes not removed}\\ 1 & \text{lymph nodes removed}\end{cases}
$$

the model is

$$
y_i = \beta_0 + \beta_1 x_{i,1} + \beta_2 x_{i,2} + \beta_{12}\,x_{i,1}x_{i,2} + \epsilon_i .
$$

$\beta_1$ and $\beta_2$ are the two main effects, and $\beta_{12}$ is the *interaction*: the extra
shift that applies only when both dummies are switched on at once. Writing out the mean for the
four grade $\times$ node combinations makes the parametrization concrete — baseline (grade 1, node
not removed) has mean $\beta_0$; switching grade alone adds $\beta_1$; switching node alone adds
$\beta_2$; switching both adds $\beta_1+\beta_2+\beta_{12}$, not simply $\beta_1+\beta_2$, unless
$\beta_{12}=0$. In R this is fit in one line,

```r
lm1 <- lm(gene ~ grade * node, data = gene)
```

where the formula `grade * node` is shorthand for `grade + node + grade:node`, i.e. exactly the
two main effects and the interaction above. What is still left open at this point is the
distribution of $\epsilon_i$ — resolved in the next section as i.i.d. $N(0,\sigma^2)$, an assumption
checked in practice with `plot(lm1)` (residuals-vs-fitted for non-constant variance, a normal
QQ-plot for non-normality), for exactly the reason flagged above: the $p$-values this model produces
are only correct if that assumption is reasonable.

## Linear regression in matrix form

### From scalar model to matrix model

Stripped of the specific example, a linear regression with predictors
$\mathbf x = (x_1,\ldots,x_p)^T$ and response $Y$ is

$$
Y = f(\mathbf x) + \epsilon = \beta_0 + \sum_{j=1}^p x_j\beta_j + \epsilon, \qquad \epsilon \sim N(0,\sigma^2)\ \text{i.i.d.}
$$

Stacking $n$ observations $(\mathbf x_1,y_1),\ldots,(\mathbf x_n,y_n)$ turns this into a single
matrix equation,

$$
\mathbf Y = \mathbf X\boldsymbol\beta + \boldsymbol\epsilon,
$$

with $\mathbf Y$ the $n\times 1$ vector of responses, $\boldsymbol\beta$ the $(p+1)\times 1$
vector of coefficients (including the intercept), $\boldsymbol\epsilon$ the $n\times1$ error
vector, and $\mathbf X$ the $n\times(p+1)$ **design matrix**, whose first column is all 1's (for
the intercept) and whose remaining columns hold the predictors — dummy variables and interaction
products, in the breast-cancer model above, or a continuous covariate, in general.

### Least squares

Fitting the model means choosing $\boldsymbol\beta$ to minimize the residual sum of squares,

$$
RSS(\boldsymbol\beta) = \sum_{i=1}^n e_i^2 = \sum_{i=1}^n\Bigl(y_i - \beta_0 - \sum_{j=1}^p x_{ij}\beta_j\Bigr)^2
= (\mathbf Y - \mathbf X\boldsymbol\beta)^T(\mathbf Y-\mathbf X\boldsymbol\beta) = \lVert \mathbf Y - \mathbf X\boldsymbol\beta\rVert_2^2 .
$$

Differentiating with respect to $\boldsymbol\beta$ and setting the result to zero gives the
**normal equations**:

$$
\frac{\partial RSS}{\partial \boldsymbol\beta} = -2\mathbf X^T(\mathbf Y - \mathbf X\boldsymbol\beta) = \mathbf 0
\quad\Longrightarrow\quad
\mathbf X^T\mathbf X\,\boldsymbol\beta = \mathbf X^T\mathbf Y
\quad\Longrightarrow\quad
\hat{\boldsymbol\beta} = (\mathbf X^T\mathbf X)^{-1}\mathbf X^T\mathbf Y,
$$

provided $\mathbf X^T\mathbf X$ is invertible.

### Geometric interpretation: projection

The normal equations have a picture behind them. The fitted values are

$$
\hat{\mathbf Y} = \mathbf X(\mathbf X^T\mathbf X)^{-1}\mathbf X^T\mathbf Y,
$$

which is exactly the orthogonal projection of $\mathbf Y$ onto the column space of $\mathbf X$ —
the set of all vectors reachable as some linear combination of $\mathbf X$'s columns. In a toy
example with $n=3$, $p=2$, and no intercept, $\mathbf X$ has two columns $\mathbf X_1=(2,0,0)^T$,
$\mathbf X_2=(0,2,0)^T$; their column space is a plane through the origin inside $\mathbb R^3$, and
a simulated $\mathbf Y$ that is not exactly on that plane (because of noise) has its fit $\hat{\mathbf
Y}$ sitting on the plane, directly "below" it.

That the residual $\mathbf e = \mathbf Y - \hat{\mathbf Y}$ is orthogonal to every column of
$\mathbf X$ — not just a picture, but a restatement of the normal equations themselves —

$$
\mathbf X^T(\mathbf Y - \mathbf X\hat{\boldsymbol\beta}) = \mathbf 0,
$$

is the reason "projection" is the right word rather than just an analogy: least squares finds the
closest point to $\mathbf Y$, in ordinary Euclidean distance, that lies in the column space of
$\mathbf X$, and the closest point in a subspace is always found by dropping a perpendicular onto
it.

<figure>
<svg viewBox="0 0 320 240" role="img" aria-label="The least squares fit as an orthogonal projection of Y onto the column space of X">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <polygon points="40,192 232,190 292,218 100,220" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="270" y="232" font-size="12" fill="currentColor">column space of X</text>

  <circle cx="140" cy="203" r="2.2" fill="currentColor"/>
  <text x="128" y="196" font-size="12" fill="currentColor">O</text>

  <line x1="140" y1="203" x2="68" y2="196" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="52" y="192" font-size="12" fill="currentColor">X1</text>

  <line x1="140" y1="203" x2="248" y2="210" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="252" y="206" font-size="12" fill="currentColor">X2</text>

  <line x1="140" y1="203" x2="150" y2="65" stroke="currentColor" stroke-width="1.8" marker-end="url(#arrow)"/>
  <text x="156" y="62" font-size="12" fill="currentColor">Y</text>

  <line x1="140" y1="203" x2="150" y2="198" stroke="currentColor" stroke-width="1.8" marker-end="url(#arrow)"/>
  <text x="152" y="192" font-size="12" fill="currentColor">Ŷ</text>

  <line x1="150" y1="65" x2="150" y2="198" stroke="currentColor" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="158" y="130" font-size="12" fill="currentColor">e = Y − Ŷ</text>
  <path d="M144,196 L144,190 L150,190" fill="none" stroke="currentColor" stroke-width="1"/>
</svg>
<figcaption>The fitted values Ŷ are the foot of the perpendicular dropped from Y onto the plane
spanned by the columns of X; the residual e is orthogonal to that plane, which is exactly what the
normal equations say.</figcaption>
</figure>

### The variance of the least-squares estimator

Because $\hat{\boldsymbol\beta}$ is a linear function of $\mathbf Y$, its variance follows from
$\mathrm{Var}[\mathbf Y]=\sigma^2\mathbf I$ (the errors are i.i.d. with common variance $\sigma^2$):

$$
\hat{\boldsymbol\Sigma}_{\hat{\boldsymbol\beta}}
= \mathrm{Var}\bigl[(\mathbf X^T\mathbf X)^{-1}\mathbf X^T\mathbf Y\bigr]
= (\mathbf X^T\mathbf X)^{-1}\mathbf X^T\,\mathrm{Var}[\mathbf Y]\,\mathbf X(\mathbf X^T\mathbf X)^{-1}
= (\mathbf X^T\mathbf X)^{-1}\mathbf X^T\mathbf X(\mathbf X^T\mathbf X)^{-1}\sigma^2
= (\mathbf X^T\mathbf X)^{-1}\sigma^2 .
$$

The middle simplification is just $\mathbf X^T\mathbf X(\mathbf X^T\mathbf X)^{-1}=\mathbf I$; the
whole calculation only needed that constant $\sigma^2$ came out of the middle of the sandwich as a
scalar.

### Degrees of freedom and estimating $\sigma^2$

$\sigma^2$ itself is not known and has to be estimated from the residuals, using

$$
\hat\sigma^2 = \frac{\sum_{i=1}^n e_i^2}{n-p}, \qquad df = n-p,
$$

where $p$ here is the number of columns of the design matrix $\mathbf X$ (intercept included) —
`ncol(X)` in R — so that $df$ is exactly the number of observations left over after every fitted
parameter has "used up" one.

### Contrasts

Many research questions are not about a single coefficient but about a linear combination of
several — a **contrast**. For the two-factor model with parameter vector
$\boldsymbol\beta = (\beta_0,\ \beta_{g3},\ \beta_{n1},\ \beta_{g3:n1})^T$, consider the question
"is there a grade effect among node-positive patients?" The mean for (grade 3, node 1) is
$\beta_0+\beta_{g3}+\beta_{n1}+\beta_{g3:n1}$ and the mean for (grade 1, node 1) is
$\beta_0+\beta_{n1}$; their difference — the log$_2$ fold change between grade 3 and grade 1,
restricted to the node-1 patients — is

$$
\log_2 FC_{g3n1-g1n1} = \beta_{g3} + \beta_{g3:n1},
$$

which is exactly $\mathbf L^T\boldsymbol\beta$ for the contrast vector $\mathbf L = (0,1,0,1)^T$.
Any such contrast inherits its variance directly from $\hat{\boldsymbol\Sigma}_{\hat{\boldsymbol\beta}}$:

$$
\mathrm{Var}\bigl[\mathbf L^T\hat{\boldsymbol\beta}\bigr] = \mathbf L^T\,\hat{\boldsymbol\Sigma}_{\hat{\boldsymbol\beta}}\,\mathbf L,
$$

which is what turns "is this combination of coefficients zero" into an ordinary $t$-test: the
estimate $\mathbf L^T\hat{\boldsymbol\beta}$ divided by the square root of this variance.

## Exercises

The following is the course's own homework on this material, using the KPNA2 dataset on the
log$_2$-transformed scale (`lgene`), with the two-factor interaction model `~ grade * node`.

1. Build the design matrix `X <- model.matrix(~ grade * node, data = gene)` and, working entirely
   with matrix operations (transpose `t()`, matrix product `%*%`, inverse `solve()`, diagonal
   `diag()` — no call to `lm()`), compute:
   - the parameter estimates $\hat{\boldsymbol\beta} = (\mathbf X^T\mathbf X)^{-1}\mathbf X^T\mathbf Y$;
   - the residual degrees of freedom $df = n - p$ and the variance estimate
     $\hat\sigma^2 = \sum_i e_i^2/(n-p)$;
   - the estimated covariance matrix $\hat{\boldsymbol\Sigma}_{\hat{\boldsymbol\beta}} = \hat\sigma^2(\mathbf X^T\mathbf X)^{-1}$
     and, from its diagonal, the standard error of each parameter;
   - the estimate, standard error and $t$-statistic of a contrast of interest (for instance, the
     grade effect within the node = 1 group derived above).
2. Compare every quantity from part 1 against the output of
   `summary(lm(lgene ~ grade * node, data = gene))`.

## Sources

- Motivating study and population: [`01-breast-cancer-example.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd)
  (statOmics SGA21, *Statistical Genomics 2021*, recap-general-linear-model deck), citing
  Sotiriou et al., [doi:10.1093/jnci/djj052](https://doi.org/10.1093/jnci/djj052).
- Hypothesis testing, $p$-values, the log transform and the single-factor conclusion:
  [`03-statistical-inference.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd)
  of the same deck. This section links onward to a "Data Exploration" section that was referred to
  (via its navigation footer) but not among the material supplied for this chapter.
- Two-factor model with interaction, its R fit and its diagnostic checking:
  [`04-general-linear-model.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd).
- Matrix form of linear regression, least squares, the projection geometry (including the $n=3,
  p=2$ toy example), the variance of $\hat{\boldsymbol\beta}$, contrasts, and the homework:
  [`05-linear-regression-in-matrix-form.md`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd).
  This section points to chapter 2 of Faraway's regression textbook for further detail on the
  implementation; that book was referred to but not supplied as source material here.
- No lecture transcript was supplied for this session — the chapter is built from the slide deck
  alone (the deck's own images, referenced by URL in the source files, were not separately
  available and are not reproduced; the projection figure above redraws the argument the deck's own
  R code walks through, not a copy of its plot).

---

[← 26. Mass Spectrometry-Based Proteomics](26-mass-spectrometry-based-proteomics.md) · [Contents](index.md) · [28. Gene-level quantification →](28-gene-level-quantification.md)
