---
title: '[1] "call" eval (e1) # what should I get? ## [1] 11'
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] "call" eval (e1) # what should I get? ## [1] 11

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can also turn it back into standard R code, as a character, using _deparse()_ , which turns the parse tree back into R code as text. _parse()_ is like _quote()_ but it takes the code in the form of a string rather than an actual expression:

codeText <- **deparse** (out) parsedCode <- **parse** (text = codeText) _## parse() works like quote() except on the code in the form of a string_ **eval** (parsedCode) **deparse** ( **quote** ( **if** (x > 1) "orange" **else** "apple")) ## [1] "if (x > 1) \"orange\" else \"apple\""

Note that the quotes have been escaped since they’re inside a string.

It can be very useful to be able to convert names of objects that are in the form of text to names that R interprets as symbols referring to objects:

x3 <- 7 i <- 3 **as.name** ( **paste** ('x', i, sep='')) ## x3 **eval** ( **as.name** ( **paste** ('x', i, sep=''))) ## [1] 7 **assign** ( **paste** ('x', i, sep = ''), 11) x3 ## [1] 11

### **9.4 Parsing replacement expressions**

Let’s consider replacement expressions.

105

animals <- **c** ('cat', 'dog', 'rat','mouse') out1 <- **quote** (animals[4] <- 'rat') out2 <- **quote** ( **`<-`** (animals[4], 'rat')) out3 <- **quote** ('[<-'(animals,4,'rat')) **as.list** (out1) ## [[1]] ## `<-` ## ## [[2]] ## animals[4] ## ## [[3]] ## [1] "rat" **as.list** (out2) ## [[1]] ## `<-` ## ## [[2]] ## animals[4] ## ## [[3]] ## [1] "rat" **identical** (out1, out2) ## [1] TRUE **as.list** (out3) ## [[1]] ## `[<-` ## ## [[2]] ## animals ##

106

---

[← \- + ## \- () ## \- c ## \- 12 ## \- 13 ## \- 15 ## \- () ## \- rnorm ## \- 3](64-------c---12---13---15-----rnorm---3.md) · [Up: contents](index.md) · [Unit 05 — programming Part 66 — →](66-unit-05-programming-part-66.md)
