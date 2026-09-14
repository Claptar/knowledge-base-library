---
title: September 13, 2004 Notes
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# September 13, 2004 Notes

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This lecture deals with the G-computation formula when there is censored data. Modifications to the uncensored data formula involve minor bookkeeping, and a clever new definition of counterfactuals.

**What is the data?** Let T denote a random time of death, and C denote the time at which a patient was censored, so that the patient is followed until time min(T, C). Note that if T < C then we know the patient’s time of death, while if C < T then we only know the patient lived at least until time C. Let A1(t) denote the treatment given at time t, A2(t) = I(C ≤ t) be an indicator of whether the patient has been censored by time t, and A(t) = (A1(t), A2(t)). Let L(t) represent covariate values measured at time t, Y (t) represent an outcome process evaluated at time t, and X(t) = (L(t), Y (t)). Let X = {X(t) : t ≤ min(T, C)} and A = {A(t) : t ≤ min(T − 1, C)}. The observed data is then:

O = ((X(0), A(0)), (X(1), A(1)), ..., (X(min(T − 1, C)), A(min(T − 1, C))), X(min(T, C)) = (A, X).

**What are the assumptions?** Temporal ordering assumption: At each time point t where observations are made, X(t) is observed before A(t). This is exactly as in the uncensored case.

Consistency assumption: Assume the existence of counterfactuals X ~~a~~<sup>~~,~~whichrepresentstheprocessthat</sup> would have been observed had we set A = ~~a,~~ where a(t) = (a1(t), a2(t)). The consistency assumption states that X = X A<sup>~~,~~exactlyasintheuncensoredcase.</sup>

Sequential Randomization Assumption (SRA): If X ~~F~~ ull denotes the set of all possible counterfactuals X <u>a</u><sup>~~,~~</sup> then the SRA assumption is that g(A(t)|A(t − 1), X ~~F~~ ull) = g(A(t)|A(t − 1), X(t)). From SRA: g(A|X F ull) =<sup>�</sup> tmin(=0 T −1,C) g(A1(t)|A2(t), A(t − 1), X(t))<sup>�min(</sup> t=0<sup>T −1,C)</sup> g(A2(t)|A(t − 1), X(t)). Here the first product is called the treatment mechanism, and the second the censoring mechanism.

Experimental Treatment Assumption (ETA): Exactly as in the uncensored case, this is the assumption that g(A(t) = a(t)|A(t − 1), X(t)) > 0 for all ~~a~~ of interest.

**What would we like to know, and how can we find it?** Denote the counterfactual distribution by P (X ~~a~~<sup>~~)~~= P(</sup> X ~~a~~ 1 ~~,a~~ 2<sup>).Thenwewouldliketoknownthedistributionof</sup> X ~~a~~ 1,0<sup>,orwhatwouldhavehappened</sup> under treatment regime ~~a~~ 1 had we set C = ∞, so that there was no censoring. This trick of incorporating the censoring into the treatment variable A allows us to write our parameter of interest as part of the counterfactual distribution, and we can then treat our problem as a missing data problem.

From SRA, we can factor P (O) =<sup><u>�min(</u></sup> t=0<sup>T,C)</sup> P (X(t)|X(t − 1), A(t − 1))g(A|X ~~F~~ ull), and P (X <u>a1,a2</u><sup>) = �min(</sup> t=1<sup>T,C)</sup> P (X(t)|X(t − 1), A1(t − 1) = ~~a~~ 1(t − 1), A2(t − 1) = ~~a~~ 2(t − 1)). Thus, P (Xa1,0<sup>) = �min(</sup> t=1<sup>T,C)</sup> P (X(t)|X(t − 1), A1(t − 1) = ~~a~~ 1(t − 1), C ≥ t). To then estimate this quantity, we must fit models for each X(t)|[X(t − 1), A1(t − 1) = ~~a~~ 1(t − 1), C ≥ t], and these can be fitted from the observed data. This technique is referred to as the G-computation method for censored data.

9

**Data Reduction.** In order to fit the G-computation formula for P (X <u>a1,0</u><sup>),itisoftenhelpfulinpracticeto</sup> reduce the dimension of the covariate process L(·). There is a vast literature on dimensionality reduction, and many common methods such as PCA, factor analysis, ICA, and principal curves. Specifically, it is useful to extract L<sup>∗</sup> 1<sup>(t) and L∗</sup> 2<sup>(t) from the fits of the conditional distribution g(·|A2(t),</sup> A(t− 1), X(t)) of A1(t), and the conditional distribution g(·|A(t − 1), X(t)) of A2(t), which are predictors of A1(t) and A2(t). The suggested procedure is then to carry out the previous analysis, while replacing L(t) with L<sup>∗</sup> (t) ≡ (L1<sup>∗(t), L</sup> 2<sup>∗(t)).</sup>

---

[← The G-computation formula](14-the-g-computation-formula.md) · [Up: contents](index.md) · [Caus2004 Part 16 — →](16-caus2004-part-16.md)
