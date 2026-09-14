---
title: All defaults
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd
source_file: sources/statomics-sga21/sequencing_technicalDE.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# All defaults

**Source:** [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

include_graphics("./images_sequencing/limmaVoomMeanVariance.png")
```

 ---

 - The mean-variance relationship is dataset-specific and needs to be estimated separately for each dataset.
 - The mean-variance trend is estimated nonparametrically across all genes, using a global mean and variance for each gene. Using this trend, observation-level variances are estimated for each individual observation.
 - These observation-level variances are then used as inverse weights in the linear modeling framework, to account for heteroscedasticity.

```r

---

[← limma-voom as an alternative approach to modeling counts](11-limma-voom-as-an-alternative-approach-to-modeling-counts.md) · [Up: contents](index.md) · [All defaults →](13-all-defaults.md)
