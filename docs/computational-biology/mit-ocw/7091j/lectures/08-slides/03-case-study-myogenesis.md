---
title: 'Case study: myogenesis'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/08-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Case study: myogenesis

**Source:** `lectures/08-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### **Transcript categories, by coverage**


<!-- Start of picture text -->
●<br>● match ● novel isoform<br>contained repeat<br>● intra−intron other •<br>~25% of transcripts have<br>●<br>●<br>● ●●●●● ● ● ● ● ● light sequence coverage,<br>●<br>● and are fragments of full<br>●<br>transcripts<br>● ● ● ●<br>● ● ● ● ● ● ● ●●● ● ● ● ● ● ● ●●● ● ●●●●●●●●●●● ●●● ● ● ●● ● ● • Intronic reads, repeats, and<br>● ● ● ● ● ● ● ● ● ● ● ● ●●●●●●●●●● ● ● ● ● ● ● ● ● ● ● ● other artifacts are<br>● ● ●● ● ● ●●●●● ● ●●●●● ● ● ● ● ● ●● numerous, but account for<br>less than 5% of the<br>0.01 0.1 1 10 100 1000 10000<br>assembled reads.<br>0.01 0.1 1 10 100 1000 10000<br>Reads per bp<br>1.0<br>0.8<br>0.6<br>0.4<br>Transcripts (%)<br>0.2<br>0.0<br>50000<br>Transcripts<br>20000<br>0<br><!-- End of picture text -->

Courtesy of Cole Trapnell. Used with permission.


<!-- Start of picture text -->
Slide courtesy Cole Trapnell<br><!-- End of picture text -->

17

### Lecture 8 – RNA-seq Analysis

- RNA-seq principles – How can we characterize mRNA isoform expression using high-throughput sequencing?

- Differential expression and PCA – What genes are differentially expressed, and how can we characterize expressed genes?

- Single cell RNA-seq – What are the benefits and challenges of working with single cells for RNA-seq?

18


19


20


21


22


23

##### Scaling RNA-seq data (DESeq)

- i gene or isoform

- j sample (experiment)

- m number of samples

- Kij number of counts for isoform i in experiment j

- sj sampling depth for experiment j (scale factor)


<!-- Start of picture text -->
K<br>ij<br>s j =  median<br>i<br>1 m<br>m<br>∏ v =1 Kiv<br>( )<br><!-- End of picture text -->

24

##### Model for RNA-seq data (DESeq)

- i gene or isoform p condition

- j sample (experiment)        p(j)  condition of sample j

- m number of samples

- Kij number of counts for isoform i in experiment j

- qip  Average scaled expression for gene i condition p


<!-- Start of picture text -->
1<br>K<br>ij<br>q = ∑<br>ip<br># of replicates j in replicates s j<br>2<br>µ ij = qip (  j ) s j σ ij = µ ij + s 2 jv p ( qip (  j ))<br>2<br>K ij ~  NB (µ ij ,σ ij )<br><!-- End of picture text -->

25

#### 2 2 σ _ij_<sup>= µ</sup> _ij_<sup>+</sup> _s jv p_ (<sup>_q_</sup> _ip_ ( _j_ ))


**Orange Line – DESeq Dashed Orange – edgeR Purple - Poission**

Courtesy of the authors. License: CC-BY.

Source: Anders, Simon, and Wolfgang Huber. "Differential Expression Analysis for Sequence Count Data." _Genome Biology_ 11, no. 10 (2010): R106.


26

###### Significance of differential expression using test statistics

- Hypothesis H0 (null) – Condition A and B identically express isoform i with random noise added

- Hypothesis H1 – Condition A and B differentially express isoform

- Degrees of freedom (dof) is the number of free parameters in H1 minus the number of free parameters in H0; in this case degrees of freedom is 4 – 2 = 2  (H1 has an extra mean and variance).

• Likelihood ratio test defines a test statistic that follows the Chi Squared distribution _<u>K</u> iA_ | _H_ 1) _P_ <u>(</u> _<u>K</u> iB_ | _H_ 1) _T i_<sup>= 2log</sup><sup>_P_</sup><sup><u>(</u></sup> _P_ | _H_ 0 _K iA_<sup>,</sup> _K iB_ ( )

_P_ ( _H_ 0) ≈ 1− _ChiSquaredCDF_ ( _T i_ | _dof_ )

27

Courtesy of the authors. License: CC-BY.

Source: Anders, Simon, and Wolfgang Huber. "Differential Expression Analysis for Sequence Count Data." _Genome Biology_ 11, no. 10 (2010): R106.


28

###### Hypergeometric test for overlap significance

N – total # of genes n1 - # of genes in set A n2 - # of genes in set B k - # of genes in both A and B

1000 20 30 3


<!-- Start of picture text -->
! $! $<br>n 1 N  − n 1<br># &# & min( n 1, n 2)<br>k n 2 − k<br>" %" % P x  ≥ k ∑ P ( i )<br>( ) =<br>P ( k ) = i = k<br>! $<br>N<br># &<br>" n 2 %<br><!-- End of picture text -->

**0.017**

**0.020**

29


30


31


32


33


34


35

### Lecture 8 – RNA-seq Analysis

- RNA-seq principles – How can we characterize mRNA isoform expression using high-throughput sequencing?

- Differential expression and PCA – What genes are differentially expressed, and how can we characterize expressed genes?

- Single cell RNA-seq – What are the benefits and challenges of working with single cells for RNA-seq?

36


Courtesy of Fluidigm Corporation. Used with permission.

37

###### **Single-cell RNA-Seq of LPS-stimulated bone-marrow-derived dendritic cells reveals extensive transcriptome heterogeneity.**


**AK Shalek** **_et al. Nature_ 000, 1-5 (2012) doi:10.1038/nature12172**

Courtesy of Macmillan Publishers Limited. Used with permission.

Source: Shalek, Alex K., Rahul Satija, et al. "Single-cell Transcriptomics Reveals Bimodality in Expression and Splicing in Immune Cells." _Nature_ (2013).

38

###### **Analysis of co-variation in single-cell mRNA expression levels reveals distinct maturity states and an antiviral cell circuit.**


**AK Shalek** **_et al. Nature_ 000, 1-5 (2012) doi:10.1038/nature12172**

Courtesy of Macmillan Publishers Limited. Used with permission.

Source: Shalek, Alex K., Rahul Satija, et al. "Single-cell Transcriptomics Reveals Bimodality in Expression and Splicing in Immune Cells." _Nature_ (2013).

39

###### **Analysis of co-variation in single-cell mRNA expression levels reveals distinct maturity states and an antiviral cell circuit.**


**AK Shalek** **_et al. Nature_ 000, 1-5 (2012) doi:10.1038/nature12172**

Courtesy of Macmillan Publishers Limited. Used with permission.

Source: Shalek, Alex K., Rahul Satija, et al. "Single-cell Transcriptomics Reveals Bimodality in Expression and Splicing in Immune Cells." _Nature_ (2013).

40

###### RNA-seq library complexity can help qualify cells for analysis

###### **Michal Grzadkowski**

> © Michal Grzadkowski. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

41

###### RNA-seq library complexity can help qualify cells for analysis

###### **Michal Grzadkowski**

> © Michal Grzadkowski. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

42

# **FIN**

43

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Case study: myogenesis](02-case-study-myogenesis.md) · [Up: contents](index.md)
