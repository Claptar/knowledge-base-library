---
title: Sequential Randomization Assumption (SRA)
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Sequential Randomization Assumption (SRA)

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

P (A(j) = a(j)|A<sup>¯</sup> (j − 1), X) = P (A(j) = a(j)|A<sup>¯</sup> (j − 1), L<sup>¯</sup> ¯A(j−1)<sup>(j)), j=0, ..., KInotherwords,weassume</sup> that, at each time point, the probability of being assigned a specific treatment only depends on the observed past up till that time point. The distribution of the observed data can be written: O ∼ PFX0 ,g0 where g0(¯a|X) ≡ P ( A<sup>¯</sup> = a¯|X) denotes

the true treatment mechanism. We can write the treatment mechanism as g0(¯a|X) =<sup>�K</sup> j=0<sup>g0(a(j)|a¯(j −1), X)</sup> Further, under the SRA: g0(¯a|X) =<sup>�K</sup> j=0<sup>g0(a(j)|a¯(j −1), ¯La¯(j−1)(j))</sup> The density of the observed data is: P (O) =<sup>�K</sup> j=0<sup>+1P(L(j)|L¯(j −1),A¯(j −1)) �K</sup> j=0<sup>P(A(j)| ¯A(j −1), ¯L(j))</sup> Under the SRA and CA, the first term of this density can be written using the G-computation formula: �Kj=0+1<sup>P(L(j)|L¯(j −1),A¯(j −1) = P</sup> L<sup>¯</sup> a¯<sup>|</sup> a¯=A<sup>¯</sup> (K+1)<sup>(Seepreviouslecturesforthisproof.)</sup> Under the SRA, the second term of the density can be written: �Kj=0<sup>P(A(j)| ¯A(j −1), ¯L(j)) = g0( ¯A|X)</sup>

**Marginal Structural Model** We assume a model for our parameter of interest (which, recall, is a parameter of the marginal distribution of the treatment-specific counterfactual outcome): E[Ya¯|V ] = m(¯a, V |β0), where β0 refers to the true parameter (we use subscript 0 throughout to refer to the truth). For example, we might assume the following model:

m(¯a, V |β0) = β(0) + β(1)<sup>�K</sup> j=0<sup>a(j) + β(2)V+ β(3)(�K</sup> j=0<sup>a(j))V(Note:β(0)referstothefirstelementof</sup> β, β(1) to the second element, etc.) Alternatively, we might also want to include, for example, a quadratic term in our model: m(¯a, V |β0) = β(0) + β(1)<sup>�K</sup> j=0<sup>a(j) + β(2)V+ β(3)(�K</sup> j=0<sup>a(j))V+ β(4)(�k</sup> j=0<sup>a(j))2</sup> (Side Note: In choosing your model, think about both your subject matter and your objective. Do you expect your curve to be monotone? Are you interested in finding an optimum treatment? etc...)

---

[← Parameter of Interest](37-parameter-of-interest.md) · [Up: contents](index.md) · [Estimation using censored data: General Approach →](39-estimation-using-censored-data-general-approach.md)
