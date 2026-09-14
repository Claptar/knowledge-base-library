---
title: Unit 04 — programming Part 22 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 22 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

28

sam <- **new** ("bear", name = "Z%a B''*", age = 20, birthday = **as.Date** ('91-08-03')) sam@age <- 150 _# so our validity check is not foolproof_

To deal with this latter issue of the user mucking with the slots, it’s recommended when using OOP that slots only be accessible through methods that operate on the object, e.g., a _setAge()_ method, and then check the validity of the supplied age within _setAge()_ .

Here’s how we create generic and class-specific methods. Note that in some cases the generic will already exist.

_## generic method_ **setGeneric** ("isVoter", **function** (object, ...) { **standardGeneric** ("isVoter") }) ## [1] "isVoter" _# class-specific method_ isVoter.bear <- **function** (object){ **if** (object@age > 17){ **cat** (object@name, "is of voting age.\n") } **else cat** (object@name, "is not of voting age.\n") } **setMethod** (isVoter, signature = **c** ("bear"), definition = isVoter.bear) ## [1] "isVoter" ## attr(,"package") ## [1] ".GlobalEnv" **isVoter** (yog) ## Yogi is of voting age.

We can have method signatures involve multiple objects. Here’s some syntax where we’d fill in the function body with appropriate code - perhaps the plus operator would create a child.

29

**setMethod** (`+`, signature = **c** ("bear", "bear"), definition = **function** (bear1, bear2) { _## method code goes here_ }

As with S3, classes can inherit from one or more other classes. Chambers calls the class that is being inherited from a _superclass_ .

**setClass** ("grizzly_bear", **representation** ( number_of_people_eaten = "numeric" ), contains = "bear" ) sam <- **new** ("grizzly_bear", name = "Sam", age = 20, birthday = **as.Date** ('91-08-03'), number_of_people_eaten = 3) **isVoter** (sam) ## Sam is of voting age. **is** (sam, "bear") ## [1] TRUE

For a more relevant example suppose we had spatially-indexed time series. We could have a time series class, a spatial location class, and a “location time series” class that inherits from both. Be careful that there are not conflicts in the slots or methods from the multiple classes. For conflicting methods, you can define a method specific to the new class to deal with this. Also, if you define your own _initialize()_ method, you’ll need to be careful that you account for any initialization of the superclass(es) and for any classes that might inherit from your class (see help on _new()_ and Chambers, p. 360).

You can inherit from other S4 classes (which need to be defined or imported into the environment in which your class is created), but not S3 classes. You can inherit (at most one) of the basic R types, but not environments, symbols, or other non-standard types. You can use S3 classes in slots, but this requires that the S3 class be declared as an S4 class. To do this, you create S4 versions of S3 classes use _setOldClass()_ - this creates a virtual class. This has been done, for example, for the _data.frame_ class:

30

**showClass** ("data.frame") ## Class "data.frame" [package "methods"] ## ## Slots: ## ## Name: .Data names ## Class: list character ## ## Name: row.names .S3Class ## Class: data.frameRowLabels character ## ## Extends: ## Class "list", from data part ## Class "oldClass", directly ## Class "vector", by class "list", distance 2

You can use _setClassUnion()_ to create what Adler calls _superclass_ and what Chambers calls a _virtual class_ that allows for methods that apply to multiple classes. So if you have a person class and a pet class, you could create a “named lifeform” virtual class that has methods for working with name and age slots, since both people and pets would have those slots. You can’t directly create an object in the virtual class.

#### **4.4.3 R6 classes**

R6 classes are a new construct in R. They are classes somewhat similar to S4. Importantly, they behave like pointers (the fields in the objects are ’mutable’). Let’s work through an example where we set up the fields of the class (like S4 slots) and class methods, including a constructor.

Here’s the initial definition of the class, with both public (user-facing) and private (internal use only) methods and fields.

**library** (R6) tsSimClass <- **R6Class** ("tsSimClass", _## class for holding time series simulators_ public = **list** ( initialize = **function** (times, mean = 0, corParam = 1){

31

**library** (fields) **stopifnot** ( **is.numeric** (corParam), **length** (corParam) == 1) **stopifnot** ( **is.numeric** (times)) private$times <- times private$n <- **length** (times) private$mean <- mean private$corParam <- corParam private$currentU <- FALSE private$ **calcMats** () }, changeTimes = **function** (newTimes){ private$times <- newTimes private$ **calcMats** () }, getTimes = **function** (){ **return** (private$times) }, print = **function** (){ _# 'print' method_ **cat** ("R6 Object of class 'tsSimClass' with ", private$n, " time points.\n", sep = '') **invisible** (self) } ), _## private methods and functions not accessible externally_ private = **list** ( calcMats = **function** () { _## calculates correlation matrix and Cholesky factor_ lagMat <- fields:: **rdist** (private$times) _# local variable_ corMat <- **exp** (-lagMat^2 / private$corParam^2) private$U <- **chol** (corMat) _# square root matrix_ **cat** ("Done updating correlation matrix and Cholesky factor.\n") private$currentU <- TRUE

32

**invisible** (self) }, n = **NULL** , times = **NULL** , mean = **NULL** , corParam = **NULL** , U = **NULL** , currentU = FALSE ) )

We can add methods after defining the class (but those methods wouldn’t be accessible to objects of the class that have already been created.

tsSimClass$ **set** ("public", "simulate", **function** () { **if** (!private$currentU) private$ **calcMats** () _## analogous to mu+sigma*z for generating N(mu, sigma^2)_ **return** (private$mean + **crossprod** (private$U, **rnorm** (private$n))) })

Now let’s see how we would use the class.

master <- tsSimClass$ **new** (1:100, 2, 1)

- _## Loading required package: spam ## Loading required package: dotCall64 ## Loading required package: grid ## Spam version 2.1-4 (2018-04-12) is loaded. ## Type ’help( Spam)’ or ’demo( spam)’ for a short introduction ## and overview of this package. ## Help for individual functions is also obtained by adding the ## suffix ’.spam’ to the function name, e.g. ’help( chol.spam)’. ## ## Attaching package: ’spam’ ## The following objects are masked from ’package:base’: ## ## backsolve, forwardsolve_

33

_## Loading required package: maps ## See www.image.ucar.edu/~nychka/Fields ## a vignette and other supplements._

_## See www.image.ucar.edu/~nychka/Fields for_

---

[← Bear of age 20 whose name is Yogi the Bear.](21-bear-of-age-20-whose-name-is-yogi-the-bear.md) · [Up: contents](index.md) · [Done updating correlation matrix and Cholesky factor. master →](23-done-updating-correlation-matrix-and-cholesky-factor-master.md)
