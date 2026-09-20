---
title: Null distribution
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-11-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-02-11-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Null distribution

- How biologically meaningful are these scores?
- Assess probability that a particular score would occur by random chance
  - How likely is it that 20 random nucleotides would match CTCF motif?

**b**
| Position | Str | Sequence | Score |
| :--- | :---: | :--- | :--- |
| 19390631 | + | TTGACCAGCAGGGGCGCCG | 26.30 |
| 32420105 | + | CTGGCCAGCAGAGGGCAGCA | 26.30 |
| 27910537 | - | CGGTGCCCCTGCTGGTTCAG | 26.18 |
| 21968106 | + | GTGACCACCAGGGGGCAGCA | 25.81 |
| 31409358 | + | CGGGCCTCCAGGGGGCGCTC | 25.56 |
| 19129218 | - | TGGCGCCACCTGCTGGTCAC | 25.44 |
| 21854623 | + | CTGGCCAGCAGAGGGCAGGG | 24.95 |
| 12364895 | + | CCCGCCAGCAGAGGAGGCGG | 24.71 |
| 13406383 | + | CTAGCCACCAGGTGGCGGTG | 24.71 |
| 18613020 | + | CCCGCCAGCAGAGGAGGCGG | 24.71 |
| 31980801 | + | ACGCCCAGCAGGGGCGCCG | 24.71 |
| 32909754 | - | TGGCTCCCCCTGGCGGCCGG | 24.71 |
| 25683654 | + | TCGGCCACTACGGGCCACTA | 24.58 |
| 31116990 | - | GGCCGCCACCTTGTGGCCAG | 24.58 |
| 29615421 | - | CTCTGCCCTCTGGTGGCTGC | 24.46 |
| 6024389 | + | GTTGCCACCAGAGGCACTA | 24.46 |
| 26610753 | - | CACTGCCCTCTGCTGGCCCA | 24.34 |
| 26912791 | - | GGGCGCCACCTGGCGGTCAC | 24.34 |
| 20446267 | + | CTGCCCACCAGGGGGCAGCG | 24.22 |
| 21872506 | - | TGGCGCCACCTGGCGGCAGC | 24.22 |

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Noble, William S. "How does Multiple Testing Correction Work?." *Nature Biotechnology* 27, no. 12 (2009): 1135.

---

- Empirical null
  - Shuffle bases of chr21 and rescan
  - Any high scoring CTCF instances occur due to random chance, not biology
  - Histogram of scores in empirical null distribution

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Noble, William S. "How does Multiple Testing Correction Work?." *Nature Biotechnology* 27, no. 12 (2009): 1135.

---

## P-value

- Probability that a score at least as large as the observed score would occur in the data drawn according to the null hypothesis

- $P(S > 26.30) = \frac{1}{68\text{ million}} = 1.5 \times 10^{-8}$
- $P(S > 17) = \frac{35}{68\text{ million}} = 5.5 \times 10^{-7}$

- Compare to confidence threshold
  - \$\alpha = 0.0

---

← Nature Biotechnology example · [Up: contents](index.md)
