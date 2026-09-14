---
title: 6. Basic optimization in R
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit11-optim.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 6. Basic optimization in R

**Source:** [`units/unit11-optim.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Core optimization functions

R has several optimization functions.

-   `optimize()` is good for 1-d optimization: "The method used is a
    combination of golden section search and successive parabolic
    interpolation, and was designed for use with continuous functions."

-   Another option is `uniroot()` for finding the zero of a function,
    which you can use to minimize a function if you can compute the
    derivative.

-   For more than one variable, `optim()` provides a variety of optimization
    methods including the robust Nelder-Mead method, the BFGS
    quasi-Newton method and simulated annealing. You can choose which
    method you prefer and can try multiple methods. You can supply a
    gradient function to `optim()` for use with the Newton-related
    methods but it can also calculate numerical derivatives on the fly.
    You can have `optim()` return the Hessian at the optimum (based on a
    numerical estimate), which then allows straighforward calculation of
    asymptotic variances based on the information matrix.

-   Also for multivariate optimization, `nlm()` uses a Newton-style
    method, for which you can supply analytic gradient and Hessian, or
    it will estimate these numerically. `nlm()` can also return the
    Hessian at the optimum.

-   The `optimx` package provides `optimx()`, which is a wrapper for a
    variety of optimization methods (including many of those in
    `optim()`, as well as `nlm()`. One nice feature is that it allow you
    to use multiple methods in the same function call.

In the demo code (not shown here; see the source Rmd file), we'll work our way through a real
example of optimizing a likelihood for some climate data on extreme
precipitation.

```r
yHundredths <- scan(file.path('..', 'data', 'precipData.txt')  # precip in hundredths of inches
yHundredths <- yHundredths[!is.na(yHundredths)]
y <- yHundredths/100  # precip now in inches

par(mfrow = c(1, 2))
hist(y)
thresh <- 3
hist(y[y > thresh])

npy=31+28+31 # number of days in winter season
cutoff <- (1/25.4) # wet days defined as those with > 1 mm (1/25.4 inches) of precip
thresh <- as.numeric(quantile(y[y > cutoff],.98,na.rm=T)) # 98%ile of wet days


pp.negloglik <- function(par, y, thresh, npy) {
  mu <- par[1]
  sc <- par[2]
  sh <- par[3]
  uInd <- y > thresh
  if(sc <= 0)
    return(10^6);
  if ((1 + ((sh * (thresh - mu))/sc)) < 0) {
    l <- 10^6;
  }
  else {
    y <- (y - mu)/sc
    y <- 1 + sh * y
    if (min(y^uInd) <= 0){
      l <- 10^6;
    } else{
      ytmp <- y
      ytmp[!uInd]=1  # 'zeroes' out those below the threshold after applying the log in next line
      l <- sum(uInd * log(sc)) + sum(uInd * log(ytmp) *
                                     (1/sh + 1)) + length(y)/npy * mean((1 + (sh * (thresh - mu))/sc)^(-1/sh))
    }
  }
  l
}

## optim() usage
## out <- optim(init, pp.negloglik, hessian = TRUE, method = "BFGS", control = list(maxit = maxit, trace = TRUE))

yExc <- y[y > thresh]
in2 <- sqrt(6 * var(yExc))/pi  # have initial values depend only on those above the threshold
in1 <- mean(yExc) - 0.57722 * in2
init0 <- c(in1, in2, 0.1)

## fit with Nelder-Mead (default) and BFGS
fit1 <- optim(init0, pp.negloglik, y = y, thresh = thresh, npy = npy, control = list(trace = TRUE)) # 118 fxn evals
fit2 <- optim(init0, pp.negloglik, y = y, thresh = thresh, npy = npy, method = 'BFGS', control = list(trace = TRUE)) # ~ 10 its
print(fit1)
print(fit2)

mle <- fit2$par

system.time(optim(init0, pp.negloglik, y = y, thresh = thresh, npy = npy))
system.time(optim(init0, pp.negloglik, y = y, thresh = thresh, npy = npy, method = 'BFGS'))

## different starting value
init1 <- c(mean(y[y > thresh]), sd(y[y > thresh]), -0.1)
optim(init1, pp.negloglik, y = y, thresh = thresh, npy = npy, control = list(trace = TRUE))
optim(init1, pp.negloglik, y = y, thresh = thresh, npy = npy, method = 'BFGS', control = list(trace = TRUE))

## bad starting value for BFGS
init2 <- c(thresh, .01, .1)
out <- optim(init2, pp.negloglik, y = y, thresh = thresh, npy = npy, control = list(trace = TRUE), hessian = TRUE)
solve(out$hessian)
out2 <- optim(init2, pp.negloglik, y = y, thresh = thresh, npy = npy, method = 'BFGS', control = list(trace = TRUE), hessian = TRUE)
solve(out2$hessian)


## suppose the data were on a different scale
yExc2 <- yExc * 1000
y2 <- y * 1000
thresh2 <- thresh * 1000


in2 <- sqrt(6 * var(yExc2))/pi  # have initial values depend only on those above the threshold
in1 <- mean(yExc2) - 0.57722 * in2
init3 <- c(in1, in2, 0.1)

optim(init3, pp.negloglik, y = y2, thresh = thresh2, npy = npy, control = list(trace = TRUE)) ## note that the parameters have changed even beyond a scaling effect
optim(init3, pp.negloglik, y = y2, thresh = thresh2, npy = npy, method = 'BFGS', control = list(trace = TRUE)) # note lack of convergence after 100 its
optim(init3, pp.negloglik, y = y2, thresh = thresh2, npy = npy, method = 'BFGS', control = list(trace = TRUE, maxit = 1000)) # convergence, but to values not concordant with those from fitting the original y data

## when we have y2 = y*1000, the location and scale parameters are on very different scales than the shape parameter
## can we use parscale to deal with the problems when the data are on a different scale?
optim(init3, pp.negloglik, y = y2, thresh = thresh2, npy = npy, control = list(trace = TRUE, parscale = c(1000,1000,1)))
optim(init3, pp.negloglik, y = y2, thresh = thresh2, npy = npy, method = 'BFGS', control = list(trace = TRUE, parscale = c(1000,1000,1)))
## yes, that works! the parameter estimates are now equivalent to those from the standard fitting of the original data

## default step size for numerical derivative is only .001; perhaps we should try with higher accuracy
optim(init0, pp.negloglik, y = y, thresh = thresh, npy = npy, method = 'BFGS', control = list(trace = TRUE, ndeps = rep(1e-6, 3)))
## note that we needed only 33 function evaluations instead of the original 43, presumably because of higher accuracy in the derivative

#### let's do some plotting of the objective fxn as a sanity check

## 3-d grid of location, scale, shape
locVals <- seq(0, 5, len = 30)
scaleVals <- seq(.1, 3, len = 30)
shapeVals <- seq(-.3, .3, by = .04)
parGrid <- expand.grid(loc = locVals, scale = scaleVals, shape = shapeVals)

obj=apply(parGrid, 1, pp.negloglik, y=y, thresh=thresh, npy=npy) # compute objective function for all parameter combos

tmp <- cbind(parGrid,obj)

par(mfrow=c(4, 4), mai = c(.6,.5, .3, .1), mgp = c(1.8, .7, 0))
for( i in 1:length(shapeVals)){
  tmp2 <- tmp[tmp$shape == shapeVals[i],] # slice of objective fxn for fixed shape parameter
  fields::image.plot(locVals, scaleVals,
        matrix((tmp2$obj), length(locVals), length(scaleVals)),
        col = fields::tim.colors(32),
        zlim = c(40,80), main = as.character(shapeVals[i]))
}
## note there a couple weird things about this log likelihood - (1) weird things happen when the shape parameter is very close to 0 (not shown) and (2) for certain combinations the likelihood is not defined (it's set to 1e6) - this is why the white regions of the plot exist - reparameterizing or optimizing with explicit constraints may be better approaches

## apart from that, it appears that optim() has probably found the minimum
```

## Various considerations in using the R functions

As we've seen, initial values are important both for avoiding divergence
(e.g., in N-R), for increasing speed of convergence, and for helping to
avoid local optima. So it is well worth the time to try to figure out a
good starting value or multiple starting values for a given problem.

Scaling can be important. One useful step is to make sure the problem is
well-scaled, namely that a unit step in any parameter has a comparable
change in the objective function, preferably approximately a unit change
at the optimum. `optim()` allows you to supply scaling information
through the `parscale` component of the `control` argument. Basically if
$x_{j}$ is varying at $p$ orders of magnitude smaller than the other
$x$s, we want to reparameterize to $x_{j}^{*}=x_{j}\cdot10^{p}$ and then
convert back to the original scale after finding the answer. Or we may
want to work on the log scale for some variables, reparameterizing as
$x_{j}^{*}=\log(x_{j})$. We could make such changes manually in our
expression for the objective function or make use of arguments such as
`parscale`.

If the function itself gives very large or small values near the
solution, you may want to rescale the entire function to avoid
calculations with very large or small numbers. This can avoid problems
such as having apparent convergence because a gradient is near zero,
simply because the scale of the function is small. In `optim()` this can
be controlled with the `fnscale` component of `control`.

Always consider your answer and make sure it makes sense, in particular
that you haven't 'converged' to an extreme value on the boundary of the
space.

Venables and Ripley suggest that it is often worth supplying analytic
first derivatives rather than having a routine calculate numerical
derivatives but not worth supplying analytic second derivatives. As
we'll see in Unit 12, R can do symbolic (i.e., analytic) differentiation
to find first and second derivatives using `deriv()`.

In general for software development it's obviously worth putting more
time into figuring out the best optimization approach and supplying
derivatives. For a one-off analysis, you can try a few different
approaches and assess sensitivity.

The nice thing about likelihood optimization is that the asymptotic
theory tells us that with large samples, the likelihood is approximately
quadratic (i.e., the asymptotic normality of MLEs), which makes for a
nice surface over which to do optimization. When optimizing with respect
to variance components and other parameters that are non-negative, one
approach to dealing with the constraints is to optimize with respect to
the log of the parameter.

---

[← 5. Multivariate optimization](10-5-multivariate-optimization.md) · [Up: contents](index.md) · [7. Combinatorial optimization over discrete spaces →](12-7-combinatorial-optimization-over-discrete-spaces.md)
