---
title: 06 notes
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lectures/06-notes.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 06 notes

**Source:** `lectures/06-notes.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

```
Systems Biology ?
```

# **Systems Biology** ≈ **Network Biology**

**GOAL** : develop a quantitative understanding of the biological function of genetic and biochemical networks

### INPUT


<!-- Start of picture text -->
g ene A g ene B<br>g ene C gene D<br>gene E gene F<br>OUTPUT<br><!-- End of picture text -->

- function of gene product A-F can be known in detail but this is not sufficient to reveal the biological function of the INPUT-OUTPUT relation

- - a system approach (looking beyond one gene/protein) is necessary to reveal the biological function of this whole network

- what is the function of the individual interactions (feedbacks and feedforwards) in the context of the entire network ?

## Alternatively,

Systems Engineering

+

Molecular Biology

Systems Engineering   Molecular Biology

Systems Biology = Applying Systems Engineering concepts to Biological Systems

## molecular biology vs systems biology

A traditional molecular biologist would ask:


<!-- Start of picture text -->
K1<br>λ λ<br>λ<br>K2<br>λ<br>λ λ<br>OR2 OR3<br>λ λ<br>OR2 OR3<br>λ λ λ λ<br>OR2 OR3<br><!-- End of picture text -->

- what is the molecular structure of the cI dimer ?

- what is DNA sequence recognized by the cI dimer ?

- what are the essential amino acids in cI responsible for dimerization ?

- what are the values for K1 and K2 ?

- is the sequence conversed during evolution ?

Focussed on the molecule cI.

## molecular biology vs systems biology

## A systems biologist would ask:


<!-- Start of picture text -->
K1<br>λ λ<br>λ<br>K2<br>λ<br>λ λ<br>OR2 OR3<br>λ λ<br>OR2 OR3<br>λ λ λ λ<br>OR2 OR3<br><!-- End of picture text -->

- what is the functional role of the feedback ?

- how can this lead to a hysteretic switch ?

- what is the role of noise in determining the stability of the switch ?

- is the performance of the switch sensitive to small changes in the parameters (fine-tuned) of not (robust).

- how are these parameters changed when this module is cross-talking to other modules.

Focussed on the network architecture.

## Goal of this course:

- provide you with the essential mathematical tools to be able to model network modules, such as biological switches, oscillators, filters, amplifiers, etc.

- provide you with lots of example of biological problems that can be successfully tackled with a systems biology approach (first well-stirred systems, second diffusiondominated systems) by discussing recent recent papers.

---

[Up: contents](../index.md)
