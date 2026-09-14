---
title: Unit 04 — programming Part 37 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 37 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can also see the nestedness of environments using the following code, using _environmentName()_ , which prints out a nice-looking version of the environment name.

x <- **environment** (lm)

**while** ( **environmentName** (x) != **environmentName** ( **emptyenv** ())) { **print** ( **environmentName** (x)) x <- **parent.env** (x) } ## [1] "stats" ## [1] "imports:stats" ## [1] "base" ## [1] "R_GlobalEnv" ## [1] "package:codetools" ## [1] "package:fields" ## [1] "package:maps" ## [1] "package:spam" ## [1] "package:grid" ## [1] "package:dotCall64" ## [1] "package:R6" ## [1] "package:methods" ## [1] "package:dplyr" ## [1] "package:pryr"

60

- ## [1] "package:knitr" ## [1] "package:stats"

- ## [1] "package:graphics" ## [1] "package:grDevices" ## [1] "package:utils" ## [1] "package:datasets" ## [1] "package:SCF" ## [1] "Autoloads" ## [1] "base"

**library** (pryr)

x <- **environment** (lm)

**parenvs** (x, all = TRUE)

- ## label

|##|1|<environment|:|namespace:stats>|
|---|---|---|---|---|
|##|2|<environment|:|0x2b586d8>|
|##|3|<environment|:|namespace:base>|
|##|4|<environment|:|R_GlobalEnv>|
|##|5|<environment|:|package:codetools>|
|##|6|<environment|:|package:fields>|
|##|7|<environment|:|package:maps>|
|##|8|<environment|:|package:spam>|
|##|9|<environment|:|package:grid>|
|##|10|<environment|:|package:dotCall64>|
|##|11|<environment|:|package:R6>|
|##|12|<environment|:|package:methods>|
|##|13|<environment|:|package:dplyr>|
|##|14|<environment|:|package:pryr>|
|##|15|<environment|:|package:knitr>|
|##|16|<environment|:|package:stats>|
|##|17|<environment|:|package:graphics>|
|##|18|<environment|:|package:grDevices>|
|##|19|<environment|:|package:utils>|
|##|20|<environment|:|package:datasets>|
|##|21|<environment|:|package:SCF>|
|##|22|<environment|:|0x1c0cd60>|


61

|##|23|<environ|ment: base>|
|---|---|---|---|
|##|24|<environ|ment: R_EmptyEnv>|
|##||name||
|##|1|""||
|##|2|"imports|:stats"|
|##|3|""||
|##|4|""||
|##|5|"package|:codetools"|
|##|6|"package|:fields"|
|##|7|"package|:maps"|
|##|8|"package|:spam"|
|##|9|"package|:grid"|
|##|10|"package|:dotCall64"|
|##|11|"package|:R6"|
|##|12|"package|:methods"|
|##|13|"package|:dplyr"|
|##|14|"package|:pryr"|
|##|15|"package|:knitr"|
|##|16|"package|:stats"|
|##|17|"package|:graphics"|
|##|18|"package|:grDevices"|
|##|19|"package|:utils"|
|##|20|"package|:datasets"|
|##|21|"package|:SCF"|
|##|22|"Autoloa|ds"|
|##|23|""||
|##|24|""||


Note that eventually the global environment and the environments of the packages are nested within the base environment (of the base package) and the empty environment. Note that here _parent_ **is** referring to the enclosing environment, even though it is best to talk about _enclosing environment_ rather than parent environment.

We can retrieve and assign objects in a particular environment and/or namespace as follows:

lm <- **function** () { **return** ( **NULL** )} _# this seems dangerous but isn't_ x <- 1:3; y <- **rnorm** (3); mod <- **lm** (y ~ x)

62

**## Error in lm(y ~ x): unused argument (y ~ x)** mod <- **get** ('lm', pos = 'package:stats')(y ~ x) mod <- stats:: **lm** (y ~ x) _# an alternative ## :: is the namespace resolution operator_ **rm** (lm) mod <- **lm** (y ~ x)

Note that our (bogus) _lm()_ function masks but does not overwrite the default function. If we remove ours, then the default one is still there.

### **6.10 Alternatives to pass by value in R**

There are occasions we do not want to pass by value. In addition to avoiding copies and the attendant computation and memory use, another reason is when we want a function to modify a complicated object without having to return it and re-assign it in the parent environment. There are several work-arounds:

1. We can use R6 (or Reference Class) objects.

2. We can access the object in the enclosing environment as a ’global variable’, as we’ve seen when discussing scoping. More generally we can access the object using _get()_ , specifying the environment from which we want to obtain the variable. To specify the location of an object when using _get()_ , we can generally specify (1) a position in the search path, (2) an explicit environment, or (3) a location in the call stack by using _sys.frame()_ . However we cannot change the value of the object in the parent environment without some additional tools:

   - (a) We can use the ’<<-’ operator to assign into an object in the parent environment (provided an object of that name exists in the parent environment).

   - (b) We can also use _assign()_ , specifying the environment in which we want the assignment to occur.

While these techniques are possible and ok for exploratory coding, they’re bad practice for more formal code development.

3. We can use replacement functions (Section 6.6), which hide the reassignment in the parent environment from the user. Note that a second copy is generally created in this case, but the original copy is quickly removed.

63

4. We can use a _closure_ , which is a function with associated data. This Wikipedia entry nicely summarizes the idea, which is not an R-specific construct. This involves creating one (or more functions) within a function call and returning the function(s) as the output. When one executes the original function, the new function(s) is created and returned and one can then call that new function(s). The new function then can access objects in the enclosing environment (the environment of the original function) and can use ‘<<-‘ to assign into the enclosing environment, to which the function (or the multiple functions) have access. The nice thing about this compared to using a global variable is that the data in the closure is bound up with the function(s) and is protected from being changed by the user of the closure. Chambers provides an example of this in Sec. 5.4.

