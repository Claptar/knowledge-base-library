---
title: 10. Computing on the language (optional)
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 10. Computing on the language (optional)

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

We won't cover this section, and I won't expect you to
know this material, but some of you may find it interesting. Also, when
I talked about R being a particularly flexible language in explaining in
part why R can be slow, much of that flexibility is illustrated here.

## The R interpreter

### Parsing

When you run R, the R interpreter takes the code you type or the lines
of code that are read in a batch session and parses each statement,
translating the text into functional form. It substitutes objects for
the symbols (names) that represent those objects and evaluates the
statement, returning the resulting object. For complicated R code, this
may be recursive.

Since everything in R is an object, the result of parsing is an object
that we'll be able to investigate, and the result of evaluating the
parsed statement is an object.

We'll see more on parsing in the next section.

### `.Primitive()` and `.Internal()` (and `.External()`)

Some functionality is implemented internally within the C implementation
that lies at the heart of R. If you see `.Internal()` or `.Primitive()`
or `.External()`, in the code of a function, you know it's implemented
internally (and therefore generally very quickly). Unfortunately, it
also means that you don't get to see R code that implements the
functionality, though Chambers p. 465 describes how you can look into
the C source code. Basically you need to download the source code for
the relevant package off of CRAN.

```r
plot.xy # plot.xy() is called by plot.default()
print(`%*%`)
```

## Parsing code and understanding language objects

R code can be manipulated in text form and we can actually write R code
that will create or manipulate R code. We can then evaluate that R code
using `eval()`.

`quote()` will parse R code, but not evaluate it. This allows you to
work with the code rather than the results of evaluating that code. The
`print()` method for language objects is not very helpful! But we can
see the parsed code by treating the result as a list.

```r
obj <- quote(if (x > 1) "orange" else "apple")
as.list(obj)
class(obj)
weirdObj <- quote(`if`(x > 1, 'orange', 'apple'))
identical(obj, weirdObj)
```

Recall that to access symbols that involve special syntax (such as
special characters), you use backquotes.

Officially, the name that you assign to an object (including functions)
is a *symbol*.

```r
x <- 3; typeof(quote(x))
```

We can create an *expression* object that contains R code as

```r
myExpr <- expression(x <- 3)
eval(myExpr)
typeof(myExpr)
```

The difference between `quote()` and `expression()` is basically that
`quote()` works with a single statement (including multiple statements
inside {\...}), while `expression()` can deal with multiple statements,
returning a list-like object of parsed statements. Both of them parse R
code.

```r
a <- quote(x <- 5)
b <- expression(x <- 5, y <- 3)
d <- quote({x <- 5; y <- 3})
class(a)
class(b)
b[[1]]
class(b[[1]])
identical(a, b[[1]])
identical(d[[2]], b[[1]])
```

The following table shows the *language* objects in R; note that there
are three classes of language objects: *expressions*, *calls*, and
*names*.

|                 |   Example syntax to create  |   Class     |         Type |
| ----------------| --------------------------| ------------| -----------------------|
|    object names  |          `quote(x)`      |        name    |    symbol (language)|
|    expressions  |     `expression(x <- 3)`   |   expression |  expression (language)|
|   function calls  |        `quote(f())`      |       call     |       language|
|   if statements  |   `quote(if(x < 3) y=5)` |    if (call)    |      language|
|   for statement |   `quote(for(i in 1:5) {})`  |  for (call)  |       language|
|    assignments   |       `quote(x <- 3)`    |    \<- (call)   |      language|
|     operators     |       `quote(3 + 7)`     |       call      |      language|

\
Basically any standard function, operator, `if` statement, `for`
statement, assignment, etc. are function calls and inherit from the
`call` class.

Objects of type language are not officially lists, but they can be
queried as such. You can convert between language objects and lists with
`as.list()` and `as.call()`.

An official expression is one or more syntactically correct R
statements. When we use `quote()`, we're working with a single
statement, while `expression()` will create a list of separate
statements (essentially separate call objects). I'm trying to use the
term *statement* to refer colloquially to R code, rather than using the
term *expression*, since that has formal definition in this context.

Let's take a look at some examples of language objects and parsing.

```r
e0 <- quote(3)
e1 <- expression(x <- 3)
e1m <- expression({x <- 3; y <- 5})
e2 <- quote(x <- 3)
e3 <- quote(rnorm(3))
print(c(class(e0), typeof(e0)))
print(c(class(e1), typeof(e1)))
print(c(class(e1[[1]]), typeof(e1[[1]])))
print(c(class(e1m), typeof(e1m)))
print(c(class(e2), typeof(e2)))
identical(e1[[1]], e2)
print(c(class(e3), typeof(e3)))
e4 <- quote(-7)
print(c(class(e4), typeof(e4))) # huh? what does this imply?
as.list(e4)
```

We can evaluate language types using `eval()`:

```r
rm(x)
eval(e1)
rm(x)
eval(e2)
e1mlist <- as.list(e1m)
e2list <- as.list(e2)
eval(as.call(e2list))
## here's how to do it if the language object is actually an expression (multiple statements)
eval(as.expression(e1mlist))
```

Now let's look in more detail at the components of R expressions. We'll
be able to get a sense from this of how R evaluates code. We see that
when R evaluates a parse tree, the first element says what function to
use and the remaining elements are the arguments. But in many cases one
or more arguments will themselves be call objects, so there's recursion.

