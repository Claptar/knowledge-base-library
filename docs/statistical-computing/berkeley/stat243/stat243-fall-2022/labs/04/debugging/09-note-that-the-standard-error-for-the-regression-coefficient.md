---
title: note that the standard error for the regression coefficient is ~3
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/04/debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/04/debugging.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# note that the standard error for the regression coefficient is ~3

**Source:** [`labs/04/debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/04/debugging.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

summary(mod)
```

## Buggy `logitBoot()` function

Take a quick look at the source code and output below:

```r
my_data <- read.csv('./data.csv')

logitBoot <- function(y, x, n_boot = 2000) {
  set.seed(5)

  # do n_boot random permutations of x and y and return coefficient on x with
  # the myGLM function
  boot_coefs <- sapply(seq_len(n_boot), myGLM, y, x)

  # compute standard deviation of those estimates and return
  boot_se <- sd(boot_coefs)
  return(boot_se)
}

myGLM <- function(i, y, x) {
  n <- length(y)

  # randomly sample with replacement from the observations in the data
  boot_sample <- sample(seq_len(n), n, replace = TRUE)

  # create vectors of the bootstrapped samples
  x_boot <- x[boot_sample]
  y_boot <- y[boot_sample]

  # fit logistic regression on permutated data
  mod_boot <- glm(y_boot ~ x_boot, family = 'binomial')

  # return the estimated coefficient
  return(mod_boot$coef[2])
}

---

[← fit model in R](08-fit-model-in-r.md) · [Up: contents](index.md) · [estimate standard error with our bootstrap function →](10-estimate-standard-error-with-our-bootstrap-function.md)
