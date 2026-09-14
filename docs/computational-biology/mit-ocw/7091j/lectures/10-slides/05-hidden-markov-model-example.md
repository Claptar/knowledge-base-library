---
title: Hidden Markov Model Example
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Hidden Markov Model Example

**Source:** `lectures/10-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
Grandpa<br>Genotype  Phenotype -<br>Simpson  (hidden)  LDL cholesterol<br>(observed)<br>A/a<br>150<br>Suppose that we can’t observe genotype directly,<br>only some phenotype related to the A locus, and<br>this phenotype depends probabilistically on the<br>Homer<br>genotype.  Then we have a Hidden Markov Model.<br>a/a<br>250<br>a/a<br>A/a<br>Probability<br>100 150  200  250 300<br>a/a<br>          LDL cholesterol<br>200<br>Bart<br><!-- End of picture text -->

Images of The Simpsons © FOX. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

13

### HMMs as Generative Models


An HMM

From Rabiner Tutorial

14

##### “Sequence Labeling” Problems

Example: Bacterial gene finding


<!-- Start of picture text -->
Open Reading Frame<br>Start  Stop<br>ORF  ORF<br><!-- End of picture text -->

accgatattcaaccatggagagtttatccggtatagtcgcccctaaataccgtagaccttgagagactgactcatgacgtagtcttacggatctaggggcatatccctagaggtacgg... Gene 1 Gene 2 ...

15

# CpG Islands


<!-- Start of picture text -->
%C+G<br><!-- End of picture text -->


<!-- Start of picture text -->
60<br>50<br>40<br>30<br><!-- End of picture text -->

- Regions of high C+G content and relatively high abundance of CpG dinucleotides (normally rare) which are unmethylated

• Associated with promoters of many human genes (~ 1/2)

16

#### CpG Island Hidden Markov Model


<!-- Start of picture text -->
Pig<br>Pgg  Pii<br>Hidden<br>Genome<br>Island<br>Pgi<br>…<br>A  C T C G  A  G T  A<br>Observable<br><!-- End of picture text -->

17


<!-- Start of picture text -->
“Initiation<br>Rabiner notation<br>CpG Island HMM<br>probabilities” πj<br>Pgg = 0.99999 Pig = 0.001<br>Pg = 0.99, Pi = 0.01<br>Genome<br>Pii = 0.999<br>“Transition<br>probabilities” aij Pgi = 0.00001 Island<br>…<br>A      C       T       C       G      A       G      T       A<br> C  G  A  T<br>“Emission<br>Probabilities” bj(k) CpG Island:  0.3  0.3  0.2  0.2<br>Genome: 0.2  0.2  0.3  0.3<br><!-- End of picture text -->

18

CpG Island HMM III <mark>Want to infer</mark>


… A      C        T       C       G       A       G        T       A Observe But HMM is written in the other direction (observable depends on hidden)

19

### Reversing the Conditioning (Bayes’ Rule)

Definition of Conditional Probability: P(A|B) = P(A,B) / P(B)

Bayes’ Rule (simple form) P(B|A) = P(B)P(A|B) / P(A)

Bayes’ Rule (more general form)

- P(Bi|A) = P(Bi)P(A|Bi)

Σ P(Bk) P(A|Bk) k

20

---

[← Markov Model Example](04-markov-model-example.md) · [Up: contents](index.md) · [Notation for HMM Calculations →](06-notation-for-hmm-calculations.md)
