---
title: unless you're running Rscript, then idk
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/05/debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/05/debugging.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# unless you're running Rscript, then idk

**Source:** [`section/05/debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/05/debugging.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

#library(methods)
set.seed(0)
nCats <- 30
n <- 100
y <- rnorm(n)
x <- rnorm(n)
cats <- sample(1:nCats, n, replace = TRUE)
data <- data.frame(y, x, cats)

params <- matrix(NA, nrow = nCats, ncol = 2)

for (i in 1:nCats) {
  sub <- data[data$cats == i, ]
  fit <- try(lm(y ~ x, data = sub))
  if (!inherits(fit, "try-error"))
    params[i, ] = fit$coef
}

---

[← methods comes installed](06-methods-comes-installed.md) · [Up: contents](index.md) · [view params →](08-view-params.md)
