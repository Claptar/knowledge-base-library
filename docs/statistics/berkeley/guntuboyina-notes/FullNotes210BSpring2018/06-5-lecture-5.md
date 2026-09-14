---
title: 5 Lecture 5
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Lecture 5

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This lecture was delivered by Chi Jin. He made some changes to the notes (his modified notes are in the folder).

23

## **5.1 Bounds for the Expected Suprema**

The next major topic of the course involves bounding the quantity:


The two main ideas here are _Symmetrization_ and _Chaining_ . We shall go over symmetrization first.

Symmetrization bounds (30) from above using the _Rademacher complexity_ of the class _F_ . Let us first define the Rademacher complexity. A Rademacher random variable is a random variable _ϵ_ that takes the two values +1 and _−_ 1 with probability 1 _/_ 2 each. For a subset _A ⊆_ R<sup>_n_</sup> , its Rademacher average is defined by


where the expectation is taken with respect to i.i.d Rademacher random variables _ϵ_ 1 _, . . . , ϵn_ . Note first that � _ni_ =1<sup>_ϵiai/n_measuresthe“correlation”betweenthevalues</sup><sup>_a_1</sup><sup>_, . . . , an_andindependentRademachernoise.</sup> This means therefore that _Rn_ ( _A_ ) is large when there exists vectors ( _a_ 1 _, . . . , an_ ) _∈ A_ that fit the Rademacher noise very well. This usually means that the set _A_ is large. In this sense, _Rn_ ( _A_ ) measures the size of the set _A_ .

In the empirical process setup, we have i.i.d random observations _X_ 1 _, . . . , Xn_ taking values in _X_ as well as a class of real-valued functions _F_ on _X_ . Let


This is a random subset of R<sup>_n_</sup> and its Rademacher average, _Rn_ ( _F_ ( _X_ 1 _, . . . , Xn_ )), is a random variable. The expectation of this random variable with respect to the distirbution of _X_ 1 _, . . . , Xn_ is called the Rademacher Complexity of _F_ :


It is easy to see that


where the expectation is taken with respect to _ϵ_ 1 _, . . . , ϵn_ and _X_ 1 _, . . . , Xn_ which are all independent ( _ϵi_ ’s are i.i.d Rademachers and _Xi_ ’s are i.i.d having distribution _P_ ).

The next result shows that the expectation in (30) is bounded from above by twice the Rademacher complexity _Rn_ ( _F_ ).

**Theorem 5.1** (Symmetrization) **.** _We have_


_where the expectation on the left hand side is taken with respect to X_ 1 _, . . . , Xn being i.i.d with distribution P while the expectation on the right hand side is taken both with respect to the X’s and independent Rademachers ϵ_ 1 _, . . . , ϵn._

_Proof._ Suppose _X_ 1<sup>_′, . . . , X_</sup> _n_<sup>_′_are random variables such that</sup><sup>_X_1</sup><sup>_, . . . , Xn, X_</sup> 1<sup>_′, . . . , X_</sup> _n_<sup>_′_are all independent having</sup> the same distribution _P_ . We can then write


24

As a result, we have


The method used above is basically called symmetrization. We now introduce i.i.d Rademacher variables _ϵ_ 1 _, . . . , ϵn_ . Because _Xi_ and _Xi_<sup>_′_areindependentcopies,itisclearthatthedistributionof</sup><sup>_f_(</sup><sup>_Xi_)</sup><sup>_−f_(</sup><sup>_X_</sup> _i_<sup>_′_)is</sup> the same as that of _ϵi_ ( _f_ ( _Xi_ ) _− f_ ( _Xi_<sup>_′_)).Asaresult,wehave</sup>


Theorem 5.1 implies that we can control (30) by bounding from above _Rn_ ( _F_ ). The usual strategy used for bounding _Rn_ ( _F_ ) is the following. One first fixes points _x_ 1 _, . . . , xn ∈X_ and bounds the Rademacher average of the set


