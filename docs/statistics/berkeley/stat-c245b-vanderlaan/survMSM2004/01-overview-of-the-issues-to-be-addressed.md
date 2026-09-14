---
title: Overview of the issues to be addressed
source: https://vanderlaan-lab.org/teach-files/survMSM2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/survMSM2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Overview of the issues to be addressed

**Source:** [`survMSM2004.pdf`](https://vanderlaan-lab.org/teach-files/survMSM2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Question of interest: defining a causal effect on a survival outcome

- Data structures: terminology and notations

- Survival causal parameter of interest: describing survival causal effects with MSMs

- How to identify and estimate MSM parameters: naive approach, IPTW estimator, assumptions, implementation, intuitive understanding

- Illustration with simulations

- Generalization of the approach to censored data and other estimators

_−→_ Illustration with an example

Romain Neugebauer - 2

#### **Question of interest**

What is the causal effect of a _treatment_ on an survival outcome marginally or conditionally on a covariate?

- At the unit level, a causal effect can be defined by comparing treatment-specific survival outcomes.

- At the population level, it can be defined by the influence of a change in treatment values on the (conditional) distribution of treatment-specific survival outcomes or counterfactuals.

Two types of causal questions of interest corresponding with two data structures:

- point-treatment data structure: the treatment of interest is a random variable occurring at one time point.

- longitudinal data structure: the treatment of interest is a stochastic process, i.e. a collection of random variables measured over time.

- _−→_ The framework and notations for longitudinal data is more general.

Romain Neugebauer - 3

#### **Illustration**

Causal effect of a chemotherapy drug on patients’ survival.

The average marginal causal effect of the chemotherapy is the difference between:1) the average survival time if all patients are treated with chemotherapy and 2) the average survival time if all patients are not treated with chemotherapy.

The average adjusted causal effect of the chemotherapy per strata of sex in the population is define by the two following differences:

- 1) the average survival time if all male patients are treated with chemotherapy and 2) the average survival time if all male patients are not treated with chemotherapy.

- 1) the average survival time if all female patients are treated with chemotherapy and 2) the average survival time if all female patients are not treated with chemotherapy.

- _−→_ This example can be used as a longitudinal data example as well (different drug doses assigned over time).

Romain Neugebauer - 4

#### **Data structures**

Whether the data are point-treatment data or longitudinal data, one can define two data sets:

- the full data: data from the ideal experiment in which all counterfactuals are collected for every subject.

_−→_ It is typically impossible to conduct such an ideal experiment in practice.

- the observed data: data that can be observed in practice in which one unique outcome is typically measured under one treatment per subject.

   - _−→_ It corresponds with a subset of the full data.

Note that causal effects are defined using the full data but only the observed data is available to evaluate these causal effects.

_−→_ Notations used to represent both data sets for both pointtreatment and longitudinal data structures.

Romain Neugebauer - 5

#### **Statistical framework for causal inference**

###### **Notations:**

- Observed treatment:

   - for point-treatment data: _A_ , possibly multivariate, i.e., _A_ = ( _A_ 1 _, . . . , AK_ )

   - for longitudinal data (history): _A_ ( _t_ ) for _t_ = 0 _, . . . , T −_ 1:


generalize notation for treatment up to time _t_ : _A_ ¯( _t_ )

- Possible outcome values _a_ or _a_ ¯

- Space of all possible treatments: _A_ , i.e., _a_ or _a_ ¯ _∈A_

Romain Neugebauer - 6

#### **Statistical framework for causal inference**

- Observed covariate:

   - for point-treatment data: baseline covariates _W ⊃ V_ (possibly multivariate) and _Y_ ( _t_ ) = _I_ ( _T ≤ t_ ) for _t_ = 0 _, . . . , T_ :

_Y_ ¯ ( _T_ ) = ( _Y_ (0) _, . . . , Y_ ( _T_ )) _,_

- for longitudinal data: _L_ ( _t_ ) = ( _W_ ( _t_ ) _, Y_ ( _t_ ) = _I_ ( _T ≤ t_ )) for _t_ = 0 _, . . . , T_ :

   - _L_ ¯( _T_ ) = ( _L_ (0) _, . . . , L_ ( _T_ )) _,_

where _W_ (0) _⊃ V_ is/are baseline covariate(s).

Note that the survival outcome of interest, _T_ , is included in the observed covariate through the variables _Y_ ( _t_ ) and that there is no censoring.

Romain Neugebauer - 7

#### **Statistical framework for causal inference**

