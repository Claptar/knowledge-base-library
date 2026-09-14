---
title: 2 Finding eQTLs (20pts)
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/psets/04-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Finding eQTLs (20pts)

**Source:** `psets/04-questions.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem, we will examine the sources of variation in gene expression that partition a population into subpopulations. You will find the datasets used in this question in the `eQTLs` folder available though the problem set folder on the course website.

- (a) In the file `ExpData.txt` , you will find log-normalized RNA-seq expression data from our population of 1000 samples, with 5000 genes profiled for each sample. Do a principal components analysis on this dataset to find the clusters of samples that have similar patters of gene expression. Plot the output of your analysis, and describe the patterns that you observe. What is the structure inherent in this population?

For PCA, we recommend you use the `princomp` function in the `stats` package available by default in `R` . However, many other languages such as MATLAB and python have analogous functions; you should use whatever you are most comfortable with. In your plots, be sure the axes are labeled with the components you are displaying in each plot. Also make sure that at least one of your plots colours the points corresponding

1

to the samples with the sub-population that you think they should belong to. (Hint: You can re-use your k-means code from Pset 3 to find these sub-populations!).

Hand in your write-up and the code you used for plotting and assigning samples to sub-populations.

- (b) In the file `SnpData.txt` , you will find genotyping data for the same 1000 samples across 500 SNPs. Each SNP’s genotype has been called with reference to the same reference genotype; “0” thus represents the reference allele, “2” represents the non-reference allele, and “1” represents a different allele on each strand.

You will find that some of the SNPs (more than 5, less than 100) are eQTLs, that is, they have an effect on the expression of one or more of the genes we collected expression data for. Using whatever model you see fit, search for these eQTLs using the genotyping data and the expression data. You may not have the computational resources to test all combinations of SNPs and genes, so you should think about smart ways to choose subsets of each to find some eQTLs - you don’t have to find all of them!

For three of the eQTLs you found, present the evidence you have for why you think it is an eQTL, and not just associated with the expression of a gene by chance alone. Be sure to include plots in your analysis to support your hypothesis, and to thoroughly explain the method you used to find eQTLs. You can assume that the association between genotype and expression is linear for eQTLs. Don’t forget that you should be correcting for the fact that you are performing multiple significance tests.

Hand in your write-up as well as the code you used to look for eQTLs in the two datasets provided.

- (c) In the above analysis, we were forced to consider all pairs of SNPs and genes to identify eQTLs. What sources of data that have not been provided as part of this problem would have been useful in constraining the amount of such pairs you had to test? For at least two sources, give a description of what the dataset would look like (what are the rows and columns of the data matrix? what kinds of values are stored in the matrix?) and explain how you would use it to filter out pairs of SNPs and genes that are unlikely to be associated with one another.

2

---

[← 1 Generalized suffix trees (10pts)](02-1-generalized-suffix-trees-10pts.md) · [Up: contents](index.md) · [3 Coalescent simulation (6.878 only, 10pts) →](04-3-coalescent-simulation-6-878-only-10pts.md)