If an upper bound is obtained for this Rademacher average that does not depend on _x_ 1 _, . . . , xn_ , then it automatically also becomes an upper bound for _Rn_ ( _F_ ). Note that in order to bound _Rn_ ( _F_ ( _x_ 1 _, . . . , xn_ )) for fixed points _x_ 1 _, . . . , xn_ , we only need to deal with the simple distribution of _ϵ_ 1 _, . . . , ϵn_ which makes this much more tractable.

The main technique for bounding _Rn_ ( _F_ ( _x_ 1 _, . . . , xn_ )) will be _chaining_ . Before we get to chaining however, we shall first look at a more elementary bound that work well in certain situations for Boolean classes _F_ . As we shall see later, this bound will not be as accurate as the bounds given by chaining however.

## **5.2 Simple bounds on the Rademacher Average** _Rn_ ( _F_ ( _x_ 1 _, . . . , xn_ ))

These bounds are based on the following simple result.

**Proposition 5.2.** _Suppose A is a finite subset of_ R<sup>_n_</sup> _with cardinality |A|. Then_


_Proof of Proposition 5.2._ It is trivial to see that for every nonnegative random variable _X_ , one has


25

which can, for example, be proved by interchanging the integral and the probability on the right hand side. We shall use this identity below.

For every _a ∈A_ , we have


The probability bound above comes from Hoeffding’s inequality. From the above, we have


where _|A|_ is the cardinality of _A_ . This can be rewritten as


Now the function _x �→ e_<sup>_x_2</sup> is convex (as can be easily checked by computing the second derivative) so that Jensen’s inequality gives


so that


From here, the inequality given in (32) follows by the trivial inequality:


Let us now apply Proposition 5.2 to control the Rademacher complexity of Boolean Function Classes. We say that _F_ is a Boolean class if _f_ ( _x_ ) takes only the two values 0 and 1 for every function _f_ and every _x ∈X_ . Boolean classes _F_ arise in the problem of classification (where _F_ can be taken to consist of all functions _f_ of the form _I{g_ ( _X_ ) _̸_ = _Y }_ ). They are also important for historical reasons: empirical process theory has its origins in the study of sup _t_ ( _Fn_ ( _t_ ) _− F_ ( _t_ )) which corresponds to taking _F_ := _{I_ ( _−∞, t_ ] : _t ∈_ R _}_ .

Let us now fix a Boolean class _F_ and points _x_ 1 _, . . . , xn_ . The set _F_ ( _x_ 1 _, . . . , xn_ ) (defined as in (31)) is obviously then finite and we can apply Proposition 5.2 to control _Rn_ ( _F_ ( _x_ 1 _, . . . , xn_ )). This gives


26

Because _F_ is Boolean, we can bound each _f_<sup>2</sup> ( _xi_ ) by 1 in the right hand side above to obtain


Now for some classes _F_ , the cardinality _|F_ ( _x_ 1 _, . . . , xn_ ) _|_ can be bounded from above by a polynomial in _n_ for every set of _n_ points _x_ 1 _, . . . , xn ∈X_ . We refer to such classes as classes having <u>polynomial</u> discrimination. For such classes, we can bound R _n_ ( _F_ ( _x_ 1 _, . . . , xn_ )) by a constant multiple of �(log _n_ ) _/n_ for every _x_ 1 _, . . . , xn_ . Because _Rn_ ( _F_ ) is defined as the expectation of R _n_ ( _F_ ( _X_ 1 _, . . . , Xn_ )), we would obtain that, for such Boolean classes, the Rademacher complexity is bounded by a constant multiple of ~~�~~ (log _n_ ) _/n_ .

**Definition 5.3.** _The class of Boolean functions F is said to have_ **_polynomial discrimination_** _if there exists a polynomial ρ_ ( _·_ ) _such that for every n ≥_ 1 _and every set of n points x_ 1 _, . . . , xn in X , the cardinality of F_ ( _x_ 1 _, . . . , xn_ ) _is atmost ρ_ ( _n_ ) _._

