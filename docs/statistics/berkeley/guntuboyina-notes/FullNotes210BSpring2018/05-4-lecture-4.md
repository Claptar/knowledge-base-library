---
title: 4 Lecture 4
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Lecture 4

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **4.1 Bennett’s Inequality**

Let us recall the Hoeffding inequality from last lecture. It states that


for every _t ≥_ 0 where _X_ 1 _, . . . , Xn_ are independent random variables with _ai ≤ Xi ≤ bi_ almost surely. We remarked that when<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_var_(</sup><sup>_Xi_) is much smaller than �</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_bi −ai_)2</sup><sup>_/_4 and when the CLT holds,then the</sup> tail bound given by Hoeffding can be loose. Bennett’s inequality attempts to given tail bounds which involve variances.

**Theorem 4.1** (Bennett’s inequality) **.** _Suppose X_ 1 _, . . . , Xn are independent random variables having finite variances. Suppose Xi ≤ B almost surely for each i_ = 1 _, . . . , n (here B is deterministic). Let V_ :=<sup>�</sup><sup>_n_</sup> _i_ =1<sup>E</sup><sup>_X_</sup> _i_<sup>2</sup><sup>_._</sup> _Then for every t ≥_ 0 _, we have_


_where_


**Remark 4.1.** _Bennett’s inequality, as stated above, gives only the upper tail bound. To get the lower bound, one needs to impose the assumption Xi ≥−B. In this case, one gets_


**Remark 4.2.** _For the function h defined in_ (22) _, it is easy to see that h_ (0) = 0 _, h_<sup>_′_</sup> (0) = 0 _and h_<sup>_′′_</sup> (0) = 1 _. Therefore for u near zero, we have h_ ( _u_ ) _≈ u_<sup>2</sup> _/_ 2 _. Thus when tB/V is small, the bound given by Bennett inequality looks like:_


_Thus Bennett’s inequality gives Gaussian like tails with V_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>E</sup><sup>_X_</sup> _i_<sup>2</sup><sup>_insomeregimes._</sup>

_As an example, suppose that_ E _Xi_ = 0 _, var_ ( _Xi_ ) = _σ_<sup>2</sup> _and Xi ≤_ 1 _. Then V_ = _nσ_<sup>2</sup> _and Bennett’s inequality gives_


_When t is small compared to_<sup>_√_</sup> _<u>nσ</u>_<sup>2</sup> _, we get a Gaussian type bound._

_Proof of Theorem 4.1._ Without loss of generality, take _B_ = 1 (by working with the variables _X_ 1 _/B, . . . , Xn/B_ instead of _X_ 1 _, . . . , Xn_ ).

This proof relies on the following observation: Let _φ_ : R _→_ R denote the function _φ_ ( _u_ ) := _e_<sup>_u_</sup> _−u−_ 1. Then the map _u �→ φ_ ( _u_ ) _/u_<sup>2</sup> is increasing on R (we take _φ_ (0) _/_ 0<sup>2</sup> = 1 _/_ 2). I will leave as homework the verification of this fact.

19

Let _S_ :=<sup>�</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_Xi −_E</sup><sup>_Xi_).Thenforevery</sup><sup>_λ ≥_0asbefore</sup>


where we have used the independence of _X_ 1 _, . . . , Xn_ . Now because _Xi ≤_ 1, we have _λXi ≤ λ_ and hence (using the fact that _φ_ ( _u_ ) _/u_<sup>2</sup> is increasing), we deduce that


which implies that


Using this bound in the right hand side of (23), we obtain


We now use the trivial inequality (1 + _x ≤ e_<sup>_x_</sup> )


to obtain


for every _λ ≥_ 0. We now optimize the above bound by taking the derivative with respect to _λ_ and setting it equal to zero to obtain:


For this value of _λ_ , it is straightforward to deduce (21).

The form of the bound in Bennett’s inequality can be simplified by using the following inequality (whose proof is left as exercise):


