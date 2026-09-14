---
title: merge pdf files into one pdf
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit12-graphics.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit12-graphics.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# merge pdf files into one pdf

**Source:** [`units/unit12-graphics.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit12-graphics.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=out.pdf \
   -dBATCH in1.pdf in2.pdf in3.pdf
```

---

[← extract pages from a pdf](06-extract-pages-from-a-pdf.md) · [Up: contents](index.md) · [4. Colors →](08-4-colors.md)
