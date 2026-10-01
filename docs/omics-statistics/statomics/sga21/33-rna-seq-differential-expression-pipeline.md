---
title: "33. RNA-seq Differential Expression Pipeline"
course: "StatOmics Sga21"
chapter: 33
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 33. RNA-seq Differential Expression Pipeline

## What this covers

This chapter follows one lecture's worked example: a complete RNA-seq differential-expression
analysis, run start to finish, on a real bulk RNA-seq dataset. It does not introduce new
statistical machinery — it applies things assumed already in place (the Poisson and negative
binomial distributions, the GLM and IRLS, and empirical-Bayes shrinkage from the proteomics part
of this course) to a concrete pipeline, organized around four challenges that recur in any
RNA-seq analysis: choosing a distribution for the counts, normalizing between samples, estimating
parameters with only a handful of replicates, and testing thousands of genes at once.

## The dataset and its structure

The dataset comes from Haglund *et al.* (2012), imported through the Bioconductor package
`parathyroidSE` as a `SummarizedExperiment`: a single container holding the count matrix
(genes x samples) alongside the sample metadata (`colData`), so a row of the matrix and its
corresponding row of metadata cannot be silently mismatched. The design has three treatments
(Control, DPN, OHT), two time points (24h, 48h), and four donor patients.

The imported object has more columns than the number of samples described in the paper's methods
section, because some samples were sequenced more than once and appear as separate columns.
Repeating a sequencing run on the same physical sample is **technical replication**, not
biological replication, and the two should not be pooled the same way. Technical replicates —
repeated draws from the same underlying RNA population — behave like a Poisson process, and the
Poisson distribution has a convenient closed-form property: if $X \sim \mathrm{Poi}(\mu_X)$ and
$Y \sim \mathrm{Poi}(\mu_Y)$ are independent, then $X + Y \sim \mathrm{Poi}(\mu_X + \mu_Y)$.
Summing technical replicates therefore keeps the Poisson structure intact; averaging them does
not (worth checking directly). So before anything else, the duplicated columns are summed and
removed, leaving one column per genuine biological sample — and the resulting counts of samples
per patient x treatment x time now match the numbers reported in the paper.

## Independent filtering and a first look at the data

Before modeling, genes with generally low counts are removed. This is **independent filtering**:
a gene with a low count has high relative uncertainty and hence low statistical power to be
detected, so keeping it only adds to the multiple-testing burden paid by every other gene without
much chance of a discovery. The criterion used here keeps a gene only if its count-per-million
exceeds 2 in at least three samples.

The remaining structure is explored with an MDS (multidimensional scaling) plot, which places each
sample in two dimensions so that the distances between the points approximate, as closely as
possible, the Euclidean distances between the samples in the full, high-dimensional count space.
Three things are visible immediately:

- Samples from the same patient cluster tightly — **between-patient variability is the largest
  source of variation** in the dataset, by a wide margin.
- Within a patient, the two time points separate more clearly than the three treatments do.
- Relative to patient and time, the treatment effect looks small.

That ordering — patient, then time, then treatment — is worth remembering: it predicts which
comparisons will turn up many differentially expressed genes later, and which will not (see
Challenge IV).

## Challenge I: choosing a distribution for the counts

Having thousands of genes measured on the same samples means the mean-variance relationship can be
checked empirically rather than assumed. Within a single experimental condition (one
treatment x time combination, chosen so biological variability is as homogeneous as possible),
plotting each gene's variance against its mean across replicates shows two things: the points sit
systematically above the line $\mathrm{Var} = \mathrm{Mean}$ that a Poisson distribution would
predict — the data is **overdispersed** — and the excess grows roughly quadratically with the
mean.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Gene-wise variance against gene-wise mean, on log-log axes, compared with the Poisson prediction that variance equals the mean">
  <line x1="50" y1="190" x2="50" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <line x1="50" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <text x="300" y="207" text-anchor="end" font-size="12" fill="currentColor">mean count (log scale)</text>
  <text x="18" y="30" font-size="12" fill="currentColor">variance (log scale)</text>
  <line x1="55" y1="182" x2="205" y2="55" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
  <text x="208" y="52" font-size="11" fill="currentColor">Poisson: Var = Mean</text>
  <path d="M55,178 C110,162 150,105 195,55 C225,32 250,20 278,15" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <text x="120" y="45" font-size="11" fill="currentColor">empirical trend (quadratic)</text>
  <g fill="currentColor" fill-opacity="0.6">
    <circle cx="80" cy="168" r="2"/>
    <circle cx="100" cy="150" r="2"/>
    <circle cx="120" cy="145" r="2"/>
    <circle cx="140" cy="118" r="2"/>
    <circle cx="150" cy="95" r="2"/>
    <circle cx="170" cy="80" r="2"/>
    <circle cx="185" cy="65" r="2"/>
    <circle cx="200" cy="50" r="2"/>
    <circle cx="220" cy="40" r="2"/>
    <circle cx="240" cy="28" r="2"/>
    <circle cx="260" cy="22" r="2"/>
  </g>
