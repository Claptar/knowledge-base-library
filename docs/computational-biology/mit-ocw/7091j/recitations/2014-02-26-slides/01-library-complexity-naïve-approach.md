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

DG Lectures 5 & 6
2/26/14

---

## Announcements

- project specific aims due in a little more than a week (March 7)
- Pset #2 due March 13, start early!
- Today:
  - library complexity
  - BWT and read mapping
  - de Bruijn graphs

---

## Library Complexity

- You isolate DNA from your sample of interest (genomic DNA, ChIP-seq, cDNA from RNA-seq, etc.)
- You go through a protocol to generate a "library" of size-selected molecules (e.g. 200-300bp for paired-end genomic DNA sample, much smaller from ChIP-seq, etc.)
  - Library is only a subset of your original sample – some molecules have been lost due to:
    - 1. Stochastic sampling (molecules w/ low count are often lost)
    - 2. Systematic exclusion at steps of the library prep. protocol
- The number of **UNIQUE** molecules in your library is known as "library complexity", $C$ (total # of molecules $T$ is $\gg C$ due to PCR amplification during library prep.)
- The number of sequencing reads you get back is $N$ ($<T$ since only a subset of reads in the library cluster on the flow cell and are sequenced)

---

- Assume each unique molecule is represented equally in the library
  - Not a terrible assumption for genomic DNA (but still not true due to PCR amplification bias)
  - Definitely not a true for ChIP-seq, RNA-seq, etc. in which most frequent molecules in the sample (millions of copies) will have certain fragments represented multiple times in the library even after random fragmentation
  - Each molecule has prob. $1/C$ of being sequenced. You sequence $N$ total molecules, with $M$ **UNIQUE** molecules in your sequencing run ($M < N$)
    - # times each molecule in the library sequenced follows a Poisson distribution with mean (= variance):
      $$\lambda = \frac{N}{C}$$
    - P(observing a molecule in sequencing output) = $1 - \text{P(sequencing the read 0 times)} =$
      $$\sum_{x=1}^{\infty} \frac{e^{-\lambda} \lambda^x}{x!} = 1 - \frac{e^{-\lambda} \lambda^0}{0!} = 1 - e^{-\lambda}$$
    - Maximum likelihood estimate of $C$ is $\hat{C}$ :
      $$M = C \times \text{P(observing a molecule)} \implies \hat{C} = \frac{M}{1 - e^{-\lambda}}$$
  - Note that our formula for estimating $C$ involves $\lambda$, but $\lambda=N/C$ (it's a function of what we're trying to estimate!). So this Poisson formula is not as simple as it appears...would likely want to perform iterative estimation of these parameters.

---

---

[Up: contents](index.md) · [Library Complexity: Naïve approach →](02-library-complexity-naïve-approach.md)
