---
title: 4.2 The random graph
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/22-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4.2 The random graph

**Source:** `lectures/22-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Analyzing biological data from the perspective of networks has gained interest recently. Much is known about the interplay of proteins that control expression of genes, the connections of the few hundred neurons in the roundworm C. elegans, and other example. One possible route to extracting information from such data is to look for specific motifs, subgroups of several nodes, that can cooperate in simple functions (e.g. a feedforward loop). A particular motif can be significant if it appears more (or less) frequently than expected. We thus need a simple model whose expectations can be compared with biological data. Random graphs, introduced by Erd¨os and R´enyi, serve this purpose. The model consists of N nodes, with any pair connected at random and independently, with probability p.

We shall explore several features of Erd¨os-R´enyi networks in the following sections. For the time being, we note that the expected number of subgraphs of n nodes and l links,


is obtained as a product of the number of ways of picking n points and connecting them with l links, and a factor that accounts for the number of ways of connecting the points into the desired graph. For example, there are n!/2 ways to string n points along a straight line with l = (n − 1), and the expected number of such linear pathways is


while there are n!/(2n) ways to make a cycle of n nodes and l = n links, such that


There is also a single way to make a complete graph in which any pair of nodes is connected by a link, i.e. l = n(n − 1)/2, and


### 4.2.1 Percolation

A network can display two types of global connectivity. With few connections amongst nodes, there will be many disjoint clusters, with their typical size (but not necessarily number)

71

increasing with the number of connections. At high connectivity there will be one very large cluster, and potentially a number of smaller clusters. In the limit of N →∞, a well defined percolation transition separates the two regimes in the random graph, as the probability p is varied.

Above the percolation transition, the number of nodes M in the largest cluster also goes to infinity, proportionately to the number of nodes, such that there is a finite percolation probability


For the random graph P (p) can be calculated from a self-consistency argument: Take a particular site and consider the probability that it is not connected to the infinite cluster. This is the case if none of the (N − 1) edges emanating from this site connect it to the large cluster. A particular edge connects to the infinite cluster with probability pP (p) (that the edge exists and that the adjoining site is on the large cluster), and hence


There is a phase transition in the limit N →∞, provided that p → 0, such that


where ⟨k⟩, the number of expected edges per node, is finite. In this limit, we can re-express Eq. (4.5) as


The above equation can be solved self-consistently, for example graphically, For ⟨k⟩≤ 1, the


only solution is P = 0, while for ⟨k⟩ > 1 a finite P is possible, indicating the appearance of an infinite cluster. Close to the percolation transition at ⟨k⟩c = 1, P is small and we can expand Eq. (4.7) as


72


### 4.2.2 Distance, Diameter, & Degree Distribution

There are typically several ways to traverse from a node i to a node j. The distance between any pair of nodes is defined as the number of edges along the shortest path between the nodes. For the entire network, we can define a diameter as the largest of all distances between pairs of nodes.

Distances to a particular node can be obtained efficiently by the following simple (burn and move) algorithm. In the first step, label the nodes connected to the starting point (d = 1), and then remove it from the network. Consider a random graph with ⟨k⟩≫ 1, such that P ≈ 1. (Distances cannot be defined to disconnected clusters.) In the random graph, the number of sites with d = 1 will be around p(N − 1) = ⟨k⟩. In the second step identify all sites connected to the set labeled before (and thus at d = 2), and then remove all sites with d = 1 from the network. From each site with d = 1, there are of the order of p(N −⟨k⟩− 1) ≈⟨k⟩ accessible sites, since ⟨k⟩≪ N. There are thus around ⟨k⟩<sup>2</sup> sites labelled with d = 2. This burn and move process can be repeated, with Np ⪅ ⟨k⟩<sup>p</sup> sites tagged at distance d = p. (Note that each step we have overestimated the number of sites by ignoring connections leading to sites already removed.) The procedure has to be stopped when all sites belonging to the cluster have been removed, i.e. for


where D is a rough measure of the diameter of the network. Note that the diameter of a random network is quite small, justifying the popular lore of “six degrees of separation.” In a population of a few billion, with each individual knowing a few thousand, Eq. (4.9) in fact predicts a distance of three or four between any two. Clearly segregation by geographical and social barriers increases this distance. The model of “small world networks” considers mostly segregated communities, but shows that even a small fraction of random links is sufficient to reintroduce a logarithmic behavior ala Eq. (4.9).

For ⟨k⟩ < 1, the typical situation is of disjoint clusters. We can then inquire about the probability pk that there are exactly k links emanating from a site. Since there are a total of (N − 1) potential connections from a site, in a random graph the probability that k such

73

links are active is given by the binomial probability


Taking the limits N →∞ and p → 0 with pN = ⟨k⟩ as before, we obtain


i.e. a Poisson distribution with mean ⟨k⟩. The above results for random graphs can be used as a potential model for assessing significance of putative anomalies in the the degree distributions of social and biological networks.

---

[← 4.1 Networks](02-4-1-networks.md) · [Up: contents](index.md) · [4.3 The Barabasi-Albert model →](04-4-3-the-barabasi-albert-model.md)
