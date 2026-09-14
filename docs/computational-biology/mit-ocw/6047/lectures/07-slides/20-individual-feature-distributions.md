---
title: Individual Feature Distributions
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Individual Feature Distributions

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Instead of a single big distribution, we have a smaller one for each feature (and class)**

**P(Target|Mito) P(Target|~Mito) P(Domain|Mito) P(Domain|~Mito) P(CE|Mito) P(CE|~Mito) P(Mass|Mito) P(Mass|~Mito) P(Homology|Mito) P(Homology|~Mito) P(Induc|Mito) P(Induc|~Mito) P(Motif|Mito) P(Motif|~Mito)**


<!-- Start of picture text -->
Targeting signal<br>Protein domains<br>Co-expression<br>Target<br>Mass Spec<br>7/13<br>Homology<br>Induction<br>3/13<br>2/13<br>Motifs  1/13<br>0<br><1  1-3  3-5  5-7  >7<br><!-- End of picture text -->

Courtesy of Nature Publishing Group. Used with permission. Source: Calvo, Sarah et al. "Systematic identification of human mitochondrial disease genes through integrative genomics." Nature Genetics 38, no. 5 (2006): 576-582.

58

---

[← Binary Classification Errors](19-binary-classification-errors.md) · [Up: contents](index.md) · [Classifying A New Protein →](21-classifying-a-new-protein.md)
