---
title: "18. Reading Chromatin State and Genome Looping"
course: "MIT 7.091J"
chapter: 18
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 18. Reading Chromatin State and Genome Looping

## What this covers

This chapter answers three linked questions about how a genome is regulated beyond its raw
sequence: how can we read off the functional state of a stretch of chromatin from the chemical
marks on it, how do regulatory proteins choose which of their many possible binding motifs to
occupy, and how can we tell which distal regulatory region controls which gene. It assumes the
reader already has ChIP-seq, hidden Markov models and Bayesian networks, and the ROC curve as a
way of scoring a classifier. The three computational tools introduced are a dynamic Bayesian
network for annotating the genome from histone marks, a log-likelihood-ratio test for calling
protein occupancy from DNase-seq footprints, and the hypergeometric distribution for deciding
whether a physical interaction between two genomic locations is more than chance.

## Chromatin has several layers, and the marks on it carry information

Epigenetic state regulates gene function without changing the underlying DNA sequence. One way to
picture it: the genome is a hotel with many rooms, most of the doors locked. Only where a door is
open — where chromatin is accessible — can regulation, transcription and translation actually
happen in that region. Chromatin organization has several nested structural layers, each carrying
functional information:

- the primary DNA sequence, including methylated CpGs (cytosine–phosphate–guanine); the mark is
  symmetric across the two strands, so a methyltransferase can copy it onto the new strand during
  replication, making it heritable;
- histone tails — chemical modifications on the amino termini of histones H3 and H4 that act as
  signposts for what is going on at that location;
- whether the chromatin is compacted (closed) or open, which relates to whether DNA-binding
  proteins can access it at all;
- association of some genomic domains with the nuclear lamina.

A schematic of an active gene shows an enhancer contacting the RNA polymerase II start site, with
characteristic histone marks at both the active gene and the active enhancer. An inactive gene
nearby can carry a boundary element bound by CTCF, which acts as a genomic insulator, blocking the
effect of the enhancer on the gene below it.

Decades of biochemistry have characterized how these marks transition as a gene switches between
states. Genes with high CpG content in their promoters cycle between active and inactive states:
repressed carries H3K27 trimethyl, poised carries both H3K4 trimethyl and H3K27 trimethyl, and
active carries H3K4 trimethyl alone. Genes with low CpG content instead go from a silenced state
(no marks, but the DNA itself methylated) through intermediate marks to H3K4 trimethyl when active.
Active enhancers characteristically carry H3K4 monomethyl together with H3K27 acetyl.

## Learning the histone code automatically: dynamic Bayesian networks

Knowing from the literature which combination of marks means "enhancer" or "poised promoter" is
useful, but the genome does not arrive labelled, and the aim is to annotate it computationally
rather than by memorizing the literature. ChIP-seq against a panel of histone marks gives one data
track per mark along the genome; what is needed is a way to turn many such tracks into a single
annotation per position.

One option is a hidden Markov model over fixed-width bins of the genome. The alternative presented
is a **dynamic Bayesian network**, as used by the tool **Segway**: still a Bayesian network — a
directed acyclic graph — but one that models data sampled along a spatial axis (the genome)
instead of along time, at base-pair resolution, and that can handle missing data cleanly by simply
not modelling it where it is absent.

The network has, along the bottom, one observation variable per base: the level of a particular
histone mark at that position, as read off from mapped reads. Beside each observation is an
indicator variable recording whether data is present there at all (if it is absent, that
observation is simply not modelled). Above the observations sits the variable that matters, $Q$:
the hidden state at that position. Each state describes an ensemble of expected mark outputs — in
effect, the mean level of every mark that state is expected to produce. Above $Q$ sit counter
variables, whose job is to force a state transition once a state has run for its maximum allowed
length, so that states cannot persist forever the way they can in an unconstrained HMM.

