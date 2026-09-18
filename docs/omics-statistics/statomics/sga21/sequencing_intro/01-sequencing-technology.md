---
title: Sequencing technology
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_intro.Rmd
source_file: sources/statomics-sga21/sequencing_intro.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sequencing_intro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_intro.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Sequencing technology

```r
# A function for captioning and referencing images
fig <- local({
    i <- 0
    ref <- list()
    list(
        cap=function(refName, text) {
            i <<- i + 1
            ref[[refName]] <<- i
            paste("Figure ", i, ": ", text, sep="")
        },
        ref=function(refName) {
            ref[[refName]]
        })
})
```

```r
suppressPackageStartupMessages({
  library(knitr)
  library(rmarkdown)
  library(ggplot2)
})
```

## The study of gene expression

 - The first part of this course focussed on proteomics, studying the concentration of proteins in biological samples. We have seen that identification of proteins and measuring their respective concentrations are extremely challenging, leading to many technological and statistical challenges in order to interpret these data.
 - In the second part of the course, we will focus on measuring gene expression, i.e., measuring the concentration of mRNA molecules, that may eventually be translated into proteins, but may also have functions on their own.

 - Measuring mRNA molecules typically happens through sequencing.
 - The technology continues to evolve at an incredible speed. The data output of so-called `next generation' sequencing machines has more than doubled each year! Simultaneously, the cost of sequencing (in terms of \$ per Gigabase) is dropping. Each year, we're able to sequence more for less money, providing more information, as well as also computational and statistical challenges.
 - This tremendous technological revolution has revolutionized biology, and genomic sequencing is now a core component of the modern-day biologist's toolkit.
 - The large majority of sequencing data is generated using sequencing-by-synthesis using machines produced by the company Illumina. While new players such as Pacific Biosciences and Oxford Nanopore have entered the scene, these are typically most useful for (but not limited to) DNA sequencing rather than gene expression studies, owing to their capability of sequencing long molecules.

```r
# All defaults
include_graphics("./images_sequencing/seqTechnology_throughput.png")
```

### The sequencing workflow

Library preparation steps:

1. First, the biological **samples of interest are collected**. Owing to the maturity of different protocols for sequencing, several types of biological input samples are amenable to sequencing, such as frozen tissues or FFPE-preserved samples.
2. The **(m)RNA molecules from our sample are captured**. This typically involves cell lysis in order to release the (m)RNA molecules from within the cells. The mRNA molecules are most often captured using (i) polyA-capture to select for polyadenylated RNA, or (ii) ribosomal depletion, where ribosomal and transfer RNAs are depleted, and so also non-polyA-mRNA molecules may be captured, such as micro RNAs. In the case of `targeted sequencing', where relevant molecules are of main interest (e.g., a gene panel), these targets can be specifically targeted in this step.
3. **Fragmentation** of captured molecules. The captured molecules are fragmented, either chemically or mechanically. The appropriate size of fragments depends on the sequencing machines, but is often in the range of 300 - 500bp.
4. **Reverse transcription**. Current dominant sequencing machines only sequence double-stranded DNA molecules. Therefore, in order to measure single-stranded mRNA, we must first reverse transcribe these molecules to a double-stranded complementary (cDNA) molecule.
5. **Adapter ligation**. Adapters are oligonucleotides (short sequences of nucleotides) that are platform-specific sequences for fragment recognition by the sequencing machines. These are added either to the 3' or 5' end of the cDNA molecules or used as primers in the reverse transcription reaction. The final cDNA library consists of cDNA inserts flanked by an adapter sequence on each end.
6. **PCR amplification**. To increase concentration, several PCR reaction cycles are performed.
7. Loading the amplified cDNA library on the **sequencing** machine. Find out how sequencing-by-synthesis works through [this video](https://www.youtube.com/watch?v=fCd6B5HRaZ8). Note that the video shows paired-end sequencing, where a number of basepairs are sequenced at each end of the fragment. All previous steps together are described as `sample prep' in that video.

```r
include_graphics("./images_sequencing/seqWorkflow1_clean.png")
```

Note that several variants of library preparation protocols are available. The most important ones are:

 - Single-end vs paired-end sequencing: In single-end sequencing, a single end (3' or 5') of the cDNA fragment is sequenced. In paired-end sequencing, both ends are sequenced, and depending on the size of the fragment, the reads may or may not overlap.
 - Strand-specific protocols: Some library preparation protocols allow measuring strand specificity, where the strand information (i.e., sense/antisense) of each read can be preserved.

### The sequencing output files

- The typical output of a sequencing machine we will be working with are FASTA or FASTQ files for each sample. Each of these files are several gigbases large and contain millions of sequences, which we will call **reads**. For paired-end sequencing, there are two files for each sample, one for each end of the sequenced fragments.
 - The difference between a FASTA file and a FASTQ file, is that while FASTA files only store the results of base calls (sequences), FASTQ files also store the quality score of each base call (i.e., each called nucleotide), which can be useful in downstream analyses such as mapping or variant calling.
 - A FASTQ file contains four lines for each sequenced read:
    1. Sequence identifier line, starting with @.
    2. The sequence.
    3. Another sequence identifier line, now starting with +.
    4. Quality scores.

```r
include_graphics("./images_sequencing/fastqLine.png")
```

As you'll have noticed, the base call quality scores are encoded as ASCII characters for efficient storage. These ASCII characters can be converted into integers called Phred scores, which are logarithmically related to the probability of an erroneous base call.

 ---

Many published papers upload their raw FASTQ-files on the Gene Expression Omnibus (GEO).
If you'll be working in transcriptomics, you will most likely have to download files from there. You can get the links manually, e.g., by following [this tutorial](https://www.imm.ox.ac.uk/files/ccb/downloading_fastq_geo), through `R` using custom packages, e.g., [GEOfastq](https://bioconductor.org/packages/release/bioc/html/GEOfastq.html), or you can use a command-line program like [kingfisher](https://github.com/wwood/kingfisher-download) (recommended).

---

[Up: contents](index.md) · [Preprocessing of raw sequencing data →](02-preprocessing-of-raw-sequencing-data.md)
