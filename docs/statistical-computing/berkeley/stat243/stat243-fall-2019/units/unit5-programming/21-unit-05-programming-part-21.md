---
title: Unit 05 — programming Part 21 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 21 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Often S3 classes inherit from lists (i.e., are special cases of lists), so you can obtain components of the object using the $ operator.

**Creating our own class** We can create an object with a new class as follows: yog <- **list** (firstname = 'Yogi', surname = 'the Bear', age = 20) **class** (yog) <- 'bear'

Actually, if we want to create a new class that we’ll use again, we want to create a _constructor_ function that initializes new bears:

bear <- **function** (firstname = NA, surname = NA, age = NA){ _# constructor for 'indiv' class_ obj <- **list** (firstname = firstname, surname = surname, age = age) **class** (obj) <- 'bear' **return** (obj) } smoke <- **bear** ('Smokey','Bear')

For those of you used to more formal OOP, the following is probably disconcerting:

**class** (yog) <- "silly" **class** (yog) <- "bear"

**Methods** The real power of OOP comes from defining _methods_ . For example,

mod <- **lm** (yc ~ x) **summary** (mod) gmod <- **glm** (yb ~ x, family = 'binomial') **summary** (gmod)

23

Here _summary()_ is a generic method (or generic function) that, based on the type of object given to it (the first argument), dispatches a class-specific function (method) that operates on the object. This is convenient for working with objects using familiar functions. Consider the generic methods _plot()_ , _print()_ , _summary()_ , _‘[‘_ , and others. We can look at a function and easily see that it is a generic method. We can also see what classes have methods for a given generic method.

summary ## function (object, ...) ## UseMethod("summary") ## <bytecode: 0x5560f98781a8> ## <environment: namespace:base>

**methods** (summary)

---

[← $names ## [1] "x" "y" ## ## $class ## [1] "data.frame" ## ## $row.names ## [1] 1 2](20-class-1-data-frame-row-names-1-1-2.md) · [Up: contents](index.md) · [Unit 05 — programming Part 22 — →](22-unit-05-programming-part-22.md)
