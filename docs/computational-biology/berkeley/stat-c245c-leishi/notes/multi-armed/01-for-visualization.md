---
title: for visualization
source: https://leishi-rocks.github.io/courses/ph240c/notes/multi-armed.Rmd
source_file: sources/berkeley-stat-c245c-leishi/notes/multi-armed.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# for visualization

**Source:** [`notes/multi-armed.Rmd`](https://leishi-rocks.github.io/courses/ph240c/notes/multi-armed.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

library(Rcpp)
if(!require("png")){
  install.packages("png")
  library(png)
}
if(!require("gifski")){
  install.packages("gifski")
  library(gifski)
}
if(!require("Matrix")){
  install.packages("Matrix")
  library(Matrix)
}
if(!require("gganimate")){
  install.packages("gganimate", "transformr")
  library(gganimate)
  library(transformr)
}
if(!require("transformr")){
  install.packages("transformr")
  library("transformr")
}

---

[Up: contents](index.md) · [for bandit →](02-for-bandit.md)
