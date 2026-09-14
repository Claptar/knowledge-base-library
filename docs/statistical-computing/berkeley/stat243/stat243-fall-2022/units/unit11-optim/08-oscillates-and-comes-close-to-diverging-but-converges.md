---
title: oscillates and comes close to diverging but converges
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit11-optim.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# oscillates and comes close to diverging but converges

**Source:** [`units/unit11-optim.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

plot(xs, fp(xs), type = 'l', xlab = 'x', ylab = "f'(x)",
     main = 'nearly diverges, gradient view',)
legend('bottomright', legend = c("f'(x)"), bty = 'n')
points(xvals, fp(xvals), pch = as.character(1:length(xvals)), col = 'red',
              cex = 1.5)
points(pi, 0, pch = 16, cex = 1.5)
## and we've found a maximum rather than a minimum...
plot(xs, f(xs), type = 'l', xlab = 'x', ylab = "f(x)",
     main = 'nearly diverges, function view ',)
legend('bottomright', legend = c("f(x)"), bty = 'n')
points(xvals, f(xvals), pch = as.character(1:length(xvals)), col = 'red',
              cex = 1.5)
points(pi, f(pi), pch = 16, cex = 1.5)


x0 <- 3.8 # good starting point
fp(x0)
fpp(x0)
x1 <- x0 - fp(x0)/fpp(x0)
xvals <- c(x0,rep(NA,9))
for(t in 2:10){
	xvals[t]=xvals[t-1]-fp(xvals[t-1])/fpp(xvals[t-1])
}
## print(xvals)

## converges quickly
plot(xs, fp(xs), type = 'l', xlab = 'x', ylab = "f'(x)",
     main = 'better starting point, gradient view',)
legend('bottomright', legend = c("f'(x)"), bty = 'n')
points(xvals, fp(xvals), pch = as.character(1:length(xvals)), col = 'red',
              cex = 1.5)
points(pi, 0, pch = 16, cex = 1.5)
## and we've found a maximum rather than a minimum...
plot(xs, f(xs), type = 'l', xlab = 'x', ylab = "f(x)",
     main = 'better starting point, function view ',)
legend('bottomright', legend = c("f(x)"), bty = 'n')
points(xvals, f(xvals), pch = as.character(1:length(xvals)), col = 'red',
              cex = 1.5)
points(pi, f(pi), pch = 16, cex = 1.5)
```

One nice, general idea is to use a fast method such as Newton's method
*safeguarded* by a robust, but slower method. Here's how one can do this
for N-R, safeguarding with a bracketing method such as bisection.
Basically, we check the N-R proposed move to see if N-R is proposing a
step outside of where the root is known to lie based on the previous
steps and the gradient values for those steps. If so, we could choose
the next step based on bisection.

Another approach is backtracking. If a new value is proposed that yields
a larger value of the function, backtrack to find a value that reduces
the function. One possibility is a line search but given that we're
trying to reduce computation, a full line search is often unwise
computationally (also in the multivariate Newton's method, we are in the
middle of an iterative algorithm for which we will just be going off in
another direction anyway at the next iteration). A basic approach is to
keep backtracking in halves. A nice alternative is to fit a polynomial
to the known information about that slice of the function, namely
$f(x_{t+1})$, $f(x_{t})$, $f^{\prime}(x_{t})$ and
$f^{\prime\prime}(x_{t})$ and find the minimum of the polynomial
approximation.

---

[← second derivative](07-second-derivative.md) · [Up: contents](index.md) · [4. Convergence ideas →](09-4-convergence-ideas.md)
