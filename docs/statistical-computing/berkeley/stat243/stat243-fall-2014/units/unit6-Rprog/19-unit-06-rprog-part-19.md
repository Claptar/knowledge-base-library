---
title: Unit 06 — Rprog Part 19 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — Rprog Part 19 —

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Often S3 classes inherit from lists (i.e., are special cases of lists), so you can obtain components of the object using the $ operator.

**Creating our own class** We can create an object with a new class as follows:

yog <- **list** (firstname = "Yogi", surname = "the Bear", age = 20) **class** (yog) <- "bear"

Actually, if we want to create a new class that we’ll use again, we want to create a _constructor_ function that initializes new bears:

bear <- **function** (firstname = NA, surname = NA, age = NA) { _# constructor for 'indiv' class_

obj <- **list** (firstname = firstname, surname = surname, age = age) **class** (obj) <- "indiv"

**return** (obj)

}

40

<mark>smoke <-</mark> **<mark>bear</mark>** <mark>("Smokey", "Bear")</mark>

For those of you used to more formal OOP, the following is probably disconcerting:

**class** (yog) <- "silly" **class** (yog) <- "bear"

**Methods** The real power of OOP comes from defining _methods_ . For example,

mod <- **lm** (yc ~ x) **summary** (mod) gmod <- **glm** (yb ~ x, family = "binomial") **summary** (gmod)

Here _summary()_ is a generic method (or generic function) that, based on the type of object given to it (the first argument), dispatches a class-specific function (method) that operates on the object. This is convenient for working with objects using familiar functions. Consider the generic methods _plot()_ , _print()_ , _summary()_ , _‘[‘_ , and others. We can look at a function and easily see that it is a generic method. We can also see what classes have methods for a given generic method.

mean ## function (x, ...) ## UseMethod("mean") ## <bytecode: 0x1869920> ## <environment: namespace:base> **methods** (mean) ## [1] mean.Date mean.default mean.difftime mean.POSIXct mean.POSIXlt

In many cases there will be a default method (here, _mean.default()_ ), so if no method is defined for the class, R uses the default. Sidenote: arguments to a generic method are passed along to the selected method by passing along the calling environment.

We can define new generic methods:

41

<mark>summarize <-</mark> **<mark>function</mark>** <mark>(object, ...)</mark> **<mark>UseMethod</mark>** <mark>("summarize")</mark>

Once _UseMethod()_ is called, R searches for the specific method associated with the class of _object_ and calls that method, without ever returning to the generic method. Let’s try this out on our _indiv_ class. In reality, we’d write either _summary.indiv()_ or _print.indiv()_ (and of course the generics for _summary_ and _print_ already exist) but for illustration, I wanted to show how we would write both the generic and the specific method, so I’ll write a _summarize_ method.

summarize.bear <- **function** (object) **return** ( **with** (object, **cat** ("Bear of age ", " whose name is ", firstname, " ", surname, ".\n", sep = ""))) **summarize** (yog)

---

[← [1] TRUE](18-1-true.md) · [Up: contents](index.md) · [Bear of age 20 whose name is Yogi the Bear. →](20-bear-of-age-20-whose-name-is-yogi-the-bear.md)
