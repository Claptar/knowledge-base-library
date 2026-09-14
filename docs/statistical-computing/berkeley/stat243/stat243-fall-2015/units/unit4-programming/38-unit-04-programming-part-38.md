---
title: Unit 04 — programming Part 38 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 38 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Or we can see this using _mem_change()_ .

**library** (pryr) **mem_change** (x <- **rnorm** (1e7)) ## -848 B **mem_change** (x[3] <- 8) ## 1.42 kB

As discussed by Radford Neal, who is working to improve the efficiency of R in a project called pqR, _“So R doesn’t copy all the time. Instead, it maintains a count, called NAMED, of how many “names” refer to an object, and copies only when an object that needs to be modified is also referred to by another name. Unfortunately, however, this scheme works rather poorly. Many unnecessary copies are still made, while many bugs have arisen in which copies aren’t made when necessary._ ” I believe some improvements have been made in recent versions of R in this regard.

Here are examples of how the NAMED count can be fooled into making a copy unnecessarily. Why do I say these copies are unnecessary and why is NAMED fooled?

78

**rm** (x, y) f <- **function** (x) **sum** (x^2) y <- **rnorm** (10) **refs** (y) _# from pryr - reports on the NAMED count_ ## [1] 2 **f** (y) ## [1] 6.13 **refs** (y) ## [1] 2 **address** (y) ## [1] "0x58d3070" y[3] <- 2 **address** (y) ## [1] "0x5aa3588" a <- 1:5 b <- a **address** (a) ## [1] "0x50472e0" **address** (b) ## [1] "0x50472e0" a[2] <- 0 b[2] <- 4 **address** (a) ## [1] "0x50467e0" **address** (b) ## [1] "0x5046568"

79

We can use the _tracemem()_ function to assess what is going on without all those _inspect()_ calls. Anything surprising in what you see?

a <- 1:10 **tracemem** (a) ## [1] "<0x63ca508>" _## b and a share memory_ b <- a b[1] <- 1

---

[← [1] "0x4fc48d0"](37-1-0x4fc48d0.md) · [Up: contents](index.md) · [Unit 04 — programming Part 39 — →](39-unit-04-programming-part-39.md)
