---
title: 3 Lecture 3
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Lecture 3

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **3.1 Hoeffding’s Inequality and Proof of the Bounded Differences Concentration Inequality**

One of the goals of this lecture is to prove the Bounded Differences Concentration Inequality. We shall prove another standard concentration inequality called Hoeffding’s inequality and then tweak the proof of Hoeffding’s inequality to yield the Bounded Differences Concentration Inequality.

**Theorem 3.1** (Hoeffding’s Inequality) **.** _Suppose ξ_ 1 _, . . . , ξn are independent random variables. Suppose a_ 1 _, . . . , an, b_ 1 _, . . . , bn are constants such that ai ≤ ξi ≤ bi almost surely for each i_ = 1 _, . . . , n. Then for every t ≥_ 0 _, we have_

_and_


13

_Proof._ Let _S_ :=<sup>�</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_ξi_= E</sup><sup>_ξi_)andwrite(forafixed</sup><sup>_λ ≥_0)</sup> P _{S ≥ t} ≤_ P _{e_<sup>_λS_</sup> _≥ e_<sup>_λt_</sup> _} ≤ e_<sup>_−λt_</sup> E _e_<sup>_λS_</sup> = exp ( _−λt_ + _ψS_ ( _λ_ ))

where


is the log moment generating function of _S_ . Now by the independence of _ξ_ 1 _, . . . , ξn_ ,


where _ψξi−_ E _ξi_ ( _·_ ) denotes the log moment generating function of _ξi −_ E _ξi_ . Fix 1 _≤ i ≤ n_ and let _U_ := _ξi −_ E _ξi_ . We shall bound _ψU_ ( _λ_ ) below. We know that E _U_ = 0 and that _ai −_ E _ξi ≤ U ≤ bi −_ E _ξi_ almost surely. By second order Taylor expansion of _ψU_ ( _λ_ ) around 0, we can write


for some 0 _≤ λ_<sup>_′_</sup> _≤ λ_ . Note now that _ψU_ (0) = log E(1) = 0. Also


so that


And


Consider now a random variable _V_ whose density with respect to the distribution of _U_ is _e_<sup>_λU_</sup> _/_ (E _e_<sup>_λU_</sup> ) i.e.,


Based on the calculation above, it is then clear that _ψU_<sup>_′′_(</sup><sup>_λ_) =</sup><sup>_var_(</sup><sup>_V_)</sup><sup>_≥_0.Notealsothat</sup><sup>_V_issupportedon</sup> the interval [ _ai −_ E _ξi, bi −_ E _ξi_ ] (because _U_ is supported on this interval and _PV_ is absolutely continuous with respect to _PU_ ). As a result,


where _η_ is the mid-point of the interval [ _ai −_ E _ξi, bi −_ E _ξi_ ]. We have thus proved that _ψU_<sup>_′′_(</sup><sup>_λ_)</sup><sup>_≤_(</sup><sup>_bi −ai_)2</sup><sup>_/_4</sup> for every _λ ≥_ 0. This, along with _ψU_ (0) = 0 and _ψU_<sup>_′_(0) = 0,gives</sup>


As a result


14

and consequently


for every _λ ≥_ 0. We can optimize this bound over _λ ≥_ 0 by setting


to prove (12). To prove the lower tail inequality, just apply (12) to _−ξ_ 1 _, . . . , −ξn_ .

The proof given above bounds the probability P _{S ≥ t}_ in terms of the Moment Generating Function of _S_ . This technique is known as the _Cramer-Chernoff Method_ .

### **3.1.1 Remarks on Hoeffding’s inequality**

Consider the following special case of Hoeffding’s inequality: Suppose _X_ 1 _, . . . , Xn_ are i.i.d with E _Xi_ = _µ_ , _var_ ( _Xi_ ) = _σ_<sup>2</sup> and _a ≤ Xi ≤ b_ almost surely ( _a_ and _b_ are constants). Suppose _X_<sup>¯</sup> _n_ := ( _X_ 1 + _· · ·_ + _Xn_ ) _/n_ . Hoeffding’s inequality then gives


Is this a good bound? By “good” here, we mean if the probability on the right hand side above is close to the bound on the right or if the bound is much looser. To answer this question, we of course need a way of approximately computing the probability on the left hand side. A natural way of doing this is via invoking the Central Limit Theorem (assuming that the CLT is valid). Indeed CLT states that


provided that the distribution of _Xi_ (and in particular the quantities _µ, σ_<sup>2</sup> _, a_ and _b_ ) do not depend on _n_ (note that Hoeffding’s inequality needs no such assumption; in particular, (13) is valid even when _µ_ , _σ_<sup>2</sup> , _a_ and _b_ all depend on _n_ ). Thus we may expect


when _n_ is large and when CLT holds. What is P _{N_ (0 _, σ_<sup>2</sup> ) _≥ t}_ ? We can bound this again by the CramerChernoff method:


for every _λ ≥_ 0 where _ψN_ (0 _,σ_ 2) is the log moment generating function of _N_ (0 _, σ_<sup>2</sup> ). By a straightforward calculation, it can be seen that _ψN_ (0 _,σ_ 2)( _λ_ ) is exactly equal to _λ_<sup>2</sup> _σ_<sup>2</sup> _/_ 2. Thus


Is this bound accurate? It is quite good as can be seen from the following inequality (see, for example, Feller [7, Section 7.1]):


15

_−t_<sup>2</sup> So exp � 2 _σ_<sup>2</sup> � is the correct exponential term controlling the behavior of P _{N_ (0 _, σ_<sup>2</sup> ) _≥ t}_ . Now let us compare Hoeffding with the bound (14). Hoeffding gives the bound


