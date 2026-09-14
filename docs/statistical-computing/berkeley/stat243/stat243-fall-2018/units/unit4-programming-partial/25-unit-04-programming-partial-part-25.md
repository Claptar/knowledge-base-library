---
title: Unit 04 — programming partial Part 25 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 25 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In many cases there will be a default method (here, summary.default()), so if no method is defined for the class, R uses the default. Sidenote: arguments to a generic method are passed along to the selected method by passing along the calling environment.

We can define new generic methods:

summarize <- **function** (object, ...) **UseMethod** ("summarize")

Once UseMethod() is called, R searches for the specific method associated with the class of object and calls that method, without ever returning to the generic method. Let’s try this out on our bear class. In reality, we’d write either summary.bear() or print.bear() (and of course the generics for summary and print already exist) but for illustration, I wanted to show how we would write both the generic and the specific method, so I’ll write a summarize method.

summarize.bear <- **function** (object) **return** ( **with** (object, **cat** ("Bear of age ", age, " whose name is ", firstname, " ", surname, ".\n", sep = ""))) **summarize** (yog)

---

[← Unit 04 — programming partial Part 24 —](24-unit-04-programming-partial-part-24.md) · [Up: contents](index.md) · [Bear of age 20 whose name is Yogi the Bear. →](26-bear-of-age-20-whose-name-is-yogi-the-bear.md)
