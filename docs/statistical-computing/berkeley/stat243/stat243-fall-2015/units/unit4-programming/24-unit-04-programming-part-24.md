---
title: Unit 04 — programming Part 24 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 24 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can add methods after defining the class.

31

tsSimClass$ **methods** ( **list** ( simulate = **function** (){ ' simulates random processes from the model ' **if** (!currentU) **calcMats** () **return** ( **crossprod** (U, **rnorm** (n))) }) )

Now let’s see how we would use the class.

master <- tsSimClass$ **new** (1:100, 10) master tsSimClass$ **help** ('calcMats') devs <- master$ **simulate** () **plot** (master$times, devs, type = 'l') mycopy <- master myDeepCopy <- master$ **copy** () master$ **changeTimes** ( **seq** (0,1, length = 100)) mycopy$times[1:5] myDeepCopy$times[1:5]

A few additional points:

- As we just saw, a copy of an object is just a pointer to the original object, unless we explicitly invoke the _copy()_ method.

- As with S3 and S4, classes can inherit from other classes. E.g., if we had a _simClass_ and we wanted the _tsSimClass_ to inherit from it:

setRefClass("tsSimClass", contains = "simClass")

   - We can call a method inherited from the superclass from within a method of the same name with _callSuper(...)_ , as we saw for our _initialize()_ method.

- If we need to refer to a field or change a field we can do so without hard-coding the field name as:

32

master$ **field** ('times')[1:5] _# the next line is dangerous in this case, since # currentU will no longer be accurate_ master$ **field** ('times', 1:10)

- Note that reference classes have Python style doc strings. We get help on a class with _class$help()_ , e.g. tsSimClass$help(). This prints out information, including the doc strings.

- If you need to refer to the entire object within an object method, you refer to it as _.self_ . E.g., with our _tsSimClass_ object, .self$U would refer to the Cholesky factor. This is sometimes necessary to distinguish a class field from an argument to a method.

- There is a new, more efficient version of ReferenceClasses call R6 classes. See the _R6_ package.

---

[← Unit 04 — programming Part 23 —](23-unit-04-programming-part-23.md) · [Up: contents](index.md) · [5 Standard dataset manipulations →](25-5-standard-dataset-manipulations.md)
