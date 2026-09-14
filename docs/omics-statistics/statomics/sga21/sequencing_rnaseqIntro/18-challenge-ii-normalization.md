---
title: 'Challenge II: Normalization'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Challenge II: Normalization

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Normalization is necessary to correct for several sources of technical variation:

 - **Differences in sequencing depth** between samples. Some samples get sequenced deeper in the sense that they consist of more (mapped) reads and therefore can be considered to contain a higher amount of information, which we should be taking into account. In addition, if a sample is sequenced deeper, it is natural that the counts for each gene will be higher, jeopardizing a direct comparison of the expression counts.
 - **Differences in RNA population composition** between samples. As an extreme example, suppose that two samples have been sequenced to the exact same depth. One sample is contaminated and has a very high concentration of the contaminant cDNA being sequenced, but otherwise the two samples are identical. Since the contaminant will be taking up a significant proportion of the reads being sequenced, the counts will not be directly comparable between the samples. Hence, we may also want to correct for differences in the composition of the RNA population of the samples.
 - **Other technical variation** such as sample-specific GC-content or transcript length effects may also be accounted for.

 ---

Let's take a look at how comparable different replicates are in the Control condition at 48h in our dataset. We will investigate this using MD-plots (mean-difference plots as introduced by [Dudoit *et al.* (2002)](https://www.jstor.org/stable/24307038)), also sometimes referred to as MA-plots.

```r
cont48ID # relevant samples
colSums(assays(se)$counts[,cont48ID]) / 1e6
combs <- combn(cont48ID, m=2) #pairwise combinations between samples

par(mfrow=c(3,2), mar=c(4,4,2,1))
for(cc in 1:ncol(combs)){
  curSamples <- combs[,cc]
  M <- rowMeans(assays(se)$counts[,curSamples])
  D <- assays(se)$counts[,curSamples[2]] / assays(se)$counts[,curSamples[1]]
  plot(x = log(M), y = log2(D),
       pch = 16, cex=1/3,
       main = paste0("Sample ", curSamples[2], " vs sample ", curSamples[1]),
       xlab = "Log mean", ylab = "Log2 fold-change",
       bty = 'l')
  abline(h = 0, col="orange", lwd=2)
}
```

 - We see clear bias for some pairwise comparisons. For example, in the first plot comparing sample 8 versus sample 2, the log fold-changes are biased downwards. This means that, on average, a gene is lower expressed in sample 8 versus sample 2. Looking at the library sizes, we can indeed see that the library size for sample 2 is about $11 \times 10^6$ while it is only about $7 \times 10^6$ for sample 8! This is a clear library size effect that we should take into account.

