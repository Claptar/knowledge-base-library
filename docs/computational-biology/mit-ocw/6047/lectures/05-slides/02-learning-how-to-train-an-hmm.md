---
title: 'Learning: How to train an HMM'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Learning: How to train an HMM

**Source:** `lectures/05-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Transition probabilities** e.g. P(Pi+1|Bi) – the probability of entering a pathogenicity island from background DNA

**Emission probabilities** i.e. the nucleotide frequencies for background DNA and pathogenicity islands


<!-- Start of picture text -->
P(Li+1|Li)<br>B  P<br>P(S|B)  P(S|P)<br><!-- End of picture text -->

42

#### **Two learning scenarios**

Case 1. Estimation when the “right answer” is known

**<u>Examples:</u>** GIVEN: a genomic region x = x1…x1,000,000 where we have good (experimental) annotations of the CpG islands

Case 2. Estimation when the “right answer” is unknown

**<u>Examples:</u>**

GIVEN:

the porcupine genome; we don’t know how frequent are the CpG islands there, neither do we know their composition

**QUESTION:**

Update the parameters  of the model to maximize P(x|)

43

#### **Two types of learning:  Supervised / Unsupervised**

###### **5. Supervised learning**

infer model parameters given **labeled** training data – GIVEN:

   - a HMM M, with unspecified transition/emission probs.

   - labeled sequence x,

- FIND:

   - parameters  = (Ei, Aij) that maximize P[ x |  ]

- Simply count frequency of each emission and transition, as observed in the training data

###### **6. Unsupervised learning**

- infer model parameters given **unlabelled** training data – GIVEN:

   - a HMM M, with unspecified transition/emission probs.

   - unlabeled sequence x,

- FIND:

   - parameters  = (Ei, Aij) that maximize P[ x |  ]

- Viterbi training:

guess parameters, find optimal Viterbi path (#2), update parameters (#5), iterate  Baum-Welch training:

guess parameters, sum over all paths (#4), update parameters (#5), iterate

44

#### **5: Supervised learning**

Estimate model parameters based on **labeled** training data

45

#### **Case 1.**

#### **When the right answer is known**

Given x = x1…xN for which the true  = 1…N is known, **<u>Define:</u>**

Akl Ek(b)

- = # times kl transition occurs in 

- = # times state k in  emits b in x

We can show that the maximum likelihood parameters  are:

Akl

> <sup>E</sup> k<sup>(b)</sup>

akl = **–––––** i  Aki

ek(b) =   –––––––

c Ek(c)

46

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Learning From Labelled Data  Maximum Likelihood Estimation →](03-learning-from-labelled-data-maximum-likelihood-estimation.md)
