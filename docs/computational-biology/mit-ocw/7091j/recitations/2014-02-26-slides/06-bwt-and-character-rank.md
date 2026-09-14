---
title: BWT and character rank
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-26-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# BWT and character rank

**Source:** `recitations/2014-02-26-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

notice that each column and each row of the BW-matrix contains every letter from the input string

##### rank? rank?

   - what do we mean by a character's <u>rank in a column?</u>

   - the rank of a specific character _qc_ is the number of _qc_ s above it in the column, +1

- 1 **$BANANA**

   - A 1 N 1 N 2 B 1

- 1 **A$BANAN**

- 2 **ANA$BAN**

- 3 **ANANA$B** 1 **BANANA$**

- 1 **NA$BANA** 2 **NANA$BA**

$ 1 A 2 A 3

Burrows Burrows Wheeler Wheeler matrix transform

- note that (for example) the "A" of rank 2 in the last column (BWT) and first column are the same lexical occurrence (the A preceded by "BAN" and followed by "NA")

- this lets us distinguish between the different "A" characters that occur in different _contexts_ in the original string:

BANANA rank in BWT? 3 2 1

- so, chars in the **F** irst and **L** ast columns have the same rank

9


10

---

[← Why use the BWT?](05-why-use-the-bwt.md) · [Up: contents](index.md) · [Last to First (LF) function →](07-last-to-first-lf-function.md)
