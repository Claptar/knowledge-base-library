---
title: Bear of age 20 whose name is Yogi the Bear.
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Bear of age 20 whose name is Yogi the Bear.

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The classes should nest within one another with the more specific classes to the left, e.g., here a _grizzly_bear_ would have some additional objects on top of those of a _bear_ , perhaps _number_of_people_eaten_ (since grizzly bears are much more dangerous than some other kinds of bears), and perhaps additional or modified methods. _grizzly_bear_ inherits from _bear_ , and R uses methods for the first class before methods for the next class(es), unless no such method is defined for the first class. If no methods are defined for any of the classes, R looks for _method.default()_ , e.g., _print.default()_ , _plot.default()_ , etc..

**Class-specific operators** We can also use operators with our classes. The following example will be a bit silly (it would make more sense with a class that is a mathematical object) but indicates the power of having methods.

26

**methods** (`+`) ## [1] +.Date +.glue* +.POSIXt ## see '?methods' for accessing help and source code `+.bear` <- **function** (object, incr) { object$age <- object$age + incr **return** (object) } older_yog <- yog + 15

**Class-specific replacement functions** We can use replacement functions with our classes. For more on what a replacement function is, see Section 6.6.

This is again a bit silly but we could do the following. We need to define the generic replacement function and then the class-specific one.

`age<-` <- **function** (x, ...) **UseMethod** ("age<-") `age<-.bear` <- **function** (object, value){ object$age <- value **return** (object) } **age** (older_yog) <- 60

**Why use class-specific methods?** We could have implemented different functionality (e.g., for _summary()_ ) for different objects using a bunch of _if_ statements (or _switch()_ ) to figure out what class of object is the input, but then we need to have all that checking. Furthermore, we don’t control the _summary()_ function, so we would have no way of adding the additional conditions in a big if-else statement. The OOP framework makes things _extensible_ , so we can build our own new functionality on what is already in R.

**Final thoughts** Consider the _Date_ class discussed in the R bootcamp. This is another example of an S3 class, with methods such as _julian()_ , _weekdays()_ , etc.

**Challenge** : how would you get R to quit immediately, without asking for any more information, when you simply type ’k’ (no parentheses!) instead of ’ _quit()_ ’?

27

What we’ve just discussed are the old-style R (and S) object orientation, called S3 methods. An old, but somewhat newer style is called S4 and we’ll discuss it next. S3 is still commonly used, in part because S4 can be slow. S4 is more structured than S3.

#### **4.4.2 S4 approach**

S4 methods are used a lot in _bioconductor_ , a project that provides a lot of bioinformatics-related code. They’re also used in _lme4_ , among other packages. Tools for working with S4 classes are in the _methods_ package.

Note that components of S4 objects are obtained as object@component so they do not use the usual list syntax. The components are called _slots_ , and there is careful checking that the slots are specified and valid when a new object of a class is created. You can use the _prototype_ argument to _setClass()_ to set default values for the slots. There is a default constructor (the method is actually called _initialize()_ ), but you can modify it. One can create methods for operators and for replacement functions too. For S4 classes, there is a default method invoked when _print()_ is called on an object in the class (either explicitly or implicitly) - the method is actually called _show()_ and it can also be modified. Let’s reconsider our _bear_ class example in the S4 context.

**library** (methods) **setClass** ("bear", **representation** ( name = "character", age = "numeric", birthday = "Date" ) ) yog <- **new** ("bear", name = 'Yogi', age = 20, birthday = **as.Date** ('91-08-03')) _## next notice the missing age slot_ yog <- **new** ("bear", name = 'Yogi', birthday = **as.Date** ('91-08-03')) _## finally, apparently there's not a default object of class Date_ yog <- **new** ("bear", name = 'Yogi', age = 20) **## Error in validObject(.Object): invalid class "bear" object: invalid**

28

