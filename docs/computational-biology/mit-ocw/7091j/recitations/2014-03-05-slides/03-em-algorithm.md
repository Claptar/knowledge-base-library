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
E step M step<br>γ( zn = m ) = M π m p ( rn | m ) πˆ  m ( i )  = MNm Reinforcing constraint that π<br>π ' r m ∑ m '=1  Nm ' must sum to 1<br>m p ( n | )'<br>∑<br>m '=1 N<br>Nm = ∑ n =1 γ( zn = m )<br><!-- End of picture text -->

- **_γ (zn=m) :_ the fraction of read** **_n_ assigned to event** **_m_**

**_Nm_ : the effective number of reads assigned to event** **_m_**

- Although _zn_ truly have _hard_ (i.e. 0/1) values – either the read did or didn’t come from a particular binding event – throughout the iterative algorithm we will allow them to take on _soft_ values - γ( _zn_ = _m_ ) - anywhere between 0 and 1, reflecting our

uncertainty as to exactly which π element the read came from

- For all binding events _m’_ , calculate the probability that a read came from a binding event (p(rn|m’)), weighted by the strength of the binding event (πm’). The probability that a read came from any particular binding event _m_ is just that event’s fraction of the total sum.

- Nm is the number of reads assigned to binding event m, where the sum is over the soft counts γ( _zn_ = _m_ )

- π<sup>(i)</sup> m<sup>: The strength of binding event</sup> _m_ in the _i_<sup>th</sup> iteration of the EM algorithm.

   - Note that the denominator sum equals _N_ , the total number of reads in the ChIP-seq data set

11

---

[← Peak-calling applications](02-peak-calling-applications.md) · [Up: contents](index.md) · [EM algorithm →](04-em-algorithm.md)
