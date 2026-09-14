---
title: Unit 04 — programming Part 20 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 20 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In many cases there will be a default method (here, _summary.default()_ ), so if no method is defined for the class, R uses the default. Sidenote: arguments to a generic method are passed along to the selected method by passing along the calling environment.

We can define new generic methods:

summarize <- **function** (object, ...) **UseMethod** ("summarize")

Once _UseMethod()_ is called, R searches for the specific method associated with the class of _object_ and calls that method, without ever returning to the generic method. Let’s try this out on our _bear_ class. In reality, we’d write either _summary.bear()_ or _print.bear()_ (and of course the generics for _summary_ and _print_ already exist) but for illustration, I wanted to show how we would write both the generic and the specific method, so I’ll write a _summarize_ method.

summarize.bear <- **function** (object) **return** ( **with** (object, **cat** ("Bear of age ", age, " whose name is ", firstname, " ", surname, ".\n", sep = ""))) **summarize** (yog)

---

[← Unit 04 — programming Part 19 —](19-unit-04-programming-part-19.md) · [Up: contents](index.md) · [Bear of age 20 whose name is Yogi the Bear. →](21-bear-of-age-20-whose-name-is-yogi-the-bear.md)
