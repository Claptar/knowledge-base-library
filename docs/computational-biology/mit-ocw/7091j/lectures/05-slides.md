---
title: Backtracking
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Backtracking

* May not be so lucky

"g"

"t"

"c"

"a" "a"

Found this alignment (eventually):

```
acaacg
 |   |
 ag  c
```

http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt

---

* Relevant alignments may lie along multiple paths
  * E.g., $Q =$ "aaa", $T =$ "acaacg"

```
acaacg
 | |
 aaa
```

```
acaacg
 |   |
 aaa
```

```
acaacg
  | |
  aaa
```

http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt

---

## Bowtie backtracks to leftmost just-visited position with minimal quality

* PHRED score $= -10\log(p)$ Where $p$ is probability of error

Sequence:
| G | C | C | A | T | A | C | G | G | A | T | T | A | G | C | C |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 40 | 35 | 40 | 40 | 40 | 40 | 30 | 30 | 20 | 15 | 15 | 40 | 40 | 40 | 40 |

(higher number = higher confidence)

| G | C | C | A | T | A | C | G | G | A | C | T | A | G | C | C |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 40 | 35 | 40 | 40 | 40 | 40 | 30 | 30 | 20 | 15 | 15 | 40 | 40 | 40 | 40 |

| G | C | C | A | T | A | C | G | G | G | C | T | A | G | C | C |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 40 | 35 | 40 | 40 | 40 | 40 | 30 | 30 | 20 | 15 | 15 | 40 | 40 | 40 | 40 |

* Greedy, depth-first, not optimal, but simple

http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt

---

## Specifying match quality

* Bowtie supports a Maq*-like alignment policy
  * $\le N$ mismatches allowed in first $L$ bases on left end
  * Sum of mismatch qualities may not exceed $E$
  * $N$, $L$ and $E$ configured with `-n`, `-l`, `-e`
  * E.g.:

| G | C | C | A | T | A | C | G | G | G | C | T | A | G | C | C |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 40 | 40 | 35 | 40 | 40 | 40 | 40 | 30 | 30 | 20 | 15 | 15 | 40 | 25 | 5 | 5 |

$L=12 \quad E=50, N=2$

If $N < 2$
If $E < 45$
If $L < 9$ and $N < 2$

* PHRED score $= -10\log(p)$ Where $p$ is probability of error

\* Li H, Ruan J, Durbin R: Mapping short DNA sequencing reads and calling variants using mapping quality scores. *Genome Res* 2008.

http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt

---

## Bowtie can match starting from the left to limit backtracking

* But how to match left-to-right?
* Double indexing:
  * Reverse read and use "mirror index": index for reference with sequence reversed

| G | C | C | A | T | A | C | G | G | A | T | T | A | G | C | C |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Forward Index
No backtracks allowed

| C | C | G | A | T | T | A | G | G | C | A | T | A | C | C | G |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Mirror Index
No backtracks allowed

---

## Time to build a BWT/FM index

* Bowtie employs a indexing algorithm* that can trade flexibly between memory usage and running time
* For human genome (NCBI 36.3) on 2.4 GHz AMD Opteron:

| Physical memory Target | Actual peak memory footprint | Wall clock time |
|---|---|---|
| 16 GB | 14.4 GB | 4h:36m |
| 8 GB | 5.8

---

[Up: contents](../index.md)

## Figures

Extracted from the original PDF. They are listed by the page they came from rather
than placed in the text: the conversion does not record where on the page each one
sat.

![Figure from page 3 of the original](05-slides/figures/p003-1.jpeg)

![Figure from page 4 of the original](05-slides/figures/p004-1.jpeg)

![Figure from page 6 of the original](05-slides/figures/p006-1.png)

![Figure from page 7 of the original](05-slides/figures/p007-3.jpeg)

![Figure from page 8 of the original](05-slides/figures/p008-1.png)

![Figure from page 9 of the original](05-slides/figures/p009-1.png)

![Figure from page 10 of the original](05-slides/figures/p010-1.jpeg)

![Figure from page 11 of the original](05-slides/figures/p011-1.png)

![Figure from page 11 of the original](05-slides/figures/p011-2.png)

![Figure from page 12 of the original](05-slides/figures/p012-1.jpeg)

![Figure from page 15 of the original](05-slides/figures/p015-1.png)

![Figure from page 17 of the original](05-slides/figures/p017-1.jpeg)

![Figure from page 22 of the original](05-slides/figures/p022-1.png)

![Figure from page 25 of the original](05-slides/figures/p025-1.png)

![Figure from page 27 of the original](05-slides/figures/p027-1.png)

![Figure from page 28 of the original](05-slides/figures/p028-1.png)

![Figure from page 29 of the original](05-slides/figures/p029-1.png)

![Figure from page 30 of the original](05-slides/figures/p030-1.png)

![Figure from page 31 of the original](05-slides/figures/p031-1.png)

![Figure from page 32 of the original](05-slides/figures/p032-1.png)

![Figure from page 33 of the original](05-slides/figures/p033-1.jpeg)

![Figure from page 33 of the original](05-slides/figures/p033-2.png)

![Figure from page 34 of the original](05-slides/figures/p034-1.png)

![Figure from page 35 of the original](05-slides/figures/p035-1.png)

![Figure from page 36 of the original](05-slides/figures/p036-1.jpeg)

![Figure from page 36 of the original](05-slides/figures/p036-2.jpeg)

![Figure from page 36 of the original](05-slides/figures/p036-3.png)

![Figure from page 36 of the original](05-slides/figures/p036-4.jpeg)

![Figure from page 45 of the original](05-slides/figures/p045-1.jpeg)

![Figure from page 45 of the original](05-slides/figures/p045-2.jpeg)

