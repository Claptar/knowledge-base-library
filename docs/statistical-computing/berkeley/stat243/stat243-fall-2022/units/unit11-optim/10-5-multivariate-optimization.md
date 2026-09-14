---
title: 5. Multivariate optimization
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit11-optim.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 5. Multivariate optimization

**Source:** [`units/unit11-optim.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Optimizing as the dimension of the space gets larger becomes
increasingly difficult:

1.  In high dimensions, there are many possible directions to go.

2.  One can end up having to do calculations with large vectors and
    matrices.

3.  Multimodality increasingly becomes a concern (and can be hard to
    detect).

First we'll discuss the idea of profiling to reduce dimensionality and
then we'll talk about various numerical techniques, many of which build
off of Newton's method (using second derivative information). We'll
finish by talking about methods that only use the gradient (and not the
second derivative) and methods that don't use any derivative
information.

## Profiling

A core technique for likelihood optimization is to analytically maximize
over any parameters for which this is possible. Suppose we have two sets
of parameters, $\theta_{1}$ and $\theta_{2}$, and we can analytically
maximize w.r.t $\theta_{2}$. This will give us
$\hat{\theta}_{2}(\theta_{1})$, a function of the remaining parameters
over which analytic maximization is not possible. Plugging in
$\hat{\theta}_{2}(\theta_{1})$ into the objective function (in this case
generally the likelihood or log likelihood) gives us the profile (log)
likelihood solely in terms of the obstinant parameters. For example,
suppose we have the regression likelihood with correlated errors:
$$Y\sim\mathcal{N}(X\beta,\sigma^{2}\Sigma(\rho)),$$ where
$\Sigma(\rho)$ is a correlation matrix that is a function of a
parameter, $\rho$. The maximum w.r.t. $\beta$ is easily seen to be the
GLS estimator
$\hat{\beta}(\rho)=(X^{\top}\Sigma(\rho)^{-1}X)^{-1}X^{\top}\Sigma(\rho)^{-1}Y$.
(In general such a maximum is a function of all of the other parameters,
but conveniently it's only a function of $\rho$ here.) This gives us the
initial profile likelihood
$$\frac{1}{(\sigma^{2})^{n/2}|\Sigma(\rho)|^{1/2}}\exp\left(-\frac{(Y-X\hat{\beta}(\rho))^{-\top}\Sigma(\rho)^{-1}(Y-X\hat{\beta}(\rho))}{2\sigma^{2}}\right).$$
We then notice that the likelihood is maximized w.r.t. $\sigma^{2}$ at
$$\hat{\sigma^{2}}(\rho)=\frac{(Y-X\hat{\beta}(\rho))^{\top}\Sigma(\rho)^{-1}(Y-X\hat{\beta}(\rho))}{n}.$$
This gives us the final profile likelihood,
$$\frac{1}{|\Sigma(\rho)|^{1/2}}\frac{1}{(\hat{\sigma^{2}}(\rho))^{n/2}}\exp(-\frac{1}{2}n),$$
a function of $\rho$ only, for which numerical optimization is much
simpler.

## Newton-Raphson (Newton's method)

For multivariate $x$ we have the Newton-Raphson update
$x_{t+1}=x_{t}-f^{\prime\prime}(x_{t})^{-1}f^{\prime}(x_{t})$, or in our
other notation, $$x_{t+1}=x_{t}-H_{f}(x_{t})^{-1}\nabla f(x_{t}).$$ In
class we'll use demo code (not shown here)
for an example of finding the nonlinear least squares fit to some weight
loss data to fit the model (but note that technically speaking one can
use profiling in this case, so it's not a perfect example):
$$Y_{i}=\beta_{0}+\beta_{1}2^{-t_{i}/\beta_{2}}+\epsilon_{i}.$$

Some of the things we need to worry about with Newton's method in
general about are (1) good starting values, (2) positive definiteness of
the Hessian, and (3) avoiding errors in deriving the derivatives.

A note on the positive definiteness: since the Hessian may not be
positive definite (although it may well be, provided the function is
approximately locally quadratic), one can consider modifying the
Cholesky decomposition of the Hessian to enforce positive definiteness
by adding diagonal elements to $H_{f}$ as necessary.

```r
library(MASS)
head(wtloss)
attach(wtloss)

plot(Days, Weight, ylab = "Weight (kg)")

### Linear fit - not a good model
wtloss.lm <- lm(Weight ~ Days, data = wtloss)
coef(wtloss.lm) # estimates of the intercept and slope
lines(Days, fitted(wtloss.lm), col = "grey")

## we need some starting values
## guess that beta2 approx 100 since the midpoint of Days is near 100

beta2.init = 100
2^(-Days/beta2.init)  ## implicit covariate

plot(2^(-Days/beta2.init), Weight)
tmpMod = lm(Weight ~ I(2^(-Days/beta2.init)))
beta0.init = tmpMod$coef[1]
beta1.init = tmpMod$coef[2]

plot(Days, Weight, ylab = "Weight (kg)")
lines(Days, beta0.init + beta1.init * 2^(-Days/beta2.init), col = 'red')
## not bad; let's go with that

expr = quote((Weight - (beta0 + beta1 * 2^(-Days/beta2)))^2) # objective is sum of this quantity over the observations
## let R do the differentiation of the basic expression for us (since human error in taking derivatives is very common)
## R won't deal with the summation, so we'll have to do that ourselves
deriv(expr, c("beta0", "beta1", "beta2"), function.arg = TRUE)
deriv3(expr, c("beta0", "beta1", "beta2"), function.arg = TRUE) # same as deriv()  with Hessian = TRUE

f =function(betas){
  sum((Weight - (betas[1] + betas[2] * 2^(-Days/betas[3])))^2)
}

## use the basic code based on deriv() and deriv3()
fp = function(betas){
  ## a bit sloppy as I use Days and Weight as global vars here
  beta0 = betas[1]
  beta1 = betas[2]
  beta2 = betas[3]
  .expr3 <- 2^(-Days/beta2)
  .expr6 <- Weight - (beta0 + beta1 * .expr3)
  grad = - c(sum(2*.expr6), sum(2*(.expr3*.expr6)),
             sum(2* (beta1 * (.expr3 * (log(2) * (Days/beta2^2))) * .expr6)))
  return(grad)
}

fpp = function(betas){
  ## a bit sloppy as I use Days and Weight as global vars here
  n = length(Days)
  beta0 = betas[1]
  beta1 = betas[2]
  beta2 = betas[3]
  .expr3 <- 2^(-Days/beta2)
  .expr6 <- Weight - (beta0 + beta1 * .expr3)
  .expr11 <- log(2)
  .expr12 <- beta2^2
  .expr14 <- .expr11 * (Days/.expr12)
  .expr15 <- .expr3 * .expr14
  .expr16 <- beta1 * .expr15

  hessian = matrix(0, 3, 3)
  hessian[1, 1] <- 2*n # don't forget to do summation (i.e., multiply by n)
  hessian[1, 2] <- sum(2 * .expr3)
  hessian[1, 3] <- sum( 2 *  .expr16)
  hessian[2, 2] <- sum( 2 * (.expr3 * .expr3))

  hessian[2, 3] <-  - sum(2 *
                          (.expr15 * .expr6 - .expr3 * .expr16))

  hessian[3, 3] <- - sum(2 * (beta1 * (.expr15 *
                                       .expr14 - .expr3 * (.expr11 * (Days * (2 * beta2)/.expr12^2))) *
                              .expr6 - .expr16 * .expr16))
  hessian[lower.tri(hessian)] = t(hessian[upper.tri(hessian)])
  return(hessian)
}


nIt = 20
xvals = matrix(NA, nr = nIt, nc = 3)
xvals[1, ] = c(beta0.init, beta1.init, beta2.init)


for(t in 2:nIt){
  xvals[t, ] = xvals[t-1, ] - solve(fpp(xvals[t-1, ]), fp(xvals[t-1, ]))
  if(FALSE){ # in case not numerically p.d., use pseudoinverse
    e = eigen(fpp(xvals[t-1, ]))
    e$val = 1/e$val
    e$val[e$val < 0] = 0 # pseudo-inverse
    xvals[t, ] = xvals[t-1, ] - e$vec%*%((t(e$vec)*e$val)%*%fp(xvals[t-1, ]))
  }
}

## let's check against R's built-in nonlinear least squares function
beta.start = xvals[1, ]
names(beta.start) = c("beta0", "beta1", "beta2")
wtloss.fm <- nls(Weight ~ beta0 + beta1*2^(-Days/beta2),
                 data = wtloss, start = beta.start, trace = TRUE)
nlsEst = coef(wtloss.fm)

f(xvals[20, ])
f(nlsEst)

plot(Days, Weight, ylab = "Weight (kg)")
lines(Days, fitted(wtloss.fm), col = "blue")
```

Next we'll see that some optimization methods used commonly for
statistical models (in particular Fisher scoring and iterative
reweighted least squares (IRLS or IWLS) are just Newton-Raphson in
disguise.

## Fisher scoring variant on N-R (optional)

The Fisher information (FI) is the expected value of the outer product
of the gradient of the log-likelihood with itself
$$I(\theta)=E_{f}(\nabla f(y)\nabla f(y)^{\top}),$$ where the expected
value is with respect to the data distribution. Under regularity
conditions (true for exponential families), the expectation of the
Hessian of the log-likelihood is minus the Fisher information,
$E_{f}H_{f}(y)=-I(\theta)$. We get the observed Fisher information by
plugging the data values into either expression instead of taking the
expected value.

Thus, standard N-R can be thought of as using the observed Fisher
information to find the updates. Instead, if we can compute the
expectation, we can use minus the FI in place of the Hessian. The result
is the Fisher scoring (FS) algorithm. Basically instead of using the
Hessian for a given set of data, we are using the FI, which we can think
of as the average Hessian over repeated samples of data from the data
distribution. FS and N-R have the same convergence properties (i.e.,
quadratic convergence) but in a given problem, one may be
computationally or analytically easier. Givens and Hoeting comment that
FS works better for rapid improvements at the beginning of iterations
and N-R better for refinement at the end. $$\begin{aligned}
(NR):\,\theta_{t+1} & = & \theta_{t}-H_{f}(\theta_{t})^{-1}\nabla f(\theta_{t})\\
(FS):\,\theta_{t+1} & = & \theta_{t}+I(\theta_{t})^{-1}\nabla f(\theta_{t})\end{aligned}$$

There is some demo code in the source Rmd file (not shown
here) that one can use to try out Fisher scoring in the weight loss example.

```r
fppFS = function(betas){
  ## a bit sloppy as I use Days and Weight as global vars here
  n = length(Days)
  beta0 = betas[1]
  beta1 = betas[2]
  beta2 = betas[3]
    .expr3 <- 2^(-Days/beta2)
    .expr6 <- 0 # Weight - (beta0 + beta1 * .expr3)
    .expr11 <- log(2)
    .expr12 <- beta2^2
    .expr14 <- .expr11 * (Days/.expr12)
    .expr15 <- .expr3 * .expr14
    .expr16 <- beta1 * .expr15

  hessian = matrix(0, 3, 3)
  hessian[1, 1] <- 2*n # don't forget to do summation (i.e., multiply by n)
    hessian[1, 2] <- sum(2 * .expr3)
    hessian[1, 3] <- sum( 2 *  .expr16)
    hessian[2, 2] <- sum( 2 * (.expr3 * .expr3))

    hessian[2, 3] <-  - sum(2 *
        (.expr15 * .expr6 - .expr3 * .expr16))

    hessian[3, 3] <- - sum(2 * (beta1 * (.expr15 *
        .expr14 - .expr3 * (.expr11 * (Days * (2 * beta2)/.expr12^2))) *
        .expr6 - .expr16 * .expr16))
  hessian[lower.tri(hessian)] = t(hessian[upper.tri(hessian)])
  return(hessian)
}


nIt = 20
xvals = matrix(NA, nr = nIt, nc = 3)
xvals[1, ] = c(beta0.init, beta1.init, beta2.init)

fpp(xvals[1, ])
fppFS(xvals[1, ])
## pretty similar - some terms in the observed FI didn't involve the data, so don't change anyway

for(t in 2:nIt){
  xvals[t, ] = xvals[t-1, ] - solve(fppFS(xvals[t-1, ]), fp(xvals[t-1, ]))
}
```

The Gauss-Newton algorithm for nonlinear least squares involves using
the FI in place of the Hessian in determining a Newton-like step.
`nls()` in R uses this approach. Note that this is not exactly the same
updating as our manual coding of FS for the weight loss example.

#### Connections between statistical uncertainty and ill-conditionedness

When either the observed or expected FI matrix is nearly singular this
means we have a small eigenvalue in the inverse covariance (the
precision), which means a large eigenvalue in the covariance matrix.
This indicates some linear combination of the parameters has low
precision (high variance), and that in that direction the likelihood is
nearly flat. As we've seen with N-R, convergence slows with shallow
gradients, and we may have numerical problems in determining good
optimization steps when the likelihood is sufficiently flat. So
convergence problems and statistical uncertainty go hand in hand. One,
but not the only, example of this occurs when we have nearly collinear
regressors.

## IRLS (IWLS) for Generalized Linear Models (GLMs)

As many of you know, iterative reweighted least squares (also called
iterative weighted least squares) is the standard method for estimation
with GLMs. It involves linearizing the model and using working weights
and working variances and solving a weighted least squares (WLS) problem
(recalling that the generic WLS solution is
$\hat{\beta}=(X^{\top}WX)^{-1}X^{\top}WY$).

Exponential families can be expressed as
$$f(y;\theta,\phi)=\exp((y\theta-b(\theta))/a(\phi)+c(y,\phi)),$$ with
$E(Y)=b^{\prime}(\theta)$ and $\mbox{Var}(Y)=b^{\prime\prime}(\theta)$.
If we have a GLM in the canonical parameterization (log link for Poisson
data, logit for binomial), we have the natural parameter $\theta$ equal
to the linear predictor, $\theta=\eta$. A standard linear predictor
would simply be $\eta=X\beta$.

Considering N-R for a GLM in the canonical parameterization (and
ignoring $a(\phi)$, which is one for logistic and Poisson regression),
one can show that the gradient of the GLM log-likelihood is the inner
product of the covariates and a residual vector,
$\nabla l(\beta)=(Y-E(Y))^{\top}X$, and the Hessian is
$H_{l}(\beta)=-X^{\top}WX$ where $W$ is a diagonal matrix with
$\{\mbox{Var}(Y_{i})\}$ on the diagonal (the working weights). Note that
both $E(Y)$ and the variances in $W$ depend on $\beta$, so these will
change as we iteratively update $\beta$. Therefore, the N-R update is
$$\beta_{t+1}=\beta_{t}+(X^{\top}W_{_{t}}X)^{-1}X^{\top}(Y-E(Y)_{t})$$
where $E(Y)_{t}$ and $W_{t}$ are the values at the current parameter
estimate, $\beta_{t}$ . For example, for logistic regression (here with
$n_{i}=1$), $W_{t,ii}=p_{ti}(1-p_{ti})$ and $E(Y)_{ti}=p_{ti}$ where
$p_{ti}=\frac{\exp(X_{i}^{\top}\beta_{t})}{1+\exp(X_{i}^{\top}\beta_{t})}$.
In the canonical parameterization of a GLM, the Hessian does not depend
on the data, so the observed and expected FI are the same, and therefore
N-R and FS are the same.

The update above can be rewritten in the standard form of IRLS as a WLS
problem, $$\begin{aligned}
\beta_{t+1} & = \beta_{t}+(X^{\top}W_{_{t}}X)^{-1}X^{\top}(Y-E(Y)_{t})\\
 & = (X^{\top}W_{_{t}}X)^{-1}(X^{\top}W_{_{t}}X)\beta_{t}+(X^{\top}W_{_{t}}X)^{-1}X^{\top}(Y-E(Y)_{t})\\
 & = (X^{\top}W_{_{t}}X)^{-1}X^{\top}W_{t}\left[X\beta_{t}+W_{t}^{-1}(Y-E(Y)_{t})\right]\\
 & = (X^{\top}W_{_{t}}X)^{-1}X^{\top}W_{t}\tilde{Y}_{t},\end{aligned}$$
where the so-called working observations are
$\tilde{Y}_{t}=X\beta_{t}+W_{t}^{-1}(Y-E(Y)_{t})$. Note that these are
on the scale of the linear predictor. The interpretation is that the
working observations are equal to the current fitted values,
$X\beta_{t}$, plus weighted residuals where the weight (the inverse of
the variance) takes the actual residuals and scales to the scale of the
linear predictor.

While IRLS is standard for GLMs, you can also use general purpose
optimization routines.

IRLS is a special case of the general Gauss-Newton method for nonlinear
least squares.

## Descent methods and Newton-like methods

More generally a Newton-like method has updates of the form
$$x_{t+1}=x_{t}-\alpha_{t}M_{t}^{-1}f^{\prime}(x_{t}).$$ We can choose
$M_{t}$ in various ways, including as an approximation to the second
derivative.

This opens up several possibilities:

1.  using more computationally efficient approximations to the second
    derivative,

2.  avoiding steps that do not go in the correct direction (i.e., go
    uphill when minimizing), and

3.  scaling by $\alpha_{t}$ so as not to step too far.

Let's consider a variety of strategies.

### Descent methods

The basic strategy is to choose a good direction and then choose the
longest step for which the function continues to decrease. Suppose we
have a direction, $p_{t}$. Then we need to move
$x_{t+1}=x_{t}+\alpha_{t}p_{t}$, where $\alpha_{t}$ is a scalar,
choosing a good $\alpha_{t}$. We might use a line search (e.g.,
bisection or golden section search) to find the local minimum of
$f(x_{t}+\alpha_{t}p_{t})$ with respect to $\alpha_{t}$. However, we
often would not want to run to convergence, since we'll be taking
additional steps anyway.

Steepest descent chooses the direction as the steepest direction
downhill, setting $M_{t}=I$, since the gradient gives the steepest
direction uphill (the negative sign in the equation below has us move
directly downhill rather than directly uphill). Given the direction, we
want to scale the step $$x_{t+1}=x_{t}-\alpha_{t}f^{\prime}(x_{t})$$
where the contraction, or step length, parameter $\alpha_{t}$ is chosen
sufficiently small to ensure that we descend, via some sort of line
search. The critical downside to steepest descent is that when the
contours are elliptical, it tends to zigzag; here's an example.

(Note that I do a full line search (using the golden section method via
*optimize()*) at each step in the direction of steepest descent - this
is generally computationally wasteful, but I just want to illustrate how
steepest descent can go wrong, even if you go the "right" amount in each
direction.)

```r
par(mai = c(.5,.4,.1,.4))
f <- function(x){
	x[1]^2/1000 + 4*x[1]*x[2]/1000 + 5*x[2]^2/1000
}
fp <- function(x){
	c(2 * x[1]/1000 + 4 * x[2]/1000,
	4 * x[1]/1000 + 10 * x[2]/1000)
}
lineSearch <- function(alpha, xCurrent, direction, FUN){
	newx <- xCurrent + alpha * direction
	FUN(newx)
}
nIt <- 50
xvals <- matrix(NA, nr = nIt, nc = 2)
xvals[1, ] <- c(7, -4)
for(t in 2:50){
	newalpha <- optimize(lineSearch, interval = c(-5000, 5000),
		xCurrent = xvals[t-1, ], direction = fp(xvals[t-1, ]),
		FUN = f)$minimum
	xvals[t, ] <- xvals[t-1, ] + newalpha * fp(xvals[t-1, ])
}
x1s <- seq(-5, 8, len = 100); x2s = seq(-5, 2, len = 100)
fx <- apply(expand.grid(x1s, x2s), 1, f)
## plot f(x) surface on log scale
fields::image.plot(x1s, x2s, matrix(log(fx), 100, 100),
	xlim = c(-5, 8), ylim = c(-5,2))
lines(xvals) ## overlay optimization path
```

If the contours are circular, steepest descent works well. Newton's
method deforms elliptical contours based on the Hessian. Another way to
think about this is that steepest descent does not take account of the
rate of change in the gradient, while Newton's method does.

The general descent algorithm is
$$x_{t+1}=x_{t}-\alpha_{t}M_{t}^{-1}f'(x_{t}),$$ where $M_{t}$ is
generally chose to approximate the Hessian and $\alpha_{t}$ allows us to
adjust the step in a smart way. Basically, since the negative gradient
tells us the direction that descends (at least within a small
neighborhood), if we don't go too far, we should be fine and should work
our way downhill. One can work this out formally using a Taylor
approximation to $f(x_{t+1})-f(x_{t})$ and see that we make use of
$M_{t}$ being positive definite. (Unfortunately backtracking with
positive definite $M_{t}$ does not give a theoretical guarantee that the
method will converge. We also need to make sure that the steps descend
sufficiently quickly and that the algorithm does not step along a level
contour of $f$.)

The conjugate gradient algorithm for iteratively solving large systems
of equations is all about choosing the direction and the step size in a
smart way given the optimization problem at hand.

### Quasi-Newton methods such as BFGS

Other replacements for the Hessian matrix include estimates that do not
vary with $t$ and finite difference approximations. When calculating the
Hessian is expensive, it can be very helpful to substitute an
approximation.

A basic finite difference approximation requires us to compute finite
differences in each dimension, but this could be computationally
burdensome. A more efficient strategy for choosing $M_{t+1}$ is to (1)
make use of $M_{t}$ and (2) make use of the most recent step to learn
about the curvature of $f^{\prime}(x)$ in the direction of travel. One
approach is to use a rank one update to $M_{t}$.

A basic strategy is to choose $M_{t+1}$ such that the secant condition
is satisfied:
$$M_{t+1}(x_{t+1}-x_{t})=\nabla f(x_{t+1})-\nabla f(x_{t}),$$ which is
motivated by the fact that the secant approximates the gradient in the
direction of travel. Basically this says to modify $M_{t}$ in such a way
that we incorporate what we've learned about the gradient from the most
recent step. $M_{t+1}$ is not fully determined based on this, and we
generally impose other conditions, in particular that $M_{t+1}$ is
symmetric and positive definite. Defining $s_{t}=x_{t+1}-x_{t}$ and
$y_{t}=\nabla f(x_{t+1})-\nabla f(x_{t})$, the unique, symmetric rank
one update (why is the following a rank one update?) that satisfies the
secant condition is
$$M_{t+1}=M_{t}+\frac{(y_{t}-M_{t}s_{t})(y_{t}-M_{t}s_{t})^{\top}}{(y_{t}-M_{t}s_{t})^{\top}s_{t}}.$$
If the denominator is positive, $M_{t+1}$ may not be positive definite,
but this is guaranteed for non-positive values of the denominator. One
can also show that one can achieve positive definiteness by shrinking
the denominator toward zero sufficiently.

A standard approach to updating $M_{t}$ is a commonly-used rank two
update that generally results in $M_{t+1}$ being positive definite is
$$M_{t+1}=M_{t}-\frac{M_{t}s_{t}(M_{t}s_{t})^{\top}}{s_{t}^{\top}M_{t}s_{t}}+\frac{y_{t}y_{t}^{\top}}{s_{t}^{\top}y_{t}},$$
which is known as the Broyden-Fletcher-Goldfarb-Shanno (BFGS) update.
This is one of the methods used in R in *optim()*.

Question: how can we update $M_{t}^{-1}$ to $M_{t+1}^{-1}$ efficiently?
It turns out there is a way to update the Cholesky of $M_{t}$
efficiently and this is a better approach than updating the inverse.

The order of convergence of quasi-Newton methods is generally slower
than the quadratic convergence of N-R because of the approximations but
still faster than linear. In general, quasi-Newton methods will do much
better if the scales of the elements of $x$ are similar. Lange suggests
using a starting point for which one can compute the expected
information, to provide a good starting value $M_{0}$.

Note that for estimating a covariance based on the numerical information
matrix, we would not want to rely on $M_{t}$ from the final iteration,
as the approximation may be poor. Rather we would spend the effort to
better estimate the Hessian directly at $x^{*}$.

### Stochastic gradient descent

Stochastic gradient descent (SGD) is the hot method in machine learning,
commonly used for fitting deep neural networks. It allows you to
optimize an objective function with respect to what is often a very
large number of parameters even when the data size is huge.

Gradient descent is a simplification of Newton's method that does not
rely on the second derivative, but rather chooses the direction using
the gradient and then a step size, $\alpha_{t}$:
$$x_{t+1}=x_{t}-\alpha_{t}f^{\prime}(x_{t})$$

The basic idea of stochastic gradient descent is to replace the gradient
with a function whose expected value is the gradient,
$E(g(x_{t}))=f^{\prime}(x_{t})$: $$x_{t+1}=x_{t}-\alpha_{t}g(x_{t})$$
Thus on average we should go in a good (downhill) direction. Given that
we know that strictly following the gradient can lead to slow
convergence, it makes some intuitive sense that we could still do ok
without using the exact gradient. One can show formally that SGD will
converge for convex functions.

SGD can be used in various contexts, but the common one we will focus on
is when $$\begin{aligned}
f(x) & = \sum_{i=1}^{n}f_{i}(x)\\
f^{\prime}(x) & = \sum_{i=1}^{n}f^{\prime}_{i}(x)\end{aligned}$$ for
large $n$. Thus calculation of the gradient is $O(n)$, and we may not
want to incur that computational cost. How could we implement SGD in
such a case? At each iteration we could randomly choose an observation
and compute the contribution to the gradient from that data point, or we
could choose a random subset of the data (this is *mini-batch SGD*), or
there are variations where we systematically cycle through the
observations or cycle through subsets. However, in some situations,
convergence is actually much faster when using randomness. And if the
data are ordered in some meaningful way we definitely do not want to
cycle through the observations in that order, as this can result in a
biased estimate of the gradient and slow convergence. So one generally
randomly shuffles the data before starting SGD. Note that using subsets
rather than individual observations is likely to be more effective as it
can allow us to use optimized matrix/vector computations.

How should one choose the step size, $\alpha_{t}$ (also called the
learning rate)? One might think that as one gets close to the optimum,
if one isn't careful, one might simply bounce around near the optimum in
a random way, without actually converging to the optimum. So intuition
suggests that $\alpha_{t}$ should decrease with $t$. Some choices of
step size have included:

-   $\alpha_{t}=1/t$
-   set a schedule, such that for $T$ iterations, $\alpha_{t}=\alpha$,
    then for the next $T$, $\alpha_{t}=\alpha\gamma$, then for the next
    $T$, $\alpha_{t}=\alpha\gamma^{2}$. A heuristic is for
    $\gamma\in(0.8,0.9)$.
-   run with $\alpha_{t}=\alpha$ for $T$ iterations, then with
    $\alpha_{t}=\alpha/2$ for $2T$, then with $\alpha_{t}=\alpha/4$ for
    $4T$ and so forth.

## Coordinate descent (Gauss-Seidel)

Gauss-Seidel is also known a back-fitting or cyclic coordinate descent.
The basic idea is to work element by element rather than having to
choose a direction for each step. For example backfitting used to be
used to fit generalized additive models of the form
$E(Y)=f_{1}(z_{1})+f_{2}(z_{2})+\ldots+f_{p}(z_{p})$.

The basic strategy is to consider the $j$th component of $f^{\prime}(x)$
as a univariate function of $x_{j}$ only and find the root, $x_{j,t+1}$
that gives $f^{\prime}_{j}(x_{j,t+1})=0$. One cycles through each
element of $x$ to complete a single cycle and then iterates. The appeal
is that univariate root-finding/minimization is easy, often more stable
than multivariate, and quick.

However, Gauss-Seidel can zigzag, since you only take steps in one
dimension at a time, as we see here.

```r
f <- function(x){
	return(x[1]^2/1000 + 4*x[1]*x[2]/1000 + 5*x[2]^2/1000)
}
f1 <- function(x1, x2){ # f(x) as a function of x1
	return(x1^2/1000 + 4*x1*x2/1000 + 5*x2^2/1000)
}
f2 <- function(x2, x1){ # f(x) as a function of x2
	return(x1^2/1000 + 4*x1*x2/1000 + 5*x2^2/1000)
}
x1s <- seq(-5, 8, len = 100); x2s = seq(-5, 2, len = 100)
fx <- apply(expand.grid(x1s, x2s), 1, f)
fields::image.plot(x1s, x2s, matrix(log(fx), 100, 100))
nIt <- 49
xvals <- matrix(NA, nr = nIt, nc = 2)
xvals[1, ] <- c(7, -4)
## 5, -10
for(t in seq(2, nIt, by = 2)){
    ## Note that full optimization along each axis is unnecessarily
    ## expensive (since we are going to just take another step in the next
    ## iteration. Just using for demonstration here.
	newx1 <- optimize(f1, x2 = xvals[t-1, 2], interval = c(-40, 40))$minimum
	xvals[t, ] <- c(newx1, xvals[t-1, 2])
	newx2 <- optimize(f2, x1 = newx1, interval = c(-40, 40))$minimum
	xvals[t+1, ] <- c(newx1, newx2)
}
lines(xvals)
```


In the notes for Unit 9 on linear algebra, I discussed the use of
Gauss-Seidel to iteratively solve $Ax=b$ in situations where factorizing
$A$ (which of course is $O(n^{3})$) is too computationally expensive.

#### The lasso

The *lasso* uses an L1 penalty in regression and related contexts. A
standard formulation for the lasso in regression is to minimize
$$\|Y-X\beta\|_{2}^{2}+\lambda\sum_{j}|\beta_{j}|$$ to find
$\hat{\beta}(\lambda)$ for a given value of the penalty parameter,
$\lambda$. A standard strategy to solve this problem is to use
coordinate descent, either cyclically, or by using directional
derivatives to choose the coordinate likely to decrease the objective
function the most (a greedy strategy). We need to use directional
derivatives because the penalty function is not differentiable, but does
have directional derivatives in each direction. The directional
derivative of the objective function for $\beta_{j}$ is
$$-2\sum_{i}x_{ij}(Y_{i}-X_{i}^{\top}\beta)\pm\lambda$$ where we add
$\lambda$ if $\beta_{j}\geq0$ and you subtract $\lambda$ if
$\beta_{j}<0$. If $\beta_{j,t}$ is 0, then a step in either direction
contributes $+\lambda$ to the derivative as the contribution of the
penalty.

Once we have chosen a coordinate, we set the directional derivative to
zero and solve for $\beta_{j}$ to obtain $\beta_{j,t+1}$.

The `glmnet` package in R (described in [this Journal of Statistical
Software paper](http://www.jstatsoft.org/article/view/v033i01))
implements such optimization for a variety of penalties in linear model
and GLM settings, including the lasso. This [Mittal et al.
paper](http://biostatistics.oxfordjournals.org/content/early/2013/10/04/biostatistics.kxt043.short)
describes similar optimization for survival analysis with very large
$p$, exploiting sparsity in the $X$ matrix for computational efficiency;
note that they do not use Newton-Raphson because the matrix operations
are infeasible computationally.

One nice idea that is used in lasso and related settings is the idea of
finding the regression coefficients for a variety of values of
$\lambda$, combined with "warm starts". A general approach is to start
with a large value of $\lambda$ for which all the coefficients are zero
and then decrease $\lambda$. At each new value of $\lambda$, use the
estimated coefficients from the previous value as the starting values.
This should allow for fast convergence and gives what is called the
"solution path". Often $\lambda$ is chosen based on cross-validation.

The LARS (least angle regression) algorithm uses a similar strategy that
allows one to compute $\hat{\beta}_{\lambda}$ for all values of
$\lambda$ at once.

The lasso can also be formulated as the constrained minimization of
$\|Y-X\beta\|_{2}^{2}$ s.t. $\sum_{j}|\beta_{j}|\leq c$, with $c$ now
playing the role of the penalty parameter. Solving this minimization
problem would take us in the direction of quadratic programming, a
special case of convex programming, discussed in Section 9.

## Nelder-Mead

This approach avoids using derivatives or approximations to derivatives.
This makes it robust, but also slower than Newton-like methods. The
basic strategy is to use a simplex, a polytope of $p+1$ points in $p$
dimensions (e.g., a triangle when searching in two dimensions,
tetrahedron in three dimensions\...) to explore the space, choosing to
shift, expand, or contract the polytope based on the evaluation of $f$
at the points.

The algorithm relies on four tuning factors: a reflection factor,
$\alpha>0$; an expansion factor, $\gamma>1$; a contraction factor,
$0<\beta<1$; and a shrinkage factor, $0<\delta<1$. First one chooses an
initial simplex: $p+1$ points that serve as the vertices of a convex
hull.

1.  Evaluate and order the points, $x_{1},\ldots,x_{p+1}$ based on
    $f(x_{1})\leq\ldots\leq f(x_{p+1})$. Let $\bar{x}$ be the average of
    the first $p$ $x$'s.

2.  (Reflection) Reflect $x_{p+1}$ across the hyperplane (a line when
    $p+1=3$) formed by the other points to get $x_{r}$, based on
    $\alpha$.

    -   $x_{r}=(1+\alpha)\bar{x}-\alpha x_{p+1}$

3.  If $f(x_{r})$ is between the best and worst of the other points, the
    iteration is done, with $x_{r}$ replacing $x_{p+1}$. We've found a
    good direction to move.

4.  (Expansion) If $f(x_{r})$ is better than all of the other points,
    expand by extending $x_{r}$ to $x_{e}$ based on $\gamma$, because
    this indicates the optimum may be further in the direction of
    reflection. If $f(x_{e})$ is better than $f(x_{r})$, use $x_{e}$ in
    place of $x_{p+1}$. If not, use $x_{r}$. The iteration is done.

    -   $x_{e}=\gamma x_{r}+(1-\gamma)\bar{x}$

5.  If $f(x_{r})$ is worse than all the other points, but better than
    $f(x_{p+1})$, let $x_{h}=x_{r}$. Otherwise $f(x_{r})$ is worse than
    $f(x_{p+1})$ so let $x_{h}=x_{p+1}$. In either case, we want to
    concentrate our polytope toward the other points.

    a.  (Contraction) Contract $x_{h}$ toward the hyperplane formed by
        the other points, based on $\beta$, to get $x_{c}$. If the
        result improves upon $f(x_{h})$ replace $x_{p+1}$ with $x_{c}$.
        Basically, we haven't found a new point that is better than the
        other points, so we want to contract the simplex away from the
        bad point.

        -   $x_{c}=\beta x_{h}+(1-\beta)\bar{x}$

    b.  (Shrinkage) Otherwise (if $x_{c}$ is not better than $x_{h}$),
        replace $x_{p+1}$ with $x_{h}$ and shrink the simplex toward
        $x_{1}$. Basically this suggests our step sizes are too large
        and we should shrink the simplex, shrinking towards the best
        point.

        -   $x_{i}=\delta x_{i}+(1-\delta)x_{1}$ for $i=2,\ldots,p+1$

Convergence is assessed based on the sample variance of the function
values at the points, the total of the norms of the differences between
the points in the new and old simplexes, or the size of the simplex. In
class we'll work through some demo code (not shown here) that
illustrates the individual steps in an iteration of Nelder-Mead.

```r
## set up tuning factors
alpha = 1
gamma = 2
beta = .5
delta = .5

## auxiliary function to plot line segments
plotseg = function(ind1, ind2, col = 1){
  if(length(ind1) == 1){
    segments(xs[ind1, 1], xs[ind1 , 2], xs[ind2, 1], xs[ind2, 2], col = col)
  } else{
    segments(ind1[1], ind1[2], xs[ind2, 1], xs[ind2, 2], col = col)
  }
}

## initial polytope
xs = matrix(c(-2,3,-6,4,-4,2),nc=2,byrow=T)

plot(xs,xlim=c(-7,-1),ylim=c(1,8))
plotseg(2, 3)
plotseg(1, 3)
plotseg(1, 2)

xbar = (xs[1,]+xs[2,])/2

text(xs[3,1], xs[3,2], expression(x[p+1]))

points(xbar[1],xbar[2], col = 'red')

### reflection

xr = (1+alpha)*xbar - alpha*xs[3,]
points(xr[1],xr[2],col = 'red', pch = 16, cex = .4)
text(xr[1],xr[2], expression(x[r]))

plotseg(xr, 1, col = 'red')
plotseg(xr, 2, col = 'red')
plotseg(1, 2, col = 'red')
## red triangle is now our proposed new polytope

### consider expansion if xr is better than all the other points

xe = gamma*xr + (1-gamma)*xbar
points(xe[1], xe[2], col = 'green', pch = 16, cex = .4)
text(xe[1],xe[2], expression(x[e]))
## if xe is better than xr, use xe, o.w. use xr

plotseg(xe, 1, col = 'green')
plotseg(xe, 2, col = 'green')
plotseg(1, 2, col = 'green')

### consider contraction if xr is worse than x_1,...,x_p

## suppose xr is worse than x_p+1
## set xh = x_p+1

points(xs[3,1], xs[3, 2], col = 'blue')

## set xh to be the best of these two points
xh = xs[3, ] # suppose the original point is better than the reflection
xc = beta*xh + (1-beta)*xbar
points(xc[1], xc[2], col = 'blue', pch = 16, cex = .4)
text(xc[1],xc[2], expression(x[c]))
## if xc is better than xh, then contract

plotseg(xc, 1, col = 'blue')
plotseg(xc, 2, col = 'blue')
plotseg(1, 2, col = 'blue')

## if not, shrink simplex toward the best point (xs[1, ])

### shrinkage

xs[2, ] = delta*xs[2, ] + (1-delta)*xs[1, ]
xs[3, ] = delta*xs[3, ] + (1-delta)*xs[1, ]

points(xs[2, 1], xs[2, 2], col = 'purple')
points(xs[3, 1], xs[3, 2], col = 'purple')

plotseg(1, 2, 'purple')
plotseg(1, 3, 'purple')
plotseg(2, 3, 'purple')

### if xr was better than x_p+1 then
## set xh = xr and do the contraction and shrinkage similarly to the above
```

We can see the points at which the function was evaluated in the same
quadratic example we saw in previous sections. The left hand panel shows
the steps from a starting point somewhat far from the optimum, with the
first 9 points numbered. In this case, we start with points 1, 2, and 3.
Point 4 is a reflection. At this point, it looks like point 5 is a
contraction but that doesn't exactly follow the algorithm above (since
Point 4 is between Points 2 and 3 so the iteration should end without a
contraction), so perhaps the algorithm as implemented is a bit different
than as described above. In any event, the new set is (2, 3, 4). Then
point 6 and point 7 are reflection and expansion steps and the new set
is (3, 4, 6). Points 8 and 9 are again reflection and expansion steps.
The right hand panel shows the steps from a starting point near
(actually at) the optimum. Points 4 and 5 are reflection and expansion
steps, with the next set being (1, 2, 5). Now step 6 is a reflection but
it is the worst of all the points, so point 7 is a contraction of point
2 giving the next set (1, 5, 7). Point 8 is then a reflection and point
9 is a contraction of point 5.


```r
f <- function(x, plot = TRUE, verbose = FALSE) {
    result <- x[1]^2/1000 + 4*x[1]*x[2]/1000 + 5*x[2]^2/1000
    if(verbose) print(result)
    if(plot && cnt < 10) {
        points(x[1], x[2], pch = as.character(cnt))
        if(cnt < 10) cnt <<- cnt + 1 else cnt <<- 1
        if(interactive())
            invisible(readline(prompt = "Press <Enter> to continue..."))
    } else if(plot) points(x[1], x[2])
    return(result)
}

par(mfrow = c(1,2), mgp = c(1.8,.7,0), mai = c(.5,.45,.1,.5), cex = 0.7)

x1s <- seq(-5, 10, len = 100); x2s = seq(-5, 2, len = 100)
fx <- apply(expand.grid(x1s, x2s), 1, f, FALSE)
cnt <- 1
fields::image.plot(x1s, x2s, matrix(log(fx), 100, 100))
init <- c(7, -4)
optim(init, f, method = "Nelder-Mead", verbose = FALSE)

par(cex = 0.7)
x1s <- seq(-.2, .2, len = 100); x2s = seq(-.12, .12, len = 100)
fx <- apply(expand.grid(x1s, x2s), 1, f, FALSE)
cnt <- 1
fields::image.plot(x1s, x2s, matrix(log(fx), 100, 100))
init <- c(-0, 0)
optim(init, f, method = "Nelder-Mead", verbose = FALSE)
```

Here's an [online graphical
illustration](http://www.benfrederickson.com/numerical-optimization/) of
Nelder-Mead.

This is the default in `optim()` in R, however it is relatively slow, so
you may want to try one of the alternatives, such as BFGS.

## Simulated annealing (SA) (optional)

Simulated annealing is a *stochastic* descent algorithm, unlike the
deterministic algorithms we've already discussed. It has a couple
critical features that set it aside from other approaches. First, uphill
moves are allowed; second, whether a move is accepted is stochastic, and
finally, as the iterations proceed the algorithm becomes less likely to
accept uphill moves.

Assume we are minimizing a negative log likelihood as a function of
$\theta$, $f(\theta)$.

The basic idea of simulated annealing is that one modifies the objective
function, $f$ in this case, to make it less peaked at the beginning,
using a "temperature" variable that changes over time. This helps to
allow moves away from local minima, when combined with the ability to
move uphill. The name comes from an analogy to heating up a solid to its
melting temperature and cooling it slowly - as it cools the atoms go
through rearrangements and slowly freeze into the crystal configuration
that is at the lowest energy level.

Here's the algorithm. We divide up iterations into stages,
$j=1,2,\ldots$ in which the temperature variable, $\tau_{j}$, is
constant. Like MCMC, we require a proposal distribution to propose new
values of $\theta$.

1.  Propose to move from $\theta_{t}$ to $\tilde{\theta}$ from a
    proposal density, $g_{t}(\cdot|\theta_{t})$, such as a normal
    distribution centered at $\theta_{t}$.

2.  Accept $\tilde{\theta}$ as $\theta_{t+1}$ according to the
    probability
    $\min(1,\exp((f(\theta_{t})-f(\tilde{\theta}))/\tau_{j})$ - i.e.,
    accept if a uniform random deviate is less than that probability.
    Otherwise set $\theta_{t+1}=\theta_{t}$. Notice that for larger
    values of $\tau_{j}$ the differences between the function values at
    the two locations are reduced (just like a large standard deviation
    spreads out a distribution). So the exponentiation smooths out the
    objective function when $\tau_{j}$ is large.

3.  Repeat steps 1 and 2 $m_{j}$ times.

4.  Increment the temperature and cooling schedule:
    $\tau_{j}=\alpha(\tau_{j-1})$ and $m_{j}=\beta(m_{j-1})$. Back to
    step 1.

The temperature should slowly decrease to 0 while the number of
iterations, $m_{j}$, should be large. Choosing these 'schedules' is at
the core of implementing SA. Note that we always accept downhill moves
in step 2 but we sometimes accept uphill moves as well.

For each temperature, SA produces an MCMC based on the Metropolis
algorithm. So if $m_{j}$ is long enough, we should sample from the
stationary distribution of the Markov chain,
$\exp(-f(\theta)/\tau_{j}))$. Provided we can move between local minima,
the chain should gravitate toward the global minima because these are
increasingly deep (low values) relative to the local minima as the
temperature drops. Then as the temperature cools, $\theta_{t}$ should
get trapped in an increasingly deep well centered on the global minimum.
There is a danger that we will get trapped in a local minimum and not be
able to get out as the temperature drops, so the temperature schedule is
quite important in trying to avoid this.

A wide variety of schedules have been tried. One approach is to set
$m_{j}=1\forall j$ and
$\alpha(\tau_{j-1})=\frac{\tau_{j-1}}{1+a\tau_{j-1}}$ for a small $a$.
For a given problem it can take a lot of experimentation to choose
$\tau_{0}$ and $m_{0}$ and the values for the scheduling functions. For
the initial temperature, it's a good idea to choose it large enough that
$\exp((f(\theta_{i})-f(\theta_{j}))/\tau_{0})\approx1$ for any pair
$\{\theta_{i},\theta_{j}\}$ in the domain, so that the algorithm can
visit the entire space initially.

Simulated annealing can converge slowly. Multiple random starting points
or stratified starting points can be helpful for finding a global
minimum. However, given the slow convergence, these can also be
computationally burdensome.

---

[← 4. Convergence ideas](09-4-convergence-ideas.md) · [Up: contents](index.md) · [6. Basic optimization in R →](11-6-basic-optimization-in-r.md)
