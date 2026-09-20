---
title: 02 questions pset2 ques Part 01 —
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/02-questions-pset2-ques.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/02-questions-pset2-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 02 questions pset2 ques Part 01 —

**PROBLEM SET 2. BWT, Library complexity, RNA-seq, Genome assembly, Motifs, Multiple hypothesis testing (31 Points)**

**Due: Thursday, March 13th at noon.**

## Python Scripts
All Python scripts must work on athena using /usr/athena/bin/python. You may **not assume availability of any third party modules** unless you are explicitly instructed so. You are advised to test your code on Athena before submitting. Please only modify the code between the indicated bounds, with the exception of adding your name at the top, and remove any print statements that you added before submission.

Electronic submissions are subject to the same late homework policy as outlined in the syllabus and submission times are assessed according to the server clock. All python programs **must be submitted electronically, as .py files on the course website** using appropriate filename for the scripts as indicated in the problem set or in the skeleton scripts provided on course website.

---

## Problem 1. Aligning reads to a genome using a Burrows Wheeler Transform and FM Index (9 points)

For this exercise you will be implementing the core of a genome search function utilizing the Burrows Wheeler transform (BWT) and an FM-index. We have provided scaffolding code so that you can focus on the core of the algorithm. Please do not use Internet search tools to try to solve this problem – the point is for you to understand how the algorithm works.

You will need the coding and testing files from the course website (keep them in the same folder). This includes scaffold code, a 10kb segment of the yeast genome, reads which you will map to the genome, and an index for testing with correct output.

**(A) (7 pt.)** Complete the LF mapping code in the `_lf(self, idx, qc)` function and the search code in the `bounds(self, q)` function (both in `fmindex.py`).

To test your implementations we have provided the FM-index of an abbreviated version of the yeast genome in `test.index`. Running

```
% python fm-search.py test.index yeast_chr1_reads.txt out.txt
```

will place the mapped reads in `out.txt` and test your implementation. The correct output of this command is given in `test_mapped.txt` for you to check the correctness of your implementation. Your implementations of the `_lf(self, idx, qc)` and `bounds(self, q)` functions are the answer to 1.1. **Submit fmindex.py.**

**(B) (2 pt.)** Now let’s make sure your implementation works on a larger genome. First you will build the FM-index. To build the index use the command:

```
% python fm-build.py yeast_chr1_10k.txt yeast_chr1_10k.index
```

Now let’s search using the FM index with the code you wrote, and use it to map some reads

To map the reads:

```
% python fm-search.py yeast_chr1_10k.index yeast_chr1_reads.txt mapped_reads.txt
```

View the output:

```
% more mapped_reads.txt
example mapped_reads.txt (you will not have this same read):
ATGGGTATCGATCACACTTCCAAGCAACAC count:1 matches:[561]
...
```

**Submit your mapped_reads.txt on course website as the answer to 1.2.**

---

---

[Up: contents](index.md) · [Problem 2. Library Complexity (5 points) →](02-problem-2-library-complexity-5-points.md)
