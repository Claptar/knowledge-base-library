---
title: 19 Lecture Nineteen
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 19 Lecture Nineteen

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The goal today is to study Monte Carlo methodology for smoothing in general state space models. We shall focus on two smoothing algorithms:

1. Complete Smoothing: This method is simple and is just an extension of the particle filter algorithm. However it generally suffers from particle degeneracy.

2. FFBS: This is based on general smoothing ideas that we previously saw in the context of linear Gaussian models. The method works well but is computationally intensive.

### **19.1 Complete Smoothing**

This algorithm is an extension of particle filtering (and can also be termed complete filtering). It generates, for each _t ≥_ 0, samples


such that the discrete uniform distribution over these samples approximates the smoothing distribution at time _t_ :


for each _t_ = 0 _, . . . , T_ .

The algorithm proceeds sequentially over time _t_ = 0 _,_ 1 _, . . . , T_ . At time _t −_ 1, one has access to samples ( _X_ 0<sup>(</sup><sup>_i_</sup> _|t_<sup>)</sup> _−_ 1<sup>_, X_</sup> 1<sup>(</sup><sup>_i_</sup> _|t_<sup>)</sup> _−_ 1<sup>_, . . . , X_</sup> _t_<sup>(</sup> _−_<sup>_i_)</sup> 1 _|t−_ 1<sup>)</sup><sup>_,_1</sup><sup>_≤i≤N_satisfying(119)fortime</sup><sup>_t −_1</sup> and using these, one generates the samples ( _X_ 0<sup>(</sup><sup>_i_</sup> _|t_<sup>)</sup><sup>_, X_</sup> 1<sup>(</sup><sup>_i_</sup> _|t_<sup>)</sup><sup>_, . . . , X_</sup> _t_<sup>(</sup> _|_<sup>_i_</sup> _t_<sup>))</sup><sup>_,_1</sup><sup>_≤i ≤N_byfollowingthe</sup> three steps given below.

1. **Generation** : For each _i_ = 1 _, . . . , N_ , let

and


2. **Weights** : For each _i_ = 1 _, . . . , N_ , compute


Normalize these weights so they sum to one:


3. **Resampling** : Generate


89

The following are useful things to know about this algorithm:

1. The weights in (120) can be deduced from importance sampling. To see this, note that the generation of ( _X_<sup>˜</sup> 0<sup>(</sup><sup>_i_</sup> _|t_<sup>)</sup><sup>_, . . . ,X_˜</sup> _t_<sup>(</sup> _|_<sup>_i_</sup> _t_<sup>))isfrom(approximately)thedensity:</sup>


where we are using the notation:


On the other hand, the target density equals


where we used Bayes rule in the second step. The importance weights are therefore given by


Note that second term above (inverse of _fYt|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ ( _yt_ )) is a constant as it does not depend on _xt−_ 1 or _xt_ . We can thus view the importance weight as simply


This is exactly the importance weight _wt_<sup>(</sup><sup>_i_)</sup> in (120) with _xt−_ 1 = _Xt_<sup>(</sup> _−_<sup>_i_)</sup> 1 _|t−_ 1<sup>and</sup><sup>_xt_=</sup><sup>_X_˜</sup> _t_<sup>(</sup> _|_<sup>_i_</sup> _t_<sup>).</sup>

2. This algorithm needs to be initialized with samples from _X_ 0 _| Y_ 0 = _y_ 0 _, θ_ :


After the first iteration, it outputs samples:


Note that _X_ 0<sup>(1)</sup> _|_ 1<sup>_, . . . , X_</sup> 0<sup>(</sup><sup>_N_</sup> _|_ 1<sup>)isaresampledrawnfromtheinitialsample</sup><sup>_X_</sup> 0<sup>(1)</sup> _|_ 0<sup>_, . . . , X_</sup> 0<sup>(</sup><sup>_N_</sup> _|_ 0<sup>).</sup> After the second iteration, the algorithm outputs samples:


90

Here _X_<sup>(1)</sup> is a resample of _X_<sup>(1)</sup> which was already a resample 0 _|_ 2<sup>_, . . . , X_</sup> 0<sup>(</sup><sup>_N_</sup> _|_ 2<sup>)</sup> 0 _|_ 1<sup>_, . . . , X_</sup> 0<sup>(</sup><sup>_N_</sup> _|_ 1<sup>)</sup> from _X_ 0<sup>(1)</sup> _|_ 0<sup>_, . . . , X_</sup> 0<sup>(</sup><sup>_N_</sup> _|_ 0<sup>).</sup> Also _X_ 1<sup>(1)</sup> _|_ 2<sup>_, . . . , X_</sup> 1<sup>(</sup><sup>_N_</sup> _|_ 2<sup>)</sup> is a resample from _X_ 1<sup>(1)</sup> _|_ 1<sup>_, . . . , X_</sup> 1<sup>(</sup><sup>_N_</sup> _|_ 1<sup>).</sup> One then proceeds iteratively ending in the final step where the algorithm ouputs:


