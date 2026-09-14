---
title: 8 Evaluating memory use
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8 Evaluating memory use

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The main things to remember when thinking about memory use are: (1) numeric vectors take 8 bytes per element and (2) we need to keep track of when large objects are created, including in the frames of functions.

In some of our work here we’ll use functions from the _pryr_ package, which provides functions to help understand what is going on under the hood in R.

In general, don’t try to run this code within RStudio, as some of how RStudio works affects memory use.

### **8.1 Allocating and freeing memory**

Unlike compiled languages like C, in R we do not need to explicitly allocate storage for objects. However, we have seen that there are times that we do want to allocate storage in advance, rather than successively concatenating onto a larger object.

R automatically manages memory, releasing memory back to the operating system when it’s not needed via garbage collection. Very occasionally you may want to remove large objects as soon as they are not needed. _rm()_ does not actually free up memory, it just disassociates the name from the memory used to store the object. In general R will clean up such objects without a

71

reference (i.e., a name) but you may need to call _gc()_ to force the garbage collection. This uses some computation so it’s generally not recommended.

In a language like C in which the user allocates and frees up memory, memory leaks are a major cause of bugs. Basically if you are looping and you allocate memory at each iteration and forget to free it, the memory use builds up inexorably and eventually the machine runs out of memory. In R, with automatic garbage collection, this is generally not an issue, but occasionally memory leaks do occur.

### **8.2 Monitoring overall memory use**

#### **8.2.1 Monitoring use within R**

There are a number of ways to see how much memory is being used. When R is actively executing statements, you can use _top_ from the UNIX shell. In R, _gc()_ reports memory use and free memory as _Ncells_ and _Vcells_ . As far as I know, _Ncells_ concerns the overhead of running R and _Vcells_ relates to objects created by the user, so you’ll want to focus on _Vcells_ . You can see the number of Mb currently used (the “ _used_ ” column of the output) and the maximum used in the session (the “ _max used_ ” column)”. A newer alternative is _mem_change()_ in the _pryr_ package.

**gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 760730 40.7 1442291 77.1 1442291 77.1 ## Vcells 21378900 163.2 31182729 238.0 22867199 174.5 x <- **rnorm** (1e8) _# should use about 800 Mb_ **object.size** (x) ## 800000040 bytes **object_size** (x) _# from pryr_ ## 800 MB **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 7.61e+05 40.7 1.44e+06 77.1 1.44e+06 77.1 ## Vcells 1.21e+08 926.1 1.75e+08 1336.6 1.21e+08 926.4

72

**mem_used** () _# from pryr_ ## 1.01 GB **rm** (x) **gc** () _# note the "max used" column_ ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 761411 40.7 1.44e+06 77.1 1.44e+06 77.1 ## Vcells 21380007 163.2 1.40e+08 1069.3 1.21e+08 926.4 **mem_change** (x <- **rnorm** (1e8)) _# from pryr_ ## 800 MB **mem_change** (x <- **rnorm** (1e7)) ## -720 MB

You can reset the value given for max used, with gc(reset = TRUE). In Windows only, _memory.size()_ tells how much memory is being used. You can check the amount of memory used by individual objects with _object.size()_ . Here is a useful function, _ls.sizes()_ , that wraps _object.size()_ to report the largest _n_ objects in a given environment:

ls.sizes <- **function** (howMany = 10, minSize = 1){ pf <- **parent.frame** () obj <- **ls** (pf) _# or ls(sys.frame(-1))_ objSizes <- **sapply** (obj, **function** (x) { **object.size** ( **get** (x, pf)) }) _## or sys.frame(-4) to get out of FUN, lapply(), sapply() and sizes()_ objNames <- **names** (objSizes) howmany <- **min** (howMany, **length** (objSizes)) ord <- **order** (objSizes, decreasing = TRUE) objSizes <- objSizes[ord][1:howMany] objSizes <- objSizes[objSizes > minSize] objSizes <- **matrix** (objSizes, ncol = 1)

73

**rownames** (objSizes) <- objNames[ord][1: **length** (objSizes)] **colnames** (objSizes) <- "bytes" **cat** ('object') **print** ( **format** (objSizes, justify = "right", width = 11), quote = FALSE) }

Unfortunately with environments, ReferenceClasses, and other such “containers”, it can be hard to see how much memory the object is using, including all the components of the object. Here’s a trick where we serialize the object, as if to export it, and then see how long the binary representation is.

_## size of an environment_ e <- **new.env** () e$x <- **rnorm** (1e7) **object.size** (e) ## 56 bytes **length** ( **serialize** (e, **NULL** )) ## [1] 80000183 _## size of a closure_ x <- **rnorm** (1e7) f <- **function** (input){ data <- input g <- **function** (param) **return** (param * data) **return** (g) } myFun <- **f** (x) **rm** (x) **object.size** (myFun) ## 1560 bytes **length** ( **serialize** (myFun, **NULL** )) ## [1] 160009701

74

One frustration with memory management is that if your code bumps up against the memory limits of the machine, it can be very slow to respond even when you’re trying to cancel the statement with _Ctrl-C_ . You can impose memory limits in Linux by starting R (from the UNIX prompt) in a fashion such as this

> R --max-vsize=1000M

Then if you try to create an object that will push you over that limit or execute code that involves going over the limit, it will simply fail with the message “ _Error: vector memory exhausted (limit reached?)_ ”. So this approach may be a nice way to avoid paging/swapping by setting the maximum in relation to the physical memory of the machine. It might also help in debugging memory leaks because the program would fail at the point that memory use was increasing. I haven’t played around with this much, so offer this with a note of caution.

We can use an internal function called _inspect()_ to see where in memory an object is stored. We’ll see that this can be a handy tool for seeing where copies are made and where they are not.

x <- **rnorm** (5) **.Internal** ( **inspect** (x)) ## @4bc6358 14 REALSXP g0c4 [NAM(2)] (len=5, tl=0) 1.16401,-0.712768,-0.19288,1.02019,0.66594 obj <- **list** (a = **rnorm** (5), b = **list** (d = "adfs")) **.Internal** ( **inspect** (obj$a)) ## @4bc5238 14 REALSXP g0c4 [NAM(2)] (len=5, tl=0) 0.367744,0.103611,0.154352,-1.90064,-0.956917

The _pryr_ package provides _address()_ or _inspect()_ as an alternative to _.Internal(inspect())_ .

obj <- **list** (a = **rnorm** (5), b = **list** (d = "adfs")) **address** (x) _# from pryr_

---

[← %% is modulo operator - it gives the remainder](39-is-modulo-operator---it-gives-the-remainder.md) · [Up: contents](index.md) · [[1] "0x4bc6358" →](41-1-0x4bc6358.md)
