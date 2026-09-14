---
title: B. R-tree
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf
source_file: sources/statomics-sga21/docs/PCI.2011.45.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# B. R-tree

**Source:** [`docs/PCI.2011.45.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This structure is the most successful variant of the R- tree family of indexing structures [9]. It indexes Minimum Bounding Rectangles (MBRs) and its purpose is to minimize both the coverage and the overlap of the MBRs. It uses a revised node splitting algorithm and a forced reinsertion policy in case of a node split. Thus, it uses a method of incremental tree optimization when reinsertion after a split takes place. It can index both multidimensional point data and data with spatial extent. Due to the concentration of measure phenomenon the discrimination of points is minimized, and finding kNN points in high dimensionality


978-0-7695-4389-5/11 $26.00 © 2011 IEEE DOI 10.1109/PCI.2011.45

41

looses its meaning and the R*-tree’s performance degrades to that of the sequential scan.

---

[← I. INTRODUCTION](03-i-introduction.md) · [Up: contents](index.md) · [C. iDistance →](05-c-idistance.md)
