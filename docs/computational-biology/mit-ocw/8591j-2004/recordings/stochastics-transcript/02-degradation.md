---
title: Degradation
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/stochastics-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Degradation

**Source:** `recordings/stochastics-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Now consider the degradation reaction:

2

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004


This reaction can represent two different processes: degradation, where molecule B is converted into a species which is not part of the subset of interest, and dilution, where it is physically separated from the volume of interest. In latter context _γ_ is the degradation rate and ln(2)/ _γ_ the half-life of the molecule. The master equation for this reaction is:


Using the same strategy as above the time evolution of the moment generation function yields:

_Forward reaction, conservation of total number of molecules_

Now consider the reaction:


where _no_ + _n_ 1 = _n_ = _const_ .  Since the total number _n_ is conserved, the system is defined by only one variable. We will use _n2_ as the single variable to define this system. For the reaction above:


This leads<sup>1</sup> to:


Based on these elementary reactions larger chemical networks can be built up. The results above are summarized in Table 1.

> 1 In this case, the sums only go up to n, instead of ∞ . However, the extra terms that appear when applying the change of variables cancel with each other.

3

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004

||Reaction Type|_F_<sup>& </sup>=|
|---|---|---|
|I|_B_<br>_A_<br>_A_<br>_k_<br>+<br>→<br>|1<br>2<br>1<br>)1<br>(<br>_z_<br>_F_<br>_z_<br>_kz_<br>∂<br>∂<br>−|
|II|→ 0<br><sup>γ</sup><br>_B_|1<br>1<br>)1<br>(<br>_z_<br>_F_<br>_z_<br>∂<br>∂<br>−<br>− γ|
|III|_B_<br>_A_<br>_k_<br>→<br><br>(_n1_+_n2_=_n_<br>_n2_)<br>= const., in terms of|2<br>2<br>2<br>2<br>)1<br>(<br>)1<br>(<br>_z_<br>_F_<br>_z_<br>_kz_<br>_F_<br>∂<br>∂<br>−<br>−<br>−<br>_z_<br>_kn_|
|.IV|_B_<br>_A_<br>_k_<br>_k_<br>−1<br>1<br><br>←<br>→<br>|2<br>2<br>1<br>1<br>1<br>1<br>2<br>1<br>)<br>(<br>)<br>(<br>_z_<br>_F_<br>_z_<br>_z_<br>_k_<br>_z_<br>_F_<br>_z_<br>_z_<br>_k_<br>∂<br>∂<br>−<br>+<br>∂<br>∂<br>−<br>−|


**_Table 1._** _Moment generating function equations for elementary reactions. The master equation for each reaction type produces different terms which can be combined to model more complex processes._

_Noise properties of a constitutively expressed gene_

Based on the results for these elementary reactions the equation for the moment generating functions of more complex networks can be easily deduced. First let us consider a constitutive expressed gene in a single copy in the chromosome of a bacterium. In this case the state of this system at any time is defined by the number of mRNA molecules _r_ and number of proteins _p_ for that gene. mRNA molecules are synthesized off the template DNA strand at a rate _kR_ and are translated at a rate _kP_ . The mRNA and protein degradation are described by the destruction rates _γ_ R and _γ_ P respectively (Fig. 1).


**_Figure 1_** _. Basic model for constitutive expression of a single gene. Only four individual reactions are considered: creation of mRNA from a DNA template, creation of proteins from individual mRNA molecules, and the degradation/dilution of both species._

4

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004

Based on the results in Table 1 the moment generating function can be deduced directly:


The first two terms are the transcription and translation reactions (Table 1, type I) and the last two terms model degradation of mRNA and proteins respectively (Table 1, type II). Below the equation will be solved for the moments in the steady state ( _F_<sup>&</sup> = 0 ). In this case:


The mean mRNA level _r_ and protein level _p_ are found by taking the derivative with respect to _z1_ and _z2_ respectively:


evaluating both expressions at _z1_ = _z2_ =1 gives:


The results are consistent with the equivalent deterministic system:


The fluctuations in mRNA and proteins level are found by differentiating the above equations again with respect to _z1_ and _z2_ and evaluating at _z1_ = _z2_ = 1:


5

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004

Further moments can be obtained sequentially in this manner. Note that for a random variable with Poissonian distribution, all moments are equal, so the variance over the mean equals one, as is the case for the mRNA in this model. The protein number fluctuates with a higher than poissonian noise, the correction determined primarily by the term _kP_ / γ _R_ (the ”burst size”), which corresponds to the average number of proteins produced per mRNA [9].

In simple cases like this, the moments can also be obtained as a function of time. For a single gene, the noise out of equilibrium can be 40% larger than its steady state value in the limit of short mRNA lifetimes [9]. A more detailed modeling of this process could include more intermediate detailed processes, such as the random steps that a ribosome takes along an mRNA, but most turn out to have little effect when compared in simulations. However, when a repressor or activator is present, its binding and unbinding might have to be included in the model, for this can be a major source of noise. It is in this context that the terms shown in Table 1, type III, are needed. Furthermore, the repressor concentration itself might be fluctuating, in which case we have to consider the entire system of genes.

_Linearized matrix formulation_

The method above can also be used for interacting systems of genes, but solving it is not straightforward unless the connections are linear. Alternatively, if the system is at a stable point in steady state, the interaction can be linearized around the steady state value. A practical way of writing this out is in matrix form. The transition probabilities for species _xi_<sup>are given by</sup><sup>_f_</sup> _i_<sup>_(x_</sup> _1_<sup>_,x_</sup> _2_<sup>_,...,x_</sup> _n_<sup>_)_for creation and γ</sup> i<sup>for destruction, and A and Γ are the</sup>


Note that since in many cases the macroscopic equations include constant creation terms. If the system is linear it might be necessary to include an additional variable, which is not fluctuating and allows the inclusion of the constant terms in the compact matrix form. As an illustration of this, the matrices for the single gene case are


where the state vector is _x_<sup>_T_</sup> = ( _d_ , _r_ , _p_ ) where _d_ is the gene copy number. This constant state coordinate needs not to represent an actual chemical; for a system where many species have a constant creation rate, these rates can all be placed in the first column of A (setting _d_ =1 and Γ1 _j_ = Γ _j_ 1<sup>=0 ). An example of this is the matrix for the case of two</sup>

6

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004

interacting genes, linearized around steady state, with fixed gene copy numbers _d1_ and _d2_ respectively, and where the first gene ( _r1_ , _p1_ ) represses the second ( _r2_ , _p2_ ) with transfer function _f_ ( _p1_ ):


Written in terms of these matrices, the master equation in generating function form would be


At steady state, _F_<sup>&</sup> = 0 , and taking the derivative with respect to _z_ l we obtain:


Setting all _z_ i=1, we have for each _i_


corresponding to the macroscopic result. Similarly, differentiating again and evaluating at _z_ i=1,


7

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004

∂ where Θ _ij_ = δ _ij_ ∂ _zi_ . These linear equations can be solved for the means, variances and

correlations.

This approach is very general and the resulting matrix equations can be solved directly<sup>2</sup> . However, even for the case of just two interacting genes this requires a 5x5 matrix system as shown, so it gets cumbersome for larger systems even though most entries are zero. Using symbolic matrix manipulation software it is straightforward to obtain the desired expressions, so for known parameters this is a good method for obtaining values without further approximations.

---

[← 1. THE MASTER EQUATION APPROACH](01-1-the-master-equation-approach.md) · [Up: contents](index.md) · [2. THE LANGEVIN APPROACH →](03-2-the-langevin-approach.md)
