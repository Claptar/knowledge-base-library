---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/07-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 7 ChIP-seq Analysis Irreproducible Discovery Rate (IDR) Analysis Foundations of Computational Systems Biology David K. Gifford

1

###### Transcription factors regulate gene expression

© Emw on wikipedia. Some rights reserved. License: CC-BY-SA. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

###### **Transcription factors are proteins that bind to specific DNA sequences and act as molecular switches (Pit1 shown)**

**Humans have ~2000 gene regulators.**

2

###### Gene Regulation: DNA -> RNA -> Protein�


<!-- Start of picture text -->
Regulators<br><!-- End of picture text -->

**Gene**


<!-- Start of picture text -->
TFIIH<br><!-- End of picture text -->


<!-- Start of picture text -->
mRNA<br>Protein<br><!-- End of picture text -->

**What are the gene regulators that control gene expression? At what genes do these regulators operate?**

3

###### Gene regulatory networks provide key insight into cellular function�

###### **Transcriptional regulatory network information will:**

- **reveal how cellular processes**

- **are connected and coordinated**

- **suggest new strategies to**

- **manipulate phenotypes and combat disease**


Courtesy of Richard Young. Used with permission.

4

###### ChIP-seq data reveals where TFs bind to the genome�


<!-- Start of picture text -->
Regulators  Gene<br>TFIIH<br>mRNA<br>ChIP-seq data<br>Protein<br><!-- End of picture text -->

5

###### ChIP-seq protocol


**Enrich for proteinbound DNA fragments with antibodies**


**Sequence ChIP DNA**

**Sequence whole cell extract (WCE) DNA (control)**

**Crosslink Harvest cells proteins to and fragment binding sites DNA in living cells**

6

###### A binding event produces a distribution of reads around its site


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Kharchenko, Peter V., Michael Y. Tolstorukov, et al. "Design and Analysis of ChIP-seq Experiments for DNA-binding Proteins." _Nature biotechnology_ 26, no. 12 (2008): 1351-9.

7

###### Data from two binding events mES cell Oct4 ChIP Seq


8

������������������������������������������������ ������������������������������������������� ���������������������������������


**ChIP-Seq reads are independently generated from a set of spatially discrete binding events**

9

##### GPS addresses the challenges in ChIP-Seq analysis


###### **ChIP DNA are randomly fragmented**

**Mixture of Reads from different events**


###### **Model the spatial distribution of the reads Construct a mixture model**

Courtesy of Wang and Zhang. Licensed CC-BY.

Source: Wang, Xi, and Xuegong Zhang. "Pinpointing Transcription Factor Binding Sites from ChIP-seqData with SeqSite." _BMC Systems Biology_ 5, no. Suppl 2 (2011): S3.

10

###### GPS estimates the spatial distribution of the reads


<!-- Start of picture text -->
0.01<br>0.005<br>+ strand<br>0<br>- strand<br>-0.005<br>-0.01<br>-400 -200 0 200 400<br>Location with respect to binding site<br>yti<br>Read dens<br><!-- End of picture text -->

11

###### GPS estimates the spatial distribution of the reads

**Si = 0 for forward strand = 1 for reverse strand**

12

GPS probabilistically models ChIP-Seq read spatial distribution using a mixture model (single-base resolution)


<!-- Start of picture text -->
1 2<br>M  Possible<br>events<br>m<br>N  Observed rn<br>reads<br>N M M<br>Likelihood of<br>observed reads  p ( R  | π) = ∏∑π m p ( r n |  m ), ∑π  m  = 1<br>n =1  m =1 m =1<br><!-- End of picture text -->

**Prob. of event m Mixing prob.**


13

_N M M_ **Likelihood of observed reads** _p_ ( _R_ | π ) = ∏∑π _m p_ ( _rn_ | _m_ ), ∑π _m_ = 1 _n_ =1 _m_ =1 _m_ =1 **Read assignment is latent** _g_ ( _zn_ = _m_ ) = 1 **Read n came from event m** π = argmax _p_ ( _R_ | π) **Read n did not come from** π _g_ ( _zn_ = _m_ ) = 0 **event m Expectation-Maximization (EM) algorithm with component elimination E step M step** _m_ π _<u>m p</u>_<sup><u>(</u></sup> _rn_<sup><u>|</u></sup> <u>)</u> _Nm_ γ( _zn_ = _m_ ) = _M_ πˆ _m_ ( _i_ ) = ∑ _mM_ '=1 _Nm_ ' ∑<sup>π</sup> _m_ '<sup>_p_(</sup><sup>_r_</sup> _n_<sup>|</sup><sup>_m_')</sup> _N m_ '=1 _Nm_ = ∑ _n_ =1<sup>γ(</sup><sup>_z_</sup> _n_<sup>=</sup><sup>_m_)</sup> **_γ (zn=m) :_ the fraction of read** **_Nm_ : the effective number of** **_n_ assigned to event** **_m_ reads assigned to event** **_m_**

14

###### **Expectation-Maximization (EM) algorithm with component elimination**

**Initialization Strength of binding event at end** 1 _N_ π _j_<sup>=</sup> _Nm_ = ∑ _n_ =1<sup>γ(</sup><sup>_z_</sup> _n_<sup>=</sup><sup>_m_)</sup> _M_ **_Nm_ : the effective number of reads assigned to event** **_m_**

