---
title: MSMs with Missing Data in Point Treatment
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# MSMs with Missing Data in Point Treatment

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Using our common notation for point treatment studies, suppose that we are interested in modelling E[Ya|V ] where V ⊂ W , the baseline covariates. Complications arise when there is missing data. Assume that V is always observed, but that the rest of W can occasionally be missing. So for ∆= I(W is observed), O = (∆, ∆W, V, A, Y ) is the observed data. There are two ways to proceed.

**Method I.** The first method is to simply redefine the baseline covariates as W<sup>′</sup> = (W ∆, ∆, V ), and fit a marginal structural model (as in previous lectures) to the observed data model O = (W<sup>′</sup> , A, Y ). In this case, the SRA assumption becomes P (A = a|W<sup>′</sup> , (Ya : a ∈A)) = P (A = a|W<sup>′</sup> ), which is different from the traditional SRA assumption.

**Method II.** The second method is to treat the unobserved (W, A, Y ) as if it were the full data structure, and apply the general techniques of van der Laan and Robins for mapping full data estimating functions into observed data estimating functions in coarsening at random models. The coarsening at random assumption is here that P (∆= 1|X) = P (∆= 1|V, A, Y ), where X is the counterfactual process (W, (Ya : a ∈A)). When making the usual SRA assumption that P (A = a|X) = P (A = a|W ), we saw in previous lectures how to derive all estimating functions (Dh(W, A, Y ) : h) for the "full" data model (observing (W,A,Y)).

The general methodology of van der Laan tells us that under the CAR assumption P (∆= 1|X) = P (∆= 1|V, A, Y ), the class of "observed" data estimating functions is given by {Dh P (∆=1∆|A,V,Y )<sup>−Π(Dh</sup> P (∆=1∆|A,V,Y )<sup>|TCAR) :</sup> h}, where TCAR is the Hilbert space in L<sup>2</sup> 0<sup>(O)containingallscoresobtainedfromvaryingthemissing-</sup> ness mechanism. Considering one-dimensional fluctuations through P (∆= 1|V, A, Y ) gives that TCAR = {φ(∆, V, A, Y ) : E[φ|V, A, Y ] = 0, Eφ<sup>2</sup> < ∞}, and hence that Π(U (O)|TCAR) = E[U |∆, V, A, Y ]−E[U |V, A, Y ]. Therefore, the class of all estimating functions in the "observed" data model is given by,

37

{Uh(O) − E[Uh(O)|∆, V, A, Y ] + E[Uh(O)|V, A, Y ] : Uh(O) = Dh(W, A, Y ) P (∆=1∆|A,V,Y )<sup>}.Fromtheseesti-</sup> mating functions, we can proceed as usual in fitting marginal structural models. **Censored Longitudinal Data and Causality: Notes for 11/22/04**

---

[← History-adjusted MSMs](44-history-adjusted-msms.md) · [Up: contents](index.md) · [Marginal Structural Models for Survival Time Outcomes →](46-marginal-structural-models-for-survival-time-outcomes.md)
