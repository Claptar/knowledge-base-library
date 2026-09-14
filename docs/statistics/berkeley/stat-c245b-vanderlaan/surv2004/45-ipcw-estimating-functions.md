---
title: IPCW-estimating functions
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# IPCW-estimating functions

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Define the full data estimating functions as:


The IPCW estimate is


where _G_<sup>¯</sup> ( _T | X_ ) = exp<sup>_−_�</sup> 0<sup>inf</sup> _λC_ ( _s|X_ )if C is continuous and _G_<sup>¯</sup> ( _T | X_ ) =<sup>�</sup> _s∈_ (0 _,t_ )<sup>(1</sup><sup>_−λC_</sup> _X_<sup>(</sup><sup>_s | X_))ingeneral.</sup>

Suppose _Dh_ ( _X, µ | η_ ) = � _h_ ( _t, Z_<sup>¯</sup> ( _t_ )) _∂Mβ,λ_ 0 where _∂Mβ,λ_ 0 = _∂N_ ( _t_ ) _− E_ [ _∂N_ ( _t_ ) _| N_<sup>¯</sup> ( _t−_ ) _, Z_<sup>¯</sup> ( _t_ )]

� _h_ ( _t, Z_<sup>¯</sup> ( _t_ )) is like the sum of unbiased estimates Use Inverse Weighting


59

This corresponds to every line getting weight _G_<sup>¯</sup> ( _t | X_ ) These weights are time dependent

In the continuous case, could use Cox PH with weights.

In discrete case (using logistic regression): Define _N_ ( _t_ ) = _I_ ( _T ≤ t_ ) as the risk of jumping at time t


The optimal estimating function for logistic regression is:


Which can alternatively be written as:


If events only happen at certain time points, glm solves this equation. This is in the Full data world (No Censoring) Suppose _N_ ( _t_ ) is a repeated process


where _f_ ( _N_<sup>¯</sup> ( _tj_ )) is a function of the past This is efficient in the full data world.

Suppose the counting process is not observed until the end of the study That it was Censored in a random manner. IPCW:


Suppose the data was of the form:

|_∂N_(_tj_)|_tj_|Z|_W_(_tj_)|
|---|---|---|---|
|0|.|.|.|
|0|.|.|.|
|1|.|.|.|
|0|.|.|.|
|...|...|...|...|


60

In any software package, use GLM (logistic link) Add weights to deal with censoring

Emperical mean of Estimating Equation


This maps full data _⇒_ observed data The mapping depends on the censoring mechanism.

Example: Suppose we wish to estimate the Marginal Survival function


There are three possible approaches

1. Use Kaplan-Meier to estimate _µ_

2. Use Kaplan-Meier to estimate _G_<sup>¯</sup>

3. Use Cox PH to estimate _G_<sup>¯</sup>

The third method is the most efficient, especially when there are covariates Example:

Suppose age is a covariate Censoring is completely independent One should still include covariates important to the outcome in the model for _G_<sup>¯</sup> . Software Confidence Intervals are conservative (computed as if _G_<sup>¯</sup> known)

To get better Confidence Intervals either compute the Influence Curve or do the Bootstrap

#### **Multiplicative Intensity Models**

Matthew Sylvester April 28, 2004

**Counting Processes** Data: ( _T_<sup>�</sup> = min( _T, C_ ) _,_ ∆= _I_ ( _T ≤ C_ ) _, X_<sup>¯</sup> ( _T_<sup>�</sup> )), where _T_ is the endpoint, _C_ is the censoring time and _X_<sup>¯</sup> ( _T_<sup>�</sup> ) is any data that might be collected on a person until time _T_<sup>�</sup> .

Suppose _X_ ( _t_ ) = ( _N_ 1<sup>_∗_(</sup><sup>_t_)</sup><sup>_, . . . , N ∗_</sup> _k_<sup>(</sup><sup>_t_)</sup><sup>_, L_(</sup><sup>_t_))</sup><sup>_,_</sup>

where _Nh_ ( _t_ ) is a counting process, h=1,. . . ,k denotes the index of that process and _∗_ denotes that it is based on the full data. _L_ ( _t_ ) is a time-dependent covariate process. Note that there might be several jumps when moving to the next state and that all counting processes stop jumping at _T._ That is, _Nh_<sup>_∗_(</sup><sup>_t_) =</sup><sup>_N ∗_</sup> _h_<sup>(</sup><sup>_min_(</sup><sup>_t, T_))</sup><sup>_._</sup>

61

#### **Examples**

1. _Consider multiple counting processes_


