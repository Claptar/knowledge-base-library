---
title: Lecture 2.
source: https://www.stat.berkeley.edu/~aldous/205B/kernel.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/kernel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 2.

**Source:** [`kernel.pdf`](https://www.stat.berkeley.edu/~aldous/205B/kernel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Want to formalize the idea “conditional distribution of X2 given X1 = s1. We could write


What sort of object is Q?

Measure-theory set-up. (S1, S1) and (S2, S2) are measure spaces, and (S1 × S2, S1 ×S2) is their product space. A kernel <u>Q</u> from S1 to S2 is a map Q : S1 × S2 → R such that

(a) B → Q(s1, B) is a p.m. on (S2, S2) for each fixed s1 ∈ S1

(b) s1 → Q(s1, B) is a measurable function S1 → R for each fixed B ∈S2. If S1 and S2 are countable then kernels correspond to stochastic <u>matrices.</u> In undergraduate course, continuous r.v.’s (X, Y ) have a joint density f (x, y), a marginal density f (x) for X, and a conditional density f (y|x) for Y given X = x: these are related by


**Proposition 5** Given a p.m. µ on S1 × S2, a p.m. µ1 on S1 and a kernel Q from S1 to S2, the following are equivalent.


where Ds1 = {s2 : (s1, s2) ∈ D}.


for all measurable h : S1×S2 → R for which either h ≥ 0 or h is µ-integrable. Note: part of assertion of (2,3) is that integrands are measurable.

Jargon: I call Q the conditional <u>probability</u> kernel for µ, but this isn’t standard.

**Lemma 6** For each D ∈S1 × S2

(i) Ds1 ∈S2 for all s1 ∈ S1

(ii) the map s1 → Q(s1, Ds1) is measurable.

3

Proof. Apply π − λ theorem (1.4.2) to class D of sets D for which assertions are true.

Proof of Proposition 5. (1) → (2). Lemma 6 says (2) is meaningful: consider class of D’s where it is true. True for D = A×B by (1). Apply π−λ theorem. (2) → (3). Conclusion is meaningful and true for h = 1D, and hence for simple h. General h ≥ 0 is increasing limit of simple hn defined by


so by monotone convergence, result holds for h ≥ 0. For general h write h = h<sup>+</sup> − h<sup>−</sup> .

**Theorem 7** [easy part] Let µ1 be a p.m. on S1 and let Q be a kernel from S1 to S2. Then there exists a unique p.m. µ on S1 × S2 such that the relations of Proposition 5 hold.

Conversely, let µ be a p.m. on S1 ×S2. Define µ1 by: µ1(A) = µ(A×S2). Then [hard part: 4.1.6] provided S2 is nice, there exists a kernel Q from S1 to S2 such that the relations of Proposition 5 hold.

Proof. [easy part] Use (2) to define µ(D): this makes sense because of Lemma 6. Need to verify µ is a p.m. Issue is countable additivity. If D<sup>n</sup> ↑ D then Ds<sup>n</sup> 1<sup>↑Ds</sup> 1<sup>,soQ(s1, D</sup> s<sup>n</sup> 1<sup>) ↑Q(s1, Ds</sup> 1<sup>),soµ(Dn) ↑µ(D).</sup>

[hard part] As with Lemma 2 we can reduce to the case S2 = R. Write S1 = S. Let r denote a <u>rational.</u> We shall use easy analysis fact. Let F (r) be a real-valued function defined on the rationals and such that


Then F extends to a distribution function, by setting


For each r let νr be the (sub-probability) measure on S defined by


So νr(A) ≤ µ1(A). Let F (s, r) be the Radon-Nikodym density of νr with respect to µ1. That is to say


4


We now modify F on µ1-null sets so that, for each s, the maps r → F (s, r) will satisfy (4 - 6). For r1 < r2,


and so the integrand is a.e. non-negative. Modify to make it everywhere non-negative. Similarly, consider rn ↓ r. Then µ(A × (r, rn]) ↓ 0 and so F (s, rn) ↓ F (s, r) µ1-a.e., and the null set depends only on r. So we can modify to make F (s, ·) right-continuous on rationals, for all s. Finally, easy to modify to get


So by analysis fact, F (s, ·) extends to a distribution function. Define Q(s, ·) to be the p.m. whose distribution function is F (s, ·). To finish the proof, we must show: for each B ⊂ R


By construction these hold for B = (−∞, r]. Apply the π − λ theorem.

5

---

[← Radon-Nikodym densities.](02-radon-nikodym-densities.md) · [Up: contents](index.md) · [Lecture 3. →](04-lecture-3.md)
