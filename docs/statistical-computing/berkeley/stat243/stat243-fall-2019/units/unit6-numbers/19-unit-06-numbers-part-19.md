---
title: Unit 06 — numbers Part 19 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit6-numbers.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit6-numbers.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 06 — numbers Part 19 —

**Source:** [`units/unit6-numbers.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit6-numbers.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let’s see what arithmetic we can do exactly with integers stored as doubles and how that relates to the absolute spacing of numbers we’ve just seen:

dgi <- **function** (x) **formatC** (x, digits = 20, format = 'g')

**dgi** (2^52) ## [1] " 4503599627370496" **dgi** (2^52+1) ## [1] " 4503599627370497"

13

**dgi** (2^53) ## [1] " 9007199254740992" **dgi** (2^53+1) ## [1] " 9007199254740992" **dgi** (2^53+2) ## [1] " 9007199254740994" **dgi** (2^54) ## [1] " 18014398509481984" **dgi** (2^54+2) ## [1] " 18014398509481984" **dgi** (2^54+4) ## [1] " 18014398509481988" **bits** (2^53) ## [1] "01000011 01000000 00000000 00000000 00000000 00000000 00000000 00000000" **bits** (2^53+1)

---

[← Unit 06 — numbers Part 18 —](18-unit-06-numbers-part-18.md) · [Up: contents](index.md) · [Unit 06 — numbers Part 20 — →](20-unit-06-numbers-part-20.md)
