---
title: 9 Lecture Nine
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 9 Lecture Nine

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **9.1 Smoothing**

Smoothing, in the context of state space models, refers to the problem of finding the conditional distribution _Xs | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ for _s ≤ t_ . The main interest in these conditional distributions is in the case _t_ = _T_ (recall that our observed data is _y_ 0 _, . . . , yT_ ).

The algorithm that we shall discuss proceeds by first running the filtering step which calculates the distributions _Xt | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ for _t_ = 0 _,_ 1 _,_ 2 _, . . ._ . Following this, one follows backward recursion starting from _s_ = _t_ and then decreasing _s_ as _t −_ 1 _, t −_ 2 _, . . ._ to calculate the conditional distributions _Xs | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ for _s ≤ t_ . The overall algorithm is often referred to as FFBS (Forward Filtering Backward Smoothing).

We shall understand the backward recursion in the general case of arbitrary state space models. Subsequently, we shall specialize this to the case of linear Gaussian state space models.

### **9.2 Backward Recursion for General State Space Models**

Fix a value of _t ≥_ 0. Assume that we have computed the conditional density:


for some _s < t_ . The goal is then to figure out how to use the above density to calculate


For this, we write

_fXs|Y_ 0= _y_ 0 _,...,Yt_ = _yt,θ_ ( _xs_ ) = _fXs|Xs_ +1= _xs_ +1 _,Y_ 0= _y_ 0 _,...,Yt_ = _yt,θ_ ( _xs_ ) _fXs_ +1 _|Y_ 0= _y_ 0 _,...,Yt_ = _yt,θ_ ( _xs_ +1) _dxs_ +1 _._ �

The key now is to note that

_Xs |_ ( _Xs_ +1 = _xs_ +1 _, Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ ) =<sup>d</sup> _Xs |_ ( _Xs_ +1 = _xs_ +1 _, Y_ 0 = _y_ 0 _, . . . , Ys_ = _ys, θ_ ) _._ In words, the above means that conditional on _Xs_ +1 = _xs_ +1 _, Y_ 0 = _y_ 0 _, . . . , Ys_ = _ys_ , the random objects _Xs_ and ( _Ys_ +1 _, . . . , Yt_ ) are independent. I will leave the verification of this

37

property as an exercise. We thus have


The next step is to calculate _fXs|Xs_ +1= _xs_ +1 _,Y_ 0= _y_ 0 _,...,Ys_ = _ys,θ_ ( _xs_ ). For this we use Bayes rule to write


We can thus write the backward smoothing recursion in one step as


Note that the right hand side above involves the densities _fXs_ +1 _|Y_ 0= _y_ 0 _,...,Yt_ = _yt,θ_ , _fXs|Y_ 0= _y_ 0 _,...,Ys_ = _ys,θ_ and _fXs_ +1 _|Xs_ = _u,θ_ . The first of these densities is available to us because we are assuming that we calculated the smoothing density for _s_ + 1. The second of these densities is a filtering density and will be available after running the forward filtering algorithm. The third of these densities is the transition density of the hidden Markov process that is available from the specification of the state space model.

For the linear Gaussian state space models, the recursion above can be re-written in closed form in terms of the means and covariances of the distributions as we show in the next section.

### **9.3 Smoothing for Linear Gaussian State Space Models**

Consider the linear Gaussian state space model:


with _X_ 0 _, U_ 1 _, . . . , V_ 0 _, V_ 1 _, . . ._ independent and _Ut ∼ N_ (0 _,_ Σ _t_ ) and _Vt ∼ N_ (0 _, Rt_ ). Each of the quantities _µ_ 0 _,_ Γ0 _, At, Bt,_ Σ _t, Rt_ appearing in the model above can depend on an unknown vector of parameters _θ_ . Every conditional distribution _Xs | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ is Gaussian and we can write


We have already seen that the Kalman filter computes _mt|t, Qt|t_ using the following equations:


and


The smoothing algorithm described below computes _ms|t, Qs|t_ for a fixed _t ≥_ 0 and all _s ≤ t_ . We shall make use of the following fact that we used previously in the derivation of the Kalman Filter:

38

**Fact 9.1.** _Suppose X ∼ N_ ( _m_ 0 _, Q_ 0) _and Y | X_ = _x ∼ N_ ( _Bx, R_ ) _(note that the condition Y | X_ = _x ∼ N_ ( _Bx, R_ ) _can also be written as Y_ = _BX_ + _V where V ∼ N_ (0 _, R_ ) _with V, X being independent). Then the following assertions hold:_

_1. X | Y_ = _y ∼ N_ ( ˜ _m_ ( _y_ ) _, Q_<sup>˜</sup> ) _where_


Note that _m_ ˜ ( _y_ ) depends on _y_ but _Q_<sup>˜</sup> does not depend on _y_ .

**Remark 9.1.** _Fact 9.1 can be reformulated in terms of densities as follows. Let φ_ ( _x_ ; _µ,_ Σ) _denote the multivariate normal density with mean vector µ and covariance matrix_ Σ _evaluated at x i.e.,_


_The first conclusion X | Y_ = _y ∼ N_ ( ˜ _m_ ( _y_ ) _, Q_<sup>˜</sup> ) _of Fact 9.1 is equivalent to the identity_


_This is because the left hand side above is simply_


_The second conclusion of Fact_ (9.1) _is equivalent to the identity:_


_This is because the left hand side above is_


_It should be easy to see that_ (55) _is easily extended to the case where the Bx term on the left hand side is replaced by Bx_ + _c for a deterministic vector c:_