**object for slot "birthday" in class "bear": got class "S4", should be or extend class "Date"**

yog ## An object of class "bear" ## Slot "name": ## [1] "Yogi" ## ## Slot "age": ## numeric(0) ## ## Slot "birthday": ## [1] "91-08-03" yog@age <- 60 S4 methods are designed to be more structured than S3, with careful checking of the slots. **setValidity** ("bear", **function** (object) { **if** (!(object@age > 0 && object@age < 130)) **return** ("error: age must be between 0 and 130") **if** ( **length** ( **grep** ("[0-9]", object@name))) **return** ("error: name contains digits") **return** (TRUE) _# what other validity check would make sense given the slots?_ } ) ## Class "bear" [in ".GlobalEnv"] ## ## Slots: ## ## Name: name age birthday ## Class: character numeric Date sam <- **new** ("bear", name = "5z%a", age = 20, birthday = **as.Date** ('91-08-03'))

29

**## Error in validObject(.Object): invalid class "bear" object: error: name contains digits** sam <- **new** ("bear", name = "Z%a B''*", age = 20, birthday = **as.Date** ('91-08-03')) sam@age <- 150 _# so our validity check is not foolproof_

To deal with this latter issue of the user mucking with the slots, it’s recommended when using OOP that slots only be accessible through methods that operate on the object, e.g., a _setAge()_ method, and then check the validity of the supplied age within _setAge()_ .

Here’s how we create generic and class-specific methods. Note that in some cases the generic will already exist.

_## generic method_ **setGeneric** ("isVoter", **function** (object, ...) { **standardGeneric** ("isVoter") }) ## [1] "isVoter" _# class-specific method_ isVoter.bear <- **function** (object){ **if** (object@age > 17){ **cat** (object@name, "is of voting age.\n") } **else cat** (object@name, "is not of voting age.\n") } **setMethod** (isVoter, signature = **c** ("bear"), definition = isVoter.bear) **isVoter** (yog) ## Yogi is of voting age.

We can have method signatures involve multiple objects. Here’s some syntax where we’d fill in the function body with appropriate code - perhaps the plus operator would create a child.

**setMethod** (`+`, signature = **c** ("bear", "bear"), definition = **function** (bear1, bear2) { _## method code goes here_ }

30

As with S3, classes can inherit from one or more other classes. Chambers calls the class that is being inherited from a _superclass_ .

**setClass** ("grizzly_bear", **representation** ( number_of_people_eaten = "numeric" ), contains = "bear" ) sam <- **new** ("grizzly_bear", name = "Sam", age = 20, birthday = **as.Date** ('91-08-03'), number_of_people_eaten = 3) **isVoter** (sam) ## Sam is of voting age. **is** (sam, "bear") ## [1] TRUE

For a more relevant example suppose we had spatially-indexed time series. We could have a time series class, a spatial location class, and a “location time series” class that inherits from both. Be careful that there are not conflicts in the slots or methods from the multiple classes. For conflicting methods, you can define a method specific to the new class to deal with this. Also, if you define your own _initialize()_ method, you’ll need to be careful that you account for any initialization of the superclass(es) and for any classes that might inherit from your class (see help on _new()_ and Chambers, p. 360).

You can inherit from other S4 classes (which need to be defined or imported into the environment in which your class is created), but not S3 classes. You can inherit (at most one) of the basic R types, but not environments, symbols, or other non-standard types. You can use S3 classes in slots, but this requires that the S3 class be declared as an S4 class. To do this, you create S4 versions of S3 classes use _setOldClass()_ - this creates a virtual class. This has been done, for example, for the _data.frame_ class:

**showClass** ("data.frame") ## Class "data.frame" [package "methods"] ##

31

---

[← Unit 05 — programming Part 23 —](23-unit-05-programming-part-23.md) · [Up: contents](index.md) · [Unit 05 — programming Part 25 — →](25-unit-05-programming-part-25.md)
