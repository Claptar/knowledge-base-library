---
title: I. Welcome to Next-Generation Sequencing
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/illumina_sequencing_introduction.pdf
source_file: sources/statomics-sga21/docs/illumina_sequencing_introduction.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`docs/illumina_sequencing_introduction.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/illumina_sequencing_introduction.pdf) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# I. Welcome to Next-Generation Sequencing

www.illumina.com/technology/next-generation-sequencing.html

## Table of Contents

Table of Contents 2
I. Welcome to Next-Generation Sequencing 3
a. The Evolution of Genomic Science 3
b. The Basics of NGS Chemistry 4
c. Advances in Sequencing Technology 5
Paired-End Sequencing 5
Tunable Coverage and Unlimited Dynamic Range 6
Advances in Library Preparation 6
Multiplexing 7
Flexible, Scalable Instrumentation 7
II. NGS Methods 8
a. Genomics 8
Whole-Genome Sequencing 8
Exome Sequencing 8
De novo Sequencing 9
Targeted Sequencing 9
b. Transcriptomics 11
Total RNA and mRNA Sequencing 11
Targeted RNA Sequencing 11
Small RNA and Noncoding RNA Sequencing 11
c. Epigenomics 12
Methylation Sequencing 12
ChIP Sequencing 12
Ribosome Profiling 12
III. Illumina DNA-to-Data NGS Solutions 13
a. The Illumina NGS Workflow 13
b. Integrated Data Analysis 13
IV. Glossary 14
V. References 15

### a. The Evolution of Genomic Science

DNA sequencing has come a long way since the days of two-dimensional chromatography in the 1970s. With the advent of the Sanger chain termination method$^1$ in 1977, scientists gained the ability to sequence DNA in a reliable, reproducible manner. A decade later, Applied Biosystems introduced the first automated, capillary electrophoresis (CE)-based sequencing instruments, the AB370 in 1987 and the AB3730xl in 1998, instruments that became the primary workhorses for the NIH-led and Celera-led Human Genome Projects.$^2$ While these "first-generation" instruments were considered high throughput for their time, the Genome Analyzer emerged in 2005 and took sequencing runs from 84 kilobase (kb) per run to 1 gigabase (Gb) per run.$^3$ The short read, massively parallel sequencing technique was a fundamentally different approach that revolutionized sequencing capabilities and launched the "next generation" in genomic science. From that point forward, the data output of next-generation sequencing (NGS) has outpaced Moore's law, more than doubling each year (Figure 1).

**Figure 1: Sequencing Cost and Data Output Since 2000**—The dramatic rise of data output and concurrent falling cost of sequencing since 2000. The Y-axes on both sides of the graph are logarithmic.

In 2005, a single run on the Genome Analyzer could produce roughly one gigabase of data. By 2014, the rate climbed to 1.8 terabases (Tb) of data in a single sequencing run, an astounding $1000\times$ increase. It is remarkable to reflect on the fact that the first human genome, famously copublished in *Science* and *Nature* in 2001, required 15 years to sequence and cost nearly three billion dollars. In contrast, the HiSeq X$^\circledR$ Ten System, released in 2014, can sequence over 45 human genomes in a single day for approximately $1000 each (Figure 2).$^4$

Beyond the massive increase in data output, the introduction of NGS technology has transformed the way scientists think about genetic information. The $1000 dollar genome enables population-scale sequencing and establishes the foundation for personalized genomic medicine as part of standard medical care. Researchers can now analyze thousands to tens of thousands of samples in a single year. As Eric Lander, founding director of the Broad Institute of MIT and Harvard and principal leader of the Human Genome Project, states:

> "The rate of progress is stunning. As costs continue to come down, we are entering a period where we are going to be able to get the complete catalog of disease genes. This will allow us to look at thousands of people and see the differences among them, to discover critical genes that cause cancer, autism, heart disease, or schizophrenia."$^5$

### Human Genomes Sequenced Annually

**Figure 2: Human Genome Sequencing Over the Decades**—The capacity to sequence all 3.2 billion bases of the human genome (at $30\times$ coverage) has increased exponentially since the 1990s. In 2005, with the introduction of the Illumina Genome Analyzer System, 1.3 human genomes could be sequenced annually. Nearly 10 years later, with the Illumina HiSeq X Ten fleet of sequencing systems, the number has climbed to 18,000 human genomes a year.

### b. The Basics of NGS Chemistry

In principle, the concept behind NGS technology is similar to CE sequencing. DNA polymerase catalyzes the incorporation of fluorescently labeled deoxyribonucleotide triphosphates (dNTPs) into a DNA template strand during sequential cycles of DNA synthesis. During each cycle, at the point of incorporation, the nucleotides are identified by fluorophore excitation. The critical difference is that, instead of sequencing a single DNA fragment, NGS extends this process across millions of fragments in a massively parallel fashion. More than 90% of the world's sequencing data are generated by Illumina sequencing by synthesis (SBS) chemistry.* It delivers high accuracy, a high yield of error-free reads, and a high percentage of base calls above Q30.$^{6-8}$

Illumina NGS workflows include four basic steps:

1. **Library Preparation**—The sequencing library is prepared by random fragmentation of the DNA or cDNA sample, followed by $5'$ and $3'$ adapter ligation (Figure 3A). Alternatively, "tagmentation" combines the fragmentation and ligation reactions into a single step that greatly increases the efficiency of the library preparation process.$^9$ Adapter-ligated fragments are then PCR amplified and gel purified.
2. **Cluster Generation**—For cluster generation, the library is loaded into a flow cell where fragments are captured on a lawn of surface-bound oligos complementary to the library adapters. Each fragment is then amplified into distinct, clonal clusters through bridge amplification (Figure 3B). When cluster generation is complete, the templates are ready for sequencing.
3. **Sequencing**—Illumina SBS technology uses a proprietary reversible terminator–based method that detects single bases as they are incorporated into DNA template strands (Figure 3C). As all four reversible terminator–bound dNTPs are present during each sequencing cycle, natural competition minimizes incorporation bias and greatly reduces raw error rates compared to other technologies.$^{6,7}$ The result is highly accurate base-by-base sequencing that virtually eliminates sequence context–specific errors, even within repetitive sequence regions and homopolymers.
4. **Data Analysis**—During data analysis and alignment, the newly identified sequence reads are aligned to a reference genome (Figure 3D). Following alignment, many variations of analysis are possible, such as single nucleotide polymorphism (SNP) or insertion-deletion (indel) identification, read counting for RNA methods, phylogenetic or metagenomic analysis, and more.

A detailed animation of SBS chemistry is available at www.illumina.com/SBSvideo.

\*Data calculations on file. Illumina, Inc., 2015.

**Figure 3: Next-Generation Sequencing Chemistry Overview**—Illumina NGS includes four steps: (A) library preparation, (B) cluster generation, (C) sequencing, and (D) alignment and data analysis.

### c. Advances in Sequencing Technology

#### Paired-End Sequencing

A major advance in NGS technology occurred with the development of paired-end (PE) sequencing (Figure 4). PE sequencing involves sequencing both ends of the DNA fragments in a library and aligning the forward and reverse reads as read pairs. In addition to producing twice the number of reads for the same time and effort in library preparation, sequences aligned as read pairs enable more accurate read alignment and the ability to detect indels, which is not possible with single-read data.$^8$ Analysis of differential read-pair spacing also allows removal of PCR duplicates, a common artifact resulting from PCR amplification during library preparation. Furthermore, PE sequencing produces a higher number of SNV calls following read-pair alignment.$^{8,9}$ While some methods are best served by single-read sequencing, such as small RNA sequencing, most researchers currently use the paired-end approach.

**Figure 4: Paired-End Sequencing and Alignment**—Paired-end sequencing enables both ends of the DNA fragment to be sequenced. Because the distance between each paired read is known, alignment algorithms can use this information to map the reads over repetitive regions more precisely. This results in better alignment of reads, especially across difficult-to-sequence, repetitive regions of the genome.

#### Tunable Coverage and Unlimited Dynamic Range

The digital nature of NGS allows a virtually unlimited dynamic range for read-counting methods, such as gene expression analysis. Microarrays measure continuous signal intensities and the detection range is limited by noise at the low end and signal saturation at the high end, while NGS quantifies discrete, digital sequencing read counts. By increasing or decreasing the number of sequencing reads, researchers can tune the sensitivity of an experiment to accommodate various study objectives. Because the dynamic range with NGS is adjustable and nearly unlimited, researchers can quantify subtle gene expression changes with much greater sensitivity than traditional microarray-based methods. Sequencing runs can be tailored to zoom in with high resolution on particular regions of the genome, or provide a more expansive view with lower resolution.

The ability to easily tune the level of coverage offers several experimental design advantages. For instance, somatic mutations may only exist within a small proportion of cells in a given tissue sample. Using mixed tumor–normal cell samples, the region of DNA harboring the mutation must be sequenced at extremely high coverage, often upwards of $1000\times$, to detect these low-frequency mutations within the mixed cell population. On the other side of the coverage spectrum, a method like genome-wide variant discovery usually requires a much lower coverage level. In this case, the study design involves sequencing many samples (hundreds to thousands) at lower resolution, to achieve greater statistical power within a given population.

#### Advances in Library Preparation

With Illumina NGS, library preparation has undergone rapid improvements. The first NGS library prep protocols involved random fragmentation of the DNA or RNA sample, gel-based size selection, ligation of platform-specific oligonucleotides, PCR amplification, and several purification steps. While the 1–2 days required to generate these early NGS libraries were a great improvement over traditional cloning techniques, current NGS protocols, such as Nextera$^\circledR$ XT DNA Library Preparation, have reduced the library prep time to less than 90 minutes.$^{10}$ PCR-free and gel-free kits are also available for sensitive sequencing methods. PCR-free library preparation kits result in superior coverage of traditionally challenging areas such as high AT/GC-rich regions, promoters, and homopolymeric regions.$^{11}$

For a complete list of Illumina library preparation kits, visit www.illumina.com/products/by-type/sequencing-kits/library-prep-kits.html.

#### Multiplexing

In addition to the rise of data output per run, the sample throughput per run in NGS has also increased over time. Multiplexing allows large numbers of libraries to be pooled and sequenced simultaneously during a single sequencing run (Figure 5). With multiplexed libraries, unique index sequences are added to each DNA fragment during library preparation so that each read can be identified and sorted before final data analysis. With PE sequencing and multiplexing, NGS has dramatically reduced the time to data for multisample studies and enabled researchers to go from experiment to data quickly and easily.

Gains in throughput from multiplexing come with an added layer of complexity, as sequencing reads from pooled libraries need to be identified and sorted computationally in a process called demultiplexing before final data analysis (Figure 5). The phenomenon of index misassignment between multiplexed libraries is a known issue that has impacted NGS technologies from the time sample multiplexing was developed.$^{12}$ Index hopping is a specific cause of index misassignment that can result in incorrect assignment of libraries from the expected index to a different index in the pool, leading to misalignment and inaccurate sequencing results.

For more information regarding index hopping, including mechanisms by which it occurs, how Illumina measures index hopping, and best practices for mitigating the impact of index hopping on sequencing data quality, read the *Effects of Index Misassignment on Multiplexing and Downstream Analysis White Paper*.

**Figure 5: Library Multiplexing Overview**—(A) Unique index sequences are added to two different libraries during library preparation. (B) Libraries are pooled together and loaded into the same flow cell lane. (C) Libraries are sequenced together during a single instrument run. All sequences are exported to a single output file. (D) A demultiplexing algorithm sorts the reads into different files according to their indexes. (E) Each set of reads is aligned to the appropriate reference sequence.

#### Flexible, Scalable Instrumentation

While the latest NGS platforms can produce massive data output, NGS technology is also highly flexible and scalable. Sequencing systems are available for every method and scale of study, from small laboratories to large genome centers (Figure 6). Illumina NGS instruments range from the benchtop MiniSeq™ System, with output ranging from 1.8–7.5 Gb for targeted sequencing studies, to the NovaSeq™ 6000 System, which can generate an impressive 6 Tb and 20 B reads in ~ 2 days$^\dagger$ for population-scale studies.

Flexible run configurations are also engineered into the design of Illumina NGS sequencers. For example, the HiSeq$^\circledR$ 2500 System offers two run modes and single or dual flow cell sequencing while the NextSeq$^\circledR$ Series of Sequencing Systems offers two flow cell types to accommodate different throughput requirements. The HiSeq 3000/4000 Series uses the same patterned flow cell technology as the HiSeq X instruments for cost-effective production-scale sequencing. The new NovaSeq Series of systems unites the latest high-performance imaging with the next generation of Illumina patterned flow cell

technology to deliver massive increases in throughput. This flexibility allows researchers to configure runs tailored to their specific study requirements, with the instrument of their choice.

For an in-depth comparison of Illumina platforms, visit www.illumina.com/systems/sequencing.html or explore the Sequencing Platform Comparison Tool at www.illumina.com/systems/sequencing-platforms/comparison-tool.html.

**Figure 6: Sequencing Systems for Virtually Every Scale**—Illumina offers innovative NGS platforms that deliver exceptional data quality and accuracy over a wide scale, from small benchtop sequencers to production-scale sequencing systems.

---

[Up: contents](index.md) · [II. NGS Methods →](02-ii-ngs-methods.md)
