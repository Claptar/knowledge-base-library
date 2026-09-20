---
title: "10. Disease Epigenomics and Genetic Epidemiology"
course: "MIT 6047"
chapter: 10
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. Disease Epigenomics and Genetic Epidemiology

## What this covers

This chapter follows one MIT 6.047 lecture on turning a genome-wide association hit into a disease
mechanism. A GWAS p-value tells you a region co-varies with a trait; it does not tell you which
cell type the effect acts in, which nucleotide is causal, which gene it regulates, or which
direction the causal arrow points. The chapter builds the pipeline the lecture uses to answer those
four questions, working from population-level epidemiology definitions down to two extended case
studies — a sub-threshold cardiac-conduction locus and a set of dispersed non-coding cancer
mutations — where every step is followed through by hand. It assumes the reader already has GWAS,
eQTLs, and the vocabulary of chromatin-state annotation (enhancer, promoter, ENCODE/Roadmap states)
from earlier in the course, plus ordinary least-squares regression and F-testing.

## Epidemiology: definitions and study design

Epidemiology is the study of the **patterns**, **causes**, and **effects** of health and disease
conditions in defined populations. The lecture fixes a small vocabulary before doing anything
genomic with it:

- **Morbidity level** — how sick a given individual is.
- **Incidence** — number of *new* cases per population per time period.
- **Prevalence** — total number of existing cases in a population.
- **Attributable risk** — the rate of disease in an exposed group relative to an unexposed one.
- **Population burden** — years of potential life lost (YPLL), or quality-/disability-adjusted life
  years (QALY/DALY).
- **Syndrome** — signs (observed), symptoms (reported), and other phenomena that co-occur, often
  without an established causal or risk-factor relationship between them.

The prevention challenge, stated plainly, is: determine the disease, determine its cause, and
decide whether, when, and how to intervene.

Determining a cause requires a study design, and the lecture lists the standard experimental-design
principles as they apply to human subjects: **control** (comparison to a baseline or placebo),
**randomization** (difficult to achieve in practice, but needed to ensure mixing), **replication**
(controlling variability in the initial sample), **grouping** (understanding variation between
subgroups), **orthogonality** (testing all combinations of factors/treatments), and the resulting
**combinatorics** of a factorial design, an $n\times n\times n\times\cdots\times n$ table of
conditions. Human subjects add legal and ethical constraints and review boards on top of this;
randomization is often achieved only indirectly, through instrumental variables (a theme the
lecture returns to under Mendelian randomization); and clinical trials are blinded to the patient,
or double-blinded to the doctor as well.

