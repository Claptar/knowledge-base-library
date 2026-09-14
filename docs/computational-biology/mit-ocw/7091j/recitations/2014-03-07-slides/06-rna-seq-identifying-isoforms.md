---
title: 'RNA-seq: identifying isoforms �'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# RNA-seq: identifying isoforms �

**Source:** `recitations/2014-03-07-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Some reads map completely within a single exon – don’t directly tell us which isoforms are present, although expression levels of different exons can be helpful (e.g. twice as many exon

- 1 reads compared to exon 4 – probably some isoforms that include exon 1 but not exon 4)


<!-- Start of picture text -->
Non-junction<br>spanning reads<br>exon 1  exon 2  exon 3  exon 4<br>genome seq<br>putative exons<br><!-- End of picture text -->

- How do we directly identify the isoforms that generated these reads? Look

- at junction-spanning reads!

- Since reads are generally 100bp or shorter, most reads only span 1 junction to give adjacent exons present in isoforms – assembling the full isoforms of 5-10+ exons and estimating their expression levels from only adjacent exon pairs is difficult

   - Promise in longer read (kb) technologies (e.g. Pacific Biosciences, Oxford Nanopore sequencing)

8

## DEseq �

- we would like to know whether, for a given _region_ (e.g. gene, TF binding site, etc.), an observed difference in read counts between different biological conditions is significant

- assume the number of reads in sample _j_ that are assigned to region _i_ is approx. distributed according to the negative binomial:

- the NB has two parameters, which we need to estimate from the data, but typically the # of replicates is too small to get good estimates, particularly for the variance for region _i_

- if we don't have enough replicates to get a good estimate of the variance for region _i_ under condition , DEseq will pool the data from regions with similar expression strength to try to get a better estimate

- we then test for significance using a LRT

9

## DEseq �

- the Likelihood Ratio Test is the ratio of the probability under the null

   - model and the alternate model

- for example, if we are testing for whether there is significant difference in counts in condition A relative to B, we calculate:

- for H_a, we allow the distribution of and to be different, while under H_0 we assume that are drawn from the same distribution (e.g. isoform _i_ is identically expressed under conditions A and B)

- then _T_  i_ follows a Chi Square distribution with _df_ = 4 – 2 = 2

10

Hypergeometric Test: when you want to know if � overlap between two subsets is significant

- From DESeq, we identified genes differentially expressed between control and treatment after treatment with two different stress conditions: (A) heat shock and (B) oxidative stress

- We propose that the pathways involved in the responses to A and B are similar, so the genes affected by A might overlap with the genes affected by B


- We observe the following:

**N** = total # of genes measured = **500 Na** = total # genes changed in A = **100 Nb** = total # genes changed in B = **150 k** = genes changed in both A and B = **40** Is this overlap significant (e.g. unlikely by chance)?

- -> do a hypergeometric test

> © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

11

---

[← RNA-seq: identifying isoforms �](05-rna-seq-identifying-isoforms.md) · [Up: contents](index.md) · [Hypergeometric Test � →](07-hypergeometric-test.md)
