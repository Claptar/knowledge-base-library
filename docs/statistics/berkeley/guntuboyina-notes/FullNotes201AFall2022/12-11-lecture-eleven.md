---
title: 11 Lecture Eleven
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 11 Lecture Eleven

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **11.1 Joint Densities**

Joint densities are used to describe the distribution of a finite set of continuous random variables. We focus on bivariate joint densities (i.e., when there are two continuous variables _X_ and _Y_ ). The ideas are the same for the case of more than two variables.

A real-valued function of two-variables _f_ ( _·, ·_ ) is called a joint density if


We say that two random variables _X_ and _Y_ have joint density _f_ ( _·, ·_ ) if


55

for every subset _B_ of R<sup>2</sup> . We shall often denote the joint density of ( _X, Y_ ) by _fX,Y_ .

Here are two simple examples of joint densities.

**Example 11.1.** _Consider the function_


_First note that this is a valid joint density as this function is always nonnegative and_


_Suppose a pair of random variables_ ( _X, Y_ ) _have this as their joint density. Then probabilities involving X, Y are calculated by integrating the density f_ ( _x, y_ ) _in the appropriate region. For example,_


_The set {_ ( _x, y_ ) : _−_ 1 _≤ x_ + _y ≤_ 2 _} represents the region betwen the two lines x_ + _y_ = 2 _and x_ + _y_ = _−_ 1 _._

**Example 11.2.** _Consider the function_


_This function takes the value 1 on the set {_ ( _x, y_ ) : 0 _≤ x ≤_ 1 _,_ 0 _≤ y ≤_ 1 _} and can also be written succinctly as_


_This is clearly a density function as this is nonnegative and integrates to one (the area of the unit square {_ ( _x, y_ ) : 0 _≤ x ≤_ 1 _,_ 0 _≤ y ≤_ 1 _} equals 1). Suppose the random variables X and Y have this joint density f , then_


_For example,_


In order to calculate joint densities, the following formula is very useful. If ∆is a _small_ region in R<sup>2</sup> around a point ( _x, y_ ), we have


56

More formally,


where the limit is taken as ∆shrinks to ( _x, y_ ). Here are two special cases of this formula:

1. By taking ∆to be the rectangle _{_ ( _a, b_ ) : _x ≤ a ≤ x_ + _δ, y ≤ b ≤ y_ + _ϵ}_ for small _δ_ and _ϵ_ , we get


2. By taking ∆to be the circle centered at ( _x, y_ ) of radius _r_ , we get


The usefulness of the formula (47) is illustrated in the following two examples.

**Example 11.3.** _Suppose_ ( _X, Y_ ) _have the joint density:_


_Define two new random variables R and_ Θ _as follows: R_ := _√X_<sup>2</sup> + _Y_<sup>2</sup> _and_ Θ _is the angle made by the vector_ ( _X, Y_ ) _with the positive X-axis (measured from the positive X-axis in the counterclockwise direction) (note that_ Θ _takes values between_ 0 _and_ 2 _π). What is the joint density of_ ( _R,_ Θ) _?_

_Let us calculate the joint density fR,_ Θ( _r, θ_ ) _of_ ( _R,_ Θ) _at a fixed point_ ( _r, θ_ ) _. Let us assume that r >_ 0 _and_ 0 _< θ <_ 2 _π. One way of calculating this is via_ (48) _:_


_We can calculate_ P _{r < R < r_ + _δ, θ <_ Θ _< θ_ + _ϵ} in the following way:_


_where S is the set of all points_ ( _x, y_ ) _such that r <_ ~~�~~ _x_<sup>2</sup> + _y_<sup>2</sup> _< r_ + _δ and the angle made by_ ( _x, y_ ) _with the positive x-axis lies between θ and θ_ + _ϵ. As can be seen from Figure 2, when δ, ϵ are small, the set S is a small region around the point_ ( _r_ cos _θ, r_ sin _θ_ ) _. Moreover, its area is approximately equal to rϵδ. We thus get_


_Combining the above with_ (58) _, we deduce that_


**Example 11.4.** _Suppose X, Y have joint density fX,Y . What is the joint density of U and V where U_ = _X and V_ = _X_ + _Y ?_

57


Figure 2: The set _S_

_We see that_ ( _U, V_ ) = _T_ ( _X, Y_ ) _where T_ ( _x, y_ ) = ( _x, x_ + _y_ ) _. This transformation T is clearly invertible and its inverse is given by S_ ( _u, v_ ) = _T_<sup>_−_1</sup> ( _u, v_ ) = ( _u, v − u_ ) _. In order to determine the joint density of_ ( _U, V_ ) _at a point_ ( _u, v_ ) _, let us consider_


