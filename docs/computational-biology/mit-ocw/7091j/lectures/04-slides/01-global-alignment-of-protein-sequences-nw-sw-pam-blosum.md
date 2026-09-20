---
title: Global Alignment of Protein Sequences (NW, SW, PAM, BLOSUM)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/04-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/04-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Global Alignment of Protein Sequences (NW, SW, PAM, BLOSUM)

7.91 / 7.36 / 20.490 / 20.390 /
6.874 / 6.801 / HST.506

C. Burge Lecture #6
Feb 13, 2014

Comparative Genomics

---

- Global sequence alignment (Needleman-Wunch-Sellers)
- Gapped local sequence alignment (Smith-Waterman)
- Substitution matrices for protein comparison

Background: Z&B Chapters 4,5 (esp. pp. 119-125)

---

## DNA Sequence Evolution

Generation $n-1$ (grandparent)
```
5' TGGCATGCACCCTGTAAGTCAATATAAATGGCTACGCCTAGCCCATGCGA 3'
   ||||||||||||||||||||||||||||||||||||||||||||||||||
3' ACCGTACGTGGGACATTCAGTTATATTTACCGATGCGGATCGGGTACGCT 5'
```

Generation $n$ (parent)
```
5' TGGCATGCACCCTGTAAGTCAATATAAATGGCTATGCCTAGCCCATGCGA 3'
   ||||||||||||||||||||||||||||||||||||||||||||||||||
3' ACCGTACGTGGGACATTCAGTTATATTTACCGATACGGATCGGGTACGCT 5'
```

Generation $n+1$ (child)
```
5' TGGCATGCACCCTGTAAGTCAATATAAATGGCTATGCCTAGCCCGTGCGA 3'
   ||||||||||||||||||||||||||||||||||||||||||||||||||
3' ACCGTACGTGGGACATTCAGTTATATTTACCGATACGGATCGGGCACGCT 5'
```

Images of The Simpsons © FOX. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Markov Model (aka Markov Chain)

**Stochastic Process:**
- a random process or
- a sequence of Random Variables

### Classical Definition

A discrete stochastic process $X_1, X_2, X_3, \dots$
which has the Markov property:

$$P(X_{n+1} = j \mid X_1=x_1, X_2=x_2, \dots X_n=x_n) = P(X_{n+1} = j \mid X_n=x_n)$$

(for all $x_i$, all $j$, all $n$)

### In words:

A random process which has the property that the future (next state) is conditionally independent of the past given the present (current state)

Andrey Markov, a Russian mathematician (1856 - 1922)

Image is in the public domain.

---

## Markov Model Example

Genotype at the Apolipoprotein locus (alleles A and a) in successive generations of boxed Simpson lineage forms a Markov model

**Past**
- Grandpa Simpson
- Grandma Simpson

**Present**
- Homer
- Marge

**Future**
- Bart

This is because, e.g., Bart's genotype is conditionally independent of Grandpa Simpson's genotype given his father Homer's genotype:

$$P(\text{Bart} = \text{a/a} \mid \text{Grandpa} = \text{A/a} \ & \ \text{Homer} = \text{a/a}) = P(\text{Bart} = \text{a/a} \mid \text{Homer} = \text{a/a})$$

Images of The Simpsons © FOX. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Review: Vector/Matrix Notation for Markov Chains

Assuming no selection

$S_n =$ base at generation $n$

$$P_{ij} = P(S_{n+1} = j \mid S_n = i)$$

$$P = \begin{pmatrix} P_{AA} & P_{AC} & P_{AG} & P_{AT} \\ P_{CA} & P_{CC} & P_{CG} & P_{CT} \\ P_{GA} & P_{GC} & P_{GG} & P_{GT} \\ P_{TA} & P_{TC} & P_{TG} & P_{TT} \end{pmatrix}$$
(from: A, C, G, T; to: A, C, G, T)

$\vec{q}^{\;n} = (q_A^n, q_C^n, q_G^n, q_T^n) =$ vector of prob's of bases at gen. $n$

Handy relations:
\$\$\vec{q}^{\;n+1} = \vec{q}^{\;n} P \qquad \vec{q}^{\;n

miR-1 8mer site in SLC35B4

Branch length $= 0.07 + 0.20 + 0.05 + 0.05$
$+ 0.21 + 0.19 + 0.06 + 0.07$
$+$ six smaller branch lengths
$= 1.0$

## Using a similar branch length conservation measure to assess and classify mammalian miRNA target sites

Freely available online through the Genome Research Open Access option. License: CC-BY-NC.
Source: Friedman, Robin C., Kyle Kai-How Farh, et al. "Most Mammalian MRNAs are Conserved Targets of MicroRNAs." *Genome Research* 19, no. 1 (2009): 92-105.

Friedman et al Genome Res 2009

---

## Identifying a family of genes (cas) associated with a bacterial repeat structure (CRISPR)

© Society for General Microbiology. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Bolotin, Alexander, Benoit Quinquis, et al. "Clustered Regularly Interspaced Short Palindrome Repeats(CRISPRs) have Spacers of Extra-chromosomal Origin." *Microbiology* 151, no. 8 (2005): 2551-61.

© Blackwell Science Ltd. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: Jansen, Ruud, Jan Embden, et al. "Identification of Genes that are Associated with DNA Repeats in Prokaryotes." *Molecular Microbiology* 43, no. 6 (2002): 1565-75.

Jansen et al Mol Microbiol 2002

---

## CRISPR spacers match phage genomes

**Fig. 4.** Localization of spacer-matching sequences along the phage Sfi21 genome. The phage genetic map is drawn after GenBank entry NC_000872 (ORFs are shown as arrows), the regions involved in different stages of phage development, identified by comparative analysis (Desiere *et al.*, 2002), are indicated above the map, and the scale (in kb) below it. Phage regions having a BLAST E score $< 0 \cdot 001$ with the CRISPR spacers are indicated by the diamonds placed above or below the map, denoting homology with the top or the bottom DNA strand, respectively.

---

[Up: contents](index.md) · [Number of spacers is correlated with resistance to phage →](02-number-of-spacers-is-correlated-with-resistance-to-phage.md)
