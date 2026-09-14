---
title: if ISLR2 isn't installed, install it
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# if ISLR2 isn't installed, install it

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

if(!"ISLR2" %in% installed.packages()[,1]){
  install.packages("ISLR2")
}

---

[← All defaults](05-all-defaults.md) · [Up: contents](index.md) · [load and preview the dataset →](07-load-and-preview-the-dataset.md)
