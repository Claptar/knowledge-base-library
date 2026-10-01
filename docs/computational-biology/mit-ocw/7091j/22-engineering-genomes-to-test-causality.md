---
title: "22. Engineering Genomes to Test Causality"
course: "MIT 7.091J"
chapter: 22
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 22. Engineering Genomes to Test Causality

## What this covers

This chapter follows a guest lecture (the speaker is identified only as "PROFESSOR" in the
transcript) on using genome engineering to test causality, given with no slide deck. It assumes
the reader already has the earlier course's tools for *analysing* a genome — read mapping,
variant calling, genome browsers — and asks the complementary question: once you have a
hypothesis about what a piece of DNA does, how do you build the genome that tests it, at a scale
running from a single base pair to a genome where nearly every codon has been reassigned? The
chapter follows the lecture from a bacterial case study — a genome recoded for biocontainment, new
chemistry, and virus resistance — through to human genome editing and the question of how
causality is established in human disease, where the "experiment" is a cell line rather than a
population of bacteria.

## Why engineer a genome at all

The lecture opens by tying genome engineering directly to causality. A hypothesis produced by
analysing a genome — this variant explains that phenotype — can only be confirmed by building the
change and testing it, and a high-throughput way of doing that lets you work with very small
cohorts, even cohorts of one, since false positives stop being the dominant worry once the variant
can be built and tested directly.

The simplest version is changing a single base pair to test a single SNP. Real phenotypes are
often multigenic, though, and at the extreme end the lecture poses a more radical question: what
if you wanted to change almost every base pair in a genome — not copy it, but redesign it for
functions it never had? The rest of the bacterial half of the lecture is organized around that
question.

## The design-build-test-analyze cycle

The work described runs through an iterated loop — design a change, build it, test it, analyze
the result, feed what was learned back into the next design — and the lecturer names the
integrated software platform tying this together "Millstone." The earlier parts of the course
supply the analysis tools that sit inside this loop: the class had already met Bowtie (read
alignment), SnpEff (variant annotation), and JBrowse together with SQL for querying results, and
the lecturer takes these as given rather than re-teaching them.

<figure>
<svg viewBox="0 0 320 320" role="img" aria-label="the design, build, test, analyze cycle of genome engineering">
  <defs>
    <marker id="arrow22" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="160" cy="40" r="34" fill="none" stroke="currentColor"/>
  <text x="160" y="44" text-anchor="middle" font-size="13" fill="currentColor">Design</text>
  <circle cx="280" cy="160" r="34" fill="none" stroke="currentColor"/>
  <text x="280" y="164" text-anchor="middle" font-size="13" fill="currentColor">Build</text>
  <circle cx="160" cy="280" r="34" fill="none" stroke="currentColor"/>
  <text x="160" y="284" text-anchor="middle" font-size="13" fill="currentColor">Test</text>
  <circle cx="40" cy="160" r="34" fill="none" stroke="currentColor"/>
  <text x="40" y="164" text-anchor="middle" font-size="12" fill="currentColor">Analyze</text>
  <line x1="188" y1="55" x2="252" y2="140" stroke="currentColor" marker-end="url(#arrow22)"/>
  <line x1="268" y1="192" x2="188" y2="264" stroke="currentColor" marker-end="url(#arrow22)"/>
  <line x1="132" y1="264" x2="68" y2="192" stroke="currentColor" marker-end="url(#arrow22)"/>
  <line x1="52" y1="140" x2="132" y2="56" stroke="currentColor" marker-end="url(#arrow22)"/>
</svg>
<figcaption>The design-build-test-analyze loop the lecture describes as "Millstone": a genomic
hypothesis is designed, built (often as a large combinatorial set rather than one construct),
tested, and analyzed, feeding back into the next design.</figcaption>
</figure>

A point flagged as distinctive to biological engineering: a combinatorial set of designs can be
built and tested in parallel, the way you cannot build a trillion different 787s to see which
flies best. This is possible partly because next-generation sequencing has a counterpart in
next-generation DNA *synthesis*, with several synthesis chemistries and matching error-correction
strategies that the lecture mentions without detailing, since it is not the focus of this course.

## Four reasons to redesign a genome radically

The lecture gives four reasons someone might want a genome changed almost everywhere rather than
at one site:

1. **Genetic and metabolic isolation**, for safety or public-relations reasons or both — an
   organism that cannot survive or exchange genetic material outside a controlled setting.
