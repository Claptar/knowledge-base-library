---
title: 22 Lecture 22
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 22 Lecture 22

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last lecture, we proved that the uniform empirical process converges in distribution to Brownian Bridge in _ℓ_<sup>_∞_</sup> [0 _,_ 1]. The main ingredient for this is proving the stochastic equicontinuity condition for the uniform empirical process. This condition states that


115

where _Xn_ ( _t_ ) is the uniform empirical process. We observed last time that this statement is equivalent to


where


In this lecture, we shall first generalize this argument to more general processes _{_<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Pnf − Pf_ ) : _f ∈F}_ . Specifically, let _F_ be a class of functions and let


We shall provide a sufficient condition on _F_ for which (206) holds. To control the expected supremum in (206), we shall use the following maximal inequality (which was also stated in the previous lecture):

**Theorem 22.1.** _Let H be an envelope for the class H with PH_<sup>2</sup> _< ∞. Then_


_for every δ satisfying_


_Here_


We shall apply Theorem 22.1 to _H_ = _Gη_ . Suppose _F_ is an envelope for _F_ , then it is clear that 2 _F_ is an envelope for _Gη_ . We shall therefore take _H_ = 2 _F_ while applying Theorem 22.1. We get


where


Here, as in Theorem 22.1, _δ_ is any real number satisfying


Now because sup _g∈Gη Pg_<sup>2</sup> _≤ η_ , we can take


so that _δ ↓_ 0 as _η ↓_ 0. Because _Gη_ is a subset of _F −F_ (which is the class of all functions _{f_ 1 _−f_ 2 : _f_ 1 _, f_ 2 _∈F}_ ), we can trivially bound the packing numbers of _Gη_ by the square of the packing numbers of _F_ . More precisely,


for a positive constant _c_ . This gives


116

for two positive constants _c_ and _C_ . Plugging this in (208), we obtain


As a result, we obtain

Lemma 22.2 below then implies that the lim sup term on the right hand side above equals zero (as long as _J_ ( _cδ, F, F_ ) _< ∞_ ) so that


If we now assume that lim _δ↓_ 0 _J_ ( _δ, F, F_ ) = 0, then we establish (206). Note that lim _δ↓_ 0 _J_ ( _δ, F, F_ ) = 0 is a consequence of


It remains to state and prove Lemma 22.2.

**Lemma 22.2.** _Suppose Y_ 1 _, . . . , Yn are identically distributed random variables (no assumption of independence here) with_ E _|Y_ 1 _| < ∞. Then_


_Proof of Lemma 22.2._ This is a consequence of the Dominated Convergence theorem. We write


For each fixed _x_ , it is clear that the integrand above converges to zero as _n →∞_ . Further the integrand is bounded by (by the union bound and the identical distribution assumption) P _{|Y_ 1 _| > x}_ which integrates to E _|Y_ 1 _| < ∞_ . The statement (210) therefore follows by the Dominated Convergence theorem.

## **22.1 Donsker’s Theorem under the Uniform Entropy Condition**

We have proved therefore that under the condition (209) (known as the **uniform entropy condition** ), the stochastic process _Xn_ ( _f_ ) :=<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Pnf − Pf_ ) satisfies the stochastic equicontinuity condition with respect to the metric ( _f, g_ ) _�→∥f − g∥L_ 2( _P_ ) on _F_ . On the other hand, we also have finite dimensional convergence here via the usual multivariate central limit theorem i.e.,


