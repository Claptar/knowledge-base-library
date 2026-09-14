---
title: Hierarchical Clustering
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Hierarchical Clustering

**Source:** `recitations/2014-04-09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Can   always   cluster   data,   get   a   dendrogram   and   discover   some “structure”   in   your   data,   but   interpre'ng   or   assigning meaning   to   clusters   is   much   more   difficult

   - clusters   may   not   corresponding   to   anything   biologically   meaningful

- In   contrast   to   agglomera've   (“bofom-­‐up”)   clustering   shown thus   far,   there   is   also   divisive   hierarchical   clustering   (top-­‐ down):

   - start   with   everything   in   one   cluster,   then   cut   the   cluster   into   2,   then cut   those   clusters,   etc.,   un'l   you   have   the   desired   number   of   clusters

29

---

[← Hierarchical Clustering](20-hierarchical-clustering.md) · [Up: contents](index.md) · [K-­‐means clustering →](22-k--means-clustering.md)
