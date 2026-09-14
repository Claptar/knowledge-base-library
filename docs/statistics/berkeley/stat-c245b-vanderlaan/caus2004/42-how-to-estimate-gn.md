---
title: How to estimate gn
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# How to estimate gn

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Maximum likelihood, based on a model for the treatment:

gn = argmaxθ �ni=1 �Kj=1<sup>gθ(Ai(j)| ¯Ai(j −1), ¯Li(j)), gn≡gθ</sup> n<sup>For example, we could use a logistic regression</sup> model of A(j) given past covariates and treatment. We could assume a single model for all time points and just run a logistic regression on the pooled data set, with each subject contributing k lines of data. Alternatively, we could assume a single model for some subset of time points, or have a separate model for each time point. You should just pool those time-points where a common model makes sense. For example, it may not make sense to model A(0) with all the rest of the time points, since at baseline, treatment can’t depend on previous measured covariates. Estimate gn as non-parametrically as possible, using crossvalidation. The more non-parametrically you estimate gn, the more asymptotically efficient your estimator will be.

---

[← How to Implement](41-how-to-implement.md) · [Up: contents](index.md) · [11/17/2004 Notes →](43-11-17-2004-notes.md)
