---
title: remove after summing counts (otherwise IDs get mixed up)
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# remove after summing counts (otherwise IDs get mixed up)

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

newCounts <- newCounts[,-toRemove]
newCD <- cd[-toRemove,]

---

[← four donor patients](09-four-donor-patients.md) · [Up: contents](index.md) · [Create new SummarizedExperiment →](11-create-new-summarizedexperiment.md)