2. **New chemistry.**
3. **New protein chemistry**, built from new amino acids beyond the canonical twenty.
4. **Multi-virus resistance** — resistance to viruses past and present, including ones never
   characterized. The lecturer calls this the most powerful of the four.

A genome changed enough starts to break in ways a computational model did not predict, so the
lecture's structure is organized around derisking each change before building on it.

## Building at scale: synthesis and its error rates

Oligonucleotides built on DNA synthesis chips can run up to about 300 nucleotides, and errors
accumulate more heavily toward the end of a longer oligo: the raw error rate rises from about 1 in
1,300 for shorter oligos to about 1 in 250 for longer ones. An enzymatic error-correction system
named ErASE brings this to about 1 in 6,000 without sequencing; sequencing-verified clones push it
lower still. The general point is about background error: synthesis, like sequencing, has a floor
that a design has to be derisked against.

A separate advance combines synthesis and sequencing closely, illustrated with a published study
(Sri Kosuri and Dan Goodman) on synthetic cis-regulatory elements. Each construct — combinations of
promoter elements, ribosome binding sites, and coding-region mutations expected to affect
transcription or translation — is built with its own DNA barcode and synthesized into a genome or
plasmid, then read out two ways. The RNA readout counts barcode occurrences in RNA sequencing,
giving the transcript level of each of the tens of thousands of constructs made in parallel. The
protein readout uses two fluorescent proteins: a red control with a tight expression distribution,
and a green reporter — subject to the engineered variants — with a wide one. Cells are sorted on a
fluorescence-activated sorter, and the result, in the lecturer's words, is a plot where every pixel
is a separate experiment.

## A discovery from the library: codon position matters

It was already known that codon usage correlates with, and can causally affect, protein
expression: common codons, which tend to pair with abundant transfer RNAs, are associated with
higher expression. The new result from this screen was that the relationship flips near the start
of a gene, close to the cis-regulatory elements: there, rare codons are associated with *higher*
expression, with a negative correlation (an $r^2$ of 0.73) between codon commonness and expression
in that region — the opposite of the genome-wide trend. This was separated from confounds such as
AT-richness and the AG-richness of ribosome binding sites, and was published in *Science*: rare
codons near the beginning of a gene help expression, where the same codons hurt it later on.

## Recoding the genetic code

The lecture's working definition of a "radically different" genome is one where somewhere between
seven and thirteen codons have been freed up genome-wide, using the redundancy of the genetic code
(one to six codons per amino acid, three stop codons) to remove every instance of a chosen codon
and replace it with a synonym, so that codon becomes available for reassignment.

The first codon freed genome-wide was the amber stop codon UAG, converted everywhere to UAA. This
was derisked by confirming the resulting genome still grows well under a range of conditions and
remains genetically engineerable.

The next targets were the arginine codons AGA and AGG — the rarest codons in the genetic code, and
complicated because they often overlap Shine-Dalgarno sequences, the ribosome binding sites
involved in initiating translation. Because the number of instances was too large to do
genome-wide at this stage, the project focused computationally on essential genes: finding every
essential gene, designing a synonymous-substitution strategy for each occurrence of AGA/AGG in
them, and synthesizing the changes directly into the genome (the lecture names a construction
process, MAIDS, without describing it further).

Some substitutions were selected against — the engineered strain could not be recovered — which
reads as a direct discovery that a "synonymous" substitution was not functionally neutral there:
some other function, perhaps a hidden ribosome binding site, is layered on top of the coding
sequence at that site. The response was to try alternative arginine codons, and in some cases
codons not even synonymous with the original amino acid; eventually every one of roughly a dozen
such difficult sites was made to work. The lecture treats this as a general finding: a recoding
strategy that can be made to work in essential genes is expected to be easier in non-essential
ones.

Scaling further, the project derisked all thirteen (of sixty-four) target codons across 42 of
E. coli's 290 essential genes (roughly 400 instances of the target codons). All but one instance
worked on the first attempt; the remaining one was again solved by trying alternative codons,
including non-synonymous ones. A risk that appears only once many codons are changed at once:
individually harmless substitutions can combine into "synthetic lethals," where a pair of changes
together is lethal though neither is alone. In practice, most of the slower growth observed in
these recoded genomes traced to incidental ("hitchhiker") mutations acquired during construction
rather than to the design itself, except in the small number of cases where a codon change
genuinely did not work.

