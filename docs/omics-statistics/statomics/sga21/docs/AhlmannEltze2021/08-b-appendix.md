---
title: B Appendix
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/AhlmannEltze2021.pdf
source_file: sources/statomics-sga21/docs/AhlmannEltze2021.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# B Appendix

**Source:** [`docs/AhlmannEltze2021.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/AhlmannEltze2021.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

and thus for large _y_


### **B.1 Variation of log fold changes and the coefficient of variation**

The coefficient of variation for a random variable _Xi_ is defined as

The linear scaling _b_ and the offset _a_ do not in- <u>�Var [</u> _Xi_ <u>]</u> _c_ v = _._ (6) fluence the variance stabilization; the important E[ _Xi_ ] insight is that the pseudo-count _c_ = 41 _α_<sup>ensures</sup> of a log fold change for two indethat the shifted logarithm is most similar to the variables is variance-stabilizing transformation derived using the delta method.

The variance of a log fold change for two independent random variables is


### **B.3 Delta method based variancestabilizing transformation and size factors**

We can use the delta method to approximate


The derivative of log( _x_ ) is

Suppl. Fig. S2 shows that delta method-based variance-stabilizing transformations struggle to incorporate varying size factors.


To incorporate cell-specific size factors in the delta method-based variance stabilizing transformation approach, the counts _Kij_ are divided by the size factor _sj_ before applying the transformation: _g_ ( _Kij/sj_ ) (Love et al., 2014). To see the implications of this, it is helpful to look at a decomposition of the variance of a Gamma-Poisson random variable _K_ :

We can now plug Eq. (8) and (9) into Eq. (7) and find that


This expression shows that the log fold changes decrease with the mean, as long as the coefficient of variation _c_ v decreases with the mean.


### **B.2 Approximating the acosh transformation with the shifted logarithm**

In the context of RNA-seq count data, the Poisson level of this hierarchical model represents the technical sampling noise and _Q_ models additional variation. According to the law of total variation

The inverse hyperbolic cosine transformation from Eq. (1) is defined as


where Var[ _K|Q_ ] = _µ_ and Var[ _Q_ ] = _αµ_<sup>2</sup> .

We want to approximate this transformation using the shifted logarithm and thus find _a_ , _b_ , and _c_ in

If we apply the same approach to a model with size factors


so that _h_ ( _y_ ) _≈ g_ ( _y_ ).

we find that

To find _a_ , _b_ , and _c_ , so that for large _y_ , _h_ ( _y_ ) converges as quickly as possible to _g_ ( _y_ ), we notice that


16

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.

where _µ_ = _sµ_<sup>_′_</sup> .

If, however, we want to apply the delta methodbased variance-stabilizing transformation to a size factor standardized count


we find that


The difference between the final line of Eq. (18) and Eq. (20) explains the problem observed when applying the delta method-based variancestabilizing transformation to correct data where the size factors vary a lot between cells.

17

bioRxiv preprint doi: https://doi.org/10.1101/2021.06.24.449781; this version posted June 25, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-ND 4.0 International license.

---

[← A Supplementary Figures](07-a-supplementary-figures.md) · [Up: contents](index.md) · [C Data Availability →](09-c-data-availability.md)
