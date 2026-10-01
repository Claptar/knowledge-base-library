---
title: "19. Heritability and Quantitative Trait Loci"
course: "MIT 7.091J"
chapter: 19
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 19. Heritability and Quantitative Trait Loci

## What this covers

This chapter answers: given the complete genome sequence of a population of related individuals
and a measured quantitative trait, how do you find the genomic loci that influence it, how much of
the trait's variation can genetics explain in principle, and why do additive models built from the
loci you can find still leave most of that variation unexplained? It assumes familiarity with means,
variances and covariances, and with the idea of a likelihood-ratio test; it does not assume any
prior genetics beyond what "haploid" and "allele" mean.

## Two loose ends from last time

The lecture opens by closing out two points from the previous session on chromatin, before turning
to genetics.

**5C** maps which regions of the genome interact physically — the same question ChIA-PET answers,
but with specific primer pairs designed to query chosen locations rather than an any-to-any
pulldown. The protocol cross-links interacting loci, digests with a restriction enzyme, performs a
proximity ligation (joining only fragments that were physically brought together), reverses the
cross-link, and anneals the resulting 3C library to multiplexed T7/T3 primer pairs tiling the region
of interest; the ligation products are amplified by PCR and read out by sequencing or microarray. A
primer pair only produces a product if its restriction sites were ligated together, so the readout
directly reports which pairs of loci were in contact (Dostie and Dekker, 2007).

**CpG methylation** adds a methyl group to the cytosine in a CpG dinucleotide. Because the
dinucleotide is symmetric on the two DNA strands, the pattern can be copied from one strand to the
other during replication by DNA methyltransferase (DNMT) — an unmethylated cluster is methylated
de novo, and a hemimethylated cluster produced by replication is remethylated to restore the full
mark. This makes methylation a stable, heritable form of epigenetic modification, typically found
in regulatory regions of lowly expressed genes, where it silences expression by blocking regulatory
factor binding and by affecting chromatin state.

## The question for today: why are you like your relatives?

The rest of the lecture is about **heritability**: you resemble your relatives more than random
members of the population because you share components of your genome with them, and the
heritability of a trait is the fraction of its variance that genotype can explain. Such models
matter for understanding disease-associated variants and for pharmacogenomics — predicting which
therapy works best given a patient's genetic makeup. The lecture builds them by adding the
contributions of individual loci, **quantitative trait loci (QTLs)**, and ends by confronting the
fact that they typically explain only part of a trait's known heritability — the **missing
heritability** problem.

A genotype is the complete genome sequence (or markers describing how it differs from a reference).
A phenotype is defined by one or more traits, which may be non-quantitative (alive or dead in a
given environment) or quantitative (height, growth rate, gene expression level). A **QTL** is a
marker associated with a quantitative trait; an **eQTL** is one associated specifically with gene
expression. One resource worth knowing for simple, largely single-gene traits is OMIM (Online
Mendelian Inheritance in Man), a curated catalogue of roughly 21,000 human genes and their
associated Mendelian phenotypes, searchable by gene or by disease. Today's models are for the harder
case: traits influenced by many genes, discovered de novo from data.

Statistics notation used throughout: mean $\mu_x = \frac{1}{N}\sum_i x_i$, variance
$\sigma_x^2 = \frac{1}{N}\sum_i (x_i - \mu_x)^2 = E[(X-\mu_x)^2]$, and covariance
$\sigma_{xy}^2 = E[(X-\mu_x)(Y-\mu_y)]$, which is zero when $X$ and $Y$ are independent.

## A simple genetic model: counting genes from a binary cross

Start as simply as possible: a **haploid** model organism (yeast, one copy of each chromosome),
with the markers from the two parents drawn as unlinked (independently inherited), so each marker
is inherited from one parent or the other by an independent coin flip. In the binary model, each
marker is either "necessary" (filled) or "not necessary" (empty) for some all-or-nothing phenotype,
such as survival in a given environment.

If a trait requires getting *all* of a certain number of genes from one parent (an AND model), the
number of genes involved can be read off a simple cross: if mom is resistant to some substance and
dad is not, and you test $F_1$ progeny for resistance, then