</svg>
<figcaption>Within one experimental condition, gene-wise variance plotted against gene-wise mean
count sits above the Poisson line Var = Mean and diverges from it as the mean grows — the pattern
that motivates the negative binomial as the working distribution for RNA-seq counts.</figcaption>
</figure>

This is the standard argument for modeling RNA-seq counts with the **negative binomial (NB)**
distribution rather than the Poisson. The negative binomial can be written as a Gamma-Poisson
mixture:
$$
\lambda \sim \Gamma(\alpha, \beta), \qquad Y \mid \lambda \sim \mathrm{Poi}(\lambda)
\quad\Longleftrightarrow\quad Y \sim \mathrm{NB}(\mu = \alpha/\beta,\ \phi = 1/\alpha).
$$
The derivation is analytic but was treated as outside the scope of the lecture; it was checked
instead by simulation — drawing from the hierarchical Gamma-then-Poisson model and comparing the
resulting density to samples drawn directly from an NB with matching mean and dispersion, which
overlap closely.

The two-layer structure has a direct interpretation and a direct consequence. The Poisson layer
captures **technical** variation — the sampling noise of sequencing itself — while the Gamma layer
captures **biological** variation, i.e. genuine differences in mean expression between biological
replicates. That is exactly why summing technical replicates was the right move earlier: the sum
of Poisson draws is still Poisson, so summing preserves the technical layer without touching the
biological one.

## Challenge II: normalization

Normalization corrects for technical differences between samples that have nothing to do with the
biology of interest:

- **Sequencing depth.** A sample with more mapped reads shows higher counts for essentially every
  gene, purely because more reads were drawn — not because expression is higher.
- **RNA composition.** If one sample is contaminated with a highly abundant contaminant
  transcript, that contaminant eats into the fixed read budget and depresses the apparent counts
  of every other gene, even at equal sequencing depth.
- **Other technical effects**, such as sample-specific GC-content or transcript-length biases.

The effect of depth alone is visible directly in a mean-difference (MD, or MA) plot: for two
replicates of the same condition, the log fold-change between them should scatter around zero. In
this dataset, one pair of Control-48h replicates shows a clear downward bias, and the two
samples' library sizes (about $11\times10^6$ and $7\times10^6$ reads) explain why.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Mean-difference plot showing a systematic offset from zero caused by unequal sequencing depth, corrected by normalization">
  <line x1="40" y1="170" x2="310" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="170" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="310" y="187" text-anchor="end" font-size="12" fill="currentColor">log mean expression</text>
  <text x="14" y="30" font-size="12" fill="currentColor">log fold-change</text>
  <line x1="45" y1="95" x2="305" y2="95" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
  <text x="315" y="98" font-size="11" fill="currentColor">0</text>
  <ellipse cx="180" cy="132" rx="115" ry="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="180" y="160" text-anchor="middle" font-size="11" fill="currentColor">unnormalized replicate pair</text>
  <defs>
    <marker id="arrow-md" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="180" y1="128" x2="180" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-md)"/>
  <text x="188" y="112" font-size="11" fill="currentColor">normalize</text>
</svg>
<figcaption>Two replicates of the same condition, before normalization: the cloud of per-gene log
fold-changes sits off zero because the two libraries differ in size. Normalizing (here, TMM)
recentres it at zero.</figcaption>
</figure>

### Offsets rather than scaling

