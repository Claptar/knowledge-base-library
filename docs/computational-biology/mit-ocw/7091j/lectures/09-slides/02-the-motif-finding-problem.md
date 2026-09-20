---
title: The Motif Finding Problem
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/09-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# The Motif Finding Problem

| Unaligned | Aligned |
| :--- | :--- |
| `agggcactagcccatgtgagagggcaaggaccagcggaag` | `gcggaagagggcactagcccatgtgagagggcaaggacca` |
| `taattcagggccaggatgtatctttctcttaaaaataaca` | `atctttctcttaaaaataacataattcagggccaggatgt` |
| `tatcctacagatgatgaatgcaaatcagcgtcacgagctt` | `gtcacgagctttatcctacagatgatgaatgcaaatcagc` |
| `tggcgggcaaggtgcttaaaagataatatcgaccctagcg` | `taaaagataatatcgaccctagcgtggcgggcaaggtgct` |
| `attcgggtaccgttcataaaagtacgggaatttcgggtag` | `gtagattcgggtaccgttcataaaagtacgggaatttcgg` |
| `gttatgttaggcgagggcaaaagtcatatacttttaggtc` | `tatacttttaggtcgttatgttaggcgagggcaaaagtca` |
| `aagagggcaatgcctcctctgccgattcggcgagtgatcg` | `ctctgccgattcggcgagtgatcgaagagggcaatgcctc` |
| `gatggggaaaatatgagaccaggggagggccacactgcag` | `aggatggggaaaatatgagaccaggggagggccacactgc` |
| `ctgccgggctaacagacacacgtctagggctgtgaaatct` | `acacgtctagggctgtgaaatctctgccgggctaacagac` |
| `gtaggcgccgaggccaacgctgagtgtcgatgttgagaac` | `gtgtcgatgttgagaacgtaggcgccgaggccaacgctga` |
| `attagtccggttccaagagggcaactttgtatgcaccgcc` | `atgcaccgccattagtccggttccaagagggcaactttgt` |
| `gcggcccagtgcgcaacgcacagggcaaggtttactgcgg` | `ctgcgggcggcccagtgcgcaacgcacagggcaaggttta` |
| `ccacatgcgagggcaacctccctgtgttgggcggttctga` | `tgtgttgggcggttctgaccacatgcgagggcaacctccc` |
| `gcaattgtaaaacgacggcaatgttcggtcgcctaccctg` | `gtcgcctaccctggcaattgtaaaacgacggcaatgttcg` |
| `gataaagaggggggtaggaggtcaactcttccgtattaat` | `cgtattaatgataaagaggggggtaggaggtcaactcttc` |
| `aggagtagagtagtgggtaaactacgaatgcttataacat` | `aatgcttataacataggagtagagtagtgggtaaactacg` |
| `gcgagggcaatcgggatctgaaccttctttatgcgaagac` | `tctgaaccttctttatgcgaagacgcgagggcaatcggga` |
| `tccaggaggaggtcaacgactctgcatgtctgacaacttg` | `tgcatgtctgacaacttgtccaggaggaggtcaacgactc` |
| `gtcatagaattccatccgccacgcggggtaatttggacgt` | `cgtgtcatagaattccatccgccacgcggggtaatttgga` |
| `gtgccaacttgtgccggggggctagcagcttcccgtcaaa` | `tcccgtcaaagtgccaacttgtgccggggggctagcagct` |
| `cgcgtttggagtgcaaacatacacagcccgggaatataga` | `acagcccgggaatatagacgcgtttggagtgcaaacatac` |
| `aagatacgagttcgatttcaagagttcaaaacgtgacggg` | `acgggaagatacgagttcgatttcaagagttcaaaacgtg` |
| `gacgaaacgagggcgatcaatgcccgataggactaataag` | `cccgataggactaataaggacgaaacgagggcgatcaatg` |
| `tagtacaaacccgctcacccgaaaggagggcaaatacctt` | `ttagtacaaacccgctcacccgaaaggagggcaaatacct` |
| `atatacagccaggggagacctataactcagcaaggttcag` | `agcaaggttcagatatacagccaggggagacctataactc` |
| `cgtatgtactaattgtggagagcaaatcattgtccacgtg` | `gtccacgtgcgtatgtactaattgtggagagcaaatcatt` |
| `...` | `...` |

...can be posed as an alignment problem

---

## Approaches to Motif Finding

- Enumerative ('dictionary')
  - search for a $k\text{mer}$/set of $k\text{mers}$/regular expression that is statistically over-represented

