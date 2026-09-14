---
title: 24 Lecture 24
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 24 Lecture 24

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This lecture will be about differentiability in quadratic mean (DQM) and local asymptotic normality (LAN). I am following the remarkably clean treatment in Pollard [19] and I recommend that you read this beautiful paper.

## **24.1 Differentiability in Quadratic Mean**

The basic setting is the following. We have a class of probability measures _P_ := _{Pθ, θ ∈_ Θ _}_ on some space that are indexed by a subset Θ of R (the extension to the case of Θ _⊆_ R<sup>_k_</sup> for a fixed _k ≥_ 1 is possible but we shall restrict to _k_ = 1 for simplicity). Assume that there is a single sigma finite measure _µ_ with respect to which each _Pθ_ has a density which will be denoted by _pθ_ . The following is the definition of DQM.

**Definition 24.1** (Differentiability in Quadratic Mean (DQM)) **.** _We say that P is differentiable in quadratic mean at θ_ 0 _∈_ Θ _if there exists a function ℓ_<sup>˙</sup> _θ_ 0 _∈ L_<sup>2</sup> ( _Pθ_ 0) _such that_


In other words, if _P_ satisfies DQM at _θ_ 0, then we have the expansion:


127

where _rθ_ satisfies


Le Cam showed that, under DQM, classical asymptotic results in statistics (such as the asymptotic normality of maximum likelihood estimators) can be proved without requiring the densities _θ �→ pθ_ ( _x_ ) to be twice or thrice differentiable at _θ_ 0.

The following lemma shows that if _P_ satisfies DQM at _θ_ 0 and if _θ �→ pθ_ ( _x_ ) is differentiable at _θ_ 0 in the usual sense, then the function _ℓ_<sup>˙</sup> _θ_ 0 given by the DQM coincides with the usual derivative of log _pθ_ ( _x_ ).

**Lemma 24.2.** _Suppose P satisfies DQM at θ_ 0 _∈_ Θ _with the function ℓ_<sup>˙</sup> _θ_ 0 _. Assume also that θ �→ pθ_ ( _x_ ) _is differentiable at θ_ 0 _with derivative p_ ˙ _θ_ 0( _x_ ) _for almost sure x with respect to the measureµ. Then_


_Proof._ Suppose _{θn}_ is a sequence converging to _θ_ 0. The DQM assumption allows us to write


for all _x_ and _n_ with


By going to a subsequence if necessary, we shall assume that


This can be done, for example, by replacing _{θn}_ by the subsequence _{θnk }_ where _{nk}_ are chosen so that


We now use the fact that<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_∥fi∥_</sup> _L_<sup>1</sup> ( _µ_ )<sup>_<∞_impliesthat�</sup> _i_<sup>_∞_</sup> =1<sup>_|fi|<∞_almostsurely(bymonotone</sup> convergence) which further implies that _fi →_ 0 almost surely as _i →∞_ . This gives that, under the assumption (223)


We can thus rewrite (221) as


Now let us use the fact that _θ �→ pθ_ ( _x_ ) is differentiable at _θ_ 0 with derivative _p_ ˙ _θ_ 0( _x_ ) almost surely with respect to _µ_ and write


Observe that (224) and (225) both hold for almost sure _x_ (with respect to _µ_ ).

We shall now work with two separate cases. The first case is when _pθ_ 0( _x_ ) _>_ 0. In this case, we can rewrite (225) as (note that _pθ_ 0( _x_ ) does not depend on _n_ so that _o_ ( _|θ − θ_ 0 _|/pθ_ 0( _x_ )) = _o_ ( _|θ − θ_ 0 _|_ )):


128

Taking square roots on both sides, we obtain


By a Taylor expansion of _x �→_<sup>_√_</sup> _<u>x</u>_ at _x_ = 0 up to first order, we deduce from above that


Comparing the above with (224), we deduce that


Let us now consider the case when _pθ_ 0( _x_ ) = 0. In this case, (224) and (225) become respectively


and