###### **Expectation-Maximization (EM) algorithm with component elimination**


<!-- Start of picture text -->
E step M step<br>γ( zn = m ) = M π m p ( rn | m ) πˆ m ( i ) = ∑ mMN '=1 m N m '<br>π ' r m<br>m p ( n | )'<br>∑<br>m '=1 N<br>Nm  = ∑ n =1 γ( z n =  m )<br>γ (zn=m) :  the fraction of read  Nm  : the effective number of<br>n  assigned to event  m reads assigned to event  m<br><!-- End of picture text -->

15

Synthetic data, EM, no prior (events at 500 and 550 bp)


16

###### GPS deconvolves homotypic events and improves spatial accuracy


**Example of a predicted joint CTCF event that contains coordinately located CTCF motifs**

22


<!-- Start of picture text -->
N M M<br>Likelihood of<br>observed reads  p ( R  | π ) = ∏∑π m p ( rn  |  m ), ∑π m = 1<br>n =1 m =1 m =1<br>A sparse prior  on mixture components (binding events)<br>M 1<br>π ∝ α > 0<br>p ( ) ,<br>α<br>∏<br>m =1 (π m ) (Figueiredo and Jain, 2002)<br><!-- End of picture text -->


<!-- Start of picture text -->
Expectation-Maximization (EM) algorithm with component elimination<br>E step M step<br>−<br>ˆ ( i ) max(0, N m α)<br>π m p ( rn |  m ) π =<br>m M<br>γ ( zn =  m ) = M<br>−<br>∑ m '=1max(,0 N m ' α)<br>∑ π m ' p ( r n |  m ')<br>N<br>m '=1<br>N m = ∑ n =1γ( zn = m )<br>γ (zn=m) :  the fraction of read  Nm  : the effective number of<br>n  assigned to event  m reads assigned to event  m<br><!-- End of picture text -->

18

Synthetic data, EM, sparse prior (events at 500 and 550 bp)


19


<!-- Start of picture text -->
EM –<br>Sparse<br>prior<br><!-- End of picture text -->

20


21

###### GPS deconvolves homotypic events and improves spatial accuracy


**Example of a predicted joint CTCF event that contains coordinately located CTCF motifs**

22

###### mES cell Oct4 ChIP Seq


23

###### We compute a p-value with a binomial test for significance

###### Null Model –

F(k,n,P) - Probability n-k reads observed in IP channel by chance with k reads observed in control.   P = 0.5 equal chance reads occurred in control and IP channels for null model.


24

We determine significant events by Benjamini Hochberg at a desired false discovery rate (FDR)


_Rank:_ Rank of event in list list of p-values, from most significant (rank = 1) to least (rank = Count) Accept events (reject null) of rank = 1 .. k up to the point that the Q-value is greater than the desired FDR.

25

###### Irreproducible Discovery Rate (IDR) Analysis

- We have two replicates of an experiment

- How do we choose events are consistent in the two replicates?

26

Spearman’s rank correlation provides a metric for replicate consistency but does not select events

- Consider two ranked lists of n detected events X and Y, one from each replicate, each ranked by scores from most significant to least significant.

- For matched event i ranks are xi and yi in X and Y


27

###### Irreproducible Discovery Rate (IDR) Analysis

- Ψn(t) is the fraction of the n events that are paired in the top n*t events in both X and Y It is roughly linear from t=0 to the point when events are no longer reproducible (not shared between replicates within the ranking)

- Ψ�n(t) is first derivative of Ψn(t) with respect to t. It allows us to visualize when we transition from reproducible to irreproducible events as t increases

28

###### Irreproducible Discovery Rate (IDR) Analysis

Courtesy of Institute of Mathematical Statistics. Used with permission. Source: Li, Qunhua, James B. Brown, et al. "Measuring Reproducibility of High-throughput Experiments." _The Annals of Applied Statistics_ 5, no. 3 (2011): 1752-79.


29

###### Irreproducible Discovery Rate (IDR) Analysis

- Consider that the lists X and Y are a mixture of two kinds of events – reproducible and irreproducible.

- Model the ranking scores as a two component mixture and learn the parameters of the reproducible and irreproducible components

- For IDR α, select top l pairs using their scores such that the probability that the rate of pairs from the irreproducible part of the mixture is α

30

###### Irreproducible Discovery Rate Results


Courtesy of Institute of Mathematical Statistics. Used with permission. Source: Li, Qunhua, James B. Brown, et al. "Measuring Reproducibility of High-throughput Experiments." _The Annals of Applied Statistics_ 5, no. 3 (2011): 1752-79.


31

##### **G** enome-wide **E** vent finding and **M** otif discovery


<!-- Start of picture text -->
ChIP-Seq  DNA<br>Reads  Sequences<br>Biases binding event<br>predictions towards<br>2<br>G E M<br>motif positions<br>Event   Motif<br>finding   discovery<br>Bias motif<br>1<br>discovery towards<br>binding sites<br>Binding events and<br>explanatory DNA motifs<br><!-- End of picture text -->

32

---

[Up: contents](index.md) · [Motif-based positional prior biases the binding event prediction →](02-motif-based-positional-prior-biases-the-binding-event-predic.md)
