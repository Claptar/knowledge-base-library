---
title: Full CPTAC study
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_robustSummarisation_peptideModels.Rmd
source_file: sources/statomics-sga21/pda_robustSummarisation_peptideModels.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Full CPTAC study

**Source:** [`pda_robustSummarisation_peptideModels.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_robustSummarisation_peptideModels.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Read data

<details><summary> Click to see background and code </summary><p>
1. We use a peptides.txt file from MS-data quantified with maxquant that
contains MS1 intensities summarized at the peptide level.
```r
peptidesFile <- "https://raw.githubusercontent.com/statOmics/PDA21/data/quantification/fullCptacDatasSetNotForTutorial/peptides.txt"
```

2. Maxquant stores the intensity data for the different samples in columnns that start with Intensity. We can retreive the column names with the intensity data with the code below:

```r
ecols <- grep("Intensity\\.", names(read.delim(peptidesFile)))
```

3. Read the data and store it in  QFeatures object

```r
pe <- readQFeatures(
  table = peptidesFile,
  fnames = 1,
  ecol = ecols,
  name = "peptideRaw", sep="\t")
```
</p></details>

## Design

<details><summary> Click to see background and code </summary><p>

```r
pe %>% colnames
```

- Note, that the sample names include the spike-in condition.
- They also end on a number.

  - 1-3 is from lab 1,
  - 4-6 from lab 2 and
  - 7-9 from lab 3.

- We update the colData with information on the design

```r
colData(pe)$lab <- rep(rep(paste0("lab",1:3),each=3),5) %>% as.factor
colData(pe)$condition <- pe[["peptideRaw"]] %>% colnames %>% substr(12,12) %>% as.factor
colData(pe)$spikeConcentration <- rep(c(A = 0.25, B = 0.74, C = 2.22, D = 6.67, E = 20),each = 9)
```

- We explore the colData

```r
colData(pe)
```

</p></details>

## Preprocessing

### Log-transform

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


### Filtering

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

## Normalization

<details><summary> Click to see R-code to normalize the data </summary><p>
```r
pe <- normalize(pe,
                i = "peptideLog",
                name = "peptideNorm",
                method = "center.median")
```
</p></details>

---

---

[← Subset of CPTAC study: A vs B comparison in lab 3](02-subset-of-cptac-study-a-vs-b-comparison-in-lab-3.md) · [Up: contents](index.md) · [Peptide-level models →](04-peptide-level-models.md)
