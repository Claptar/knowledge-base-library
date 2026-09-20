---
title: "8. Interaction Effects and Stage-wise Testing"
course: "StatOmics Sga21"
chapter: 8
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 8. Interaction Effects and Stage-wise Testing

## What this covers

A single worked case study — comparing the proteome of the four chambers of the heart in three
patients — used to answer three questions that come up whenever a design crosses two factors:
how do you write down the effect of interest as a *contrast* of model parameters, why do some
contrasts of the same model come out far more powerful than others, and how can you test more
hypotheses than a flat correction would allow without inflating the false discovery rate. It
assumes the standard proteomics quantification pipeline (`QFeatures`, peptide-to-protein
aggregation) and robust linear modelling with `msqrob2`, together with the basic ideas of a
design matrix, a linear contrast, and Benjamini–Hochberg/Holm-style multiple testing correction.

## The case study and its design

Researchers quantified the proteome of the left atrium (LA), right atrium (RA), left ventricle
(LV) and right ventricle (RV) of the heart, in three patients (a subset of the public dataset
PXD006675 on PRIDE). Every sample therefore carries three labels: which **location** (left or
right), which **tissue** (atrium or ventricle), and which **patient** it came from.

Location and tissue are *crossed*: every combination (LA, LV, RA, RV) is observed, in every
patient. That crossing is what makes an *interaction* askable at all, and it is the reason this
design supports four distinct scientific questions rather than one:

- how does the ventricle differ from the atrium **on the left** side,
- how does the ventricle differ from the atrium **on the right** side,
- how do they differ **on average**, pooling left and right,
- and does that ventricle-vs-atrium difference **itself differ** between left and right — the
  interaction.

<figure>
<svg viewBox="0 0 460 240" role="img" aria-label="Two-by-two design of location and tissue, with the left and right ventricle-versus-atrium contrasts drawn as arrows">
  <defs>
    <marker id="arrowhead" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <polygon points="0,0 10,5 0,10" fill="currentColor"/>
    </marker>
  </defs>

  <text x="95" y="24" text-anchor="middle" font-size="12" fill="currentColor">Atrium</text>
  <text x="295" y="24" text-anchor="middle" font-size="12" fill="currentColor">Ventricle</text>

  <text x="15" y="76" font-size="12" fill="currentColor">Left</text>
  <rect x="55" y="55" width="80" height="34" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="255" y="55" width="80" height="34" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <line x1="140" y1="72" x2="248" y2="72" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <text x="195" y="64" text-anchor="middle" font-size="11" fill="currentColor">FC(V-A) left</text>

  <text x="10" y="186" font-size="12" fill="currentColor">Right</text>
  <rect x="55" y="165" width="80" height="34" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="255" y="165" width="80" height="34" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <line x1="140" y1="182" x2="248" y2="182" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <text x="195" y="174" text-anchor="middle" font-size="11" fill="currentColor">FC(V-A) right</text>

  <line x1="380" y1="72" x2="380" y2="182" stroke="currentColor" stroke-width="1.5"/>
  <line x1="373" y1="72" x2="380" y2="72" stroke="currentColor" stroke-width="1.5"/>
  <line x1="373" y1="182" x2="380" y2="182" stroke="currentColor" stroke-width="1.5"/>
  <text x="388" y="122" font-size="11" fill="currentColor">right</text>
  <text x="388" y="136" font-size="11" fill="currentColor">minus</text>
  <text x="388" y="150" font-size="11" fill="currentColor">left</text>
</svg>
<figcaption>The location-by-tissue design. Each row gives one ventricle-versus-atrium arrow; the
average contrast combines both arrows (using every sample), and the interaction contrast is the
difference between them.</figcaption>
</figure>

## From peptides to protein-level intensities

The raw input is a MaxQuant `peptides.txt` file — peptide-level intensities, one column per
sample. It is read into a `QFeatures` object, and the sample metadata (location, tissue, patient)
is recovered directly from the intensity column names:

```r
pe <- readQFeatures(table = peptidesFile, fnames = 1, ecol = ecols,
                     name = "peptideRaw", sep = "\t")

colData(pe)$location <- substr(colnames(pe[["peptideRaw"]]), 11, 11) %>% as.factor
colData(pe)$tissue   <- substr(colnames(pe[["peptideRaw"]]), 12, 12) %>% as.factor
colData(pe)$patient  <- substr(colnames(pe[["peptideRaw"]]), 13, 13) %>% as.factor
```

A peptide with intensity zero was not observed at a very low level — it was not measured — so
before anything else the zeros are recoded as missing rather than as data: `pe <- zeroIsNA(pe,
"peptideRaw")`.

Standard preprocessing follows, each step justified by what would otherwise contaminate the
model:

- **Log-transform** the raw intensities (`logTransform`, base 2), since intensity noise scales
  with intensity and the model works on an additive, symmetric scale.
- **Collapse to the smallest unique protein groups.** A peptide can map to several proteins; it is
  kept against a protein group only if no subset of that group already explains it, so shared
  peptides are not double-counted.
- **Drop contaminants** (and, in another dataset, decoy hits) — features that are not the biology
  being measured.
- **Drop peptides seen in fewer than two samples.** A peptide observed once contributes no
  within-peptide information and is pure noise for the purpose of fitting a model.
- **Normalize by median-centering** each sample. Before normalization the per-sample intensity
  distributions sit at different heights; after it they line up, which is what makes samples
  comparable at all. A multidimensional scaling (MDS) plot — whose first axis shows the leading
  log-fold-changes between samples — is used to check that samples still cluster by location and
  tissue rather than by some technical artefact.
- **Aggregate peptides to proteins** with a *robust* summary (`aggregateFeatures(..., fun =
  MsCoreUtils::robustSummary)`) rather than, say, a plain mean, because a handful of aberrant
  peptides within a protein should not be allowed to drag the protein-level intensity with them.

## Modelling and the four contrasts

Each protein gets its own robust linear model, fit by `msqrob`, with location and tissue crossed
and patient entered as a blocking factor:

```r
pe <- msqrob(object = pe, i = "proteinRobust", formula = ~ location*tissue + patient)
```

With atrium (A) and left (L) as the reference levels, the model's `tissue` and interaction terms
carry exactly the four biological questions above, once combined the right way. Write
$\beta_{V}$ for the ventricle-vs-atrium effect *at the reference location* (left) and
$\beta_{RV}$ for the extra shift the interaction contributes when the location is right. Then

$$
\log_2 FC_{V-A}^{L} = \beta_V, \qquad
\log_2 FC_{V-A}^{R} = \beta_V + \beta_{RV},
$$
$$
\log_2 FC_{V-A} \;(\text{average}) = \tfrac12\!\left(\log_2 FC_{V-A}^{L} + \log_2 FC_{V-A}^{R}\right) = \beta_V + \tfrac12\beta_{RV},
$$
$$
\text{interaction} = \log_2 FC_{V-A}^{R} - \log_2 FC_{V-A}^{L} = \beta_{RV}.
$$

These four linear combinations are exactly the rows of the contrast matrix built with
`makeContrast`:

```r
L <- makeContrast(
  c("tissueV = 0",
    "tissueV + locationR:tissueV = 0",
    "tissueV + 0.5*locationR:tissueV = 0",
    "locationR:tissueV = 0"),
  parameterNames = colnames(design))

pe <- hypothesisTest(object = pe, i = "proteinRobust", contrast = L, overwrite = TRUE)
```

Each contrast is then evaluated the same way for every protein: a volcano plot (log-fold-change
against $-\log_{10}$ p-value, coloured by whether the 5%-FDR-adjusted p-value is significant), a
heatmap of the proteins declared significant, and a ranked table of those proteins.

## Why the contrasts don't have equal power

