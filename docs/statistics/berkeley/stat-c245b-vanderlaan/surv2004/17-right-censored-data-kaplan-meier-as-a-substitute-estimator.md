---
title: 'Right Censored Data: Kaplan-Meier as a substitute estimator'
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Right Censored Data: Kaplan-Meier as a substitute estimator

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We observe:


We wish to estimate:


We want to find a _φ_ s.t. if applied to the data we get back the survival function.


[Question: Is this a parameter at this point? – No – that would be true only in the Full data model. Here we have Right Censored data.]

We start with the following:


23


Now we have written the survival function in terms of the observed data. Next we plug in the empirical by defining some subdistributions.


So we have:


Survival function as _φ_ of distribution of the data.


Now our estimator is :


This is the Kaplan-Meier estimator.

For any such 2 distributions – any distribution of the data can be indexed. So the unnivariate Right-censored data model is a nonn-parametric model. Whenever a model is locally nonnparametric, any consistent estimator is asymptotically efficient.

Another estimator uses the general trick - inverse probability censored data mapping (IPCD).


24

_G_ ¯ _KM_ is Kaplan-Meier estimator based on _T_ ˜ _i,_ (1 _−_ ∆ _i_ ), _i_ = 1 _, . . . , n_ . IPCD will be discussed further next lecture.

Raul Aguilar Schall

---

[← Log Likelihood – Maximum Likelihood](16-log-likelihood-maximum-likelihood.md) · [Up: contents](index.md) · [General approach for constructing an estimator →](18-general-approach-for-constructing-an-estimator.md)