Fitting the model learns, unsupervised, both what each state means (the marks it outputs) and the
transition structure between states; meaning is assigned to a state afterwards by matching its
output against what the literature says those marks mean (as for the comparable tool, ChromHMM).
Once trained, held-out data is decoded with a Viterbi-style decoder, as for an HMM, to read off the
most likely state at every base.

There is no principled rule for how many states to use: too many and the model fits noise; too few
and distinct states collapse together, so the number is chosen by trial and error and checked
against what is already known about genome function. The payoff is finding regions such as active
enhancers purely from the mark data — positions decoded to H3K4 mono- or dimethyl together with
H3K27 acetyl, say — without reference to the primary sequence at all.

## Why only some of the possible binding sites are occupied

The second question is a genuine puzzle: there are hundreds of thousands of instances of a given
regulatory motif in the genome, but only tens of thousands are actually occupied by the
corresponding factor. It is not that the occupied copies carry a different sequence — identical
motif sequences can be bound in one cell type (say, endoderm) and not another (say, ES cells). So
sequence alone does not decide occupancy; something about chromatin state does.

**DNase-seq** reads out chromatin accessibility directly. Chromatin is exposed to DNase I, which
cuts (nicks) DNA preferentially where it is open; the cut fragments are then size-selected and
sequenced. Reads pile up where DNA is accessible and are depleted — "shadowed" — wherever a
histone or another protein covers the DNA (a nucleosome wraps about 147 bases). Averaged over
thousands of binding instances of the same factor, this produces a reproducible **protection
profile**, the characteristic footprint that factor casts on a roughly 400-base window around its
motif; CTCF's averaged profile even shows a periodic dip pattern from the nucleosomes it phases. A
single binding instance, by contrast, is sparse and noisy compared with the clean aggregate
profile, so any method built on this data has to work against substantial per-site noise.

The method presented, **PIQ**, takes three inputs — the genome sequence, the motifs of the factors
of interest (hundreds at a time, in practice), and aligned DNase-seq read counts — and outputs, for
every motif instance, a probabilistic call of whether the corresponding factor is occupying it.
Its design goals are robustness to low coverage and noise, calling many factors from one
experiment at once, genome scale, high spatial accuracy, and reasonable behaviour in bad cases.

The model has two pieces. First, a background model of what the *unoccupied* genome looks like:
read counts at each base are modelled as Poisson, with the log rate itself drawn from a
multivariate normal whose covariance structure lets information be shared ("smoothed") across
neighbouring bases — so a base with little direct coverage can borrow strength from its
well-covered neighbours. Second, a learned protection profile for every motif describing the
pattern of read depletion and enrichment that factor's binding produces; the profile excludes
positions immediately under the motif, since the DNase I enzyme itself has some intrinsic sequence
bias there, and a profile is only used if it is statistically robust above background.

The two pieces combine through a **binding indicator** $\delta$ at each motif instance, which
switches the protection profile on or off in the predicted read counts, and a **log likelihood
ratio** — the log of the probability of the observed counts given the protein is bound there, over
the probability of the same counts given it is not. That log-ratio, combined with some prior
information, is the test statistic ranked across all instances of a motif; significance is set by
comparison against a null distribution of the statistic computed at genomic locations known not to
be occupied, at a chosen p-value in the tail.

Validated against ChIP-seq as a gold standard for three mouse ES cell factors, the area under the
ROC curve exceeds 0.9; across 313 ChIP-seq experiments from the ENCODE project, matched against
DNase-seq from the same cell types, the mean AUC is 0.93. Roughly 75 factors are strongly
detectable this way — detectability depends on having a strong motif, binding in DNase-accessible
regions, and strong DNA-binding affinity.

## Pioneer factors open chromatin; settlers follow

A separate question is how chromatin opening and closing is itself controlled. Because DNase-seq
reads out accessibility directly, accessibility measured at two related developmental time points
reveals which locations changed, and which motifs sit at the locations that opened. **Pioneer
factors** are hypothesized to bind *closed* chromatin and open it; known examples include FoxA and
some of the iPS reprogramming factors. Non-pioneer motifs, by construction of the comparison, show
no corresponding gain in accessibility.