How does one check that a given Boolean class _F_ has polynomial discrimination? The most popular way is via the _Vapnik Chervonenkis dimension_ (or simply the VC dimension) of the class.

**Definition 5.4** (VC dimension) **.** _The VC dimension of a class of Boolean functions F on X is defined as the maximum integer D for which there exists a finite subset {x_ 1 _, . . . , xD} of X satisfying_


_The VC dimension is taken to be ∞ if the above condition is satisfied for every integer D._

**Definition 5.5** (Shattering) **.** _A finite subset {x_ 1 _, . . . , xm} of X is said to be_ **_shattered_** _by the Boolean class F if_


_By convention, we extend the definition of shattering to empty subsets as well by saying that the empty set is shattered by every nonempty class F._

It should be clear from the above pair of definitions that an alternative definition of VC dimension is: **The maximum cardinality of a finite subset of** _X_ **that is shattered by** _F_ .

The link between VC dimension and polynomial discrimination comes via the following famous result, knows as the Sauer-Shelah lemma or the VC lemma.

**Lemma 5.6** (Sauer-Shelah-Vapnik-Chevronenkis) **.** _Suppose that the VC dimension of a Boolean class F of functions on X is D. Then for every n ≥_ 1 _and x_ 1 _, . . . , xn ∈X , we have_


_Here_ � _nk_ � _is taken to be 0 if n < k. Moreoever, if n ≥ D, then_

Combining (33) with Lemma 5.6, we obtain the following bound on the control of Rademacher complexity and Expected suprema for Boolean classes with finite VC dimension.

**Proposition 5.7.** _Suppose F is a Boolean function class with VC dimension D. Then, for n ≥ D, we have_


_and_


_Here C is a universal positive constant._

27

**Remark 5.1.** _It turns out that the logarithmic term is not needed in the bounds given by the above proposition. We shall see later that the bounds given by chaining do not have the superfluous logarithmic factor._

We shall provide the proof of Lemma 5.6 in the next subsection. Before that, we give two examples of Boolean classes with finite VC dimension.

**Example 5.8.** _Let V be a D-dimensional vector space of real functions on X . Let F_ := _{I_ ( _f ≥_ 0) : _f ∈V}. The VC dimension of F is at most D._

_Proof._ For any _D_ + 1 points _{x_ 1 _, ..., xD_ +1 _}_ , consider the set


Since _V_ is a _D_ -dimensional vector space, _T_ is a linear subspace of R<sup>_D_+1</sup> with dimension at most _D_ . Therefore there exists _y ∈_ R<sup>_D_+1</sup> and _y̸_ = 0 such that _y_ is orthogonal to the subspace _T_ , i.e.


Without loss of generality, we can assume that there is an index _k_ such that _yk >_ 0. Now suppose _F_ shatters _{x_ 1 _, ..., xD_ +1 _}_ . Then there is _f ∈V_ satisfying


Then we have<sup>�</sup> _i_<sup>_yif_(</sup><sup>_xi_) = �</sup> _i_ : _yi≤_ 0<sup>_yif_(</sup><sup>_xi_) + �</sup> _i_ : _yi>_ 0<sup>_yif_(</sup><sup>_xi_)</sup><sup>_<_0,whichisacontradictionto(34).Thus</sup><sup>_F_</sup> cannot shatter _{x_ 1 _, ..., xD_ +1 _}_ and so the VC dimension is at most _D_ .

**Example 5.9.** _Let Hk denote the indicators of all closed half-spaces in_ R<sup>_k_</sup> _. The VC dimension of Hk is exactly equal to k_ + 1 _._

_Proof._ Left as a homework problem.

---

[← 4 Lecture 4](05-4-lecture-4.md) · [Up: contents](index.md) · [6 Lecture 6 →](07-6-lecture-6.md)