Using the identities (54) and (55), we can rewrite the general backward smoothing recursion (48) as follows.


39

Applying (54) with _m_ 0 = _ms|s_ , _Q_ 0 = _Qs|s_ , _B_ = _As_ +1 and _R_ = Σ _s_ +1, we deduce that the term inside the square brackets above equals


where


As a result


We now apply (56). Note that _m_ ˜ ( _xs_ +1) is a linear function of _xs_ +1 and it can be written as _Bxs_ +1 + _c_ with


and


The identity (56) therefore gives that the integral on the right hand side of (58) equals the multivariate normal density with mean _Bm_ 0 + _c_ and covariance _BQ_ 0 _B_<sup>_′_</sup> + _R_ evaluated at _xs_ (here _m_ 0 = _ms_ +1 _|t_ , _Q_ 0 = _Qs_ +1 _|t_ and _R_ = _Q_<sup>˜</sup> ). Because the left hand side of (58) is the multivariate normal density with mean _ms|t_ and _Qs|t_ , we deduce the equations


and


We shall now write these equations concisely by using the following notation. Recall that from the one-step ahead prediction updates (51), we have


Replacing the terms _As_ +1 _ms|s_ and _Qs_ +1 _|s_ = _As_ +1 _Qs|sA_<sup>_′_</sup> _s_ +1<sup>+ Σ</sup><sup>_s_+1by</sup><sup>_m_</sup> _s_ +1 _|s_<sup>and</sup><sup>_Q_</sup> _s_ +1 _|s_<sup>in</sup> the smoothing recursion equations, we get


40

Finally using the notation


we get


These are the Kalman Smoothing equations; alternatively known as the Rauch-Tung-Striebel equations. They allow the calculation of _ms|t, Qs|t_ from knowledge of _ms_ +1 _|t, Qs_ +1 _|t_ as well as from _ms|s, Qs|s, ms_ +1 _|s, Qs_ +1 _|s_ (these four quantities are obtained by running the Kalman filter). One runs these smoothing equations starting from _s_ = _t −_ 1 and decreasing _s_ all the way to zero.

### **9.4 Dealing with missing data in the context of state space models**

Consider a time series dataset _y_ 0 _, y_ 1 _, . . . , yT_ where observations corresponding to certain time points may be missing. More precisely, the data might look like _y_ 0 _, y_ 1 _, y_ 2 _,_ miss _, y_ 4 _, y_ 5 _, y_ 6 _,_ miss _, y_ 8 _, . . ._ . How does one analyze this dataset? In the context of state space models, this is quite straightforward. As usual, we use a state space model with a hidden Markov process _{Xt}_ and then connect it to the observation random variables _Y_ 0 _, Y_ 1 _, . . ._ . In contrast to the fully observed setup, we now assume that each _Yt_ takes an additional value “miss” which means that we should also model:


Modeling this probability requires us to know the missing mechanism which is quite difficult in general. A simplistic assumption is that


This is can be viewed as a “missing at random” assumption. Under this assumption, analysis is quite straightforward and the Kalman filter and smoother for the model with missing observations are obtained by a simple modification of the model without missing observations. For example, here is how to run the Kalman filter in the presence of missing observations and the missing at random assumption (59). The Kalman filter tells us about the step:


which is the one-step ahead prediction update and then about the


which is the filter update. When _yt_ is observed, both these steps are carried out as usual. However when _yt_ is missing, then there is nothing to do in the filter update so we just take the two conditional distributions in (60) to be the same (observe that the missing at random assumption is crucial here). The smoothing procedure is the same as in the fully observed case. We shall look at specific examples in the next class.

### **9.5 Recommended Reading for Today**

1. The general smoothing approach described in Section 9.2 can be found in:

   - a) Section 6.2.1 of the Kitagawa-Gersch book (in particular, see Equation (6.7))

41

   - b) Section 14.2 of the Kitagawa book.

   - c) Section 2.7.4 of the Petris-Petrone-Campagnoli book

   - d) Section 8.1 of the S¨arkk¨a book

2. The Kalman/Rauch-Tung-Striebel smoothing equations are described in all the books listed in the course outline:

   - a) Section 5.2 of the Kitagawa-Gersch book (in particular, see equation (5.6)

   - b) Section 9.3 of the Kitagawa book

   - c) Section 4.4 of the Durbin-Koopman book

   - d) Section 8.2 of the S¨arkk¨a book

   - e) Proposition 2.4 of the Petris-Petrone-Campagnoli book

   - f) Theorem 3.4 of the Triantafyllopoulos book

Section 7.2 of the Chopin-Papaspiliopoulos book also discusses the Kalman smoothing equations. They however derive the algorithm from a general Feynman-Kac formalism (see their Chapter 5). I will discuss the Feynman-Kac stuff in class a few weeks later.

3. For missing data:

   - a) See Section 2.7 of the Durbin-Koopman book for a treatment of missing observations for the local level model and Section 4.10 of the Durbin-Koopman book for a more general treatment of missing observations for linear Gaussian state space models.

   - b) See Section 9.7 of the Kitagawa book.

   - c) Section 2.7.3 of the Petris-Petrone-Campagnoli book for filtering with missing observations (also see page 62 of Petris-Petrone-Campagnoli where it is argued that no changes to the smoothing step is necessary for dealing with missing observations).

---

[← 8 Lecture Eight](09-8-lecture-eight.md) · [Up: contents](index.md) · [10 Lecture Ten →](11-10-lecture-ten.md)
