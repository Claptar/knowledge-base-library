---
title: 8 Evaluating memory use
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8 Evaluating memory use

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The main things to remember when thinking about memory use are: (1) numeric vectors take 8 bytes per element and (2) we need to keep track of when large objects are created, including local variables in the frames of functions.

In some of our work here we’ll use functions from the _pryr_ package, which provides functions to help understand what is going on under the hood in R.

**In general, don’t try to run this code within RStudio, as some of how RStudio works affects memory use. Also, some of the output in this PDF is missing or incorrect relative to running the code directly within R, because of effects from the knitting process.**

82

### **8.1 Allocating and freeing memory**

Unlike compiled languages like C, in R we do not need to explicitly allocate storage for objects. However, we have seen that there are times that we do want to allocate storage in advance, rather than successively concatenating onto a larger object.

R automatically manages memory, releasing memory back to the operating system when it’s not needed via garbage collection. Very occasionally you may want to remove large objects as soon as they are not needed. _rm()_ does not actually free up memory, it just disassociates the name from the memory used to store the object. In general R will quickly clean up such objects without a reference (i.e., a name), but it’s possible that very occasionally you might need to call _gc()_ to force the garbage collection. This uses some computation so it’s generally not recommended.

In a language like C in which the user allocates and frees up memory, memory leaks are a major cause of bugs. Basically if you are looping and you allocate memory at each iteration and forget to free it, the memory use builds up inexorably and eventually the machine runs out of memory. In R, with automatic garbage collection, this is generally not an issue, but occasionally memory leaks do occur.

### **8.2 Monitoring overall memory use**

#### **8.2.1 Monitoring use within R**

There are a number of ways to see how much memory is being used. When R is actively executing statements, you can use _top_ from the UNIX shell. In R, _gc()_ reports memory use and free memory as _Ncells_ and _Vcells_ . _Ncells_ concerns the overhead of running R and _Vcells_ relates to objects created by the user, so you’ll want to focus on _Vcells_ . You can see the number of Mb currently used (the “ _used_ ” column of the output) and the maximum used in the session (the “ _max used_ ” column)”. A newer alternative is to use functions in the _pryr_ package such as _mem_used()_ and _mem_change()_ .

**rm** (x) **gc** (reset = TRUE) ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 1195500 63.9 2300772 123 1195500 63.9 ## Vcells 22263269 169.9 34632528 264 22263269 169.9 x <- **rnorm** (1e8) _# should use about 800 Mb_ **object.size** (x)

83

---

[← Unit 05 — programming Part 42 —](42-unit-05-programming-part-42.md) · [Up: contents](index.md) · [Unit 05 — programming Part 44 — →](44-unit-05-programming-part-44.md)