<figure>
<svg viewBox="0 0 420 180" role="img" aria-label="Pioneer factors open closed chromatin, then settler factors bind the resulting open chromatin">
  <rect x="20" y="60" width="100" height="60" rx="6" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <circle cx="45" cy="80" r="8" fill="currentColor" fill-opacity="0.4"/>
  <circle cx="70" cy="95" r="8" fill="currentColor" fill-opacity="0.4"/>
  <circle cx="95" cy="80" r="8" fill="currentColor" fill-opacity="0.4"/>
  <text x="70" y="140" text-anchor="middle" font-size="12" fill="currentColor">closed chromatin</text>

  <line x1="130" y1="90" x2="190" y2="90" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow18)"/>
  <text x="160" y="75" text-anchor="middle" font-size="11" fill="currentColor">pioneer binds,</text>
  <text x="160" y="105" text-anchor="middle" font-size="11" fill="currentColor">opens chromatin</text>

  <rect x="200" y="60" width="100" height="60" rx="6" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <circle cx="225" cy="100" r="6" fill="currentColor" fill-opacity="0.3"/>
  <text x="250" y="140" text-anchor="middle" font-size="12" fill="currentColor">open chromatin</text>

  <line x1="310" y1="90" x2="370" y2="90" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow18)"/>
  <text x="340" y="75" text-anchor="middle" font-size="11" fill="currentColor">settler</text>
  <text x="340" y="105" text-anchor="middle" font-size="11" fill="currentColor">binds</text>

  <rect x="380" y="60" width="30" height="60" rx="6" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <defs>
    <marker id="arrow18" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0 0, 8 4, 0 8" fill="currentColor"/>
    </marker>
  </defs>
</svg>
<figcaption>A pioneer factor binds closed chromatin and opens it; a settler factor then binds
preferentially in the now-open chromatin the pioneer created.</figcaption>
</figure>

Three computational indices flagged candidate pioneers from the accessibility data alone: a
*dynamic* opening index (change in accessibility between two time points), a *static* openness
index (how open chromatin already is around a factor's sites), and a *social* index (how many
other factors' motifs cluster around a given factor's sites). Factors scoring highly across these
were classified as computational pioneers.

Correlative computational analysis is never causal on its own, so the predictions were tested with
a reporter construct: a candidate pioneer's motif was placed upstream of a retinoic acid receptor
site driving GFP, designed so the pioneer could not simply activate GFP by itself — GFP only turns
on if the pioneer opens the chromatin *and* the downstream activator (plus retinoic acid) is also
present. Almost all of the factors predicted to be pioneers produced GFP activity in this assay.
Through this approach, about 120 motifs were identified as corresponding to proteins that open
chromatin.

Some of the learned protection profiles are asymmetric — more depletion/enrichment on one side of
the motif than the other (seen for NRF1, for example). This asymmetry is only visible because the
motif itself is not palindromic, so the genome can be oriented relative to it, which raises the
question of whether the opening itself is directional. This was tested by cloning the motif into
the reporter construct in both orientations: GFP turned on only when the motif was in the
orientation matching its DNase-seq asymmetry, confirming that at least some pioneers open
chromatin **directionally**.

This gives two classes of factor: **pioneers**, which open closed chromatin, and **settlers**,
which bind preferentially wherever chromatin is already open — following behind the pioneers
rather than opening anything themselves.

Two further experiments tested the model in vivo. Dominant-negative constructs of two pioneers
(NFYA and Nrf1) — retaining only the DNA-binding domain, lacking whatever domain performs the
remodelling — reduce DNase hypersensitivity at native NFYA and Nrf1 sites when induced, relative to
wild type ($p<0.01$). The same dominant-negative NFYA also reduces ChIP-qPCR binding of a
downstream factor, c-Myc, at sites predicted to be pioneered by NFYA but not at non-pioneered
sites, and asymmetrically: binding drops on the side NFYA is predicted to open and is largely
unaffected on the other side — further, in vivo, confirmation of directional opening.

