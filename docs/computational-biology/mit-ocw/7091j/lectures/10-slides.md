---
title: 10 slides
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/10-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 10 slides

7.91 / 20.490 / 6.874 / HST.506
7.36 / 20.390 / 6.802

C. Burge Lecture #10

March 11, 2014

## Markov & Hidden Markov Models of Genomic & Protein Features

---

## Modeling & Discovery of Sequence Motifs

• Motif Discovery with Gibbs Sampling Algorithm

• Information Content of a Motif

• Parameter Estimation for Motif Models (+ others)

---

## Relative Entropy*

Relative entropy, $\text{D}(p||q) = \text{mean bit-score}$: $\sum_{k=1}^{n} p_k \log_2 \left(\frac{p_k}{q_k}\right)$

*If* $q_k = \frac{1}{4^w}$ *then* $\text{mean bit-score} = \text{RelEnt} = 2w - H_{\text{motif}} = I_{\text{motif}}$

RelEnt is a measure of **information**, not entropy/uncertainty.
In general RelEnt is different from $H_{\text{before}} - H_{\text{after}}$ and is a better
measure when background is non-random

Example: $q_A = q_T = 3/8$, $q_C = q_G = 1/8$

Suppose: $p_C = 1$. $H(q) - H(p) < 2$

But RelEnt $\text{D}(p||q) = \log_2(1/(1/8)) = 3\text{ bits}$

Which one better describes frequency of C in background seq?

\* Alternate names: "Kullback-Leibler distance", "information for discrimination"

---

## Position-specific probability matrix (PSPM)

5' Splice Site Motif:

| Pos | -3 | -2 | -1 | +1 | +2 | +3 | +4 | +5 | +6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A | 0.3 | 0.6 | 0.1 | 0.0 | 0.0 | 0.4 | 0.7 | 0.1 | 0.1 |
| C | 0.4 | 0.1 | 0.0 | 0.0 | 0.0 | 0.1 | 0.1 | 0.1 | 0.2 |
| G | 0.2 | 0.2 | 0.8 | 1.0 | 0.0 | 0.4 | 0.1 | 0.8 | 0.2 |
| T | 0.1 | 0.1 | 0.1 | 0.0 | 1.0 | 0.1 | 0.1 | 0.0 | 0.5 |

**Ex: TAGGTCAGT**
$S = S_1 S_2 S_3 S_4 S_5 S_6 S_7 S_8 S_9$

$P(S|+) = P_{-3}(S_1)P_{-2}(S_2)P_{-1}(S_3) \cdots P_5(S_8)P_6(S_9)$

'Inhomogeneous', assumes independence between positions

**What if this is not true?**

---

## Inhomogeneous 1st-Order Markov Model

-3 -2 -1 1 2 3 4 5 6

$$P_{-2}(A|C) = \frac{N_{CA}^{(-3,-2)}}{N_C^{(-3)}}$$

-3 $\rightarrow$ -2 $\rightarrow$ -1 $\rightarrow$ 1 $\rightarrow$ 2 $\rightarrow$ 3 $\rightarrow$ 4 $\rightarrow$ 5 $\rightarrow$ 6

$S = S_1 S_2 S_3 S_4 S_5 S_6 S_7 S_8 S_9$

$$R = \frac{P(S|+) = P_{-3}(S_1)P_{-2}(S_2|S_1)P_{-1}(S_3|S_2) \cdots P_6(S_9|S_8)}{P(S|-) = P_{bg}(S_1)P_{bg}(S_2|S_1)P_{bg}(S_3|S_2) \cdots P_{bg}(S_9|S_8)}$$

Inhomogeneous (numerator)
Homogeneous (denominator)

$$s = \log_2 R$$

---

## WMM vs 1st-order Markov Models of Human 5'ss

**Decoy 5'ss**
**True 5'ss**
**WMM**
WMM 5'ss Score

**Decoy 5'ss**
**Markov**
**True 5'ss**
I1M 5'ss Score

Markov models also improve modeling of transcriptional motifs - Zhou & Liu Bioinformatics 2004

---

## Estimating Parameters for a Markov Model

-3 -2 -1 1 2 3 4 5 6

$$P_{-2}(A|C) = \frac{N_{CA}^{(-3,-2)}}{N_C^{(-3)}}$$

-3 $\rightarrow$ -2 $\rightarrow$ -1 $\rightarrow$ 1 $\rightarrow$ 2 $\rightarrow$ 3 $\rightarrow$ 4 $\rightarrow$ 5 $\rightarrow$ 6

What about longer-range dependence?

• k-order Markov model
- next base depends on previous k bases
$2^{\text{nd}}$-order Markov model

Parameters per position for Markov model of order k: $\sim 4^{k+1}$

---

## Dealing With Limited Training Sets

