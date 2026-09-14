---
title: '[1] "Hi there"'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] "Hi there"

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Since operators are just functions, there are cases in which there are optional arguments that we might not expect. Here’s how to pass a sometimes useful argument to the bracket operator (in this case avoiding conversion from a matrix to a vector, which can mess up subsequent code).

70

mat <- **matrix** (1:4, 2, 2) mat[ , 1] ## [1] 1 2 mat[ , 1, drop = FALSE] _# what's the difference?_ ## [,1] ## [1,] 1 ## [2,] 2 We can also use operators with our S3 classes. Picking up our example from our discussion of S3 OOP, the following example will be a bit silly (it would make more sense with a class that is a mathematical object) but indicates the power of having methods. yog <- **list** (firstnamefirstname = 'Yogi',, surname = 'the Bear', **class** (yog) <- 'bear' **methods** ( ` + ` ) ## [1] +,matrix,spam-method +,spam,matrix-method ## [3] +,spam,missing-method +,spam,spam-method ## [5] +.Date +.gg* ## [7] +.glue* +.POSIXt ## [9] +.vctrs_vctr* ## see '?methods' for accessing help and source code ` +.bear ` <- **function** (object, incr) { object$age <- object$age + incr **return** (object) } older_yog <- yog + 15 older_yog ## $firstname ## [1] "Yogi" ##

We can also use operators with our S3 classes. Picking up our example from our discussion of S3 OOP, the following example will be a bit silly (it would make more sense with a class that is a mathematical object) but indicates the power of having methods.

yog <- **list** (firstnamefirstname = 'Yogi',, surname = 'the Bear', age = 20) **class** (yog) <- 'bear'

71

---

[← Unit 05 — programming Part 37 —](37-unit-05-programming-part-37.md) · [Up: contents](index.md) · [$surname ## [1] "the Bear" ## ## $age ## [1] 35 ## ## attr(,"class") ## [1] "bear" →](39-age-1-35-attr-class-1-bear.md)
