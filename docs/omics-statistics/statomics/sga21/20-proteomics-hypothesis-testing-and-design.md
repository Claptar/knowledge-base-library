---
title: "20. Proteomics Hypothesis Testing and Design"
course: "StatOmics Sga21"
chapter: 20
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 20. Proteomics Hypothesis Testing and Design

## What this covers

This chapter follows one real differential-abundance analysis — wild-type versus arginine-transporter
knockout *Francisella tularensis* — from a single protein to nearly eleven hundred of them, to build up
the three ideas that make quantitative proteomics testing work: what a hypothesis test on one protein
actually claims, why testing every protein at the usual 5% level stops being safe once there are
thousands of proteins, and why the ordinary variance estimate a t-test relies on is too noisy to trust
protein by protein — which is what empirical-Bayes moderation repairs. It ends with the other half of
the same problem: how the size and structure of an experiment — replication and blocking — fix how much
power any of this machinery can have before a single measurement is taken. It assumes the peptide-to-protein
pipeline (log-transformation, filtering, normalisation, summarisation to protein level) and ordinary
least-squares regression and t-tests as background.

## The experiment

*Francisella tularensis* causes tularemia. Like many intracellular pathogens it depends on metabolic
adaptation to survive inside a host cell: after entering, it must escape the phagosome quickly and
multiply in the cytosol. Francisella is auxotrophic for several amino acids, including arginine, so it
needs an arginine transporter to get the amino acid from its host. Knocking that transporter out (the
ArgP mutant) delays both phagosomal escape and intracellular multiplication — a plausible mechanism, but
one that should leave a mark on the bacterium's own proteome if it is right. The experiment compares the
proteome of 3 wild-type (WT) replicates against 3 ArgP-knockout (D8) replicates.

The raw output is peptide-level MS1 intensities from MaxQuant. Getting from there to one number per
protein per sample goes through the preprocessing steps: peptides with zero intensity are treated as
missing rather than zero, intensities are log2-transformed, peptides that cannot be assigned to a unique
protein group, decoys and contaminants, and peptides seen in only one sample are dropped, the remaining
intensities are normalised by median-centering each sample, and peptides are aggregated (robustly) to a
protein-level summary. What is left after filtering is a matrix of $m = 1066$ proteins by 6 samples (3 WT,
3 D8) — the object every test in this chapter operates on.

## Testing one protein

Fix a single protein and ask: is its average abundance different between WT and the knockout? Two
quantities do all the work. The estimated log2 fold change is the difference of the two group means of
log2 intensity,

$$
\log_2\text{FC} = \bar y_{p1}-\bar y_{p2},
$$

and the test statistic standardises it by its own uncertainty,

$$
T_g=\frac{\log_2\text{FC}}{\text{se}_{\log_2\text{FC}}} = \frac{\widehat{\text{signal}}}{\widehat{\text{noise}}}.
$$

If the two groups are assumed to have equal variance, that standard error has a closed form in terms of
the pooled standard deviation and the two group sizes,

$$
\text{se}_{\log_2\text{FC}} = \text{SD}\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}.
$$

Fitting `intensity ~ genotype` for one protein (`WP_003023392` in the lecture) with ordinary least
squares reproduces exactly this ratio: the fitted genotype coefficient is the log2 fold change, its
standard error is $\text{se}_{\log_2\text{FC}}$, and their ratio is the $t$ read off the regression
summary.

The logic that gives that $t$ a meaning is Popper's: data can never *prove* a hypothesis, only falsify
one. So the analysis is framed the other way around from what is actually of interest. What we want to
show is the *alternative* hypothesis,

$H_1$: on average, protein abundance in WT differs from KO,

but what gets tested is its negation,

$H_0$: on average, protein abundance in WT equals KO.

A p-value answers a precise question about $H_0$: if the null were true, how likely would it be to see an
effect at least as extreme as the one observed? For the one protein above, running `t.test()` with equal
variances gives a p-value on the order of a few parts per million — tiny — which is the number quoted
against a significance threshold $\alpha$ (conventionally 0.05). Two things about this number matter
before it can be trusted: the calculation is only correct if the assumptions behind it (normality, equal
variance) hold, and, crucially, **p-values are uniform under the null** — if $H_0$ really is true, every
value between 0 and 1 is equally likely, which is exactly the fact the next section needs.

