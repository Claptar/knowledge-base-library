---
title: second derivative
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit11-optim.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# second derivative

**Source:** [`units/unit11-optim.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

fpp <- function(x) -cos(x)
xs <- seq(0, 2*pi, len = 300)

x0 <- 5.5 # starting point
fp(x0) # positive
fpp(x0) # negative
x1 <- x0 - fp(x0)/fpp(x0) # whoops, we've gone uphill
## because of the negative second derivative
xvals <- c(x0,rep(NA,9))
for(t in 2:10){
	xvals[t]=xvals[t-1]-fp(xvals[t-1])/fpp(xvals[t-1])
}
## print(xvals)

plot(xs, fp(xs), type = 'l', xlab = 'x', ylab = "f'(x)",
     main = 'uphill to local maximum, gradient view',)
legend('bottomright', legend = c("f'(x)"), bty = 'n')
points(xvals, fp(xvals), pch = as.character(1:length(xvals)), col = 'red',
              cex = 1.5)
points(pi, 0, pch = 16, cex = 1.5)
## and we've found a maximum rather than a minimum...
plot(xs, f(xs), type = 'l', xlab = 'x', ylab = "f(x)",
     main = 'uphill to local maximum, function view ',)
legend('bottomright', legend = c("f(x)"), bty = 'n')
points(xvals, f(xvals), pch = as.character(1:length(xvals)), col = 'red',
              cex = 1.5)
points(pi, f(pi), pch = 16, cex = 1.5)


## in contrast, with better starting points we can find the minimum

x0 <- 4.3 # ok starting point
fp(x0)
fpp(x0)
x1 <- x0 - fp(x0)/fpp(x0)
xvals <- c(x0,rep(NA,9))
for(t in 2:10){
	xvals[t]=xvals[t-1]-fp(xvals[t-1])/fpp(xvals[t-1])
}
## print(xvals)

---

[← gradient](06-gradient.md) · [Up: contents](index.md) · [oscillates and comes close to diverging but converges →](08-oscillates-and-comes-close-to-diverging-but-converges.md)
