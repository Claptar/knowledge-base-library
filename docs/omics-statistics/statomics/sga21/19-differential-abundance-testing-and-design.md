---
title: "19. Differential Abundance Testing and Design"
course: "StatOmics Sga21"
chapter: 19
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 19. Differential Abundance Testing and Design

## What this covers

This chapter answers the question: once a proteomics experiment has produced a table of
protein-level intensities, how do you decide which proteins actually differ between two
conditions, and how do you design the experiment so that the answer is trustworthy? It follows a
single worked case — wild-type versus a knockout mutant of the bacterium *Francisella tularensis*
— from a single protein's t-test, through the problem of testing thousands of proteins at once, to
the "moderated" test statistics that proteomics software actually uses, and finally to the two
design choices (sample size and blocking) that determine how much power any of this has. It
assumes the reader already has the ordinary two-sample t-test, the linear model, and the vocabulary
of hypothesis testing (null and alternative hypotheses, p-values, type I error), and that
protein-level intensities have already been produced by a preprocessing pipeline — log-transforming,
filtering out contaminants and singleton peptides, normalising, and summarising peptides to
proteins — which is treated elsewhere in the course and only sketched here.

## Case study: a transporter knockout in *Francisella tularensis*

*Francisella tularensis* is the pathogen that causes tularemia. Its intracellular life cycle
depends on rapid metabolic adaptation: after entering a host cell it escapes the phagosome quickly
and multiplies in the cytosol. The bacterium is auxotrophic for several amino acids, including
arginine, so it depends on transporting arginine in from the host. Knocking out the arginine
transporter (the gene *argP*) delays both phagosomal escape and intracellular multiplication —
which motivates asking exactly which proteins in the bacterium's own proteome shift in abundance
when that transporter is disabled.

The experiment compares three wild-type (WT) replicates against three *argP* knockout (KO, labelled
`D8`) replicates. Peptide-level MS1 intensities from MaxQuant are read in, peptides mapping to
non-unique protein groups, decoy/reverse hits, contaminants and peptides seen in only one sample are
filtered out, the remaining intensities are log2-transformed and median-centred, and peptides are
summarised (robustly) to protein-level intensities. After this pipeline, **1066 proteins** remain,
each with six intensity values: three WT, three KO. That $m = 1066$ and that $n_1 = n_2 = 3$ are the
two numbers that drive everything that follows.

## From an experiment to a test statistic

For a single protein, the quantity of interest is the log2 fold change between the two group means:

$$
\log_2 \text{FC} = \bar{y}_{p1}-\bar{y}_{p2}
$$

and the test statistic is this fold change scaled by its own uncertainty — signal over noise:

$$
T_g=\frac{\log_2 \text{FC}}{\text{se}_{\log_2 \text{FC}}} = \frac{\widehat{\text{signal}}}{\widehat{\text{Noise}}}
$$

If the two groups are assumed to have equal variance, the standard error of the fold change has the
familiar two-sample form

$$
\text{se}_{\log_2 \text{FC}}=\text{SD}\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}
$$

so $T_g$ is exactly the statistic of an ordinary two-sample t-test with equal variances, computed
separately, protein by protein, on the log2 intensities. Fitting `lm(intensity ~ genotype)` (or
equivalently `t.test(..., var.equal = TRUE)`) for one protein gives its estimated log2 fold change,
the standard error of that estimate, and their ratio $t$ — the same quantity computed three
different ways.

## Null and alternative hypotheses, and what a p-value actually means

Data can never *prove* a hypothesis — this is Popper's falsification principle — it can only reject
one. So the working direction is reversed from what you actually want to show:

- $H_1$ (what you want to demonstrate): on average, the protein's abundance in WT differs from its
  abundance in KO.
- $H_0$ (what you actually test): on average, the protein's abundance in WT equals its abundance in
  KO.