A comparison of the chromatin opening index for a given motif across human and mouse data found it
largely conserved evolutionarily ($r^2 = 0.84$): the same factors tend to act as pioneers in both
species.

Summarizing this half of the lecture: PIQ predicts TF binding from DNase-seq data accurately; it
can identify pioneer factors that regulate proximal chromatin opening and TF binding; certain
pioneer factors are directional; and settler factors follow pioneer binding, with loss of pioneer
binding returning the chromatin to a closed state.

## Mapping enhancers to the genes they regulate

The traditional way to assign a regulatory region (or a SNP) to a target gene is to pick the
nearest gene. But roughly a third of regulatory sites in the genome skip over their nearest gene to
regulate one farther away, so nearest-gene assignment is often wrong, and a more direct, molecular
way of making the connection is needed.

The physical mechanism is genome looping: an enhancer, together with cohesin, mediator and master
regulators, is brought into contact with the Pol II holoenzyme sitting at a gene's promoter. If
these looped complexes can be captured and the two ends of DNA involved identified, the enhancer
can be tied directly to the gene it is contacting.

**ChIA-PET** (Chromatin Interaction Analysis by Paired-End Tag sequencing) is one protocol in this
family, restricted to interactions mediated by one chosen protein — here, RNA polymerase II, which
makes the interactions found specifically ones involving actively transcribed genes. The protocol:
cross-link the complexes in place, immunoprecipitate for the protein of interest, sonicate, and
ligate the resulting DNA in a very dilute solution. Dilution matters because it favours ligation
between the two ends already held together by the same protein complex, rather than between
unrelated fragments. This produces two classes of product: **self-ligation** products, where a
fragment ligates back to itself, and **inter-ligation** products, where a fragment from the
enhancer joins a fragment from the gene the polymerase was transcribing. Sequencing the
inter-ligation products from both ends and mapping them to the genome gives pairs of loci that were
physically interacting.

Example data from the SOX2 locus, shown across the same roughly 600,000-base window in three cell
states — pluripotent mouse ES cells, motor neurons produced by a small-molecule protocol over seven
days, and motor neurons produced by ectopic expression of three reprogramming transcription
factors — combines Pol II ChIA-PET loops with ChIP-seq for a relevant factor in each state. In ES
cells, SOX2 regulates its own locus; in the small-molecule motor neuron state, OLIG2 (a key
regulator of that fate) appears to regulate SOX2 instead; in the induced motor neuron state, LHX3
(one of the reprogramming factors) is seen interacting with the SOX2 locus.

The resolution of this kind of data is on the order of the size of the window shown, not
single-base-pair resolution, since each sequenced read pair spans many bases at each end and the
protocol does not pin down an exact start and end for a loop. Shearing effects can be deconvolved
computationally to bring resolution down to roughly 10–100 base pairs, but identifying the exact
motif under an interaction still requires an integrative step: scanning the implicated region for
motifs, or combining it with matched DNase-seq data to ask what protein's protection profile is
present there.

## Is an observed interaction real? The hypergeometric test

Suppose a location $A$ in the genome accumulates $c_A$ ligation-event ends, a location $B$
accumulates $c_B$ ends, and $N$ is the total number of ligation event ends genome-wide. Of those,
$I_{A,B}$ are observed to be inter-ligation events specifically between $A$ and $B$. The question
is whether that count is more than would be expected if ligation partners were chosen at random.

