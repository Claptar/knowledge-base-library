---
title: Intuition behind the SRA
source: https://vanderlaan-lab.org/teach-files/survMSM2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/survMSM2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Intuition behind the SRA

**Source:** [`survMSM2004.pdf`](https://vanderlaan-lab.org/teach-files/survMSM2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Intuitively the SRA means that: the way a treatment variable is assigned at each time point in _Reality_ using the full data, also called the treatment mechanism, should only depend on **PAST OBSERVED** variables, i.e. in particular it cannot depend on unobserved confounders.

The SRA implies that we had enough information to predict at each time point the treatment received (based one the full data) using the past observed variables at that time only. Thus, the SRA is an assumption dealing with the information available in the observed data. It can be viewed as one of the minimal assumptions that insures that there is enough information in the observed data _O_ to identify a parameter (like _β_ ) defined using the unavailable full data _X_ .

Romain Neugebauer - 17

### **Estimating** _β_ **: a missing data approach**

Three estimators developed for missing data problems can be used to estimate causal effects like _β_ under the SRA assumption. Under the SRA assumption, the likelihood factorizes into two parts:


Under the SRA, we denote the distribution of _O_ , _P_ , with _PFX,g_ .

Thus the three estimators of _β_ can rely on models for different part of the observed likelihood:

- Inverse Probability of Treatment Weighted (IPTW) estimator

- G-computation (G-comp) estimator

- Double Robust (DR) estimator.

- _−→_ We focus on the IPTW estimator of _β_ in this presentation.

Romain Neugebauer - 18

#### **The IPTW estimator: definition**

###### **Definition:**

The IPTW estimating function for _β_ with nuisance parameter _g_ is defined as:

_Dh_ ( _O | g, β_ ) =<sup>_h_</sup><sup><u>( ¯</u></sup><sup>_A, V_</sup><sup><u>)</u></sup><sup>_ϵ_</sup><sup><u>(</u></sup><sup>_<u>β</u>_</sup><sup><u>)</u></sup> where _ε_ ( _β_ ) = log _T − m_ ( _A, V_<sup>¯</sup> _| β_ ) _. g_ ( _A_<sup><u>¯</u></sup> _| X_ )

Note that the IPTW estimating function is indeed a function of the observed data under the SRA.

We denote the estimator of the nuisance parameter _g_ with _gn_ .

The IPTW estimator of _β_ is defined as the solution of the estimating equation associated with the observed data _O_ and the IPTW estimating function at _gn_ :

_n_ � _i_ =1<sup>_Dh_(</sup><sup>_oi| gn, β_) = 0</sup><sup>_,_</sup>

where _oi_ for _i_ = 1 _, . . . , n_ represents the _n_ i.i.d. observed data.

observations in the

Romain Neugebauer - 19

#### **Property of the IPTW estimator**

The IPTW estimating function is unbiased at _β_ :


if the Experimental Treatment Assignment (ETA) assumption holds:


- ” _at each time point, treatments are NOT DETERMINISTICALLY assigned according to observed covariate values_ ”

_−→_ More than required to hold in theory: it cannot be practically violated

If _gn_ is a consistent estimator of _g_ and the ETA assumption holds for _g_ then the IPTW estimator is asymptotically linear and thus consistent.

_−→_ the consistency of the IPTW estimator relies on correct specification of the _g_ part of the likelihood AND the ETA assumption

Romain Neugebauer - 20

#### **Property of the IPTW estimator**

###### **Proof:**


where _εa_ ¯( _β_ ) = log _Ta_ ¯ _− m_ (¯ _a, V | β_ ) and _ε_ ( _β_ ) = _εA_ ¯( _β_ ) under the consistency assumption.

Romain Neugebauer - 21

#### **The IPTW estimator: implementation**

The IPTW estimate of _β_ can be obtained in practice by performing a weighted least squares regression of _Y_ on _A_<sup>¯</sup> and _V_ using the MSM and weights inversely proportional to the treatment mechanism:


where _λ_ can be any non-null function of _A_<sup>¯</sup> and _V_ .

It can indeed be shown that the resulting estimate is a solution of the IPTW estimating equation where _h_ (¯ _a, V_ ) = _λ_ (¯ _a, V_ )<sup>_<u>d</u>_</sup> _<u>dβ</u>_<sup>_m_(¯</sup><sup>_a, V| β_).</sup>

Romain Neugebauer - 22

#### **The IPTW estimator: implementation**

Robins, Hernan and Brumback recommended the following choice for _λ_ : _λ_ ( _A, V_<sup>¯</sup> ) = _g′_ ( ¯ _A | V_ ) where _g′_ is the conditional distribution of _A_ ¯ given _V_ :

- to improve the efficiency of the IPTW estimator (more stable weights)

_•_ to be consistent with the naive estimation approach we would use if we know the treatment is randomized per strata of _V_ . _<u>n</u>_<sup><u>(</u></sup><sup>_A_¯</sup><sup>_<u>|V</u>_</sup><sup><u>)</u></sup> The resulting weights are called stabilized weights: _w_ ( _A, V_<sup>¯</sup> ) =<sup>_<u>g′</u>_</sup> _gn_ ( _A_<sup>~~¯~~</sup> _|X_ )<sup>_._</sup>

In addition, it was shown, see van der Laan and Robins (2002), that _g_ should always be estimated even when _g_ is known. As a result, the IPTW estimator may gain in efficiency by taking into account possible empirical confounding, without loss of consistency.

Romain Neugebauer - 23

#### **The IPTW estimator: implementation**

Do not trust the standard errors provided by the weighted regression routines in standard statistical package.

They assume the weights provided are known, i.e. not estimated. The resulting confidence intervals would be conservative.

Use the bootstrap to obtain correct standard errors and confidence intervals or calculate them with the influence curve of the IPTW estimator you used.

Romain Neugebauer - 24

#### **The IPTW estimator**

**An intuitive understanding of the IPTW estimator?**

The IPTW estimator can be viewed intuitively as a ”smart” weighted regression accomplishing two steps simultaneously:

1. Modify the original data such that the treatment is randomized in the ghost data artificially created by the weights: importance of the SRA, ETA assumptions and the models for the weights.

2. Estimate _β_ using a simple (unweighted) mean regression of _Y_ on _A_ using the MSM and the ghost data.

Romain Neugebauer - 25

#### **Importance of the ETA assumption: violation AND practical violation**

Illustration by simulations:


<!-- Start of picture text -->
Y 0 (unobserved)<br>� @<br>� � @<br>@<br>W @<br>MSM: E (log  Ta ) = 2  − 5 a<br>� @<br>� � @@R<br>A - T<br><!-- End of picture text -->

To obtain one data set with _N_ observations, repeat _N_ times:

1. Generate _Y_ 0 _∼U_ [ _−_ 10 _,_ 10]

2. Generate _W ∼N_ (<sup>_<u>Y</u>_</sup> <u>3</u><sup><u>0</u></sup><sup>_,_1)</sup>

3. Generate _A_ using _g_ ( _A | W_ )

4. Generate log _T ∼N_ (2 + 4 _Y_ 0 _−_ 5 _A,_ 1)

One generates 500 data sets for each _g_ considered and each sample size _N_ = 100 _,_ 200 _,_ 300 _,_ 400 _,_ 500 _,_ 1000 _,_ 2000 _,_ 100000 _._

_−→_ For each data set, one estimates _β_ = (2 _,_ 5) using the IPTW and reports the mean estimates per _g_ and _N_ considered.

Romain Neugebauer - 26

#### **Binary treatment and logistic treatment mechanism**


<!-- Start of picture text -->
p1=logit(1+1.5w) p2=logit(0.5+w)<br>.. ...... 0.950.05 ........ ................ ................ . ........................................ . ........................ . ................ ..... ............................... . ....... . . .. . 0.950.05 ...................... ....................... . .................... . ....... . .................... .. ............................. ....... .................... . ....... . .<br>-6 -4 -2 0 2 4 6 -6 -4 -2 0 2 4 6<br>W W<br>p3=logit(1.5+0.5w) p4=logit(0.1+0.25w)<br>.. ... .. .. . . ...... . ..... 0.95 ................... . .......... . .... . .... . ........................ ............... .............. . ....... . . .. ... .. .. . ..... .. ............... . ....... . .... .. 0.95 ................................................. . .. . ....... . .<br>0.05 0.05<br>-6 -4 -2 0 2 4 6 -6 -4 -2 0 2 4 6<br>W W<br>−→ the ETA assumption becomes less practically violated as we go<br>from model 1 to 4<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>p1 p2<br>0.4 0.4<br>0.2 0.2<br>0.0 0.0<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>p3 p4<br>0.4 0.4<br>0.2 0.2<br>0.0 0.0<br><!-- End of picture text -->

Romain Neugebauer - 27

#### **Comparison of the four estimators: bias**


<!-- Start of picture text -->
Model 1 Model 2 Model 3 Model 4<br>4 1-step 4 4 4<br>DR 1-step<br>2 G 2 DRG 2 DRG 1-step 2 G, IPTW, 1-step and DR<br>IPTW<br>IPTW<br>0 IPTW 0 0 0<br>-2 -2 -2 -2<br>-4 -4 -4 -4<br>// // // //<br>0 500 1,000 2,000 100,000 0 500 1,000 2,000 100,000 0 500 1,000 2,000 100,000 0 500 1,000 2,000 100,000<br>sample size sample size sample size sample size<br>Model 1 Model 2 Model 3 Model 4<br>5 5 5 5<br>3 3 3 3<br>1 1 1 1<br>-1 -1 -1 -1<br>IPTW<br>-3 -3 -3 -3<br>-5 G -5 DRG 1-stepIPTW -5 DRG 1-stepIPTW -5 G, IPTW, 1-step and DR<br>DR<br>-7 1-step -7 -7 -7<br>-9 -9 -9 -9<br>// // // //<br>0 500 1,000 2,000 100,000 0 500 1,000 2,000 100,000 0 500 1,000 2,000 100,000 0 500 1,000 2,000 100,000<br>sample size sample size sample size sample size<br>intercept intercept intercept intercept<br>slope slope slope slope<br><!-- End of picture text -->

Romain Neugebauer - 28

#### **Categorical treatment and multinomial treatment mechanism**

###### p0=1/[1+exp(0.5w)+exp(1.5w)]

###### p1=p0exp(0.5w)


<!-- Start of picture text -->
. . ... . ....... ................. 0.950.05 .................. . .......................................... . .......................... .............. .................... .. . .. . . .. . . . ........... . .................. . ........... 0.05 ........... . ................... . ............................ .. ................................. . .............. . ................ . ... . ..................... ...... .................... .. . ..<br>-6 -4 -2 0 2 4 6 -6 -4 -2 0 2 4 6<br>w w<br>1.0<br>0.3<br>0.8<br>0.6<br>0.2<br>p0 p1<br>0.4<br>0.1<br>0.2<br>0.0 0.0<br><!-- End of picture text -->

###### p2=p0exp(1.5w)


<!-- Start of picture text -->
. .... .0.950.05 ................... ............... ........................................................................................ . ............. ....... ..................... .. . ..<br>-6 -4 -2 0 2 4 6<br>w<br>1.0<br>0.8<br>0.6<br>p2<br>0.4<br>0.2<br>0.0<br><!-- End of picture text -->

##### _−→_ the ETA assumption is practically violated

Romain Neugebauer - 29

#### **Comparison of the four estimators: bias**


<!-- Start of picture text -->
4<br>1-step<br>DR<br>2<br>G<br>IPTW<br>0<br>-2<br>/ /<br>0 500 1,000 2,000 100,000<br>sample size<br>intercept<br><!-- End of picture text -->


<!-- Start of picture text -->
0<br>-1<br>-2<br>-3<br>IPTW<br>-4<br>G<br>-5<br>DR<br>-6 1-step<br>-7<br>-8<br>/ /<br>0 500 1,000 2,000 100,000<br>sample size<br>slope<br><!-- End of picture text -->

Romain Neugebauer - 30

#### **Continuous treatment and gaussian treatment mechanism**


<!-- Start of picture text -->
A ∼N ( W − 1 ,  1)<br><!-- End of picture text -->


<!-- Start of picture text -->
10<br>8 IPTW<br>6<br>4<br>G<br>2<br>DR<br>0<br>-2<br>1-step<br>-4<br>-6<br>/ /<br>0 500 1,000 2,000 100,000<br>sample size<br>intercept<br><!-- End of picture text -->


<!-- Start of picture text -->
3<br>2<br>1<br>IPTW<br>0<br>-1<br>-2<br>-3<br>-4 G<br>-5<br>-6 DR<br>-7<br>-8<br>-9<br>1-step<br>-10<br>-11<br>/ /<br>0 500 1,000 2,000 100,000<br>sample size<br>slope<br><!-- End of picture text -->

_−→_ The IPTW estimates are still biased at _N_ = 100000!

Romain Neugebauer - 31

#### **Importance of the ETA assumption**

These simulation results should convince you of the importance of checking the validity of the ETA assumption in practice. A visual check of the validity of the ETA assumption can be performed by plotting y) the observed treatment or predicted probability of treatment against x) the linear part of the treatment mechanism model.

