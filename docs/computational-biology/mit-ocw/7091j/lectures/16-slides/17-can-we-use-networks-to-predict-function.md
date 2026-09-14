---
title: Can we use networks to predict function
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Can we use networks to predict function

**Source:** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Courtesy of EMBO. Used with permission. Source: Sharan, Roded, Igor Ulitsky, et al. "Network `‐` based Prediction of Protein Function." _Molecular Systems Biology_ 3, no. 1 (2007).

**Network-based prediction of protein function** Roded Sharan, Igor Ulitsky & Ron Shamir doi:10.1038/msb4100129


Systematically deduce the annotation of unknown nodes _u_ from the known (filled) nodes


<!-- Start of picture text -->
K=2<br>K=1<br><!-- End of picture text -->

- “Direct” method for gene annotation

- K-nearest neighbors – assume that a node has the same function as its neighbors


Should _u_ and _v_ have the same annotation?


Advantages of kNN approach: very easy to compute Disadvantages: how do you choose the best annotation?

- “Direct” Local search (Karaoz[2004]):

- For each annotation:

   - Sv=1 if v has the annotation, -1 otherwise

   - Procedure: for each unassigned node u, set Su maximize ΣSuSv for all edges (u,v)

   - iterate until convergence


<!-- Start of picture text -->
S=1<br>S=? S=-1 S=1<br>S=1<br><!-- End of picture text -->

**Network-based prediction of protein function** Roded Sharan, Igor Ulitsky & Ron Shamir doi:10.1038/msb4100129

---

[← Finding Modules](16-finding-modules.md) · [Up: contents](index.md) · [A B C →](18-a-b-c.md)
