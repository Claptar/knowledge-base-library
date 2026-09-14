---
title: 12 Lecture Twelve
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 12 Lecture Twelve

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **12.1 Last Class: Joint Density**

In the last lecture, we started discussing joint densities. Any function _f_ ( _x, y_ ) of two real variables _x_ and _y_ is a joint density provided it is nonnegative and integrates (over both _x_ and _y_ ) to 1. If two random variables _X_ and _Y_ have joint density _fX,Y_ , then


for every set _B ⊆_ R<sup>2</sup> . One further has


which implies that


provided ∆is a small region around the point ( _x, y_ ). The precise shape of the small region ∆is immaterial for (53).

### **12.2 Marginal Densities corresponding to a Joint Density**

Suppose _X_ and _Y_ have joint density _fX,Y_ . Then probabilities involving only the random variable _X_ can be calculated as:


Comparing this with the formula for the density _fX_ ( _x_ ) of a single random variable _X_ :


60

we immediately deduce that _fX_ ( _x_ ) can be written in terms of _fX,Y_ ( _x, y_ ) as:


Analogous, the density _fY_ ( _y_ ) of _Y_ is given by:


In words, the density of a single random variable can be derived by integrating the joint density (of this random variable and another random variable) with respect to the other variable.

When discussing a joint density _fX,Y_ , individual densities _fX_ of _X_ and _fY_ of _Y_ are referred to as _marginal_ densities.

### **12.3 Independence in terms of Joint Densities**

Independence of two random variables _X_ and _Y_ can be characterized in terms of their joint density _fX,Y_ using any of the following statements. The following statements are all equivalent to each other:

1. The random variables _X_ and _Y_ are independent.

2. The joint density _fX,Y_ ( _x, y_ ) factorizes into the product of a function depending on _x_ alone and a function depending on _y_ alone.

3. _fX,Y_ ( _x, y_ ) = _fX_ ( _x_ ) _fY_ ( _y_ ) for all _x, y_ .

**Example 12.1.** _The joint density_


_factorizes into the product of a function depending on x alone and a function depending on y alone because_


_The factorization above immediately says that if f_ = _fX,Y , then X and Y are independent. The marginal densities of X and Y are uniform densities on_ [0 _,_ 1] _._

**Example 12.2.** _Suppose X, Y have the joint density_


_Show that the marginal density of X is given by_


_Are X and Y independent? (Ans: No. Why?)_

61

### **12.4 How linear transformations change joint densities**

In the last lecture, we looked at the following fact. Suppose _X, Y_ have joint density _fX,Y_ and let ( _U, V_ ) = _T_ ( _X, Y_ ) for a linear and invertible transformation _T_ : R<sup>2</sup> _→_ R<sup>2</sup> . Let the inverse transformation of _T_ be denoted by _S_ . Then the joint density of _U_ and _V_ is given by


where _MS_ is the 2 _×_ 2 matrix corresponding to the linear transformation _S_ .

As an example suppose _U_ = _X_ and _V_ = _X_ + _Y_ so that _T_ ( _x, y_ ) = ( _x, x_ + _y_ ) and _S_ ( _u, v_ ) = ( _u, v − u_ ). The matrix corresponding to _S_ is


The determinant of _MS_ is clearly 1. The formula (54) then gives


We shall next study the problem of obtaining the joint densities under differentiable and invertible transformations that are not necessarily linear.

### **12.5 General Invertible Transformations**

Let ( _X, Y_ ) have joint density _fX,Y_ . We transform ( _X, Y_ ) to two new random variables ( _U, V_ ) via ( _U, V_ ) = _T_ ( _X, Y_ ). What is the joint density _fU,V_ ? Suppose that _T_ is invertible (having an inverse _S_ = _T_<sup>_−_1</sup> ) and differentiable. Note that _S_ and _T_ are not necessarily linear transformations.

In order to compute _fU,V_ at a point ( _u, v_ ), we consider


