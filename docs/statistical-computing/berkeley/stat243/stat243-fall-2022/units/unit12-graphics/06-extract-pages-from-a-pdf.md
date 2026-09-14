---
title: extract pages from a pdf
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit12-graphics.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit12-graphics.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# extract pages from a pdf

**Source:** [`units/unit12-graphics.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit12-graphics.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dFirstPage=m \
   -dLastPage=n -sOutputFile=out.pdf in.pdf

---

[← convert from pdf to jpeg](05-convert-from-pdf-to-jpeg.md) · [Up: contents](index.md) · [merge pdf files into one pdf →](07-merge-pdf-files-into-one-pdf.md)
