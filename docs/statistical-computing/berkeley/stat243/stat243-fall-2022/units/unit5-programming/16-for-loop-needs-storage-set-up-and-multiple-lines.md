---
title: 'for loop: needs storage set up and multiple lines'
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# for loop: needs storage set up and multiple lines

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

results <- list()
length(results) <- length(subsets)
for(i in seq_along(subsets))
  results[[i]] <- analysis_function(subsets[[i]])
```

Map operations are also at the heart of the famous map-reduce paradigm, used in Hadoop and Spark for big data processing.

## Function evaluation, frames, and the call stack

### Overview

When we run code, we end up calling functions inside of other function calls.
This leads to a nested series of function calls. The series of calls is the *call stack*.
The stack operates like a stack of cafeteria trays - when a
function is called, it is added to the stack (pushed) and when it
finishes, it is removed (popped).

Understanding the series of calls is important when reading error messages and debugging.
In Python, when an error occurs, the call stack is shown, which has the advantage of
giving the complete history of what led to the error and the disadvantage of producing
often very verbose output that can be hard to understand. In R, only the function in which
the error occurs is shown, but you can see the full call stack by invoking `traceback()` (see the [debugging tutorial](https://github.com/berkeley-scf/tutorial-R-debugging)).

What happens when an R function is evaluated?

  - The user-provided function arguments are evaluated in the calling environment and the results are
matched to the argument names in the function definition.
  - A new environment with its own frame is created, with the frame on the call stack. Assignment to the argument names is done in the environment, including any default arguments.
  - The body of the function is evaluated in the environment. Any look-up of variables not found in the
environment is done using R's lexical scoping rules to look in the
series of enclosing environments.
  - When the function finishes, the return
value is passed back to the calling frame and the function frame is
taken off the stack. The environment is removed, unless the environment
serves as the enclosing environment of another environment.

I'm not expecting you to fully understand that previous paragraph and
all the terms in it yet. We'll see all the details as we proceed through this Unit.

### Frames and the call stack

R keeps track of the call stack. Each function call is associated with
a *frame* that contains the local variables for that function call.

There are a bunch of functions that let us query what frames are on the
stack and access objects in particular frames of interest. This gives us
the ability to work with objects in the frame from which a function was
called.

Some terminology: for our purposes we'll use the terms *frame* and
*environment* somewhat interchangeably for the moment. A *frame* or
*environment* is a collection of named objects. (Note that when we talk
about variable scope later in this Unit, we'll have to be more careful with
our terminology.) So in the context of a function call, the frame is the
set of local variables available in the function, including arguments
passed to the function.

R provides some functions that allow you to query the call stack and its frames.
*sys.nframe* returns the number of the current frame/environment and
*sys.parent* the number of the parent, while *parent.frame* gives
the name of the frame/environment of the parent (i.e., the calling)
frame. *sys.frame* gives the name of the frame/environment for a given
frame number (for non-negative numbers). For negative numbers, it goes
back that many frames in the call stack and returns the name of the
frame/environment. I need to manually insert the output here because the R Markdown processing
up the frame counting somehow.


```r
sys.nframe()
f <- function() {
	cat('in f: Frame number is ', sys.nframe(),
            '; parent frame number is ', sys.parent(), '.\n', sep = '')
	cat('in f: Frame (i.e., environment) is: ')
	print(sys.frame(sys.nframe()))
	cat('in f: Parent is ')
	print(parent.frame())
	cat('in f: Two frames up is ')
	print(sys.frame(-2))
}
f()
```

```
in f: Frame number is 1; parent frame number is 0.
in f: Frame (i.e., environment) is: <environment: 0x55a4d71beb88>
in f: Parent is <environment: R_GlobalEnv>
in f: Two frames up is Error in sys.frame(-2) : not that many frames on the stack
```

```r
ff <- function() {
	cat('in ff: Frame (i.e., environment) is: ')
	print(sys.frame(sys.nframe()))
	cat('in ff: Parent is ')
	print(parent.frame())
	f()
}
ff()
```

```
in ff: Frame (i.e., environment) is: <environment: 0x55a4d7391700>
in ff: Parent is <environment: R_GlobalEnv>
in f: Frame number is 2; parent frame number is 1.
in f: Frame (i.e., environment) is: <environment: 0x55a4d7393b38>
in f: Parent is <environment: 0x55a4d7391700>
in f: Two frames up is <environment: R_GlobalEnv>
```

Next we'll use a recursive function to illustrate what information we can gather
about the call stack using *sys.status*. *sys.status* gives extensive information about the call
stack and the frames involved (*sys.status* uses *sys.calls*,
*sys.parents* and *sys.frames*).


```r
g <- function(y) {
    if(y > 0) g(y-1) else gg()
}

