---
title: (2) Consistency assumption (CA)
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# (2) Consistency assumption (CA)

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let A denote the collection of all possible treatment regimes. Then there exists, for each subject, a collection of treatment-specific processes X<sup>F ull</sup> = {X<sup>¯</sup> a¯ : ¯a ∈A}. The observed data for a given subject simply consist of that element of X<sup>F ull</sup> that corresponds to the treatment regime assigned to the subject: O = ( A,<sup>¯</sup> X<sup>¯</sup> ¯A<sup>).</sup> This assumption allows us to view causal inference as a missing-data problem: If we had access to X<sup>F ull</sup> for each subject, inference about causal parameters would be straightforward; the difficulties arise because we only observe one element of X<sup>F ull</sup> for each subject.

Example 1: Consider the case of a binary point treatment at baseline A ∈{0, 1}, an outcome Y , and no other covariates. Then we assume that for each subject there exist Y0 and Y1, the outcomes we would observe if the treatment were 0 or 1, respectively. Thus X<sup>F ull</sup> = {Y0, Y1}. Depending on which treatment we observe for a given subject, we only have access to either Y0 or Y1.

This allows us to parameterize the data-generating distribution as


where F0 is the distribution of X<sup>F ull</sup> and g0(·|X<sup>F ull</sup> ) is the conditional distribution of A<sup>¯</sup> given X<sup>F ull</sup> . In order to simulate such data for one subject in R, we could thus first generate a realization of X<sup>F ull</sup> , then a realization of the treatment process A<sup>¯</sup> , and finally pick that file Xa¯ that corresponds to the specific treatment process a¯ we generated.

In example 1, we would do the following for each subject: We generate both Y0 and Y1, then the treatment assignment a, and then we pick Ya.

<u>Claim:</u> If the treatment assignment in example 1 is at random, i.e. independent of X<sup>F ull</sup> = (Y0, Y1), then the expectation of Y among subjects who actually received a given treatment a in your study equals the

6

expectation of Y among all subjects if everybody had received treatment a: E[Y |A = a] = E[Ya]. This is very useful since we would like to make statements about the dependence of E[Ya] on a, but only have access to E[Y |A = a].

<u>Proof:</u> E[Y |A = a] = E[YA|A = a] = E[Ya|A = a] = E[Ya]

where the first equality follows from the consistency assumption, and the third equality follows from the independence assumption A ⊥ (Y0, Y1).

Example 2: Suppose in example 1 we also measured a baseline covariate W , and we knew that treatment assignment is only based on W , i.e. , conditional on W , treatment assignment is independent of X<sup>F ull</sup> : A ⊥ (Y0, Y1)|W . Then we have


In this case, we can thus make statements about causal effects of A on Y within strata of W . This corresponds to the usual case of adjusting for a baseline covariate by using multiple regression.

---

[← (1) Temporal ordering assumption (TA)](10-1-temporal-ordering-assumption-ta.md) · [Up: contents](index.md) · [(3) Sequential randomization assumption (SRA) →](12-3-sequential-randomization-assumption-sra.md)
