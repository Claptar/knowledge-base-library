---
title: EM algorithm
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# EM algorithm

**Source:** `recitations/2014-03-05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Expectation-Maximization (EM) algorithm with component elimination**


<!-- Start of picture text -->
E step M step<br>z = m = π m p ( rn | m ) ( i )  = Nm<br>γ( n ) M π ' r m πˆ  m ∑ mM '=1  Nm '<br>m p ( n | )'<br>∑<br>m '=1 N<br>Nm = ∑ n =1 γ( zn = m )<br>γ (zn=m) :  the fraction of read  Nmm  : the effective number of<br>n  assigned to event  m reads assigned to event<br><!-- End of picture text -->

**_Nmm_ : the effective number of reads assigned to event** **_m_**

###### **E (Expectation) step:**

- Calculate the expected value of the likelihood of the observed reads. We must assign reads to binding events in order to do this.

###### **M (Maximization) step:**

Choose values of the parameters (π, the locations of the binding events) that maximize the likelihood of the observed reads – these formulas give the values of those parameters.

1 Initialize the binding events to be equally likely at every nucleotide (<sup>π</sup> _j_<sup>=</sup> _M_ ), then run the EM algorithm (iterate between the E and M steps – assigning reads to events and then updating the location/strength of events) until convergence

12

---

[← EM algorithm](03-em-algorithm.md) · [Up: contents](index.md) · [EM algorithm →](05-em-algorithm.md)
