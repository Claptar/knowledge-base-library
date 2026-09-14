---
title: VII Biological Oscillators
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/10-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# VII Biological Oscillators

**Source:** `lecture-outlines/10-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

During class we consider the following two coupled differential equations:


From the phase plane analysis (see L9_notes.pdf) it was clear that for certain values of a and b this system exhibits periodic oscillations as a function of time. Let us analyze [VII.1] in more detail. The nullclines are:


There is only one fixed point (x<sup>*</sup> ,y ): *


The matrix A is (using [V.4] and [V.5]):


The determinant and trace are:

∆= _a_ + _b_<sup>2</sup> > 0


The fixed point is stable when τ < 0. The region in a-b-parameter space where the system is oscillating (stable limit cycle) and is not oscillating (stable fixed point) is illustrated in Fig. 10.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

35


**Figure 11.** a-b-parameter space indicating for which values of a and b the system exhibits stable oscillations and a stable fixed point

**MATLAB code 5** : Limit cycle

% filename: cyclefunc.m function dydt = f(t,y,flag,a,b) dydt = [-y(1)+a*y(2)+y(1)*y(1)*y(2); b-a*y(2)-y(1)*y(1)*y(2)]; plot(y(1),y(2),'.'); drawnow; hold on; axis([0 2 0 2]);

% filename: limitcycle.m close; clear; a=0.1; b=0.5; options=[]; [t y]=ode23('cyclefunc',[0 50],[0.6 1.4],options,a,b); plot(y(:,1),y(:,2));

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

36

Recently Elowitz et al. constructed a genetic oscillator ‘from scratch’ in the bacterium _Escherichia coli._ Details of these experiments can be found in:

M. B. Elowitz and S. Leibler. A synthetic oscillatory network of transcriptional regulators. _Nature_ **403** , 335-338 (2000).

In class we derived the conditions under which the network exhibits oscillations. The chemical reactions describing the concentration of mRNA m and protein concentration p are (see Box):


where the index i=[lacI,tetR,cI] and the index j=[cI,lacI,tetR]. Below will we use numerical indices to represent the repressors. Let us assume that we can ignore the intermediate step of mRNA synthesis. This leads to the following three equations:


In the analysis below we will assume that all three genes have the same basal synthesis rate αo, maximum synthesis rate α, and Hill coefficient n. Note that time is measured with respect to protein decay rate. As all three genes have the same properties, the steadystate values of the mRNA and protein concentrations will be:

_p_ ≡ _p_ 1 = _p_ 2 = _p_ 3


therefore in steady-state,


For the stability analysis we have to determine the matrix A (Jacobian) as described before (see section V):

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

37

where


**[VII.10]**

For the steady state to be stable, the real part of the eigenvalues of matrix A have to be negative. As mentioned in [V.8] the eigenvalues can be found by solving:


Leading to


This equation has three solutions, one real and two complex:


For a stable fixed point the real part of all eigenvalues should be negative. Therefore the system is stable for:


X is negative by definition (see [VII.11]) so the final stability condition is:


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

38

---

[Up: contents](../index.md)