The natural way to correct for depth inside a GLM is an **offset**, not a rescaling of the raw
counts. An offset accounts for the amount of "effort" behind an observation without spending a
free parameter on it: fitting a coefficient for a covariate estimates how much the response
changes per unit of that covariate, whereas adding an offset fixes that coefficient at exactly $1$
and folds it straight into the linear predictor. A biologist who spends different amounts of time
watching for migrating whales on different days, and uses the time spent as an offset, is doing
the same thing as using sequencing depth $N_i = \sum_g Y_{gi}$ as an offset for sample $i$: a
sample sequenced more deeply carries more information, and the offset says so without being
estimated. With a gene- and sample-specific offset $O_{gi}$, the NB GLM becomes
$$
Y_{gi} \sim \mathrm{NB}(\mu_{gi}, \phi_g), \qquad \log \mu_{gi} = \eta_{gi} = \mathbf{X}_i^\top
\beta_g + \log(O_{gi}).
$$

### Three ways to compute the offset

**TMM** (trimmed mean of M-values; the `edgeR` default), due to Robinson and Oshlack, computes,
for each sample $i$ against a reference sample $r$, a normalization factor
$$
\log_2 F_i^{(r)} = \frac{\sum_{g \in \mathcal{G}^*} w_{gi}^r M_{gi}^r}{\sum_{g \in \mathcal{G}^*}
w_{gi}^r}, \qquad M_{gi}^r = \log_2\!\left(\frac{Y_{gi}/N_i}{Y_{gr}/N_r}\right),
$$
a weighted average, over a trimmed set of genes $\mathcal{G}^*$, of each gene's log fold-change in
expression fraction relative to the reference. The weight
$$
w_{gi}^r = \frac{N_i - Y_{gi}}{N_i Y_{gi}} + \frac{N_r - Y_{gr}}{N_r Y_{gr}}
$$
downweights genes with low counts, whose fold-changes are noisier. By default TMM trims the 30% of
genes with the most extreme fold-changes and the 5% with the most extreme average expression
before averaging, and picks as reference the sample whose upper quartile is closest to the average
upper quartile across samples. The resulting **effective library size** $N_i^{\mathrm{eff}} = N_i
F_i^{(r)}$ is used as the GLM offset. Applying it to the biased Control-48h pair recentres the
MD-plot on zero.

**Median-of-ratios** (the `DESeq2` default, due to Love, Huber and Anders) assumes
$\mu_{gi} = s_i q_{gi}$ — the mean count for gene $g$ in sample $i$ is a per-sample size factor
$s_i$ times the gene's "true" expression $q_{gi}$ — and estimates $s_i$ against a synthetic
reference built from the geometric mean of each gene's counts across samples,
$$
s_i = \mathrm{median}_{\{g:\, Y_{gr}^* \neq 0\}} \frac{Y_{gi}}{Y_{gr}^*}, \qquad Y_{gr}^* =
\left(\prod_{i=1}^n Y_{gi}\right)^{1/n}.
$$
This relies on genes being expressed (nonzero) in every sample — a mild requirement with a
handful of bulk replicates, but one where the number of genes nonzero everywhere shrinks steadily
as the number of samples grows, and turns into a real problem once cells replace samples in
single-cell data. TMM's and DESeq2's size factors agree closely once rescaled to a common overall
level — a useful check that two differently-derived procedures are estimating the same quantity.

**Full-quantile normalization**, originally developed for microarrays, produces no offset at all —
it rewrites the counts directly, forcing every sample to share the same distribution: sort each
sample's column, replace every value in a given rank position by the median (or mean) across
samples at that rank, then restore each column to its original gene order.

Whichever method computes it, the offset itself is an **estimate**, and the downstream GLM
conditions on it as if it were known — the analysis quietly ignores the uncertainty in the
normalization step.

## Challenge III: parameter estimation under limited replication

Fitting the mean model has two separate difficulties: getting the *structure* of the model right —
which covariates to include and how — and estimating its parameters well with only a handful of
replicates per condition.

The original paper describes its mean model as using "treatment type, time point and sample ID as
factors" — and "sample ID" here means the donor patient, not the `sample` variable actually stored
in the imported metadata, an ambiguity that would have been resolved by reading the authors' code,
had it been shared. Read at face value, the model includes patient as a blocking factor (exactly
the blocking strategy used in the proteomics part of this course) but only *main effects* for
treatment and time — which assumes the time effect (the average change from 24h to 48h) is
identical across Control, DPN and OHT. Given how naturally that assumption could be relaxed by
adding a treatment x time interaction, it is worth treating it as an assumption rather than a given.

