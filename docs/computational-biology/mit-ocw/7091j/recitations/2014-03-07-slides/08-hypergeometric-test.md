---
title: Hypergeometric Test �
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Hypergeometric Test �

**Source:** `recitations/2014-03-07-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- For this example, we obtain:


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Therefore, with α = 0.05, we reject the null hypothesis that the overlap between conditions A and B are due to random chance, suggesting there is some similarity between gene expression changes caused by heat shock and oxidative stress

13


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Gkountela, Sofia, Ziwei Li, et al. "The Ontogeny of cKIT+ Human Primordial Germ Cells Proves to be a Resource for Human Germ Line Reprogramming, Imprint Erasure and in Vitro Differentiation." _Nature Cell Biology_ 15, no. 1 (2013): 113-22.

14

### PCA identifies the directions (PC1 and PC2) along which the data have the largest spread


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- -1<sup>st</sup> principal component is the direction of maximal variation among your sample

   - Magnitude of this component is related to how much variation there is in this direction

- -2<sup>nd</sup> principal component is next direction (orthogonal to 1<sup>st</sup> direction) of remaining maximal variation in your sample

   - Magnitude of this component will be smaller than that of 1<sup>st</sup>

etc.

15

### PCA identifies the directions (PC1 and PC2) along which the data have the largest spread


-Each principal component gets smaller –this is why summarizing data with first 2 or 3 components is an OK first approximation of data - This example: first 2 components retain 22% of total variance; 63 components retain 90% of variance


<!-- Start of picture text -->
-Visualizing data points<br>as projections onto first<br>PCs often reveals<br>“clustering” of samples<br>into groups – want to<br>make sure these are<br>biologically relevant and<br>not technical artifacts<br>(e.g., samples cluster<br>into 2 groups based on<br>which of two different<br>days libraries were<br>See 2 page Nature Biotech Primer: prepared)<br><!-- End of picture text -->

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Ringnér, Markus. "What is Principal Component Analysis?" _Nature Biotechnology_ 26, no. 3 (2008): 303-4.

http://www.nature.com/nbt/journal/v26/n3/pdf/nbt0308-303.pdf

16

---

[← Hypergeometric Test �](07-hypergeometric-test.md) · [Up: contents](index.md) · [Topic Models � →](09-topic-models.md)