The resulting plot should demonstrate that for any value of the covariates in the treatment mechanism model all treatment regimen are possible with a probability different enough from 0 or 1 (e.g. _≥_ 0 _._ 1 and _≤_ 0 _._ 9).

Romain Neugebauer - 32

#### **Generalization of the approach to censored data**

We assume in this presentation that all events are observed for all subject in the data set.

In practice, censoring makes the problem more complex however the approach and the tools used to estimate causal effects remain the same.

Example of right censoring: Censoring, _C_ , is treated as another treatment variable and the counterfactuals are defined using a joint treatment _A_ ( _t_ ) = ( _A_ 1( _t_ ) _, A_ 2( _t_ )) where _A_ 1( _t_ ) corresponds with the treatment of interest and _A_ 2( _t_ ) = _I_ ( _C ≤ t_ ) and the MSM becomes:

_E_ (log _Ta_ ¯1 _,a_ ¯2=0 _| V_ ) = _m_ (¯ _a_ 1 _, V | β_ )

Romain Neugebauer - 33

#### **Other estimators**

With or without censoring, the IPTW estimator fails to provide unbiased estimates of causal parameters of interest when the ETA assumption is violated or practically violated.

Other estimators should then be used. Two alternate estimators are possible: the G-computation and Double Robust (DR) estimators. They rely on the other part of the likelihood: the _FX_ part (and on the _g_ part of the likelihood as well for the DR).

Romain Neugebauer - 34

---

[← The Sequential Randomization Assumption](02-the-sequential-randomization-assumption.md) · [Up: contents](index.md)