<figure>
<svg viewBox="0 0 400 190" role="img" aria-label="Read ends at two genomic loci, most ligating elsewhere, a few ligating between the two loci">
  <line x1="20" y1="150" x2="380" y2="150" stroke="currentColor" stroke-width="1.5"/>
  <text x="200" y="175" text-anchor="middle" font-size="12" fill="currentColor">genome</text>

  <rect x="60" y="140" width="24" height="20" fill="currentColor" fill-opacity="0.25"/>
  <text x="72" y="130" text-anchor="middle" font-size="12" fill="currentColor">A</text>
  <text x="72" y="115" text-anchor="middle" font-size="11" fill="currentColor">c_A ends</text>

  <rect x="300" y="140" width="24" height="20" fill="currentColor" fill-opacity="0.25"/>
  <text x="312" y="130" text-anchor="middle" font-size="12" fill="currentColor">B</text>
  <text x="312" y="115" text-anchor="middle" font-size="11" fill="currentColor">c_B ends</text>

  <path d="M72 140 C 150 60, 230 60, 312 140" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="192" y="55" text-anchor="middle" font-size="12" fill="currentColor">I(A,B) inter-ligation events</text>

  <path d="M72 140 C 40 90, 10 70, 10 40" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <path d="M312 140 C 350 90, 380 70, 380 40" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="200" y="20" text-anchor="middle" font-size="11" fill="currentColor">remaining ends ligate elsewhere, at random under the null</text>
</svg>
<figcaption>The hypergeometric setup: of c_A ends at A and c_B ends at B, out of N total ends
genome-wide, I(A,B) of them happen to ligate to each other.</figcaption>
</figure>

Under the null hypothesis that every ligation event end has equal probability of ligating with any
other end, this is a hypergeometric sampling problem — the same distribution used elsewhere in the
course for testing whether an overlap between two sets is more than chance. The probability of
observing exactly $I_{A,B}$ shared ends is

$$P(I_{A,B} \mid N, c_A, c_B) = \frac{\binom{c_A}{I_{A,B}}\binom{N - c_A}{c_B - I_{A,B}}}{\binom{N}{c_B}}$$

and the significance of observing *at least* that many is the upper-tail sum

$$p = \sum_{i=I_{A,B}}^{\min\{c_A, c_B\}} P(i \mid N, c_A, c_B).$$

A small $p$ rejects the null of random ligation and supports treating $A$ and $B$ as a genuine
interacting pair.

## Estimating how many true interactions exist in total

A related but different question: having run the experiment and obtained some number of
interactions, how many interactions are actually out there, including ones the experiment missed?
Suppose two replicate experiments each yield some number of called interactions, with a certain
number common to both. Treating the interactions found in each replicate as two samples of sizes
$m$ and $n$ drawn (without replacement) from an unknown total population of $N$ true interactions,
with $k$ shared between the two samples, is again a hypergeometric problem — now solved for the
population size:

$$\hat{N} = \operatorname*{argmax}_N \left[P(X = k; N, m, n)\right]$$

With $m = n = 1000$ events in each replicate and $k = 900$ shared, this predicts about 1100 total
events exist.

This maximum has an approximate closed form,

$$\hat{N}(m, n, k) = \frac{mn}{k},$$

motivated by approximating the hypergeometric with a binomial — $X=k$ drawn from $n$ trials with
success probability $p = m/N$ — and that binomial with a normal distribution:

$$P(X = k; N, m, n) \approx \text{Binomial}\left(X = k;\, n = n,\, p = \frac{m}{N}\right) \approx \text{Normal}\left(X = k;\, \mu = \frac{mn}{N},\, \sigma^2 = \frac{mn}{N}\left(1 - \frac{m}{N}\right)\right).$$

**Allowing for false positives.** If some of the events called in each replicate are false
positives, the formula above overestimates the total. The correction assumes the events shared
between the two replicates are true positives, and that a fraction $(1-f)$ of the remaining,
non-shared events in each replicate are false negatives, where $f$ is the true positive rate —
rescaling the two sample sizes before the same argmax computation is applied:

$$m' = (1 - f)(m - k) + k, \qquad n' = (1 - f)(n - k) + k.$$

