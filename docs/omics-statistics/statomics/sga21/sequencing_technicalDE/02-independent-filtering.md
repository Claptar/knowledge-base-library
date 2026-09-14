---
title: Independent filtering
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Independent filtering

**Source:** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Independent filtering, where genes/transcripts/proteins are filtered out prior to statistical analysis, is a common practice in 'omics experiments. Typically, lowly expressed features are filtered out, and one can argue that these features' expression is too low to be deemed biologically relevant. In addition, low-count features are also associated with a low statistical power for differential expression (remember relative uncertainty of counts, and `edgeR`'s BCV plot), and will increase the number of tests performed, and therefore lead to a more severe multiple testing correction.

```r

---

[← A function for captioning and referencing images](01-a-function-for-captioning-and-referencing-images.md) · [Up: contents](index.md) · [All defaults →](03-all-defaults.md)