<figure>
<svg viewBox="0 0 340 270" role="img" aria-label="A true effect sits in the population; the experimental design draws a noisy sample from it; estimation and inference reason back from the sample to a claim about the population">
  <rect x="40" y="10" width="240" height="80" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="50" y="28" font-size="12" fill="currentColor">population</text>
  <circle cx="160" cy="58" r="26" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="160" y="62" text-anchor="middle" font-size="11" fill="currentColor">true effect</text>

  <rect x="40" y="170" width="240" height="80" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="50" y="188" font-size="12" fill="currentColor">sample</text>
  <circle cx="120" cy="215" r="5" fill="currentColor"/>
  <circle cx="140" cy="222" r="5" fill="currentColor"/>
  <circle cx="130" cy="235" r="5" fill="currentColor"/>
  <circle cx="190" cy="215" r="5" fill="none" stroke="currentColor"/>
  <circle cx="210" cy="222" r="5" fill="none" stroke="currentColor"/>
  <circle cx="200" cy="235" r="5" fill="none" stroke="currentColor"/>
  <text x="112" y="252" font-size="11" fill="currentColor">3 WT</text>
  <text x="182" y="252" font-size="11" fill="currentColor">3 KO</text>

  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="70" y1="92" x2="70" y2="168" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="8" y="132" font-size="11" fill="currentColor">design</text>
  <line x1="250" y1="168" x2="250" y2="92" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="255" y="132" font-size="11" fill="currentColor">inference</text>
</svg>
<figcaption>The effect of the knockout on the protein is a fixed but unknown property of the population
(top). The experimental design determines how a sample — here 3 WT and 3 KO replicates — is drawn from it
(down arrow). Estimation and inference reason back from that noisy sample to a probabilistic claim about
the population effect (up arrow), which is exactly what a p-value is doing.</figcaption>
</figure>

## Testing many proteins at once: the multiple-testing problem

Now repeat that test for every one of the $m = 1066$ proteins in the dataset simultaneously. If each test
is individually run at level $\alpha = 0.05$, the individual guarantee — a 5% chance of a false positive
*for that one protein* — does not scale up to a 5% chance of a false positive somewhere in the whole list.
In a typical experiment most proteins are genuinely not differentially abundant, and each of those has an
independent 5% chance of being called a false positive by chance alone. With $m_0 \approx m$ non-DA
proteins, the expected number of false positives is of order $m\times\alpha$ — here
$1066\times 0.05\approx 53$ — regardless of how the true effects are distributed. Testing at the usual
per-protein $\alpha$ therefore guarantees a large number of false calls every time the experiment is run.

**Family-wise error rate.** One way to regain control is to stop guaranteeing something about each
individual test and instead control the probability of *any* false positive across the whole list:

$$
\text{FWER} = \text{P}\left[FP \geq 1\right].
$$

The Bonferroni method controls FWER by testing each protein at the much stricter level
$\alpha_\text{adj} = \alpha/m$, or equivalently by comparing an adjusted p-value
$p_\text{adj} = \min(p\times m, 1)$ against $\alpha$. For this dataset, $\alpha_\text{adj} = 0.05/1066
\approx 4.7\times10^{-5}$ — a bar few proteins will clear even when the effect is real. Bonferroni is
correct but very conservative: it is built to guard against even one false positive across the whole
list, and pays for that in lost power everywhere else.

**False discovery rate.** A less punishing target is the *proportion* of false positives among the
proteins actually called significant, rather than the chance of even one. The false discovery
proportion,

$$
\text{FDP} = \frac{FP}{R},
$$

is the fraction of false positives among the $R$ rejections — but it cannot be observed directly, because
$R$ is known once the test is run while $FP$ is not. Benjamini and Hochberg (1995) defined the **false
discovery rate** as the expectation of this unobservable quantity,

$$
\text{FDR} = \text{E}\left[\frac{FP}{R}\right] = \text{E}[\text{FDP}].
$$

Controlling FDR at, say, 1% means that on average 1% of the proteins on the significant list are false
positives — a statement about the *list*, not about any one protein on it. Because it tolerates a
controlled fraction of errors rather than forbidding any, controlling FDR allows longer lists of
discoveries than Bonferroni for the same nominal level, catching more of the true positives.

A small worked example makes the logic concrete. Suppose $m = 1000$ tests, and a researcher rejects every
null with $p < 0.01$. Conservatively assuming *all* $m$ nulls are true, the number of false positives
expected at that cutoff is $0.01\times 1000 = 10$. If the researcher actually observes $R = 200$ genes
with $p < 0.01$, the estimated false discovery proportion among that list is

$$
\widehat{\text{FDP}} = \frac{FP}{R} = \frac{10}{200} = \frac{0.01\times 1000}{200} = 0.05.
$$

