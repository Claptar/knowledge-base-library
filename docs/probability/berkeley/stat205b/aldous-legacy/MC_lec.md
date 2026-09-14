---
title: MC lec
source: https://www.stat.berkeley.edu/~aldous/205B/MC_lec.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/MC_lec.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# MC lec

**Source:** [`MC_lec.pdf`](https://www.stat.berkeley.edu/~aldous/205B/MC_lec.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# MARKOV CHAINS

What I will talk about in class is pretty close to Durrett Chapter 5 sections 1-5. We stick to the countable state case, except where otherwise mentioned.

Lecture 7. We can regard (p(i, j)) as defining a (maybe infinite) matrix P. Then a basic fact is


where P<sup>n</sup> denotes matrix multiplication. There are two conceptually different ways to get this. First regard X0 as having some arbitrary initial distribution µ0. Write µn for the distribution of Xn:


By considering the n + 1’st step we get the forward equation (in vectormatrix notation)


which implies


Putting µ0(·) = δi(·) gives (12). On the other hand we could fix a bounded function h : S → R and define


By considering the first step we get the backward equation


which implies


Putting h(·) = δj(·) gives (12).

Hitting times. Fix A ⊂ S and consider the first hitting time τA = min{n ≥ 0 : Xn ∈ A}. Now consider


12

The next result says hA is the minimal solution of equations (i)-(iii) below. (i)h(i) ≥ 0 for all i ∈ S. (ii) h(i) = 1 for i ∈ A. (iii) h(i) =<sup>�</sup> j<sup>p(i, j)h(j)fori̸ ∈A.</sup>

Proposition 18 (a) hA satisfies (i)-(iii). (b) If h is a solution of (i)-(iii) then hA ≤ h.

Proof. (a) is easy. For (b) consider the transition matrix PA for “the chain stopped on A”

= pA(i, j) p(i, j), i̸ ∈A = δi(j), i ∈ A

Then (ii) and (iii) imply (iv) h = PAh (jargon: h is a harmonic function for PA.) Fix h satisfying (i)-(iii). Since h ≥ 1A, h = P<sup>n</sup> A<sup>h ≥Pn</sup> A<sup>1A.</sup>

This says that h(i) ≥ Pi(Xn<sup>A∈A)whereXAdenotesaMarkovchainwith</sup> transition matrix PA. Now given an (i, P)-chain (Xn) it is clear that


defines an (i, P<sup>A</sup> )-chain. So

h(i) ≥ Pi(Xn<sup>A∈A) = Pi(τA≤n).</sup>

Let n →∞.

13

Lecture 10. In this class we prove the basic results about invariant measures and stationary distributions. The results are those of Durrett Theorems 4.3 - 4.7, though the organization of the proofs is a little different. Most of the work is in the first result (c.f. Durrett Theorem 4.3: note we don’t assume recurrence).

Fix a reference state b and define the b-block occupation measure


Proposition 19 Consider the equations


Then µ(b, ·) is the minimal solution of (13). Moreover


Theorem 20 Suppose the chain is irreducible and recurrent. Then there exists an invariant measure µ, unique up to scalar multiples. Either (i) µ(S) = ∞ and ExTx = ∞ for all x; or (ii) µ(S) < ∞ and ExTx < ∞ for all x.

In case (i) the chain is null-recurrent. In case (ii) the chain is positive-recurrent.

Theorem 21 Suppose the chain is irreducible. Then it is positive-recurrent iff a stationary distribution π exists. If so, then π(x) = 1/ExTx for all x.

14

Lecture 11. Here is a counterpart to the basic convergence result, Durrett 5.5.

Proposition 22 Suppose the chain is irreducible but not positive-recurrent. Then Pµ(Xn = y) → 0 for all y and all initial distributions µ.

Proof. First, we can reduce to the aperiodic case. Next, the result is obvious in the transient case, because


So we may suppose the chain is null-recurrent. Consider independent copies (Xn, Yn) as a chain on S × S. This product chain is irreducible. If the product chain is transient then as above


But the summands are (Pµ(Xn = y))<sup>2</sup> , and these must converge to 0. So suppose the product chain is recurrent. We argue by contradiction. If the result were false, then there exists an initial distribution µ, a state b and a subsequence of times jn such that


By the diagonal argument, we can then pick a subsequence (kn) such that for every state y


Now the coupling argument in the proof of Durrett 5.5 depended only on the fact that the product chain was recurrent. So this argument shows that convergence in (14) holds for all initial distributions. The rest of the argument is analysis. Fatou’s lemma shows<sup>�</sup> y<sup>αy≤1,andthen</sup>


15

Now if there really was a strict inequality for some y then


which is impossible. So we have shown α = αP: this is a finite invariant measure, implying positive-recurrence.

Lecture 12.

The “ergodic theorem” (Durrett 5.1) is a consequence of the SLLN and the following deterministic fact, worth isolating.

Lemma 23 Let (ti) be increasing with n<sup>−1</sup> tn → t<sup>¯</sup> . Let


Then n(t)/t → 1/t<sup>¯</sup> . Now let (ri) be such that ri ≥ 0 and n<sup>−1 �n</sup> i=1<sup>ri→r¯,</sup> and let r(t) be such that


Then r(t)/t → r/¯ t<sup>¯</sup> .

A number of useful identities may be derived from the following result. For simplicity, suppose our chain is irreducible and finite, aperiodic (really we only need positive-recurrent).

Proposition 24 Consider the chain started at state x. Let 0 < S < ∞ be a stopping time such that XS = x. Let y be an arbitrary state. Then


In the phrase “number of . . . before time t”, our convention is to include time 0 but exclude time t.

The following series of lemmas arise from particular choices of y and S. Some involve the fundamental matrix


(the sum is finite by exercise 5.8).

16

Lemma 25 For y̸ = x,


Lemma 26


Lemma 27 π(x)Eπτx = Zxx.

Lemma 28 π(y)Exτy = Zyy − Zxy.

17

---

[Up: contents](index.md)
