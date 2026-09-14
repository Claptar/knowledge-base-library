---
title: 'function (x, ...) ## UseMethod("mean") ## ##'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# function (x, ...) ## UseMethod("mean") ## ##

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

x <- 0; y <- 0 out <- **mean** (x = **c** (3,7)) _# usual way to pass an argument to a function by name_ out <- **mean** ( **c** (3,7)) _# or by position ## what does the following do?_ out <- **mean** (x <- **c** (3,7)) _# this is allowable, but confusing_ out <- **mean** (y = **c** (3,7)) _# why doesn't this work?_

**## Error in mean.default(y = c(3, 7)): argument "x" is missing, with no default**

out <- **mean** (y <- **c** (3,7)) _# again, allowable, but confusing_

What can you tell me about what is going on in each case above?

One situation in which you want to use ’ _<-_ ’ is if it is being used as part of an argument to a

function, so that R realizes you’re not indicating one of the function arguments, e.g.:

_## NOT OK, system.time() expects its argument to be a complete R expression:_ **system.time** (out = **rnorm** (10000))

**## Error in system.time(out = rnorm(10000)): unused argument (out = rnorm(10000))**

_# OK:_

**system.time** (out <- **rnorm** (10000))

19

---

[← Unit 05 — programming Part 14 —](14-unit-05-programming-part-14.md) · [Up: contents](index.md) · [user system elapsed ## 0.001 0.000 0.001 →](16-user-system-elapsed-0-001-0-000-0-001.md)
