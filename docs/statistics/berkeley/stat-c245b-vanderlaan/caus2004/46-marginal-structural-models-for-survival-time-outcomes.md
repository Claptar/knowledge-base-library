---
title: Marginal Structural Models for Survival Time Outcomes
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Marginal Structural Models for Survival Time Outcomes

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For Reference, see Mark and Jamie’s book, section 6.4.

Let La¯1(t) = (Ya¯1(t), Wa¯1(t)), indexed by treatment ¯a1, where La¯1(t) = La¯1(min(t, Ta¯1)). Let Ya¯1 = I(Ta¯1 ≤ t), where Ta¯1 is a treatment-specific survival time. Note: we treat time as discrete here, so t = 0, 1, ... However, we have censoring, so that for some individuals we do not observe their survival time. Let A2(t) = I(C ≤ t), where C = ∞ if TA¯1<sup><C.(NotewemakethisconventionsothatCisalwaysob-</sup> served, even if an individual is not censored.). We can define the full data in terms of action-specific processes indexed by treatment and censoring actions: La¯1,a¯2 (t) = La¯1 (min(t, c(¯a2))) where c(¯a2) is the time at which a2 jumps from zero to one. Let A(t) = (A1(min(t, C, T )), A2(t)). We can then write the Full data as: X = (La¯ : ¯a ∈A).

**Temporal Ordering assumption:** We assume La¯1 (t) = La¯1(t−1)(t)

**Consistency Assumption:** The observed data can be written chronologically as: (L(0), A(0), L(1), A(1), ..., L(min(T − 1), C), A(min(T − 1), C), L(min(T, C))). Under the consistency assumption, we can write the observed data as: O = ( A, L<sup>¯</sup> A¯<sup>) ∼P</sup> FX ,g(¯a|X)<sup>whereg(¯a|X) = P( ¯A = ¯a|X)</sup>

**Sequential Randomization Assumption:** We assume the SRA on the action process A(t) = (A1(min(t, C)), A2(t)) :


Note that the last equality represents factorization of the action mechanism, into the first component (treatment) and the second (censoring). To shorten our notation, let (A2(t), A<sup>¯</sup> (t − 1), L<sup>¯</sup> (t)) = F1(t) and let ( A<sup>¯</sup> (t − 1), L<sup>¯</sup> (t)) = F2(t). **Parameter of interest:** In this case the full data consist of counterfactual treatment-specific survival times under possible treatment regimes. We might be interested in, e.g., the treatment specific hazard. Recall that Ya¯1(t) = I(Ta¯1 ≤ t). So we might be interested in:


Note that the hazard is a specific case of the intensity of a counting process, in which we are interested in the expectation of a jump in a counting process (dN (t)) given a past. While a survival function can only jump once, we can imagine many counting processes which could jump mulitple times (eg number of hospitalizations, etc...).

**Estimation:** Recall that the density of the observed data can be factorized as:


The first term of this factorization gives us the G-comp formula. If we wished to use a likelihood-based estimation approach, we could evaluate this expression at C > j and A<sup>¯</sup> 1 equal to the treatment of interest to get La¯1,a¯2=0.

**Estimating Function Approach:** Alternatively, we can use the estimating function-based approach. We begin by asking what is the class of estimating functions for the type of model that defines our parameter

38

of interest (in this case an intensity model) in the full data world? <u>General Result:</u> Say we are interested in

E(dN (t)|F(t)) = Y (t)P (dN (t) = 1|F(t), Y (t) = 1), where

- F(t) is the past, including the past of the counting process N<sup>¯</sup> (t − 1),

- Y (t) = I(N (t)at risk of jumping at time t), and

- P (dN (t) = 1|F(t), Y (t) = 1) is either a probability (if time is discrete) or an intensity (if time is continuous)

E(dN (t)|F(t)) can be modelled accordingly, as, e.g. Y (t)m(t, F(t)|β). Then,

(21) TNUIS<sup>⊥= h(t, F(t))(dN(t) −Y (t)m(t, F(t)|β))</sup>

for each time point t

However, we are interested in the intersection of these models over all time points, so the nuisance tangent space is just the sum over time points of the tangent space for each time point:

(22) TNUIS<sup>⊥=</sup> � h(t, F(t))(dN (t) − E(dN (t)|F(t)) t Because when Y (t) goes to zero, E(dN (t)|F(t)) = 0, (22) can also be written as: (23) � Y (t)h(t, F(t))(dN (t) − E(dN (t)|F(t))) t

The equivalent for continuous time is:

(24)


where dM (t) is the martingale for dN (t) − E(dN (t)|F(t))

Result applied to our <u>parameter</u> of interest: So, the class of all estimating functions for any given (fixed) a¯1 is:


where we can replace F(t) with V because we know Y (t − 1) = 0. However, our MSM is really an intersection over all a¯1 ∈A1, so


A standard choice of h would be


Class of estimating functions for our <u>parameter</u> of interest using observed data: We are interested in treatment specific survival times in the absence of censoring. So we can write our MSM as:

(28) E(dYa¯1,0(t)|Y<sup>¯</sup> a¯1,0(t − 1), V ) = I(Ya¯1,0(t − 1) = 0)P (Ta¯1,0 = t|Ta¯1,0 ≥ t, V )

In addition, because we are only interested in our outcomes in the absence of censoring we are only looking at the censoring mechanism where a¯2 = 0 We can now write our Inverse Probability of Action Weighted estimating function for this MSM as a function of the observed data:


where we note that I( A<sup>¯</sup> 2 = 0) = I(C > T ) and we note that I(T = t) − I(T ≥ t)m( A<sup>¯</sup> 1(t − 1), t, V |β) is a martingale (in other words, the change in a counting process minus the expectation of a change given the past: dY (t) − E(dY (t)|past).

We now have a class of estimating functions that is indeed a function of the observed data. If we take the conditional expectation of this class of estimating functions given the full data, we get back the class of

39

estimating functions for the full data.

In (29) we only use those individuals who are not censored (A<sup>¯</sup> 2 = 0 throughout). Alternatively, we can write the IPAW estimating function as:


where now each individual get a weight for every time point until they are censored (so we use subjects even if they are censored before time T).

∂∂β<sup>(m( ¯</sup> A(t−1),t,V )) If we make our standard choice h<sup>∗</sup> = g( A<sup>¯</sup> 1(t − 1), A<sup>¯</sup> 2(t) = 0|V ) m(1−m) , we can estimate our parameter of interest using standard logistic regression of the binary outcome of death or not at each time point on our model, with each subject contributing one weighted line of data for each time point until being censored. Using the above choice of h<sup>∗</sup> , the weights are equal to:

---

[← MSMs with Missing Data in Point Treatment](45-msms-with-missing-data-in-point-treatment.md) · [Up: contents](index.md) · [Caus2004 Part 47 — →](47-caus2004-part-47.md)
