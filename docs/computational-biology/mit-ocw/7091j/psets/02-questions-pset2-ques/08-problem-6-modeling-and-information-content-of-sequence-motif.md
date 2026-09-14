---
title: Problem 6. Modeling and information content of sequence motifs (5 points).
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/02-questions-pset2-ques.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 6. Modeling and information content of sequence motifs (5 points).

**Source:** `psets/02-questions-pset2-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

To analyze gene evolution in three phylogenetic groups of protists, you collect samples of three different protist species, A, B, and C, that represent these lineages. You conduct both genome sequencing and cDNA sequencing from each and use spliced alignment of cDNAs to genomes to obtain sets of 10,000 confirmed 3' splice site (3'SS) sequences from each species.  In all three species the invariant AG at the end of each intron is preceded by an 8 base polypyrimidine tract (PPT), with frequencies fC = fT = 1 at each position.  Your goal is to develop probabilistic models 2 of the PPT motif in each species for use in exon-intron prediction.  Throughout this problem, <u>unless instructed otherwise, you should describe the simplest possible model (fewest parameters) that accurately models the frequencies of all 8mers in the training data (and should therefore give good predictive accuracy). Information content of models should be calculated using the formula given in lecture: I = 2w – H(model), in bits, where w is the width of the motif and H(model) is the Shannon entropy of the model. The abbreviation Y8 refers to 8mers that consist exclusively of pyrimidine (C or T) nucleotides.</u>

**(A) (1 pt.)** In species A, all four dinucleotides CC, CT, TC, and TT occur equally often 1 (𝑓𝐶𝐶 = 𝑓𝐶𝑇 = 𝑓𝑇𝐶 = 𝑓𝑇𝑇 = 4 ~~)~~ at each of the seven pairs of positions (1,2), (2,3),…,(7,8), and each 8mer of the form Y8 occurs with frequency 2<sup>-8</sup> .  In one sentence, describe a model for the PPT of species A.  What is the information content of this model?

**(B) (1 pt.)** In species B, all four dinucleotides CC, CT, TC, and TT are equally likely 1 (𝑓𝐶𝐶 = 𝑓𝐶𝑇 = 𝑓𝑇𝐶 = 𝑓𝑇𝑇 = 4 ~~)~~ at each of the seven pairs of positions (1,2), (2,3),…,(7,8), 1 but examining the frequencies of 8mers reveals that 𝑓𝑇8 = 𝑓𝐶8 = 𝑓(𝑇𝐶)4 = 𝑓(𝐶𝑇)4 = 4 ~~.~~ In one sentence, describe a model for the PPT of species B.  What is the information content of this motif?

8

3 1 **(C) (3 pt.)** In species C, 𝑓𝐶𝐶 = 𝑓𝑇𝑇 = , 𝑓𝑇𝐶 = 𝑓𝐶𝑇 = at each of the seven pairs of 8 8 consecutive positions (1,2), (2,3),…,(7,8), and the frequencies of all 8mers of the form Y8 are equal to 3<sup>a+b</sup> /Z where a is the number CC dinucleotides in the 8mer and b is the number of TT dinucleotides in the 8mer, and Z is the normalization constant that causes the frequencies to sum to 1.  In one sentence, describe a model for the PPT of species B. What is the information content of this motif?

9

---

[← Problem 5. de Bruijn graphs (5 points)](07-problem-5-de-bruijn-graphs-5-points.md) · [Up: contents](index.md) · [(Extra 6.874 Problem) Multiple Hypothesis Testing (4 points) →](09-extra-6-874-problem-multiple-hypothesis-testing-4-points.md)