The columns of the above output (121) in the final iteration of the algorithm are samples from the smoothing distribution of interest: ( _X_ 0 _, . . . , XT_ ) _| Y_ 0 = _y_ 0 _, . . . , YT_ = _yT , θ_ .

3. This algorithm is very similar to the Sequential Importance Resampling (SIR) algorithm from the last couple of lectures for filtering. Indeed, if we keep track of only the filtering samples i.e., the samples


for _t_ = 0 _,_ 1 _, . . . , T_ , and ignore the set of time indices _s | t_ for _s < t_ , we get back the SIR algorithm.

4. **Particle Degeneracy** : This algorithm suffers from serious particle degeneracy. Specifically, the number of unique values _Nt_ among _Xt_<sup>(1)</sup> _|T_<sup>_, . . . , X_</sup> _t_<sup>(</sup> _|_<sup>_N_</sup> _T_<sup>)</sup> can be much smaller than _N_ and this is especially true for small values of _t_ . This is because the samples _Xt_<sup>(1)</sup> _|t_<sup>_, . . . , X_</sup> _t_<sup>(</sup> _|_<sup>_N_</sup> _t_<sup>)</sup> are created in the _t_<sup>_th_</sup> iteration and the subsequent samples


are all obtained by resampling from _X_<sup>(1)</sup> with various choices of weights. _t|t_<sup>_, . . . , X_</sup> _t_<sup>(</sup> _|_<sup>_N_</sup> _t_<sup>)</sup> This means that _Xt_<sup>(1)</sup> _|T_<sup>_, . . . , X_</sup> _t_<sup>(</sup> _|_<sup>_N_</sup> _T_<sup>)are obtained after resampling</sup><sup>_T−t_times from</sup><sup>_X_</sup> _t_<sup>(1)</sup> _|t_<sup>_, . . . , X_</sup> _t_<sup>(</sup> _|_<sup>_N_</sup> _t_<sup>).</sup> Every resampling leads to a decrease in the effective sample size, and thus if _T − t_ is large (which will be the case for small _t_ ), the number of unique samples will be much smaller than _N_ .

**Computational Complexity** : The complexity of this algorithm is _O_ ( _NT_ ). This is because in each iteration of the algorithm, _O_ ( _N_ ) computations are done (note that weights need to be calculated for each of the generated samples). The final complexity is therefore _O_ ( _NT_ ) as there are _T_ iterations.

### **19.2 FFBS**

This algorithm is similar to the FFBS (Forward Filtering Backward Sampling) algorithms that we studied previously for linear Gaussian state space models (we also previously looked at a numerical version of FFBS for general state space models).

The goal of FFBS is to generate _M_ samples:


91

form the conditional distribution


Note that we are using the notation _M_ for the number of smoothing samples.

The first step in FFBS is to run a particle filtering algorithm. This will result in samples:


for each _t_ = 0 _, . . . , T_ . The discrete uniform distribution over the samples (122) approximates the filtering distribution _Xt | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ for each _t_ = 0 _,_ 1 _, . . . , T_ . Note that, because of the resampling steps that are used in particle filtering algorithms, there need not be any connection between _Xt_<sup>(</sup> _−_<sup>_i_)</sup> 1 _|t−_ 1<sup>and</sup><sup>_X_(</sup> _t|_<sup>_i_</sup> _t_<sup>)forfixed</sup><sup>_i_(inthenotationofourfiltering</sup> algorithms, _Xt_<sup>(</sup> _−_<sup>_i_)</sup> 1 _|t−_ 1<sup>and</sup> _X_<sup>˜</sup> _t_<sup>(</sup><sup>_i_)</sup> would be related but there won’t be any connection between _X_ ˜ _t_<sup>(</sup><sup>_i_)</sup> and _Xt_<sup>(</sup> _|_<sup>_i_</sup> _t_<sup>)becauseofresampling).Iamusingthenotation</sup><sup>_X_(insteadoftheusual</sup><sup>_X_)</sup> for the filtering particles to distinguish them from the smoothing samples which will be subsequently generated by FFBS.

Observe that we have _N_ filtering samples for each time _t_ . This _N_ can be distinct from the desired number _M_ of smoothing samples.

The step of running a particle filter algorithm represents the “FF” part of FFBS. We shall now describe the “BS” (Backward Sampling) part of the algorithm. Here, for each _i_ = 1 _, . . . , M_ , we shall generate samples


