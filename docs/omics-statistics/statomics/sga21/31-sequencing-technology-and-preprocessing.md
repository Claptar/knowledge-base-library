---
title: "31. Sequencing Technology and Preprocessing"
course: "StatOmics Sga21"
chapter: 31
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 31. Sequencing Technology and Preprocessing

## What this covers

This chapter follows an mRNA molecule from a tube of cells to a number in a table. It answers two
questions: what does a sequencing machine actually produce, and how does that raw output get turned
into the gene-by-sample count matrix that the rest of the course treats as its starting point. It
assumes you know what genes, transcripts and mRNA are, and — since it follows directly on the
course's proteomics unit — that measuring the concentration of a biological molecule is already
known to be hard.

## Why sequencing, and why now

The first part of the course studied proteomics: the concentration of proteins in a sample. The
second part studies gene expression, i.e. the concentration of mRNA molecules — molecules that may
go on to be translated into protein, or may have functions of their own. Measuring mRNA
concentration is done almost entirely by sequencing.

The technology has been moving fast enough that it changes the kind of course this can be: the data
output of "next generation" sequencing machines has more than doubled every year, while the cost per
gigabase has dropped every year. Each year buys more information for less money, which is also why
the statistical and computational problems keep changing. The large majority of gene-expression
sequencing is done by sequencing-by-synthesis on Illumina machines. Other platforms — Pacific
Biosciences, Oxford Nanopore — have entered the field and are typically most useful for sequencing
long molecules, which matters more for DNA sequencing than for the short-read gene expression
studies this course focuses on.

## From sample to sequencing library

Turning a biological sample into something a sequencer can read is a fixed sequence of steps, and
each one leaves a mark on the data that later analysis has to account for.

1. **Sample collection.** Frozen tissue, FFPE-preserved samples and other input types are all
   amenable to sequencing, thanks to mature protocols.
2. **Capture of (m)RNA.** Cells are lysed to release RNA, which is then captured either by
   poly-A capture (selecting polyadenylated RNA) or by ribosomal depletion (removing ribosomal and
   transfer RNA, which also keeps non-poly-A mRNA such as microRNAs). In targeted sequencing, a
   specific panel of genes is captured at this step instead.
3. **Fragmentation.** Captured molecules are broken up, chemically or mechanically, into fragments
   whose size (often 300–500 bp) is chosen to suit the sequencing machine.
4. **Reverse transcription.** Current sequencing machines only read double-stranded DNA, so
   single-stranded mRNA is first reverse-transcribed into complementary DNA (cDNA).
5. **Adapter ligation.** Adapters — short, platform-specific oligonucleotide sequences — are
   attached to the 3' or 5' ends of the cDNA (or used as primers during reverse transcription), so
   the machine can recognise each fragment. The resulting library is cDNA inserts flanked by
   adapters on both ends.
6. **PCR amplification.** Several PCR cycles raise the concentration of the library to a usable
   level.
7. **Sequencing.** The amplified cDNA library is loaded onto the machine, which reads it by
   sequencing-by-synthesis.

Two choices made during library preparation matter throughout the rest of the course:

- **Single-end vs paired-end.** Single-end sequencing reads one end (3' or 5') of each cDNA
  fragment; paired-end sequencing reads both ends, and depending on fragment size the two reads may
  or may not overlap.
- **Strand-specific protocols.** Some protocols preserve which strand (sense or antisense) each
  read came from.

## What comes out of the machine

The output for each sample is a FASTA or FASTQ file, several gigabases in size, containing millions
of **reads** — for paired-end sequencing, two files per sample, one per end. A FASTA file stores
only the called sequence; a FASTQ file also stores a **quality score** for every called base,
useful in downstream steps such as mapping or variant calling. Each read occupies four lines of a
FASTQ file: a sequence identifier starting with `@`, the sequence itself, a second identifier line
starting with `+`, and the quality scores. The quality scores are stored as ASCII characters for
compactness; converted to integers, they are **Phred scores**, related logarithmically to the
probability that the base call is wrong.

Many published studies deposit their raw FASTQ files on the Gene Expression Omnibus (GEO). Working
in transcriptomics means, sooner or later, retrieving files from there — by hand, through an R
package such as GEOfastq, or with a command-line tool such as `kingfisher`.

## Quality control

Before doing anything else with the reads, a QC check looks for aberrant samples — for instance,
degraded mRNA — that would otherwise contaminate every later step. FastQC is the standard tool for
a single bulk RNA-seq sample; when many samples are sequenced, MultiQC aggregates their FastQC
reports into one overview.

## Mapping: assigning reads to genes

A read on its own is just a short sequence; it becomes useful once it is attributed to the genomic
feature — gene, exon, transcript — that plausibly produced it through gene expression. This
attribution is **mapping**, and it is what turns reads into a proxy for expression: the more reads
that map to a gene, the more highly that gene is taken to be expressed.

