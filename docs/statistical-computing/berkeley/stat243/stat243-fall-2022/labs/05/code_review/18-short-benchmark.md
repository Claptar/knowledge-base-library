---
title: short benchmark
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/05/code_review.qmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# short benchmark

**Source:** [`labs/05/code_review.qmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/05/code_review.qmd) · **Licence:** unresolved · Converted 2026-09-14 from `.qmd` (lossless)

microbenchmark::microbenchmark(
    "apply" = apply(X = probs, MARGIN = 1,
                    FUN = rmultinom, n = 1, size = 100),
    "vector" = extraDistr::rmnom(n = 2, size = 100,
                                 prob = probs),
    times = 100)
```

If you want to learn a bit more about vectorization, check out [24.5 Vectorize](https://adv-r.hadley.nz/perf-improve.html#vectorise)
in the _AdvancedR_ book.

---

[← vectorized multinomial](17-vectorized-multinomial.md) · [Up: contents](index.md)
