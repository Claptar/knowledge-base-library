---
title: "9. Illumina Next-Generation Sequencing Overview"
course: "StatOmics Sga21"
chapter: 9
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 9. Illumina Next-Generation Sequencing Overview

## What this covers

Before any statistical method for read counts, base calls, or variant calls makes sense, a more basic
question has to be settled: what actually happens between a tube of DNA or RNA and the data a downstream
analysis works with? This chapter walks through Illumina's sequencing-by-synthesis chemistry, the
four-step workflow that turns a sample into reads, the main families of experiments the technology
supports — genomics, transcriptomics, epigenomics — and the vocabulary needed to read a methods
section (coverage, insert, cluster, index, and so on). It assumes only familiarity with DNA/RNA
structure, PCR, and the idea of aligning a sequence read to a reference genome; it assumes nothing
about sequencing instruments themselves.

## From capillary electrophoresis to massively parallel sequencing

DNA sequencing before the 2000s was a "first-generation" technology. Sanger's chain-termination
method (1977) made sequencing reliable and reproducible, and a decade later Applied Biosystems built
automated, capillary-electrophoresis (CE) instruments around it — the AB370 (1987) and the AB3730xl
(1998) — which became the workhorses of the NIH-led and Celera-led Human Genome Project. Those
instruments were high throughput for their time, but they still sequenced one fragment at a time.

The break came in 2005, with the Genome Analyzer: instead of sequencing a single fragment, it
sequenced millions of fragments in parallel, and a single run went from roughly 84 kilobases of
output to about 1 gigabase. That short-read, massively parallel approach is what "next-generation
sequencing" (NGS) refers to, and from that point the data output of NGS more than doubled every
year — outpacing Moore's law. By 2014, a single run produced 1.8 terabases, a roughly $1000\times$
increase over 2005.

The same period tells the story in cost. The first human genome, published in 2001, took fifteen
years and cost nearly three billion dollars. By 2014, the HiSeq X Ten system could sequence over 45
human genomes in a single day for approximately \$1000 each. That drop is what people mean by "the
\$1000 genome": it is not just cheaper sequencing, it is what makes population-scale sequencing and
routine clinical genomics possible, because a lab can now run thousands to tens of thousands of
samples in a year rather than one genome over a decade and a half. As Eric Lander (Broad Institute,
and a leader of the Human Genome Project) put it:

> "The rate of progress is stunning. As costs continue to come down, we are entering a period where
> we are going to be able to get the complete catalog of disease genes. This will allow us to look
> at thousands of people and see the differences among them, to discover critical genes that cause
> cancer, autism, heart disease, or schizophrenia."

## The core chemistry: sequencing by synthesis

The chemical idea behind NGS is the same one CE sequencing already used: a DNA polymerase
incorporates fluorescently labelled nucleotides (dNTPs) into a growing strand, and at each
incorporation the identity of the base is read off from the fluorophore. The difference is scale —
NGS runs this cycle across millions of DNA fragments simultaneously rather than one at a time. Over
90% of the world's sequencing data comes from Illumina's sequencing-by-synthesis (SBS) chemistry,
which uses a reversible-terminator nucleotide: all four labelled, terminator-bound bases are present
at once during a cycle, so they compete for incorporation, which is what keeps incorporation bias
and raw error rates low even in repetitive sequence and homopolymer runs. After each base is
incorporated and imaged, the terminator and dye are cleaved so the next cycle can proceed.

That single-base chemistry sits inside a four-stage workflow that is the skeleton of every Illumina
NGS method, whatever the downstream question:

1. **Library preparation** — the sample (DNA or cDNA) is randomly fragmented, and adapters are
   ligated to the $5'$ and $3'$ ends of each fragment. "Tagmentation" is a faster variant that
   fragments and ligates in a single step. Adapter-ligated fragments are then PCR-amplified and
   purified.
2. **Cluster generation** — the library is loaded onto a flow cell, a glass slide whose surface is
   coated with oligos complementary to the adapters. Each library molecule binds the surface, and
   its free end bends over and "bridges" to a neighbouring complementary oligo. Repeated cycles of
   denaturation and extension — bridge amplification — turn each single template molecule into a
   clonal cluster of about a thousand copies, so that its signal is strong enough to detect. A
   cluster is what a single template becomes; it is also what will produce a single sequencing read.
