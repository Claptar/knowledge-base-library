---
title: Preprocessing
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing_noframes.Rmd
source_file: sources/statomics-sga21/pda_quantification_preprocessing_noframes.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Preprocessing

**Source:** [`pda_quantification_preprocessing_noframes.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing_noframes.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Log-transformation

### Explore the data with plots

Peptide AALEELVK from spiked-in UPS protein P12081.
We only show data from lab1.

<details><summary> Click to see code to make plot </summary><p>
```r
subset <- pe["AALEELVK",colData(pe)$lab=="lab1"]
plotWhyLog <- data.frame(concentration = colData(subset)$spikeConcentration,
           y = assay(subset[["peptideRaw"]]) %>% c
           ) %>%
  ggplot(aes(concentration, y)) +
  geom_point() +
  xlab("concentration (fmol/l)") +
  ggtitle("peptide AALEELVK in lab1")
```
</p></details>

```r
plotWhyLog
```

- Variance increases with the mean
$\rightarrow$ Multiplicative error structure

<details><summary> Click to see code to make plot </summary><p>
```r
plotLog <- data.frame(concentration = colData(subset)$spikeConcentration,
           y = assay(subset[["peptideRaw"]]) %>% c
           ) %>%
  ggplot(aes(concentration, y)) +
  geom_point() +
  scale_x_continuous(trans='log2') +
  scale_y_continuous(trans='log2') +
  xlab("concentration (fmol/l)") +
  ggtitle("peptide AALEELVK in lab1 with axes on log scale")
```
</p></details>

```r
plotLog
```

- Data seems to be homoscedastic on log-scale $\rightarrow$ log transformation of the intensity data
- In quantitative proteomics analysis on $\log_2$

$\rightarrow$ Differences on a $\log_2$ scale: $\log_2$ fold changes

$$
\log_2 B - \log_2 A = \log_2 \frac{B}{A} = \log FC_\text{B - A}
$$
$$
\begin{array} {l}
log_2 FC = 1 \rightarrow FC = 2^1 =2\\
log_2 FC = 2 \rightarrow FC = 2^2 = 4\\
\end{array}
$$


### log-transformation of the data

<details><summary> Click to see code to log-transfrom the data </summary><p>
- We calculate how many non zero intensities we have for each peptide and this can be useful for filtering.

```r
rowData(pe[["peptideRaw"]])$nNonZero <- rowSums(assay(pe[["peptideRaw"]]) > 0)
```


- Peptides with zero intensities are missing peptides and should be represent
with a `NA` value rather than `0`.

```r
pe <- zeroIsNA(pe, "peptideRaw") # convert 0 to NA
```

- Logtransform data with base 2

```r
pe <- logTransform(pe, base = 2, i = "peptideRaw", name = "peptideLog")
```
</p></details>

---

## Filtering

- Reverse sequences
- Only identified by modification site (only modified peptides detected)
- Razor peptides: non-unique peptides assigned to the protein group with the most other peptides
- Contaminants
- Peptides few identifications
- Proteins that are only identified with one or a few peptides

Filtering does not induce bias if the criterion is independent from the downstream data analysis!

<details><summary> Click to see code to filter the data </summary><p>

1. Handling overlapping protein groups

In our approach a peptide can map to multiple proteins, as long as there is
none of these proteins present in a smaller subgroup.

```r
pe <- filterFeatures(pe, ~ Proteins %in% smallestUniqueGroups(rowData(pe[["peptideLog"]])$Proteins))
```

2. Remove reverse sequences (decoys) and contaminants

We now remove the contaminants, peptides that map to decoy sequences, and proteins
which were only identified by peptides with modifications.

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
</p></details>

---

## Normalization

<details><summary> Click to see code to make plot </summary><p>

```r
densityConditionD <- pe[["peptideLog"]][,colData(pe)$condition=="D"] %>%
  assay %>%
  as.data.frame() %>%
  gather(sample, intensity) %>%
  mutate(lab = colData(pe)[sample,"lab"]) %>%
  ggplot(aes(x=intensity,group=sample,color=lab)) +
    geom_density() +
    ggtitle("condition D")

densityLab2 <- pe[["peptideLog"]][,colData(pe)$lab=="lab2"] %>%
  assay %>%
  as.data.frame() %>%
  gather(sample, intensity) %>%
  mutate(condition = colData(pe)[sample,"condition"]) %>%
  ggplot(aes(x=intensity,group=sample,color=condition)) +
    geom_density() +
    ggtitle("lab2")
```
</p></details>

```r
densityConditionD
```

```r
densityLab2
```
- Even in very clean synthetic dataset (same background, only 48 UPS
proteins can be different) the marginal peptide intensity distribution
across samples can be quite distinct

- Considerable effects between and within labs for replicate samples
- Considerable effects between samples with different spike-in
concentration

$\rightarrow$ Normalization is needed

---


### Mean or median?

- Miller and Fishkin (1997) reported that over a period of 30 years males would like to have on average 64.3 partners and females 2.8.


<details><summary> </summary><p>
- Miller and Fishkin (1997) reported that the median number of partners someone would like to have over a period of 30 years males is 1 for both males and females.
</p></details>

<details><summary> </summary><p>
Mean is very sensitive to outliers!

```r
knitr::include_graphics("./figures/partners.png")
```
</p></details>


---

### Normalization of the data by median centering

$$y_{ip}^\text{norm} = y_{ip} - \hat\mu_i$$
with $\hat\mu_i$ the median intensity over all observed peptides in sample $i$.

<details><summary> Click to see R-code to normalize the data </summary><p>
```r
pe <- normalize(pe,
                i = "peptideLog",
                name = "peptideNorm",
                method = "center.median")
```
</p></details>

### Plots of normalized data


<details><summary> Click to see code to make plot </summary><p>
```r
densityConditionDNorm <- pe[["peptideNorm"]][,colData(pe)$condition=="D"] %>%
  assay %>%
  as.data.frame() %>%
  gather(sample, intensity) %>%
  mutate(lab = colData(pe)[sample,"lab"]) %>%
  ggplot(aes(x=intensity,group=sample,color=lab)) +
    geom_density() +
    ggtitle("condition D")

densityLab2Norm <- pe[["peptideNorm"]][,colData(pe)$lab=="lab2"] %>%
  assay %>%
  as.data.frame() %>%
  gather(sample, intensity) %>%
  mutate(condition = colData(pe)[sample,"condition"]) %>%
  ggplot(aes(x=intensity,group=sample,color=condition)) +
    geom_density() +
    ggtitle("lab2")
```
</p></details>

```r
densityConditionDNorm
```

```r
densityLab2Norm
```

- Upon normalization the marginal distributions of the peptide intensities across samples are much more comparable
- We still see deviations
- This can be due to technical variability
- In micro-array literature, quantile normalisation is used to force the median and all other quantiles to be equal across samples
- In proteomics quantile normalisation often introduces artifacts due to a difference in missing peptides across samples
- More advanced methods should be developed for normalizing proteomics data
- If there are differences in the width of the marginal distributions of the data across samples. They can also be standardized by using a robust estimator for location and scale, i.e.
$$y_{ip}^\text{norm} = \frac{y_{ip} - \mu_i}{s_i}$$

---

## Summarization

- We illustrate summarization issues using a subset of the cptac study (Lab 2, condition A and E) for a spiked protein (UPS P12081).

<details><summary> Click to see code to make plot </summary><p>
```r
summaryPlot <- pe[["peptideNorm"]][
    rowData(pe[["peptideNorm"]])$Proteins == "P12081ups|SYHC_HUMAN_UPS",
    colData(pe)$lab=="lab2"&colData(pe)$condition %in% c("A","E")] %>%
  assay %>%
  as.data.frame %>%
  rownames_to_column(var = "peptide") %>%
  gather(sample, intensity, -peptide) %>%
  mutate(condition = colData(pe)[sample,"condition"]) %>%
  ggplot(aes(x = peptide, y = intensity, color = sample, group = sample, label = condition), show.legend = FALSE) +
  geom_line(show.legend = FALSE) +
  geom_text(show.legend = FALSE) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1)) +
  xlab("Peptide") +
  ylab("Intensity (log2)")
