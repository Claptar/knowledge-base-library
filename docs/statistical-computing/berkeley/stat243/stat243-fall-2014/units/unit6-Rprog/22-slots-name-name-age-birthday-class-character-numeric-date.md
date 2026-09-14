---
title: 'Slots: ## ## Name: name age birthday ## Class: character numeric Date'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Slots: ## ## Name: name age birthday ## Class: character numeric Date

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

sam <- **new** ("bear", name = "5z%a", age = 20, birthday = **as.Date** ("91-08-03")) **## Error: invalid class "bear" object: error: name contains digits** sam <- **new** ("bear", name = "Z%a B''*", age = 20, birthday = **as.Date** ("91-08-03" sam@age <- 150 _# so our validity check is not foolproof_

To deal with this latter issue of the user mucking with the slots, it’s recommended when using OOP that slots only be accessible through methods that operate on the object, e.g., a _setAge()_ method, and then check the validity of the supplied age within _setAge()_ .

Here’s how we create generic and class-specific methods. Note that in some cases the generic will already exist.

_# generic method_ **setGeneric** ("isVoter", **function** (object, ...) { **standardGeneric** ("isVoter") }) ## [1] "isVoter" _# class-specific method_ isVoter.bear <- **function** (object) { **if** (object@age > 17) { **cat** (object@name, "is of voting age.\n") } **else cat** (object@name, "is not of voting age.\n") } **setMethod** (isVoter, signature = **c** ("bear"), definition = isVoter.bear) ## [1] "isVoter" ## attr(,"package") ## [1] ".GlobalEnv" **isVoter** (yog) ## Yogi is of voting age.

46

We can have method signatures involve multiple objects. Here’s some syntax where we’d fill in the function body with appropriate code - perhaps the plus operator would create a child. setMethod(‘+‘, signature = c("bear", "bear"), definition = function(bear1, bear2) { }

As with S3, classes can inherit from one or more other classes. Chambers calls the class that is being inherited from a _superclass_ .

**setClass** ("grizzly_bear", **representation** ( number_of_people_eaten = "numeric" ), contains = "bear" ) sam <- **new** ("grizzly_bear", name = "Sam", age = 20, birthday = **as.Date** ('91-08-03'), number_of_people_eaten = 3) **isVoter** (sam) ## Sam is of voting age. **is** (sam, "bear") ## [1] TRUE

For a more relevant example suppose we had spatially-indexed time series. We could have a time series class, a spatial location class, and a “location time series” class that inherits from both. Be careful that there are not conflicts in the slots or methods from the multiple classes. For conflicting methods, you can define a method specific to the new class to deal with this. Also, if you define your own _initialize()_ method, you’ll need to be careful that you account for any initialization of the superclass(es) and for any classes that might inherit from your class (see help on _new()_ and Chambers, p. 360).

You can inherit from other S4 classes (which need to be defined or imported into the environment in which your class is created), but not S3 classes. You can inherit (at most one) of the basic R types, but not environments, symbols, or other non-standard types. You can use S3 classes in slots, but this requires that the S3 class be declared as an S4 class. To do this, you create S4 versions of S3 classes use _setOldClass()_ - this creates a virtual class. This has been done, for example, for the _data.frame_ class:

47

**showClass** ("data.frame") ## Class "data.frame" [package "methods"] ## ## Slots: ## ## Name: .Data names row.names ## Class: list character data.frameRowLabels ## ## Name: .S3Class ## Class: character ## ## Extends: ## Class "list", from data part ## Class "oldClass", directly ## Class "vector", by class "list", distance 2

You can use _setClassUnion()_ to create what Adler calls _superclass_ and what Chambers calls a _virtual class_ that allows for methods that apply to multiple classes. So if you have a person class and a pet class, you could create a “named lifeform” virtual class that has methods for working with name and age slots, since both people and pets would have those slots. You can’t directly create an object in the virtual class.

### **4.3 Reference classes**

Reference classes are a new construct in R. They are classes somewhat similar to S4 that allow us to access their fields by reference. Importantly, they behave like pointers (the fields in the objects are ’mutable’). Let’s work through an example where we set up the fields of the class (like S4 slots) and class methods, including a constructor. Note that one cannot add fields to an already existing class.

Here’s the initial definition of the class.

tsSimClass <- **setRefClass** ("tsSimClass", fields = **list** ( n = "numeric", times = "numeric", corMat = "matrix",

48

lagMat = "matrix", corParam = "numeric", U = "matrix", currentU = "logical"), methods = **list** ( initialize = **function** (times = 1:10, corParam = 1, ...){ _# we seem to need default values for the copy()_ **require** (fields) times <<- times _# field assignment requires using_ n <<- **length** (times) corParam <<- corParam currentU <<- FALSE **calcMats** () **callSuper** (...) _# calls initializer of base class_ }, calcMats = **function** (){ _# Python-style doc string_ ' calculates correlation matrix and Cholesky factor lagMat <- **rdist** (times) _# local variable_ corMat <<- **exp** (-lagMat / corParam) _# field assignment_ U <<- **chol** (corMat) _# field assignment_ **cat** ("Done updating correlation matrix and Cholesky currentU <<- TRUE }, changeTimes = **function** (newTimes){ times <<- newTimes **calcMats** () }, show = **function** (){ _# 'print' method_ **cat** ("Object of class 'tsSimClass' with ", n, " time } )

49

) ## Warning: local assignment to field name will not change the field: ## lagMat <- rdist(times) ## Did you mean to use "«-"? ( in method "calcMats" for class "tsSimClass")

We can add methods after defining the class.

tsSimClass$ **methods** ( **list** ( simulate = **function** (){ ' simulates random processes from the model ' **if** (!currentU) **calcMats** () **return** ( **crossprod** (U, **rnorm** (n))) }) )

Now let’s see how we would use the class.

master <- tsSimClass$ **new** (1:100, 10) master tsSimClass$ **help** ("calcMats") devs <- master$ **simulate** () **plot** (master$times, devs, type = "l") mycopy <- master myDeepCopy <- master$ **copy** () master$ **changeTimes** ( **seq** (0, 1, length = 100)) mycopy$times[1:5] myDeepCopy$times[1:5]

A few additional points:

- As we just saw, a copy of an object is just a pointer to the original object, unless we explicitly invoke the _copy()_ method.

- As with S3 and S4, classes can inherit from other classes. E.g., if we had a _simClass_ and we wanted the _tsSimClass_ to inherit from it:

setRefClass("tsSimClass", contains = "simClass")

50

   - We can call a method inherited from the superclass from within a method of the same name with _callSuper(...)_ , as we saw for our _initialize()_ method.

- If we need to refer to a field or change a field we can do so without hard-coding the field name as:

master$ **field** ("times")[1:5]

_# the next line is dangerous in this case, since currentU will no longer be # accurate_ master$ **field** ("times", 1:10)

- Note that reference classes have Python style doc strings. We get help on a class with _class$help()_ , e.g. tsSimClass$help(). This prints out information, including the doc strings.

- If you need to refer to the entire object within an object method, you refer to it as _.self_ . E.g., with our _tsSimClass_ object, .self$U would refer to the Cholesky factor. This is sometimes necessary to distinguish a class field from an argument to a method.

---

[← Bear of age 20 whose name is Yogi the Bear.](21-bear-of-age-20-whose-name-is-yogi-the-bear.md) · [Up: contents](index.md) · [5 Creating and working in an environment →](23-5-creating-and-working-in-an-environment.md)
