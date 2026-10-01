---
title: "1. Introduction to Computational Biology"
course: "MIT 7.091J"
chapter: 1
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 1. Introduction to Computational Biology

## What this covers

This chapter answers two questions an orientation lecture is supposed to answer: what kind of
field is computational biology, and what does studying it, in this course, consist of. It assumes
only general undergraduate biology — genes, proteins, chromosomes — and no prior exposure to
sequence analysis, probability, or algorithms; the course builds all three from here. Nothing
technical is introduced yet: the content proper (alignment, BLAST statistics, assembly, and so on)
starts in the lectures this chapter previews, and is covered in the chapters that follow it.

## Where computational biology sits

Computational biology is a part of biology, not a branch of computer science applied to biology
from outside. In the way that genetics or biochemistry are disciplines with their own strategies
for answering biological questions, so is computational biology — it is a strategy for
understanding gene regulation and much else, built on quantitative and computational tools rather
than on, say, biochemical assays alone.

A few neighbouring terms get used loosely, and it is worth placing them rather than pretending they
are interchangeable:

- **Bioinformatics** is sometimes distinguished from computational biology by emphasis: bioinformatics
  as *building* tools, computational biology as *using* them. The line is blurry in practice and
  most people do not police it.
- **Informatics** is the broader field of managing and analysing data in general, and bioinformatics
  sits inside it. Many of the core algorithms used in bioinformatics — substitution matrices,
  dynamic programming, hidden Markov models — were developed in computer science, statistics, and
  other branches of engineering before being brought to sequence data.
- **Synthetic biology** cuts across the others differently: it is fundamentally an *engineering*
  discipline, designing and building synthetic molecular and cellular systems, though the same
  modelling tools can also be turned around to understand natural systems.
- **Systems biology** is a related but separate course of study (several more specialised systems
  biology classes exist); this course covers some of the same ground — the tools needed to analyse
  complex systems — without being a systems biology course itself.

This course is also, deliberately, not an algorithms course: bioinformatics algorithms are
discussed and one gets implemented on a homework, but analysing or designing algorithms in general
is not the centre of what is taught.

## A history, decade by decade

The field did not arrive all at once; each decade's technology opened a different set of questions.
This is not a scholarly history — it is one researcher's anecdotal sketch of what was happening,
mentioned to set the stage for the rest of the course rather than as examinable content in its own
right. A proper scholarly treatment, referenced in the lecture, is Hallam Stevens's history of
bioinformatics.

**The 1970s.** No genome sequences and no large sequence databases existed yet, though protein
sequences were beginning to accumulate. Early computational biologists therefore focused on
comparing *protein* sequences — their function, structure, and evolution. Comparing proteins
properly requires an amino acid substitution matrix: a matrix describing how often one amino acid
is substituted for another over evolutionary time. Margaret Dayhoff pioneered this, and her PAM
series of matrices is still in use. On the evolutionary side, Russ Doolittle and Carl Woese analysed
ribosomal RNA sequences. Woese's analysis overturned the assumed prokaryote–eukaryote split: a
subgroup of single-celled, anuclear organisms turned out to be closer to eukaryotes than to the rest
of the prokaryotes, and he named it the Archaea — a whole kingdom of life recognised by sequence
analysis alone. Doolittle's sequence comparisons fed the molecular clock idea: building systematics
on molecular sequence rather than on phenotypic characteristics.

**The 1980s.** Sequence databases expanded, and alignment and search became central problems in
their own right. Fast algorithms for comparing and aligning protein and DNA sequences were
developed: FASTA was widely used, and BLAST followed (Lipman, Pearson, Webb Miller, and Altschul
among its authors). The statistics needed to judge when a BLAST hit is significant were worked out
by Karlin and Altschul. Gapped alignment also progressed, notably with Smith–Waterman, and RNA
secondary structure prediction progressed with Nusinov and Zuker. Literature databases such as
PubMed also date from this period.

**The 1990s.** Computational biology expanded further, driven by microarrays, the first genome
sequences, and new questions — how to identify domains within a protein, how to identify genes in
a genome. The hidden Markov model, borrowed from electrical engineering, turned out to be well
suited to these sequence-labelling problems; Anders Krogh and David Haussler pioneered its use here.
The first genomes of free-living organisms were sequenced in the mid-1990s, opening comparative
genomics. And David Baker's Rosetta algorithm made notable early progress on predicting protein
structure from primary sequence — a biophysics problem that is nonetheless squarely part of
computational biology.

