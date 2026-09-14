---
title: 3 Debugging Strategies
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit5-debug.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Debugging Strategies

**Source:** [`units/unit5-debug.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Debugging is about figuring out what went wrong and where it went wrong.

In compiled languages, one of the difficulties is figuring out what is going on at any given place in the program. This is a lot easier in R by virtue of the fact that R is interpreted and we can step through code line by line at the command line. However, beyond this, there are a variety of helpful tools for debugging R code. In particular these tools can help you step through functions and work inside of functions from packages.

### **3.1 Basic strategies**

Read and think about the error message. Sometimes it’s inscrutable, but often it just needs a bit of deciphering. Looking up a given error message in the R mailing list archive or on Stack Overflow or simply doing a web search with the exact message in double quotes can be a good strategy.

Fix errors from the top down - fix the first error that is reported, because later errors are often caused by the initial error. It’s common to have a string of many errors, which looks daunting, caused by a single initial error.

Is the bug reproducible - does it always happen in the same way at at the same point? It can help to restart R and see if the bug persists - this can sometimes help in figuring out if there is a scoping issue and we are using a global variable that we did not mean to.

Another basic strategy is to build up code in pieces (or tear it back in pieces to a simpler version). This allows you to isolate where the error is occurring.

4

The _codetools_ library has some useful tools for checking code, including a function, _findGlobals()_ , that let’s you look for the use of global variables

**library** (codetools) **findGlobals** (lm)[1:25]

---

[← 2 Tips for avoiding bugs](04-2-tips-for-avoiding-bugs.md) · [Up: contents](index.md) · [Unit 05 — debug Part 06 — →](06-unit-05-debug-part-06.md)