Equating the above two equations, we obtain


Dividing through by _|θn −θ_ 0 _|_ and letting _n →∞_ , we obtain _p_ ˙ _θ_ 0( _x_ ) = 0 i.e., the equation _ℓ_<sup>˙</sup> _θ_ 0( _x_ ) _pθ_ 0( _x_ ) = _p_ ˙ _θ_ 0( _x_ ) is satisfied in this case as well. This completes the proof.

The above lemma implies that


The right hand side above is the classical _score function_ . Thus when the DQM holds, we shall refer to the function _ℓ_<sup>˙</sup> _θ_ 0 as the score function.

A standard fact about the classical score function is that its expectation with respect to the probability measure _Pθ_ 0 equals zero. The classical proof for this involves interchanging the order of differentiation w.r.t _θ_ and the integral:


The following lemma shows that the DQM assumption implies this fact directly.

**Lemma 24.3.** _Suppose P satisfies DQM at θ_ 0 _with score function ℓ_<sup>˙</sup> _θ_ 0 _. Then_


_Proof._ Let _θn_ be a sequence converging to _θ_ 0. By the DQM representation, we can write (221) with the remainder term _rθn_ satisfying (222). Note then that


129

We now expand the square in the right hand side above which will lead to six terms. One of the terms equals � _pθ_ 0 = 1 which cancels with the left hand side. We thus obtain


(227)

The first term in the right hand side above is clearly _O_ ( _|θn − θ_ 0 _|_ ) in absolute value. The third term is _O_ (( _θn − θ_ 0)<sup>2</sup> ). The final term (by (222)) equals _o_ (( _θn − θ_ 0)<sup>2</sup> ). The remaining two terms (second and fourth) can be controlled via the Cauchy-Schwarz inequality as


by (222) and


again by (222). It is clear therefore that the leading term on the right hand side in (227) is the first term. By dividing the equation (227) through by _|θn − θ_ 0 _|_ and letting _n →∞_ , we deduce (226).

We shall now define _Fisher Information_ . Assume that _P_ satisfies DQM with score function _ℓ_<sup>˙</sup> _θ_ 0. Then the Fisher Information at _θ_ 0 is given by


The argument used in the proof of Lemma 24.3 above leads to an interesting and important fact involving _ℓ_ ˙ _θ_ 0 and the Fisher Information. Because � _ℓ_ ˙ _θ_ 0 _pθ_ 0 _dµ_ = 0, we can plug this into (227) to obtain (also using the fact that the last two terms in (227) are _o_ ( _|θn − θ_ 0 _|_<sup>2</sup> )):


Plugging in the fact that � ( _ℓ_<sup>˙</sup> _θ_ 0)<sup>2</sup> _pθ_ 0 _dµ_ = _I_ ( _θ_ 0), we obtain

This fact is crucial for establishing that DQM implies LAN. The interesting aspect about (228) is the following. The statement (222) implies that _∥rθn∥L_ 2( _µ_ ) = _o_ ( _|θn−θ_ 0 _|_ ). Therefore, if we use the Cauchy-Schwarz inequality on the left hand side above, we obtain that the left hand side is _o_ ( _|θn − θ_ 0 _|_ ). But the equality above implies that the right hand side is _O_ (( _θn − θ_ 0)<sup>2</sup> ) which is a much stronger conclusion that what can be derived from Cauchy-Schwarz. Therefore � _rθn√pθ_ 0 _<u>dµ</u>_ is much smaller in comparison to the _L_<sup>2</sup> ( _µ_ ) norm of _rθn_ . Pollard [19] attributes this phenomenon to the fact that the functions<sup>_√_</sup> _<u>pθn</u>_ in _L_<sup>2</sup> ( _µ_ ) all have norm one (this is clear from the above proof of (228)) and argues that this is the main reason behind the magic of the DQM.

## **24.2 Local Asymptotic Normality**