where Σ( _i, j_ ) = Cov( _fi_ ( _X_ 1) _, fj_ ( _X_ 1)) for every _k ≥_ 1 and _f_ 1 _, . . . , fk ∈F_ . We can thus apply our process convergence result from last class which gives that _Xn_ ( _f_ ) _, f ∈F_ converges in distribution on _ℓ_<sup>_∞_</sup> ( _F_ ). The theorem also guarantees that the limit process _X_ ( _f_ ) _, f ∈F_ is a Gaussian process (i.e., ( _X_ ( _f_ 1) _, . . . , X_ ( _fk_ )) has a multivariate Gaussian distirbution for every _k ≥_ 1 and _f_ 1 _, . . . , fk ∈F_ ) has continuous sample paths with respect to the metric ( _f, g_ ) _�→∥f − g∥L_ 2( _P_ ). These conclusions are restated in the following theorem.

**Theorem 22.3.** _Assume the uniform entropy condition_ (209) _. Then there exists a Gaussian process X_ ( _f_ ) _, f ∈ F with continuous sample paths (with respect to the metric ∥f − g∥L_ 2( _P_ ) _) such that the sequence of stochastic processes {Xn} defined by Xn_ ( _f_ ) :=<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Pnf − Pf_ ) _, f ∈F converges in distribution to X in ℓ_<sup>_∞_</sup> ( _F_ ) _._

117

**Definition 22.4** (Donsker Class of Functions) **.** _Say that a class of functions F is Donsker with respect to a probability measure P (also written as P -Donsker) if the stochastic process Xn_ ( _f_ ) :=<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Pnf − Pf_ ) _, f ∈F converges in distribution to a Gaussian process X_ ( _f_ ) _, f ∈F which has continuous sample paths with respect to the metric_ ( _f, g_ ) _�→∥f − g∥L_ 2( _P_ ) _._

Theorem (22.3) states therefore that if _F_ satisfies the uniform entropy condition (209), then _F_ is _P_ - Donsker for every probability measure _P_ .

## **22.2 Bracketing Condition for Donsker Classes**

Another sufficient condition for being _P_ -Donsker is obtained by replacing the uniform entropies in (209) by bracketing entropy numbers. Specifically, assume that


Note that this condition depends on the probability measure _P_ (unlike (209)). The following theorem proves that, under the above condition, _F_ is _P_ -Donsker.

**Theorem 22.5.** _If F satisfies the bracketing condition_ (211) _for the probability measure P , then F is P - Donsker._

To prove this theorem, it is enough to show that the process _Xn_ ( _f_ ) =<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Pnf −Pf_ ) satisfies the stochastic equicontinuity condition under (211). For this, we shall use the following maximal inequality from Van der Vaart [24, Lemma 19.34].

**Theorem 22.6.** _Suppose H is an envelope for a class of functions H and assume that ∥H∥L_ 2( _P_ ) _< ∞. Then for every δ >_ 0 _satisfying_


_the following inequality holds:_


_where_

_and_


Theorem 22.6 is an analogue of Theorem 21.3 for entropy with bracketing. Also, Theorem 22.6 can be seen an improvement of our earlier bracketing based maximal inequality:


When _δ_ is small, the bound given by Theorem 22.6 is much better than the above bound.

We shall now prove Theorem 22.5 using Theorem 22.6 (for proof of Theorem 22.6, refer to Van der Vaart [24, Lemma 19.34]).

118

_Proof of Theorem 22.5._ To prove _F_ is _P_ -Donsker, the key is to verify stochastic equicontinuity (finite dimensional convergence follows from the usual Central Limit Theorem). For stochastic equicontinuity, we need to prove that


where


For this, we use Theorem 22.6 with _H_ := _Gη_ and _H_ = 2 _F_ (where _F_ is the envelope of _F_ ) to obtain


with


Because the bracketing numbers of _{f − g_ : _f, g ∈F}_ can be bounded by the squares of the bracketing numbers of _F_ , we get


for two positive constants _c_ and _C_ . We obtain thus

Also


We thus have


Note that _a_<sup>_′_</sup> ( _δ_ ) does not depend on _n_ . The second term above can be bounded as


By the dominated convergence theorem, the above expectation converges to zero as _n →∞_ (note that we have assumed that E _F_<sup>2</sup> ( _X_ 1) _< ∞_ ). We have thus proved


