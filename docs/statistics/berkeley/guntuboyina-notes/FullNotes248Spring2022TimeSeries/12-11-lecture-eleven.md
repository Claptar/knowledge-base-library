---
title: 11 Lecture Eleven
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 11 Lecture Eleven

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We shall discuss optimization algorithms for maximum likelihood estimation for state space models. We start with a general discussion of optimization algorithms before specializing to the case of state space models.

### **11.1 Basic Optimization Algorithms**

The goal is to maximize a function _F_ ( _θ_ ) over _θ_ . Optimization algorithms are iterative and output a sequence of values _θ_<sup>(0)</sup> _, θ_<sup>(1)</sup> _, . . ._ which is supposed to converge to a (local) maximizer of _F_ . We shall describe briefly three standard optimization algorithms: Gradient Ascent, Newton’s method and BFGS.

#### **11.1.1 Gradient Ascent**

Given the current iterate _θ_<sup>(</sup><sup>_n_)</sup> , consider the first order Taylor expansion of _F_ near _θ_<sup>(</sup><sup>_n_)</sup> :


This suggests that _F_ ( _θ_ ) _≥ F_ ( _θ_<sup>(</sup><sup>_n_)</sup> ) provided


46

which will be satisfied when


Motivated by this, the gradient ascent update is


The quantity _αn_ is called the step-size and the best way to choose it (which guarantees improvement in function values) is to maximize the quantity


The above one-parameter maximization can be done by a line search.

#### **11.1.2 Newton’s Method**

Given the current iterate _θ_<sup>(</sup><sup>_n_)</sup> , consider the second order Taylor expansion of _F_ near _θ_<sup>(</sup><sup>_n_)</sup> :


The maximizer of the right hand side above can be calculated in closed form as:


This motivates setting


where again _αn_ is chosen to maximize the quantity