## Ultimately, gg() is called, and it prints out info about the call stack
gg <- function() {
    ## this gives us the information from sys.calls(),
    ##   sys.parents() and sys.frames() as one object
    ## Rather than running print(sys.status()),
    ## which would involve adding print() to the call stack,
    ## we'll run sys.status and then print the result out.
    tmp <- sys.status()
    print(tmp)
}

g(3)
```

```
$sys.calls
$sys.calls[[1]]
g(3)

$sys.calls[[2]]
if(y > 0) g(y-1) else gg()

$sys.calls[[3]]
if(y > 0) g(y-1) else gg()

$sys.calls[[4]]
if(y > 0) g(y-1) else gg()

$sys.calls[[5]]
if(y > 0) g(y-1) else gg()

$sys.calls[[6]]
tmp <- sys.status()


$sys.parents
[1] 0 1 2 3 4 5

$sys.frames
$sys.frames[[1]]
<environment: 0x55a4d63479e8>

$sys.frames[[2]]
<environment: 0x55a4d6347ba8>

$sys.frames[[3]]
<environment: 0x55a4d5736638>

$sys.frames[[4]]
<environment: 0x55a4d5732028>

$sys.frames[[5]]
<environment: 0x55a4d5732098>

$sys.frames[[6]]
<environment: 0x55a4d5732488>
```

> **Challenge**
> Why did I not do `print(sys.status())` directly?

If you're interested in parsing a somewhat complicated example of frames
in action, Adler provides a user-defined timing function that evaluates
statements in the calling frame.

## Function inputs and outputs

### Arguments

Arguments can be specified by position (based on the order of the inputs)
or by name, using `name = value`. R first tries to match arguments by name and
then by position. In general the more important arguments are specified
first. You can see the arguments and defaults for a function using
*args*:

```r
args(lm)
```

You can't generally tell directly which arguments are required; in
general you'd need to look at the documentation. For example,
`lm()` requires `formula` but not `data`, `subset`, etc., even though
none of them have default arguments.

R will error out if it
is expecting an argument, rather than looking for that argument
elsewhere.

```r
print(sum)
sum()
print(quantile)
try(quantile())

x <- 1
y <- 2
myfun <- function(x) {
    z <- y+3
    w <- x+3
}
try(myfun())
```

You can check if an argument is missing with `missing()`. Arguments can
also have default values, which may be `NULL`. If you are writing a
function and designate the default as `argname = NULL`, you can check
whether the user provided anything using `is.null(argname)`. The default
values can also relate to other arguments. As an example, consider
*dgamma*:

```r
args(dgamma)
```

Functions may have unspecified arguments, which are designated using
`...`. Unspecified arguments occurring at the beginning of the argument
list are generally a collection of like objects that will be manipulated
(consider *paste*, *c*, and *rbind*), while unspecified arguments
occurring at the end are often optional arguments (consider *plot*).
These optional arguments are sometimes passed along to a function within
the function. For example, here's my own wrapper for plotting, where any
additional arguments specified by the user (such as `xlab` and `ylab`) will get passed along to
plot:

```r
pplot <- function(x, y, pch = 16, cex = 0.4, ...) {
	plot(x, y, pch = pch, cex = cex, ...)
}
pplot(rnorm(10), rnorm(10), xlab = 'x', ylab = 'y')
```

If you want to manipulate what the user passed in as the `...` args,
rather than just passing them along, you can extract them:

```r
myFun <- function(...){
  print(..2)
  args <- list(...)
  print(args[[2]])
}
myFun(1,3,5,7)
```


As we've seen, functions can be passed in as arguments (e.g., see the
variants of *apply* and *lapply*). Note that one does not need to pass in a named
function - you can create the function on the spot - this is called an
*anonymous function* (also called a *lambda function* in some languages
such as Python):

```r
mylist <- list(rnorm(2), rnorm(3), rnorm(5))
sapply(mylist, length)
lapply(mylist, function(x) x[x < 0])
```

We can see the arguments using `args()` and extract the arguments using
`formals()`. `formals()` can be helpful if you need to manipulate the
arguments.

```r
f <- function(x, y = 2, z = 3 / y) {
  x + y + z
}
args(f)
formals(f)
```

*match.call()* will show the user-suppled arguments explicitly matched
to named arguments.

```r
match.call(definition = mean,
  call = quote(mean(y, na.rm = TRUE)))
