---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/10-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

7.91 / 20.490 / 6.874 / HST.506 7.36 / 20.390 / 6.802 C. Burge Lecture #10 March 11, 2014

Markov & Hidden Markov Models of Genomic & Protein Features

1

###### **Modeling & Discovery of Sequence Motifs**

- Motif Discovery with Gibbs Sampling Algorithm

- Information Content of a Motif

- Parameter Estimation for Motif Models (+ others)

2

Relative Entropy* _<u>p</u>_ _~~k~~_ ) Relative entropy, D(p||q) = mean bit-score: ∑ _n pk_ log 2 ~~(~~ _k_ =1 _qk If_ qk =<sup>1</sup> _then_ mean bit-score = RelEnt = 2w - Hmotif = Imotif 4 _w_

RelEnt is a measure of **information** , not entropy/uncertainty. In general RelEnt is different from Hbefore - Hafter and is a better measure when background is non-random

Example: qA = qT = 3/8, qC = qG = 1/8 Suppose: pC = 1. H(q) - H(p) < 2

But RelEnt D(p||q) = log2(1/(1/8)) = 3 bits Which one better describes frequency of C in background seq?

* Alternate names: “Kullback-Leibler distance”, “information for discrimination”

3

###### **Position-specific probability matrix (PSPM)**


<!-- Start of picture text -->
5' Splice Site Motif:<br>Pos  -3  -2  -1 +1 +2 +3 +4 +5 +6<br>A  0.3  0.6  0.1  0.0  0.0  0.4  0.7  0.1  0.1<br> C  0.4  0.1  0.0  0.0  0.0  0.1  0.1  0.1  0.2<br> G  0.2  0.2  0.8  1.0  0.0  0.4  0.1  0.8  0.2<br>T  0.1  0.1  0.1  0.0  1.0  0.1  0.1  0.0  0.5<br>Ex:  TAGGTCAGT<br>S = S1 S2 S3 S4 S5 S6 S7 S8 S9<br>P(S|+) = P-3(S1)P-2(S2)P-1(S3) ••• P5(S8)P6(S9)<br><!-- End of picture text -->

‘Inhomogeneous’, assumes independence between positions **What if this is not true?**

4


<!-- Start of picture text -->
Inhomogeneous 1st-Order<br>Markov Model<br>-3 -2 -1 1 2 3 4 5 6<br>(−3,−2)<br>N CA<br>(−3)<br>P-2(A |C) =  N C<br>-3 -2  -1  1  2  3  4  5  6<br>S = S1 S2 S3 S4 S5 S6 S7 S8 S9<br>Inhomogeneous<br>P(S|+) = P-3(S1)P-2(S2 |S1)P-1(S3 |S2) ••• P6(S9 |S8)<br>R =<br>P(S|-) = Pbg(S1)Pbg(S2 |S1)Pbg(S3 |S2) ••• Pbg(S9 |S8)<br>Homogeneous<br>s = log2R<br><!-- End of picture text -->

5

### WMM vs 1st-order Markov Models of Human 5’ss


<!-- Start of picture text -->
Decoy 5’ss<br>True<br>WMM<br> 5’ss<br>WMM 5’ss Score<br>Decoy 5’ss<br>True<br>Markov   5’ss<br>I1M 5’ss Score<br><!-- End of picture text -->

Markov models also improve modeling of transcriptional motifs - Zhou & Liu Bioinformatics 2004

- © sources unknown. All rights reserved. This content is excluded from our Creative Commons license. or more information, see http://ocw.mit.edu/help/faq-fair-use/.

6

###### **Estimating Parameters for a Markov Model**


<!-- Start of picture text -->
-3 -2 -1 1 2 3 4 5 6<br>(−3,−2)<br>N CA<br>(−3)<br>P-2(A |C) =  N C<br>-3  -2  -1  1  2  3  4  5  6<br>What about longer-range dependence?<br>• k-order Markov model<br>- next base depends on previous k bases<br>2 nd -order Markov model<br>Parameters per position for Markov model of order k:  ~4 k+1<br><!-- End of picture text -->

7

#### **Dealing With Limited Training Sets**

Position: <u>1 2 3 4 5</u> `A 8 C 1 G 1 T 0` If the true frequency of T at pos. 1 was 10%, what’s the probability we wouldn’t see any Ts in a sample of 10 seqs? P(N=0) = (10!/0!10!)(0.1)<sup>0</sup> (0.9)<sup>10</sup> = ~35% Motivates adding “pseudocounts”

**Training Set** ACCTG AGCTG ACCCG ACCTG ACCCA GACTG ACGTA ACCTG CCCCG ACATC

8

---

[Up: contents](index.md) · [Pseudocounts ( Ψ counts) →](02-pseudocounts-ψ-counts.md)
