---
title: Problem 2. Gapped sequence alignment (6 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/01-questions-pset1-ans.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/01-questions-pset1-ans.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Problem 2. Gapped sequence alignment (6 points)

In this problem, you will use the algorithms discussed in class to find the optimal alignment for a pair of short peptides.

**(A) (1 pt.)** In order to perform this alignment, you must first choose a scoring matrix. For example, you could use a constant match and mismatch penalty of 1 and -1, respectively, so that $S_{ij} = 1$ if $i = j$ and $S_{ij} = -1$ otherwise. Is this a good idea? Why or why not? In one sentence, briefly describe how you might obtain a better scoring matrix for protein comparison.

No - not all amino acid substitutions are equally (dis)favored. Some changes will more heavily impact protein structure and function than others, and will therefore evolve less frequently, and so they should be scored differently. For example, changing from one medium-sized hydrophobic residue to another (e.g., Val to Ile or Leu) within a signal peptide or transmembrane helix is often tolerated, but changing a hydrophobic to a charged residue could disrupt function in these contexts, and changing a buried medium-sized hydrophobic residue like Val to a much larger residue (e.g., Trp) could disrupt packing. Instead, commonly used scoring matrices are created by comparing related protein sequences and seeing how often evolution has allowed particular substitutions occur - these matrices better capture proteins' functional constraints than this simple +1/-1 scoring scheme.

**(B) (1 pt.)** You decide to explore more commonly used protein alignment scoring matrices instead. Compare the score for aligning two tryptophans (W) to the score for aligning two alanines (A) in the PAM250 scoring matrix. Both of these alignments are "matches", so why are these scores so different?

W-W pairings have a large positive score, while A-A pairings have a small positive score. This means that tryptophan residues are generally highly conserved, and changes from tryptophan to another amino acid are rare (and therefore generally evolutionarily unfavorable). Conversely, alanine is not as strongly conserved and changes relatively frequently. From a biochemical perspective, this makes sense since alanine is very small and won't generally have a big impact on protein structure (and is similar to many other nonpolar amino acids), while tryptophan is very big and changing it to almost anything else could dramatically alter protein structure.

**(C) (2 pts.)** Perform a global alignment of the two peptides ATWES and TCAET, using the Needleman-Wunsch algorithm to fill out the alignment matrix below. Use the **BLOSUM62** scoring matrix and a linear gap penalty of 2.

After filling out the matrix, circle the traceback path and write the final alignment. If there are multiple traceback paths, write out all top-scoring alignments.

Using the BLOSUM62 matrix in the textbook or commonly found online:

| | Gap | A | T | W | E | S |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Gap** | **0** | **-2** | -4 | -6 | -8 | -10 |
| **T** | -2 | 0 | **3** | 1 | -1 | -3 |
| **C** | -4 | -2 | 1 | **1** | -1 | -2 |
| **A** | -6 | 0 | -1 | -1 | **0** | 0 |
| **E** | -8 | -2 | -1 | -3 | **4** | 2 |
| **T** | -10 | -4 | 3 | 1 | 2 | **5** |

The traceback is highlighted in gray above. The final alignment is:

```
A  T  W  -  E  S
-  T  C  A  E  T
```

Note: There was a slightly different version of the BLOSUM62 matrix on the lecture slides (the scoring matrix was created from a different set of aligned sequences). This does not change the traceback or final alignment, only a few scores as shown below. Full credit was given for either answer. Using the BLOSUM62 matrix in the lecture slides:

| | Gap | A | T | W | E | S |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Gap** | **0** | **-2** | -4 | -6 | -8 | -10 |
| **T** | -2 | 0 | **3** | 1 | -1 | -3 |
| **C** | -4 | -2 | 1 | **3** | 1 | 0 |
| **A** | -6 | 1 | -1 | 1 | **3** | 1 |
| **E** | -8 | -1 | 1 | -1 | **6** | 4 |
| **T** | -10 | -3 | 4 | 2 | 4 | **8** |

**(D) (2 pts.)** Different scoring matrices and gap penalties can give very different alignment results. Below is the alignment of the peptides from part (C) using the **PAM250** scoring matrix (same gap penalty). The traceback path is shaded.

| | Gap | A | T | W | E | S |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Gap** | **0** | -2 | -4 | -6 | -8 | -10 |
| **T** | -2 | **1** | 1 | -1 | -3 | -5 |
| **C** | -4 | **-1** | -1 | -3 | -5 | -3 |
| **A** | -6 | -2 | **0** | -2 | -3 | -4 |
| **E** | -8 | -4 | -2 | -4 | **2** | 0 |
| **T** | -10 | -6 | -1 | -3 | 0 | **3** |

What is the resulting alignment?

```
A  -  T  W  E  S
T  C  A  -  E  T
```

Compare the optimal alignments obtained using the BLOSUM62 and PAM250 scoring matrices. Why are they different?

The main reason the alignments are different is because of how strongly the C-W mismatch is penalized under the PAM250 matrix (score = -8), compared to in the BLOSUM62 matrix (score = -2). This means that under BLOSUM62 the C-W mismatch is tolerated without producing a gap, whereas under PAM250 a gap is preferred over the strong -8 penalty. Additionally, under PAM250, A-T pairings are more favorable (score = +1 vs. 0 for BLOSUM62).

---

[← Problem 1. Sequence search (6 points)](01-problem-1-sequence-search-6-points.md) · [Up: contents](index.md) · [Problem 3. Sequence similarity search statistics (7 points) →](03-problem-3-sequence-similarity-search-statistics-7-points.md)