**The 2000s.** Genome sequencing became fashionable at larger scale, including the human genome,
which introduced a host of computational challenges: assembling a genome from its reads, and then
annotating it. Jim Kent did the first widely used human genome assembly and helped found UCSC's
genome browser; Ewan Birney started Ensembl and still runs it. At the same time, molecular biology
became more *high-throughput* than its traditional focus on one gene or protein at a time:
microarrays made it possible, in principle, to measure the expression of every gene, and to profile
every transcript or protein in a cell. That data was used to study transcription, splicing,
microRNAs, translation, and epigenetics, and bioimage informatics — particularly for developmental
biology — became a popular new area. Systems biology, as a named field, was born around this time
too: Eric Davidson's gene regulatory network models of sea urchin development are a prominent
early example, alongside models of the networks controlling cell proliferation and apoptosis.
Synthetic biology was born alongside it, with the first completely artificial gene networks
designed to make a cell behave in a chosen way. The repressilator is the example given: three
transcription factors, each repressing the next in a cycle, with one of them also repressing GFP.
Put into bacteria, the circuit — described by a small system of differential equations — causes
sustained oscillations in GFP expression.

**The late 2000s and 2010s.** Second-generation ("next-gen") sequencing began transforming a wide
range of applications: genome sequencing that once required a genome centre could now be done in
an individual lab; transcriptome sequencing became routine; and new assays mapped protein–DNA
interactions genome-wide — both sequence-specific transcription factors and more general factors
such as histones — protein–RNA interactions (CLIP-seq), translated messages, methylated sites, and
open chromatin. Barbara Wold is credited as a pioneer of both RNA-seq and ChIP-seq. The Metzger
review was recommended as a well-written overview of the sequencing technologies themselves
(Illumina, 454, PacBio, and others) ahead of the next lecture.

## The questions that motivate the field

Two clusters of motivating questions recur throughout the course, and it is worth having them in
mind before the machinery for answering them arrives.

**Questions about the genome itself.** What instructions are actually encoded in a genome — think
of it as a book, but written in an unfamiliar language whose rules (the regulatory code) still need
decoding. How are chromosomes organised? What genes are present, and how can they be found
computationally (gene annotation)? What regulatory circuitry is encoded — can a feedback circuit
responding to a stimulus such as light or nutrient deprivation eventually be read directly off
sequence? Can the transcriptome be predicted from the genome? The genetic code already lets the
proteome be read off the transcriptome, codon by codon; the open dream is to predict the other
steps of gene expression — where a polymerase starts and stops transcribing, how a transcript is
spliced — with that same precision. Can protein function be predicted from sequence? Can
evolutionary history be reconstructed from sequence — a long-standing goal, and one on which enough
progress has been made that most evolutionary classification, and the definition of new species, is
now done at the sequence level.

**Questions about systems and disease.** Given a newly discovered organism that causes a disease,
what should be measured to find the cause, understand the mechanism of existing drugs, or map a
metabolic pathway — its genome, its transcriptome, proteomics, a time-course of some perturbation?
What is the most efficient way to gather that information, and how should it be integrated into an
understanding of the organism's physiology, well enough to suggest a drug target? What modelling
would let that same data be used to design new therapies, or — in a synthetic biology setting — to
re-engineer an organism for a new purpose, such as a microbe that produces fuel? What can current
high-throughput methods actually measure, what does each data type mean on its own, and what are
its particular strengths and weaknesses? Finally, how should all the data collected on one system be
integrated to understand how that system functions as a whole? This last question is what motivates
the later material on regulatory networks.

## The shape of this course

The course is organised into six topics, each opening with its own motivating question and its own
discussion of the experimental method that produces the data being analysed — the computation is
always tied to a specific wet-lab technique, not taught in the abstract.

**Genomic Analysis I** covers the classical core of sequence analysis: local alignment and BLAST,
global alignment with gaps (Needleman–Wunsch, Smith–Waterman), and the use of cross-genome sequence
similarity to locate regulatory elements such as microRNA target sites. BLAST is described in the
lecture as something like the Google search engine of bioinformatics — one of the most widely used
tools in the field — and understanding how to judge the significance of a BLAST hit, via an extreme
value distribution, is treated as essential rather than incidental.

**Genomic Analysis II** covers what is needed once sequencing produces hundreds of millions of
reads per experiment: an index built with the Burrows–Wheeler transform to map reads back to a
reference genome quickly, even in repetitive regions; assembly, where a reference genome itself is
reconstructed from sheared, size-selected, sequenced fragments — reads assembled into contigs and
then into scaffolds, like a jigsaw puzzle whose ambiguities come mostly from repeats; ChIP-seq, which
locates where a regulatory protein binds across the genome (the example shown is Oct4 binding near
the Sox2 gene); and RNA-seq, which reads off both expression level and splice isoform by looking at
how reads align across exons and across splice junctions.

