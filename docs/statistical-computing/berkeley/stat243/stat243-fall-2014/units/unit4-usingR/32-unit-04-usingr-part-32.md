---
title: Unit 04 — usingR Part 32 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 32 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Where are arguments evaluated?** User-supplied arguments are evaluated in the calling frame, while default arguments are evaluated in the frame of the function:

z <- 3 x <- 100 f <- **function** (x, y = x * 3) { x + y } **f** (z * 5) ## [1] 60

Here, when _f()_ is called, _z_ is evaluated in the calling frame and z*5 is assigned to _x_ in the frame of the function, while y = x*3 is evaluated in the frame of the function.

**Comprehension problem** Here’s a case where something I tried failed and I had to think more carefully about scoping to understand why.

**set.seed** (0) **rnorm** (1) ## [1] 1.26

49

**save** (.Random.seed, file = "tmp.Rda") **rnorm** (1) ## [1] -0.326 tmp <- **function** () { **load** ("tmp.Rda") **print** ( **rnorm** (1)) } **tmp** () ## [1] 1.33

Question: what was I hoping that code to do, and why didn’t it work?

### **7.4 Environments and the search path**

So far we’ve seen lexical scoping in action primarily in terms of finding variables in a single enclosing environment. But what if the variable is not found in either the frame/environment of the function or the enclosing environment? When R goes looking for an object (in the form of a symbol), it starts in the current environment (e.g., the frame/environment of a function) and then runs up through the enclosing environments, until it reaches the global environment, which is where R starts when you open R (it actually continues further up; see below). In general, as we’ve seen, these are _not_ the frames on the stack (see the next Section).

By default objects are created in the global environment, _.GlobalEnv_ . As we’ve seen, the environment within a function call has as its enclosing environment the environment where the function was defined (not the environment from which it was called), and this is next place that is searched if an object can’t be found in the frame of the function call. This is called lexical scoping (and differs from the S language on which R was based). As an example, if an object couldn’t be found within the environment of an _lm()_ function call, R would first look in the environment (also called the namespace) of the stats package (since this is the environment where _lm()_ is defined and is therefore the enclosing environment for _lm()_ ), then in packages imported by the stats package, then the base package, and then the global environment.

If R can’t find the object when reaching the global environment, it runs through the search path, which you can see with _search()_ . The search path is a set of additional environments. Generally packages are created with namespaces, i.e., each has its own environment, as we see based on _search()_ .

50

#### **search** ()

- ## [1] ".GlobalEnv" "package:fields" ## [3] "package:maps" "package:spam" ## [5] "package:grid" "package:methods" ## [7] "package:knitr" "package:stats" ## [9] "package:graphics" "package:grDevices" ## [11] "package:utils" "package:datasets" ## [13] "package:SCF" "Autoloads" ## [15] "package:base"

**searchpaths** ()

- ## [1] ".GlobalEnv" ## [2] "/system/linux/lib/R/3.0/x86_64/site-library/fields" ## [3] "/system/linux/lib/R/3.0/x86_64/site-library/maps" ## [4] "/accounts/gen/vis/paciorek/R/x86_64-pc-linux-gnu-library/3.0/spam" ## [5] "/usr/lib/R/library/grid" ## [6] "/usr/lib/R/library/methods" ## [7] "/system/linux/lib/R/3.0/x86_64/site-library/knitr" ## [8] "/usr/lib/R/library/stats" ## [9] "/usr/lib/R/library/graphics"

---

[← $x ## ## ## $y ## [1] 2 ## ## $z ## 3/y class ( formals (f)) ## [1] "pairlist"](31-y-1-2-z-3-y-class-formals-f-1-pairlist.md) · [Up: contents](index.md) · [[10] "/usr/lib/R/library/grDevices" →](33-10-usr-lib-r-library-grdevices.md)