Once the mean-model structure is fixed, the mean parameters $\beta$ can be estimated reasonably
well even with few replicates, by IRLS. The dispersion parameter $\phi$ (or, in a Gaussian model,
the variance $\sigma$) is a different story: with only a handful of samples per gene, a per-gene
maximum-likelihood dispersion estimate is noisy.

### Borrowing strength across genes: empirical Bayes

Because the same model is fit gene by gene across thousands of genes in parallel, information
about the dispersion can be **borrowed across genes**, in a procedure called empirical Bayes —
the same idea already met in the proteomics part of this course. In a standard Bayesian analysis, a
prior $p(\theta)$, fixed before any data is seen, combines with the data likelihood via Bayes' rule
to give a posterior
$$
p(\theta \mid \mathbf{Y}) = \frac{p(\mathbf{Y}\mid\theta)\,p(\theta)}{\int_{\theta\in\Theta}
p(\mathbf{Y}\mid\theta)\,p(\theta)\,d\theta}.
$$
**Empirical Bayes** is semi-Bayesian: instead of assuming the prior is known, it is estimated from
the data itself, and that estimated prior $\hat p(\theta)$ is then used exactly as a prior
normally would be. When the resulting posterior is awkward to work with directly, the **maximum a
posteriori (MAP)** estimate — the mode of the posterior — plays the role a point estimate plays in
frequentist inference.

The specific assumption that makes this useful for dispersion is that genes with similar mean
expression tend to have similar dispersions, since the mean-variance trend from Challenge I links
the two. In practice: fit an initial, per-gene maximum-likelihood dispersion
$\hat\phi_g^{\mathrm{ML}}$ for every gene; fit a smooth trend of dispersion against mean expression
across all genes, and treat that trend as the (empirically estimated) prior; then shrink each
gene's initial estimate towards the trend, by an amount that depends on how precise that gene's
own estimate is and how much the prior itself varies. The gain from this shrinkage is large enough
that some version of it sits inside every popular differential-expression package — `limma`,
`edgeR` and `DESeq2` each implement it slightly differently. (The lecture pointed to David
Robinson's blog post and book on empirical Bayes via baseball batting averages as an accessible
primer on the same idea outside genomics.)

Fit to this dataset with a design of `treatment * time + patient` — the richer model that adds the
interaction the original paper's model lacked — `edgeR`'s dispersion-versus-mean trend (its BCV,
biological coefficient of variation, plot) is exactly this shrinkage curve, and the fitted
gene-wise GLM coefficients are what the contrasts in the next section operate on.

## Challenge IV: testing thousands of genes with contrasts

With the mean model
$$
\log \mu_{gi} = \beta_{g0} + \beta_{g1} x_{\mathrm{DPN}} + \beta_{g2} x_{\mathrm{OHT}} + \beta_{g3}
x_{48h} + \beta_{g4} x_{\mathrm{pat2}} + \beta_{g5} x_{\mathrm{pat3}} + \beta_{g6} x_{\mathrm{pat4}}
+ \beta_{g7} x_{\mathrm{DPN:}48h} + \beta_{g8} x_{\mathrm{OHT:}48h}
$$
(the intercept $\beta_{g0}$ is the log mean expression in the Control group at 24h, patient 1), any
comparison of biological interest is a linear combination of the $\beta$'s — a **contrast**.
Reading off two group means and subtracting gives, for example,
$$
\text{DPN vs Control, 24h: } \delta_g = \beta_{g1}, \qquad \text{DPN vs Control, 48h: } \delta_g =
\beta_{g1} + \beta_{g7},
$$
and symmetrically for OHT with $\beta_{g2}, \beta_{g8}$. The interaction coefficients answer a
different question — not "is DPN different from control", but "does the *time* effect differ
between DPN and control" — and reduce to $\delta_{\mathrm{DPN-con}} = \beta_{g7}$,
$\delta_{\mathrm{OHT-con}} = \beta_{g8}$, and $\delta_{\mathrm{OHT-DPN}} = \beta_{g8} - \beta_{g7}$
for the three pairwise interaction comparisons.

