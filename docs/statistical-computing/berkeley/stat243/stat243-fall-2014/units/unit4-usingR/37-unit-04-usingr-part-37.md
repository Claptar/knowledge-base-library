---
title: Unit 04 — usingR Part 37 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 37 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The enclosing environments for a function from an attached package are a bit more complicated:

x <- **environment** (lm) x ## <environment: namespace:stats> **while** ( **environmentName** (x) != **environmentName** ( **emptyenv** ())) { **print** ( **environmentName** (x)) x <- **parent.env** (x) } ## [1] "stats" ## [1] "imports:stats" ## [1] "base" ## [1] "R_GlobalEnv" ## [1] "package:fields" ## [1] "package:maps" ## [1] "package:spam" ## [1] "package:grid" ## [1] "package:methods" ## [1] "package:knitr" ## [1] "package:stats" ## [1] "package:graphics" ## [1] "package:grDevices" ## [1] "package:utils" ## [1] "package:datasets" ## [1] "package:SCF" ## [1] "Autoloads" ## [1] "base"

We can retrieve and assign objects in a particular environment as follows:

53

lm <- **function** () { **return** ( **NULL** ) } _# this seems dangerous but isn't_ x <- 1:3 y <- **rnorm** (3) mod <- **lm** (y ~ x) **## Error: unused argument (y ~ x)** mod <- **get** ("lm", pos = "package:stats")(y ~ x) mod <- stats:: **lm** (y ~ x) _# an alternative_ **rm** (lm) mod <- **lm** (y ~ x)

Note that our (bogus) _lm()_ function masks but does not overwrite the default function. If we remove ours, then the default one is still there.

### **7.5 Frames and the call stack**

R keeps track of the call stack, which is the set of nested calls to functions. The stack operates like a stack of cafeteria trays - when a function is called, it is added to the stack (pushed) and when it finishes, it is removed (popped). There are a bunch of functions that let us query what frames are on the stack and access objects in particular frames of interest. This gives us the ability to work with objects in the environment(s) from which a function was called.

_sys.nframe()_ returns the number of the current frame and _sys.parent()_ the number of the parent, while parent.frame() gives the name of the environment of the parent frame. Careful: here, _parent_ refers to the parent in terms of the call stack and has nothing to do with enclosing environments. _sys.frame()_ gives the name of the environment for a given frame number (for non-negative numbers). For negative numbers, it goes back that many frames in the call stack and returns the name of the associated environment. I won’t print the results here because _knitr_ messes up the frame counting somehow.

_## NOTE: run this chunk outside RStudio as it seems to ## inject additional frames_ **sys.nframe** () f <- **function** () { **cat** ("f: Frame number is ", **sys.nframe** (), "; parent frame number is ",

54

**sys.parent** (), ".\n", sep = "") **cat** ("f: Frame (i.e., environment) is: ") **print** ( **sys.frame** ( **sys.nframe** ())) **cat** ("f: Parent is ") **print** ( **parent.frame** ()) **cat** ("f: Two frames up is ") **print** ( **sys.frame** (-2)) } **f** () f2 <- **function** () { **cat** ("f2: Frame (i.e., environment) is: ") **print** ( **sys.frame** ( **sys.nframe** ())) **cat** ("f2: Parent is ") **print** ( **parent.frame** ()) **f** () } **f2** () Now let’s look at some code that gets more information about the call stack and involved using _sys.status()_ , _sys.calls()_ , _sys.parents()_ and _sys.frames()_ . _# exploring functions that give us information the # frames in the stack_ g <- **function** (y) { gg <- **function** () { _# this gives us the information from sys.calls(), # sys.parents() and sys.frames() as one object # print(sys.status())_ tmp <- **sys.status** () **print** (tmp) } **if** (y > 0) **g** (y - 1) **else gg** () } **g** (3)

Now let’s look at some code that gets more information about the call stack and the frames involved using _sys.status()_ , _sys.calls()_ , _sys.parents()_ and _sys.frames()_ .

Challenge: why did I not do print(sys.status()) directly?

55

If you’re interested in parsing a somewhat complicated example of frames in action, Adler provides a user-defined timing function that evaluates statements in the calling frame.

### **7.6 with() and within()**

_with()_ provides a clean way to use a function (or any R code, specified as R statements enclosed within {}, unless you are evaluating a single expression as in the demo here) within the context of a data frame (or an environment). _within()_ is similar, evaluating within the context of a data frame or a list, but it allows you to modify the data frame (or list) and returns the result.

**with** (mtcars, cyl * mpg)

---

[← Unit 04 — usingR Part 36 —](36-unit-04-usingr-part-36.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 38 — →](38-unit-04-usingr-part-38.md)
