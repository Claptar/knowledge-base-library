---
title: merge pdf files into one pdf
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit12-graphics.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit12-graphics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# merge pdf files into one pdf

**Source:** [`units/unit12-graphics.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit12-graphics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=out.pdf \
   -dBATCH in1.pdf in2.pdf in3.pdf
```

---

[← extract pages from a pdf](06-extract-pages-from-a-pdf.md) · [Up: contents](index.md) · [4. Colors →](08-4-colors.md)