You show $H_1$ indirectly, by falsifying $H_0$. Given the observed $t$ for a protein, the question
becomes: *how likely is it to observe a $t$ this large, or larger in magnitude, if $H_0$ is true and
there is really no effect of the knockout?* Once a distribution is assumed for the test statistic
under $H_0$ (here, a t-distribution), that probability is the **p-value** — and it is only correct
if the assumptions behind that distribution actually hold. If the p-value falls below a chosen
significance level $\alpha$, $H_0$ is rejected; doing so controls the probability of a false
positive (a type I error) at $\alpha$. A fact worth keeping in mind for what follows: **when $H_0$
is true, p-values are uniformly distributed** — every value between 0 and 1 is equally likely.

## The multiple testing problem

Now scale this up: the experiment tests all $m = 1066$ proteins simultaneously, one t-test each. If
each individual test is run at level $\alpha = 0.05$, the probability of at least one false
positive *somewhere* among the 1066 tests is far larger than 0.05. In a typical experiment most
proteins are not truly differentially abundant, and each of those non-DA proteins still has a 5%
chance of returning a false positive on its own. Treating all $m$ proteins as non-DA (the
conservative case) gives an upper bound on the number of false positives you should expect of

$$
m \times \alpha = 1066 \times 0.05 \approx 53.
$$

Testing every protein at the same uncorrected $\alpha$ therefore guarantees calling dozens of
proteins "significant" purely by chance, every time the experiment is run. Some correction for
testing many hypotheses at once is unavoidable.

## Controlling error across many tests

### Family-wise error rate and Bonferroni

The **family-wise error rate (FWER)** stops controlling the type I error of each individual test
and instead controls the probability of *any* false positive across the whole family of tests:

$$
\text{FWER} = \text{P}\left[FP \geq 1 \right].
$$

The classical way to control it is the **Bonferroni method**: test each hypothesis at the much
stricter level

$$
\alpha_\text{adj} = \frac{\alpha}{m}
$$

or, equivalently, adjust each p-value upward and compare it to the original $\alpha$:

$$
p_\text{adj} = \min\left(p \times m,\, 1\right).
$$

For the Francisella data, $\alpha_\text{adj} = 0.05 / 1066 \approx 4.7\times 10^{-5}$ — a single
protein needs an extremely small raw p-value to survive. Bonferroni does control the FWER, but at a
cost: **the method is very conservative**, and controlling the chance of even a single false
positive across a thousand-plus tests throws away a great deal of power.

### False discovery rate and the Benjamini–Hochberg procedure

The alternative, due to Benjamini and Hochberg (1995), controls a different and more forgiving
quantity: the expected *proportion* of false positives among the results you actually report,
rather than the chance of having any at all.

Define the **false discovery proportion**

$$
FDP = \frac{FP}{R},
$$

the fraction of the $R$ rejected hypotheses that are, in truth, false positives. $FDP$ cannot be
observed directly — you know how many hypotheses you rejected ($R$) but not how many of those
rejections were wrong ($FP$). The **false discovery rate (FDR)** is its expectation:

$$
\text{FDR} = \text{E}\left[\frac{FP}{R}\right] = \text{E}\left[\text{FDP}\right].
$$

Controlling the FDR (rather than the FWER) allows longer lists of significant results while still
keeping the average fraction of false ones among them under control — so more of the true positives
get detected.

**A worked intuition.** Suppose $m = 1000$ tests, and a threshold of $p < 0.01$ is used. If all
null hypotheses were true ($m_0 = m = 1000$, the conservative case), you would expect
$0.01 \times 1000 = 10$ false positives among the rejections. If the actual number of proteins
found with $p < 0.01$ is $R = 200$, the estimated FDP is

$$
\widehat{\text{FDP}} = \frac{FP}{R} = \frac{10}{200} = \frac{0.01 \times 1000}{200} = 0.05.
$$

Controlling the FDR at $\alpha$ generalises this reasoning across all thresholds at once. The
**Benjamini–Hochberg (BH) procedure**:

1. Order the $m$ p-values ascending: $p_{(1)} \leq \ldots \leq p_{(m)}$.
2. Find the largest integer $k$ such that
   $$
   \frac{p_{(k)} \times m}{k} \leq \alpha \qquad\text{equivalently}\qquad p_{(k)} \leq \frac{k\,\alpha}{m}.
   $$
3. If such a $k$ exists, reject all $k$ null hypotheses corresponding to $p_{(1)},\ldots,p_{(k)}$.
   If no such $k$ exists, reject none.

The **adjusted p-value** (the $q$-value of the FDR literature) is

$$
q_{(i)} = \tilde{p}_{(i)} = \min\left[\min_{j = i,\ldots,m}\left(\frac{m\,p_{(j)}}{j}\right),\, 1\right],
$$

and comparing $q_{(i)}$ to $\alpha$ gives the same rejections as the rank-based rule above.

### Applying it to the Francisella data

Running BH on the 1066 t-tests in this experiment is dramatic: only **two** proteins fail to reach
significance at 5% FDR. Sorted by increasing p-value, the last two entries in the whole ranked list
— rank 1065 and rank 1066 out of 1066 — are `WP_003040562` ($p = 0.998$) and `WP_003041130`
($p = 0.999$); every other protein is called differentially abundant. Both criteria for these two
agree that they should *not* be rejected: their raw p-values exceed their rank-dependent BH
threshold ($k\,\alpha/m$, here $\approx 0.05$ since $k$ is close to $m$), and their adjusted
p-values exceed $\alpha = 0.05$. Contrast this with the Bonferroni threshold computed above,
$\approx 4.7\times 10^{-5}$: almost the entire proteome differs between WT and KO under BH's
looser, proportion-based criterion, while Bonferroni's guarantee against even one false positive
would be far harder to meet. A volcano plot — log2 fold change against $-\log_{10}(p)$, coloured by
whether the adjusted p-value is below 0.05 — is the usual way to see this at a glance.

## Moderated statistics: why the ordinary t-test misbehaves here

With only three replicates per genotype, each protein's within-group standard deviation is
estimated from just 4 degrees of freedom — an inherently noisy estimate. Plotting the standard
error against the fold change for every protein, coloured by significance, shows the problem
directly: many of the proteins flagged as significant by the ordinary t-test have an *implausibly
small* estimated standard error, not necessarily a large fold change. A t-statistic can become huge
simply because the denominator — the noise estimate — happened, by chance, to come out tiny for
that one protein; plotting the raw intensities for some of these "significant" proteins shows
points that barely differ within each genotype, which is exactly what a spuriously small variance
estimate looks like.

The general fix is a class of **moderated test statistics**:

$$
T_g^{mod} = \frac{\bar{Y}_{g1} - \bar{Y}_{g2}}{C\;\tilde{S}_g},
$$

where $C$ depends on the design (e.g. $\sqrt{1/n_1 + 1/n_2}$ for a t-test) and $\tilde{S}_g$ is a
*moderated* standard deviation estimate, rather than the protein's own raw $S_g$.

**The ad hoc route** (used in the software Perseus) simply adds a small positive constant:
$\tilde{S}_g = S_g + S_0$. This shrinks the influence of small variance estimates, but it has real
problems: the choice of $S_0$ is arbitrary, the resulting statistic is no longer t-distributed, a
permutation test to recalibrate it is difficult for anything beyond the simplest designs, and
because the analyst is free to pick $S_0$, the approach opens the door to data dredging — tuning the
correction until the result looks the way you want.

**The principled route is empirical Bayes**, which provides a formal statistical framework for
*borrowing strength across proteins* to estimate variance, rather than trusting each protein's own
noisy estimate in isolation. It is implemented in the widely used Bioconductor packages **limma**
and **msqrob2**. The moderated standard deviation is a weighted combination of the protein's own
variance and a common variance shared across all proteins:

$$
\tilde{S}_g = \sqrt{\frac{d_g S_g^2 + d_0 S_0^2}{d_g + d_0}},
$$