in backward order for _t_ = _T, . . . ,_ 0. The first sample _X_<sup>(</sup><sup>_i_)</sup> _T |T_<sup>isjustdrawnfromthediscrete</sup> filtering approximation for _t_ = _T_ (this is because the filtering and smoothing marginal distributions for _t_ = _T_ coincide):


The recursive process for obtaining the subsequent samples _XT_<sup>(</sup><sup>_i_</sup> _−_<sup>)</sup> 1 _|T_<sup>_, . . . , X_</sup> 0<sup>(</sup><sup>_i_</sup> _|T_<sup>)isdescribed</sup> next. To go from _Xt_<sup>(</sup> +1<sup>_i_)</sup> _|T_<sup>to</sup><sup>_X_</sup> _t_<sup>(</sup> _|_<sup>_i_</sup> _T_<sup>),wewouldneedtogeneratefromtheconditionaldensity</sup> (below _xt_ +1 := _X_<sup>(</sup><sup>_i_)</sup> _t_ +1 _|T_<sup>)</sup>


A natural idea of generating _X_<sup>(</sup><sup>_i_)</sup> _t|T_<sup>istothereforeuseimportancesamplingwherewefirst</sup> generate from a proposal density _q_ ( _xt | xt_ +1 _,_ data _, θ_ ) and then use the weight:


92

The proportionality sign above is in terms of _xt_ (factors not depending on _xt_ can be taken as part of the proportionality).

Any proposal density _q_ ( _xt | xt_ +1 _,_ data _, θ_ ) can be used for this purpose. However, it is especially convenient to take it as the filtering density at time _t_ :


for the following two reasons:


2. With the choice (124), the weights in (123) become quite simple:


With the choice (124), the method for generating _Xt_<sup>(</sup> _|_<sup>_i_</sup> _T_<sup>)from</sup><sup>_X_</sup> _t_<sup>(</sup> +1<sup>_i_)</sup> _|T_<sup>becomes:</sup>


where


(125) just means that _X_<sup>(</sup><sup>_i_)</sup> _t|T_<sup>is just sampled from the discrete distribution that is concentrated</sup> on the filtering samples _X_<sup>(1)</sup> with weights _w_ 1 _, . . . , wN_ . _t|t_<sup>_, . . . , X_(</sup> _t|_<sup>_N_</sup> _t_<sup>)</sup>

The overall FFBS algorithm is therefore:

1. **Filtering** : Run a particle filter algorithm to generate samples _Xt_<sup>(1)</sup> _|t_<sup>_, . . . , X_(</sup> _t|_<sup>_N_</sup> _t_<sup>)</sup> which approximate the filtering distribution _Xt | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ at each time _t_ = 0 _,_ 1 _, . . . , T_ .

2. Repeat the following for _i_ = 1 _, . . . , M_

   - a) **Initialization for Backward Recursion** : Draw one sample _X_<sup>(</sup><sup>_i_)</sup> _T |T_<sup>fromthe</sup>

   - discrete uniform distribution on _XT_<sup>(1)</sup> _|T_<sup>_, . . . , X_(</sup> _T_<sup>_N_</sup> _|T_<sup>).</sup>

   - b) **Backward Recursion** : Repeat the following _t_ = _T −_ 1 _, . . . ,_ 0:

      - i. Calculate weights _wj_ = _fXt_ +1 _|Xt_ = _X_ ( _t|jt_ )<sup>_,θ_(</sup><sup>_X_</sup> _t_<sup>(</sup> +1<sup>_i_)</sup> _|T_<sup>)foreach</sup><sup>_j_=1</sup><sup>_, . . . , N_.Nor-</sup> malize these weights to obtain _W_ 1 _, . . . , WN_ which sum to one.

      - ii. Generate _X_<sup>(</sup><sup>_i_)</sup> with proba- _t|T_<sup>fromthediscretedistributionon</sup><sup>_X_(1)</sup> _t|t_<sup>_, . . . , X_(</sup> _t|_<sup>_N_</sup> _t_<sup>)</sup>

      - bilities _W_ 1 _, . . . , WN_ .

### **19.3 Recommended Reading for Today**

1. The complete smoothing algorithm is described in Section 15.3 of the Kitagawa book, Section 11.1 of the S¨arkk¨a book, and Section 12.1.2 of the Chopin-Papaspiliopoulos book.

93

2. The FFBS algorithm is described in Section 12.3.2 of the Chopin-Papaspiliopoulos book, and in Section 11.2 of the S¨arkk¨a book (S¨arkk¨a calls it the Backward-Simulation Particle Smoother algorithm).

---

[← 18 Lecture Eighteen](19-18-lecture-eighteen.md) · [Up: contents](index.md) · [20 Lecture Twenty →](21-20-lecture-twenty.md)
