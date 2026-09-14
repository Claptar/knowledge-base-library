---
title: 6 Lecture Six
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Lecture Six

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The goal of today’s lecture is to study the general filtering algorithm and then specialize it to the case of linear Gaussian State Space Models leading to the Kalman Filter.

Let us recall the basic setup. We have a state space model describing the distribution of random variables _X_ 0 _, Y_ 0 _, X_ 1 _, Y_ 1 _, . . . , XT , YT_ as


Here _fX_ 0 _|θ_ is the density of _X_ 0, _fXt|Xt−_ 1= _xt−_ 1 _,θ_ is the conditional density of _Xt_ given _Xt−_ 1 = _xt−_ 1 and _fYt|Xt_ = _xt,θ_ is the conditional density of _Yt_ given _Xt_ = _xt_ . Throughout there is additional conditioning on _θ_ .

Our aim is to calculate the conditional distributions:


for various values of _s_ and _t_ . These conditional distributions have known by different names depending on the specific values of _s_ and _t_ :

1. **Filtering Distributions** : These correspond to _s_ = _t_ .

2. **Smoothing Distributions** : These correspond to _s ≤ t_ .

3. **Prediction Distributions** : These correspond to _s > t_ .

The importance of calculating these three types of conditional distributions varies with the application. In tracking applications, interest mainly lies in filtering and prediction distributions while in applications such as trend estimation, interest mainly lies in smoothing and prediction distributions.

### **6.1 General Approach for calculating Filtering Distributions**

Let us now study the general recursive scheme for calculating the filtering distributions. The main step is to go from the filtering density at time _t −_ 1:


to the filtering density at time _t_ :


This recursion is carried out in two steps:

1. **Step One** : Go from the filtering density _fXt−_ 1 _|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ ( _xt−_ 1) at time _t −_ 1 to the one-step ahead prediction density _fXt|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ ( _xt_ ) at time _t −_ 1. This step is known as the _one-step prediction update_ .

2. **Step Two** : Go from the one-step ahead prediction density _fXt|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ ( _xt_ ) at time _t −_ 1 to the filtering density _fXt|Y_ 0= _y_ 0 _,...,Yt_ = _yt,θ_ ( _xt_ ) at time _t_ . This step is known as the _filtering update_ .

24

The one-step ahead prediction update is carried out via the formula:


Now by the Markov nature of the state variables and the independence of the observation random variables conditioned on the state variables, we have


Thus


This equation tells us how to go from the filtering density at time _t −_ 1 to the one-step up ahead prediction density at time _t −_ 1.

Let us now see the filtering update which specifies how to go from the one-step ahead prediction density at time _t −_ 1 to the filtering density at time _t_ . By Bayes rule, we can write


The Markov nature of the state variables and the independence of the observation random variables conditioned on the state variables implies that


Thus


The constant underlying the proportionality symbol _∝_ above is simply the constant that makes the left hand side integrate to one. We thus get


The two steps (27) and (28) together describe the recursion to go from the filtering density at time _t −_ 1 to the filtering density at time _t_ . The recursion can be initialized by simply using (28) with _t_ = 0 and replacing _fXt|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ ( _xt_ ) on the right hand by _fX_ 0 _|θ_ ( _x_ 0) for _t_ = 0.

For linear Gaussian state space models, steps (27) and (28) can be implemented in closed form leading to the Kalman Filter which we shall study next.

### **6.2 The Kalman Filter**

Consider the linear Gaussian state space model:


25

with _X_ 0 _, U_ 1 _, . . . , V_ 0 _, V_ 1 _, . . ._ independent and _Ut ∼ N_ (0 _,_ Σ _t_ ) and _Vt ∼ N_ (0 _, Rt_ ). In this case, it turns out every conditional distributions _Xs | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ are Gaussian so we can write


The Kalman filtering algorithm specifies how to compute _mt|t, Qt|t_ for _t_ = 0 _,_ 1 _, . . ._ by essentially solving the equations (27) and (28) in closed form. Equation (27) specifies how to calculate _mt|t−_ 1 _, Qt|t−_ 1 from _mt−_ 1 _|t−_ 1 _, Qt−_ 1 _|t−_ 1. For this, we can either explicitly compute the integral in (27) or just use standard properties of normal distributions as:


Because, conditional on _Y_ 0 = _y_ 0 _, . . . , Yt−_ 1 = _yt−_ 1 _, θ_ , the random variables _Xt−_ 1 and _Ut_ are independently distributed as _N_ ( _mt−_ 1 _|t−_ 1 _, Qt−_ 1 _|t−_ 1) and _N_ (0 _,_ Σ _t_ ) respectively, we obtain

_Xt | Y_ 0 = _y_ 0 _, . . . , Yt−_ 1 = _yt−_ 1 _, θ ∼ N_ ( _Atmt−_ 1 _|t−_ 1 _, AtQt−_ 1 _|t−_ 1 _At_<sup>_′_+ Σ</sup><sup>_t_)</sup>

Thus


We next calculate _mt|t, Qt|t_ from _mt|t−_ 1 _, Qt|t−_ 1 by calculating filtering update (28). The basic idea behind this calculation is encapsulated in the result below.

**Fact 6.1.** _Suppose X ∼ N_ ( _m_ 0 _, Q_ 0) _and Y | X_ = _x ∼ N_ ( _Bx, R_ ) _(note that the condition Y | X_ = _x ∼ N_ ( _Bx, R_ ) _can also be written as Y_ = _BX_ + _V where V ∼ N_ (0 _, R_ ) _with V, X being independent). Then_