$$N = \log_2\left(\frac{\#\ F_1\text{s tested}}{\#\ F_1\text{s with phenotype}}\right).$$

Worked in class: out of 32 $F_1$ individuals, 2 are resistant (mom resistant, dad not). Each
resistance gene is inherited from mom with probability $1/2$, independently, so the chance of
inheriting all $N$ of them is $(1/2)^N$. Observing $2/32=1/16$ resistant individuals means
$(1/2)^N=1/16$, i.e. $N=\log_2(32/2)=\log_2(16)=4$: four genes separate mom from dad for this trait.
(What the count measures is the number of genes that *differ* between the two parents and matter
for the trait — not an absolute count of genes "for" the trait in general.)

## From binary to quantitative traits

Now let the phenotype be continuous. Keep the same cross, but instead of a necessity flag, give
each of mom's genes an effect size of $0$ and each of dad's genes an effect size $1/N$, so that
dad's total contribution, if a child inherited all $N$ of his alleles, would be $1$. An example
phenotype is growth rate.

A child inherits each marker from mom or dad by an independent coin flip, so if $k$ is the number
of dad alleles a child inherits, $k$ can take $N+1$ distinct values ($0$ through $N$), and the
child's phenotype score (the sum of inherited effect sizes) is $k/N$. Since $k$ follows a binomial
distribution with $N$ trials and probability $1/2$,

$$p(k, N) = \binom{N}{k}(1-.5)^{N-k}(.5)^{k},$$

and for the normalized score $x = k/N$,

$$E[x] = .5, \qquad \sigma_x^2 = \frac{.25}{N}.$$

(A question from the floor caught an ambiguity here: the raw count $k$ has expectation $N/2$, not
$0.5$ — the professor agreed the slide's labeling conflated the raw count with the normalized score.
The two moments above are for $x=k/N$, consistent with each dad allele contributing $1/N$.) As $N$
grows, this binomial converges toward a normal distribution, so a trait controlled by many loci of
equal, additive effect looks approximately Gaussian in the population.

This simple model already contains the central difficulty of QTL mapping: as the number of
contributing genes $N$ grows, each gene's individual effect shrinks like $1/N$, and the variance it
contributes shrinks like $1/N$ too (consistent with $\sigma_x^2=.25/N$ falling as $N$ grows). A
trait can be completely heritable in principle and still be very hard to detect locus by locus if
it is spread over, say, a thousand genes of small effect — the signal from each one is buried in
noise.

**Linkage** complicates the picture further: markers that are physically close on a chromosome are
unlikely to be separated by crossing over during meiosis, so they are inherited together rather
than independently. Linked markers therefore show correlated inheritance, and because they travel
as a block, they behave as though they had a single, larger combined effect size.

## Partitioning phenotypic variance

Let $p_i$ be the quantitative phenotype of individual $i$, $g_i$ its genotype, and $e_i$ the
environmental contribution (how it was fed, how much sunlight it got — anything shaping the trait
that is not genetic). The model is

$$p_i = f(g_i) + e_i,$$

where $f$ is the function to be discovered: the mapping from genotype to phenotype. Over a
population,

$$\sigma_p^2 = \sigma_g^2 + \sigma_e^2 + 2\sigma_{ge}^2, \qquad E[e_i]=0,\ E[e_i^2]=\sigma_e^2.$$

Assuming (as essentially all such studies do) that genotype and environment are independent, the
covariance term vanishes and

$$\sigma_p^2 = \sigma_g^2 + \sigma_e^2.$$

There is nothing to be done about $\sigma_e^2$ except measure it. The way to measure it directly is
to hold genotype fixed: grow genetically identical individuals (clones, or for yeast, a population
of one genotype) separately and measure the variance in their phenotype — since the genotype term
vanishes, whatever variance remains is purely environmental. For humans, the closest equivalent is
studying monozygotic (identical) twins.

The independence assumption is not free, and for human studies it is often false: genotype can be
correlated with environment (through place of origin, or diet, for instance), in which case the
covariance term does not actually disappear and the decomposition above overstates what can be
attributed to genetics alone. This confounding is one of the practical obstacles to estimating
heritability outside a controlled laboratory setting.

## Two heritabilities, and why both matter

- **Broad-sense heritability**, $H^2$, is the fraction of phenotypic variance explained by genetic
  causes under an arbitrary (unconstrained) model of $f$. It describes the upper bound on phenotype
  prediction achievable by *any* model, and so reveals the underlying complexity of the molecular
  mechanism.
- **Narrow-sense heritability**, $h^2$, is the fraction explained when $f$ is restricted to be
  **additive** (linear in the genotype). It describes the upper bound achievable by a linear model,
  the relative resemblance between relatives and the utility of family disease history, and is the
  quantity efficient genetic mapping studies are built around.

Caveats worth keeping in mind: heritability is a property of a *population* (which alleles are
segregating, at what frequencies) and an *environment* (how much noise it contributes), not a fixed
property of a trait in the abstract. In practice "heritability" is often used without specifying
which sense is meant, or with an implicit assumption that they coincide — worth checking when the
term comes up. And both are genuinely hard to estimate well, because of the confounding problem
above.

**Broad-sense heritability** is

$$H^2 = \frac{\sigma_g^2}{\sigma_p^2} = \frac{\sigma_p^2-\sigma_e^2}{\sigma_p^2},$$

with $\sigma_e^2$ estimated from clones or identical twins. Worked example (reproduced from Hartl's
*Essential Genetics*): three genotypic classes ($aa$, $Aa$, $AA$) with no environmental variation
give a genotypic variance $\sigma_g^2=2.0$; the same genotypes grown under environmental noise
alone give $\sigma_e^2=1.0$; combined, $\sigma_p^2=\sigma_g^2+\sigma_e^2=3.0$, so

$$H^2 = \frac{2.0}{3.0} = \frac{2}{3}.$$

## The additive model and narrow-sense heritability

Restrict $f$ to a linear sum over discovered QTLs. Writing $g_{ij}\in\{0,1\}$ for the allele of
individual $i$ at QTL $j$, with coefficient $\beta_j$ and offset $\beta_0$,

$$f_a(g_i) = \sum_{j\in\text{QTL}} \beta_j g_{ij} + \beta_0.$$

One consequence of additivity falls out immediately: since a child inherits roughly half its alleles
from each parent, the expected value of a child's trait under this model is the midpoint of the two
parents,

$$E[f_a(g_i)] = \frac{f_a(p_1)}{2} + \frac{f_a(p_2)}{2}.$$

This was noticed long before QTL mapping existed: Galton's 1886 study of human height plotted
children's height against mid-parent height and found children's deviations from the population
mean to be consistently about two-thirds of their mid-parents' deviations — tall mid-parents had
children who tended to be shorter than they were, short mid-parents had children who tended to be
taller, a "regression toward mediocrity" that is the origin of the statistical term *regression*.
That children cluster near the mid-parent line is itself evidence that much of the variation in a
trait like height can be captured by an additive model.

Narrow-sense heritability is the fraction of phenotypic variance the additive model actually
explains:

$$\sigma_a^2 = \sigma_p^2 - \frac{1}{N}\sum_{i=1}^N \left(p_i - f_a(g_i)\right)^2, \qquad h^2 = \frac{\sigma_a^2}{\sigma_p^2}.$$

In words: take the total phenotypic variance, subtract the part the additive model fails to explain
(the mean squared residual), and divide by the total. Whatever gap remains between what the additive
model achieves and the broad-sense upper bound $H^2$ is one source of "missing heritability."

Reported $h^2$ values vary a good deal by kind of trait (Visscher et al. 2008): morphological traits
tend to be more heritable than fitness traits — human height is around $0.8$ and cattle yearling
weight around $0.35$, while *Drosophila* life history is around $0.2$ and wild-animal life history
around $0.3$. This suggests that predicting how tall you will be from your parents' height is more
productive than predicting how long you will live from how long they lived.

## Case study: mapping QTLs in a yeast cross

The lecture's running example is Bloom, Ehrenreich, Loo, Võ Lite and Kruglyak, "Finding the sources
of missing heritability in a yeast cross" (*Nature*, 2013). Two haploid yeast strains, BY and RM,
differ by only about 35,000 SNPs — roughly 0.5% of the genome, comparable to the divergence between
two unrelated humans. Both parents were sequenced at 50x coverage, so their genotypes are known
exactly; they were crossed to produce roughly 1,000 $F_1$ segregants, each genotyped on a microarray
that calls, at every marker along all 16 chromosomes, whether that stretch came from BY or RM. Each
segregant was then phenotyped for growth (via colony size) in 46 conditions — different sugars,
heavy-metal and drug stressors, and so on. Because some conditions could be measuring much the same
underlying biology, the authors checked pairwise correlations in growth rate across conditions and
found clusters of correlated traits (among the sugar conditions and ethanol, for example), so the
46 phenotypes are not all independent.

## LOD scores: testing one marker at a time

For a single marker, the test is: does conditioning on this marker's genotype change the mean
phenotype? One hypothesis is that phenotype is essentially the same whether the marker is $0$ or
$1$ (a single mean, $\mu$, fits well); the alternative is that phenotype is better described by two
different means $\mu_0,\mu_1$, one per genotype at that marker. This is a likelihood-ratio test
between a one-parameter and a two-parameter model, summarized as a **LOD score**:

$$LOD = \log_{10}\prod_{i=1}^N \frac{P(p_i \mid g_{ij}, \mu_0,\mu_1,\sigma)}{P(p_i\mid \mu,\sigma)}.$$

The study had 11,623 unique, unlinked markers to test for each of the 46 traits — enough that some
will look significant by chance alone. The fix is a **permutation test**: scramble the pairing
between genotypes and phenotypes and recompute the LOD scores for all markers; repeat 1,000 times
to build a null distribution of LOD scores reflecting pure chance. Because the permutation already
runs over all markers being tested, reading a threshold off it handles the multiple-testing
correction automatically — no separate correction is needed. The threshold is set so only 5% of the
null distribution's mass lies beyond it (FDR $=0.05$); in the first round here that threshold was a
LOD score of $2.63$, and any marker whose real (unpermuted) LOD score exceeds it is accepted as a
QTL.

<figure>
<svg viewBox="0 0 340 210" role="img" aria-label="Null distribution of permuted LOD scores, with the 5 percent tail beyond the significance threshold shaded.">
  <line x1="30" y1="160" x2="310" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <path d="M30,150 C55,30 80,20 105,35 C135,55 165,85 195,115 C220,135 250,150 310,158"
        fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M225,124 C250,143 280,153 310,158 L310,160 L225,160 Z"
        fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <line x1="225" y1="160" x2="225" y2="121" stroke="currentColor" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="225" y="112" text-anchor="middle" font-size="12" fill="currentColor">LOD = 2.63</text>
  <text x="270" y="148" text-anchor="middle" font-size="11" fill="currentColor">5% (FDR)</text>
  <text x="170" y="185" text-anchor="middle" font-size="12" fill="currentColor">LOD score, 1000 permutations</text>
  <text x="18" y="90" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 18 90)">frequency</text>
</svg>
<figcaption>The distribution of LOD scores computed after randomly permuting genotype–phenotype
pairings 1,000 times. The threshold is set where only 5% of this null distribution lies beyond it;
a real marker's LOD score is compared against that threshold to decide whether it is a QTL.</figcaption>
</figure>

## Iterating on the residuals

Fitting the additive model with the first-pass significant QTLs leaves a residual for each
individual: observed phenotype minus the model's prediction. The next step is to repeat the whole
discovery procedure — including a fresh permutation and a fresh threshold — on these residuals
rather than the original phenotype, to find a second set of QTLs; the model is expanded to include
both sets, new residuals are computed, and the process repeats a third time.

This can find more QTLs than a single pass because a locus's effect can be too small to clear the
threshold while competing against the variance contributed by other, larger-effect QTLs; once those
are subtracted out, a smaller signal previously swamped can become visible. A question raised in
class: since the threshold is recomputed by permutation at every round, could discarding the first
round's "false positives" distort the next round's threshold? The professor conceded that the
threshold genuinely has to be reset each iteration, since the model has changed — though he noted
it is hard to call something a false positive once it has demonstrably improved prediction.

## What this procedure found

For growth in the compound E6 berbamine, the full panel of roughly 1,000 segregants yielded 15
significant QTLs, explaining 78% of narrow-sense heritability for that trait; repeating the
identical procedure on only 100 segregants found just 2 significant QTLs, explaining 21% of the
variance — severely underpowered. Plotting LOD score against genome position typically shows not a
sharp spike but a gradual rise and fall around a causal locus: markers physically near the true QTL
are linked to it, correlated with it, and show partial, decaying signal further away.

Statistical power depends on both the number of individuals and the number and effect size of the
loci contributing: more loci means a heavier multiple-testing burden, and smaller effect sizes both
require more individuals to detect reliably.

Across all 46 traits, detected QTLs recovered narrow-sense heritability well: variance explained
tracked $h^2$ closely (72–100% of it), and a cross-validated additive model of 22 QTLs predicted
observed phenotype (growth in lithium chloride) well enough to explain 88% of $h^2$, with predicted
and observed values close to the diagonal. Most individual QTLs, though, have small effect — the
fraction of variance a QTL explains is the square of its fitted coefficient, $\beta_j^2$, and a
histogram of effect sizes across all 46 traits is heavily right-skewed (fit by a truncated
exponential). Traits were typically explained by 5 to 29 QTLs (median 12) at the 5% FDR threshold.

The gap shows up when $h^2$ is compared against $H^2$ rather than against the additive model's own
residual: plotted against each other across the 46 traits, narrow-sense heritability falls
consistently below broad-sense heritability. That persistent gap — genetic variance the additive
model cannot reach, even though it is present according to the clone-based estimate of $H^2$ — is
the missing heritability this study set out to chase down, and because every variant in this cross
is known (50x sequencing of both parents), the gap cannot be attributed simply to variants that were
never looked for.

## Where missing heritability could be hiding

A non-exhaustive list of candidate explanations, drawn partly from what the slides name and partly
from what the class proposed when asked: incorrect heritability estimates (including misestimated
environmental variance — if replicate "identical" environments are not actually identical, the
apparent genetic/environmental split shifts); non-chromosomal elements; rare variants; structural
variants; many common variants of individually low effect (the statistical-power problem already
discussed); and **epistasis** (non-linear, gene–gene interactions). Epigenetic marks were raised as
a possibility too, though the slides' own list does not include that category explicitly.

**Epistasis** is where an additive model fails structurally, not just for lack of power. Consider
two loci with phenotype values

$$f(ab)=0,\qquad f(aB)=f(Ab)=1,\qquad f(AB)=0,$$

an exclusive-or pattern. Neither locus has any effect on its own — averaged over the other locus's
state, each allele's marginal effect is zero — so neither would be detected by the single-marker
test above. Assuming no environmental noise, this trait has $H^2=1$ (genotype determines phenotype
completely) and $h^2=0$ (a linear model captures none of it): the entire gap between the two
heritabilities can in principle come from an interaction invisible to additive testing. Such
interactions can involve more than two loci, but testing all combinations is not tractable: testing
all pairs among 11,623 markers is a far larger multiple-hypothesis problem than testing the markers
singly, and statistical power collapses under the correction it would require. The workaround used
in the study was to restrict attention to pairs involving at least one locus already identified as
a significant single-marker QTL for that trait — on the order of 20 loci, each tested against all
other markers, rather than all markers against each other.

With that restricted search, pairwise interactions were found in 24 of the 46 traits. The clearest
example was growth in maltose, where an interaction between a locus on chromosome 7 and one on
chromosome 11 explained 71% of the gap between broad- and narrow-sense heritability for that trait:
individuals with the BY allele at both loci had a markedly lower phenotype than individuals carrying
the RM allele at either one, a jump rather than the gradual increase an additive effect would give.
For most other traits, though, the pairwise interactions found did not close the gap nearly as much
— so pairwise epistasis among the markers tested is only a partial answer.

**Non-chromosomal inheritance** is a separate source entirely. Besides the nuclear chromosomes,
mitochondria are inherited too, and the two parent strains can carry different mitochondrial
genomes. A second, less obvious cytoplasmic element is the yeast "killer" system: wild yeast strains
often carry a cytoplasmic (non-chromosomal) viral element, and crossing such a strain with the
standard laboratory strain (S288C — used because it is fully sequenced and well-behaved) passes
that element to all the progeny, where it interacts with chromosomal variants: a given chromosomal
deletion's phenotypic effect can depend on whether the strain also carries the killer element. This
is why the gene *MKT1* ("maintenance of killer toxin 1") turned up as a significant QTL in many past
yeast crosses for seemingly unrelated traits — it governs competence for the killer element, so its
apparent effect on a trait is really mediated by whether that cytoplasmic element is present.
Edwards et al. (2014) showed this directly for the gene *PEP7*: a model using only the chromosomal
deletion leaves a large unexplained gap between mutant and wild-type phenotype; adding the
non-chromosomal ([kil-k] versus [kil-0]) element as a second, additive term narrows it; only a model
that also includes an explicit **interaction term** between the two removes the gap almost
entirely.

## Missing heritability beyond yeast

The problem is not confined to a controlled cross. Manolio et al. (2009) tabulated, after hundreds
of human GWAS studies, how many loci had been found for several complex traits and what fraction of
each trait's estimated heritability they explained:

| Disease/trait | Number of loci | Heritability explained |
| --- | --- | --- |
| Age-related macular degeneration | 5 | 50% |
| Crohn's disease | 32 | 20% |
| Systemic lupus erythematosus | 6 | 15% |
| Type 2 diabetes | 18 | 6% |
| HDL cholesterol | 7 | 5.2% |
| Height | 40 | 5% |
| Early-onset myocardial infarction | 9 | 2.8% |
| Fasting glucose | 4 | 1.5% |

For most of these traits, the loci found so far account for only a small fraction of the
heritability known (from family and twin studies) to be there — the same gap seen in the yeast
cross, at a much larger and harder-to-control scale.

The slides' suggestions for where to look next: use external data (SNPs sitting in enhancers,
nonsense mutations, and so on) to shrink the marker search space before testing interactions, since
a smaller space makes non-linear interaction testing tractable; explicitly consider non-chromosomal
genetic elements; and use complementary data — protein-protein interaction networks, for instance —
to decide which marker pairs are worth testing for interaction, rather than testing blindly. Beyond
that, the slides leave the question open.

