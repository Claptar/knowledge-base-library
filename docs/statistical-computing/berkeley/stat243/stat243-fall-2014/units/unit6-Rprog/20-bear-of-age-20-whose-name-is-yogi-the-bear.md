---
title: Bear of age 20 whose name is Yogi the Bear.
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Bear of age 20 whose name is Yogi the Bear.

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note that the _print()_ function is what is called when you simply type the name of the object, so we can have object information printed out in a structured way. Recall that the output when we type the name of an _lm_ object is NOT simply a regurgitation of the elements of the list - rather _print.lm()_ is called.

Similarly, when we used print(object.size(x)) we were invoking the _object_size_ - specific print method which gets the value of the size and then formats it. So there’s actually a fair amount going on behind the scenes.

Surprisingly, the _summary()_ method generally doesn’t actually print out information; rather it computes things not stored in the original object and returns it as a new class (e.g., class _summary.lm_ ), which is then automatically printed, per my comment above, using _print.summary.lm()_ , unless one assigns it to a new object. Note that _print.summary.lm()_ is hidden from user view.

out <- **summary** (mod) out **print** (out) **getS3method** (f = "print", class = "summary.lm")

**More on inheritance** As noted with _lm_ and _glm_ objects, we can assign more than one class to an object. Here _summarize()_ still works, even though the primary class is _grizzly_bear_ .

**class** (yog) <- **c** ("grizzly_bear", "bear") **summarize** (yog)

---

[← Unit 06 — Rprog Part 19 —](19-unit-06-rprog-part-19.md) · [Up: contents](index.md) · [Bear of age 20 whose name is Yogi the Bear. →](21-bear-of-age-20-whose-name-is-yogi-the-bear.md)
