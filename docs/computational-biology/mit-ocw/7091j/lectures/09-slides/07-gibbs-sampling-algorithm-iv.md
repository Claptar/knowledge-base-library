---
title: Gibbs Sampling Algorithm IV
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Gibbs Sampling Algorithm IV

**Source:** `lectures/09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

4. Score possible sites in the sequence using weight matrix

Likelihood (probability)

Θ

21

- The Gibbs Sampling Algorithm In Words, II Given **N** sequences of length **L** and desired motif width **W:** 5) Sample a starting position in seq 1 based on this probability distribution and set **a1** to this new position.

- 6) Choose a sequence at random from the set (say, seq 2).

- 7) Make a weight matrix model of width **W** from the sites in all sequences _except_ the one chosen in step 6.

- 8) Assign a probability to each position in seq 2 using the weight matrix model constructed in step 7.

- Step 9) Sample a starting position in seq 2 based on this dist. Step 10) Repeat until convergence (of positions or motif model)

Lawrence et al. _Science_ 1993

22

---

[← Gibbs Sampling Algorithm III](06-gibbs-sampling-algorithm-iii.md) · [Up: contents](index.md) · [Gibbs Sampling Algorithm V →](08-gibbs-sampling-algorithm-v.md)
