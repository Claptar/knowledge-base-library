---
title: 3 RNA secondary structure
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/psets/03-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 RNA secondary structure

**Source:** `psets/03-questions.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem we will explore the output of the Nussinov algorithm on random RNA sequences. Submit all code you write.

- (a) Implement the Nussinov algorithm, scoring A–U, G–U, and C–G pairs as −1 and all other pairs as 0.

- (b) Generate 1000 RNA sequences of length 100 where each base is drawn uniformly at random. What is the average score for these sequences?

- (c) How does the score vary as a function of length? (You will need to repeat (b) for various lengths.)

- (d) How does the score vary as a function of GC content? Is this function symmetric around GC content equal to 0.5? Why or why not? (You will need to repeat (b) for different distributions from which you draw bases.)

- (e) Given an RNA transcript of interest, how should you interpret the score output by the Nussinov algorithm with respect to your observations about its dependence on length and sequence composition? Is there a better way to estimate the effect of these biases on the score?

---

[← 2 Evolutionary signatures of motifs](03-2-evolutionary-signatures-of-motifs.md) · [Up: contents](index.md) · [4 Upcoming project milestones →](05-4-upcoming-project-milestones.md)
