---
title: "35. Filtering, Aliasing, and limma-voom"
course: "StatOmics Sga21"
chapter: 35
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 35. Filtering, Aliasing, and limma-voom

## What this covers

This chapter collects three practical problems that show up once you already have a fitted count
model and want to test for differential expression: whether it is legitimate to throw out
lowly-expressed features before testing at all (independent filtering), what happens when a design
matrix you wrote down cannot actually be fit because one effect duplicates information already
carried by another (aliasing), and an alternative to fitting a dedicated count distribution
altogether, by borrowing limma's linear-model machinery instead (limma-voom). It assumes the
standard 'omics DE pipeline is already familiar: a count-based model such as edgeR or DESeq2,
design matrices and contrasts, multiple-testing correction, and the limma empirical-Bayes
framework from the proteomics module.

## Independent filtering

Filtering out features — genes, transcripts, proteins — before running the statistical analysis is
routine in 'omics experiments. The usual target is lowly expressed features, for two reasons: their
expression may be too low to be biologically interesting, and low counts carry high relative
uncertainty and hence low statistical power (the same intuition behind edgeR's BCV plot). A feature
that stood no real chance of being called significant is also a wasted test: keeping it around only
adds to the multiple-testing burden and makes the correction more severe for everyone else.

[Bourgon *et al.* (2010)](https://www.pnas.org/content/107/21/9546) formalised this practice.
For every feature compute two statistics, a filter statistic $S_F$ and a test statistic $S_T$. A
feature is only declared significant if both exceed some cutoff — first it must pass the filter,
then it must pass the test. The subtlety is that the testing stage is now **conditional** on the
filtering stage: only features that passed the filter are tested, adjusted, and reported, yet the
usual multiple-testing correction is computed as though every feature had gone forward into the
test, filtering or no filtering. If filtering changes the distribution of $S_T$ among the features
that survive it, that correction is computed against the wrong distribution, and the reported
adjusted $p$-values can be overoptimistic.

Bourgon *et al.* show exactly when this is safe: filtering does not inflate the type I error rate
provided the *conditional* null distribution of the test statistic, given that a feature passed the
filter, is the same as the *unconditional* null distribution. Equivalently, **the filter statistic
must be independent of the test statistic under the null hypothesis**. That alone is not enough to
make a good filter, though — a filter statistic that is independent of the test statistic under
*both* the null and the alternative is a random filter: it throws away a fixed fraction of features
without regard to which ones are true positives, which only costs power for nothing. A useful
filter is independent under the null, but informative under the alternative.

<figure>
<svg viewBox="0 0 640 280" role="img" aria-label="Filtering that correlates with the test statistic shifts its null distribution; filtering that is independent of it does not.">
  <text x="160" y="20" text-anchor="middle" font-size="12" fill="currentColor">dependent filter</text>
  <text x="480" y="20" text-anchor="middle" font-size="12" fill="currentColor">independent filter</text>

  <line x1="40" y1="200" x2="280" y2="200" stroke="currentColor" stroke-width="1.5"/>
  <line x1="160" y1="200" x2="160" y2="40" stroke="currentColor" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="160" y="215" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="160" y="235" text-anchor="middle" font-size="12" fill="currentColor">test statistic</text>
  <path d="M40,200 C100,200 148,60 160,60 C172,60 220,200 280,200" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <path d="M120,200 C165,200 192,110 210,110 C228,110 255,200 300,200" fill="none" stroke="#c1440e" stroke-width="1.8" stroke-dasharray="5,4"/>

  <line x1="360" y1="200" x2="600" y2="200" stroke="currentColor" stroke-width="1.5"/>
  <line x1="480" y1="200" x2="480" y2="40" stroke="currentColor" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="480" y="215" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="480" y="235" text-anchor="middle" font-size="12" fill="currentColor">test statistic</text>
  <path d="M360,200 C420,200 468,60 480,60 C492,60 540,200 600,200" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <path d="M365,200 C424,200 470,65 480,65 C490,65 536,200 595,200" fill="none" stroke="#c1440e" stroke-width="1.8" stroke-dasharray="5,4"/>

  <line x1="230" y1="258" x2="250" y2="258" stroke="currentColor" stroke-width="1.8"/>
  <text x="256" y="262" font-size="11" fill="currentColor">unconditional (before filtering)</text>
  <line x1="230" y1="272" x2="250" y2="272" stroke="#c1440e" stroke-width="1.8" stroke-dasharray="5,4"/>
  <text x="256" y="276" font-size="11" fill="currentColor">conditional (kept after filtering)</text>
</svg>
<figcaption>Schematic of the simulated DESeq2 example. Filtering on a statistic tied to the group
difference shifts the retained null distribution of the test statistic away from the unconditional
one (left); filtering on overall expression level leaves it essentially unchanged (right).</figcaption>
</figure>

The lecture makes this concrete with a small simulated dataset (`DESeq2::makeExampleDESeqDataSet()`,
two groups A and B) and two candidate filters, each removing about 20% of genes.

### A dependent filter statistic

Filter on the absolute difference in group means, $|\overline{y}_A - \overline{y}_B|$, keeping genes
above a cutoff. This is a bad filter statistic to pair with a two-sample $t$-test, because the same
difference in means sits in the numerator of the $t$-statistic. Plot the density of the $t$-statistic
for all genes, then again restricted to the genes that passed this filter: the two densities look
very different — the conditional one is shifted and no longer symmetric around zero the way the
unconditional null distribution is. Genes get kept precisely because they showed a large sample
difference, and some of those large differences are just noise under the true null; conditioning on
"large observed difference" therefore enriches the retained set for large $|t|$ even when there is no
real effect. Correcting $p$-values afterwards as if no filtering had happened understates how many
of the surviving hits are false positives.

### An independent filter statistic

Filter instead on the overall row mean across *all* samples, `rowMeans(simCounts)`, ignoring group
membership. Because this statistic does not use the group labels at all, it carries no information
about which direction or how large a group difference is; under the null hypothesis it is (close to)
independent of the $t$-statistic. Plotting the two densities again — before and after this filter —
shows them essentially unchanged. This is the shape of filter that ordinary DE pipelines use in
practice: filtering by overall expression level (as `edgeR`'s `filterByExpr`, used again later in
this chapter, does) removes features that were never going to be reliably tested anyway, without
distorting the null distribution that the multiple-testing correction relies on.

## Aliasing

A design matrix can be well-intentioned and still fail to be fittable, because one of its columns
turns out to be a linear combination of others. When that happens the corresponding parameter
cannot be estimated at all — not "estimated with low precision", but **not identifiable**, because
the data contain no information beyond what other parameters already carry. This is aliasing, and
complex 'omics designs with paired or blocked samples run into it easily.

Take a study of a drug's effect on gene expression in colon cancer: four cancer patients and four
healthy individuals, each sampled twice — once before and once two weeks after a daily dose of the
drug. The scientific question is whether the change over time differs between the two groups, i.e.
the interaction between `disease` and `time`. A natural design is `~ patient + disease*time`, with
`patient` (8 levels), `disease` (healthy/cancer) and `time` (before/after). Simulating a single gene's
counts from a plain Poisson and fitting `glm(y ~ patient + disease*time, family = "poisson")`
produces an `NA` coefficient — not because of missing data, but because R's `glm` detected that one
parameter is redundant.

The redundant parameter is the `disease` main effect. Once you know which patient a sample came
from, you already know whether that patient is a cancer or a healthy case — disease status never
varies within a patient, so it adds nothing once the eight patient-level intercepts are already in
the model. Concretely, in the design matrix $X$ for `~ patient + disease*time`, the `diseasecancer`
column is *exactly* the sum of the four patient-indicator columns for the cancer patients:

$$X_{\text{diseasecancer}} = X_{\text{patiente}} + X_{\text{patientf}} + X_{\text{patientg}} + X_{\text{patienth}}.$$

R's `alias()` function confirms this directly: it reports `diseasecancer` as a linear combination of
those four patient effects.

<figure>
<svg viewBox="0 0 460 210" role="img" aria-label="Grid of eight patients by two timepoints, showing disease status is constant within each patient.">
  <text x="60" y="42" text-anchor="middle" font-size="12" fill="currentColor">a</text>
  <text x="110" y="42" text-anchor="middle" font-size="12" fill="currentColor">b</text>
  <text x="160" y="42" text-anchor="middle" font-size="12" fill="currentColor">c</text>
  <text x="210" y="42" text-anchor="middle" font-size="12" fill="currentColor">d</text>
  <text x="260" y="42" text-anchor="middle" font-size="12" fill="currentColor">e</text>
  <text x="310" y="42" text-anchor="middle" font-size="12" fill="currentColor">f</text>
  <text x="360" y="42" text-anchor="middle" font-size="12" fill="currentColor">g</text>
  <text x="410" y="42" text-anchor="middle" font-size="12" fill="currentColor">h</text>
  <text x="8" y="68" font-size="11" fill="currentColor">before</text>
  <text x="8" y="108" font-size="11" fill="currentColor">after</text>

  <g>
    <rect x="40" y="50" width="40" height="30" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
    <rect x="90" y="50" width="40" height="30" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
    <rect x="140" y="50" width="40" height="30" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
    <rect x="190" y="50" width="40" height="30" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
    <rect x="240" y="50" width="40" height="30" fill="#c1440e" fill-opacity="0.18" stroke="#c1440e"/>
    <rect x="290" y="50" width="40" height="30" fill="#c1440e" fill-opacity="0.18" stroke="#c1440e"/>
    <rect x="340" y="50" width="40" height="30" fill="#c1440e" fill-opacity="0.18" stroke="#c1440e"/>
    <rect x="390" y="50" width="40" height="30" fill="#c1440e" fill-opacity="0.18" stroke="#c1440e"/>

    <rect x="40" y="90" width="40" height="30" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
    <rect x="90" y="90" width="40" height="30" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
    <rect x="140" y="90" width="40" height="30" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
    <rect x="190" y="90" width="40" height="30" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
    <rect x="240" y="90" width="40" height="30" fill="#c1440e" fill-opacity="0.18" stroke="#c1440e"/>
    <rect x="290" y="90" width="40" height="30" fill="#c1440e" fill-opacity="0.18" stroke="#c1440e"/>
    <rect x="340" y="90" width="40" height="30" fill="#c1440e" fill-opacity="0.18" stroke="#c1440e"/>
    <rect x="390" y="90" width="40" height="30" fill="#c1440e" fill-opacity="0.18" stroke="#c1440e"/>
  </g>

  <rect x="40" y="150" width="18" height="14" fill="currentColor" fill-opacity="0.08" stroke="currentColor"/>
  <text x="64" y="161" font-size="11" fill="currentColor">healthy patient (a-d)</text>
  <rect x="230" y="150" width="18" height="14" fill="#c1440e" fill-opacity="0.18" stroke="#c1440e"/>
  <text x="254" y="161" font-size="11" fill="currentColor">cancer patient (e-h)</text>
</svg>
<figcaption>Disease status is a property of the column (patient), constant down every column,
while time is a property of the row and varies within every patient. So the four cancer-patient
columns alone already determine the disease effect: it carries no information beyond the patient
intercepts.</figcaption>
</figure>

Since the `disease` main effect is redundant given `patient`, it can be dropped: `~ patient + time +
disease:time`. That is still aliased, though — the interaction term generates *two* columns,
`timebefore:diseasecancer` and `timeafter:diseasecancer`, and only the second is new information. The
reason is the same idea one level down: a patient's own intercept already pins down that patient's
mean expression at the reference (`before`) timepoint, healthy or cancer alike, so a disease-specific
offset added at that same reference timepoint duplicates what the cancer patients' intercepts already
say. It can be recovered by averaging those intercepts — it isn't new data, so `glm` cannot estimate
it as a separate parameter. Only the offset at the *other* timepoint — the extra shift for being both
cancer and post-drug — is new, and that is exactly the interaction the study wants to test. Dropping
the `timebefore:diseasecancer` column from $X$ and refitting leaves every remaining coefficient
estimable: `timeafter` is the drug's effect for the reference (healthy) group, and
`timeafter:diseasecancer` is the difference in that effect for cancer patients — the answer to the
research question.

Aliasing is a property of the design, not of the data: no amount of extra samples repairs it if the
confound is built into which units were measured under which combination of conditions. It has to be
diagnosed and removed at the design stage — by reasoning about which factor is nested inside which
(here, disease is nested inside patient), or by checking with `alias()` — before the model is fit.

**A follow-up question the lecture poses.** Suppose instead you are willing to assume there is *no*
disease-by-time interaction, so the design simplifies to `~ patient + time` (no `disease` term at
all, since it is fully absorbed by `patient`). How do you now test healthy versus cancer patients at
the first (`before`) timepoint? You cannot just read off a coefficient, because there is no `disease`
coefficient in this design — the comparison has to be built as a contrast across the relevant patient
intercepts. Writing $\beta_0$ for the reference patient (patient a, healthy) and $\beta_1,\dots,\beta_7$
for the remaining patients' offsets, the average log-expression at the `before` timepoint is, for the
healthy patients,

$$\log \mu_{\text{healthy}} = \frac{1}{4}\left\{\beta_0 + (\beta_0+\beta_1) + (\beta_0+\beta_2) + (\beta_0+\beta_3)\right\},$$

and for the cancer patients,

$$\log \mu_{\text{diseased}} = \frac{1}{4}\left\{(\beta_0+\beta_4) + (\beta_0+\beta_5) + (\beta_0+\beta_6) + (\beta_0+\beta_7)\right\}.$$

The contrast of interest is the difference of these two averages,

$$\log\frac{\mu_{\text{diseased}}}{\mu_{\text{healthy}}} = \frac14(\beta_4+\beta_5+\beta_6+\beta_7) - \frac14(\beta_1+\beta_2+\beta_3).$$

Notice the asymmetry: three explicit offsets on the healthy side against four on the cancer side.
That is not a mistake — patient a is the design's reference level, so its own offset is folded into
$\beta_0$ and cancelled out of the difference, leaving only $\beta_1,\beta_2,\beta_3$ to average over
for the other three healthy patients. Forgetting that the reference level's implicit zero has to be
accounted for is the standard way to get a contrast like this wrong.

## limma-voom: an alternative to modelling counts directly

`limma` is the linear-model framework already met in the proteomics module for microarray data: it
fits a linear model per feature and then uses an empirical Bayes step to borrow information across
features, shrinking each feature's variance estimate toward a common trend. In its default form it
cannot be applied to count data, because it has no way to account for the count mean-variance
relationship — the fact that variance grows with the mean, which `edgeR` and `DESeq2` build in by
assuming a distribution (typically negative binomial) whose mean-variance relationship matches the
data reasonably well.

[Law *et al.* (2014)](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2014-15-2-r29)
found a way to keep the count-aware behaviour without adopting a count distribution: **limma-voom**
estimates the mean-variance trend of the dataset directly and nonparametrically — using each gene's
overall mean and variance across all samples — and then converts that trend into an
**observation-level weight** for every individual observation (one weight per gene-sample
combination, not just per gene). Those weights are plugged into an ordinary (Gaussian) weighted
linear regression, so heteroscedasticity is handled through the weights rather than through an
assumed count distribution. This buys a real simplification: dedicated count models are more
accurate when their distributional assumption holds, but they are also more complex to fit and to
reason about; voom keeps the familiar linear-model-plus-empirical-Bayes pipeline and only changes how
the variance going into it is estimated. The trend itself is dataset-specific and has to be
re-estimated for every dataset.

Applied to the parathyroid dataset, with design `~ treatment*time + patient`: genes are first
filtered with `filterByExpr` (independent filtering by overall expression level, exactly the
principle from the first section of this chapter) and normalised with `calcNormFactors`, exactly as
in `edgeR`. Then `voom(dge, design)` estimates the mean-variance trend and returns the weighted data
object, which goes into `lmFit` and `eBayes` precisely as an ordinary limma analysis would. `topTable`
extracts results for the coefficients of interest — in this example, the treatment-by-time
interaction — and gives a similar answer (no differential expression detected) to the count-model
approach.

### Testing contrasts under limma-voom

`edgeR` lets you test a numeric contrast against the fitted model's coefficients directly, in one
step. `limma` does not support that pattern: instead, the fitted model is *reparametrised* so that
each new coefficient corresponds exactly to one contrast of interest, using `contrasts.fit`. The
recipe is: build a contrast matrix $L$ with one row per original design coefficient and one column
per contrast wanted, where column $j$ holds the linear-combination weights that produce contrast $j$
from the original coefficients. `contrasts.fit(fit, L)` returns a new fit whose coefficients are
$L^\top\hat\beta$ — one per contrast — after which `eBayes` and `topTable` are run again exactly as
before, once per contrast column.

In the parathyroid example this produces seven contrasts of interest at once: each of two drugs
(DPN, OHT) compared to control at each of two timepoints (24h, 48h), plus three interaction contrasts
comparing how each drug's effect changes between timepoints, and how the two drugs' changes compare
to each other. Looping `topTable` over the seven columns of $L$ and counting adjusted $p$-values
below 0.05 for each gives the number of differentially expressed genes per contrast, in the same way
a set of separate `edgeR` contrast tests would.

## Sources

- **Independent filtering** — `docs/omics-statistics/statomics/sga21/sequencing_technicalDE/01-independent-filtering.md`,
  converted from [`sequencing_technicalDE.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_technicalDE.Rmd)
  (statomics SGA21, CC BY-NC-SA 4.0), including its worked simulated-data example
  (`DESeq2::makeExampleDESeqDataSet`). The formal criterion is attributed there to
  [Bourgon *et al.*, PNAS (2010)](https://www.pnas.org/content/107/21/9546), which the lecture cites
  but does not reproduce. Two referenced figures (`independentFiltering.png`,
  `independentFiltering2.png`) were not available to this chapter; the diagram here is original,
  built to match the description in the text.
- **Aliasing** — `docs/omics-statistics/statomics/sga21/sequencing_technicalDE/02-aliasing.md`, same
  source file, including the colon-cancer worked example, the design-matrix identity, the fix to the
  model, and the follow-up contrast question with its worked answer.
- **limma-voom** — `docs/omics-statistics/statomics/sga21/sequencing_technicalDE/03-limma-voom-as-an-alternative-approach-to-modeling-counts.md`,
  same source file. The method is attributed there to
  [Law *et al.*, Genome Biology (2014)](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2014-15-2-r29).
  The lecture points to the parathyroid dataset (`data/seParathyroid.rds`) and to two figures
  (`limmaVoomMeanVariance.png`, `limmaVoomWeights.png`) that were not available here, and assumes
  the `limma` fundamentals (linear model plus empirical Bayes moderation) from "the proteomics
  module of this course", which this chapter does not repeat.
- No slides or transcript were supplied for this lecture; all three parts are converted lecture
  notes from the same source `.Rmd`, split by topic.

---

[← 34. Scaling Normalization and Offsets](34-scaling-normalization-and-offsets.md) · [Contents](index.md) · [36. Single-Cell RNA-Seq: A First Look →](36-single-cell-rna-seq-a-first-look.md)
