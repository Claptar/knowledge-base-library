---
title: Unit 04 — programming Part 51 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 51 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

92

**print** (`%*%`) ## function (x, y) .Primitive("%*%")

### **9.2 Parsing code and understanding language objects**

R code can be manipulated in text form and we can actually write R code that will create or manipulate R code. We can then evaluate that R code using _eval()_ .

_quote()_ will parse R code, but not evaluate it. This allows you to work with the code rather than the results of evaluating that code. The _print()_ method for language objects is not very helpful! But we can see the parsed code by treating the result as a list.

obj <- **quote** ( **if** (x > 1) "orange" **else** "apple") **as.list** (obj) ## [[1]] ## `if` ## ## [[2]] ## x > 1 ## ## [[3]] ## [1] "orange" ## ## [[4]] ## [1] "apple" **class** (obj) ## [1] "if" weirdObj <- **quote** ( **`if`** (x > 1, 'orange', 'apple')) **identical** (obj, weirdObj) ## [1] TRUE

Recall that to access symbols that involve special syntax (such as special characters), you use backquotes.

93

Officially, the name that you assign to an object (including functions) is a _symbol_ .

x <- 3; **typeof** ( **quote** (x)) ## [1] "symbol"

We can create an _expression_ object that contains R code as

myExpr <- **expression** (x <- 3) **eval** (myExpr) **typeof** (myExpr) ## [1] "expression"

The difference between _quote()_ and _expression()_ is basically that _quote()_ works with a single statement (including multiple statements inside {...}), while _expression()_ can deal with multiple statements, returning a list-like object of parsed statements. Both of them parse R code.

a <- **quote** (x <- 5) b <- **expression** (x <- 5, y <- 3) d <- **quote** ({x <- 5; y <- 3}) **class** (a) ## [1] "<-" **class** (b) ## [1] "expression" b[[1]] ## x <- 5 **class** (b[[1]]) ## [1] "<-" **identical** (a, b[[1]]) ## [1] TRUE **identical** (d[[2]], b[[1]]) ## [1] TRUE

94

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

Objects of type language are not officially lists, but they can be queried as such. You can convert between language objects and lists with _as.list()_ and _as.call()_ .

An official expression is one or more syntactically correct R statements. When we use _quote()_ , we’re working with a single statement, while _expression()_ will create a list of separate statements (essentially separate call objects). I’m trying to use the term _statement_ to refer colloquially to R code, rather than using the term _expression_ , since that has formal definition in this context.

Let’s take a look at some examples of language objects and parsing.

e0 <- **quote** (3) e1 <- **expression** (x <- 3) e1m <- **expression** ({x <- 3; y <- 5}) e2 <- **quote** (x <- 3) e3 <- **quote** ( **rnorm** (3)) **print** ( **c** ( **class** (e0), **typeof** (e0))) ## [1] "numeric" "double" **print** ( **c** ( **class** (e1), **typeof** (e1))) ## [1] "expression" "expression" **print** ( **c** ( **class** (e1[[1]]), **typeof** (e1[[1]]))) ## [1] "<-" "language"

**print** ( **c** ( **class** (e1m), **typeof** (e1m)))

95

---

[← Unit 04 — programming Part 50 —](50-unit-04-programming-part-50.md) · [Up: contents](index.md) · [Unit 04 — programming Part 52 — →](52-unit-04-programming-part-52.md)