Every one of these is a row of weights against the model's coefficients, assembled into a contrast
matrix $\mathbf{L}$ (one column per hypothesis), and each column is tested separately — here with
a likelihood-ratio test — against the fitted GLM. Because the test is repeated for every gene, each
contrast produces its own p-value histogram; and because the test is repeated across thousands of
genes for the *same* contrast, the p-values need a multiple-testing correction (FDR) before
counting how many genes are called differentially expressed at, say, 5%.

Testing the treatment contrasts this way turns up only a small number of differentially expressed
genes — unsurprising, given how small the treatment effect already looked in the MDS plot. A
**time** contrast, averaged across the three treatments,
$$
\log\left(\frac{\mu_{g,48h}}{\mu_{g,24h}}\right) = \beta_{g3} + \tfrac13(\beta_{g7} + \beta_{g8}),
$$
gives a p-value distribution sharply peaked near zero and many more significant genes — again
consistent with time, not treatment, being the dominant signal once patient is accounted for. For
a single contrast, a volcano plot (log fold-change against $-\log_{10}$ p-value) and an MD-plot
(log fold-change against average log expression, with the DE genes highlighted) are the usual way
to look at the result gene by gene, and plotting the raw counts against the model's fitted values
for the genes with the largest fold-changes checks that the model is actually tracking the data.

## Alternative parameterizations

The same mean model can be written with a different design matrix — for instance, dropping the
intercept and giving every treatment x time combination its own coefficient (plus a patient term),
so that each coefficient is directly a group mean rather than a difference from a baseline. The two
parameterizations describe the same fitted model: a comparison such as "DPN vs control at 24h"
comes out numerically identical whether it is read off as $\beta_{g1}$ in the first
parameterization or as the difference of two group-mean coefficients in the second, and a contrast
built in the second parameterization reproduces the same p-values as the corresponding contrast in
the first. Which parameterization is more convenient is purely a matter of which contrasts are
easiest to write down for the comparisons at hand.

The lecture closed by flagging, rather than working through, a further issue: that none of this is
worth much if the analysis cannot be reproduced by someone else, and pointed to a lecture by Keith
Baggerly on reproducibility in high-throughput biology as further, external viewing.

## Sources

All from the statOmics SGA21 lecture *Sequencing: RNA-seq data intro*
(`sequencing_rnaseqIntro.Rmd`), split into seven linked parts in the library:

- Dataset and pipeline overview — `01-introduction.md`.
- Experimental design, technical vs. biological replication, `SummarizedExperiment`, independent
  filtering, and the MDS exploration — `02-experimental-design-data-import-and-data-exploration.md`.
- Mean-variance exploration and the negative-binomial/Gamma-Poisson argument (Challenge I) —
  `03-challenge-i-choice-of-modeling-assumptions.md`.
- MD-plots, offsets, TMM, median-of-ratios, full-quantile normalization, and the note on
  normalization uncertainty (Challenge II) — `04-challenge-ii-normalization.md`.
- Mean-model structure, empirical Bayes, and dispersion shrinkage (Challenge III) —
  `05-challenge-iii-parameter-estimation-under-limited-information.md`.
- Contrasts, multiple testing, and the time-effect contrast (Challenge IV) —
  `06-challenge-iv-statistical-inference-across-many-genes.md`.
- The no-intercept reparameterization and the reproducibility aside — `07-alternative-parameterizations.md`.

Referred to but not contained in this material: the original dataset paper, Haglund *et al.*
(2012, *JCEM*); Robinson & Oshlack (2010) on TMM; Love, Huber & Anders (2014) on the DESeq2
median-of-ratios method; Dudoit *et al.* (2002) on MD/MA-plots; Bolstad *et al.* (2003) on
full-quantile normalization; a StatQuest video on DESeq2 normalization; a linked page on offsets
versus count scaling (`sequencing_scalingNormalization`, covered in a separate part of this
course); David Robinson's blog post and book on empirical Bayes via baseball statistics; a lecture
by Keith Baggerly on reproducible research in high-throughput biology; and several figures shown
in the original slides (the paper's experimental-design paragraph, its model-specification
paragraph, and diagrams of the empirical-Bayes-shrinkage and normalization-uncertainty arguments)
that were not present as reproducible material here.

---

[← 32. Negative Binomial Model](32-negative-binomial-model.md) · [Contents](index.md) · [34. Scaling Normalization and Offsets →](34-scaling-normalization-and-offsets.md)
