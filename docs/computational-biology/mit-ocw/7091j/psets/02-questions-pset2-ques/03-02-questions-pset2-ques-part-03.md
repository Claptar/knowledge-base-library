---
title: 02 questions pset2 ques Part 03 —
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/02-questions-pset2-ques.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 02 questions pset2 ques Part 03 —

**Source:** `psets/02-questions-pset2-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For this exercise you will be implementing the core of a genome search function utilizing the Burrows Wheeler transform (BWT) and an FM-index.  We have provided scaffolding code so that you can focus on the core of the algorithm.   Please do not use Internet search tools to try to solve this problem – the point is for you to understand how the algorithm works.

You will need the coding and testing files from the course website (keep them in the same folder). This includes scaffold code, a 10kb segment of the yeast genome, reads which you will map to the genome, and an index for testing with correct output.

- **(A) (7 pt.)** Complete the LF mapping code in the _lf(self, idx, qc) function and the search code in the bounds(self, q) function (both in fmindex.py).

To test your implementations we have provided the FM-index of an abbreviated version of the yeast genome in test.index. Running

**_%_** _python fm-search.py test.index yeast_chr1_reads.txt out.txt_

will place the mapped reads in out.txt and test your implementation. The correct output of this command is given in test_mapped.txt for you to check the correctness of your implementation.  Your implementations of the _lf(self, idx, qc) and bounds(self, q) functions are the answer to 1.1. **Submit** fmindex.py.

- **(B) (2 pt.)** Now let’s make sure your implementation works on a larger genome.   First you will build the FM-index.   To build the index use the command:

**_%_** _python fm-build.py yeast_chr1_10k.txt yeast_chr1_10k.index_

Now let’s search using the FM index with the code you wrote, and use it to map some reads

To map the reads:

**_%_** _python fm-search.py yeast_chr1_10k.index yeast_chr1_reads.txt mapped_reads.txt_

View the output:

**%** more mapped_reads.txt example mapped_reads.txt (you will not have this same read): ATGGGTATCGATCACACTTCCAAGCAACAC count:1 matches:[561] …

**Submit** your mapped_reads.txt on course website as the answer to 1.2.

2

---

[← Python Scripts](02-python-scripts.md) · [Up: contents](index.md) · [Problem 2. Library Complexity (5 points) →](04-problem-2-library-complexity-5-points.md)
