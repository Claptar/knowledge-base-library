---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/08-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/08-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### Lecture 8 Understanding Transcription RNA-seq analysis

Foundations of Computational Systems Biology David K. Gifford

1

### Lecture 8 – RNA-seq Analysis

- RNA-seq principles – How can we characterize mRNA isoform expression using high-throughput sequencing?

- Differential expression and PCA – What genes are differentially expressed, and how can we characterize expressed genes?

- Single cell RNA-seq – What are the benefits and challenges of working with single cells for RNA-seq?

2

##### RNA-Seq characterizes RNA molecules


<!-- Start of picture text -->
High-throughput<br>sequencing of RNAs<br>at various stages of<br>processing<br>cytoplasm<br>Slide courtesy Cole Trapnel<br><!-- End of picture text -->


<!-- Start of picture text -->
export to cytoplasm<br>nucleus<br>A  B  C  High-throughput<br>mRNA  sequencing of RNAs<br>A  C  at various stages of<br>processing<br>splicing<br>A  B  C<br>pre-mRNA or<br>ncRNA<br>transcription<br>A  B  C  Gene in genome<br>cytoplasm<br><!-- End of picture text -->

Courtesy of Cole Trapnell. Used with permission.

3

###### **Pervasive tissue-specific regulation of alternative mRNA isoforms.**


**ET Wang** **_et al. Nature_ 000, 1-7 (2008) doi:10.1038/ nature07509**

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Wang, Eric T., Rickard Sandberg, et al. "Alternative Isoform Regulation in Human Tissue Transcriptomes." _Nature_ 456, no. 7221 (2008): 470-6.

4

###### **RNA-Seq: millions of short reads from fragmented mRNA**


<!-- Start of picture text -->
Extract RNA from<br>cells/tissue<br><!-- End of picture text -->


<!-- Start of picture text -->
+ splice junctions!<br><!-- End of picture text -->

Courtesy of Macmillan Publishers Limited. Used with permission.

Source: Pepke, Shirley, Barbara Wold, et al. "Computation for ChIP-seq and RNA-seq Studies." _Nature Methods_ 6 (2009): S22-32.

**Pepke et. al.** **_Nature Methods_ 2009**

5

###### Mapping RNA-seq reads to a reference genome reveals expression


<!-- Start of picture text -->
Sox2<br><!-- End of picture text -->

6

###### RNA-seq reads map to exons and across exons


<!-- Start of picture text -->
Reads over exons<br><!-- End of picture text -->


<!-- Start of picture text -->
Smug1<br><!-- End of picture text -->

###### **Junction reads (split between exons)**

7

###### Two major approaches to RNA-seq analysis

1. Assemble reads into transcripts.   Typical issues with coverage and correctness.

2. Map reads to reference genome and identify isoforms using constraints

- Goal is to quantify isoforms and determine significance of differential expression

**Short sequencing reads, randomly sampled from a transcript**


**exon 1**

**exon 2**

**exon 3**

- Common RNA-seq expression metrics are Reads per killobase per million reads (RPKM) or Fragments per killobase per million (FPKM)

8

###### Aligned reads reveal isoform possibilities


<!-- Start of picture text -->
A  B  C<br><!-- End of picture text -->

**identify candidate exons via genomic mapping**


<!-- Start of picture text -->
A  B  A  C  B  C<br><!-- End of picture text -->

**Generate possible pairings of exons**


<!-- Start of picture text -->
A  B  A  C  B  C<br><!-- End of picture text -->


**Align reads to possible junctions**

Courtesy of Cole Trapnell. Used with permission.

**Slide courtesy Cole Trapnell**

9

###### We can use mapped reads to learn the isoform mixture ψ"


<!-- Start of picture text -->
D<br>A<br>C<br>Isoform   Fraction<br>B  T1 ψ1" E<br>T2 ψ2"<br>T3 ψ3"<br>T4 ψ4"<br><!-- End of picture text -->

Courtesy of Cole Trapnell. Used with permission.


<!-- Start of picture text -->
Slide courtesy Cole Trapnell<br><!-- End of picture text -->

10

###### Detecting alternative splicing from mRNA-Seq data

###### **Isoforms**


###### **Inclusion reads**


**Common reads**


**Common reads**

**Exclusion reads**

**Given a set of reads, estimate:**


**= Distribution of  isoforms**

11

##### P(Ri | T=Tj) – Excluded reads

**If a single ended read or read pair R** **_i_ is structurally incompatible with transcript T** **_j_ , then**


<!-- Start of picture text -->
P ( R  =  Ri  | T  =  Tj ) = 0<br><!-- End of picture text -->


<!-- Start of picture text -->
Ri<br>Tj<br><!-- End of picture text -->


<!-- Start of picture text -->
Intron in Tj<br><!-- End of picture text -->

Courtesy of Cole Trapnell. Used with permission.

**Slide courtesy Cole Trapnell**

12

##### P(Ri | T=Tj) – Single end reads

**Cufflinks assumes that fragmentation is roughly uniform.  The probability of observing a fragment starting at a specific position** **_Si_ in a transcript of length** **_lj_ is:**


<!-- Start of picture text -->
P ( S  =  Si  | T  =  Tj ) = 1<br>l j<br>starting position in transcript, Si<br>Ri<br>Tj<br><!-- End of picture text -->


<!-- Start of picture text -->
Transcript length  lj<br><!-- End of picture text -->

Courtesy of Cole Trapnell. Used with permission.

**Slide courtesy Cole Trapnell**

13

##### P(Ri | T=Tj) – Paired end reads

**Assume our library fragments have a length distribution described by a probability density F** . **Thus, the probability of observing a particular paired alignment to a transcript:** _P_ ( _R_ = _Ri_ | _T_ = _Tj_ ) =<sup>_F_(</sup><sup>_l_</sup><sup>_<u>j</u>_(</sup><sup>_Rj_))</sup> _l j_


<!-- Start of picture text -->
Implied fragment length  lj ( Ri )<br>Ri<br><!-- End of picture text -->

**Tj**


Courtesy of Cole Trapnell. Used with permission.

**Slide courtesy Cole Trapnell**

14

###### Estimating Isoform Expression

- Find expression abundances ψ1,…,ψ _n_ for

- a set of isoforms T1,…,T _n_

- Observations are the set of reads R1,…,R _m_

_m n P_ ( _R_ | Ψ) = ∏ ∑ Ψ _jP_ ( _R_ = _Ri_ | _T_ = _Tj_ ) _i_ =0 _j_ =0 _L_ (Ψ | _R_ ) ∝ _P_ ( _R_ | Ψ) _P_ (Ψ) Ψ = argmax _L_ (Ψ | _R_ )

Ψ

- Can estimate mRNA expression of each isoform using total number of reads that map to a gene and ψ

15

---

[Up: contents](index.md) · [Case study: myogenesis →](02-case-study-myogenesis.md)
