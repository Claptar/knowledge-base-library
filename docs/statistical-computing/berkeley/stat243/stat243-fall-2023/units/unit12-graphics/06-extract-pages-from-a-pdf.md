---
title: extract pages from a pdf
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit12-graphics.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit12-graphics.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# extract pages from a pdf

**Source:** [`units/unit12-graphics.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit12-graphics.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage=m \
   -dLastPage=n -sOutputFile=out.pdf in.pdf

---

[← convert from pdf to jpeg](05-convert-from-pdf-to-jpeg.md) · [Up: contents](index.md) · [merge pdf files into one pdf →](07-merge-pdf-files-into-one-pdf.md)
