---
title: Introduction
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/18-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/18-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**6.047/6.878 - Computational Biology:  Genomes, Networks, Evolution**

#### **Lecture 18 Molecular Evolution and Phylogenetics**


<!-- Start of picture text -->
Patrick Winston’s 6.034<br><!-- End of picture text -->

_Somewhere, something went wrong_ …

1

###### **Challenges in Computational Biology**

**4 Genome Assembl** **~~<u>y</u>~~**

**5 Regulatory motif discovery**

**1 Gene Finding**

**DNA**

**2 Sequence alignment**

**6 Comparative Genomics 7 Evolutionary Theory**

**`TCATGCTAT TCGTGATAA TGAGGATAT` 3 Database lookup** **`TTATCATAT TTATGATTT`**

**8 Gene expression analysis**

**RNA transcript**


**9 Cluster discovery**


**10 Gibbs sampling**

###### **11 Protein network analysis**


**12 Metabolic modelling**

**13 Emerging network properties**


2

#### **Concepts of Darwinian Evolution**


<!-- Start of picture text -->
Selection<br><!-- End of picture text -->

Image in the public domain.

Courtesy of Yuri Wolf; slide in the public domain.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014

3

#### **Concepts of Darwinian Evolution**


Image in the public domain.

**Charles Darwin 1859** . _Origin of Species_ [one and only illustration]: "descent with modification"

Courtesy of Yuri Wolf; slide in the public domain.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014

4

#### **Tree of Life**


© Neal Olander. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit. edu/help/faq-fair-use/.

Image in the public domain.

5

#### **Goals for today: Phylogenetics**

- **Basics of phylogeny: Introduction and definitions** – Characters, traits, nodes, branches, lineages, topology, lengths

   - Gene trees, species trees, cladograms, chronograms, phylograms

**1. From alignments to distances: Modeling sequence evolution** – Turning pairwise sequence alignment data into pairwise distances

   - Probabilistic models of divergence: Jukes Cantor/Kimura/hierarchy

**2. From distances to trees: Tree-building algorithms**

   - Tree types: Ultrametric, Additive, General Distances

   - – Algorithms: UPGMA, Neighbor Joining, guarantees and limitations

   - – Optimality: Least-squared error, minimum evolution (require search)

**3. From alignments to trees: Alignment scoring given a tree** – Parsimony: greedy (union/intersection) vs. DP (summing cost)

– ML/MAP (includes back-mutations, lengths): peeling algorithm (DP)

4. Tree of Life in Genomic Era

   - The prokaryotic problem (no real taxa and HGT)

   - – Interpreting the forest of life

6

#### **Introduction: Basics and Definitions**

Characters, traits, gene/species trees

7

#### **Common Phylogenetic Tree Terminology**

**Terminal Nodes**

**Branches or A Represent the Lineages TAXA (genes, B populations, species, etc.) used to infer C the phylogeny D Ancestral Node or ROOT of Internal Nodes or E the Tree Divergence Points (represent hypothetical ancestors of the taxa)**

8

#### **Extinctions part of life**

Phylogenetic tree showing archosaurs, dinosaurs, birds, etc. through geologic time removed due to copyright restrictions.

9

#### **Phylogenetics**

**General Problem:** Infer complete ancestry of a set of ‘ **objects** ’ based on knowledge of their ‘ **traits** ’ Mammal family tree removed due to copyright restrictions. **‘Objects’ can be:** Species, Genes, Cell types, Diseases, Cancers, Languages, Faiths, Cars, Architectural Styles **‘Traits’ can be:** Morphological, molecular, gene expression, TF binding, motifs, words… **Historical record varies:** Fossils, imprints, timing of geological events, ‘living fossils’, sequencing of extinct species, paintings, stories. **Today:** Phylogenies using only extant species data  **gene trees** (paralog / ortholog / homolog trees)

Mammal family tree removed due to copyright restrictions.

10

**Inferring Phylogenies: Traits and Characters Trees can be inferred by several criteria:** – Traditional traits: Morphology data


© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. – Modern traits: Molecular data


