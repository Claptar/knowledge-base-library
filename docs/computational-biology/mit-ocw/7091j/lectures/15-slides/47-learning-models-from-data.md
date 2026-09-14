---
title: Learning Models from Data
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Learning Models from Data

**Source:** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Searching for the BN structure:  NP-complete

   - Too many possible structures to evaluate all of them, even for very small networks.

   - Many algorithms have been proposed

   - Incorporated some prior knowledge can reduce the search space.

      - Which nodes should regulate transcription?

      - Which should cause changes in phosphorylation?

   - Intervention experiments help

111


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Sachs, Karen, Omar Perez, et al. "Causal Protein-signaling Networks Derived From Multiparameter Single-cell Data." _Science_ 308, no. 5721 (2005): 523-9.

• Without interventions, all we can say is that X and Y are correlated

• Interventions allow us to determine which is the parent.

**K.  Sachs et al.,  Science  308, 523 -529 (2005)**

112

**Fig. 1. Bayesian network modeling with single-cell data**

If we don’t measure “Y” can we still model the data? The relationship of X and Z,W will be noisy and might be missed.


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Sachs, Karen, Omar Perez, et al. "Causal Protein-signaling Networks Derived From Multiparameter Single-cell Data." _Science_ 308, no. 5721 (2005): 523-9.

**K.  Sachs et al.,  Science  308, 523 -529 (2005)**

113

---

[← Application to Gene Networks](46-application-to-gene-networks.md) · [Up: contents](index.md) · [Outline →](48-outline.md)