3. **Sequencing** — the reversible-terminator SBS chemistry described above is run simultaneously
   across every cluster on the flow cell.
4. **Data analysis** — reads are aligned to a reference genome, and everything downstream — variant
   calling, read counting, phylogenetic or metagenomic analysis — starts from that alignment.

<figure>
<svg viewBox="0 0 640 170" role="img" aria-label="The four-stage Illumina NGS workflow, from a fragmented sample to aligned data">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <g fill="none" stroke="currentColor" stroke-width="1.5">
    <rect x="10" y="55" width="130" height="60" rx="4" fill="currentColor" fill-opacity="0.15"/>
    <rect x="175" y="55" width="130" height="60" rx="4" fill="currentColor" fill-opacity="0.15"/>
    <rect x="340" y="55" width="130" height="60" rx="4" fill="currentColor" fill-opacity="0.15"/>
    <rect x="500" y="55" width="130" height="60" rx="4" fill="currentColor" fill-opacity="0.15"/>
    <line x1="140" y1="85" x2="172" y2="85" marker-end="url(#arrow)"/>
    <line x1="305" y1="85" x2="337" y2="85" marker-end="url(#arrow)"/>
    <line x1="470" y1="85" x2="497" y2="85" marker-end="url(#arrow)"/>
  </g>
  <text x="75" y="80" text-anchor="middle" font-size="12" fill="currentColor">Library</text>
  <text x="75" y="95" text-anchor="middle" font-size="12" fill="currentColor">preparation</text>
  <text x="240" y="80" text-anchor="middle" font-size="12" fill="currentColor">Cluster</text>
  <text x="240" y="95" text-anchor="middle" font-size="12" fill="currentColor">generation</text>
  <text x="405" y="80" text-anchor="middle" font-size="12" fill="currentColor">Sequencing</text>
  <text x="405" y="95" text-anchor="middle" font-size="12" fill="currentColor">(SBS)</text>
  <text x="565" y="80" text-anchor="middle" font-size="12" fill="currentColor">Data</text>
  <text x="565" y="95" text-anchor="middle" font-size="12" fill="currentColor">analysis</text>
  <text x="75" y="140" text-anchor="middle" font-size="11" fill="currentColor">fragment + adapter</text>
  <text x="240" y="140" text-anchor="middle" font-size="11" fill="currentColor">bridge amplification</text>
  <text x="405" y="140" text-anchor="middle" font-size="11" fill="currentColor">read-out per cycle</text>
  <text x="565" y="140" text-anchor="middle" font-size="11" fill="currentColor">align to reference</text>
</svg>
<figcaption>The workflow shared by every Illumina NGS method: only the library preparation step
changes between whole-genome sequencing, RNA-seq, methylation sequencing, and the rest.</figcaption>
</figure>

## What changed on top of that core chemistry

Several advances sit on top of the basic SBS cycle and explain why NGS displaced CE sequencing
rather than merely competing with it.

**Paired-end sequencing** reads both ends of each library fragment and aligns them as a pair. This
doubles the number of reads for the same library preparation effort, but the more important gain is
information: because the distance between the two ends is roughly known, paired reads align more
accurately across repetitive regions, make indel detection possible (which single-end reads cannot
do), let PCR duplicates be identified from anomalous pair spacing, and increase the number of usable
SNV calls. Some methods, such as small RNA sequencing, are still better served by single-end reads,
but paired-end is now the default for most applications.

**Tunable, digital coverage.** A microarray reports a continuous intensity, bounded below by noise
and above by saturation. NGS instead counts discrete reads, so its dynamic range is set only by how
many reads are collected — and that can be dialled up or down to match the question. Detecting a
somatic mutation present in only a small fraction of cells in a tumour–normal mixture needs very deep
coverage of the region in question, often upwards of $1000\times$; discovering variants across a
population needs the opposite trade-off, spreading reads thinly (lower depth per sample) but across
many samples to gain statistical power. The same chemistry supports both, just by changing how
sequencing effort is allocated.

**Faster, cleaner library preparation.** Early NGS libraries took one to two days to prepare, an
improvement on cloning-based approaches but still a bottleneck; kits such as Nextera XT brought this
under 90 minutes, and PCR-free protocols avoid the amplification bias that otherwise degrades
coverage of GC/AT-rich regions, promoters, and homopolymers.

