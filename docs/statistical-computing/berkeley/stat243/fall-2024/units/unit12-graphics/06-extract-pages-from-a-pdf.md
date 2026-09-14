---
title: extract pages from a pdf
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit12-graphics.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit12-graphics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# extract pages from a pdf

**Source:** [`units/unit12-graphics.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit12-graphics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage=m \
   -dLastPage=n -sOutputFile=out.pdf in.pdf

---

[← convert from pdf to jpeg](05-convert-from-pdf-to-jpeg.md) · [Up: contents](index.md) · [merge pdf files into one pdf →](07-merge-pdf-files-into-one-pdf.md)
