---
title: "81. Regression: Estimation and Evaluation"
course: "Berkeley Stat 153 Fall 2024"
chapter: 81
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 81. Regression: Estimation and Evaluation

## What this covers

This chapter follows one problem set on linear regression: how the regression coefficients are
defined and estimated, how good the resulting estimator is as an estimator, and how to tell whether
a fitted regression model is actually any good at predicting new data. It assumes the reader already
knows informally what a regression line is, and is comfortable with expectation, variance and
covariance, and with basic matrix algebra (transposes, inverses). A few pieces of the underlying
theory — the covariance-of-linear-combinations rule, the definitions of two of the error metrics
below, and the R code for time series cross-validation — were given in lectures that are not part of
the material supplied for this chapter; where that happens it is flagged rather than filled in.

## Population and sample regression

The most basic regression problem asks for the best linear approximation to a response $y$ using a
single feature $x$. "Best" needs a criterion, and this course sets up the same criterion twice, once
in theory and once in practice.

In the **population** version, $x$ and $y$ are random variables with some joint distribution, and
the least squares coefficients $\beta_0,\beta_1$ are the minimisers of the mean squared error over
the whole population:

$$
\min_{\beta_0,\beta_1} \; \mathbb{E}\big[(y-\beta_0-\beta_1 x)^2\big].
$$

This is a genuinely theoretical object — it depends on the joint distribution of $(x,y)$, not on any
particular sample — and it is what a slope coefficient means "in the population."

In the **sample** version, the same idea is applied to $n$ observed pairs $(x_i,y_i)$, with the
expectation replaced by an average over the data:

$$
\min_{\beta_0,\beta_1} \; \sum_{i=1}^n (y_i-\beta_0-\beta_1 x_i)^2.
$$

Both problems are solved the same way: differentiate the criterion with respect to each $\beta_j$,
set the two derivatives to zero, and solve the resulting pair of equations (the *normal equations*)
for $\beta_0$ and $\beta_1$. The population and sample calculations are formally the same
calculation, with an expectation in one place and a sample average in the other, which is the point
of doing them side by side.

A variant drops the intercept altogether, forcing the line through the origin:
$\min_{\beta_1}\mathbb{E}[(y-\beta_1 x)^2]$ in the population, or the corresponding sum in the
sample. The same differentiate-and-solve method applies, now with only one unknown, and it gives a
different coefficient in general than the version with an intercept.

## Two regressions, two lines

A recurring trap is to treat "the regression of $y$ on $x$" and "the regression of $x$ on $y$" as two
descriptions of the same line. They are not, in general: minimising $\mathbb{E}[(y-\beta_1x)^2]$
over $\beta_1$ and minimising $\mathbb{E}[(x-\gamma_1y)^2]$ over $\gamma_1$ are different
optimisation problems, and there is no reason for $\gamma_1$ to equal $1/\beta_1$ — whether it does,
in the no-intercept model, is exactly the kind of question this course asks you to settle by
calculation rather than by intuition.

The Galton-style example below sits on top of this. Two separate regressions of a child's height on
a parent's height — one using fathers, one using mothers — can have a *smaller* slope for fathers
even though the father-child correlation is *larger* than the mother-child correlation. This is only
puzzling if slope and correlation are assumed to move together; slope and correlation are related but
not identical (the slope also depends on the relative spread of $x$ and $y$), and finding the precise
mechanism that lets them diverge here is left as an exercise.

## Multiple regression, two ways

With $p$ features per observation, $x_i \in \mathbb{R}^p$ for $i=1,\dots,n$, the multiple regression
coefficient vector was presented in lecture in two forms. Written as a sum over observations,

$$
\hat\beta = \Big(\sum_{i=1}^n x_ix_i^T\Big)^{-1} \sum_{i=1}^n x_iy_i,
$$

and written in terms of the $n\times p$ feature matrix $X$ (with $i$th row $x_i^T$) and the response
vector $y$ (with $i$th entry $y_i$),

$$
\hat\beta = (X^TX)^{-1}X^Ty.
$$

These look different — one is a sum over $n$ observations, the other a single matrix expression —
but lecture asserted they are the same estimator. Making that identification precise, and
re-deriving the estimator directly from the least squares criterion $\min_\beta \sum_i (y_i -
x_i^T\beta)^2$ by the same differentiate-and-solve method as in the simple regression case, are both
left as exercises.

## Covariance under linear maps, and the variance of $\hat\beta$