Kangaroo **`ACAGTGACGCCCCAAACGT`** Elephant **`ACAGTGACGCTACAAACGT`** Dog **`CCTGTGACGTAACAAACGA`** Mouse **`CCTGTGACGTAGCAAACGA`** Human **`CCTGTGACGTAGCAAACGA`**

11

#### **From physiological traits to DNA characters**

- Traditional phylogenetics

   - Building species trees

   - Small number of traits

      - Hoofs, nails, teeth, horns

   - Well-behaved traits, each arose once

      - Parsimony principle, Occam’s razor

- Modern phylogenetics

   - Building gene trees and species trees

   - Very large number of traits

      - Every DNA base and every protein residue

   - Frequently ill-behaved traits

      - Back-mutations are frequent (convergent evolution)

      - Small number of letters, arise many times independently

12

###### **Three types of trees**


<!-- Start of picture text -->
Clado gram  Chrono gram  Phylo gram<br>6<br>Taxon B  Taxon B  1 Taxon B<br>1<br>Taxon C Taxon C 3 Taxon C<br>1<br>Taxon A  Taxon A  Taxon A<br>Taxon D  Taxon D  5<br>Taxon D<br>t1  t2  t3<br><!-- End of picture text -->

###### **Topology only Topology + Divergence times**

###### **Topology + Divergence times + Divergence rates**

13

#### **Inferring a tree from nucleotides/peptides**

Molecular phylogenetic methods

Sequence data: -Nucleotide alignments -Peptide alignments

Evolutionary history represented as a binary tree

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

14

#### **Two basic approaches for phylogenetic inference**

###### **Distance based**


<!-- Start of picture text -->
1  2<br>From Sequences<br>Tree building<br>To Distances<br>algorithms<br>Sequence alignment  Pair-wise distance matrix  Output tree<br><!-- End of picture text -->

###### **Character based**


**Sequence alignment**


<!-- Start of picture text -->
3<br>From alignments<br>To phylogenies<br>Couple to<br>tree proposal<br>Output tree<br>and scoring<br>4<br><!-- End of picture text -->

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

15

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

**3. From alignments to trees: Alignment scoring given a tree** –

3 Parsimony: greedy (union/intersection) vs. DP (summing cost) – ML/MAP (includes back-mutations, lengths): peeling algorithm (DP)

4. Tree of Life in Genomic Era

- The prokaryotic problem (no real taxa and HGT)

- 4 – Interpreting the forest of life

16

#### **1. From alignments to distances** Modeling evolutionary rates


<!-- Start of picture text -->
Distance estimation<br><!-- End of picture text -->

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

17

#### **Measuring evolutionary rates**

- Nucleotide divergence

   - Uniform rate.  Overall percent identity.

- Transitions and transversions

   - Two-parameter model. A-G, C-T more frequent.

- Synonymous and non-synonymous substitutions

   - Ka/Ks rates.  Amino-acid changing substitutions


- Nactual mutations > N observed substitutions

   - Some fraction of “conserved” positions mutated twice


<!-- Start of picture text -->
.6<br>.1  .1<br>.6  C  C<br>A  .2  G  A  .2  .1  G<br>.1<br>T  T<br><!-- End of picture text -->

18

#### **‘Evolving’ a nucleotide under random model**

- At time step 0, start with letter A

- At time step 1:

   - Remain A with probability 0.7

   - Change to C,G,T with prob. 0.1 each

- At time step 2:

   - In state A with probability 0.52

      - Remain A with probability 0.7 * 0.7

      - Go back to A from C,G,T with 0.1*0.1 each


<!-- Start of picture text -->
.1<br>.7  .7<br>A  G<br>.1<br>.1<br>.1<br>.1<br>C  T<br>.1<br>.7  .7<br><!-- End of picture text -->

- In states C,G,T with prob. 0.16 each

||t=1|t=2|t=3|t=4|t=5|
|---|---|---|---|---|---|
|A|1|0.7|0.52|0.412|0.3472|
|C|0|0.1|0.16|0.196|0.2176|
|G|0|0.1|0.16|0.196|0.2176|
|T|0|0.1|0.16|0.196|0.2176|


