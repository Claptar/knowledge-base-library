---
title: Unit 04 — programming Part 32 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 32 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can retrieve and assign objects in a particular environment and/or namespace as follows:

lm <- **function** () { **return** ( **NULL** )} _# this seems dangerous but isn't_ x <- 1:3; y <- **rnorm** (3); mod <- **lm** (y ~ x)

**## Error in lm(y ~ x): unused argument (y ~ x)** mod <- **get** ('lm', pos = 'package:stats')(y ~ x) mod <- stats:: **lm** (y ~ x) _# an alternative # :: is the namespace resolution operator_ **rm** (lm) mod <- **lm** (y ~ x)

Note that our (bogus) _lm()_ function masks but does not overwrite the default function. If we remove ours, then the default one is still there.

### **6.9 Frames and the call stack**

R keeps track of the call stack, which is the set of nested calls to functions. The stack operates like a stack of cafeteria trays - when a function is called, it is added to the stack (pushed) and when it finishes, it is removed (popped). There are a bunch of functions that let us query what frames are on the stack and access objects in particular frames of interest. This gives us the ability to work with objects in the environment(s) from which a function was called.

_sys.nframe()_ returns the number of the current frame and _sys.parent()_ the number of the parent, while _parent.frame()_ gives the name of the environment of the parent frame. Careful: here, _parent_ refers to the parent in terms of the call stack and has nothing to do with enclosing environments. _sys.frame()_ gives the name of the environment for a given frame number (for non-negative numbers). For negative numbers, it goes back that many frames in the call stack and returns the name of the associated environment. I won’t print the results here because _knitr_ messes up the frame counting somehow.

57

_## NOTE: run this chunk outside RStudio as it seems to inject additional_ **sys.nframe** () f <- **function** () { **cat** ('f: Frame number is ', **sys.nframe** (), '; parent frame number is ', **sys.parent** (), '.\n', sep = '') **cat** ('f: Frame (i.e., environment) is: ') **print** ( **sys.frame** ( **sys.nframe** ())) **cat** ('f: Parent is ') **print** ( **parent.frame** ()) **cat** ('f: Two frames up is ') **print** ( **sys.frame** (-2)) } **f** () f2 <- **function** () { **cat** ('f2: Frame (i.e., environment) is: ') **print** ( **sys.frame** ( **sys.nframe** ())) **cat** ('f2: Parent is ') **print** ( **parent.frame** ()) **f** () } **f2** () Now let’s look at some code that gets more information about the call stack and the frames involved using _sys.status()_ , _sys.calls()_ , _sys.parents()_ and _sys.frames()_ . _# exploring functions that give us information the frames in the stack_ g <- **function** (y) { gg <- **function** () { _# this gives us the information from sys.calls(), sys.parents() #print(sys.status())_ tmp <- **sys.status** () **print** (tmp) } **if** (y > 0) **g** (y-1) **else gg** () } **g** (3)

58

Challenge: why did I not do print(sys.status()) directly?

If you’re interested in parsing a somewhat complicated example of frames in action, Adler provides a user-defined timing function that evaluates statements in the calling frame.

### **6.10 Alternatives to pass by value in R**

There are occasions we do not want to pass by value. In addition to avoiding copies and the attendant computation and memory use, another reason is when we want a function to modify a complicated object without having to return it and re-assign it in the parent environment. There are several work-arounds:

1. We can use Reference Class (or R6) objects.

2. We can access the object in the enclosing environment as a ’global variable’, as we’ve seen when discussing scoping. More generally we can access the object using _get()_ , specifying the environment from which we want to obtain the variable. To specify the location of an object when using _get()_ , we can generally specify (1) a position in the search path, (2) an explicit environment, or (3) a location in the call stack by using _sys.frame()_ . However we cannot change the value of the object in the parent environment without some additional tools:

   - (a) We can use the ’<<-’ operator to assign into an object in the parent environment (provided an object of that name exists in the parent environment).

   - (b) We can also use _assign()_ , specifying the environment in which we want the assignment to occur.

While these techniques are possible and ok for exploratory coding, they’re bad practice for more formal code development.

3. We can use replacement functions (Section 6.6), which hide the reassignment in the parent environment from the user. Note that a second copy is generally created in this case, but the original copy is quickly removed.

4. We can use a _closure_ , which is a function with associated data. This involves creating one or more functions within a function call and returning the function(s) as the output. When one executes the original function, the new functions are created and returned as a list and one can call the functions in that list. Those functions then can access objects in the enclosing environment (the environment of the original function) and can use ‘<<-‘ to assign into the

59

enclosing environment, to which all the functions have access. Chambers provides an example of this in Sec. 5.4.

x <- **rnorm** (10) f <- **function** (input){ data <- input g <- **function** (param) **return** (param * data) **return** (g) } myFun <- **f** (x) **rm** (x) _# to demonstrate we no longer need x_ **myFun** (3) ## [1] -2.7857 -0.8842 -0.0173 7.2140 2.2908 -2.3970 ## [7] -3.4430 -0.8684 -0.8976 -1.2345 x <- **rnorm** (1e7) myFun <- **f** (x) **object.size** (myFun) _# hmmm_ ## 1560 bytes **object.size** ( **environment** (myFun)$data) ## 80000040 bytes

Here’s a fun example. You might do this with an _apply()_ variant, in particular _replicate()_ , but this is slick:

make_container <- **function** (n) { x <- **numeric** (n) i <- 1 **function** (value = **NULL** ) { **if** ( **is.null** (value)) { **return** (x) } **else** {

60

x[i] <<- value i <<- i + 1 } } } nboot <- 100 bootmeans <- **make_container** (nboot) data <- faithful[ , 1] _# Old Faithful geyser eruption lengths_ **for** (i **in** 1:nboot)

**bootmeans** ( **mean** ( **sample** (data, **length** (data), replace=TRUE)))

_# this will place results in x in the function env't and you can grab it out_ **bootmeans** ()

---

[← Unit 04 — programming Part 31 —](31-unit-04-programming-part-31.md) · [Up: contents](index.md) · [Unit 04 — programming Part 33 — →](33-unit-04-programming-part-33.md)
