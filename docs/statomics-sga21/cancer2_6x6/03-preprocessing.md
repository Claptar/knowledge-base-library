---
title: Preprocessing
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cancer2_6x6.Rmd
source_file: sources/statomics-sga21/cancer2_6x6.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Preprocessing

**Source:** [`cancer2_6x6.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cancer2_6x6.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

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

```r
pe <- filterFeatures(pe,~Reverse != "+")
pe <- filterFeatures(pe,~ Contaminant != "+")
```

### Remove peptides of proteins that were only identified with modified peptides

I will skip this step for the moment. Large protein groups file needed for this.

### Drop peptides that were only identified in one sample

We keep peptides that were observed at last twice.

```r
pe <- filterFeatures(pe,~nNonZero >= 2)
nrow(pe[["peptideLog"]])
```

We keep `r nrow(pe[["peptideLog"]])` peptides after filtering.

## Normalize the data using median centering

We normalize the data by substracting the sample median from every intensity for peptide $p$  in a sample $i$:

$$y_{ip}^\text{norm} = y_{ip} - \hat\mu_i$$

with $\hat\mu_i$ the median intensity over all observed peptides in sample $i$.

```r
pe <- normalize(pe,
                i = "peptideLog",
                name = "peptideNorm",
                method = "center.median")
```


## Explore  normalized data

Upon the normalisation the density curves are nicely registered

```r
pe[["peptideNorm"]] %>%
  assay %>%
  as.data.frame() %>%
  gather(sample, intensity) %>%
  mutate(condition = colData(pe)[sample,"outcome"]) %>%
  ggplot(aes(x = intensity,group = sample,color = condition)) +
    geom_density()
```


We can visualize our data using a Multi Dimensional Scaling plot,
eg. as provided by the `limma` package.

```r
limma::plotMDS(assay(pe[["peptideNorm"]]), col = as.numeric(colData(pe)$outcome))
```

The first axis in the plot is showing the leading log fold changes
(differences on the log scale) between the samples.


## Summarization to protein level

We use robust summarization in aggregateFeatures. This is the default workflow of aggregateFeatures so you do not have to specifiy the argument `fun`.


```r
pe <- aggregateFeatures(pe,
 i = "peptideNorm",
 fcol = "Proteins",
 na.rm = TRUE,
 name = "proteinRobust")
```

```r
plotMDS(assay(pe[["proteinRobust"]]), col = as.numeric(colData(pe)$outcome))
```

---

[← Data](02-data.md) · [Up: contents](index.md) · [Data Analysis →](04-data-analysis.md)
