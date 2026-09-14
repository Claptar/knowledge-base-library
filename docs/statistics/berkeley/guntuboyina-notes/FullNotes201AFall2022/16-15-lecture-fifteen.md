---
title: 15 Lecture Fifteen
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 15 Lecture Fifteen

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **15.1 LTP and Bayes Rule for general random variables**

The LTP describes how to compute the distribution of _X_ based on knowledge of the conditional distribution of _X_ given Θ = _θ_ as well as the marginal distribution of Θ. The Bayes rule describes how to compute the conditional distribution of Θ given _X_ = _x_ based on the same knowledge of the conditional distribution of _X_ given Θ = _θ_ as well as the marginal distribution of Θ.

The precise formulae for the LTP and Bayes Rule can be broken down into four cases according to whether _X_ and/or Θ is discrete or continuous.

#### **15.1.1** _X_ **and** Θ **are both discrete**

The LTP is


and the Bayes rule is


**15.1.2** _X_ **and** Θ **are both continuous**

Here LTP is


75

and Bayes rule is


**15.1.3** _X_ **is discrete while** Θ **is continuous**

LTP is


and Bayes rule is


**15.1.4** _X_ **is continuous while** Θ **is discrete**

LTP is


and Bayes rule is

These formulae are useful when the conditional distribution of _X_ given Θ = _θ_ as well as the marginal distribution of Θ are given as part of the model specification and the goal is to determine the marginal distribution of _X_ as well as the conditional distribution of Θ given _X_ = _x_ .

We shall look at some more applications of these formulae today.

### **15.2 A Simple Model Selection Application**

Suppose Θ has the _Ber_ (0 _._ 5) distribution i.e.,


Next assume that _X_ 1 _, . . . , Xn_ have the following distributions conditional on Θ = _θ_ :

and


_f_ 0 is the standard normal density and _f_ 1 is a Laplace density. Both densities have the same maximal value of 1 _/√_ 2 _π_ . Based on the information given, calculate the conditional distribution of Θ given _X_ 1 = _x_ 1 _, X_ 2 = _x_ 2 _, . . . , X_ 6 = _x_ 6 (i.e., _n_ = 6) where


76

Here is the context for this question. We observe data _x_ 1 _, . . . , xn_ with _n_ = 6. We want to use one of the models _f_ 0 or _f_ 1 for this data. The random variable Θ is used to describe the choice of the model. We want to treat both the models on an equal footing so we assumed that Θ has the uniform prior distribution on _{_ 0 _,_ 1 _}_ .

To calculate the conditional distribution of Θ given the data, we use the formula (74) because Θ is discrete and the data _X_ 1 _, . . . , Xn_ are continuous. This gives


Similarly


Plugging in the above formula the data values given in (75) for _x_ 1 _, . . . , x_ 6, we obtain


Thus, conditioning on the data, we have a 72% probability for the normal model compared to 28% probability for the Laplace model. Now suppose that we add in an additional observation _x_ 7 = 5. It can be checked that


Now there is overwhelming preference for the Laplace model. This is because _x_ 7 = 5 is an outlying observation to which the Laplace model gives much higher probability compared to the Normal model owing to heavy tails of the Laplace density.

### **15.3 Model Selection with unknown parameters**

Suppose Θ has the _Ber_ (0 _._ 5) distribution i.e.,


Next assume that _X_ 1 _, . . . , Xn_ have the following distributions conditional on Θ = _θ_ :


77

and

_X_ 1 _, . . . , Xn |_ Θ = 1<sup>i.i.d</sup> _∼ Lap_ (0 _, σ_ 1) for some _σ_ 1 _>_ 0 _._

Here _Lap_ (0 _, σ_ 1) denotes the Laplace density centered at 0 and having scale _σ_ 1; its density is given by


Based on this information, calculate the conditional distribution of Θ given _X_ 1 = _x_ 1 _, . . . , Xn_ = _xn_ where _n_ = 10 and _x_ 1 _, . . . , xn_ are given by


Once again, this is a model selection problem where we need to choose between the normal model and the Laplace model based on the observed data given above. We can proceed exactly as in the last section and write down the conditional probabilities of Θ given _X_ 1 = _x_ 1 _, . . . , Xn_ = _xn_ . However the answers would depend on _σ_ 0 and _σ_ 1. We would not be able to make a decision between the two models because of this annoying dependence on _σ_ 0 _, σ_ 1. To get rid of the dependence on the specific values of _σ_ 0 _, σ_ 1, a natural strategy is to treat _σ_ 0 and _σ_ 1 as unknown parameters and further make distributional assumptions on them to reflect our ignorance of their precise values. One way of doing this is to assume that:


as well as


for a large constant value _C_ . In other words, we are using the uniform distribution on ( _−C, C_ ) to reflect our ignorance of log _σ_ 0 and log _σ_ 1. We can now calculate the conditional distribution of Θ given _X_ 1 = _x_ 1 _, . . . , Xn_ = _xn_ in the following way. As in the previous section, we first obtain


and similarly


We therefore need to calculate


These densities are not directly given to us (unlike in the problem of the previous section) but they are given conditionally on the parameters _σ_ 0 and _σ_ 1. We shall therefore calculate

78

them using the Law of Total Probability (72) (note that _X_ 1 _, . . . , Xn_ as well as _σ_ 0 _, σ_ 1 are all continuous parameters). We thus have


Because we assumed that log _σ_ 0 has the uniform distribution on ( _−C, C_ ) (conditional on Θ = 0), we get


As a result


Because _C_ is large, the limits in the above integral will effectively be between 0 and _∞_ (as _e_<sup>_−C_</sup> _≈_ 0 and _e_<sup>_C_</sup> _≈∞_ ). Thus


To evaluate the integral above, we use the change of variable


which gives


79

#### Similarly


The change of variable


leads to


Plugging these expressions in (79) and (80), we obtain


and


Now the observed data values in (76) can be plugged in to compute the posterior probabilities. This gives


Thus the observed data in (76) (which seems to contain some outliers) overwhelmingly favors the Laplace model compared to the Normal model.

80

#### **15.3.1 Considering one more model**

Suppose now that Θ has the distribution given by:


and that _X_ 1 _, . . . , Xn_ have the following distributions conditional on Θ = _θ_ :

and


and


Here _C_ (0 _, σ_ 2) is the Cauchy density with location parameter 0 and scale parameter _σ_ 2. This density is given by _π_ <u>1</u> _x_<sup>2</sup> _<u>σ</u>_ +2 _σ_ 2<sup>2.</sup> What then is the conditional distribution of Θ given _X_ 1 = _x_ 1 _, . . . , Xn_ = _xn_ for the same data (76)?

This is basically the same problem as that considered in the previous section except that we are considering the Cauchy model in addition to the normal and the Laplace models.

Using the Bayes rule, it is easy to see that


for each _θ_ = 0 _,_ 1 _,_ 2. The calculation for _fX_ 1 _,...,Xn|_ Θ= _θ_ ( _x_ 1 _, . . . , xn_ ) for _θ_ = 0 and _θ_ = 1 is done based on the assumptions (77) and (78), and this leads to exactly the same values as in the previous section. More specifically


and


For _fX_ 1 _,...,Xn|_ Θ=2( _x_ 1 _, . . . , xn_ ), we shall make the assumption (analogous to (77) and (78)):

log _σ_ 2 _|_ Θ = 2 _∼_ Unif( _−C, C_ ) and _X_ 1 _, . . . , Xn | σ_ 2 _,_ Θ = 2<sup>i.i.d</sup> _∼ C_ (0 _, σ_ 2) _._

This leads to


It is probably difficult to calculate this integral in closed form. But it is quite straightforward to compute this numerically (in the code file, I computed this after the change of variable _t_ = log _σ_ 2).

81

For the dataset in (76), the above analysis leads to


Thus the Cauchy model has the highest probability. The Laplace model which received the highest probability when only the two models (Normal and Laplace) were being considered now gets low probability when we are also considering the Cauchy model.

This approach for Model Selection is often known as Bayesian Model Selection. An important role in this approach is played by the quantities _fX_ 1 _,...,Xn|_ Θ= _θ_ ( _x_ 1 _, . . . , xn_ ) for different values of _θ_ . In the Machine Learning literature, this quantity is known as the **Evidence** for the model represented by Θ = _θ_ in light of the observed data _x_ 1 _, . . . , xn_ . When each individual model contains additional parameters (such as in the present case where the _i_<sup>_th_</sup> model is expressed in terms of the parameter _σi_ ), the Evidence is calculated (via the Law of Total Probability) as the integral of the probability for each value of the parameter with respect to a prior on the parameter. Thus the Evidence for a model is also known as the **Integrated Likelihood** of the model.

For more on Bayesian model selection using Evidences, see Jaynes [1, Chapter 20] or MacKay [5, Chapter 28].

---

[← 14 Lecture Fourteen](15-14-lecture-fourteen.md) · [Up: contents](index.md) · [16 Lecture Sixteen →](17-16-lecture-sixteen.md)
