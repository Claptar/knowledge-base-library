---
title: "18. Import Data and Preprocessing"
course: "StatOmics Sga21"
chapter: 18
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 18. Import Data and Preprocessing

## What this covers

A quantitative proteomics experiment does not arrive as a clean table of protein abundances: it
arrives as a peptide-by-sample intensity matrix straight out of the search engine (here, MaxQuant),
full of zeros, ambiguous peptide-to-protein assignments, decoy hits and contaminants. This chapter
follows the R pipeline that turns that raw table into a per-protein matrix fit for a linear model,
using a real dataset — intensities for two T-cell subtypes (Treg and Tconv) from a set of mice — and
ends with the model fits and contrasts that the next chapter uses to compare designs. It assumes you
know, at least loosely, what a peptide and a protein group are, that MaxQuant-style output has one
intensity column per sample, and what a linear model formula such as `~ celltype + mouse` specifies.

## Three copies of the same comparison

The pipeline is run three times, on three peptide tables, because the point of the exercise is to
compare designs rather than to analyse one dataset:

- **`peptides.txt`** — the original quantification, seven mice, labelled *"Original (RCB)"* in the
  plots below.
- **`peptidesRCB.txt`** — a four-mouse **randomized complete block** subset: every mouse contributes
  both a Treg and a Tconv sample, so mouse and cell type are crossed and each mouse is its own block.
- **`peptidesCRD.txt`** — an eight-mouse **completely randomized design**: every mouse contributes
  only one of the two cell types, so there is no pairing to exploit.

Each table is read into a `QFeatures` object (`readQFeatures`), which stores the peptide intensities
alongside the sample metadata. The metadata itself is not supplied separately — it is read straight
off the sample names. The columns holding intensities are found by matching `"Intensity."` in the
header, and for every one of the three datasets the same two lines recover the design:

```r
colData(pe)$celltype <- substr(colnames(pe[["peptideRaw"]]), 11, 14) %>% unlist %>% as.factor
colData(pe)$mouse    <- pe[[1]] %>% colnames %>% strsplit(split="[.]") %>%
  sapply(function(x) x[3]) %>% as.factor
```

Cell type is a fixed substring of the column name; the mouse identifier is the third field once the
name is split on its dots. This is worth noticing precisely because it is unglamorous: before any
statistics happens, the experimental design has to be parsed correctly out of whatever naming
convention the instrument software produced.

## From raw intensities to something a model can use

Three things happen to the raw peptide intensities before anything else is asked of them.

**Counting how many samples see each peptide.** `rowSums(assay(...) > 0)` is stored as `nNonZero`
for every peptide. This is not used yet — it is computed here so it is available for the filtering
step below.

**Zero is not a measurement of zero.** In this kind of intensity data a `0` does not mean "the
peptide was present at zero abundance"; it means the peptide was not detected in that run at all —
a missing value, for reasons that have nothing to do with its true abundance (below the instrument's
detection limit, a run that happened to miss it, and so on). Leaving it as `0` would tell a linear
model that the peptide's abundance really was zero, which is a much stronger and generally false
claim. `zeroIsNA()` converts every `0` to `NA` so that the peptide is correctly recorded as *not
observed* rather than *observed at zero*.

**Log-transforming.** `logTransform(pe, base = 2, i = "peptideRaw", name = "peptideLog")` puts every
remaining intensity on a log2 scale. Intensity data of this kind is right-skewed, and differences
that matter biologically are naturally multiplicative (a two-fold change) rather than additive — the
log scale turns fold-changes into differences, which is what the additive model formulas used later
(`~ celltype + mouse`) are built to compare.

## Filtering: removing peptides that cannot be trusted or cannot be compared

Three filters run in sequence, each removing a different kind of unusable peptide.