for every _δ >_ 0. Under the assumption (211), the right hand side above converges to zero as _δ →_ 0. This proves stochastic equicontinuity and consequently the fact that _F_ is _P_ -Donsker.

## **22.3 Application to convergence rate of the sample median**

We gave the example of finding the convergence rate of the sample median as one of the motivations for studying process convergence. Now that we understand what process convergence is, let us revisit this

119

example and rigorize the argument. The setting is as follows. We have i.i.d data _X_ 1 _, . . . , Xn_ generated from, say, the _N_ ( _θ_ 0 _,_ 1) distribution. Let


for _θ ∈_ R. The estimator _θ_<sup>ˆ</sup> _n_ is defined as any minimizer of _Mn_ ( _θ_ ) over _θ ∈_ R. Also note that _θ_ 0 uniquely maximizes _M_ ( _θ_ ) _, θ ∈_ R. We have proved earlier that _θ_<sup>ˆ</sup> _n_ is consistent for _θ_ 0 and that its rate of convergence is _n_<sup>_−_1</sup><sup>_/_2</sup> . To obtain the limiting distribution of _θ_<sup>ˆ</sup> _n_ , we considered the process:


where


and


We have earlier seen that _An_ ( _h_ ) _→L A_ ( _h_ ) := _hZ_ where _Z ∼ N_ (0 _,_ 1) and _Bn_ ( _h_ ) _→ B_ ( _h_ ) := _M ′′_ ( _θ_ 0) _h_ 2 _/_ 2 for every fixed _h ∈_ R. The first convergence was an application of the Lindeberg-Feller CLT and the second convergence followed from Taylor expansion to second order. These convergence statements actually can be much strengthened. In fact, it holds that


and


The uniform convergence above means that sup _|h|≤_ Γ _|Bn_ ( _h_ ) _− B_ ( _h_ ) _| →_ 0 as _n →∞_ . The statement (213) is straightforward to prove via the usual Taylor expansion argument (left as exercise). We shall sketch the argument for (212) below. The process convergence statement (212) requires two ingredients: finite dimensional convergence and stochastic equicontinuity. For finite dimensional convergence, we need to prove that


for every _k ≥_ 1 and _h_ 1 _, . . . , hk ∈_ [ _−_ Γ _,_ Γ]. This can be proved via the multivariate Lindeberg-Feller Central Limit Theorme (left as exercise). For stochastic equicontinuity, we need to show that


For this, note that


where


The statement (214) can then be proved by using one of our bounds on the expected suprema of empirical process (say the bounds based on bracketing numbers). This is again left as exercise.

The two statements (212) and (213) can be added to yield (verify this):


The limit process of _M_<sup>˜</sup> _n_ is therefore _M_<sup>˜</sup> ( _h_ ) := _hZ_ + _M_<sup>_′′_</sup> ( _θ_ 0) _h_<sup>2</sup> _/_ 2 for _h ∈_ R. The limiting distribution of _√n_ <u>(</u> _θ_<sup>ˆ</sup> _n − θ_ 0) now follows if we can prove that argmin _h∈_ R _M_<sup>˜</sup> _n_ ( _h_ ) converges in distribution to argmin _h∈_ R _M_<sup>˜</sup> ( _h_ ). This can be deduced from a general _argmax Continuous Mapping Theorem_ which is proved next.

120

## **22.4 The Argmax Continuous Mapping Theorem**

**Theorem 22.7.** _Let H be a metric space. Let {Mn_ ( _h_ ) _, h ∈ H} and {M_ ( _h_ ) _, h ∈ H} be stochastic processes indexed by H. Suppose the following conditions holds:_

_1. M →L M in ℓ∞_ ( _K_ ) _for every compact subset K of H._

_2. Every realization of M is continuous on H._

_3. Let h_<sup>ˆ</sup> _n maximize Mn_ ( _h_ ) _over h ∈ H._