- Probabilistic Optimization (e.g., Gibbs sampler)
  - stochastic search of the space of possible PSPMs

- Deterministic Optimization (e.g., MEME)
  - deterministic search of space of possible PSPMs

---

## What the motif landscape might look like

---

## Monte Carlo Algorithms

The Gibbs motif sampler is a **Monte-Carlo algorithm**

**General definition:** class of computational algorithms that rely on repeated random sampling to compute their results

**Specific definition:** randomized algorithm where the computational resources used are bounded but the answer is not guaranteed to be correct 100% of the time

### Related to

**Las Vegas algorithm** - a randomized algorithm that always gives correct results (or informs about failure)

---

## Example: The Gibbs Motif Sampler

The likelihood function for a set of sequences $\vec{s}$ with motif locations $\vec{A}$

$$P(\vec{s}, \vec{A} \mid \Theta, \theta_B) = \prod_k \theta_{B,S_{k,1}} \times \dots \times \theta_{B,S_{k,A_k-1}} \times \Theta_{1,S_{k,A_k}} \times \Theta_{2,S_{k,A_k+1}} \times \dots \times \Theta_{8,S_{k,A_k+7}} \times \theta_{B,S_{k,A_k+8}} \times \dots \times \theta_{B,L}$$

$S_k = \text{“actactgtatcgtactgactgattaggccatgactgcat”}$

Motif location $A_k$

Lawrence et al. *Science* 1993

---

## The Gibbs Sampling Algorithm In Words I

Given **N** sequences of length **L** and desired motif width **W**:

1) Choose a starting position in each sequence at random:
   **a$_1$** in seq 1, **a$_2$** in seq 2, ..., **a$_N$** in sequence **N**

2) Choose a sequence at random from the set (say, seq 1).

3) Make a weight matrix model of width **W** from the sites in all sequences *except* the one chosen in step 2.

4) Assign a probability to each position in seq 1 using the weight matrix model constructed in step 3:
   **p** = { **p$_1$**, **p$_2$**, **p$_3$**, ..., **p$_{L-W+1}$** }

Lawrence et al. *Science* 1993

---

## Gibbs Sampling Algorithm I

### 1. Select a random position in each sequence

---

## Gibbs Sampling Algorithm II

### 2. Build a weight matrix

---

## Gibbs Sampling Algorithm III

### 3. Select a sequence at random

---

## Gibbs Sampling Algorithm IV

### 4. Score possible sites in the sequence using weight matrix

---

## The Gibbs Sampling Algorithm In Words, II

Given **N** sequences of length **L** and desired motif width **W**:

5) Sample a starting position in seq 1 based on this probability distribution and set **a$_1$** to this new position.

6) Choose a sequence at random from the set (say, seq 2).

7) Make a weight matrix model of width **W** from the sites in all sequences *except* the one chosen in step 6.

8) Assign a probability to each position in seq 2 using the weight matrix model constructed in step 7.

Step 9) Sample a starting position in seq 2 based on this dist.

Step 10) Repeat until convergence (of positions or motif model)

Lawrence et al. *Science* 1993

---

## Gibbs Sampling Algorithm V

### 5. Sample a new site proportional to likelihood and update motif instances

---

## Gibbs Sampling Algorithm VI

### 6. Update weight matrix

---

## Gibbs Sampling Algorithm VII

### 7. Iterate until convergence ($\Delta\text{sites} = 0$ or $\Delta\Theta \sim 0$)

---

## Input Sequences with Strong Motif

---

## Gibbs Sampler - Strong Motif Example

---

## Input Sequences (Weak Motif)

```
gcggaagagggcactagcccatgtgagagggcaaggacca
atctttctcttaaaaataacataattcagggccaggatgt
gtcacgagctttatcctacagatgatgaatgcaaatcagc
taaaagataatatcgaccctagcgtggcgggcaaggtgct
gtagattcgggtaccgttcataaaagtacgggaatttcgg
tatacttttaggtcgttatgttaggcgagggcaaaagtca
ctctgccgattcggcgagtgatcgaagagggcaatgcctc
aggatggggaaaatatgagaccaggggagggccacactgc
acacgtctagggctgtgaaatctctgccgggctaacagac
gtgtcgatgttgagaacgtaggcgccgaggccaacgctga
atgcaccgccattagtccggttccaagagggcaactttgt
ctgcgggcggcccagtgcgcaacgcacagggcaaggttta
tgtgttgggcggttctgaccacatgcgagggcaacctccc
gtcgcctaccctggcaattgtaaaacgacggcaatgttcg
cgtattaatgataaagaggggggtaggaggtcaactcttc
aatgcttataacataggagtagagtagtgggtaaactacg
tctgaaccttctttatgcgaagacgcgagggcaatcggga
tgcatgtctgacaacttgtccaggaggaggtcaacgactc
cgtgtcatagaattccatccgccacgcggggtaatttgga
tcccgtcaaagtgccaacttgtgccggggggctagcagct
acagcccgggaatatagacgcgtttggagtgcaaacatac
acgggaagatacgagttcgatttcaagagttcaaaacgtg
cccgataggactaataaggacgaaacgagggcgatcaatg
ttagtacaaacccgctcacccgaaaggagggcaaatacct
agcaaggttcagatatacagccaggggagacctataactc
gtccacgtgcgtatgtactaattgtggagagcaaatcatt
...
```

