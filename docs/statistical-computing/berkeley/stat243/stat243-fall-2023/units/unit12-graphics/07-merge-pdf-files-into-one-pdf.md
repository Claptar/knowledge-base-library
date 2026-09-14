---
title: merge pdf files into one pdf
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit12-graphics.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit12-graphics.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# merge pdf files into one pdf

**Source:** [`units/unit12-graphics.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit12-graphics.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=out.pdf \
   -dBATCH in1.pdf in2.pdf in3.pdf
```

---

[← extract pages from a pdf](06-extract-pages-from-a-pdf.md) · [Up: contents](index.md) · [4. Colors →](08-4-colors.md)
