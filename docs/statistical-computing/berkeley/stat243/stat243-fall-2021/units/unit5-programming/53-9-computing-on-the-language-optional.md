---
title: 9 Computing on the language (optional)
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 9 Computing on the language (optional)

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We won’t cover much, if any, of this section and I won’t expect you to know this material, but some of you may find it interesting. Also, when I talked about R being a particularly flexible language in explaining in part why R can be slow, much of that flexibility is illustrated here.

### **9.1 The R interpreter**

**Parsing** When you run R, the R interpreter takes the code you type or the lines of code that are read in a batch session and parses each statement, translating the text into functional form. It substitutes objects for the symbols (names) that represent those objects and evaluates the statement,

101

returning the resulting object. For complicated R code, this may be recursive.

Since everything in R is an object, the result of parsing is an object that we’ll be able to investigate, and the result of evaluating the parsed statement is an object.

We’ll see more on parsing in the next section.

**_.Primitive()_ and** **_.Internal()_ (and** **_.External_ ())** Some functionality is implemented internally within the C implementation that lies at the heart of R. If you see _.Internal()_ or _.Primitive()_ or _.External()_ , in the code of a function, you know it’s implemented internally (and therefore generally very quickly). Unfortunately, it also means that you don’t get to see R code that implements the functionality, though Chambers p. 465 describes how you can look into the C source code. Basically you need to download the source code for the relevant package off of CRAN.

plot.xy _# plot.xy() is called by plot.default()_

---

[← @55691c5b8f80 14 REALSXP g0c7 [REF(1)] (len=100, tl=0)](52-55691c5b8f80-14-realsxp-g0c7-ref-1-len-100-tl-0.md) · [Up: contents](index.md) · [Unit 05 — programming Part 54 — →](54-unit-05-programming-part-54.md)
