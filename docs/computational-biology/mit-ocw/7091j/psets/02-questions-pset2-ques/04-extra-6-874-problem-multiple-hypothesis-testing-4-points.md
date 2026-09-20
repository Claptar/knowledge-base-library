---
title: (Extra 6.874 Problem) Multiple Hypothesis Testing (4 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/02-questions-pset2-ques.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/02-questions-pset2-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# (Extra 6.874 Problem) Multiple Hypothesis Testing (4 points)

Differential expression analysis of RNA-seq data involves testing thousands of hypotheses in a single experiment. To limit false positives, it is necessary to adjust P-values. Two popular methods for doing so are Bonferroni correction and Benjamini-Hochberg.

Consider the following uncorrected p-values of 20 genes from a gene expression study in which we wish to identify differentially expressed genes, say using DEseq.

| Gene | P-value | Gene | P-value |
| :--- | :--- | :--- | :--- |
| 1 | 0.0002 | 11 | 0.01500 |
| 2 | 0.0005 | 12 | 0.02300 |
| 3 | 0.0040 | 13 | 0.02400 |
| 4 | 0.0060 | 14 | 0.03400 |
| 5 | 0.0070 | 15 | 0.03900 |
| 6 | 0.0080 | 16 | 0.04700 |
| 7 | 0.0090 | 17 | 0.05000 |
| 8 | 0.0110 | 18 | 0.05800 |
| 9 | 0.0120 | 19 | 0.06000 |
| 10 | 0.0120 | 20 | 0.09800 |

**(A) (1 pt.)** Apply Bonferroni correction and list the genes that would be reported as differentially expressed at $\text{alpha} = 0.05$. Show how you obtain the list.

**(B) (1 pt.)** List the genes that would be reported as differentially expressed using Benjamini-Hochberg correction at $\text{alpha} = 0.05$. Show how you obtain the list.

**(C) (2 pt.)** How do the two lists differ in composition? What does this show about the stringency of these corrections?

---

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Problem 6. Modeling and information content of sequence motifs (5 points).](03-problem-6-modeling-and-information-content-of-sequence-motif.md) · [Up: contents](index.md)
