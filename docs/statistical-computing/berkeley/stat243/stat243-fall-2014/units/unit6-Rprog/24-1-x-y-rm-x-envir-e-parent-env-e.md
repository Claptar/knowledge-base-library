---
title: '[1] "x" "y" rm ("x", envir = e) parent.env (e) ##'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] "x" "y" rm ("x", envir = e) parent.env (e) ##

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Before the existence of Reference Classes, using an environment was one way to pass objects by reference, avoiding having to re-assign the output. Here’s an example where we iteratively update a random walk.

myWalk <- **new.env** () myWalk$pos = 0 nextStep <- **function** (walk) walk$pos <- walk$pos + **sample** ( **c** (-1, 1), size = 1) **nextStep** (myWalk)

We can use _eval()_ to evaluate some code within a specified environment. By default, it evaluates in the result of _parent.frame()_ , which amounts to evaluating in the frame from which _eval()_ was called. _evalq()_ avoids having to use _quote()_ .

**eval** ( **quote** (pos <- pos + **sample** ( **c** (-1, 1), 1)), envir = myWalk) **evalq** (pos <- pos + **sample** ( **c** (-1, 1), 1), envir = myWalk)

---

[← 5 Creating and working in an environment](23-5-creating-and-working-in-an-environment.md) · [Up: contents](index.md) · [6 Computing on the language →](25-6-computing-on-the-language.md)
