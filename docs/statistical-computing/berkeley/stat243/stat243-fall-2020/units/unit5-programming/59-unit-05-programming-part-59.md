---
title: Unit 05 — programming Part 59 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 59 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Recall that to access symbols that involve special syntax (such as special characters), you use backquotes.

Officially, the name that you assign to an object (including functions) is a _symbol_ .

x <- 3; **typeof** ( **quote** (x)) ## [1] "symbol"

We can create an _expression_ object that contains R code as

myExpr <- **expression** (x <- 3) **eval** (myExpr) **typeof** (myExpr) ## [1] "expression"

The difference between _quote()_ and _expression()_ is basically that _quote()_ works with a single statement (including multiple statements inside {...}), while _expression()_ can deal with multiple statements, returning a list-like object of parsed statements. Both of them parse R code.

103

a <- **quote** (x <- 5) b <- **expression** (x <- 5, y <- 3) d <- **quote** ({x <- 5; y <- 3}) **class** (a) ## [1] "<-" **class** (b) ## [1] "expression" b[[1]] ## x <- 5 **class** (b[[1]]) ## [1] "<-" **identical** (a, b[[1]]) ## [1] TRUE **identical** (d[[2]], b[[1]]) ## [1] TRUE

The following table shows the _language_ objects in R; note that there are three classes of language objects: _expressions_ <u>,</u> _calls_ <u>, and</u> _names_ .

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

104

Objects of type language are not officially lists, but they can be queried as such. You can convert between language objects and lists with _as.list()_ and _as.call()_ .

An official expression is one or more syntactically correct R statements. When we use _quote()_ , we’re working with a single statement, while _expression()_ will create a list of separate statements (essentially separate call objects). I’m trying to use the term _statement_ to refer colloquially to R code, rather than using the term _expression_ , since that has formal definition in this context.

Let’s take a look at some examples of language objects and parsing.

e0 <- **quote** (3) e1 <- **expression** (x <- 3) e1m <- **expression** ({x <- 3; y <- 5}) e2 <- **quote** (x <- 3) e3 <- **quote** ( **rnorm** (3)) **print** ( **c** ( **class** (e0), **typeof** (e0))) ## [1] "numeric" "double" **print** ( **c** ( **class** (e1), **typeof** (e1))) ## [1] "expression" "expression" **print** ( **c** ( **class** (e1[[1]]), **typeof** (e1[[1]]))) ## [1] "<-" "language" **print** ( **c** ( **class** (e1m), **typeof** (e1m))) ## [1] "expression" "expression" **print** ( **c** ( **class** (e2), **typeof** (e2))) ## [1] "<-" "language" **identical** (e1[[1]], e2) ## [1] TRUE **print** ( **c** ( **class** (e3), **typeof** (e3))) ## [1] "call" "language"

105

e4 <- **quote** (-7) **print** ( **c** ( **class** (e4), **typeof** (e4))) _# huh? what does this imply?_ ## [1] "call" "language" **as.list** (e4) ## [[1]] ## `-` ## ## [[2]] ## [1] 7

We can evaluate language types using _eval()_ :

**rm** (x) **eval** (e1) **rm** (x) **eval** (e2) e1mlist <- **as.list** (e1m) e2list <- **as.list** (e2) **eval** ( **as.call** (e2list)) _## here's how to do it if the language object is actually an expression_ **eval** ( **as.expression** (e1mlist))

Now let’s look in more detail at the components of R expressions. We’ll be able to get a sense from this of how R evaluates code. We see that when R evaluates a parse tree, the first element says what function to use and the remaining elements are the arguments. But in many cases one or more arguments will themselves be call objects, so there’s recursion.

e1 <- **expression** (x <- 3) _## e1 is one-element list with the element an object of class '<-'_ **print** ( **c** ( **class** (e1), **typeof** (e1))) ## [1] "expression" "expression" e1[[1]] ## x <- 3

106

**as.list** (e1[[1]]) ## [[1]] ## `<-` ## ## [[2]] ## x ## ## [[3]] ## [1] 3 **lapply** (e1[[1]], class) ## [[1]] ## [1] "name" ## ## [[2]] ## [1] "name" ## ## [[3]] ## [1] "numeric" y <- **rnorm** (5) e3 <- **quote** ( **mean** (y)) **print** ( **c** ( **class** (e3), **typeof** (e3))) ## [1] "call" "language" e3[[1]] ## mean **print** ( **c** ( **class** (e3[[1]]), **typeof** (e3[[1]]))) ## [1] "name" "symbol" e3[[2]] ## y

107

**print** ( **c** ( **class** (e3[[2]]), **typeof** (e3[[2]]))) ## [1] "name" "symbol" _## we have recursion_ e3 <- **quote** ( **mean** ( **c** (12,13,15) + **rnorm** (3))) **as.list** (e3) ## [[1]] ## mean ## ## [[2]] ## c(12, 13, 15) + rnorm(3) **as.list** (e3[[2]]) ## [[1]] ## `+` ## ## [[2]] ## c(12, 13, 15) ## ## [[3]] ## rnorm(3) **as.list** (e3[[2]][[3]]) ## [[1]] ## rnorm ## ## [[2]] ## [1] 3 **library** (pryr) **call_tree** (e3) ## \- () ## \- `mean ## \- ()

108

---

[← 9 Computing on the language (optional)](58-9-computing-on-the-language-optional.md) · [Up: contents](index.md) · [\- + ## \- () ## \- c ## \- 12 ## \- 13 ## \- 15 ## \- () ## \- rnorm ## \- 3 →](60-------c---12---13---15-----rnorm---3.md)