This leads to the following result which is known as Bernstein’s inequality.

**Theorem 4.2** (Bernstein’s Inequality) **.** _Suppose X_ 1 _, . . . , Xn are independent random variables with finite variances and suppose that |Xi| ≤ B almost surely for each i_ = 1 _, . . . , n (B is deterministic). Let V_ := � _ni_ =1<sup>E</sup><sup>_X_</sup> _i_<sup>2</sup><sup>_.Thenforeveryt ≥_0</sup><sup>_,wehave_</sup>

_and_


**Remark 4.3.** _There is a version of Bernstein’s inequality that replaces the boundedness assumption by weaker moment restrictions. See Boucheron et al. [3, Theorem 2.10]._

20

The two bounds in Bernstein’s inequality can be combined to write


We can now attempt to find the value of _t_ which makes the bound on the right hand side above exactly equal to _α_ i.e., we want to solve the equation


This leads to the quadratic equation


whose nonnegative solution is given by


where, in the last inequality, we used the fact that _√a_ + _b ≤_<sup>_√_</sup> _<u>a</u>_ + _√b_ . Thus Bernstein’s inequality implies that


with probability at least 1 _− α_ . Now if _X_ 1 _, . . . , Xn_ are i.i.d with mean zero, variance _σ_<sup>2</sup> and bounded in absolute value by _B_ , then _V_ = _nσ_<sup>2</sup> which gives that the inequality


holds with probability at least 1 _− α_ . Note that if _X_<sup>¯</sup> _n_ is normal, then _|X_<sup>¯</sup> _n|_ will be bounded by the first term in the right hand side above with probability at least 1 _− α_ . Therefore the deviation bound (24) agrees with the normal approximation bound except for the smaller order term (which if of order 1 _/n_ ; the leading term being of order 1 _/_<sup>_√_</sup> _<u>n</u>_ <u>).</u>

## **4.2 Back to Concentration of** sup _f ∈F | . . . |_

Let us now get back to the concentration behavior of


Let us introduce some notation here. We denote the empirical measure of _X_ 1 _, . . . , Xn_ by _Pn_ . The common distribution of the i.i.d random observations _X_ 1 _, . . . , Xn_ will be denoted by _P_ . We also let


The quantity can therefore be written as


21

The concentration inequality that we proved via the Bounded Differences Inequality is the following. Suppose that _F_ consists of functions that are uniformly bounded by _B_ , then


with probability 1 _− α_ .

We remarked previously that when _var_ ( _f_ ( _X_ 1)) is small compared to _B_ for every _f ∈F_ , this inequality is not sharp. In such situations, it is much more helpful to use _Talagrand’s concentration inequality for the suprema of empirical processes_ which is stronger than (26) and also deeper and harder to prove. We shall give the statement of this inequality but not the proof (for a proof, you can refer to Boucheron et al. [3, Section 12.4]). Before stating Talagrand’s inequality, let us look at a statistical application where it becomes necessary to deal with function classes _F_ where the variances are small compared to the uniform bound. This application concerns the regression problem (it also applies similarly to the classification problem).

**Example 4.3** (Bounded Regression) **.** _We have two random objects X and Y taking values in spaces X and Y respectively. Assume that Y is a bounded subinterval of the real line. The problem is to predict Y ∈Y on the basis of X ∈X . A predictor (or estimator) is any function g which maps X to_ R _. The (test) error of an estimator g is defined by_


_The goal of regression is to construct an estimator with small error based on n i.i.d observations_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _having the same distribution as_ ( _X, Y_ ) _. For an estimator g, its empirical error is given by_


_A natural strategy is to select a class of predictors G and then to choose the predictor in G which has the smallest empirical error i.e.,_


_The key question now is how good a predictor is g_ ˆ _n in terms of test error i.e., how small is its error:_