where $S_0^2$ is the common variance estimated over all proteins together. The resulting moderated
t-statistic is t-distributed with $d_0 + d_g$ degrees of freedom — **more** degrees of freedom than
the protein's own $d_g$, because borrowing information across proteins effectively adds information.
The consequence for the shrinkage itself: proteins with a small individual variance are pulled
*up*, towards the common variance, giving them a larger (more honest) moderated variance; proteins
with a large individual variance are pulled *down*. Because the pooled degrees of freedom are
larger, the resulting moderated variance estimates are, on the whole, better estimates of the truth
than the individual per-protein ones.

Refitting the Francisella data with the empirical-Bayes estimator (rather than the plain t-test)
changes the volcano plot noticeably: it "opens up," because proteins are no longer flagged as
significant purely for having an accidentally tiny variance estimate — borrowing strength across
proteins fixes exactly the failure mode described above.

## A linear model per protein: the msqrob2 workflow

In practice the test is run through a linear model rather than by hand-coding a t-test. Each
protein's log2 intensities are modelled with `genotype` as the only predictor
(`formula = ~genotype`), which produces two model parameters: an intercept and a coefficient for
the knockout genotype (`genotypeD8`). These give two fitted group means:

$$
\text{E}[Y\mid \text{genotype}=\text{WT}] = \text{(Intercept)}, \qquad
\text{E}[Y\mid \text{genotype}=\text{D8}] = \text{(Intercept)} + \text{genotypeD8}.
$$

The average log2 fold change between KO and WT is exactly the second coefficient:

$$
\log_2\text{FC}_{D8-WT} = \text{E}[Y\mid \text{D8}] - \text{E}[Y\mid \text{WT}] = \text{genotypeD8},
$$

so testing "no differential abundance" is testing $H_0:\ \text{genotypeD8} = 0$ — a contrast on a
single model coefficient, tested with the moderated (empirical Bayes) statistic described above,
protein by protein. The list of significant proteins at 5% FDR, and the accompanying volcano plot,
follow directly from this contrast.

<figure>
<svg viewBox="0 0 340 230" role="img" aria-label="A population's true effect connects to an observed sample through experimental design going one way and estimation and inference going the other">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="20" y="12" width="300" height="60" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2"/>
  <text x="170" y="30" text-anchor="middle" font-size="12" fill="currentColor">Population</text>
  <text x="170" y="48" text-anchor="middle" font-size="11" fill="currentColor">true effect of the argP knockout</text>

  <rect x="20" y="158" width="300" height="60" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2"/>
  <text x="170" y="176" text-anchor="middle" font-size="12" fill="currentColor">Sample</text>
  <text x="170" y="194" text-anchor="middle" font-size="11" fill="currentColor">3 WT vs 3 KO measurements</text>

  <line x1="115" y1="72" x2="115" y2="158" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="70" y="118" text-anchor="middle" font-size="11" fill="currentColor">experimental</text>
  <text x="70" y="130" text-anchor="middle" font-size="11" fill="currentColor">design</text>

  <line x1="225" y1="158" x2="225" y2="72" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="270" y="118" text-anchor="middle" font-size="11" fill="currentColor">estimation</text>
  <text x="270" y="130" text-anchor="middle" font-size="11" fill="currentColor">and inference</text>
</svg>
<figcaption>The relationship a hypothesis test stands in for: experimental design determines how the
sample is drawn from the population; estimation and inference are the (uncertain) route back from
the sample to a statement about the population.</figcaption>
</figure>

## Experimental design: sample size and blocking

### Sample size and power

The same three formulas govern design as govern testing:

$$
\log_2 \text{FC} = \bar{y}_{p1}-\bar{y}_{p2}, \qquad
T_g=\frac{\log_2 \text{FC}}{\text{se}_{\log_2 \text{FC}}}, \qquad
\text{se}_{\log_2 \text{FC}} = \text{SD}\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}.
$$

Since the standard error shrinks as $n_1$ and $n_2$ grow, increasing the number of biological
replicates directly increases the test statistic for a true effect of fixed size — i.e. it
increases the power of the experiment to detect it. (The course points to a study of
tamoxifen-treated, oestrogen-receptor-positive breast cancer patients as a further illustration of
this design trade-off.)