_4. Let h_<sup>ˆ</sup> _be the_ **_unique_** _maximizer of M_ ( _h_ ) _over h ∈ H._

_5._ **_Tightness_** _: For each ϵ >_ 0 _, there exists a compact subset Kϵ ⊆ H such that_


_Then h_<sup>ˆ</sup> _n→L h_ ˆ _in H i.e., for every bounded continuous function f_ : _H →_ R _, we have_ E _f_ (ˆ _hn_ ) _→_ E _f_ (ˆ _h_ ) _as n →∞._

**Remark 22.1.** _Usually Theorem 22.7 will applied to the process M_<sup>˜</sup> _n_ ( _h_ ) := _rn_<sup>2</sup> � _Mn_ ( _θ_ 0 + _hrn_<sup>_−_1)</sup><sup>_−Mn_(</sup><sup>_θ_0)</sup> � _and M_<sup>˜</sup> _as the limit process of M_<sup>˜</sup> _n. In this case, note that h_<sup>ˆ</sup> _n_ = _rn_ � _θ_ ˆ _n − θ_ 0� _and hence the tightness condition is equivalent to θ_<sup>ˆ</sup> _n −θ_ 0 = _OP_ ( _rn_<sup>_−_1)</sup><sup>_.Thus a preliminary rate result needs to be proved before applying Theorem_</sup> _22.7 for obtaining the asymptotic distribution of rn_ ( _θ_<sup>ˆ</sup> _n − θ_ 0) _._ **Remark** _M_ ˜ _). This_ **22.2.** _will usuallyOne canleadapplyto a Theoremconsistency22.7resultto Mforn_ ( _θθ_<sup>ˆ</sup> ) _n, θ. ∈_ Θ _and M_ ( _θ_ ) _, θ ∈_ Θ _as well (instead of M_<sup>˜</sup> _n and_

_Proof of Theorem 22.7._ It is enough to show that


for every closed subset _F_ of _H_ . Fix a closed subset _F ⊆ H_ and also fix an arbitrary compact set _K_ in _H_ . Write


which gives

Note now that


is a closed subset of _ℓ_<sup>_∞_</sup> ( _K_ ). This follows because if sup _h∈F ∩K mk_ ( _h_ ) _−_ sup _h∈K mk_ ( _h_ ) _≥_ 0 for each _k_ and _mk → m_ uniformly in _K_ , then sup _h∈F ∩K m_ ( _h_ ) _−_ sup _h∈K m_ ( _h_ ) _≥_ 0. Thus from the convergence of _Mn_ to _M_ in _ℓ_<sup>_∞_</sup> ( _K_ ), we get


121

We thus get


We now claim that

The reason for this is that when the right hand side holds, we have sup _h∈F ∩K M_ ( _h_ ) _≥_ sup _h∈K M_ ( _h_ ) _≥_ sup _h∈H M_ ( _h_ ). The continuity of the sample paths of _M_ and the closedness of _F_ (which implies that _F ∩ K_ is compact) implies that sup _h∈F ∩K M_ ( _h_ ) is achieved at some point in _F ∩K_ . The unique maximum assumption on _M_ will imply that the point in _F ∩ K_ achieving the maximum of _M_ will have to equal _h_<sup>ˆ</sup> which implies that _h_<sup>ˆ</sup> _∈ F_ . This therefore gives


Note that this is true for every closed subset _F_ of _H_ and every compact subset _K_ of _H_ . Now fix _ϵ >_ 0 and choose _Kϵ_ as in the tightness condition. This will give


Let _ϵ_ tend to zero to complete the proof.

Use this result along with the process convergence results of the previous section to complete the proof of the result for the limiting distribution of the sample median.

---

[← 21 Lecture 21](22-21-lecture-21.md) · [Up: contents](index.md) · [23 Lecture 23 →](24-23-lecture-23.md)
