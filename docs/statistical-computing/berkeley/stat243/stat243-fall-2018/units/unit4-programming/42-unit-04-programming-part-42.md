---
title: Unit 04 — programming Part 42 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 42 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One frustration with memory management is that if your code bumps up against the memory limits of the machine, it can be very slow to respond even when you’re trying to cancel the statement with _Ctrl-C_ . You can impose memory limits in Linux by starting R (from the UNIX prompt) in a fashion such as this

> R --max-vsize=1000M

Then if you try to create an object that will push you over that limit or execute code that involves going over the limit, it will simply fail with the message “ _Error: vector memory exhausted (limit reached?)_ ”. So this approach may be a nice way to avoid paging/swapping by setting the maximum in relation to the physical memory of the machine. It might also help in debugging memory leaks because the program would fail at the point that memory use was increasing. I haven’t played around with this much, so offer this with a note of caution.

We can use an internal function called _inspect()_ to see where in memory an object is stored. We’ll see that this can be a handy tool for seeing where copies are made and where they are not.

x <- **rnorm** (5) **.Internal** ( **inspect** (x)) ## @5a193b8 14 REALSXP g0c4 [NAM(2)] (len=5, tl=0) -0.224897,-0.160423,1.49911,1.82671,-0.00600455 obj <- **list** (a = **rnorm** (5), b = **list** (d = "adfs")) **.Internal** ( **inspect** (obj$a)) ## @5002648 14 REALSXP g0c4 [NAM(2)] (len=5, tl=0) -0.979494,0.0127224,-0.602454,-0.313131,0.0855851 **.Internal** ( **inspect** (obj)) ## @5dc81d0 19 VECSXP g0c2 [NAM(2),ATT] (len=2, tl=0) ## @5002648 14 REALSXP g0c4 [NAM(2)] (len=5, tl=0) ## @5c43248 19 VECSXP g0c1 [ATT] (len=1, tl=0) ## @5e3e318 16 STRSXP g0c1 [NAM(2)] (len=1, tl=0)

78

---

[← Unit 04 — programming Part 41 —](41-unit-04-programming-part-41.md) · [Up: contents](index.md) · [Unit 04 — programming Part 43 — →](43-unit-04-programming-part-43.md)