## Sources

- Slides: `19-slides.md` — all section headings and figures, including the statistics review, the
  binary and quantitative haploid cross diagrams, the broad/narrow heritability definitions and the
  Hartl textbook figure, Galton's 1886 regression figure, the LOD score and QTL-discovery slides,
  the Bloom et al. figures (crossing scheme, LOD plots, effect-size histogram, heritability
  scatterplots, pairwise-interaction figure), the Edwards et al. figure, and the Manolio et al.
  table. The 5C workflow and CpG methylation slides at the top of the deck.
- Transcript: `recordings/lectures/19.md`, 00:00–03:21 (5C and CpG recap), 03:21–09:58 (heritability
  framing, OMIM, genotype/phenotype definitions), 10:07–23:31 (binary and quantitative haploid
  models, the 32-individual worked example, linkage), 23:31–32:40 (variance partition, measuring
  environmental variance, confounding), 32:40–41:32 (broad/narrow heritability, the Hartl example,
  the additive model, Galton, example $h^2$ values), 41:32–1:03:47 (the Bloom et al. study design,
  LOD scores, permutation testing, iterative residual fitting, results), 1:03:47–end (missing
  heritability discussion, epistasis, non-chromosomal elements, MKT1/killer virus, Edwards et al.,
  Manolio et al., closing remarks).
- Named but not contained in the supplied material: Dostie and Dekker, "Mapping Networks of Physical
  Interactions Between Genomic Elements using 5C Technology," *Nature Protocols* 2(4) (2007); Hartl,
  *Essential Genetics: A Genomics Perspective* (Jones & Bartlett, 2011); Galton, "Regression towards
  mediocrity in hereditary stature" (1886); Visscher, Hill et al., "Heritability in the Genomics
  Era," *Nature Reviews Genetics* 9(4) (2008); Bloom, Ehrenreich, Loo, Võ Lite and Kruglyak, "Finding
  the sources of missing heritability in a yeast cross," *Nature* 494 (2013); Edwards,
  Symbor-Nagrabska et al., "Interactions Between Chromosomal and Nonchromosomal Elements Reveal
  Missing Heritability," *PNAS* 111(21) (2014); Manolio, Collins et al., "Finding the Missing
  Heritability of Complex Diseases," *Nature* 461 (2009).

---

[← 18. Reading Chromatin State and Genome Looping](18-reading-chromatin-state-and-genome-looping.md) · [Contents](index.md) · [20. Genome-Wide Association Studies →](20-genome-wide-association-studies.md)
