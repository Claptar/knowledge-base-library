---
title: Introduction
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/psets/01-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `psets/01-questions.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# 6.047/6.878/HST.507

Fall 2015 Problem Set 1: Aligning and Modeling Genomes

Due: Wednesday, September 30 at 8pm (submit on the course website)

When you submit this pset, please turn in the following files in a zip file:

- Your answers to the problem set questions in a pdf file

- A directory named “code” with all the code you are submitting

- A directory named “data” with all other results you are submitting

In your answers to the questions please refer to the appropriate file name where your results/code for that problem are located.

1. **Evolutionary distances of orthologs and paralogs**

In this problem, you will implement the Needleman-Wunsch algorithm for pairwise sequence alignment, apply it to the protein-coding sequences of related genes from several mammalian genomes, and use the results to learn about their evolution.

- (a) On the class web site, we have provided a python skeleton program `ps1-seqalign.py` , which you will complete. We provide a traceback routine, but you will write the code to fill in the score and traceback matrices. The skeleton program specifies a substitution matrix and gap penalty. If you so choose, you may rewrite the program in any programming language. Please submit (1) the portion of the code that you wrote; (2) an optimal alignment of the two sequences `CTAAGTACT` and `CATTA` , and the corresponding score matrix F with the optimal path indicated; and (3) the score of the alignment of the human and mouse HoxA13 genes, which we also provide on the web site. The command to run the program is: `python ps1-seqalign.py <FASTA 1> <FASTA 2>`

The Hox cluster is a set of genes that are crucial in determining body plan formation during embryo development. They are found in all bilateral animals, in species as distant as the fruit fly. The fruit fly has one Hox cluster, while most vertebrates have four. It is thought that vertebrates have undergone two rounds of whole-genome duplication, giving rise to four Hox clusters from the ancestral one, although the hypothesis remains controversial.

In the remainder of this problem, you will use your Needleman-Wunsch alignment program to analyze the sequences of several Hox genes, and estimate the date of the most recent vertebrate whole-genome duplication. In particular, we are interested in using the N-W alignment score as a distance metric between two sequences.

- (b) Make minor adjustments to your alignment program so that the score it computes can be interpreted as a distance metric. That is, the score of a sequence aligned with itself should be zero, all scores should be non-negative, and sequences that are more dissimilar should be given a score with a greater magnitude. Describe the changes you made in your handin; no code is necessary.

- (c) Apply your modified program to compute a distance between the human HoxA13 gene and the mouse HoxA13 gene.

- (d) The modern mammalian genes HoxA13 and HoxD13 arose from a single ancestral gene by wholegenome duplication, long before the human-mouse divergence. We provide the sequences of the human and mouse HoxD13 genes on the web site. Given that the fossil record shows that human and mouse diverged about 70 million years ago, use your distance metric and your results from part (c) to estimate the date of the whole-genome duplication that gave rise to HoxA13 and HoxD13. Make sure to state the assumptions underlying your estimate.

1

**6.047/6.878/HST.507 Fall 2015**

**Problem Set 1**

---

[Up: contents](index.md) · [2. Sequence hashing and dotplot visualization →](02-2-sequence-hashing-and-dotplot-visualization.md)
