---
title: 12 Lecture Twelve
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 12 Lecture Twelve

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **12.1 Pairwise Smoothing Distributions**

In our study of smoothing algorithms, we have focussed on calculating the distribution of _Xs | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ for fixed _s ≤ t_ . For the score vector calculation (as well in the EM algorithm), we would need to calculate the conditional joint distribution of _Xs_ and _Xs_ +1 given _Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ . In the general case, this can be done via


We have seen in Lecture Nine that the first term in the right hand side above equals


We thus have


The above formula expresses the joint smoothing density of _Xs, Xs_ +1 in terms of the smoothing density of _Xs_ +1 as well filtering and transition densities.

For linear Gaussian state space models, explicit calculations can be done leading to the formula:


Here, as before, _ms|t_ and _Qs|t_ denote the mean and covariance of _Xs | Y_ 0 = _y_ 0 _, . . . , Yt, θ_ respectively. Also Γ _s_ +1 equals


52

Note that Γ _s_ +1 appears in the Kalman smoother recursions. To prove (79), we only need to verify that


This is true because (below data _t_ stands for _Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt_ )

We have seen in Lecture Nine that


which gives


where “non-random” refers to a quantity which is deterministic. Thus


This proves (81) which completes the proof of (79).

### **12.2 Fisher’s Identity (from last time)**

In the last class, we looked at the Fisher identity for the score function. The setting is that of a latent variable model that describes the joint density _fY,X|θ_ ( _y, x_ ) of two variables _Y, X_ in terms of parameters _θ_ . _Y_ is the observed variable ( _y_ is the observed data) and _X_ is the hidden or latent variable. Fisher’s identity says that


where


### **12.3 The Score Function for the Local Level Model**

Let us illustrate the Fisher identity for calculating the score function in the local level model:


53

The parameter vector here is _θ_ := ( _σZ, σϵ_ ). Let us calculate _E_ ( _θ, θ_<sup>(0)</sup> ) to calculate the score vector at _θ_<sup>(0)</sup> := ( _σZ_<sup>(0)</sup><sup>_, σ_</sup> _ϵ_<sup>(0)).Thelog-likelihoodof</sup><sup>_Y_</sup> 0<sup>_, . . . , Y_</sup> _T_<sup>_, X_</sup> 0<sup>_, . . . , X_</sup> _T_<sup>equals</sup>


Therefore


where “data” represents _Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ (this is basically data _T_ in the notation of Section 12.1). As a result

The Fisher identity therefore gives

The expectations appearing above can be calculated using the output of the Kalman smoother as shown below. Let _ms|T_ ( _θ_<sup>(0)</sup> ) and _Qs|T_ ( _θ_<sup>(0)</sup> ) denote the output of the Kalman smoother when the parameters are set to _θ_<sup>(0)</sup> . Then


where, in the last equation, we used the formula (81) for _s_ = _t −_ 1. The quantity Γ _t_ ( _θ_<sup>(0)</sup> ) equals (see (80)):


54

which can be calculated by the Kalman filter output.

Also


Observe that (86) is a closed form expression for the score function (in terms of the Kalman smoother output). Using the expression (86) for the score function, we can use standard optimization methods (such as gradient ascent or BFGS) to obtain the maximum likelihood estimator for _θ_ = ( _σZ, σϵ_ ).

### **12.4 The EM Algorithm**

The EM algorithm is another method for maximizing the log-likelihood log _fY |θ_ ( _y_ ) over _θ_ in latent variable models. It is also an iterative algorithm. The EM update


consists of the following two steps:

1. **E-Step** : Calculate _E_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) (this is (83) with _θ_<sup>(0)</sup> replaced by _θ_<sup>(</sup><sup>_n_)</sup> ).

2. **M-Step** : Take _θ_<sup>(</sup><sup>_n_+1)</sup> to be the maximizer of _E_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) over _θ_ .

Some intuition behind this algorithm will be provided in the next class.

### **12.5 EM for the local level model**

For the local level model, the expression for _E_ ( _θ, θ_<sup>(0)</sup> ) as well as _∇θE_ ( _θ, θ_<sup>(0)</sup> ) ���� _θ_ = _θ_<sup>(0)are</sup> calculated in Section 12.3 (see (84) and (85)). Using these, we can immediately write down the EM iterate in closed form. Indeed, _θ_<sup>(</sup><sup>_n_+1)</sup> is obtained by maximizing _E_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) over _θ_ . Setting the gradient of _E_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) (calculated in (85)) to zero, we can immediately deduce that

and


This is a very easy update (there are no line searches for step size selection) and thus the EM is very popular for state space models.

55

### **12.6 Calculation of** _E_ ( _θ, θ_<sup>(0)</sup> ) **for general state space models**

For a general state space model,


Observe that the right hand side above involves three kinds of quantities: the observed data _y_ 0 _, . . . , yT_ , the parameters _θ_ and the quantities _x_ 0 _, . . . , xT_ . From here, to obtain _E_ ( _θ, θ_<sup>(0)</sup> ), we leave _y_ 0 _, . . . , yT , θ_ unchanged in the right hand side and take the expectation over _x_ 0 _, . . . , xT_ conditional on _y_ 0 _, . . . , yT_ . This conditional expectation depends on parameters and we shall fix the parameters at _θ_<sup>(0)</sup> (as opposed to the _θ_ that is already appearing on the right hand side). We can thus write


where


and


and


Note that _I_ 3( _θ, θ_<sup>(0)</sup> ) involves expectation with respect to the conditional distribution


and _I_ 1( _θ, θ_<sup>(0)</sup> ) involves expectation with respect to the above conditional distribution for _t_ = 0. These conditional distributions are obtained from the smoothing algorithm. Further _I_ 2( _θ, θ_<sup>(0)</sup> ) involves expectation with respect to


which can be obtained from the pairwise smoothing algorithm of Section 12.1.

For linear Gaussian state space models, _I_ 1( _θ, θ_<sup>(0)</sup> ) _, I_ 2( _θ, θ_<sup>(0)</sup> ) _, I_ 3( _θ, θ_<sup>(0)</sup> ) can be computed in closed form in terms of the output of the Kalman smoothing algorithm. The details of this calculation are given in Theorem 12.4 of the S¨arkk¨a book. Often maximization of _E_ ( _θ, θ_<sup>(0)</sup> ) can also be done in closed form for linear Gaussian state space models (see Theorem 12.5 of the S¨arkk¨a book).

56

### **12.7 Recommended Reading for Today**

1. The pairwise smoothing distributions for the linear Gaussian state space model are described in the proof of Theorem 8.2 of the S¨arkk¨a book.

2. The EM algorithm is described in Section 12.2.3 of the S¨arkk¨a book, Section 2.4.2 of the Triantafyllopoulos book, and Section 14.1.3 of the Chopin-Papaspiliopoulos book.

3. The EM algorithm for the local level model is given in Example 14.1 of the ChopinPapaspiliopoulos book.

4. More details on the EM algorithm for linear Gaussian state space models are given in Section 12.3.2 of the S¨arkk¨a book.

---

[← 11 Lecture Eleven](12-11-lecture-eleven.md) · [Up: contents](index.md) · [13 Lecture Thirteen →](14-13-lecture-thirteen.md)
