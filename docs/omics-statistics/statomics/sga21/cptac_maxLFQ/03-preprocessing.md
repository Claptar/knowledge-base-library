---
title: Preprocessing
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_maxLFQ.Rmd
source_file: sources/statomics-sga21/cptac_maxLFQ.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Preprocessing

**Source:** [`cptac_maxLFQ.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_maxLFQ.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

This section preforms preprocessing for the peptide data.
This include

- log transformation,
- filtering

## Log transform the data

```r
pe <- logTransform(pe, base = 2, i = "proteinRaw", name = "proteinLog")
```

## Filtering

1. Remove reverse sequences (decoys) and contaminants

We now remove the contaminants and proteins that map to decoys.

```r
pe <- filterFeatures(pe,~ Reverse != "+")
pe <- filterFeatures(pe,~ Potential.contaminant != "+")
```

We keep `r nrow(pe[["proteinLog"]])` peptides upon filtering.


## Normalize the data using median centering

We normalize the data by substracting the sample median from every intensity for peptide $p$  in a sample $i$:

$$y_{ip}^\text{norm} = y_{ip} - \hat\mu_i$$

with $\hat\mu_i$ the median intensity over all observed peptides in sample $i$.

```r
pe <- normalize(pe,
                i = "proteinLog",
                name = "protein",
                method = "center.median")
```


## Explore  normalized data

Upon the normalisation the density curves are nicely registered

```r
pe[["protein"]] %>%
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
pe[["protein"]] %>%
  assay %>%
  limma::plotMDS(col = as.numeric(colData(pe)$condition))
```

Note that the samples show a clear separation according to the spike-in condition in the second dimension of the MDS plot.

---

[← Data](02-data.md) · [Up: contents](index.md) · [Data Analysis →](04-data-analysis.md)