```

> **Challenge**
> In the above code, what do you think `quote()`does? Why is it needed?

#### Where are arguments evaluated?

User-supplied arguments are evaluated in the calling frame (why?), while
default arguments are evaluated in the frame of the function (why?):

```r
z <- 3
x <- 100
f <- function(x, y = x*3) {x+y}
f(z*5)
```

Here, when `f()` is called and the code is evaluated, `z` is evaluated in the calling frame
and `z*5` is assigned to `x` in the frame of the function, while `x*3`
is evaluated in the frame of the function (using the local `x` that was just created) and assigned to `y`.

### Function outputs

`return(x)` will specify `x` as the output of the function. By default,
if `return()` is not specified, the output is the result of the last
evaluated statement. `return()` can occur anywhere in the function, and
allows the function to exit as soon as it is done.

```r
f <- function(x) {
    if(x < 0) {
        return(-x^2)
    } else res <- x^2
}
f(-3)
f(3)
a <- f(3)
a
```

`invisible(x)` will return `x` and the result can be assigned in the
calling environment but it will not be printed if not assigned:

```r
f <- function(x){
  invisible(x^2)
}
f(3)
a <- f(3)
a
```

A function can only return a single object (unlike Matlab, e.g.), but of
course we can tack things together as a list and return that, as occurs with many functions, such as
*lm*. (Of course `lm()` actually returns an object of the S3 `lm` class, which inherits from the list class.)

```r
mod <- lm(mpg ~ cyl, data = mtcars)
class(mod)
is.list(mod)
```

## Pass by value vs. pass by reference

When talking about programming languages, one often distinguishes
*pass-by-value* and *pass-by-reference*.

*Pass-by-value* means that when a
function is called with one or more arguments, a copy is made of each
argument and the function operates on those copies.

*Pass-by-reference*
means that the arguments are not copied, but rather that information is
passed allowing the function to find and modify the original value of
the objects passed into the function.

In pass-by-value, changes to an
argument made within a function do not affect the value of the argument
in the calling environment. In pass-by-reference changes inside a
function do affect the object outside of the function. R is (roughly)
pass-by-value. R's designers chose not to allow pass-by-reference
because they didn't like the idea that a function could have the side
effect of changing an object. However, passing by reference can
sometimes be very helpful, and we'll see ways of passing by reference
later (and also note our discussion of R6 classes).

Pass-by-value is elegant and modular in that functions do not have side
effects - the effect of the function occurs only through the return
value of the function. However, it can be inefficient in terms of the
amount of computation and of memory used. In contrast, pass-by-reference
is more efficient, but also more dangerous and less modular. It's more
difficult to reason about code that uses pass-by-reference because
effects of calling a function can be hidden inside the function.
Thus pass-by-value is directly related to functional programming.

Arrays in Python are pass-by-reference (but note that tuples are immutable,
so one could not modify a tuple that is passed as an argument).

```python
def myfun(x):
    x[1] = 99

