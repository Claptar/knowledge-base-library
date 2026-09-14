---
title: set things up
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/05/code_review.qmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# set things up

**Source:** [`labs/05/code_review.qmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd) · **Licence:** unresolved · Converted 2026-09-14 from `.qmd` (lossless)

n <- 50
x <- 1:n
y <- runif(n = n, min = 0, max = 10)

col_factor <- sample(x = c(1, 2), size = n, replace = T, prob = c(1, 2))

df <- data.frame(x, y, color = as.factor(col_factor))

---

[← Good plotting](13-good-plotting.md) · [Up: contents](index.md) · [make the plot →](15-make-the-plot.md)