## Why a recoded genome resists viruses

The mechanism, explained in response to an audience question: a phage infecting a recoded host
still carries its normal complement of codons in its genes, including ones reassigned in the host
(the freed stop codon, the rare arginine codons, and, as described below, codons for serine and
leucine). Every time the host ribosome meets a reassigned codon in a phage transcript, it does
something other than what the phage genome "expects," producing a translational mess in every
phage protein containing such a codon — and a large phage genome may contain dozens to hundreds of
these sites.

For the phage to escape, every one of those codons would have to mutate, independently, to
something the recoded host translates correctly, without any of those changes being lethal to the
phage itself. The escape probability falls off roughly like $p^n$, where $p$ is the chance a given
disrupted codon mutates to a working substitute and $n$ is the number of reassigned codons the
phage would need to fix at once: as $n$ grows, the phage population required to contain even one
correctly-escaped member becomes astronomically large.

Tested against this logic: a host with the stop codon recoded shows roughly a thousandfold
resistance to a highly virulent mutant of phage lambda, and resistance to two of three viruses
tested against the naturally lytic phage T7, from reassigning that single codon. The hypothesis —
not yet fully tested at the time of the lecture — is that reassigning around seven codons would
give resistance to all viruses tested, strong enough that a viral population could not mutate fast
enough to escape. The lecturer distinguishes this from gradual antibiotic resistance, where a
concentration gradient lets a population adapt incrementally: a recoded host offers no such
gradient, since a phage's translational machinery is disrupted the instant it enters the cell,
with no partially-working intermediate to select on.

## Making the organism dependent on a new amino acid

Genetic and metabolic isolation uses a freed codon (the stop codon UAG) to encode an amino acid
that does not occur naturally — an orthogonal transfer RNA and tRNA synthetase pair, taken from a
very distantly related organism (the hyperthermophilic archaeon *Methanococcus jannaschii*), with
the tRNA's anticodon changed to recognize UAG. This works cleanly only for certain synthetases: in
E. coli the serine and leucine synthetases happen to be "blind" to the anticodon, so changing it
does not disrupt their normal function — which is why those amino acids' codons were chosen as
further reassignment targets beyond the stop codon and the arginine codons.

The amino acid used, bipA, resembles tyrosine or phenylalanine but carries two benzene rings
rather than one, making it bulkier than any naturally occurring amino acid. The design goal was to
make essential proteins *addicted* to bipA: substituted at a position in place of a smaller
natural residue, with nearby residues also mutated to accommodate its bulk, so that reverting the
position to any natural amino acid no longer fits. This was done computationally across the
crystal structures of essentially all of E. coli's essential proteins (around 120 structures),
using a version of the protein-design software Rosetta modified for nonstandard amino acids. In
the illustrated case, a buried leucine not at the active site was swapped for bipA; the initial
model showed three steric clashes, resolved by shrinking nearby residues, and the design was then
confirmed by X-ray crystallography against the predicted structure.

To make the test demanding, the strain had to resist not just evolving out of the dependency but
also *escaping by cannibalism* — surviving on free amino acids released by lysing neighboring
cells. Classic biocontainment strains made by deleting standard biosynthetic genes show
substantial survival on such lysates; the bipA-dependent strain showed a much lower escape rate
under the same test, though not zero. This strain requires the stop codon to be free throughout the
genome, since it also allows deletion of the release factor that would otherwise recognize UAG as
a stop signal (lethal to delete if UAG is still in use).

Escape frequency was measured in two backgrounds: mutS-minus, which knocks out a mismatch-repair
protein to accelerate mutation for testing purposes, and the more realistic mutS-plus background,
where escape frequencies as low as $10^{-8}$ were measured. Wanting to push lower still, the
lecturer put the question to the class: an audience suggestion — that the bipA-encoding codon
could revert to encode some other amino acid that lets the enzyme survive adequately without bipA
— was confirmed as the actual failure mode, and a further suggestion to modify multiple essential
genes simultaneously, so no single reversion suffices, was confirmed as the strategy taken. To find
which natural amino acid is most likely to substitute for bipA, all twenty standard amino acids
were forced into the bipA site in turn, and the resulting strains put through a fast, intentional,
twenty-doubling selection (far short of evolutionary timescales) to find survivors. For the
tyrosyl-tRNA synthetase protein, tryptophan — the largest natural amino acid — was the substitute;
for a second protein, adenosine kinase, tryptophan rarely rescued it but some hydrophobic
aliphatic amino acids such as leucine did. Combining the two resistant mutations into a double
mutant brought the escape rate down to what the lecturer calls vanishingly small.

