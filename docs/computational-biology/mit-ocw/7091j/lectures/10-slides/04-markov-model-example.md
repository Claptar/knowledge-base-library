---
title: Markov Model Example
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Markov Model Example

**Source:** `lectures/10-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
Genotype at the Apolipoprotein locus<br>Grandpa<br>(alleles A and a) in successive generations of<br>Simpson<br>boxed Simpson lineage forms a Markov model<br>Grandma Simpson<br>Past<br>Homer<br>Marge<br>Present<br>This is because, e.g., Bart’s genotype is<br>conditionally independent of Grandpa Simpson’s<br>genotype given Homer’s genotype:<br>P(Bart = a/a | Grandpa = A/a & Homer = a/a)<br>Future<br>= P(Bart = a/a | Homer = a/a)<br>Bart<br><!-- End of picture text -->

This is because, e.g., Bart’s genotype is conditionally independent of Grandpa Simpson’s genotype given Homer’s genotype:

Images of The Simpsons © FOX. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

12

---

[← Hidden Markov Models Hidden (HMMs)](03-hidden-markov-models-hidden-hmms.md) · [Up: contents](index.md) · [Hidden Markov Model Example →](05-hidden-markov-model-example.md)
