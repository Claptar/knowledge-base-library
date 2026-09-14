---
title: vectorized division
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/05/code_review.qmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# vectorized division

**Source:** [`labs/05/code_review.qmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd) · **Licence:** unresolved · Converted 2026-09-14 from `.qmd` (lossless)

#####################

x <- 1:100
y <- 100:1

a_div <- mapply(FUN = "/", x, y)
v_div <- x / y

all.equal(a_div, v_div)
identical(a_div, v_div)

########################

---

[← make the plot](15-make-the-plot.md) · [Up: contents](index.md) · [vectorized multinomial →](17-vectorized-multinomial.md)