19

#### **Modeling Nucleotide Evolution**

During infinitesimal time t, there is not enough time for two substitutions to happen on the same nucleotide

So we can estimate P(x | y, t), for x, y  {A, C, G, T}

Then let

S(t) =

P(A|A, t) ……  P(A|T, t) … … P(T|A, t) …… P(T|T, t)

20

#### **Modeling Nucleotide Evolution**

Reasonable assumption: multiplicative (implying a stationary Markov process)

S(t+t’) = S(t)S(t’)

That is, P(x | y, t+t’) = z P(x | z, t) P(z | y, t’)

Jukes-Cantor: constant rate of evolution

1 - 3     1 - 3   For short time , S() =   1 - 3     1 - 3

21

#### **Modeling Nucleotide Evolution**

###### **<u>Jukes-Cantor:</u>**

For longer times,


<!-- Start of picture text -->
r(t) s(t)   s(t)   s(t)<br>S(t) =  s(t)  r(t)  s(t)   s(t)<br>s(t)  s(t)  r(t)  s(t)<br>s(t)  s(t)   s(t)  r(t)<br><!-- End of picture text -->

Where we can derive:

r(t) = ¼ (1 + 3 e<sup>-4t</sup> ) s(t) = ¼ (1 – e<sup>-4t</sup> )

Geometric asymptote to 1/4


<!-- Start of picture text -->
<br>A  G<br><br><br><br><br>C  T<br><br>1-3  1-<br>3<br>A  other<br><br><!-- End of picture text -->


22

#### **Modeling Nucleotide Evolution**

**<u>Kimura:</u>**

Transitions: A/G, C/T Transversions: A/T, A/C, G/T, C/G

Transitions (rate ) are much more likely than transversions (rate )

A G C T A r(t) s(t) u(t) u(t) S(t) = G s(t) r(t) u(t) u(t) C u(t) u(t) r(t) s(t) T u(t) u(t) s(t) r(t)

Where

s(t) = ¼ (1 – e<sup>-4t</sup> ) u(t) = ¼ (1 + e<sup>-4t</sup> – e<sup>-2(+)t</sup> ) r(t)  = 1 – 2s(t) – u(t)

23

#### **Distance between two sequences**

Given (well-aligned portion of) sequences x<sup>i</sup> , x<sup>j</sup> , Define

dij = distance between the two sequences One possible definition: dij = fraction _f_ of sites u where x<sup>i</sup> [u]  x<sup>j</sup> [u]

Better model (Jukes-Cantor): r(t) = ¼ (1 + 3 e<sup>-4t</sup> ) dij = - ¾ log(1 – 4 _f_ / 3) s(t) = ¼ (1 – e<sup>-4t</sup> ) Observed F = [ 0.1,    0.2,  0.3,    0.4,   0.5,   0.6,   0.7]) Actual      D = [0.11, 0.23, 0.38, 0.57, 0.82, 1.21, 2.03]

24

#### **Many nucleotide models have been developed**

###### Varying levels of complexity (parameters)


© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**Models also exist for peptides and codons**

25

#### **Goals for today: Phylogenetics**

- **Basics of phylogeny: Introduction and definitions** – Characters, traits, nodes, branches, lineages, topology, lengths

   - Gene trees, species trees, cladograms, chronograms, phylograms

**1. From alignments to distances: Modeling sequence evolution** – Turning pairwise sequence alignment data into pairwise distances

   - Probabilistic models of divergence: Jukes Cantor/Kimura/hierarchy

**2. From distances to trees: Tree-building algorithms**

   - Tree types: Ultrametric, Additive, General Distances

   - – Algorithms: UPGMA, Neighbor Joining, guarantees and limitations

   - Optimality: Least-squared error, minimum evolution (require search)

**3. From alignments to trees: Alignment scoring given a tree** – Parsimony: greedy (union/intersection) vs. DP (summing cost)

– ML/MAP (includes back-mutations, lengths): peeling algorithm (DP)

4. Tree of Life in Genomic Era

   - The prokaryotic problem (no real taxa and HGT)

   - Interpreting the forest of life

26

