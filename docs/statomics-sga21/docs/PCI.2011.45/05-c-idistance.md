---
title: C. iDistance
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf
source_file: sources/statomics-sga21/docs/PCI.2011.45.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# C. iDistance

**Source:** [`docs/PCI.2011.45.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/PCI.2011.45.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The design of this structure was motivated by the following three observations [10]:

- The (dis)similarity between data points can be derived with reference to a chosen reference or representative point.

- Data points can be ordered based on their distances to a reference point.

- Distance is essentially a single dimensional value.

The iDistance method maps high-dimensional data in single dimensional space, thereby enabling reuse of existing single dimensional indexes, such as the B+tree. This is done using the following procedure: a data point _𝑝_ ( _𝑥_ 0 _, 𝑥_ 1 _, ⋅⋅⋅ , 𝑥𝑑−_ 1), 0 _≤ 𝑥𝑗 ≤_ 1, 0 _≤ 𝑗< 𝑑_ , has an index key, _𝑦_ , based on the distance from the nearest reference point _𝑂𝑖_ as follows:

---

[← B. R-tree](04-b-r-tree.md) · [Up: contents](index.md) · [PCI.2011.45 Part 06 — →](06-pci-2011-45-part-06.md)
