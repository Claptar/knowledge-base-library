---
title: Using epigenomic maps to predict disease-relevant tissues
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/20-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Using epigenomic maps to predict disease-relevant tissues

**Source:** `lectures/20-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

23

### Identifying disease-relevant cell types

Region of association Individual SNPs Height Type 1 Diabetes Blood Pressure Cholesterol Stem Cell Immune Heart Liver Enhancers Enhancers Enhancers Enhancers


- For every trait in the GWAS catalog:

   - Identify all associated regions at P-value threshold

   - Consider all SNPs in credible interval (R<sup>2</sup> ≥;8)

   - Evaluate overlap with tissue-specific enhancers

- Keep tissues showing significant enrichment (P<0.001)

- • Repeat for all traits (rows) and all cell types (columns)

24

##### **<mark>GWAS hits in enhancers of relevant cell types</mark>**

25


<!-- Start of picture text -->
Linking traits to their relevant cell/tissue types<br>ES<br>Liver<br>Brain<br>Digestive<br>Heart<br>T cells B cells<br><!-- End of picture text -->

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

26


27

###### **Immune activation + neural repression in human + mouse**


Courtesy of Macmillan Publishers Limited. Used with permission.

Source: Gjoneska, E., Pfenning, A. R., Mathys, H., Quon, G.,Kundaje, A., Tsai, L., & Kellis, M. (2015). "Conserved Epigenomic signals in mice and humans reveal immune basis of Alzheimer’s disease." Nature, 518 (7539), 365-369. doi:10.1038/nature14252

**_Sample mouse brain epigenomics during Two contrasting signatures of neurodegeneration immune activation vs. neural repression_**

**_Is inflammation simply a consequence of neuronal loss?_**

28

###### **Genetic evidence for immune vs. neuronal components**


<!-- Start of picture text -->
Increasing Decreasing<br>(immune) (neuronal)<br><!-- End of picture text -->


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Gjoneska, E., Pfenning, A. R., Mathys, H., Quon, G., Kundaje, A., Tsai, L., & Kellis, M. (2015). "Conserved Epigenomic signals in mice and humans reveal immune basis of Alzheimer’s disease." Nature, 518(7539), 365-369. doi:10.1038/nature14252

**_Only increasing (immune) enhancers Neuronal cell types are depleted enriched in AD-associated SNPs for AD-associated SNPs Indicates immune cell dysregulation is causal component_** _Microglial cells: resident immune cells of adult brain Macrophages: infiltrate brain in neurodegeneration_

29

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Using epigenomic annotations for fine-mapping disease regions →](03-using-epigenomic-annotations-for-fine-mapping-disease-region.md)
