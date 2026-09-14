---
title: de Bruijn graph post-processing
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-26-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# de Bruijn graph post-processing

**Source:** `recitations/2014-02-26-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• Before traversing the graph:

- Simplify chains


<!-- Start of picture text -->
• Collapse two nodes (or sets of nodes), one with only 1 outgoing<br>arrow and the other with only 1 incoming arrow, into one longer<br>CCG  TCC<br>node<br>CGA  CTC<br>AAG  AGA  GAC  ACT  CTT  TTT<br>GGA  CTG<br>GGG  TGG<br>CTCCGA&<br>CCGA& CTCC&<br>AAGA& GACT& CTTT& AAGA& GACT& CTTT&<br>GGGA& CTGG&<br>CTGGGA&<br>Figure&adapted&from&presentaQon&by&Michael&Schatz&<br><!-- End of picture text -->

---

[← de Bruijn graph post-processing](15-de-bruijn-graph-post-processing.md) · [Up: contents](index.md) · [de Bruijn graph post-processing →](17-de-bruijn-graph-post-processing.md)
