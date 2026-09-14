---
title: convert from ps to jpeg
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit13-graphics.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit13-graphics.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# convert from ps to jpeg

**Source:** [`units/unit13-graphics.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit13-graphics.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

gs -dNOPAUSE -r[xres]x[yres] -sDEVICE=jpeg -sOutputFile=file.jpg file.ps

32

---

[← Unit 13: Graphics](01-unit-13-graphics.md) · [Up: contents](index.md) · [Unit 13 — graphics Part 03 — →](03-unit-13-graphics-part-03.md)