Note that it is important that _−HF_ ( _θ_<sup>(</sup><sup>_n_)</sup> must be positive semi-definite for the quadratic approximation (70) to have a well-defined maximum (otherwise, its maximum will be + _∞_ ).

Newton’s method works very well when initialized reasonably close to the actual maximizer of _F_ . But one needs to calculate the Hessian matrix _HF_ ( _θ_<sup>(</sup><sup>_n_)</sup> ) which may be difficult on impossible in some applications.

#### **11.1.3 Quasi-Newton Method: BFGS**

Quasi-Newton methods mimic the Newton update (71) without explicitly including Hessian matrices. Instead the idea is to have approximate Hessians and update them at each step. The most popular of these methods is BFGS (Broyden-Fletcher-Goldfarb-Shanno) and this method works as follows. At each step of the procedure, the current estimate of the maximizer _θ_<sup>(</sup><sup>_n_)</sup> is updated to the next value _θ_<sup>(</sup><sup>_n_+1)</sup> and the current approximate Hessian matrix _H_<sup>(</sup><sup>_n_)</sup> is also updated to the next value _H_<sup>(</sup><sup>_n_+1)</sup> . The update _θ_<sup>(</sup><sup>_n_)</sup> _→ θ_<sup>(</sup><sup>_n_+1)</sup> is exactly the same as (71) with _HF_ ( _θ_<sup>(</sup><sup>_n_)</sup> ) replaced by the current Hessian approximation _H_<sup>(</sup><sup>_n_)</sup> :


47

where, as before, _αn_ is chosen to maximize the quantity


The update for the Hessian is given by (we are assuming that each _−H_<sup>(</sup><sup>_n_)</sup> is symmetric and positive definite)


where

_s_ := _θ_<sup>(</sup><sup>_n_+1)</sup> _− θ_<sup>(</sup><sup>_n_)</sup> and _g_ := _∇F −∇F ._ � _θ_<sup>(</sup><sup>_n_+1)�</sup> � _θ_<sup>(</sup><sup>_n_)�</sup>

The Hessian update can also be written in terms of ( _H_<sup>(</sup><sup>_n_)</sup> )<sup>_−_1</sup> :


This is useful because the _θ_ -update (72) is written in terms of the inverse of _H_<sup>(</sup><sup>_n_)</sup> .

Here is some intuition behind the Hessian update (73) (or, equivalently, (74)). It is easy to check that _H_<sup>(</sup><sup>_n_+1)</sup> _s_ = _g_ which is same as


This is a reasonable condition to insist because _H_<sup>(</sup><sup>_n_+1)</sup> is supposed to approximate _HF_ ( _θ_<sup>(</sup><sup>_n_+1)</sup> ). Observe that when the dimension equals 1, the equality _H_<sup>(</sup><sup>_n_+1)</sup> _s_ = _g_ is the same as


The matrix _H_<sup>(</sup><sup>_n_+1)</sup> defined by (73) is actually the solution to the following optimization problem:

where


Here _d_ is the dimension of _θ_ (note that each _H_ is _d×d_ ). The above expression _D_ ( _X∥H_ ) is the Kullback-Leibler divergence between the multivariate normal distribution with covariance _X_ and the multivariate normal distribution with covariance _H_ . At a high level, _H_<sup>(</sup><sup>_n_+1)</sup> should be understood as the closed matrix to _H_<sup>(</sup><sup>_n_)</sup> (measured in terms of the divergence _D_ ( _·∥H_<sup>(</sup><sup>_n_)</sup> )) subject to the condition _H_<sup>(</sup><sup>_n_+1)</sup> _s_ = _g_ . It is standard to initialize _H_<sup>(0)</sup> with the identity matrix.

Observe that in order to apply the gradient ascent and the BFGS methods, it is necessary to be able to compute the gradients of _F_ . To apply the Newton method, one also needs to compute the Hessian of _F_ .

If you want to learn more about these optimization algorithms, you can read standard books on nonlinear optimization; I can recommend _Numerical Optimization_ by Nocedal and Wright, or the first chapter of _Introductory Lectures on Convex Optimization_ by Nesterov, or _Iterative Methods for Optimization_ by Kelley.

48

### **11.2 Application to Maximum Likelihood Estimation in State Space Models**

We shall apply the optimization algorithms for obtaining maximum likelihood estimates in state space models. The function _F_ in the previous section will now be the log-likelihood function. We have seen that it can be calculated for state space models by filtering (in particular, the Kalman filter can be used for likelihood computation in linear Gaussian state space models). As we saw in the previous section, gradient ascent and BFGS require gradient evaluations. We thus need to calculate the gradient of the log-likelihood function in state space models. One often uses the term _score vector_ or _score function_ for the gradient of the log-likelihood function.

For calculating the score vector in state space models (and more generally in latent variable models), it is convenient to use the Fisher identity which we shall describe next.

#### **11.2.1 Fisher Identity for the Score**

Consider a general latent variable model which describes the joint density _fY,X|θ_ ( _y, x_ ) of two variables _Y, X_ in terms of parameters _θ_ . Here _Y_ denotes the observed variable (the observed data from _Y_ will be denoted by _y_ ) and _X_ denotes the hidden or latent variable (we will not be observing any specific realizations _x_ corresponding to _X_ ). This setting is quite general and includes the state space model as special case. For state space models, _Y_ = ( _Y_ 0 _, . . . , YT_ ) and _X_ = ( _X_ 0 _, . . . , XT_ ).

The likelihood of the observation _y_ is simply equal to the density of _Y_ at _y_ :


viewed as a function of the parameters _θ_ . Generally in latent variable models, _fY |θ_ ( _y_ ) is harder to evaluate compared to _fY,X|θ_ ( _y, x_ ). Our goal here is to calculate the score function (gradient of the log-likelihood) at a specific parameter value _θ_<sup>(0)</sup> . More precisely, we want to calculate:


Fisher’s identity provides a formula for the score in terms of _fY,X|θ_ :

**Fact 11.1** (Fisher’s Identity) **.** _For every θ_<sup>(0)</sup> _and y, we have_


_where_


_Proof._ Fix _θ_<sup>(0)</sup> and _y_ . Note that for every _x_ ,


which can be rewritten as


49

We now integrate both sides of the above equality with respect to the probability density


Note that the function _x �→ q_ ( _x_ ) depends on _y_ and _θ_<sup>(0)</sup> but it does not depend on the generic parameter value _θ_ appearing in (77). Integrating both sides of (77) with respect to _q_ ( _x_ ) (note that the left hand side of (77) does not depend on _x_ ), we get


We now take the gradient on both sides with respect to _θ_ and evaluate the gradient at _θ_ = _θ_<sup>(0)</sup> . This leads to


Thus, to complete the proof of (82), it is enough to show that the last term above equals zero. This is true because


Note that at two places in the above chain of equalities, we interchanged the operations of differentiation (with respect to _θ_ ) and integration (with respect to _x_ ).

As we shall see in the next class, the quantity _E_ ( _θ, θ_<sup>(0)</sup> ) also appears in the EM algorithm. We shall often write it as


The notation on the right hand side needs to be understood correctly. The parameter _θ_ appearing in log _fY,X|θ_ ( _y, X_ ) will remain as _θ_ (i.e., it will not be replaced by _θ_<sup>(0)</sup> ). E _θ_ (0) represents expectation over _X_ with respect to the density _fX|Y_ = _y,θ_ = _θ_ (0).

50

**11.2.2** _E_ ( _θ, θ_<sup>(0)</sup> ) **for state space models**

For state space models,


Observe that the right hand side above involves three kinds of quantities: the observed data _y_ 0 _, . . . , yT_ , the parameters _θ_ and the quantities _x_ 0 _, . . . , xT_ . From here, to obtain _E_ ( _θ, θ_<sup>(0)</sup> ), we leave _y_ 0 _, . . . , yT , θ_ unchanged in the right hand side and take the expectation over _x_ 0 _, . . . , xT_ conditional on _y_ 0 _, . . . , yT_ . This conditional expectation depends on parameters and we shall fix the parameters at _θ_<sup>(0)</sup> (as opposed to the _θ_ that is already appearing on the right hand side). We can thus write


where


and


and


Note that _I_ 3( _θ, θ_<sup>(0)</sup> ) involves expectation with respect to the conditional distribution


and _I_ 1( _θ, θ_<sup>(0)</sup> ) involves expectation with respect to the above conditional distribution for _t_ = 0. These conditional distributions are obtained from the smoothing algorithm. Further _I_ 2( _θ, θ_<sup>(0)</sup> ) involves expectation with respect to


which can also be obtained from the smoothing algorithm (we shall see the reasoning behind this in the next class).

For the linear Gaussian state space models, _I_ 1( _θ, θ_<sup>(0)</sup> ) _, I_ 2( _θ, θ_<sup>(0)</sup> ) _, I_ 3( _θ, θ_<sup>(0)</sup> ) can be computed in closed form in terms of the output of the Kalman smoothing algorithm. It is also possible to obtain closed form expressions for the gradient of _E_ ( _θ, θ_<sup>(0)</sup> ). This is a nice way of computing the score function in linear Gaussian state space models using the Kalman smoother output. We shall see the details in the next class.

51

### **11.3 Recommended Reading for Today**

1. Some references for an in-depth coverage of optimization algorithms are the books _Numerical Optimization_ by Nocedal and Wright, or the first chapter of _Introductory Lectures on Convex Optimization_ by Nesterov, or _Iterative Methods for Optimization_ by Kelley.

2. For a quick review of optimization algorithms with the goal of applying them to parameter estimation in state space models, see Section 7.3 of the Durbin-Koopman book, Section 14.4 of the Chopin-Papaspiliopoulos book, and Appendix A of the Kitagawa book.

3. Fisher’s identity can be found in Section 7.3.3 of the Durbin-Koopman book (although they don’t call it the Fisher identity), and Exercise 12.5 of the Chopin-Papaspiliopoulos book, and Equation (12.32) in the S¨arkk¨a book.

4. For the formula (87), see equations (12.29) and (12.30) of the S¨arkk¨a book.

---

[← 10 Lecture Ten](11-10-lecture-ten.md) · [Up: contents](index.md) · [12 Lecture Twelve →](13-12-lecture-twelve.md)
