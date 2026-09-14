---
title: 4. Convergence ideas
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit11-optim.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Convergence ideas

**Source:** [`units/unit11-optim.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Convergence metrics

We might choose to assess whether $f^{\prime}(x_{t})$ is near zero,
which should assure that we have reached the critical point. However, in
parts of the domain where $f(x)$ is fairly flat, we may find the
derivative is near zero even though we are far from the optimum.
Instead, we generally monitor $|x_{t+1}-x_{t}|$ (for the moment, assume
$x$ is scalar). We might consider absolute convergence:
$|x_{t+1}-x_{t}|<\epsilon$ or relative convergence,
$\frac{|x_{t+1}-x_{t}|}{|x_{t}|}<\epsilon$. Relative convergence is
appealing because it accounts for the scale of $x$, but it can run into
problems when $x_{t}$ is near zero, in which case one can use
$\frac{|x_{t+1}-x_{t}|}{|x_{t}|+\epsilon}<\epsilon$. We would want to
account for machine precision in thinking about setting $\epsilon$. For
relative convergence a reasonable choice of $\epsilon$ would be to use
the square root of machine epsilon or about $1\times10^{-8}$. This is
the *reltol* argument in *optim()* in R.

Problems with the optimization may show up in a convergence measure that
fails to decrease or cycles (oscillates). Software generally has a
stopping rule that stops the algorithm after a fixed number of
iterations; these can generally be changed by the user. When an
algorithm stops because of the stopping rule before the convergence
criterion is met, we say the algorithm has failed to converge. Sometimes
we just need to run it longer, but often it indicates a problem with the
function being optimized or with your starting value.

For multivariate optimization, we use a distance metric between
$x_{t+1}$ and $x_{t}$, such as $\|x_{t+1}-x_{t}\|_{p}$ , often with
$p=1$ or $p=2$.

## Starting values

Good starting values are important because they can improve the speed of
optimization, prevent divergence or cycling, and prevent finding local
optima.

Using random or selected multiple starting values can help with multiple
optima (aka multimodality).

Here's a function (the Rastrigin function) with multiple optima that is
commonly used for testing methods that claim to work well for multimodal
problems. This is a hard function to optimize with respect to,
particularly in higher dimensions (one can do it in higher dimensions
than 2 by simply making the $x$ vector longer but having the same
structure). In particular Rastrigin with 30 dimensions is considered to
be very hard.

```r
rastrigin <- function(x) {
	A <- 10
	n <- length(x)
	return(A*n + sum(x^2 - A * cos(2*pi*x)))
}
const <- 5.12
nGrid <- 100
gr <- seq(-const, const, len = nGrid)
xs <- expand.grid(x1 = gr, x2 = gr)
y <- apply(xs, 1, rastrigin)
fields::image.plot(gr, gr, matrix(y, nGrid, nGrid),
                       col = fields::tim.colors(32))
```


One R package that may be useful for multi-modal problems is *DEoptim*,
which implements an evolutionary algorithm (genetic algorithms are one
kind of evolutionary algorithm). It would be interesting to try an
evolutionary algorithm on a test function like this.

## Convergence rates

Let $\epsilon_{t}=|x_{t}-x^{*}|$. If the limit

$$\lim_{t\to\infty}\frac{|\epsilon_{t+1}|}{|\epsilon_{t}|^{\beta}}=c$$
exists for $\beta>0$ and $c\ne0$, then a method is said to have order of
convergence $\beta$. This basically measures how big the error at the
$t+1$th iteration is relative to that at the $t$th iteration, with the
approximation that $|\epsilon_{t+1}|\approx c|\epsilon_{t}|^{\beta}$.

Bisection doesn't formally satisfy the criterion needed to make use of
this definition, but roughly speaking it has linear convergence
($\beta=1$), so the magnitude of the error decreases by a factor of $c$
at each step. Next we'll see that N-R has quadratic convergence
($\beta=2$), which is fast.

To analyze convergence of N-R, consider a Taylor expansion of the
gradient at the minimum, $x^{*}$, around the current value, $x_{t}$:
$$f^{\prime}(x^{*})=f^{\prime}(x_{t})+(x^{*}-x_{t})f^{\prime\prime}(x_{t})+\frac{1}{2}(x^{*}-x_{t})^{2}f^{\prime\prime\prime}(\xi_{t})=0,$$
for some $\xi_{t}\in[x^{*},x_{t}]$. Making use of the N-R update
equation:
$x_{t+1}=x_{t}-\frac{f^{\prime}(x_{t})}{f^{\prime\prime}(x_{t})}$ to
substitute , and some algebra, we have
$$\frac{|x^{*}-x_{t+1}|}{(x^{*}-x_{t})^{2}}=\frac{1}{2}\frac{f^{\prime\prime\prime}(\xi_{t})}{f^{\prime\prime}(x_{t})}.$$
If the limit of the ratio on the right hand side exists and is equal to
$c$:
$$c=\lim_{x_{t}\to x^{*}}\frac{1}{2}\frac{f^{\prime\prime\prime}(\xi_{t})}{f^{\prime\prime}(x_{t})}=\frac{1}{2}\frac{f^{\prime\prime\prime}(x^{*})}{f^{\prime\prime}(x^{*})}$$
then we see that $\beta=2$.

If $c$ were one, then we see that if we have $k$ digits of accuracy at
$t$, we'd have $2k$ digits at $t+1$ (e.g., $|\epsilon_{t}|=0.01$ results
in $|\epsilon_{t+1}|=0.0001$), which justifies the characterization of
quadratic convergence being fast. In practice $c$ will moderate the rate
of convergence. The smaller $c$ the better, so we'd like to have the
second derivative be large and the third derivative be small. The
expression also indicates we'll have a problem if
$f^{\prime\prime}(x_{t})=0$ at any point (think about what this
corresponds to graphically - what is our next step when
$f^{\prime\prime}(x_{t})=0$?). The characteristics of the derivatives
determine the domain of attraction (the region in which we'll converge
rather than diverge) of the minimum.

Givens and Hoeting show that using the secant-based approximation to the
second derivative in N-R has order of convergence, $\beta\approx1.62$.

Here's an example of convergence comparing bisection and N-R:

```r
options(digits = 10)
f <- function(x) cos(x)
fp <- function(x) -sin(x)
fpp <- function(x) -cos(x)
xstar <- pi # known minimum

## N-R
x0 <- 2
xvals <- c(x0,rep(NA,9))
for(t in 2:10){
	xvals[t] <- xvals[t-1] - fp(xvals[t-1]) / fpp(xvals[t-1])
}
print(xvals)

## bisection
bisecStep <- function(interval, fp){
	xt <- mean(interval)
	if(fp(interval[1]) * fp(xt) <= 0)
            interval[2] <- xt else interval[1] <- xt
	return(interval)
}
nIt <- 30
a0 <- 2; b0 <- (3*pi/2) - (xstar - a0)
## have b0 be as far from min as a0 for fair comparison with N-R
interval <- matrix(NA, nr = nIt, nc = 2)
interval[1, ] <- c(a0, b0)
for(t in 2:nIt){
	interval[t, ] <- bisecStep(interval[t-1, ], fp)
}
rowMeans(interval)
```

---

[← oscillates and comes close to diverging but converges](08-oscillates-and-comes-close-to-diverging-but-converges.md) · [Up: contents](index.md) · [5. Multivariate optimization →](10-5-multivariate-optimization.md)
