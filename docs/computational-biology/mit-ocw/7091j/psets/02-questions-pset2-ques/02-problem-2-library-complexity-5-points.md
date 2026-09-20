---
title: Problem 2. Library Complexity (5 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/02-questions-pset2-ques.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/02-questions-pset2-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Problem 2. Library Complexity (5 points)

Imagine you are responsible for sequencing DNA samples for your lab's latest important experiment. Using extensive simulations, you know that you need to observe at least 12 million unique molecules in order to test your current hypothesis. From previous experience, you know that each time a DNA library is constructed from a sample, it will contain exactly 40 million unique molecules (selected perfectly at random). You also know that *C. elegans*, your model organism, has a genome size of approximately 100 million base pairs.

You can have your sample sequenced in units called lanes. Each lane gives you 10 million reads, and a library can be sequenced on as many lanes as you want. However, ever-protective of your grant money, you want to achieve your experimental goals in the most efficient way possible. Suppose that each sample collection and library preparation step costs $500 and that each sequencing lane costs $1000.

**(A) (2 pt.)** Assume that each molecule in the library had equal probability of being sequenced. What is the most cost-effective experimental design (number of libraries and lanes sequenced for each library) for achieving your goal of observing 12 million unique molecules? Show your work.

**(B) (3 pt.)** Now suppose that there is variation in the selection probabilities across each molecule, which follows a negative binomial distribution with rate $\text{lambda} = 0.25$ (10 million reads divided by 40 million molecules) and variance factor $k = 2$ (estimated from previous experiments). What is the most cost-effective experimental design for this situation? Show your work and comment on any differences between the two cases.

*Hint:* A more common formulation of the negative binomial distribution is in terms of failures $n$ and a success probability $p$. This conversion is found in the lecture slides.

---

## Problem 3. Differential gene expression (4 points)

You are analyzing RNA-seq data to identify differentially expressed genes between two treatment conditions. You have three biological replicates in each of the two conditions for a total of 6 samples, and you process and sequence each of the samples separately.

**(A) (1 pts)** Imagine you first pool the sequencing results for each of the conditions, resulting in two pools. What kind of variation have you lost the ability to observe, and why might this variation be important?

**(B) (3 pts)** Devise an improved analysis strategy for these six samples and identify the sources of variation it can detect. Identify how you would estimate the mean-dispersion function for use in a negative binomial model of variation.

---

## Problem 4. RNA Isoform quantification (3 points)

Consider the gene structure in the above figure.

Fig. 1

**Fig. 1**

Exon numbers and sizes in nucleotides are indicated. The transcript can initiate at either of the arrows shown, and exons 2 and/or 3 can be spliced out.

**(A) (1 pt.)** How many possible isoforms of this gene could exist?

**(B) (1 pt.)** For each isoform, list the junction spanning RNA-seq reads that would support it.

**(C) (1 pt.)** Assuming single ended reads, what is the shortest read length that would guarantee the ability to unambiguously identify all isoforms of this gene if we require that a junction read must have minimum overlap of 5bp with each exon?

---

## Problem 5. de Bruijn graphs (5 points)

Suppose you are interested in sequencing a particular RNA sequence. You opt to take a next generation sequencing approach and submit your sample to your local sequencing facility. You receive the following set of 6 bp reads in return, which are all in the same orientation.

AGCTGT, CAGCTG, TTCTGC, GCTGTA, TCAGCT, CTGTAT, TGTAGC, TTCAGC, CTGTAG, TTTCAG

**(A) (1 pt.)** Construct the corresponding de Bruijn graph with $k = 5$

**(B) (1 pt.)** Simplify any chains in the graph. Remove any tips present in the graph.

**(C) (1 pt.)** Identify any bubbles in the graph. Resolve the bubbles by removing the path most likely to be caused by a sequencing error.

**(D) (1 pt.)** Which read(s) contain sequencing errors? Identify the error(s).

**(E) (1 pt.)** Write the sequence represented by the de Bruijn graph after the error correction steps.

---

---

[← 02 questions pset2 ques Part 01 —](01-02-questions-pset2-ques-part-01.md) · [Up: contents](index.md) · [Problem 6. Modeling and information content of sequence motifs (5 points). →](03-problem-6-modeling-and-information-content-of-sequence-motif.md)
