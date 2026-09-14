---
title: Problem 2. Gapped sequence alignment ( 6 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/01-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 2. Gapped sequence alignment ( 6 points)

**Source:** `psets/01-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<mark>In this problem, you will use the algorithms discussed in class to find the optimal alignment for a pair of short peptides.</mark>

**<mark>(A) (</mark> 1 pt.)** <mark>In order to perform this alignment, you must first choose a scoring matrix.  For example, you could use a constant match and mismatch penalty of 1 and -1, respectively, so that S!" = 1 if</mark> _<mark>i</mark>_ <mark>=</mark> _<mark>j</mark>_ <mark>and S!" = −1 otherwise.  Is this a good idea?</mark> Why or why not? In one sentence, briefly describe how you might obtain a better scoring matrix for protein comparison.

**<mark>(B)</mark> (1 pt.)** <mark>You decide to explore more commonly used protein alignment scoring matrices instead. Compare the score for aligning two tryptophans (W) to the score for aligning two alanines (A) in the PAM250 scoring matrix.  Both of these alignments are “matches”, so why are these scores so different?</mark>

4

**<mark>(C) (</mark> 2 pts.)** <mark>Perform a</mark> **<mark>global</mark>** <mark>alignment of the two peptides ATWES and TCAET, using the Needleman-Wunsch algorithm to fill out the alignment matrix below.  Use the</mark> **<mark>BLOSUM62</mark>** <mark>scoring matrix and a linear gap penalty of 2.</mark>

<mark>After filling out the matrix, circle the traceback path and write the final alignment.  If there are multiple traceback paths, write out all top-scoring alignments.</mark>

||Gap|A|T|W|E|S|
|---|---|---|---|---|---|---|
|Gap|0||||||
|T|||||||
|C|||||||
|A|||||||
|E|||||||
|T|||||||


Final Alignment:

5

**<mark>(D)</mark>** ( **2 pts.)** <mark>Different scoring matrices and gap penalties can give very different alignment results. Below is the alignment of the peptides from part (C) using the</mark> **<mark>PAM250</mark>** <mark>scoring matrix (same gap penalty). The traceback path is shaded.</mark>

||Gap|A|T|W|E|S|
|---|---|---|---|---|---|---|
|Gap|0|-2|-4|-6|-8|-10|
|T|-2|**1**|1|-1|-3|-5|
|C|-4|**-1**|-1|-3|-5|-3|
|A|-6|-2|**0**|**-2**|-3|-4|
|E|-8|-4|-2|-4|**2**|0|
|T|-10|-6|-1|-3|0|3|


<mark>What is the resulting alignment?</mark>

<mark>Compare the optimal alignments obtained using the BLOSUM62 and PAM250 scoring matrices. Why are they different?</mark>

6

**<mark>Problem 3.  Sequence similarity search statistics</mark> (7 points)** <mark>You are conducting local nucleotide sequence alignments with your favorite local alignment tool (e.g. BLAST) with match and mismatch scores of +1 and -1 respectively.  You align a 100bp query sequence to a 1Mbp genome and find that a 20-nt subsequence from your query is a perfect match.</mark>

<mark>For each of the following cases, calculate the significance of a 20-nt perfect match (assume</mark> _<mark>K</mark>_ <mark>= 1 in each case):</mark>

**<mark>(A) (</mark> 2 pts.)** <mark>Query sequence and genome both have approximately balanced base composition A=C=G=T=25%).</mark>

**(B) (1 pt.)** <mark>Query sequence and genome are both</mark> highly A-T rich (A=T=40%, C=G=10%).

7

**<mark>(C) (</mark> 1 pt.)** <mark>Query is moderately</mark> **<mark>A+T</mark>** <mark>-rich (A = T = 30%, C = G = 20%) but genome is moderately</mark> **<mark>C+G</mark>** <mark>-rich (A = T = 20%, C = G = 30%).</mark>

**<mark>(D) (</mark> 1 pt.)** <mark>Briefly explain why the ordering of the P-values from (A) - (C) makes sense.</mark>

8

**<mark>(E)</mark> (2 pts.)** <mark>Design a new scoring system for application to searching a 20 nt query of unbiased composition against a highly A+T-rich genome (as in (B) above) that will increase the sensitivity for detection of matches to that genome by drawing lines from each box on the left to its new score in the right box (+1, 0, or -1 for different types of matches/mismatches). What would the P- value of a perfect match to this query (with 5 A’s, 5 C’s, 5 G’s, 5 T’s) be using your new scoring system?</mark>

|A/A or T/T match|+1|
|---|---|
|C/C or G/G match|0|
|mismatch|-1|


9

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology

Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Due: Thursday, February 20th at noon.](02-due-thursday-february-20th-at-noon.md) · [Up: contents](index.md)
