---
title: Lazy Evaluation
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s08/s08.rmd
source_file: sources/berkeley-stat243/stat243-fall-2017/section/s08/s08.rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Lazy Evaluation

**Source:** [`section/s08/s08.rmd`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s08/s08.rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.rmd` (lossless)

Without running the code below, can you guess the output of the expressions at the end of the chunk?  Also, why are two sets of parentheses necessary?

```r
x <- 10

lazy <- function(x=0) {
  y <- 2
  z <- 3
  w <- x + y + z
  x <- 1
  return(w)
}

lazy2 <- function(x=0) {
  y <- 2
  z <- 3
  w <- x + y + z
  g <- function() w
  x <- 1
  return(g)
}

lazy3 <- function(x=0) {
  y <- 2
  z <- 3
  delayedAssign("w", x + y + z)
  g <- function() w
  x <- 1
  return(g)
}

lazy4 <- function(x=0) {
  y <- 2
  z <- 3
  g <- function() x + y + z
  x <- 1
  return(g)
}

lazy5 <- function(x) {
  y <- 2
  z <- 3
  g <- function() w
  w <- x + y + z
  return(g)
}

lazy6 <- function(x) {
  y <- 2
  z <- 3
  g <- function() x + y + z
  return(g)
}

lazy()
lazy2()()
lazy3()()
lazy4()()
lazy5(x)()
lazy6(x)()

lazy7 <- lazy5(x)
lazy8 <- lazy6(x)
lazy9 <- lazy6(x)
lazy9()
rm(x)
lazy7()
lazy8()
lazy9()
```

---

[← Paired Code Review](01-paired-code-review.md) · [Up: contents](index.md) · [Practice →](03-practice.md)
