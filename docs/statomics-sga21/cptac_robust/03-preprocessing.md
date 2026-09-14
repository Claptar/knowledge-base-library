---
title: Preprocessing
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust.Rmd
source_file: sources/statomics-sga21/cptac_robust.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Preprocessing

**Source:** [`cptac_robust.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

This section preforms preprocessing for the peptide data.
This include

- log transformation,
- filtering and
- summarisation of the data.

## Log transform the data

```r
pe <- logTransform(pe, base = 2, i = "peptideRaw", name = "peptideLog")
```

## Filtering

1. Handling overlapping protein groups

In our approach a peptide can map to multiple proteins, as long as there is
none of these proteins present in a smaller subgroup.

```r
pe <- filterFeatures(pe, ~ Proteins %in% smallestUniqueGroups(rowData(pe[["peptideLog"]])$Proteins))
```

2. Remove reverse sequences (decoys) and contaminants

We now remove the contaminants and peptides that map to decoy sequences.

```r
pe <- filterFeatures(pe,~Reverse != "+")
pe <- filterFeatures(pe,~ Potential.contaminant != "+")
```

3. Drop peptides that were only identified in one sample

We keep peptides that were observed at last twice.

```r
pe <- filterFeatures(pe,~ nNonZero >=2)
nrow(pe[["peptideLog"]])
```

We keep `r nrow(pe[["peptideLog"]])` peptides upon filtering.


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
  mutate(condition = colData(pe)[sample,"condition"]) %>%
  ggplot(aes(x = intensity,group = sample,color = condition)) +
    geom_density()
```

We can visualize our data using a Multi Dimensional Scaling plot,
eg. as provided by the `limma` package.

```r
pe[["peptideNorm"]] %>%
  assay %>%
  limma::plotMDS(col = as.numeric(colData(pe)$condition))
```

The first axis in the plot is showing the leading log fold changes
(differences on the log scale) between the samples.

We notice that the leading differences (log FC)
in the peptide data seems to be driven by technical variability.
Indeed, the samples do not seem to be clearly separated according
to the spike-in condition.


## Summarization to protein level

- By default robust summarization is used:  `fun = MsCoreUtils::robustSummary()`

```r
pe <- aggregateFeatures(pe,
  i = "peptideNorm",
  fcol = "Proteins",
  na.rm = TRUE,
  name = "protein")
```


```r
plotMDS(assay(pe[["protein"]]), col = as.numeric(colData(pe)$condition))
```

Note that the samples upon robust summarisation show a clear separation according to the spike-in condition in the second dimension of the MDS plot.

---

[← Data](02-data.md) · [Up: contents](index.md) · [Data Analysis →](04-data-analysis.md)