y = [0, 1, 2]
z = myfun(y)
y
```

### Pointers

By way of contrast to a pass-by-value system, I want to briefly discuss
the idea of a pointer, common in compiled languages such as C.

```
int x = 3;
int* ptr;
ptr = &x;
*ptr * 7; // returns 21
```

  - The `int*` declares `ptr` to be a pointer to (the address of) the integer `x`.
  - The `&x` gets the address where `x` is stored.
  - `*ptr` dereferences `ptr`, returning the value in that address (which is 3 since `ptr` is the address of `x`.

Vectors in C are really pointers to a block of memory:

```
int x[10];
```

In this case `x` will be the address of the first element of the vector.
We can access the first element as `x[0]` or `*x`.

Why have we gone into this? In C, you can pass a pointer as an argument
to a function. The result is that only the scalar address is copied and
not the entire object, and inside the function, one can modify the
original object, with the new value persisting on exit from the
function. For example in the following example one passes in the address of an
object and that object is then modified in place, affecting its value when the function
call finishes.

```
int myCal(int* ptr){
    *ptr = *ptr + *ptr;
}

myCal(&x)  # x itself will be modified
```

> **Note** When calling C or C++ from R, one (implicitly) passes pointers to the vectors into C.


### Pointers in R?

Are there pointers in R? From a user perspective, one might say 'no',
because an R programmer can't use pointers explicitly. But pointer-like
behavior is occurring behind the scenes in lots of ways:

  -   Lists in R are essentially vectors of pointers to the elements of the list.
  -   Character vectors in R are essentially pointers to the individual character strings.
  -   Environments behave like pointers and are passed by reference rather than by copy.
  -   R6 objects behave like pointers and are passed by reference, as seen earlier.

We'll see more on these ideas later in the Unit.

### Alternatives to pass by value in R

There are occasions we do not want to pass by value. In addition to
avoiding copies and the  computation and memory use that that causes, another
reason is when we want a function to modify a complicated object without
having to return it and re-assign it in the parent environment. There
are several work-arounds:

1.  We can use R6 (or Reference Class) objects.
2.  We can use a *closure*, as discussed later.
3.  We can access the object in the enclosing environment as a 'global
    variable', as we'll see when  discussing scoping. More generally we
    can access the object using `get()`, specifying the environment from
    which we want to obtain the variable. To specify the location of an
    object when using `get()`, we can generally specify (1) a position
    in the search path, (2) an explicit environment, or (3) a location
    in the call stack by using `sys.frame()`. However we cannot change
    the value of the object in the parent environment without some
    additional tools:
    a.  We can use the `<<-` operator to assign into an object in the
        enclosing environment (provided an object of that name exists in
        the enclosing environment). We'll discuss enclosing environments when we talk about scoping.
    b.  We can also use `assign()`, specifying the environment in which
        we want the assignment to occur.
    While these techniques are possible and ok for exploratory coding,
    they're generally bad practice for more formal code development.
4.  We can use replacement functions, which hide the
    reassignment in the parent environment from the user. Note that a
    second copy is generally created in this case, but the original copy
    is quickly removed.

### Promises and lazy evaluation

In actuality, R is not quite pass-by-value; rather it is
*call-by-value*. Copying of arguments is delayed in two ways:

  - The first is the idea of *promises*, described next. Promises are an example of a general programming concept called *lazy evaluation*.
  - The second is the idea of *copy-on-modify*, described in more detail later. Basically, with copy-on-modify,
copies of arguments are only made if the argument is changed within the
function. Until then the object in the function just refers back to the
original object.

Let's see what a *promise* object is. In function calls, when R matches
user input arguments to formal argument names, it does not (usually)
evaluate the arguments until they are needed, which is called *lazy
evaluation*. Instead the formal arguments are of a special type called a
*promise*. Let's see lazy evaluation in action.

What's strange about this?

```r
f <- function(x) print("hi")
system.time(mean(rnorm(1000000)))
system.time(f(3))
system.time(f(mean(rnorm(1000000))))
```

Here's an even stranger situation. Do you think the
following code will run?

```r
f <- function(a, b = d) {
	d <- a*3;
	return(a*b)
}

