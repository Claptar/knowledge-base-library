---
title: Overlap graph
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-26-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Overlap graph

**Source:** `recitations/2014-02-26-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- To simplify the graph, can remove edges that provide no additional information 1


http://www.langmead-lab.org/teaching-materials/ http://www.langmead-lab.org/teaching-materials/

- This produces _contigs_ of consecutive sequence: each contig corresponds to a clear path through part of the graph


23

## From overlap graphs  de Bruijn graphs

- Overlap graphs: each _k_ mer is a node – Would like to visit each _node_ once to assemble a version of the genome

- Hamiltonian path through the graph

- – However, this very hard (NP-hard) and computationally does not scale to large genomes

- • de Bruijn graphs: each _k_ mer is an edge – In contrast, the problem of visiting each _edge_ once to assemble a version of the genome is computationally tractable

   - Eulerian path through the graph

24

---

[← Overlap graph](10-overlap-graph.md) · [Up: contents](index.md) · [de Bruijn graph →](12-de-bruijn-graph.md)
