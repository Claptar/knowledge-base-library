---
title: '2. Probabilistic formulation of reaction kinetics: the Master Equation'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/12-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. Probabilistic formulation of reaction kinetics: the Master Equation

**Source:** `lecture-outlines/12-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

If a reaction occurs at some rate _r_ , then in a large time interval _T_ it will occur, on average, _rT_ times. If this interval is divided into _N_ smaller sub-intervals, the chance that the reaction occurred in any one of those sub-intervals is _rT_ / _N_ . Writing _dt_ = _T/N_ , this shows that the probability of reaction with rate _r_ occurring in a small time interval _dt_ is just _rdt_ . (To be careful, we must eliminate the possiblity that more than one reaction occurred in this interval; however, for small enough _dt_ , that outcome is negligible.)

We now consider an ensemble of identical systems, each having the same initial conditions, and define _pn_ ( _t_ ) as the number of these systems which have precisely _n_ molecules at time _t_ . This number can increase if a molecule of _X_ is created in some system having _n_ -1 molecules, or if a molecule of _X_ is destroyed in some system having _n_ +1 molecules; it can decrease if a molecule of _X_ is created or destroyed in some system having _n_ molecules. These four possibilities are shown in Fig. 2; for clarity, consider just one of these for the moment. Suppose there are _pn_ -1 systems having _n_ -1 molecules at some time _t_ . In a small time interval _dt_ , the probability that there will be a molecule created in any one of these systems is _fn_ -1 _dt_ . Therefore, the total number of systems in which a molecule is created will be given by _pn_ -1 _fn_ -1 _dt_ . Each of these systems will then enter the pool of systems which have _n_ molecules, adding to the number _pn_ that were there to begin with. Thus, _p n_ ( _t_ + _dt_ ) = _p n_ (<sup>_t_</sup> ) + _pn_ − 1<sup>_f_</sup> _n_ − 1<sup>_dt_, or</sup><sup>_dp_</sup> _n_<sup>/</sup><sup>_dt_=</sup><sup>_f_</sup> _n_ − 1<sup>_p_</sup> _n_ − 1<sup>. If we now</sup> include all four fluxes, we obtain the Master Equation:


<!-- Start of picture text -->
dpn<br>= − (  f n  +  g n  )  pn  +  f n  − 1  pn  − 1  +  g n + 1  pn  + 1 .  (2)<br>dt<br>fn -1  fn<br>pn -1  pn pn +1<br>gn  gn +1<br><!-- End of picture text -->

Figure 2: Derivation of the Master Equation

Note that this is actually an infinite set of equations, one for each _n_ . The Master Equation is linear in the quantities _pn_ , so it remains unchanged when divide the number of systems in a given state _n_ by the fixed total number of systems. In that case, Σ _n pn_ = 1, and we can think of _pn_ ( _t_ ) as the probability for any given system to be in state _n_ . To connect with experiments: the ensemble of systems could be a population of cells, and _pn_ would represent the fraction of cells having _n_ copies of some protein.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004

---

[← 1. Introduction](02-1-introduction.md) · [Up: contents](index.md) · [3. Emergence of the deterministic law →](04-3-emergence-of-the-deterministic-law.md)
