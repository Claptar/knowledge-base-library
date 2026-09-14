---
title: Viterbi Example
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Viterbi Example

**Source:** `lectures/10-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### ACG

27

#### More Viterbi Examples

What is the optimal parse of the sequence for the CpG island HMM defined previously?

• (ACGT)10000

• A1000C80T1000C20A1000G60T1000

<u>Powers of 1.5:</u> N = 20 40 60 80 (1.5)<sup>N</sup> = 3x10<sup>3</sup> 1x10<sup>7</sup> 3x10<sup>10</sup> 1x10<sup>14</sup>

28

**Run time for k-state HMM on sequence of length L?**

O(k<sup>2</sup> L)

The computational efficiency of the Viterbi algorithm is a major reason for the popularity of HMMs

29

#### **Midterm Logistics**

Midterm 1 is **Tuesday, March 18th during regular class time/room*** Will start promptly at 1:05pm and end at 2:25pm - arrive in time to get settled

***except for 6.874 students who will meet at 12:40 PM.**

###### **Closed book, open notes:**

- you may bring **up to two pages** (double-sided) of notes if you wish No calculators or other electronic aids (you won’t need them anyway)

Study lecture notes, readings/tutorials and past exams/Psets 1st, textbook 2nd

Midterm exams from previous years are posted on course web site Note: there is some variation in topics from year to year

30

#### **Midterm 1**

**Exam will cover course topics from Topics 1, 2 and 3 through Hidden Markov Models (but will NOT cover RNA Secondary Structure)**

R Feb 06 CB L2 DNA Sequencing, Local Alignment (BLAST) and Statistics T Feb 11 CB L3 Global Alignment of Protein Sequences R Feb 13 CB L4 Comparative Genomic Analysis of Gene Regulation R Feb 20 DG L5 Library complexity and BWT

T Feb 25 DG L6 Genome assembly

- R Feb 27 DG L7 ChIP-Seq analysis (DNA-protein interactions) T Mar 04 DG L8 RNA-seq analysis (expression, isoforms)

R Mar 06 CB L9 Modeling & Discovery of Sequence Motifs T Mar 11 CB L10 Markov & Hidden Markov Models (+HMM content on 3/13)

Exam may have some overlap with topics from Pset 1+2 but will be biased towards topics NOT covered on PSets

There may be questions on algorithms, but none related to python or programming

31

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Notation for HMM Calculations](06-notation-for-hmm-calculations.md) · [Up: contents](index.md)