The **Benjamini–Hochberg procedure** turns this into an algorithm. Order the p-values
$p_{(1)}\le\cdots\le p_{(m)}$, and find the largest $k$ such that

$$
\frac{p_{(k)}\times m}{k}\le\alpha \qquad\text{equivalently}\qquad p_{(k)}\le \frac{k\alpha}{m}.
$$

If such a $k$ exists, reject the $k$ nulls corresponding to $p_{(1)},\dots,p_{(k)}$; otherwise reject
none. The corresponding adjusted p-value (the $q$-value) is

$$
q_{(i)} = \min_{j = i,\dots,m}\left(\frac{m\, p_{(j)}}{j}\right)\wedge 1.
$$

In the toy example, $k = 200$, $p_{(k)} = 0.01$, $m = 1000$, giving $q_{(200)} = 0.05$ — the estimated FDP
above. Applied to the Francisella data, this is the procedure `p.adjust(pval, "fdr")` runs across all
1066 proteins, and the resulting `adjPval < 0.05` flag is what colours the significant points in a
volcano plot of $-\log_{10}(p)$ against $\log_2\text{FC}$.

## The trouble with the ordinary t-test, and moderated statistics

With only 3 replicates per genotype, the per-protein sample standard deviation is itself a very noisy
estimate — sometimes it comes out small purely by chance, and a small denominator inflates $T_g$
regardless of how small the actual fold change is. Plotting $\text{se}$ against $\log_2\text{FC}$ for the
Francisella proteins shows exactly this: some of the points flagged significant have a negligible fold
change and are only significant because their estimated standard error happened to be tiny.

A general fix replaces the plain sample SD with a **moderated** one,

$$
T_g^{\text{mod}} = \frac{\bar Y_{g1}-\bar Y_{g2}}{C\,\tilde S_g},
$$

where $C$ is a constant fixed by the design (e.g. $\sqrt{1/n_1+1/n_2}$ for a two-group t-test, a different
form for a general linear model) and $\tilde S_g$ is some more stable estimate of the standard deviation
than the raw per-protein $S_g$.

One historical fix, used in the software Perseus, simply adds a small constant, $\tilde S_g = S_g+S_0$.
This has real problems: the choice of $S_0$ is ad hoc, and once it is added the statistic is no longer
t-distributed, so a p-value cannot be read off a t-table — it has to come from a permutation test, which
becomes difficult once the design is more structured than a simple two-group comparison. Worse, because
$S_0$ is a free knob, a user can tune it until the result list looks the way they want — an open door to
data dredging.

**Empirical Bayes** gives a principled version of the same idea, implemented in `limma` and `msqrob2`.
Instead of an arbitrary additive constant, the moderated SD is a precision-weighted average of the
protein's own variance estimate and a variance common to *all* proteins:

$$
\tilde S_g = \sqrt{\frac{d_g S_g^2 + d_0 S_0^2}{d_g+d_0}},
$$

where $S_0^2$ is the variance shared across proteins and $d_g$, $d_0$ are the corresponding degrees of
freedom — $d_g$ from the individual protein's own residuals (small, here around 4 for a 3-vs-3 design),
$d_0$ estimated from the whole dataset (large, because it pools information across roughly a thousand
proteins). The resulting moderated $t$-statistic is exactly t-distributed with $d_0+d_g$ degrees of
freedom: borrowing strength across proteins does not just stabilise the variance estimate, it also
*increases* the effective degrees of freedom every single protein gets to use, which is the formal sense
in which information is being shared.

The effect of this shrinkage is visible directly: plotting each protein's raw SD against its moderated
(posterior) SD against the line $y=x$ shows small raw variances pulled up toward the common value, and
large raw variances pulled down toward it. That is exactly what removes the spurious small-fold-change,
small-SD false positives, and rescues real but noisy large-fold-change proteins that an unstable
individual variance estimate would otherwise have masked — which is why the volcano plot for the
Francisella data changes shape once the ordinary t-test's variance is replaced by the moderated one.

## From t-test to linear model: `msqrob2`

