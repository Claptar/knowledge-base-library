---
title: (Extra 6.874 Problem) Multiple Hypothesis Testing (4 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/02-questions-pset2-ques.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# (Extra 6.874 Problem) Multiple Hypothesis Testing (4 points)

**Source:** `psets/02-questions-pset2-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Differential expression analysis of RNA-seq data involves testing thousands of hypotheses in a single experiment. To limit false positives, it is necessary to adjust P-values. Two popular methods for doing so are Bonferroni correction and Benjamini-Hochberg.

Consider the following uncorrected p-values of 20 genes from a gene expression study in which we wish to identify differentially expressed genes, say using DEseq.

|**Gene**|**P-value**|11|0.01500|
|---|---|---|---|
|1|0.0002|12|0.02300|
|2|0.0005|13|0.02400|
|3|0.0040|14|0.03400|
|4|0.0060|15|0.03900|
|5|0.0070|16|0.04700|
|6|0.0080|17|0.05000|
|7|0.0090|18|0.05800|
|8|0.0110|19|0.06000|
|9|0.0120|20|0.09800|
|10|0.0120|||


- **(A) (1 pt.)** Apply Bonferroni correction and list the genes that would be reported as differentially expressed at alpha = 0.05. Show how you obtain the list.

- **(B) (1 pt.)** List the genes that would be reported as differentially expressed using BenjaminiHochberg correction at alpha = 0.05. Show how you obtain the list.

- **(C) (2 pt.)** How do the two lists differ in composition? What does this show about the stringency of these corrections?

10

MIT OpenCourseWare http://ocw.mit.edu

7.91J  / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology

Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Problem 6. Modeling and information content of sequence motifs (5 points).](08-problem-6-modeling-and-information-content-of-sequence-motif.md) · [Up: contents](index.md)
