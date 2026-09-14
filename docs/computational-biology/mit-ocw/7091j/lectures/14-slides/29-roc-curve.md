---
title: ROC curve
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/14-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# ROC curve

**Source:** `lectures/14-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
e<br> )<br>es<br>denc<br>ex<br>onfi pl<br>-c om  )<br>gh c<br>FN<br>+<br>om<br>ng hii fr ( (TP<br>/<br>us<br>es<br>v TP<br>tii<br>pute<br>pos<br>Com<br><!-- End of picture text -->

© American Society for Biochemistry and Molecular Biology. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Collins, Sean R., Patrick Kemmeren, et al. "Toward a Comprehensive Atlas of the Physical Interactome of Saccharomyces Cerevisiae." _Molecular & Cellular Proteomics_ 6, no. 3 (2007): 439-50.

True positives = interactions between proteins that occur in a complex annotated in a humancurated database (MIPS or SGD).

True negatives =  proteins pairs that

1. are annotated to belong to distinct complexes

2. have different sub-cellular locations OR anticorrelated mRNA expression

Compute using highconfidence negatives FP/(TN+FP)

ROC curve

Collins et al. Mol. Cell. Proteomics 2007

67

68

---

[← ROC curve](28-roc-curve.md) · [Up: contents](index.md) · [ROC curve →](30-roc-curve.md)