```
</p></details>

```r
summaryPlot
```

We observe:

- intensities from multiple peptides for each protein in a sample
- Strong peptide effect
-Unbalanced peptide identification
- Pseudo-replication: peptide intensities from a particular protein in the same sample are correlated, i.e. they more alike than peptide intensities from a particular protein between samples.


$\rightarrow$ Summarize all peptide intensities from the same protein in a sample into a single protein expression value

Commonly used methods are

- Mean summarization
$$
y_{ip}=\beta_i^\text{samp} + \epsilon_{ip}
$$

- Median summarization
- Maxquant's maxLFQ summarization (in protein groups file)
- Model based summarization:
$$
y_{ip}=\beta_i^\text{samp} + \beta_p^\text{pep} + \epsilon_{ip}
$$


<details><summary> Click to see R-code to normalize the data </summary><p>
We use the standard sumarization in aggregateFeatures, which is
robust model based summarization.

```r
pe <- aggregateFeatures(pe,
    i = "peptideNorm",
    fcol = "Proteins",
    na.rm = TRUE,
    name = "protein")
```

Other summarization methods can be implemented by using the `fun` argument in the `aggregateFeatures` function.

- `fun = MsCoreUtils::medianPolish()` to fits an additive model (two way decomposition) using Tukey's median polish_ procedure using stats::medpolish()

- `fun = MsCoreUtils::robustSummary()` to calculate a robust aggregation using MASS::rlm() (default)

- `fun = base::colMeans()` to use the mean of each column

- `fun = matrixStats::colMedians()` to use the median of each column

- `fun = base::colSums()` to use the sum of each column

</p></details>

---

---

[← Import the data in R](03-import-the-data-in-r.md) · [Up: contents](index.md) · [Exercise →](05-exercise.md)