while normal approximation suggests


Note now that because _a ≤ X_ 1 _≤ b_ almost surely,


Thus in the regime where CLT holds, Hoeffding is a looser inequality where the variance _σ_<sup>2</sup> is replaced by the upper bound ( _b − a_ )<sup>2</sup> _/_ 4. This looseness can be quite pronounced when _X_ 1 puts less mass near the end points _a_ and _b_ . Here is a potential statistical implication of this looseness.

**Example 3.2.** _Suppose X_ 1 _, . . . , Xn are i.i.d with_ E _Xi_ = _µ, var_ ( _Xi_ ) = _σ_<sup>2</sup> _and a ≤ Xi ≤ b almost surely (a and b are constants). Suppose σ_<sup>2</sup> _, a and b are known while µ is unknown and that we seek a confidence interval for µ. There are two ways of solving this problem._

_The first method uses the CLT (normal approximation). Indeed, by CLT:_


_as n →∞ for each t. Thus_


_where zα/_ 2 _is defined so that the last equality above holds. This leads to the following C.I for µ:_


_Note that this is an “asymptotically valid”_ 100(1 _− α_ )% _confidence interval for µ. Its finite sample coverage, on the other hand, may not be_ 100(1 _− α_ )% _._

_The second method for constructing a confidence interval for µ uses the Hoeffding inequality which states that_

_Thus, by taking,_


_one gets the following confidence interval for µ:_


_This inequality has guaranteed finite sample coverage_ 100(1 _− α_ )% _. But this interval might be much too big compared to_ (15) _. Which of the two intervals_ (15) _and_ (16) _would you prefer?_

16

### **3.1.2 Hoeffding’s inequality for Martingale Differences**

**Theorem 3.3** (Hoeffding’s inequality for Martingale Differences) **.** _Suppose F_ 1 _, . . . , Fn are increasing σ-fields and suppose ξ_ 1 _, . . . , ξn are random variables with ξi being Fi-measurable. Assume that_


_for all i_ = 1 _, . . . , n. Also assume that, for each_ 1 _≤ i ≤ n, the conditional distribution of ξi given Fi−_ 1 _is supported on an interval whose length is bounded from above by the deterministic quantity Ri. Then_

_and_


_for every t ≥_ 0 _._

**Remark 3.1.** _The assumption_ (17) _means that_ ( _Sj, Fj_ ) _, j_ = 1 _, . . . , n is a martingale where Sj_ :=<sup>�</sup><sup>_j_</sup> _i_ =1<sup>(</sup><sup>_ξi −_</sup> E _ξi_ ) _. Therefore the sequence {ξi −_ E _ξi, i_ = 1 _, . . . , n} is a martingale difference sequence._

_Proof._ Let _S_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_ξi −_E</sup><sup>_ξi_).Asbefore,forevery</sup><sup>_t ≥_0and</sup><sup>_λ ≥_0,</sup>


with


Observe now that


Now because E _ξn_ = E( _ξn|Fn−_ 1), we can use exactly the same argument as in the proof of Hoeffding’s inequality in the independent case (via second order Taylor expansion of the log Moment Generating Function) to deduce that


and this gives


Now repeat the above argument (by conditioning on _Fn−_ 2, then _Fn−_ 3 and so on) to deduce that


This gives


Optimize over _λ_ to deduce (18). For the proof of the lower tail inequality, argue with _−ξi_ in place of _ξi_ .

17

### **3.1.3 Proof of the Bounded Differences Concentration Inequality**

We shall now prove the bounded differences concentration inequality as a simple consequence of Theorem 3.3. Recall the statement of the Bounded Differences Concentration Inequality:

**Theorem 3.4** (Bounded Differences Concentration Inequality) **.** _Suppose X_ 1 _, . . . , Xn are independent random variables taking values in a set X . Suppose g_ : _X × · · · × X →_ R _be a function that satisfies the following “bounded differences” assumption’:_


_for some constants c_ 1 _, . . . , cn. Then for every t ≥_ 0 _, we have_


_and_


_Proof of Theorem 3.4._ We shall apply the martingale Hoeffding inequality to


and _Fi_ taken to be the sigma field generated by _X_ 1 _, . . . , Xi_ for _i_ = 1 _, . . . , n_ . Clearly _ξi_ is _Fi_ measurable and E _ξi_ = 0. Also


Thus ( _ξi, Fi_ ) is a martingale difference sequence. We shall now argue that the conditional distribution of _ξi_ given _Fi−_ 1 is supported on an interval of length bounded from above by _ci_ . For this, we need to look at the condition distribution of _ξi_ given _X_ 1 _, . . . , Xi−_ 1. So let us fix _X_ 1 _, . . . , Xi−_ 1 at _x_ 1 _, . . . , xi−_ 1. Then _ξi_ is a function solely of _Xi_ and we need to look at the range of values of _ξi_ as _Xi_ = _x_ varies. We therefore need to look at the values:


as _x_ varies and _x_ 1 _, . . . , xi−_ 1 are fixed. Now, by **independence** of _X_ 1 _, . . . , Xn_ , the right hand side above equals


where the “constant” term only depends on _x_ 1 _, . . . , xi−_ 1. Thus we can take _Ri_ to be


It is clear now that _Ri ≤ ci_ by the bounded differences assumption (19). We can therefore apply Theorem 3.3 with _Ri_ = _ci_ which finishes the proof of Theorem 3.4.

18

---

[← 2 Lecture 2](03-2-lecture-2.md) · [Up: contents](index.md) · [4 Lecture 4 →](05-4-lecture-4.md)
