---
title: Unit 05 — programming Part 45 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 45 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One frustration with memory management is that if your code bumps up against the memory limits of the machine, it can be very slow to respond even when you’re trying to cancel the statement with _Ctrl-C_ . You can impose memory limits in Linux by starting R (from the UNIX prompt) in a fashion such as this

> R --max-vsize=1000M

Then if you try to create an object that will push you over that limit or execute code that involves going over the limit, it will simply fail with the message “ _Error: vector memory exhausted (limit reached?)_ ”. So this approach may be a nice way to avoid paging/swapping by setting the maximum in relation to the physical memory of the machine. It might also help in debugging memory leaks because the program would fail at the point that memory use was increasing. I haven’t played around with this much, so offer this with a note of caution.

85

We can use an internal function called _inspect()_ to see where in memory an object is stored. We’ll see that this can be a handy tool for seeing where copies are made and where they are not. Here we can see how the overall list is stored as well as the elements of the list and the attributes of the list.

x <- **rnorm** (5) **.Internal** ( **inspect** (x)) ## @5639aeaec6a8 14 REALSXP g0c4 [NAM(7)] (len=5, tl=0) obj <- **list** (a = **rnorm** (5), b = **list** (d = "adfs")) **.Internal** ( **inspect** (obj$a)) ## @5639b05ab038 14 REALSXP g0c4 [NAM(7)] (len=5, tl=0) **.Internal** ( **inspect** (obj))

---

[← Unit 05 — programming Part 44 —](44-unit-05-programming-part-44.md) · [Up: contents](index.md) · [Unit 05 — programming Part 46 — →](46-unit-05-programming-part-46.md)
