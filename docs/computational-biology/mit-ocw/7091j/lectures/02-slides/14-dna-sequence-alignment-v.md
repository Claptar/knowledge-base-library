---
title: DNA Sequence Alignment V
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# DNA Sequence Alignment V

**Source:** `lectures/02-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Figuring out how to choose the mismatch penalty … “Target frequencies”* : qij = pipje<sup>λ</sup> s<sup>ij</sup> ⇒ sij  =  ln(qij / pipj )/λ qij are nt pair frequencies expected in high-scoring matches If you want to find regions with R% identities: r   = R /100      qii = r/4      qij = (1-r)/12  (i≠j)     Set sii = 1 Then   m = sij = sij/sii = (ln(qij / pipj )/λ) / (ln(qii / pipi )/λ) (i≠j)

⇒ <mark>m =</mark> ln(4(1-r)/3)/ln(4r)

(Assuming all pi, pj = 1/4, 1/4 < r < 1)

*Karlin & Altschul, 1990

24

---

[← DNA Sequence Alignment IV](13-dna-sequence-alignment-iv.md) · [Up: contents](index.md) · [DNA Sequence Alignment VI →](15-dna-sequence-alignment-vi.md)
