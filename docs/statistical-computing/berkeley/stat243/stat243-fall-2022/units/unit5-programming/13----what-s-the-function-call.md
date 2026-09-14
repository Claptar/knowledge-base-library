---
title: -- what's the function call?
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# -- what's the function call?

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

a + b
`+`(a, b)
```

In general, you can use back-ticks to refer to the operators as
operators instead of characters. In some cases single or double quotes
also work. We can look at the code of an operator as follows using
back-ticks to escape out of the standard R parsing, e.g.,

```r
`%*%`
```

Finally, since an operator is just a function, you can use it as an
argument in various places:

```r
x <- 1:3; y <- c(100,200,300)
outer(x, y, `+`)

myList <- list(list(state = 'new york', value = 1:5),
               list(state = 'california', value = 6:10),
               list(state = 'delaware', value = 11:15))

## note that the index "2" is the additional argument to the [[ function
result <- lapply(myList, `[[`, 2)
result

myMat <- sapply(myList, `[[`, 2)
myMat
cbind(myList[[1]][[2]], myList[[2]][[2]])  ## equivalent but doesn't scale
```

You can define your own *binary* operator (an operator taking two
arguments) using a string inside *%* symbols. Here's how we could do
Python-style string addition:

```r
`%+%` <- function(a, b) paste0(a, b, collapse = '')
"Hi " %+% "there"
```

Since operators are just functions, there are cases in which there are
optional arguments that we might not expect. Here's how to pass a
sometimes useful argument to the bracket operator (in this case avoiding
conversion from a matrix to a vector, which can mess up subsequent
code).

```r
mat <- matrix(1:4, 2, 2)
mat[ , 1]
mat[ , 1, drop = FALSE] # what's the difference?
```

We can also use operators with our S3 classes. Picking up our example
from our discussion of S3 OOP, the following example will be a bit silly
(it would make more sense with a class that is a mathematical object)
but indicates the power of having methods.

```r
yog <- list(firstname = 'Yogi', surname = 'the Bear', age = 20)
class(yog) <- 'bear'

methods(`+`)
`+.bear` <- function(object, incr) {
	object$age <- object$age + incr
	return(object)
}
older_yog <- yog + 15

older_yog
```

#### Other operations that are functions

Even beyond operators, all code in R can be viewed as a function call, including
if statements and for and while loops.

What do you think is the functional version of the following code? What
are the arguments?

```r
if(x > 27){
	print(x)
} else{
	print("too small")
}
```

#### Replacement functions

Assignments that involve functions or operators on the left-hand side
(LHS) are called *replacement expressions* or *replacement functions.*
These can be quite handy. Here are a few examples:

```r
diag(mat) <- c(3, 2)
is.na(vec) <- 3
names(df) <- c('var1', 'var2')
```

Replacement expressions are actually function calls. The R interpreter
calls the replacement function (which often creates a new object that
includes the replacement) and then assigns the result to the name of the
original object.

```r
mat <- matrix(rnorm(4), 2, 2)
diag(mat) <- c(3, 2)
mat
mat <- `diag<-`(mat, c(10, 21))
mat
base::`diag<-`
```

The old version of *mat* still exists until R's memory management cleans
it up, but it's no longer referred to by the symbol *mat*.
This can cause memory use to increase temporarily (but generally very briefly).
So it's something to keep in mind if you're doing replacements on large objects.

You can define your own replacement functions like this, with the
requirements that the last argument be named `value` and that the
function return the entire object:

```r
yog <- list(firstName = 'Yogi', lastName = 'Bear')

`firstName<-` <- function(obj, value){
  obj$firstName <- value
  return(obj)
}

firstName(yog) <- 'Yogisandra'
```

We can use replacement functions with functional OOP. We need to define the generic
replacement function and then the class-specific one.

```r
`age<-` <- function(x, ...) UseMethod("age<-")

`age<-.bear` <- function(object, value){
	object$age <- value
	return(object)
}
age(older_yog) <- 60

older_yog
```

### Map operations

A *map* operation takes a function and runs the function on each element of some collection of items,
analogous to a mathematical map.
This kind of operation is very commonly used in programming, particularly functional programming,
and often makes for clean, concise, and readable code.

Base R provides a variety of map-type functions: *lapply* and *sapply* and their variants, as well as *apply*.
In addition, the *purrr* package for functional programming provides `purrr::map`.
In R, often the map-type function is run on the elements of a list, but they can also generally be run on elements of a vector and in other ways. In other languages, map-type functions are run on a variety of data structures.
These are  examples of higher-order functions -- functions that take a function as an argument.

Let's compare using *lapply* to using a for loop to run a stratified analysis for a generic example (this code won't run because the variables don't exist):

```r

---

[← let's think about the following as a mathematical function](12-let-s-think-about-the-following-as-a-mathematical-function.md) · [Up: contents](index.md) · [stratification →](14-stratification.md)