x <- **rnorm** (10) f <- **function** (input){ data <- input g <- **function** (param) **return** (param * data) **return** (g) } myFun <- **f** (x) **rm** (x) _# to demonstrate we no longer need x_ **myFun** (3) ## [1] 1.462 2.215 1.727 -0.916 4.535 1.170 -1.864 ## [8] -6.644 3.375 -0.135 x <- **rnorm** (1e7) myFun <- **f** (x) **object.size** (myFun) _# hmmm_ ## 3584 bytes **object.size** ( **environment** (myFun)$data) ## 80000040 bytes **library** (pryr) **object_size** (myFun) _# that's better!_ ## 80 MB

64

Here’s a fun example. You might do this with an _apply()_ variant, in particular _replicate()_ , but this is slick:

make_container <- **function** (n) { x <- **numeric** (n) i <- 1 **function** (value = **NULL** ) { **if** ( **is.null** (value)) { **return** (x) } **else** { x[i] <<- value i <<- i + 1 } } } nboot <- 100 bootmeans <- **make_container** (nboot) data <- faithful[ , 1] _# Old Faithful geyser eruption lengths_ **for** (i **in** 1:nboot) **bootmeans** ( **mean** ( **sample** (data, **length** (data), replace=TRUE))) _## this will place results in x in the function env't and you can grab it out_ **bootmeans** () ## [1] 3.43 3.42 3.37 3.43 3.31 3.57 3.44 3.45 3.41 3.45 ## [11] 3.64 3.60 3.58 3.52 3.61 3.53 3.41 3.44 3.60 3.39 ## [21] 3.54 3.57 3.51 3.49 3.57 3.48 3.43 3.51 3.51 3.48 ## [31] 3.48 3.48 3.51 3.61 3.45 3.52 3.55 3.43 3.50 3.52 ## [41] 3.50 3.46 3.45 3.58 3.36 3.50 3.51 3.56 3.50 3.34 ## [51] 3.39 3.52 3.53 3.43 3.55 3.31 3.54 3.54 3.52 3.51 ## [61] 3.47 3.57 3.47 3.42 3.48 3.39 3.42 3.49 3.53 3.38 ## [71] 3.53 3.60 3.59 3.60 3.45 3.67 3.51 3.60 3.48 3.54 ## [81] 3.44 3.49 3.57 3.54 3.53 3.55 3.50 3.53 3.38 3.46 ## [91] 3.44 3.54 3.34 3.59 3.51 3.55 3.56 3.34 3.42 3.49

• A related approach is to wrap data with a function using _with()_ .

65

x <- **rnorm** (10) myFun2 <- **with** ( **list** (data = x), **function** (param) **return** (param * data)) **rm** (x) **myFun2** (3) ## [1] -4.614 2.132 2.458 4.069 -3.814 3.707 -3.463 ## [8] 2.041 0.021 -2.204 x <- **rnorm** (1e7) myFun2 <- **with** ( **list** (data = x), **function** (param) **return** (param * data)) **object_size** (myFun2) ## 80 MB

**Question** : When would it be useful to have an object carried along with a function as done here?

### **6.11 Creating and working in an environment**

We’ve already talked extensively about the environments that R creates. Occasionally you may want to create your own environment in which to store objects.

e <- **new.env** () **assign** ('x', 3, envir = e) _# same as e$x <- 3_ e$x ## [1] 3 **get** ('x', envir = e, inherits = FALSE) ## [1] 3 _## the FALSE avoids looking for x in the enclosing environments_ e$y <- 5 **ls** (e) ## [1] "x" "y" **rm** ('x', envir = e) **parent.env** (e) ## <environment: R_GlobalEnv>

66

Before the existence of R6 and Reference Classes, using an environment was one way to pass objects by reference, avoiding having to re-assign the output (and in fact R6 classes are just a wrapper around the use of environments). Here’s an example where we iteratively update a random walk (but note that if I were actually doing this I would use an R6 class and not an environment).

myWalk <- **new.env** (); myWalk$pos = 0 nextStep <- **function** (walk) walk$pos <- walk$pos + **sample** ( **c** (-1, 1), size = 1) **nextStep** (myWalk)

We can use _eval()_ to evaluate some code within a specified environment. By default, it evaluates in the result of _parent.frame()_ , which amounts to evaluating in the frame from which _eval()_ was called. _evalq()_ avoids having to use _quote()_ . Here we override the default and evaluate in the _myWalk_ environment we created:

**eval** ( **quote** (pos <- pos + **sample** ( **c** (-1, 1), 1)), envir = myWalk) **evalq** (pos <- pos + **sample** ( **c** (-1, 1), 1), envir = myWalk)

### **6.12 Summing up**

What happens when an R function is evaluated? The user-provided function arguments are evaluated in the calling environment and the results are matched to the argument names in the function definition. A new environment with its own frame is created, with the frame on the call stack. Assignment to the argument names is done in the environment, including any default arguments. The body of the function is evaluated in the environment. Any look-up of variables not found in the environment is done using R’s lexical scoping rules to look in the series of enclosing environments. When the function finishes, the return value is passed back to the calling frame and the function frame is taken off the stack. The environment is removed, unless the environment serves as the enclosing environment of another environment.

---

[← Unit 04 — programming Part 36 —](36-unit-04-programming-part-36.md) · [Up: contents](index.md) · [7 Efficiency →](38-7-efficiency.md)