_Let R denote the rectangle joining the points_ ( _u, v_ ) _,_ ( _u_ + _δ, v_ ) _,_ ( _u, v_ + _ϵ_ ) _and_ ( _u_ + _δ, v_ + _ϵ_ ) _. Then the above probability is the same as_


_where S_ ( _R_ ) _is the image of the rectangle R under the mapping S. How does S_ ( _R_ ) _look like? It is the_ **_parallelogram_** _joining the points_ ( _u, v − u_ ) _,_ ( _u_ + _δ, v − u − δ_ ) _,_ ( _u, v − u_ + _ϵ_ ) _and_ ( _u_ + _δ, v − u_ + _ϵ − δ_ ) _. When δ and ϵ are small, S_ ( _R_ ) _is clearly a small region around_ ( _u, v − u_ ) _which allows us to write_


_The area of the parallelogram S_ ( _R_ ) _can be computed to be δϵ (using the formula that the area of a parallelogram equals base times height) so that_


_Comparing with_ (50) _, we obtain_


_This gives the formula for the joint density of_ ( _U, V_ ) _in terms of the joint density of_ ( _X, Y_ ) _._

The logic behind the above two examples can be extended to obtain formulae for the joint density of an arbitrary transformation of a pair of random variables with known joint density. We shall first consider linear transformations (as in Example 11.4) and, in the next class, consider nonlinear transformations.

58

### **11.2 Joint Densities under General Linear Invertible transformations**

Let us first recall some basic properties of linear transformations.

#### **11.2.1 Linear Transformations**

By a linear transformation _L_ : R<sup>2</sup> _→_ R<sup>2</sup> , we mean a function that is given by


where _M_ is a 2 _×_ 2 matrix and _c_ is a 2 _×_ 1 vector. The first term on the right hand side above involves multiplication of the 2 _×_ 2 matrix _M_ with the 2 _×_ 1 vector with components _x_ and _y_ .

We shall refer to the 2 _×_ 2 matrix _M_ as the matrix corresponding to the linear transformation _L_ and often write _ML_ for the matrix _M_ .

The linear transformation _L_ in (51) is invertible if and only if the matrix _M_ is invertible. We shall only be dealing with invertible linear transformations. The following are two standard properties of linear transformations that you need to familiar with.

1. If _P_ is a parallelogram in R<sup>2</sup> , then _L_ ( _P_ ) is also a parallelogram in R<sup>2</sup> . In other words, linear transformations map parallelograms to parallelograms.

2. For every parallelogram _P_ , the following identity holds:


In other words, the ratio of the areas of _L_ ( _P_ ) to that of _P_ is given by the absolute value of the determinant of the matrix _ML_ .

#### **11.2.2 Invertible Linear Transformations**

Suppose _X, Y_ have joint density _fX,Y_ and let ( _U, V_ ) = _T_ ( _X, Y_ ) for a linear and invertible transformation _T_ : R<sup>2</sup> _→_ R<sup>2</sup> . Let the inverse transformation of _T_ be denoted by _S_ . In the previous example, we had _T_ ( _x, y_ ) = ( _x, x_ + _y_ ) and _S_ ( _u, v_ ) = ( _u, v − u_ ). The fact that _T_ is assumed to be linear and invertible means that _S_ is also linear and invertible.

To compute _fU,V_ at a point ( _u, v_ ), we consider


for small _δ_ and _ϵ_ . Let _R_ denote the rectangle joining the points ( _u, v_ ) _,_ ( _u_ + _δ, v_ ) _,_ ( _u, v_ + _ϵ_ ) and ( _u_ + _δ, v_ + _ϵ_ ). Then the above probability is the same as


What is the region _S_ ( _R_ )? Clearly now _S_ ( _R_ ) is a small region (as _δ_ and _ϵ_ are small) around the point _S_ ( _u, v_ ) so that


59

By the facts mentioned in the previous subsection, we now note that _S_ ( _R_ ) is a parallelogram whose area equals _|det_ ( _MS_ ) _|_ multiplied by the area of _R_ (note that the area of _R_ equals _δϵ_ ). We thus have

_fU,V_ ( _u, v_ ) _δϵ ≈_ P _{_ ( _U, V_ ) _∈ R}_ = P _{_ ( _X, Y_ ) _∈ S_ ( _R_ ) _}_ = _fX,Y_ ( _S_ ( _u, v_ )) _|_ det( _MS_ ) _|δϵ_

which allows us to deduce that


Remember again that _MS_ is the 2 _×_ 2 matrix corresponding to the linear transformation _S_ .

In the next class, we shall see extensions of the formula (54) for nonlinear transformations.

---

[← 10 Lecture Ten](11-10-lecture-ten.md) · [Up: contents](index.md) · [12 Lecture Twelve →](13-12-lecture-twelve.md)
