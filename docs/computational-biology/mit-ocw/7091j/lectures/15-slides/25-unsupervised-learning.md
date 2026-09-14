---
title: Unsupervised Learning
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unsupervised Learning

**Source:** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

© Netflix, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

42

Clustering 8600 human genes based on time course of expression following serum stimulation of fibroblasts

Key:  Black = little change   Green = down Red = up (relative to initial time point)

- (A) cholesterol biosynthesis (B) the cell cycle (C) the immediate-early response (D) signaling and angiogenesis (E) wound healing and tissue remodeling


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Iyer, Vishwanath R., Michael B. Eisen, et al. "The Transcriptional Program in the Response of Human Fibroblasts to Serum." _Science_ 283, no. 5398 (1999): 83-7.

Iyer et al. _Science_ 1999

43

##### Why cluster?

• Cluster genes (rows)

– Measure expression at multiple time-points, different conditions, etc.

Similar expression patterns may suggest similar functions of genes

- Cluster samples (columns)

   - e.g., expression levels of thousands of genes for each tumor sample

Similar expression patterns may suggest biological relationship among samples

44

---

[← Clustering](24-clustering.md) · [Up: contents](index.md) · [Hierarchcial clustering →](26-hierarchcial-clustering.md)