_where_


The following two simple examples can be used to better understand the formula (32). **Example 6.2** (Normal Mean Estimation) **.** _Suppose_ Θ _∼ N_ ( _µ, τ_<sup>2</sup> ) _and Y_ 1 _, . . . , Yn |_ Θ = _θ_<sup>_i.i.d_</sup> _∼ N_ ( _θ, σ_<sup>2</sup> ) _. Then it is well-known that_


_This result is a special case of_ (32) _corresponding to m_ 0 = _µ, Q_ 0 = _τ_<sup>2</sup> _, Y_ = ( _Y_ 1 _, . . . , Yn_ )<sup>_′_</sup> _, y_ = ( _y_ 1 _, . . . , yn_ )<sup>_′_</sup> _, B_ = (1 _, . . . ,_ 1)<sup>_′_</sup> _and R_ = _σ_<sup>2</sup> _In._

**Example 6.3** (Linear Regression) **.** _Suppose β ∼ N_ ( _m_ 0 _, Q_ 0) _and Y | β ∼ N_ ( _Zβ, σ_<sup>2</sup> _In_ ) _where Z is a deterministic n × p matrix. The formula_ (32) _then gives_


_This result is expected because when Q_ 0 = _CI for a large constant C, we can neglect the effect of Q_ 0 _and this leads to_


_which is familiar from usual least squares theory._

26

The Sherman-Morrison-Woodbury formula:


can be used with _A_ = _Q_<sup>_−_</sup> 0<sup>1,</sup><sup>_U_=</sup><sup>_B′_,</sup><sup>_C_=</sup><sup>_R−_1,</sup><sup>_V_=</sup><sup>_B_toobtainthefollowingalternative</sup> formulae for _m_ 1 and _Q_ 1:


Note that (32) involves inversion of the matrix _Q_<sup>_−_</sup> 0<sup>1+</sup><sup>_B′R−_1</sup><sup>_B_while (53) involves inversion of</sup> _BQ_ 0 _B_<sup>_′_</sup> + _R_ . When the dimension of _BQ_ 0 _B_<sup>_′_</sup> + _R_ is much smaller than that of _Q_<sup>_−_</sup> 0<sup>1+</sup><sup>_B′R−_1</sup><sup>_B_,</sup> it is computationally advantageous to work with (53) compared to (32). This will often be the case so we shall mainly use the formula (53).

Now let us get back to the derivation of the filtering updates for the Linear Gaussian State Space Model where we need to calculate _mt|t_ and _Qt|t_ in terms of _mt|t−_ 1 and _Qt|t−_ 1. It is easy to check that Fact 9.1 is directly applicable with _m_ 0 = _mt|t−_ 1, _Q_ 0 = _Qt|t−_ 1, _B_ = _Bt_ , _R_ = _Rt_ and _m_ 1 = _mt|t_ , _Q_ 1 = _Qt|t_ . The formula (53) then gives


The equations (51) and (52) together comprise the Kalman Filter. They provide the solution for the filtering problem for linear Gaussian state space models. Here is a formal description of the Kalman Filter including the initialization step: We are given the model (49) and we assume that _µ_ 0 _,_ Γ0 _, {At, t ≥_ 1 _}, {Bt, t ≥_ 0 _}_ , _{_ Σ _t, t ≥_ 0 _}_ and _{Rt, t ≥_ 0 _}_ are known. The Kalman filter for calculating the conditional distributions (50) for _s_ = _t_ is:

1. **Initialization** : Set _m_ 0 _|−_ 1 = _µ_ 0 and _Q_ 0 _|−_ 1 = Γ0. Implement (52) for _t_ = 0 to obtain _m_ 0 _|_ 0 and _Q_ 0 _|_ 0.

2. **Recursion** : For each _t_ = 1 _,_ 2 _, . . ._ , implement (51) and (52).

Note that the Kalman Filter algorithm also computes the one-step ahead prediction means _mt|t−_ 1 and covariances _Qt|t−_ 1 in intermediate computations. So the Kalman Filter can also be used to obtain these one-step ahead predictions.

### **6.3 Recommended Reading for Today**

1. The general filtering approach described in Section 6.1 can be found in:

   - a) Section 6.2 of the Kitagawa-Gersch book

   - b) Section 14.2 of the Kitagawa book.

   - c) Section 2.7.1 of the Petris-Petrone-Campagnoli book

2. The Kalman filter is described in the all the books listed in the course outline:

   - a) Section 5.2 of the Kitagawa-Gersch book

   - b) Section 9.2 of the Kitagawa book

   - c) Section 4.3 of the Durbin-Koopman book

27

- d) Section 4.3 of the S¨arkk¨a book

- e) Section 2.7.2 of the Petris-Petrone-Campagnoli book

- f) Section 3.2 of the Triantafyllopoulos book

Section 7.2 of the Chopin-Papaspiliopoulos book also discusses the Kalman filter. They however derive the algorithm from a general Feynman-Kac formalism (see their Chapter 5). I will discuss the Feynman-Kac stuff in class a few weeks later.

---

[← 5 Lecture Five](06-5-lecture-five.md) · [Up: contents](index.md) · [7 Lecture Seven →](08-7-lecture-seven.md)
