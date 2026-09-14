---
title: comes installed
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/05/debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/05/debugging.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# comes installed

**Source:** [`section/05/debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/05/debugging.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

#library(MASS)

gamma_est <- function(data) {
  # this fits a gamma distribution to a collection of numbers
  m <- mean(data)
  v <- var(data)
  s <- v/m
  a <- m/s
  return(list(a=a,s=s))
}

calc_var <- function(estimates){
  var_of_ests <- apply(estimates, 2, var)
  return(((n-1)^2/n)*var_of_ests)
}

gamma_jackknife <- function(data) {
  ## jackknife the estimation

  n <- length(data)
  jack_estimates = gamma_est(data[-1])
  for (omitted_point in 2:n) {
    jack_estimates = rbind(jack_estimates, gamma_est(data[-omitted_point]))
  }

  jack_var = calc_var(jack_estimates)

  return(sqrt(jack_var))
}

---

[← Need MASS for cats data](03-need-mass-for-cats-data.md) · [Up: contents](index.md) · [jackknife gamma dist. estimates of cat heart weights →](05-jackknife-gamma-dist-estimates-of-cat-heart-weights.md)
