---
title: Unit 06 — numbers Part 24 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 24 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let’s see what arithmetic we can do exactly with integers stored as doubles and how that relates to the absolute spacing of numbers we’ve just seen:

dgi <- **function** (x) **formatC** (x, digits = 20, format = 'g') **dgi** (2^52) ## [1] " 4503599627370496" **dgi** (2^52+1) ## [1] " 4503599627370497" **dgi** (2^53) ## [1] " 9007199254740992" **dgi** (2^53+1) ## [1] " 9007199254740992" **dgi** (2^53+2) ## [1] " 9007199254740994" **dgi** (2^54) ## [1] " 18014398509481984" **dgi** (2^54+2) ## [1] " 18014398509481984" **dgi** (2^54+4)

14

---

[← Unit 06 — numbers Part 23 —](23-unit-06-numbers-part-23.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 25 — →](25-unit-06-numbers-part-25.md)
