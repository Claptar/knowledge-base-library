---
title: 16 Lecture Sixteen
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 16 Lecture Sixteen

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **16.1 Conditional Expectation**

Given two random variables _X_ and _Y_ , the conditional expectation (or conditional mean) of _Y_ given _X_ = _X_ is denoted by


and is defined as the expectation of the conditional distribution of _Y_ given _X_ = _x_ .

We can write


More generally


and also


The most important fact about conditional expectation is the **Law of Iterated Expectation** (also known as the **Law of Total Expectation** ). We shall see this next.

82

#### **16.1.1 Law of Iterated/Total Expectation**

The law of total expectation states that


Basically the law of total expectation tells us how to compute the expectation of E( _Y_ ) using knowledge of the conditional expectation of _Y_ given _X_ = _x_ . Note the similarity to law of total probability which specifies how to compute the marginal distribution of _Y_ using knowledge of the conditional distribution of _Y_ given _X_ = _x_ .

The law of total expectation can be proved as a consequence of the law of total probability. The proof when _Y_ and _X_ are continuous is given below. The proof in other cases (when one or both of _Y_ and _X_ are discrete) is similar and left as an exercise.

**Proof of the law of total expectation:** Assume that _Y_ and _X_ are both continuous. Then


By the law of total probability, we have


which proves the law of total expectation.

There is an alternate more succinct form of stating the law of total expectation which justifies calling the law of **iterated** expectation. We shall see this next. Note that E( _Y |X_ = _x_ ) depends on _x_ . In other words, E( _Y |X_ = _x_ ) is a function of _x_ . Let us denote this function by _h_ ( _·_ ):


If we now apply this function to the random variable _X_ , we obtain a new random variable _h_ ( _X_ ). This random variable is denoted by simply E( _Y |X_ ) i.e.,


Note that when _X_ is discrete, the expectation of this random variable E( _Y |X_ ) becomes


And when _X_ is continuous, the expectation of E( _Y |X_ ) is


Observe that the right hand sides in these expectations are precisely the terms on the right hand side of the law of total expectation. Therefore the law of total expectation can be rephrased as


83

Because there are two expectations on the right hand side, the law of total expectation is also known as the Law of Iterated Expectation.

The law of iterated expection has many applications. A couple of simple examples are given below following which we shall explore applications to _risk minimization_ .

**Example 16.1.** _Consider a stick of length ℓ. Break it at a random point X that is chosen uniformly across the length of the stick. Then break the stick again at a random point Y that is also chosen uniformly across the length of the stick. What is the expected length of the final piece?_

_According to the description of the problem,_


_and we are required to calculate_ E( _Y_ ) _. Note first that_ E( _Y |X_ = _x_ ) = _x/_ 2 _for every x which means that_ E( _Y |X_ ) = _X/_ 2 _. Hence by the Law of Iterated Expectation,_


**Example 16.2.** _Suppose X, Y, Z are i.i.d Unif_ (0 _,_ 1) _random variables. Find the value of_ P _{X ≤ Y Z}?_

_By the Law of Iterated Expectation,_


**Example 16.3** (Sum of a random number of i.i.d random variables) **.** _Suppose X_ 1 _, X_ 2 _, . . . are i.i.d random variables with_ E( _Xi_ ) = _µ. Suppose also that N is a discrete random variable that takes values in {_ 1 _,_ 2 _, . . . , } and that is independent of X_ 1 _, X_ 2 _, . . . . Define_


_In other words, S is the sum of a random number (N ) of the random variables Xi. The law of iterated expectation can be used to compute the expectation of S as follows:_


_This fact is actually a special case of a general result called_ **_Wald’s identity_** _._

#### **16.1.2 Application of the Law of Total Expectation to Statistical Risk Minimization**

The law of the iterated expectation has important applications to statistical risk minimization problems. The simplest of these problems is the following.

**Problem 1:** Given two random variables _X_ and _Y_ , what is the function _g_<sup>_∗_</sup> ( _X_ ) of _X_ that minimizes


over all functions _g_ ? The resulting random variable _g_<sup>_∗_</sup> ( _X_ ) can be called the Best Predictor of _Y_ as a function of _X_ in terms of expected squared error.

To find _g_<sup>_∗_</sup> , we use the law of iterated expectation to write


84

The value _g_<sup>_∗_</sup> ( _x_ ) which minimizes the inner expectation:


is simply


This is because E( _Z − c_ )<sup>2</sup> is minimized as _c_ varies over R at _c_<sup>_∗_</sup> = E( _Z_ ). We have thus proved that the function _g_<sup>_∗_</sup> ( _X_ ) which minimizes _R_ ( _g_ ) over all functions _g_ is given by


Thus the function of _X_ which is closest to _Y_ in terms of _expected squared error_ is given by the conditional mean E( _Y |X_ ).

Let us now consider a different risk minimization problem.

**Problem 2:** Given two random variables _X_ and _Y_ , what is the function _g_<sup>_∗_</sup> ( _X_ ) of _X_ that minimizes


over all functions _g_ ? The resulting random variable _g_<sup>_∗_</sup> ( _X_ ) can be called the Best Predictor of _Y_ as a function of _X_ in terms of expected absolute error.

