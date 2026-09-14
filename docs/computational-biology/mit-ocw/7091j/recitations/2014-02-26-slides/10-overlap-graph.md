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

- Each node is a read

   - Directed edge is overlap between suffix of that read to prefix of another read (overlap at least length _l_ )

   - Also include reverse complements of reads since we only sequence 1 of 2 strands of DNA

CTCTAGGCC GCCCTCAAT %%%%%%||| %%%%%|||| %%%%%%GCCCTCAAT %%%%%CAATTTTT http://www.langmead-lab.org/teaching-materials/ http://www.langmead-lab.org/teaching-materials/

- To assemble the genome, we would ideally find the _shortest common superstring_

   - This is the _shortest_ string that contains all relationships implied by the overlap graph from all of the reads

   - Finding a “Hamiltonian path” (traveling salesman problem) to visit all of the nodes: turns out this is too complex of a problem to solve

   - Greedy methods that will find not the shortest but close to shortest (bounded by ~2.5x shortest)

- Greedy method makes the locally optimal choice at each step but doesn’t look any further ahead to take steps that may lead to overall better solutions in the end

- – Even if it were tractable, one problem with this approach is that finding the _shortest common superstring_ will collapse repeats longer than your overlap

22

---

[← Two main approaches](09-two-main-approaches.md) · [Up: contents](index.md) · [Overlap graph →](11-overlap-graph.md)