Running the four contrasts side by side on this dataset gives a strikingly uneven picture: far
more proteins are called significant for the **average** contrast than for either the left-only
or the right-only contrast, and **none** are significant for the interaction. That is not a
biological finding by itself — it is a consequence of how much information each contrast draws
on, and it is visible directly in the design matix, before looking at any protein's data.

For a contrast vector $L$ against design matrix $X$, ordinary least-squares theory gives

$$
\mathrm{Var}(L^\top\hat\beta) = \sigma^2\, L^\top (X^\top X)^{-1} L .
$$

Because location and tissue are fully crossed and balanced, the left-only and right-only
ventricle-vs-atrium contrasts are built from disjoint halves of the samples and turn out to have
*equal* variance, call it $v$, computed directly from `t(L) %*% solve(t(X) %*% X) %*% L` in R.
Treating them as two independent estimates of comparable but distinct quantities:

- the **average** contrast is their mean, $\tfrac12(\text{left}+\text{right})$, so its variance is
  $\tfrac14(v+v) = v/2$ — a standard error smaller by a factor of $1/\sqrt2$;
- the **interaction** contrast is their difference, $\text{right}-\text{left}$, so its variance is
  $v+v=2v$ — a standard error *larger* by a factor of $\sqrt2$.

Both ratios were checked numerically against the design matrix (`varContrasts[3]/varContrasts[2]
== 1/2`, `varContrasts[4]/varContrasts[2] == 2`). The mechanism is simply that the average
contrast is estimated from twice as many samples as either one-sided contrast, while the
interaction is a difference of two noisy quantities and inherits both of their variances. This is
exactly why interaction effects are notoriously hard to detect: the same design that estimates a
main effect comfortably estimates the corresponding interaction with a standard error $\sqrt2$
times larger.

## Robust regression breaks the clean scaling

The variance ratios above assume ordinary least squares, where every sample carries the same
weight. `msqrob` instead fits the model by **robust regression**, which down-weights outlying
observations, so the effective design-variance for a contrast is

$$
\mathrm{Var}(L^\top\hat\beta) = \hat\sigma^2_{\text{post}}\, L^\top (X^\top W X)^{-1} L, \qquad
W = \mathrm{diag}(w_1,\dots,w_n),
$$

with $\hat\sigma^2_{\text{post}}$ the empirical-Bayes (posterior) residual variance and $w_i$ the
robust weight assigned to sample $i$. For most proteins this tracks the OLS calculation closely,
but for at least one protein in this dataset (protein 2) the four contrasts' standard errors do
**not** follow the tidy $1,\ 1,\ 1/\sqrt2,\ \sqrt2$ pattern predicted above. The reason is visible
in the fitted weights: the left-side and right-side samples for that protein were down-weighted
differently, because the robust fit judged some of them to be outliers. So the precision achieved
on a given contrast is not purely a property of the design — it also depends on how much evidence
that particular protein's own data gave the fit reason to discount.

## Stagewise testing: screening then confirming

A flat correction across all four contrasts, for all proteins, wastes exactly the power the
previous section explains away: the interaction test is intrinsically the weakest of the four, so
under one blanket correction it may return no discoveries at all, even where the other three
contrasts show plenty. The [stageR method](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-017-1277-0)
addresses this with a two-stage procedure.

**Screening stage.** For every protein, run one *omnibus* test of the joint null hypothesis that
both $\beta_V=0$ and $\beta_{RV}=0$ — i.e. that there is no ventricle-vs-atrium shift on either
side. This 2-degree-of-freedom test pools the evidence for the main effect and the interaction
into a single p-value per protein. Only these omnibus p-values are corrected for multiple testing
across all proteins, at the usual 5% FDR, giving the set of proteins that pass screening.

```r
pe <- omnibusTest(pe, "proteinRobust", L)
```