#### **2. Distance-based tree-building algorithms**

##### Mapping a distance matrix to a tree


<!-- Start of picture text -->
UPGMA, NJ,<br>LSE, ME<br><!-- End of picture text -->

- © Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

27

#### **Distance matrix**  **Phylogenetic tree**

|**Hum**|**Mou**|**Rat**||**Dog**<br>**Cat**|
|---|---|---|---|---|
|**Human**<br>0|4|5||7<br>6|
|**Mouse**<br>h.y.m|0|3||8<br>5|
|**Rat**<br>h.y.r|m.r|0||9<br>7|
|**Dog**<br>h.z.x.d|m.y.z.x.d|r.y.z.x|.d|0<br>2|
|**Cat**<br>h.z.x.c|m.y.z.x.c|r.y.z.x|.c|d.c<br>0|
|Tree implies|x|d|Dog|Map distances Dij|
|Goal:<br>a distance matrix<br>Mij|z<br>y|c<br>h<br>m<br>r|Hum<br>Cat<br>Mous<br>Rat|an<br>e<br> <br>to a tree<br>minij(Dij-Mij)<sup>2</sup>|
|Minimize discrepancy betw|eenobserve|d dista|nces|andtree-based distances<br>28|


28

#### **Ultrametric distances & 3 Point Condition**

- For all points i, j, k

   - two distances are equal and third is smaller

   - d(i,j) <= d(i,k) = d(j,k) a+a  <=  a+b  =  a+b


<!-- Start of picture text -->
i<br>a<br>b<br>k<br>j  a<br><!-- End of picture text -->

where a <= b

- Result:

   - All paths from leaves are equidistant to the root

   - Rooted tree with uniform rates of evolution

29

#### **Ultrametric trees**

A    B    C A     0    6    6 B     6    0    4 C     6    4    0

A    B    C A     0    3    3 B     3    0    2 C     3    2    0

For now imagine that these are just the number of substitutions between pairs:

###### **Symmetric 0-diagonal matrix of divergence times**

```
A :   G CCCAA CT A
B :   G TTTCC CT C
```

Taken from Ran Libeskind-Hadas, Lecture Slides, Fall, 2013

30

#### **Ultrametric Trees**

- Given a symmetric n x n 0-diagonal matrix D, an ultrametric tree T for that matrix is one in which:

   - There are n leaves, one for each row (column) of D

   - Each internal node is labeled by a time in D and has exactly two children

   - Along any path from the root to a leaf, the (divergence) times at the internal nodes strictly decrease

   - For any two leaves i, j of T, the LCA of i, j is labeled with time D(i, j)

3 `A    B    C A 0    3    3` 2 `B     3    0    2 C     3    2    0` A B C

Taken from Ran Libeskind-Hadas, Lecture Slides, Fall, 2013

31

#### **Ultrametric Matrix Construction**

A    B    C    D    E A     0    5    2    5    7 B     5    0    5    3    7 C     2    5    0    5    7 D     5    3    5    0    7 E     7     7    7    7    0

|A    B|C    D    E|
|---|---|
|A0    5|2    5    7|
|B5    0|**4**3    7|
|C2**4**|0    5    7|
|D5    3|5    0    7|
|E7     7|7    7    0|


##### • Algorithms exist for “ultrametrifying” matrices.

Taken from Ran Libeskind-Hadas, Lecture Slides, Fall, 2013

32

#### **Minimum Spanning Tree (MST)**

- There is a unique path between any two vertices in a spanning tree

- Adding an edge to a spanning tree creates a cycle

- Any edge on that cycle can be removed and we’ll still have a spanning tree

- MST is found using Prim’s Algorithm (graph traversal)

Taken from Ran Libeskind-Hadas, Lecture Slides, Fall, 2013

33

#### **The “Ultrametrification” Algorithm**

Given n x n symmetric 0-diagonal matrix D that is not ultrametric

1.Construct a completely connected graph with n vertices, one per row of A.  The edge weight from vertex i to vertex j is D(i, j).

2.Find a minimum spanning tree (MST) of this graph.

