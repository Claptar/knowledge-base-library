---
title: How to Implement
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# How to Implement

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

h<sup>∗</sup> ( A, V<sup>¯</sup> ) = g( A<sup>¯</sup> |V ) ∂β<sup><u>∂</u>m( ¯A, V |β)isagoodchoiceofh( ¯A, V )forlinearregression.</sup>


These choices of h( A, V<sup>¯</sup> ) correspond to the weighted regressions performed by standard software. The solution βn,IP T W of 0 =<sup>�n</sup> i=1<sup>Dh(Oi|gn, β)equals</sup> βn,IP T W = argminβ �ni=1<sup>(Yi−m( ¯Ai, Vi|β))2</sup> gn( A<sup><u>¯</u></sup> ig|nX(iA<sup>¯</sup> )iσ|<sup>2</sup> V( iA)<sup><u>¯</u></sup> i,Vi)<sup>orinotherwords,thesolutiontoordinary</sup> 36

weighted least squares. So we can implement this estimator using standard software and supplying a n- dimensional vector of weights, with the weight for each subject equal to wi =<sup><u>gn(</u></sup> A<sup>¯</sup> i|Vi) gn(A<sup><u>¯</u></sup> i|Xi) Note: The ETA makes this a dangerous estimator. At the very least, we must inspect the ETA (via the bootstrap technique presented in an earlier lecture). If there is enough experimentation in our data that we can estimate our parameter of interest without extrapolation, then this is a good estimator. In contrast, even if the ETA is violated, the DR-IPTW estimator will extrapolate to sparse areas of your data as well as MLE.

---

[← IPTW Estimating Function](40-iptw-estimating-function.md) · [Up: contents](index.md) · [How to estimate gn →](42-how-to-estimate-gn.md)