The lecture's own outline for the rest of the material is: genetic epidemiology (GWAS, functional
interpretation, enrichment), molecular epidemiology (meQTLs, EWAS), resolving causality (Mendelian
randomization, applied to genotype and methylation in Alzheimer's disease), and systems genomics
(polygenic risk prediction, sub-threshold loci, and somatic heterogeneity in cancer). The slide
material available for this chapter covers all of these except the EWAS/Mendelian-randomization
statistical machinery itself — see Sources.

## Why a GWAS hit is not a mechanism

A genome-wide association study identifies genomic regions whose allele frequency co-varies with a
trait: a risk allele **G** is more common in patients, allele **A** more common in controls. GWAS
itself, mechanically, is a simple statistical association test (a $\chi^2$ test); the difficulty is
entirely downstream of that test. Three problems recur:

1. Large genomic regions are co-inherited as a block, so a significant SNP rarely *is* the causal
   variant — it only marks one.
2. Genetics on its own does not specify a cell type or a biological process.
3. The GWAS catalog is large (thousands of studies, thousands of individuals each, spanning trait
   categories from digestive and cardiovascular disorders to cancer and quantitative biomarkers)
   and still growing as meta-analyses add power, yet the loci found so far explain only a fraction
   of the heritability estimated for most traits.

The scale of what to test ranges from family-specific risk alleles tied to a known history, through
monogenic protein-coding mutations (best understood, easiest to interpret, but rare), to *all*
coding SNPs with known disease association, to the full set of GWAS associations — by one snapshot,
1,350 significant associations as of mid-2012 — down to every common SNP captured by HapMap/1000
Genomes, and finally the whole genome including rare and private mutations. Screening itself splits
into diagnostic testing (after symptoms appear, to confirm a hypothesis) and predictive testing
(before any symptom, at the newborn, pre-natal, pre-conception, or carrier stage) — which sharpens
a question the rest of the lecture keeps coming back to: **genetics versus biomarkers, cause versus
consequence?**

That question has teeth because coding and non-coding disease burden split very differently by
disease class. For monogenic/Mendelian disease, the Human Genetic Mutation Database (April 2010)
reports 89% of known disease mutations as coding and only 11% as non-coding. For polygenic/complex
disease, the GWAS catalog (Hindorff et al., PNAS 2009) shows the opposite: 12% coding, 88%
non-coding. Genomic medicine's promise — disease mechanism, new target genes, new therapeutics,
personalized medicine — collides with a genuine challenge for complex disease: more than 90% of
disease-associated hits fall outside protein-coding sequence, so the cell type of action, the
causal variant, and the mechanism are all, by default, unknown (Hillmer, *Nature Genetics* 2008).
The lecture's proposed remedy is annotation of the non-coding genome (ENCODE/Roadmap Epigenomics)
and methods for linking enhancers to their regulators and target genes, aiming at six concrete
deliverables: relevant cell type, target genes, causal variant, upstream regulator, relevant
pathways, and intermediate phenotypes (Roadmap Epigenomics, *Nature* 2015; Ernst, *Nature* 2011).

The lecture frames the rest of the material as one reference map of the regulatory genome, applied
to three different situations at once:

| | What GWAS/mutation data looks like | The problem | What's needed |
|---|---|---|---|
| **GWAS hits** | most top hits non-coding, sitting in haplotype blocks | mechanism? cell type? causal variant(s)? | fine-mapping and cell-type assignment |
| **"Hidden" heritability** | many variants of small effect, many false positives | most of the heritability is still unaccounted for | pathway-level burden, prioritized by regulatory annotation |
| **Cancer mutations** | loss-of-function coding, gain-of-function regulatory | coding mutations converge on known genes; regulatory ones look individually heterogeneous | recognizing convergence at the level of a regulatory region or pathway |

## A framework: from locus to mechanism

Dissecting a non-coding genetic association is broken into six steps: establish the relevant
**tissue/cell type**; establish the downstream **target gene(s)**; establish the causal
**nucleotide variant**; establish **upstream regulator** causality; establish **cellular**
phenotypic consequences; and establish **organismal** phenotypic consequences. Equivalently, the
lecture's "reference map of the regulatory genome" moves through the same five layers: regions
(enhancer, promoter, transcribed, repressed) $\to$ cell types (which tissues show the epigenomic
activity) $\to$ target genes (linked via eQTL, activity correlation, or Hi-C) $\to$ nucleotides
(the regulatory consequence of the exact mutation, via conservation and motif disruption) $\to$
regulators (which upstream factor's binding is disrupted). The case studies later in this chapter
walk this pipeline end to end.

## Step 1: finding the relevant cell type

The method, applied to every trait in the GWAS catalog: identify all regions associated with the
trait at a chosen p-value threshold; expand each region to every SNP in its credible interval
(defined by linkage-disequilibrium $R^2 \ge 0.8$ to the lead SNP); test that expanded SNP set for
overlap with tissue-specific enhancers; and keep only the tissues that show significant enrichment
($P<0.001$). Repeating this for every trait (as rows) against every cell type (as columns) builds a
matrix linking traits to the tissues where their genetic signal is concentrated.

The lecture's worked example is Alzheimer's disease (Gjoneska, Pfenning, Mathys, Quon, Kundaje,
Tsai & Kellis, *Nature* 2015). Sampling mouse brain epigenomics across a time course of
neurodegeneration reveals two contrasting signatures: enhancers of immune activation increasing
over the course of disease, and enhancers of neuronal genes being repressed. That observation alone
leaves an obvious question open: **is the immune activation simply a consequence of neuronal
loss**, or is it doing something causal? The genetic evidence answers it — only the *increasing*
(immune) enhancers are enriched for AD-associated SNPs; the neuronal cell types are actually
*depleted* for AD-associated SNPs. Since genetic association reflects a cause rather than a
downstream consequence, this indicates that immune cell dysregulation is itself a causal component
of the disease, not merely a passive reaction to dying neurons — with microglia (the brain's
resident immune cells) and infiltrating macrophages as the candidate cell types.

## Step 2 & 3: fine-mapping the causal nucleotide

Linkage disequilibrium (LD) is "both a blessing and a curse" for exactly the reason step 1 needs
to be followed by fine-mapping. Two contrasting haplotype-frequency tables make the point
concrete. Under linkage **equilibrium** ($r^2=0$):

| | B | b |
|---|---|---|
| **A** | 0.60 | 0.20 |
| **a** | 0.15 | 0.05 |

and under linkage **disequilibrium** ($r^2=0.75$, with $p_A=0.8,\ p_a=0.2,\ p_B=0.75,\ p_b=0.25$):

| | B | b |
|---|---|---|
| **A** | 0.75 | 0.05 |
| **a** | 0.00 | 0.20 |

In the second table only two of the four possible haplotypes appear at any real frequency — there
is no evidence of historical recombination between the two loci, so they are inherited as a block.
That is a **blessing** for the initial mapping step: a handful of tag SNPs can capture a whole
block, which is what makes genome-wide genotyping arrays with far fewer than 12 million markers
work at all. It is a **curse** for fine-mapping: association alone cannot distinguish the causal
SNP from every other SNP that merely co-inherits with it, so the causal variant is unknown in most
GWAS regions until something beyond the association test is brought in.

That something is functional annotation, combined along three lines of evidence (Ward and Kellis,
*Nature Biotechnology* 2012): **epigenomic information** (which SNP sits in an enhancer, and what
that enhancer's linked target gene is), **motif information** (which SNP disrupts a known
transcription-factor binding motif, implicating both the causal variant and its upstream
regulator), and **evolutionary conservation** (a causal variant is more likely to sit in a
conserved motif). SNPs that disrupt a *conserved* regulatory motif are disproportionately the
functionally-associated ones — enriched for lying in regulatory chromatin states and under
sequence constraint — which prioritizes candidates and increases the resolution of the mapping.

The most direct version of this evidence is allele-specific: in a diploid genome where the two
haplotypes have been separately sequenced and phased (the lecture's example is the GM12878 cell
line, maternal and paternal genomes both sequenced), reads can be mapped back to the phased genome
while handling the intervening SNPs and indels, and chromatin activity compared allele by allele. A
single base-pair difference between the two haplotypes at a Zeb1 binding motif —
`CCACACCTGGGC` on the paternal chromosome versus `CCACATCTGGGC` on the maternal one — can then be
correlated directly with a measured difference in chromatin activity between the two alleles: about
as direct as evidence gets that *this exact nucleotide* changes *this exact regulatory element*.

The same logic scales differently depending on how many copies of a variant exist to compare. For
**common** variants, allelic activity can be measured directly in heterozygous individuals or cell
lines. For **rare or somatic** mutations — typically seen only once — there is no heterozygous
population to compare, so the approach instead predicts transcription-factor binding disruption
computationally from sequence and motif information (work credited to Richard Sallari and Xinchen
Wang). All three tiers — common, rare, and everything in between — still draw on the same base
layer of regulatory and epigenomic annotation.

A public tool built around this whole pipeline is **HaploReg** (Ward, Kellis, *Nucleic Acids
Research* 2011, at `compbio.mit.edu/HaploReg`): give it any list of SNPs, or select a GWAS study
outright, and it mines ENCODE and Roadmap epigenomics data — hundreds of assays, dozens of cell
types, conservation scores, and motifs — reporting significant overlaps with links back into a
genome browser.

## Step 4: linking variants to target genes

Three lines of evidence are used to connect a non-coding variant to the gene it actually regulates,
which is not necessarily the nearest gene: **physical** (Hi-C measures direct 3D proximity in the
folded genome), **functional** (correlating an enhancer's activity with a candidate gene's
expression across many cell types), and **genetic** (an eQTL — the SNP's genotype is directly
associated with a specific transcript's expression level).

The lecture's worked example starts from a locus contained within a 2.5 Mb topologically
associating domain, which by proximity alone implicates eight candidate genes. Testing a cohort of
20 individuals homozygous for the risk allele against 18 homozygous for the non-risk allele for
genotype-dependent expression across those eight candidates narrows the field to two eQTL targets,
*IRX3* and *IRX5*, both showing *increased* expression on the risk allele — a gain-of-function
direction of effect. The example is a demonstration of why 3D structure plus expression genetics
together outperform "assign the hit to the nearest gene," which is the default and often wrong
heuristic.

## Molecular epidemiology: the epigenome as an intermediate phenotype

<figure>
<svg viewBox="0 0 480 260" role="img" aria-label="Causal diagram in which confounders and environment act on both the epigenome and disease, genotype acts only through the epigenome, and disease can feed back onto the epigenome">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <circle cx="90" cy="30" r="18" fill="none" stroke="currentColor"/>
  <text x="90" y="35" text-anchor="middle" font-size="13" fill="currentColor">C</text>
  <text x="90" y="58" text-anchor="middle" font-size="11" fill="currentColor">confounders</text>

  <circle cx="330" cy="30" r="18" fill="none" stroke="currentColor"/>
  <text x="330" y="35" text-anchor="middle" font-size="13" fill="currentColor">E</text>
  <text x="330" y="58" text-anchor="middle" font-size="11" fill="currentColor">environment</text>

  <circle cx="60" cy="220" r="18" fill="none" stroke="currentColor"/>
  <text x="60" y="225" text-anchor="middle" font-size="13" fill="currentColor">G</text>
  <text x="60" y="248" text-anchor="middle" font-size="11" fill="currentColor">genome</text>

  <circle cx="210" cy="150" r="22" fill="none" stroke="currentColor"/>
  <text x="210" y="155" text-anchor="middle" font-size="13" fill="currentColor">X</text>
  <text x="210" y="185" text-anchor="middle" font-size="11" fill="currentColor">epigenome</text>

  <circle cx="360" cy="150" r="20" fill="none" stroke="currentColor"/>
  <text x="360" y="155" text-anchor="middle" font-size="13" fill="currentColor">D</text>
  <text x="360" y="183" text-anchor="middle" font-size="11" fill="currentColor">disease</text>

  <circle cx="450" cy="150" r="16" fill="none" stroke="currentColor"/>
  <text x="450" y="155" text-anchor="middle" font-size="13" fill="currentColor">S</text>
  <text x="450" y="178" text-anchor="middle" font-size="11" fill="currentColor">symptoms</text>

  <line x1="76" y1="212" x2="190" y2="159" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="103" y1="43" x2="194" y2="134" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="317" y1="43" x2="226" y2="134" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="334" y1="48" x2="355" y2="131" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="231" y1="142" x2="342" y2="142" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="342" y1="158" x2="231" y2="158" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="380" y1="150" x2="434" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>

  <text x="286" y="132" text-anchor="middle" font-size="11" fill="currentColor">causes</text>
  <text x="286" y="174" text-anchor="middle" font-size="11" fill="currentColor">effects</text>
</svg>
<figcaption>The genome (G) reaches disease (D) only through the epigenome (X); confounders (C) and
environment (E) act on both X and D directly, and D can feed back onto X ("effects"). G alone is
untouched by confounding or by reverse causation from D — the asymmetry a Mendelian-randomization
argument exploits, though the statistical machinery for that argument is not in the slide material
available for this chapter.</figcaption>
</figure>

The diagram names molecular epidemiology's central object: the epigenome (X) sits as an
intermediate molecular phenotype between genotype (G) and disease (D). It can be reached two ways —
directly, genotype to disease, which is what GWAS measures; or via the epigenome, genotype to
epigenome (an **meQTL**) to disease (an **MWAS**, methylome-wide association study). The diagram is
also a warning about the second route: unlike the genome, the epigenome is not causally
one-directional with respect to disease. It can be altered by confounders and environment just as
disease itself can, and it can be a *consequence* of disease rather than (or as well as) a cause —
exactly the "cause versus consequence" question raised earlier for any biomarker.

The concrete dataset behind this section is a joint genotype/epigenome/disease cohort of 750
individuals from the Memory and Aging Project (MAP) and the Religious Order Study (ROS), profiled
in dorsolateral prefrontal cortex. All subjects were cognitively normal on intake, with Alzheimer's
status established afterward by pathology rather than by clinical diagnosis alone (Bennett). On the
same 750 individuals: genotype (roughly 1,000,000 SNPs $\times$ 700 individuals, De Jager);
reference chromatin states, including a nine-state model for brain (active promoter,
promoter/flanking, active enhancer, weak enhancer, gene bodies, active gene bodies, repetitive,
heterochromatin, low signal) alongside liver, blood, lung, GI, skin, muscle, and bone (Bernstein);
and DNA methylation (Illumina 450k array, 450,000 probes $\times$ 700 individuals, De Jager).

Generalizing that cohort to the data-matrix picture used through the rest of the lecture: for
$n=750$ individuals there is a genotype matrix **G** (Affy SNP arrays, imputed against the CEU
1000 Genomes reference panel, about 12,000,000 SNPs), a methylation matrix **M** (the Illumina 450k
array, 450,000 CpG probes), an environment matrix **E** (about 15 clinical covariates that could
otherwise mask the phenotype's true variation — gender, smoking, age, sample batch), and a
phenotype matrix **P** (about 10 different measures of the same underlying disease — clinical
Alzheimer's diagnosis, pathological diagnosis, and neuritic-plaque counts among them).

## Cis-meQTLs: testing genotype against methylation

A **cis-meQTL** is an association, within a chosen genomic window, between a SNP's genotype and a
nearby methylation mark. For methylation mark $m_i$ and SNP $g_j$, fit the linear model

$$m_i = \beta_0 + \beta_1(g_j) + \varepsilon$$

The question is whether adding genotype as a predictor increases predictive accuracy by more than
the model complexity it introduces. Because a model with genotype nests the model without it, this
is answerable with a likelihood-ratio-style test comparing two nested linear models, under the null
hypothesis $H_0:\beta_1=0$ (genotype explains no significant additional variation):

$$\text{LM1: } m_i=\beta_0+\varepsilon \qquad \text{LM2: } m_i=\beta_0+\beta_1(g_j)+\varepsilon$$

with $p$ the number of parameters in LM1, $q$ the number of parameters in LM2, $n$ the sample size,
and RSS the residual sum of squares of each fit. Under the null hypothesis,

$$\frac{(\mathrm{RSS}_{\mathrm{LM1}}-\mathrm{RSS}_{\mathrm{LM2}})/(q-p)}{\mathrm{RSS}_{\mathrm{LM2}}/(n-q)}$$

is distributed as an F distribution with $(q-p,\,n-q)$ degrees of freedom. If the resulting
F-statistic is significant, the null is rejected — that p-value is what a meQTL study reports.
Otherwise, there is no detectable meQTL: the reduction in RSS from adding genotype was too small
relative to the extra complexity it cost the model.

Two alternatives to the F-test are named without further detail: a **permutation** test —
correlate methylation and genotype directly, then repeatedly permute the genotype labels and
recompute the correlation to build an empirical null distribution, reading off an empirical
p-value by comparing the observed correlation to that distribution — and **linear mixed models**
(LMMs) as a further alternative. Once tests like these are run genome-wide, most epigenomic
variability turns out to be genotype-driven, which is the empirical backing for drawing the G
$\to$ X arrow in the diagram above as a strong effect rather than a weak or occasional one.

## Beyond genome-wide significance: weak associations and polygenic architecture

A GWAS's genome-wide-significant hits are only the visible tip of its polygenic architecture.
Ranking all SNPs in a study by association p-value (the lecture's example is type 1 diabetes) and
testing, at every rank, for functional enrichment against an annotation such as enhancers shows the
enrichment does not stop at the top few hits: it peaks tens of thousands of SNPs down the ranked
list, and survives LD pruning (1.6K overlaps within just the top 30K ranked SNPs, 78K overlaps in
total). Restricting to the overlapping enhancer set shows it is concentrated in T-cell-type
enhancers — a panel spanning CD4+ memory and naive subsets, CD8 memory and naive subsets, CD56,
CD3, and stimulated T-cell populations — matching T1D's known immune biology; after LD-pruning at
CEU $r^2>0.2$ the overlap count drops from roughly 50k to 41k independent loci but the enrichment
persists.

Cell-type specificity is much sharper for enhancers than for other annotation classes: T- and
B-cell enrichment shows up for promoters and transcribed regions too, but far less distinctly than
it does for enhancers, which discriminate T-cell from B-cell from other cell types much more
cleanly. Genomically, the signal is not simply an MHC artifact: the MHC region does carry a high
concentration of overlapping loci (unsurprising for an immune trait), but thousands of distinct
loci elsewhere in the genome show the same enrichment pattern.

## Polygenic risk prediction

The basic study design has three cohorts. A **training cohort** (genotype and phenotype, where
statistical power matters) is used for SNP selection, effect-size estimation, and ranking. A
**testing cohort** (genotype and phenotype, power still matters) applies the resulting predictor
and evaluates its accuracy. A **target cohort** — genotyped individuals with no known phenotype,
evaluated one at a time, so power is limited to that single individual — has the predictor applied
with an estimated confidence. The testing-cohort application answers population-level questions:
how much heritability is captured by common variants, how many SNPs the trait's genetic
architecture actually involves, and which functional classes carry weak-but-real associations. The
target-cohort application is individual-level: giving health recommendations, or prioritizing
high-risk individuals for further testing.

How many SNPs should a predictor include? Parametrize the unknown genetic architecture by
$\pi_0$, the proportion of markers with truly zero effect: $\pi_0=0.95$ means "only 5% of markers
matter," $\pi_0=0.90$ means "10% matter" (though which 10% cannot be identified without the full
ranked list), and $\pi_0=0$ means every marker carries a real effect. The optimal SNP-inclusion
threshold $P_T$ depends on both this architecture and the cohort's power to rank SNPs correctly
(Purcell et al., *Nature* 2009, schizophrenia risk prediction; Dudbridge, *PLoS Genetics* 2013). It
only peaks near 5% (approximately $1-\pi_0$) when there is enough power to rank accurately; with
limited power, even at $\pi_0=0.90$, the predictor still needs to include essentially all SNPs to
reach its best accuracy, because a large fraction of the truly associated markers sit below the
nominal significance threshold and can only be captured in aggregate, not by name.

The same design applied across two traits tests for shared genetic architecture: build the
predictor on a schizophrenia case-control cohort, then apply it to a bipolar-disorder case-control
cohort. If schizophrenia-ranked SNPs also predict bipolar-disorder diagnosis, but not an unrelated
trait such as a cardiovascular one, that is genetic evidence the two disorders share common risk —
which was exactly the first result this cross-trait design produced.

Several caveats limit what any of this can claim:

- Prediction is capped by however much of the trait actually is genetic — environment and random
  effects dominate most complex traits.
- A common-variant risk score is probabilistic, unlike a near-deterministic Mendelian mutation; it
  is only a first screen, not a diagnosis.
- Discovery power (cohort size) limits both which SNPs can be found and how well they can be
  ranked.
- Genotyping arrays cover common SNPs, not all SNPs — natural selection has already pushed the
  most fitness-reducing variants to low frequency, and arrays are designed around common variants,
  so exactly the class of variant most likely to have a large effect is under-sampled.
- **Winner's curse**: even a correctly identified SNP has its effect size over-estimated at
  discovery, because only the subset of truly-associated SNPs whose sample estimate happened to
  cross the significance threshold gets reported.
- Non-independence between training and testing cohorts — relatives, cryptic relatedness,
  population stratification — inflates apparent accuracy unless explicitly corrected for.

## Case study: a sub-threshold cardiac-conduction locus

The QRS/QT interval — an electrical-conduction trait of the heart — was chosen for this case study
because it already has large GWAS cohorts, many genome-wide-significant hits, and well-characterized
tissue drivers: a favorable setting to test whether epigenomic annotation can recover loci that fall
*short* of genome-wide significance, such as rs1743292 ($P=10^{-4.2}$, roughly $6\times10^{-5}$ —
far above the conventional $5\times10^{-8}$ threshold).

The approach trains a classifier to distinguish enhancers that overlap strong GWAS hits from
generic left-ventricle enhancers, using measurable chromatin and sequence features:

| Feature | Fold difference (GWAS-overlapping vs. generic LV enhancer) | p-value |
|---|---|---|
| H3K27ac density | 3.10 | $1.54\times10^{-4}$ |
| Activity, fetal heart / right atrium / right ventricle | 1.24 / 1.18 / 1.34 | $4.40\times10^{-3}$ / $4.13\times10^{-2}$ / $1.15\times10^{-2}$ |
| Breadth of activity in non-cardiac tissues | 0.59 | $9.05\times10^{-3}$ |
| LV-specific hypomethylation | 2.34 | $1.07\times10^{-6}$ |
| LV-specific hypermethylation | 0.39 | 0.60 (n.s.) |
| Primate sequence conservation | 1.14 | $6.82\times10^{-5}$ |
| Fetal heart DNase I hypersensitivity | 1.45 | $5.25\times10^{-4}$ |
| CAGE-seq, fetal heart | 0.83 | $1.44\times10^{-3}$ |
| CAGE-seq, adult heart | 0.89 | 0.17 (n.s.) |

GWAS-overlapping enhancers, in other words, are more active, more cardiac-restricted, more
conserved, and more accessible in fetal heart than a generic left-ventricle enhancer — differences
a trained model can use to rank sub-genome-wide-significant SNPs by how genuine their enhancer
looks, without waiting for a larger sample.

That prioritization is itself testable. Sub-threshold SNPs sitting inside a prioritized enhancer
are far more likely to be at least nominally significant in the actual QRS GWAS than sub-threshold
SNPs outside one ($p=3.04\times10^{-5}$); their candidate target genes are enriched for
cardiac-conduction or contractility phenotypes when knocked out in mouse, both against genes near
generic LV enhancers ($p=6.84\times10^{-5}$) and against sub-threshold loci that fall outside
enhancers altogether ($p=1.92\times10^{-3}$); and two of the implicated genes, *POPDC2* and
*POPDC3*, show relevant phenotypes in zebrafish as well.

Eleven of these prioritized sub-threshold loci were then tested directly, with a luciferase
reporter assay (does the candidate enhancer drive expression, and does that differ between the two
alleles?) and 4C-seq (which gene promoters does the fragment physically contact?):

| Lead SNP | GWAS p-value | Enhancer region | Luciferase p-value | 4C-seq target(s) |
|---|---|---|---|---|
| rs1886512 | $4.30\times10^{-8}$ | chr13:74,520,000–74,520,400 | 0.015 | none |
| rs1044503 | $5.13\times10^{-7}$ | chr14:102,965,400–102,972,000 | $4.70\times10^{-9}$ | CINP, RCOR1 |
| rs10030238 | $6.21\times10^{-7}$ | chr4:141,807,800–141,809,600 and 141,900,800–141,908,000 | $1.35\times10^{-14}$ | RNF150 |
| rs6565060 | $1.52\times10^{-5}$ | chr16:82,746,400–82,750,800 | $5.00\times10^{-3}$ | none |
| rs3772570 | $1.73\times10^{-5}$ | chr3:148,733,200–148,738,600 | 0.67 | — |
| rs3734637 | $2.23\times10^{-5}$ | chr6:126,081,200–126,081,800 | $1.06\times10^{-4}$ | HDDC2 |
| **rs1743292** | $6.48\times10^{-5}$ | chr6:105,706,600–105,710,200 and 105,720,200–105,723,000 | $3.20\times10^{-4}$ | BVES, POPDC3 |
| rs11263841 | $6.87\times10^{-5}$ | chr1:35,307,600–35,312,200 | 0.22 | GJA4, DLGAP3 |
| rs11119843 | $7.14\times10^{-5}$ | chr1:212,247,600–212,248,600 | 0.031 | — |
| rs6750499 | $7.37\times10^{-5}$ | chr2:11,559,600–11,563,000 (two 2kb fragments) | 0.54 and $3.26\times10^{-7}$ | ROCK2 |
| rs17779853 | $7.73\times10^{-5}$ | chr17:30,063,800–30,066,800 | $4.33\times10^{-3}$ | none |

Nine of the eleven tested loci showed allelic activity, chromatin interactions, or both.

The deepest dive is on rs1743292: its enhancer's 4C contacts link it to two candidate promoters,
*BVES* and *POPDC3*; an enhancer-driven eGFP reporter confirms heart activity; the enhancer
contains a Nuclear Factor I binding motif that the SNP disrupts; allele-specific DNase
accessibility (DGF and DHS read counts) differs between the two alleles across several
heterozygous individuals; and the two alleles drive significantly different luciferase activity
($p=3.2\times10^{-4}$) — five separate lines of evidence converging on the same causal call.

Closing the loop from variant to organismal phenotype, *BVES* was tested directly in zebrafish
embryo hearts: a voltage-sensitive fluorescent dye combined with optical voltage mapping measures
transmembrane voltage across the ventricle directly, and perturbing *BVES* shifts action-potential
duration ($\Delta\mathrm{APD}_{80}$) relative to control — electrophysiological confirmation that
the target gene identified through this whole pipeline genuinely affects cardiac conduction.

The reason this locus is a good advertisement for the whole approach is a power argument. rs1743292
has a minor allele frequency of 0.134 and an estimated effect size of $-0.5773\pm0.17$ msec on the
interval — comparable to many already genome-wide-significant loci. With the 68,900 individuals
actually available, the power to discover it at $p<5\times10^{-8}$ was only 12.8%; reaching 80%
power at that same threshold would require 146,700 individuals, more than twice the actual cohort.
Since many already-published GWAS hits share similarly weak effect sizes, many of them were
themselves only found because of **winner's curse**: reported hits are the lucky subset of true
associations whose sample estimate happened to cross the significance threshold, drawn from a much
larger pool of true associations with only 5–20% power to be discovered at all. Combining
epigenomics with existing GWAS data therefore does two things at once: it lends confidence that
near-threshold hits are more likely real than chance, and it discovers genuinely new sub-threshold
loci that will never reach significance at the sample sizes actually available.

## Somatic heterogeneity and regulatory convergence in cancer

Return to the three-way table from earlier: cancer's loss-of-function driver mutations are
protein-coding and converge on a comparatively small, well-studied set of genes and pathways, but
its gain-of-function mutations are regulatory — individually heterogeneous, since different tumors
disrupt different non-coding elements, so recurrence has to be sought at the level of a gene's
whole regulatory neighborhood rather than at one fixed nucleotide.

The unit introduced for that neighborhood is a gene's **regulatory plexus**: the complete set of
candidate enhancers and promoters across a gene's surroundings that could plausibly regulate it
(illustrated with the *ITM2A* plexus; work credited to Richard Sallari). A driver mutation, on this
view, can land anywhere within a target gene's plexus rather than at a single hotspot, so the
recurrent signal to look for is "mutations concentrate somewhere in this plexus across many
tumors," not "the same base pair recurs across tumors."

Applying this to a prostate cancer cohort surfaces several findings. Genes found dysregulated
between tumor and normal samples are more often found **up-regulated** than down-regulated. Both
up- and down-regulated genes carry an excess of non-coding mutations in their plexus at every
distance tested — proximal (within 200kb, roughly 1,000–1,900 mutations pooled across the up- and
down-regulated sets), distal-cis (within 3.3Mb, tens of thousands of mutations), and distal-trans
(within 4.9Mb, tens of thousands of mutations) — with the excess strongest, by a wide margin, for
up-regulated genes at the more distal ranges (reported fold-enrichment values of 2.07, $>8$, and
7.16 respectively for up-regulated genes at proximal, distal-cis, and distal-trans distances,
against $-0.52$, $-0.67$, and $0.41$ for down-regulated genes at the same three distances — the
lecture does not specify the exact units of this fold-enrichment score beyond the sign indicating
depletion versus enrichment). Separately, disruptive mutations that fall in chromatin the tumor's
own cell type treats as inactive ("low" state) are nonetheless enriched for lying in promoters or
enhancers active in some *other* tissue or cell type (fold enrichment up to 11.7 for promoters,
11.4 for enhancers) — an element that looks silent in the tumor's own chromatin context can still
be a real, working regulatory element borrowed from another cell type's repertoire.

Because mutation rate itself varies by chromatin state, genomic region, and tumor, calling any of
this an "excess" needs a background model: expected mutation counts (mean and standard deviation)
are estimated per plexus-state and region combination, correcting for region-, state-, and
tumor-specific rate variation, before observed counts are compared against that expectation.

At the pathway level, scoring individual genes for how concentrated their non-coding mutations are
within a single most-enriched chromatin state, compared to across all regulatory states combined,
surfaces a convergence pattern among genes that share no obvious sequence-level relationship (state
abbreviations: enh = enhancer, pro = promoter, txn = transcribed, poi = poised, rep = repressed;
the lecture's table also reports element counts, kilobase coverage, and chromosome/tumor counts per
gene, omitted here to keep the pathway argument visible):

| Gene | Enriched state | p-value | Convergence (single state) | Convergence (all states) | Putative function | Convergence group |
|---|---|---|---|---|---|---|
| ITM2A | enh | $1\times10^{-7}$ | 56% | 87% | immune evasion | 2 |
| INSRR | poi | $2\times10^{-7}$ | 62% | 100% | insulin/androgen | 1 |
| ZCCHC16 | txn | $3\times10^{-7}$ | 60% | 98% | unknown | — |
| ZBED2 | pro | $9\times10^{-7}$ | 71% | 100% | immune evasion | 2 |
| SPANXN3 | pro | $1\times10^{-6}$ | 35% | 85% | spermatogenesis | 1 |
| PLCB4 | txn | $2\times10^{-6}$ | 67% | 98% | insulin/androgen | 1 |
| COQ3 | pro | $2\times10^{-6}$ | 64% | 100% | mitochondrial | 3 |
| EDNRA | txn | $2\times10^{-6}$ | 75% | 100% | blood flow | — |
| CRY2 | txn | $3\times10^{-6}$ | 65% | 100% | insulin/androgen | 1 |
| ZC3H12B | rep | $3\times10^{-6}$ | 89% | 100% | immune evasion | 2 |
| C14orf180 | txn | $4\times10^{-6}$ | 51% | 93% | secreted | — |
| IDO2 | rep | $4\times10^{-6}$ | 87% | 98% | immune evasion | 2 |
| RRAD | poi | $4\times10^{-6}$ | 51% | 95% | insulin/androgen | 1 |
| SLC25A5 | rep | $4\times10^{-6}$ | 67% | 91% | mitochondrial | 3 |
| SSX3 | enh | $4\times10^{-6}$ | 65% | 78% | spermatogenesis | 1 |

Fifteen genes with no obvious relationship to each other converge, at the pathway level, onto a
small number of functional themes — most visibly immune evasion, insulin/androgen signaling, and
mitochondrial function. A related line of evidence in the same cohort found convergence
specifically in inositol phosphate metabolism, adjacent to the known cancer genes *PTEN* and
*PIK3CA*; and as a direct functional check, overexpressing one of the implicated genes, *PLCB4*, in
a PC3 prostate cancer cell line reduced ERK/AKT signaling activity synergistically with *PTEN* —
tying the statistical convergence argument back to a measured effect on a cancer-relevant pathway
(work credited to Richard Sallari).

## Outlook

The lecture closes on scale and on what is still missing rather than on new methodology. Personal
genomics already has hundreds of thousands of complete genomes to work with, aimed at three goals:
translating genomic regions into disease mechanism and drug targets, and single genes into systems
and pathways; resolving human ancestral relationships and the history of migrations and selection;
and — repeatedly named as the actual bottleneck — the computation itself: new algorithms, machine
learning, and dimensionality reduction, individualized treatment drawing on thousands of genes at
once, accounting for missing heritability, revealing co-evolution between genes and elements, and
correcting for modulating effects in GWAS. Moving any of this from research into the clinic is
framed as six concurrent efforts: systematic medical genotyping and sequencing; systematic
molecular profiling in relevant cell types; systematic perturbation studies to validate regulatory
predictions at scale (thousands of predictions across hundreds of cell types); systematic
repurposing of already-approved drugs from a systems-biology view of drug response; genomics
applied to drug response within clinical trials, toward personalized prescription and combination
therapy; and partnerships across academia, industry, and hospitals to train people who can work
across all of these institutions at once.

## Sources

All material in this chapter comes from the slide deck for MIT 6.047/6.878/HST.507 (Fall 2015),
Lecture 21, "Personal genomics, disease epigenomics, systems approaches to disease":

- `01-lecture-21.md` — epidemiology definitions and study design; GWAS scale, scope, and the
  coding/non-coding split by disease class; the genomic-medicine challenge/remedy/deliverables
  framing; the reference-map framework and six dissecting steps; identifying disease-relevant cell
  types and the Alzheimer's immune-vs-neuronal case study; the LD blessing/curse tables; the
  fine-mapping evidence types, allele-specific Zeb1 example, and HaploReg; the target-gene evidence
  types and the IRX3/IRX5 worked example; the C/E/G/X/D/S causal diagram; and the MAP/ROS
  Alzheimer's cohort description.
- `02-data-matrices-an-example-scenario.md` — the genotype/methylation/environment/phenotype
  data-matrix picture (G, M, E, P, n).
- `04-cis-meqtls.md` — the cis-meQTL linear model and nested-model F-test; permutation and
  linear-mixed-model alternatives; the rank-based weak-association enrichment method and its T1D
  worked example; the basic polygenic risk prediction setup, SNP-inclusion-threshold argument, and
  pleiotropy/caveats discussion.
- `05-enhancers-overlapping-gwas-loci-share-functional-properties.md` — the enhancer-characteristics
  table and the mouse/zebrafish phenotype evidence for the cardiac case study.
- `06-experimental-validation-of-11-sub-threshold-loci.md` — the 11-locus validation table, the
  rs1743292 deep dive, and the discovery-power/winner's-curse calculation.
- `07-convergence-in-immune-signaling-mitoch-functions.md` — the regulatory-plexus concept, the
  prostate cancer dysregulation findings, the background mutation-rate correction, the
  pathway-convergence table, and the closing outlook slides.

Two things this chapter does not cover, because they were not in the supplied material: the slide
titled "EWAS: Capturing variability in the Epigenome attributable to disease" (file `03`, linked
from the navigation in `01` and `04` but not included among the inputs), and the statistical
machinery of Mendelian randomization itself, which the lecture's own outline lists under "Resolving
Causality" but which is not spelled out on any slide supplied here — only the causal diagram that
motivates it is. No lecture transcript, written notes, or problem set were supplied alongside the
slides for this lecture, so no worked commentary beyond the slide text and no exercises are
included.

Papers and tools named on the slides, cited here only as slide references rather than as sources
independently read: Hindorff et al., *PNAS* 2009; Hillmer, *Nature Genetics* 2008; Roadmap
Epigenomics, *Nature* 2015; Ernst, *Nature* 2011; Gjoneska et al., *Nature* 2015; Ward and Kellis,
*Nature Biotechnology* 2012; Ward and Kellis, *Nucleic Acids Research* 2011 (HaploReg); Purcell et
al., *Nature* 2009; Dudbridge, *PLoS Genetics* 2013.

Each supplied slide file is itself a model's reconstruction of a PDF with no extractable text layer
(noted in each file's own front matter, which flags every equation as unverified); the definitions,
numbers, and formulas reported in this chapter are relayed as given in that reconstruction.

---

[← 9. Molecular Evolution and Phylogenetics](09-molecular-evolution-and-phylogenetics.md) · [Contents](index.md) · [11. Genome Alignment and Evolution →](11-genome-alignment-and-evolution.md)