**Modeling biological function** returns to sequence analysis at a different level: motif finding —
searching a set of sequences for a shared subsequence with some biological function, such as a
protein binding site, using algorithms such as Gibbs sampling; Markov and hidden Markov models,
described as "the Legos of bioinformatics" for the range of sequence-labelling problems they solve;
and RNA secondary structure prediction, from thermodynamic tools (the mfold tool) and from
comparative genomic approaches, recovering the alternative folds a given RNA can adopt.

**Proteomics and protein structure** moves from nucleic acids to proteins: structure comparison and
classification; predicting a protein's three-dimensional structure from its sequence, a problem that
has gone from computationally intractable to, for small proteins, strikingly accurate — approached
both by special-purpose hardware (the Anton machine) and, at the opposite extreme, by crowdsourcing
the problem to video-game players (FoldIt), with both approaches shown succeeding on the same set of
fast-folding proteins; and predicting protein–protein interactions, which is what makes it possible
to move from a single protein's structure to how proteins function as a network.

**Regulatory and interaction networks** is an extended unit covering gene regulatory networks (building
on the kind of network Eric Davidson pioneered), protein interaction networks, genetic interaction
networks, and "computable" network models — models that make a specific, checkable prediction, such
as a Boolean on/off call or a Bayesian probability, rather than only a diagram. A guest lecture from
Ron Weiss on synthetic biology, and another from Doug Lauffenburger, fall within this unit.

**Computational genetics** closes the course by asking how genome variation relates to phenotype:
how to find quantitative trait loci (QTLs) — regions of the genome whose allelic variation predicts
a quantitative trait, illustrated with a yeast cross mapping the sources of growth-rate variation —
and how genome-wide association studies (GWAS) locate human genetic variants associated with
increased disease risk, read off a genome-wide scan as a "Manhattan plot" (so called because the
points of high significance stick up like buildings). A final guest lecture from George Church
closes the semester.

## Exercises

The problems below are Problem set 1, as the course issued it. It was assigned across several of
the lectures that this chapter only previews — most of its content (BLAST, scoring matrices,
gapped alignment, and the statistics of local alignment) belongs to the lectures that come after
this one, not to the orientation lecture itself. It is reproduced here, unsolved, because this is
where it falls in the course's numbering.

### Problem set 1

**Problem 1. Sequence search.** A strain of mice becomes ill unless fed a diet free of
phenylalanine. Sequencing this strain's genome turns up several differences from wild type,
including a change to a region encoding a highly expressed 68-nucleotide RNA. The sequence in the
mutant strain is

$$5'\text{-UGUACAUGAUGAAGUCAUAGCGAACGGAGAAGGGCCGGCUGAGGAAACUGCACGUCACCCUCCUGAAA-}3'$$

and in wild-type mice it is

$$5'\text{-UGUACAUGAUGAAAACAGUCUCCCUCUUCUGAAUCUCGCUGAGGAAACUGCACGUCACCCUCCUGAAA-}3'$$

