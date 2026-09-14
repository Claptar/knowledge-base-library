---
title: Library Complexity
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-26-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Library Complexity

**Source:** `recitations/2014-02-26-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- You isolate DNA from your sample of interest (genomic DNA, ChIP-seq, cDNA from RNA-seq, etc.)

- You go through a protocol to generate a “ **library** ” of sizeselected molecules (e.g. 200-300bp for paired-end genomic DNA sample, much smaller from ChIP-seq, etc.)

   - Library is only a subset of your original sample – some molecules have been lost due to:

      - 1. Stochastic sampling (molecules w/ low count are often lost)

- 2. Systematic exclusion at steps of the library prep. protocol

- • The number of _UNIQUE_ molecules in your library is known as “library complexity”, **_C_** (total # of molecules **_T_** is >> **_C_** due to PCR amplification during library prep.)

- • The number of sequencing reads you get back is **_N_** (< _T_ since only a subset of reads in the library cluster on the flow cell and are sequenced)

3

## Library Complexity: Naïve approach

- Assume each unique molecule is represented equally in the library – Not a terrible assumption for genomic DNA (but still not true due to PCR amplification bias)

   - Definitely not a true for ChIP-seq, RNA-seq, etc. in which most frequent molecules in the sample (millions of copies) will have certain fragments represented multiple times in the library even after random fragmentation

   - Each molecule has prob. 1/ **_C_** of being sequenced. You sequence **_N_** total molecules, with **_M_** UNIQUE molecules in your sequencing run ( **_M_** _<_ **_N_** )

      - # times each molecule in the library sequenced follows a Poisson distribution with mean (= variance): _N_

_A_ = _C_

• P(observing a molecule in sequencing output) =1 – P(sequencing the read 0 times) = _1 e-Aλx e-Aλ_ 0 _-A_ = 1 _-_ = 1 _- e_ X _x_ ! 0! _x_ =1 ˆ

- Maximum likelihood estimate of _C_ is _C_ :

ˆ _M M_ = _C ⇥ P_ (observing a molecule) = _) C_ = 1 _- e-A_

- Note that our formula for estimating _C_ involves λ, but λ=N/C (it’s a function of what we’re trying to estimate!). So this Poisson formula is not as simple as it appears…would likely want to perform iterative estimation of these parameters.

4

## Library Complexity: Naïve approach

- Testing this against real data (e.g. subsampling) reveals the assumption (each unique molecule is represented equally in the library) is totally off!

   - Again, due to: 1. Stochastic sampling of sample molecules into library

   - 2. Original highly expressed molecules are represented multiple times

   - 3. PCR amplification bias of some molecules

- Thus, λ is not the same for every molecule, and we should allow it to vary

- This motivates using the Negative Binomial (2 parameters) instead of the

- Poisson (1 parameter)

- • Negative binomial distribution models an overdispersed Poisson distribution: useful when the variance > mean (they’re equal in Poisson).

   - The dispersion is _k_ (this needs to be fit to data)

   - Higher _k_ more over-dispersed library  more “biased” library and further deviation from assumption that each unique molecule is represented equally

   - Note that there are different parameterizations of the Negative Binomial: In terms of (λ and _k_ ) or ( _r_ and _p_ ) in lecture slides, as well as whether _r_ is the desired success or the last failure. See http://www.johndcook.com/negative_binomial.pdf

   - Use Wikipedia/Matlab/WolframAlpha for Problem Set

5

---

[← Announcements](02-announcements.md) · [Up: contents](index.md) · [Short read alignment (mapping) →](04-short-read-alignment-mapping.md)
