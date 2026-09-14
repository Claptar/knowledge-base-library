---
title: Unit 11 — optim Part 06 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit11-optim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 11 — optim Part 06 —

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit11-optim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

7


<!-- Start of picture text -->
converges diverges<br>3<br>f'(x) f'(x) 1<br>1<br>f"(x) f"(x)<br>3<br>4 567891<br>2<br>2<br>−15 −5 0 5 10 15 −15 −5 0 5 10 15<br>x x<br>0.4 0.4<br>0.2 0.2<br>f'(x) 0.0 f'(x) 0.0<br>−0.4 −0.4<br><!-- End of picture text -->

_<mark>## whoops</mark>_

Now let’s see an example of climbing uphill and finding a local maximum rather than minimum.

_## example of mistakenly climbing uphill_ **par** (mfrow = **c** (3,1)) _# original fxn_ f <- **function** (x) **cos** (x) _# gradient_ fp <- **function** (x) - **sin** (x) _# second derivative_ fpp <- **function** (x) - **cos** (x) xs <- **seq** (0, 2*pi, len = 300) x0 <- 1 _# starting point_ **fp** (x0) _# negative_ ## [1] -0.841471 **fpp** (x0) _# negative_

8

---

[← Unit 11 — optim Part 05 —](05-unit-11-optim-part-05.md) · [Up: contents](index.md) · [Unit 11 — optim Part 07 — →](07-unit-11-optim-part-07.md)