3.Build a new matrix D’ such that D’(i, j) is the **_largest_** weight on the unique path from i to j in the MST.

Taken from Ran Libeskind-Hadas, Lecture Slides, Fall, 2013

34

#### **Distances: (b) Additive distances**

- All distances satisfy the four-point condition

   - Any quartet can be labeled i,j,k,l such that:

      - d(i,j) + d(k,l) <=    d(i,k)  +    d(j,l)    =    d(i,l)  +  d(j,k)

      - (a+b)+(c+d) <= (a+m+c)+(b+m+d) = (a+m+d)+(b+m+c)


<!-- Start of picture text -->
i  k<br>a<br>c<br>m<br>b<br>j  d<br>l<br><!-- End of picture text -->

- Result:

   - All pairwise distances obtained by traversing a tree

35

#### **Distances: (c) General distances**

- In practice, a distance matrix is neither ultrametric nor additive – Noise

      - Measured distances are not exact

      - Evolutionary model is not exact

   - Fluctuations

      - Regions used to measure distances not representative of the species tree

      - Gene replacement (gene conversion), lateral transfer

      - Varying rates of mutation can lead to discrepancies

- In the general case, tree-building algorithms must handle noisy distance matrices

   - Such a tree can be obtained by

      - Enumeration and scoring of all trees (too expensive)

      - Neighbor-Joining (typically gives a good tree)

      - UPGMA (typically gives a poor tree)

36

**Algorithms: (a) UPGMA (aka Hierarchical Clustering)** (Unweighted Pair Group Method with Arithmetic mean) **<u>Initialization:</u>**

Assign each xi into its own cluster Ci Define one leaf per sequence, height 0

###### **<u>Iteration:</u>**

Find two clusters Ci, Cj s.t. dij is min Let Ck = Ci  Cj Define node connecting Ci, Cj, & place it at height dij/2 Delete Ci, Cj

**<u>Termination:</u>**

When two clusters i, j remain, place root at height dij/2


<!-- Start of picture text -->
1  4<br>3<br>2  5<br>1  4  2  3  5<br><!-- End of picture text -->

37

#### **Ultrametric Distances & UPGMA**


<!-- Start of picture text -->
1  4  2  3  5<br><!-- End of picture text -->

###### UPGMA is guaranteed to build the correct tree if distance is ultrametric

- **<u>Proof:</u>**

1. The tree topology is unique, given that the tree is binary

2. UPGMA constructs a tree obeying the pairwise distances

38

#### **Weakness of UPGMA**

###### <u>Molecular clock assumption:</u>

implies time is constant for all species

However, certain species (e.g., mouse, rat) evolve much faster

Example where UPGMA messes up:


<!-- Start of picture text -->
Correct tree<br>3<br>2<br>4<br>1<br><!-- End of picture text -->


<!-- Start of picture text -->
UPGMA<br>1  4  2  3<br><!-- End of picture text -->

39

#### **Algorithms: (b) Neighbor-Joining**

- Guaranteed to produce the correct tree if distance is additive

- • May produce a good tree even when distance is not additive

###### **<u>Step 1:</u>** Finding neighboring leaves

Define

Dij = dij – (ri + rj)

###### Where

1

ri = –––––k dik |L| - 2


<!-- Start of picture text -->
1  3<br>0.1  0.1<br>0.1<br>0.4<br>0.4<br>2  4<br><!-- End of picture text -->

**<u>Claim:</u>** The above “magic trick” ensures that Dij is minimal **<u>iff</u>** i, j are neighbors **<u>Proof:</u>** Beyond the scope of this lecture (Durbin book, p. 189)

40

#### **Algorithm: Neighbor-joining**

###### **<u>Initialization:</u>**

Define T to be the set of leaf nodes, one per sequence Let L = T

###### **<u>Iteration:</u>**

Pick i, j s.t. Dij is minimal

Define a new node k, and set dkm = ½ (dim + djm – dij) for all m  L

Add k to T, with edges of lengths dik = ½ (dij + ri – rj) Remove i, j from L; Add k to L

**<u>Termination:</u>**

When L consists of two nodes, i, j, and the edge between them of length dij

41