## Count scaling versus GLM offsets

 - We have previously discussed count scaling transformations such as CPM and TPM.
 - A more appropriate and natural way when working with GLMs is through the use of **offsets**. The general use of an offset is to account for the 'effort' performed in order to gather that observation of the response variable. Two examples:
   1. A biologist studying whale migration has one fixed spot where, in the migration season, she counts migrating whales day after day, over several years. For each day she records the number of spotted whales. Of course, the time spent whale-watching may differ from day to day and it is natural that you are more likely to spot more whales if you spend more time looking for them. The time spent spotting whales can then be used as an offset.
   2. In our case, a sample being sequenced deeper contains more information, i.e., more 'effort' has been performed, as compared to a sample being sequenced relatively shallow. We have more confidence of a count from a deeply sequenced sample than from a shallowly sequenced sample. We can therefore use the sequencing depth $N_i = \sum_g Y_{gi}$ as offset in the model.
  - Adding an offset to the model is different from adding a new variable to the model. For each new variable we add, we will estimate its average effect $\beta$ on the response variable. When adding an offset, however, we are implicitly assuming that $\beta=1$.
  - Offsets are typically added on the scale of the linear predictor. Suppose we have a gene $g$ and sample $i$ specific offset $O_{gi}$, then we can define a negative binomial GLM including the offset as
  $$
  \left\{
  \begin{array}{ccc}
  Y_{gi} & \sim & NB(\mu_{gi}, \phi_g) \\
  \log \mu_{gi} & = & \eta_{gi} \\
  \eta_{gi} & = & \mathbf{X}^T_i \beta_g + \log(O_{gi}). \\
  \end{array}
  \right.
  $$
 - Please [read this page](https://statomics.github.io/SGA21/sequencing_scalingNormalization.html) for an intuitive reasoning as to why offsets are preferred over count scaling.

## How to normalize?

Many approaches are available for normalizing RNA-seq data, and we will review a couple of these. Most methods calculate an offset that is used in the GLM used to model gene expression. One notable method, full-quantile normalization, does not calculate an offset, and rather normalizes counts directly, immediately enforcing the same sequencing depth for all samples.

### TMM method (default of `edgeR`)

The trimmed mean of M-values (TMM) method introduced by [Robinson & Oshlack (2010)](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2010-11-3-r25) is a normalization procedure that calculates a single normalization factor for each sample. As the name suggests, it is based on a trimmed mean of fold-changes ($M$-values) as the scaling factor. A trimmed mean is an average after removing a set of 'extreme' values.
Specifically, TMM calculates a normalization factor $F_i^{(r)}$ across genes $g$ for each sample $i$ as compared to a reference sample $r$,
$$
\log_2(F_i^{(r)}) = \frac{\sum_{g \in {\cal G}^*} w_{gi}^r M_{gi}^r}{\sum_{g \in {\cal G}^*} w_{gi}^r},
$$
where $M_{gi}^r$ represents the $\log_2$-fold-change of the gene expression fraction as compared to a reference sample $r$, i.e.,
$$ M_{gi}^r = \log_2\left( \frac{Y_{gi} / N_i}{ Y_{gr} / N_r} \right), $$
and $w_{gi}^r$ represents a precision weight calculated as
$$
 w_{gi}^r = \frac{N_i - Y_{gi}}{N_i Y_{gi}} + \frac{N_r - Y_{gr}}{N_r Y_{gr}},
$$
and ${\cal G}^*$ represents the set of genes after trimming those with the most extreme average expression and fold-change. The weights serve to account for the fact that fold-changes for genes with lower read counts are more variable.

The procedure only takes genes into account where both $Y_{gi}>0$ and $Y_{gr}>0$. By default, TMM trims genes with the $30\%$ most extreme $M$-values and $5\%$ most extreme average gene expression, and chooses as reference $r$ the sample whose upper-quartile is closest to the across-sample average upper-quartile. The normalization factor is then used in conjunction with the library size to calculate an **effective library size**
$$
N_i^{eff} = N_i F_i^{(r)}
$$
which is used as offset in the GLM.
The normalized counts may be given by $\tilde{Y}_{gi} = Y_{gi} / N_i^s$, with size factor
$$N_i^s = \frac{N_i F_i^{(r)}}{\frac{1}{n}\sum_{i=1}^n N_i F_i^{(r)}}.$$

TMM normalization may be performed from the `calcNormFactors` function implemented in `edgeR`:

```r
dge <- edgeR::calcNormFactors(se)
dge$samples #normalization factors added to colData
```

Let's check how our MD-plots look like after normalization. Note that, we can rewrite the GLM as
$$ \log\left( \frac{\mu_{gi}}{N_i^s} \right) = \mathbf{X}_i^T \beta_g $$
and so $\frac{\mu_{gi}}{N_i^s}$ can be considered as an 'offset-corrected average count'.

We see that all MD-plots are now nicely centered around a log-fold-change of zero!

```r
## normalize
effLibSize <- dge$samples$lib.size * dge$samples$norm.factors
normCountTMM <- sweep(assays(se)$counts, 2, FUN="/", effLibSize)


par(mfrow=c(3,2), mar=c(4,4,2,1))
for(cc in 1:ncol(combs)){
  curSamples <- combs[,cc]
  M <- rowMeans(normCountTMM[,curSamples])
  D <- normCountTMM[,curSamples[2]] / normCountTMM[,curSamples[1]]
  plot(x = log(M), y = log2(D),
       pch = 16, cex=1/3,
       main = paste0("Sample ", curSamples[2], " vs sample ", curSamples[1]),
       xlab = "Log mean", ylab = "Log2 fold-change",
       bty = 'l')
  abline(h = 0, col="orange", lwd=2)
}
```


## Median-of-ratios method (default of `DESeq2`)

The median-of-ratios method is used in `DESeq2` as described in [Love *et al.* (2014)](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-014-0550-8).
It assumes that the expected value $\mu_{gi} = E(Y_{gi})$ is proportional to the true expression of the gene, $q_{gi}$, scaled by a size factor $s_{i}$ for each sample,
$$ \mu_{gi} = s_{i}q_{gi}. $$

The size factor $s_{i}$ is then estimated using the median-of-ratios method compared to a synthetic reference sample $r$ defined based on geometric means of counts across samples
$$
s_i = \text{median}_{\{{g:Y^{*}_{gr} \ne 0}\}} \frac{Y_{gi}}{Y^{*}_{gr}},
$$
with
$$ Y^{*}_{gr} = \left( \prod_{i=1}^n Y_{gi} \right)^{1/n}. $$

We can then use the size factors $s_i$ as offsets to the GLM.

**Question**. Do you see any issues with the procedure described as such?

<details><summary> Answer. </summary><p>
The procedure relies on genes being expressed in all samples.
As sample size increases, the number of genes with this property steadily decreases.
This will become crucial in single-cell RNA-seq data analysis.
</p></details>

Median-of-ratios normalization is implemented in the `DESeq2` package:

```r
dds <- DESeq2::DESeqDataSetFromMatrix(countData = assays(se)$counts,
                                      colData = colData(se),
                                      design = ~ 1) #just add intercept to showcase normalization
dds <- DESeq2::estimateSizeFactors(dds)
sizeFactors(dds)
```

You may also want to check out the [StatQuest video on DESeq2 normalization](https://www.youtube.com/watch?v=UFB993xufUU).

### Comparing TMM with DESeq2 normalization

We can compare the size factors for both normalizations to verify if they agree on the normalization factors. Note we need to scale the effective library sizes from `edgeR` to enforce a similar scale as the size factors from `DESeq2`. While below we are using an arithmetic mean, a geometric mean may be used as well, which will be more robust to outlying effective library sizes.

```r
plot(effLibSize / mean(effLibSize), sizeFactors(dds),
     xlab = "edgeR size factor",
     ylab = "DESeq2 size factor")
```


## Full-quantile (FQ) normalization

In full-quantile normalization, originally introduced in the context of microarrays by [Bolstad *et al.* (2003)](https://academic.oup.com/bioinformatics/article/19/2/185/372664), the samples are forced to each have a distribution identical to the distribution of the median/average of the quantiles across samples.
In practice, we can implement full-quantile normalization using the following procedure

 1. Given a data matrix $\mathbf{Y}_{G \times n}$ for $G$ genes (rows) and $n$ samples (columns),
 2. sort each column to get $\mathbf{Y}^S$,
 3. replace all elements of each row by the median (or average) for that row,
 4. obtain the normalized counts $\tilde{\mathbf{Y}}$ by re-arranging (i.e., unsorting) each column.

## Uncertainty in normalization

 - The offsets that are being cacluated for normalization purposes are estimates.
 - The downstream analyses incorporates these estimates as if they are known, i.e., conditions on the estimates.
 - The analysis therefore **ignores the uncertainty** in their estimation.

```r

---

[← note phi = 1 / size](17-note-phi-1-size.md) · [Up: contents](index.md) · [All defaults →](19-all-defaults.md)
