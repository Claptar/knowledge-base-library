---
title: vectorized multinomial
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/05/code_review.qmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# vectorized multinomial

**Source:** [`labs/05/code_review.qmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd) · **Licence:** unresolved · Converted 2026-09-14 from `.qmd` (lossless)

########################

probs <- matrix(data = c(0.1,0.1,0.8, 1/3,1/3,1/3), nrow = 2, byrow = T)

set.seed(0)
a_mnom <- t(apply(X = probs, MARGIN = 1, FUN = rmultinom,
                 n = 1, size = 100))

set.seed(0)
v_mnom <- extraDistr::rmnom(n = 2, size = 100, prob = probs)

all.equal(a_mnom, v_mnom)
identical(a_mnom, v_mnom) # why false?

---

[← vectorized division](16-vectorized-division.md) · [Up: contents](index.md) · [short benchmark →](18-short-benchmark.md)
