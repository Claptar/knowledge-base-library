---
title: 6.874 Recitation
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-07-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-03-07-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 6.874 Recitation

3-7-13

DG Lectures 8 + Topic Models

## Announcements

- Project specific aims due Sunday
    - Look at NIH examples
- Pset #2 due in 1 week (03/13)
    - For problem 2B, Matlab and Mathematica use a (1-p) parameterization in contrast to lecture
      slides (p):
        - R or N = 1/k (same as in lecture slides)
        - P = $\dfrac{1/k}{\lambda + 1/k}$ for Matlab/Mathematica vs. $\dfrac{\lambda}{\lambda + 1/k}$
          in lecture slides
    - Mean dispersion function problem

## RNA-Seq Analysis

- Central Dogma: DNA $\rightarrow$ mRNA $\rightarrow$ protein
    - pre-mRNA contains not only protein coding exons, but non-coding regions: 5'- and 3'-UTR,
      introns, poly(A) tail
    - Introns must be spliced out to create mature mRNA that can be translated into protein
    - Some exons may also be spliced out (alternative splicing to create different mRNA isoforms
      of the same gene)

A diagram shows a pre-mRNA (5' UTR, Exon, Intron, Exon, Intron, Exon, 3' UTR) with the two introns
spliced out to produce the mature mRNA (5' UTR, Exon, Exon, Exon, 3' UTR). Source uncredited;
excluded from the Creative Commons license (see http://ocw.mit.edu/help/faq-fair-use/).

- We'd like to know what mRNA isoforms of gene are present in cells

## RNA-Seq Analysis – Alternative Splicing

- Central Dogma: DNA $\rightarrow$ mRNA $\rightarrow$ protein
    - some exons may also be spliced out (alternative splicing to create different mRNA isoforms of
      the same gene)

The figure shows a 10-exon gene (exons 5-9 alternatively spliced) and nine resulting mRNA isoforms
(G1a–G1o) that combine different subsets of exons 5-9 while keeping exons 1-4 and 10 fixed,
illustrating that alternative splicing of one gene produces multiple distinct proteins. Courtesy of
Elsevier B.V., used with permission. Source: Aoki-Suzuki, Mika, Kazuo Yamada, et al. "A
Family-based Association Study and Gene Expression Analyses of Netrin-G1 and G2 Genes in
Schizophrenia." *Biological Psychiatry* 57, no. 4 (2005): 382-93.

## RNA-seq Protocol

(1) isolate total RNA — the figure shows pre-mRNA, mature (polyadenylated) mRNA, tRNA and miRNA as
distinct species isolated from a cell.

(2) select fraction of interest (e.g. polyA selection) — only the polyadenylated mature mRNAs are
retained.

(3) fragment, reverse transcribe, sequence and map — reads are shown mapping back to a reference
genome divided into 5' UTR, exon 1, exon 2, exon 3 and 3' UTR; some reads map entirely within one
exon, and junction-spanning reads include an exon-exon junction.

## [Untitled — replicate design figure]

The figure shows two flasks processed as technical replicates (split after one culture, each
undergoing separate library prep and sequencing to give Technical Rep 1 and Technical Rep 2) versus
two separately grown flasks processed as biological replicates (each undergoing library prep and
sequencing to give Biological Rep 1 and Biological Rep 2). Source unknown; excluded from the
Creative Commons license (see http://ocw.mit.edu/help/faq-fair-use/).

## RNA-seq: identifying isoforms

- Some reads map completely within a single exon – don't directly tell us which isoforms are
  present, although expression levels of different exons can be helpful (e.g. twice as many exon 1
  reads compared to exon 4 – probably some isoforms that include exon 1 but not exon 4)

The figure shows four exons (1–4) along a genome sequence with non-junction-spanning reads mapped
above each exon, illustrating the distinction between non-junction-spanning reads, the genome
sequence and the putative exons.

- How do we directly identify the isoforms that generated these reads? Look at junction-spanning
  reads!
- Assuming exons 1 and 4 must be included, which isoform(s) are consistent with the following
  reads? A read spanning exon 1–exon 3 implies the isoform exon1-exon3-exon4; a read spanning exon
  1–exon 4 implies the isoform exon1-exon4; a read spanning exon 1–exon 2 implies either
  exon1-exon2-exon4 or exon1-exon2-exon3-exon4.

## RNA-seq: identifying isoforms

(Continued from the previous slide — same exon/read figure.)

- How do we directly identify the isoforms that generated these reads? Look at junction-spanning
  reads!
- Since reads are generally 100bp or shorter, most reads only span 1 junction to give adjacent
  exons present in isoforms – assembling the full isoforms of 5-10+ exons and estimating their
  expression levels from only adjacent exon pairs is difficult
    - Promise in longer read (kb) technologies (e.g. Pacific Biosciences, Oxford Nanopore
      sequencing)

## DEseq

- we would like to know whether, for a given *region* (e.g. gene, TF binding site, etc.), an
  observed difference in read counts between different biological conditions is significant
- assume the number of reads in sample $j$ that are assigned to region $i$ is approx. distributed
  according to the negative binomial:

$$K_{ij} \sim NB(\mu_{ij}, \sigma_{ij}^2)$$

- the NB has two parameters, which we need to estimate from the data, but typically the # of
  replicates is too small to get good estimates, particularly for the variance for region $i$
- if we don't have enough replicates to get a good estimate of the variance for region $i$ under
  condition $\rho(j)$, DEseq will pool the data from regions with similar expression strength to
  try to get a better estimate
- we then test for significance using a LRT

## DEseq

- the Likelihood Ratio Test is the ratio of the probability under the null model and the alternate
  model
- for example, if we are testing for whether there is significant difference in counts in
  condition A relative to B, we calculate:

$$T_i = 2\log \frac{P(K_{iA}|H_a)P(K_{iB}|H_a)}{P(K_{iA}, K_{iB}|H_0)}$$

- for $H_a$, we allow the distribution of $K_{iA}$ and $K_{iB}$ to be different, while under $H_0$
  we assume that $K_{iA}, K_{iB}$ are drawn from the same distribution (e.g. isoform $i$ is
  identically expressed under conditions A and B)
- then $T_i$ follows a Chi Square distribution with $df = 4 - 2 = 2$

## Hypergeometric Test: when you want to know if overlap between two subsets is significant

- From DESeq, we identified genes differentially expressed between control and treatment after
  treatment with two different stress conditions: (A) heat shock and (B) oxidative stress
- We propose that the pathways involved in the responses to A and B are similar, so the genes
  affected by A might overlap with the genes affected by B
- We observe the following:

N = total # of genes measured = 500
Na = total # genes changed in A = 100
Nb = total # genes changed in B = 150
k = genes changed in both A and B = 40

Is this overlap significant (e.g. unlikely by chance)? -> do a hypergeometric test

A Venn diagram shows N = 500 total genes, with a set of size Na = 100 (60 unique + 40 shared) and a
set of size Nb = 150 (110 unique + 40 shared) overlapping in 40 genes. Source unknown; excluded
from the Creative Commons license (see http://ocw.mit.edu/help/faq-fair-use/).

## Hypergeometric Test

The probability of observing exactly $k$ items overlapping among $Na$ and $Nb$ size groups drawn
from $N$ total items is

$$P(k; n_a, n_b, N) = \frac{\binom{n_a}{k}\binom{N-n_a}{n_b-k}}{\binom{N}{n_b}}$$

Our p-value is the probability of observing an overlap *at least as extreme* as the overlap we
observed (which is $k$):

$$P(x \geq k) = \sum_{i=k}^{\min(n_a,n_b)} P(i; n_a, n_b, N)$$

(min$(n_a,n_b)$ is the max value for $k$, since the smaller set can be at most completely contained
within the larger set.) The same Venn diagram (N=500, Na=100, Nb=150, overlap=40) is repeated
alongside. Source unknown; excluded from the Creative Commons license (see
http://ocw.mit.edu/help/faq-fair-use/).

## Hypergeometric Test

For this example, we obtain:

$$P(x \geq 40) = \sum_{i=40}^{100} P(i; 100, 150, 500) = \sum_{i=40}^{100}
\frac{\binom{100}{i}\binom{500-100}{150-i}}{\binom{500}{150}} = 0.0112$$

Therefore, with $\alpha = 0.05$, we reject the null hypothesis that the overlap between conditions
A and B are due to random chance, suggesting there is some similarity between gene expression
changes caused by heat shock and oxidative stress. The same Venn diagram is repeated alongside.
Source unknown; excluded from the Creative Commons license (see
http://ocw.mit.edu/help/faq-fair-use/).

## [Untitled — GO category heatmap figure]

The figure is a clustered heatmap (colour key −2 to 2) of gene expression across H1 hESCs, Female
and Male samples, with a dendrogram grouping genes into 13 numbered GO categories (e.g. category 1:
negative transcription regulation/sex differentiation; category 6: meiosis, oocyte
development, DNA repair; category 8: homeobox, meiosis, spermatogenesis, germ plasm,
anterior-posterior pattern; category 13: regulation of apoptosis, nuclear lumen, protein complex
biogenesis). Courtesy of Macmillan Publishers Limited, used with permission. Source: Gkountela,
Sofia, Ziwei Li, et al. "The Ontogeny of cKIT+ Human Primordial Germ Cells Proves to be a Resource
for Human Germ Line Reprogramming, Imprint Erasure and in Vitro Differentiation." *Nature Cell
Biology* 15, no. 1 (2013): 113-22.

## PCA identifies the directions (PC1 and PC2) along which the data have the largest spread

The figure shows a cloud of points along a diagonal trend, with two arrows v1 and v2 (the first and
second principal component directions) drawn through the centre of the cloud, and a red marginal
density curve along the v1 direction. Source unknown; excluded from the Creative Commons license
(see http://ocw.mit.edu/help/faq-fair-use/).

- 1st principal component is the direction of maximal variation among your sample
    - Magnitude of this component is related to how much variation there is in this direction
- 2nd principal component is next direction (orthogonal to 1st direction) of remaining maximal
  variation in your sample
    - Magnitude of this component will be smaller than that of 1st
- etc.

---

[Up: contents](index.md) · [PCA identifies the directions (PC1 and PC2) along which the data have the largest spread →](02-pca-identifies-the-directions-pc1-and-pc2-along-which-the-da.md)
