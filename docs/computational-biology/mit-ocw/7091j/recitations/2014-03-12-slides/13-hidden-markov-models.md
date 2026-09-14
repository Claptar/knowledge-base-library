---
title: Hidden Markov Models
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-12-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Hidden Markov Models

**Source:** `recitations/2014-03-12-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- What if we cannot observe the states (genotypes) directly, but instead observe some phenotype that depends on the state

#### Actual genotypes unknown

Instead we observe cholesterol level _x_ , which is distributed differently for different genotypes _G_ :


<!-- Start of picture text -->
1  AA  Aa  2<br>3  Aa  aa  4<br>5  Aa<br><!-- End of picture text -->


<!-- Start of picture text -->
if genotype is aa<br>if genotype is Aa<br>if genotype is AA<br><!-- End of picture text -->

This is now a Hidden Markov Model – and we want to infer the most likely sequence of hidden genotypes for individuals 1,3, and 5, given observed cholesterol levels, and transition 15 probabilities between genotypes.

---

[← Review: Markov Chains](12-review-markov-chains.md) · [Up: contents](index.md) · [Graphical Representations →](14-graphical-representations.md)
