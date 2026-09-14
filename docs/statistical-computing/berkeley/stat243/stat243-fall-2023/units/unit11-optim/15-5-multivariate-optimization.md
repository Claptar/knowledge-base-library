---
title: 5. Multivariate optimization
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 5. Multivariate optimization

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

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
other notation, $$x_{t+1}=x_{t}-H_{f}(x_{t})^{-1}\nabla f(x_{t}).$$

Let's consider a very simple example of nonlinear least squares.
We'll use the famous Mauna Loa atmospheric carbon dioxide record.

Let's suppose (I have no real reason to think this) that we
think that the data can be well-represented by this nonlinear model:
$$Y_{i}=\beta_{0}+\beta_{1}\exp(t_i/\beta_{2})+\epsilon_{i}.$$

Some of the things we need to worry about with Newton's method in
general about are (1) good starting values, (2) positive definiteness of
the Hessian, and (3) avoiding errors in deriving the derivatives.

A note on the positive definiteness: since the Hessian may not be
positive definite (although it may well be, provided the function is
approximately locally quadratic), one can consider modifying the
Cholesky decomposition of the Hessian to enforce positive definiteness
by adding diagonal elements to $H_{f}$ as necessary.

```python
import os
import pandas as pd
import statsmodels.api as sm
data = pd.read_csv(os.path.join('..','data', 'co2_annmean_mlo.csv'),
    header = 0, names = ['year','co2','unc'])

plt.scatter(data.year, data.co2)
plt.xlabel('year')
plt.ylabel("CO2")
plt.show()

## Center years for better numerical behavior
data.year = data.year - np.mean(data.year)
### Linear fit - not a good model
X = sm.add_constant(data.year)
model = sm.OLS(data.co2, X).fit()

plt.scatter(data.year, data.co2)
plt.plot(data.year, model.fittedvalues, '-')

plt.show()
```

We need some starting values. Having centered the year variable,
$\beta_2$ seems plausibly like it would be order of magnitude of 10,
which is about the magnitude of the year values.

```python
beta2_init = 10
implicit_covar = np.exp(data.year/beta2_init)

X = sm.add_constant(implicit_covar)
model = sm.OLS(data.co2, X).fit()
beta0_init, beta1_init = model.params

plt.scatter(data.year, data.co2)

def fit(params):
    return params[0] + params[1] * np.exp(data.year / params[2])

beta = (beta0_init, beta1_init, beta2_init)
plt.plot(data.year, fit(beta), '-')
plt.show()
```

That's not great. How about changing the scale of beta2 more?

```python
beta2_init = 100
implicit_covar = np.exp(data.year/beta2_init)

X = sm.add_constant(implicit_covar)
model = sm.OLS(data.co2, X).fit()
beta0_init, beta1_init = model.params

plt.scatter(data.year, data.co2)
beta = (beta0_init, beta1_init, beta2_init)
plt.plot(data.year, fit(beta), '-')

plt.show()
```


Let's get derivative information using automatic differentation
(the algorithmic implementation of the chain rule for derivatives also
used in gradient descent in deep learning, as well as various other contexts).
We'll use Jax, but PyTorch or Tensorflow are other options.
We need to use the Jax versions of various numpy operations in order
to be able to get the derivatives.

```python
import jax.numpy as jnp
import jax

def loss(params):
    fitted = params[0] + params[1]*jnp.exp(jnp.array(data.year)/params[2])
    return jnp.sum((fitted - jnp.array(data.co2))**2.0)

deriv1 = jax.grad(loss)
deriv2 = jax.hessian(loss)

deriv1(jnp.array([beta0_init, beta1_init, beta2_init]))
hess = deriv2(jnp.array([beta0_init, beta1_init, beta2_init]))
hess

np.linalg.eig(hess)[0]
```

The Hessian is not positive definite. We could try tricks such
as adding to the diagonal of the Hessian or using the pseudo-inverse
(i.e., setting all negative eigenvalues in the inverse to zero).

Instead, let's try a bit more to find starting values where
the Hessian is positive definite. The order of magnitude of
our initial value for $\beta_2$ seems about right, so let's
try halving or doubling it.

```python
beta2_init = 50
implicit_covar = np.exp(data.year/beta2_init)

X = sm.add_constant(implicit_covar)
model = sm.OLS(data.co2, X).fit()
beta0_init, beta1_init = model.params

hess = deriv2(jnp.array([beta0_init, beta1_init, beta2_init]))

np.linalg.eig(hess)[0]
```

That seems better. Let's try with that.

```python
#| error: true
n_it = 10
xvals = np.zeros(shape = (n_it, 3))
xvals[0, :] = (beta0_init, beta1_init, beta2_init)

for t in range(1, n_it):
  jxvals = jnp.array(xvals[t-1, :])
  hess = deriv2(jxvals)
  e = np.linalg.eig(hess)
  if(np.any(e[0] < 0)):
    raise ValueError("not positive definite")
  xvals[t, :] = xvals[t-1, :] - np.linalg.solve(hess, deriv1(jxvals))
  print(loss(xvals[t,:]))

beta_hat = xvals[t,:]

plt.scatter(data.year, data.co2)
plt.plot(data.year, fit(beta_hat), 'r-')

plt.show()
```

That looks pretty good, but the lack of positive definiteness/sensitivity to starting values should make us
cautious. That said, in this case we can visually
assess the fit and see that it looks pretty good.

Next we'll see that some optimization methods used commonly for
statistical models (in particular Fisher scoring and iterative
reweighted least squares (IRLS or IWLS) are just Newton-Raphson in
disguise.

## Fisher scoring variant on N-R (optional)

The Fisher information (FI) is the expected value of the outer product
of the gradient of the log-likelihood with itself

$$I(\theta)=E_{f}(\nabla f(y)\nabla f(y)^{\top}),$$

where the expected value is with respect to the data distribution. Under regularity
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


The Gauss-Newton algorithm for nonlinear least squares involves using
the FI in place of the Hessian in determining a Newton-like step.
`nls()` in R uses this approach.

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

My original code for this was in R, so I'm just leaving it that way
rather than having to do a lot of fine-tuning to get the image to display
the way I want in Python.

(Note that I do a full line search (using the golden section method via
`optimize()`) at each step in the direction of steepest descent - this
is generally computationally wasteful, but I just want to illustrate how
steepest descent can go wrong, even if you go the "right" amount in each
direction.)


```
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

![Path of steepest descent](https://raw.githubusercontent.com/berkeley-stat243/stat243-fall-2023/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/steep-descent.png)

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

One thing to note is that often one would scale the objective function
(and therefore the gradient) by dividing by the number of observations.
This of course doesn't change the
optimum or the directions involved, but it does mean that the magnitude
of the estimated gradient won't change with the batch size. And it means
that the expected gradient is equal to the true gradient, rather than a scaled version
of the true gradient.


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
dimension at a time, as we see here. (Again the code is in R.)

```
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

![Coordinate descent](https://raw.githubusercontent.com/berkeley-stat243/stat243-fall-2023/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/gauss-seidel.png)

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
class we'll work through some demo code (click below to show the code in the html version of this document) that
illustrates the individual steps in an iteration of Nelder-Mead.

```python
#| code-fold: True
#| eval: False

alpha = 1
gamma = 2
beta = 0.5
delta = 0.5

---

[← Define the second derivative](14-define-the-second-derivative.md) · [Up: contents](index.md) · [Auxiliary function to plot line segments →](16-auxiliary-function-to-plot-line-segments.md)
