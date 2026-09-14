---
title: IPTW Estimating Function
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# IPTW Estimating Function

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Dh,IP T W (O|g0, β0) = g<sup>h</sup> (<sup><u>(</u></sup> A<sup>¯</sup> A<sup><u>¯</u></sup> |,XV <u>))</u><sup>(Y</sup> A<sup>¯−m( ¯A, V |β0))</sup> <u>Result:</u> If


then, E[Dh,IP T W (O|g0, β0)|X] =<sup>�</sup> a¯<sup>h(¯a, V )(Ya¯−m(¯a, V |β0))(inotherwords,bytakingtheexpectation</sup> conditional on the full data, we get back the full data estimating function), and E[Dh,IP T W (O|g0, β0)] = 0 (in other words, the IPTW estimating function is unbiased at the true data generating distribution). **Proof:**


(17)

Note: (16) is a specific version of the ETA assumption. More generally, the ETA assumption states that any possible treatment at each time point, given past treatment and covariate history, needs to have a positive probability of occurring.

Side Note: Choice of an estimator (IPTW, DR-IPTW or G-comp) must depend on the problem at hand. For example, if you have a very high-dimensional treatment or treatment mechanism, the IPTW and DR-IPTW may not give you any extra-robustness (due to misspecification of the treatment mechanism). In this case, you may in fact be better off with the MLE-based G-comp estimator (but remember, this is different from the standard MLE approach in that you integrate out those covariates which are not part of your parameter of interest).

---

[← Estimation using censored data: General Approach](39-estimation-using-censored-data-general-approach.md) · [Up: contents](index.md) · [How to Implement →](41-how-to-implement.md)
