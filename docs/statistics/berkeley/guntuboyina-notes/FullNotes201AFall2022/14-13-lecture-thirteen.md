---
title: 13 Lecture Thirteen
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 13 Lecture Thirteen

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **13.1 Joint Density under Transformations**

Let ( _X, Y_ ) have joint density _fX,Y_ . We transform ( _X, Y_ ) to two new random variables ( _U, V_ ) via ( _U, V_ ) = _T_ ( _X, Y_ ). Suppose that _T_ is invertible (having an inverse _S_ = _T_<sup>_−_1</sup> ) and differentiable. In the last class, we saw the following formula relating the joint density of ( _U, V_ ) to _fX,Y_ :


Let us start today by working out the following simple application of the formula (61).

**Example 13.1.** _Suppose X and Y are independent random variables with_


_Note the the rate parameter is the same in both the Gamma distributions. Now define_


_What is the joint density of U and V ? Here the transformation T is given by T_ ( _x, y_ ) = ( _x_ + _y, x/_ ( _x_ + _y_ )) _and its inverse transformation can be checked to be S_ ( _u, v_ ) = ( _uv, u_ (1 _−v_ )) _. The formula_ (61) _then gives that for every u >_ 0 _and_ 0 _< v <_ 1 _(we are taking u >_ 0 _because the random variable U is always positive and V is between 0 and 1):_


_Plugging in the relevant Gamma densities for fX and fY , we can deduce that_


66

_This implies that U ∼ Gamma_ ( _α_ 1 + _α_ 2 _, λ_ ) _._ (62) _also implies that the density of V is_


_The above density is known as the Beta density with parameters α_ 1 _and α_ 2 _: Beta_ ( _α_ 1 _, α_ 2) _. Using the notation_


_the Beta density can also be written as_


_The name “Beta density” is derived from the Beta function which is the name given to the function_ (63) _in mathematics._

One of the conclusions of the above example is that if _X_ 1 _∼ Gamma_ ( _α_ 1 _, λ_ ) and _X_ 2 _∼ Gamma_ ( _α_ 2 _, λ_ ) are independent, then


More generally, if _X_ 1 _, . . . , Xn_ are independent random variables with _Xi ∼ Gamma_ ( _αi, λ_ ), then


(65) can be proved from (64) by, for example, mathematical induction over _n_ . One consequence of (65) is that if _Z_ 1 _, . . . , Zn_ are independent random variables having the standard normal distribution, then


This is because, as we saw earlier in Lecture 10 (see Example 1.2 of Lecture 10), the square of a normal random variable has the _Gamma_ (1 _/_ 2 _,_ 1 _/_ 2) distribution. The distribution of the sum of squares of _n_ independent normal random variables is also known as the chi-squared distribution with _n_ degrees of freedom: _χ_<sup>2</sup> _n_<sup>.Wethushave</sup>


### **13.2 Conditional Densities for Continuous Random Variables**

Consider two random variables _X_ and _Y_ with joint density _fX,Y_ . How do we calculate the conditional probability:


for some subset _A ⊆_ R and _y_ 0 _∈_ R. The naive way to calculate the above probability is to write it as


The denominator on the right hand side above equals 0 because _Y_ is a continuous random variable. As a result, the numerator is also equal zero. Thus the right hand side equals<sup><u>0</u></sup> 0 and hence undefined.

67

The proper way to define (66) is to think of the conditioning event _Y_ = _y_ 0 as _y_ 0 _− ϵ/_ 2 _≤ Y ≤ y_ 0 + _ϵ/_ 2 for some small _ϵ_ . We then have


Motivated by the above calculation, we define the conditional density of _X_ given _Y_ = _y_ as


This is well-defined as long as _fY_ ( _y_ ) _>_ 0. The result we just derived can also be written as


Here are important facts about conditional densities.

#### **13.2.1 Conditional Density is Proportional to Joint Density**

As a function of _x_ (and keeping _y_ fixed), _fX|Y_ = _y_ ( _x_ ) is a valid density i.e.,


The integral above equals one because


Because _fX|Y_ = _y_ ( _x_ ) integrates to one as a function of _x_ and because the denominator _fY_ ( _y_ ) in the definition (67) does not depend on _x_ , it is common to write


