---
title: Experimental design, data import and data exploration
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Experimental design, data import and data exploration

## Experimental design

Let's try to work out the experimental design using the following paragraph from the Methods section of the paper.

```r
# All defaults
include_graphics("./images_sequencing/expDesign_para.png")
```

## Data import and exploration

We will be importing the dataset using the [parathyroidSE](https://www.bioconductor.org/packages/release/data/experiment/html/parathyroidSE.html) data package from [Bioconductor](https://bioconductor.org/).

```r
if (!requireNamespace("BiocManager", quietly = TRUE)){
  install.packages("BiocManager")
}
if(!"SummarizedExperiment" %in% installed.packages()[,1]){
  BiocManager::install("SummarizedExperiment")
}
# install package if not installed.
if(!"parathyroidSE" %in% installed.packages()[,1]) BiocManager::install("parathyroidSE")

suppressPackageStartupMessages({
  library(parathyroidSE)
  library(SummarizedExperiment)
})

# import data
data("parathyroidGenesSE", package="parathyroidSE")
# rename for convenience
se1 <- parathyroidGenesSE
rm(parathyroidGenesSE)

# three treatments
treatment1 <- colData(se1)$treatment
table(treatment1)
# two timepoints
time1 <- colData(se1)$time
table(time1)
# four donor patients
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

# remove after summing counts (otherwise IDs get mixed up)
newCounts <- newCounts[,-toRemove]
newCD <- cd[-toRemove,]

# Create new SummarizedExperiment
se <- SummarizedExperiment(assays = list("counts" = newCounts),
                            colData = newCD,
                            metadata = metadata(se1))

treatment <- colData(se)$treatment
table(treatment)
time <- colData(se)$time
table(time)
patient <- colData(se)$patient
table(patient)

table(patient, treatment, time) # agrees with paper.

```

 - After summing the technical replicates and appropriately updating the sample information, we again create a `SummarizedExperiment` object, which is essentially a data container that contains all relevant information about your experiment. Please see the [vignette](https://bioconductor.org/packages/release/bioc/vignettes/SummarizedExperiment/inst/doc/SummarizedExperiment.html) for more information on how to use this class.
 - By directly matching columns (samples) and rows (genes) to their relevant metadata, the `SummarizedExperiment` class avoids mistakes by mis-matching columns and rows with each other (provided you haven't mismatched them when you create the object).
 - The `SummarizedExperiment` class is modular and extendable, and extensions exist for example for the analysis of single-cell RNA-seq data, i.e., the `SingleCellExperiment` class.
 - Due to their convenient organization and widely supported usage within Bioconductor, we will typically work with such classes in the analysis of RNA-seq data.

## Independent filtering

Independent filtering is a strategy to remove features (in this case, genes) prior to the analysis. Removal of these features may lower the multiple testing correction for other genes that pass the filter. We try to remove genes that have a low power to be found statistically significant, and/or that are biologically less relevant.
A common filtering strategy is to remove genes with a generally low expression, as low counts have lower relative uncertainty (hence lower statistical power), and may be considered biologically less relevant.

```r
suppressPackageStartupMessages({
  library(limma)
  library(edgeR)
})

keep <- rowSums(cpm(se) > 2) >= 3
table(keep)
se <- se[keep,]
```

## Data exploration

```r
# library size distribution
hist(colSums(assays(se)$counts)/1e6, breaks=10)
boxplot(colSums(assays(se)$counts)/1e6 ~ treatment)
boxplot(colSums(assays(se)$counts)/1e6 ~ time)
boxplot(colSums(assays(se)$counts)/1e6 ~ patient)
boxplot(colSums(assays(se)$counts)/1e6 ~ interaction(treatment, time))

# MDS plot
plotMDS(se,
        labels = treatment,
        col=as.numeric(patient))

## hard to see influence of experimental factors due to large between-patient variation
## we could also make an MDS plot per patient to take a look.
for(kk in 1:4){
  id <- which(patient == kk)
  plotMDS(se[,id],
        labels = paste0(treatment[id],"_",time[id]),
        col=as.numeric(time[id]))
}
```

```r
# Explain concept of MDS: preserve Euclidean distance from high to low dim.
```

Observations based on MDS plot:

 - There is a very large between-patient variability, which is the major source of variation in this dataset. The samples from each patient cluster together tightly.
 - Within patient, time consistently explains more variation than the treatments.
 - Relative to patients and time, the treatment seems to have a fairly small effect.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Challenge I: Choice of modeling assumptions →](03-challenge-i-choice-of-modeling-assumptions.md)