1. **Ambiguous protein assignment.** A peptide sequence can belong to more than one protein group
   (isoforms, paralogues sharing an exon). The rule applied here keeps a peptide only if its protein
   group is the *smallest* one consistent with the evidence — a peptide is kept as evidence for a
   larger, less specific group only if none of the proteins in that group also appear in some
   smaller subgroup:

   ```r
   pe <- filterFeatures(pe, ~ Proteins %in% smallestUniqueGroups(rowData(pe[["peptideLog"]])$Proteins))
   ```

2. **Decoys and contaminants.** A database search estimates its own false-discovery rate by also
   searching a reversed ("decoy") version of the protein database; any peptide that matched a decoy
   is a known false hit and must be dropped, along with peptides flagged as laboratory contaminants
   (common background proteins that do not belong to the biological sample):

   ```r
   pe <- filterFeatures(pe, ~ Reverse != "+")
   pe <- filterFeatures(pe, ~ Potential.contaminant != "+")
   ```

3. **Peptides seen only once.** Using the `nNonZero` count computed earlier, any peptide observed in
   fewer than two samples is dropped (`filterFeatures(pe, ~ nNonZero >= 2)`). A single observation
   carries no information about how variable a peptide's measurement is, so it cannot contribute to
   a comparison between groups.

## Normalization: median centering

```r
pe <- normalize(pe, i = "peptideLog", name = "peptideNorm", method = "center.median")
```

Each sample's log2 intensities are shifted so that the sample's median is the same across all
samples. This corrects for overall differences between runs — how much material was loaded, how
efficiently a given run ionised peptides — that shift every intensity in a sample up or down together
and have nothing to do with the biology being compared.

## Summarization: from peptides to proteins

```r
pe <- aggregateFeatures(pe, i = "peptideNorm", fcol = "Proteins", na.rm = TRUE, name = "protein")
```

The normalized, log-scale peptide intensities that share a `Proteins` group are combined into a
single per-protein value, ignoring missing peptide values (`na.rm = TRUE`). This is the matrix the
rest of the analysis works with: one log2 abundance per protein per sample.

## What the design costs you if you ignore it

Before fitting anything, an MDS plot of the protein matrix is made for each of the three datasets,
plotting samples in two dimensions so that the distance between two points reflects how different
their protein profiles are, and connecting each mouse's two samples with a dashed line.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="MDS plot showing mouse identity dominating the first axis and cell type separating consistently along the second">
  <line x1="30" y1="190" x2="345" y2="190" stroke="currentColor" stroke-width="1.2"/>
  <line x1="30" y1="20" x2="30" y2="190" stroke="currentColor" stroke-width="1.2"/>
  <text x="187" y="210" text-anchor="middle" font-size="12" fill="currentColor">MDS 1 — separates mice</text>
  <text x="18" y="105" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 18 105)">MDS 2 — cell type</text>

  <!-- mouse 1 -->
  <line x1="62" y1="123" x2="78" y2="153" stroke="tomato" stroke-width="1.2" stroke-dasharray="3 3"/>
  <circle cx="62" cy="123" r="5" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <circle cx="78" cy="153" r="5" fill="currentColor" fill-opacity="0.35" stroke="currentColor"/>

  <!-- mouse 2 -->
  <line x1="142" y1="96" x2="158" y2="126" stroke="tomato" stroke-width="1.2" stroke-dasharray="3 3"/>
  <circle cx="142" cy="96" r="5" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <circle cx="158" cy="126" r="5" fill="currentColor" fill-opacity="0.35" stroke="currentColor"/>

  <!-- mouse 3 -->
  <line x1="222" y1="132" x2="238" y2="162" stroke="tomato" stroke-width="1.2" stroke-dasharray="3 3"/>
  <circle cx="222" cy="132" r="5" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <circle cx="238" cy="162" r="5" fill="currentColor" fill-opacity="0.35" stroke="currentColor"/>

  <!-- mouse 4 -->
  <line x1="298" y1="106" x2="314" y2="136" stroke="tomato" stroke-width="1.2" stroke-dasharray="3 3"/>
  <circle cx="298" cy="106" r="5" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <circle cx="314" cy="136" r="5" fill="currentColor" fill-opacity="0.35" stroke="currentColor"/>

  <circle cx="55" cy="35" r="4" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <text x="65" y="39" font-size="11" fill="currentColor">Treg</text>
  <circle cx="115" cy="35" r="4" fill="currentColor" fill-opacity="0.35" stroke="currentColor"/>
  <text x="125" y="39" font-size="11" fill="currentColor">Tconv</text>