```r
e1 <- expression(x <- 3)
## e1 is one-element list with the element an object of class '<-'
print(c(class(e1), typeof(e1)))
e1[[1]]
as.list(e1[[1]])
lapply(e1[[1]], class)
y <- rnorm(5)
e3 <- quote(mean(y))
print(c(class(e3), typeof(e3)))
e3[[1]]
print(c(class(e3[[1]]), typeof(e3[[1]])))
e3[[2]]
print(c(class(e3[[2]]), typeof(e3[[2]])))
## we have recursion
e3 <- quote(mean(c(12,13,15) + rnorm(3)))
as.list(e3)
as.list(e3[[2]])
as.list(e3[[2]][[3]])
library(pryr)
call_tree(e3)
```

## Manipulating the parse tree

Of course since the parsed code is just an object, we can manipulate it,
i.e., *compute on the language*:

```r
out <- quote(y <- 3)
out[[3]] <- 4
eval(out)
y
```

Here's another example:

```r
e1 <- quote(4 + 5)
e2 <- quote(plot(x, y))
e2[[1]] <- `+`
eval(e2)
e1[[3]] <- e2
e1
class(e1[[3]]) # note the nesting
eval(e1) # what should I get?
```

We can also turn it back into standard R code, as a character, using
`deparse()`, which turns the parse tree back into R code as text.
`parse()` is like `quote()` but it takes the code in the form of a
string rather than an actual expression:

```r
codeText <- deparse(out)
parsedCode <- parse(text = codeText)
## parse() works like quote() except on the code in the form of a string
eval(parsedCode)
deparse(quote(if (x > 1) "orange" else "apple"))
```

Note that the quotes have been escaped since they're inside a string.

It can be very useful to be able to convert names of objects that are in
the form of text to names that R interprets as symbols referring to
objects:

```r
x3 <- 7
i <- 3
as.name(paste('x', i, sep=''))
eval(as.name(paste('x', i, sep='')))
assign(paste('x', i, sep = ''), 11)
x3
```

## Parsing replacement expressions

Let's consider replacement expressions.

```r
animals <- c('cat', 'dog', 'rat','mouse')
out1 <- quote(animals[4] <- 'rat')
out2 <- quote(`<-`(animals[4], 'rat'))
out3 <- quote('[<-'(animals,4,'rat'))
as.list(out1)
as.list(out2)
identical(out1, out2)
as.list(out3)
identical(out1, out3)
typeof(out1[[2]]) # language
class(out1[[2]]) # call
```

The parse tree for `out3` is different than those for `out1` and `out2`,
but when `out3` is evaluated the result is the same as for `out1` and
`out2`:

```r
eval(out1)
animals
animals[4] <- 'mouse'  # reset things to original state
eval(out3)
animals # both do the same thing
```

Why? When R evaluates a call to '\<-', if the first argument is a name,
then it does the assignment, but if the first argument (i.e. what's on
the left-hand side of the "assignment") is a call then it calls the
appropriate replacement function. The second argument (the value being
assigned) is evaluated first. Ultimately in all of these cases, the
replacement function is used.

## substitute()

The substitute function acts like `quote()`:

```r
identical(quote(z <- x^2), substitute(z <- x^2))
```

But if you also pass `substitute()` an environment, it will replace
symbols with their object values in that environment.

```r
e <- new.env(); e$x <- 3
substitute(z <- x^2, e)
```

This can do non-sensical stuff:

```r
e$z <- 5
substitute(z <- x^2, e)
```

Let's see a practical example of substituting for variables in
statements:

```r
plot(x = rnorm(5), y = rgamma(5, 1))
```

How does `plot()` get the axis label names?
In the `plot()` function, you can see this syntax:

```r
xlabel <- if(!missing(x)) deparse(substitute(x))
```

So what's going on is that within `plot.default()`, it substitutes in
for '`x`' with the statement that was passed in as the `x` argument, and
then uses `deparse()` to convert to character. The fact that `x` still
has `rnorm(5)` associated with it rather than the five numerical values
from evaluating `rnorm()` has to do with lazy evaluation and promises.
Here's the same idea in action in a stripped down example:

```r
f <- function(obj){
objName <- deparse(substitute(obj))
print(objName)
}
f(y)
```

More generally, we can substitute into *expression* and *call* objects
by providing a named list (or an environment) - the substition happens
within the context of this list.

```r
substitute(a + b, list(a = 1, b = quote(x)))
```

Things can get intricate quickly:

```r
e1 <- quote(x + y)
e2 <- substitute(e1, list(x = 3))
```

The problem is that `substitute()` doesn't evaluate its first argument,
`e1`, so it can't replace the parsed elements in `e1`. Instead, we'd
need to do the following, where we force the evaluation of `e1`:

```r
e2 <- substitute(substitute(e, list(x = 3)), list(e = e1))
substitute(substitute(e, list(x = 3)), list(e = e1))
## so e1 is substituted as an evaluated object,
## which then allows for substitution for 'x'
e2
eval(e2)
substitute_q(e1, list(x = 3))  # from pryr
```

If this subsection is confusing, let me assure you that it has confused
me too. The indirection going on here is very involved.

## Final thoughts

**Challenge**: figure out how a `for` loop is parsed in R. See how a
`for` loop with one statement within the loop differs from one with two
or more statements.

We'll see `expression()` again when we talk about inserting mathematical
notation in plots.

---

[← part of an iterative optimization to find a maximum likelihood estimator](22-part-of-an-iterative-optimization-to-find-a-maximum-likeliho.md) · [Up: contents](index.md)
