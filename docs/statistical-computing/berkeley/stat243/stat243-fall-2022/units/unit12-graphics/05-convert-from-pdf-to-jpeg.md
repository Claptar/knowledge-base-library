---
title: convert from pdf to jpeg
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit12-graphics.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit12-graphics.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# convert from pdf to jpeg

**Source:** [`units/unit12-graphics.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit12-graphics.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

gs -dNOPAUSE -r[xres]x[yres] -sDEVICE=jpeg -sOutputFile=file.jpg file.pdf

---

[← 3. Graphics file formats](04-3-graphics-file-formats.md) · [Up: contents](index.md) · [extract pages from a pdf →](06-extract-pages-from-a-pdf.md)
