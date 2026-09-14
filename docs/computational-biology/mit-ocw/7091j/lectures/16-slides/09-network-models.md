---
title: Network Models
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Network Models

**Source:** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Structure of network

   - Coexpression

   - Mutual information

   - Physical/genetic interactions

- Analysis of network

   - Ad hoc

   - Shortest path

   - Clustering

   - Optimization

Graph Algorithms for Interaction Networks

- Rich area of computer science

- Applications to Interaction Networks:

   - Distances:

      - Finding kinase substrates

   - Clustering

      - PPI->Protein complexes, functional annotation

      - Coexpression -> Modules

      - Blast ->Protein families

   - Active subnetworks

      - Finding hidden components of processes

### Networkin


<!-- Start of picture text -->
P<br>P<br>P<br><!-- End of picture text -->

If I know a protein has been phosphorylated, can I determine the kinase?


<!-- Start of picture text -->
P<br><!-- End of picture text -->

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Yeger-Lotem, Esti, Laura Riva, et al. "Bridging High-throughput Genetic and Transcriptional Data Reveals Cellular Responses to Alpha-synuclein Toxicity."

_Nature Genetics_ 41, no. 3 (2009): 316-23.


Courtesy of Elsevier, Inc., http://www.sciencedirect.com. Used with permission. Source: Linding, Rune, Lars Juhl Jensen, et al. "Systematic Discovery of in Vivo Phosphorylation Networks." _Cell_ 129, no. 7 (2007): 1415-26.

Linding _et al._ (2007) Cell. doi:10.1016/j.cell.2007.05.052


Step 1: Use sequence motifs to determine family of kinase

Courtesy of Elsevier, Inc., http://www.sciencedirect.com. Used with permission. Source: Linding, Rune, Lars Juhl Jensen, et al. "Systematic Discovery of in Vivo Phosphorylation Networks." _Cell_ 129, no. 7 (2007): 1415-26.

Linding _et al._ (2007) Cell. doi:10.1016/j.cell.2007.05.052


Step 1: Use sequence motifs to determine family of kinase

Step 2: Use Interactome data to find most likely family member

Courtesy of Elsevier, Inc., http://www.sciencedirect.com. Used with permission.

Source: Linding, Rune, Lars Juhl Jensen, et al. "Systematic Discovery of in Vivo Phosphorylation Networks." _Cell_ 129, no. 7 (2007): 1415-26.

Linding _et al._ (2007) Cell. doi:10.1016/j.cell.2007.05.052

Which is best?

High-throughput Two-hybrid assay <mark>High confidence inte</mark> raction

---

[← Joint probability of graph](08-joint-probability-of-graph.md) · [Up: contents](index.md) · [How do we find the closest kinase? →](10-how-do-we-find-the-closest-kinase.md)