_In particular, we are interested in how small L_ (ˆ _gn_ ) _is compared to_ inf _g∈G L_ ( _g_ ) _. Suppose that this infimum is achieved at some g_<sup>_∗_</sup> _∈G. To bound L_ (ˆ _gn_ ) _− L_ ( _g_<sup>_∗_</sup> ) _, it is natural to write:_


_We can now use Empirical Process Notation. Let P denote the joint distribution of_ ( _X, Y_ ) _and Pn denote the empirical distribution of_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _. Let F denote the class of all functions_ ( _x, y_ ) _�→_ ( _y − g_ ( _x_ ))<sup>2</sup> _as g varies over G._

_With this notation, the above inequality becomes_


_where f_<sup>ˆ</sup> _n_ ( _x, y_ ) := ( _y − g_ ˆ _n_ ( _x_ ))<sup>2</sup> _and f_<sup>_∗_</sup> ( _x, y_ ) := ( _y − g_<sup>_∗_</sup> ( _x_ ))<sup>2</sup> _. In order to proceed further, we need to bound the right hand side above. A crude bound is_


_If we now assume that the class of functions F is uniformly bounded by B, we can use the concentration inequality_ (26) _. This will give some bound on L_ (ˆ _gn_ ) _− L_ ( _g_<sup>_∗_</sup> ) _provided one can control the Expectation (we_

22

_shall study how to do this later). It is important now to note that this method will never give a bound better than_ 1 _/_<sup>_√_</sup> _<u>n</u> for L_ (ˆ _gn_ ) _− L_ ( _g_<sup>_∗_</sup> ) _. This is because there is already a term of n_<sup>_−_1</sup><sup>_/_2</sup> _in the right hand side of_ (26) _. But in regression, at least for small classes G (such as finite dimensional function class), we would expect the test error to decay much faster than n_<sup>_−_1</sup><sup>_/_2</sup> _(such as at the n_<sup>_−_1</sup> _rate). Such fast rates cannot be proved by this method._

_To prove faster rates, one needs to use a technique called “localization” instead of the crude bound_ (28) _. Let δ_<sup>ˆ</sup> _denote the left hand side of_ (27) _and the goal is to get bounds for δ_<sup>ˆ</sup> _. The inequality_ (27) _implies that_


_Thus we really need to understand how to bound_


_This is a bit complicated because the class of functions in the supremum is random and depends on δ_<sup>ˆ</sup> _. But let us ignore that for the moment and focus on obtaining bounds for_


_for a deterministic but small δ. The key now is to realize that the functions involved here have small variances (at least in the well specified case where g_<sup>_∗_</sup> ( _x_ ) = E( _Y |X_ = _x_ ) _). Indeed, in the well specified case, we have_


_Hence when P_ ( _f − f_<sup>_∗_</sup> ) _≤ δ, we have_


_If we use the concentration inequality_ (26) _to control_ (29) _, the resulting bound will be atleast_ � _B/n independent of δ. This will not lead to any faster rates. However Talagrand’s inequality will make sure of the small variances to give a better bound. Together wil suitable bounds for the expectation, one will obtain faster rates for regression under appropriate assumptions on G._

_Similar analysis can be done for classification but certain assumptions._

Let us now state Talagrand’s concentration inequality for empirical processes. As before, assume that _F_ is uniformly bounded by a constant _B_ . Then, letting, _Z_ := sup _f ∈F |Pnf − Pf |_ , we have


with probability at least 1 _− α_ . Here _C_ is a universal constant which can be made explicit. Note that the leading terms are E _Z_ and the second term which involves only the variances. The final term is of order 1 _/n_ .

After learning how to control E _Z_ , we shall come back to regression and classification to provide explicit error bounds on the test error for various classes _G_ . We shall use Talagrand’s inequality together with localization.

---

[← 3 Lecture 3](04-3-lecture-3.md) · [Up: contents](index.md) · [5 Lecture 5 →](06-5-lecture-5.md)