- Counterfactuals:

   - ”variables/processes observed contrary to the fact, i.e. under a treatments which are not the observed treatment”.

By extension, treatment-specific variables/processes:

- for point treatment data: _Ta_ and _Ya_ ( _t_ ) = _I_ ( _Ta ≤ t_ ) for _t_ = 0 _, . . . , Ta_

- for longitudinal data: _Ta_ ¯ and _La_ ¯( _t_ ) for _t_ = 0 _, . . . , Ta_ ¯, i.e. _L_<sup>¯</sup> _a_ ¯( _Ta_ ¯)

- Note the difference between _E_ ( _T | A_ = _a_ ) and _E_ ( _Ta_ ).

Romain Neugebauer - 8

#### **Statistical framework for causal inference**

- Full data = ideal data: _X ∼ FX_

   - for point treatment data: _X_ = ( _W,_ ( _Y_<sup>¯</sup> _a_ ( _Ta_ )) _a∈A_ ) or a simpler representation is _X_ = ( _W,_ ( _Ta_ ) _a∈A_ )

   - for longitudinal data: _X_ = ( _L_<sup>¯</sup> _a_ ¯( _Ta_ ¯)) _a_ ¯ _∈A_ or a simpler representation is _X_ = ( _Ta_ ¯ _, W_<sup>¯</sup> _a_ ¯( _Ta_ ¯)) _a_ ¯ _∈A_

In particular, it includes all treatment-specific outcomes and baseline covariates.

- Observed data = only available data: _O ∼ P_

   - for point treatment data: _O_ = ( _W, A, Y_<sup>¯</sup> ( _T_ )) or a simpler representation is _O_ = ( _W, A, T_ )

   - for longitudinal data:

_O_ = ( _L_<sup>¯</sup> ( _T_ ) _, A_<sup>¯</sup> ( _T −_ 1)) = ( _L_ (0) _, A_ (0) _, L_ (1) _, A_ (1) _, . . . , A_ ( _T −_ 1) _, L_ ( _T_ )) or a simpler representation is _O_ = ( _T, W_<sup>¯</sup> ( _T_ ) _, A_<sup>¯</sup> ( _T −_ 1))

- _−→_ **The longitudinal data notations cover the point treatment data notations (more general)**

Romain Neugebauer - 9

#### **Defining the survival causal parameter of interest**

A **(conditional) survival causal effect** can be described by the following parameters:

- at the subject/unit level by log _Ta_ ¯1 _−_ log _Ta_ ¯2,

- at the population level by

**–** _βa_ ¯1 _,a_ ¯2( _V_ ) = _E_ (log _Ta_ ¯1 _−_ log _Ta_ ¯2 _| V_ ) = _E_ (log _Ta_ ¯1 _| V_ ) _− E_ (log _Ta_ ¯2 _| V_ ), **–** _βa_ ¯1 _,a_ ¯2( _V_ ) = median(log _Ta_ ¯1 _| V_ )-median(log _Ta_ ¯1 _| V_ ),

**–** etc.

If _V_ = _∅_ , _βa_ ¯1 _,a_ ¯2 describe marginal causal effects unlike _βa_ ¯1 _,a_ ¯2( _V_ ) describe adjusted causal effects.

Typically it is the average causal effect that is of interest and it is described by the parameter:


Romain Neugebauer - 10

#### **Defining the survival causal parameter of interest**

Such a parameter _β_<sup>_∗_</sup> is typically very high-dimensional and nonparametric estimation of _β_ is then not possible with finite sample data or suffer from poor practical performance: curse of dimensionality.

A parametric model can be used to summarize a very high-dimensional parameter into a lower-dimensional parameter of interest _β_ .

A parametric Marginal Structural Model describes average causal effects with a lower-dimensional parameter _β_ using the mean feature of the counterfactuals distribution:

_E_ (log _Ta_ ¯ _| V_ ) = _m_ (¯ _a, V | β_ ) _,_

e.g. _β_ = ( _β_ 1 _, β_ 2 _, β_ 3) and _m_ (¯ _a, V | β_ ) = _β_ 0 + _β_ 1mean(¯ _a_ ) + _β_ 2 _V_ + _β_ 3mean(¯ _a_ ) _V._

_−→ β_ is the survival causal parameter of interest

Romain Neugebauer - 11

#### **Defining the survival causal parameter of interest**

We proposed to describe survival causal effects by comparing mean treatment-specific log _Ta_ ¯ per strata of _V_ however survival causal effects can be described by comparing other mean treatment-specific survival outcomes like:

