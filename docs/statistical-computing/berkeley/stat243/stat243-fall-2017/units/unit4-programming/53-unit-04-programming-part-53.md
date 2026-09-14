---
title: Unit 04 — programming Part 53 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 53 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **9.3 Manipulating the parse tree**

Of course since the parsed code is just an object, we can manipulate it, i.e., _compute on the language_ :

out <- **quote** (y <- 3) out[[3]] <- 4 **eval** (out) y ## [1] 4

Here’s another example:

95

e1 <- **quote** (4 + 5) e2 <- **quote** ( **plot** (x, y)) e2[[1]] <- `+` **eval** (e2) ## [1] 7 e1[[3]] <- e2 e1 ## 4 + .Primitive("+")(x, y) **class** (e1[[3]]) _# note the nesting_ ## [1] "call" **eval** (e1) _# what should I get?_ ## [1] 11

We can also turn it back into standard R code, as a character, using _deparse()_ , which turns the parse tree back into R code as text. _parse()_ is like _quote()_ but it takes the code in the form of a string rather than an actual expression:

codeText <- **deparse** (out) parsedCode <- **parse** (text = codeText) _## parse() works like quote() except on the code in the form of a string_ **eval** (parsedCode) **deparse** ( **quote** ( **if** (x > 1) "orange" **else** "apple")) ## [1] "if (x > 1) \"orange\" else \"apple\""

Note that the quotes have been escaped since they’re inside a string.

It can be very useful to be able to convert names of objects that are in the form of text to names that R interprets as symbols referring to objects:

x3 <- 7 i <- 3 **as.name** ( **paste** ('x', i, sep=''))

96

---

[← function (x, y) .Primitive("%%")](52-function-x-y-primitive.md) · [Up: contents](index.md) · [Unit 04 — programming Part 54 — →](54-unit-04-programming-part-54.md)