Mapping is harder than it sounds, because a read cannot always be assigned to a single feature
unambiguously — some reads are compatible with more than one gene and are called **multi-mapping**.
A note on words: this chapter (and the field) uses "read" and "fragment" for the same datum,
whether that is a single read (single-end) or a read pair (paired-end); "fragment" is the less
ambiguous of the two.

### Reference genome or reference transcriptome

Mapping needs something to map *against*. The traditional choice is a **reference genome** — a
representative example of the species' genome, updated and re-released periodically, downloadable
from providers such as Ensembl or Gencode — together with a GFF/GTF annotation file giving the
coordinates of known features. (A *de novo* reference, built from the reads themselves rather than
downloaded, is also possible, but is not the focus here.)

More recently, mapping is done increasingly against a **reference transcriptome**: a file of the
sequences of all known isoforms, used by tools such as kallisto and Salmon. Because the set of
spliced transcripts is much smaller than the whole genome, this is faster and lighter on memory.
It has a cost, though: mapping against a transcriptome can introduce spurious expression for genes
that are not actually expressed, because **intronic reads** can share enough sequence with a
transcript to map to it. Newer tools such as alevin-fry avoid this by expanding the reference to
include intronic sequence as well.

### Alignment-based workflows

The traditional approach finds the exact coordinates a read maps to on the reference. Because of
alternative splicing, a read does not necessarily map contiguously to the genome — it can overlap a
splice junction, where an intron has been excised, and the two halves of the read then sit
thousands of base pairs apart on the genome even though they were adjacent on the mRNA. Mapping
against a transcriptome avoids this, since transcript sequences are already spliced and reads
should align contiguously; its own difficulty is the redundant sequence shared between related
transcripts, which drives up the multi-mapping rate. Spliced alignment against a genome is
therefore the computationally harder of the two problems.

<figure>
<svg viewBox="0 0 380 210" role="img" aria-label="A read spanning a splice junction maps as two widely separated blocks on the genome but as one contiguous block on a spliced reference transcript">
  <text x="190" y="14" text-anchor="middle" font-size="11" fill="currentColor">same read: two aligned blocks</text>
  <rect x="105" y="20" width="20" height="10" fill="none" stroke="currentColor"/>
  <rect x="250" y="20" width="20" height="10" fill="none" stroke="currentColor"/>
  <line x1="125" y1="25" x2="250" y2="25" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>

  <text x="8" y="50" font-size="12" fill="currentColor">On the genome</text>
  <rect x="40" y="58" width="90" height="18" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="85" y="71" text-anchor="middle" font-size="11" fill="currentColor">exon 1</text>
  <line x1="130" y1="67" x2="250" y2="67" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="190" y="87" text-anchor="middle" font-size="11" fill="currentColor">intron, thousands of bp</text>
  <rect x="250" y="58" width="90" height="18" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="295" y="71" text-anchor="middle" font-size="11" fill="currentColor">exon 2</text>

  <text x="8" y="140" font-size="12" fill="currentColor">On the spliced transcript</text>
  <rect x="40" y="148" width="90" height="18" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="85" y="161" text-anchor="middle" font-size="11" fill="currentColor">exon 1</text>
  <rect x="130" y="148" width="90" height="18" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="175" y="161" text-anchor="middle" font-size="11" fill="currentColor">exon 2</text>
  <rect x="100" y="126" width="60" height="10" fill="none" stroke="currentColor"/>
  <text x="190" y="190" text-anchor="middle" font-size="11" fill="currentColor">same read, one contiguous alignment</text>
</svg>
<figcaption>The same read, split by a splice junction. Against the genome it lands as two blocks
separated by an intron that can be thousands of base pairs long; against the already-spliced
transcript it lands as a single contiguous block. This is why spliced genome alignment carries the
extra computational burden that transcriptome alignment avoids.</figcaption>
</figure>

### Alignment-free ("lightweight") workflows

Modern methods sidestep finding a read's exact coordinates altogether. Instead they posit a
probabilistic model in which transcript abundance is expressed in terms of the transcript's
constituent **$k$-mers** — short subsequences of length $k$. The set of possible $k$-mers and which
transcripts contain them can be precomputed once from the reference transcriptome and indexed, so
the expensive work happens only once. For each fragment, the set of transcripts whose $k$-mers are
compatible with it is looked up in this index; that set is the fragment's **$k$-compatibility
class** (also called its equivalence class, or transcript compatibility class).

## From mappings to abundances

Once reads are mapped, there are two broad ways to turn the mappings into a number per feature.

**Counting.** In alignment-based workflows, one can simply count the fragments that map to each
gene. This was the dominant approach for RNA-seq's first decade, typically built on genome
alignments. It hides several heuristic choices: does a fragment count as soon as it intersects the
gene's coordinates, or only if it maps fully within them? Are intronic reads counted? Are
multi-mapping reads counted, and if so, how?