For a fixed matrix $A$ and a random vector $x$, $\mathrm{Cov}(Ax)$ measures how the transformed
vector varies. The scalar version of this idea — $\mathrm{Cov}(aX+b,\,cY+d) = ac\,\mathrm{Cov}(X,Y)$
for constants $a,b,c,d$ — was covered in an earlier lecture ("Measures of dependence and
stationarity", week 2), which is not part of the material for this chapter. What is new here is the
matrix version: for random vectors $x\in\mathbb{R}^n$, $y\in\mathbb{R}^m$ and fixed matrices
$A\in\mathbb{R}^{k\times n}$, $B\in\mathbb{R}^{\ell\times m}$,

$$
\mathrm{Cov}(Ax,By) = A\,\mathrm{Cov}(x,y)\,B^T,
$$

with the single-vector case $\mathrm{Cov}(Ax) = A\,\mathrm{Cov}(x)\,A^T$ following by taking $y=x$,
$B=A$. This rule is the tool for everything below.

It applies directly to the regression model $y = X\beta + \epsilon$, with $X$ and $\beta$ fixed and
$\epsilon$ white noise of variance $\sigma^2$ — meaning $\mathrm{Cov}(\epsilon) = \sigma^2 I$, entries
uncorrelated with a common variance. The OLS estimator $\hat\beta = (X^TX)^{-1}X^Ty$ is a *linear*
function of $y$: a fixed matrix, $(X^TX)^{-1}X^T$, times the random vector $y$. So the linear-map
rule applies to it directly, and the claim to be checked is that

$$
\mathrm{Cov}(\hat\beta) = \sigma^2 (X^TX)^{-1}.
$$

This is what "more data, or more spread-out features, shrink the estimator's variability" means
precisely: $\mathrm{Cov}(\hat\beta)$ scales inversely with $X^TX$, which grows with $n$ and with how
spread out the features are.

## The Gauss-Markov theorem

Among all **linear** estimators of $\beta$ — meaning $\tilde\beta = My$ for some fixed matrix $M$,
not necessarily $(X^TX)^{-1}X^T$ — and among those that are **unbiased**
($\mathbb{E}[\tilde\beta]=\beta$), the Gauss-Markov theorem says the OLS estimator has the smallest
covariance matrix. "Smallest" needs a partial order on matrices, since covariance matrices are not
numbers: write $A \lesssim B$ (the *positive semidefinite*, or *PSD*, ordering) when $B-A$ is
positive semidefinite, i.e. $z^T(B-A)z \geq 0$ for every vector $z$. In this language the theorem
reads

$$
\mathrm{Cov}(\hat\beta) \lesssim \mathrm{Cov}(\tilde\beta) \quad \text{for every unbiased linear } \tilde\beta,
$$

which is the statement that OLS is *BLUE*: the best linear unbiased estimator, where "best" means
smallest variance in every direction $z^T\tilde\beta$ simultaneously. That this PSD-ordering
statement is really equivalent to the form of the theorem given in lecture is left as an exercise.

## Judging predictions: MAE, MAPE, and why the denominator matters

Fitting a model is one thing; judging whether its predictions $\hat y_t$ are good, against the
realised values $y_t$, is another — and this part of the course is titled "metrics matter" for a
reason. Two standard summaries of prediction error, both defined in lecture, are the **mean absolute
error**,

$$
\mathrm{MAE} = \frac{1}{N}\sum_{t=1}^N |y_t - \hat y_t|,
$$

and the **mean absolute percentage error**,

$$
\mathrm{MAPE} = 100\times\frac{1}{N}\sum_{t=1}^N \frac{|y_t-\hat y_t|}{|y_t|},
$$

which rescales each error by the size of the actual value, so an error of $1$ counts for more when
$y_t$ is small than when it is large. A third metric, given directly in the homework, is the **mean
absolute relative error**,

$$
\mathrm{MARE} = 100\times\frac{1}{N}\sum_{t=1}^N \frac{|y_t-\hat y_t|}{|\hat y_t|},
$$

which looks almost identical to MAPE but divides by the *prediction* $\hat y_t$ instead of the
*actual value* $y_t$. That single change is not cosmetic: MAPE penalises a fixed absolute error more
when the true value happens to be small, while MARE penalises it more when the *prediction* happens
to be small. A model can score very differently under the two conventions if its predictions and the
truth diverge in scale somewhere in the series — exactly the situation set up in the exercises below,
where a series changes regime partway through and competing predictions track that regime change at
different rates.

## Time series cross-validation

Evaluating a model on the same data used to fit it overstates how well it will do on new data (see
the next section); the standard fix is **cross-validation**, and for data indexed in time the split
into "training" and "test" data has to respect the order of time — a model may only be judged on
predictions it made without seeing the future. The homework's setup (its R code is from lecture and
is not part of the supplied material) has two parts:

- a **burn-in set**, times $1$ through $t_0$, used to fit one initial regression model; the fitted
  values on this stretch give a **training error** (e.g. training MAE), which is a measure of fit to
  already-seen data, not of forecast quality;
- a **trailing window**: at each time after $t_0$, the model is refit using only the most recent
  fixed-length stretch of data (not the entire past), and used to predict the single next point.
  Sliding this window forward one step at a time, and comparing every such prediction to the value
  that actually occurred, gives an out-of-sample, **cross-validated** error over the whole
  evaluation period.

<figure>
<svg viewBox="0 0 620 220" role="img" aria-label="A trailing window sliding forward in time to make one-step-ahead predictions after an initial burn-in fit">
  <defs>
    <marker id="cv-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="40" y1="180" x2="590" y2="180" stroke="currentColor" stroke-width="1.5" marker-end="url(#cv-arrow)"/>
  <text x="555" y="200" font-size="12" fill="currentColor">time</text>
  <rect x="40" y="60" width="160" height="100" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="120" y="50" text-anchor="middle" font-size="12" fill="currentColor">burn-in (1..t0), fit once</text>
  <line x1="200" y1="60" x2="200" y2="180" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="200" y="196" text-anchor="middle" font-size="11" fill="currentColor">t0</text>
  <rect x="210" y="95" width="90" height="55" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="255" y="88" text-anchor="middle" font-size="11" fill="currentColor">trailing window</text>
  <line x1="300" y1="130" x2="322" y2="176" stroke="currentColor" stroke-width="1.2" marker-end="url(#cv-arrow)"/>
  <circle cx="325" cy="180" r="3" fill="currentColor"/>
  <text x="305" y="145" font-size="11" fill="currentColor">predict</text>
  <rect x="280" y="95" width="90" height="55" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
  <line x1="258" y1="78" x2="308" y2="78" stroke="currentColor" stroke-width="1.2" marker-end="url(#cv-arrow)"/>
  <text x="283" y="68" text-anchor="middle" font-size="11" fill="currentColor">slides forward</text>
  <line x1="370" y1="130" x2="392" y2="176" stroke="currentColor" stroke-width="1.2" marker-end="url(#cv-arrow)"/>
  <circle cx="395" cy="180" r="3" fill="currentColor"/>
  <text x="430" y="150" font-size="14" fill="currentColor">…</text>
</svg>
<figcaption>The model is fit once on the burn-in set, then a fixed-length trailing window slides
forward through time, refitting and predicting one step ahead at each position, so that no fitted
model ever sees the point it is being asked to predict.</figcaption>
</figure>

The dataset used to illustrate this is a regression of cardiovascular mortality on lagged particulate
air pollution levels (and, in later exercises, lagged temperature too), with the lag length and the
number of lagged features increasing across the exercises below — from a single 4-week lag, to lags
$4,8,12$, to lags $4,5,\dots,50$ for each variable.

## More features, the merrier? Overfitting

Adding a feature to a regression can only help the fit on the data used to fit it. Precisely: if
$\hat y_i$ are the fitted values from regressing $y_i$ on $x_i\in\mathbb{R}^p$, and $\tilde y_i$ are
the fitted values after appending one more feature to get $\tilde x_i \in \mathbb{R}^{p+1}$, then

$$
\sum_{i=1}^n (y_i-\tilde y_i)^2 \;\leq\; \sum_{i=1}^n (y_i-\hat y_i)^2.
$$

The reason this has to be true is that the smaller model is a special case of the larger one: every
coefficient vector achievable in the $p$-feature model is also achievable in the $(p+1)$-feature
model, by giving the new feature a coefficient of $0$. So the larger model's least squares problem
minimises the same kind of sum of squares over a *bigger* set of candidate fits than the smaller
model does, and minimising over a bigger set can never produce a larger minimum. Turning that
sentence into a rigorous inequality is left as an exercise; the sentence itself says nothing about
whether the extra feature *should* be there, only that training error is the wrong quantity to ask.

Pushed far enough, this becomes a statement about exact interpolation: with enough linearly
independent features relative to the number of observations, a regression can fit the training data
perfectly, driving the training MSE to exactly zero. How many features that takes, and why, is left
as an exercise — as is checking it by simulation, ideally on the cardiovascular mortality data with
enough lagged features. The lesson to notice, alongside the cross-validation exercises above, is that
a perfect in-sample fit is entirely compatible with wild, useless out-of-sample predictions. That gap
between training error and cross-validated error is the reason the cross-validation machinery exists
at all.

## Exercises

Numbered as in the original homework; points are shown in parentheses, and "bonus" problems are
optional (they can earn back points lost elsewhere but cannot push a score above full marks).

**Simple regression**

1. (2 pts) Derive the population least squares coefficients $\beta_0,\beta_1$ that solve
   $\min_{\beta_0,\beta_1}\mathbb{E}[(y-\beta_0-\beta_1x)^2]$, by differentiating the criterion with
   respect to each $\beta_j$, setting the derivatives to zero, and solving. Repeat without the
   intercept term $\beta_0$.

2. (2 pts) Do the same for the sample least squares coefficients solving
   $\min_{\beta_0,\beta_1}\sum_{i=1}^n (y_i-\beta_0-\beta_1x_i)^2$, again with and without an
   intercept.

3. (2 pts) Prove or disprove: in the model without an intercept, the regression coefficient of $x$ on
   $y$ is the inverse of the regression coefficient of $y$ on $x$. Answer for both the population and
   the sample version.

4. (3 pts) In a large population, let $y$ be a child's height and $x$ a parent's height, and consider
   separate regressions of $y$ on $x$ for fathers and for mothers. Suppose the slope from the father
   regression, $\hat\beta_1^{\text{dad}}$, is smaller than the slope from the mother regression,
   $\hat\beta_1^{\text{mom}}$, while the sample correlation between father and child heights is
   *larger* than that between mother and child heights. Give a plausible explanation.

**Multiple regression**

5. (2 pts) With responses $y_i$ and feature vectors $x_i\in\mathbb{R}^p$, $i=1,\dots,n$, prove that
   $$
   \hat\beta = \Big(\sum_{i=1}^n x_ix_i^T\Big)^{-1}\sum_{i=1}^n x_iy_i
   \quad\text{and}\quad
   \hat\beta = (X^TX)^{-1}X^Ty
   $$
   (where $X\in\mathbb{R}^{n\times p}$ has $i$th row $x_i^T$, and $y\in\mathbb{R}^n$ has $i$th entry
   $y_i$) are the same expression.

6. (Bonus) Derive the population and sample multiple regression coefficients directly from the
   corresponding least squares problem, by differentiating with respect to each $\beta_j$ and
   solving. For the sample coefficient, deriving either form from Exercise 5 is enough.

**Covariance calculations**

7. (3 pts) For random vectors $x\in\mathbb{R}^n$, $y\in\mathbb{R}^m$ and fixed matrices
   $A\in\mathbb{R}^{k\times n}$, $B\in\mathbb{R}^{\ell\times m}$, prove that
   $\mathrm{Cov}(Ax,By)=A\,\mathrm{Cov}(x,y)\,B^T$, and deduce that
   $\mathrm{Cov}(Ax)=A\,\mathrm{Cov}(x)\,A^T$. (You may use the covariance-of-linear-combinations
   rule from the week 2 lecture on measures of dependence and stationarity.)

8. (2 pts) For the model $y=X\beta+\epsilon$, with $X,\beta$ fixed and $\epsilon$ white noise of
   variance $\sigma^2$, use Exercise 7 to show that the sample least squares coefficient
   $\hat\beta=(X^TX)^{-1}X^Ty$ satisfies $\mathrm{Cov}(\hat\beta)=\sigma^2(X^TX)^{-1}$.

9. (4 pts) One statement of the Gauss-Markov theorem is: if $\tilde\beta=My$ is any other unbiased
   linear estimator of $\beta$ (for a fixed matrix $M$), then
   $\mathrm{Cov}(\hat\beta)\lesssim\mathrm{Cov}(\tilde\beta)$, where $A\lesssim B$ means $B-A$ is
   positive semidefinite (i.e. $z^T(B-A)z\geq0$ for every $z$). Show that this is equivalent to the
   form of the theorem given in lecture.

**Metrics matter**

10. (4 pts) Data `y` and predictions `yhat1`, `yhat2` from two hypothetical models are generated by:
    ```r
    set.seed(0)
    x = 1:50
    y = rpois(n = 50, lambda = c(rep(5, 25), 5 + exp(0:24 * 0.2)))
    yhat1 = c(rep(6.5, 25), 6.5 + exp(0:24 * 0.2))
    yhat2 = c(rep(5, 25), 5 + exp(0:24 * 0.18))
    ```
    Plot both predictions as coloured lines over the data, with a legend. Compute and report the MAE
    and MAPE (as defined in lecture) for each model, and discuss what you find.

11. (4 pts) Define `yhat3` by taking `yhat2` and changing the exponent multiplier for the last 25
    predictions from `0.18` to `0.22`. Plot `yhat2` and `yhat3` against the data with a legend, and
    compute and compare their MAE and MAPE — it should be worse for `yhat3` by both. Then, for each
    of `yhat2` and `yhat3`, compute the mean absolute relative error
    $$
    \mathrm{MARE} = 100\times\frac{1}{N}\sum_{t=1}^N\frac{|y_t-\hat y_t|}{|\hat y_t|}.
    $$
    Discuss what you find.

**Cross-validation**

12. (3 pts) Adapt the lecture's R code for time series cross-validation (evaluating the MAE of
    cardiovascular mortality regressed on 4-week lagged particulate levels) to a regression on
    4-week lagged particulate levels *and* 4-week lagged temperature (2 features). Fit each model on
    a trailing window of 200 time points (not all past data). Plot the predictions with the MAE
    printed on the plot, along with the fitted values on the burn-in set (times 1 through $t_0$) in
    a different colour, labelled with the training MAE.

