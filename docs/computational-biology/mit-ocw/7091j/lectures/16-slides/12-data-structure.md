---
title: Data Structure
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Data Structure

**Source:** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
0.5 2 1<br>1<br>1 3 5<br>0.2<br>4<br>Weights can represent<br>our confidence in the<br>link<br><!-- End of picture text -->

Adjacency Matrix


<!-- Start of picture text -->
 1   2   3   4   5<br> 1   0 .5   0   0   0<br> 2   .5  0   1   0   1<br> 3   0   1   0   .2  0<br> 4   0   0   .2  0   0<br> 5   0   1   0   0   0<br><!-- End of picture text -->

Weighted graph: aij=wij if edge exists; 0 otherwise

Shortest Path Algorithms

• Efficient Algorithms for

- single pair (u,v)

– single source/destination to all other nodes

– all-pairs

- Reliability of edges

- • Assign weight to each edge based on reliability.

- Total distance in network = sum of edge weights

- If weightij=-log(Pij): minΣwij = min(-log ΠPij) = max (joint probability)

   - = most probable path

---

[← Data Structure](11-data-structure.md) · [Up: contents](index.md) · [Interaction Weights →](13-interaction-weights.md)
