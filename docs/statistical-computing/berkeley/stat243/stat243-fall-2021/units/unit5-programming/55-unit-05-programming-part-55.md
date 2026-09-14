---
title: Unit 05 — programming Part 55 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 55 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **9.3 Manipulating the parse tree**

Of course since the parsed code is just an object, we can manipulate it, i.e., _compute on the language_ :

out <- **quote** (y <- 3) out[[3]] <- 4 **eval** (out) y ## [1] 4

Here’s another example:

109

e1 <- **quote** (4 + 5) e2 <- **quote** ( **plot** (x, y)) e2[[1]] <- ` + ` **eval** (e2) ## [1] 7 e1[[3]] <- e2 e1 ## 4 + .Primitive("+")(x, y) **class** (e1[[3]]) _# note the nesting_ ## [1] "call" **eval** (e1) _# what should I get?_ ## [1] 11

We can also turn it back into standard R code, as a character, using _deparse()_ , which turns the parse tree back into R code as text. _parse()_ is like _quote()_ but it takes the code in the form of a string rather than an actual expression:

codeText <- **deparse** (out) parsedCode <- **parse** (text = codeText) _## parse() works like quote() except on the code in the form of a string_ **eval** (parsedCode) **deparse** ( **quote** ( **if** (x > 1) "orange" **else** "apple")) ## [1] "if (x > 1) \"orange\" else \"apple\""

Note that the quotes have been escaped since they’re inside a string.

It can be very useful to be able to convert names of objects that are in the form of text to names that R interprets as symbols referring to objects:

x3 <- 7 i <- 3 **as.name** ( **paste** ('x', i, sep=''))

110

---

[← Unit 05 — programming Part 54 —](54-unit-05-programming-part-54.md) · [Up: contents](index.md) · [Unit 05 — programming Part 56 — →](56-unit-05-programming-part-56.md)