**Multiplexing.** Because each library fragment can carry a short (8–12 bp) index sequence added
during library preparation, many libraries can be pooled and run in a single flow cell lane, then
computationally sorted ("demultiplexed") afterwards. This is what makes running hundreds of samples
in one instrument run practical. It also introduces a specific failure mode, index misassignment
("index hopping"): a read's index sequence gets attached to the wrong library during pooling or
sequencing, so it is assigned to the wrong sample downstream.

**Scalable instrumentation.** The chemistry is the same across a benchtop instrument producing a few
gigabases for a targeted panel and a production-scale instrument producing terabases across
population-scale studies; what differs is flow cell design and run configuration, so the same
methodology development carries across the range of scale a lab might need.

## Applications I: genomics

**Whole-genome sequencing (WGS)** reads the full genome rather than a fixed panel of markers, which
is what a genotyping microarray does. Its cost has fallen enough that it is now practical not just
for human genomes but for any organism — including, for example, the rapid strain-level sequencing
used to trace the source and virulence of the 2011 European *E. coli* outbreak.

**Exome sequencing (WES)** sequences only the protein-coding exome, under 2% of the genome by size
but the location of most known disease-causing variants, making it a cheaper alternative to WGS for
many disease and population-genetics questions.

**De novo sequencing** applies when there is no reference genome to align to, so reads must instead
be assembled into overlapping contigs from scratch. Assembly quality depends on the diversity of
insert sizes in the library: short-insert paired-end reads, sequenced at high depth, resolve fine
detail, while long-insert mate-pair libraries (2–5 kb gaps between the paired reads), sequenced at
lower depth, span the repetitive regions that short inserts cannot bridge and let structural variants
be detected. Combining both is the standard route to a good assembly.

**Targeted sequencing** captures and sequences only a chosen subset of the genome, which lets the
same sequencing budget buy much higher depth: a typical WGS study covers each base $30$–$50\times$,
while a targeted panel can reach $500$–$1000\times$ or more, which is what makes detecting rare
variants affordable. There are two ways to do this: target enrichment (hybridisation capture of a
region anywhere from 10 kb to 62 Mb) and amplicon sequencing (highly multiplexed PCR of 16 up to
1536 specific targets). Amplicon panels are the standard approach both for finding rare somatic
mutations in a tumour sample diluted by normal DNA, and for surveying the bacterial 16S rRNA gene
across many species at once in metagenomic samples.

## Applications II: transcriptomics

RNA-seq library preparation typically starts from total RNA, removes ribosomal RNA, and converts the
remainder to cDNA before standard NGS library prep; which additional enrichment step is added before
that conversion determines which slice of the transcriptome is captured.

**Total RNA and mRNA sequencing** give a snapshot of the whole transcriptional state of a sample
rather than a fixed, pre-chosen set of genes — the same digital-counting advantage described above
lets rare and common transcripts both be quantified in the same run, and reads spanning splice
junctions support detection of isoforms, novel transcripts, and gene fusions.

**Targeted RNA sequencing** restricts this to a chosen panel of transcripts — useful for measuring
differential expression, allele-specific expression, fusions, or splice junctions within a pathway
of interest, and for validating results from an array or whole-transcriptome experiment more cheaply.

**Small RNA and noncoding RNA sequencing** targets the 18–22 bp microRNAs, which act largely as gene
repressors and silencers; their role in transcriptional and translational regulation is the reason
this has become its own sequencing category rather than a byproduct of total RNA-seq.

## Applications III: epigenomics

Epigenomics studies heritable changes in gene activity that are not changes in the DNA sequence
itself — methylation, small-RNA regulation, DNA–protein binding, histone modification.

**Methylation sequencing** reads cytosine methylation (5mC) at single-base resolution, genome-wide.
Two protocols dominate: whole-genome bisulfite sequencing (WGBS) treats DNA with sodium bisulfite,
which converts unmethylated cytosines to uracil (read out as thymine after sequencing) while leaving
methylated cytosines unchanged, so methylation status is read directly from the sequence; reduced
representation bisulfite sequencing (RRBS) first digests DNA with the enzyme MspI — which is
insensitive to methylation status — and keeps only the 100–150 bp fragments enriched for CpG-rich,
promoter-proximal DNA, then applies the same bisulfite step to a much smaller, cheaper library.

