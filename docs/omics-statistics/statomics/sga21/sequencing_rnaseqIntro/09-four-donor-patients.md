---
title: four donor patients
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# four donor patients

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

patient1 <- colData(se1)$patient
table(patient1)

table(patient1, treatment1, time1)
```

- We observe that the number of samples that we are observing here is larger than what is described in the paper. As also described in the [parathyroidSE vignette](https://www.bioconductor.org/packages/release/data/experiment/vignettes/parathyroidSE/inst/doc/parathyroidSE.pdf), some samples were spread over multiple sequencing runs (i.e., the same sample being sequenced repeatedly) and therefore constitute **technical replication**, rather than biological replication.
- We have previously seen that technical replicates can be considered to be distributed according to a Poisson distribution. One important property of Poisson random variables is that a sum of Poisson random variables still follow a Poisson distribution. Indeed, if $X \sim Poi(\mu_X)$ and $Y \sim Poi(\mu_Y)$, then $X + Y = Z \sim Poi(\mu_X + \mu_Y)$.
- For this reason, it is often suggested to sum technical replicates rather than, for example, averaging, which does not retain the Poisson property (try for yourself!). We'll therefore first sum the technical replicates.

```r
dupExps <- as.character(colData(se1)$experiment[duplicated(colData(se1)$experiment)])
dupExps

counts <- assays(se1)$counts
newCounts <- counts
cd <- colData(se1)
for(ss in 1:length(dupExps)){
  # check which samples are duplicates
  relevantId <- which(colData(se1)$experiment == dupExps[ss])
  # sum counts
  newCounts[,relevantId[1]] <- rowSums(counts[,relevantId])
  # keep which columns / rows to remove.
  if(ss == 1){
    toRemove <- relevantId[2]
  } else {
    toRemove <- c(toRemove, relevantId[2])
  }
}

---

[← two timepoints](08-two-timepoints.md) · [Up: contents](index.md) · [remove after summing counts (otherwise IDs get mixed up) →](10-remove-after-summing-counts-otherwise-ids-get-mixed-up.md)
