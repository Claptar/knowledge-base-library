---
title: Why use the BWT?
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-26-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-02-26-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Why use the BWT?

| final char (L) | sorted rotations |
| :---: | :--- |
| a | n to decompress. It achieves compression |
| o | n to perform only comparisons to a depth |
| o | n transformation} This section describes |
| o | n transformation} We use the example and |
| o | n treats the right-hand side as the most |
| a | n tree for each 16 kbyte input block, enc |
| a | n tree in the output stream, then encodes |
| i | n turn, set $L[i]$ to be the |
| i | n turn, set $R[i]$ to the |
| o | n unusual data. Like the algorithm of Man |
| a | n use a single set of probabilities table |
| e | n using the positions of the suffixes in |
| i | n value at a given point in the vector $R |
| e | n we present modifications that improve t |
| e | n when the block size is quite large. Ho |
| i | n which codes that have not been seen in |
| i | n with $ch$ appear in the {\em same order |
| i | n with $ch$. In our exam |
| o | n with Huffman or arithmetic coding. Bri |
| o | n with figures given by Bell~\cite{bell}. |

Figure 1: Example of sorted rotations. Twenty consecutive rotations from the sorted list of rotations of a version of this paper are shown, together with the final character of each rotation.

© Digital Equipment Corporation. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Burrows, Michael, and David J. Wheeler. "A Block-sorting Lossless Data Compression Algorithm." (1994).

we have grouped together rotations of our "genome" by their suffixes, and stored information about this ordering (the BWT)

e.g. all the rotations beginning with "n with" are grouped together

Burrows M, Wheeler DJ: A block sorting lossless data compression algorithm. *Digital Equipment Corporation, Palo Alto, CA 1994, Technical Report 124; 1994*

---

## BWT and character rank

notice that each column and each row of the BW-matrix contains every letter from the input string

| rank? | | rank? |
| :---: | :--- | :---: | :---: |
| 1 | $BANANA | A | 1 |
| 1 | A$BANAN | N | 1 |
| 2 | ANA$BAN | N | 2 |
| 3 | ANANA$B | B | 1 |
| 1 | BANANA$ | $ | 1 |
| 1 | NA$BANA | A | 2 |
| 2 | NANA\$BA | A | 3 |

Burrows Wheeler matrix
Burrows Wheeler transform

- what do we mean by a character's **rank** in a column?
- the **rank** of a specific character *qc* is the number of *qc*s above it in the column, +1
- note that (for example) the "A" of rank 2 in the last column (BWT) and first column are the same lexical occurrence (the A preceded by "BAN" and followed by "NA")
- this lets us distinguish between the different "A" characters that occur in different contexts in the original string:

$$\text{B A N A N A}$$
$$\text{rank in BWT? } \quad 3 \quad 2 \quad 1$$

- so, chars in the **First** and **Last** columns have the same rank

---

## Last to First (LF) function

$$\text{LF}(i, qc) = \text{occ}(qc) + \text{count}(i, qc)$$

returns the index of the char in the First column that is **lexically equivalent** to the instance of *qc* in position $i$ of the BWT, using the fact that **rank** is same in First and Last columns

**$\text{occ}(qc)$** = # characters lexically smaller than *qc* in the BWT (e.g. rank in **First** column of matrix)

**$\text{count}(i, qc)$** = # of *qc* characters before position $i$ in the BWT (e.g. rank of *qc* character at position $i$, minus 1)

| idx | BWT |
| :---: | :--- |
| 0 | $ B A N A N A |
| 1 | A $ B A N A N |
| 2 | A N A $ B A **N** |
| 3 | A N A N A $ B |
| 4 | B A N A N A $ |
| 5 | N A $ B A N A |
| 6 | **N** A N A $ B A |

What is the output of LF(2, 'N')? 6
$\text{occ}(\text{'N'})$? 5
$\text{count}(2, \text{'N'})$? 1

**Note:** the character at position $i\$ in the BWT does not need to be *qc*! For example, what is:

$$\text{LF}(0, \text{'N'}) \quad 5 \quad (=5+0)$$

---

## Last to First (LF) function

$$\text{LF}(i, qc) = \text{occ}(qc) + \text{count}(i, qc)$$

returns the index of the char in the First column that is **lexically equivalent** to the instance of *qc* in position $i$ of the BWT, using the fact that **rank** is same in First and Last columns

**$\text{occ}(qc)$** = # characters lexically smaller than *qc* in the BWT (e.g. rank in **First** column of matrix)

**$\text{count}(i, qc)$** = # of *qc* characters before position $i$ in the BWT (e.g. rank of *qc* character at position $i$, minus 1)

| idx | BWT |
| :---: | :--- |
| 0 | $ B A N A N A |
| 1 | A $ B A N A N |
| 2 | A N A $ B A N |
| 3 | A N A N A $ B |
| 4 | B A N A N A $ |
| 5 | N A $ B A N A |
| 6 | N A N A $ B A |

In other words, since the first column is alphabetical, we first find the row where our character starts in the First column (e.g. Ns begin at index 5), then use the fact that rank is same in first and last column to find the specific char in First col that is the same lexical occurrences as our query in the BWT

---

## Using the BWT and LF function to do exact matching

- say we have the following sequence: $ABBABA, and we want to find occurrences of BBA
- using the BW-matrix, we can start by finding all rows beginning with "A"

$ A B B A B A
**A** $ A B B A **B**
**A** B A $ A B **B**
**A** B B A B A **$**
B A $ A B B A
B A B A $ A B
B B A B A $ A

but, we're only interested in rows where the A is preceded by a B

$ A B B A B A
A $ A B B A B
A B A $ A B B
A B B A B A $
**B** A $ A B B A
**B** A B A $ **A B**
B B A B A $ A

and now, we only want suffixes where the B is preceded by another B

Once we know where our matches to our query begin in the BWT, use LF to get these locations in original string

To make this clearer, we showed the entire BW matrix. But how to do this if we only have the BWT?
- use the LF function!

http://www.cs.jhu.edu/~langmea/resources/lecture_notes/bwt_and_fm_index.pdf

---

---

[← Library Complexity: Naïve approach](02-library-complexity-naïve-approach.md) · [Up: contents](index.md) · [Using the BWT and LF function to do exact matching →](04-using-the-bwt-and-lf-function-to-do-exact-matching.md)
