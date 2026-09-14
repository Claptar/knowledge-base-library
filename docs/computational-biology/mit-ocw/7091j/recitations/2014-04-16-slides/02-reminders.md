---
title: Reminders
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-16-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Reminders

**Source:** `recitations/2014-04-16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Project due next Tuesday at midnight!

   - writeup description posted, email us if any questions

- Problem Set #5 (last one!) will be out next Tuesday also

   - due Thurs, May 1<sup>st</sup>

   - a bit shorter, not a lot of programming

2

## Predicting Protein Levels

#### <u>Recall the central dogma:</u>


<!-- Start of picture text -->
vsr ksp<br>DNA  transcription  translation<br>protein<br>mRNA<br>mRNA   protein<br>kdr kdp<br>degradation<br>degradation<br><!-- End of picture text -->


- Let’s elaborate a little:

   - assume transcription and translation occur at rates vsr and ksp respectively

   - and mRNAs and proteins also degrade at rates kdr and kdp respectively

   - Then we can describe how _R_ = mRNA conc. and _P_ = protein conc. change over time using differential equations:


<!-- Start of picture text -->
dP<br>dR<br>=  vsr – kdr R  =  kspR – kdp P<br>dt<br>dt<br><!-- End of picture text -->

3

## Predicting Protein Levels <u>Recall the central dogma:</u>


<!-- Start of picture text -->
vsr ksp<br>DNA  transcription  translation<br>protein<br>mRNA<br>dR<br>=  vsr – kdr R  mRNA   protein<br>kdr kdp<br>dt degradation<br>degradation<br>dP<br>=  kspR – kdp P<br>dt<br>Experimentally, it is much easier to get mRNA levels<br>(microarray, RNA-seq) than protein levels (2D<br>electrophoresis, mass-spec), so we often use gene<br>expression as an approximation of protein levels<br>However, mRNA levels alone are generally poor<br>predictors of protein levels, since they fail to account<br>for either translation rates or protein degradation<br>rates<br><!-- End of picture text -->

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

4

## Predicting Protein Levels

#### <u>Recall the central dogma:</u>


<!-- Start of picture text -->
vsr ksp<br>DNA  transcription  translation<br>protein<br>dR mRNA<br>=  vsr – kdr R<br>dt mRNA   kdr protein  kdp<br>degradation<br>degradation<br>dP<br>=  kspR – kdp P<br>dt<br>Also, proteins tend to be more<br>stable than RNA and to stick<br>around in the cell longer, so the<br>total amount of protein<br>depends on the amount of RNA<br>over a long period of time<br><!-- End of picture text -->

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Schwanhäusser, Björn, Dorothea Busse, et al. "Global Quantification of Mammalian Gene Expression Control." _Nature_ 473, no. 7347 (2011): 337-42.

5

## Graph Terminology


<!-- Start of picture text -->
A  B<br>node/vertex  A  B<br>undirected  0.2  0.8<br>edge  C  C  directed edge +<br>0.6  0.9  edge weights<br>D  E<br>D  E<br>Graph G1:  Graph G2:<br>undirected  directed<br><!-- End of picture text -->

- A graph G is specified as a list of nodes/vertices V and a list of edges E, so G = (V,E) - G1 and G2 both have V = [A,B,C,D,E]

- G1 has undirected edges E = [(A,C),(A,D),(C,B),(B,E),(E,C),(D,E)] = 6 edges - G2 has directed edges, so must give (parent,child) lists:  E = [(A,C),(B,C),(C,D),(C,E)]

- Degree(vertex) = # of edges incident on vertex, can split into in and out-degree if directed - in G1, Degree(C) = 3

   - in G2, vertex C has in-degree 2 and out-degree 2

Paths between two vertices have length = sum of edge weights (= # of edges if no weights) - in G1, one path from A to E is <A,C,E> and is of length 2. - in G2, path from A to E is also <A,C,E> but is of length 0.2 + 0.9 = 1.1

6

## Adjacency Matrix

A B The adjacency matrix A of a graph with N nodes is an NxN matrix where Aij = C the weight of edge from node _i_ to node _j_ in the graph if it exists, and 0 if there is D E no edge **Graph G1: 1: :** - symmetric if graph is undirected


<!-- Start of picture text -->
Graph G1: 1: :<br>undirected<br><!-- End of picture text -->


<!-- Start of picture text -->
A  B<br>0.2  0.8<br>C<br>0.6  0.9<br>D  E<br>Graph G2:<br>directed<br><!-- End of picture text -->


<!-- Start of picture text -->
Adjacency matrix for G1<br>i  j  A  B  C  D  E<br>A 0  0  1  1  0<br>B 0  0  1  0  1<br>C 1  1  0  0  1<br>D 1  0  0  0  1<br>E 0  1  1  1  0<br><!-- End of picture text -->


<!-- Start of picture text -->
Adjacency matrix for G2<br><!-- End of picture text -->


<!-- Start of picture text -->
i  j A  B  C  D  E<br>A 0  0  0.2  0  0<br>B 0  0  0.8  0  0<br>C 0  0  0  0.6  0.9<br>D 0  0  0  0  0<br>E 0  0  0  0  0<br><!-- End of picture text -->

7

A

B

C

D E

###### **A**<sup>**1**</sup>

## Adjacency Matrix

Let A<sup>k</sup> be adjacency matrix A raised to the _k_ th power where Aij is either 1 or 0 (e.g. does not take edge weights into account).  Then the _ij_ th entry of A<sup>k</sup> corresponds to the number of paths from node _i_ to node _j_ of length _k_

##### _- note:  path length = # of edges traversed_ **A**<sup>**2**</sup> **A**<sup>**3**</sup>

|**_i_**<sup>**_j_**</sup>|A|B|C|D|E|
|---|---|---|---|---|---|
|A|0|0|1|1|0|
|B|0|0|1|0|1|
|C|1|1|0|0|1|
|D|1|0|0|0|1|
|E|0|1|1|1|0|


|**_i_**<sup>**_j_**</sup>|A|B|C|D|E|
|---|---|---|---|---|---|
|A|2|1|0|0|2|
|B|1|2|1|1|1|
|C|0|1|3|2|1|
|D|0|1|2|2|0|
|E|2|1|1|0|3|


|**_i_**<sup>**_j_**</sup>|A|B|C|D|E|
|---|---|---|---|---|---|
|A|0|2|5|4|1|
|B|2|2|4|2|4|
|C|5|4|2|1|6|
|D|4|2|1|0|5|
|E|1|4|6|5|2|


How many paths of length 2 are there from A to E? A<sup>2</sup> AE<sup>= 2 so there are 2 paths of length 2 from A to E:  A-C-E and A-D-E</sup> How many paths of length 3 are there from A to E?

A<sup>3</sup> AE<sup>= 1 so there is 1 path of length 3 from A to E:  A-C-B-E</sup> How many paths of length 3 are there from A to D? A<sup>3</sup> AD<sup>= 4 so 4 paths:  A-D-E-D, A-C-E-D, A-C-A-D, A-D-A-D</sup>

8

## Network Models in Biology

- Many types of large (hairball) networks

   - PPI, genetic interactions, expression networks….

- Many large networks exist today – we can use these to predict function for the large number of functionally unannotated genes

- Today, we will cover algorithms to annotate nodes in these networks


A large number of genes across many organisms still have unknown function


Networks can help us predict function – closeness in a network may indicate functional similarity

© EMBO and Nature Publishing Group. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Sharan, Roded, Igor Ulitsky, et al. "Network ‐ based Prediction of Protein Function." _Molecular Systems Biology_ 3, no. 1 (2007).

9

## Annotating graphs

- Directly annotating unknown nodes

   - K-nearest neighbors

   - Local search

   - Simulated annealing

- Clustering graphs (then annotate each cluster)

   - Betweenness clustering

   - Markov clustering

10

## Annotating graphs

- Directly annotating unknown nodes

   - K-nearest neighbors

   - Local search

   - Simulated annealing

- Clustering graphs (then annotate each cluster)

   - Betweenness clustering

   - Markov clustering

11

## K-nearest neighbor approach

- Assumes that a node has related function to its neighbors

- Start with a partially known graph (shaded nodes)

- Assign function based on its neighbors within distance _k_ – easy to compute


<!-- Start of picture text -->
k  = 2<br>k  = 1<br>u  v<br><!-- End of picture text -->


**_k_ = 1:** No neighbors are annotated and we are unable to annotate node _u._

**_k_ = 2:** Two neighbors are now annotated. We assign the same annotation to node _u_ .

**_What if nodes have different annotations? Should u and v have the same annotation?_**

12

## Local Search Algorithm

- Allows us to deal with multiple nearby annotations

   - For each annotation (e.g. green, blue):

      - For each node _i_ , set Si=1 if i has that annotation, Si=-1 otherwise

      - For each unannotated node, set Si such that it maximizes                 over all neighbors v

If most neighbors are +1, this will lead to Si=+1. If most neighbors are -1, this will lead to Si=-1.

Sa=1

Values assigned currently considering blue annotation a


<!-- Start of picture text -->
u  d  c<br>Su=-1  Sd=-1  Sc=1<br>b<br><!-- End of picture text -->

Sb=1

Values assigned currently considering green annotation


<!-- Start of picture text -->
a<br><!-- End of picture text -->


<!-- Start of picture text -->
Sa=-1<br>u  d  c<br>Su=-1  Sd=1  Sc=-1<br>b<br><!-- End of picture text -->

Sb=-1

13

## Local Search Algorithm

- Allows us to deal with multiple nearby annotations

   - For each annotation (e.g. green, blue):

      - For each node _i_ , set Si=1 if i has that annotation, Si=-1 otherwise

      - For each unannotated node, set Si such that it maximizes                 over all neighbors v

If most neighbors are +1, this will lead to Si=+1. If most neighbors are -1, this will lead to Si=-1.

Sa=1

Values assigned currently considering blue annotation a

u d c Su=-1 Sd=-1 Sc=1

b

Sb=1

If we want to annotate Su, we see that it should be blue (+1 from the blue perspective) in order to maximize:

Su(Sa+Sb+Sd) =Su(1+1-1) =Su  Su=1

14

## Local Search Algorithm

- In complex graphs with lots of unannotated nodes, local search may not find good solutions – local optimization can’t find global solution

- • For example, if we try to annotate node _b_ first, turning it to blue would actually make the score worse, so we would never turn _b_ blue


<!-- Start of picture text -->
a  b  c<br><!-- End of picture text -->


15

## Simulated Annealing

As before, to perform global optimization, we use our usual Simulated Annealing approach with Metropolis Acceptance criterion. If we want a high scoring graph (instead of low energy as in protein structure):

- Initialize with starting T and a graph G with score S

- For some number of iterations:

   - Randomly perturb the network (may add/remove/reweight an edge or include/exclude a vertex), giving Gtest with score Stest

   - If Stest > S, accept the new graph and update G and S

   - Otherwise, accept the new graph with probability P=e<sup>-(S-Stest)/kT</sup> and update accordingly

- Lower _T_ according to the cooling schedule

16

## Annotating graphs

- Directly annotating unknown nodes

   - K-nearest neighbors

   - Local search

   - Simulated annealing

- Clustering graphs (then annotate each cluster)

   - Betweenness clustering

   - Markov clustering

17

## Annotating graphs

- Directly annotating unknown nodes

   - K-nearest neighbors

   - Local search

   - Simulated annealing

- Clustering graphs (then annotate each cluster)

   - Betweenness clustering

   - Markov clustering

18

## Clustering graphs

- Divide large graph into subgraphs, each of which has:

   - Lots of internal connections

   - Few connections to the rest of the graph

- Two algorithms

   1. Betweenness clustering

   2. Markov clustering


We would like to split this graph into its 2 logical subgraphs.

- Once we have clustered a graph, we can annotate each cluster

19

## Betweenness clustering

- Betweenness – property of edges

   - Number (or summed weight) of shortest paths between all pairs of vertices that pass through that edge

• Split weight among multiple shortest paths if there are more than 1 for a pair of nodes This edge (and others within the respective clusters) have low betweenness. In this particular case, this edge is contained in only one shortest path (the shortest path between the two nodes it connects)

This edge (connecting the two clusters) has high betweenness. This edge is contained in all shortest paths between the left and right subgraphs.

20

## Betweenness clustering algorithm

- Precompute shortest paths between all pairs of nodes (FloydWarshall/Johnson’s algorithm)


- Repeat until max betweenness < threshold:

   - For each edge in the graph:

      - Compute betweenness

   - Remove edge with high betweenness

- As we remove edges with high betweenness, we are breaking the graph into chunks that are more connected internally

21

## Markov clustering

### • Intuition: A random walk will spend more time within a cluster than passing between cluster


If we assume all edges are equally weighted in this graph, there is only one way to get from the left subgraph to the right subgraph, while there are many more options (and therefore we are more likely) to stay in a particular subgraph.

22

## Stochastic Matrix

- If we normalize along the rows of the adjacency matrix, we generate a new matrix M (with the same dimensions as A), where the _ij_ th entry of M represents the probability of moving from node _i_ to node _j_ during the random walk


<!-- Start of picture text -->
A  B<br>C<br>D  E<br><!-- End of picture text -->


<!-- Start of picture text -->
A  A  B  C  D  E<br>A 0  0  1  1  0<br>B 0  0  1  0  1<br>C 1  1  0  0  1<br>D 1  0  0  0  1<br>E 0  1  1  1  0<br><!-- End of picture text -->


<!-- Start of picture text -->
M  A  B  C  D  E<br>A 0  0  ½  ½   0<br>B 0  0  ½  0  ½<br>C .33 .33  0  0  .33<br>D ½   0  0  0  ½<br>E 0  .33  .33  .33  0<br><!-- End of picture text -->


23

## Stochastic Matrix


<!-- Start of picture text -->
A  B<br>C<br>D  E<br><!-- End of picture text -->


<!-- Start of picture text -->
A  A  B  C  D  E<br>A 0  0  1  1  0<br>B 0  0  1  0  1<br>C 1  1  0  0  1<br>D 1  0  0  0  1<br>E 0  1  1  1  0<br><!-- End of picture text -->


<!-- Start of picture text -->
M  A  B  C  D  E<br>A 0  0  ½  ½   0<br>B 0  0  ½  0  ½<br>C .33 .33  0  0  .33<br>D ½   0  0  0  ½<br>E 0  .33  .33  .33  0<br><!-- End of picture text -->


- Recall: the _ij_ th entry of A<sup>k</sup> corresponds to the number of paths from node _i_ to node _j_ of length _k_

- Similarly: the _ij_ th entry of M<sup>k</sup> corresponds to the probability of moving from node _i_ to node _j_ in _k_ steps

   - The probability of moving from _i_ to _j_ in two steps is given by

24

## Stochastic Matrix

- the _ij_ th entry of M<sup>k</sup> corresponds to the probability of moving from node _i_ to node _j_ in _k_ steps

   - The probability of moving from _i_ to _j_ in two steps is given by

- If we keep multiplying the stochastic matrix, we compute probabilities of longer walks – we expect that transitions will occur more frequently within a natural cluster than between them

- To produce discrete clusters, Markov clustering also includes an inflation step to exaggerate these effects – make high probabilities higher and low probabilities lower

   - Inflation step: raise each element to the _k_ power and renormalize


<!-- Start of picture text -->
k = 2<br><!-- End of picture text -->


25

## Markov clustering algorithm

- **G** is a graph

- add self-transition loops to G to allow for no transition (e.g. staying in current node)

- Set inflation parameter (e.g. k=2)

- Initialize **M1** to be the initial stochastic matrix of G

- Until convergence (e.g. while the stochastic matrix keeps changing):

   - **M2 = M1 * M1**

   - **M1 = inflate M2**

- Once you’ve converged, set the clustering to be the components of **M1**

26

## Clustering graphs

- Markov clustering is a faster algorithm since it only requires matrix operations

- How do we decide which function to assign to members of a cluster?

   - Consensus based on nodes within each cluster that are already annotated

   - Determine significance by hypergeometric / use Gene Ontology

27

## Annotating graphs

- Directly annotating unknown nodes

   - K-nearest neighbors

   - Local search

   - Simulated annealing

- Clustering graphs (then annotate each cluster)

   - Betweenness clustering

   - Markov clustering

28

## Network Modules

- Networks have a modular structure

- • Topological modules

   - subgraphs which are locally dense and have more connections among nodes within the module than with nodes outside the module

- we found topological modules in our _clustering_ algorithms

- • Functional modules

   - subgraphs with a high density of functionally related nodes

   - we will look for functional modules in the **_active subnet_** algorithms (next)


Courtesy of Macmillan Publishers Limited.  Used with permission. Source: Barabási, Albert-László, Natali Gulbahce, et al. "Network Medicine: A Network-based Approach to Human Disease." _Nature Reviews Genetics_ 12, no. 1 (2011): 56-68.

29

## Active Subnet Problem

- So far, we have focused on labelling the nodes of a graph

- Now, assume we already have a labelled graph (e.g. We took a PPI network and labelled the edges with expression data – high/low)

- We would now like to find connected components of these graphs are enriched in a particular label – this is the **active subnet problem** (e.g. finding PPI subnetwork with high expression)

- This can reveal the hidden components of a biological response

30

## Active Subnet Problem

- This problem has already been studied in theoretical Computer Science

We would like to find the minimum tree connecting all yellow nodes (given by blue lines).

- Steiner Tree Problem (NP-hard):

   - Given a graph **G = (V, E, w)** ( _vertices, edges, and weights)_ and a subset ( _vertices of interest_ )

   - **Find** the minimum weight tree (connected set of edges) that spans all the vertices in S


- (we didn’t cover any algorithms in class – a couple optimization algorithms were sited)

However, we would also like to exclude the rightmost yellow node as its distance suggests it may be a false positive.

31

## Active Subnet Problem

- To avoid false positives, we solve a problem variant – the **_prize-collecting_** Steiner tree problem


• Intuition:

We pay a penalty for each vertex we do not include in the Steiner tree (we _collect a prize_ for each vertex we do include)

We pay a cost for including edges in the Steiner tree

- The terms in the objective function balance each other • Adding too many edges to get to a node far away will induce a high edge penalty while collecting lower prize for the node

32

## Active Subnet Problem

- While a traditional Steiner Tree would include the distant node, given some setting of the edge penalties and vertex prizes, the prize collecting Steiner Tree could exclude the node

- Eg. If this is a PPI network, the distantly labelled node could be highly expressed, but we would consider it unlikely to interact given its distance in the network


33

## Data Integration

- When looked at individually, different data sources (mRNA levels vs gene knockout fitness) can give very different results

   - Genetic screens usually detect  master regulators

   - mRNA measurements detect effectors (metabolic proteins)

- We can integrate these sources by piling the data into one network


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

34

## Logic modeling of cell signaling networks

- We can study gene signaling networks at many data levels

   - DNA sequence

   - mRNA expression

   - Protein levels

   - Dynamic protein operations (e.g. phosphorylation)

- Integrating these is difficult, but important to understand the full range of processes that might contribute to differences between normal and disease states

35

## Difficulties in studying cancer

• There are many different genetic alterations that are observed within a tumor type


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Jones, Siân, Xiaosong Zhang, et al. "Core Signaling Pathways in Human Pancreatic Cancers Revealed by Global Genomic Analyses." _Science_ 321, no. 5897 (2008): 1801-6.

36

## Difficulties in studying cancer

- There are many different genetic alterations that are observed within a tumor type

- But many of these mutations converge into a limited set of proteins and pathways


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Jones, Siân, Xiaosong Zhang, et al. "Core Signaling Pathways in Human Pancreatic Cancers Revealed by Global Genomic Analyses." _Science_ 321, no. 5897 (2008): 1801-6.

37

## Difficulties in studying cancer

- There are many different genetic alterations that are observed within a tumor type

- But many of these mutations converge into a limited set of proteins and pathways

   - We need to turn these pathways into computable models and circuitry that we can make predictions from and use as a basis for intervention strategies

38

## Computational Modeling Approaches

- Differential equations (“theory-driven”)

   - Can write down differential equation models for up to dozens of variables to represent cellular mechanisms

   - However, we generally don’t know enough about the rate constants to make differential equation models useful

- “Data-driven”: regression, clustering of large data sets (e.g. RNA-seq, signaling pathway output measurements, mass-spec. proteomics)

39

## Logic-based modeling

- We often take an intermediate approach that incorporates what is known (theory-driven) with data-driven experimental analyses

   - Incorporate existing pathway/interactome databases

      - Challenge: different databases often give disparate or even conflicting results!

      - Data is also very diverse: may come from different species, cell type, growth conditions, etc.

      - We can use these pathways and interactions as a starting point, but due to these limitations they can’t tell us everything

      - We must turn this starting network topology into an actionable, computable model by integrating relevant experimental data

40

## Boolean Framework

- Often used on top of the network structure to explain experimental observations

- Variables (nodes – e.g. TFs or signaling molecules) are ON/OFF

- We connect nodes through AND & OR logic gates to represent cellular interactions & pathways


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

41

## Boolean Framework

- Often used on top of the network structure to explain experimental observations

- Variables (nodes – e.g. TFs or signaling molecules) are ON/OFF

- We connect nodes through AND & OR logic gates to represent cellular interactions & pathways

- We can then perturb the variables _in silico_ to predict outcomes if we introduce a therapeutic

42

## Sample Experimental Data

- Phoshoproteomic data (measuring the activity state of pathway molecules)

   - Multiple relevant signaling pathways

   - Introduce perturbations (e.g. inhibitor molecules) and measure outputs at various time points


<!-- Start of picture text -->
TRANSIENT  LATE<br>NO RESPONSE  SUSTAINED<br><!-- End of picture text -->

**Time-points: 0, 30 min, 3 hrs**

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

43

## Sample Experimental Data

- Phoshoproteomic data (measuring the activity state of pathway molecules)

   - Multiple relevant signaling pathways

   - Introduce perturbations (e.g. inhibitor molecules) and measure outputs at various time points

- Try to model the experimental data using the multiple potential networks (graph structures and associated quantitative relationships) from the databases

   - We must define some way to evaluate the model’s performance to decide which is the most likely network


- We want to consider not necessarily the single best model (because of experimental noise), but look at the full spectrum of top performing models to come up with a representative family of models

44

## Improving upon models

- From the top performing model(s), make some perturbations of the model (via genetic algorithms) to improve the fit (similar to what we saw for Bayesian networks, e.g. Pebl)

- How well does this work in practice?

   - If we simply take the best result from the database and fit the experimental data to the model, we get ~45% error (because not all interactions are real and some are missing, might be the wrong cell type or environmental condition, etc.)

   - After model improvement (e.g. adding and removing edges), we may be able to reduce the error to below 10%

   - Often the model is not as complex as we might expect! Introducing too many variables may lead to simply fitting to noise and increase false positives

45

## What are models used for?

- Can make predictions for new inhibitor combinations (therapeutic drug cocktails) that may be infeasible to exhaustively test experimentally • Comparing where our model predictions went wrong based on new experimental data informs us where our network model may be incorrect and how we might improve it

   - Edges that are included in the model and needed to explain the data can inform us about cellular processes (interactions that are missing in the databases or offtarget effects of drugs)

46

## Extending Boolean Logic for analog data

- Boolean logic deals with qualitative YES/NO (ON/OFF) relationships, but quantitative data is continuous

   - Instead of a step function from OFF to ON at a particular value, use continuous functions that have a graded slope from OFF to ON over a range of values

      - More realistic, but this ~doubles the number of free parameters in the model, so we need much more experimental data

47

## Fin

48

###### MIT OpenCourseWare

http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 4-16 Recitation](01-4-16-recitation.md) · [Up: contents](index.md)
