---
title: 7. Functional programming
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 7. Functional programming

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Overview of functional programming

Functional programming is an approach to programming that emphasizes the use of modular, self-contained functions.
Such functions should operate only on arguments provided to
them (avoiding global variables), and **produce no side effects**, although in some cases there are good
reasons for making an exception. Another aspect of functional programming is
that functions are considered 'first-class' citizens in that they can be passed as arguments to another function,
returned as the result of a function, and assigned to variables. In other words, a function can be treated as any other variable.

In many cases (including R and Python), anonymous functions (also called 'lambda functions') can be created on-the-fly for use in various circumstances.

## Functional programming in R

R is a language that has strong functional programming aspects to it, including:

  - All operations are carried out by functions.
  - Functions are first class citizens.
  - Functions (generally) do not have side effects.
  - *Map* operations (e.g., *lapply*) are central to programming in R.

Functions that are not implemented internally in R  are also referred to officially as *closures* (this is their
*type*) - this terminology sometimes comes up in error messages.

```r
typeof(mean)
typeof(lm)
typeof(length)
```


### No side effects

Most functions available in R (and ideally functions that you write as well) operate by taking in arguments and producing output that is then (presumably) used subsequently. The functions generally don't have any effect on the state of your R environment/session other than the output they produce.

An important reason for this (plus for not using global variables) is that it means that it is easy for people using the language to understand what code does. Every function can be treated a black box -- you don't need to understand what happens in the function or worry that the function might do something unexpected (such as changing the value of one of your variables). The result of running code is simply the result of a composition of functions, as in mathematical function composition.

One aspect of this is that R uses a *pass-by-value* approach to function arguments (as opposed to a *pass-by-reference* approach). We'll talk about function arguments and when copies are made  in much more detail later, but briefly, when you pass an object in as an argument and then modify it in the function, you are modifying a local copy of the variable that exists in the context (the *frame*) of the function and is deleted when the function call finishes:

```r
x <- 1:3
myfun <- function(x) {
      x[2] <- 7
      print(x)
      return(x)
}

new_x <- myfun(x)
x   # unmodified
```

In contrast, let's see what happens in Python

```python
x = [1,2,3]
def myfun(x):
  x[1] = 7
  print(x)
  return(x)

new_x = myfun(x)
x   # modified!
```

There are some (necessary) exceptions to the idea of no side effects in R.
An important exception is *par()*. If you change graphics parameters by
calling *par()* in a user-defined function, they are changed permanently
outside of the function. One trick is as follows:

```r
f <- function(){
  oldpar <- par()
  par(cex = 2)

  # body of code

  par() <- oldpar
}
```
Note that changing graphics parameters within a specific plotting
function - e.g., `plot(x, y, pch = '+')`, doesn't change things except
for that particular plot.

> **Challenge**
> What are some other functions that are called for the purpose of the side effects they produce? (For example, which functions change the state of your R session in some way?

### Functions are first-class objects

Everything in R is an object, including functions. We can assign
functions to variables in the same way we assign numeric and other
values.

```r
x <- 3
class(x); typeof(x)

try(x(2))    # x is not a function (yet)
x <- function(z) z^2  # now it is a function
x(2)
class(x); typeof(x)
```

We can call a function based on the text name of the function.

```r
myFun <- 'mean'; x <- rnorm(10)
eval(as.name(myFun))(x)
```

We can also pass a function into another function as the actual function
object. This is an important aspect of R being a functional programming language.

```r
x <- rnorm(10)
sapply(x, abs)

f <- function(fxn, x) {
    fxn(x)
}
f(mean, x)
```

We can also pass in a function based on a a character vector of length
one with the name of the function. Here *match.fun()* is a handy
function that extracts a function when the function is passed in as an
argument of a function. It looks in the calling environment for the
function and can handle when the function is passed in as a function
object or as a character vector of length 1 giving the function name.


```r
f <- function(fxn, x){
  match.fun(fxn)(x)
}
f("mean", x)
f(mean, x)
```


Function objects contain three components: an argument list, a body (a
parsed R statement), and an environment.

```r
f1 <- function(x) y <- x^2
f2 <- function(x) {
    y <- x^2
    z <- x^3
    return(list(y, z))
}
class(f1)
body(f2)
typeof(body(f1)); class(body(f1))
typeof(body(f2)); class(body(f2))
```

We'll see more about objects relating to the R language and parsed code
in the final section of this Unit. For now, just realize that the parsed
code itself is treated as an object(s) with certain types and certain
classes.


The *do.call* function is another example of a function that takes a function as an argument.
It will apply a function to the elements of a
list. For example, we can `rbind()` together (if compatible) the
elements of a list of vectors instead of having to loop over the
elements or manually type them in:

```r
myList <- list(a = 1:3, b = 11:13, c = 21:23)
args(rbind)
rbind(myList$a, myList$b, myList$c)
rbind(myList)
do.call(rbind, myList)
```

Why couldn't we just use *rbind* directly? Basically we're using
`do.call()` to use functions that take `...` as input (i.e., functions
accepting an arbitrary number of arguments) and to use the list as the
input instead (i.e., to use the list elements).

More generally *do.call* is a way to pass arguments to a function when
the arguments you want to pass are part of a list.

```r
do.call(mean, list(1:10, na.rm = TRUE))
```


### All operations are functions

All operations in R are actually function calls, even things that don't look like function calls,
including various operators (such as addition,
subtraction, etc.), printing to the screen, etc.

#### Operators

Operators, such as `+` and `[` are just functions, but their arguments
can occur both before and after the function call:

```r
a <- 7; b <- 3

---

[← suppress package-loading messages by loading here](10-suppress-package-loading-messages-by-loading-here.md) · [Up: contents](index.md) · [let's think about the following as a mathematical function →](12-let-s-think-about-the-following-as-a-mathematical-function.md)
