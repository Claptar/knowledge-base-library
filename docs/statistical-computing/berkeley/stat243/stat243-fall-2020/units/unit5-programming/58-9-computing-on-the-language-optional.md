---
title: 9 Computing on the language (optional)
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 9 Computing on the language (optional)

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We won’t cover much, if any, of this section and I won’t expect you to know this material, but some of you may find it interesting. Also, when I talked about R being a particularly flexible language in explaining in part why R can be slow, much of that flexibility is illustrated here.

### **9.1 The R interpreter**

**Parsing** When you run R, the R interpreter takes the code you type or the lines of code that are read in a batch session and parses each statement, translating the text into functional form. It substitutes objects for the symbols (names) that represent those objects and evaluates the statement, returning the resulting object. For complicated R code, this may be recursive.

Since everything in R is an object, the result of parsing is an object that we’ll be able to investigate, and the result of evaluating the parsed statement is an object.

101

We’ll see more on parsing in the next section.

**_.Primitive()_ and** **_.Internal()_ (and** **_.External_ ())** Some functionality is implemented internally within the C implementation that lies at the heart of R. If you see _.Internal()_ or _.Primitive()_ or _.External()_ , in the code of a function, you know it’s implemented internally (and therefore generally very quickly). Unfortunately, it also means that you don’t get to see R code that implements the functionality, though Chambers p. 465 describes how you can look into the C source code. Basically you need to download the source code for the relevant package off of CRAN.

plot.xy _# plot.xy() is called by plot.default()_ ## function (xy, type, pch = par("pch"), lty = par("lty"), col = par("col"), ## bg = NA, cex = 1, lwd = par("lwd"), ...) ## invisible(.External.graphics(C_plotXY, xy, type, pch, lty, col, ## bg, cex, lwd, ...)) ## <bytecode: 0x5639aef128c0> ## <environment: namespace:graphics> **print** (`%*%`) ## function (x, y) .Primitive("%*%")

### **9.2 Parsing code and understanding language objects**

R code can be manipulated in text form and we can actually write R code that will create or manipulate R code. We can then evaluate that R code using _eval()_ .

_quote()_ will parse R code, but not evaluate it. This allows you to work with the code rather than the results of evaluating that code. The _print()_ method for language objects is not very helpful! But we can see the parsed code by treating the result as a list.

obj <- **quote** ( **if** (x > 1) "orange" **else** "apple") **as.list** (obj) ## [[1]] ## `if` ## ## [[2]]

102

---

[← Unit 05 — programming Part 57 —](57-unit-05-programming-part-57.md) · [Up: contents](index.md) · [Unit 05 — programming Part 59 — →](59-unit-05-programming-part-59.md)
