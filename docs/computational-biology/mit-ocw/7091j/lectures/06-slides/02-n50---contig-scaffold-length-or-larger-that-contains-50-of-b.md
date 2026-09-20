---
title: N50 - contig/scaffold length or larger that contains 50% of bases
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/06-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/06-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# N50 - contig/scaffold length or larger that contains 50% of bases

**Table 1. Assembly statistics for *C. elegans* data set**

| | OLC
$t >= 75$
SGA | De Bruijn
$k = 61$
Velvet | De Bruijn
$k = 67$
ABySS | De Bruijn
$k = 59$
SOAPdenovo |
| :--- | :--- | :--- | :--- | :--- |
| Scaffold N50 size | 26.3 kbp | 31.3 kbp | 23.8 kbp | 31.1 kbp |
| Aligned contig N50 size | 16.8 kbp | 13.6 kbp | 18.4 kbp | 16.0 kbp |
| Mean aligned contig size | 4.9 kbp | 5.3 kbp | 6.0 kbp | 5.6 kbp |
| Sum aligned contig size | 96.8 Mbp | 95.2 Mbp | 98.3 Mbp | 95.4 Mbp |
| Reference bases covered | 96.2 Mbp | 94.8 Mbp | 95.9 Mbp | 95.1 Mbp |
| Reference bases covered by contigs $\ge$ 1 kb | 93.0 Mbp | 92.1 Mbp | 93.9 Mbp | 92.3 Mbp |
| Mismatch rate at all assembled bases | 1 per 21,545 bp | 1 per 8786 bp | 1 per 5577 bp | 1 per 26,585 bp |
| Mismatch rate at bases covered by all assemblies | 1 per 82,573 bp | 1 per 18,012 bp | 1 per 8209 bp | 1 per 81,025 bp |
| Contigs with split/bad alignment (sum size) | 458 (4.4 Mbp) | 787 (7.2 Mbp) | 638 (9.1 Mbp) | 483 (4.4 Mbp) |
| Total CPU time | 41 h | 2 h | 5 h | 13 h |
| Max memory usage | 4.5 GB | 23.0 GB | 14.1 GB | 38.8 GB |

100 MBase genome, 33.8M read pairs, 100bp reads each end, 250bp insert size

Efficient de novo assembly of large genomes using compressed data structures
Jared T Simpson and Richard Durbin Genome Res. 2012. 22: 549–556

---

## FIN

---

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Lecture 6](01-lecture-6.md) · [Up: contents](index.md)
