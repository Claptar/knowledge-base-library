---
title: Unit 04 — programming partial Part 29 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 29 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can use setClassUnion() to create what Adler calls superclass and what Chambers calls a virtual class that allows for methods that apply to multiple classes. So if you have a person class and a pet class, you could create a “named lifeform” virtual class that has methods for working with name and age slots, since both people and pets would have those slots. You can’t directly create an object in the virtual class.

#### 4.4.3 R6 classes

R6 classes are a new construct in R. They are classes somewhat similar to S4. Importantly, they behave like pointers (the fields in the objects are ’mutable’). Let’s work through an example where we set up the fields of the class (like S4 slots) and class methods, including a constructor.

Here’s the initial definition of the class, with both public (user-facing) and private (internal use only) methods and fields.

**library** (R6) tsSimClass <- **R6Class** ("tsSimClass", ## class for holding time series simulators public = **list** ( initialize = **function** (times, mean = 0, corParam = 1){

31

**library** (fields) **stopifnot** ( **is.numeric** (corParam), **length** (corParam) == 1) **stopifnot** ( **is.numeric** (times)) private$times <- times private$n <- **length** (times) private$mean <- mean private$corParam <- corParam private$currentU <- FALSE private$ **calcMats** () }, changeTimes = **function** (newTimes){ private$times <- newTimes private$ **calcMats** () }, getTimes = **function** (){ **return** (private$times) }, print = **function** (){ # 'print' method **cat** ("R6 Object of class 'tsSimClass' with ", private$n, " time points.\n", sep = '') **invisible** (self) } ), ## private methods and functions not accessible externally private = **list** ( calcMats = **function** () { ## calculates correlation matrix and Cholesky factor lagMat <- fields:: **rdist** (private$times) # local variable corMat <- **exp** (-lagMat^2 / private$corParam^2) private$U <- **chol** (corMat) # square root matrix **cat** ("Done updating correlation matrix and Cholesky factor.\n") private$currentU <- TRUE

32

**invisible** (self) }, n = **NULL** , times = **NULL** , mean = **NULL** , corParam = **NULL** , U = **NULL** , currentU = FALSE ) )

We can add methods after defining the class (but those methods wouldn’t be accessible to objects of the class that have already been created.

tsSimClass$ **set** ("public", "simulate", **function** () { **if** (!private$currentU) private$ **calcMats** () ## analogous to mu+sigma*z for generating N(mu, sigma^2) **return** (private$mean + **crossprod** (private$U, **rnorm** (private$n))) })

Now let’s see how we would use the class.

master <- tsSimClass$ **new** (1:100, 2, 1)

---

[← Unit 04 — programming partial Part 28 —](28-unit-04-programming-partial-part-28.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 30 — →](30-unit-04-programming-partial-part-30.md)
