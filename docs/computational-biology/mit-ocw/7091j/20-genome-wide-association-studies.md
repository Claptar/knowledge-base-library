---
title: "20. Genome-Wide Association Studies"
course: "MIT 7.091J"
chapter: 20
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 20. Genome-Wide Association Studies

## What this covers

This chapter answers one practical question: given genotype or sequencing data from a group of
people with a disease and a group without it, how do you decide whether a particular genetic
variant is associated with the disease, and how much should you trust the answer? It assumes you
already know what a SNP, a haplotype and a BAM/VCF file are, and have seen Bayes' rule and basic
hypothesis testing. The chapter follows the lecture's own arc: start from clean, array-called
genotypes and simple contingency-table tests; add the complications of real sequencing reads,
which force a probabilistic model of genotyping; and end by asking what an association is actually
worth once you have found one.

## Rare alleles, common alleles, and effect size

A Mendelian disorder is caused by a single gene, which makes it relatively easy to map. Such
variants also tend to be rare: severe Mendelian disorders are selected against, so the mutations
behind them stay at low frequency in the population. Contrast this with a trait influenced by,
say, two hundred genes, none of which is individually necessary or sufficient — a variant in any
one of them can be common, because it only causes disease in combination with many others. The
result is a general relationship between an allele's frequency and the size of its effect: rare
variants can have large effects, common variants tend to have small ones.

<figure>
<svg viewBox="0 0 340 260" role="img" aria-label="Triangle showing that rarer alleles tend to carry larger phenotypic effects">
  <path d="M170,20 L30,240 L310,240 Z" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="1.2"/>
  <line x1="119" y1="100" x2="221" y2="100" stroke="currentColor" stroke-width="1"/>
  <line x1="74" y1="170" x2="266" y2="170" stroke="currentColor" stroke-width="1"/>
  <text x="170" y="60" text-anchor="middle" font-size="11" fill="currentColor">rare, large effect</text>
  <text x="170" y="140" text-anchor="middle" font-size="11" fill="currentColor">lower-frequency, moderate effect</text>
  <text x="170" y="210" text-anchor="middle" font-size="11" fill="currentColor">common, small effect</text>
  <text x="170" y="255" text-anchor="middle" font-size="12" fill="currentColor">allele frequency &#8594;</text>
  <text x="18" y="130" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 18 130)">effect size &#8594;</text>