13. (2 pts) Repeat Exercise 12 using lags 4, 8, 12 of each variable (6 features total). Did the
    training MAE go down? Did the cross-validated MAE go down? Discuss.

14. (2 pts) Repeat again using lags 4 through 50 of each variable (94 features total). Did the
    training MAE go down? Did the cross-validated MAE go down? Are you surprised? Discuss.

**More features, the merrier?**

15. (2 pts) Let $y_i$ be a response and $x_i\in\mathbb{R}^p$ a feature vector, $i=1,\dots,n$, and let
    $\tilde x_i = (x_{i1},\dots,x_{ip},\tilde x_{i,p+1})$ append one more feature. Let $\hat y_i$ and
    $\tilde y_i$ be the fitted values of $y_i$ regressed on $x_i$ and on $\tilde x_i$ respectively.
    Prove that
    $$
    \sum_{i=1}^n(y_i-\tilde y_i)^2 \leq \sum_{i=1}^n(y_i-\hat y_i)^2,
    $$
    i.e. training MSE never gets worse when a feature is added.

16. (2 pts) How many linearly independent features (how large should $p$ be?) are needed to make the
    training MSE exactly zero? Why?

17. (Bonus) Verify your answer to Exercise 16 empirically in R. Extra credit for doing it on the
    cardiovascular mortality data with enough lagged features — the fitted values on the training set
    should match the observations exactly, and the cross-validated predictions should look wild.

