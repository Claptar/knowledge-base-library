---
title: Introduction
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/17-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/17-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# 2.5 RNA structure

Like DNA, RNA is also a polymer made from nucleotides, each consisting of sugar, a phosphate and a nucleic acid base. The sugar ribose in RNA has one more OH group, compared to deoxyribose in DNA. The four distinct bases in DNA are adenine (A), guanine (G), cytosine (C) and thymine (T), while in RNA uracil (U) takes the place of thymine. While the central role of DNA is storage of genetic information, RNA molecules carry a variety of roles from structural (the protein building machinery of ribosome) to information transfer (in messenger RNA). Concomitant with their diverse roles, the structure of RNA molecules is more complicated and they can assume a variety of shapes. An important distinction to DNA that enables this variety is that RNA is a single stranded molecule. While two complimentary strands of DNA wrap around each other to form a stable and relatively rigid molecule, the single strand of RNA is more flexible. The molecule can loop upon itself so that bases on different parts of the molecule can form complimentary Watson-Crick pairs. While the primary structure refers to the sequence of bases along RNA, its secondary structure indicates the bases that come into contact to form complimentary bonds. The thus connected macromolecule then assumes particular shape(s) in three dimensions, known as its tertiary structure.

Given the sequence of RNA, can one predict its secondary structure? There are indeed a number of algorithms to do this. The idea is to list all possible pairing (for N bases there are roughly (N − 1)!! pairings, but not all are physically allowed), compute their energies (say by adding specified energies for the different Watson-Crick pairings), and select the best one. Given the large number of pairings, this is a hard computational task. Fortunately the constraint of folding into a viable three dimensional structure severely limits the number of possible secondary structures. A particularly convenient subset is that of planar graphs for which the RNA backbone, and all secondary connections can be drawn on a two dimensional plane, without any two lines crossing. Secondary connections that violate planarity lead to three dimensional structures containing elements called pseudoknots which are very rare (though not impossible) in actual RNAs. Thus limiting the search to this subset is not a bad restriction.


The advantage of the planar subset is that it can be represented in multiple ways, and importantly enables finding the optimal configuration in polynomial time. One simple representation, indicated above, is obtained by stretching the RNA along a straight line and

55

connecting the paired monomers by arches. Two arches are either disconnected, or one is entirely enclosed by the other– the arches will not intersect for planar graphs. Another representation is in terms of parentheses: Starting from one end of the DNA an open parenthesis is placed when the first monomer of pair is encountered, the parenthesis is closed when its partner is encountered. A planar diagram will then correspond to a grammatically correct string. The latter representation then yields a useful graphical prescription as a random walk: Moving along the sequence an up step indicates a parenthesis opened, a down step one that is closed. The planar diagram is now depicted as an island or mountain landscape with no segments where the height is negative.


Let us consider a simple model for secondary structures in which all pairings without pseudo-knots are allowed (i.e. without consideration of bending or steric constraints). For each configuration C, the energy is the sum over energies assigned to all bonded pairs, i.e. E[C] =<sup>�</sup> <ij><sup>εij,whereεijistheenergyofthebondbetweenmonomersiandj;naturally</sup> the sum includes only the subset of indices paired in configuration C. The configuration of minimal E can be obtained recursively as follows. Suppose we have found optimal configurations (and energies) for all sub-sequences of length n and shorter. The optimal energy for a sub-sequence of length (n + 1), say spanning sites i to j = i + n + 1 is obtained by considering the following (n + 2) possibilities: j is unpaired in the optimal configuration, or j is paired to a site i ≤ k ≤ j − 1. In any one of the latter (n + 1) cases the arch between j and k creates two segments (from i to k − 1, and from k + 1 to j − 1) which are independent due to the planarity restriction. The best energy is thus given by


Starting from segments of length n = 1, where Ei,i+1 = εi i+1, the above equation can be used to generate optimal energies for longer segments. The optimal configuration can then be obtained by tracing back.

The above procedure is easily extended to finite temperatures where considerations of entropy may be relevant. We can then assign free energies to segments of the RNA, obtained from corresponding partition functions which may be computed recursively by appealing to Eq. (2.96) as


56

---

[Up: contents](index.md) · [2.5.1 Free energy of molten RNA →](02-2-5-1-free-energy-of-molten-rna.md)
