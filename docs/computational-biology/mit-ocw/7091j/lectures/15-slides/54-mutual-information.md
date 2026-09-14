---
title: Mutual Information
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Mutual Information

**Source:** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Does knowing variable X reduce the uncertainty in variable Y?

• Example: – P(Rain) depends on P(Clouds) – P(target expressed) depends on P(TF expressed) − = _H x_ + _I x_ , _y_ ( ) _H_ ( _y_ ) _H_ ( _x_ , _y_ ) ( )

• I(x,y) = 0 means variables are independent

- Reveals non-linear relationships that are missed by correlation.

122

## Mutual information detects non-linear relationships Incoherent feed-forward loop (FFL)


<!-- Start of picture text -->
A<br>C<br>B<br><!-- End of picture text -->

Mutual information = 1.7343

Correlation coefficient = -0.0464

No correlation, but knowing A reduces the uncertainty in the distribution of B

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

123

## Mutual information detects non-linear relationships

• Complex regulatory network structure => complex relationships between protein levels


- Example: incoherent feed-forward loop (FFL)

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

124

---

[← Outline](53-outline.md) · [Up: contents](index.md) · [ARACNe →](55-aracne.md)
