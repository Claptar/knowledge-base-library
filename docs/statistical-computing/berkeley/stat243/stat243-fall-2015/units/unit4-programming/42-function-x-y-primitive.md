---
title: function (x, y) .Primitive("%%")
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# function (x, y) .Primitive("%%")

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **9.2 Parsing code and understanding language objects**

R code can be manipulated in text form and we can actually write R code that will create or manipulate R code. We can then evaluate that R code using _eval()_ .

83

_quote()_ will parse R code, but not evaluate it. This allows you to work with the code rather than the results of evaluating that code. The _print()_ method for language objects is not very helpful! But we can see the parsed code by treating the result as a list.

obj <- **quote** ( **if** (x > 1) "orange" **else** "apple") **as.list** (obj) ## [[1]] ## `if` ## ## [[2]] ## x > 1 ## ## [[3]] ## [1] "orange" ## ## [[4]] ## [1] "apple" **class** (obj) ## [1] "if" weirdObj <- **quote** ( **`if`** (x > 1, 'orange', 'apple')) **identical** (obj, weirdObj) ## [1] TRUE

Recall that to access symbols that involve special syntax (such as special characters), you use backquotes.

Officially, the name that you assign to an object (including functions) is a _symbol_ .

x <- 3; **typeof** ( **quote** (x)) ## [1] "symbol"

We can create an _expression_ object that contains R code as

84

myExpr <- **expression** (x <- 3) **eval** (myExpr) **typeof** (myExpr) ## [1] "expression"

The difference between _quote()_ and _expression()_ is basically that _quote()_ works with a single statement (including multiple statements inside {...}), while _expression()_ can deal with multiple statements, returning a list-like object of parsed statements. Both of them parse R code.

a <- **quote** (x <- 5) b <- **expression** (x <- 5, y <- 3) d <- **quote** ({x <- 5; y <- 3}) **class** (a) ## [1] "<-" **class** (b) ## [1] "expression" b[[1]] ## x <- 5 **class** (b[[1]]) ## [1] "<-" **identical** (a, b[[1]]) ## [1] TRUE **identical** (d[[2]], b[[1]]) ## [1] TRUE

The following table shows the _language_ objects in R; note that there are three classes of language objects: _expressions_ , _calls_ , and _names_ .

85

||Example syntax to create|Class|Type|
|---|---|---|---|
|object names|quote(x)|name|symbol (language)|
|expressions|expression(x <- 3)|expression|expression (language)|
|function calls|quote(f())|call|language|
|if statements|quote(if(x < 3)y=5)|if (call)|language|
|for statement|quote(for(i in 1:5) {})|for (call)|language|
|assignments|quote(x <- 3)|<- (call)|language|
|operators|quote(3 + 7)|call|language|


Basically any standard function, operator, _if_ statement, _for_ statement, assignment, etc. are function calls and inherit from the _call_ class.

Objects of type language are not officially lists, but they can be queried as such. You can convert between language objects and lists with _as.list()_ and _as.call()_ .

An official expression is one or more syntactically correct R statements. When we use _quote()_ , we’re working with a single statement, while _expression()_ will create a list of separate statements (essentially separate call objects). I’m trying to use the term _statement_ to refer colloquially to R code, rather than using the term _expression_ , since that has formal definition in this context.

Let’s take a look at some examples of language objects and parsing.

e0 <- **quote** (3) e1 <- **expression** (x <- 3) e1m <- **expression** ({x <- 3; y <- 5}) e2 <- **quote** (x <- 3) e3 <- **quote** ( **rnorm** (3)) **print** ( **c** ( **class** (e0), **typeof** (e0))) ## [1] "numeric" "double" **print** ( **c** ( **class** (e1), **typeof** (e1))) ## [1] "expression" "expression" **print** ( **c** ( **class** (e1[[1]]), **typeof** (e1[[1]]))) ## [1] "<-" "language" **print** ( **c** ( **class** (e1m), **typeof** (e1m))) ## [1] "expression" "expression"

86

**print** ( **c** ( **class** (e2), **typeof** (e2))) ## [1] "<-" "language" **identical** (e1[[1]], e2) ## [1] TRUE **print** ( **c** ( **class** (e3), **typeof** (e3))) ## [1] "call" "language" e4 <- **quote** (-7) **print** ( **c** ( **class** (e4), **typeof** (e4))) _# huh? what does this imply?_ ## [1] "call" "language" **as.list** (e4) ## [[1]] ## `-` ## ## [[2]] ## [1] 7

We can evaluate language types using _eval()_ :

**rm** (x) **eval** (e1) **rm** (x) **eval** (e2) e1mlist <- **as.list** (e1m) e2list <- **as.list** (e2) **eval** ( **as.call** (e2list)) _# here's how to do it if the language object is actually an expression (multiple_ **eval** ( **as.expression** (e1mlist))

Now let’s look in more detail at the components of R expressions. We’ll be able to get a sense from this of how R evaluates code. We see that when R evaluates a parse tree, the first element

87

says what function to use and the remaining elements are the arguments. But in many cases one or more arguments will themselves be call objects, so there’s recursion.

e1 <- **expression** (x <- 3) _# e1 is one-element list with the element an object of class '<-'_ **print** ( **c** ( **class** (e1), **typeof** (e1))) ## [1] "expression" "expression" e1[[1]] ## x <- 3 **as.list** (e1[[1]]) ## [[1]] ## `<-` ## ## [[2]] ## x ## ## [[3]] ## [1] 3 **lapply** (e1[[1]], class) ## [[1]] ## [1] "name" ## ## [[2]] ## [1] "name" ## ## [[3]] ## [1] "numeric" y <- **rnorm** (5) e3 <- **quote** ( **mean** (y)) **print** ( **c** ( **class** (e3), **typeof** (e3))) ## [1] "call" "language"

88

e3[[1]] ## mean **print** ( **c** ( **class** (e3[[1]]), **typeof** (e3[[1]]))) ## [1] "name" "symbol" e3[[2]] ## y **print** ( **c** ( **class** (e3[[2]]), **typeof** (e3[[2]]))) ## [1] "name" "symbol" _# we have recursion_ e3 <- **quote** ( **mean** ( **c** (12,13,15) + **rnorm** (3))) **as.list** (e3) ## [[1]] ## mean ## ## [[2]] ## c(12, 13, 15) + rnorm(3) **as.list** (e3[[2]]) ## [[1]] ## `+` ## ## [[2]] ## c(12, 13, 15) ## ## [[3]] ## rnorm(3) **as.list** (e3[[2]][[3]])

89

---

[← Unit 04 — programming Part 41 —](41-unit-04-programming-part-41.md) · [Up: contents](index.md) · [Unit 04 — programming Part 43 — →](43-unit-04-programming-part-43.md)
