---
title: Unit 04 — programming Part 32 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 32 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can see the arguments using _args()_ and extract the arguments using _formals(). formals()_ can be helpful if you need to manipulate the arguments.

f <- **function** (x, y = 2, z = 3 / y) { x + y + z } **args** (f) ## function (x, y = 2, z = 3/y) ## NULL **formals** (f) ## $x ## ## ## $y ## [1] 2 ## ## $z ## 3/y **class** ( **formals** (f)) ## [1] "pairlist"

A _pairlist_ is like a list, but with pairing that in this case pairs argument names with default values.

_match.call()_ will show the user-suppled arguments explicitly matched to named arguments.

**match.call** (definition = mean, call = **quote** ( **mean** (y, na.rm = TRUE))) ## mean(x = y, na.rm = TRUE)

44

_<mark>## what do you think quote does? Why is it needed?</mark>_

### **6.3 Outputs**

return(x) will specify _x_ as the output of the function. By default, if _return()_ is not specified, the output is the result of the last evaluated statement. _return()_ can occur anywhere in the function, and allows the function to exit as soon as it is done.

f <- **function** (x) { **if** (x < 0) { **return** (-x^2) } **else** res <- x^2 } **f** (-3) ## [1] -9 **f** (3)

_invisible(x)_ will return _x_ and the result can be assigned in the calling environment but it will not be printed if not assigned:

f <- **function** (x){ **invisible** (x^2) } **f** (3) a <- **f** (3) a ## [1] 9

A function can only return a single object (unlike Matlab, e.g.), but of course we can tack things together as a list and return that, as with _lm()_ and many other functions.

mod <- **lm** (mpg ~ cyl, data = mtcars) **class** (mod) ## [1] "lm" **is.list** (mod) ## [1] TRUE

45

### **6.4 Frames and the call stack**

R keeps track of the call stack, which is the series of nested calls to functions. The stack operates like a stack of cafeteria trays - when a function is called, it is added to the stack (pushed) and when it finishes, it is removed (popped). There are a bunch of functions that let us query what frames are on the stack and access objects in particular frames of interest. This gives us the ability to work with objects in the frame from which a function was called.

Some terminology: for our purposes we’ll use the terms _frame_ and _environment_ somewhat interchangeably for the moment. A _frame_ or _environment_ is a collection of named objects. (Note that when we talk about variable scope in Section 6.8, we’ll have to be more careful with our terminology.)

_sys.nframe()_ returns the number of the current frame/environment and _sys.parent()_ the number of the parent, while _parent.frame()_ gives the name of the frame/environment of the parent (i.e., the calling) frame. _sys.frame()_ gives the name of the frame/environment for a given frame number (for non-negative numbers). For negative numbers, it goes back that many frames in the call stack and returns the name of the frame/environment. I won’t print the results here because _knitr_ messes up the frame counting somehow.

_## NOTE: run this chunk outside RStudio as it seems to ## inject additional frames_ **sys.nframe** () f <- **function** () { **cat** ('f: Frame number is ', **sys.nframe** (), '; parent frame number is ', **sys.parent** (), '.\n', sep = '') **cat** ('f: Frame (i.e., environment) is: ') **print** ( **sys.frame** ( **sys.nframe** ())) **cat** ('f: Parent is ') **print** ( **parent.frame** ()) **cat** ('f: Two frames up is ') **print** ( **sys.frame** (-2)) } **f** () f2 <- **function** () { **cat** ('f2: Frame (i.e., environment) is: ') **print** ( **sys.frame** ( **sys.nframe** ())) **cat** ('f2: Parent is ') **print** ( **parent.frame** ())

46

**f** () } **f2** ()

Now let’s look at some code that gets more information about the call stack and the frames involved using _sys.status()_ , _sys.calls()_ , _sys.parents()_ and _sys.frames()_ .

_## exploring functions that give us information the frames in the stack_ g <- **function** (y) { gg <- **function** () { _## this gives us the information from sys.calls(), ## sys.parents() and sys.frames() as one object ## print(sys.status())_ tmp <- **sys.status** () **print** (tmp) } **if** (y > 0) **g** (y-1) **else gg** () } **g** (3)

Challenge: why did I not do print(sys.status()) directly?

If you’re interested in parsing a somewhat complicated example of frames in action, Adler provides a user-defined timing function that evaluates statements in the calling frame.

### **6.5 Operators**

Operators, such as ’ _+_ ’, ’ _[_ ’ are just functions, but their arguments can occur both before and after the function call:

a <- 7; b <- 3 _# let's think about the following as a mathematical function # -- what's the function call?_ a + b ## [1] 10 **`+`** (a, b) ## [1] 10

47

In general, you can use back-ticks to refer to the operators as operators instead of characters. In some cases single or double quotes also work. We can look at the code of an operator as follows using back-ticks to escape out of the standard R parsing, e.g., ‘%*%‘.

Finally, since an operator is just a function, you can use it as an argument in various places:

|x <br>**ou**|<- 1:<br>**ter**(x|3; y <- **c**(100,200,300)<br>, y, `+`)|
|---|---|---|
|##||[,1] [,2] [,3]|
|##|[1,]|101<br>201<br>301|
|##|[2,]|102<br>202<br>302|
|##|[3,]|103<br>203<br>303|
|my|List|<- **list**(**list**(a = 'new york', b = 1:5), **list**(a = 'california', b = 6:1|
|re|sult|<- **lapply**(myList, `[[`, 2)|
|re|sult||
|##|[[1]|]|
|##|[1]|1 2 3 4 5|
|##|||
|##|[[2]|]|
|##|[1]|6<br>7<br>8<br>9 10|
|_## _|_note_|_that the index "2" is the additional argument to the [[ function_|
|my|Mat <|- **sapply**(myList, `[[`, 2)|
|my|Mat||
|##||[,1] [,2]|
|##|[1,]|1<br>6|
|##|[2,]|2<br>7|
|##|[3,]|3<br>8|
|##|[4,]|4<br>9|
|##|[5,]|5<br>10|
|**cb**|**ind**(m|yList[[1]][[2]], myList[[2]][[2]])<br>_## equivalent but doesn't scale_|
|##||[,1] [,2]|
|##|[1,]|1<br>6|
|##|[2,]|2<br>7|


48

---

[← Unit 04 — programming Part 31 —](31-unit-04-programming-part-31.md) · [Up: contents](index.md) · [Unit 04 — programming Part 33 — →](33-unit-04-programming-part-33.md)
