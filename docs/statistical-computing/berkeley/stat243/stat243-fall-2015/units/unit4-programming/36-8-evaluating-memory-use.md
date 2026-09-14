---
title: 8 Evaluating memory use
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8 Evaluating memory use

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The main things to remember when thinking about memory use are: (1) numeric vectors take 8 bytes per element and (2) we need to keep track of when large objects are created, including in the frames of functions.

In some of our work here we’ll use functions from the _pryr_ package, which provides functions to help understand what is going on under the hood in R.

In general, don’t try to run this code within RStudio, as some of how RStudio works affects memory use.

### **8.1 Allocating and freeing memory**

Unlike compiled languages like C, in R we do not need to explicitly allocate storage for objects. However, we have seen that there are times that we do want to allocate storage in advance, rather than successively concatenating onto a larger object.

R automatically manages memory, releasing memory back to the operating system when it’s not needed via garbage collection. Very occasionally you may want to remove large objects as soon as they are not needed. _rm()_ does not actually free up memory, it just disassociates the name from the memory used to store the object. In general R will clean up such objects without a reference (i.e., a name) but you may need to call _gc()_ to force the garbage collection. This uses some computation so it’s generally not recommended.

In a language like C in which the user allocates and frees up memory, memory leaks are a major cause of bugs. Basically if you are looping and you allocate memory at each iteration and forget to free it, the memory use builds up inexorably and eventually the machine runs out of memory. In R, with automatic garbage collection, this is generally not an issue, but occasionally memory leaks do occur.

### **8.2 Monitoring overall memory use**

There are a number of ways to see how much memory is being used. When R is actively executing statements, you can use _top_ from the UNIX shell. In R, _gc()_ reports memory use and free memory

69

as _Ncells_ and _Vcells_ . As far as I know, _Ncells_ concerns the overhead of running R and _Vcells_ relates to objects created by the user, so you’ll want to focus on _Vcells_ . You can see the number of Mb currently used (the “ _used_ ” column of the output) and the maximum used in the session (the “ _max used_ ” column)”. A newer alternative is _mem_change()_ in the _pryr_ package.

**gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 594538 31.8 1168576 62.5 1168576 62.5 ## Vcells 20836268 159.0 30402572 232.0 21191785 161.7 x <- **rnorm** (1e8) _# should use about 800 Mb_ **object.size** (x) ## 800000040 bytes **object_size** (x) _# from pryr_ ## 800 MB **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 5.95e+05 31.8 1.17e+06 62.5 1.17e+06 62.5 ## Vcells 1.21e+08 922.0 1.74e+08 1330.7 1.21e+08 922.3 **mem_used** () _# from pryr_ ## 1 GB **rm** (x) **gc** () _# note the "max used" column_ ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 595165 31.8 1.17e+06 62.5 1.17e+06 62.5 ## Vcells 20837064 159.0 1.40e+08 1064.5 1.21e+08 922.3 **mem_change** (x <- **rnorm** (1e8)) _# from pryr_ ## 800 MB **mem_change** (x <- **rnorm** (1e7)) ## -720 MB

70

You can reset the value given for max used, with gc(reset = TRUE). In Windows only, _memory.size()_ tells how much memory is being used. You can check the amount of memory used by individual objects with _object.size()_ . Here is a useful function, _ls.sizes()_ , that wraps _object.size()_ to report the largest _n_ objects in a given environment:

ls.sizes <- **function** (howMany = 10, minSize = 1){ pf <- **parent.frame** () obj <- **ls** (pf) _# or ls(sys.frame(-1))_ objSizes <- **sapply** (obj, **function** (x) { **object.size** ( **get** (x, pf))}) _# or sys.frame(-4) to get out of FUN, lapply(), sapply() and sizes()_ objNames <- **names** (objSizes) howmany <- **min** (howMany, **length** (objSizes)) ord <- **order** (objSizes, decreasing = TRUE) objSizes <- objSizes[ord][1:howMany] objSizes <- objSizes[objSizes > minSize] objSizes <- **matrix** (objSizes, ncol = 1) **rownames** (objSizes) <- objNames[ord][1: **length** (objSizes)] **colnames** (objSizes) <- "bytes" **cat** ('object') **print** ( **format** (objSizes, justify = "right", width = 11), quote = FALSE) }

Unfortunately with environments, ReferenceClasses, and other such “containers”, it can be hard to see how much memory the object is using, including all the components of the object. Here’s a trick where we serialize the object, as if to export it, and then see how long the binary representation is.

e <- **new.env** () e$x <- **rnorm** (1e7) **object.size** (e) ## 56 bytes **length** ( **serialize** (e, **NULL** )) ## [1] 80000183

71

One frustration with memory management is that if your code bumps up against the memory limits of the machine, it can be very slow to respond even when you’re trying to cancel the statement with _Ctrl-C_ . You can impose memory limits in Linux by starting R (from the UNIX prompt) in a fashion such as this

> R --max-vsize=1000M

Then if you try to create an object that will push you over that limit or execute code that involves going over the limit, it will simply fail with the message “ _Error: vector memory exhausted (limit reached?)_ ”. So this approach may be a nice way to avoid paging/swapping by setting the maximum in relation to the physical memory of the machine. It might also help in debugging memory leaks because the program would fail at the point that memory use was increasing. I haven’t played around with this much, so offer this with a note of caution.

We can use an internal function called _inspect()_ to see where in memory an object is stored. We’ll see that this can be a handy tool for seeing where copies are made and where they are not.

a <- **rnorm** (5) **.Internal** ( **inspect** (a)) ## @5ab8150 14 REALSXP g0c4 [NAM(2)] (len=5, tl=0) 1.20738,0.313843,0.959564,0.190907,0.646543 obj <- **list** (a = **rnorm** (5), b = **list** (d = "adfs")) **.Internal** ( **inspect** (obj$a)) ## @5046778 14 REALSXP g0c4 [NAM(2)] (len=5, tl=0) 0.271147,-1.31208,-1.08012,-0.845882,1.09931

The _pryr_ package provides _address()_ or _inspect()_ as an alternative to _.Internal(inspect())_ . Note that you should make sure you have the most recent version of pryr as there was a bug in _address()_ in older versions that give the wrong info for the example below.

obj <- **list** (a = **rnorm** (5), b = **list** (d = "adfs")) **address** (obj) _# from pryr_

---

[← 7 Efficiency](35-7-efficiency.md) · [Up: contents](index.md) · [[1] "0x4fc48d0" →](37-1-0x4fc48d0.md)
