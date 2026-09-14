---
title: Unit 06 — Rprog Part 28 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — Rprog Part 28 —

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

59

### **6.3 Manipulating the parse tree**

Of course since the parsed code is just an object, we can manipulate it, i.e., _compute on the language_ :

out <- **quote** (y <- 3) out[[3]] <- 4 **eval** (out) y ## [1] 4

Here’s another example:

e1 <- **quote** (4 + 5) e2 <- **quote** ( **plot** (x, y)) e2[[1]] <- `+` **eval** (e2) ## [1] 7 e1[[3]] <- e2 e1 ## 4 + .Primitive("+")(x, y) **class** (e1[[3]]) _# note the nesting_ ## [1] "call" **eval** (e1) _# what should I get?_ ## [1] 11

We can also turn it back into standard R code, as a character, using _deparse()_ , which turns the parse tree back into R code as text. _parse()_ is like _quote()_ but it takes the code in the form of a string rather than an actual expression:

60

codeText <- **deparse** (out) parsedCode <- **parse** (text = codeText) _# parse() works like quote() except on the code in the form of a string_ **eval** (parsedCode) **deparse** ( **quote** ( **if** (x > 1) "orange" **else** "apple")) ## [1] "if (x > 1) \"orange\" else \"apple\""

Note that the quotes have been escaped since they’re inside a string.

It can be very useful to be able to convert names of objects that are in the form of text to names that R interprets as symbols referring to objects:

x3 <- 7 i <- 3 **as.name** ( **paste** ("x", i, sep = "")) ## x3 **eval** ( **as.name** ( **paste** ("x", i, sep = ""))) ## [1] 7 **assign** ( **paste** ("x", i, sep = ""), 11) x3 ## [1] 11

### **6.4 Parsing replacement expressions**

Let’s consider replacement expressions.

animals = **c** ("cat", "dog", "rat", "mouse") out1 = **quote** (animals[4] <- "rat") out2 = **quote** (animals[4] <- "rat") out3 = **quote** ( **`[<-`** (animals, 4, "rat")) **as.list** (out1) ## [[1]]

61

---

[← Unit 06 — Rprog Part 27 —](27-unit-06-rprog-part-27.md) · [Up: contents](index.md) · [Unit 06 — Rprog Part 29 — →](29-unit-06-rprog-part-29.md)
