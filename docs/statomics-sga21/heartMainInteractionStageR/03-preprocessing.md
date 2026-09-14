---
title: Preprocessing
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/heartMainInteractionStageR.Rmd
source_file: sources/statomics-sga21/heartMainInteractionStageR.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Preprocessing

**Source:** [`heartMainInteractionStageR.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/heartMainInteractionStageR.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

This section preforms standard preprocessing for the peptide data. This
include log transformation, filtering and summarisation of the data.

## Log transform the data

```r
pe <- logTransform(pe, base = 2, i = "peptideRaw", name = "peptideLog")
limma::plotDensities(assay(pe[["peptideLog"]]))
```


## Filtering

### Handling overlapping protein groups
In our approach a peptide can map to multiple proteins, as long as there is
none of these proteins present in a smaller subgroup.

```r
pe <- filterFeatures(pe, ~ Proteins %in% smallestUniqueGroups(rowData(pe[["peptideLog"]])$Proteins))
```

### Remove reverse sequences (decoys) and contaminants

We now remove the contaminants, peptides that map to decoy sequences, and proteins
which were only identified by peptides with modifications.

First look to the names of the variables for the peptide features
```r
pe[["peptideLog"]] %>%
  rowData %>%
  names
```

No information on decoys.

```r
pe <- filterFeatures(pe,~ Potential.contaminant != "+")
```


### Drop peptides that were only identified in one sample

We keep peptides that were observed at last twice.

```r
pe <- filterFeatures(pe,~nNonZero >= 2)
nrow(pe[["peptideLog"]])
```

We keep `r nrow(pe[["peptideLog"]])` peptides after filtering.

## Normalize the data
```r
pe <- normalize(pe,
                i = "peptideLog",
                name = "peptideNorm",
                method = "center.median")
```


## Explore normalized data

After  normalisation the density curves for all samples are comparable.

```r
limma::plotDensities(assay(pe[["peptideNorm"]]))
```

This is more clearly seen is a boxplot.

```r
boxplot(assay(pe[["peptideNorm"]]), col = palette()[-1],
       main = "Peptide distribtutions after normalisation", ylab = "intensity")
```


We can visualize our data using a Multi Dimensional Scaling plot,
eg. as provided by the `limma` package.

```r
limma::plotMDS(assay(pe[["peptideNorm"]]),
  col = colData(pe)$location:colData(pe)$tissue %>%
    as.numeric,
  labels = colData(pe) %>%
    rownames %>%
    substr(start = 11, stop = 13)
  )
```

The first axis in the plot is showing the leading log fold changes
(differences on the log scale) between the samples.


## Summarization to protein level

We use robust summarization in aggregateFeatures. This is the default workflow of aggregateFeatures so you do not have to specifiy the argument `fun`.
However, because we compare methods we have included the `fun` argument to show the summarization method explicitely.

```r
pe <- aggregateFeatures(pe,
 i = "peptideNorm",
 fcol = "Proteins",
 na.rm = TRUE,
 name = "proteinRobust",
 fun = MsCoreUtils::robustSummary)
```

```r
plotMDS(assay(pe[["proteinRobust"]]),
  col = colData(pe)$location:colData(pe)$tissue %>%
    as.numeric,
  labels = colData(pe) %>%
    rownames %>%
    substr(start = 11, stop = 13)
)
```

---

[← Data](02-data.md) · [Up: contents](index.md) · [Data Analysis →](04-data-analysis.md)
