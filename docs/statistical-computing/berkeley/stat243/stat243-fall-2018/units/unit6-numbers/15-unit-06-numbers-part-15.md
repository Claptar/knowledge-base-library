---
title: Unit 06 — numbers Part 15 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 15 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

8

**dg** (1/32) ## [1] "0.03125000000000000000" **dg** (1/33) ## [1] "0.03030303030303030387"

So why is 0.5 stored exactly and 0.1 not stored exactly? By analogy, consider the difficulty with representing 1/3 in base 10.

### **2.2 Overflow and underflow**

The largest and smallest numbers we can represent are 2<sup>_e_max</sup> and 2<sup>_e_min</sup> where _e_ max and _e_ min are the smallest and largest possible values of the exponent. Let’s consider the exponent and what we can infer about the range of possible numbers. With 11 bits for _e_ , we can represent _±_ 2<sup>10</sup> = _±_ 1024 different exponent values (see _.Machine$double.max.exp_ ) (why is _.Machine$double.min.exp_ only -1022? ). So the largest number we could represent is 2<sup>1024</sup> . What is this in base 10?

**log10** (2^1024) _# whoops ... we've actually just barely overflowed_ ## [1] Inf **log10** (2^1023) ## [1] 307.9537 .Machine$double.xmax ## [1] 1.797693e+308 .Machine$double.xmin ## [1] 2.225074e-308

We could have been smarter about that calculation: log10 2<sup>1024</sup> = log2 2<sup>1024</sup> _/_ log2 10 = 1024 _/_ 3 _._ 32 _≈_ 308. Analogously for the smallest number, so we have that floating points can range between 1 _×_ 10<sup>_−_308</sup> and 1 _×_ 10<sup>308</sup> . Take a look at _.Machine$double.xmax_ and _.Machine.double.xmin_ . Producing something larger or smaller in magnitude than these values is called overflow and underflow respectively. When we overflow, R gives back an Inf or -Inf (and in other cases we might get an

9

error message). When we underflow, we get back 0, which in particular can be a problem if we try to divide by the value.

### **2.3 Integers or floats?**

Values stored as integers should overflow if they exceed _.Machine$integer.max_ .

Should 2<sup>45</sup> overflow?

x <- 2^45 z <- 25 **class** (x) ## [1] "numeric" **class** (z) ## [1] "numeric" **as.integer** (x) ## Warning: NAs introduced by coercion to integer range ## [1] NA **as.integer** (z) ## [1] 25 1e308 ## [1] 1e+308 1e309 ## [1] Inf 2^31 ## [1] 2147483648 x <- 2147483647L x

10

---

[← Unit 06 — numbers Part 14 —](14-unit-06-numbers-part-14.md) · [Up: contents](index.md) · [[1] 2147483647 class (x) ## [1] "integer" x <- 2147483648L class (x) ## [1] "numeric" →](16-1-2147483647-class-x-1-integer-x---2147483648l-class-x-1-num.md)