where _T_ 1 _, . . . , Tk_ refer to distinct counting processes (i.e. the time to certain events). For example, _T_ 1 might refer to the time to AIDS while _T_ 2 refers to the time to death. This might mean that the first process jumps when AIDS is contracted and that the second process jumps at death or _T_ .

2. _Now consider just one counting process_


that jumps whenever the events occur. For example, for asthmatic children, _T_ 1 might be the time to the first attack, _T_ 2 might be the time to the second attack, etc.

3. _Consider the Simplest Case_


that jumps at death.

#### **Observed Data**


We have the history:


When _t_ = _∞_ , we see the full data past.

**Multiplicative Intensity Models** Suppose we have coarsening at random (CAR). We can get an intensity with respect to history when we are trying to model the probability of a counting process jumping given the past:

_Nh_ with history _F_ ( _t_ ) :


For _t < T_ ,


62

which is reasonable if censoring is only determined by the past. Then the intensity of the observed counting process is:


where we are conditioning on the full data past, and the censoring only depends on the past. We are assuming censoring does not depend on covariates not included, but this assumption becomes weaker as more covariates are put in the past. Note that the multiplicative intensity model can only be applied to the individual counting processes, of which every subject might have several (failure, infection, etc.)

If there are no covariates, the baseline hazard of dying now given that the person has not died yet and censoring has not occurred yet is given by:


which is what we would estimate with the Cox proportional hazards model with no covariates. If there is independent censoring, this reduces to _P_ ( _T_ = _t | T ≥ t_ ) _._

Now, if we would like to estimate the intensity with respect to a subset of the past:


where ( _Nh_ ( _t_ ) _, Z_ ( _t_ ) _⊂ X_ ( _t_ )).

If censoring is independent of the past, this is consistent, but inefficient. If we have CAR for the original data, we can use IPCW:


Or,


where we use cox proportional hazards to model the hazard of censoring mechanism. However, even when it is known that this is one, we should still estimate because it is more efficient.

Now, when we are adjusting for the entire past, the IPCW is not necessary. We implement it when we have just Z(t) where Z(t) is not the whole past. For example, we might just have the

63

treatment arm. Now, for the partial likelihood approach, we need to throw in everything that might be informative of censoring. We need to keep adjusting for confounding.

**More on Multiplicative Intensity Models** When the counting process is continuous(i.e. it can jump at any point in time), assume:


where _Yh_ ( _t_ ) is defined as the indicator that _Nh_ ( _t_ ) is still at risk of jumping at time t, _F_ ( _t_ ) indicates the past, _λ_ 0 _h_ ( _t_ ) indicates the baseline hazard, _Zh_ ( _t_ ) is a function of _F_ ( _t_ ), and is composed of covariates thought predictive of the counting process jumping, and _βh_ denotes the regression coefficients.

For the special case of proportional hazards with one counting process and setting the history of censoring equal to _A_<sup>¯</sup> ( _min_ ( _t, T_<sup>�</sup> ) :


where we are only adjusting for the baseline covariates.

Then,


which is the Cox proportional hazards model. Then, Cox proportional hazards assumes that _λT |W_ ( _t | W_ ) = _λ_ 0( _t_ ) _exp_ ( _βW_ ), a proportional hazards assumption. The ratio of two will not be dependent on time, a restrictive assumption. Our method is more general, and we do not need to make this assumption. Then W can be a function of time. This means that we can do data-adaptive work by pluggin on other basis functions for W, etc.

**Maximum Likelihood Estimation** We are interested in estimating the baseline hazards and coefficients _β_ .

Give every counting process its own covariates. Then, we can create a long vector that has the real values when counting process 1 occurs and 0’s when counting process 2 occurs, for example.


where we choose the covariate so that it reduces to what is wanted.

64

**Example** We have _β_ 1 _W_ 1 and _β_ 2 _W_ 2. Then, set _Z_ 1 = ( _W_ 1 _,_ 0), _Z_ 2 = (0 _, W_ 2), and _β_ = ( _β_ 1 _, β_ 2) We then have,


The partial likelihood of ( _N_ 1 _, . . . , Nk_ ) with respect to _F_ ( _t−_ ) is defined as:


where:


and


If something jumps, we use the intensity of the counting process; otherwise, we use one minus the intensity.

So, for the maximum likelihood estimate over the parameter fixing the coefficients and maximizing over the baseline hazards:


and only keep track of counting processes at time t where _Oi, i_ = 1 _. . . n_ are the observations.

65

---

[← 4 Right Censored Data Structure (Cont’d)](44-4-right-censored-data-structure-cont-d.md) · [Up: contents](index.md)