**Confirmation stage.** For the proteins that passed screening, the four specific contrasts
(left, right, average, interaction) are now tested and adjusted — but with a much weaker
correction than Holm or BH would apply to four independent tests, because these four hypotheses
are not independent: they are all built from just the two free parameters $\beta_V$ and
$\beta_{RV}$. Enumerating what can happen to those two parameters shows that **at most one** of
the four confirmation hypotheses can be a false rejection for a given protein:

- if neither parameter is truly nonzero, all four could be falsely rejected together — but this
  is exactly the case the screening-stage FDR correction has already priced in;
- if only the main effect $\beta_V\neq0$ (interaction $=0$): left, right and average are all truly
  nonzero, so only the interaction hypothesis could be a false rejection;
- if only the interaction $\beta_{RV}\neq0$ (main effect $=0$): left is the true null, and it is
  the only one of the four that could be falsely rejected;
- if both are nonzero: unless $\beta_{RV}=-\beta_V$ (making the right-side contrast zero) or
  $\beta_{RV}=-2\beta_V$ (making the average zero), all four contrasts are genuinely nonzero and
  nothing can be falsely rejected; in either special case exactly one of the four (right, or
  average, respectively) is the true null and the only possible false rejection.

Because the family of confirmation hypotheses can contribute at most one false rejection per
protein — and the risk of testing a protein that should never have reached this stage at all was
already controlled by the screening-stage FDR — the confirmation stage can be run with **no**
multiple-testing correction (`method = "none"`) instead of Holm, without inflating the FDR. Doing
so recovers extra significant proteins, including some for the interaction contrast that a flat
correction would have missed entirely.

```r
stageWiseAnalysis <- stageR(pAll[, 1], pAll[, -1])
stageWiseAnalysis <- stageWiseAdjustment(stageWiseAnalysis, method = "none",
                                          alpha = 0.05, allowNA = TRUE)
```

This argument is specific to this design and this particular family of four contrasts (all built
from the same two parameters); it is **not** a general licence to skip correction in a
confirmation stage. For a different design or a different set of hypotheses of interest, more
than one false rejection can be possible per gene/protein, and Holm's method — always valid,
if conservative — is the recommended default.

## Sources

All of this chapter comes from one converted lecture tutorial, `heartMainInteractionStageR.Rmd`
(statOmics SGA21, CC BY-NC-SA 4.0), split across four files with no accompanying slide deck or
transcript for this session:

- The dataset, the research questions, and data import/exploration:
  `docs/omics-statistics/statomics/sga21/heartMainInteractionStageR/01-data.md`.
- Log-transformation, filtering, normalization, MDS exploration and protein-level aggregation:
  `docs/omics-statistics/statomics/sga21/heartMainInteractionStageR/02-preprocessing.md`.
- The `msqrob` model formula, the four contrasts, and their volcano-plot/heatmap evaluation:
  `docs/omics-statistics/statomics/sga21/heartMainInteractionStageR/03-data-analysis.md`.
- The design-matrix variance argument, the robust-regression weight example (protein 2), and the
  stageR screening/confirmation procedure:
  `docs/omics-statistics/statomics/sga21/heartMainInteractionStageR/04-large-difference-in-number-of-proteins-that-are-returned.md`.

The lecture points to, but does not itself contain, two external items: the full PXD006675
dataset on PRIDE (only a small subset is used here), and the stageR method paper (Van den Berge &
Clement, *Genome Biology*, 2017), linked above. Exact counts of significant proteins in the
source are left as inline, unevaluated R expressions (e.g. `` `r length(sigNamesLeft)` ``) rather
than fixed numbers, so this chapter reports the qualitative pattern the lecture describes rather
than inventing specific counts. No separate problem set was supplied for this material.

---

[← 6. The msqrob2gui Analysis Workflow](06-the-msqrob2gui-analysis-workflow.md) · [Contents](index.md) · [9. Illumina Next-Generation Sequencing Overview →](09-illumina-next-generation-sequencing-overview.md)
