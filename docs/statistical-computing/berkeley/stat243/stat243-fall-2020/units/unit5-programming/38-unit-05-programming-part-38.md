---
title: Unit 05 — programming Part 38 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 38 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note that eventually the global environment and the environments of the packages are nested within the base environment (of the base package) and the empty environment. Note that here _parent_ **is** referring to the enclosing environment, even though it is best to talk about _enclosing environment_ rather than parent environment.

We can retrieve and assign objects in a particular environment and/or namespace as follows:

lm <- **function** () { **return** ( **NULL** )} _# this seems dangerous but isn't_ x <- 1:3; y <- **rnorm** (3); mod <- **lm** (y ~ x)

**## Error in lm(y ~ x): unused argument (y ~ x)** mod <- **get** ('lm', pos = 'package:stats')(y ~ x) mod <- stats:: **lm** (y ~ x) _# an alternative ## :: is the namespace resolution operator_ **rm** (lm) mod <- **lm** (y ~ x)

Note that our (bogus) _lm()_ function masks but does not overwrite the default function. If we remove ours, then the default one is still there.

### **6.8 Alternatives to pass by value in R**

There are occasions we do not want to pass by value. In addition to avoiding copies and the attendant computation and memory use, another reason is when we want a function to modify a

65

complicated object without having to return it and re-assign it in the parent environment. There are several work-arounds:

1. We can use R6 (or Reference Class) objects.

2. We can use a _closure_ , as discussed previously.

3. We can access the object in the enclosing environment as a ’global variable’, as we’ve seen when discussing scoping. More generally we can access the object using _get()_ , specifying the environment from which we want to obtain the variable. To specify the location of an object when using _get()_ , we can generally specify (1) a position in the search path, (2) an explicit environment, or (3) a location in the call stack by using _sys.frame()_ . However we cannot change the value of the object in the parent environment without some additional tools:

   - (a) We can use the ’<<-’ operator to assign into an object in the parent environment (provided an object of that name exists in the parent environment).

   - (b) We can also use _assign()_ , specifying the environment in which we want the assignment to occur.

While these techniques are possible and ok for exploratory coding, they’re bad practice for more formal code development.

4. We can use replacement functions (Section 6.11), which hide the reassignment in the parent environment from the user. Note that a second copy is generally created in this case, but the original copy is quickly removed.

- A related approach is to wrap data with a function using _with()_ .

x <- **rnorm** (10)

myFun2 <- **with** ( **list** (data = x), **function** (param) **return** (param * data)) **rm** (x) **myFun2** (3) ## [1] -1.414 3.411 5.041 -2.310 -0.182 2.426 -1.747 ## [8] 0.283 0.123 -2.021 x <- **rnorm** (1e7)

myFun2 <- **with** ( **list** (data = x), **function** (param) **return** (param * data)) **object_size** (myFun2) ## 80 MB

66

**Question** : When would it be useful to have an object carried along with a function as done here?

### **6.9 Creating and working in an environment (optional)**

We’ve already talked extensively about the environments that R creates. Occasionally you may want to create your own environment in which to store objects.

e <- **new.env** () **assign** ('x', 3, envir = e) _# same as e$x <- 3_ e$x ## [1] 3 **get** ('x', envir = e, inherits = FALSE) ## [1] 3 _## the FALSE avoids looking for x in the enclosing environments_ e$y <- 5 **ls** (e) ## [1] "x" "y" **rm** ('x', envir = e) **parent.env** (e) ## <environment: R_GlobalEnv>

Before the existence of R6 and Reference Classes, using an environment was one way to pass objects by reference, avoiding having to re-assign the output (and in fact R6 classes are just a wrapper around the use of environments). Here’s an example where we iteratively update a random walk (but note that if I were actually doing this I would use an R6 class and not an environment).

myWalk <- **new.env** (); myWalk$pos = 0 nextStep <- **function** (walk) walk$pos <- walk$pos + **sample** ( **c** (-1, 1), size = 1) **nextStep** (myWalk)

