---
title: Conditioning
source: https://www.stat.berkeley.edu/~aditya/resources/FullLectureNotes201AFall2019.pdf
source_file: sources/berkeley-guntuboyina-notes/FullLectureNotes201AFall2019.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Conditioning

**Source:** [`FullLectureNotes201AFall2019.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullLectureNotes201AFall2019.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Our next main topic is conditioning which is very important for statistics classes.

#### **2.0.1 Basics**

Let us first start by looking at the definition of conditional probability. Given two events _A_ and _B_ with P( _A_ ) _>_ 0, we define the conditional probability of _B_ given _A_ as


See Section 1.1 of Lecture 10 of Jim Pitman’s 2016 notes for 201A to get some intuitive justification for this definition of conditional probability.

Using this definition of conditional probability, we can see that


Note here that _A_ and _A_<sup>_c_</sup> are disjoint events whose union is the entire space of outcomes Ω. More generally, if _A_ 1 _, A_ 2 _, . . ._ are disjoint events whose union is Ω, we have


This is referred to as the **Law of total probability** .

Let us now come to **Bayes rule** which states that


49

_CHAPTER 2. CONDITIONING_

50

#### **2.0.2 Conditional Distributions, Law of Total Probability and Bayes Rule for Discrete Random Variables**

Consider two random variables _X_ and Θ. Assume that both are discrete random variables. One can then define the conditional distribution of _X_ given Θ = _θ_ simply by defining the conditional probabilities:


assuming that P _{_ Θ = _θ} >_ 0. If P _{_ Θ = _θ}_ = 0, we would not attempt to define P _{X_ = _x|_ Θ = _θ}_ .

As _x_ varies over all values that the random variable _X_ takes, the probabilities (2.3) determine the conditional distribution of _X_ given Θ = _θ_ . Note that the conditional probability P _{X_ = _x|_ Θ = _θ}_ always lies between 0 and 1 and we have<sup>�</sup> _x_<sup>P</sup><sup>_{X_=</sup><sup>_x|_Θ =</sup><sup>_θ}_= 1.</sup>

**Example 2.0.1.** _Suppose X and Y are independent random variables having the Poi_ ( _λ_ 1) _and Poi_ ( _λ_ 2) _distributions respectively. For n ≥_ 0 _, what is the conditional distribution of X given X_ + _Y_ = _n?_

_We need to compute_


_for various values of i. It is clear that the above probability is non-zero only when i is an integer between_ 0 _and n. Let us therefore assume that i is an integer between_ 0 _and n. By definition_


_The numerator above can be evaluated directly as X and Y are independently distributed as Poi_ ( _λ_ 1) _and Poi_ ( _λ_ 2) _respectively. For the denominator, we use the fact that X_ + _Y is Poi_ ( _λ_ 1 + _λ_ 2) _(the proof of this fact is left as exercise). We thus have_


_which means that the conditional distribution of X given X_ + _Y_ = _n is the Binomial distribution with parameters n and p_ = _λ_ 1 _/_ ( _λ_ 1 + _λ_ 2) _._

51

Let us now look at the law of total probability and Bayes rule for discrete random variables _X_ and Θ. As a consequence of (2.2), we have


where the summation is over all values of _θ_ that are taken by the random variable Θ. This formula allows one to calculate P _{X_ = _x}_ using knowledge of P _{X_ = _x|_ Θ = _θ}_ and P _{_ Θ = _θ}_ . We shall refer to (2.4) as the **Law of Total Probability** for discrete random variables.

The Bayes rule is


The Bayes rule allows one to compute the conditional probabilities of Θ given _X_ using knowledge of the conditional probabilities of _X_ given Θ as well as the marginal probabilities of Θ. We shall refer to (2.5) as the **Bayes Rule** for discrete random variables.

**Example 2.0.2.** _Suppose N is a random variable having the Poi_ ( _λ_ ) _distribution. Also suppose that, conditional on N_ = _n, the random variable X has the Bin_ ( _n, p_ ) _distribution. This setting is known as the_ **_Poissonization of the Binomial_** _. Find the marginal distribution of X. Also what is the conditional distribution of N given X_ = _i?_

_To find the marginal distribution of X, we need to find_ P _{X_ = _i} for every integer i ≥_ 0 _. For this, we use the law of total probability which states that_


_Because X|N_ = _n is Bin_ ( _n, p_ ) _, the probability_ P _{X_ = _i|N_ = _n} is non-zero only when_ 0 _≤ i ≤ n. Therefore the terms in the sum above are non-zero only when n ≥ i and we obtain_


_This means that X has the Poi_ ( _λp_ ) _distribution._

_To find the conditional distribution of N given X_ = _i, we need to use Bayes rule which states that_


_CHAPTER 2. CONDITIONING_

52

_This is only nonzero when n ≥ i (otherwise_ P _{X_ = _i|N_ = _n} will be zero). And when n ≥ i, we have_


_This means that conditional on X_ = _i, the random variable N is distributed as i_ + _Poi_ ( _λ_ (1 _− p_ )) _._

_What is the joint distribution of X and N − X in this example? To compute this, note that_


_Note that this factorizes into a term involving only i and a term involving only j. This means therefore that X and N − X are independent. Also from the expression above, it is easy to deduce that the marginal distribution of X is Poi_ ( _λp_ ) _(which we have already derived via the law of total probability) and that N − X is Poi_ ( _λ_ (1 _− p_ )) _._

_The setting of this example arises when one tosses a coin with probability of heads p independently a Poi_ ( _λ_ ) _number of times. Then N denotes the total number of tosses, X denotes the number of heads and N − X denotes the number of tails. We have thus shown that X and N − X are independent and are distributed according to Poi_ ( _λp_ ) _and Poi_ ( _λ_ (1 _− p_ )) _respectively. Independence of X and N − X here is especially interesting. When a coin is tossed a fixed number n of times, the number of heads and tails are obviously not independent (as they have to sum to n). But when the number of tosses is itself random and has the Poisson distribution, then the number of heads and tails become independent random variables._

### **2.1 Conditional Densities for Continuous Random Variables**

Consider now two continuous random variables _X_ and Θ having a joint density _fX,_ Θ( _x, θ_ ). Recall then that _fX,_ Θ( _x, θ_ ) _≥_ 0 for all _x, θ_ and �� _f_ ( _x, θ_ ) _dxdθ_ = 1. Also recall that the marginal densities of _X_ and Θ are given by


We shall now define the conditional density of _X_ given Θ = _θ_ for a fixed value of _θ_ . In order to

_2.1. CONDITIONAL DENSITIES FOR CONTINUOUS RANDOM VARIABLES_

53

define this conditional density at a point _x_ , we need to consider


for a small _δ >_ 0. Because P _{_ Θ = _θ}_ = 0 (note that Θ is a continuous random variable), we cannot define this conditional probability using the definition P( _B|A_ ) := P( _B ∩ A_ ) _/_ P( _A_ ). But, intuitively, conditioning on Θ = _θ_ should be equivalent to conditioning on _θ ≤_ Θ _≤ θ_ + _ϵ_ for small _ϵ_ . Therefore we can write


for small _ϵ_ . For the probability on the right hand side above, we can use P( _B|A_ ) := P( _B ∩ A_ ) _/_ P( _A_ ) to obtain


We have thus obtained that


for small _δ_ . This suggests the definition


for the conditional density of _X_ given Θ = _θ_ . This definition makes sense as long as _f_ Θ( _θ_ ) _>_ 0. If _f_ Θ( _θ_ ) = 0, we do not attempt to define _fX|_ Θ= _θ_ .

**Example 2.1.1.** _Suppose X and_ Θ _are independent random variables having the Gamma_ ( _α, λ_ ) _and Gamma_ ( _β, λ_ ) _distributions respectively. What then is the conditional density of X given X_ + Θ = 1 _._

_The definition_ (2.9) _gives_


_By the Jacobian formula for calculating densities of transformed random variables, it can be checked that_


_for_ 0 _< x <_ 1 _. We have also seen previously that X_ + Θ _is distributed as_ Γ( _α_ + _β, λ_ ) _. Thus_


_Therefore_


_This means therefore that_

_X|_ ( _X_ + Θ = 1) _∼ Beta_ ( _α, β_ ) _._

_CHAPTER 2. CONDITIONING_

54

**Example 2.1.2.** _Suppose X and Y are independent Unif_ (0 _,_ 1) _random variables. What is fU |V_ = _v where U_ = min( _X, Y_ ) _and V_ = max( _X, Y_ ) _and_ 0 _< v <_ 1 _?_

_Note first that_


_When_ 0 _< u < v <_ 1 _, we know that_


_Also V_ = max( _X, Y_ ) _∼ Beta_ (2 _,_ 1) _so that_


_We thus have_


_In other words, U |V_ = _v is uniformly distributed on the interval_ (0 _, v_ ) _._

### **2.2 Conditional Densities for Continuous Random Variables**

Consider now two continuous random variables _X_ and Θ having a joint density _fX,_ Θ( _x, θ_ ). Recall then that _fX,_ Θ( _x, θ_ ) _≥_ 0 for all _x, θ_ and �� _f_ ( _x, θ_ ) _dxdθ_ = 1. Also recall that the marginal densities of _X_ and Θ are given by


We shall now define the conditional density of _X_ given Θ = _θ_ for a fixed value of _θ_ . In order to define this conditional density at a point _x_ , we need to consider


for a small _δ >_ 0. Because P _{_ Θ = _θ}_ = 0 (note that Θ is a continuous random variable), we cannot define this conditional probability using the definition P( _B|A_ ) := P( _B ∩ A_ ) _/_ P( _A_ ). But, intuitively, conditioning on Θ = _θ_ should be equivalent to conditioning on _θ ≤_ Θ _≤ θ_ + _ϵ_ for small _ϵ_ . Therefore we can write

P _{x ≤ X ≤ x_ + _δ|_ Θ = _θ} ≈_ P _{x ≤ X ≤ x_ + _δ|θ ≤_ Θ _≤ θ_ + _ϵ}_

for small _ϵ_ . For the probability on the right hand side above, we can use P( _B|A_ ) := P( _B ∩ A_ ) _/_ P( _A_ ) to obtain


We have thus obtained that

_2.2. CONDITIONAL DENSITIES FOR CONTINUOUS RANDOM VARIABLES_

55

for small _δ_ . This suggests the definition


for the conditional density of _X_ given Θ = _θ_ . This definition makes sense as long as _f_ Θ( _θ_ ) _>_ 0. If _f_ Θ( _θ_ ) = 0, we do not attempt to define _fX|_ Θ= _θ_ .

**Example 2.2.1.** _Suppose X and_ Θ _are independent random variables having the Gamma_ ( _α, λ_ ) _and Gamma_ ( _β, λ_ ) _distributions respectively. What then is the conditional density of X given X_ + Θ = 1 _._

_The definition_ (2.9) _gives_


_By the Jacobian formula for calculating densities of transformed random variables, it can be checked that_


_for_ 0 _< x <_ 1 _. We have also seen previously that X_ + Θ _is distributed as_ Γ( _α_ + _β, λ_ ) _. Thus_


_Therefore_


_This means therefore that_


**Example 2.2.2.** _Suppose X and Y are independent Unif_ (0 _,_ 1) _random variables. What is fU |V_ = _v where U_ = min( _X, Y_ ) _and V_ = max( _X, Y_ ) _and_ 0 _< v <_ 1 _?_

_Note first that_


_When_ 0 _< u < v <_ 1 _, we know that_


_Also V_ = max( _X, Y_ ) _∼ Beta_ (2 _,_ 1) _so that_


_We thus have_


_In other words, U |V_ = _v is uniformly distributed on the interval_ (0 _, v_ ) _._

_CHAPTER 2. CONDITIONING_

56

**Example 2.2.3.** _Suppose X and_ Θ _are independent random variables having densities fX and f_ Θ _respectively. (a) What is the conditional density of X_ + Θ _given_ Θ = _θ? (b) What is the conditional density of_<sup>_<u>X</u>_</sup> Θ<sup>_given_Θ =</sup><sup>_θ?_</sup>

_For fX_ +Θ _|_ Θ= _θ, write_


_For f X_ Θ<sup>_|_Θ=</sup><sup>_θ_(</sup><sup>_u_)</sup><sup>_,write_</sup>


### **2.3 Conditional Density is Proportional to Joint Density**

The conditional density


has the following important property. As a function of _x_ (and keeping _θ_ fixed), _fX|_ Θ= _θ_ ( _x_ ) is a valid density i.e.,


The integral above equals one because


Because _fX|_ Θ= _θ_ ( _x_ ) integrates to one as a function of _x_ and because the denominator _f_ Θ( _θ_ ) in the definition (2.11) does not depend on _x_ , it is common to write


The symbol _∝_ here stands for “proportional to” and the above statement means that _fX|_ Θ= _θ_ ( _x_ ), as a function of _x_ , is proportional to _fX,_ Θ( _x, θ_ ). The proportionality constant then has to be _f_ Θ( _θ_ ) because that is equal to the value of the integral of _fX,_ Θ( _x, θ_ ) as _x_ ranges over ( _−∞, ∞_ ).

The proportionality statement (2.12) often makes calculations involving conditional densities much simpler. To illustrate this, let us revisit the calculations in Examples (2.2.1) and (2.2.2) respectively.

**Example 2.3.1** (Example 2.2.1 revisited) **.** _Suppose X and_ Θ _are independent random variables having the Gamma_ ( _α, λ_ ) _and Gamma_ ( _β, λ_ ) _distributions respectively. What then is the conditional density_

_2.4. CONDITIONAL DENSITIES AND INDEPENDENCE_

57

_of X given X_ + Θ = 1 _? By_ (2.12) _,_


_which immediately implies that X|X_ + Θ = 1 _has the Beta distribution with parameters α and β._

**Example 2.3.2** (Example 2.2.2 revisited) **.** _Suppose X and Y are independent Unif_ (0 _,_ 1) _random variables. What is fU |V_ = _v where U_ = min( _X, Y_ ) _and V_ = max( _X, Y_ ) _and_ 0 _< v <_ 1 _?_

_Write_


_Thus for v <_ 1 _, the conditional density of U given V_ = _v is the uniform density on_ [0 _, v_ ] _. For v >_ 1 _, the conditional density of U given V_ = 1 _is not defined as the density of V at v >_ 1 _equals 0._

### **2.4 Conditional Densities and Independence**

_X_ and Θ are independent if and only if _fX|_ Θ= _θ_ = _fX_ for every value of _θ_ . This latter statement is precisely equivalent to _fX,_ Θ( _x, θ_ ) = _fX_ ( _x_ ) _f_ Θ( _θ_ ). By switching roles of _X_ and Θ, it also follows that _X_ and Θ are independent if and only if _f_ Θ _|X_ = _x_ = _f_ Θ for every _x_ .

It is also not hard to see that _X_ and Θ are independent if and only if the conditional density of _X_ given Θ = _θ_ is the same for all values of _θ_ for which _f_ Θ( _θ_ ) _>_ 0.

**Example 2.4.1** (Back to the Gamma example) **.** _We have previously seen that when X ∼ Gamma_ ( _α, λ_ ) _and Y ∼ Gamma_ ( _β, λ_ ) _, then_


_This can be also be directly seen (using the observation that X/_ ( _X_ + Θ) _is distributed as Beta_ ( _α, β_ ) _and that X/_ ( _X_ + Θ) _is independent of X_ + Θ _) as follows:_


_where_ = _d means “equality in distribution”. Note that we removed the conditioning on X_ + Θ = 1 _in the last step above because X/_ ( _X_ + Θ) _is independent of X_ + Θ _._

_CHAPTER 2. CONDITIONING_

58

**Example 2.4.2** (Example 2.2.3 revisited) **.** _In Example 2.2.3, we considered two independent random variables X and_ Θ _having the densities fX and f_ Θ _. We then showed that_


_This can also be seen in the following way:_


_Because the density of X_ + _θ is fX_ + _θ_ ( _u_ ) = _fX_ ( _u − θ_ ) _, this proves_ (2.13) _. A similar argument can also be given for the fact f X_ Θ<sup>_|_Θ=</sup><sup>_θ_(</sup><sup>_u_) =</sup><sup>_|θ|fX_(</sup><sup>_uθ_)</sup><sup>_(leftasanexercise)._</sup>

### **2.5 Law of Total Probability for Continuous Random Variables**

Note first that from the definition of _fX|_ Θ= _θ_ ( _x_ ), it directly follows that


This tells us how to compute the joint density of _X_ and Θ using knowledge of the marginal of Θ and the conditional density of _X_ given Θ.

From here (and the fact that integrating the joint density with respect to one of the variables gives the marginal density of the other random variable), it is easy to derive the formula


This formula, known as the **Law of Total Probability** allows us to deduce the marginal density of _X_ using knowledge of the conditional density of _X_ given Θ and the marginal density of Θ.

The formula (2.17) has interesting consequences. For example, it can be used to rederive the convolution formula that we have seen previously for the density of the sum of two independent random variables. Indeed, the convolution formula states that if _X ∼ fX_ and Θ _∼ f_ Θ are independent random variables, then


This can be derived as a consequence of (2.17) (and (2.13)) via

We also saw previously that


This can also be easily derived from (2.17) (and (2.10)) and this is left as exercise.

Here are two other applications of the Law of Total Probability.

_2.5. LAW OF TOTAL PROBABILITY FOR CONTINUOUS RANDOM VARIABLES_

59

**Example 2.5.1.** _Suppose_ Θ _∼ Exp_ (1 _/_ 2) _(i.e., f_ Θ( _θ_ ) = 0 _._ 5 _e_<sup>_−θ/_2</sup> _I{θ >_ 0 _}) and X|_ Θ = _θ ∼ N_ (0 _, θ_ ) _. Then the marginal density of X is the Double Exponential density (also known as the Laplace density):_


_To show this, first use the Law of Total Probability which gives_


_Plugging in the formulae for fX|_ Θ= _θ and f_ Θ _, we get_


_The following trick can be used to evaluate this integral. First do the change of variable θ_ = _u_<sup>2</sup> _to get_


_Note first that when x_ = 0 _, we have fX_ (0) = (2 _π_ )<sup>_−_1</sup><sup>_/_2 �</sup> 0<sup>_∞_</sup> _e_<sup>_−u_2</sup><sup>_/_2</sup> _du_ = 1 _/_ 2 _. So let us assume that x̸_ = 0 _. The trick to evaluate fX_ ( _x_ ) _involves differentiating the formula_ (2.16) _with respect to x. This gives_


_Let us now do the change of variable v_ =<sup>_<u>|</u>_</sup> _u_<sup>_x|.Itiseasytoseethatthisgives_</sup>

_We thus have_


_or equivalently,_


_From here (and the fact fX_ (0) = 1 _/_ 2 _), it is straightforward to derive_ (2.15) _._

**Example 2.5.2.** _Suppose_ Θ _∼ N_ ( _µ, τ_<sup>2</sup> ) _and X|_ Θ = _θ ∼ N_ ( _θ, σ_<sup>2</sup> ) _. It then follows that X ∼ N_ ( _µ, τ_<sup>2</sup> + _σ_<sup>2</sup> ) _. We shall derive this in the next class._

In the last class, we discussed the law of total probability for continuous random variables:


This formula allows us to deduce the marginal density of _X_ using knowledge of the conditional density of _X_ given Θ and the marginal density of Θ.

We started discussing the following example last class.

_CHAPTER 2. CONDITIONING_

60

**Example 2.5.3.** _Suppose_ Θ _∼ N_ ( _µ, τ_<sup>2</sup> ) _and X|_ Θ = _θ ∼ N_ ( _θ, σ_<sup>2</sup> ) _. It then follows that X ∼ N_ ( _µ, τ_<sup>2</sup> + _σ_<sup>2</sup> ) _. We shall derive this now. We use the LTP which says_


_Now_


_The term in the exponent above can be simplified as_

_where I skipped a few steps to get to the last equality (complete the square and simplify the resulting expressions)._

_As a result_


_Consequently,_

_which gives_


### **2.6 Bayes Rule for Continuous Random Variables**

Next we shall discuss the Bayes rule which tells us how to derive the conditional density of Θ given _X_ = _x_ using information on the conditional density of _X_ given Θ = _θ_ and the marginal density of Θ. The Bayes rule says:


_2.6. BAYES RULE FOR CONTINUOUS RANDOM VARIABLES_

61

The denominator in the above formula does not depend on _θ_ (as _θ_ is integrated out) and thus


Here are two applications of the Bayes rule for continous variables.

**Example 2.6.1.** _Suppose_ Θ _∼ N_ ( _µ, τ_<sup>2</sup> ) _and X|_ Θ = _θ ∼ N_ ( _θ, σ_<sup>2</sup> ) _. What is the conditional density of_ Θ _|X_ = _x?_

_To obtain f_ Θ _|X_ = _x_ ( _θ_ ) _, we use the Bayes rule:_


_which means that_

_For a normal density with mean m and variance v_<sup>2</sup> _, the inverse of the variance_ 1 _/v_<sup>2</sup> _is called the precision. The above calculation therefore reveals that the precision of the conditional distribution of_ Θ _given X equals the sum of the precisions of the distribution of_ Θ _and the distribution of X respectively._

_In statistical terminology, it is common to call:_

_1. the marginal distribution of_ Θ _as the prior distribution of the unknown parameter θ._

_2. the conditional distribution of X|_ Θ = _θ as the distribution of the data conditioned on the value of the true parameter._

_3. the conditional distribution of_ Θ _|X_ = _x as the posterior distribution of_ Θ _given the data._

_In this particular example, the mean of the posterior distribution is a weighted linear combination of the prior mean as well as the data where the weights are proportional to the precisions. Also, posterior precision equals the sum of the prior precision and the data precision which informally means, in particular, that the posterior is more precise than the prior._

**Example 2.6.2.** _Suppose_ Θ _∼ Gamma_ ( _α, λ_ ) _and X|_ Θ = _θ ∼ Exp_ ( _θ_ ) _. What is the conditional density of_ Θ _given X_ = _x? We can argue via proportionality that_


_which means that_


_Note that_


_CHAPTER 2. CONDITIONING_

62

### **2.7 LTP and Bayes Rule for general random variables**

The LTP describes how to compute the distribution of _X_ based on knowledge of the conditional distribution of _X_ given Θ = _θ_ as well as the conditional distribution of Θ. The Bayes rule describes how to compute the conditional distribution of Θ given _X_ = _x_ based on the same knowledge of the conditional distribution of _X_ given Θ = _θ_ as well as the conditional distribution of Θ. We have so far looked at the LTP and Bayes rule when _X_ and Θ are both discrete or when they are both continuous. Now we shall also consider the cases when one of them is discrete and the other is continuous.

#### **2.7.1** _X_ **and** Θ **are both discrete**

In this case, we have seen that the LTP is


and the Bayes rule is


#### **2.7.2** _X_ **and** Θ **are both continuous**

Here LTP is


and Bayes rule is


#### **2.7.3** _X_ **is discrete while** Θ **is continuous**

LTP is


and Bayes rule is


**2.7.4** _X_ **is continuous while** Θ **is discrete**

LTP is


_2.7. LTP AND BAYES RULE FOR GENERAL RANDOM VARIABLES_

63

and Bayes rule is


These formulae are useful when the conditional distribution of _X_ given Θ = _θ_ as well as the marginal distribution of Θ are easy to determine (or are given as part of the model specification) and the goal is to determine the marginal distribution of _X_ as well as the conditional distribution of Θ given _X_ = _x_ .

We shall now look at two applications of the LTP and Bayes Rule to when one of _X_ and Θ is discrete and the other is continuous.

**Example 2.7.1.** _Suppose that_ Θ _is the uniformly distributed on_ (0 _,_ 1) _and let X|_ Θ = _θ has the binomial distribution with parameters n and θ (i.e., conditioned on_ Θ = _θ, the random variable X is distributed as the number of successes in n independent tosses of a coin with probability of success θ). What then is the marginal distribution of X as well as the conditional distribution of_ Θ _given X_ = _x?_

_Note that this is a situation where X is discrete (taking values in_ 0 _,_ 1 _, . . . , n) and_ Θ _is continuous (taking values in the interval_ (0 _,_ 1) _). To compute the marginal distribution of X, we use the appropriate LTP to write (for x_ = 0 _,_ 1 _, . . . , n)_


_which means that X is (discrete) uniformly distributed on the finite set {_ 0 _,_ 1 _, . . . , n}._

_Let us now calculate the posterior distribution of_ Θ _given X_ = _x. Using the Bayes rule, we obtain_


_for_ 0 _< θ <_ 1 _. From here, it immediately follows that_


_The mean of the Beta_ ( _α, β_ ) _distribution is α/_ ( _α_ + _β_ ) _. Therefore the mean of the conditional distribution of_ Θ _given X_ = _x (also known as the posterior mean) equals_


_CHAPTER 2. CONDITIONING_

64

_As the prior mean equals_ 1 _/_ 2 _and we can write_


_it follows that the posterior mean falls between the prior mean and x/n. As n becomes large, the posterior mean approaches x/n._

We shall start with an example of the LTP and Bayes Rule when Θ is a discrete random variable and _X_ is continuous. Recall that in this case, the formulae are

and


**Example 2.7.2** (Statistical Classification) **.** _In a statistical classification problem, the random variable_ Θ _is discrete and X is usually continuous. The simplest situation is when_ Θ _is binary. Let us say that_


_Also assume that the conditional density of X given_ Θ = 0 _is f_ 0 _and that the conditional density of X given_ Θ = 1 _is f_ 1 _i.e.,_


_Using the LTP, we see that the marginal density of X equals_


_In other words, fX is a_ **_mixture_** _of f_ 0 _and f_ 1 _with the mixing weights being equal to the marginal probabilities of_ Θ _._

_According to the Bayes rule, the conditional distribution of_ Θ _given X_ = _x is given by_


_and_


_These are also referred to as the posterior probabilities of_ Θ _given X_ = _x._

### **2.8 Conditional Joint Distributions**

Given random variables _X_ 1 _, . . . , Xm, Y_ 1 _, . . . , Yk_ , how do we describe the joint distribution of _Y_ 1 _, . . . , Yk_ given _X_ 1 = _x_ 1 _, . . . , Xm_ = _xm_ . If all these random variables are discrete, then one can simply specify all the values ( _y_ 1 _, . . . , yk_ ) that _Y_ 1 _, . . . , Yk_ take together with the probabilities:


_2.8. CONDITIONAL JOINT DISTRIBUTIONS_

65

Here is an example of this.

**Example 2.8.1.** _Suppose N_ 1 _, . . . , Nk have the multinomial distribution with parameters n and p_ 1 _, . . . , pk (where p_ 1 _, . . . , pk are nonnegative numbers summing to one). What is the conditional joint distribution of N_ 2 _, . . . , Nk given N_ 1 = _n_ 1 _? Given N_ 1 = _n_ 1 _, N_ 1 _, . . . , Nk will take values n_ 2 _, . . . , nk which are nonnegative integers such that n_ 2 + _· · ·_ + _nk_ = _n − n_ 1 _. The probabilities are given by_


_This means that_


When the random variables are continuous, the conditional joint distribution will be given by a density. Given continuous random variables _X_ 1 _, . . . , Xm, Y_ 1 _, . . . , Yk_ , the conditional joint density of _Y_ 1 _, . . . , Yk_ given _X_ 1 = _x_ 1 _, X_ 2 = _x_ 2 _, . . . , Xm_ = _xm_ is defined as


provided _x_ 1 _, . . . , xm_ are such that _fX_ 1 _,...,Xm_ ( _x_ 1 _, . . . , xm_ ) _>_ 0.

**Example 2.8.2.** _Suppose U_ 1 _, . . . , Un are independent observations having the uniform density on_ (0 _,_ 1) _. What is the conditional joint density of U_ (1) _, . . . , U_ ( _n−_ 1) _given U_ ( _n_ ) = _u?_

_By definition,_


_By the joint distribution of order statistics that we worked out previously, it follows first that the above quantity is non-zero only when_ 0 _< u_ 1 _< · · · < un−_ 1 _< u <_ 1 _and it is then equal to_


_For the denominator above, we used the fact that U_ ( _n_ ) _∼ Beta_ ( _n,_ 1) _. We have thus proved that_


_Note that the right hand side above is the joint density of the order statistics of_ ( _n−_ 1) _i.i.d observations drawn from the uniform distribution on the interval_ (0 _, u_ ) _. We have therefore proved that, conditioned on U_ ( _n_ ) = _u, the joint density of U_ (1) _, . . . , U_ ( _n−_ 1) _is the same as the joint density of the order statistics of_ ( _n −_ 1) _i.i.d observations drawn from the uniform distribution on_ (0 _, u_ ) _._

Here are some simple but important properties of conditional joint densities.

_CHAPTER 2. CONDITIONING_

66

1. For every _x_ 1 _, . . . , xm, y_ 1 _, . . . , yk_ , we have


2. The joint density of every set of random variables _Y_ 1 _, . . . , Yn_ satisfies the following:


3. This is a generalization of the previous fact. The conditional joint density


of _Y_ 1 _, . . . , Yn_ given _X_ 1 = _x_ 1 _, . . . , Xm_ = _xm_ equals the product


4. This can be viewed as a **law of total conditional probability** : For random variables _Y_ 1 _, . . . , Yk, X_ 1 _, . . . , Xm_ and Θ, we have


Here is an application of the above facts.

**Example 2.8.3** (Joint density of an autoregressive process) **.** _Suppose X_ 1 _, Z_ 2 _, . . . , Zn are independent random variables with Z_ 2 _, . . . , Zn being distributed as N_ (0 _, σ_<sup>2</sup> ) _. Define new random variables X_ 2 _, . . . , Xn via_


_where φ is some real number. The process X_ 1 _, . . . , Xn is called an autoregressive process of order 1. What is the conditional joint density of X_ 2 _, . . . , Xn given X_ 1 = _x_ 1 _? What is the joint density of X_ 1 _, . . . , Xn?_

_Let us first calculate the conditional joint density of X_ 2 _, . . . , Xn given X_ 1 = _x_ 1 _. For this, write_


_Now for each i_ = 2 _, . . . , n, observe that_


_We were able to remove conditioning on X_ 1 = _x_ 1 _, . . . , Xi−_ 1 = _xi−_ 1 _above because X_ 1 _, . . . , Xi−_ 1 _only depend on X_ 1 _, Z_ 2 _, . . . , Zi−_ 1 _and hence are independent of Zi._

_2.9. CONDITIONAL JOINT DENSITIES_

67

_From the above chain of assertions, we deduce that_


_Combining with_ (2.18) _, we obtain_


_To obtain the joint density of X_ 1 _, . . . , Xn, write_

_In a statistical setting, this joint density is used to estimate the parameters φ and σ_<sup>2</sup> _via maximum likelihood estimation. For this model however, it is easier to work with the conditional density of X_ 2 _, . . . , Xn given X_ 1 = _x_ 1 _instead of the full joint density of X_ 1 _, . . . , Xn._

### **2.9 Conditional Joint Densities**

In the last class, we discussed conditional joint densities which are defined in the following way. Given continuous random variables _X_ 1 _, . . . , Xm, Y_ 1 _, . . . , Yk_ , the conditional joint density of _Y_ 1 _, . . . , Yk_ given _X_ 1 = _x_ 1 _, X_ 2 = _x_ 2 _, . . . , Xm_ = _xm_ is defined as


provided _x_ 1 _, . . . , xm_ are such that _fX_ 1 _,...,Xm_ ( _x_ 1 _, . . . , xm_ ) _>_ 0.

We also looked at the following properties of conditional joint densities.


2. The joint density of every set of random variables _Y_ 1 _, . . . , Yn_ satisfies the following:


3. This is a generalization of the previous fact. The conditional joint density


_CHAPTER 2. CONDITIONING_

68

of _Y_ 1 _, . . . , Yn_ given _X_ 1 = _x_ 1 _, . . . , Xm_ = _xm_ equals the product


4. This can be viewed as a **law of total conditional probability** : For random variables _Y_ 1 _, . . . , Yk, X_ 1 _, . . . , Xm_ and Θ, we have


#### **2.9.1 Application to the Normal prior-Normal data model**

Let us now look at the application of the conditional density formulae for the normal prior-normal data model. Here we first have a random variable Θ that has the _N_ ( _µ, τ_<sup>2</sup> ) distribution. We also have random variables _X_ 1 _, . . . , Xn_ +1 such that


In other words, conditional on Θ = _θ_ , the random variables _X_ 1 _, . . . , Xn_ +1 are i.i.d _N_ ( _θ, σ_<sup>2</sup> ).

Let us first find the conditional distribution of Θ given _X_ 1 = _x_ 1 _, . . . , Xn_ = _xn_ . The answer to this turns out to be


where _x_ ¯ _n_ := ( _x_ 1 + _· · ·_ + _xn_ ) _/n_ . Let us see why this is true below. Note first that we had solved this problem for _n_ = 1 in the last class where we proved the following:


The result (2.19) for general _n ≥_ 1 can actually be deduced from the above result for _n_ = 1. There are two ways of seeing this.

**Method One** : We use mathematical induction on _n ≥_ 1. We already know that (2.19) is true for _n_ = 1. Assume that it is true for _n_ and we shall try to prove it for _n_ + 1. The key to this is to note that


where


In words, (2.20) states that the posterior of Θ after observing ( _n_ +1) observations _X_ 1 = _x_ 1 _, . . . , Xn_ +1 = _xn_ +1 is the same as the posterior after observing one observation _Y_ = _xn_ +1 under the prior Θ _|X_ 1 = _x_ 1 _, . . . , Xn_ = _xn_ .

_2.9. CONDITIONAL JOINT DENSITIES_

69

To formally see why (2.20) is true, just note that


The first equality is a consequence of the properties of conditional densities. The second equality above is a consequence of the fact that _Xn_ +1 is independent of _X_ 1 _, . . . , Xn_ **conditional on** Θ.

The statement (2.20) allows us to use the result for _n_ = 1 and the induction hypothesis that (2.19) holds for _n_ . Indeed, using the _n_ = 1 result for


and _x_ = _xn_ +1, we deduce that Θ _|X_ 1 = _x_ 1 _, . . . , Xn_ +1 = _xn_ +1 is a normal distribution with mean

and variance


This proves (2.19) for _n_ + 1. The proof of (2.19) is complete by induction.

**Method Two** . The second method for proving (2.19) proceeds more directly by writing:


This now resembles the calculation we did previously for _n_ = 1. The only difference being that _x_ is now replaced by _x_ ¯ _n_ and _σ_<sup>2</sup> is replaced by _σ_<sup>2</sup> _/n_ . Therefore the _n_ = 1 result applied to _x → x_ ¯ _n_ and _σ_<sup>2</sup> _→ σ_<sup>2</sup> _/n_ should yield (2.19). This proves (2.19).

Let us now compute the conditional density of _Xn_ +1 given _X_ 1 = _x_ 1 _, . . . , Xn_ = _xn_ . For this, we can use the law of total conditional probability to write


_CHAPTER 2. CONDITIONING_

70

This again resembles the calculation of the marginal density of _X_ in the _n_ = 1 problem (where the answer is _X ∼ N_ ( _µ, τ_<sup>2</sup> + _σ_<sup>2</sup> )). The only difference is that the prior _N_ ( _µ, τ_<sup>2</sup> ) is now replaced by the posterior density which is given by (2.19). We therefore obtain that


### **2.10 Conditional Expectation**

Given two random variables _X_ and _Y_ , the conditional expectation (or conditional mean) of _Y_ given _X_ = _X_ is denoted by


and is defined as the expectation of the conditional distribution of _Y_ given _X_ = _x_ .

We can write


More generally


and also


The most important fact about conditional expectation is the **Law of Iterated Expectation** (also known as the **Law of Total Expectation** ). We shall see this next.

#### **2.10.1 Law of Iterated/Total Expectation**

The law of total expectation states that


Basically the law of total expectation tells us how to compute the expectation of E( _Y_ ) using knowledge of the conditional expectation of _Y_ given _X_ = _x_ . Note the similarity to law of total probability which specifies how to compute the marginal distribution of _Y_ using knowledge of the conditional distribution of _Y_ given _X_ = _x_ .

_2.10. CONDITIONAL EXPECTATION_

71

The law of total expectation can be proved as a consequence of the law of total probability. The proof when _Y_ and _X_ are continuous is given below. The proof in other cases (when one or both of _Y_ and _X_ are discrete) is similar and left as an exercise.

**Proof of the law of total expectation:** Assume that _Y_ and _X_ are both continuous. Then


By the law of total probability, we have


which proves the law of total expectation.

There is an alternate more succinct form of stating the law of total expectation which justifies calling the law of **iterated** expectation. We shall see this next. Note that E( _Y |X_ = _x_ ) depends on _x_ . In other words, E( _Y |X_ = _x_ ) is a function of _x_ . Let us denote this function by _h_ ( _·_ ):


If we now apply this function to the random variable _X_ , we obtain a new random variable _h_ ( _X_ ). This random variable is denoted by simply E( _Y |X_ ) i.e.,


Note that when _X_ is discrete, the expectation of this random variable E( _Y |X_ ) becomes


And when _X_ is continuous, the expectation of E( _Y |X_ ) is


Observe that the right hand sides in these expectations are precisely the terms on the right hand side of the law of total expectation. Therefore the law of total expectation can be rephrased as


Because there are two expectations on the right hand side, the law of total expectation is also known as the Law of Iterated Expectation. The law of iterated expection has many applications which we shall explore in the next class.

_CHAPTER 2. CONDITIONING_

72

### **2.11 Law of Iterated/Total Expectation**

In the last class, we defined conditional expectation and looked at the law of total expectation:


Basically the law of total expectation tells us how to compute the expectation of E( _Y_ ) using knowledge of the conditional expectation of _Y_ given _X_ = _x_ . Note the similarity to law of total probability which specifies how to compute the marginal distribution of _Y_ using knowledge of the conditional distribution of _Y_ given _X_ = _x_ .

We also saw that there is an alternate more succinct form of stating the law of total expectation which justifies calling it the law of **iterated** expectation. We shall see this next. Note that E( _Y |X_ = _x_ ) depends on _x_ . In other words, E( _Y |X_ = _x_ ) is a function of _x_ . Let us denote this function by _h_ ( _·_ ):


If we now apply this function to the random variable _X_ , we obtain a new random variable _h_ ( _X_ ). This random variable is denoted by simply E( _Y |X_ ) i.e.,


Note that when _X_ is discrete, the expectation of this random variable E( _Y |X_ ) becomes


And when _X_ is continuous, the expectation of E( _Y |X_ ) is


Observe that the right hand sides in these expectations are precisely the terms on the right hand side of the law of total expectation. Therefore the law of total expectation can be rephrased as


Because there are two expectations on the right hand side, the law of total expectation is also known as the Law of Iterated Expectation.

The law of iterated expection has many applications. A couple of simple examples are given below following which we shall explore applications to _risk minimization_ .

**Example 2.11.1.** _Consider a stick of length ℓ. Break it at a random point X that is chosen uniformly across the length of the stick. Then break the stick again at a random point Y that is also chosen uniformly across the length of the stick. What is the expected length of the final piece?_

_2.11. LAW OF ITERATED/TOTAL EXPECTATION_

73

_According to the description of the problem,_


_and we are required to calculate_ E( _Y_ ) _. Note first that_ E( _Y |X_ = _x_ ) = _x/_ 2 _for every x which means that_ E( _Y |X_ ) = _X/_ 2 _. Hence by the Law of Iterated Expectation,_


**Example 2.11.2.** _Suppose X, Y, Z are i.i.d Unif_ (0 _,_ 1) _random variables. Find the value of_ P _{X ≤ Y Z}?_

_By the Law of Iterated Expectation,_

P _{X ≤ Y Z}_ = E ( _I{X ≤ Y Z}_ ) = E [E ( _I{X ≤ Y Z}|Y Z_ )] = E( _Y Z_ ) = E( _Y_ )E( _Z_ ) = 1 _/_ 4 _._

**Example 2.11.3** (Sum of a random number of i.i.d random variables) **.** _Suppose X_ 1 _, X_ 2 _, . . . are i.i.d random variables with_ E( _Xi_ ) = _µ. Suppose also that N is a discrete random variable that takes values in {_ 1 _,_ 2 _, . . . , } and that is independent of X_ 1 _, X_ 2 _, . . . . Define_


_In other words, S is the sum of a random number (N ) of the random variables Xi. The law of iterated expectation can be used to compute the expectation of S as follows:_


_This fact is actually a special case of a general result called_ **_Wald’s identity_** _._

#### **2.11.1 Application of the Law of Total Expectation to Statistical Risk Minimization**

The law of the iterated expectation has important applications to statistical risk minimization problems. The simplest of these problems is the following.

**Problem 1:** Given two random variables _X_ and _Y_ , what is the function _g_<sup>_∗_</sup> ( _X_ ) of _X_ that minimizes


over all functions _g_ ? The resulting random variable _g_<sup>_∗_</sup> ( _X_ ) can be called the Best Predictor of _Y_ as a function of _X_ in terms of expected squared error.

To find _g_<sup>_∗_</sup> , we use the law of iterated expectation to write


_CHAPTER 2. CONDITIONING_

74

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

_2.11. LAW OF ITERATED/TOTAL EXPECTATION_

75

We have thus shown that the function _g_<sup>_∗_</sup> ( _x_ ) which minimizes _R_ ( _g_ ) over all functions _g_ is given by any conditional mean of _Y_ given _X_ = _x_ . Thus the conditional mean of _Y_ given _X_ = _x_ is the function of _X_ that is closest to _Y_ in terms of expected absolute error.

**Problem 3:** Suppose _Y_ is a binary random variable taking the values 0 and 1 and let _X_ be an arbitrary random variable. What is the function _g_<sup>_∗_</sup> ( _X_ ) of _X_ that minimizes


over all functions _g_ ? To solve this, again use the law of iterated expectation to write


In the inner expectation above, we can treat _X_ as a constant so that the problem is similar to minimizing P _{Z̸_ = _c}_ over _c ∈_ R for a binary random variable _Z_ . It is easy to see that P _{Z̸_ = _c}_ is minimized at _c_<sup>_∗_</sup> where


In case P _{Z_ = 1 _}_ = P _{Z_ = 0 _}_ , we can take _c_<sup>_∗_</sup> to be either 0 or 1. From here it can be deduced (via the law of iterated expectation) that the function _g_<sup>_∗_</sup> ( _X_ ) which minimizes P _{Y̸_ = _g_ ( _X_ ) _}_ is given by


**Problem 4:** Suppose again that _Y_ is binary taking the values 0 and 1 and let _X_ be an arbitrary random variable. What is the function _g_<sup>_∗_</sup> ( _X_ ) of _X_ that minimizes


Using an argument similar to the previous problems, deduce that the following function minimizes _R_ ( _g_ ):


The argument (via the law of iterated expectation) used in the above four problems can be summarized as follows. The function _g_<sup>_∗_</sup> which minimizes


over all functions _g_ is given by


_CHAPTER 2. CONDITIONING_

76

### **2.12 Conditional Variance**

Given two random variables _Y_ and _X_ , the conditional variance of _Y_ given _X_ = _x_ is defined as the variance of the conditional distribution of _Y_ given _X_ = _x_ . More formally,


Like conditional expectation, the conditional variance _V ar_ ( _Y |X_ = _x_ ) is also a function of _x_ . We can apply this function to the random variable _X_ to obtain a new random variable which we denote by _V ar_ ( _Y |X_ ). Note that


Analogous to the Law of Total Expectation, there is a Law of Total Variance as well. This formula says that


To prove this formula, expand the right hand side as


**Example 2.12.1.** _We have seen before that_


_This, of course, means that_


_Using the laws of total expectation and total variance, it is possible to prove these directly as follows._


_and_


**Example 2.12.2** (Sum of a random number of i.i.d random variables) **.** _Suppose X_ 1 _, X_ 2 _, . . . are i.i.d random variables with_ E( _Xi_ ) = _µ and V ar_ ( _Xi_ ) = _σ_<sup>2</sup> _< ∞. Suppose also that N is a discrete random variable that takes values in {_ 1 _,_ 2 _, . . . , } and that is independent of X_ 1 _, X_ 2 _, . . . . Define_


_We have seen previously that_


_Using the law of total variance, we can calculate V ar_ ( _X_ ) _as follows._

_V ar_ ( _S_ ) = E( _V ar_ ( _S|N_ )) + _V ar_ (E( _S|N_ )) = E( _Nσ_<sup>2</sup> ) + _V ar_ ( _Nµ_ ) = _σ_<sup>2</sup> (E _N_ ) + _µ_<sup>2</sup> _V ar_ ( _N_ ) _._

_2.12. CONDITIONAL VARIANCE_

77

78 _CHAPTER 2. CONDITIONING_

## **Chapter 3**

---

[← Review of Undergraduate Probability](02-review-of-undergraduate-probability.md) · [Up: contents](index.md) · [The Central Limit Theorem →](04-the-central-limit-theorem.md)
