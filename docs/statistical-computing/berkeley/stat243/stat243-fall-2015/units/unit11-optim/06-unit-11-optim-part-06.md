---
title: Unit 11 — optim Part 06 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit11-optim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 11 — optim Part 06 —

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit11-optim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_## bisection_

12

bisecStep <- **function** (interval, fp){ xt <- **mean** (interval) **if** ( **fp** (interval[1]) * **fp** (xt) <= 0) interval[2] <- xt **else** interval[1] **return** (interval) } nIt <- 30 a0 <- 2; b0 <- (3*pi/2) - (xstar - a0) _## have b0 be as far from min as a0 for fair comparison with N-R_ interval <- **matrix** (NA, nr = nIt, nc = 2) interval[1, ] <- **c** (a0, b0) **for** (t **in** 2:nIt){ interval[t, ] <- **bisecStep** (interval[t-1, ], fp) } **rowMeans** (interval) ## [1] 2.785398163 3.178097245 2.981747704 3.079922475 3.129009860 ## [6] 3.153553552 3.141281706 3.147417629 3.144349668 3.142815687 ## [11] 3.142048697 3.141665201 3.141473454 3.141569328 3.141617264 ## [16] 3.141593296 3.141581312 3.141587304 3.141590300 3.141591798 ## [21] 3.141592547 3.141592922 3.141592734 3.141592641 3.141592687 ## [26] 3.141592664 3.141592652 3.141592658 3.141592655 3.141592654

---

[← 4 Convergence ideas](05-4-convergence-ideas.md) · [Up: contents](index.md) · [5 Multivariate optimization →](07-5-multivariate-optimization.md)