To find _g_<sup>_∗_</sup> we use the law of iterated expectation to write


The value _g_<sup>_∗_</sup> ( _x_ ) which minimizes the inner expectation:


is simply given by any conditional median of _Y_ given _X_ = _x_ . This is because E _|Z − c|_ is minimized as _c_ varies over R at any median of _Z_ . To see this, assume that _Z_ has a density _f_ and write


Differentiating with respect to _c_ , we get


Therefore when _c_ is a median, the derivative of E _|Z − c|_ will equal zero. This shows that _c �→_ E _|Z − c|_ is minimized when _c_ is a median of _Z_ .

We have thus shown that the function _g_<sup>_∗_</sup> ( _x_ ) which minimizes _R_ ( _g_ ) over all functions _g_ is given by any conditional mean of _Y_ given _X_ = _x_ . Thus the conditional mean of _Y_ given _X_ = _x_ is the function of _X_ that is closest to _Y_ in terms of expected absolute error.

**Problem 3:** Suppose _Y_ is a binary random variable taking the values 0 and 1 and let _X_ be an arbitrary random variable. What is the function _g_<sup>_∗_</sup> ( _X_ ) of _X_ that minimizes

_R_ ( _g_ ) := P _{Y̸_ = _g_ ( _X_ ) _}_

85

over all functions _g_ ? To solve this, again use the law of iterated expectation to write


In the inner expectation above, we can treat _X_ as a constant so that the problem is similar to minimizing P _{Z̸_ = _c}_ over _c ∈_ R for a binary random variable _Z_ . It is easy to see that P _{Z̸_ = _c}_ is minimized at _c_<sup>_∗_</sup> where


In case P _{Z_ = 1 _}_ = P _{Z_ = 0 _}_ , we can take _c_<sup>_∗_</sup> to be either 0 or 1. From here it can be deduced (via the law of iterated expectation) that the function _g_<sup>_∗_</sup> ( _X_ ) which minimizes P _{Y̸_ = _g_ ( _X_ ) _}_ is given by


**Problem 4:** Suppose again that _Y_ is binary taking the values 0 and 1 and let _X_ be an arbitrary random variable. What is the function _g_<sup>_∗_</sup> ( _X_ ) of _X_ that minimizes


Using an argument similar to the previous problems, deduce that the following function minimizes _R_ ( _g_ ):


The argument (via the law of iterated expectation) used in the above four problems can be summarized as follows. The function _g_<sup>_∗_</sup> which minimizes


over all functions _g_ is given by


### **16.2 Conditional Variance**

Given two random variables _Y_ and _X_ , the conditional variance of _Y_ given _X_ = _x_ is defined as the variance of the conditional distribution of _Y_ given _X_ = _x_ . More formally,


Like conditional expectation, the conditional variance _V ar_ ( _Y |X_ = _x_ ) is also a function of _x_ . We can apply this function to the random variable _X_ to obtain a new random variable which we denote by _V ar_ ( _Y |X_ ). Note that


Analogous to the Law of Total Expectation, there is a Law of Total Variance as well. This formula says that


86

To prove this formula, expand the right hand side as

E( _V ar_ ( _Y |X_ )) + _V ar_ (E( _Y |X_ )) = E �E( _Y_<sup>2</sup> _|X_ ) _−_ (E( _Y |X_ ))<sup>2�</sup> + E (E( _Y |X_ ))<sup>2</sup> _−_ (E(E( _Y |X_ ))<sup>2</sup> = E(E( _Y_<sup>2</sup> _|X_ )) _−_ E(E( _Y |X_ ))<sup>2</sup> + E(E( _Y |X_ ))<sup>2</sup> _−_ (E( _Y_ ))<sup>2</sup> = E( _Y_<sup>2</sup> ) _−_ (E _Y_ )<sup>2</sup> = _V ar_ ( _Y_ ) _._

**Example 16.4.** _We have seen before that_


_This, of course, means that_


_Using the laws of total expectation and total variance, it is possible to prove these directly as follows._


_and_


**Example 16.5** (Sum of a random number of i.i.d random variables) **.** _Suppose X_ 1 _, X_ 2 _, . . . are i.i.d random variables with_ E( _Xi_ ) = _µ and V ar_ ( _Xi_ ) = _σ_<sup>2</sup> _< ∞. Suppose also that N is a discrete random variable that takes values in {_ 1 _,_ 2 _, . . . , } and that is independent of X_ 1 _, X_ 2 _, . . . . Define_


_We have seen previously that_


_Using the law of total variance, we can calculate V ar_ ( _X_ ) _as follows._

_V ar_ ( _S_ ) = E( _V ar_ ( _S|N_ )) + _V ar_ (E( _S|N_ )) = E( _Nσ_<sup>2</sup> ) + _V ar_ ( _Nµ_ ) = _σ_<sup>2</sup> (E _N_ ) + _µ_<sup>2</sup> _V ar_ ( _N_ ) _._

---

[← 15 Lecture Fifteen](16-15-lecture-fifteen.md) · [Up: contents](index.md) · [17 Lecture Seventeen →](18-17-lecture-seventeen.md)