#### **Algorithms: (c) Distance-fitting algoriths**

• With distance-based algorithms, we can also aim to directly minimize discrepancy between original distance matrix and tree-based distance matrix **COMPUTATIONAL METHOD Optimality criterion Clustering algorithm PARSIMONY MAXIMUM LIKELIHOOD MINIMUM EVOLUTION UPGMA LEAST SQUARES NEIGHBOR-JOINING**

42

#### **Distance matrix**  **Phylogenetic tree**

|**Hum**|**Mou**|**Rat**||**Dog**<br>**Cat**|
|---|---|---|---|---|
|**Human**<br>0|4|5||7<br>6|
|**Mouse**<br>h.y.m|0|3||8<br>5|
|**Rat**<br>h.y.r|m.r|0||9<br>7|
|**Dog**<br>h.z.x.d|m.y.z.x.d|r.y.z.x|.d|0<br>2|
|**Cat**<br>h.z.x.c|m.y.z.x.c|r.y.z.x|.c|d.c<br>0|
|Tree implies|x|d|Dog|Map distances Dij|
|Goal:<br>a distance matrix<br>Mij|z<br>y|c<br>h<br>m<br>r|Hum<br>Cat<br>Mous<br>Rat|an<br>e<br> <br>to a tree<br>minij(Dij-Mij)<sup>2</sup>|
|Minimize discrepancy betw|eenobserve|d dista|nces|andtree-based distances<br>43|


43

#### **Aside: Alternative to Molecular clock?**

Divergence between orthologous sequences is proportional to time separating the species. Different genes evolve at specific, roughly constant rates. **Zuckerkandl & Pauling 1962**


divergence time


<!-- Start of picture text -->
sampling<br>error<br>rate<br><!-- End of picture text -->

time

Taken from Yuri Wolf, Lecture Slides, Feb. 2014

Courtesy of Yuri Wolf; slide in the public domain.

44

#### **Molecular Clock**

Under MC all individual gene trees are ultrametric (up to a sampling error) and identical to the species tree up to a scaling factor (evolution rate).

###### Are these really ultrametric?


<!-- Start of picture text -->
species  gene 1  gene 2<br>tree<br>A  A  A<br>B  B  B<br>C  C  C<br>D  D  D<br>E  E  E<br>F  F  F<br>G  G  G<br>H  H  H<br>time  distance  distance<br><!-- End of picture text -->

Courtesy of Yuri Wolf; slide in the public domain.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014

45

#### **Molecular Clock**

Most of the real phylogenetic trees are far from being ultrametric. Molecular clock is substantially overdispersed **.**


<!-- Start of picture text -->
observed<br>ideal  expected based<br>on sampling error<br>time<br>rate<br><!-- End of picture text -->


<!-- Start of picture text -->
0.2<br><!-- End of picture text -->

Courtesy of Yuri Wolf; slide in the public domain.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014

46

#### **Relaxed Molecular Clock**

Relaxed molecular clock models allows for rate variation. Rates are sampled from prior distributions with limited variance, independently or in autocorrelated manner.

Genes are either analyzed individually, or as concatenated alignments (implying evolution as a single unit).


<!-- Start of picture text -->
rate<br><!-- End of picture text -->


###### time

Courtesy of Yuri Wolf; slide in the public domain.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014

47

#### **Universal Pacemaker**

Universal Pacemaker model assumes that evolutionary time runs at different pace in each lineage.

Under the UPM, species trees are intrinsically non-ultrametric.


<!-- Start of picture text -->
A<br>A<br>B  B<br>C  C<br>D  D<br>E  E<br>F  F<br>G  G<br>H  H<br>time  pacemaker<br>ticks<br><!-- End of picture text -->

Courtesy of Yuri Wolf; slide in the public domain.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014

48

#### **Pacemaker vs Clock**

Both overdispersed MC and UPM models predict that individual gene trees would deviate from ultrametricity.

Under MC these deviations are expected to be uncorrelated.

Under UPM these deviations are expected to be correlated, so there exists a non-ultrametric pacemaker tree that can significantly reduce variance of observed rates.

A testable hypothesis!