A follow-up question noted that compensating mutations around a bipA substitution were generally
to smaller amino acids, except for one changed to tryptophan. The explanation: the Rosetta-based
search considered many candidate substitutions by computed energy, trying combinations including
both phenylalanine and tryptophan; tryptophan is large and aromatic, and the lecturer's guess is
that it stacks against bipA's aromatic ring, consistent with tryptophan outperforming
phenylalanine empirically at that position.

## From bacteria to humans: tools and the discovery of Cas9

The lecture turns to genome editing tools used in human cells, organized by what recognizes the
target site: Watson-Crick base pairing (DNA-DNA, as in recombination tools such as RecA and Red
Beta; or RNA-DNA, as in CRISPR/Cas9), or protein-DNA recognition (as in zinc-finger nucleases and
TALE nucleases, where amino acid side chains typically recognize DNA through an alpha helix in the
major groove). The lecturer calls Cas9 the "star" of these going forward.

Cas9 is presented as a case study in computational biology's own history. The repetitive sequences
that make up CRISPR loci were found in E. coli in 1987 by Ishino and colleagues, and were, at the
time, classified as junk DNA — not conserved and repetitive, both taken then as hallmarks of
non-functional sequence, and cited by some as an argument against sequencing non-coding DNA at
all, three years before the NIH arm of the Human Genome Project began. It eventually became clear
to specialists that the system was a form of adaptive immunity, analogous to antibodies, distinct
from the fixed (innate) immunity of restriction enzymes — but it did not become a widely used tool
until January 2013, when it was adapted to work in human cells, a large jump from its native
bacterial context. Once that jump was made, it transferred readily to many further organisms — at
least twenty by the time of the lecture, including fungi, plants, and (unpublished at the time) an
elephant.

## Keeping genome editing on target

The most common question raised about this technology is off-target activity. Complementary
approaches, in roughly the order they appeared:

- **Theoretical screening** (from the earliest human experiments, January 2013): compute candidate
  off-target sites elsewhere in the genome differing from the intended target by one or two
  nucleotides, and avoid guides with likely off-targets of this kind.
- **Empirical search**: because a guide RNA is cheap to make (twenty nucleotides, placed into a
  standard vector), a shortlist of candidates can be tested directly to find sites reliably cut at
  the intended location and not at flagged off-targets.
- **Paired nickases**: Cas9 engineered to nick one DNA strand rather than cut both. Requiring two
  nickases at two nearby, specifically-oriented sites — like needing two PCR primers close
  together — makes an unwanted double-strand break roughly as likely as the product of the two
  single-site off-target probabilities, of order $p^2$ rather than $p$.
- **Truncated guide RNA**: shortening the guide below its natural length (by about two nucleotides,
  in the case described) improves specificity — too long tolerates mismatches, too short lacks
  enough information to specify a unique site, so there is an optimum in between.
- **Nuclease-dead Cas9 fused to FokI** (from Keith Joung's and David Liu's labs, at the time of the
  lecture): remove Cas9's own cutting activity and fuse it to the cutting domain of the bacterial
  restriction enzyme FokI, echoing how zinc-finger and TALE proteins were engineered. Like
  FokI-based zinc-finger/TALE nucleases, and like paired nickases, this needs two bound complexes
  to come together before cutting occurs.

## Establishing causality in human disease

Two further ways of establishing causality close the lecture, both aimed at phenotypes where
cohorts may be extremely small. The first is a double-null example: a highly conserved gene
(myostatin) found with both copies missing in a human case so rare that, at one point, only a
single characterized individual existed, with a striking phenotype of unusually heavy musculature
from birth. A prior hypothesis from the known biology of the pathway, matching the observed
phenotype, was tested not in one but in several animal species already available or straightforward
to make — cows, dogs, and mice — each showing a consistent phenotype.

