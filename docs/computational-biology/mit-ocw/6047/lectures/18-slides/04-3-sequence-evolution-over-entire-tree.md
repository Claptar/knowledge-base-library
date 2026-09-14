---
title: 3. Sequence evolution over entire tree
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/18-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Sequence evolution over entire tree

**Source:** `lectures/18-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Assume branch independence

   - P(x1, …xn, …, x2n-1|T, **t** ) = P(x2n-1)Πi P(xi|xparent(i), ti)

- Assume prior on root sequence, e.g.

   - P(x2n-1) = P(x2n-1,j) = (1/4)^m  for sequence length m

Use product and prior to define **sequence evolution over tree:**

###### **x9 = “AAACTG”**


<!-- Start of picture text -->
t8<br>x8<br>t6 t7 P(x1, …xn, …, x2n-1|T,  t )<br>t1 x6 x7<br>t2 t3 t4 t5<br>x1 x2 x3 x4 x5<br><!-- End of picture text -->

63

4. Integrate (marginalize) over hidden ancestral seqs!

   - Notice, all sequences are needed, both internal nodes and leaves – P(x1, …xn, …, x2n-1|T, **t** )

   - But, only leaves are given: x1, …xn

   - Therefore, need to marginalize (sum) over unknowns: xn+1, …, x2n-1

   - This looks expensive!


<!-- Start of picture text -->
x9 = “AAACTG”<br>t )<br>t8<br>x8<br>t6 t7<br>t1 x6 x7<br>t2 t3 t4 t5<br>x1 x2 x3 x4 x5<br><!-- End of picture text -->

   - P(x1, …xn|T, **t** ) = Σxn+1, …, Σ x2n-1 P(x1, …xn, …, x2n-1|T, **t** )

- Don’t worry, dynamic programming can do it efficiently.

64

## Basic trick to efficient marginalization

**Apply factorization trick to every internal node in the tree.** P(x1,x2,x3,x4|T, **t** ) = Σx5Σx6Σx7 P(x1,x2,x3,x4,x5,x6,x7|T, **t** ) = Σx5Σx6Σx7 P(x1|x5,t1) P(x2|x5,t1) P(x3|x6,t3) P(x4|x6,t4) P(x5|x7,t5) P(x6|x7,t6) P(x7) = Σx7 P(x7) t4 4 [Σx5 P(x5|x7,t5) P(x1|x5,t1) P(x2|x5,t1)] [Σx6 P(x6|x7,t6) P(x3|x6,t3) P(x4|x6,t4)]


<!-- Start of picture text -->
x7<br>t5 t6<br>x5  x6<br>t1 t2  t3 t4 4<br>x1 x2 x3 x4<br><!-- End of picture text -->

# Peeling algorithm

- L(i,j,a) is the DP table.

- Each entry contains the probability of seeing the leaf data below node i, given that node i has base a at site j.

- The leaves of the table are initialized based on the observed sequence. Entries populated in post-order traversal.

- Runtime: O(2n * k^2)

65

#### **Use DP to compute argmax P(D|B,T) efficiently**


<!-- Start of picture text -->
Li[a]<br>Char  a  at node  i<br><!-- End of picture text -->


<!-- Start of picture text -->
tleft tright<br>b at j  c at j<br>Lj[b] Lk[c]<br><!-- End of picture text -->

- If we know the branch lengths tleft & tright.

- • And we already have the likelihood tables Lj&Lk of left and right subtrees

   - (for each possible ending character at **b** , **c** )

-  Fill in likelihood table Li for each char **a** at i


<!-- Start of picture text -->
L i  Lj  Lk<br>A<br>P(.|‘C<br>C<br>’)<br>G<br>T<br><!-- End of picture text -->

Li[a] = Σb{ACGT} Σc{ACGT} (  P(b|a,tleft)*Lleft[b] * P(c|a,tright)*Lright[c]  )

**Prob(a**  **b) Prob(a**  **c)**

66

#### **Initialization and Termination**

###### Root

###### Internal Nodes

###### Leaves

||**2n-1**|**…**|**…**|**…**|**i**|**j**|**k**|**…**|n+1|**n**|**…**|**3**|**2**|**1**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|A||||||||||0|0|1|0|0|
|C||||||||||1|0|0|0|1|
|G||||||||||0|0|0|0|0|
|T||||||||||0|1|0|1|0|


- Characters at the leaves are already known – Their likelihood is 1 or 0, indicating the known char

- Fill in internal node likelihood vectors iteratively

- Once we reach the root, multiply by the base freqs

- Maximization over Topologies and Lengths

   -  Numerical: gradient descent, Newton’s method

67

#### **Advantages/disadvantages of ML/MAP methods**

- **Advantages:**

   - Inherently statistical and evolutionary model-based.

   - Usually the most ‘consistent’ of the methods available.

   - Used for both character and rate analyses

   - Can be used to infer the sequences of the extinct ancestors.

   - Account for branch-length effects in unbalanced trees.

   - Nucleotide or amino acid sequences, other types of data.

- **Disadvantages:**

   - Not as intuitive as parsimony (e.g. may choose more events if they’re more likely in our probabilistic model)

   - Computationally intense (Iimits num taxa, sequence length).

   - Like parsimony, can be fooled by high levels of homoplasy.

   - Violations of model assumptions can lead to incorrect trees.

68

#### **Tree reliability: Bootstrapping**

1. Re-sample alignments:

– Randomly sample alignment columns with replacement

– Create many alignments of equal size.

2. Build a phylogenetic tree for each sample

3. Repeat (1) and (2) many times – 1000s of times

4. Output summary tree

   - Tree constructed most frequently

   - – Consensus tree (even if not most freq)

   - Other options

5. Report observation frequency of each branch

   - Each branch is a binary split

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.69

#### **Goals for today: Phylogenetics**

- **Basics of phylogeny: Introduction and definitions** – Characters, traits, nodes, branches, lineages, topology, lengths

   - Gene trees, species trees, cladograms, chronograms, phylograms

**1. From alignments to distances: Modeling sequence evolution** –

1 Turning pairwise sequence alignment data into pairwise distances

   - Probabilistic models of divergence: Jukes Cantor/Kimura/hierarchy

**2. From distances to trees: Tree-building algorithms**

2

   - Tree types: Ultrametric, Additive, General Distances

   - – Algorithms: UPGMA, Neighbor Joining, guarantees and limitations

   - Optimality: Least-squared error, minimum evolution (require search)

**3. From alignments to trees: Alignment scoring given a tree**

-

- 3 Parsimony: greedy (union/intersection) vs. DP (summing cost)

   - ML/MAP (includes back-mutations, lengths): peeling algorithm (DP)

4. Tree of Life in Genomic Era

- The prokaryotic problem (no real taxa and HGT)

- 4 – Interpreting the forest of life

70

#### **Tree of Life in Genomic Era**

Genomic era – growing frustration with discrepancies between the trees reconstructed for individual genes and heroic efforts to overcome the noise. Role of horizontal gene transfer in the evolution of prokaryotic genomes is established.

Major lines of approach:

- gene repertoire and gene order

- distribution of distances between orthologs

- concatenated alignments of "non-transferable" gene cores

- consensus trees and supertrees


**Ciccarelli 2006.** _Towards automatic reconstruction of a highly resolved tree of life_ . Science 311, 1283-1287 [Figure 2]

Courtesy of Yuri Wolf; slide in the public domain.

Image in the public domain.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014 71

**Tree of Life, Rejected** Troubled times – "uprooting" of TOL for prokaryotes.

- horizontal gene transfer is rampant; no gene is exempt

- histories of individual genes are non-coherent with each other

- vertical signal is completely lost (or never existed at all)

- there are no species (or other taxa) in prokaryotes


<!-- Start of picture text -->
• a consistent signal we observe is created by biases in HGT<br>"Standard Model"  Eukaryotes  "Net of Life"  Eukaryotes<br>Bacteria  Archaea  Bacteria  Archaea<br><!-- End of picture text -->

**Doolittle 2000.** _Uprooting the tree of life_ . Sci. Am. 282, 90-95 [modified]

© Scientific American, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Doolittle, W. Ford. "Uprooting the tree of life." Scientific American 282, no. 2 (2000): 90.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014

Courtesy of Yuri Wolf; slide in the public domain.

72

#### **Forest of Life – Methods**

Source data and basic analysis methods:

- 100 hand-picked microbial genomes (41 archaea and 59 bacteria) representing a "fair" sample of prokaryote diversity (as known in 2008)

- clusters of orthologous genes (NCBI COGs and EMBL EggNOGs)

- multiple protein sequence alignments → index orthologs → ML phylogenetic trees

- 6901 trees cover 4-100 species; of them 102 cover 90-100 species (Nearly Universal Trees)

- direct tree comparison (distances between trees)

- quartet decomposition; analysis of quartet spectra

- simulation evolutionary models

Courtesy of Yuri Wolf; slide in the public domain.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014 73

#### **Forest of Life – Analysis**


<!-- Start of picture text -->
1<br>random<br>0.5<br>NUTs<br>0<br>IS<br>COG0541 COG0532 COG0092 COG0100 COG0090 COG0528 COG0096 COG0525 COG0051 COG0452 COG0495 COG0172 COG0089 COG0522 COG0124 COG0185 COG0094 COG0126 COG0519 COG0540 COG0149 COG0198 COG0177 COG0057 COG0009 COG0537<br><!-- End of picture text -->


NUTs are much closer to each other than expected by chance

NUTs form a tightly connected network when clustered by similarity


NUTs don’t form clusters (random scatter around center)


NUTs are connected to the rest of the forest

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014

Courtesy of Yuri Wolf; slide in the public domain.

74

#### **Forest of Life – Analysis**

“Tree-like” vs “Net-like” components of the trees  (how many quartets agree/disagree with the consensus tree).


<!-- Start of picture text -->
NUTs  FOL<br>0.63 +/- 0.35  0.39 +/- 0.31<br><!-- End of picture text -->


<!-- Start of picture text -->
© Source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

###### NUTs are dominated by tree-like descent

Overall the forest of life is dominated by network-like relationships (HGT)

Courtesy of Yuri Wolf; slide in the public domain.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014 75

#### **Forest of Life – Analysis**

###### Simulated example of 16 trees for 10 organisms:


No two trees are the same; each contains 2 random deviations from the consensus tree. Common statistical trend is visible.

Courtesy of Yuri Wolf; slide in the public domain.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014

76

#### **Module V: Evolution/phylogeny/populations**

- Phylogenetics / Phylogenomics

   - Phylogenetics: Evolutionary models, Tree building, Phylo inference

   - Phylogenomics: gene/species trees, reconciliation, coalescent, pops

- Population genomics:

   - Learning population history from genetic data

   - Assembling and getting information on genomes

   - Recitation about suffix arrays used in genome mapping and assembly

- Next Pset due on Nov 1<sup>st</sup>

   - Don’t wait until the last week to start it!

77

MIT OpenCourseWare http://ocw.mit.edu

6.047 / 6.878 / HST.507 Computational Biology Fall 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 2. Sequence evolution over single branch](03-2-sequence-evolution-over-single-branch.md) · [Up: contents](index.md)
