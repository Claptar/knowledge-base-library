---
title: 'user system elapsed ## 0.001 0.000 0.001'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# user system elapsed ## 0.001 0.000 0.001

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Here’s another example:

mat <- **matrix** ( **c** (1, NA, 2, 3), nrow = 2, ncol = 2) **apply** (mat, 1, sum.isna <- **function** (vec) { **return** ( **sum** ( **is.na** (vec)))}) ## [1] 0 1 _## What is the side effect of what I have done just above?_ **apply** (mat, 1, sum.isna = **function** (vec) { **return** ( **sum** ( **is.na** (vec)))}) _# NOPE_ **## Error in match.fun(FUN): argument "FUN" is missing, with no default**

R often treats integers as numerics, but we can force R to store values as integers:

vals <- **c** (1, 2, 3) **class** (vals) ## [1] "numeric" vals <- 1:3 **class** (vals) ## [1] "integer" vals <- **c** (1L, 2L, 3L) vals ## [1] 1 2 3 **class** (vals) ## [1] "integer"

We convert between classes using variants on _as()_ : e.g.,

20

**as.character** ( **c** (1,2,3)) ## [1] "1" "2" "3" **as.numeric** ( **c** ("1", "2.73")) ## [1] 1.00 2.73 **as.factor** ( **c** ("a", "b", "c")) ## [1] a b c ## Levels: a b c

Some common conversions are converting numbers that are being interpreted as characters into actual numbers, converting between factors and characters, and converting between logical TRUE/FALSE vectors and numeric 1/0 vectors. In some cases R will automatically do conversions behind the scenes in a smart way (or occasionally not so smart way). Consider these examples of implicit coercion:

x <- **rnorm** (5) x[3] <- 'hat' _# What do you think is going to happen?_ indices <- **c** (1, 2.73) myVec <- 1:10 myVec[indices] ## [1] 1 2

Be careful of using factors as indices:

students <- **factor** ( **c** ("basic", "proficient", "advanced", "basic", "advanced", "minimal")) score <- **c** (minimal = 3, basic = 1, advanced = 13, proficient = 7) score["advanced"] ## advanced ## 13 score[students[3]]

21

---

[← function (x, ...) ## UseMethod("mean") ## ##](15-function-x-usemethod-mean.md) · [Up: contents](index.md) · [minimal ## 3 score[ as.character (students[3])] ## advanced ## 13 →](17-minimal-3-score-as-character-students-3-advanced-13.md)
