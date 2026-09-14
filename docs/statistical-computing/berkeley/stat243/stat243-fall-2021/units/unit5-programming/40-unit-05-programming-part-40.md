---
title: Unit 05 — programming Part 40 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 40 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The old version of _mat_ still exists until R’s memory management cleans it up, but it’s no longer referred to by the symbol ’ _mat_ ’. Occasionally this sort of thing might cause memory usage to increase (for example it’s possible if you’re doing replacements on large objects within a loop), but in general things should be fine.

You can define your own replacement functions like this, with the requirements that the last argument be named ’ _value_ ’ and that the function return the entire object:

yog <- **list** (firstName = 'Yogi', lastName = 'Bear') ` firstName<- ` <- **function** (obj, value){ obj$firstName <- value **return** (obj) } **firstName** (yog) <- 'Yogisandra'

We can use replacement functions with S3 classes we define. Again, picking up our example from our discussion of S3 OOP, this is again a bit silly but we could do the following. We need to define the generic replacement function and then the class-specific one.

73

` age<- ` <- **function** (x, ...) **UseMethod** ("age<-") ` age<-.bear ` <- **function** (object, value){ object$age <- value **return** (object) } **age** (older_yog) <- 60 older_yog ## $firstname ## [1] "Yogi" ## ## $surname ## [1] "the Bear" ## ## $age ## [1] 60 ## ## attr(,"class") ## [1] "bear"

### **6.12 Summing up**

Now that we’ve seen all that, this summary that I included at the start of Section 6 should make sense.

What happens when an R function is evaluated? The user-provided function arguments are evaluated in the calling environment and the results are matched to the argument names in the function definition. A new environment with its own frame is created, with the frame on the call stack. Assignment to the argument names is done in the environment, including any default arguments (as promises if the input arguments are variables or code). The body of the function is evaluated in the environment. Any look-up of variables not found in the environment is done using R’s lexical scoping rules to look in the series of enclosing environments. When the function finishes, the return value is passed back to the calling frame and the function frame is taken off the stack. The environment is removed, unless the environment serves as the enclosing environment of another environment.

74

---

[← $surname ## [1] "the Bear" ## ## $age ## [1] 35 ## ## attr(,"class") ## [1] "bear"](39-age-1-35-attr-class-1-bear.md) · [Up: contents](index.md) · [7 Efficiency →](41-7-efficiency.md)