| Position: | 1 | 2 | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| A | 8 | | | | |
| C | 1 | | | | |
| G | 1 | | | | |
| T | 0 | | | | |

If the true frequency of T at pos. 1 was 10%, what's the probability we wouldn't see any Ts in a sample of 10 seqs?

$$P(N=0) = (10!/0!10!)(0.1)^0(0.9)^{10} = \sim 35\%$$

Motivates adding "pseudocounts"

**Training Set**
ACCTG
AGCTG
ACCCG
ACCTG
ACCCA
GACTG
ACGTA
ACCTG
CCCCG
ACATC

---

## Pseudocounts ($\Psi$counts)

| Nt | Count | $\Psi$count | Bayescount | ML est. | Bayes est. |
| :---: | :---: | :---: | :---: | :---: | :---: |
| A | 8 | + 1 | 9 | 0.80 | 0.64 |
| C | 1 | + 1 | 2 | 0.10 | 0.14 |
| G | 1 | + 1 | 2 | 0.10 | 0.14 |
| T | 0 | + 1 | 1 | 0.00 | 0.07 |
| | 10 | | 14 | 1.00 | 1.00 |

ML = maximum likelihood (of generating the observed data)

Bayes est. = Bayesian posterior relative to Dirichlet prior

Good treatment of this in appendix of:
*Biological Sequence Analysis* by Durbin, Eddy, Krogh, Mitchison
See also: Probability and Statistics Primer (under Materials > Resources)

---

## Hidden Markov Models of Genomic & Protein Features

• Hidden Markov Model terminology

• Viterbi algorithm

• Examples
- CpG Island HMM
- TMHMM (transmembrane helices)

Background reading for today's lecture:
NBT Primer on HMMs, Z&B Chapter 6, Rabiner tutorial on HMMs

For Thursday's lecture:
NBT Primer on RNA folding, Z&B Ch. 11.9

---

## Hidden Markov Models (HMMs)

• Provide a foundation for probabilistic models of linear sequence 'labeling' problems

• Can be designed just by drawing a graph diagram

• The 'Legos' of computational sequence analysis

Developed in Electrical Engineering for applications to voice recognition

Read Rabiner's "Tutorial on hidden Markov models with applications ..."

---

## Markov Model Example

Genotype at the Apolipoprotein locus (alleles A and a) in successive generations of boxed Simpson lineage forms a Markov model

Grandpa Simpson (Past)
$\downarrow$
Grandma Simpson
Homer (Present)
$\downarrow$
Marge
Bart (Future)

This is because, e.g., Bart's genotype is conditionally independent of Grandpa Simpson's genotype given Homer's genotype:

$$P(\text{Bart} = a/a \mid \text{Grandpa} = A/a \ & \ \text{Homer} = a/a) = P(\text{Bart} = a/a \mid \text{Homer} = a/a)$$

---

## Hidden Markov Model Example

| | Genotype (hidden) | Phenotype - LDL cholesterol (observed) |
| :--- | :---: | :---: |
| Grandpa Simpson | $A/a$ | 150 |
| Homer | $a/a$ | 250 |
| Bart | $a/a$ | 200 |

Suppose that we can't observe genotype directly, only some phenotype related to the A locus, and this phenotype depends probabilistically on the genotype. **Then we have a Hidden Markov Model.**

---

## HMMs as Generative Models

An HMM can be used as a generator to give an observation sequence

$$O = O_1 O_2 \cdots O_T \tag{10}$$

(where each observation $O_t$ is one of the symbols from $V$, and $T$ is the number of observations in the sequence) as follows:

1) Choose an initial state $q_1 = S_i$ according to the initial state distribution $\pi$.
2) Set $t = 1$.
3) Choose $O_t = v_k$ according to the symbol probability distribution in state $S_i$, i.e., $b_i(k)$.
4) Transit to a new state $q_{t+1} = S_j$ according to the state transition probability distribution for state $S_i$, i.e., $a_{ij}$.
5) Set $t = t + 1$; return to step 3) if $t < T$; otherwise terminate the procedure.

From Rabiner Tutorial

---

## "Sequence Labeling" Problems

Example: Bacterial gene finding

Open Reading Frame: Start $\rightarrow$ ORF $\rightarrow$ Stop

accgatattcaaccatggagagtttatccggtatagtcgcccctaaataccgtagaccttgagagactgactcatgacgtagtcttacggatctaggggcatatccctagaggtacgg...

Gene 1 | Gene 2 ...

---

## CpG Islands

%C+G

• Regions of high C+G content and relatively high abundance of CpG dinucleotides (normally rare) which are unmethylated

• Associated with promoters of many human genes (~ 1/2)

---

## CpG Island Hidden Markov Model

Hidden: Genome ($P_{gg}$, $P_{gi}$), Island ($P_{ii}$, $P_{ig}$)

