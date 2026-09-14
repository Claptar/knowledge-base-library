---
title: extract pages from a pdf
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit12-graphics.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit12-graphics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# extract pages from a pdf

**Source:** [`units/unit12-graphics.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit12-graphics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage=m \
   -dLastPage=n -sOutputFile=out.pdf in.pdf

---

[← convert from pdf to jpeg](05-convert-from-pdf-to-jpeg.md) · [Up: contents](index.md) · [merge pdf files into one pdf →](07-merge-pdf-files-into-one-pdf.md)