</svg>
<figcaption>Each dashed line joins one mouse's two samples. The four mice sit far apart along the
first axis — mouse identity is the largest source of variation — while within every pair the Treg
sample sits a consistent distance below its Tconv partner along the second axis, the cell-type
signal that a design blocked on mouse can isolate.</figcaption>
</figure>

Concretely: the leading fold change in the data is explained by which mouse a sample came from, not
by cell type; the cell-type separation only shows up as a smaller, second-order effect. A randomized
complete block design — where the same mouse supplies both cell types — makes it possible to remove
the mouse effect from the analysis, because it can be modelled and subtracted out; a completely
randomized design, where each mouse supplies only one cell type, has no such handle on it.

## Fitting the model and setting up the comparison

The protein-level matrix is handed to `msqrob()`, which fits, for every protein, a linear model of
log2 protein intensity against the terms named in a formula. Three fits are made, matching the three
comparisons the next chapter draws on:

```r
# RCB, modelled correctly: block on mouse
pe <- msqrob(object = pe, i = "protein", formula = ~ celltype + mouse)

# the same RCB data, modelled as if it hadn't been blocked
pe <- msqrob(object = pe, i = "protein", formula = ~ celltype,
             modelColumnName = "wrongModel")

# CRD data: no blocking to add, because there's no pairing to exploit
pe2 <- msqrob(object = pe2, i = "protein", formula = ~ celltype)
```

The middle fit is deliberately labelled `wrongModel`: it re-analyses the *same* blocked data as the
first fit, but drops the `mouse` term, which is the wrong analysis for data that was collected in
pairs. `VisualizeDesign()` (from the `ExploreModelMatrix` package) is used to display the two design
matrices for `~ celltype + mouse` and `~ celltype` side by side, making concrete what adding `+ mouse`
does to the model: one extra column per mouse, there specifically to absorb mouse-to-mouse variation
before the cell-type term is tested.

Finally, the same contrast is tested against all three fits, so that the correct RCB model, the
wrong RCB model and the CRD model can be compared directly:

```r
L <- makeContrast("celltypeTreg = 0", parameterNames = c("celltypeTreg"))
pe  <- hypothesisTest(object = pe,  i = "protein", contrast = L)
pe  <- hypothesisTest(object = pe,  i = "protein", contrast = L,
                       modelColumn = "wrongModel", resultsColumnNamePrefix = "wrong")
pe2 <- hypothesisTest(object = pe2, i = "protein", contrast = L)
```

The contrast asks, for every protein, whether the estimated Treg-versus-Tconv effect is zero. What
each of the three test results actually looks like — and whether blocking correctly changes the
answer — is the subject of the next chapter.

## Sources

- `docs/omics-statistics/statomics/sga21/pda_blocking_wrapup/01-import-data-and-preprocessing.md`
  (converted from `pda_blocking_wrapup.Rmd`, statOmics SGA21 course, CC BY-NC-SA 4.0) — the sole
  input for this chapter; all code, comments and figure titles quoted or paraphrased above come from
  it. No slide deck, transcript or problem set was supplied alongside it.
- The source page itself links onward to "Advantage of Blocking: comparison between designs," which
  works out the consequence of the correct-versus-wrong and RCB-versus-CRD fits set up here; that
  page was not part of the material supplied for this chapter.

---

[← 17. Multiple Regression with Interactions](17-multiple-regression-with-interactions.md) · [Contents](index.md) · [19. Differential Abundance Testing and Design →](19-differential-abundance-testing-and-design.md)
