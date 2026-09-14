---
title: MCL clustering
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# MCL clustering

**Source:** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Stochastic Matrix:  each element Mij represents a probability of moving from i to j (this is a “Column Stochastic Matrix”).


- Therefore,

- The probability of moving from i to j in two steps is given by


Courtesy of Elsevier, Inc., http://www.sciencedirect.com. . Used with permission. Source: Schaeffer, Satu Elisa. "Graph Clustering." _Computer Science Review_ 1, no. 1 (2007): 27-64.

- If we keep multiplying the stochastic matrix by itself, we compute the probabilities of longer and longer walks – we expect that the transitions will occur more frequently within a natural cluster than between them.


Courtesy of Elsevier, Inc., http://www.sciencedirect.com. Used with permission. Source: Schaeffer, Satu Elisa. "Graph Clustering." _Computer Science Review_ 1, no. 1 (2007): 27-64.

• This procedure won’t produce discrete clusters, so the algorithm includes an “inflation” step that exaggerates these effects: raise each element of the matrix to the power r and renormalize.


<!-- Start of picture text -->
pA = 0.9<br>pB = 0.1<br>.81<br>= .99<br>pA →<br>.81 + .01<br>.01<br>= .01<br>pB →<br>.81 + .01<br><!-- End of picture text -->


**Protein Interaction Networks: Computational Analysis**

By Aidong Zhang

http://books.google.com/books?id=hOzAUrwW-ZoC&lpg=PA141&ots=Vd0TK0fCAR&dq=mcl%20inflation%20operator&pg=PA142#v=onepage&q&f=true

**G** is a graph

add loops to **G** # needed for a prob. of no transition set Γ to some value # affects granularityaffects granularity

set Γ to some value # affects granularityaffects granularity set **M_1** to be the matrix of random walks on **G** while (change) {

**M_2** = **M_1** * **M_1** # expansion

**M_1** = Γ( **M_2** ) # inflation change = difference( **M_1** , **M_2** ) }

set CLUSTERING as the components of **M_1**

---

[← MCL clustering](27-mcl-clustering.md) · [Up: contents](index.md) · [Example →](29-example.md)
