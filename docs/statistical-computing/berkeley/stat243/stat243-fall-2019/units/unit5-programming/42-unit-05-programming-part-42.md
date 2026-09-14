---
title: Unit 05 — programming Part 42 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 42 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note that eventually the global environment and the environments of the packages are nested within the base environment (of the base package) and the empty environment. Note that here _parent_ **is** referring to the enclosing environment, even though it is best to talk about _enclosing environment_ rather than parent environment.

We can retrieve and assign objects in a particular environment and/or namespace as follows:

lm <- **function** () { **return** ( **NULL** )} _# this seems dangerous but isn't_ x <- 1:3; y <- **rnorm** (3); mod <- **lm** (y ~ x)

**## Error in lm(y ~ x): unused argument (y ~ x)** mod <- **get** ('lm', pos = 'package:stats')(y ~ x) mod <- stats:: **lm** (y ~ x) _# an alternative ## :: is the namespace resolution operator_ **rm** (lm) mod <- **lm** (y ~ x)

Note that our (bogus) _lm()_ function masks but does not overwrite the default function. If we remove ours, then the default one is still there.

### **6.10 Alternatives to pass by value in R**

There are occasions we do not want to pass by value. In addition to avoiding copies and the attendant computation and memory use, another reason is when we want a function to modify a complicated object without having to return it and re-assign it in the parent environment. There are several work-arounds:

1. We can use R6 (or Reference Class) objects.

2. We can access the object in the enclosing environment as a ’global variable’, as we’ve seen when discussing scoping. More generally we can access the object using _get()_ , specifying the environment from which we want to obtain the variable. To specify the location of an object when using _get()_ , we can generally specify (1) a position in the search path, (2) an explicit environment, or (3) a location in the call stack by using _sys.frame()_ . However we cannot change the value of the object in the parent environment without some additional tools:

66

- (a) We can use the ’<<-’ operator to assign into an object in the parent environment (provided an object of that name exists in the parent environment).

- (b) We can also use _assign()_ , specifying the environment in which we want the assignment to occur.

While these techniques are possible and ok for exploratory coding, they’re bad practice for more formal code development.

3. We can use replacement functions (Section 6.6), which hide the reassignment in the parent environment from the user. Note that a second copy is generally created in this case, but the original copy is quickly removed.

4. We can use a _closure_ , which is a function with associated data. This Wikipedia entry nicely summarizes the idea, which is not an R-specific construct. This involves creating one (or more functions) within a function call and returning the function(s) as the output. When one executes the original function, the new function(s) is created and returned and one can then call that new function(s). The new function then can access objects in the enclosing environment (the environment of the original function) and can use ‘<<-‘ to assign into the enclosing environment, to which the function (or the multiple functions) have access. The nice thing about this compared to using a global variable is that the data in the closure is bound up with the function(s) and is protected from being changed by the user of the closure. Chambers provides an example of this in Sec. 5.4.

x <- **rnorm** (10) f <- **function** (input){ data <- input g <- **function** (param) **return** (param * data) **return** (g) } myFun <- **f** (x) **rm** (x) _# to demonstrate we no longer need x_ **myFun** (3) ## [1] 1.462 2.215 1.727 -0.916 4.535 1.170 -1.864 ## [8] -6.644 3.375 -0.135

67

x <- **rnorm** (1e7) myFun <- **f** (x) **object.size** (myFun) _# hmmm_ ## 3800 bytes **object.size** ( **environment** (myFun)$data) ## 80000048 bytes **library** (pryr) **object_size** (myFun) _# that's better!_ ## 80 MB

Here’s a fun example. You might do this with an _apply()_ variant, in particular _replicate()_ , but this is slick:

make_container <- **function** (n) { x <- **numeric** (n) i <- 1 **function** (value = **NULL** ) { **if** ( **is.null** (value)) { **return** (x) } **else** { x[i] <<- value i <<- i + 1 } } } nboot <- 100 bootmeans <- **make_container** (nboot) data <- faithful[ , 1] _# Old Faithful geyser eruption lengths_ **for** (i **in** 1:nboot) **bootmeans** ( **mean** ( **sample** (data, **length** (data), replace=TRUE))) _## this will place results in x in the function env't and you can grab it out_

68

**bootmeans** ()

---

[← Unit 05 — programming Part 41 —](41-unit-05-programming-part-41.md) · [Up: contents](index.md) · [Unit 05 — programming Part 43 — →](43-unit-05-programming-part-43.md)