67

We can use _eval()_ to evaluate some code within a specified environment. By default, it evaluates in the result of _parent.frame()_ , which amounts to evaluating in the frame from which _eval()_ was called. _evalq()_ avoids having to use _quote()_ . Here we override the default and evaluate in the _myWalk_ environment we created:

**eval** ( **quote** (pos <- pos + **sample** ( **c** (-1, 1), 1)), envir = myWalk) **evalq** (pos <- pos + **sample** ( **c** (-1, 1), 1), envir = myWalk)

### **6.10 Operators**

Operators, such as ’ _+_ ’, ’ _[_ ’ are just functions, but their arguments can occur both before and after the function call:

a <- 7; b <- 3 _# let's think about the following as a mathematical function # -- what's the function call?_ a + b ## [1] 10 **`+`** (a, b) ## [1] 10

In general, you can use back-ticks to refer to the operators as operators instead of characters. In some cases single or double quotes also work. We can look at the code of an operator as follows using back-ticks to escape out of the standard R parsing, e.g., ‘%*%‘.

Finally, since an operator is just a function, you can use it as an argument in various places:

x <- 1:3; y <- **c** (100,200,300) **outer** (x, y, `+`) ## [,1] [,2] [,3] ## [1,] 101 201 301 ## [2,] 102 202 302 ## [3,] 103 203 303 myList <- **list** ( **list** (state = 'new york', value = 1:5),

68

|||**list**(state = 'california', value = 6:10),|
|---|---|---|
|||**list**(state = 'delaware', value = 11:15))|
|re|sult|<- **lapply**(myList, `[[`, 2)|
|re|sult||
|##|[[1]|]|
|##|[1]|1 2 3 4 5|
|##|||
|##|[[2]|]|
|##|[1]|6<br>7<br>8<br>9 10|
|##|||
|##|[[3]|]|
|##|[1]|11 12 13 14 15|
|_## _|_note_|_that the index "2" is the additional argument to the [[ function_|
|my|Mat <|- **sapply**(myList, `[[`, 2)|
|my|Mat||
|##||[,1] [,2] [,3]|
|##|[1,]|1<br>6<br>11|
|##|[2,]|2<br>7<br>12|
|##|[3,]|3<br>8<br>13|
|##|[4,]|4<br>9<br>14|
|##|[5,]|5<br>10<br>15|
|**cb**|**ind**(m|yList[[1]][[2]], myList[[2]][[2]])<br>_## equivalent but doesn't scale_|
|##||[,1] [,2]|
|##|[1,]|1<br>6|
|##|[2,]|2<br>7|
|##|[3,]|3<br>8|
|##|[4,]|4<br>9|
|##|[5,]|5<br>10|


You can define your own _binary_ operator (an operator taking two arguments) using a string inside _%_ symbols. Here’s how we could do Python-style string addition:

69

`%+%` <- **function** (a, b) **paste0** (a, b, collapse = '') "Hi " %+% "there" ## [1] "Hi there"

Since operators are just functions, there are cases in which there are optional arguments that we might not expect. Here’s how to pass a sometimes useful argument to the bracket operator (in this case avoiding conversion from a matrix to a vector, which can mess up subsequent code).

mat <- **matrix** (1:4, 2, 2) mat[ , 1] ## [1] 1 2 mat[ , 1, drop = FALSE] _# what's the difference?_ ## [,1] ## [1,] 1 ## [2,] 2

We can also use operators with our S3 classes. Picking up our example from our discussion of S3 OOP, the following example will be a bit silly (it would make more sense with a class that is a mathematical object) but indicates the power of having methods.

yog <- **list** (firstname = 'Yogi', surname = 'the Bear', age = 20) **class** (yog) <- 'bear'

**methods** (`+`)

---

[← Unit 05 — programming Part 37 —](37-unit-05-programming-part-37.md) · [Up: contents](index.md) · [Unit 05 — programming Part 39 — →](39-unit-05-programming-part-39.md)
