---
title: Unit 04 — programming Part 03 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 03 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- To see some of the options that control how R behaves, try the _options()_ function. The _width_ option changes the number of characters of width printed to the screen, while the _max.print_ option prevents too much of a large object from being printed to the screen. The _digits_ option changes the number of digits of numbers printed to the screen (but be careful as this can be deceptive if you then try to compare two numbers based on what you see on the screen).

_# options() # this would print out a long list of options_ **options** ()[1:5] ## $add.smooth ## [1] TRUE ## ## $bitmapType ## [1] "cairo" ## ## $browser ## [1] "xdg-open" ## ## $browserNLdisabled ## [1] FALSE

3

---

[← 1 Interacting with the operating system from R and controlling R’s behavior](02-1-interacting-with-the-operating-system-from-r-and-controlli.md) · [Up: contents](index.md) · [Unit 04 — programming Part 04 — →](04-unit-04-programming-part-04.md)
