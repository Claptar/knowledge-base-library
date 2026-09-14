---
title: '[1] TRUE'
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] TRUE

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For a more relevant example suppose we had spatially-indexed time series. We could have a time series class, a spatial location class, and a “location time series” class that inherits from both. Be careful that there are not conflicts in the slots or methods from the multiple classes. For conflicting methods, you can define a method specific to the new class to deal with this. Also, if you define your own _initialize()_ method, you’ll need to be careful that you account for any initialization of the superclass(es) and for any classes that might inherit from your class (see help on _new()_ and Chambers, p. 360).

You can inherit from other S4 classes (which need to be defined or imported into the environment in which your class is created), but not S3 classes. You can inherit (at most one) of the basic R types, but not environments, symbols, or other non-standard types. You can use S3 classes in slots, but this requires that the S3 class be declared as an S4 class. To do this, you create S4 versions of S3 classes use _setOldClass()_ - this creates a virtual class. This has been done, for example, for the _data.frame_ class:

**showClass** ("data.frame") ## Class "data.frame" [package "methods"] ## ## Slots: ## ## Name: .Data names ## Class: list character ## ## Name: row.names .S3Class ## Class: data.frameRowLabels character ## ## Extends: ## Class "list", from data part ## Class "oldClass", directly ## Class "vector", by class "list", distance 2

31

You can use _setClassUnion()_ to create what Adler calls _superclass_ and what Chambers calls a _virtual class_ that allows for methods that apply to multiple classes. So if you have a person class and a pet class, you could create a “named lifeform” virtual class that has methods for working with name and age slots, since both people and pets would have those slots. You can’t directly create an object in the virtual class.

#### **4.4.3 Reference classes**

Reference classes are a new construct in R. They are classes somewhat similar to S4 that allow us to access their fields by reference. Importantly, they behave like pointers (the fields in the objects are ’mutable’). Let’s work through an example where we set up the fields of the class (like S4 slots) and class methods, including a constructor. Note that one cannot add fields to an already existing class.

Here’s the initial definition of the class.

tsSimClass <- **setRefClass** ("tsSimClass", fields = **list** ( n = "numeric", times = "numeric", corMat = "matrix", corParam = "numeric", U = "matrix", currentU = "logical"), methods = **list** ( initialize = **function** (times = 1:10, corParam = 1, ...){ _## we seem to need default values for the copy() method ## to function properly_ **require** (fields) times <<- times _# field assignment requires using <<-_ n <<- **length** (times) corParam <<- corParam currentU <<- FALSE **calcMats** () **callSuper** (...) _# calls initializer of base class (envRefClass)_ },

32

calcMats = **function** (){ _## Python-style doc string_ ' calculates correlation matrix and Cholesky factor ' lagMat <- **rdist** (times) _# local variable_ corMat <<- **exp** (-lagMat / corParam) _# field assignment_ U <<- **chol** (corMat) _# field assignment_ **cat** ("Done updating correlation matrix and Cholesky factor\n") currentU <<- TRUE }, changeTimes = **function** (newTimes){ times <<- newTimes **calcMats** () }, show = **function** (){ _# 'print' method_ **cat** ("Object of class 'tsSimClass' with ", n, " time points.\n", sep = '') } ) )

We can add methods after defining the class.

tsSimClass$ **methods** ( **list** ( simulate = **function** (){ ' simulates random processes from the model ' **if** (!currentU) **calcMats** () **return** ( **crossprod** (U, **rnorm** (n))) }) )

Now let’s see how we would use the class.

33

master <- tsSimClass$ **new** (1:100, 10) master tsSimClass$ **help** ('calcMats') devs <- master$ **simulate** () **plot** (master$times, devs, type = 'l') mycopy <- master myDeepCopy <- master$ **copy** () master$ **changeTimes** ( **seq** (0,1, length = 100)) mycopy$times[1:5] myDeepCopy$times[1:5]

A few additional points:

- As we just saw, a copy of an object is just a pointer to the original object, unless we explicitly invoke the _copy()_ method.

- As with S3 and S4, classes can inherit from other classes. E.g., if we had a _simClass_ and we wanted the _tsSimClass_ to inherit from it:

setRefClass("tsSimClass", contains = "simClass")

   - We can call a method inherited from the superclass from within a method of the same name with _callSuper(...)_ , as we saw for our _initialize()_ method.

- If we need to refer to a field or change a field we can do so without hard-coding the field name as:

master$ **field** ('times')[1:5] _## the next line is dangerous in this case, since ## currentU will no longer be accurate_ master$ **field** ('times', 1:10)

- Note that reference classes have Python style doc strings. We get help on a class with _class$help()_ , e.g. tsSimClass$help(). This prints out information, including the doc strings.

- If you need to refer to the entire object within an object method, you refer to it as _.self_ . E.g., with our _tsSimClass_ object, .self$U would refer to the Cholesky factor. This is sometimes necessary to distinguish a class field from an argument to a method.

34

- There is a new, more efficient version of ReferenceClasses call R6 classes. See the _R6_ package.

---

[← Unit 04 — programming Part 26 —](26-unit-04-programming-part-26.md) · [Up: contents](index.md) · [5 Standard dataset manipulations →](28-5-standard-dataset-manipulations.md)