Applied to a real pair of replicates — 3811 events in replicate A, 1384 in replicate B, and 533
events common to both — the estimated total depends strongly on the assumed true positive rate:
$\hat{N} = 7180$ at $\text{TPR}=0.80$, $\hat{N} = 8482$ at $\text{TPR}=0.90$, and $\hat{N} = 9896$
at $\text{TPR}=1.00$. A higher assumed true positive rate pushes the estimated total upward for the
same observed overlap.

## What goes wrong with ChIA-PET

1. **High false negative rate.** Repeating the experiment under matched conditions and getting,
   say, ten thousand interactions each time but only a small overlap between the two runs is the
   central practical problem — the libraries produced are not complex enough for more sequencing
   alone to recover much additional signal, so this is a limit on the biology captured, not just on
   sequencing depth.
2. **It is specific to whichever protein is immunoprecipitated** — RNA polymerase II in the
   examples above — so it only reveals interactions mediated by that one protein.
3. A further noise source is **chimeric ligation**: fragments from two unrelated, nearby
   cross-linked complexes ligating to each other by chance rather than reflecting a real
   interaction. The chimeric rate can be estimated by splitting a single preparation into two
   halves, tagging each half with a distinct linker, recombining them, and counting how many
   resulting molecules carry linkers from both halves — those are necessarily chimeric, since they
   could only have formed after the split. Chimeric rates of around 20% were typical at the time
   (down from roughly 50% previously).
4. **Hi-C and related protocols may eventually address these limitations.** ChIA-PET sits in a
   family that also includes 3C (interactions between one chosen pair of loci), 4C (one chosen
   locus against all others) and 5C (many loci against many others); ChIA-PET and Hi-C, like 5C,
   can in principle reveal many-to-many interactions from a single experiment, with ChIA-PET
   restricted to those mediated by one immunoprecipitated protein.

## Sources

- Slides, `lectures/18-slides.md`: chromatin-layer and histone-mark-transition diagrams; the
  Segway dynamic Bayesian network figure; the PIQ/pioneer-factor results (dominant-negative
  NFYA/Nrf1 figures, human/mouse pioneer-conservation plot, overview-of-results slide); the
  ChIA-PET protocol diagram and example SOX2 locus tracks; the hypergeometric significance
  formula; the overlap-based total-event estimator, its normal approximation, the false-positive
  correction, and the 3811/1384/533 replicate example.
- Transcript, `recordings/lectures/18.md`: the "hotel" framing of epigenetic state (00:00–02:12);
  the Segway walkthrough and Q&A on states, counters and model selection (11:10–19:17); the
  DNase-seq/PIQ model, including the Poisson/multivariate-normal background and the
  log-likelihood-ratio statistic (23:53–36:02); the pioneer/settler narrative, GFP reporter
  validation, and directional-opening Q&A (38:25–51:55); the live derivation of the hypergeometric
  interaction test and the overlap-based total-event estimate (54:18–1:19:00); the ChIA-PET
  protocol devised interactively with the class, chimeric-ligation estimation, and the
  3C/4C/5C/Hi-C discussion (56:39–1:14:07).
- The slide citing the dominant-negative pioneer figures names its source as Sherwood, Hashimoto,
  et al., "Discovery of Directional and Nondirectional Pioneer Transcription Factors by Modeling
  DNase Profile Magnitude and Shape," *Nature Biotechnology* 32, no. 2 (2014): 171–8 — referred to
  by the lecture but not itself supplied as course material.
- The lecture also refers to, without supplying, the ChromHMM tool (as a comparison point for
  Segway), the ENCODE project's compendium of ChIP-seq experiments, and the Epigenome Roadmap
  Initiative's cross-cell-type mark profiling.

---

[← 17. Logic Models of Cell Signaling](17-logic-models-of-cell-signaling.md) · [Contents](index.md) · [19. Heritability and Quantitative Trait Loci →](19-heritability-and-quantitative-trait-loci.md)
