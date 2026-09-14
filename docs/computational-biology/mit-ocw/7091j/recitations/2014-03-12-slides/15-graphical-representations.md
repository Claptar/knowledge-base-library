---
title: Graphical Representations
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-12-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Graphical Representations

**Source:** `recitations/2014-03-12-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- can be represented graphically by drawing circles for states, and arrows to indicate transitions between states

Given that we're currently in a CpG island, what is the probability that the next two states are CpG island (I) and not island (G), respectively?


<!-- Start of picture text -->
0.05<br>0.95  0.99<br>CpG island  not island<br>0.01<br>markov property<br>0.7  0.1  0.2<br>sunny  rainy<br>0.4<br>0.4  0.3<br>foggy<br>0.2  0.4<br>17<br>0.3<br><!-- End of picture text -->


If it's currently rainy, what's the probability that it will be rainy 2 days from now?

Need to sum the probabilities over the 3 possible paths RRR, RSR, RFR:

---

[← Graphical Representations](14-graphical-representations.md) · [Up: contents](index.md) · [HMMs continued →](16-hmms-continued.md)
