---
title: Unit 05 — programming Part 25 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 25 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can use _setClassUnion()_ to create what Adler calls _superclass_ and what Chambers calls a _virtual class_ that allows for methods that apply to multiple classes. So if you have a person class and a pet class, you could create a “named lifeform” virtual class that has methods for working with name and age slots, since both people and pets would have those slots. You can’t directly create an object in the virtual class.

#### **4.4.3 R6 classes**

R6 classes are a new construct in R. They are classes somewhat similar to S4. Importantly, they behave like pointers (the fields in the objects are ’mutable’). Let’s work through an example where we set up the fields of the class (like S4 slots) and class methods, including a constructor.

Here’s the initial definition of the class, with both public (user-facing) and private (internal use only) methods and fields.

**library** (R6) tsSimClass <- **R6Class** ("tsSimClass", _## class for holding time series simulators_ public = **list** ( initialize = **function** (times, mean = 0, corParam = 1){ **library** (fields) **stopifnot** ( **is.numeric** (corParam), **length** (corParam) == 1) **stopifnot** ( **is.numeric** (times)) private$times <- times

32

private$n <- **length** (times) private$mean <- mean private$corParam <- corParam private$currentU <- FALSE private$ **calcMats** () }, changeTimes = **function** (newTimes){ private$times <- newTimes private$ **calcMats** () }, getTimes = **function** (){ **return** (private$times) }, print = **function** (){ _# 'print' method_ **cat** ("R6 Object of class 'tsSimClass' with ", private$n, " time points.\n", sep = '') **invisible** (self) } ), _## private methods and functions not accessible externally_ private = **list** ( calcMats = **function** () { _## calculates correlation matrix and Cholesky factor_ lagMat <- fields:: **rdist** (private$times) _# local variable_ corMat <- **exp** (-lagMat^2 / private$corParam^2) private$U <- **chol** (corMat) _# square root matrix_ **cat** ("Done updating correlation matrix and Cholesky factor.\n") private$currentU <- TRUE **invisible** (self) }, n = **NULL** , times = **NULL** ,

33

mean = **NULL** , corParam = **NULL** , U = **NULL** , currentU = FALSE ) )

We can add methods after defining the class (but those methods wouldn’t be accessible to objects of the class that have already been created.

tsSimClass$ **set** ("public", "simulate", **function** () { **if** (!private$currentU) private$ **calcMats** () _## analogous to mu+sigma*z for generating N(mu, sigma^2)_ **return** (private$mean + **crossprod** (private$U, **rnorm** (private$n))) })

Now let’s see how we would use the class.

master <- tsSimClass$ **new** (1:100, 2, 1) _## Loading required package: spam ## Loading required package: dotCall64 ## Loading required package: grid ## Spam version 2.2-2 (2019-03-07) is loaded. ## Type ’help( Spam)’ or ’demo( spam)’ for a short introduction ## and overview of this package. ## Help for individual functions is also obtained by adding the ## suffix ’.spam’ to the function name, e.g. ’help( chol.spam)’. ## ## Attaching package: ’spam’ ## The following objects are masked from ’package:base’: ## ## backsolve, forwardsolve ## Loading required package: maps ## See https://github.com/NCAR/Fields for ## an extensive vignette, other supplements and source code_

34

---

[← Bear of age 20 whose name is Yogi the Bear.](24-bear-of-age-20-whose-name-is-yogi-the-bear.md) · [Up: contents](index.md) · [Done updating correlation matrix and Cholesky factor. master →](26-done-updating-correlation-matrix-and-cholesky-factor-master.md)
