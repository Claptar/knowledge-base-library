---
title: Bear of age 20 whose name is Yogi the Bear.
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Bear of age 20 whose name is Yogi the Bear.

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note that the print() function is what is called when you simply type the name of the object, so we can have object information printed out in a structured way. Recall that the output when we type the name of an lm object is NOT simply a regurgitation of the elements of the list - rather print.lm() is called.

24

Similarly, when we used print(object.size(x)) we were invoking the object_sizespecific print method which gets the value of the size and then formats it. So there’s actually a fair amount going on behind the scenes.

Surprisingly, the summary() method generally doesn’t actually print out information; rather it computes things not stored in the original object and returns it as a new class (e.g., class summary.lm), which is then automatically printed, per my comment above, using print.summary.lm(), unless one assigns it to a new object. Note that print.summary.lm() is hidden from user view.

out <- **summary** (mod) out **print** (out) **getS3method** (f="print",class="summary.lm")

More on inheritance As noted with lm and glm objects, we can assign more than one class to an object. Here summarize() still works, even though the primary class is grizzly_bear.

**class** (yog) <- **c** ('grizzly_bear', 'bear') **summarize** (yog) ## Bear of age 20 whose name is Yogi the Bear.

The classes should nest within one another with the more specific classes to the left, e.g., here a grizzly_bear would have some additional objects on top of those of a bear, perhaps number_of_people_eaten (since grizzly bears are much more dangerous than some other kinds of bears), and perhaps additional or modified methods. grizzly_bear inherits from bear, and R uses methods for the first class before methods for the next class(es), unless no such method is defined for the first class. If no methods are defined for any of the classes, R looks for method.default(), e.g., print.default(), plot.default(), etc..

Class-specific operators We can also use operators with our classes. The following example will be a bit silly (it would make more sense with a class that is a mathematical object) but indicates the power of having methods.

**methods** (`+`) ## [1] +.Date +.POSIXt ## see '?methods' for accessing help and source code

25

`+.bear` <- **function** (object, incr) { object$age <- object$age + incr **return** (object) } older_yog <- yog + 15

Class-specific replacement functions We can use replacement functions with our classes. For more on what a replacement function is, see Section 6.6.

This is again a bit silly but we could do the following. We need to define the generic replacement function and then the class-specific one.

`age<-` <- **function** (x, ...) **UseMethod** ("age<-") `age<-.bear` <- **function** (object, value){ object$age <- value **return** (object) } **age** (older_yog) <- 60

Why use class-specific methods? We could have implemented different functionality (e.g., for summary()) for different objects using a bunch of if statements (or switch()) to figure out what class of object is the input, but then we need to have all that checking. Furthermore, we don’t control the summary() function, so we would have no way of adding the additional conditions in a big if-else statement. The OOP framework makes things extensible, so we can build our own new functionality on what is already in R.

Final thoughts Consider the Date class discussed in the R bootcamp. This is another example of an S3 class, with methods such as julian(), weekdays(), etc.

Challenge: how would you get R to quit immediately, without asking for any more information, when you simply type ’q’ (no parentheses!) instead of ’quit()’?

What we’ve just discussed are the old-style R (and S) object orientation, called S3 methods. The new style is called S4 and we’ll discuss it next. S3 is still commonly used, in part because S4 can be slow (or at least it was when I last looked into this a few years ago). S4 is more structured than S3.

26

#### 4.4.2 S4 approach

S4 methods are used a lot in bioconductor, a project that provides a lot of bioinformatics-related code. They’re also used in lme4, among other packages. Tools for working with S4 classes are in the methods package.

Note that components of S4 objects are obtained as object@component so they do not use the usual list syntax. The components are called slots, and there is careful checking that the slots are specified and valid when a new object of a class is created. You can use the prototype argument to setClass() to set default values for the slots. There is a default constructor (the method is actually called initialize()), but you can modify it. One can create methods for operators and for replacement functions too. For S4 classes, there is a default method invoked when print() is called on an object in the class (either explicitly or implicitly) - the method is actually called show() and it can also be modified. Let’s reconsider our bear class example in the S4 context.

**library** (methods) **setClass** ("bear", **representation** ( name = "character", age = "numeric", birthday = "Date" ) ) yog <- **new** ("bear", name = 'Yogi', age = 20, birthday = **as.Date** ('91-08-03')) ## next notice the missing age slot yog <- **new** ("bear", name = 'Yogi', birthday = **as.Date** ('91-08-03')) ## finally, apparently there's not a default object of class Date yog <- **new** ("bear", name = 'Yogi', age = 20)

**## Error in validObject(.Object): invalid class "bear" object: invalid object for slot "birthday" in class "bear": got class "S4", should be or extend class "Date"**

yog

27

---

[← Unit 04 — programming partial Part 25 —](25-unit-04-programming-partial-part-25.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 27 — →](27-unit-04-programming-partial-part-27.md)
