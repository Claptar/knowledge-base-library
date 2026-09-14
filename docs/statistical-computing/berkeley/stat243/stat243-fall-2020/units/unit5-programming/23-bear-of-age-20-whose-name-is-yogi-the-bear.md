---
title: Bear of age 20 whose name is Yogi the Bear.
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Bear of age 20 whose name is Yogi the Bear.

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**The print method** Like _summary()_ , _print()_ is a generic method, with various class-specific methods, such as _print.lm()_ .

26

Note that the _print()_ function is what is called when you simply type the name of the object, so we can have object information printed out in a structured way. Recall that the output when we type the name of an _lm_ object is NOT simply a regurgitation of the elements of the list - rather _print.lm()_ is called.

Similarly, when we used print(object.size(x)) we were invoking the _object_size_ - specific print method which gets the value of the size and then formats it. So there’s actually a fair amount going on behind the scenes.

Surprisingly, the _summary()_ method generally doesn’t actually print out information; rather it computes things not stored in the original object and returns it as a new class (e.g., class _summary.lm_ ), which is then automatically printed, per my comment above, using _print.summary.lm()_ , unless one assigns it to a new object. Note that _print.summary.lm()_ is hidden from user view.

out <- **summary** (mod) out **print** (out) **getS3method** (f="print",class="summary.lm")

**More on inheritance** As noted with _lm_ and _glm_ objects, we can assign more than one class to an object. Here _summarize()_ still works, even though the primary class is _grizzly_bear_ .

**class** (yog) <- **c** ('grizzly_bear', 'bear') **summarize** (yog) ## Bear of age 20 whose name is Yogi the Bear.

The classes should nest within one another with the more specific classes to the left, e.g., here a _grizzly_bear_ would have some additional objects on top of those of a _bear_ , perhaps _number_of_people_eaten_ (since grizzly bears are much more dangerous than some other kinds of bears), and perhaps additional or modified methods. _grizzly_bear_ inherits from _bear_ , and R uses methods for the first class before methods for the next class(es), unless no such method is defined for the first class. If no methods are defined for any of the classes, R looks for _method.default()_ , e.g., _print.default()_ , _plot.default()_ , etc..

**Why use class-specific methods?** We could have implemented different functionality (e.g., for _summary()_ ) for different objects using a bunch of _if_ statements (or _switch()_ ) to figure out what class of object is the input, but then we need to have all that checking. Furthermore, we don’t control the _summary()_ function, so we would have no way of adding the additional conditions in a

27

big if-else statement. The OOP framework makes things _extensible_ , so we can build our own new functionality on what is already in R.

**Final thoughts** Consider the _Date_ class discussed in the R bootcamp. This is another example of an S3 class, with methods such as _julian()_ , _weekdays()_ , etc.

**Challenge** : how would you get R to quit immediately, without asking for any more information, when you simply type ’k’ (no parentheses!) instead of ’ _quit()_ ’?

What we’ve just discussed are the old-style R (and S) object orientation, called S3 methods. An old, but somewhat newer style is called S4 and we’ll discuss it next. S3 is still commonly used, in part because S4 can be slow. S4 is more structured than S3.

#### **4.4.2 S4 approach (optional)**

S4 methods are used a lot in _bioconductor_ , a project that provides a lot of bioinformatics-related code. They’re also used in _lme4_ , among other packages. Tools for working with S4 classes are in the _methods_ package.

Note that components of S4 objects are obtained as object@component so they do not use the usual list syntax. The components are called _slots_ , and there is careful checking that the slots are specified and valid when a new object of a class is created. You can use the _prototype_ argument to _setClass()_ to set default values for the slots. There is a default constructor (the method is actually called _initialize()_ ), but you can modify it. One can create methods for operators and for replacement functions too. For S4 classes, there is a default method invoked when _print()_ is called on an object in the class (either explicitly or implicitly) - the method is actually called _show()_ and it can also be modified. Let’s reconsider our _bear_ class example in the S4 context.

**library** (methods) **setClass** ("bear", **representation** ( name = "character", age = "numeric", birthday = "Date" ) ) yog <- **new** ("bear", name = 'Yogi', age = 20, birthday = **as.Date** ('91-08-03'))

28

_## next notice the missing age slot_ yog <- **new** ("bear", name = 'Yogi', birthday = **as.Date** ('91-08-03')) _## finally, apparently there's not a default object of class Date_ yog <- **new** ("bear", name = 'Yogi', age = 20) **## Error in validObject(.Object): invalid class "bear" object: invalid object for slot "birthday" in class "bear": got class "S4", should be or extend class "Date"** yog ## An object of class "bear" ## Slot "name": ## [1] "Yogi" ## ## Slot "age": ## numeric(0) ## ## Slot "birthday": ## [1] "91-08-03" yog@age <- 60 S4 methods are designed to be more structured than S3, with careful checking of the slots. **setValidity** ("bear", **function** (object) { **if** (!(object@age > 0 && object@age < 130)) **return** ("error: age must be between 0 and 130") **if** ( **length** ( **grep** ("[0-9]", object@name))) **return** ("error: name contains digits") **return** (TRUE) _# what other validity check would make sense given the slots?_ } ) ## Class "bear" [in ".GlobalEnv"]

29

---

[← Unit 05 — programming Part 22 —](22-unit-05-programming-part-22.md) · [Up: contents](index.md) · [Unit 05 — programming Part 24 — →](24-unit-05-programming-part-24.md)
