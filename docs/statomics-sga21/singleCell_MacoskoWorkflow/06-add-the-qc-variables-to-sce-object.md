---
title: add the QC variables to sce object
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd
source_file: sources/statomics-sga21/singleCell_MacoskoWorkflow.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# add the QC variables to sce object

**Source:** [`singleCell_MacoskoWorkflow.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_MacoskoWorkflow.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

colData(sce) <- cbind(colData(sce), df)
# the QC variables have now been added to the colData of our SCE object.
colData(sce)
```

---

[← Calculate QC variables](05-calculate-qc-variables.md) · [Up: contents](index.md) · [EDA →](07-eda.md)
