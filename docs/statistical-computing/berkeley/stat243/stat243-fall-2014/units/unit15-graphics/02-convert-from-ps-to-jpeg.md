---
title: convert from ps to jpeg
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit15-graphics.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit15-graphics.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# convert from ps to jpeg

**Source:** [`units/unit15-graphics.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit15-graphics.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

gs -dNOPAUSE -r[xres]x[yres] -sDEVICE=jpeg -sOutputFile=file.jpg file.ps

27

---

[← Unit 15: Graphics](01-unit-15-graphics.md) · [Up: contents](index.md) · [extract pages from a pdf gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage=m →](03-extract-pages-from-a-pdf-gs--sdevice-pdfwrite--dnopause--dqu.md)
