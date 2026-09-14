---
title: 'Extension 3: Combs and Random Projections'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Extension 3: Combs and Random Projections

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### **Key idea:**

- No reason to use only consecutive symbols

- Instead, we could use combs, e.g., `RGIKW`  `R*IK* , RG**W, …`

- Indexing same as for W-mers: – For each comb, store the list of positions in the database where it occurs – Perform lookups to answer the query

- How to choose the combs?  At random

   - Random projections: Califano-Rigoutsos’93, Buhler’01, Indyk-Motwani’98

   - Choose the positions of * at random

   - Analyze false positives and false negatives

###### **Performance Analysis:**

- Assume we select k positions, which do not contain *, at random with replacement

- What is the probability of a false negative ? – At most: 1-idperc<sup>k</sup> – In our case: 1-(7/9)<sup>4</sup> =0.63...

Query: `RKIWGDPRS` Datab.: `RKIVGDRRS`

k=4

- What is we repeat the process l times, independently ?

   - Miss prob. = 0.63<sup>l</sup>

   - – For l=5, it is less than 10%

Query: `*KI*G***S` Datab.: `*KI*G***S`

33

---

[← Extensions to the basic algorithm](28-extensions-to-the-basic-algorithm.md) · [Up: contents](index.md) · [Today’s Goal: Diving deeper into alignments →](30-today-s-goal-diving-deeper-into-alignments.md)