</svg>
<figcaption>The allele-frequency spectrum the lecture opened with: high-frequency polymorphisms
(&#8805;5%, first-generation SNP arrays, HapMap), lower-frequency ones such as CFTR delta-508 or
PCSK9 C679X (1000 Genomes, newer arrays and imputation), and rare mutations such as most Mendelian
disease alleles (direct sequencing, array-based detection of copy-number variants). Slide courtesy
of David Altshuler, HMS/Broad.</figcaption>
</figure>

Two early phases of mapping human variation follow directly from this. First-generation studies
of "common" variants used an allele-frequency threshold of 5% or above. The 1000 Genomes Project
pushed further, down to variants present at roughly 0.5% frequency — in a 1,000-person sample that
is about 5 copies, and because the project pooled several distinct populations, those 5 copies
might sit in only one of them. SNP arrays are designed from exactly this kind of population
survey: find the common variants, then build a chip that reads them out directly.

A small story makes the "necessary and sufficient" point concrete. Imagine a mutation (G to A)
arises in a population with no disease. Many generations later, a second, independent mutation
arises, and only the people who carry *both* mutations get the disease — so the first mutation was
not *sufficient* on its own. Separately, some people who do have the disease turn out not to carry
the first mutation at all — so it is not *necessary* either. It is neither necessary nor
sufficient, and yet it is a real marker of increased risk. That is the kind of relationship a
case/control association study is built to detect: an association between genotype and phenotype,
not a proof of causation.

## Setting up a case/control test: contingency tables

The worked example is age-related macular degeneration (AMD), a disease in which the center of the
visual field degenerates with age. A 2004 study genotyped a cohort of 2,172 unrelated
European-descent individuals at least 60 years old: 934 controls with normal vision and 1,238
cases with AMD. At the time, little was known about the cause of AMD.

For a single SNP, rs1061170, the allele counts (two alleles per person) form a 2x2 contingency
table:

| Allele | Cases (AMD) | Controls | Total |
| :--- | ---: | ---: | ---: |
| C (a, b) | 1522 | 670 | 2192 |
| T (c, d) | 954 | 1198 | 2152 |
| Total | 2476 | 1868 | 4344 |

The *marginal* probability of carrying a C allele, ignoring case/control status entirely, is read
straight off the margin of the table: $2192/4344$.

**The chi-square test.** The usual Pearson statistic compares, for every cell, the observed count
against the count expected under independence of allele and disease status, summed as
$(\text{observed} - \text{expected})^2/\text{expected}$. Expanding that sum for a 2x2 table and
simplifying gives the closed form in terms of the cell labels $a,b,c,d$:

$$\chi^2 = \frac{N(ad-bc)^2}{(a+b)(c+d)(a+c)(b+d)}, \qquad N = a+b+c+d,$$

with $(\text{rows}-1)(\text{columns}-1) = 1$ degree of freedom. For rs1061170 this gives a p-value
around $10^{-62}$ — small enough to survive correction for testing on the order of a million SNPs
across the genome. This looks like a genuine hit.

**Fisher's exact test.** A second way to ask the same question — could this table have arisen by
chance? — is to compute the exact probability of the observed arrangement directly, without a
chi-square approximation. It is the hypergeometric probability: out of the $a+b$ C alleles, the
chance that exactly $a$ of them land in the case column, combined with the chance that, out of the
$c+d$ T alleles, exactly $c$ land in the case column, divided by the total number of ways to split
$a+b+c+d$ alleles into $a+c$ "case" alleles while holding the marginal totals fixed:

$$P(\text{table}) = \frac{\dbinom{a+b}{a}\dbinom{c+d}{c}}{\dbinom{a+b+c+d}{a+c}}.$$

Summing this probability over the observed table and every table at least as extreme gives the
exact p-value under the null hypothesis. This is the same idea as the hypergeometric test used
elsewhere in the course.

## A confound: population stratification

Suppose you genotype all your AMD cases at one hospital and, to save money, genotype all your
controls in a different country. Any SNP whose allele frequency simply differs between those two
underlying populations — for reasons having nothing to do with AMD — will come out looking
associated. This is *population stratification*. The standard check is to genotype a panel of SNPs
believed to be unrelated to the disease and run the same chi-square test on them: if those controls
come back significant too, the case and control samples are not drawn from the same population, and
the apparent disease association is suspect. Correcting for stratification by re-clustering
individuals is an active area of research and was explicitly out of scope for the lecture, along
with non-random genotyping failure and structural variants/CNVs.

For AMD itself the result held up: three genes with five common variants together explain about
50% of the risk, making it one of the clear early successes of this methodology for a polygenic
disease — a result that then opened the door to therapeutics targeting those genes.

Running this single-SNP test across the whole genome, for a given disease, produces what is called
a **Manhattan plot** — a scatter of $-\log_{10}(p)$ against genomic position, in which a truly
associated locus stands out as a "skyscraper." Studies in this style, scanning many diseases this
way (the lecture's example ran from bipolar disorder down to type 2 diabetes), began appearing
around 2007.

## Linkage disequilibrium and haplotype blocks

A single gamete inherits one allele from each of two linked loci, and if the two loci were
unlinked, all four combinations (AB, aB, Ab, ab) would occur independently. If instead only two of
the four combinations are ever observed, the loci are in high **linkage disequilibrium (LD)**:
they are usually inherited together, which is evidence that they sit close together on the
chromosome, with little chance of a recombination event falling between them. (The lecture's
working estimate was that crossover events are spaced on the order of 50 to 100 megabases apart in
the human genome.)

LD between two loci with reference-allele frequencies $p_A$ and $p_B$ is quantified by

$$D = P(AB) - p_A p_B,$$

the deviation of the joint haplotype frequency from what independence would predict, or
equivalently by the correlation measure

$$r^2 = \frac{D^2}{p_A(1-p_A)\, p_B(1-p_B)}.$$

Plotting $r^2$ against physical distance (for example along chromosome 22, over the first
megabase) shows the expected decay with distance, but not uniformly: there are recombination
hotspots, so some loci far apart still show surprisingly high $r^2$, and figuring out how
recombination is targeted across the genome is itself a current research question.

**Haplotype blocks** are the practical consequence: stretches of the genome where markers travel
together. The HapMap project mapped these empirically — there is no equation that predicts block
boundaries, only observation of what travels together in a population sample. Block size also
depends on how closely related the individuals are: your genome contribution from an ancestor
falls off exponentially with each generation back (half from a parent, a quarter from a
grandparent, an eighth from a great-grandparent, and so on), so blocks shared within a trio (mother,
father, child) are large, while blocks shared between unrelated individuals drawn at random from
the population — exactly the samples used in an association study — are much smaller. That is
actually convenient for association mapping: it means a marker can be a useful proxy for a nearby
causal variant across almost any stretch of the genome, since even unrelated individuals share
short haplotype blocks everywhere.

The direct consequence for interpreting an association hit: because LD links nearby variants
together, a significant SNP need not be the **causative SNP** itself (sitting in a coding exon
causing a missense change, or in a protein-binding site, for example). It may simply be a **proxy
SNP**, correlated with the true causal variant through LD.

## Phasing: which chromosome carries which mutation

Consider a hypothetical important gene, call it RIG, with two mutations relative to reference.
Does it matter whether both mutations sit on the *same* copy of the gene (one good copy remains on
the other chromosome) or on *different* copies (both copies of the gene are disrupted)? It matters
exactly when the disease allele is recessive: two mutations in *cis* (same chromosome) still leave
one functional copy, while two mutations in *trans* (different chromosomes, one from each parent)
can knock out both.

<figure>
<svg viewBox="0 0 380 200" role="img" aria-label="Two mutations on the same chromosome copy versus on different copies">
  <text x="95" y="24" text-anchor="middle" font-size="12" fill="currentColor">cis: one good copy remains</text>
  <line x1="30" y1="60" x2="160" y2="60" stroke="currentColor" stroke-width="2"/>
  <line x1="30" y1="100" x2="160" y2="100" stroke="currentColor" stroke-width="2"/>
  <circle cx="70" cy="60" r="4" fill="currentColor"/>
  <circle cx="120" cy="60" r="4" fill="currentColor"/>
  <text x="95" y="130" text-anchor="middle" font-size="11" fill="currentColor">both mutations, one homolog</text>

  <text x="285" y="24" text-anchor="middle" font-size="12" fill="currentColor">trans: both copies disrupted</text>
  <line x1="220" y1="60" x2="350" y2="60" stroke="currentColor" stroke-width="2"/>
  <line x1="220" y1="100" x2="350" y2="100" stroke="currentColor" stroke-width="2"/>
  <circle cx="260" cy="60" r="4" fill="currentColor"/>
  <circle cx="310" cy="100" r="4" fill="currentColor"/>
  <text x="285" y="130" text-anchor="middle" font-size="11" fill="currentColor">one mutation per homolog</text>
</svg>
<figcaption>Why phasing matters for a recessive disorder: two mutations in cis (left) leave a
functional allele on the other chromosome; two mutations in trans (right) disrupt both copies.</figcaption>
</figure>

**Phasing** is the act of assigning variants to a parental chromosome; the set of alleles along one
chromosome is a **haplotype**. Two ways to phase were described. One is statistical: if you already
know, from population data, which haplotypes actually exist, you can check which combination of
observed alleles matches a known haplotype and infer the phase that way. The other is direct and
far simpler: a single sequencing read that spans both variant positions shows the phase outright.
The obstacle is read length — short reads rarely span both sites, so most of genotyping amounts to
reassembling phase from a genome that sequencing has shattered into short pieces; long-read
platforms (the lecture named PacBio, and noted Illumina has its own trick) can phase directly by
simply covering both positions in one read. In a VCF file, a vertical bar between the two alleles
of a genotype (rather than a slash) indicates the phase is known.

## From arrays to raw reads

Everything so far assumed genotypes were already called cleanly, as they are from a SNP array.
Sequencing data makes far fewer assumptions and is correspondingly messier. The clean case is an
aligned read pileup where some reads show one base and others show a different base at the same
position — a clear heterozygote call, with the reference genome shown underneath for comparison.
Real data rarely looks that clean: alignments are noisy, and a principled, probabilistic treatment
of "is there really a variant here" is needed.

The underlying file formats: a **BAM** file holds aligned reads together with, for every base, a
machine-reported **Phred quality score** — an estimate of the probability the base call is wrong.
The output of variant calling is a **VCF** file: a header describing the fields, then one line per
variant giving its position, reference and alternate allele, summary statistics (e.g. `DP`, the
read depth), and per-individual fields such as `GT` (genotype), `GQ` (genotype quality) and `GP`
(genotype probability).

The lecture walked through the broad shape of a variant-calling pipeline (drawn from the Genome
Analysis Toolkit, GATK, and an article by Heng Li on the underlying mathematics, both pointed to
but not reproduced in the slides):

- **Map** reads to the reference genome.
- **Recalibrate** the reported quality scores. Manufacturers' reported Phred scores are often
  optimistic; recalibration compares reported against actual error rate, as a function of the raw
  score, how far into the read a base sits (cycle number), and the surrounding dinucleotide
  context — figuring this out was one of the methodological contributions of the 1000 Genomes
  Project. It matters because the genotyping model below leans on these error estimates directly.
- **Indel-adjust** (local realignment). A real deletion in one chromosome, aligned against a
  reference that lacks it, forces the bases downstream of the gap to misalign and throws off
  variant calls at the end of each read from both directions — reads from one strand show spurious
  variants at one end, reads from the other strand at the other end. The lecture's example involved
  a seven-base homopolymer run of T's near the deletion, which sequencers are notoriously bad at
  reading accurately; realigning around the indel (and correcting the homopolymer miscalls) makes
  the spurious variant calls disappear. This step has no analogue in array genotyping — it is a
  consequence of mapping reads de novo rather than reading out pre-specified probe positions.
- **Reduce representation.** Most of a BAM file is uninformative once you only care about
  positions that differ from reference, so reads can be stripped down to the variable regions,
  which compresses the data and speeds everything downstream.
- **Jointly call variants** across all individuals, **refine**, and **evaluate** — the stages taken
  up in the next section.

Before full genome sequencing was practical, people instead captured and sequenced just the
expressed part of the genome (the exome), using sequence-specific probes to pull out the genes of
interest — a cheaper way to get at an important subset of the genome.

## A probabilistic model for genotype calling

A **genotype** for an individual, at a given position, is a pair of bases — one inherited from each
parent — which may be phased or not. Unphased, it is often simplified to a count of reference
alleles present: 0 (no reference allele, homozygous for the alternate), 1 (heterozygote), or 2
(homozygous reference). Whatever representation is chosen, the probability distribution over
genotypes must sum to 1.

**Per-individual genotype likelihood.** At one genomic position, given a hypothesized genotype $G$
(one base from "mom," one from "dad") and the full set of reads $D = \{d_1,\dots,d_n\}$ covering
that position, assume each read came, independently, with probability one-half from the maternal
chromosome and one-half from the paternal one. The per-read probability of observing base $d_j$
given a hypothesized true base $b$ uses the machine's reported error rate $\epsilon_j$ directly:

$$P(d_j \mid b) = \begin{cases} 1-\epsilon_j & \text{if } d_j = b \\ \epsilon_j & \text{if } d_j \neq b. \end{cases}$$

The read-set likelihood under genotype $G = (b_{\text{mom}}, b_{\text{dad}})$ is then the product,
over independent reads, of the read's probability averaged over its two possible parental origins:

$$P(D \mid G) = \prod_{j=1}^{n} \left[ \tfrac{1}{2} P(d_j \mid b_{\text{mom}}) + \tfrac{1}{2} P(d_j \mid b_{\text{dad}}) \right].$$

Applying Bayes' rule converts this into the quantity actually wanted, the posterior probability of
the genotype given the data in hand:

$$P(G \mid D) = \frac{P(D \mid G)\, P(G)}{P(D)}.$$

**The population prior.** $P(G)$ — what we expect the genotype to be before looking at this
individual's reads — comes from the population as a whole, and estimating it is a joint problem
across every individual in the sample (say, all the cases, or all the controls): an iterative
expectation-maximization procedure alternates between each individual's genotype posterior and a
population-wide allele-frequency estimate, repeating until convergence. (The practical numerical
tricks for doing this well are in the paper the lecture referred to but did not reproduce.) The
output of this whole process, for a population, is a probability distribution over genotype state
(0, 1 or 2 reference alleles) at each site — the sequencing-data analogue of the clean array
genotype call this chapter started from.

## Hardy-Weinberg equilibrium, and choosing the right test

**Hardy-Weinberg equilibrium (HWE)** describes the genotype frequencies expected in a population
under random mating, diploidy, no selection and no bottlenecks: if $\psi$ is the population
frequency of the reference allele, the equilibrium genotype frequencies are $\psi^2$ (homozygous
reference), $2\psi(1-\psi)$ (heterozygote), and $(1-\psi)^2$ (homozygous alternate). Because the
genotype-calling procedure above already produces an estimated genotype-frequency distribution for
a population, HWE can be tested directly: compare the observed genotype frequencies against those
predicted from the single allele-frequency parameter $\psi$, with a log-likelihood ratio test. A
large enough statistic says the divergence is unlikely to be chance, and the population is not in
equilibrium — which can happen from strong selection or population substructure.

Why care? Because there are two different ways to test a SNP for case/control association once you
have genotype probabilities rather than raw allele counts:

- Compare just the *reference-allele frequency* between cases and controls (the same kind of test
  run earlier on raw allele counts) — one additional degree of freedom for the case/control split.
- Compare the *full genotype-frequency distribution* between cases and controls directly, as a
  likelihood-ratio test: likelihood of the data under separate case and control genotype
  distributions, against likelihood under a single combined distribution — two additional degrees
  of freedom, since three genotype frequencies sum to one and both populations get their own.

If the population is in Hardy-Weinberg equilibrium, genotype frequencies are fully determined by
the single allele-frequency parameter $\psi$, so the genotypic test's extra degrees of freedom add
nothing the allelic test did not already capture. Knowing whether your populations are actually in
equilibrium is therefore a prerequisite for deciding which of the two tests is the right one to
use, not an optional side check.

## Beyond single bases: local assembly

The methods above treat every position independently and say nothing about which chromosome (mom's
or dad's) a variant sits on, nor do they handle structural variation well. An alternative approach
for a region flagged as variable is **local assembly**: assemble the most likely haplotypes
directly from the reads covering that region, then estimate each assembly's divergence from the
reference the same way sequence divergence was estimated earlier in the course, rather than scoring
individual bases one at a time. This handles general structural variation and can reveal that an
apparent cluster of SNP calls was actually caused by an insertion or deletion on one chromosome.
Phasing from read data, and full structural-variant/CNV detection, were both flagged as large
enough topics to deserve lectures of their own and were only touched on here.

## From association to function

A genome-wide scan finds correlations; confirming that a variant is actually causal is separate
work. The lecture's example involved a pancreatic disorder and an enhancer region marked by the
H3K4 mono-methylation signal (a mark associated with active enhancers, introduced earlier in the
course) and bound by two pancreatic transcription factors. Within that enhancer, five SNP variants
were called, along with a separate 7.6-kilobase deletion nearby, and inheritance of these variants
tracked closely with disease prevalence. To move from association to function, the study's authors
mutated the enhancer at each of the five SNP positions individually and showed a measurable
decrease in enhancer activity at every one, and separately showed (by chromosome-conformation
capture) that the enhancer physically interacts with the gene's promoter — tracing the association
signal down to specific disrupted transcription-factor motifs within the enhancer.

## Correlation is not causation

The lecture closed on a cautionary result about what a genetic association is actually worth for an
individual. In monozygotic (identical) twins, for a number of common diseases, if one twin has the
disease there is roughly a 30% chance the other twin does too. Looking at twin data without making
any assumption about which genotypes are responsible, the fraction of actual disease cases that
would have tested positive on a genetic test is fairly low for many of these diseases — meaning a
test will miss more than half of true cases for over half the diseases studied — and testing
negative does not reduce an individual's relative risk by much either. Because this conclusion
relied only on twin data, with no further modeling assumptions, it raised a real question in the
field about how predictive personal genome sequencing can actually be for common disease, which is
exactly the distinction the lecture opened with: an association is not the same thing as a cause,
and it does not automatically make a good predictive test.

## Sources

- Slides: `lectures/20-slides.md` ("Analysis of Genome Wide Association Studies (GWAS)," David K.
  Gifford) — narrative arc, computational approaches, out-of-scope list, allele-frequency pyramid
  (slide courtesy of David Altshuler, HMS/Broad), AMD cohort description, and the rs1061170
  contingency table. The chi-square formula on this slide is cut off in conversion; the completed
  form given here is the standard closed form for a 2x2 table, matching the professor's verbal
  description in the transcript.
- Transcript: `recordings/lectures/20.md`, timestamps throughout — in particular 04:33–09:18
  (Mendelian vs. polygenic, the two-mutation story), 11:31–16:24 (contingency tables, chi-square,
  Fisher's exact test), 16:24–19:47 (population stratification, AMD result, Manhattan plots),
  20:58–30:27 (linkage disequilibrium, haplotype blocks, causative vs. proxy SNPs), 31:38–37:04
  (the RIG example and phasing), 37:04–49:46 (BAM/VCF, the GATK pipeline, indel realignment, quality
  recalibration, exome capture, reduced representation), 49:46–1:05:46 (genotype representation,
  the per-read and per-individual likelihood model, Bayes' rule, the EM procedure, Hardy-Weinberg
  and the choice of association test), 1:06:58–1:11:51 (local assembly, phasing in trios, VCF
  phase notation), 1:11:51–1:15:19 (the pancreatic enhancer study), 1:15:19–1:16:32 (the twin
  study).
- Referred to but not contained in either source, and not reproduced here: the Heng Li article on
  the mathematics of SNP calling, the Genome Analysis Toolkit (GATK) documentation, the paper
  behind the pancreatic-enhancer result, and the twin study discussed at the end — the lecture
  pointed to these as further reading without giving full citations.

---

[← 19. Heritability and Quantitative Trait Loci](19-heritability-and-quantitative-trait-loci.md) · [Contents](index.md) · [21. Synthetic Biology: Building Genetic Circuits →](21-synthetic-biology-building-genetic-circuits.md)