---

## Gibbs Sampler - Weak Motif Example

---

## Gibbs Sampler Summary

- A stochastic (Monte Carlo) algorithm for motif finding
- Works by 'stumbling' onto a few motif instances, which bias the weight matrix, which causes it to sample more motif instances, which biases the weight matrix more, ... until convergence
- Not guaranteed to converge to same motif every time - run several times, compare results
- Works for protein, DNA, RNA motifs

---

## What does this algorithm accomplish?

The likelihood function for a set of sequences $\vec{s}$ with motif locations $\vec{A}$

$$P(\vec{s}, \vec{A} \mid \Theta, \theta_B) = \prod_k \theta_{B,S_{k,1}} \times \dots \times \theta_{B,S_{k,A_k-1}} \times \Theta_{1,S_{k,A_k}} \times \Theta_{2,S_{k,A_k+1}} \times \dots \times \Theta_{8,S_{k,A_k+7}} \times \theta_{B,S_{k,A_k+8}} \times \dots \times \theta_{B,L}$$

$S_k = \text{“actactgtatcgtactgactgattaggccatgactgcat”}$

Motif location $A_k$

Likelihood function tends to increase

---

## Features that affect motif finding

No. of sequences

Length of sequences

Information content of motif

Match between expected length and actual length of motif

### Motif finding issues

"shifted" motifs

biased background composition

---

## Practical Motif Finding

- MEME is a classic method
  Deterministic - like Gibbs, but uses expectation maximization
  Bailey & Elkan 1995 paper is posted.
  Run MEME at:
  http://meme.nbcr.net/meme/

The Fraenkel lab's WebMotifs combines
AlignACE (similar to Gibbs), MDscan, MEME, Weeder, THEME
Described in Romer et al. and references therein
http://fraenkel.mit.edu/webmotifs.html

---

## Mean Log-odds (bit-) Score of a Motif

$$\text{bit-score: } \log_2 \left( \frac{p_k}{q_k} \right) \qquad \text{mean bit-score: } \sum_{k=1}^n p_k \log_2 \left( \frac{p_k}{q_k} \right)$$

motif width $w$, $n = 4^w$

$$\text{If } q_k = \frac{1}{4^w} \text{ then mean bit-score} = 2w - H_{\text{motif}} = I_{\text{motif}}$$

### What is the use of knowing the information content of a motif?

**Rule of thumb\*:** a motif with $m$ bits of information will occur about once every $2^m$ bases of random sequence

\* Strictly true for regular expressions, approximately true for general motifs

For more on information theory, see: *Elements of Information Theory* by T. Cover

---

## Relative Entropy*

$$\text{Relative entropy, } D(p \parallel q) = \text{mean bit-score: } \sum_{k=1}^n p_k \log_2 \left( \frac{p_k}{q_k} \right)$$

$$\text{If } q_k = \frac{1}{4^w} \text{ then mean RelEnt} = 2w - H_{\text{motif}} = I_{\text{motif}}$$

RelEnt is a measure of **information**, not entropy/uncertainty. In general RelEnt is different from $H_{\text{before}} - H_{\text{after}}$ and is a better measure when background is non-random

Example: $q_A = q_T = 3/8, \quad q_C = q_G = 1/8$

Suppose: $p_C = 1. \quad H(q) - H(p) < 2$

But RelEnt $D(p \parallel q) = \log_2(1 / (1/8)) = 3$

Which one better describes frequency of C in background seq?

\* Alternate names: "Kullback-Leibler distance", "information for discrimination"

---

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Modeling & Discovery of Sequence Motifs](01-modeling-discovery-of-sequence-motifs.md) · [Up: contents](index.md)