for small _δ_ and _ϵ_ . Let _R_ denote the rectangle joining the points ( _u, v_ ) _,_ ( _u_ + _δ, v_ ) _,_ ( _u, v_ + _ϵ_ ) and ( _u_ + _δ, v_ + _ϵ_ ). Then the above probability is the same as


What is the region _S_ ( _R_ )? If _S_ is linear then _S_ ( _R_ ) (as we have seen in the last class) will be a parallelogram. For general _S_ , the main idea is that, as long as _δ_ and _ϵ_ are small, the region _S_ ( _R_ ) can be approximated by a parallelogram. This is because _S_ itself can be approximated by a linear transformation on the region _R_ . To see this, let us write the function _S_ ( _a, b_ ) as ( _S_ 1( _a, b_ ) _, S_ 2( _a, b_ )) where _S_ 1 and _S_ 2 map points in R<sup>2</sup> to R. Assuming that _S_ 1 and _S_ 2 are differentiable, we can approximate _S_ 1( _a, b_ ) for ( _a, b_ ) near ( _u, v_ ) by


Similarly, we can approximate _S_ 2( _a, b_ ) for ( _a, b_ ) near ( _u, v_ ) by


62

Putting the above two equations together, we obtain that, for ( _a, b_ ) close to ( _u, v_ ),


Therefore _S_ can be appromixated by a linear transformation with matrix given by


for ( _a, b_ ) near ( _u, v_ ). Note that, in particular, when _δ_ and _ϵ_ are small, that this linear appximation for _S_ is valid over the region _R_ . The matrix _JS_ ( _u, v_ ) is called the Jacobian matrix of _S_ ( _u, v_ ) = ( _S_ 1( _u, v_ ) _, S_ 2( _u, v_ )) at the point ( _u, v_ ).

Because of the above linear approximation, we can write


This gives us the important formula


The following is an example of this formula (we derived the result in this example using first principles in the last class)

**Example 12.3.** _Suppose X and Y are two random variables having joint density_ _<u>fX,Y .</u> Define two new random variables R and_ Θ _in the following way. R_ := _√X_<sup>2</sup> + _Y_<sup>2</sup> _and_ Θ _is the angle made by the vector_ ( _X, Y_ ) _with the positive X-axis in the counterclockwise direction. What is the joint density of_ ( _R,_ Θ) _?_

_Clearly_ ( _R,_ Θ) = _T_ ( _X, Y_ ) _where the inverse of T is given by S_ ( _r, θ_ ) = ( _r_ cos _θ, r_ sin _θ_ ) _. The density of_ ( _R,_ Θ) _at_ ( _r, θ_ ) _is zero unless r >_ 0 _and_ 0 _< θ <_ 2 _π. The formula_ (55) _then gives_


_We have thus derived the formula:_


_We can also write this formula as:_


_where_ ~~�~~ _x_<sup>2</sup> + _y_<sup>2</sup> _represents r and θ_ ( _x, y_ ) _is the made by the vector_ ( _x, y_ ) _with the positive X-axis in the counterclockwise direction._

_The formulae_ (56) _and_ (57) _have an important connection to the Herschel-Maxwell derivation of the normal distribution which we discuss next._

### **12.6 The Herschel-Maxwell Derivation of the Normal Distribution**

In the context of Example 12.3, the astronomer John Herschel derived the normal distribution in the following way (this derivation was extended to the three dimensional case by the physicist James Clerk Maxwell). See Jaynes [1, Section 7.2] for more details. Their result is the following.

63

**Fact 12.4.** _Suppose X and Y are two random variables. Suppose that R and_ Θ _are defined as in Example 12.3. Assume the following three conditions:_

_1. X and Y are independent and identically distributed_

_2. R and_ Θ _are independent_

_3._ Θ _is uniformly distributed on_ (0 _,_ 2 _π_ ) _._

_Then X and Y have the normal distribution N_ (0 _, σ_<sup>2</sup> ) _with mean zero and some variance σ_<sup>2</sup> _._