b <- 100
f(5)
```


Lazy evaluation is not just an R thing. It also occurs in Tensorflow (particularly version 1),
the Python Dask package, and in Spark. The basic idea is to delay executation until
it's really needed, with the goal that if one does so, the system may be
able to better optimize a series of multiple steps as a joint operation
relative to executing them one by one.


## Variable scope and lookup

### Lexical scoping

In this section, we seek to understand what happens in the following
circumstance. Namely, where does R get the value for the object `x`?

```r
f <- function(y) {
  return(x + y)
}
f(3)
```

To consider variable scope, we need to define the terms *environment*
and *frame*. Environments and frames are closely related.

  -   A *frame* is a collection of named objects.
  -   An *environment* is a frame, with a pointer to the 'enclosing
    environment', i.e., the next environment to look for something in.
    (Be careful as this is different than the parent frame of a
    function, discussed when we were talking about the call stack.)

Variables in the enclosing environment (also called the parent
environment) are available within a function. This is the analog of
*global variables* in other languages. **The enclosing environment is the
environment in which a function is defined, not the environment from
which a function is called.**

This approach is called *lexical scoping*. Python and many other languages
also use lexical scoping.


Why is the enclosing environment defined in this way? Recall our example where
I tried to break the usage of the *lm* function by redefining *lm.fit*.

```r
lm.fit <- function(x) print('hi')
y <- rnorm(10)
x <- rnorm(10)
mod <- lm(y~x)  # this still works!
```

When R looks for `lm.fit` when it is called within `lm`, it looks in the enclosing
environment of `lm`. That is where `lm` is defined, which is the stats package namespace.
It finds `lm.fit` there. All is well! In contrast, if the scoping rules looked for `lm.fit`
where `lm` was called from, then the user-defined `lm.fit` would be found and `lm()`
would not work until that `lm.fit` was removed. That would be a very fragile system!


Let's dig deeper to understand where R looks for non-local variables, illustrating lexical scoping:

```r
x <- 3
f2 <- function() print(x)
f <- function() {
    x <- 7
    f2()
}
f() # what will happen?

x <- 3
f2 <- function() print(x)
f <- function() {
    x <- 7
    f2()
}
x <- 100
f() # what will happen?

x <- 3
f <- function() {
    f2 <- function() { print(x) }
    x <- 7
    f2()
}
f() # what will happen?

x <- 3
f <- function() {
    f2 <- function() { print(x) }
    f2()
}
f() # what will happen?

 ```

Here's a tricky example:

```r
y <- 100
fun_constructor <- function(){
	y <- 10
	g <- function(x) {
            return(x + y)
        }
	return(g)
}
## fun_constructor() creates functions
myfun <- fun_constructor()
myfun(3)
```

Let's work through this:

1.  What is the enclosing environment of the function *g()*?
2.  What does *g()* use for *y*?
3.  When *fun_constructor()* finishes, does its environment disappear?
    What would happen if it did?
4.  What is the enclosing environment of *myfun()*?

The following code helps explain things, but it's a bit confusing because
`environment()` gives back different results depending on whether it is
given a function as its argument. If given a function, it returns the
enclosing environment for that function. If given no argument, it
returns the current execution environment.

```r
environment(myfun)  # enclosing environment of h()
ls(environment(myfun)) # objects in that environment
fun_constructor <- function(){
	print(environment()) # execution environment of fun_constructor()
	y <- 10
	g <- function(x) x + y
	return(g)
}
myfun <- fun_constructor()
environment(myfun)
myfun(3)
environment(myfun)$y
## advanced: explain this:
environment(myfun)$g
```

Be careful when using variables from the enclosing environment as the
value of that variable in the enclosing environment may well not be what
you expect it to be. In general it's bad practice to use variables that
are taken from environments outside that of a function, but in some
cases it can be useful. Here are some examples of using variables
outside of the frame of a function.

```r
x <- 3
f <- function() {x <- x^2; print(x)}
f()
x # what do you expect?
f <- function() { assign('x', x^2, env = .GlobalEnv) }
## careful: could be dangerous as a variable is changed as a side effect
f()
x
f <- function(x) { x <<- x^2 }
## careful: could be dangerous as a variable is changed as a side effect
f(5)
x
```

#### Comprehension problem

Here's a case where something I tried failed and I had to think more
carefully about scoping to understand why.

```r
set.seed(1)
rnorm(1)
save(.Random.seed, file = 'tmp.Rda')
rnorm(1)
tmp <- function() {
  load('tmp.Rda')
  print(rnorm(1))
}
tmp()
```

Question: what was I hoping that code to do, and why didn't it work?

#### Detecting non-local variables {#detecting-non-local-variables .unnumbered}

We can use `codetools::findGlobals()` to detect non-local variables when
we are programming.

```r
f <- function() {
    y <- 3
    print(x + y)
}
codetools::findGlobals(f)
```

Is that result what you would expect? What does it say about my
statement that using non-local variables is a bad idea?

### Closures

One way to avoid passing data by value is to associate data with a
function, using a *closure*. This is a functional programming way to
achieve something like an OOP class. This [Wikipedia
entry](https://en.wikipedia.org/wiki/Closure_(computer_programming))
nicely summarizes the idea, which is a general functional programming idea and not specific to R.

Using a closure
involves creating one (or more functions) within a function call and
returning the function(s) as the output. When one executes the original
function, the new function(s) is created and returned and one can then
call that new function(s). The new function then can access objects in
the enclosing environment (the environment of the original function) and
can use `<<-` to assign into the enclosing environment, to which the
function (or the multiple functions) have access. The nice thing about
this compared to using a global variable is that the data in the closure
is bound up with the function(s) and is protected from being changed by
the user of the closure. Chambers provides an example of this in Sec.
5.4.

```r
x <- rnorm(10)
scaler_constructor <- function(input){
	data <- input
	g <- function(param) return(param * data)
	return(g)
}
scaler <- scaler_constructor(x)
rm(x) # to demonstrate we no longer need x
scaler(3)
```

So calling `scaler(3)` multiplies 3 by the value of `data` stored in the closure (the enclosing environment) of the function `scaler`.

It turns out that it can be hard to see the memory used involved in the closure.

```r
x <- rnorm(1e7)
scaler <- scaler_constructor(x)
object.size(scaler) # hmmm
object.size(environment(scaler)$data)

