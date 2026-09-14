---
title: 'Estimation Road Map: Generating candidate estimators'
source: https://vanderlaan-lab.org/teach-files/dsaslides.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/dsaslides.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Estimation Road Map: Generating candidate estimators

**Source:** [`dsaslides.pdf`](https://vanderlaan-lab.org/teach-files/dsaslides.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- The minimum empirical risk estimator

argminψ∈Ψ L(o, ψ | υn)dPn(o) �

typically suffers from the curse of dimensionality due to the size of Ψ. A general approach is to construct a sequence or collection of subspaces approximating the whole parameter space Ψ, a so called sieve , and select the actual subspace whose corresponding minimum empirical risk estimator minimizes an appropriately penalized empirical risk or a cross-validated empirical risk.

Nov. 8, 2004

7

## ▶ Let {Ψk} be a sieve and Ψk ⊂ Ψ, define


where φj is a tensor product of basis functions. Choose univariate function ek(W ) = W<sup>k</sup> as the basis function, I is a vector which represents for a polynomial.

Given a vector⃗p = (p1, . . . , pd) ∈ N<sup>d</sup> , the tensor product identified by⃗p is:


Nov. 8, 2004

8

- Define a collection of subspaces as Ψs ⊂ Ψ, indexed by an s. Such subspaces are obtained by restricting the subsets I of basis functions to be contained in Is ⊂I, and/or restricting the values for the corresponding coefficients (β⃗p :⃗p ∈ I) to be contained in BI,s ⊂ BI : Ψs = {ψI,β : I ∈Is ⊂I, β ∈ BI,s ⊂ BI }.

Nov. 8, 2004

9

- For each s, compute (or approximate as best as one can) the minimizer of the empirical risk over the subspace Ψs:

      - L(o, ψ | υn)dPn(o).

      - ˆΨs(Pn) ≡ argminψ∈Ψs �

   - Step 1. Given each possible subset I ∈Is of basis functions, compute the corresponding minimum risk estimator of β: β(Pn | I, s) ≡ argminβ∈BI,s L �o, ψI,β | υn� dPn(o); �

For each I, this results in an estimator ψI,s,n = Ψ<sup>ˆ</sup> I,s(Pn) ≡ ψI,β(Pn|I,s).

- Step 2. Minimize the empirical risk over all allowed subsets I ∈Is of basis functions. Specifically, one needs to minimize the function fE : Is → R defined by


Nov. 8, 2004

10

Estimation Road Map: Selection among candidate estimators: cross-validation

- Select s with cross-validation

Cross-validation : the observations in the training set (P<sup>0</sup> ) are used to estimate the parameters and the observations in the validation set (P<sup>1</sup> ) are used to access performance of the estimators. The cross-validation selector is the chosen to have the best performance on the validation sets.

Given an estimator Υ<sup>ˆ</sup> of the nuisance parameter υ0, the cross-validation selector of s is now defined as follows: Sˆ(Pn) ≡ argminsEBn L(o, Ψ<sup>ˆ</sup> s(Pn,B<sup>0</sup> n<sup>) |ˆΥ(P</sup> n,B<sup>0</sup> n<sup>))dP</sup> n,B<sup>1</sup> n<sup>(o).</sup> �

Nov. 8, 2004

11

---

[← Estimation Road Map: Choices of loss function](03-estimation-road-map-choices-of-loss-function.md) · [Up: contents](index.md) · [Estimation Road Map: D/S/A algorithm for computing the optimal index set →](05-estimation-road-map-d-s-a-algorithm-for-computing-the-optima.md)
