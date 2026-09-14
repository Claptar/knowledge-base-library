---
title: HMMs continued
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-12-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# HMMs continued

**Source:** `recitations/2014-03-12-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
0.2<br>0.8  0.9<br>Island ( I )  Genome ( G )<br>0.1<br><!-- End of picture text -->

### **What information do we need in order to fully specify one of these models?**


<!-- Start of picture text -->
I G<br><!-- End of picture text -->

- **(1)** _P_ 1( _S_ ) = probability of starting in a particular state _S_ (vector with dimension = # of states)


<!-- Start of picture text -->
I G<br>I<br>G<br>C G A T<br><!-- End of picture text -->

- **(2)** probability of transitioning from one state to another (square matrix w/ each dimension = # of states, usually called the transition matrix, _T_ ) **(3)** _P_ E( _X_ | _S_ ) = probability of emitting X given current state S


18

---

[← Graphical Representations](15-graphical-representations.md) · [Up: contents](index.md) · [Using HMMs as generative models →](17-using-hmms-as-generative-models.md)