library(pryr)
object_size(scaler) # that's better!
```

Here's a fun example. You might do this with an *apply* variant, in
particular *replicate*, but this is slick:

```r
make_container <- function(n) {
	x <- numeric(n)
	i <- 1

	function(value = NULL) {
		if (is.null(value)) {
			return(x)
		} else {
			x[i] <<- value
			i <<- i + 1
		}
	}
}
nboot <- 100
bootmeans <- make_container(nboot)
data <- faithful[ , 1] # Old Faithful geyser eruption lengths
for (i in 1:nboot)
	bootmeans(mean(sample(data, length(data),
      replace=TRUE)))
bootmeans()
```


The closure stores the bootstrapped values and

### Environments and the search path

So far we've seen lexical scoping in action primarily in terms of
finding variables in a single enclosing environment. But what if the
variable is not found in either the frame/environment of the function or
the enclosing environment? When R goes looking for an object (in the
form of a symbol), it starts in the current environment (e.g., the
frame/environment of a function) and then runs up through the enclosing
environments, until it reaches the global environment, which is where R
starts when you open R.

Then, if R can't find the object when reaching the global environment, it runs
through the search path, which you can see with `search()`. The search
path is a set of additional environments, mainly the namespaces of packages loaded in the R session.


```r
search()
```

We can see the full set of environments in which R looks using code such as the following.
This illustrates that in looking for a local variable
used in *lm* the search process would go through the stats namespace, the base R namespace,
the global environment and then the various packages loaded in the current R session.


```r
x <- environment(lm)
while (environmentName(x) != environmentName(emptyenv())) {
	print(environmentName(x))
	x <- parent.env(x) # enclosing env't, NOT parent frame!
}
```

That code uses `environmentName()`, which prints out a nice-looking version of
the environment name.


Here's an alternative way using *pryr*:

```r
library(pryr)
x <- environment(lm)
parenvs(x, all = TRUE)
```

Note that eventually the global environment and the environments of the
packages are nested within the base environment (of the base package)
and the empty environment.

---

[← lapply: one line, easy to understand](15-lapply-one-line-easy-to-understand.md) · [Up: contents](index.md) · [8. Memory and copies →](17-8-memory-and-copies.md)
