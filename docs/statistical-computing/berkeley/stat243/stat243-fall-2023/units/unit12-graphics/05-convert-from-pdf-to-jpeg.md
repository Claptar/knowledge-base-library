---
title: convert from pdf to jpeg
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit12-graphics.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit12-graphics.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# convert from pdf to jpeg

**Source:** [`units/unit12-graphics.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit12-graphics.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

gs -dNOPAUSE -r[xres]x[yres] -sDEVICE=jpeg -sOutputFile=file.jpg file.pdf

---

[← 3. Graphics file formats](04-3-graphics-file-formats.md) · [Up: contents](index.md) · [extract pages from a pdf →](06-extract-pages-from-a-pdf.md)
