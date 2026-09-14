---
title: STOCHASTIC CHEMICAL REACTION SYSTEMS AND APPROXIMATIONS
source: https://thesis.library.caltech.edu/17389/
source_file: sources/fang-2025-biophysical-normalisation/Thesis.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# STOCHASTIC CHEMICAL REACTION SYSTEMS AND APPROXIMATIONS

**Source:** `Thesis.pdf` from [fang-2025-biophysical-normalisation](https://thesis.library.caltech.edu/17389/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **2.1 Introduction**

As discussed in Chapter 1.1, the chemical master equation (CME) offers a probabilistic framework for modeling the time evolution of a system’s state, capturing the intrinsic stochastic fluctuations present in small, discrete systems. However, obtaining analytical solutions to the CME is generally intractable (Schnoerr, Sanguinetti, and Grima, 2017), and qualitative understanding is often achieved through various approximations.

A natural direction is to consider the limit of large system volumes, with the expectation that as the number of molecules becomes sufficiently large, the system’s stochastic behavior will converge to either deterministic dynamics or a simplified form of stochastic dynamics. The convergence of the CME to the reaction rate equations and to the Chemical Langevin Equation (CLE) over finite time intervals has been well established (Kurtz, 1972; Gillespie, 2000). By applying the system-size expansion (also known as the linear noise approximation) and retaining the first two orders, one obtains a Fokker–Planck equation that approximates the evolution of the probability distribution (Van Kampen, 2007). A recent study has also established the validity of the linear noise approximation for stationary distributions under certain restricted conditions (Grunberg and Del Vecchio, 2023).

However, approximations that remain uniform in time in the large volume limit are generally lacking. In fact, it is believed that the limits of large volume and infinite time are not interchangeable (Hanggi et al., 1984; Baras, Mansour, and Pearson, 1996; Srivastava et al., 2002; Vellela and Qian, 2007; Vellela and Qian, 2009; Assaf and Meerson, 2017). In this chapter, we review various approximations to the CME and discuss when the large volume and infinite time limits can, or cannot, be interchanged. We argue that the (non)interchangeability of these limits arises from the specific asymptotic approximation method employed. Notably, a time-uniform large volume approximation may be attainable through the Wentzel–Kramers–Brillouin (WKB) approximation and Poisson representation, which offers a different perspective on the system’s stochastic dynamics.

11


Figure 2.1: Approximations to CME

## **CME**

Generally, a master equation for the probability distribution function _𝑃_ ( **x** _, 𝑡_ ) can be expressed as follows:


where _𝑃_ ( **x** _, 𝑡_ ) is the probability of being in state **x** at time _𝑡_ and _𝑊_ ( **x**<sup>′</sup> → **x** ) is the transition rate from state **x**<sup>′</sup> to **x** .

Now consider specifically for chemically reacting system. Let a mixture of _𝑛_ molecular species _𝑆_ 1 _, ..., 𝑆𝑛_ chemically interact through m chemical reactions _𝑅_ 1 _, ..., 𝑅𝑚_ :


where _𝑠𝑖𝑗_ , _𝑟𝑖𝑗_ are stoichiometric constant and _𝑘 𝑗_ is the reaction rate constant.

12

Let _𝑋_ ( _𝑡_ ) = ( _𝑋_ 1( _𝑡_ ) _, ..., 𝑋𝑛_ ( _𝑡_ )) denote the numbers of molecules of species in the system at time t and _𝑃_ the probability. The chemical master equation assumes the system is a continuous time Markov chain and the transition rate matrix is completely determined by the reactions. Then we have that the probability distribution _𝑃_ ( _𝑥, 𝑡_ ) := _𝑃_ ( _𝑋_ ( _𝑡_ ) = _𝑥_ | _𝑋_ ( _𝑡_ 0) = _𝑥_ 0) follows (Gillespie, 2000)


Let V be the volume of the system and _𝑧_ be the concentration _𝑧𝑖_ = _𝑥𝑉𝑖_<sup>.</sup> The corresponding reaction rate equation for Equation 2.1 is


where _𝜅 𝑗_ = _𝑘 𝑗𝑉_ � _𝑖_<sup>_𝑠_</sup> _𝑖𝑗_<sup>−1</sup> is the macroscopic reaction rate.

## **2.2 Large-volume approximations to the chemical master equation Kramers–Moyal expansion/Chemical Langevin equation**

The first type of approximation is the chemical Langevin equation:


The first derivation to this form, which is straightforward but not mathematically rigorous, is based on the Kramers–Moyal expansion. Kramers–Moyal expansion refers to a Taylor series expansion of the chemical master equation (Equation 2.2):


By only keeping only the first two terms of the series, we derive Equation 2.4.

However, this truncation is not rigorously justified and is primarily adopted for analytical convenience. A rigorous foundation was established by Kurtz in the

13

1970s, albeit under strong assumptions on the reaction rate functions (Kurtz, 1978). He proved a central limit theorem for the random variable governed by the chemical master equation (CME). Later, Gillespie proposed a more intuitive derivation in 2000 (Gillespie, 2000). His approach relies on the existence of a macroscopically infinitesimal time scale during which the propensity functions remain effectively constant, while a large number of reactions occur. Both derivations follow the underlying stochastic process directly, rather than analyzing the associated CME, and are valid only over finite time intervals.

## **System size expansion/Linear noise approximation**

A more rigorous approach to analyzing the CME than the Kramers–Moyal expansion is the system size expansion developed by Van Kampen (Van Kampen, 2007). This approach is analogous to the small noise approximation used in the analysis of the Fokker–Planck equation (C. Gardiner, 2009), which employs boundary-layer theory to handle regions near the solution of ODE (Bender and Orszag, 2010).

Let _𝑧_ ( _𝑡_ ) be the solution to the rate equation (Equation 2.3). Then, the probability distribution _𝑃_ ( _𝑥, 𝑡_ ) can be approximated in terms of the rescaled deviation _𝑦_ as


which describes fluctuations around the deterministic trajectory _𝑧_ ( _𝑡_ ). The evolution of _𝑃_ ( _𝑦, 𝑡_ ) is governed by the following Fokker–Planck equation:


## **WKB approximation**

Although not commonly presented in the literature, one can also apply the WKB (Wentzel–Kramers–Brillouin) approximation directly to Equation 2.2. Let _𝑃_ ( _𝑥, 𝑡_ ) = exp( _𝑉𝜙_ ( _𝑥, 𝑡_ )) and plug it into Equation 2.5. Keeping only the _𝑂_ ( _𝑉_ ) terms gives


14

This can be solved numerically but does not provide an intuitive understanding of the dynamics of the systems.

## **Non-interchangeability of the limits of infinite system size and infinite time**

It has been pointed out in several studies that the limits of infinite system size and infinite time do not, in general, commute (Hanggi et al., 1984; Baras, Mansour, and Pearson, 1996; Srivastava et al., 2002; Vellela and Qian, 2007; Vellela and Qian, 2009; Assaf and Meerson, 2017). The underlying argument can be summarized as follows: (1) both the linear noise approximation and the deterministic rate equations fail to capture multistability, and (2) the Fokker–Planck equation yields asymptotically incorrect predictions for switching times and the relative stability of states in the stationary distribution. These shortcomings arise because the linear noise approximation is only valid in the vicinity of a fixed point, while the Fokker–Planck approximation is formally justified only for finite time horizons.

Therefore, the issue is not strictly that the infinite-time and infinite-system-size limits are fundamentally non-interchangeable, but rather that the system-size expansion and Fokker–Planck approximation is not valid uniformly in time.

## **2.3 Large-volume approximations to the chemical master equation through Poisson representation**

Below we describe a preliminary and incomplete attempt to construct a large-volume approximation to the chemical master equation that is uniform in time through Poisson representation.

The chemical master equation for bimolecular reactions is translated into a FokkerPlanck equation in the complex domain using the positive Poisson representation developed by Drummond and Gardiner (Drummond and C. W. Gardiner, 1980). We note that the large volume limit and the infinity time limit are interchangeable for Fokker-Planck equation since it is a linear PDE, i.e., the WKB method provides an uniform approximation in time. Graham and Tel has shown that the stationary distribution of Fokker-Planck equation in the weak-noise limit is associated to the ODE by the drift term (Graham and Tél, 1985). Therefore, the long-term behavior of the chemical master equation in the large volume limit is determined by the fixed points of the corresponding reaction rate equation in the complex domain. We show that a stable fixed point cannot exist outside the real axis.

The Poisson representation of _𝑃_ ( _𝑥, 𝑡_ ) is _𝑃_ ( _𝑥, 𝑡_ ) = ∫ _𝐷_ _<u>𝜆𝑥</u>_<sup>_𝑥_</sup> !<sup>_𝑒_−</sup><sup>_𝜆𝑓_(</sup><sup>_𝜆, 𝑡_)</sup><sup>_𝑑𝜆_.Assume the</sup>

15

surface terms of the domain of the integration vanish. Then


Let _𝛼_ = _𝑉_<sup>_<u>𝜆</u>_and</sup><sup>_𝑔_(</sup><sup>_𝛼, 𝑡_):=</sup><sup>_𝑉𝑛𝑓_(</sup><sup>_𝛼𝑉, 𝑡_).Recall that</sup><sup>_𝜅_=</sup><sup>_𝑘𝑗𝑉_</sup> � _𝑖_<sup>_𝑠_</sup> _𝑖𝑗_<sup>−1</sup> . We have


We only consider bimolecular reactions where<sup>�</sup> _𝑖_<sup>_𝑠_</sup> _𝑖𝑗_<sup>≤2 and �</sup> _𝑖_<sup>_𝑟_</sup> _𝑖𝑗_<sup>≤2 for all</sup><sup>_𝑗_,</sup> which includes the majority of elementary reactions.

Then


where _𝜀_ = _𝑉_<sup><u>1</u>,</sup><sup>_𝐴𝑖_(</sup><sup>_𝛼_)= �</sup> _𝑗_<sup>(</sup><sup>_𝑟_</sup> _𝑖𝑗_<sup>−</sup><sup>_𝑠_</sup> _𝑖𝑗_<sup>)</sup><sup>_𝑘_</sup> _𝑗_<sup>Π</sup> _𝑖_<sup>_𝛼_</sup> _𝑖_<sup>_𝑠𝑖𝑗_</sup> and _𝐵𝑖_ 1 _,𝑖_ 2 ( _𝛼_ ) =<sup>�</sup> _𝑗_<sup>(</sup><sup>_𝑟_</sup> _𝑖_ 1 _𝑗_<sup>_𝑟_</sup> _𝑖_ 2 _𝑗_<sup>−</sup><sup>_𝑠_</sup> _𝑖_ 1 _𝑗_<sup>_𝑠_</sup> _𝑖_ 2 _𝑗_<sup>−</sup> _𝛿𝑖_ 1 _,𝑖_ 2 _𝑟𝑖𝑗_ ) _𝑘 𝑗_ Π _𝑖𝛼𝑖_<sup>_𝑠𝑖𝑗_.</sup>

Note that the diffusion term is no longer positive semidefinite, and the corresponding SDE can have imaginary noise. To resolve that, Gardiner proposed the positive Poisson representation (C. Gardiner, 2009), where _𝛼_ is a complex variable _𝛼_ = _𝑥_ + _𝑖𝑦_ and _𝑑𝜇_ ( _𝛼_ ) = _𝑑𝑥𝑑𝑦_ . Write the drift and diffusion terms also explicitly with real and imaginary parts _𝐴_ ( _𝑥, 𝑦_ ) = _𝐴𝑥_ ( _𝑥, 𝑦_ )+ _𝑖𝐴𝑦_ ( _𝑥, 𝑦_ ) and _𝐵_ ( _𝑥, 𝑦_ ) = _𝐶_ ( _𝑥, 𝑦_ ) _𝐶_ ( _𝑥, 𝑦_ )<sup>_𝑇_</sup> where _𝐶_ = _𝐶𝑥_ ( _𝑥, 𝑦_ ) + _𝑖𝐶𝑦_ ( _𝑥, 𝑦_ ). By doubling the dimension, it becomes a Fokker-Planck equation with positive semidefinite:


_𝐶𝑥𝐶𝑥_<sup>_𝑇_</sup> _𝐶𝑥𝐶𝑦_<sup>_𝑇_</sup> . where A = [ _𝐴𝑥_ ( _𝑥, 𝑦_ ) _, 𝐴𝑦_ ( _𝑥, 𝑦_ )]<sup>_𝑇_</sup> and B = � _𝐶𝑦𝐶𝑥_<sup>_𝑇_</sup> _𝐶𝑦𝐶𝑦_<sup>_𝑇_</sup> �

Note that Poisson representation (Equation 2.7) is valid for both finite and infinite time and for all volume.

<u>�∞</u> _<u>𝑛</u>_ =0<sup>_𝜀𝑛𝜑𝑛_</sup><sup><u>(</u></sup><sup>**x**</sup><sup>_,_</sup><sup>**<u>y</u>**</sup><sup>_,𝑡_</sup><sup><u>)</u></sup> Apply WKB approximation and assume _ℎ_ ( **x** _,_ **y** _, 𝑡_ ) = exp(− _𝜀_ ). To the leading order in _𝜀_ , Equation 2.7 can be approximated as

16


Let _𝜙_ 0 = _𝜑_ 0( **x** _,_ **y** _,_ ∞), then


Graham and Tél has showed that _𝜙_ 0, interpreted as the non-equilibrium potential, is continuous, even though its derivatives may have infinitely many discontinuities (Graham and Tél, 1985). Importantly, given that B is positive semidefinite, the quasi-potential _𝜑_ 0 inherits the asymptotic structure of the underlying deterministic system: _𝜑_ 0 attains local minima at the attractors, local maxima at the repellors, and saddle points at the deterministic saddles, provided that B is nonzero at those fixed points. If B is zero at a fixed point, then the point is absorbing and thus dynamically stable, which explains the Keizer’s paradox discussed in (Vellela and Qian, 2007).

Therefore, the systems in the large volume limit is determined by the attractors of the deterministic system expanded in the complex domain:


We focus on systems where attractors consist only of fixed points. As the ODE (eq 2.10) is in the complex domain, all fixed points in the real domain remain fixed points, and generally, additional fixed points exist outside the real domain. However, we will show that the fixed points with non-zero imaginary parts cannot be stable.

Recall that we only consider bimolecular reactions. Therefore, we can write


where _𝑎𝑖𝑗𝑘_ = _𝑎𝑖𝑘𝑗_ . Consequently,


17

Then the Jacobi matrix is


The second equality follows from Cauchy–Riemann equations and


Nowsuppose _𝛼_<sup>∗</sup> = ( _𝑥_<sup>∗</sup> _, 𝑦_<sup>∗</sup> )<sup>_𝑇_</sup> isafixedpointsatisfying A( _𝛼_ ) = [ _𝐴𝑥_ ( _𝑥, 𝑦_ ) _, 𝐴𝑦_ ( _𝑥, 𝑦_ )]<sup>_𝑇_</sup> = 0 and denote the Jacobi matrix evaluated at _𝛼_<sup>∗</sup> by _𝐽_<sup>∗</sup> . Then


and


Therefore, unless _𝑦_<sup>∗</sup> = 0, _𝐽_<sup>∗</sup> cannot be negative definite, which means that the fixed points with non-zero imaginary parts cannot be stable.

18

_C h a p t e r 3_

---

[← INTRODUCTION](06-introduction.md) · [Up: contents](index.md) · [AN EXTRINSIC NOISE MODEL FOR NORMALIZATION →](08-an-extrinsic-noise-model-for-normalization.md)
