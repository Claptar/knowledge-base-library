---
title: Problem 6. Modeling and information content of sequence motifs (5 points).
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/02-questions-pset2-ques.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/02-questions-pset2-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Problem 6. Modeling and information content of sequence motifs (5 points).

To analyze gene evolution in three phylogenetic groups of protists, you collect samples of three different protist species, A, B, and C, that represent these lineages. You conduct both genome sequencing and cDNA sequencing from each and use spliced alignment of cDNAs to genomes to obtain sets of 10,000 confirmed 3' splice site (3'SS) sequences from each species. In all three species the invariant AG at the end of each intron is preceded by an 8 base polypyrimidine tract (PPT), with frequencies $f_C = f_T = \frac{1}{2}$ at each position. Your goal is to develop probabilistic models of the PPT motif in each species for use in exon-intron prediction. **Throughout this problem, unless instructed otherwise, you should describe the simplest possible model (fewest parameters) that accurately models the frequencies of all 8mers in the training data (and should therefore give good predictive accuracy). Information content of models should be calculated using the formula given in lecture: $I = 2w - H(\text{model})$, in bits, where $w$ is the width of the motif and $H(\text{model})$ is the Shannon entropy of the model. The abbreviation $\text{Y}_8$ refers to 8mers that consist exclusively of pyrimidine (C or T) nucleotides.**

**(A) (1 pt.)** In species A, all four dinucleotides CC, CT, TC, and TT occur equally often ($f_{CC} = f_{CT} = f_{TC} = f_{TT} = \frac{1}{4}$) at each of the seven pairs of positions $(1,2), (2,3), \dots, (7,8)$, and each 8mer of the form $\text{Y}_8$ occurs with frequency $2^{-8}$. In one sentence, describe a model for the PPT of species A. What is the information content of this model?

**(B) (1 pt.)** In species B, all four dinucleotides CC, CT, TC, and TT are equally likely ($f_{CC} = f_{CT} = f_{TC} = f_{TT} = \frac{1}{4}$) at each of the seven pairs of positions $(1,2), (2,3), \dots, (7,8)$, but examining the frequencies of 8mers reveals that $f_{T_8} = f_{C_8} = f_{(TC)_4} = f_{(CT)_4} = \frac{1}{4}$. In one sentence, describe a model for the PPT of species B. What is the information content of this motif?

**(C) (3 pt.)** In species C, $f_{CC} = f_{TT} = \frac{3}{8}$, $f_{TC} = f_{CT} = \frac{1}{8}$ at each of the seven pairs of consecutive positions $(1,2), (2,3), \dots, (7,8)$, and the frequencies of all 8mers of the form $\text{Y}_8$ are equal to $3^{a+b}/Z$ where $a$ is the number CC dinucleotides in the 8mer and $b$ is the number of TT dinucleotides in the 8mer, and $Z$ is the normalization constant that causes the frequencies to sum to 1. In one sentence, describe a model for the PPT of species B. What is the information content of this motif?

---

---

[← Problem 2. Library Complexity (5 points)](02-problem-2-library-complexity-5-points.md) · [Up: contents](index.md) · [(Extra 6.874 Problem) Multiple Hypothesis Testing (4 points) →](04-extra-6-874-problem-multiple-hypothesis-testing-4-points.md)
