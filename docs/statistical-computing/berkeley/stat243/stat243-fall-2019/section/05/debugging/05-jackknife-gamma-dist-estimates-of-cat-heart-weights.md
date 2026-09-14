---
title: jackknife gamma dist. estimates of cat heart weights
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/05/debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/05/debugging.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# jackknife gamma dist. estimates of cat heart weights

**Source:** [`section/05/debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/05/debugging.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

gamma_jackknife(MASS::cats$Hwt)
```

### 3.3) A More Involved Example: `logitBoot()`

- Load `data.csv`
- Fit a logistic regression model `y~x` called `mod` in the script provided.
- What is the std of the coefficient of `x` from `summary(mod)`?
- Now find the estimate of the same parameter now using bootstrap by simply calling `logitBoot()` as provided in the script.
- Why is this estimate so much larger?
- Use debugging tools to figure out the bug.

Code found [here](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/05/logitBoot.R)
Data found [here](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/05/data.csv)
```r
myData <- read.csv('./data.csv')

logitBoot <- function(y, x, nBoot = 2000) {
  set.seed(5)
  out <- sapply(seq_len(nBoot), myglm, y, x)
  boot_se <- sd(out)
  return(boot_se)
}

myglm <- function(i, y, x) {
  n <- length(y)
  ind <- sample(seq_len(n), n, replace = TRUE)
  out <- glm(y[ind]~x[ind], family='binomial')
  return(out$coef[2])
}

mod <- glm(y ~ x, data = myData, family = 'binomial')
summary(mod)
## note that the standard error for the regression coefficient is ~3

logitBoot(myData$y, myData$x)
```

### 3.3) Example of Defensive Programming

When writing functions, and software more generally, you'll want to warn the user
or stop execution when there is an error and exit gracefully, giving the user some
idea of what happened. Here are some things to consider:

- check function inputs and warn users if the code will do something they might not expect or makes particular choices
    - eg `assertthat`, `assertr`, and `checkmate` packages
- check inputs to `if` and the ranges in `for` loops
- provide reasonable default arguments
- document the range of valid inputs
- check that the output produced is valid
- stop execution based on checks and give an informative error message
- catch run-time erros using `try()` or `tryCatch()`.

```r

---

[← comes installed](04-comes-installed.md) · [Up: contents](index.md) · [methods comes installed →](06-methods-comes-installed.md)
