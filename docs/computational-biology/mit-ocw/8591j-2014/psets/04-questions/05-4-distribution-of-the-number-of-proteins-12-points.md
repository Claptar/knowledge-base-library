---
title: 4 Distribution of the number of proteins (12 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/04-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Distribution of the number of proteins (12 points)

**Source:** `psets/04-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

a. The number of proteins per burst, _k_ , is expected to follow a geometric distribution<sup>2</sup> :


where 1 _− ρ_ corresponds to the probability that the mRNA is translated and _ρ_ corresponds to the probability that the mRNA is degraded. Let's assume that the degradation rate of mRNA is _γ_ = 1 _min_<sup>_−_1</sup> and the translation rate is _β_ = 10 _min_<sup>_−_1</sup> . \hat is the mean and the variance of the number of proteins produced from one mRNA?


_β mRNA → mRNA_ + _protein_

- b. In the following, we will derive the distribution of number of proteins produced from more than one mRNA.

> 2yu et al. Probing gene expression in live cells, one protein molecule at a time. Science (2006)

2

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 4

1. \e can approximate the geometrical distribution by the exponential distribution. Show that in the limit of _ρ «_ 1 , _P_ ( _k_ ) ≈ exp( _−ρk_ ) _ρ_ . For _ρ_ = 0 _._ 1 , what is the probability that 1, 10 and 20 proteins are produced from one mRNA according to the exact and the approximate expression?

2. From now we change the discrete variable _k_ to a continuous varialbe _x_ , such that _P_ ( _k_ ) _dk_ = _P_ ( _k_ ) ≈ _ρexp_ ( _−ρx_ ) _dx_ = _p_ ( _x_ ) _dx_ , where _dk_ = 1 . _p_ ( _x_ ) = _ρexp_ ( _−ρx_ ) is the probability density function (pdf ) of the distribution of protein numbers _x_ produced from a single mRNA molecule. The pdf of the distribution for the sum of two indel pendent variables is the convolution of their respective pdf. Thus, we can fnd the pdf for the number of proteins produced from two mRNAs by convolving two identical exl ponential distributions. The convolution ( _f ∗ g_ )( _x_ ) of two functions _f_ ( _x_ ) and _g_ ( _x_ ) is defned by


Plot the pdf of: 1) an exponentially distributed random variable; 2) the sum of two independent exponentially distributed random variables.

3. Show that the probability density function for the number of proteins produced from _m_ mRNAs follows a Gamma distribution<sup>3</sup> :


\hat is _b_ in this equation? For which protein burst size is our continous approximation good?

> 3Equation (5) in "Linking stochastic dynamics to population distribution: an analytical framework of gene expression", by Friedman, N et al. PRL (2006)

3

MIT OpenCourseWare http://ocw.mit.edu

8.591J / 7.81J / 7.32 Systems Biology Fall 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 3 Discrete probability distributions (12 points)](04-3-discrete-probability-distributions-12-points.md) · [Up: contents](index.md)