Before proving (12.4), let us note that if _X_ and _Y_ are independently distributed as _N_ (0 _, σ_<sup>2</sup> ), then all the conditions above are true. To see this, observe first that, by independence,


The formula (56) then gives


The above is the joint density of _R_ and Θ at ( _r, θ_ ) provided _r >_ 0 and 0 _< θ <_ 2 _π_ . To make the ranges of the variables _r_ and _θ_ clear, we write


The right hand side above clearly factorizes into the product of a function depending on _r_ alone and a function depending on _θ_ alone. This implies that _R_ and Θ are independent. The marginal distribution of Θ is given by integrating over _r_ :


_<u>r</u>_<sup>2</sup> The substitution _s_ = 2 _σ_<sup>2(so</sup><sup>_ds_=</sup><sup>_rdr/σ_2)leaddsto</sup>


This means that Θ is uniformly distributed over (0 _,_ 2 _π_ ). We have thus proved that all the three conditions of Fact 12.4 are satisfied when _X, Y_ are independently distributed as _N_ (0 _, σ_<sup>2</sup> ).

We shall now prove Fact 12.4 by showing that _X, Y_ being _N_ (0 _, σ_<sup>2</sup> ) is the only way all the three conditions are satisfied.

_Proof of Fact 12.4._ We shall work with (57) which connects the joint density of ( _X, Y_ ) to the joint density of ( _R,_ Θ). Because _X_ and _Y_ are assumed to be independent and identically distributed, the left hand side of (57) becomes


64

where _f_ is the common density of _X_ and _Y_ . On the other hand, because _R_ and Θ are independent and Θ _∼_ Unif(0 _,_ 2 _π_ ), the right hand side of (57) becomes


We thus obtain

for every _−∞ < x, y < ∞_ . Plugging in _y_ = 0 above, we obtain


Plugging in ~~�~~ _x_<sup>2</sup> + _y_<sup>2</sup> in place of _x_ above, we obtain


Combining the above identity with (58), we deduce


This identity implies that _f_ is a symmetric function (i.e., _f_ ( _x_ ) = _f_ ( _−x_ ) = _f_ ( _|x|_ )) because if we take _y_ = 0, we get _f_ ( _x_ ) _f_ (0) = _f_ ( _|x|_ ) _f_ (0) or _f_ ( _x_ ) = _f_ ( _|x|_ ).

Let _h_ : [0 _, ∞_ ) _→_ [0 _, ∞_ ) be defined by


Then (59) implies


or equivalently


This implies that for every nonnegative integer _m_ and _u ≥_ 0,


Two consequences of the above are:


which is obtained by replacing _u_ by _u/n_ in (60), and


which is obtained by replacing _u_ by _u/n_ in (60) and taking _m_ = _n_ . Combining the above two equations, we obtain


65

As _m_ and _n_ are nonnegative integers, we have deduced (take _u_ = 1)


whenever _x ≥_ 0 is a rational number (i.e., of the form _m/n_ for some integers _m_ and _n_ ). If we now assume that _h_ is continuous, we can deduce the above for every _x ≥_ 0. We have thus proved that


for some constants _c_ ( _c_ = _h_ (0)) and _b_ ( _b_ = log<sup>_h_</sup><sup><u>(1)</u></sup> _<u>u</u>_ <u>) =</u> _h_ ( _u_ ) (and _f_ is symmetric), _h_ (0)<sup>).As</sup><sup>_f_(</sup><sup>_√_</sup> we get


We have thus proved that


As _f_ needs to be a valid density, we must have _b <_ 0 so we can write _b_ = _−_ 2 _σ_<sup><u>12</u>forsome</sup> _σ >_ 0. This will necessarily imply that _c_ = _~~√~~_ 21 _πσ_<sup>leadingto</sup><sup>_f_beingthe</sup><sup>_N_(0</sup><sup>_, σ_2)density.</sup> This completes the proof of Fact 12.4.

---

[← 11 Lecture Eleven](12-11-lecture-eleven.md) · [Up: contents](index.md) · [13 Lecture Thirteen →](14-13-lecture-thirteen.md)
