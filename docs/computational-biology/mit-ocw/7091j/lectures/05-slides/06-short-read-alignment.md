---
title: Short Read Alignment
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Short Read Alignment

**Source:** `lectures/05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Given a reference and a set of reads, report at least one “good” local alignment for each read if one exists

   - Approximate answer to: where in genome did read originate?

- What is “good”?  For now, we concentrate on:

**`…TGATCATA… …TGATCATA…`** better than **`GATCAA GAGAAT …TGATATTA… …TGATcaTA…`** better than **`GATcaT GTACAT`**

- Fewer mismatches are better

- Failing to align a low-quality base is better than failing to align a high-quality base

Courtesy of Ben Langmead. Used with permission.

21

**http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt**

##### The Burrows-Wheeler Transform is a reversible representation with handy properties

- Sort all the possible rotations of original string

**T**

**BWT(T)**

**Burrows Wheeler Matrix**

**Last column**

- Once BWT(T) is built, all else shown here is discarded – Matrix will be shown for illustration only

Burrows M, Wheeler DJ: **A block sorting lossless data compression algorithm** . Digital Equipment Corporation, Palo Alto, CA 1994, Technical Report 124; 1994

Courtesy of Ben Langmead. Used with permission.

**http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt**

22

A text occurrence has the same rank in the first and last columns

- When we rotate left and sort, the first character retains its rank.   Thus the same text occurrence of a character has the same rank in the **L** ast and **F** irst columns.

**Rank: 2**


**T**


**BWT(T)**

**Rank: 2**

**Burrows Wheeler Matrix**

23

Courtesy of Ben Langmead. Used with permission.

**http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt**

#### The Last to First (LF) function matches character and rank

**LF(6, ‘c’) = Occ(‘c’) + Count(6,’c’) = 5**

**Occ(‘c’) = 4 Count(6,’c’) = 1**


**0 1 2 3 BWT(T) 4 5 Rank: 2 6**

**Occ(qc) – Number of characters lexically smaller than qc in BWT(T)**

**Count(idx, qc) – Number of qc characters before position idx in BWT(T)**

Courtesy of Ben Langmead. Used with permission.

24

**http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt**

#### The Walk Left Algorithm inverts the BWT

**i = 0 t = “” while bwt[i] != ‘$’:**

**t = bwt[i] + t i = LF(i, bwt[i])**

Final **t**


Courtesy of Ben Langmead. Used with permission.

25

**http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt**

### Lecture 5 – Libraries and Indexing

- Library Complexity

   - How do we estimate the complexity of a sequencing library?

- Full-text Minute-size index (FM Index/BWT) – How do we convert a genome into an alternate representation that permits rapid matching of millions of sequence reads?

- Read Alignment

   - How can we use an FM index and BWT to rapidly align reads to a reference genome?

26

---

[← Short Read Applications](05-short-read-applications.md) · [Up: contents](index.md) · [Exact Matching with FM Index →](07-exact-matching-with-fm-index.md)