- 2,300 trees of 100 prokaryotic species;

- 7,000 trees of 6 _Drosophila_ species

- 1,000 trees of 9 yeast species

- 5,700 trees of 8 mammalian species

Courtesy of Yuri Wolf; slide in the public domain.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014

49

#### **Pacemaker vs Clock**

- 2,300 trees of 100 prokaryotic species;

- 7,000 trees of 6 _Drosophila_ species

- 1,000 trees of 9 yeast species

- 5,700 trees of 8 mammalian species

All show an overwhelming support to UPM model.

**Snir 2012; work in progress at NCBI (NIH)**

Courtesy of Yuri Wolf; slide in the public domain.

Taken from Yuri Wolf, Lecture Slides, Feb. 2014

50

#### **Goals for today: Phylogenetics**

- **Basics of phylogeny: Introduction and definitions** – Characters, traits, nodes, branches, lineages, topology, lengths

   - Gene trees, species trees, cladograms, chronograms, phylograms

**1. From alignments to distances: Modeling sequence evolution** – Turning pairwise sequence alignment data into pairwise distances

   - Probabilistic models of divergence: Jukes Cantor/Kimura/hierarchy

**2. From distances to trees: Tree-building algorithms**

   - Tree types: Ultrametric, Additive, General Distances

   - – Algorithms: UPGMA, Neighbor Joining, guarantees and limitations

- Optimality: Least-squared error, minimum evolution (require search)

- **3. From alignments to trees: Alignment scoring given a tree** – Parsimony: greedy (union/intersection) vs. DP (summing cost)

- – ML/MAP (includes back-mutations, lengths): peeling algorithm (DP)

4. Tree of Life in Genomic Era

   - The prokaryotic problem (no real taxa and HGT)

   - – Interpreting the forest of life

51

**3. Character-based tree-scoring algorithms** 3a: Parsimony (set-based) 3b: Parsimony (Dyn. Prog.) 3c: Maximum Likelihood


© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

52

#### **Basic algorithms of phylogenetic methods**

###### **Distance based**


<!-- Start of picture text -->
1  2<br>From Sequences<br>Tree building<br>To Distances<br>algorithms<br><!-- End of picture text -->

**Sequence alignment**

**Pair-wise distance matrix**

**Output tree**

###### **Character based**


<!-- Start of picture text -->
Sequence alignment<br><!-- End of picture text -->


<!-- Start of picture text -->
3<br>From alignments<br>To phylogenies<br>Couple to<br>tree proposal<br>Output tree<br>and scoring<br>4<br><!-- End of picture text -->

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

53

#### **Character-based phylogenetic inference**

- Really about tree **scoring** techniques, not tree finding techniques

   - Couple them with tree proposal and update and you have an algorithm (part 4 of the lecture)

- Two approaches exist, all use same architecture: – Minimize events: Parsimony (union/intersection)

   - Probabilistic: Max Likelihood / MAP

54

#### **Parsimony scoring (a): Union and intersection**

Given a tree, and an alignment column

Label internal nodes to minimize the number of required substitutions

**<u>Initialization:</u>**

{A, B} C+=1

Set cost C = 0; k = 2N – 1

**<u>Iteration:</u>**

{A}

If k is a leaf, set Rk = { x<sup>k</sup> [u] }

If k is not a leaf, Let i, j be the daughter nodes; Set Rk = Ri  Rj if intersection is nonempty

{A, B} C+=1

Set Rk = Ri  Rj, and C += 1, if intersection is empty

A **<u>Termination:</u>** {A} Minimal cost of tree for column u, = C

B A B {B} {A} {B}

55

#### **Parsimony traceback to find ancestral nucleotides**

**<u>Traceback:</u>**

1. Choose an arbitrary nucleotide from R2N – 1 for the root

2. Having chosen nucleotide r for parent k, If r  Ri choose r for daughter i Else, choose arbitrary nucleotide from Ri

Easy to see that this traceback produces some assignment of cost C

###### Accessible to traceback