Search the mutant-strain sequence against the mouse genome and transcriptome using NCBI's BLASTn
(nucleotide blast, "Mouse genomic + transcript" database, optimised for "somewhat similar
sequences", match/mismatch scores set to +1/−3).

(A) How many statistically significant hits are there at an E-value of 0.05? In one sentence, what
does an E-value of 0.05 mean? For the transcript hits, what are the maximum reported scores, are
they raw scores or bit scores, which parts of the query RNA do they correspond to, and what is the
percent match?

(B) Using the E-value and reported score of the highest-percent-identity hit from part (A),
estimate the length of the Mouse (G+T) database searched.

(C) Suppose a query sequence $Q$ of length $L$ matches a database sequence perfectly, giving a
BLAST E-value $E_1$. If only the first half of $Q$ were searched instead, would the E-value stay
the same, increase, or decrease — and roughly how (linearly, exponentially, or some combination)?

(D) For the transcript hits with E-value below 0.05, which genes and RNA classes do they belong to,
and does the query RNA match their sense or antisense strand?

(E) An RNA-protein pulldown from mouse cell lysate followed by mass spectrometry shows that this
RNA interacts with the product of the *ADAR1* gene. What does this enzyme do, and what kind of RNA
does it act on? Using the identity and strand of the gene hit found in part (D), propose a
hypothesis for how this RNA might cause the mouse's metabolic disorder.

**Problem 2. Gapped sequence alignment.**

(A) A scoring matrix could simply assign $+1$ for a match and $-1$ for any mismatch,
$S_{ij} = 1$ if $i = j$ and $S_{ij} = -1$ otherwise. Is this a good choice for comparing protein
sequences? Why or why not, and, in one sentence, how would you obtain a better scoring matrix?

(B) Compare the score for aligning two tryptophans (W-W) to the score for aligning two alanines
(A-A) under the PAM250 matrix. Both are "matches" — why are the scores so different?

(C) Align the peptides ATWES and TCAET globally, using the Needleman–Wunsch algorithm, the
BLOSUM62 scoring matrix, and a linear gap penalty of 2. Fill in the dynamic programming matrix,
circle the traceback path, and write out the final alignment (list every top-scoring alignment if
there is more than one).

(D) Below is the same pair of peptides aligned instead with the PAM250 matrix and the same gap
penalty, traceback already shaded:

| | Gap | A | T | W | E | S |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Gap** | 0 | −2 | −4 | −6 | −8 | −10 |
| **T** | −2 | 1 | 1 | −1 | −3 | −5 |
| **C** | −4 | −1 | −1 | −3 | −5 | −3 |
| **A** | −6 | −2 | 0 | −2 | −3 | −4 |
| **E** | −8 | −4 | −2 | −4 | 2 | 0 |
| **T** | −10 | −6 | −1 | −3 | 0 | 3 |

What alignment does this traceback give? Compare it with the alignment obtained from BLOSUM62 in
part (C): why do the two scoring matrices lead to different alignments?

**Problem 3. Sequence similarity search statistics.** Local nucleotide alignments are run with a
favourite local-alignment tool (e.g. BLAST), using match and mismatch scores of $+1$ and $-1$. A
100 bp query is aligned against a 1 Mbp genome, and a 20-nt subsequence of the query turns out to
match perfectly.

For each of the base-composition scenarios below, calculate the significance of this 20-nt perfect
match, taking $K = 1$ throughout. (Note: the Gumbel distribution used for these scores is
continuous, so $P(S \ge x)$ and $P(S > x)$ coincide for continuous $x$; applied to a scoring scheme
that only takes discrete values, the intended quantity is $P(S \ge 20) = P(S > 19)$, i.e. $19$
substituted into the Gumbel CDF given on the lecture slides, though an answer using $20$ is also
acceptable given the two ways the slides and the textbook phrase the inequality.)

(A) Query and genome both have balanced base composition, $A = C = G = T = 25\%$.

(B) Query and genome are both highly A+T-rich, $A = T = 40\%$, $C = G = 10\%$.

(C) The query is moderately A+T-rich ($A = T = 30\%$, $C = G = 20\%$) but the genome is moderately
C+G-rich ($A = T = 20\%$, $C = G = 30\%$).

## Sources

- Slides: `lectures/01-slides/01-genomic-analysis-module.md`, `02-computational-genetics-module.md`,
  and `03-gwas-analysis-can-identify-human-variants-associated-with-di.md` — these are the
  mid-semester preview figures (BWT indexing, genome assembly into contigs and scaffolds, ChIP-seq
  of Oct4/Sox2, RNA-seq junction reads, chromatin accessibility, the yeast-cross QTL paper
  (Bloom et al., *Nature* 2013), the seven-disease GWAS Manhattan plots (Burton et al., *Nature*
  2007), fast-folding protein structure prediction, protein interaction and regulatory network
  figures, and the course's project/exam comparison table) shown by the three instructors as they
  each previewed their unit.
- Transcript: `recordings/lectures/01.md`, the full lecture. Course framing and distinctions between
  bioinformatics/computational biology/informatics/synthetic biology, 06:27–08:38; the
  decade-by-decade history, 07:33–17:30; the course's six-topic structure and the motivating
  questions, 17:30–24:21; the syllabus walkthrough and per-instructor topic previews, 24:21–1:02:00;
  question-and-answer on course mechanics, 1:02:00–end. Administrative material specific to that
  one offering of the course — grading weights, due dates, recitation times, collaboration policy,
  the textbook and probability/statistics primer recommendations — has been left out of this
  chapter as it does not carry into later lectures.
- Problem set: `psets/01-questions-pset1-ans/01-problem-1-sequence-search-6-points.md`,
  `02-problem-2-gapped-sequence-alignment-6-points.md`, and
  `03-problem-3-sequence-similarity-search-statistics-7-points.md` — Problem Set 1, reproduced here
  unsolved; the posted answers (including the worked E-value and Karlin–Altschul formulas) were used
  only to recover question (C) of Problem 3, whose statement is cut off in the source conversion,
  and are not reproduced.
- Named but not contained in any supplied file: Hallam Stevens's history of bioinformatics (referred
  to for a scholarly treatment); the Metzger review of next-generation sequencing technologies;
  Zvelebil and Baum, *Understanding Bioinformatics* (the course's non-required textbook); and the
  course's probability and statistics primer.

---

[Contents](index.md) · [2. Sequencing Platforms and BLAST Statistics →](02-sequencing-platforms-and-blast-statistics.md)