Observable: A C T C G A G T A

---

## CpG Island HMM

Rabiner notation

"Initiation probabilities" $\pi_j$:
$P_g = 0.99$, $P_i = 0.01$

"Transition probabilities" $a_{ij}$:
Genome $\rightarrow$ Genome: $P_{gg} = 0.99999$
Genome $\rightarrow$ Island: $P_{gi} = 0.00001$
Island $\rightarrow$ Genome: $P_{ig} = 0.001$
Island $\rightarrow$ Island: $P_{ii} = 0.999$

"Emission Probabilities" $b_j(k)$:

| | C | G | A | T |
| :--- | :---: | :---: | :---: | :---: |
| **CpG Island:** | 0.3 | 0.3 | 0.2 | 0.2 |
| **Genome:** | 0.2 | 0.2 | 0.3 | 0.3 |

Sequence: A C T C G A G T A

---

## CpG Island HMM III

Want to infer (hidden states)
Observe (A C T C G A G T A)

But HMM is written in the other direction (observable depends on hidden)

---

## Reversing the Conditioning (Bayes' Rule)

Definition of Conditional Probability:
$$P(A|B) = P(A,B) / P(B)$$

Bayes' Rule (simple form)
$$P(B|A) = P(B)P(A|B) / P(A)$$

Bayes' Rule (more general form)
$$P(B_i|A) = \frac{P(B_i)P(A|B_i)}{\sum_k P(B_k) P(A|B_k)}$$

---

## Notation for HMM Calculations

$$P(H = h_1,\ldots,h_n, O = o_1,\ldots,o_n)$$
- Random vector of hidden states: $H$
- Specific hidden state values: $h_1,\ldots,h_n$
- Random vector of observable data (DNA bases): $O$
- Specific sequence of bases: $o_1,\ldots,o_n$

$$P(H = h'_1,\ldots,h'_n, O = o_1,\ldots,o_n)$$
- Another specific set of hidden state values: $h'_1,\ldots,h'_n$

---

## Reversing the Hidden/Observable Conditioning (Bayes' Rule)

Conditional Prob:
$$P(A|B) = P(A,B)/P(B)$$

$$P(H = h_1, h_2, \ldots, h_n \mid O = o_1, o_2, \ldots, o_n) = \frac{P(H = h_1, \ldots, h_n, O = o_1, \ldots, o_n)}{P(O = o_1, \ldots, o_n)}$$

$$= \frac{P(H = h_1, \ldots, h_n)P(O = o_1, \ldots, o_n \mid H = h_1, \ldots, h_n)}{P(O = o_1, \ldots, o_n)}$$

$P(O = o_1, \ldots, o_n)$ a bit tricky to calculate, but is independent of $h_1, \ldots, h_n$ so can treat as a constant and simply maximize

$$P(H = h_1, \ldots, h_n, O = o_1, \ldots, o_n)$$

---

## Inferring the Hidden from the Observable (Viterbi Algorithm)

Want to find sequence of hidden states $H^{opt} = h_1^{opt}, h_2^{opt}, h_3^{opt}, \ldots$ that maximizes joint probability:

$$P(H = h_1, \ldots, h_n, O = o_1, \ldots, o_n)$$

(optimal "parse" of sequence)

**Solution:**

Define $R_i^{(h)} =$ probability of optimal parse of the subsequence $1..i$ ending in state $h$

Solve **recursively**, i.e. determine $R_2^{(h)}$ in terms of $R_1^{(h)}$, etc.

---

Andrew Viterbi, an MIT BS/MEng student in E.E. - founder of Qualcomm

---

## CpG Island HMM

Rabiner notation

"Initiation probabilities" $\pi_j$:
$P_g = 0.99$, $P_i = 0.01$

"Transition probabilities" $a_{ij}$:
Genome $\rightarrow$ Genome: $P_{gg} = 0.99999$
Genome $\rightarrow$ Island: $P_{gi} = 0.00001$
Island $\rightarrow$ Genome: $P_{ig} = 0.001$
Island $\rightarrow$ Island: $P_{ii} = 0.999$

"Emission Probabilities" $b_j(k)$:

| | C | G | A | T |
| :--- | :---: | :---: | :---: | :---: |
| **CpG Island:** | 0.3 | 0.3 | 0.2 | 0.2 |
| **Genome:** | 0.2 | 0.2 | 0.3 | 0.3 |

Sequence: A C T C G A G T A

---

$\delta_t(i)$ probability of optimal parse of the subsequence $1..t$ ending in state $i$
$\psi_t(i)$ the state at $t-1$ that resulted in the optimal parse of $1..t$ ending in $i$

$N$ no. of states
$T$ length of sequence

## Viterbi Algorithm

