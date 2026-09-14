---
title: R6 Object of class 'tsSimClass' with 100 time points.
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# R6 Object of class 'tsSimClass' with 100 time points.

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**set.seed** (1) _## here's a simulated time series_ y <- myts$ **simulate** ()

35

**plot** (myts$ **getTimes** (), y, type = 'l', xlab = 'time', ylab = 'process values') _## here's a second simulated time series_ y2 <- myts$ **simulate** () **lines** (myts$ **getTimes** (), y2, lty = 2) myts2 <- tsSimClass$ **new** (1:100, 2, 3) ## Done updating correlation matrix and Cholesky factor. **set.seed** (1) _## here's a simulated time series with a different value of ## the correlation parameter (corParam)_ y <- myts2$ **simulate** () **lines** (myts2$ **getTimes** (), y, col = 'red')


<!-- Start of picture text -->
0 20 40 60 80 100<br>time<br>4<br>3<br>2<br>1<br>process values<br>0<br><!-- End of picture text -->

_## That simulated time series is less wiggly because the corParam value ## is larger than before._

mytsRef <- myts

_## 'mytsRef' and 'myts' are names for the same underlying object_

36

mytsFullCopy <- myts$ **clone** () _# mytsFullCopy is a true copy and a new object_ myts$ **changeTimes** ( **seq** (0,1000, length = 100)) ## Done updating correlation matrix and Cholesky factor. myts$ **getTimes** ()[1:5] _# this and_ ## [1] 0.0 10.1 20.2 30.3 40.4 mytsRef$ **getTimes** ()[1:5] _# this are the same_ ## [1] 0.0 10.1 20.2 30.3 40.4 mytsFullCopy$ **getTimes** ()[1:5] _# this is different_ ## [1] 1 2 3 4 5

A few additional points:

- As we just saw, a copy of an object is just a pointer to the original object, unless we explicitly invoke the _clone()_ method.

- As with S3 and S4, classes can inherit from other classes. E.g., if we had a _simClass_ and we wanted the _tsSimClass_ to inherit from it: R6Class("tsSimClass", inherit = "simClass", ...)

- Here we see that use of private fields shields them from modification by users. In this example, the correlation matrix and the Cholesky factor U are both functions of the vector of times. So we don’t want to allow a user to directly modify _times_ . Instead we force them to use _setTimes()_ , which correctly keeps all the fields in the object internally consistent (by calling _calcMats()_ ):

_## the next line would be dangerous if 'times' were public, since ## changing 'times' should result in changing the correlation matrix and ## changing U._ myts$times <- 1:10

**## Error in myts$times <- 1:10: cannot add bindings to a locked environment**

37

- If you need to refer to methods and fields you refer to the entire object as either _self_ or _private_ .

- There is a older, more complicated, slower variation on R6 classes called ReferenceClasses. See the _help(ReferenceClasses)_ .

More details on R6 classes can be found in the Advanced R book: https://adv-r.hadley.nz/r6.html.

---

[← [1] TRUE](22-1-true.md) · [Up: contents](index.md) · [5 Standard dataset manipulations →](24-5-standard-dataset-manipulations.md)
