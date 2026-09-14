---
title: Unit 04 — programming Part 22 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 22 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

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

22

mod <- **lm** (yc ~ x) **summary** (mod) gmod <- **glm** (yb ~ x, family = 'binomial') **summary** (gmod)

Here _summary()_ is a generic method (or generic function) that, based on the type of object given to it (the first argument), dispatches a class-specific function (method) that operates on the object. This is convenient for working with objects using familiar functions. Consider the generic methods _plot()_ , _print()_ , _summary()_ , _‘[‘_ , and others. We can look at a function and easily see that it is a generic method. We can also see what classes have methods for a given generic method.

summary

---

[← [1] 1.00 2.73 as.factor ( c ("a", "b", "c")) ## [1] a b c ## Levels: a b c](21-1-1-00-2-73-as-factor-c-a-b-c-1-a-b-c-levels-a-b-c.md) · [Up: contents](index.md) · [Unit 04 — programming Part 23 — →](23-unit-04-programming-part-23.md)
