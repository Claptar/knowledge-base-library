---
title: 20 Lecture Twenty
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 20 Lecture Twenty

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **20.1 Recap: Complete Smoothing**

In the last class, we studied two algorithms for smoothing in general state space models. These algorithms produce samples


which approximate the smoothing distribution ( _X_ 0 _, . . . , XT_ ) _| Y_ 0 = _y_ 0 _, . . . , YT_ = _yT , θ_ . The first of these algorithms was the complete smoothing algorithm (also known as the SIRPS: Sequential Importance Resampling Particle Smoother). This algorithm works in the following way:


2. Repeat the following for each _t_ = 1 _, . . . , T_ :


b) Calculate weights


Renormalize these weights to obtain _Wt_<sup>(</sup><sup>_i_)</sup><sup>_, i_= 1</sup><sup>_, . . . , M_whichsumtoone.</sup>

c) Append the samples to the state histories:


The above description of the complete smoothing algorithm is slightly different from that given in the previous class but algorithm is exactly the same. Its computational complexity is _O_ ( _MT_ ).

### **20.2 Complete Smoothing with partial trajectory resampling**

The main problem with the complete smoothing algorithm is particle degeneracy. Specifically, for the samples ( _X_ 0<sup>(</sup><sup>_i_)</sup><sup>_, . . . , X_</sup> _T_<sup>(</sup><sup>_i_))</sup><sup>_,_1</sup><sup>_≤i ≤M_obtainedinthefinaliteration,thenumber</sup> of unique values among _Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_M_)</sup> will be quite small (compared to _M_ ) especially for

94

small values of _t_ . This is because a fixed number of particles ( _M_ ) are repeatedly being resampled. One, somewhat adhoc, fix to this problem is to resample, instead of the full state trajectories _X_ 0:<sup>(1)</sup> _t_<sup>_, . . . , X_</sup> 0:<sup>(</sup><sup>_M_</sup> _t_<sup>),justthetrajectories</sup>


for some fixed _L_ . Of course, here we are assuming that _t ≥ L_ (if _t < L_ , the resamping is done as before from the full trajectories). This method fixes the particle degeneracy issue and the marginal samples _Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_M_)</sup> will have distribution which is nearly the same as _Xt | Y_ 0 = _y_ 0 _, . . . , YT_ = _yT , θ_ (if _L_ is not too small). However, the final trajectories _X_ 0:<sup>(1)</sup> _T_<sup>_, . . . , X_</sup> 0:<sup>(</sup><sup>_M_</sup> _T_<sup>)</sup> can no longer be treated as samples from _X_ 0 _, . . . , XT | Y_ 0 = _y_ 0 _, . . . , YT_ = _yT , θ_ .

Another way of thinking about this partial trajectory resampling fix is the following. The main problem with the complete smoothing algorithm is that it gives poor approximation, due to particle degeneracy, to the smoothing distributions of _Xs_ (given _Y_ 0 = _y_ 0 _, . . . , YT_ = _yT , θ_ ) when _s_ is small. More generally, the samples will provide a poor approximation to the joint distribution:


when _s_ 1 _< · · · < sk_ and _sk_ is small. One heuristic way to obtain better approximation of this joint density is as follows. First reason that


for some fixed _L_ that is much smaller than _T − sk_ . The idea is that the observation values _Yt_ = _yt_ for _t_ larger than _sk_ + _L_ probably do not have much influence on the distribution of _Xs_ 1 _, . . . , Xsk_ . Under the approximation (127), the full smoothing distribution (126) can therefore be obtained by the right hand side of (127) which is well-approximated by the complete smoothing algorithm at iteration _sk_ + _L_ . In other words, we don’t need to run the complete smoothing algorithm till iteration _T_ to approximate (126). The amount of resampling at iteration _sk_ + _L_ will be much smaller than until time _T_ and this will lead to much less particle degeneracy. It is tricky however to choose an appropriate value of _L_ (one usually just takes an arbitrary value such as _L_ = 30).

### **20.3 Recap: FFBS**

The FFBS algorithm is:

1. **Filtering** : Run a particle filter algorithm to generate samples _Xt_<sup>(1)</sup> _|t_<sup>_, . . . , X_(</sup> _t|_<sup>_N_</sup> _t_<sup>)</sup> which approximate the filtering distribution _Xt | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ at each time _t_ = 0 _,_ 1 _, . . . , T_ .

2. Repeat the following for _i_ = 1 _, . . . , M_

   - a) **Initialization for Backward Recursion** : Draw one sample _X_<sup>(</sup><sup>_i_)</sup> _T |T_<sup>fromthe</sup>

   - discrete uniform distribution on _XT_<sup>(1)</sup> _|T_<sup>_, . . . , X_(</sup> _T_<sup>_N_</sup> _|T_<sup>).</sup>

   - b) **Backward Recursion** : Repeat the following _t_ = _T −_ 1 _, . . . ,_ 0:

      - i. Calculate weights _wj_ = _fXt_ +1 _|Xt_ = _X_ ( _t|jt_ )<sup>_,θ_(</sup><sup>_X_</sup> _t_<sup>(</sup> +1<sup>_i_)</sup> _|T_<sup>)foreach</sup><sup>_j_=1</sup><sup>_, . . . , N_.Nor-</sup> malize these weights to obtain _W_ 1 _, . . . , WN_ which sum to one.

95

ii. Generate _X_<sup>(</sup><sup>_i_)</sup> with proba- _t|T_<sup>fromthediscretedistributionon</sup><sup>_X_(1)</sup> _t|t_<sup>_, . . . , X_(</sup> _t|_<sup>_N_</sup> _t_<sup>)</sup> bilities _W_ 1 _, . . . , WN_ .

The level of particle degeneracy of this algorithm can be checked by looking at the number of unique values among _X_<sup>(1)</sup> for each _t_ = 0 _, . . . , T_ . Generally, particle degeneracy _t|T_<sup>_, . . . , X_</sup> _t_<sup>(</sup> _|_<sup>_M_</sup> _T_<sup>)</sup> is not a problem for FFBS. The issue however is speed. Notice the double loop present in the algorithm (an outer loop over _i_ = 1 _, . . . , M_ and then an inner loop over _t_ = _T −_ 1 _, . . . ,_ 0). In the inner loop, there is a calculation of _N_ weights. The total computational complexity is therefore _O_ ( _MNT_ ). The FFBS algorithm will therefore be much slower compared to the complete smoothing algorithms. However, as there is not much particle degeneracy, one can afford to choose _M_ to be much smaller than _N_ (e.g., _M_ can be of the order of a few hundreds while _N_ is in the order of tens of thousands).

### **20.4 Recommended Reading for Today**

1. The complete smoothing algorithm and the partial trajectory resampling variant are described in Section 15.3 of the Kitagawa book (see also Section 12.1 of the ChopinPapaspiliopoulos book).

2. The FFBS algorithm is described in Section 12.3.2 of the Chopin-Papaspiliopoulos book, and in Section 11.2 of the S¨arkk¨a book (S¨arkk¨a calls it the Backward-Simulation Particle Smoother algorithm). A technique for making FFBS faster is described in Section 12.3.3 of the Chopin-Papaspiliopoulos book.

---

[← 19 Lecture Nineteen](20-19-lecture-nineteen.md) · [Up: contents](index.md) · [21 Lecture Twenty One →](22-21-lecture-twenty-one.md)
