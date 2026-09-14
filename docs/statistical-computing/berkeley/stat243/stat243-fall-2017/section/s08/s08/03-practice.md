---
title: Practice
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s08/s08.rmd
source_file: sources/berkeley-stat243/stat243-fall-2017/section/s08/s08.rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Practice

**Source:** [`section/s08/s08.rmd`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s08/s08.rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.rmd` (lossless)

Write a function `new_counter()` the creates a closure which counts the number of times it has been called.  For example, you should be able to do:

```r
counter1 <- new_counter()
counter2 <- new_counter()
```

```r
counter1()
#[1] 1
counter1()
#[1] 2
counter1()
#[1] 3
counter2() # This is a different counter
#[1] 1
```

Write a function `delayed_by(t, f)` that admits two arguments `t`, time in milliseconds and `f`, any function.  It should return a modified copy of `f` that runs `t` milliseconds slower.

---

[← Lazy Evaluation](02-lazy-evaluation.md) · [Up: contents](index.md)