**ChIP sequencing** combines chromatin immunoprecipitation with sequencing to map where a protein of
interest binds DNA (or RNA) genome-wide; the immunoprecipitation step is specific to the protein,
species, and tissue, and only the resulting fragments enter a standard NGS library prep.

**Ribosome profiling** sequences the mRNA fragments physically protected by a bound ribosome, giving
a genome-wide snapshot of which transcripts are being actively translated at a given moment — useful
for studying translational control, estimating protein synthesis rates, and predicting protein
abundance directly, rather than inferring it from mRNA levels alone.

## From reads to data: the workflow around the chemistry

The four-step chemistry above sits inside a larger pipeline built to move data off the instrument and
into analysis with as little manual handling as possible. Library preparation kits exist for every
method above, scaled from manual protocols for small labs to automated workstations for large
sequencing centres; sequencing platforms range correspondingly from benchtop instruments to
production-scale systems. Illumina's cloud platform (BaseSpace Sequence Hub, with an on-site variant
for labs that need to keep data local) streams data straight off the instrument and offers a
standard set of downstream applications — alignment and variant calling, RNA expression profiling,
16S metagenomics, tumour–normal comparison, epigenetic analysis — built by Illumina and third-party
developers on a common infrastructure, so that the specific method chosen at the library-preparation
step is what determines the downstream analysis, not a change in instrument or chemistry.

## Glossary

A short reference for terms that recur across methods sections without necessarily being defined
each time:

- **Adapter** — the oligo ligated to each end of a library fragment, complementary to the lawn of
  oligos on the flow cell surface.
- **Insert** — the original sample fragment sitting between the two adapters (typically 200–500 bp,
  or 2–5 kb for a mate-pair library).
- **Cluster** — the clonal group of roughly a thousand copies of one template molecule, produced by
  bridge amplification on the flow cell; one cluster produces one read (two, if paired-end).
  10,000 clusters therefore give 10,000 single reads or 20,000 paired-end reads.
- **Flow cell** — the glass slide, divided into one to eight lanes, whose surface carries the
  adapter-complementary oligo lawn that clusters form on.
- **Coverage (depth)** — the average number of sequenced bases aligning to each reference base;
  "$30\times$ coverage" means each base was sequenced 30 times on average.
- **Index / barcode / tag** — a short (8–12 bp) sequence added to a library during preparation so
  that pooled ("multiplexed") libraries can be sorted computationally after sequencing.
- **Contig** — a stretch of continuous sequence assembled in silico from overlapping reads, used
  when there is no reference to align to.
- **Reference genome** — the assembled genome that new reads are aligned against as the first step
  of most downstream analyses.
- **Mate-pair library** — a paired-end library with a long (2–5 kb) gap between the two ends,
  useful for spanning repeats during de novo assembly and for detecting larger structural variants.

## Sources

All material in this chapter comes from a single document supplied as course reading, split by the
converter into five files, all part of `omics-statistics/statomics/sga21`:

- Section I (evolution of genomic science, SBS chemistry basics, paired-end sequencing, dynamic
  range, library-prep advances, multiplexing, instrumentation) —
  `illumina_sequencing_introduction/01-i-welcome-to-next-generation-sequencing.md`.
- Section II (genomics, transcriptomics, epigenomics methods) —
  `illumina_sequencing_introduction/02-ii-ngs-methods.md`.
- Section III (the Illumina DNA-to-data workflow and BaseSpace) —
  `illumina_sequencing_introduction/03-iii-illumina-dna-to-data-ngs-solutions.md`.
- Section IV (glossary) — `illumina_sequencing_introduction/04-iv-glossary.md`.
- Section V (numbered references, e.g. Sanger et al. 1977 on chain-termination sequencing, Bentley
  et al. 2008 on reversible-terminator chemistry, Grad et al. 2012 on the 2011 *E. coli* outbreak) —
  `illumina_sequencing_introduction/05-v-references.md`.

The source is an Illumina white paper ("Welcome to Next-Generation Sequencing"), converted from a
PDF with no extractable text layer; the conversion note on each file flags the prose as a paraphrase
in places and every equation as unverified, so numeric claims here should be checked against the
original PDF (linked from each file's front matter) before being cited further. No slide deck,
transcript, or exercise set was supplied alongside this reading.

---

[← 8. Interaction Effects and Stage-wise Testing](08-interaction-effects-and-stage-wise-testing.md) · [Contents](index.md) · [10. Course Description and Program →](10-course-description-and-program.md)