### Sources of variance and blocking

Total variance in a proteomics measurement is a sum of contributions from several sources:

$$
\sigma^2 = \sigma^2_{bio} + \sigma^2_\text{lab} + \sigma^2_\text{extraction} + \sigma^2_\text{run} + \ldots
$$

Some of these are **biological** — fluctuations in protein level between mice, or between cells —
and some are **technical**: cage effects, lab effects, week effects, differences between plasma
extractions, differences between mass-spec runs. Left unaccounted for, technical sources of
variation inflate $\sigma^2$ and drown out the biological signal.

**Blocking** is the design response: arrange the experiment so that all treatments of interest are
present within each block (e.g. within each mouse), rather than each mouse receiving only one
treatment. This makes it possible to estimate the treatment effect *within* each block and then
isolate the between-block variability from the analysis, using a linear model with the blocking
variable as an additional term, e.g.

$$
y \sim \text{type} + \text{mouse}
$$

for a design comparing cell types within the same mice (after Duguet et al., 2017, *MCP*
16(8):1416–1432). This is not possible in software such as Perseus, which does not support
arbitrary linear-model designs. The course poses this as something to work through directly in the
tutorial: comparing a **completely randomised design**, where each mouse contributes only one cell
type (Treg or Tconv), against a **randomised complete block design**, where both cell types are
assessed on every mouse — and seeing what blocking buys in terms of power for the same number of
mice.

## Sources

- `docs/omics-statistics/statomics/sga21/pda_quantification_inference/01-introduction.md`,
  `02-francisella-tularensis-experiment.md` and `03-experimental-design.md`, converted from
  `pda_quantification_inference.Rmd` (statOmics/SGA21 repository, commit
  `0ad787d4cc2bb2f4636440840a8a923cf6c09839`), licensed CC BY-NC-SA 4.0. This is the entirety of the
  supplied material for this chapter; no slides, transcript or problem set were supplied separately
  — the case study, all formulas, the multiple-testing and moderated-statistics discussion, and the
  experimental-design material are all drawn from these three files.
- The biological background on *Francisella tularensis* and the argP transporter, the experimental
  design (3 WT vs 3 KO), the preprocessing pipeline summary, and the numerical results (m = 1066
  proteins; the BH results table; the Bonferroni threshold) are from
  `02-francisella-tularensis-experiment.md`.
- The hypothesis-testing framework (Popper falsification, $H_0$/$H_1$, p-value definition), the
  FWER/Bonferroni and FDR/Benjamini–Hochberg material, and the moderated-statistics and
  empirical-Bayes discussion are also from `02-francisella-tularensis-experiment.md`.
- The sample-size and blocking material, including the mouse T-cell design (Duguet et al., 2017)
  and the completely-randomised-vs-block-design comparison for the tutorial, is from
  `03-experimental-design.md`.
- Referred to but not contained in the supplied material: the course's Part I on preprocessing
  (linked from `01-introduction.md` as a separate video playlist and a separate `.Rmd`); the
  Benjamini and Hochberg (1995) paper itself, *Journal of the Royal Statistical Society Series B*,
  57(1):289–300; the Nature Methods "Points of Significance: Blocking" article
  (nature.com/articles/nmeth.3005); the Duguet et al. (2017) *MCP* paper and its figure of the mouse
  T-cell design; the figures `francisella.jpg`, `tularemia_lesion.jpg` and `limmaShrinkage.png`
  (the last credited in the source to Rafael Irizarry); and the bibliography entries cited in
  `03-experimental-design.md` as `[@goeminne2016]`, `[@goeminne2020]` and `[@sticker2020]`, none of
  which were resolved in the supplied files.

---

[← 18. Import Data and Preprocessing](18-import-data-and-preprocessing.md) · [Contents](index.md) · [20. Proteomics Hypothesis Testing and Design →](20-proteomics-hypothesis-testing-and-design.md)
