---
title: Lecture 3.
source: https://www.stat.berkeley.edu/~aldous/205A/notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 3.

**Source:** [`notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Topics: Uses of Fubini’s theorem, Kolmogorov extension theorem.

Given p.m.’s µ1 on S1 and µ2 on S2 we can define the <u>product</u> measure µ = µ1 × µ2 on S1 × S2, which has properties (7 - 9) below. These properties follow from Theorem 7, putting Q(s1, ·) = µ2(·).


For measurable h : S1 × S2 → R with either h ≥ 0 or h is µ-integrable,


The final equalities are <u>Fubini’s Theorem.</u> These results also hold for σ- finite measures. See Appendix 6 for examples illustrating the necessity of the hypotheses. Here are some more “practical” examples. Here X, Y denote real-valued r.v.’s with distributions µ, ν, and λ is Lebesgue measure on the line.


Proof. Apply Fubini’s theorem to the set D = {(x, t) : x ≥ t} ⊂ [0, ∞) × [0, ∞) and the product measure µ × λ.

Example. Parseval’s identity. Let X have characteristic function φ(t) = E exp(itX) and Y have characteristic function φ<sup>ˆ</sup> (t). Then � φ(t)ν(dt) = � φˆ(t)µ(dt).

Proof. Compute E exp(iXY ).

Example. Suppose X and Y are independent, and set S = X + Y . In undergraduate course we see the convolution formula for densities:


which assumes densities fY and fX exist. A completely general version can be stated in terms of distribution functions as


6

In the case where Y does have a density fY


Example. <u>Conditional densities.</u> We used these to motivate kernels; now we can prove the following. Suppose (X, Y ) has joint density f (x, y). Define f (y|x) = f (x, y)/fX(x) where fX (x) > 0. Define Q(x, ·) to be the distribution with density f (·|x). Then Q is the conditional probability kernel for Y given X.

Proof. Use Fubini’s theorem to verify (1):


I will give the “probabilistic” proof of the (countable) Kolmogorov extension theorem. Appendix 7 gives the measure theory proof. Some texts give a version for uncountable families, but this has no practical use.

We start with a “random variable” version of Theorem 7.

**Corollary 8** Let (X, U ) be independent r.v.’s such that U is uniform on [0, 1], and X takes values in S and has distribution µ1. Let µ be a p.m. on S × R with marginal µ1. Then there exists measurable f : S × [0, 1] → R such that


Proof. Let Q be the conditional probability kernel from S to R associated with µ (Theorem 7). For each x ∈ S let f (x, ·) be the inverse distribution function for the p.m. Q(x, ·). Lemma 1 says f (x, U ) has distribution Q(x, ·). In terms of measures, this is:


We have to verify: for A ⊂ S, B ⊂ R


Easy.

7

**Theorem 9 (Kolmogorov extension)** Let (µn; 1 ≤ n < ∞) be p.m.’s on R<sup>n</sup> . Suppose they are <u>consistent</u> in the following sense. For each n, regard µn+1 as a measure on R<sup>n</sup> × R: then the marginal of µn+1 is µn. Then there exists a unique p.m. µ∞ on R<sup>∞</sup> such that, writing R<sup>∞</sup> = R<sup>n</sup> × R<sup>∞</sup> , the marginal of µ∞ is µn.

Proof. Let (U1, U2, . . .) be independent U (0, 1), which exist by Corollary 4. Define X1 = Fµ<sup>−</sup> 1<sup>1(U1).</sup> Inductively, suppose we have defined **X** n = (X1, . . . , Xn) as a measurable function of (U1, . . . , Un) so that dist( **X** n) = µn. We shall define **X** n+1 as a measurable function of ( **X** n, Un+1). Then the induction goes through, and we can define a infinite sequence of r.v.’s (Xn; 1 ≤ n < ∞). Clearly µ∞ = dist(Xn; 1 ≤ n < ∞) satisfies the conclusion of the Theorem.

To do the inductive step, just apply Corollary 8 with X = **X** n, U = Un+1 and µ = µn+1 regarded as a measure on R<sup>n</sup> × R.

---

[← Lecture 2.](03-lecture-2.md) · [Up: contents](index.md) · [Lecture 4. →](05-lecture-4.md)
