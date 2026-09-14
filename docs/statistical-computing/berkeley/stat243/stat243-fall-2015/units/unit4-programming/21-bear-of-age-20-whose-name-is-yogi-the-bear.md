---
title: Bear of age 20 whose name is Yogi the Bear.
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Bear of age 20 whose name is Yogi the Bear.

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The classes should nest within one another with the more specific classes to the left, e.g., here a _grizzly_bear_ would have some additional objects on top of those of a _bear_ , perhaps _number_of_people_eaten_ (since grizzly bears are much more dangerous than some other kinds of bears), and perhaps additional or modified methods. _grizzly_bear_ inherits from _bear_ , and R uses methods for the first class before methods for the next class(es), unless no such method is defined for the first class. If no methods are defined for any of the classes, R looks for _method.default()_ , e.g., _print.default()_ , _plot.default()_ , etc..

**Class-specific operators** We can also use operators with our classes. The following example will be a bit silly (it would make more sense with a class that is a mathematical object) but indicates the power of having methods.

**methods** (`+`) ## [1] +.Date +.POSIXt ## [3] +,spam,missing-method +,spam,spam-method ## see '?methods' for accessing help and source code

24

`+.bear` <- **function** (object, incr) { object$age <- object$age + incr **return** (object) } older_yog <- yog + 15

**Class-specific replacement functions** We can use replacement functions with our classes. For more on what a replacement function is, see Section 6.6.

This is again a bit silly but we could do the following. We need to define the generic replacement function and then the class-specific one.

`age<-` <- **function** (x, ...) **UseMethod** ("age<-") `age<-.bear` <- **function** (object, value){ object$age <- value **return** (object) } **age** (older_yog) <- 60

**Why use class-specific methods?** We could have implemented different functionality (e.g., for _summary()_ ) for different objects using a bunch of _if_ statements (or _switch()_ ) to figure out what class of object is the input, but then we need to have all that checking. Furthermore, we don’t control the _summary()_ function, so we would have no way of adding the additional conditions in a big if-else statement. The OOP framework makes things _extensible_ , so we can build our own new functionality on what is already in R.

**Final thoughts** Consider the _Date_ class discussed in the R bootcamp. This is another example of an S3 class, with methods such as _julian()_ , _weekdays()_ , etc.

**Challenge** : how would you get R to quit immediately, without asking for any more information, when you simply type ’ _q_ ’ (no parentheses!)?

What we’ve just discussed are the old-style R (and S) object orientation, called S3 methods. The new style is called S4 and we’ll discuss it next. S3 is still commonly used, in part because S4 can be slow (or at least it was when I last looked into this a few years ago). S4 is more structured than S3.

25

#### **4.4.2 S4 approach**

S4 methods are used a lot in _bioconductor_ , a project that provides a lot of bioinformatics-related code. They’re also used in _lme4_ , among other packages. Tools for working with S4 classes are in the _methods_ package.

Note that components of S4 objects are obtained as object@component so they do not use the usual list syntax. The components are called _slots_ , and there is careful checking that the slots are specified and valid when a new object of a class is created. You can use the _prototype_ argument to _setClass()_ to set default values for the slots. There is a default constructor (the method is actually called _initialize()_ ), but you can modify it. One can create methods for operators and for replacement functions too. For S4 classes, there is a default method invoked when _print()_ is called on an object in the class (either explicitly or implicitly) - the method is actually called _show()_ and it can also be modified. Let’s reconsider our _indiv_ class example in the S4 context.

**library** (methods) **setClass** ("bear", **representation** ( name = "character", age = "numeric", birthday = "Date" ) ) yog <- **new** ("bear", name = 'Yogi', age = 20, birthday = **as.Date** ('91-08-03')) _# next notice the missing age slot_ yog <- **new** ("bear", name = 'Yogi', birthday = **as.Date** ('91-08-03')) _# finally, apparently there's not a default object of class Date_ yog <- **new** ("bear", name = 'Yogi', age = 20)

**## Error in validObject(.Object): invalid class "bear" object: invalid object for slot "birthday" in class "bear": got class "S4", should be or extend class "Date"**

yog

26

---

[← Unit 04 — programming Part 20 —](20-unit-04-programming-part-20.md) · [Up: contents](index.md) · [Unit 04 — programming Part 22 — →](22-unit-04-programming-part-22.md)
