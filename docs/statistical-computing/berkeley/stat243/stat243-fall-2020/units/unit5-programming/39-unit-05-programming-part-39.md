---
title: Unit 05 — programming Part 39 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 39 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

70

} older_yog <- yog + 15 older_yog ## $firstname ## [1] "Yogi" ## ## $surname ## [1] "the Bear" ## ## $age ## [1] 35 ## ## attr(,"class") ## [1] "bear"

### **6.11 Unexpected functions and replacement functions**

All code in R can be viewed as a function call.

What do you think is the functional version of the following code? What are the arguments?

**if** (x > 27){ **print** (x) } **else** { **print** ("too small") }

Assignments that involve functions or operators on the left-hand side (LHS) are called _replacement expressions_ or _replacement functions._ These can be quite handy. Here are a few examples:

**diag** (mat) <- **c** (3, 2) **is.na** (vec) <- 3 **names** (df) <- **c** ('var1', 'var2')

Replacement expressions are actually function calls. The R interpreter calls the replacement function (which often creates a new object that includes the replacement) and then assigns the result to the name of the original object.

71

mat <- **matrix** ( **rnorm** (4), 2, 2) **diag** (mat) <- **c** (3, 2) mat <- **`diag<-`** (mat, **c** (10, 21)) base::`diag<-` ## function (x, value) ## { ## dx <- dim(x) ## if (length(dx) != 2L) ## stop("only matrix diagonals can be replaced") ## len.i <- min(dx) ## len.v <- length(value) ## if (len.v != 1L && len.v != len.i) ## stop("replacement diagonal has wrong length") ## if (len.i) { ## i <- seq_len(len.i) ## x[cbind(i, i)] <- value ## } ## x ## } ## <bytecode: 0x5639b0103008> ## <environment: namespace:base>

The old version of _mat_ still exists until R’s memory management cleans it up, but it’s no longer referred to by the symbol ’ _mat_ ’. Occasionally this sort of thing might cause memory usage to increase (for example it’s possible if you’re doing replacements on large objects within a loop), but in general things should be fine.

You can define your own replacement functions like this, with the requirements that the last argument be named ’ _value_ ’ and that the function return the entire object:

yog <- **list** (firstName = 'Yogi', lastName = 'Bear') `firstName<-` <- **function** (obj, value){ obj$firstName <- value **return** (obj) } **firstName** (yog) <- 'Yogisandra'

72

We can use replacement functions with S3 classes we define. Again, picking up our example from our discussion of S3 OOP, this is again a bit silly but we could do the following. We need to define the generic replacement function and then the class-specific one.

`age<-` <- **function** (x, ...) **UseMethod** ("age<-") `age<-.bear` <- **function** (object, value){ object$age <- value **return** (object) } **age** (older_yog) <- 60 older_yog ## $firstname ## [1] "Yogi" ## ## $surname ## [1] "the Bear" ## ## $age ## [1] 60 ## ## attr(,"class") ## [1] "bear"

### **6.12 Summing up**

Now that we’ve seen all that, this summary that I included at the start of Section 6 should make sense.

What happens when an R function is evaluated? The user-provided function arguments are evaluated in the calling environment and the results are matched to the argument names in the function definition. A new environment with its own frame is created, with the frame on the call stack. Assignment to the argument names is done in the environment, including any default arguments. The body of the function is evaluated in the environment. Any look-up of variables not found in the environment is done using R’s lexical scoping rules to look in the series of enclosing

73

environments. When the function finishes, the return value is passed back to the calling frame and the function frame is taken off the stack. The environment is removed, unless the environment serves as the enclosing environment of another environment.

---

[← Unit 05 — programming Part 38 —](38-unit-05-programming-part-38.md) · [Up: contents](index.md) · [7 Efficiency →](40-7-efficiency.md)