1) Initialization:
   $$\delta_1(i) = \pi_i b_i(O_1), \quad 1 \le i \le N \tag{32a}$$
   $$\psi_1(i) = 0. \tag{32b}$$

2) Recursion:
   $$\delta_t(j) = \max_{1 \le i \le N} [\delta_{t-1}(i) a_{ij}] b_j(O_t), \quad 2 \le t \le T, \; 1 \le j \le N \tag{33a}$$
   $$\psi_t(j) = \operatorname{argmax}_{1 \le i \le N} [\delta_{t-1}(i) a_{ij}], \quad 2 \le t \le T, \; 1 \le j \le N. \tag{33b}$$

3) Termination:
   $$P^* = \max_{1 \le i \le N} [\delta_T(i)] \tag{34a}$$
   $$q_T^* = \operatorname{argmax}_{1 \le i \le N} [\delta_T(i)]. \tag{34b}$$

4) Path (state sequence) backtracking:
   $$q_t^* = \psi_{t+1}(q_{t+1}^*), \quad t = T - 1, T - 2, \cdots, 1. \tag{35}$$

Rabiner 1989

---

## Viterbi Example

ACG

---

## More Viterbi Examples

What is the optimal parse of the sequence for the CpG island HMM defined previously?

• $(\text{ACGT})_{10000}$

• $\text{A}_{1000}\text{C}_{80}\text{T}_{1000}\text{C}_{20}\text{A}_{1000}\text{G}_{60}\text{T}_{1000}$

**Powers of 1.5:**

| $N =$ | 20 | 40 | 60 | 80 |
| :--- | :---: | :---: | :---: | :---: |
| $(1.5)^N =$ | $3 \times 10^3$ | $1 \times 10^7$ | $3 \times 10^{10}$ | $1 \times 10^{14}$ |

---

## Run time for k-state HMM on sequence of length L?

$$O(k^2L)$$

The computational efficiency of the Viterbi algorithm is a major reason for the popularity of HMMs

---

## Midterm Logistics

Midterm 1 is **Tuesday, March 18th during regular class time/room\***

Will start promptly at 1:05pm and end at 2:25pm - arrive in time to get settled

**\*except for 6.874 students who will meet at 12:40 PM.**

**Closed book, open notes:**
- you may bring **up to two pages** (double-sided) of notes if you wish
No calculators or other electronic aids (you won't need them anyway)

Study lecture notes, readings/tutorials and past exams/Psets 1st, textbook 2nd

Midterm exams from previous years are posted on course web site
Note: there is some variation in topics from year to year

---

## Midterm 1

**Exam will cover course topics from Topics 1, 2 and 3 through Hidden Markov Models (but will NOT cover RNA Secondary Structure)**

R Feb 06 CB L2 DNA Sequencing, Local Alignment (BLAST) and Statistics
T Feb 11 CB L3 Global Alignment of Protein Sequences
R Feb 13 CB L4 Comparative Genomic Analysis of Gene Regulation
R Feb 20 DG L5 Library complexity and BWT
T Feb 25 DG L6 Genome assembly
R Feb 27 DG L7 ChIP-Seq analysis (DNA-protein interactions)
T Mar 04 DG L8 RNA-seq analysis (expression, isoforms)
R Mar 06 CB L9 Modeling & Discovery of Sequence Motifs
T Mar 11 CB L10 Markov & Hidden Markov Models (+HMM content on 3/13)

Exam may have some overlap with topics from Pset 1+2 but will be biased towards topics NOT covered on PSets

There may be questions on algorithms, but none related to python or programming

---

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)

## Figures

Extracted from the original PDF. They are listed by the page they came from rather
than placed in the text: the conversion does not record where on the page each one
sat.

![Figure from page 4 of the original](10-slides/figures/p004-1.jpx)

![Figure from page 5 of the original](10-slides/figures/p005-1.jpx)

![Figure from page 7 of the original](10-slides/figures/p007-1.jpx)

![Figure from page 12 of the original](10-slides/figures/p012-1.jpeg)

![Figure from page 12 of the original](10-slides/figures/p012-2.jpx)

![Figure from page 12 of the original](10-slides/figures/p012-3.jpeg)

![Figure from page 12 of the original](10-slides/figures/p012-4.png)

![Figure from page 12 of the original](10-slides/figures/p012-5.jpeg)

![Figure from page 13 of the original](10-slides/figures/p013-1.jpeg)

![Figure from page 13 of the original](10-slides/figures/p013-2.jpeg)

![Figure from page 13 of the original](10-slides/figures/p013-3.png)

![Figure from page 14 of the original](10-slides/figures/p014-1.jpx)

![Figure from page 24 of the original](10-slides/figures/p024-1.jpeg)

![Figure from page 24 of the original](10-slides/figures/p024-2.jpeg)

![Figure from page 26 of the original](10-slides/figures/p026-1.jpx)

