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


<!-- Start of picture text -->
0.05<br>0.95  0.99<br>CpG island  not island<br>0.01<br>0.7  0.1  0.2<br>sunny  rainy<br>0.4<br>0.4  0.3<br>foggy<br>0.2  0.4<br>16<br>0.3<br><!-- End of picture text -->

arrow weights indicate probability of that transition

each hidden state "emits" an observable variable whose distribution depends on the state – what can we actually observe from the CpG island model?

we observe the bases A, T, G, C, where observing a G or C is more likely in a CpG island

what might we observe to infer the state in this "weather" model? (pretend you can't see the weather because you're toiling away in a basement lab with no windows)

we could use whether or not people brought their umbrellas to lab

---

[← Hidden Markov Models](13-hidden-markov-models.md) · [Up: contents](index.md) · [Graphical Representations →](15-graphical-representations.md)
