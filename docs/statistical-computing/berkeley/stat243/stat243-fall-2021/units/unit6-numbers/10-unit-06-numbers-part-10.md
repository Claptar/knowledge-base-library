---
title: Unit 06 — numbers Part 10 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit6-numbers.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 10 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit6-numbers.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let’s see what arithmetic we can do exactly with integers stored as doubles and how that relates to the absolute spacing of numbers we’ve just seen:

dgi <- **function** (x) **formatC** (x, digits = 20, format = 'g') **dgi** (2^52) ## [1] " 4503599627370496" **dgi** (2^52+1) ## [1] " 4503599627370497" **dgi** (2^53) ## [1] " 9007199254740992" **dgi** (2^53+1) ## [1] " 9007199254740992" **dgi** (2^53+2) ## [1] " 9007199254740994" **dgi** (2^54)

14

---

[← Unit 06 — numbers Part 09 —](09-unit-06-numbers-part-09.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 11 — →](11-unit-06-numbers-part-11.md)