The symbol _∝_ here stands for “proportional to” and the above statement means that _fX|Y_ = _y_ ( _x_ ), as a function of _x_ , is proportional to _fX,Y_ ( _x, y_ ). The proportionality constant then has to be _fY_ ( _y_ ) because that is equal to the value of the integral of _fX,Y_ ( _x, y_ ) as _x_ ranges over ( _−∞, ∞_ ).

The proportionality statement (68) often makes calculations involving conditional densities much simpler.

#### **13.2.2 Conditional Densities and Independence**

_X_ and _Y_ are independent if and only if _fX|Y_ = _y_ = _fX_ for every value of _y_ such that _fY_ ( _y_ ) _>_ 0. This latter statement is precisely equivalent to _fX,Y_ ( _x, y_ ) = _fX_ ( _x_ ) _fY_ ( _y_ ). By switching roles of _X_ and _Y_ , it also follows that _X_ and _Y_ are independent if and only if _fY |X_ = _x_ = _fY_ for every _x_ such that _fX_ ( _x_ ) _>_ 0.

68

#### **13.2.3 Law of Total Probability for Continuous Random Variables**

Note first that from the definition of _fX|Y_ = _y_ ( _x_ ), it directly follows that


This tells us how to compute the joint density of _X_ and _Y_ using knowledge of the marginal of _Y_ and the conditional density of _X_ given _Y_ .

From here (and the fact that integrating the joint density with respect to one of the variables gives the marginal density of the other random variable), it is easy to derive the formula


This formula, known as the **Law of Total Probability** , allows us to deduce the marginal density of _X_ using knowledge of the conditional density of _X_ given _Y_ and the marginal density of _Y_ .

Here are two applications of the Law of Total Probability.

**Example 13.2.** _Suppose X and Y are independent standard normal random variables. What is the density of U_ = _X/Y ?_

_Using the Law of Total Probability, we get_


_Now (below_ =<sup>_d_</sup> _stands for equality in distribution: A_ =<sup>_d_</sup> _B means that the random variables A and B have the same distribution)_


_where the last equality follows because X and Y are independent. We thus get_


_By the change of variable formula in the univariate case, we get_

_Thus_


_The last equality is derived by the change of variable w_ = _v_<sup>2</sup> _/_ 2 _to evaluate the integral. We have therefore proved that U has the Cauchy density._

69

The Cauchy density is a special case of the _t_ -density when the degrees of freedom is equal to one (i.e., the _t_ -density with one degree of freedom is the same as the Cauchy density). The _t_ -density for _n_ degrees of freedom can also be derived as a consequence of the law of total probability (this is done in the next example).

**Example 13.3.** _Suppose Z, X_ 1 _, . . . , Xn are independent random variables all having the standard normal distribution. The distribution of the random variable_


_is said to be the t-distribution with n degrees of freedom. Its density can be calculated using the Law of Total Probability as shown below. First let_


_As a result_


_The integrand in the integral above is equal to the main part of the Gamma_ ( _α, λ_ ) _density with_


_Thus the value of the integral is simply the normalization constant of the Gamma density:_


_We have thus proved:_


70

_This density, which is proportional to_ 1 +<sup>_<u>t</u>_</sup> _n_<sup>2</sup> _, is the t-density with n degrees of_ � � _−_ ( _n_ +1) _/_ 2 _freedom. When n_ = 1 _, this density if proportional to_ (1+ _t_<sup>2</sup> )<sup>_−_1</sup> _so the t-density with 1 degree of freedom is exactly equal to the Cauchy density. When n becomes large, the tails of the t-density become less heavy and it eventually becomes the standard normal density. Indeed, when n is large, we can write (for each fixed u)_


#### **13.2.4 Bayes Rule for Continuous Random Variables**

A direct consequence of the definition of the conditional density is:


This is the Bayes rule and it is useful for calculating the conditional density of _Y_ given _X_ = _x_ from knowledge of the conditional density of _X_ given _Y_ = _y_ (and the marginal density of _Y_ ). We shall see many applications of this rule in the next few lectures.

---

[← 12 Lecture Twelve](13-12-lecture-twelve.md) · [Up: contents](index.md) · [14 Lecture Fourteen →](15-14-lecture-fourteen.md)