The two-group t-test above is a special case of the linear model `~genotype`, which is how the moderated
version is actually fit in `msqrob2` (by default using robust regression, so a single outlying replicate
does not dominate a protein's estimated mean). The model matrix for `~genotype` has two parameters — an
intercept and a `genotypeD8` coefficient — giving two group means:

$$
\text{E}[Y\mid\text{genotype}=\text{WT}] = \text{(Intercept)}, \qquad
\text{E}[Y\mid\text{genotype}=\text{D8}] = \text{(Intercept)} + \text{genotypeD8}.
$$

Subtracting the two, the average log2 fold change between knockout and wild type is exactly the fitted
coefficient,

$$
\log_2\text{FC}_{D8-WT} = \text{genotypeD8},
$$

so the same null hypothesis as before — no difference between WT and D8 — is now the statement
$H_0: \text{genotypeD8}=0$, tested through a contrast (`makeContrast("genotypeD8 = 0", ...)` followed by
`hypothesisTest()`), with the empirical-Bayes moderated variance from the previous section doing the
standardising. The output is the same shape as before — a ranked list of proteins with fold change,
moderated $t$, p-value and FDR-adjusted p-value — filtered to the proteins significant at 5% FDR, which
can then be inspected as a heatmap across samples, or protein by protein as peptide-level intensities
alongside the summarised protein-level value, to sanity-check that a "hit" is not an artefact of the
summarisation step.

## Experimental design: buying power before the data exist

Everything above operates on a dataset that has already been collected. The standard error formula from
the very first section,

$$
\text{se}_{\log_2\text{FC}} = \text{SD}\sqrt{\frac{1}{n_1}+\frac{1}{n_2}},
$$

says that this is also where power comes from before the experiment is even run: the noise term shrinks
as $1/\sqrt{n}$, so more biological replicates give a larger $T_g$ for the same true effect, and hence
higher power to detect it — this is the reasoning behind sample-size studies such as the one on
tamoxifen-treated, estrogen-receptor-positive breast cancer patients referenced in the lecture.

Replication is only half of what a design controls; where the variance comes from is the other half. The
total variance behind every test in this chapter is really a sum of contributions,

$$
\sigma^2 = \sigma^2_{\text{bio}} + \sigma^2_{\text{lab}} + \sigma^2_{\text{extraction}} + \sigma^2_{\text{run}} + \cdots,
$$

split between genuinely biological sources (fluctuation in protein level between mice, between cells) and
technical ones (cage effects, lab effects, week effects, plasma extraction, the MS run itself). Every one
of these adds noise to the denominator of every test unless the design is built to account for it.

**Blocking** is how a design accounts for it. In the mouse T-cell example (Duguet et al., 2017, *MCP*
16(8):1416–1432), the treatments of interest — different T-cell types — are measured on *every* mouse
rather than one type per mouse. Because all treatments are present within each block (mouse), the
treatment effect can be estimated *within* each mouse, and the between-mouse variability can be isolated
from the comparison altogether by fitting

$$
y \sim \text{type} + \text{mouse}.
$$

That is not something the point-and-click tool Perseus can do — it requires a genuine linear model with
a block term. The contrast this sets up is between a **completely randomised design**, where each mouse
contributes only one cell type (Treg or Tconv, but not both), and the corresponding **randomised complete
block design**, where both are measured on every mouse. Working through the same comparison both ways —
once ignoring the mouse-to-mouse structure and once blocking on it — is the natural way to see directly
how much of $\sigma^2$ blocking removes from the test. Further reading on the general principle is the
*Nature Methods* "Points of Significance" column on blocking.

## Sources

- `docs/omics-statistics/statomics/sga21/pda_quantification_inference_noFrames/01-francisella-tularensis-experiment.md`
  — the Francisella tularensis motivation, the preprocessing pipeline summary, the single-protein t-test,
  the FWER/Bonferroni and FDR/Benjamini–Hochberg sections (including the $m=1000$ worked example and the
  Francisella $m=1066$ application), the moderated-statistics and Perseus-versus-empirical-Bayes
  discussion, and the `msqrob2` model/contrast section.
- `docs/omics-statistics/statomics/sga21/pda_quantification_inference_noFrames/02-experimental-design.md`
  — the sample-size/power argument and the blocking section, including the variance decomposition and the
  mouse T-cell example.

Both are converted from `pda_quantification_inference_noFrames.Rmd` (statOmics/SGA21, commit
`0ad787d`), licensed CC BY-NC-SA 4.0.

Referred to but not contained in the supplied material: the *Nature Methods* "Points of Significance:
Blocking" column (`https://www.nature.com/articles/nmeth.3005.pdf`); Duguet et al. (2017), *Molecular &
Cellular Proteomics* 16(8):1416–1432 (the mouse T-cell dataset itself); the tamoxifen/ER-positive breast
cancer sample-size study mentioned only by name; and a figure on limma's variance shrinkage credited to
Rafael Irizarry, whose content the source text does not reproduce.

---

[← 19. Differential Abundance Testing and Design](19-differential-abundance-testing-and-design.md) · [Contents](index.md) · [21. Preprocessing Quantitative Proteomics Data →](21-preprocessing-quantitative-proteomics-data.md)