## Sources

- Simple and multiple regression setup, the no-intercept variant, the inverse-regression question,
  the Galton height example, and the two forms of the multiple regression estimator: `01-simple-
  regression.md` (Homework 2, Q1-6), converted from `homeworks/homework2/homework2.Rmd`,
  berkeley-stat153 fall 2024.
- Covariance of linear transformations, the covariance of $\hat\beta$, and the PSD-ordering form of
  the Gauss-Markov theorem: `02-covariance-calculations.md` (Homework 2, Q7-9). Q7 explicitly draws
  on "the lecture from week 2, Measures of dependence and stationarity" for the scalar
  covariance-of-linear-combinations rule; that lecture is not part of the supplied material.
- MAE and MAPE (stated in the homework as "defined in lecture," not reproduced there) and MARE, and
  the worked numerical setup contrasting them: `03-metrics-matter.md` (Homework 2, Q10-11).
- Time series cross-validation with a burn-in set and trailing window, and the overfitting/
  training-MSE result: `04-cross-validation.md` (Homework 2, Q12-17). Q12 refers to "the R code from
  lecture" for time series cross-validation of cardiovascular mortality on lagged particulate levels;
  that code is not part of the supplied material, and the description of the burn-in/trailing-window
  procedure above is reconstructed from the exercise text alone.

All four files are lossless conversions of `homeworks/homework2/homework2.Rmd` from the
berkeley-stat153 fall-2024 course repository, licensed CC BY 4.0.

---

[← 80. Correlation, Random Walks, and Stationarity](80-correlation-random-walks-and-stationarity.md) · [Contents](index.md) · [82. Homework 3 →](82-homework-3.md)