**Estimation.** More recent methods replace counting with a statistical model that estimates
expression, typically at the transcript level. This fits naturally with alignment-free workflows,
because the number of fragments in each equivalence class is a *sufficient statistic* for the
estimation — it contains everything the model needs to estimate feature-level abundances, whether
or not any individual read was mapped to an exact location. The estimation itself is usually done
with the EM algorithm (Dempster *et al.*, 1977), though Salmon and similar tools also use other
approaches. Its main advantage is that fragments are assigned to transcripts *probabilistically*,
which handles multi-mapping automatically: the total count for a transcript is just the sum, over
all fragments, of the probability that each fragment belongs to it. Because of this, "estimated
counts" need not be integers.

## Correcting for technical biases: CPM and TPM

Feature-level counts (from either counting or estimation) are only one possible proxy for
expression, and a biased one: two technical factors change the observed count even when the true
mRNA concentration does not.

- **Sequencing depth.** For a gene at the same concentration in two samples, sequencing one sample
  more deeply will, on average, produce a higher count.
- **Transcript length.** For two transcripts at the same concentration but different lengths, the
  longer one tends to produce more fragments, because it can be broken into more fragments of the
  usable size during the fragmentation step.

Write $Y_{fi}$ for the expression count of feature $f$ in sample $i$ (a simple fragment sum or an
estimated count), and $N_i = \sum_f Y_{fi}$ for the sequencing depth ("library size") of sample $i$.

**Counts per million (CPM)** corrects for depth: it is the count you would expect if the sample had
been sequenced to a depth of exactly one million.

$$
CPM_{fi} = \frac{Y_{fi}}{N_i}\, 10^6
$$

**Transcripts per million (TPM)** corrects for depth *and* length, and is closer to a concentration
or proportion. Length is expressed as an *effective length*, $l_{fi}^{(eff)}$: the number of
possible start sites for fragments of the typical size actually observed in the data,

$$
l_{fi}^{(eff)} = l_f - \hat{\bar F}_i + 1,
$$

where $l_f$ is the feature's length in nucleotides and $\hat{\bar F}_i$ is the estimated mean
fragment length in sample $i$. TPM is then

$$
TPM_{fi} = \frac{Y_{fi}}{l_{fi}^{(eff)}} \left( \frac{1}{\sum_f \frac{Y_{fi}}{l_{fi}^{(eff)}}} \right) 10^6.
$$

Read this in two pieces. $Y_{fi}/l_{fi}^{(eff)}$ is the count normalised for the feature's length
alone; it is still affected by sequencing depth, so dividing by $\sum_f Y_{fi}/l_{fi}^{(eff)}$
removes that too. TPM therefore normalises for both feature length and sequencing depth, while CPM
normalises for depth only. Most of the statistical methods later in the course work directly with
(estimated) counts rather than with CPM or TPM.

## The count matrix

Once abundances are quantified, they are stored in a matrix with features (typically genes) as rows
and samples as columns. This count matrix is the object almost every later lecture in the course
starts from.

## Sources

- Both note files are conversions of a single source: `sequencing_intro.Rmd` from the statOmics
  SGA21 course (CC BY-NC-SA 4.0), split into two pages.
  - `docs/omics-statistics/statomics/sga21/sequencing_intro/01-sequencing-technology.md` — the
    motivation for sequencing gene expression, the library-preparation workflow, and the FASTA/FASTQ
    output format.
  - `docs/omics-statistics/statomics/sga21/sequencing_intro/02-preprocessing-of-raw-sequencing-data.md`
    — quality control, mapping (reference genome/transcriptome, alignment-based and alignment-free
    workflows), abundance quantification (counting vs. EM-based estimation), CPM/TPM, and the count
    matrix.
- No slide deck or lecture transcript was supplied for this material; the two files above are the
  entire input.
- The source material itself points to, but does not reproduce, several external resources that a
  reader may want to follow up: a video walkthrough of Illumina sequencing-by-synthesis; the FastQC
  and MultiQC tools and their example good/bad-quality reports; GEOfastq and `kingfisher` for
  downloading FASTQ files from GEO; the kallisto and Salmon papers; a bioRxiv note on spurious
  expression from intronic reads under transcriptome mapping, and the alevin-fry preprint that
  addresses it; Dempster, Laird & Rubin (1977) on the EM algorithm; Ensembl and Gencode as reference
  genome/annotation providers; and the course's own `sequencing_preprocessing.sh` tutorial script.

---

[← 30. Bulk RNA-seq DE Homework](30-bulk-rna-seq-de-homework.md) · [Contents](index.md) · [32. Negative Binomial Model →](32-negative-binomial-model.md)
