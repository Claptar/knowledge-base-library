---
title: 6 Computing on the language
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Computing on the language

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **6.1 The R interpreter**

**Parsing** When you run R, the R interpreter takes the code you type or the lines of code that are read in a batch session and parses each statement, translating the text into functional form. It substitutes objects for the symbols (names) that represent those objects and evaluates the statement, returning the resulting object. For complicated R code, this may be recursive.

Since everything in R is an object, the result of parsing is an object that we’ll be able to investigate, and the result of evaluating the parsed statement is an object.

We’ll see more on parsing in the next section.

52

**_.Primitive()_ and** **_.Internal()_ (and** **_.External_ ())** Some functionality is implemented internally within the C implementation that lies at the heart of R. If you see _.Internal()_ or _.Primitive()_ or _.External()_ , in the code of a function, you know it’s implemented internally (and therefore generally very quickly). Unfortunately, it also means that you don’t get to see R code that implements the functionality, though Chambers p. 465 describes how you can look into the C source code. Basically you need to download the source code for the relevant package off of CRAN.

plot.xy _# plot.xy() is called by plot.default()_ ## function (xy, type, pch = par("pch"), lty = par("lty"), col = par("col"), ## bg = NA, cex = 1, lwd = par("lwd"), ...) ## invisible(.External.graphics(C_plotXY, xy, type, pch, lty, col, ## bg, cex, lwd, ...)) ## <bytecode: 0x21aac7b8> ## <environment: namespace:graphics> **print** (`%*%`) ## function (x, y) .Primitive("%*%")

### **6.2 Parsing code and understanding language objects**

R code can be manipulated in text form and we can actually write R code that will create or manipulate R code. We can then evaluate that R code using _eval()_ .

_quote()_ will parse R code, but not evaluate it. This allows you to work with the code rather than the results of evaluating that code. The _print()_ method for language objects is not very helpful! But we can see the parsed code by treating the result as a list.

obj <- **quote** ( **if** (x > 1) "orange" **else** "apple") **as.list** (obj) ## [[1]] ## `if` ## ## [[2]] ## x > 1 ##

53

---

[← [1] "x" "y" rm ("x", envir = e) parent.env (e) ##](24-1-x-y-rm-x-envir-e-parent-env-e.md) · [Up: contents](index.md) · [Unit 06 — Rprog Part 26 — →](26-unit-06-rprog-part-26.md)
