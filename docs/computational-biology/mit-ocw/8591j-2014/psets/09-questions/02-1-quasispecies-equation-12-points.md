---
title: 1 Quasispecies Equation (12 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/09-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Quasispecies Equation (12 points)

**Source:** `psets/09-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This problem will introduce you to the quasispecies equation and teach you how to set up the equation for a few diferent scenarios. The word quasispecies refers to a group of individuals that form a single species but have slightly diferent genotypes. The quasispecies equation, frst formulated by Manfred Eigen and Peter Schuster, is a mathematical model that describes how the frequencies of diferent genotypes change within a population over time. Let's take a look at this equation<sup>1</sup> :


_←→_

Here, _xi_ and _fi_ are the frequency and ftness of genotype _i_ . _Q_ is the mutation matrix. _Qji ←→_ denotes the fraction of individuals of genotype _j_ that mutate to genotype _i_ . \e note that _Q_ is a _←→_ right stochastic matrix (transition matrix), i.e., _Q_ is a square matrix of nonnegative real numbers, with each row summing up to 1 . _φ_ ( _ix_ ) = Σ _ifixi_ is the average ftness of the population.

- a. [6 points] Now that we know what the various terms mean, it's time to perform a sanity check on the quasispecies equation.

         - _←→_

   1. Explain in words what it means when _Q_ is equal to the identity matrix.

      - _←→_

   2. Set the mutation matrix _Q_ equal to the identity matrix and simplify the quasispecies equation to obtain an equation for _x_ ˙ _i_ .

   3. The frequencies of all the genotypes must add up to 1 ( Σ _ixi_ = 1 ). So what is Σ _ix_ ˙ _i_ ?

   4. Verify your result in part a3 by summing up the simplifed quasispecies expression you found for _x_ ˙ _i_ in part a2.

            - _←→_

- b. [6 points] Let's return to the original quasispecies equation. ( _Q_ is an arbitrary right stochas­ tic matrix.) _φ_ ( _ix_ ) _≡ φ_ ( _ix_ ( _t_ )) denotes the average ftness of the population at time _t_ . Defne _ψ_ ( _t_ ) = ´0 _t_<sup>_φ_(</sup><sup>_ix_(</sup><sup>_s_))</sup><sup>_ds_and</sup><sup>_Ni_(</sup><sup>_t_)=</sup><sup>_N_0</sup><sup>_xi_(</sup><sup>_t_)</sup><sup>_eψ_(</sup><sup>_t_),where</sup><sup>_xi_(</sup><sup>_t_)isthefractionofindividualsof</sup> type _i_ at time _t_ .

   1. Find out the equation for _N_<sup>˙</sup> _i_ ( _t_ ) .

   2. Defne _NT_ ( _t_ ) = _Ni_ ( _t_ ) . How does _N_<sup>˙</sup> _T_ ( _t_ ) depend on _φ_ ( _ix_ ) ?

   3. Show that we can interpret _NT_ as the total population size and _Ni_ as the number of individuals of type _i_ .

> lChapter 3 of "Evolutionary Dynamics" by Martin Nowak.

1

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 9

Note that the ftness of a given individual can depend on the actual population size and on the relative frequencies of other individuals. The population size may be important when resources are limiting. On the other hand, frequency dependent selection can arise when there is a cooperative behavior in the population that can be exploited by cheaters. To incorporate these features into the quasispecies equation, the ftness function can be modifed to include the relevant dependencies _fi_ = _fi_ ( _NT , ix_ ) .

---

[← Problem Set 9 (70 points)](01-problem-set-9-70-points.md) · [Up: contents](index.md) · [2 Adaptation in a Sharply Peaked Fitness Landscape (10 points) →](03-2-adaptation-in-a-sharply-peaked-fitness-landscape-10-points.md)
