---
title: Phylogenomics and Population Genomics
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/compiled/compiled-compiled.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Phylogenomics and Population Genomics

**Source:** `compiled/compiled-compiled.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

397

CHAPTER

## **TWENTYSEVEN**

## MOLECULAR EVOLUTION AND PHYLOGENETICS

Scribed by Andrew Cooper, Stephanie Chang, and Stephen Serene (2012) Akashnil Dutta (2011) Albert Wang and Mashaal Sohail (2010) Guo-Liang Chew and Sara Baldwin (2009)

### **Figures**

|27.1 Evolutionary History of Life . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|398|
|---|---|
|27.2 Defining tree terminology. A tree of branching nodes is depicted with leaves at the top<br>and the root on the bottom. Time continues upward, toward the leaves. . . . . . . . . . .|398|
|27.3 Three types of trees. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|399|
|27.4 The two steps of distance based phylogenetic reconstruction.<br>. . . . . . . . . . . . . . . .|402|
|27.5 Markov chain accounting for back mutations<br>. . . . . . . . . . . . . . . . . . . . . . . . .|403|
|27.6 The y axis denotes probability of observing the bases - A(red), others(green). x axis denotes<br>time. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|403|
|27.7 Fraction of altered bases (x axis) versus the Jukes Cantor distance(y axis).<br>Black line||
|denotes the curve, green is the trend line for small values of f while the red line denotes<br>the asymptotic boundary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|405|
|27.8 Distance models of varying levels of complexity(parameters).<br>. . . . . . . . . . . . . . . .|406|
|27.9 Mapping from a tree to a distance matrix and vice versa . . . . . . . . . . . . . . . . . . .|407|
|27.10Ultrametric distances.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|408|
|27.11Additive distances. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|408|
|27.12UPGMA / Hierarchical Clustering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|409|
|27.13UPGMA fails to find the correct tree in this case . . . . . . . . . . . . . . . . . . . . . . .|410|
|27.14An overview of the character based methods . . . . . . . . . . . . . . . . . . . . . . . . . .|411|
|27.15Parsimony scoring: union and intersection . . . . . . . . . . . . . . . . . . . . . . . . . . .|412|
|27.16Parsimony traceback to find ancestral neucleotides . . . . . . . . . . . . . . . . . . . . . .|413|
|27.17Parsimony scoring by dynamic programming<br>. . . . . . . . . . . . . . . . . . . . . . . . .|413|
|27.18A tree to be scored using the peeling algorithm. n=4 . . . . . . . . . . . . . . . . . . . . .|415|
|27.19The recurrence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|415|
|27.20An unit step using Nearest Neighbor Interchange scheme. . . . . . . . . . . . . . . . . . .|418|


399

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

## **27.1 Introduction**

Phylogenetics is the study of relationships among a set of objects having a common origin, based on the knowledge of the individual traits of the objects. Such objects may be species, genes, or languages, and their corresponding traits may be morphological characteristics, sequences, words etc. In all these examples the objects under study change gradually with time and diverge from common origins to present day objects.

In Biology, phylogenetics is particularly relevant because all biological species happen to be descendants of a single common ancestor which existed approximately 3.5 to 3.8 billion years ago. Throughout the passage of time, genetic variation, isolation and selection have created the great variety of species that we observe today. Not just speciation however, but extinction has also played a key role in shaping the biosphere as we see today. Studying the ancestry between different species is fundamentally important to biology because they shed much light in understanding different biological functions, genetic mechanisms as well as the process of evolution itself.

Figure 27.1: Evolutionary History of Life

## **27.2 Basics of Phylogeny**

### **27.2.1 Trees**

A tree is a mathematical representation of relationships between objects. A general tree is built from nodes and edges. Each node represents an object, and each edge represents a relationship between two nodes. In the case of phylogenetic trees, we represent evolution using trees. In this case, each node represents a divergence event between two ancestral lineages, the leaves denote the set of present objects and the root represents the common ancestor.


Figure 27.2: Defining tree terminology. A tree of branching nodes is depicted with leaves at the top and the root on the bottom. Time continues upward, toward the leaves.

400

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

However, sometimes more information is reflected in the branch lengths, such as time elapsed or the amount of dissimilarity. According to these differences, biological phylogenetic trees may be classified into three categories:

**Cladogram:** gives no meaning to branch lengths; only the sequence and topology of the branching matters.

- **Phylogram:** Branch lengths are directly related to the amount of **genetic change** . The longer the branch of a tree, the greater the amount of phylogenetic change that has taken place. The leaves in this tree may not necessarily end on the same vertical line, due to different rates of mutation.

- **Chronogram (ultrametric tree):** Branch lengths are directly related to **time** . The longer the branches of a tree, the greater the amount of time that has passed. The leaves in this tree necessarily end on the same vertical line (i.e. they are the same distance from the root), since they are all in the present unless extinct species were included in the tree. Although there is a correlation between branch lengths and genetic distance on a chronogram, they are not necessarily exactly proportional because evolution rates / mutation rates are not constant. Some species evolve and mutate faster than others, and some historical time periods foster faster rates of evolution than others.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 27.3: Three types of trees.

### **27.2.2 Traits**

A trait is any characteristic that an object or species possesses. In humans, an example of a trait may be bipedalism (the ability to walk upright) or the opposable thumb. Another human trait may be a specific DNA sequence that humans possess. The first examples of physical traits are called **morphological traits** , while the latter DNA traits are called **sequence traits** . Each has its advantages and disadvantages to study. All methods for tree-reconstruction rely on studying the occurrence of different traits in the given objects. In traditional phylogenetics the morphological data of different species were used for this purpose. In modern methods, genetic sequence data is used instead. Each has its advantages and disadvantages.

- **Morphological Traits:** Arise from empirical evaluation of physical traits. This can be advantageous because physical characteristics are very easy to quantify and understand for everyone, scientists and

401

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

children alike. The disadvantages to this approach are that we can only evaluate a small set of traits, such as hair, nails, hoofs, teeth, etc. Further, these traits only allow us to build species. Finally, it is much easier to be ”tricked” by convergent evolution. Species that diverged millions of years ago may converge again on the few traits that are observable to scientists, giving a false representation of how closely related the species are.

- **Sequence Traits:** Are discovered by studying the genomes of different species. This approach can be advantageous because it creates much more data and allows scientists to create gene trees in addition to species trees. The primary difficulty with this approach is that DNA is only built from 4 bases, so back mutations are frequent. In this approach, scientists must reconcile the signals of a large number of ill-behaved traits as opposed to that of a small number of well-behaved traits in the traditional approach. The rest of the chapter will focus principally on tree building from gene sequences.

Since this approach deals with comparing between pairs of genes, it is useful to understand the concept of **homology** : A pair of genes are called **paralogues** if they diverged from a duplication event, and **orthologues** if they diverged from a speciation event.

## **_FAQ_**

- **Q:** Would it be possible to use extinct species’ DNA sequences?

- **A:** Current technologies only allow for usage of extant sequences. However, there have been a few successes in using extinct species’ DNA. DNA from frozen mammoths have been collected and are being sequences but due to DNA breaking down over time and contamination from the environment, it is very hard to extract correct sequences.

### **27.2.3 Methods for Tree Reconstruction**

Once we have found genetic data for a set of species, we are interested in learning how those species relate to one another. Since we can, for the most part, only obtain DNA from living creatures, we must infer the existence of ancestors of each species, and ultimately infer the existence of a common ancestor. This is a challenging problem, because very limited data is available. The following sections will explore the modern methods for inferring ancestry from sequence data. They can be classified into two approaches, distance based methods and character based methods.

- **Distance based approaches** take two steps to solve the problem, i.e. to quantify the amount of mutation that separates each pair of sequences (which may or may not be proportional to the time since they have been separated) and to fit the most likely tree according to the pair-wise distance matrix. The second step is usually a direct algorithm, based on some assumtions, but may be more complex.

- **Charecter based approaches** instead try to find the tree that best explains the observed sequences. As opposed to direct reconstruction, these methods rely on tree proposal and scoring techniques to perform a heuristic search over the space of trees.

402

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

## **_Did You Know?_**

**Occam’s Razor** , as discussed in previous chapters, does not always provide the most accurate hypothesis. In many cases during tree reconstruction, the simplest explanation is not the most probable. For example, a set of possible ancestries may be possible, given some observed data. In this case, the simplest ancestry may not be correct if a trait arose independently in two seperate lineages. This issue will be considered in a later section.

403

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

## **27.3 Distance Based Methods**


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 27.4: The two steps of distance based phylogenetic reconstruction.

The distance based models sequester the sequence data into pairwise distances. This step loses some information, but sets up the platform for direct tree reconstruction. The two steps of this method are hereby discussed in detail.

### **27.3.1 From alignment to distances**

In order to understand how a distance-based model works, it is important to think about what distance means when comparing two sequences. There are three main interpretations.

- **Nucleotide Divergence** is the idea of measuring distance between two sequences based on the number of places where nucleotides are not consistent. This assumes that evolution happens at a uniform rate across the genome, and that a given nucleotide is just as likely to evolve into any of the other three nucleotides. Although it has shortcomings, this is often a great way to think about it.

- **Transitions and Transversions** This is similar to nucleotide divergence, but it recognizes that A-G and T-C substitutions are most frequent. Therefore, it keeps two parameters, the probability of a transition and the probability of a transversion.

- **Synonymous and non-synonymous substitutions** This method keeps tracks of substitutions that affect the coded amino-acid by assuming that substitutions that do not change the coded protein will not be selected against, and will thus have a higher probability of occurring than those substitutions which do change the coded amino acid.

The naive way to interpret the separation between two sequences may be simply the number of mismatches, as described by nucleotide divergence above. While this does provide us a distance metric (i.e. _d_ ( _a, b_ ) + _d_ ( _b, c_ ) _≥ d_ ( _a, c_ )) this does not quite satisfy our requirements, beecause we want **additive distances** , i.e. those that satisfy _d_ ( _a, b_ ) + _d_ ( _b, c_ ) = _d_ ( _a, c_ ) for a path _a → b → c_ of evolving sequence, because the amount of mutations accumulated along a path in the tree should be the sum of that of its individual components. However, the naive mismatch fraction do not always have this property, because this quantity is bounded by 1, while the sum of individual components can easily exceed 1.

The key to resolving this paradox is **back-mutations** . When a large number of mutations accumulate on a sequence, not all the mutations introduce new mismatches, some of them may occur on already mutated base pair, resulting in the mismatch score remaining the same or even decreasing. For small mismatchscores however, this effect is statistically insignificant, because there are vastly more identical pairs than

404

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

mismatching pairs. However, for sequences separated by longer evolutionary distance, we must correct for this effect. The Jukes-Cantor model is one such simple markov model that takes this into account.

#### **Jukes-Cantor distances**

To illustrate this concept, consider a nucleotide in state ’A’ at time zero. At each time step, it has a probability 0 _._ 7 of retaining its previous state and probability 0 _._ 1 of transitioning to each of the other three states. The probability _P_ ( _B|t_ ) of observing state (base) _B_ at time _t_ essentially follows the recursion


Figure 27.5: Markov chain accounting for back mutations

If we plot _P_ ( _B|t_ ) versus _t_ , we observe that the distribution starts off as concentrated at the state ’A’ and gradually spreads over to the rest of the states, eventually going towards an equilibrium of equal probabilities. This progression makes sense, intuitively. Over millions of years, species can evolve so dramatically that they no longer resemble their ancestors. At that extreme, a given base location in the ancestor is just as likely to have evolved to any of the four possible bases in that location over time.

|time:-|0|1|2|3|4|
|---|---|---|---|---|---|
|A|1|0.7|0.52|0.412|0.3472|
|C|0|0.1|0.16|0.196|0.2196|
|G|0|0.1|0.16|0.196|0.2196|
|T|0|0.1|0.16|0.196|0.2196|


Figure 27.6: The y axis denotes probability of observing the bases - A(red), others(green). x axis denotes time.

405

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

The essence of the Jukes Cantor model is to backtrack _t_ , the amount of time elapsed from the fraction of altered bases. Conceptually, this is just inverting the x and y axis of the green curve. To model this quantitatively, we consider the following matrix _S_ ( _t_ ) which denotes the respective probabilities _P_ ( _x|y,_ ∆ _t_ ) of observing base _x_ given a starting state of base _y_ in time ∆ _t_ .


We can assume this is a stationary markov model, implying this matrix is multiplicative, i.e.


For a very short time _ϵ_ , we can assume that there is no second order effect, i.e. there isn’t enough time for two mutations to occur at the same nucleotide. So the probabilities of cross transitions are all proportional to _ϵ_ . Further, in Jukes Cantor model, we assume that all the transition rates are same from each nucleotide to another nucleotide. Hence, for a short time _ϵ_


At time _t_ , the matrix is given by


From the equation _S_ ( _t_ + _ϵ_ ) = _S_ ( _t_ ) _S_ ( _ϵ_ ) we obtain


Which rearrange as the coupled system of differential equations


With the initial conditions _r_ (0) = 1 and _s_ (0) = 0. The solutions can be obtained as


Now, in a given alignment, if we have the fraction _f_ of the sites where the bases differ, we have:


implying


To agree asymptotically with _f_ , we set the evolutionary distance _d_ to be


406

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

Note that distance is approximately proportional to _f_ for small values of _f_ and asymptotically approaches infinity when _f →_ 0 _._ 75. Intuitively this happens because after a very long period of time, we would expect the sequence to be completely random and that would imply about three-fourth of the bases mismatching with original. But the uncertainty values of the Jukes-Cantor distance also becomes very large when _f_ approaches 0 _._ 75.


Figure 27.7: Fraction of altered bases (x axis) versus the Jukes Cantor distance(y axis). Black line denotes the curve, green is the trend line for small values of f while the red line denotes the asymptotic boundary.

407

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

#### **Other Models**

The Jukes Cantor model is the simplest model that gives us theoretically consistent additive distance model. However, it is a one-parameter model that assumes that the mutations from each base to a different base has the same chance. But, changes between AG or between TC are more likely than changes across them. The first type of substitution is called transitions while the second type is called transversions. The Kimura model has two parameters which take this into account. There are also many other modifications of this distance model that takes into account the different rates of transitions and transversions etc. that are depicted below.


Figure 27.8: Distance models of varying levels of complexity(parameters).

## **_FAQ_**

- **Q:** Can we use different parameters for different parts of the tree? To account for different mutation rates?

**A:** Its possible, it is a current area of research.

408

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

### **27.3.2 Distances to Trees**

If we have a weighted phylogenetic tree, we can find the total weight (length) of the shortest path between a pair of leaves by summing up the individual branch lengths in the path. Considering all such pairs of leaves, we have a distance matrix representing the data. In distance based methods, the problem is to reconstruct the tree given this distance matrix.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 27.9: Mapping from a tree to a distance matrix and vice versa

## **_FAQ_**

- **Q:** In Figure 27.9 The m and r sequence divergence metrics can have some overlap so distance between mouse and rat is not simply m+r. Wouldn’t that only be the case if there was no overlap?

- **A:** If you model evolution correctly, then you would get evolutionary distance. It’s an inequality rather than an equality and we agree that you can’t exactly infer that the given distance is the precise distance. Therefore, the sequences’ distance between mouse and rat is probably less than m + r because of overlap, convergent evolution, and transversions.

However, note that there is not a one-to-one correspondence between a distance matrix and a weighted tree. Each tree does correspond to one distance matrix, but the opposite is not always true. A distance matrix has to satisfy additional properties in order to correspond to some weighted tree. In fact, there are two models that assume special constraints on the distance matrix:

- **Ultrametric:** For all triplets ( _a, b, c_ ) of leaves, two pairs among them have equal distance, and the third distance is smaller; i.e. the triplet can be labelled _i, j, k_ such that


Conceptually this is because the two leaves that are more closely related (say _i, j_ ) have diverged from the thrid ( _k_ ) at exactly the same time. and the time separation from the third should be equal, whereas the separation between themselves should be smaller.

409

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics


Figure 27.10: Ultrametric distances.

**Additive:** Additive distance matrices satisfy the property that all quartet of leaves can be labelled _i, j, k, l_ such that

_dij_ + _dkl ≤ dik_ + _djl_ = _dil_ + _djk_

This is in fact true for all positive-weight trees. For any 4 leaves in a tree, there can be exactly one topology, i.e.


Figure 27.11: Additive distances.

Then the above condition is term by term equivalent to

( _a_ + _b_ ) + ( _c_ + _d_ ) _≤_ ( _a_ + _m_ + _c_ ) + ( _b_ + _m_ + _d_ ) = ( _a_ + _m_ + _d_ ) + ( _b_ + _m_ + _c_ )

. This equality corresponds to all pairwise distances that are possible from traversing this tree.

These types of redundant equalities must occur while mapping a tree to a distance matrix, because a tree of _n_ nodes has _n −_ 1 parameters, one for each branch length, while a distance matrix has _n_<sup>2</sup> parameters. Hence, a tree is essentially a lower dimensional projection of a higher dimensional space. A corollary of this observation is that not all distance matrices have a corresponding tree, but all trees map to unique distance matrices.

However, real datasets do not exactly satisfy either ultrameric or additive constraints. This can be due to noise (when our parameters for our evolutionary models are not precise), stochasticity and randomness (due to small samples), fluctuations, different rates of mutations, gene conversions and horizontal transfer. Because of this, we need tree-building algorithms that are able to handle noisy distance matrices.

Next, two algorithms that directly rely on these assumptions for tree reconstruction will be discussed.

410

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

#### **UPGMA - Unweighted Pair Group Method with Arithmetic Mean**

This is exactly same as the method of **Hierarchical clustering** discussed in Lecture 13, Gene Expression Clustering. It forms clusters step by step, from closely related nodes to ones that are further separated. A branching node is formed for each successive level. The algorithm can be described properly by the following steps:

#### **Initialization:**

1. Define one leaf _i_ per sequence _xi_ .

2. Place each leaf _i_ at height 0.

3. Define Clusters _Ci_ each having one leaf _i_ .

#### **Iteration:**

1. Find the pairwise distances _dij_ between each pairs of clusters _Ci, Cj_ by taking the arithmetic mean of the distances between their member sequences.

2. Find two clusters _Ci, Cj_ such that _dij_ is minimized.

3. Let _Ck_ = _Ci ∪ Cj_ .


Figure 27.12: UPGMA / Hierarchical Clustering

   4. Define node _k_ as parent of nodes _i, j_ and place it at height _dij/_ 2 above _i, j_ .

   5. Delete _Ci, Cj_ .

- **Termination:** When two clusters _Ci, Cj_ remain, place the root at height _dij/_ 2 as parent of the nodes _i, j_

#### **Ultrametrification of non-ultrametric trees**

If a tree does not satisfy ultrametric conditions, we can attempt to find a set of alterations to an nxn symmetric distance matrix that will make it ultrametric. This can be accomplished by constructing a completely connected graph with weights given by the original distance matrix, finding a minimum spanning tree (MST) of this graph, and then building a new distance matrix with elements D(i,j) given by the largest weight on the unique path in the MST from i to j. A spanning tree of the fully connected graph simply identifies a subset of edges that connects all nodes without creating any cycles, and a minimum spanning tree is a spanning tree that minimizes the total sum of edge weights. An MST can be found using ie Prims algorithm, and then used to correct a non-ultrametric tree.

#### **Weaknesses of UPGMA**

Although this method is guaranteed to find the correct tree if the distance matrix obeys the ultrameric property, it turns out to be a inaccurate algorithm in practice. Apart from lack of robustness, it suffers from the molecular clock assumption that the mutation rate over time is constant for all species. However, this is not true as certain species such as rat and mice evolve much faster than others. Such differences in mutation

411

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

rate can lead to long branch attraction; nodes sharing a lower mutation rate but found in distinct lineages may be merged, leaving those nodes with higher mutation rates (long branches) to appear together in the tree. The following figure illustrates an example where UPGMA fails:


Figure 27.13: UPGMA fails to find the correct tree in this case

#### **Neighbor Joining**

The neighbor joining method is guaranteed to produce the correct tree if the distance matrix satisfies the additive property. It may also produce a good tree when there is some noise in the data. The algorithm is described below:

**Finding the neighboring leaves:** Let


Here _n_ is the number of nodes in the tree; hence, _ri_ is the average distance of a node to the other nodes. It can be proved that the above modification ensures that _Dij_ is minimal only if _i, j_ are neighbors. (A proof can be found in page 189 of Durbin’s book).

**Initialization:** Define _T_ to be the set of leaf nodes, one per sequence. Let _L_ = _T_

#### **Iteration:**

1. Pick _i, j_ such that _Dij_ is minimized.


   3. Add _k_ to _T_ , with edges of lengths _dik_ = 2<sup><u>1</u></sup> ( _dij_ + _rirj_ )

   4. Remove _i, j_ from _L_

   5. Add _k_ to _L_

- **Termination:** When _L_ consists of two nodes _i, j_ , and the edge between them of length _dij_ , add the root node as parent of _i_ and _j_ .

#### **Summary of Distance Methods Pros and Cons**

The methods described above have been shown to capture many interesting features of phylogenetic relationships, and are typically very fast in the algorithmic sense. However, some information is certainly

412

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

lost in the distance matrix, and typically only a single tree is proposed. Serious errors, such as long branch attraction, can be made when basic assumptions about mutation rate etc. are violated. Finally, distance methods make no inference about the history of a particular site, and thus do not make suggestions about the ancestral state of a sequence.

## **27.4 Character-Based Methods**


Figure 27.14: An overview of the character based methods

In character-based methods, the goal is to first create a valid algorithm for scoring the probability that a given tree would produce the observed sequences at its leaves, then to search through the space of possible trees for a tree that maximizes that probability. Good algorithms for tree scoring, and while searching the space of trees is theoretically NP-Hard (Due to the large number of possible trees), tractable heuristic search methods can in many cases find good trees. We’ll first discuss tree scoring algorithms, then search techniques.

413

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

### **27.4.1 Scoring**

There are two main algorithms for tree scoring. The first approach, which we will call parsimony reconstruction, is based on Occam’s razor, and scores a topology based on the minimum number of mutations it implies, given the (known) sequences at the leaves. This method is simple, intuitive, and fast. The second approach is a maximum likelihood method which scores trees by explicitly modeling the probability of observing the sequences at the leaves given a tree topology.

#### **Parsimony**

Conceptually, this method is simple. It simply assigns a value of for each base pair at each ancestral node such that the number of substitutions is minimized. The score is then just the sum over all base pairs of that minimal number of mutations at each base pair. (Recall that the eventual goal is to find a tree that minimizes that score.)

To reconstruct the ancestral sequences at internal nodes on the tree, the algorithm first scans up from the (known) leaf sequences, assigning a set of bases at each internal node based on its children. Next, it iterates down the tree, picking bases out of the allowed sets at each node, this time based on the node’s parents. The following illustrates this algorithm in detail (note that there are 2 _N −_ 1 total nodes, indexed from the root, such that the known leaf nodes have indices _N −_ 1 through 2 _N −_ 1):


Figure 27.15: Parsimony scoring: union and intersection

414

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics


Figure 27.16: Parsimony traceback to find ancestral neucleotides


Figure 27.17: Parsimony scoring by dynamic programming

As we mentioned before, this method is simple and fast. However, this simplicity can distort the scores it assigns. For one thing, the algorithm presented here assumes that a given base pair undergoes a substitution along at most one branch from a given node, which may lead it to ignore highly probably internal sequences that violate this assumption. Furthermore, this method does not explicitly model the time represented along each edge, and thus cannot account for the increased chance of a substitution along edges that represent a long temporal duration, or the possibility of different mutation rates across the tree. Maximum likelihood methods largely resolve these shortcomings, and are thus more commonly used for tree scoring.

415

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

#### **Maximum Likelihood - Peeling Algorithm**

As with the general Maximum likelihood methods, this algorithm scores a tree according to the (log) joint probability of observing the data and the given tree, i.e. _P_ ( _D, T_ ). The peeling algorithm again considers individual base pairs and assumes that all sites evolve independently. As in the parsimony method, this algorithm considers all base pairs independently: it calculates the probability of observing the given characters at each base pair in the leaf nodes, given the tree, a set of branch lengths, and the maximum likelihood assignment of the internal sequence, then simply multiplies this probabilities over all base pairs to get the total probability of observing the tree. Note that the explicit modeling of branch lengths is a difference from the previous approach.

416

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics


Figure 27.18: A tree to be scored using the peeling algorithm. n=4

Here each node has a character _xi_ and _ti_ is the corresponding branch length from its parent. Note that we already know the values _x_ 1 _, x_ 2 _· · · xn_ , so they are constants, but _xn_ +1 _, · · · x_ 2 _n−_ 1<sup>areunknowncharacters</sup> at ancestral nodes which are variables to which we will assign maximum likelihood values. (Also note that we have adopted a leaves-to-root indexing scheme for the nodes, the opposite of the scheme we used before.) We want to compute _P_ ( _x_ 1 _x_ 2 _· · · xn|T_ ). For this we sum over all possible combinations of values at the ancestral nodes. this is called marginalization. In this particular example


There are 4<sup>_n−_1</sup> terms in here, but we can use the following factorization trick:


Here we assume that each branch evolves independently. And the probability _P_ ( _b|c, t_ ) denotes the probability of base _c_ mutating to base _b_ given time _t_ , which is essentially obtained from the Jukes Cantor model or some more advanced model discussed earlier. Next we can move the factors that are independent of the summation variable outside the summation. That gives:


Let _Ti_ be the subtree below _i_ . In this case, our 2 _n −_ 1 _×_ 4 dynamic programming array computes _L_ [ _i, b_ ], the probability _P_ ( _Ti|xi_ = _b_ ) of observing _Ti_ , if node _i_ contains base _b_ . Then we want to compute the probability of observing _T_ = _T_ 2 _n−_ 1<sup>,whichis</sup>


Note that for each ancestral node _i_ and its childer _j, k_ , we have


Subject to the initial conditions for the leaf nodes, i.e. for _i ≤ n_ :

_L_ [ _i, b_ ] = 1 if _xi_ = _b_ and 0 otherwise


Figure 27.19: The recurrence

417

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

418

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

Note that we still do not have the values _P_ ( _x_ 2 _n−_ 1 = _b_ ). It is usually assigned equally or from some prior distribution, but it does not affect the results greatly. The final step is of course to multiply all the probabilities for individual sites to obtain the probability of observing the set of entire sequences. In addition, once we have assigned the maximum likelihood values for each internal node given the tree structure and the set of branch lengths, we can multiply the resulting score by some prior probabilities of the tree structure and the set of branch lengths, which are often generated using explicit modeling of evolutionary processes, such as the Yule process or birth-death models like the Moran process. The result of this final multiplication is called the a posteriori probability, using the language of Bayesian inference. The overall complexity of this algorithm is _O_ ( _nmk_<sup>2</sup> ) where _n_ is the number of leaves (taxa), _m_ is the sequence length, and _k_ is the number of characters.

There are addvantages and disadvantages of this algorithm. Such as

#### **Advantages:**

1. Inherently statistical and evolutionary model-based.

2. Usually the most consistent of the methods available.

3. Used for both character and rate analyses

4. Can be used to infer the sequences of the extinct ancestors.

5. Account for branch-length effects in unbalanced trees.

6. Nucleotide or amino acid sequences, other types of data.

#### **Disadvantages:**

1. Not as simple and intuitive as many other methods.

2. Computationally intense Limited by, number of taxa and sequence length).

3. Like parsimony, can be fooled by high levels of homoplasy.

4. Violations of model assumptions can lead to incorrect trees.

### **27.4.2 Search**

A comprehensive search over the space of all trees would be extremely costly. The number of full rooted trees with _n_ + 1 leaves is the _n_ -th catalan number


Moreover, we must compute the maximum likelihood set of branch lengths for each of these trees. Thus, it is an NP-Hard problem to maximize the score absolutely for all trees. Fortunately, heuristic search algorithms can generally identify good solutions in the tree space. The general framework for such search algorithms is as follows:

- **Inititalization:** Take some tree as the base of iteration (randomly or according to some other prior, or from the distance based direct algorithms).

**Proposal:** Propose a new tree by randomly modifying the current tree slightly.

**Score:** Score the new proposal according to the methods described above.

419

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

- **Select:** Randomly select the new tree or the old tree (corresponding probabilities according to the score(likelihood) ratio.

- **Iterate:** Repeat to proposal step unless some termination criteria is met (some threshold score or number of steps reached.

the basic idea here is the heuristic assumption that the scores of closely related trees are similar, so that good solutions may be obtained by successive local optimization, which is expected to converge towards a overall good solution.

#### **Tree Proposal**

One method for modifying trees is the Nearest Neighbor Exchange (NNI), illustrated below.

Figure 27.20: An unit step using Nearest Neighbor Interchange scheme

Another common method, not described here, is Tree Bisection and Join (TBJ). The important criteria for such proposal rules is that:

- (a) The tree space should be connected, i.e. any pair of trees should be obtainable from each other by successive proposals.

- (b) An individual new proposal should be sufficiently close to the original. So that it is more likely to be a good solution by virtue of the proximity to an already discovered good solution. If individual steps are too big, the algorithm may move away from an already discovered solution (also depends on the selection step). In particular, note that the measure of similarity by which the measure these step sizes is precisely the difference in the likelihood scores assigned to the two trees.

#### **Selection**

Choosing whether or not to adopt a given proposal, like the process of generating the proposal itself, is inherently heuristic and varies. A general rules of thumb is:

1. If the new one has a better score, always accept it.

2. If it has a worse score, there should be some probability of selecting it, otherwise the algorithm will soon fixate in a local minima, ignoring better alternatives a little far away.

3. There should not be too much probability of selecting an worse new proposal, otherwise, it risks rejecting a known good solution.

It is the trade-off between the steps 2 and 3 that determines a good selection rule. Metropolis Hastings is a Markov Chain Monte Carlo Method (MCMC) that defines specific rules for exploring the state space in a way that makes it a sample from the posterior distribution. These algorithms work somewhat well in practice, but there is no guarantee for finding the appropriate tree. So a method known as bootstrapping is used, which is basically running the algorithm over and over using subsets of the base pairs in the leaf sequences,. then favoring global trees that match the topologies generated by using only these subsequences.

420

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

## **27.5 Possible Theoretical and Practical Issues with Discussed Approach**

A special point must be made about distances. Since distances are typically calculated between aligned gene sequences, most current tree reconstruction methods rely on heavily conserved genes, as non-conserved genes would not give information on species without those genes. This causes the ignoring of otherwise useful data. Therefore, there are some algorithms that try to take into account less conserved genes in reconstructing trees but these algorithms tend to take a long time due to the NP-Hard nature of reconstructing trees.

Additionally, aligned sequences are still not explicit in regards to the events that created them. That is, combinations of speciation, duplication, loss, and horizontal gene transfer (hgt) events are easy to mix up because only current DNA sequences are available. (see [11] for a commentary on such theoretical issues) A duplication followed by a loss would be very hard to detect. Additionally, a duplication followed by a speciation could look like an HGT event. Even the probabilities of events happening is still contested, especially horizontal gene transfer events.

Another issue is that often multiple marker sequences are concatenated and the concatenated sequence is used to calculate distance and create trees. However, this approach assumes that all the concatenated genes had the same history and there is debate over if this is a valid approach given that events such as hgt and duplications as described above could have occurred differently for different genes. [8] is an article showing how different phylogenetic relationships were found depending on if the tree was created using multiple genes concatenated together or if it was created using each of the individual genes. Conversely, additional [4] claims that while hgt is prevalent, orthologs used for phylogenetic reconstruction are consistent with a single tree of life. These two issues indicate that there is clearly debate in the field on a non arbitrary way to define species and to infer phylogenetic relationships to recreate the tree of life.

## **27.6 Towards final project**

### **27.6.1 Project Ideas**

1. Creating better distance models such as taking into account duplicate genes or loss of genes. It may also be possible to analyze sequences for peptide coding regions and calculate distances based on peptide chains too.

2. Creating a faster/more accurate search algorithm for turning distances into trees.

3. Analyze sequences to calculate probabilities of speciation, duplication, loss, and horizontal gene transfer events.

4. Extending an algorithm that looks for HGTs to look for extinct species. A possible use for HGTs is that if a program were to infer HGTs between different times, it could mean that there was a speciation where one branch is now extinct (or not yet discovered) and that branch had caused an HGT to the other extant branch.

### **27.6.2 Project Datasets**

1. 1000 Genomes Project http://www.1000genomes.org/

2. Microbes Online http://microbesonline.org/

421

6.047/6.878 Lecture 20:Molecular Evolution and Phylogenetics

## **27.7 What Have We Learned?**

In this chapter, we have learnt different methods and approaches for reconstructing Phylogenetic trees from sequence data. In the next chapter, its application in gene trees and species trees and the relationship between those two will be discussed, as well as modelling phylogenies among populations within a species and between closely related species.

## **Bibliography**

- [1] 1000 genomes project.

- [2] et al Ciccarelli, Francesca. Toward automatic reconstruction of a highly resolved tree of life. _Science_ , 311, 2006.

- [3] Tal Dagan and William Martin. The tree of one percent. _Genome Biology_ , Nov 2006.

- [4] Ochman Howard Daubin Vincent, Moran Nancy A. Phylogenetics and the cohesion of bacterial genomes. _Science_ , 301, 2003.

- [5] A.J. Enright, S. Van Dongen, and C. A. Ouzounis. An efficient algorithm for large-scale detection of protein familes. _Nucleic Acids Research_ , 30(7):1575–1584, Apr 2002.

- [6] Stephanie Guindon and Olivier Gascuel. A simple, fast, and accurate algorithm to estimate large phylogenies by maximum likelihood. _Systems Biology_ , 52(5):696–704, 2003.

- [7] Sanderson MJ. r8s: Inferring absolute rates of molecular evolution and divergence times in the absence of a molecular clock. _Bioinformatics_ , 19(2):301–302, Jan 2003.

- [8] R. Thane Papke, Olga Zhaxybayeva, Edward J Fiel, Katrin Sommerfeld, Denise Muise, and W. Ford Doolittle. Searching for species in haloarchaea. _PNAS_ , 104(35):14092–14097, 2007.

- [9] Pere Puigbo, Yuri I Wolf, and Eugene V Koonin. Search for a ’tree of life’ in the thicket of the phylogenetic forest. _Journal of Biology_ , 8(59), July 2009.

- [10] Sagi Snir, Yuri I Wolf, and Eugene V Koonin. Universal pacemaker of genome evolution. _PLoS computational biology_ , 8(11), 2012.

- [11] Douglas L Theobald. A formal test of the theory of universal common ancestry. _Nature_ , 465:219–222, 2010.

422

CHAPTER

## **TWENTYEIGHT**

## PHYLOGENOMICS II

Guest Lecture by Matt Rasmussen

2012: Updated by Orit Giguzinsky and Ethan Sherbondy

### **Figures**

|28.1 Species Tree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|422|
|---|---|
|28.2 Gene Tree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|423|
|28.3 Gene Tree Inside a Species Tree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|423|
|28.4 Gene Family Evolution: Gene Trees and Species Trees . . . . . . . . . . . . . . . . . . . .|424|
|28.5 Mapping Diagram<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|424|
|28.6 Nesting Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|424|
|28.7 Maximum Parsimony Reconciliation (MPR)<br>. . . . . . . . . . . . . . . . . . . . . . . . .|425|
|28.8 Maximum Parsimony Reconciliation Recursive Algorithm<br>. . . . . . . . . . . . . . . . . .|425|
|28.9 Reconciliation Example 1, simple mapping case . . . . . . . . . . . . . . . . . . . . . . . .|426|
|28.10Reconciliation Example 2, parsimonious reconciliation for complex case<br>. . . . . . . . . .|426|
|28.11Reconciliation Example 3, non parsimonious reconciliation for complex case . . . . . . . .|427|
|28.12Reconciliation Example 4, invalid Reconciliation<br>. . . . . . . . . . . . . . . . . . . . . . .|427|
|28.13Species Tree Reconstruction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|428|
|28.14Using species trees to improve gene tree reconstruction.<br>. . . . . . . . . . . . . . . . . . .|429|
|28.15We can develop a model for what kind of branch lengths we can expect.<br>We can use<br>conserved gene order to tell orthologs and build trees.<br>. . . . . . . . . . . . . . . . . . . .|429|
|28.16Branch length can be modeled as two different rate components: gene specific and species<br>specific.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|430|
|28.17The Wright-Fisher model<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|431|
|28.18Many iterations of Wright-Fisher yielding a lineage tree<br>. . . . . . . . . . . . . . . . . . .|431|
|28.19The coalescent model. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|432|
|28.20Geometric probability distribution for coalescent events in k lineages. . . . . . . . . . . . .|433|
|28.21Multispecies Coalescent Model. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|434|
|28.22MPR reconciliation of genes and species tree. . . . . . . . . . . . . . . . . . . . . . . . . .|435|
|28.23Inaccuracies in gene tree.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|435|


423

6.047/6.878 Lecture 21: Phylogenomics II

437

28.24Recombination. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## **28.1 Introduction**

In the previous chapter, we covered techniques for reasoning about evolution in terms of trees of descent. The algorithms we covered for tree-building, UPGMA and neighbor-joining, assumed that we were comparing fully aligned sections of sequences.

In this section, we present additional models for using phylogenetic trees in different contexts. Here we clarify the differences between species and gene trees. We then cover a framework called reconciliation which lets us effectively combine the two by mapping gene trees onto species trees. This mapping gives us a means of inferring gene duplication and loss events.

We will also present a phylogenetic perspective for reasoning about population genetics. Since population genetics deals with relatively recent mutation events, we offer the Wright-Fisher model as a tool for representing changes in whole populations. Unfortunately, when dealing with real-world data, we usually are only able to sequence genes from the current living descendants of a group. As a remedy to this shortcoming, we cover the Coalescent model, which you can think of as a time-reversed Wright-Fisher analog.

By using coalescence, we gain a new means for estimating divergence times and population sizes across multiple species. At the end of the chapter, we touch briefly on the challenges of using trees to model recombination events and summarize recent work in the field along with frontiers open for exploration.

## **28.2 Inferring Orthologs/Paralogs, Gene Duplication and Loss**

There are two commonly used trees, Species tree and Gene tree. This section explains how these trees can be used and how to fit a gene tree inside a species tree (reconciliation).

### **28.2.1 Species Tree**

Species trees that show how different species evolved from one another. These trees are created using morphological characters, fossil evidence, etc. The leaves of each tree are labeled as species and the rest of the tree shows how these species are related. An example of a species tree is shown in Figure 28.1. Note: in lecture it is mentioned that a species can be thought of as a ”bag of genes”, that is to say the group of common genes among members of a species.

424

6.047/6.878 Lecture 21: Phylogenomics II


Figure 28.1: Species Tree

### **28.2.2 Gene Tree**

Gene trees are trees that look at specific genes in different species. The leaves of gene trees are labeled with gene sequences or gene ids associated with specific sequences. Figure 28.2 shows an example of a gene tree that has 4 genes (leaves). The sequences associated with each gene are presented on the right side of Figure 28.2.


Figure 28.2: Gene Tree

### **28.2.3 Gene Family Evolution**

Gene trees evolve inside a species tree. An example of a gene tree contained in a species tree is shown in Figure 28.3 below.


Figure 28.3: Gene Tree Inside a Species Tree

The next sub section explains how we can fit gene trees inside a species trees using Reconciliation.

425

6.047/6.878 Lecture 21: Phylogenomics II

### **28.2.4 Reconciliation**

Reconciliation is an algorithm that helps compare gene trees to genome trees by fitting a gene tree fits inside a species tree. This is done by by mapping the vertices in the gene tree to vertices in the species tree. This sub section will focus on Reconciliation, related definitions, algorithms (Maximum Parsimony Reconciliation and SPIDIR) and examples.

#### **Definitions**

Two genes are **orthologs** if their most recent common ancestor (MRCA) is a speciation (splitting into different species).

**Paralogs** are genes whose MRCA is a duplication.

Figure 28.4 below illustrates how these types of genes can be represented in a gene tree. The tree below has 4 speciation nodes, one duplication and one loss.


Figure 28.4: Gene Family Evolution: Gene Trees and Species Trees

A mapping diagram is a diagram that shows the node mapping from the gene tree to the species tree. Figure 28.5 shows an example of a mapping diagram.


Figure 28.5: Mapping Diagram

A nesting diagram shows how the gene tree can be nested inside the species tree. For every mapping diagram there is a nesting diagram. Figure 28.6 shows an example of a possible nesting diagram for the mapping diagram in Figure 28.5.


Figure 28.6: Nesting Diagram

426

6.047/6.878 Lecture 21: Phylogenomics II

#### **Maximum Parsimony Reconciliation (MPR) Algorithm**

MPR is an algorithm that fits a gene tree into a species tree while minimizing the number of duplications and deletions.


Figure 28.7: Maximum Parsimony Reconciliation (MPR)

Given a gene tree and a species tree, the algorithm finds the reconciliation that minimizes the number of duplications and deletions. Figure 28.7 above shows an example of a possible mapping from a gene tree to a species tree. Figure 28.8 presents the pseudocode for the MPR algorithm. The base case involves matching the leaves of the gene tree to the leaves of the species tree; the algorithm then progresses up the vertices of the gene tree, drawing a relationship between the MRCA of all leaves within a given vertex’s sub-tree and the corresponding MRCA vertex in the species tree. In the pseudocode, I(G) represents the species tree and L(G) represents the gene tree.


Figure 28.8: Maximum Parsimony Reconciliation Recursive Algorithm

We map the arrows low as possible, since lower mapping usually results in fewer events. However, we cannot map too low. Mapping too low means that we’re violating the constraint that the MRCA of a given node is at least as high as the MRCA of its children. We map as low as we can without violating the descendentancestor relationships. The algorithm goes recursively from bottom up, starting from the leaves. Since we sample genes from known species to build the gene tree, there’s a direct mapping between the leaves of the gene tree and the leaves of the species tree. To map the ancestors, for each node (going recursively up the tree) we look at the right child and left child and take the least common ancestor (LCA) of the species that they map to. If a node maps to its right or left child, we know there is a duplication. An expected branch that does not exist indicates a loss.

427

6.047/6.878 Lecture 21: Phylogenomics II

#### **Reconciliation Examples**


Figure 28.9: Reconciliation Example 1, simple mapping case

In Figure 28.9, the nodes can be mapped straight across, since there are no duplications or losses.


Figure 28.10: Reconciliation Example 2, parsimonious reconciliation for complex case

In Figure 28.10, we see a parsimonious (minimum number of losses and duplications) reconciliation for a case in which nodes from the gene tree cannot be mapped straight across. This is a result of the swapped locations of h1 and d1 in the gene tree; the least common ancestor for d1, m1, and r1 is now the root vertex of the species tree.

428

6.047/6.878 Lecture 21: Phylogenomics II


Figure 28.11: Reconciliation Example 3, non parsimonious reconciliation for complex case

Figure 28.11 shows a non-parsimonious reconciliation . The parsimonious mapping for the same trees is shown in Figure 28.9.


Figure 28.12: Reconciliation Example 4, invalid Reconciliation

Figure 28.12 shows an invalid reconciliation. This reconciliation is invalid since it does not respect descendentancestor relationships. In order for this reconciliation to be possible, the descendent would have to travel back in time and be created before its ancestor. Clearly, such a scenario would be impossible. A valid reconciliation must satisfy the following: **If a** _<_ **b in G, then R[a]** _≤_ **R[b] in S** .

### **28.2.5 Interpreting Reconciliation Examples**

Gene trees, when reconciled with species trees, offer significant insight into evolutionary events (namely duplications and losses). Duplications describe the same gene being found at a separate loci - m2 or r2, in this situation - and is a major mechanism for creating new genes and functions. These evolutionary consequences fall into three categories: nonfunctionalization, neofunctionalization and subfunctionalization. Nonfunctionalization is quite common and causes one of the copies, unsurprisingly, to simply not function. Neofunctionalization is when one of the copies develops an entirely new function. Subfunctionalization is when the copies retain different parts (dividing up the labor, in a way), and together, perform the same function.

429

6.047/6.878 Lecture 21: Phylogenomics II

In Figure 4, we see that a duplication event occurred before the divergence of mice and rats as species. This is why we see similar genes at both m1 and m2, which represent two separate loci. d2 and h2 are not included in the graph because at the gene being considered is not present at those loci (since no duplication event occurred), whereas it is at both m2 and r2.

If the duplication event were to have occurred one level higher in Figure 4, without seeing a corresponding h2 in the gene tree, this would imply a loss within the h branch of the species tree.

## **28.3 Reconstruction**

In the previous section we learned how to compare and combine gene trees and species trees. In this section, we will use this information to reconstruct gene trees and species trees.

### **28.3.1 Species Tree Reconstruction**

In the past, it was really hard to identify a marker gene that would give insight into the differentiation for a specific species. As sequencing improved, we started having lots of sequencing data on various genes. Based on different sets of loci, people built different trees, which were highly dependent on the set of loci chosen. Possible reasons why trees differ include noise (from statistical estimate errors and noise), hidden duplications and losses, and allele sorting in a population.

#### **Species Tree Reconstruction Problem**


Figure 28.13: Species Tree Reconstruction

Given lots of different gene trees that disagree, our goal is to make them into one species tree (as shown in Figure 28.13. There are lots of different algorithms that reconstruct species trees. These algorithms include Supermatrix methods (Rokas 2003, Ciccareli 2006), Supertree methods (Creevey & McInerney 2005), Minimizing Deep Coalescence (Maddison & Knowles 2006) and Modeling coalescence (Liu & Pearl 2007).

One way to do this, which is mostly effective for noisy data, is to pull more data together in order to increase accuracy. This is done by concatenating gene alignments into a super-matrix.

Another method involves building a tree for each one and using a consensus method to summarize these

430

6.047/6.878 Lecture 21: Phylogenomics II

trees. Then we identify analogous branches across the a lot of trees and build a species tree that has the branches that occur most frequently.

There is another way to reconstruct a species tree, which is effective in case the gene trees disagree because of duplications and losses. The goal is to find the species tree that applies the fewest duplications. We build all the gene trees and then propose a species tree. Next, we use reconciliation to determine the number of events each gene tree combined with the proposed species tree implies. Then, we propose other species trees and move branches around. Wrong species trees tend to have lots of events that did not happen. The correct tree should have the fewest number of events.

### **28.3.2 Improving Gene Tree Reconstruction and Learning Across Gene Trees**

We can use methods similar to those described above to build better gene trees. This can be done by using information from a species tree to study a gene tree of interest. For example, species trees can be used to determine when losses and duplications occurred. The idea is that we can use the fact that species trees are often built from the entire genome, to obtain more information about related gene trees. We can use both the branch length and the number of events to do this.


Figure 28.14: Using species trees to improve gene tree reconstruction.

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

If we know the species tree, we can develop a model for what kind of branch lengths we can expect. We can use conserved gene order to tell orthologs and build trees.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 28.15: We can develop a model for what kind of branch lengths we can expect. We can use conserved gene order to tell orthologs and build trees.

431

6.047/6.878 Lecture 21: Phylogenomics II

When a gene is fast evolving in one species, it is fast evolving in all species. We can model a branch length as two different rate components. One is gene specific (present across all species) and the other is species specific, which is customized to a specific species.


Figure 28.16: Branch length can be modeled as two different rate components: gene specific and species specific.

This method greatly improves reconstruction accuracy.

## **28.4 Modeling Population and Allele Frequencies**

With the advent of next-gen sequencing, it is becoming economical to sequence the genomes of many individuals within a population. In order to make sense of how alleles spread through a population, it’s helpful to have a model to compare data against. The **Wright-Fisher** reproduction model has filled this role for the past 70 years.

### **28.4.1 The Wright-Fisher Model**

Like HMMs, Wright-Fisher is a Markov process: at each step, the system randomly progresses, and the current state of the system depends only on the previous state. In this case, state transitions represent reproduction. By modeling the transmission of chromosomes to offspring, we can study genetic drift.

The model makes a number of simplifying assumptions:

1. Population size, **N** , is constant at each generation.

2. Only members of the same generation reproduce (no overlap).

3. Reproduction occurs at random.

4. The gene being modeled only has 2 alleles.

5. Genes undergo neutral selection.

Note that Wright-Fisher is not an appropriate choice if you’re trying to model the change in frequency of a gene that is positively or negatively selected for. If we use Wright-Fisher to model the chromosomes of diploid individuals, the population size of the model becomes **2N** .

432

6.047/6.878 Lecture 21: Phylogenomics II


Figure 28.17: The Wright-Fisher model

In English, here’s how Wright-Fisher works:

At every generation, for each child, we randomly select from the parents (with replaccement). The allele of the child becomes that of the randomly selected parent.

We repeat this process for many generation, with the children serving as the new parents, ignoring the ordering of chromosomes.

It really is that simple. To determine the probability of _k_ copies of an allele existing in the child generation when it had a frequency of _p_ in the parent generation, we can use this formula:


Here, _q_ = (1 _− p_ ). It is the frequency of non-p alleles in the parent generation.


© Sinauer Associates, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 28.18: Many iterations of Wright-Fisher yielding a lineage tree

Now we can begin to explore such questions as: how probable is it and how many generations is it

433

6.047/6.878 Lecture 21: Phylogenomics II

expected to take for a given allele to become **fixed** , meaning the allele is present in _every_ member of the population?

The expected time (in generations) for fixation, given the assumptions made by Wright-Fisher, is proportionate to 4 _NE_ , where _NE_ is the effective population size.

Again, it’s important to keep in mind the limitations of this model and ask if it actually makes sense for the system you’re trying to represent. Consider how you could tweak the proposed model to account for a selection coefficient ranging between -1 (lethal negative selection) and 1 (strong positive selection).

### **28.4.2 The Coalescent Model**

The problem with the Wright-Fisher model is that it assumes you know the allele frequencies of the ancentral generation. When dealing with the genomes of present species, these quantities are unknown. The Coalescent Model solves this conundrum by thinking retrospectively. That is to say: we start with the alleles of the _current_ generation, and work our way _backwards_ in time. The basic Coalescence Model makes the same assumptions as Wright-Fisher. At each generation, we ask: what is the probability of the two identical alleles coalescing, or sharing a parent, in the previous generation.

We can pose the probability of a coalescence event occuring in the previous generation as the probability of coalescence _not_ occuring in any of the _t −_ 1 generations prior to the last one, times the probability of it occuring in the previous (the t-th) generation. This is equivalent to the expression:


Where _Ne_ is the effective population size.


Figure 28.19: The coalescent model.

By approximating this geometric distribution as an exponential one: _Pc_ ( _t_ ) = 2 _N_ <u>1</u> _e_<sup>_e−_(</sup> 2<sup>_t−_</sup> _Ne_<sup>1)</sup> , we can determine the expected number of generations back until coalescence, which turns out to be 2 _Ne_ , with a standard deviation of 2 _Ne_ .

434

6.047/6.878 Lecture 21: Phylogenomics II

To ask about the coalescence of _multiple_ lineages at a given generation, we must, as in Wright-Fisher, use a binomial distribution. The probability of _k_ lineages coalescing for the _first_ time at generation t is:


And again, this can be approximated with an exponential distribution for sufficiently large k. The individual at which two lineages converge is referred to as the **Most Recent Common Ancestor** . By continually moving backwards until all ancestors coalesce, we end up with a new kind of tree! And by comparing the tree resulting from coalescence with a gene tree we’ve constructed, discrepancies between the two may signal that certain assumptions of the Coalescent Model have been violated. Namely, selection may be occuring.


Figure 28.20: Geometric probability distribution for coalescent events in k lineages.

435

6.047/6.878 Lecture 21: Phylogenomics II

### **28.4.3 The Multispecies Coalescent Model**


Figure 28.21: Multispecies Coalescent Model.

Courtesy of Elsevier, Incorporate. Used with permission. Source: Degnan, James H., and Noah A. Rosenberg. "Gene Tree Discordance, Phylogenetic Inference and the Multispecies Coalescent." _Trends in Ecology & Evolution_ 24, no. 6 (2009): 332-40.

We can take this idea once step further and track coalescence events across multiple species. Here, each genome of an individual species is treated as a lineage.

Note that there is a lag time between the separation of two populations and the time at which two gene lineages coalesce into a common ancestor. Also note how the rate of coalescence slows down as N gets bigger and for short branches.

In the image above, deep coalescence is depicted in light blue for three lineages. The species and gene trees here are incongruent since C and D are sisters in gene tree but not the species tree.

There is a<sup><u>2</u></sup> 3<sup>chancethatincongruencewilloccurbecauseoncewegettothelightbluesection,Wright-</sup> Fisher is memoryless and there is only<sup><u>1</u></sup> 3 chance that it will be congruent. The effect of incongruence is called **Incomplete Lineage Sorting** . By measuring the frequency at which **ILS** occurs, we gain insight into unusually large populations or unsually short branch lengths within the species tree.

You can build a maximum parsimony species tree based on the notion of minimizing the number of ILS events rather than minimizing implied duplication/loss events as covered previously. It is even possible to combine these two methods to, ideally, create a phylogeny that is more accurate than either of them would be individually.

## **28.5 SPIDIR**

### **28.5.1 Background**

As presented in the supplementary information for SPIDIR, a gene family is the set of genes that are descendents of a single gene in the most recent common ancestor (MRCA) of all species under consideration. Furthermore, genetic sequences undergo evolution at multiple scales, namely at the level of base pairs, and at the level of genes. In the context of this lecture, two genes are orthologs if their MRCA is a speciation event; two genes are paralogs if their MRCA is a duplication event.

436

6.047/6.878 Lecture 21: Phylogenomics II

In the genomic era, the species of a modern genes is often known; ancestral genes can be inferred by reconciling gene- and species-trees. A reconciliation maps every gene-tree node to a species-tree node. A common technique is to perform Maximum Parsimony Reconciliation (MPR), which finds the reconciliation R implying the fewest number of duplications or losses using the recursion over inner nodes _v_ of a gene tree _G_ . MPR fist maps each leaf of the gene tree to the corresponding species leaf of the species tree. Then the internal nodes of _G_ are mapped recursively:

#### _R_ ( _v_ ) = _MRCA_ ( _R_ ( _right_ ( _v_ )) _, R_ ( _left_ ( _v_ )))

If a speciation event and its ancestral node are mapped to the same node on the species tree. Then the ancestral node must be an duplication event.

Using MPR, the accuracy of the gene tree is crucial. Suboptimal gene trees may lead to an excess of loss and duplication events. For example, if just one branch is misplaced (as in **??** ) then reconciliation infers 3 losses and 1 duplication event. In [6], the authors show that the contemporaneous current gene tree methods perform poorly (60% accuracy) on single genes. But if we have longer concatenated genes, then accuracy may go up towards 100%. Furthermore, very quickly or slowly evolving genes carry less information as compared with moderately diverging sequences (40-50% sequence identity), and perform correspondingly worse. As corroborated by simulations, single genes lack sufficient information to reproduce the correct species tree. Average genes are too short and contains too few phylogenetically informative characters. While many early gene tree construction algorithms ignored species information, algorithms like SPIDIR capitalize on the insight that the species tree can provide additional information which can be leveraged for gene tree construction. Synteny can be used to independently test the relative accuracy of different gene tree reconstructions. This is because syntenic blocks are regions of the genome where recently diverged organisms have the same gene order, and contain much more information than single genes.


Figure 28.22: MPR reconciliation of genes and species tree.


Figure 28.23: Inaccuracies in gene tree.

There have been a number of recent phylogenomic algorithms including: RIO [2], which uses neighbor joining (NJ) and bootstrapping to deal with incogruencies, Orthostrapper [7], which uses NJ and reconciles to a vague species tree, TreeFAM [3], which uses human curation of gene trees as well as many others. A number of algorithms take a more similar track to SPIDIR [6], including [4], a probabilistic reconciliation algorithm [8], a Bayesian method with a clock,[9],and parsimony method using species tree , as well as more

437

6.047/6.878 Lecture 21: Phylogenomics II

recent developments: [1] a Bayesian method with relaxed clock and [5], a Bayesian method with gene and species specific relaxed rates (an extension to SPIDIR) .

### **28.5.2 Method and Model**

SPIDIR exemplifies an iterative algorithm for gene tree construction using the species tree. In SPIDIR, the authors define a generative model for gene-tree evolution. This consists of a prior for gene-tree topology and branch lengths. SPIDIR uses a birth and death process to model duplications and losses (which informs the prior on topology) and then then learns gene-specific and species-specific substitution rates (which inform the prior on branch lengths). SPIDIR is a _Maximum a posteriori (MAP)_ method, and, as such, enjoys several nice optimality criteria.

In terms of the estimation problem, the full SPIDIR model appears as follows:

_argmaxL, T, RP_ ( _L, T, R|D, S,_ Θ) = _argmaxL, T, RP_ ( _D|T, L_ ) _P_ ( _L|T, R, S,_ Θ) _P_ ( _T, R|S,_ Θ)

The parameters in the above equation are: _D_ = alignment data , _L_ = branch length _T_ = gene tree topology , _R_ = reconciliation , _S_ = species tree (expressed in times) , Θ = ( gene and species specific parameters [estimated using EM training], _λ_ , _µ_ dup/loss parameters)). This model can be understood through the three terms in the right hand expression, namely:

1. the sequence model– _P_ ( _D|T, L_ ). The authors used the common HKY model for sequence substitutions, which unifies Kimura’s two parameter model for transitions and transversions with Felsenstein’s model where substitution rate depends upon nucleotide equilibrium frequency.

2. the first prior term, for the rates model– _P_ ( _L|T, R, S,_ Θ), which the authors compute numerically after learning species and gene specific rates.

3. the second prior term, for the duplication/loss model– _P_ ( _T, R|S,_ Θ), which the authors describe using a birth and death process.

Having a rates model is very rates model very useful, since mutation rates are quite variable across genes. In the lecture, we saw how rates were well described by a decomposition into gene and species specific rates. In lecture we saw that an inverse gamma distribution appears to parametrize the gene specific substitution rates, and we were told that a gamma distribution apparently captures species specific substitution rates. Accounting for gene and species specific rates allows SPIDIR to build gene trees more accurately than previous methods. A training set for learning rate parameters can be chosen from gene trees which are congruent to the species tree. An important algorithmic concern for gene tree reconstructions is devising a fast tree search method. In lecture, we saw how the tree search could be sped up by only computing the full _argmaxL, T, RP_ ( _L, T, R|D, S,_ Θ) for trees with high prior probabilites. This is accomplished through a computational pipeline where in each iteration 100s of trees are proposed by some heuristic. The topology prior _P_ ( _T, R|D, S,_ Θ) can be computed quickly. This is used as a filter where only the topologies with high prior probabilities are selected as candidates for the full likelihood computation.

The performance of SPIDIR was tested on a real dataset of 21 fungi. SPIDER recovered over 96% of the synteny orthologs while other algorithms found less than 65%. As a result, SPIDER invoked much fewer number of duplications and losses.

438

6.047/6.878 Lecture 21: Phylogenomics II

## **28.6 Ancestral Recombination Graphs**

images/Recombination.jpg

Figure 28.24: Recombination.

In Figure 28.24 a, the two chromosomes at the top represent the homologous chromosomes of a parent. The red chromosome represents the genetic information from the mother and the blue chromosome represents the genetic information from the father (of the grandparent generation). Without crossing-over (recombination), the parent will either pass on the red or the blue genetic information to the offspring. In reality, recombination happens during meiosis so that a parent will pass on some genetic information from both grandparents, effectively passing on a better representation of the parent genetic information. At each generation, a recombination event can occur at any loci. The evolutionary history of recombination can be tracked through a sequential graph of trees, such that the _i_ th tree in the graph represents recombination at the _i_ th locus.

_Fill in this section based on: ������������������������������������������ and the course notes from 2012._ More on this topic could be added in the future

### **28.6.1 The Sequentially Markov Coalescent**

The Sequentially Markov Coalescent Model addresses the role of recombination in tree construction. With recombination involved, a sequence may have two parents, which complicates construction. The Sequentially Markov Coalescent Model tells us that move sequentially from left to right is a simpler and much more efficient approach to analyzing the tree; the approach essentially breaks the tree into local trees and overlays them to describe recombination events. More can be read in the following paper:

Elaborate upon intricacies of the model itself: http://www.ncbi.nlm.nih.gov/pubmed/21270390

## **28.7 Conclusion**

Incorporating species tree information into the gene tree building process via introducing separate gene and species substitution rates allows for accurate parsimonious gene tree reconstructions. Previous gene tree reconstructions probably vastly overestimated the number of duplication and loss events. Reconstructing gene trees for large families remains a challenging problem.

439

6.047/6.878 Lecture 21: Phylogenomics II

## **28.8 Current Research Directions**

## **28.9 Further Reading**

- Paper on discovering Whole Genome Duplication event in yeast: http://www.nature.com/nature/journal/v428/n6983/pdf/nature02424.pdf

## **28.10 Tools and Techniques**

## **28.11 What Have We Learned?**

In this chapter, we drew conclusions regarding the relationship between gene trees and species trees. We then explored methods using gene trees to develop more accurate species trees and vice versa, involving the mutation rates of specific to both genes and species. The Wright-Fisher Model, as well as the Coalescent Model, helped us further interpret these mutation rates and understand the dynamics of allele frequencies within a population.

## **Bibliography**

- [1] O. Akerborg, B. Sennblad, L. Arvestad, and J. Lagergren. Bayesian gene tree reconstruction and reconciliation analysis. _Proc Natl Acad Sci_ , 106(14):5714–5719, Apr 2009.

- [2] Zmasek C.M. and Eddy S.R. Analyzing proteomes by automated phylogenomics using resampled inference of orthologs. _BMC Bioinformatics_ , 3(14), 2002.

- [3] Li H, Coghlan A, Ruan J, Coin LJ, Heriche JK, Osmotherly L, Li R, Liu T, Zhang Z, Bolund L, Wong GK, Zheng W, DEhal P, Wang J, and Durbin R. Treefam: a curated database of phylogenetic trees of animal gene families. _Nucleic Acids Res_ , 34, 2006.

- [4] Arvestad L., Berglund A., Lagergren J., and Sennblad B. Bayesian gene/species tree reconciliation and orthology analysis using mcmc. _Bioinformatics_ , 19 Suppl 1, 2003.

- [5] M. D. Rasmussen and M. Kellis. A bayesian approach for fast and accurate gene tree reconstruction. _Mol Biol Evol_ , 28(1):273290, Jan 2011.

- [6] Matthew D. Rasmussen and Manolis Kellis. Accurate gene-tree reconstruction by learning gene and species-specific substitution rates across multiple complete genomes. _Genome Res_ , 17(12):1932–1942, Dec 2007.

- [7] C.E.V. Storm and E.L.L. Sonnhammer. Automated ortholog inference from phylogenetic trees and calculation of orthology reliability. _Bioinformatics_ , 18(1):92–99, Jan 2002.

- [8] Hollich V., Milchert L., Arvestad L., and Sonnhammer E. Assessment of protein distance measures and tree-building methods for phylogenetic tree reconstruction. _Mol Biol Evol_ , 22:2257–2264, 2005.

- [9] Wapinski, I. A. Pfeffer, N. Friedman, and A. Regev. Automatic genome-wide reconstruction of phylogenetic gene trees. _Bioinformatics_ , 23(13):i549–i558, 2007.

440

CHAPTER

## **TWENTYNINE**

## POPULATION HISTORY

Guest Lecture by David Reich Scribed by Deena Wang (2013) Brian Cass (2010) Layla Barkal and Matt Edwards (2009)

### **Figures**

|29.1 Similarity between two subpopulations can be measured by comparing allele frequencies||
|---|---|
|in a scatterplot.<br>The plots show the relative dissimilarity of European American and<br>American Indian populations along with greater similarity of European American and<br>Chinese populations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|441|
|29.2 Populations can be projected onto the principal components of other populations: South<br>Asians projected onto Chinese and European principal components produces a linear effect<br>(the India Cline), while Europeans projected onto South Asian and Chinese principal<br>components does not.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|443|
|29.3 An admixture graph that fits Indian history . . . . . . . . . . . . . . . . . . . . . . . . . .|444|
|29.4 Projection onto two dimensions of a principle component analysis of different human pop-<br>ulations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|446|
|29.5 Data and models for ancestral gene flow. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|447|
|29.6 Ancient Europeans projected onto the two dimensional PCP of all modern European pop-<br>ulations. The modern Western Europeans, represented primarily by the bottom left cline,<br>cannot be described as a mixture of only EEF and WHG populations. However, with the<br>addition of an ANE component, the variations can be explained.<br>. . . . . . . . . . . . . .|448|
|29.7 European genetic composition over time shows two massive migrations: first, the migration<br>of the EEF population, almost completely replacing the native WHG population; and<br>second, the migration of the ANE Yamnaya population, replacing about 75% of the native<br>population at that point.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|450|
|29.8 Height selection in European populations from 8000 years ago to the present. . . . . . . .|450|


441

6.047/6.878 Lecture 22: Population History

## **29.1 Introduction**

Humans share 99.9% of the same genetic information, and are 99% similar to chimpanzees. Although humans have less genetic diversity than many other species [ **?** ], polymorphisms in populations can nonetheless lead to differences in disease risk. Learning about the 0.1% difference between humans can be used to understand population history, trace lineages, predict disease, and analyze natural selection trends.

In this lecture, Dr. David Reich of Harvard Medical School describes three historic examples of gene flow between human populations: gene flow between Africans and Europeans due to the slave trade, Indian intermixing due to migration, and interbreeding between Neanderthals, Denisovans and modern humans of Western Eurasian decent.

## **29.2 Quick Survey of Human Genetic Variation**

In the human genome, there is generally a polymorphism every 1000 bases, though there are regions of the genome where this rate can quadruple. These Single Nucleotide Polymorphisms (SNPs) are one manifestation of genetic variation. When SNPs occur, they segregate according to recombination rates, advantages or disadvantages of the mutation, and the population structure that exists and continues during the lifespan of the SNP. Following a genetic mixing event, for example, one initially sees entire chromosomes, or close to entire chromosomes, coming from each constituent. As generations pass, recombination splits the SNP haplotype blocks into smaller pices. The rate of change of the length of these blocks, then, is dependent on the rate of recombination and the stability of the recombination product. Therefore, the length of conserved haplotypes can be used to infer the age of a mutation or its selection. An important consideration, however, is that the rate of recombination is not uniform across the genome; rather, there are recombination hot spots that can skew the measure of haplotype age or selectivity. This makes the haplotype blocks longer than expected under a uniform model.

Every place in the genome can be thought of as a tree when compared across individuals. Depending on where are you look within the genome, one tree will be different than another tree you may get from a specific set of SNPs. The trick is to use the data that we have available on SNPs to infer the underlying trees, and then the overarching phylogenetic relationships. For example, the Y chromosome undergoes little to no recombination and thus can produce a highly accurate tree as it passed down from father to son. Likewise, we can look at mitochondrial DNA passed down from mother to child. While these trees can have high accuracy, other autosomal trees are confounded with recombination, and thus show lower accuracy to predict phylogenetic relationships. Gene trees are best made by looking at areas of low recombination, as recombination mixes trees. In general, there are about 1 to 2 recombinations per generation.

Humans show about 10,000 base-pairs of linkage, as we go back about 10,000 generations. Fruit fly linkage equilibrium blocks, on the other hand, are only a few hundred bases. Fixation of an allele will occur over time, proportional to the size of the population. For a population of about 10,000, it will take about 10,000 years to reach that point. When a population grows, the effect of gene drift is reduced. Curiously enough, the variation in humans looks like what would have been formed in a population size of 10,000.

If long haplotypes are mapped to genetic trees, approximately half of the depth is on the first branch; most morphology changes are deep in the tree because there was more time to mutate. One simple model of mutation without natural selection is the Wright-Fisher neutral model which utilizes binomial sampling. In this model, a SNP will either reach fixation (frequency 1) or die out (frequency 0).

In the human genome, there are 10-20 million common SNPs. This is less diversity than chimpanzees,

442

6.047/6.878 Lecture 22: Population History

implying that humans are genetically closer to one another.

With this genetic similarity in mind, comparing human sub-populations can give information about common ancestors and suggest historical events. The similarity between two sub-populations can be measured by comparing allele frequencies in a scatter plot. If we plot the frequencies of SNPs across different populations on a scatterplot, we see more spread between more distant populations. The plot below, for example, shows the relative dissimilarity of European American and American Indian populations along with the greater similarity of European American and Chinese populations. The plots indicate that there was a divergence in the past between Chinese and Native Americans, evidence for the North American migration bottleneck that has been hypothesized by archaeologists. The spread among different populations within Africa is quite large. We can measure spread by the fixation index ( _Fst_ ) which describes the variance.


Figure 29.1: Similarity between two subpopulations can be measured by comparing allele frequencies in a scatterplot. The plots show the relative dissimilarity of European American and American Indian populations along with greater similarity of European American and Chinese populations. © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Several current studies have shown that unsupervised clustering of genetic data can recover self-selected labels of ethnic identity.[3] Rosenberg's experiment used a Bayesian clustering algorithm. They took a sample size of 1000 people (50 populations, 20 people per population), and clustered those people by their SNP genetic data, but they did not tag any of the people with their population, so they could see how the algorithm would cluster without knowledge of ethnicity. They tried many different numbers of clusters to find the optimal number. With 2 clusters, East-Asians and non-East-Asians were separated. With 3 clusters, Africans were separated from everyone else. With 4, East-Asians and Native Americans were separated. With 5, the smaller sub-populations began to emerge.

When waves of humans left Africa, genetic diversity decreased; the small numbers of people in the groups that left Africa allowed for serial founder events to occur. These serial founder events lead to the formation of sub-populations with less genetic diversity. This founder effect is demonstrated by the fact that genetic diversity decreases moving out of Africa and that West Africans have the highest diversity of any human sub-population.

## **29.3 African and European Gene Flow**

The Atlantic Slave Trade took place from the 16th century to the 19th century, and moved about 5 million people from Africa to the Americas. Most African-Americans today have a mixture of 80% African and 20% European heritage. When two parents of different ethnicities have children, their children will inherit one chromosome from each parent, and their grandchildren will inherit chromosomes that are a mosaic of the two ethnicities due to recombination. As time passes, the increasing number of recombination events will decrease the length of the “African” or “European” stretches of DNA.

443

6.047/6.878 Lecture 22: Population History

Recombination events are not spread evenly throughout the chromosomes, but happen at hotspots. African and European DNA have different hot spots, which could be due to differences in the amino acid composition of _PRDM9_ , a histone H3(K4) trimethyltransferase which is essential for meiosis.

Difference in disease succeptibility can be predicted for African and European populations. With sequencing, this knowledge can also be applied to mixed populations. For example, Africans have a higher risk of prostrate cancer which is directly linked to an area in chromosome 8 that maps to a cancer protooncogene[ **?** ]. If a mixed individual has the African sequence in that area, he or she will have the increased risk, but if the individual has the European sequence, he or she will not have an increased risk. The same approach can be applied to breast cancer, colon cancer, multiple sclerosis, and other diseases.

## **29.4 Gene Flow on the Indian Subcontinent**

Genetic evidence suggests that modern populations on the Indian subcontinent descended from two different ancestral populations that mingled 4,000 years ago. SNP array data was collected from about 500 different people from 73 Indian groups with different language families [ **?** ]. A principle component analysis plot reveals that the the Dravidian/Indo-European language groups and the Austro-Asiatic language groups are in two different clusters, which suggests they have different lineages. Within the Dravidian/Indo-European language groups, there is a gradient of relatedness to West Eurasian groups.

The same mosaic technique used in the African/European intermixing study was used to estimate the date of mixture. The Indian population is a mixture of a Central Asian/European group and another group most closely related to the people of the Andaman Islands. The chunk size of the DNA belonging to each group suggests a mixture about 100 generations old, or 2,000 to 4,000 years ago. Many groups have this mixed heritage, but mixture stops after the creation of the caste system.

Knowledge of the heritage of genes can predict diseases. For example, a South Asian mutation in myosin binding protein C causes a seven-fold increase in heart failure Many ethnic groups are endogamous and have a low genetic diversity, resulting in a higher prevelance of recessive diseases.

Past surveys in India have studied such aspects as anthropometric variation, mtDNA, and the Y chromosome. The anthropometric study looked at significant differences in physical characteristics between groups separated by geography and ethnicity. The results showed variation much higher than that of Europe. The mtDNA study was a survey of maternal lineage and the results suggested that there was a single Indian tree such that age of lineage could be inferred by the number of mutations. The data also showed that Indian populations were separated from non-Indian populations at least 40,000 years ago. Finally, the Y chromosome study looked at paternal lineage and showed a more recent similarity to Middle Eastern men and dependencies on geography and caste. This data conflicts with the mtDNA results. One possible explanation is that there was a more recent male migration. Either way, the genetic studies done in India have served to show its genetic complexity. The high genetic variation, dissimilarity with other samples, and difficulty of obtaining more samples lead to India being left out of HapMap, the 1000 Genomes Project, and the HGDP.

In David Reich and collaborators study of India, 25 Indian groups were chosen to represent various geographies, language roots, and ethnicities. The raw data included five samples for each of the twenty five groups. Even though this number seems small, the number of SNPs from each sample has a lot of information. Approximately five hundred thousand markers were genotyped per individual. Looking at the data to emerge from the study, if Principal Components Analysis is used on data from West Eurasians and Asians, and if the Indian populations are compared using the same components, the India Cline emerges. This shows a gradient of similarity that might indicate a staggered divergence of Indian populations and

444

6.047/6.878 Lecture 22: Population History

European populations.

### **29.4.1 Almost All Mainland Indian Groups are Mixed**

Further analysis of the India Cline phenomenon produces interesting results. For instance, some Pakistani sub-populations have ancestry that also falls along the Indian Cline. Populations can be projected onto the principal components of other populations: South Asians projected onto Chinese and European principal components produces a linear effect (the India Cline), while Europeans projected onto South Asian and Chinese principal components does not. One interpretation is that Indian ancestry shows more variability than the other groups. A similar variability assessment appears when comparing African to non-African populations. Two tree hypotheses emerge from this analysis:

1. there were serial founder events in Indias history or

2. there was gene flow between ancestral populations.

The authors developed a formal four population test to test ancestry hypotheses in the presence of admixture or other confounding effects. The test takes a proposed tree topology and sums over all SNPs of (Pp1 Pp2)(Pp3 Pp4), where P values are frequencies for the four populations. If the proposed tree is correct, the correlation will be 0 and the populations in question form a clade. This method is resistant to several problems that limit other models. A complete model can be built to fit history. The topology information from the admixture graphs can be augmented with _Fst_ values through a fitting procedure. This method makes no assumptions about population split times, expansion and contractions, and duration of gene flow, resulting in a more robust estimation procedure.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 29.2: Populations can be projected onto the principal components of other populations: South Asians projected onto Chinese and European principal components produces a linear effect (the India Cline), while Europeans projected onto South Asian and Chinese principal components does not.

Furthermore, estimating the mixture proportions using the 4 population statistic gives error estimates for each of the groups on the tree. Complicated history does not factor into this calculation, as long as the topology as determined by the 4-population test is valid.

These tests and the cline analysis allowed the authors to determine the relative strength of Ancestral North Indian and Ancestral South Indian ancestry in each representative population sample. They found

445

6.047/6.878 Lecture 22: Population History


Figure 29.3: An admixture graph that fits Indian history

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

that high Ancestral North Indian ancestry is correlated with traditionally higher caste and certain language groupings. Furthermore, Ancestral North Indian (ANI) and South Indian (ASI) ancestry is as different from Chinese as European.

### **29.4.2 Population structure in India is different from Europe**

Population structure in India is much less correlated with geography than in Europe. Even correcting populations for language, geographic, and social status differences, the _Fst_ value is 0.007, about 7 times that of the most divergent populations in Europe. An open question is whether this could be due to missing (largely India-specific) SNPs on the genotyping arrays. This is because the set of targeted SNPs were identified primarily from the HapMap project, which did not include Indian sources.

Most Indian genetic variation does not arise from events outside India. Additionally, consanguineous marriages cannot explain the signal. Many serial founder events, perhaps tied to the castes or precursor groups, could contribute. Analyzing a single group at a time, it becomes apparent that castes and subcastes have a lot of endogamy. The autocorrelation of allele sharing between pairs of samples within a group is used to determine whether a founder event occurred and its relative age. There are segments of DNA from a founder, many indicating events more than 1000 years old. In most groups there is evidence for a strong, ancient founder event and subsequent endogamy. This stands in contrast to the population structure in most of Europe or Africa, where more population mixing occurs (less endogamy).

These serial founder events and their resulting structure have important medical implications. The strong founder events followed by endogamy and some mixing have lead to groups that have strong propensities for various recessive diseases. This structure means that Indian groups have a collection of prevalent diseases, similar to those already known in other groups, such as Ashkenazi Jews or Finns. Unique variation within India means that linkages to disease alleles prevalent in India might not be discoverable using only non-Indian data sources. A small number of samples are needed from each group, and more groups, to better map these recessive diseases. These maps can then be used to better predict disease patterns in India.

446

6.047/6.878 Lecture 22: Population History

### **29.4.3 Discussion**

Overall, strong founder events followed by endogamy have given India more substructure than Europe. All surveyed tribal and caste groups show a strong mixing of ANI and ASI ancestry, varying between 35% and 75% ANI identity. Estimating the time and mechanism of the ANI-ASI mixture is currently a high priority. Additionally, future studies will determine whether and how new techniques like the 4-population test and admixture graphs can be applied to other populations.

## **29.5 Gene Flow Between Archaic Human Populations**

Dr. Reich worked with the Max Planck Institute as a population geneticist studying Neanderthal genetic data. This section will discuss the background of his research as part of the Neanderthal genome project, the draft sequence that they assembled, and the evidence that has been compiled for gene flow between modern humans and Neanderthals.

### **29.5.1 Background**

Neanderthals are the only other hominid with a brain as large as _Homo sapiens_ . Neanderthal fossils from 200,000 years ago have been found in West Eurasia (Europe and Western Asia), which is far earlier than _Homo erectus_ . The earliest human fossils come from Ethiopia dating about 200,000 years ago. However, there is evidence that Neanderthals and humans overlapped in time and space between 135,000 and 35,000 years ago.

The first place of contact could have occurred in The Levant, in Israel. There are human fossils from 120,000 years ago, then a gap, Neanderthal fossils about 80,000 years ago, another gap, and then human fossils again 60,000 years ago. This is proof of an overlap in place, but not in time. In the upper paleolithic era, there was an explosion of populations leaving Africa (the migration about 60,000 to 45,000 years ago). In Europe after 45,000 years ago, there are sites where Neanderthals and humans exist side by side in the fossil record. Since there is evidence that the two species co-existed, was there interbreeding? This is a question that can be answered by examining population genomics.

See Tools and Techniques for a discussion of DNA extraction from Neanderthals.

### **29.5.2 Evidence of Gene Flow between Humans and Neanderthals**

1. A comparison test between Neanderthal DNA and human DNA from African and non-African populations demonstrates that non-African populations are more related to Neanderthals than African populations. We can look at all the SNPs in the genome and see whether the human SNP from one population matches the Neanderthal SNP. When different human populations were compared to Neanderthals, it was found that French, Chinese, and New Guinea SNPs matched Neanderthal SNPs much more than Nigerian Yoruba SNPs matched Neanderthal SNPs. San Bushmen and Yoruba populations from Africa, despite being very distinct genetically, both had the same distance from Neanderthal DNA. This evidence suggests that human populations migrating from Africa interbred with Neanderthals.

2. A long-range haplotype study demonstrates that when the deepest branch of a haplotype tree was in non-African populations, the regions frequently matched Neanderthal DNA. African populations

447

6.047/6.878 Lecture 22: Population History

today are the most diverse populations in the world. When humans migrated out of Africa, diversity decreased due to the founder effect. From this history, one would expect that if you built a tree of relations, the deepest split would be African.

To show Neanderthal heritage, Berkley researchers picked long range sections of the genome and compared them among randomly chosen humans from various populations. The deepest branch of the tree constructed from that haplotype is almost always from the African population. However, occasionally non-Africans have the deepest branch. The study found that there were 12 regions where non-Africans have the deepest branch. When this data was used to analyze the Neanderthal genome, it was found that 10 out of 12 of these regions in non-Africans matched Neanderthals more than the matched the human reference sequence (a compilation of sequences from various populations). This is evidence of that haplotype actually being of Neanderthal origin.

3. Lastly, there is a bigger divergence than expected among humans. The average split between a Neanderthal and a human is about 800,000 years. The typical divergence between two humans is about 500,000 years. When looking at African and non-African sequences, regions of low divergence emerged in non-African sequences when compared with Neanderthal material. The regions found were highly enriched for Neanderthal material (94% Neanderthal), which would increase the average divergence between humans (as the standard Neanderthal - human divergence is about 800,000 years).

### **29.5.3 Gene Flow between Humans and Denisovans**

In 2010, scientists discovered a 50,000 year old finger bone in southern Siberia. The DNA in this Denisovan sample was not like any previous human DNA. Denisovan mitochondrial DNA is an out-group to both Neanderthals and modern humans. (Mitochondrial DNA was used because it is about 1000 times more frequent than somatic DNA. The polymorphism rate is also 10 times higher.) Denisovans are more closely related to Neanderthals than humans.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 29.4: Projection onto two dimensions of a principle component analysis of different human populations.

Using the same SNP matching technique from the Neanderthal example, it was discovered that Denisovan DNA matches New Guinean DNA more than Chinese DNA or European DNA. It is estimated that Denisovans contributed about 5% of the ancestry of New Guineans today. A princple component analysis projection (see figure) between relatedness to chimpanzees, Neanderthals, and Denisovans shows that nonAfrican populations are more related to Neanderthals, and New Guinean/Bougainvillians are more related to Denisovans.

This evidence suggests a model for human migration and interbreeding. Humans migrated out of Africa

448

6.047/6.878 Lecture 22: Population History

and interbred with Neanderthals, then spread across Asia and interbred with Denisovans in Southeast Asia. It is less plausible that humans interbred with Denisovans in India because not all of the populations in Southeast Asia have Denisovan ancestry.

### **29.5.4 Analysis of High Coverage Archaic Genomes**

High-coverage archaic genomes can tell us a lot about the history of hominid populations. A high coverage Altai Neanderthal sequence was acquired from a toe bone found in Denisova cave. From this sequence, we can look at the time to convergence of the two copies of chromosomes to estimate the size of the population. Neanderthal DNA contains many long stretches of homozygosity, indicating a persistant small population size and inbreeding. For the Altai Neanderthal, one eighth of the genome was homozygous, about the expected level of inbreeding of half-siblings. Applying the technique to non-African populations shows a bottleneck 50,000 years ago and a subsequent population expansion, which is consistent with the Out Of Africa theory.

Neanderthals and Denisovans also interbred, demonstrating the remarkable proclivity of humanoids towards reproduction. Although most of the Neanderthal genome has a minimum depth of hundreds of thousands of years from the Denisovan genome, at least 0.5% of the Denisovan genome has a much shorter distance from Neanderthal genome, especially for immune genes.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 29.5: Data and models for ancestral gene flow.

Denisovans most likely have ancestry from an unknown archaic population unrelated to Neanderthals. An African sequence has a 23% match with Neanderthal DNA and 47% match with Denisovan DNA, which is statistically significant. If you stratify the D-statistic by the frequency of an allele in the population, you see an increasing slope and a sharp jump when you reach fixation which most closely matches the predictions one would obtain from an unknown population flowing into Denisovans (see figure).

### **29.5.5 Discussion**

The bottleneck caused by the migration from Africa is only one example of many. Most scientists usually concentrate on the age and intensity of migration events and not necessarily the duration, but the duration is very important because long bottlenecks create a smaller range of diversity. One way to predict the length of a bottleneck is to determine if any new variations arose during it, which is more likely during longer bottlenecks. The change in the range of diversity is also what helped create the different human

449

6.047/6.878 Lecture 22: Population History

sub-populations that became geographically isolated. This is just another way that population genomics can be useful for helping to piece together historical migrations.

Genetic differences between species (here within primates) can be used to help understand the phylogenetic tree from which we are all derived. We looked at the case study of comparisons with Neanderthal DNA, learned about how ancient DNA samples are obtained, how sequences are found and interpreted, and how that evidence shows high likelihood of interbreeding between modern humans (of Eurasian descent) and Neanderthals. Those very small differences between one species and the next, and within species, allow us to deduce a great deal of human history through population genetics.

## **29.6 European Ancestry and Migrations**

### **29.6.1 Tracing the Origins of European Genetics**

Before 2014, it was believed that modern European genetics was primarily a mixture of two ancestral populations. The first population is what is known as the Western hunter-gathere (WHG) population, and is considered the indigenous European population. The second population is known as the Early European farmer (EEF) population, and represents the rapid migration of farming peoples into Europe, and the subsequent mixing of the new farming population with the original WHG population. However, in 2012, Patterson et al [ **?** ] used the principal component analysis in Figure 29.6 to show that European genetics does not match up with being a mixture of only these two populations. Rather, genetic mixture analysis showed that some Europeans could only be explained as a mix of EEF/WHG populations with a third population whose genetics resembled Native Americans. While this does not mean that Native Americans are ancestral to Europeans, the study concluded that the most likely hypothesis was the mixture of these two known populations with an Ancient North Eurasian (ANE) population which migrated to both Asia and Europe, and is no longer found in North Eurasia. This study called this mystery population the ”Ghost of North Eurasia.”

Two years later, in 2014, however, a sample was found confirming the existence of this population. Proclaiming that ”The ghost is Found”, Raghavan, Skoglund et al. [ **?** ] studied the newly found ”Mal’ta” sample from Lake Baikal (currently in Southern Russia) and determined that it matched the predicted ghost population from 2012, and could explain the two dimensional variation in modern European populations. In particular, modern Europeans were found to be composed of 0-50% WHG, 32-93% EEF, and 1-18% ANE populations.

### **29.6.2 Migration from the Steppe**

Given this new population as a source of European ancestry, the natural questions are when and why did the members of the ANE population migrate to Europe? The answer, of course, can be teased out of further genetic data about the history of European populations. The first clue was found in mitochondrial DNA data, in a 2013 paper by Brandt, Haak et al. [ **?** ], which found that there were two discontinuities in European mitochondrial DNA: one between the Mesolithic and the early Neolithic ages, and one between the mid Neolithic age and the Late Neolithic and Bronze ages. In 2014, studies of 9, and then 94 samples of ancient European individuals showed clearly the two migration events, visualized in Figure 29.7. The first migration, at roughly 6500 BCE, was a migration of the EEF population, which replaced the existing WHG population at a rate of between 60 and 100%. The second migration was a migration of steppe pastoralists, known as the Yamnaya, which replaced the existing population with a rate between 60 and 80%. In both

450

6.047/6.878 Lecture 22: Population History


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Lazaridis, Iosif, et al. "Ancient Human Genomes Suggest Three Ancestral Populations for Present-day Europeans." _Nature_ 513, no. 7518 (2014): 409-13.

Figure 29.6: Ancient Europeans projected onto the two dimensional PCP of all modern European populations. The modern Western Europeans, represented primarily by the bottom left cline, cannot be described as a mixture of only EEF and WHG populations. However, with the addition of an ANE component, the variations can be explained.

cases, the migrating population takes over a chunk of the genetic composition almost immediately, and then the previous population gradually resurges over several thousand years.

### **29.6.3 Screening for Natural Selection**

Another application of DNA data to history is in tracing natural selection events. Essentially, one can look at the frequencies of various alleles in modern European DNA data, and find cases where it does not match the ancestral mixing model of the population. Such cases will tend to signify alleles that have been selected for or against since the ancestral mixing events occurred. The easiest to identify, and most well known example of such a trait is lactase persistence. The current level of prevalence of this trait is well above any of the levels represented by ancestral populations, suggesting that it underwent positive selection (due to the domestication and milking of animals) since the ancestral mixing events.

Several other traits can also be detected as candidates for selection. Another straightforward example is skin pigmentation. More interesting is the tale of height selection shown by the genetics of Northern and Southern Europeans. In particular, the data shows that two distinct selection effects occurred. First, the early farmers of Southern Europe underwent selection for decreasing height between 8000 and 4000 years ago. Second, the peoples of Northern Europe (modern Scandinavians, etc.) underwent positive selection around the same time period and through the present. While the anthropological explanations of these effects are disputed, the effects themselves are shown clearly in the genetic data.

451

6.047/6.878 Lecture 22: Population History


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Haak, Wolfgang, et al. "Massive Migration from the Steppe was a Source for Indo-European Languages in Europe." _Nature_ (2015).

Figure 29.7: European genetic composition over time shows two massive migrations: first, the migration of the EEF population, almost completely replacing the native WHG population; and second, the migration of the ANE Yamnaya population, replacing about 75% of the native population at that point.


Figure 29.8: Height selection in European populations from 8000 years ago to the present.

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Mathieson, Iain et al. "Genome-wide Patterns of Selection in 230 Ancient Eurasians." _Nature_ 528, no. 7583 (2015): 499-503.

452

6.047/6.878 Lecture 22: Population History

## **29.7 Tools and Techniques**

### **29.7.1 Techniques for Studying Population Relationships**

There are several different methods for studying population relationships with genetic data. The first general type of study utilizes both phylogeny and migration data. It fits the phylogenies to _Fst_ values, values of sub-population heterozygosity (pioneered by Cavalli-Sforza and Edwards in 1967 [ **?** ]). This method also makes use of synthetic maps and Principal Components Analysis. [2] The primary downside to analyzing population data this way is uncertainty about results. There are mathematical and edge effects in the data processing that cannot be predicted. Also, certain groups have shown that separate, bounded mixing populations can produce significant-seeming principal components by chance. Even if the results of the study are correct, then, they are also uncertain.

The second method of analyzing sub-population relationships is genetic clustering. Clusters can be formed using self-defined ancestry [1] or the STRUCTURE database. [3] This method is overused and can over-fit the data; the composition of the database can bias the clustering results.

Technological advances and increased data collection, though, have produced data sets that are 10,000 times larger than before, meaning that most specific claims can be disproved by some subset of data. So in effect, many models that are predicted either by phylogeny and migration or genetic clustering will be disproved at some point, leading to large-scale confusion of results. One solution to this problem is to use a simple model that makes a statement that is both useful and has less probability of being falsified.

### **29.7.2 Extracting DNA from Neanderthal Bones**

Lets take a look at how you go about finding and sequencing DNA from ancient remains. First, you have to obtain a bone sample with DNA from a Neanderthal. Human DNA and Neanderthal DNA is very similar (we are more similar to them than we are to chimps), so when sequencing short reads with very old DNA, it is impossible to tell if the DNA is Neanderthal or human. The cave where the bones were found is first classified as human or non-human using trash or tools as an identifier, which helps predict the origin of the bones. Even if you have a bone, it is still very unlikely that you have any salvageable DNA. In fact, 99% of the sequence of Neanderthals comes from only three long bones found in one site: the Vindija cave in Croatia (5.3 Gb, 1.3x full coverage).

Next, the DNA is sent to an ancient-DNA lab. Since they are 40,000 year old bones, there is very little DNA left in them. So, they are first screened for DNA. If they find DNA, the next question is whether it is primate DNA? Usually it is DNA from microbes and fungi that live in soil and digest dead organisms. Only about 1-10% of the DNA on old bones is the primates DNA. If it is primate DNA, is it contamination from the human (archeologist or lab tech) handling it? Only one out of 600 bp are different between humans and Neanderthals DNA. The size of reads from a 40,000 year old bone sample is 30-40 bp. The reads are almost always identical for a human and Neanderthal, so it is difficult to distinguish them.

In one instance, 89 DNA extracts were screened for Neanderthals DNA, but only 6 bones were actually sequenced (requires lack of contamination and high enough amount of DNA). The process of retrieving the DNA requires drilling beneath the bone surface (to minimize contamination) and taking samples from within. For the three long bones, less than 1 gram of bone powder was able to be obtained. Then the DNA is sequenced and aligned to a reference chimp genome. It is mapped to a chimp instead of a particular human because mapping to a human might cause bias if you are looking to see how the sequence relates to specific human sub-populations.

453

6.047/6.878 Lecture 22: Population History

Most successful finds have been in cool limestone caves, where it is dry and cold and perhaps a bit basic. The best chance of preservation occurs in permafrost areas. Very little DNA is recoverable from the tropics. The tropics have a great fossil record, but DNA is much harder to obtain. Since most bones dont yield enough or good DNA, scientists have the screen samples over and over again until they eventually find a good one.

### **29.7.3 Reassembling Ancient DNA**

DNA extracted from Neanderthal bones have short reads, about 37 bp on average. There are lots of holes due to mutations caused by time eroding the DNA. It is difficult to tell whether a sequence is the result of contamination because humans and Neanderthals only differ in one out of one thousand bases. However, we can use DNA damage characteristic of ancient DNA to distinguish old and new DNA. Old DNA has a tendency towards C to T and G to A errors. The C to T error is by far the most common, and is seen about 2% of the time. Over time, a methyl group gets knocked off of a C, which causes it to resemble to U. When PCR is used to amplify the DNA for sequencing, the polymerase sees a U and repairs it to a T. In order to combat this error, scientists use a special enzyme that recognizes the U, and cuts the strand instead of replacing it with a T. This helps to identify those sites. The G to A mutations are the result of seeing that on the opposite strand.

The average fragment size is quite small, and the error rate is still 0.1% - 0.3%. One way to combat the mutations is to note that on a double stranded fragment, the DNA is frayed towards the ends, where it becomes single stranded for about 10 bp. There tend to be high rates of mutations in the first and last 10 bases, but high quality DNA elsewhere, i.e. more C to T mutations in the beginning and G to A in the end. In chimps, the most common mutations are transitions (purine to purine, pyrimidine to pyrimidine), and transversions are much rarer. The same goes for humans. Since the G to A and C to T mutations are transitions, it can be determined that there are about 4x more mutations in the old Neanderthal DNA than if it were fresh by noting the number of transitions seen compared to the number of transversions seen (by comparing Neanderthal to human DNA). Transversions have a fairly stable rate of occurrence, so that ratio helps determine how much error has occurred through C to T mutations.

We are now able to get human contamination of artifact DNA down to around ¡1%. When the DNA is brought in, as soon as it is removed from the bone it is bar coded with a 7 bp tag. That tag allows you to avoid contamination at any later point in the experiment, but not earlier. Extraction is also done in a clean room with UV light, after having washed the bone. Mitochondrial DNA is helpful for distinguishing what percent of the sample is contaminated with human DNA. Mitochondrial DNA is filled with characteristic event sites because humans and Neanderthals are reciprocally monophylogenetic. The contamination can be measured by counting the ratio of those sites. In the Neanderthal DNA, contamination was present, but it was ¡ 0.5%.

In sequencing, the error rate is almost always higher than the polymorphism rate. Therefore, most sites in the sequence that are different from humans are caused by sequencing errors. So we cant exactly learn about Neanderthal biology through the sequence generated, but we can analyze particular SNPs as long as we know where to look. The probability of a particular SNP being changed due to an error in sequencing is only 3001 to 11000, so usable data can still be obtained.

After aligning the chimp, Neanderthal, and modern human sequences, we can measure the distance from Neanderthals to humans and chimps. This distance is only about 12.7% from the human reference sequence. A French sample measures about 8% distance from the reference sequence, and a Bushman about 10.3%. What this says is that the Neanderthal DNA is within our range of variation as a species.

454

6.047/6.878 Lecture 22: Population History

## **29.8 Research Directions**

Currently, the most exciting trend in the field is the existence of more and more data on both ancient and modern population genetics. With more samples, we can devise more fine statistical tests, and tease more and more information about population composition and history.

## **29.9 Further Reading**

## **Bibliography**

- [1] Bowcock AM, Ruiz-Linares A, Tomfohrde J, Minch E, Kidd JR, and Cavalli-Sforza LL. High resolution of human evolutionary history trees with polymorphic microsatellites. _Nature_ , 368:455–457, 1994.

- [2] Menozzi. Synthetic maps of human gene frequencies in europeans. _Science_ , 201(4358):768–792, Sep 1978.

- [3] Rosenberg N. Genetic structure of human populations. _Science_ , 298(5602):2381–2385, 2002.

455

6.047/6.878 Lecture 22: Population History

456

CHAPTER

**THIRTY**

## POPULATION GENETIC VARIATION

Guest Lecture by Pardis Sabeti Scribed by Mohammad Ghassemi, Jonas Helfer, Ben Mayne (2012), Alex McCAuley (2010), Matthew Lee (2009), Arjun K. Manrai and Clara Chan (2008)

### **Figures**

|30.1 Plot of genotype frequencies for different allele frequencies . . . . . . . . . . . . . . . . . .|458|
|---|---|
|30.2 Changes in allele frequency over time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|459|
|30.3 A comparison of the hetrozygous and homozygous derived and damaging genotypes per<br>individual in an African American (AA) and European American (EA) population study.|461|
|30.4 Two isolated populations<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|461|
|30.5 Approximate Time Table of Effects Sabeti et al. _Science_ 2006 . . . . . . . . . . . . . . . .|464|
|30.6 Localized positive selection for Malaria resistance within species Sabeti et al. _Science_ 2006|465|
|30.7 Localized positive selection for lactase persistence allele Sabeti et al. _Science_ 2006<br>. . . .|466|
|30.8 Mean allele frequency difference of height SNPs, matched SNPS, and genome-wide SNPS<br>between Northern- and Southern-European populations Turchin et al., Nature _Genetics_<br>(2012) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|466|
|30.9 Broken haplotype as a signal of natural selection . . . . . . . . . . . . . . . . . . . . . . .|467|
|30.10A depiction of two major bottleneck events, one in the founding population from Africa,<br>and other, smaller subsequent bottleneck events in the East Asian and Western European<br>populations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|469|
|30.11An illustration of two bottleneck events<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|470|
|30.12The figure illustrate the effects of a bottleneck events on the number of rare Alleles in a<br>population.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|471|
|30.13A depiction of European admixture levels in the Mexican, and African American populations|.471|
|30.14As illustration of the magnitude and origin of migrants based on the tract length and<br>number of tracts in the admixed population.. . . . . . . . . . . . . . . . . . . . . . . . . .|472|


457

6.047/6.878 Lecture 23: Population Genetic Variation

## **30.1 Introduction**

For centuries, biologists had to rely on morphological and phenotypical properties of organisms in order to infer the tree of life and make educated guesses about the evolutionary history of species. Only recently, the ability to cheaply sequence entire genomes and find patterns in them has transformed evolutionary biology. Sequencing and comparing genomes on a molecular level has become a fundamental tool that allows us to gain insight into much older evolutionary history than before, but also to understand evolution at a much smaller resolution of time. With these new tools, we can not only learn the relationship between distant clades that separated billions of years ago, but also understand the present and recent past of species and even different populations inside a species.

In this chapter we will discuss the study of Human genetic history and recent selection. The methodological framework of this section builds largely on the concepts from previous chapters. Most specifically, the methods for association mapping of disease and phylogenetic constructs such as tree building among species and genes, and the history of mutations using coalescence. Having learned about these methods in the last chapter, we now will study how their application can inform us about the relationships, and differences between human populations. Additionally, we will look for how these differences can be exploited to look for signals of recent natural selection and the identification of disease loci. We will also discuss in this chapter what we currently know about the differences between human populations and describe some parameters we can infer that quantify population differences, using only the extent genetic variation we observe. In the study of Human Genetic history and recent selection, there are two principal topics of investigation which are often studied. The first is the history of population sizes. The second is the history of interactions between populations. Questions are often asked about these areas because the answers can often provide knowledge to improve the disease mapping process. Thus far, all present research based knowledge of human history was found by investigating functionally neutral regions of the genome, and assuming genetic drift. The reason that neural regions are employed is because mutations are subject to positive, negative and balancing selection pressure, when they take place on a functional region. Hence investigating a neural regions provides a selection unbiased proxy for the drift between species. In this chapter we will delve into some of the characteristics of selection process in humans and look for patterns of human variation in terms of cross species comparisons, comparison synonymous and non-synonymous mutations, and haplotype structure.

## **30.2 Population Selection Basics**

### **30.2.1 Polymorphisms**

**Polymorphisms** are differences in appearance amongst members of the same species. Many of them arise from mutations in the genome. These mutations, or genetic polymorphisms, can be characterized into different types.

#### **Single Nucleotide Polymorphisms (SNPs)**

- The mutation of only a single nucleotide base within a sequence. In most cases, these changes are without consequence. However, there are some cases where the mutation of a single nucleotide has a major effect.

458

6.047/6.878 Lecture 23: Population Genetic Variation

- For example, is caused by a from A to T, that causes a change from glutamic acid (GAG) to valine (GTG) in hemoglobin.

#### **Variable Number Tandem Repeats**

- When a short sequence is repeated multiple times, DNA Polymerase can sometimes ”slip”, causing it to make either too many or too few copies of the repeat. This is called a .

- For example, **Huntingtons disease** that is caused by too many repeats of the trinucleotide CAG repeat in the HTT gene. Having more than 36 repeats can lead to gradual muscle control loss and severe neurological degradation. Generally, the more repeats there are, the stronger the symptoms.

#### **Insertion/Deletion**

- Through faulty copying or DNA-repair, or of one or multiple nucleotides can occur.

- If the insertion or deletion is inside an exon (the protein-coding region of a gene) and does not consist of a multiple of three nucleotides, a will occur.

- Prime example is deletions in the CFTR gene, which codes for chloride channels in the lungs and may cause **Cystic Fibrosis** where the patient cannot clear mucous in the lungs and causes infection

## **_Did You Know?_**

DNA profiling is based on short variable number tandem repeats (STR). DNA is cut with certain restriction enzymes, resulting in fragments of variable length that can be used to identify an individual. Different countries use different (but often overlapping) loci for these profiles. In North America, a system based on 13 loci is used.

### **30.2.2 Allele and Genotype Frequencies**

In order to understand the evolution of a species through analysis of alleles or genotypes, we must have a model of how the alleles are passed on from one generation to another. It is of immense importance that the reader has a firm intuition for the Hardy-Weinberg Principle and Wright fisher model before continuing. Hence, we will provide here a short reminder of modelling the history of mutations via the these methods. First introduced over a hundred years ago, the Wright-Fisher Model is a mathematical model of genetic drift in a population. Specifically, it describes the probability of obtaining k copies of a new allele p within a population of size N, with a non-mutant frequency of q, and what its expected frequency will be in successive generations.

#### **Hardy-Weinberg Principle**

The states that allele and genotype frequencies within a population will remain constant unless there is an outside influence that pushes them away from that equilibrium.

The Hardy-Weinberg principle is based on the following assumptions:

- The population observed is very large

459

6.047/6.878 Lecture 23: Population Genetic Variation

- The population is isolated, i.e. there is no introduction of another subpopulation into the general population

- All individuals have equal probability of producing offspring

- All mating in the population is at random

- No random mutations occur in the population from one generation to the next

- Allele frequency drives future genotype frequency (Prevalent allele drives Prevalent genotype)

In a Hardy-Weinberg Equilibrium, for two alleles A and a, occurring with probability _p_ and _q_ = 1 _p_ , respectively, the probabilities of a randomly chosen individual having the homozygous AA or aa (pp or qq, respectively) or heterozygous Aa or aA (2pq) genotypes can be described by the equation:


This equation gives a table of probabilities for each genotype, which can be compared with the observed genotype frequencies using statistical error tests such as the chi-squared test to determine if the HardyWeinberg model is applicable. Figure 30.1 shows the distribution of genotype frequencies at different allele frequencies.


Figure 30.1: Plot of genotype frequencies for different allele frequencies

In natural populations, the assumptions made by the Hardy-Weinberg principle will rarely hold. Natural selection occurs, small populations undergo genetic drift, populations are split or merged, etc. In Nature a mutation will always either disappear (frequency = 0) from the population or become prevalent in a species - this is called fixation; in general, 99% of mutations disappear. Figure 30.2 shows a simulation of a mutations prevalence in a finite-sized population over time: both perform random walks, with one mutation disappearing and the other becoming prevalent:

Once a mutation has disappeared, the only way for it to reappear is the introduction of a new mutation into the population. For humans, it is believed that a given mutation under no selective pressure should fixate to 0 or 1 (within, e.g., 5%) within a few million years. However, under selection this will happen much faster.

#### **Wright-Fisher Model**

Under this model the time to fixation is 4N and the probability of fixation is 1/2N. In general Wright-Fisher is used to answer questions related to fixation in one way or another. To make sure your intuitions about

460

6.047/6.878 Lecture 23: Population Genetic Variation


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 30.2: Changes in allele frequency over time

the method are absolutely clear considering the following questions:

## **_FAQ_**

- **Q:** Say you have a total of 5 mutations on a chromosome among a population of size 30, on average, how many mutations will be present in the next generation if each entity produces only one child?

- **A:** If each parent has only one offspring, then there will be, on average, 5 mutations in the next generation because the expectation of allele frequencies is to remain constant according to the Hardy-Weinberg equilibrium principle in basic biology.

## **_FAQ_**

- **Q:** Is the Hardy-Weinberg Equilibrium principle’s assumption about constant allele frequency reasonable?

- **A:** No, the reality is far more complex as there is stochasticity in population size and selection at each generation. A more appropriate way to envision this is to image drawing alleles from a set of parents, with the amount of alleles in the next generation varying with the size of the population. Hence the frequency in the next generation could very well go up or down. Note here that if the allele frequency goes to zero it will always be at zero. The probability at each successive generation is lower if it’s under negative selection and higher if it’s under positive selection. Hence if it’s a beneficial mutation the fixation time will be smaller, if the mutation is deleterious the fixation will be larger. If there are no offspring with a given mutation, then there won’t be any decedents with that mutation either. If one produces multiple offspring however, who in turn produce multiple offspring of their own, then there is a greater chance that this allele frequency will rise.

461

6.047/6.878 Lecture 23: Population Genetic Variation

## **_FAQ_**

- **Q:** Consider that the average human individual carries roughly 100 entirely unique mutations. So, when an individual produces offspring we could expect that half (or 50) of those mutations may appear in the child because in each sperm or egg cell, 50 of those mutations will be present, on average. Hence the offspring of an individual are likely to inherit approximately 100 mutations, 50 from one parent, and 50 from another in addition to their own unique mutations which come from neither parent. With this in mind, one might be interested in The understanding what the chances are of some mutations appearing in the next generation if an individual produces, say, n children. How can one do this?

- **A:** Hint: To compute this value, we assume that some allele originates in the founder, at some arbitrary chromosome (1 for example). Then we ask the question, how many chromosome 1s exist in the entire population? At the moment, the size of the human population is 7 Billion, each carrying two copies of chromosome 1.

above questions and answers should make it painfully clear that the standard Hardy-Weinberg assumption of allele frequencies remaining constant from one generation to the next is violated in many natural cases including migration, genetic mutation, and selection. In the case of selection, this issue is addressed by modifying the formal definition to include a S, term which measures the skew in genotypes due to selection. See table 30.1 for a comparison of the original and selection compensated versions:

|Behavior|With only drift|With drift and selection|
|---|---|---|
|n in next generation|Mean: _n_(= 2_Np_), Dist: _Binomial_(2_N, p_)|Mean: _n_(1 +<br>_s_<br>1+_ps_<sup>), Dist:</sup> <sup>_Binomial_(2</sup><sup>_N, p_</sup> <sup>1+</sup><sup>_s_</sup><br>1+_ps_<sup>)</sup><br><br>|
|Time to fixation|4_N_|4_N_<br>1+ <sup>3</sup><br>8 <sup>_N|s|_( 1+ 1</sup><br>2 <sup>(ln</sup><sup>_N_)</sup><sup>_|s|_</sup><br>1+_|s|_<br>)<br>|
|Probability of fixation|1<br>2_N_|1_−e_<sup>_−_2</sup><sup>_s_</sup><br>1_−e_<sup>_−_4</sup><sup>_Ns_</sup>|


Table 30.1: Comparison of Wright-Fisher Model With Drift, Versus Drift and Selection

The main point to take away from Table 30.1, and this section of the chapter is that weather you have selection or not, it is highly unlikely that a single allele will fixate in a population. If you have a very small population, however, then the chances of an allele fixating are much better. This is often the case in human populations, where there are often small, interbred populations which allow for mutations to fix in a population after only a few generations, even if the mutation is deleterious in nature. This is precisely why we tend to see recessive deleterious mandolin disorders in isolated populations.

### **30.2.3 Ancestral State of Polymorphisms**

How can we determine for a given polymorphism which version was the and which one is the mutant? The ancestral state can be inferred by comparing the genome to that of a closely related species (e.g. humans and chimpanzees) with a known phylogenetic tree. Mutations can occur anywhere along the phylogenetic tree sometimes mutations at the split fix differently in different populations (“fixed difference”), in which case the entire populations differ in genotype. However, recent mutations will not have had enough time to become fixed, and a polymorphism will be present in one species but fully absent in the other as simultaneous mutations in both species are very rare. In this case, the “derived variant” is the version of the polymorphism appearing after the split, while the ancestral variant is the version occuring in both species.

462

6.047/6.878 Lecture 23: Population Genetic Variation


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 30.3: A comparison of the hetrozygous and homozygous derived and damaging genotypes per individual in an African American (AA) and European American (EA) population study.

### **30.2.4 Measuring Derived Allele Frequencies**

The the frequency of the derived allele in the population can be easily calculated, if we assume that the population is homogeneous. However, this assumption may not hold when there is an unseen divide between two groups that causes them to evolve separately as shown in figure 30.4.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 30.4: Two isolated populations

In this case the prevalence of the variants among subpopulations is different and the Hardy-Weinberg principle is violated.

One way to quantify this difference is to use the ( _Fst_ ) to compare subpopulations within a species. In reality only a portion of the total heterozygosity in a species is found in a given subpopulation. Fst estimates the reduction in heterozygosity (2pq with alleles p and q) expected when 2 different populations are erroneously grouped together. Given a population having n alleles with frequencies _pi_ where (1 _≤ i ≤ n_ ),

463

6.047/6.878 Lecture 23: Population Genetic Variation

the homozygosity G of the population is calculated as:


The total heterozygosity in the population is given by 1-G.


In the case shown in figure 30.4 there is no heterozygosity between the populations, so _Fst_ = 1. In reality the Fst will be small within one species. In humans, for example, it is only 0.0625. For in practise, the Fst is computed either by clustering sub-populations randomly or using an obvious characteristic such as ethnicity or origin.

## **30.3 Genetic Linkage**

In the simple models we’ve seen so far, alleles are assumed to be passed on independently of each other. While this assumption generally holds in the long term, in the short term we will generally observe a that certain alleles are passed on together more frequently than expected. This is termed genetic linkage.

The , also known as Mendel’s second law states:

_Alleles of different genes are passed on independently from parent to offspring._

When this “law” holds, there is no correlation between different polymorphisms and the probability of a haplotype (a given set of polymorphisms) is simply the product of the probabilities of each individual polymorphism.

In the case where the two genes lie on different chromosomes this assumption of independence generally holds, but if the two genes lie on the same chromosome, they are more often than not passed on together. Without genetic recombination events, in which segments of DNA on homologous chromosomes are swapped (crossing-over), the alleles of the two genes would remain perfectly correlated. With however, the correlation between the genes will be reduced over several generations. Over a suitably long time interval, recombination will completely remove the linkage between two polymorphisms; at which point they are said to be in equilibrium. When, on the other hand, the polymorphisms are correlated, we have **Linkage Disequilibrium** (LD). The amount of disequilibrium is the difference between the observed haplotype frequencies and those predicted in equilibrium.

The linkage disequilibrium can be used to measure the difference between observed and expected assortments. If there are two alleles (1 and 2) and two loci (A and B) we can calculate haplotype probabilities and find the expected allele frequencies.

- Haplotype frequencies


464

6.047/6.878 Lecture 23: Population Genetic Variation

**–** _P_ ( _B_ 1) = _x_ 12 **–** _P_ ( _A_ 2) = _x_ 21

**–** _P_ ( _B_ 2) = _x_ 22

• Allele frequencies

**–** _P_ 11 = _x_ 11 + _x_ 12 **–** _P_ 21 = _x_ 21 + _x_ 22 **–** _P_ 12 = _x_ 11 + _x_ 21 **–** _P_ 22 = _x_ 12 + _x_ 22

- _D_ = _P_ 11 _∗ P_ 22 _P_ 12 _∗ P_ 21

_Dmax_ , the maximum value of D with given allele frequencies, is related to D in the following equation:

_D_<sup>_′_</sup> = _<u>D</u> Dmax_

_D_<sup>_′_</sup> is the maximum linkage disequilibrium or complete skew for the given alleles and allele frequencies. _Dmax_ can be found by taking the smaller of the expected haplotype frequencies _P_ ( _A_ 1 _, B_ 2) or _P_ ( _A_ 2 _, B_ 1). If the two loci are in complete equilibrium, then _D_<sup>_′_</sup> = 0. If _D_<sup>_′_</sup> = 1, there is full linkage.

The key point is that relatively recent mutations have not had time to be broken down by crossing-overs. Normally, such a mutation will not be very common. However, if it is under positive selection, the mutation will be much more prevalent in the population than expected. Therefore, by carefully combining a measure of LD and derived allele frequency, we can determine if a region is under positive selection.

Decay of is driven by recombination rate and time (in generations) and has an exponential decay. For a higher recombination rate, linkage disequilibrium will decay faster in a shorter amount of time. However, the background recombination rate is difficult to estimate and varies depending on the location in the genome. Comparison of genomic data across multiple species can help in determining these background rates.

### **30.3.1 Correlation Coefficient** _r_<sup>2</sup>

Answers how predictive an allele at locus A is of an allele at locus B


As the value of _r_<sup>2</sup> approaches 1, the more two alleles at two loci are correlated. There may be linkage disequilibrium between two haplotypes, even if the haplotypes are not correlated at all. The correlation coefficient is particularly interesting when studying associations of diseases with genes, where knowing the genotype at locus A may not predict a disease whereas locus B does. There is also the possibility where neither locus A nor locus B are predictive of the disease alone but loci A and B together are predictive.

## **30.4 Natural Selection**

In the mid 1800s the concept of evolution was not an uncommon idea, but it wasn’t before Darwin and Wallace proposed natural selection as the mechanism that drives evolution in nature that the theory of

465

6.047/6.878 Lecture 23: Population Genetic Variation

evolution got widespread recognition. It took 70 years (1948) until J.B.S Haldanes Malaria Hypothesis found the first example for natural selection in humans. He showed a correlation between genetic mutations in red blood cells and the distribution of malaria prevalence and discovered that individuals who had a specific mutation that made them suffer from sickle cell anaemia also gave made them resistant to malaria.

Lactose tolerance (lasting into adulthood) is another example of natural selection. Such explicit examples were hard to prove without genome sequences. With whole genome sequencing readily available, we can now search the genome for regions with the same patterns as these known examples to identify further regions undergoing natural selection.

### **30.4.1 Genomics Signals of Natural Selection**

- _Ka/Ks_ ratio of non-synonymous to synonymous changes per gene

- Low diversity and many rare alleles over a region (ex Tajima’s D with regard to sickel-cell anemia)

- High derived allele frequency (or low) over a region (ex Fay and Wu’s H)

- Differentiation between populations faster than expected from drift (Measured with _Fst_ )

- Long haplotypes: evidence of selective sweep.

- Exponential prevalence of a feature in sequential generations

- Mutations that help a species prosper


Figure 30.5: Approximate Time Table of Effects Sabeti et al. _Science_ 2006

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Sabeti, P. C., et al. "Positive Natural Selection in the Human Lineage." _Science_ 312, no. 5780 (2006): 1614-20.

#### **Examples of Negative (Purifying) Selection**

- **Across species** we see negative selection of new mutations in conserved functional elements (exons, etc.).

466

6.047/6.878 Lecture 23: Population Genetic Variation

- **New alleles** within one species tend to have lower allele frequencies if the allele is non-synonymous than synonymous. Lethal alleles have very low frequencies.

#### **Examples of Positive (Adaptive) Selection**

- **Similar to negative selection** in that positive selection more likely in functional elements or nonsynonymous alleles.

- **Across species** in a conserved element, a positively selected mutation might be the same over most mammals, but change in a specific species because a positvely selected mutation appeared after speciation or caused speciation.

- **Within a species** positvely selected alleles likely differ in allele frequency ( _Fst_ ) across populations. Examples include malaria resistance in African populations (30.6) and lactose persistence in European populations (30.7).

- **Polygenic selection** within species can arise when a trait is selected for that depends on many genes. An example is human height where 139 SNPs are known to be related to height. Most are not population specific mutations but alleles across all humans that are seleced for in some populations more than others. (30.8)


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Sabeti, P. C., et al. "Positive Natural Selection in the Human Lineage." _Science_ 312, no. 5780 (2006): 1614-20.

Figure 30.6: Localized positive selection for Malaria resistance within species Sabeti et al. _Science_ 2006

#### **Statistical Tests**

- **Long range correlations (iHs, Xp, EHH):** If we tag genetic sequences in an individual based on their ancestry, we end up with a broken haplotype, where the number of breaks (color changes) is correlated with the number of recombinations and can tell us how long ago a particular ancestry was introduced.

- **SWEEP** A program developed by Pardis Sabeti, Ben Fry and Patrick Varilly. SWEEP detects evidence of natural selection by analyzing haplotype structures in the genome using the long range

467

6.047/6.878 Lecture 23: Population Genetic Variation


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Sabeti, P. C., et al. "Positive Natural Selection in the Human Lineage." _Science_ 312, no. 5780 (2006): 1614-20.

Figure 30.7: Localized positive selection for lactase persistence allele Sabeti et al. _Science_ 2006


Courtesy of  Macmillan Publishers Limited. Used with permission. Source: Turchin, Michael C., et al. "Evidence of Widespread Selection on Standing Variation in Europe at Height-associated SNPs." _Nature Genetics_ 44, no. 9 (2012): 1015-9.

Figure 30.8: Mean allele frequency difference of height SNPs, matched SNPS, and genome-wide SNPS between Northern- and Southern-European populations Turchin et al., Nature _Genetics_ (2012)

haplotype test (LRH). It looks for high frequency alleles with long range linkage disequilibrium that hints to large scale proliferation of a haplotype that occurred at a rate greater than recombination could break it from its markers .

- **High Frequency Derived Alleles** Look for large spikes in the frequency of derived alleles in set positions.

- **High Differentiation (** _Fst_ **)** Large spikes in differentiation at certain positions.

Using these tests, we can find genomic regions under selective pressure. One problem is that a single SNP under positive selection will allow nearby SNPs to piggy-back and ride along. It is difficult to distinguish the SNP under selection from its neighbours with only one test. Under selection, all the tests are strongly

468

6.047/6.878 Lecture 23: Population Genetic Variation


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 30.9: Broken haplotype as a signal of natural selection

correlated; however, in the absence of selection they are generally independent. Therefore, by employing a composite statistic built from all of these tests, it is possible to isolate the individual SNP under selection.

Examples where a single SNP has been implicated in a trait:

- Chr15 Skin pigmentation in Northern Europe

- Chr2 Hair traits in Asia

- Chr10 Unknown trait in Asia

- Chr12 Unknown Trait in Africa

## **30.5 Human Evolution**

### **30.5.1 A History of the Study of Population Dynamics**

Not surprisingly, the scientific community has a long, and somewhat controversial history of interest in recent population dynamics. While indeed some of this interest was applied toward more nefarious aims, such as the scientific justifications for racism for eugenics but these are increasingly the exception and not the rule. Early studies of population dynamic were primitive in many ways. Quantifying the differences between human populations was originally performed using blood types, as they seemed to be phenotypically neutral, could be tested for outside of the body, and seemed to be polymorphic in many different human populations. Fast forward to the present, and the scientific community has realized that there are other glycoproteins beyond the A,B and O blood groups that are far more polymorphic in the population. As science continued to advance and sequencing became a reality, they began whole genome sequencing of the Y-chromosome, mitochondrial and microsatellite markers around them. What’s special about those two types of genetic data? First and foremost, they are quite short so they can be sequenced more easily than other chromosomes. Beyond just the size, the reason that the Y and mitochondrial chromosomes were of such interest is because they do not recombine, and can be used to easily reconstruct inheritance trees. This is precisely what makes these chromosomes special relative to a short chunk on an autosome; we know exactly where it comes from because we can trace paternal or maternal lineage backward in time.

469

6.047/6.878 Lecture 23: Population Genetic Variation

This type of reconstruction does not work with other chromosomes. If one were to generate a tree using a certain chunk of all of chromosome 1 in a certain population, for instance, they would indeed form a phylogeny but that phylogeny would be picked from random ancestors in each of the family trees.

As sequencing continued to develop and grow more effective, the human genome project was being proposed, and along with it there was a strong push to include some sort of diversity measure in genomic data. Technically speaking, it was easiest to simply look at microsatellites for this diversity measure because they can be studied on gel to see size polymorphisms instead of inspecting a sequence polymorphism. As a reminder, a microsatellite is a region of variable length in the human genome often characterised by short tandem repeats. One reason for microsatellites is retroviruses inserting themselves into the genome, such as the ALU elements in the human genome. These elements sometimes become active and will retro-transpose as insertion events and one can trace when those insertion events have happened in human lineage. Hence, there was a push, early on to assay these parts of the genome in a variety of different populations. The really attractive thing about microsatellites is that they are highly polymorphic and one can actually infer their rate of mutation. Hence, we can not only say that there is a certain relationship between populations based on these rates, but we can also say how long they have been evolving and even when certain mutations occurred, and how long it’s been on certain branches of the phylogenetic tree.

## **_FAQ_**

**Q:** Can’t this simply be done with SNPs

**A:** You can’t do it very easily with SNPs.

You can get an idea of how old they are based on their allele frequency, but they’re also going to be influenced by selection.

After the human genome project, came the Haplotype inheritance Hapmap project which looked at SNPs genome wide. We have discussed Haplotype inheritance in detail in prior chapters where we learned the importance of Hapmap in designing genotyping arrays which look at SNPs that mark common haplotypes in the population.

The effects of Bottlenecks on Human diversity Using this wealth of data across studies and a plethora of mathematical techniques has led to the realization that humans, in fact, have a very low diversity given our census population; which implies a small effective population size. Utilizing the Wright-Fisher model it is possible to work back from the level of diversity and the number of mutations we see in the population today to generate a founding population size. When this computation is performed it works out to being around 10,000.

## **_FAQ_**

**Q:** Why is this so much smaller than our census population size?

**A:** There was A population bottleneck somewhere.

470

6.047/6.878 Lecture 23: Population Genetic Variation


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 30.10: A depiction of two major bottleneck events, one in the founding population from Africa, and other, smaller subsequent bottleneck events in the East Asian and Western European populations.

Most of the total variation between humans is happening within-continent. One can measure how much diversity is explained by geography and how much is not. It turns out that most of it is not explained by geography. In fact, most common variants are polymorphic in every population and if a common variant is unique to a given population, there probably hasn’t been enough time for that to happen by drift itself. Recall what an unlikely process it is to get to a high allele frequency over the course of several generations by mere chance alone. Hence, we may interpret this as a signal of selection when it occurs. All of the evidence in terms of comparing diversity patterns and trees back to ancestral haplotypes converges to an Out-of-Africa hypothesis which is the overwhelming consensus in the field and is the lens through which we review all the genetic population data. Starting from the African founder population, there have been works which have demonstrated that it’s possible to model population growth using the wright fisher model. The studies have shown that the growth rate we see in Asian and European populations are only consistent with large exponential growth after the out-of-Africa event.


Table 30.2: Genetic Estimates of Recent Population Growth in Europe

This helps us understand the reasons for phonotypical differences between the races as Bottlenecks which

471

6.047/6.878 Lecture 23: Population Genetic Variation

are followed by exponential growth can lead to an excess of rare alleles. The present theory on human diversity states that there were secondary bottleneck events after the founding population migrated out of Africa. These founders were, at some earlier point subject to an even smaller bottleneck event which is now reflected in every human genome on the planet, regardless of their immediate ancestry. It is possible to estimate how small the original bottle neck was by looking at differences between African and European origin individuals, inferring the effects of the secondary bottleneck, and the term of exponential growth of the European population. The other way of approaching bottleneck event estimation is to simply inspect the allele frequency spectrum needed to build coalescent trees. In this way, one can take haplotypes across the genome and ask what the most recent common ancestor was by observing how the coalescence varies across the genome. For instance, one may guess that some haplotype was positively selected for only recently given the length of the haplotype. An example of one such recent mutation in the European population is the lactase gene. Another example for the Asian population is the ER locus.

There is a wealth of literature showing that when one draws a coalescence tree for most haplotypes it ends up going way back before when we think speciation happened. This indicates that certain features have been kept polymorphic for a very long time. One can, however, look at this distribution of features across the whole genome and infer something about population history from it. If there was a recent bottle neck in a population, it will be reflected by the ancestors being very recent whereas more ancient things will have survived the bottleneck. One can take the distribution of coalescent times and run simulations for how the effect of population size would have varied with time. The model for doing this type of study was outlined by Li and Durbin. The Figure 30.11 from their study illustrates two such bottleneck events. The first is the bottleneck which occurred in Africa long before migrations out of the continent. This was then followed by a population specific bottleneck that resulted from migration groups out of Africa. This is reflected in the diversity of the populations today based on their ancestry and it can be derived from looking at a pair of chromosome from any two people in these populations.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 30.11: An illustration of two bottleneck events

### **30.5.2 Understanding Disease**

Understanding that human populations went through bottlenecks has important implications for understanding population specific disease. A study published by Tennessen et al. this year was looking at exome sequences in many classes of individuals. The study intended to look at how rare variants might be contributing to disease and as a consequence they were able to fit population genetics models to the data, and ask what sort of deleterious variants were seen when sequencing exomes from a broad population panel. Using this approach, they were then able to generate parameters which describe how long ago exponential

472

6.047/6.878 Lecture 23: Population Genetic Variation

growth between the founder, and branching populations occured. See figure 30.12 below for an illustration of this:


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Tennessen, Jacob A., et al. "Evolution and Functional Impact of Rare Coding Variation from Deep Sequencing of Human Exomes." _Science_ 337, no. 6090 (2012): 64-69.

Figure 30.12: The figure illustrate the effects of a bottleneck events on the number of rare Alleles in a population.

### **30.5.3 Understanding Recent Population Admixture**

In addition to viewing coalescent times, one can also perform Principal Component Analysis on SNPs to gain an understanding of more recent population admixtures. Running this on most populations shows clustering with respect to geographical location. There are some populations, however, that experienced a recent admixture for historical reason. The two most commonly referred to in the scientific literature are: African Americans, who on average are 20

Courtesy of Elsevier, Inc., http://www.sciencedirect.com. Used with permission. Source: Kidd, Jeffrey M., et al. "Population Genetic Inference from Personal Genome Data: Impact of Ancestry and Admixtureon Human Genomic Variation." _The American Journal of Human Genetics_ 91, no. 4 (2012): 660-71.

Figure 30.13: A depiction of European admixture levels in the Mexican, and African American populations.

There are two major things one can say about the admixture event of African Americans and Mexican Americans. The first and more obvious is inferring the admixture level. The second, and more interesting, is inferring when the admixture event happened based on the actual mixture level. As we have discussed in previous chapters, the racial signifiers of the genome break down with admixture because of recombination in each generation. If the population is contained, the percentage of those with European and West African

473

6.047/6.878 Lecture 23: Population Genetic Variation

origin should stay the same in each generation, but the segments will get shorter, due to the mixing. Hence, the length of the haplotype blocks can be used to date back to when the mixing originally happened. (When it originally happened we would expect large chunks, with some gambits being entirely of African origin, for instance.) Using this approach, one can look at the distribution of recent ancestry traps and then fit a model to when these migrants entered an ancestral population as shown below:


Courtesy of Elsevier, Inc., http://www.sciencedirect.com. Used with permission. Source: Kidd, Jeffrey M., et al. "Population Genetic Inference from Personal Genome Data: Impact of Ancestry and Admixtureon Human Genomic Variation." _The American Journal of Human Genetics_ 91, no. 4 (2012): 660-71.

Figure 30.14: As illustration of the magnitude and origin of migrants based on the tract length and number of tracts in the admixed population.

## **30.6 Current Research**

### **30.6.1 HapMap project**

The International Project aims to catalog the genomes of humans from various countries and regions and find similarities and differences to help researchers find genes that will benefit the advance in disease treatment and administration of health related technologies.

### **30.6.2 1000 genomes project**

The 1000 Genomes Project is an international consortium of researchers aiming to establish a detailed catalogue of human genetic variation. Its aim was to sequence the genomes of more than a thousand anonymous participants from a number of different ethnic groups. In October 2012, the sequencing of 1092 genomes was announced in a Nature paper. It is hoped that the data collected by this project will help scientists gain more insight into human evolution, natural selection and rare disease-causing variants.

## **30.7 Further Reading**

- Campbell Biology, 9th edition; _Pearson_ ; Chapter 23: The Evolution of Populations

474

6.047/6.878 Lecture 23: Population Genetic Variation

- The Cell, 5th edition, _Garland publishing_ ; Chapters 5: DNA replication, repair and recombination, Chapter 20: Germ cells and fertilization

## **Bibliography**

475

6.047/6.878 Lecture 23: Population Genetic Variation

476

---

[← Part IV](08-part-iv.md) · [Up: contents](index.md) · [Part V →](10-part-v.md)