The DQM is a statement about the first differentiability of the densities _pθ_ at _θ_ 0. There is of course no mention of second order differentiability in DQM. Yet, remarkably, the DQM assumption implies that the log-likelihood function has a second-order Taylor expansion around _θ_ 0 at a scale of _n_<sup>_−_1</sup><sup>_/_2</sup> . Such a local Taylor expansion is known as Local Asymptotic Normality (LAN) and is proved in the following result.

130

**Theorem 24.4.** _Suppose P satisfies DQM at θ_ 0 _with score function ℓ_<sup>˙</sup> _θ_ 0 _and Fisher information I_ ( _θ_ 0) _. Then for every fixed h ∈_ R _, we have_


Equivalently, the conclusion of the above theorem can be written


We say that _P_ satisfies the LAN property at _θ_ 0 if the above holds for every _h ∈_ R. Why is this called local asymptotic normality? To see this, note first that, by the CLT, we have


Therefore, as a consequence of (229), we obtain that for every _h ∈_ R,

Now consider a second estimation problem where we have one observation _Y_ whose density belongs to the family _{Qh, h ∈_ R _}_ were _Qh_ has the density _qsh_ which is the density of the normal distribution with mean _h_ and variance 1 _/I_ ( _θ_ 0). It is easy to see then that


Therefore (229) effectively says that the likelihood ratios of _{Pθ, θ ∈_ Θ _}_ (which can be arbitrary as long as _P_ satisfies DQM) behave like the likelihood ratios of a Normal Experiment _{Qh, h ∈_ R _}_ where _Qh_ = _N_ ( _h,_ 1). Hence asymptotically around _θ_ 0 at the scale _n_<sup>_−_1</sup><sup>_/_2</sup> , the original statistical problem _P_ becomes a Normal mean estimation problem. This is why (229) is referred to as Local Asymptotic Normality.

We shall now prove Theorem 24.4.

_Proof of Theorem 24.4._ All expectations and probabilities in this proof are with respect to the probability measure _Pθ_ 0. Write

where


We will use the fact that


or equivalently, _β_ ( _y_ ) = _o_ ( _y_<sup>2</sup> ) as _y →_ 0. This gives


131

Using the DQM representation, we can write


This gives that<sup>�</sup><sup>_n_</sup> _i_ =1<sup>E</sup><sup>_θ_</sup> 0<sup>_R_</sup> _ni_<sup>2=</sup><sup>_o_(1)andhence�</sup><sup>_n_</sup> _i_ =1<sup>_R_</sup> _ni_<sup>2</sup><sup>_→_0in</sup><sup>_L_1(</sup><sup>_Pθ_</sup> 0<sup>)whichfurtherimpliesthat</sup> � _ni_ =1<sup>_R_</sup> _ni_<sup>2</sup> _→P_ 0. Also, by the Cauchy-Schwarz inequality, we have


We thus have

We shall prove later that

so that we have


The third term in the right hand side above clearly converges to _−h_<sup>2</sup> _I_ ( _θ_ 0) _/_ 4 in probability (by the Strong Law of Large Numbers) so to complete the proof of Theorem 24.4, we only need to show that


For this, write


132

Because

we get


Note that


We shall now use the fact (228) which gives

so that


Combining with (232), we obtain (231). To finish the proof of Theorem 24.4, we only need to verify (230). This is mainly a consequence of _β_ ( _y_ ) = _o_ ( _y_<sup>2</sup> ) as _y →_ 0. It turns out that in order to prove (230), it is enough to show that


Indeed, if these statements hold, then (as _β_ ( _y_ ) = _o_ ( _y_<sup>2</sup> )), we can write (rigorize this):


We shall complete the proof now by proving the assertions in (233). For the first assertion in (233), write (for a fixed _ϵ >_ 0),


which converges to zero as _n →∞_ by the Dominated Convergence Theorem.

For the second assertion in (233), write


This completes the proof of Theorem 24.4.

133

---

[← 23 Lecture 23](24-23-lecture-23.md) · [Up: contents](index.md) · [25 Lecture 25 →](26-25-lecture-25.md)