<!-- Start of picture text -->
{A, B}<br>B  A<br>x<br>{A}<br> A   A<br>{A, B}  x<br>A  A<br>x  x<br>A  B A  B<br>{A}  {B} {A} {B}  A  B A  B  A  B A  B<br><!-- End of picture text -->

Still optimal, but not found by traceback


<!-- Start of picture text -->
B<br> B<br>B  x<br>x<br>A  B A  B  56<br><!-- End of picture text -->

#### **Parsimony Scoring (b): Dynamic programming**

||M|R|B1|H|B2|D|B3|
|---|---|---|---|---|---|---|---|
|A|0|1|1|0|1|1|2|
|C|1|1|2|1|3|1|4|
|G|1|0|1|1|2|0|2|
|T|1|1|2|1|3|1|4|


- Each cell (N,C) represents the min cost of the subtree rooted at N, if the label at N is C.

- • Update table by walking up the tree from the leaves to the root, remembering max choices.

- • Traceback from root to leaves to construct a min cost assignment


<!-- Start of picture text -->
B3<br>B2<br>B1<br>A  G  A  G<br>Mouse  Rat  Human  Dog<br><!-- End of picture text -->

57

#### **Goals for today: Phylogenetics**

- **Basics of phylogeny: Introduction and definitions** – Characters, traits, nodes, branches, lineages, topology, lengths

   - Gene trees, species trees, cladograms, chronograms, phylograms

**1. From alignments to distances: Modeling sequence evolution** – Turning pairwise sequence alignment data into pairwise distances

   - Probabilistic models of divergence: Jukes Cantor/Kimura/hierarchy

**2. From distances to trees: Tree-building algorithms**

   - Tree types: Ultrametric, Additive, General Distances

   - – Algorithms: UPGMA, Neighbor Joining, guarantees and limitations

   - – Optimality: Least-squared error, minimum evolution (require search)

**3. From alignments to trees: Alignment scoring given a tree** – Parsimony: greedy (union/intersection) vs. DP (summing cost)

<mark>– ML/MAP (includes back-mutations, lengths): peeling algorithm (DP)</mark>

4. Tree of Life in Genomic Era

   - The prokaryotic problem (no real taxa and HGT)

   - – Interpreting the forest of life

58

#### **Scoring (c) Maximum Likelihood & Max-a-Posteriori**

**Input:** Sequence alignment

**Output:** tree with maximum likelihood / max a posteriori prob. **Search:** Heuristic search for max likelihood tree. **Maximum Likelihood (ML) Maximum a Posteriori (MAP)** B^,T^ = argmaxB,T P(D|B,T) B^,T^ = argmaxB,T P(B,T|D) B,T P(B,T|D)  P(B,T|D)

**Maximum a Posteriori (MAP)** B^,T^ = argmaxB,T P(B,T|D) B,T P(B,T|D)  P(B,T|D) = argmaxB,T P(B,T,D) / P(D) = argmaxB,T P(B,T,D) = argmaxB,T P(D|B,T)P(B,T)

D = seq. alignment data B = branch lengths T = topology

likelihood likelihood

**P(D|B,T)** is the likelihood of data given model  Use seq evolution model: JC,K2P,HKY. **P(B,T)** is a prior on trees/branch lengths

**Compute recursively using DP**

 Use Yule process, Birth-Death process to model

59

**‘Peeling’ algorithm for P(D|B,T) term**


1. Assume **sites j evolve independently** .

 Treat each column of the alignment in isolation

2. Assume **branch independence** , conditioned on parent  Expand total joint probability into prod of P(xi|xparent,ti)  Only P(x2n-1) remains, root prior, background nucl. freq.

3. We know how to compute **P(xi|xparent(i),ti)** for fixed pair Defined by our sequence model (JC, K2P, HKY, etc)

Easily calculate for any given assignment of internal nodes

4. As internal node values are not known  **marginalize** Sum over all possible values of all internal/root nodes

Let xn+1,…,x2n-1 represent seqs of n-1 internal nodes

60

---

[Up: contents](index.md) · [1. Site evolution over single branch Remember: Jukes-Cantor (JC) →](02-1-site-evolution-over-single-branch-remember-jukes-cantor-jc.md)
