---
title: is larger than before.
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# is larger than before.

```r
mytsRef <- myts
## 'mytsRef' and 'myts' are names for the same underlying object

mytsFullCopy <- myts$clone() # mytsFullCopy is a true copy and a new object
myts$changeTimes(seq(0,1000, length = 100))
## Done updating correlation matrix and Cholesky factor.

myts$getTimes()[1:5] # this and
## [1]  0.0 10.1 20.2 30.3 40.4

mytsRef$getTimes()[1:5] # this are the same
## [1]  0.0 10.1 20.2 30.3 40.4

mytsFullCopy$getTimes()[1:5] # this is different
## [1] 1 2 3 4 5
```

A few additional points:

* As we just saw, a copy of an object is just a pointer to the original object, unless we explicitly invoke the `clone()` method.

* As with S3 and S4, classes can inherit from other classes. E.g., if we had a simClass and we wanted the tsSimClass to inherit from it:

```r
R6Class("tsSimClass", inherit = "simClass", ...)
```

* Here we see that use of private fields shields them from modification by users. In this example, the correlation matrix and the Cholesky factor U are both functions of the vector of times. So we don't want to allow a user to directly modify *times*. Instead we force them to use `setTimes()`, which correctly keeps all the fields in the object internally consistent (by calling `calcMats()`):

```r
## the next line would be dangerous if 'times' were public, since
## changing 'times' should result in changing the correlation matrix and
## changing U.
myts$times <- 1:10
## Error in myts$times <- 1:10: cannot add bindings to a locked environment
```

* If you need to refer to methods and fields you refer to the entire object as either *self* or *private*.

* There is a older, more complicated, slower variation on R6 classes called ReferenceClasses. See the `help(ReferenceClasses)`.

More details on R6 classes can be found in the Advanced R book: https://adv-r.hadley.nz/r6.html.

---

[← 4 Types, classes, and object-oriented programming](04-4-types-classes-and-object-oriented-programming.md) · [Up: contents](index.md) · [5 Standard dataset manipulations →](06-5-standard-dataset-manipulations.md)
