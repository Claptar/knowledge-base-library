---
title: Peak-calling applications
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Peak-calling applications

**Source:** `recitations/2014-03-05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• ChIP-Seq

• MeDIP-Seq (Methylated DNA IP) – Finding methylated regions of DNA • CLIP-Seq (CrossLinking and ImmunoPrecipitation)

- Conceptually similar to ChIP-Seq, but for RNA instead of DNA

• MeRIP-Seq (aka M6A-Seq) – Post-transcriptional methylation of N6 position of adenosine in RNA

6

## GPS – genome positioning system

- Find binding sites of DNA binding proteins (e.g. transcription factors) that have sequence specificity (6-8 bp of preferred motifs)

   - ChIP-seq experiments help us understand how gene expression programs are regulated and how they change in development or in response to a stimulus

- In addition to ChIP with your antibody, perform a parallel set of experiments with everything the same except either with no antibody or a nonspecific (e.g. IgG) antibody

   - Whole cell extract

   - Negative control that represents the experimental background – only binding stronger than background is specifically due to your protein of interest binding

7

## GPS empirically estimates read distribution profiles


<!-- Start of picture text -->
0.01<br>0.005<br>+ strand<br>0<br>- strand<br>-0.005<br>-0.01<br>-400  -200  0  200  400<br>Location with respect to binding site<br>Read density<br><!-- End of picture text -->

-Each protein, read length, sequencing depth, etc. will have a slightly different binding profile, so it’s important to estimate this for each experiment

8

## GPS models every base _m_ in genome as a possible binding event


**Prob. of event m** 13 **Mixing prob.**

-On average, there are on the order of ~10,000 binding events. But genome size M is

~3 billion, so we want to force most to zero and only ~10,000 to be nonzero.

9


<!-- Start of picture text -->
N M M<br>Likelihood of<br>= =<br>observed reads  p ( R | π) π m p ( rn | m ,) π m 1<br>EM algorithm ∏∑ ∑<br>n =1 m =1 m =1<br><!-- End of picture text -->

- We want to maximize the probability of observing our reads – We can maximize this if there are binding events near the clusters of ChIPseq reads, since each of these reads will then individually have a relatively large probability of having been observed.

   - So maximizing this likelihood of observed reads is coupled to learning the distribution of binding events, π

   - We start out with no knowledge of π, and want to force most of its terms to 0 (component elimination) and learn the ~10,000 that are nonzero

- The EM (Expectation-Maximization) algorithm is an iterative method for finding the maximum likelihood (ML) estimates of parameters in statistical models, where the model depends on unobserved latent variables π = argmax _p_ ( _R_ | π )

   - What is the parameter to be estimated? π

      - Choose π to be that which (arg max) maximizes the likelihood of the ChIP-seq read set R


10

---

[← Announcements](01-announcements.md) · [Up: contents](index.md) · [EM algorithm →](03-em-algorithm.md)
