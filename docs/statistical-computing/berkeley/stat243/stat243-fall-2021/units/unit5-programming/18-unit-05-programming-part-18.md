---
title: Unit 05 — programming Part 18 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 18 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Often S3 classes inherit from lists (i.e., are special cases of lists), so you can obtain components of the object using the $ operator.

yog <- **list** (firstnamefirstname = 'Yogi',, surname = 'the Bear',, age = 20) **class** (yog) <- 'bear'

Actually, if we want to create a new class that we’ll use again, we want to create a _constructor_ function that initializes new bears:

For those of you used to more formal OOP, the following is probably disconcerting:

24

**class** (yog) <- "silly" **class** (yog) <- "bear"

**Methods** The real power of OOP comes from defining _methods_ . For example,

mod <- **lm** (yc ~ x) **summary** (mod) gmod <- **glm** (yb ~ x, family = 'binomial') **summary** (gmod)

Here _summary()_ is a generic method (or generic function) that, based on the type of object given to it (the first argument), dispatches a class-specific function (method) that operates on the object. This is convenient for working with objects using familiar functions. Consider the generic methods _plot()_ , _print()_ , _summary()_ , _‘[‘_ , and others. We can look at a function and easily see that it is a generic method. We can also see what classes have methods for a given generic method.

summary ## function (object, ...) ## UseMethod("summary") ## <bytecode: 0x556919f90cf8> ## <environment: namespace:base>

**methods** (summary)

---

[← minimal ## 3 score[ as.character (students[3])] ## advanced ## 13](17-minimal-3-score-as-character-students-3-advanced-13.md) · [Up: contents](index.md) · [Unit 05 — programming Part 19 — →](19-unit-05-programming-part-19.md)