The second route applies where no animal model exists, including structures (the lecture gives
human brain structure as the example) with no counterpart in other species, leaving nothing to
mutate. There, the lecture turns to organoids or organs on chips grown from human cells —
acknowledged as imperfect, the way animal models carry their own artifacts, but still informative.
The illustrated case, done with two other labs (Keith Parker's and Bill Pu's) and nearing
publication at the time of the lecture, concerns a cardiomyopathy hypothesized to be caused by a
single deleted base affecting mitochondrial function. Using CRISPR-mediated homology-directed
repair, three isogenic cell lines were built from the same starting stem cell line: one left
unedited, one carrying the patient's exact single-base deletion, and one carrying an unrelated
small insertion/deletion at the same site as a disruption control. The stem cells were derived,
through the Personal Genome Project, from the lecturer's own fibroblasts, and differentiated into
the striated, ribbon-like tissue characteristic of cardiac muscle. The lines carrying either the
patient mutation or the control disruption both produced disorganized muscle morphology, assessed
alongside lipid biochemistry and the tissue's contractility (systole and diastole); introducing a
corrective messenger RNA to compensate for the mutation restored normal morphology.

## Delivery and the state of human gene therapy

An audience question identifies delivery, not the editing technology, as the practical bottleneck,
and the lecturer agrees, separating it into two semi-solved sub-problems: getting the editing
machinery to the right tissue, and to the right base pair once there. An example of the first, done
ex vivo: T cells can be removed from a patient, treated with a zinc-finger nuclease to disrupt both
copies of CCR5 (the co-receptor HIV uses to enter cells), and reinfused, producing a population of
HIV-resistant T cells in patients who already had full-blown AIDS. In vivo delivery to the liver is
described as comparatively easy, achievable with non-viral vectors or with a viral vector described
as popular for reaching nearly every cell type in the body — named in the lecture but inaudible in
the recording.

The lecture situates this against the earlier history of gene therapy: roughly a decade or more
before the lecture, overambitious early trials using random viral (lentiviral/retroviral)
integration of extra gene copies caused cancer in a small number of patients, because the
integrated viral promoter could land near, and activate, an oncogene such as LMO2. The contrast is
with the precise, non-random base-pair editing described in this lecture, which does not carry that
risk. At the time of the lecture, roughly 2,000 gene therapy trials were underway across phases one
through three, with one treatment having reached full approval in Europe — a detail the lecturer
notes as ironic, given the same region's general resistance to genetically modified food.

## New chemistry from nonstandard amino acids

Closing questions return to what a nonstandard amino acid in a protein's active site can do
chemically. Prior to the low-escape, competition-free strain described above, nonstandard amino
acids had already been incorporated at lower efficiency and still produced functional enzyme — a
low incorporation efficiency still yields enough correctly-made protein to work with. One
literature example: a redox-active coumarin derivative of an amino acid was placed into the active
site of a well-studied enzyme whose activity could not be improved beyond its natural optimum by
protein design or random mutagenesis using the natural twenty amino acids; adding the
coumarin-derivative amino acid produced roughly a tenfold improvement in the catalytic rate
constant. A second, non-catalytic example is attaching polyethylene glycol at a precisely chosen
site via a nonstandard amino acid, rather than at a random site, which substantially extends the
serum half-life of protein therapeutics such as human growth hormone, which otherwise clears
quickly from serum.

## Sources

- MIT 7.91J (Spring 2014), Lecture 22: guest lecture transcript,
  `computational-biology/mit-ocw/7091j/recordings/lectures/22.md` (timestamps throughout,
  00:00–51:22). There was no slide deck for this lecture; every figure, bar chart, and table the
  speaker gestures at ("here's a bar chart," "there's a genetic code up there in circular form,"
  the color-coded table of genome-editing tools) is referred to in the transcript but not
  reproduced here, because its contents cannot be recovered from the audio.
- Specific items the lecture refers to without describing, named here as pointers rather than
  content: the published cis-regulatory element study (Kosuri and Goodman); the published codon
  position/expression study (described as appearing in *Science*); the synthesis platform named
  "Millstone"; the construction process named "MAIDS"; the nonstandard-amino-acid incorporation
  system originating from Peter Schultz's lab and others; and the in vivo liver delivery vector
  named at 45:35, which is inaudible in the transcript.
- The computational tools Bowtie, SnpEff, JBrowse, and SQL are named at 03:29 as already covered
  earlier in the course and are not re-explained in this lecture.

---

[← 21. Synthetic Biology: Building Genetic Circuits](21-synthetic-biology-building-genetic-circuits.md) · [Contents](index.md) · [23. Recitation Worked Examples →](23-recitation-worked-examples.md)
