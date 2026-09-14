---
title: 04 questions
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/psets/04-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 04 questions

**Source:** `psets/04-questions.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**_Systems Biology_**

**_7.81/8.591/9.531_**

**_Problem Set 4 Assigned: 10.21.04 Due in class Due: 11.16.04_**

1. _Waiting times for chemical reactions._

We showed in class that, for a chemical reaction occurring at rate _r_ , the distribution of waiting times τ between reaction events is given by:


- _a_ . By integrating over time, verify that the distribution is normalized.

(5) _b._ Suppose _u_ is a random variable with some distribution ℘ ( _u_ ), and θ ( _u_ ) is a function of _u_ . Then the probability that θ _’_ lies between θ ( _u_ ) and θ ( _u_ + _du_ ) is the same as the probability that _u’_ lies between _u_ and _u_ + _du_ . This gives us a recipe for calculating the distribution ℘ ( θ ):


Assuming _u_ is uniformly distributed between 0 and 1, show that the number


is distributed precisely as required by Eq. 1.

2. _Stochastic simulation of an autoregulatory system._


For the remainder of this problem, use γ = 1.


   - _a._ Suggest a plausible biochemical origin for the hyperbolic repression term in scheme (2).

- (10) _b._ If we measure volume in units of cell size, then concentrations are equivalent to molecule numbers. The accompanying MATLAB code implements a discrete stochastic simulation. Fill in the required lines to model scheme (1). For both _A_ = 10 and _A_ = 100, verify that the variance and mean of the steady state distribution are consistent with Poisson statistics. Print out histograms of final _x_ values in each case, as well as a copy of your code.

- (15) _c._ For scheme (2), set _K_ = 1/100, and choose _B_ so that < _x_ > ~ 100 in steady state. Modify the MATLAB code to model scheme (2). Use the simulation to show that the variance of the autoregulated system is lower than that of the constitutive system with the same mean. Print out the final histogram as well as a copy of your code.

**_FA04_**

1

**Systems Biology                                                                                                7.81/8.591/9.531**

# 2. Stability of a reaction-diffusion system.

In class we discussed the following example of a reaction-diffusion system (equation (128) in the syllabus):


where


In the question below you may assume R >> 1.

- (5)

- _a._ Describe in words what this assumption means.


- _b._ Let’s introduce a new parameter _U_ ≡ _Q_ / _P_ . Give an interpretation for _U_ .

As shown in the syllabus, inhomogeneous perturbations can have the following form:


where A’ and I’ are the variations of the activator and inhibitor concentrations around the homogeneous solution.. There exists a critical value Uc such that, for U > Uc, the homogenous solution is always stable, independent of the perturbation wavelength l . However for U < Uc, stability depends on the value of the wavelength l .

- (10) _c._ Demonstrate that, in order for the homogenous solution to be stable against all inhomogenous perturbations, U should be larger than Uc ≈ 0.17.

- (15) _d._ Plot U versus l and indicate the regions of parameter space for the homogenous solution is stable against inhomogenous perturbations.

- (10) _e._ If U is tuned just below Uc, the homogenous solution is stable for most wavelengths. However, perturbations close to a critical wavelength l _c_ will blow up. Show that the critical wavelength l _c_ ≈ .155 .

FA04

2

---

[Up: contents](../index.md)
