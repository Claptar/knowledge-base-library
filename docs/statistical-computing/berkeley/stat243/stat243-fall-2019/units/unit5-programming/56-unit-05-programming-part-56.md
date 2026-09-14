---
title: Unit 05 — programming Part 56 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 56 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Or we can see this using _mem_change()_ .

**library** (pryr) **rm** (x) **mem_change** (x <- **rnorm** (1e7)) ## 80 MB **address** (x) ## [1] "0x7ff692aa8010" **mem_change** (x[3] <- 8) ## 320 B **address** (x) ## [1] "0x7ff692aa8010"

91

**mem_change** (y <- x) ## -80 MB **address** (y) ## [1] "0x7ff692aa8010" **mem_change** (x[3] <- 8) ## 80 MB **address** (x) ## [1] "0x7ff68de5c010" **address** (y) ## [1] "0x7ff692aa8010"

**Challenge** : explain the results of the example above.

**How does copy-on-change work and how can it be fooled?** As discussed by Radford Neal, who is working to improve the efficiency of R in a project called pqR, _“So R doesn’t copy all the time. Instead, it maintains a count, called NAMED, of how many “names” refer to an object, and copies only when an object that needs to be modified is also referred to by another name. Unfortunately, however, this scheme works rather poorly. Many unnecessary copies are still made, while many bugs have arisen in which copies aren’t made when necessary._ ” I believe improvements have been made in recent versions of R in this regard.

Here are examples of how the NAMED count can be fooled into making a copy unnecessarily. Why do I say these copies are unnecessary and why is NAMED fooled?

a <- 1:5 **refs** (a) ## [1] 7 b <- a **address** (a)

92

---

[← Unit 05 — programming Part 55 —](55-unit-05-programming-part-55.md) · [Up: contents](index.md) · [Unit 05 — programming Part 57 — →](57-unit-05-programming-part-57.md)