- the hazard of survival per strata of _V_ : _λa_ ¯( _t | V_ ) = _P_ ( _Ta_ ¯ = _t | Ta_ ¯ _> t, V_ ) �

- _•_ the survival function per strata of _V_ : _Sa_ ¯( _t | V_ ) = _j≤t_<sup>(1</sup><sup>_−λ_</sup> _a_ ¯<sup>(</sup><sup>_j| V_).</sup>

- Similarly , Marginal Structural Models modelling can be used to model these other expected treatment-specific outcomes and describe the average survival causal effects using different parameters of interest. _−→_ In this presentation, we only consider MSMs of the type _E_ (log _Ta_ ¯ _| V_ ) = _m_ (¯ _a, V | β_ ) but results can be generalized to more general MSMs

Romain Neugebauer - 12

#### **Naive approach to MSM estimation**

Consider the estimation problem of the parameter _β_ = ( _β_ 0 _, β_ 1) defined by the following MSM for a point-treatment data set:

_E_ (log _Ta_ ) = _β_ 0 + _β_ 1 _a_

A naive estimation approach would consist in 1) performing a simple regression of log _T_ on _A_ using the association model _α_ 0 + _α_ 1 _A_ and 2) interpreting the resulting estimate _α_ ˆ as an estimate of _β_ . This is saying that _E_ (log _T | A_ = _a_ ) = _E_ (log _Ta_ ) for all _a ∈A_ .

This equality holds only if treatment _A_ is randomized, i.e. _A ⊥_ ( _Ya_ ) _a∈A_ .

In most cases, the effect of _A_ on _T_ is confounded and treatment _A_ is thus not randomized. Using this naive estimation procedure leads to bias estimation of _β_ .

_−→_ This type of bias is similar to the bias induced by informative censoring, i.e. by missing data

Romain Neugebauer - 13

### **How to estimate** _β_ **: a missing data approach**

The observed data _O_ can be linked to the ideal data one would have liked to observe to investigate the average causal effect of interest. The ideal data corresponds with _n_ i.i.d. observations of the full data _X_ = ( _L_<sup>¯</sup> _a_ ¯( _Ta_ ¯)) _a_ ¯ _∈A_ = ( _Ta_ ¯ _, W_<sup>¯</sup> _a_ ¯( _Ta_ ¯)) _a_ ¯ _∈A ∼ FX_ and we can link _X_ to _O_ as follows:

_O_ = Φ( _A, X_<sup>¯</sup> ) = ( _A_<sup>¯</sup> ( _T −_ 1) _, L_<sup>¯</sup> ¯ _A_ ( _T −_ 1)( _T_ )) = ( _A_<sup>¯</sup> ( _T −_ 1) _, T_ ¯ _A_ ( _T −_ 1) _, W_<sup>¯</sup> ¯ _A_ ( _T −_ 1)( _T_ )) _._ The problem of estimating _β_ using _O_ can thus be treated as a missing data problem. The estimation methods developed for missing data problems can thus be applied to the estimation of causal parameters defined by MSMs.

_−→_ Certain conditions are necessary, at least in practice, for the identification of _β_ with _O_ .

Romain Neugebauer - 14

### **Conditions for identification of** _β_

- Correct MSM specification: _∃ β ∈ IR E_ (log _Ta_ ¯ _| V_ ) = _m_ (¯ _a, V | β_ )

- Existence of counterfactuals

- Time ordering: _L_<sup>¯</sup> _a_ ¯( _t_ ) = _L_<sup>¯</sup> _a_ ¯( _t−_ 1)( _t_ ) (causal graph not deductible from the data only)

_•_ Consistency assumption: _L_ ( _t_ ) = _L_ ¯ _A_ ( _t_ )

- Sequential Randomization Assumption (SRA):

_A_ ( _t_ ) _⊥ X | A_<sup>¯</sup> ( _t −_ 1) _, L_<sup>¯</sup> ( _t_ )

This assumption is called the No Unobserved Confounder assumption or Randomization assumption (RA) for point-treatment data. It is necessary **in practice** for identification of _β_ when one is not willing to make specific assumptions about _FX_ likely not to hold in most cases.

_−→_ Under these assumptions, it is possible to estimate _β_ consistently with the available data _O_ (under additional assumptions).

Romain Neugebauer - 15

---

[Up: contents](index.md) · [The Sequential Randomization Assumption →](02-the-sequential-randomization-assumption.md)
