---
title: 8 Evaluating memory use
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8 Evaluating memory use

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The main things to remember when thinking about memory use are: (1) numeric vectors take 8 bytes per element and (2) we need to keep track of when large objects are created, including in the frames of functions.

In some of our work here we’ll use functions from the _pryr_ package, which provides functions to help understand what is going on under the hood in R.

**In general, don’t try to run this code within RStudio, as some of how RStudio works affects memory use. Also, some of the output in this PDF is missing or incorrect relative to running the code directly within R.**

### **8.1 Allocating and freeing memory**

Unlike compiled languages like C, in R we do not need to explicitly allocate storage for objects. However, we have seen that there are times that we do want to allocate storage in advance, rather than successively concatenating onto a larger object.

R automatically manages memory, releasing memory back to the operating system when it’s not needed via garbage collection. Very occasionally you may want to remove large objects as soon as they are not needed. _rm()_ does not actually free up memory, it just disassociates the name from the memory used to store the object. In general R will clean up such objects without a reference (i.e., a name) but you may need to call _gc()_ to force the garbage collection. This uses some computation so it’s generally not recommended.

74

In a language like C in which the user allocates and frees up memory, memory leaks are a major cause of bugs. Basically if you are looping and you allocate memory at each iteration and forget to free it, the memory use builds up inexorably and eventually the machine runs out of memory. In R, with automatic garbage collection, this is generally not an issue, but occasionally memory leaks do occur.

### **8.2 Monitoring overall memory use**

#### **8.2.1 Monitoring use within R**

There are a number of ways to see how much memory is being used. When R is actively executing statements, you can use _top_ from the UNIX shell. In R, _gc()_ reports memory use and free memory as _Ncells_ and _Vcells_ . As far as I know, _Ncells_ concerns the overhead of running R and _Vcells_ relates to objects created by the user, so you’ll want to focus on _Vcells_ . You can see the number of Mb currently used (the “ _used_ ” column of the output) and the maximum used in the session (the “ _max used_ ” column)”. A newer alternative is _mem_change()_ in the _pryr_ package.

**gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 830559 44.4 1442291 77.1 1442291 77.1 ## Vcells 21468650 163.8 31311083 238.9 22936754 175.0 x <- **rnorm** (1e8) _# should use about 800 Mb_ **object.size** (x) ## 800000040 bytes **object_size** (x) _# from pryr_ ## 800 MB **gc** () ## used (Mb) gc trigger (Mb) max used (Mb) ## Ncells 8.31e+05 44.4 1.44e+06 77.1 1.44e+06 77.1 ## Vcells 1.21e+08 926.8 1.75e+08 1337.6 1.22e+08 927.0 **mem_used** () _# from pryr_

75

---

[← %% is modulo operator - it gives the remainder](39-is-modulo-operator---it-gives-the-remainder.md) · [Up: contents](index.md) · [Unit 04 — programming Part 41 — →](41-unit-04-programming-part-41.md)
