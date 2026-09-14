---
title: Likelihood ratio test
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Likelihood ratio test

**Source:** `recitations/2014-03-05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

-Used to compare the fit of two models (the _null_ model _H_ 0 and the _alternative_ model _H_ 1 ) to the data -The likelihood ratio ⇤ tells us how many times more likely our observed data _x_ are under one model than the other:


- -since the model with more parameters (usually _H_ 1 ) will always fit at least as well as the other (therefore _L_ ( _D|H_ 1) _≥ ≥ L_ ( _D|H_ 0)), we can't just choose the model with the greatest likelihood – we can only choose _H_ 1 if it is "significantly" better – how to decide?

   - compute the test statistic _T_ : _T_ = 2 _ln_ ⇤

2 - _T_ is asymptotically _χ_<sup>_χ_</sup> distributed with _df_ equal to the difference in the # of free parameters between the two hypotheses

27

## DEseq

- we would like to know whether, for a given _region_ (e.g. gene, TF binding site, etc.), an observed difference in read counts between different biological conditions is significant

• assume the number of reads in sample _j_ that are assigned to region (gene) _i_ is approx. distributed according to the negative binomial: 2 _σ σ Kij ⇠ NB_ ( _µij, ij_ )

- the NB has two parameters, which we need to estimate from the data, but typically the # of replicates is too small to get good estimates, particularly for the variance for region **_i_**

- if we don't have enough replicates to get a good estimate of the variance for region _i_ under condition _⇢_ ( _j_ ) , DEseq will pool the data from regions with similar expression strength to try to get a better estimate

- From these estimates of the background variability among samples in the same condition, we can determine if the variance between different conditions is significantly greater than that observed between samples within the same condition

28

##### Hypergeometric Test: when you want to know if overlap between two subsets is significant

- From DESeq, we identified genes differentially expressed between control and treatment after treatment with two different stress conditions: (A) heat shock and (B) oxidative stress

- We propose that the pathways involved in the responses to A and B are similar, so the genes affected by A might overlap with the genes affected by B

- We observe the following:

**N** = total # of genes measured = **500 Na** = total # genes changed in A = **100 Nb** = total # genes changed in B = **150 k** = genes changed in both A and B = **40**

Is this overlap significant (e.g. unlikely by chance)?

-> do a hypergeometric test


29

---

[← RNA-seq: quantifying isoforms](14-rna-seq-quantifying-isoforms.md) · [Up: contents](index.md) · [Hypergeometric Test →](16-hypergeometric-test.md)
