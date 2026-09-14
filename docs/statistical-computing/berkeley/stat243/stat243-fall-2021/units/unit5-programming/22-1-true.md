---
title: '[1] TRUE'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] TRUE

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For a more relevant example suppose we had spatially-indexed time series. We could have a time series class, a spatial location class, and a “location time series” class that inherits from both. Be careful that there are not conflicts in the slots or methods from the multiple classes. For conflicting methods, you can define a method specific to the new class to deal with this. Also, if you define your own _initialize()_ method, you’ll need to be careful that you account for any initialization of the superclass(es) and for any classes that might inherit from your class (see help on _new()_ and Chambers, p. 360).

You can inherit from other S4 classes (which need to be defined or imported into the environment in which your class is created), but not S3 classes. You can inherit (at most one) of the basic R types, but not environments, symbols, or other non-standard types. You can use S3 classes in slots, but this requires that the S3 class be declared as an S4 class. To do this, you create S4 versions of S3 classes use _setOldClass()_ - this creates a virtual class. This has been done, for example, for the _data.frame_ class:

**showClass** ("data.frame") ## Class "data.frame" [package "methods"] ## ## Slots: ## ## Name: .Data names ## Class: list character ## ## Name: row.names .S3Class ## Class: data.frameRowLabels character ## ## Extends: ## Class "list", from data part ## Class "oldClass", directly ## Class "vector", by class "list", distance 2

32

You can use _setClassUnion()_ to create what Adler calls _superclass_ and what Chambers calls a _virtual class_ that allows for methods that apply to multiple classes. So if you have a person class and a pet class, you could create a “named lifeform” virtual class that has methods for working with name and age slots, since both people and pets would have those slots. You can’t directly create an object in the virtual class.

#### **4.4.3 R6 classes**

R6 classes are a somewhat new construct in R. They are classes somewhat similar to S4. Importantly, they behave like pointers (the fields in the objects are ’mutable’). We’ll discuss pointers in Section 6.5. Let’s work through an example where we set up the fields of the class (like S4 slots) and class methods, including a constructor.

Here’s the initial definition of the class, with both public (user-facing) and private (internal use only) methods and fields.

**library** (R6) tsSimClass <- **R6Class** ("tsSimClass", _## class for holding time series simulators_ public = **list** ( initialize = **function** (times, mean = 0, corParam = 1){ **library** (fields) **stopifnot** ( **is.numeric** (corParam), **length** (corParam) == 1) **stopifnot** ( **is.numeric** (times)) private$times <- times private$n <- **length** (times) private$mean <- mean private$corParam <- corParam private$currentU <- FALSE private$ **calcMats** () }, changeTimes = **function** (newTimes){ private$times <- newTimes private$ **calcMats** () },

33

getTimes = **function** (){ **return** (private$times) }, print = **function** (){ _# 'print' method_ **cat** ("R6 Object of class 'tsSimClass' with ", private$n, " time points.\n", sep = '') **invisible** (self) } ), _## private methods and functions not accessible externally_ private = **list** ( calcMats = **function** () { _## calculates correlation matrix and Cholesky factor_ lagMat <- fields:: **rdist** (private$times) _# local variable_ corMat <- **exp** (-lagMat^2 / private$corParam^2) private$U <- **chol** (corMat) _# square root matrix_ **cat** ("Done updating correlation matrix and Cholesky factor.\n") private$currentU <- TRUE **invisible** (self) }, n = **NULL** , times = **NULL** , mean = **NULL** , corParam = **NULL** , U = **NULL** , currentU = FALSE ) )

We can add methods after defining the class (but those methods wouldn’t be accessible to objects of the class that have already been created.

tsSimClass$ **set** ("public", "simulate", **function** () { **if** (!private$currentU)

34

private$ **calcMats** () _## analogous to mu+sigma*z for generating N(mu, sigma^2)_ **return** (private$mean + **crossprod** (private$U, **rnorm** (private$n))) })

That’s just for demonstration. In general we would define _simulate_ when we define the class originally.

Now let’s see how we would use the class.

myts <- tsSimClass$ **new** (1:100, 2, 1)

- _## Loading required package: spam ## Loading required package: dotCall64 ## Loading required package: grid ## Spam version 2.6-0 (2020-12-14) is loaded. ## Type ’help( Spam)’ or ’demo( spam)’ for a short introduction_

- _## and overview of this package. ## Help for individual functions is also obtained by adding the ## suffix ’.spam’ to the function name, e.g. ’help( chol.spam)’. ##_

- _## Attaching package: ’spam’ ## The following objects are masked from ’package:base’: ## ## backsolve, forwardsolve ## Loading required package: viridis ## Loading required package: viridisLite ## See https://github.com/NCAR/Fields for_

- _## an extensive vignette, other supplements and source code_

- ## Done updating correlation matrix and Cholesky factor.

myts

---

[← Bear of age 20 whose name is Yogi the Bear.](21-bear-of-age-20-whose-name-is-yogi-the-bear.md) · [Up: contents](index.md) · [R6 Object of class 'tsSimClass' with 100 time points. →](23-r6-object-of-class-tssimclass-with-100-time-points.md)
