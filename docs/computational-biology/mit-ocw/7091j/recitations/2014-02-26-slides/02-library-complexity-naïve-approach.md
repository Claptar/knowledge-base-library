---
title: 'Library Complexity: Naïve approach'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-26-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-02-26-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Library Complexity: Naïve approach

- Testing this against real data (e.g. subsampling) reveals the assumption (each unique molecule is represented equally in the library) is totally off!
  - Again, due to: 1. Stochastic sampling of sample molecules into library
  - 2. Original highly expressed molecules are represented multiple times
  - 3. PCR amplification bias of some molecules
- Thus, $\lambda$ is not the same for every molecule, and we should allow it to vary
  - This motivates using the Negative Binomial (2 parameters) instead of the Poisson (1 parameter)
- Negative binomial distribution models an overdispersed Poisson distribution: useful when the variance > mean (they're equal in Poisson).
  - The dispersion is $k$ (this needs to be fit to data)
  - Higher $k \implies$ more over-dispersed library $\implies$ more "biased" library and further deviation from assumption that each unique molecule is represented equally
  - Note that there are different parameterizations of the Negative Binomial: In terms of ($\lambda$ and $k$) or ($r$ and $p$) in lecture slides, as well as whether $r$ is the desired success or the last failure. See http://www.johndcook.com/negative_binomial.pdf
  - Use Wikipedia/Matlab/WolframAlpha for Problem Set

---

## Short read alignment (mapping)

- Motivation: Common sequencing experiments: ~100 million 100bp reads to align to a billion base pair genome
- Naïve ("ctrl-F" search) method of taking a read and searching the entire genome:
  - O(genome size = 1 billion) per read (without indels)
  - For all reads: O(1 billion x 200 million) – infeasible!
  - Ideally, something that approaches O(# of reads) – approximately independent of the size of genome
- We do this through BWT transform and FM index of genome

---

## Burrows-Wheeler Transform (BWT)

BANANA$

$\downarrow$ (1) take all rotations of $BANANA

BANANA$
ANANA$B
NANA$BA
ANA$BAN
NA$BANA
A$BANAN
$BANANA

7x7 matrix

$\xrightarrow{\text{(2) sort rows alphabetically ($ sorts first)}}$

note that the first column is just BANANA$ sorted alphabetically

$BANANA
A$BANAN
ANA$BAN
ANANA$B
BANANA$
NA$BANA
NANA$BA

Burrows Wheeler matrix

$\xrightarrow{\text{(3) last col of matrix is the BW transform}}$

A
N
N
B
\$
A
A

---

---

[← Library Complexity: Naïve approach](01-library-complexity-naïve-approach.md) · [Up: contents](index.md) · [Why use the BWT? →](03-why-use-the-bwt.md)
