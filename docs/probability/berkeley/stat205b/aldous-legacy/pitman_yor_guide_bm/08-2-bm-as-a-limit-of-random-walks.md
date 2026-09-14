---
title: 2. BM as a limit of random walks
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. BM as a limit of random walks

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let _Sn_ := _X_ 1 + _. . ._ + _Xn_ where the _Xi_ are independent random variables with mean 0 and variance 1, and let _St_ for real _t_ be defined by linear interpolation between integer values. Let _B_ be a standard one-dimensional BM. It follows easily from the central limit theorem [43, Th. 27.1] that


in the sense of weak convergence of finite-dimensional distributions. According to _Donsker’s theorem_ [44, 106, 370], this convergence holds also in the path space _C_ [0 _, ∞_ ) equipped with the topology of uniform convergence on compact intervals. That is to say, for every _T >_ 0, and every functional _f_ of a continuous path _x_ = ( _xs,_ 0 _≤ s ≤ T_ ) that is bounded and continuous with respect to the supremum norm on _C_ [0 _, T_ ],


Here, for ease of notation, we suppose that the random walk _X_ 1 _, X_ 2 _, . . ._ and the limiting Brownian motion _B_ are defined on the same probability space (Ω _, F,_ P), and E denotes expectation with respect to P. One way to do this, which can be used to prove (1), is to use the _Skorokhod embedding_ technique of constructing the _Xi_ = _BTi − BTi−_ 1 for a suitable increasing sequence of stopping times 0 _≤ T_ 1 _≤ T_ 2 _· · ·_ such that the _Ti − Ti−_ 1 are independent copies of _T_ 1 with E( _T_ 1) = E( _X_ 1<sup>2).See[106,Th.8.6.1],[44]or[370]fordetails,and[327]fora</sup> survey of variations of this construction. To illustrate a consequence of (1),


where the equality in distribution is due to the well known _reflection principle_ for Brownian motion. This can be derived via Donsker’s theorem from the corresponding principle for a simple random walk with _Xi_ = _±_ 1 discussed in [127],

_J. Pitman and M. Yor/Guide to Brownian motion_

6

or proved directly in continuous time [43][106][139][370]. See also [222], [86] for various more refined senses in which Brownian motion may be approximated by random walks.

Many generalizations and variations of Donsker’s theorem are known [44]. The assumption of independent and identically distributed _Xi_ can be weakened in many ways: with suitable auxilliary hypotheses, the _Xi_ can be stationary, or independent but not identically distributed, or martingale differences, or otherwise weakly dependent, with little affect on the conclusion apart from a scale factor. More interesting variations are obtained by suitable conditioning. For instance, assuming that the _Xi_ are integer valued, let _o_ (<sup>_√_</sup> _<u>n</u>_ <u>)</u> denote any sequence of possible values of _Sn_ with _o_ (<sup>_√_</sup> _<u>n</u>_ <u>)</u> _/_<sup>_√_</sup> _<u>n</u> →_ 0 as _n →∞_ . Then [108]


where _B_<sup>br</sup> is the _standard Brownian bridge_ , that is, the centered Gaussian process with covariance E( _Bs_<sup>br</sup><sup>_B_</sup> _t_<sup>br)=</sup><sup>_s_(1</sup><sup>_−t_)andcontinuouspathswhichisob-</sup> tained by conditioning ( _Bt,_ 0 _≤ t ≤_ 1) on _B_ 1 = 0. Some well known descriptions of the distribution of _B_<sup>br</sup> are [370, Ch. III, Ex (3.10)]


where = _d_ denotes equality of distributions on the path space _C_ [0 _,_ 1], and the rightmost process is defined to be 0 for _t_ = 1. See Section 7.1 for further discussion of this process. Let _T−_ := inf _{n_ : _Sn <_ 0 _}_ . Then as _n →∞_


where _B_<sup>me</sup> is the _standard Brownian meander_ [174, 53], and as _n →∞_ through possible values of _T−_


where _Bt_<sup>ex</sup> is the _standard Brownian excursion_ [200, 85]. Informally,


where = _d_ denotes equality in distribution. These definitions of conditioned Brownian motions have been made rigorous in a number of ways: for instance by the method of Doob _h_ -transforms [221, 376, 129], and as weak limits as _ε ↓_ 0 of the distribution of _B_ given suitable events _Aε_ , as in [103, 51], for instance


_J. Pitman and M. Yor/Guide to Brownian motion_

7

where _<u>X</u>_ <u>(</u> _s, t_ ) denotes the infimum of a process _X_ over the interval ( _s, t_ ). See Section 7.1 for further treatment of Brownian bridges, excursions and meanders.

The standard Brownian bridge arises also as a weak limit of _empirical processes_ : for _U_ 1 _, U_ 2 _, . . ._ a sequence of independent uniform [0 _,_ 1] variables, and


so that


it is found that


in the sense of convergence of finite-dimensional distributions, and also in the sense of weak convergence in the function space _D_ [0 _,_ 1] of right-continuous paths with left limits, equipped with the Skorokhod topology. See [391] for the proof and applications to empirical process theory.

Some further references related to random walk approximations are Lawler [249], Spitzer [397], Ethier and Kurtz [122], Le Gall [251].

---

[← • Step 4: Check that (i) and (ii) still hold for the process so defined.](07-step-4-check-that-i-and-ii-still-hold-for-the-process-so-def.md) · [Up: contents](index.md) · [3. BM as a Gaussian process →](09-3-bm-as-a-gaussian-process.md)
