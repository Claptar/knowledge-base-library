---
title: Energy Minimization Approach
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Energy Minimization Approach

**Source:** `lectures/11-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

ΔGfolding = Gunfolded - Gfolded

There are typically many possible folded states - assumption that minimum energy state(s) will be occupied

ΔG = ΔH - TΔS

Enthalpy favors folding Entropy favors unfolding

**What environmental variables affect RNA folding?**

26

###### How Do Energy Minimization Algorithms Work?

Consider Simple Model: Base Pair Maximization **Scoring System:**

+1 for base pair (C:G, A:U)

0 for anything else

Maximizing score equivalent to minimizing folding free energy for a model which assigns same enthalpy to all allowed base pairs (and ignores details such as base stacking, loops, entropy)

Nussinov algorithm: recursive maximization of base pairing

27

##### Recursive Maximization of Base Pairing

Given an RNA sequence of length N

Define S(i,j) to be the score of the best structure for the subsequence (i, j) Notice that S(i,j) can be defined recursively in terms of optimal scores of smaller subsequences of the interval (i,j)

There are four possible ways that the score of the optimal structure on (i,j) can relate to scores of optimal structures of nested subsequences:


<!-- Start of picture text -->
S(i+1,j-1)  S(i+1,j)<br>i+1 j-1<br> i  j<br>i  i+1  j<br><!-- End of picture text -->


<!-- Start of picture text -->
S(i+1,j)<br><!-- End of picture text -->


<!-- Start of picture text -->
S(i,j-1)<br>i  j-1  j<br><!-- End of picture text -->


<!-- Start of picture text -->
S(i,k)  S(k+1,j)<br>i  k  k+1  j<br><!-- End of picture text -->

###### 1. i,j pair 2. i unpaired 3. j unpaired

4. bifurcation

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Eddy, Sean R. "How do RNA Folding Algorithms Work?" _Nature Biotechnology_ 22, no. 11 (2004): 1457-8.

Eddy, Nature Biotech. 2004

28

###### Base Pair Maximization Algorithm

S(i,j) = score of the optimal structure for the subsequence (i, j)

   - S(i+1,j-1) + 1 (if i,j base pair) S(i+1,j) (i is unpaired)

- S(i,j) = max

   - S(i,j-1) (j is unpaired)

   - max(i<k<j) S(i,k) + S(k+1,j) (bifurcation)

- 1) Initialize an N x N matrix S with S(i,i) = S(i,i-1) = 0

- 2) Fill in S(i,j) matrix recursively from the diagonal up and to the right (keep track of which choice was made at each step)

- 3) Trace back from S(1,N) (upper right corner of matrix) to diagonal to determine optimal structure

29

###### Dynamic Programming for Base Pair Maximization


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Eddy, Sean R. "How do RNA Folding Algorithms Work?" _Nature Biotechnology_ 22, no. 11 (2004): 1457-8.

Eddy, Nature Biotech. 2004

30

Base Pair Maximization Algorithm Issues

- What is computational complexity of algorithm? (for sequence of length N)

Answer: Memory - O(N<sup>2</sup> ) Time - O(N<sup>3</sup> )

- Can it handle pseudoknots?


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Answer: No. Pseudoknots invalidate recursion for S(i,j)

31

###### **Viral**

###### **Pseudoknots and “Kissing loops”**

Baranov et al. Virology 2005


Courtesy of Elsevier, Inc., http://www.sciencedirect.com. Used with permission. Source: Baranov, Pavel V., Clark M. Henderson, et al. "Programmed Ribosomal Frameshifting in Decoding the SARS-CoV Genome." _Virology_ 332, no. 2 (2005): 498-510.

32

---

[← Classes of Non-coding RNAs](04-classes-of-non-coding-rnas.md) · [Up: contents](index.md) · [RNA Energetics I →](06-rna-energetics-i.md)
