---
title: The Central Limit Theorem
source: https://www.stat.berkeley.edu/~aditya/resources/FullLectureNotes201AFall2019.pdf
source_file: sources/berkeley-guntuboyina-notes/FullLectureNotes201AFall2019.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The Central Limit Theorem

**Source:** [`FullLectureNotes201AFall2019.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullLectureNotes201AFall2019.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

I am using the second chapter of the book _Elements of Large Sample Theory_ by Erich Lehmann as the reference for our treatment of the CLT.

The Central Limit Theorem (CLT) is not a single theorem but encompasses a variety of results concerned with the sum of a large number of random variables which, suitably normalized, has a normal limit distribution. The following is the simplest version of the CLT and this is the version that we shall mostly deal with in this class.

**Theorem 3.0.1** (Central Limit Theorem) **.** _Suppose Xi, i_ = 1 _,_ 2 _, . . . are i.i.d with_ E( _Xi_ ) = _µ and var_ ( _Xi_ ) = _σ_<sup>2</sup> _< ∞. Then_


_converges in distribution to N_ (0 _,_ 1) _where X_<sup>¯</sup> _n_ = ( _X_ 1 + _· · ·_ + _Xn_ ) _/n._

We will discuss the following points about the CLT:

1. What does “convergence in distribution” mean?

2. How is the CLT proved?

3. Consequences and applications.

Informally, the CLT says that for i.i.d observations _X_ 1 _, . . . , Xn_ with finite mean _µ_ and variance _σ_<sup>2</sup> , the quantity<sup>_√_</sup> _<u>n</u>_ <u>(</u> _X_<sup>¯</sup> _n − µ_ ) _/σ_ is approximately (or asymptotically) _N_ (0 _,_ 1). Informally, the CLT also implies that

1.<sup>_√_</sup> _<u>n</u>_ <u>(</u> _X_<sup>¯</sup> _n − µ_ ) is approximately _N_ (0 _, σ_<sup>2</sup> ).

2. _X_<sup>¯</sup> _n_ is approximately _N_ ( _µ, σ_<sup>2</sup> _/n_ ).

79

_CHAPTER 3. THE CENTRAL LIMIT THEOREM_

80

3. _Sn_ = _X_ 1 + _· · ·_ + _Xn_ is approximately _N_ ( _nµ, nσ_<sup>2</sup> ).

4. _Sn − nµ_ is approximately _N_ (0 _, nσ_<sup>2</sup> ).

5. ( _Sn − nµ_ ) _/_ (<sup>_√_</sup> _<u>nσ</u>_ ) is approximately _N_ (0 _,_ 1).

It may be helpful here to note that


and also


The most remarkable feature of the CLT is that it holds regardless of the distribution of _Xi_ (as long as they are i.i.d from a distribution _F_ that has a finite mean and variance). Therefore the CLT is, in this sense, distribution-free. This makes it possible to derive, using the CLT, statistical procedures which are asymptotically valid without specific distributional assumptions. To illustrate the fact that the distribution of _Xi_ can be arbitrary, let us consider the following examples.

1. **Bernoulli** : Suppose _Xi_ are i.i.d Bernoulli random variables with probability of success given by _p_ . Then E _Xi_ = _p_ and _var_ ( _Xi_ ) = _p_ (1 _− p_ ) so that the CLT implies that<sup>_√_</sup> _<u>n</u>_ <u>(</u> _X_<sup>¯</sup> _n − p_ ) _/_ ~~�~~ _p_ (1 _− p_ ) is approximately _N_ (0 _,_ 1). This is actually called De Moivre’s theorem which was proved in 1733 before the general CLT. The general CLT stated above was proved by Laplace in 1810. The CLT also implies here that _Sn_ is approximately _N_ ( _np, np_ (1 _− p_ )). We know that _Sn_ is exactly distributed according to the _Bin_ ( _n, p_ ) distribution. We therefore have the following result: When _p_ is fixed and _n_ is large, the Binomial distribution _Bin_ ( _n, p_ ) is approximately same as the normal distribution with mean _np_ and variance _np_ (1 _− p_ ).

2. **Poisson** : Suppose _Xi_ are i.i.d _Poi_ ( _λ_ ) random variables. Then E _Xi_ = _λ_ = _var_ ( _Xi_ ) so that the CLT says that _Sn_ = _X_ 1 + _· · ·_ + _Xn_ is approximately Normal with mean _nλ_ and variance _nλ_ . It is not hard to show here that _Sn_ is exactly distributed as a _Poi_ ( _nλ_ ) random variable ( **prove this!** ). We deduce therefore that when _n_ is large and _λ_ is held fixed, _Poi_ ( _nλ_ ) is approximately same as the Normal distribution with mean _nλ_ and variance _nλ_ .

3. **Gamma** : Suppose _Xi_ are i.i.d random variables having the _Gamma_ ( _α, λ_ ) distribution. Check then that E _Xi_ = _α/λ_ and _var_ ( _Xi_ ) = _α/λ_<sup>2</sup> . We deduce then, from the CLT, that _Sn_ = _X_ 1 + _· · ·_ + _Xn_ is approximately normally distributed with mean _nα/λ_ and variance _nα/λ_<sup>2</sup> . We derived in the last class that _Sn_ is exactly distributed as _Gamma_ ( _nα, λ_ ). Thus when _n_ is large and _α_ and _λ_ are held fixed, the _Gamma_ ( _nα, λ_ ) is approximately closely by the _N_ ( _nα/λ, nα/λ_<sup>2</sup> ) distribution according to the CLT.

4. **Chi-squared** . Suppose _Xi_ are i.i.d chi-squared random variables with 1 degree of freedom i.e., _Xi_ = _Zi_<sup>2for i.i.d standard normal random variables</sup><sup>_Z_1</sup><sup>_, Z_2</sup><sup>_, . . ._.It is easy to check then that</sup><sup>_Xi_is</sup> a _Gamma_ (1 _/_ 2 _,_ 1 _/_ 2) random variable. This gives that _X_ 1 + _· · ·_ + _Xn_ is exactly _Gamma_ ( _n/_ 2 _,_ 1 _/_ 2).

_3.1. CONVERGENCE IN DISTRIBUTION_

81

This exact distribution of _X_ 1 + _· · ·_ + _Xn_ is also called the chi-squared distribution with _n_ degrees of freedom (denoted by _χ_<sup>2</sup> _n_<sup>).</sup> The CLT therefore implies that the _χ_<sup>2</sup> _n_<sup>distributionisclosely</sup> approximated by _N_ ( _n,_ 2 _n_ ).

5. **Cauchy** . Suppose _Xi_ are i.i.d standard Cauchy random variables. Then _Xi_ ’s do not have finite mean and variance. Thus the CLT does not apply here. In fact, it can be proved here that ( _X_ 1 + _· · ·_ + _Xn_ ) _/n_ has the Cauchy distribution for every _n_ .

### **3.1 Convergence in Distribution**

In order to understand the precise meaning of the CLT, we need to understand the notion of _convergence in distribution_ .

**Definition 3.1.1** (Convergence in Distribution) **.** _Suppose Y_ 1 _, Y_ 2 _, . . . are random variables and F is a cdf. We say that Yn converges in distribution to F (or that Yn converges in Law to F ) as n →∞ if_

P _{Yn ≤ y} → F_ ( _y_ ) _as n →∞_

_for every y at which the cdf F is continuous. We denote this by Yn→L F ._

Put another way, if _Fn_ denotes the cdf of _Yn_ , then _Yn→L F_ if and only if

_Fn_ ( _y_ ) _→ F_ ( _y_ ) as _n →∞_

for every _y_ that is a continuity point of _F_ .

We shall use the following conventions when talking about convergence in distribution.

1. If _F_ is the cdf of a standard distribution such as _N_ (0 _,_ 1), then we shall take


to mean that _Yn_ converges in distribution to the cdf of _N_ (0 _,_ 1).

2. For a random variable _Y_ , we shall take


to mean that _Yn_ converges in distribution to the cdf of _Y_ .

Note that convergence in distribution is defined in terms of cdfs which makes it possible to talk about a sequence of discrete random variables converging to a continuous distribution. For example, if _Yn_ has the discrete uniform distribution on the finite set _{_ 1 _/n,_ 2 _/n, . . . ,_ 1 _}_ , then according to the above definition _Yn→L Unif_ (0 _,_ 1). Note however that _Yn_ is discrete but _U_ (0 _,_ 1) is a continuous distribution.

Here are some things to remember about convergence in distribution:

_CHAPTER 3. THE CENTRAL LIMIT THEOREM_

82

1. Note that the definition of _Yn→L Y_ only requires that _Fn_ ( _y_ ) converges to _F_ ( _y_ ) at every _y_ which is a continuity point of _F_ (here _Fn_ and _F_ are the cdfs of _Yn_ and _Y_ respectively). If _F_ is a continuous cdf (such as a normal or a uniform cdf), then every point is a continuity point and then _Yn→L F_ is the same as saying that


But when _F_ is a discrete cdf, then, for _Yn→L F_ , we do not insist on P _{Yn ≤ y}_ converging to _F_ ( _y_ ) at points _y_ where _F_ is discontinuous. This is advantageous in a situation such as the following. Suppose that _Yn_ = 1 _/n_ for every _n ≥_ 1 and _Y_ = 0. Then it is easy to see that


However, the convergence above does not hold for _y_ = 0 as P _{Yn ≤_ 0 _}_ = 0 for every _n_ while P _{Y ≤_ 0 _}_ = 1. Thus if insisted on P _{Yn ≤ y}_ to converge to P _{Y ≤ y}_ at all points _y_ (as opposed to only continuity points), then _Yn_ = 1 _/n_ will not converge in distribution to _Y_ = 0 (which will be quite unnatural). This is one justification for including the restriction of continuity points of _F_ in the definition of convergence of distribution.

2. The statement _Yn→L Y_ might suggest that _Yn_ is close to _Y_ for large _n_ . This is actually not true. _Yn→L Y_ only says that the **distribution** of _Yn_ is close to that of _Y_ . It is actually more appropriate to write _Yn→L F_ where _F_ is the cdf of _Y_ . For example, suppose that _Y ∼ Unif_ (0 _,_ 1) and let _Yn_ be equal to _Y_ for odd values of _n_ and equal to (1 _− Y_ ) for even values of _n_ . Then, clearly each _Yn ∼ Unif_ (0 _,_ 1) so that both _Yn→L Y_ as well as _Yn→L_ 1 _− Y_ are true. But obviously _Yn_ is not close to _Y_ for even _n_ and _Yn_ is not close to 1 _− Y_ for odd _n_ .

3. When _F_ is a continuous cdf (which is the case when _F_ is, for example, the cdf of _N_ (0 _,_ 1)), the statement _Yn→L F_ is equivalent to


In this case (i.e., when _F_ is continuous), it also follows that


and also that


Let us now get back to the Central Limit Theorem.

**Theorem 3.1.2** (Central Limit Theorem) **.** _Suppose Xi, i_ = 1 _,_ 2 _, . . . are i.i.d with_ E( _Xi_ ) = _µ and var_ ( _Xi_ ) = _σ_<sup>2</sup> _< ∞. Then_


_where X_<sup>¯</sup> _n_ = ( _X_ 1 + _· · ·_ + _Xn_ ) _/n._

_3.2. MOMENT GENERATING FUNCTIONS_

83

The precise implication of the CLT is that


for every _y ∈_ R. Here Φ( _·_ ) is the cdf of _N_ (0 _,_ 1). Equivalently, the CLT also implies that


for every _a ≤ b_ . This is same as


Suppose now that _zα/_ 2 _>_ 0 is the point on the real line such that Φ( _zα/_ 2) = 1 _− α/_ 2 for 0 _< α <_ 1. Then taking _a_ = _−zα/_ 2 and _b_ = _zα/_ 2, we deduce that


This means that

is an asymptotic 100(1 _− α_ ) % confidence interval for _µ_ (assuming that _σ_ is known). The application of the CLT ensures that no specific distributional assumptions on _X_ 1 _, X_ 2 _, . . ._ are required for this result.

### **3.2 Moment Generating Functions**

Our next goal is to prove the CLT. Our main tool for the proof is the Moment Generating Function which is introduced now.

The Moment Generating Function (MGF) of a random variable _X_ is defined as the function:


for all _t ∈_ R for which E( _e_<sup>_tX_</sup> ) _< ∞_ . Note that _MX_ (0) = 1. There exist random variables (such as those that are distributed according to the standard Caucy distribution) for which _MX_ ( _t_ ) is infinite for every _t̸_ = 0.

**Example 3.2.1** (MGF of Standard Gaussian) **.** _If X ∼ N_ (0 _,_ 1) _, then its MGF can be easily computed as follows:_


_Thus MX_ ( _t_ ) = _e_<sup>_t_2</sup><sup>_/_2</sup> _for all t ∈_ R _._

_CHAPTER 3. THE CENTRAL LIMIT THEOREM_

84

The basic properties of MGFs are summarized below.

**1) Factorization for Sums of Independent Random Variables** : Suppose _X_ 1 _, . . . , Xn_ are independent, then


This is a consequence of the fact that


the last equality being a consequence of independence.

**2) Scaling** : _Ma_ + _bX_ ( _t_ ) = _e_<sup>_at_</sup> _MX_ ( _bt_ ) for all _t_ ( _a_ and _b_ are constants here). This is easy to prove.

**3) MGFs determine distributions** : If two random variables have MGFs that are finite and equal in an open interval containing 0, then they have the same distribution (i.e., same cdf everywhere). An implication of this is that _N_ (0 _,_ 1) is the same distribution which has MGF equal to _e_<sup>_t_2</sup><sup>_/_2</sup> for all _t_ .

**4) MGFs** **<u>provide</u> information on moments** : For _k ≥_ 1, the number E( _X_<sup>_k_</sup> ) is called the _k_<sup>_th_</sup> moment of the random variable _X_ . Knowledge of the MGF allows one to easily read off the moments of _X_ . Indeed, the power series expansion of the MGF is:


Therefore the _k_<sup>_th_</sup> moment of _X_ is simply the coefficient of _t_<sup>_k_</sup> in the power series of expansion of _MX_ ( _t_ ) multiplied by _k_ !.

Alternatively, one can derive the moments E( _X_<sup>_k_</sup> ) as derivatives of the MGF at 0. Indeed, it is easy to see that


so that


In words, E( _X_<sup>_k_</sup> ) equals the _k_<sup>_th_</sup> derivative of _MX_ at 0. Therefore


and so on.

As an example, we can deduce the moments of the standard normal distribution from the fact that its MGF equals _e_<sup>_t_2</sup><sup>_/_2</sup> . Indeed, because


_3.3. PROOF OF THE CLT USING MGFS_

85

it immediately follows that the _k_<sup>_th_</sup> moment of _N_ (0 _,_ 1) equals 0 when _k_ is odd and equals


The final important property of the MGF is the following.

**5) Connection between MGFs and Convergence in Distribution** : Suppose _Y, Y_ 1 _, Y_ 2 _, . . ._ are random variables that have finite MGFs in an open interval containing zero. Suppose that _MYn_ ( _t_ ) converges to _MY_ ( _t_ ) as _n →∞_ for every _t_ in that open interval. Then _Yn→L Y_ .

We shall use the above property in the next class to prove the CLT.

### **3.3 Proof of the CLT using MGFs**

Let us recall the basic setting. We have i.i.d random variables _X_ 1 _, X_ 2 _, . . ._ which have mean _µ_ and finite variance _σ_<sup>2</sup> .

Let _Yn_ :=<sup>_√_</sup> _<u>n</u>_ <u>(</u> _X_<sup>¯</sup> _n − µ_ ) _/σ_ . We need to show that _Yn→L N_ (0 _,_ 1). From the discussion on MGFs in the previous section, it is clear that it is enough to show that


Note that


As a result,


where _M_ ( _·_ ) is the MGF of ( _X_ 1 _− µ_ ) _/σ_ . We now use Taylor’s theorem to expand _M_ ( _tn_<sup>_−_1</sup><sup>_/_2</sup> ) up to a quadratic polynomial around 0.

Let us first quickly recap Taylor’s theorem. This says that for a function _f_ and two points _x_ and _p_ in the domain of _f_ , we can write


where _ξ_ is some point that lies between _x_ and _p_ . This formula requires that _f_ has ( _r_ + 1) derivatives in an open interval containing _p_ and _x_ .

Using Taylor’s theorem with _r_ = 1, _x_ = _tn_<sup>_−_1</sup><sup>_/_2</sup> and _p_ = 0, we obtain


_CHAPTER 3. THE CENTRAL LIMIT THEOREM_

86

for some _sn_ that lies between 0 and _tn_<sup>_−_1</sup><sup>_/_2</sup> . This implies therefore that _sn →_ 0 as _n →∞_ . Note now that _M_ (0) = 0 and _M_<sup>_′_</sup> (0) = E(( _X_ 1 _− µ_ ) _/σ_ ) = 0. We therefore deduce that


Note now that


We therefore invoke the following fact:

to deduce that

This completes the proof of the CLT assuming the fact (3.1). It remains to prove (3.1). There exist many proofs for this. Here is one. Write


Let _ℓ_ ( _x_ ) := log(1 + _x_ ). Taylor’s theorem for _ℓ_ for _r_ = 2 and _p_ = 0 gives


for some _ξ_ that lies between 0 and _x_ . Taking _x_ = _an/n_ , we get


for some _ξn_ that lies between 0 and _an/n_ (and hence _ξn →_ 0 as _n →∞_ ). As a result,


as _n →∞_ . This proves (3.1).

This completes the proof of the CLT. Note that we have tacitly assumed that the moment generating function of _X_ 1 _, . . . , Xn_ exists for all _t_ . This is much stronger than the existence of the variance of _Xi_ . This proof does not work if the MGF is not finite. There exist more advanced proofs (for example, which work with Characteristic functions as opposed to MGFs) which work only under the assumption of finite variance. These are beyond the scope of this class.

### **3.4 Two Remarks on the CLT**

A natural question with respect to the CLT is: why is _N_ (0 _,_ 1) (or _N_ (0 _, σ_<sup>2</sup> )) arising as the limit for sums of independent random variables (and not some other distribution)?

This can be explained in many ways. I will mention two common explanations below.

_3.5. CONVERGENCE IN DISTRIBUTION AND CONVERGENCE IN PROBABILITY_

87

1. The CLT computes the limiting distribution of


Consider now the following:


where _Yn_<sup>_′_is an independent copy of</sup><sup>_Yn_(independent copy means that</sup><sup>_Y_</sup> _n_<sup>_′_and</sup><sup>_Yn_are independent</sup> and have the same distribution). Thus if _Yn→L Y_ for a random variable _Y_ , then it must hold that


where = _d_ means “equality in distribution” meaning that _Y_ and ( _Y_ + _Y ′_ ) _/√_ 2 have the same distribution.

It is easy to see that if _Y ∼ N_ (0 _, τ_<sup>2</sup> ), then _Y_ and ( _Y_ + _Y_<sup>_′_</sup> ) _/√_ 2 have the same distribution. Conversely and remarkably, the _N_ (0 _, τ_<sup>2</sup> ) distribution is the only distribution which has this property (harder to prove). This, and the fact that _var_ ( _Yn_ ) = 1 for all _n_ , implies that _N_ (0 _,_ 1) is the only possible limiting distribution of _Yn_ .

2. Another interesting interpretation and explanation for the CLT comes from information theoretic considerations. Note that the random variables _Yn_ have variance equal to 1 for each _n_ . However, as _n_ increases, more variables _Xi_ are involved in the formula for _Yn_ . One can say therefore that the “entropy” of _Yn_ is increasing with _n_ while the variance stays the same at 1. Now there is a way of formalizing this notion of entropy and it is possible to show that the _N_ (0 _,_ 1) is the distribution that **maximizes** entropy subject to variance being equal to 1. This therefore says that the entropy of _Yn_ increases with _n_ (as more variables _Xi_ are involved in computing _Yn_ ) and eventually as _n →∞_ , one gets the maximally entropic distribution, _N_ (0 _,_ 1), as the limit. There is a way of making these precise.

### **3.5 Convergence in Distribution and Convergence in Probability**

Let us recall the definition of convergence in distribution which states that _Yn→L Y_ if


for every _y_ that is a continuity point of _F_ . Here _Fn_ is the cdf of _Yn_ and _F_ is the cdf of _Y_ . Note that only the cdf of the random variable _Y_ is relevant for _Yn→L Y_ and so one often writes _Yn→L F_ .

The statement _Yn→L Y_ might suggest that _Yn_ is close to _Y_ for large _n_ . This is actually not true. _Yn→L Y_ only says that the **distribution** of _Yn_ is close to that of _Y_ . It is actually more appropriate to

_CHAPTER 3. THE CENTRAL LIMIT THEOREM_

88

write _Yn→L F_ where _F_ is the cdf of _Y_ . For example, suppose that _Y ∼ Unif_ (0 _,_ 1) and let _Yn_ be equal to _Y_ for odd values of _n_ and equal to (1 _− Y_ ) for even values of _n_ . Then, clearly each _Yn ∼ Unif_ (0 _,_ 1) so that both _Yn→L Y_ as well as _Yn→L_ 1 _− Y_ are true. But obviously _Yn_ is not close to _Y_ for even _n_ and _Yn_ is not close to 1 _− Y_ for odd _n_ .

Let us introduce another notion of convergence between random variables known as _convergence in probability_ .

**Definition 3.5.1.** _We say that a sequence of random variables {Yn} converges to a random variable Y (written Yn→P Y ) if_ P _{|Yn − Y | ≥ ϵ} converges to zero as n →∞ for every ϵ >_ 0 _._

In this class, we shall use convergence in probability only when the limiting random variable _Y_ is equal to a constant. In this case, it is interesting to note that the notions of convergence in probability and convergence in distribution coincide. More specifically, for a constant _c_ ,


To see this, note first that the cdf _F_ ( _y_ ) of the constant random variable _c_ is equal to 0 for _y < c_ and 1 for _y > c_ . The definition of _→L_ then implies that _Yn→L c_ if and only if P _{Yn ≤ y}_ converges to 0 for _y < c_ and converges to 1 for _y > c_ . This then is easily seen to be equivalent to :


for every _ϵ >_ 0. One can then check that this is equivalent to _Yn→P c_ which proves (3.2).

The following result presents an intuitively obvious simple fact about convergence in probability. However, this result is slightly tricky to prove (you are welcome to try proving this; the result itself is useful for us but not the proof).

**Lemma 3.5.2.** _If X_ 1 _, X_ 2 _, . . . and Y_ 1 _, Y_ 2 _, . . . are two sequences of random variables satisfying Xn→P c and Yn→P c for two constants c and d. Then_


_3.6. EXAMPLES OF CONVERGENCE IN PROBABILITY_

89

### **3.6 Examples of Convergence in Probability**

#### **3.6.1 The Weak Law of Large Numbers**

**Theorem 3.6.1** (Weak Law of Large Numbers) **.** _Suppose X_ 1 _, X_ 2 _, . . . are independent and identically distributed random variables. Suppose that_ E _|Xi| < ∞ so that_ E _Xi is well-defined. Let_ E _Xi_ = _µ. Then_


Note that (3.6.1) holds with any distributional assumptions on the random variables _X_ 1 _, X_ 2 _, . . ._ (only the assumptions of independence and having identical distributions and the existence of the expectations are sufficient). The weak law is easy to prove under the additional assumption that the random variables have finite variances. This proof is based on the Chebyshev inequality which says that


Because


as _n →∞_ . As a result, from (3.4), we have that the left hand side of (3.4) converges to 0 which means that _X_<sup>¯</sup> _n→P µ_ .

#### **3.6.2 A sufficient condition for convergence in probability in terms of mean and variance**

It follows more generally that if _Y_ 1 _, Y_ 2 _, . . ._ is a sequence of random variables for which E _Yn_ converges to some parameter _θ_ and for which _var_ ( _Yn_ ) converges to zero, then _Yn→P θ_ . This is given in the following result.

**Lemma 3.6.2.** _Suppose Y_ 1 _, Y_ 2 _, . . . is a sequence of random variables such that_

_1._ E _Yn → θ as n →∞_

_2. var_ ( _Yn_ ) _→_ 0 _as n →∞._

_Then Yn→P θ as n →∞._

_Proof._ Write _Yn_ = E _Yn_ + ( _Yn −_ E _Yn_ ). Chebyshev’s inequality (and the fact that _var_ ( _Yn_ ) _→∞_ ) gives


for every _ϵ >_ 0 so that _Yn −_ E _Yn→P_ 0. This and E _Yn → θ_ implies (via the first assertion of Lemma 3.5.2) that _Yn_ = E _Yn_ + ( _Yn −_ E _Yn_ ) _→P θ_ .

_CHAPTER 3. THE CENTRAL LIMIT THEOREM_

90

#### **3.6.3 Consistency and examples**

In mathematical statistics, when _Yn→P θ_ , we say that _Yn_ is a consistent estimator for _θ_ or simply that _Yn_ is consistent for _θ_ . The Weak Law of Large Numbers simply says that _X_<sup>¯</sup> _n_ is consistent for E( _X_ 1). More generally, Lemma 3.6.2 states that _Yn_ is consistent for _θ_ if E( _Yn_ ) _→_ 0 and _var_ ( _Yn_ ) _→_ 0. The following examples present two more situations where consistency holds. **Example 3.6.3.** _Suppose X_ 1 _, X_ 2 _, . . . are i.i.d having the uniform distribution on_ (0 _, θ_ ) _for a fixed θ >_ 0 _. Then the maximum order statistic X_ ( _n_ ) := max( _X_ 1 _, . . . , Xn_ ) _is a consistent estimator for θ i.e., X_ ( _n_ ) _→P θ. We can see this in two ways. The first way is to use the Result (Lemma 3.6.2) above and compute the mean and variance of X_ ( _n_ ) _. X_ ( _n_ ) _/θ is the largest order statistic from an i.i.d sample of size n from Unif_ (0 _,_ 1) _and, as we have seen in the last class, X_ ( _n_ ) _/θ has the Beta_ ( _n,_ 1) _distribution. Therefore, using the mean and variance formulae for the Beta distribution (see wikipedia for these formulae), we have_

_and_

_which gives_


_and_


_It is clear from these that_ E _X_ ( _n_ ) _converges to θ and var_ ( _X_ ( _n_ )) _converges to_ 0 _respectively as n →∞ which implies (via Lemma 3.6.2) that X_ ( _n_ ) _converges in probability to θ._

_There is a second (more direct) way to see that X_ ( _n_ ) _→P θ. This involves writing_


_which clearly goes to zero as n →∞ (note that ϵ and θ are fixed). This, by the definition of convergence →P θ. in probability, shows that X_ ( _n_ )

**Example 3.6.4.** _Suppose X_ 1 _, X_ 2 _, . . . are i.i.d observations with mean µ and finite variance σ_<sup>2</sup> _. Then_


_is a consistent estimator for σ_<sup>2</sup> _. To see this first note that_


_converges in probability to σ_<sup>2</sup> _as n →∞ by the Weak Law of Large Numbers. This is because σ_ ˜ _n_<sup>2</sup><sup>_isthe_</sup> _average of i.i.d random variables Yi_ = ( _Xi − µ_ )<sup>2</sup> _for i_ = 1 _, . . . , n. The Weak Law therefore says that σ_ ˜ _n_<sup>2</sup><sup>_convergesinprobabilityto_E</sup><sup>_Y_1= E(</sup><sup>_X_1</sup><sup>_−µ_)2=</sup><sup>_σ_2</sup><sup>_._</sup>

_3.7. SLUTSKY’S THEOREM, CONTINUOUS MAPPING THEOREM AND APPLICATIONS_ 91

_Now to argue that σ_ ˆ _n_<sup>2</sup> _→P σ_ 2 _, the idea is simply to relate σ_ ˆ _n_ 2<sup>_toσ_˜</sup> _n_<sup>2</sup><sup>_.Thiscanbedoneasfollows:_</sup>


_The first term on the right hand side above converges to σ_<sup>2</sup> _by the Weak Law of Large Numbers (note that σ_<sup>2</sup> = E( _X_ 1 _− µ_ )<sup>2</sup> _). The second term converges to zero because X_<sup>¯</sup> _n→P µ (and Lemma 3.5.2). We use Lemma 3.5.2 again to conclude that σ_ ˆ _n_<sup>2</sup> _→P σ_ 2 _. Note that we have not assumed any distributional assumptions on X_ 1 _, X_ 2 _, . . . , Xn (the only requirement is they have mean zero and variance σ_<sup>2</sup> _)._

_By the way, we could have also defined σ_ ˆ _n by_


_with the factor of_ 1 _/_ ( _n −_ 1) _as opposed to_ 1 _/n. This will also converge in probability to σ_<sup>2</sup> _simply because_


_Since the first term above converges in probability to σ_<sup>2</sup> _and the second term converges to one, the product converges in probability to σ_<sup>2</sup> _(by Lemma 3.5.2)._

### **3.7 Slutsky’s Theorem, Continuous Mapping Theorem and Applications**

As we have seen before, an important consequence of the CLT from the statistical point of view is that it gives asymptotically valid confidence intervals for a mean parameter _µ_ . Indeed, given i.i.d observations _X_ 1 _, X_ 2 _, . . ._ with mean _µ_ and finite variance _σ_<sup>2</sup> , we have, as a consequence of the CLT,


for every _a ≤ b_ . This is same as

Suppose now that _zα/_ 2 _>_ 0 is the point on the real line such that Φ( _zα/_ 2) = 1 _− α/_ 2 for 0 _< α <_ 1. Then taking _a_ = _−zα/_ 2 and _b_ = _zα/_ 2, we deduce that


92

_CHAPTER 3. THE CENTRAL LIMIT THEOREM_

This means that


is an asymptotic 100(1 _− α_ ) % confidence interval for _µ_ (assuming that _σ_ is known). The application of the CLT ensures that no distributional assumptions on _X_ 1 _, X_ 2 _, . . ._ are required for this result.

The problem with the interval (3.5) is that it depends on _σ_ which will be unknown in a statistical setting (the only available data will be _X_ 1 _, . . . , Xn_ ). A natural idea is to replace _σ_ by a natural estimate such as


This will result in the interval:


Slutsky’s theorem stated next will imply that


which will mean that (3.7) is also an asymptotic 100(1 _− α_ )% confidence interval for _µ_ .

_→L Y , An→P a and Bn→P b, then_

**Theorem 3.7.1** (Slutsky’s theorem) **.** _If Yn_


Another useful result that we shall often use is the continuous mapping theorem:

**Theorem 3.7.2** (Continuous Mapping Theorem) **.** _1. Suppose Yn→L Y and f is a function that is continuous in the range of values of Y , then f_ ( _Yn_ ) _→L f_ ( _Y_ ) _._


One immediate application of these two results is (3.8) as shown below.

**Example 3.7.3.** _Let X_ 1 _, . . . , Xn be i.i.d observations with mean µ and variance σ_<sup>2</sup> _. We need to look at the limiting distribution of:_


_where σ_ ˆ _n is as defined in_ (3.6) _. Note that_


_The first term on the right hand side above converges in probability to N_ (0 _,_ 1) _by the usual CLT. For the second term, note that σn_<sup>2</sup> _→P σ_ 2 _(as proved in Example 3.6.4) and so applying the continuous mapping_

_3.7. SLUTSKY’S THEOREM, CONTINUOUS MAPPING THEOREM AND APPLICATIONS_ 93

_theorem with f_ ( _x_ ) = � _σ_<sup>2</sup> _/x implies that f_ (ˆ _σn_<sup>2)</sup> _→P_ 1 _. This gives that the second term above converges in probabilty to 1. We can thus use Slutsky’s theorem to observe that, since the first term above converges to N_ (0 _,_ 1) _in distribution and the second term converges in probability to 1, the random variable Tn converges in distribution to N_ (0 _,_ 1) _. As a result,_


_is still a_ 100(1 _− α_ ) _% asymptotically valid C.I for µ. Note that we have not assumed any distributional assumptions on X_ 1 _, . . . , Xn. In particular, the data can be non-Gaussian._

_The random variable Tn in_ (3.9) _is called the sample t-statistic. The name comes from the t- distrbution or t-density. For a given integer k ≥_ 1 _, the t-density with k degrees of freedom is the density of the random variable_


_where Z ∼ N_ (0 _,_ 1) _, A has the chi-squared density with k degrees (i.e., A ∼ χ_<sup>2</sup> _k_<sup>_)andZandAare_</sup> _independent random variables._

_Now when X_ 1 _, . . . , Xn are i.i.d N_ ( _µ, σ_<sup>2</sup> ) _, it can be shown (we will see how to do this later) that_


_and moreover the above two random variables are independent. As a result, the t-statistic Tn has the t-distribution with n −_ 1 _degrees of freedom when X_ 1 _, . . . , Xn are i.i.d N_ ( _µ, σ_<sup>2</sup> ) _._

_Therefore_

_1. When X_ 1 _, . . . , Xn are i.i.d N_ ( _µ, σ_<sup>2</sup> ) _, the sample t-statistic Tn has the t-distribution with n −_ 1 _degrees of freedom._

_2. When X_ 1 _, . . . , Xn are i.i.d with mean µ and finite variance σ_<sup>2</sup> _(no distributional assumption), the t-statistic, Tn converges in distribution to N_ (0 _,_ 1) _._

_It may be helpful to note in connection with the above that the t-distribution with k degrees of freedom itself converges in distribution to N_ (0 _,_ 1) _as k →∞._

**Example 3.7.4** (Bernoulli Parameter Estimation) **.** _Suppose X_ 1 _, X_ 2 _, . . . , Xn are i.i.d having the Ber_ ( _p_ ) _distribution. The CLT then gives_

_which gives_


_CHAPTER 3. THE CENTRAL LIMIT THEOREM_

94

_This will not directly lead to a C.I for p. To do this, it is natural to replace p in the denominator by X_ ¯ _. This can be done because_


_and by Slutsky’s theorem, the above random variables converge in distribution to N_ (0 _,_ 1) _. To give more details, we are using the fact that the first random variable above converges in distribution to N_ (0 _,_ 1) _by the CLT and the second random variable converges in probabiliity to_ 1 _(basically X_<sup>¯</sup> _n→P µ and then use the continuous mapping theorem). This allows us to deduce that_

_so that_


_is an asymptotically valid_ 100(1 _− α_ ) _% C.I for p._

**Example 3.7.5** (Poisson Mean Estimation) **.** _Suppose X_ 1 _, X_ 2 _, . . . , Xn are i.i.d having the Poi_ ( _λ_ ) _distribution. The CLT then gives_


_which gives_


_It is not easy to convert this into a C.I for λ. This will become much simpler if we can replace the λ in the denominator by X_<sup>¯</sup> _. This can be done because_


_and by Slutsky’s theorem, the above random variables converge in distribution to N_ (0 _,_ 1) _(we are using here that X_<sup>¯</sup> _n→P λ which is a consequence of the Weak Law of Large Numbers). This allows us to deduce that_

_so that_


_is an asymptotically valid_ 100(1 _− α_ ) _% C.I for λ._

**Example 3.7.6** (Asymptotic Distribution of sample variance) **.** _Let X_ 1 _, X_ 2 _, . . . be i.i.d with mean µ and finite variance σ_<sup>2</sup> _. Let_


_3.8. DELTA METHOD_

95

_We know that σ_ ˆ _n_<sup>2</sup> _→P σ_ 2 _. Can we also find the limiting distribution of_<sup>_√_</sup> _<u>n</u>_ � _σ_ ˆ _n_<sup>2</sup><sup>_−σ_2�</sup> _?_

_To do this, write_


_Now by the CLT,_


_where τ_<sup>2</sup> = _var_ (( _X_ 1 _− µ_ )<sup>2</sup> ) _(we are assuming, of course, that τ_<sup>2</sup> _< ∞) and, by Slutsky’s theorem,_


_Thus by Slutsky’s theorem again, we obtain_


Another easy consequence of Slutsky’s theorem is the following.

**Fact** : If _rn_ ( _Tn − θ_ ) _→L Y_ for some rate _rn →∞_ (typically _rn_ =<sup>_√_</sup> _<u>n</u>_ <u>).</u> Then _Tn→P θ_ .

This immediately follows from Slutsky’s theorem because


as 1 _/rn →_ 0 and _rn_ ( _Tn − θ_ ) _→L Y_ .

Here is a simple consequence of the CLT and the continuous mapping theorem. Suppose _X_ 1 _, X_ 2 _, . . ._ are i.i.d random variables with mean _µ_ and finite variance _σ_<sup>2</sup> . Then the CLT says that


The continuous mapping theorem then gives


### **3.8 Delta Method**

Delta Method is another general statement about convergence in distribution that has interesting applications when used in conjunction with the CLT.

_CHAPTER 3. THE CENTRAL LIMIT THEOREM_

96

**Theorem 3.8.1** (Delta Method) **.** _If_<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Tn − θ_ ) _→L N_ (0 _, τ_ 2) _, then_


_provided g_<sup>_′_</sup> ( _θ_ ) _exists and is non-zero._

Informally, the Delta method states that if _Tn_ has a limiting Normal distribution, then _g_ ( _Tn_ ) also has a limiting normal distribution and also gives an explicit formula for the asymptotic variance of _g_ ( _Tn_ ). This is surprising because _g_ can be linear or non-linear. In general, non-linear functions of normal random variables do not have a normal distribution. But the Delta method works because under the assumption that<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Tn − θ_ ) _→L N_ (0 _, τ_ 2), it follows that _Tn→P θ_ so that _Tn_ will be close to _θ_ at least for large _n_ . In a neighborhood of _θ_ , the non-linear function _g_ can be approximated by a linear function which means that _g_ effectively behaves like a linear function. Indeed, the Delta method is a consequence of the approximation:


Here is an application of the Delta method.

**Example 3.8.2.** _Suppose_ 0 _≤ p ≤_ 1 _is a fixed parameter and suppose that we want to estimate p_<sup>2</sup> _. Let us assume that we have two choices for estimating p_<sup>2</sup> _:_

_1. We can estimate p_<sup>2</sup> _by X/n where X is the number of successes in n binomial trials with probability p_<sup>2</sup> _of success._

_2. We can estimate p_<sup>2</sup> _by_ ( _Y/n_ )<sup>2</sup> _where Y is the number of successes in n binomial trials with probability p of success._

_Which of the above is a better estimator of p_<sup>2</sup> _and why? The Delta method provides a simple answer to this question. Note that, by the CLT, we have_


_and that_


_The Delta method can now be used to convert the above limiting statement into an accuracy statement for_ ( _Y/n_ )<sup>2</sup> _as:_


_We deduce therefore that_ ( _X/n_ ) _is a better estimator of p_<sup>2</sup> _compared to_ ( _Y/n_ )<sup>2</sup> _provided_


_which is equivalent to p >_ 1 _/_ 3 _. Thus when p >_ 1 _/_ 3 _, X/n is a better estimator of p_<sup>2</sup> _compared to_ ( _Y/n_ )<sup>2</sup> _and when p <_ 1 _/_ 3 _,_ ( _Y/n_ )<sup>2</sup> _is the better estimator._

_3.9. APPLICATION OF THE DELTA METHOD TO VARIANCE STABILIZING TRANSFORMATIONS_ 97

### **3.9 Application of the Delta Method to Variance Stabilizing Transformations**

#### **3.9.1 Motivating Variance Stabilizing Transformations**

The Delta method can be applied to variance stabilizing transformations. For example, consider the example where we observe data _X_ 1 _, X_ 2 _, . . . , Xn_ that are i.i.d having the _Ber_ ( _p_ ) distribution. The CLT then states that


It is inconvenient that _p_ also appears in the variance term. This presents an annoyance while finding confidence intervals for _p_ . One way around this problem is to observe that, by Slutsky’s theorem,


This was done in the last class. While this method is okay, one might still wonder if it is possible to obtain a function _f_ having the property that


where the variance _c_<sup>2</sup> **does not depend on** _p_ . Such a function _f_ would be called a variance stabilizing transformation.

For another example, consider the case where we observe data _X_ 1 _, . . . , Xn_ that are i.i.d having the _Poi_ ( _λ_ ) distribution. The CLT then states that


The fact that _λ_ appears in the variance term above presents an annoyance while finding confidence intervals for _λ_ . As done in last class, we can get around this by observing (via Slutsky’s theorem) that


While this method is okay, one might still wonder if it is possible to obtain a function _f_ having the property that


where the variance _c_<sup>2</sup> does not depend on _λ_ . If one could indeed find such an _f_ , it will be referred to as a variance stabilizing transformation.

#### **3.9.2 Construction of the Variance Stabilizing Transformation**

More generally, given the result:


_CHAPTER 3. THE CENTRAL LIMIT THEOREM_

98

where the variance _τ_<sup>2</sup> ( _θ_ ) depends on _θ_ , is it possible to find a transformation _f_ for which


where the variance _c_<sup>2</sup> does not depend on _θ_ . We would then say that the function _f_ is a _variance stabilizing transformation_ .

This is possible to do via the Delta method. Indeed, Delta method states that


and so, in order to guarantee (3.13), we only have to choose _f_ so that


which means that _f_ ( _θ_ ) = � _τ_ ( _<u>cθ</u>_ )<sup>_dθ_(indefiniteintegral).</sup>

#### **3.9.3 Back to the Bernoulli Example**

Here we have _X_ 1 _, . . . , Xn_ which are i.i.d having the _Ber_ ( _p_ ) distribution so that by CLT


Therefore (3.12) holds with _Tn_ = _X_<sup>¯</sup> _n_ , _θ_ = _p_ and _τ_<sup>2</sup> ( _θ_ ) = _θ_ (1 _− θ_ ). The formula (3.13) says therefore that we choose _f_ as


which means that _f_ ( _θ_ ) = 2 _c_ arcsin( _√θ_ ). The Delta method then guarantees that


This implies that

so that


is an approximate 100(1 _− α_ )% C.I for<sup>_√_</sup> _<u>p</u>_ . The lower end point of the above interval can be negative (note that arcsin(� _X_ <u>¯</u> _n_ ) takes values between 0 and _π/_ 2 but arcsin(� _X_ <u>¯</u> _n_ ) _− zα/_ 2 _/_ (2<sup>_√_</sup> _<u>n</u>_ <u>)</u> can be negative) while<sup>_√_</sup> _<u>p</u>_ is always positive. So we can replace the lower end point by 0 if it turns out to be negative. Using the notation _x_ + = max( _x,_ 0), we see that


_3.9. APPLICATION OF THE DELTA METHOD TO VARIANCE STABILIZING TRANSFORMATIONS_ 99

is an approximate 100(1 _− α_ )% C.I for<sup>_√_</sup> _<u>p</u>_ <u>.</u> To get a confidence interval for _p_ , we can simply square the two end points of the above interval. This allows us to deduce that


is an approximate 100(1 _− α_ )% C.I for _p_ .

#### **3.9.4 Back to the Poisson Example**

Let us now get back to the Poisson distribution where we have _X_ 1 _, . . . , Xn_ are i.i.d _Poi_ ( _λ_ ) and CLT gives (3.11). Therefore _Tn_ = _X_<sup>¯</sup> _n_ , _θ_ = _λ_ and _τ_<sup>2</sup> ( _θ_ ) = _θ_ . The equation (3.14) suggests that we choose _f_ as


where means that _f_ ( _θ_ ) = 2 _c√θ_ . The Delta method then guarantees that


Therefore the square-root transformation applied to _X_<sup>¯</sup> _n_ ensures that the resulting variance (of ~~�~~ _X_ <u>¯</u> _n_ ) does not depend on _λ_ (in a limiting sense).

The fact (3.15) will lead to approximate confidence intervals for _λ_ . Indeed, (3.15) immediately implies that

so that


is an approximate 100(1 _− α_ ) % C.I for _√λ_ . Note that the lower end point of the above interval can be negative while _λ_ is always positive. So we can replace the lower end point by 0 if it turns out to be negative. Again using the notation _x_ + := max( _x,_ 0), we see that


is an approximate 100(1 _− α_ ) % C.I for _√λ_ . To get a confidence interval for _λ_ , we can simply square the two end points of the above interval. This allows us to deduce that


is an approximate 100(1 _− α_ ) % C.I for _λ_ .

_CHAPTER 3. THE CENTRAL LIMIT THEOREM_

100

This interval can be compared with the interval that was obtained in the previous lecture using Slutsky’s theorem. That interval was


The intervals (3.16) and (3.17) may look different but they are actually quite close to each other for large _n_ . To see this, note that the difference between the upper bounds of these two intervals is at most _zα/_<sup>2</sup> 2<sup>_/_(4</sup><sup>_n_)whichisverysmallwhen</sup><sup>_n_islarge(thesameistrueofthelowerbounds).</sup>

#### **3.9.5 Chi-squared Example**

Let us now look at another example where the variance stabilizing transformation is the log function.

Suppose _X_ 1 _, X_ 2 _, . . ._ are i.i.d such that _Xi/σ_<sup>2</sup> has the chi-squared distribution with one degree of freedom. In other words,


Because E( _X_ 1) = _σ_<sup>2</sup> and _var_ ( _X_ 1) = 2 _σ_<sup>4</sup> , the CLT says that


Can we now find a function _f_ such that _f_ ( _X_<sup>¯</sup> _n_ ) has a limiting variance that is independent of _σ_<sup>2</sup> ? Because (3.18) has the form (3.12) with _Tn_ = _X_<sup>¯</sup> _n_ , _θ_ = _σ_<sup>2</sup> and _τ_<sup>2</sup> ( _θ_ ) = 2 _θ_<sup>2</sup> , we can use (3.14) which suggests taking _f_ so that _f_<sup>_′_</sup> ( _θ_ ) = _c/τ_ ( _θ_ ) = _c/_ ( _√_ 2 _θ_ ). This gives

allowing us to conclude that


Square-roots and logarithms are common transformations that are applied to data when there is varying variance (see, for example, `https://en.wikipedia.org/wiki/Variance-stabilizing_ transformation` ).

#### **3.9.6 Geometric Example**

Suppose _X_ 1 _, X_ 2 _, . . ._ are i.i.d having the Geometric distribution with parameter _p_ . Recall that _X_ has the _Geo_ ( _p_ ) distribution if _X_ takes the values 1 _,_ 2 _, . . ._ with the probabilities


_3.10. DELTA METHOD WHEN G_<sup>_′_</sup> ( _θ_ ) = 0

101

The number of independent tosses (of a coin with probability of heads _p_ ) required to get the first head has the _Geo_ ( _p_ ) distribution.

I leave as an easy exercise to verify that for _X ∼ Geo_ ( _p_ )


The CLT therefore states that for i.i.d observations _X_ 1 _, X_ 2 _, . . ._ having the _Geo_ ( _p_ ) distribution, we have


What is the variance stabilizing transformation for _X_<sup>¯</sup> _n_ i.e., what is the transformation _f_ for which _f_ ( _X_<sup>¯</sup> _n_ ) has constant asymptotic variance? To answer this, note that the above displayed equation is of the same form as (3.12) with _Tn_ = _X_<sup>¯</sup> _n_ , _θ_ = 1 _/p_ and _τ_<sup>2</sup> ( _θ_ ) = (1 _− p_ ) _/p_<sup>2</sup> . We then write _τ_ ( _θ_ ) in terms of _θ_ as (note that _p_ = 1 _/θ_ )


The variance stabilizing transformation is therefore given by


Therfore _f_ ( _θ_ ) = 2 _c_ log( _√θ_ + _√θ −_ 1) is the variance stabilizing transformation here and


### **3.10 Delta Method when** _g_<sup>_′_</sup> ( _θ_ ) = 0

Suppose that<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Tn − θ_ ) _→L N_ (0 _, τ_ 2). We are now interested in the asymptotic distribution of _g_ ( _Tn_ ). The Delta method stated that when _g_<sup>_′_</sup> ( _θ_ ) _̸_ = 0, we have


This is essentially a consequence of the Taylor approximation: _g_ ( _Tn_ ) _g_ ( _θ_ ) _≈ g_<sup>_′_</sup> ( _θ_ )( _Tn − θ_ ). What would happen if _g_<sup>_′_</sup> ( _θ_ ) = 0? In this case, the statement (3.19) will still be correct if the right hand side is interpreted as the constant 0 i.e., when _g_<sup>_′_</sup> ( _θ_ ) = 0, the following holds:


However this only states that _g_ ( _Tn_ ) _− g_ ( _θ_ ) is of a smaller order compared to _n_<sup>_−_1</sup><sup>_/_2</sup> but does not precisely say what the exact order is and what the limiting distribution is when scaled by the correct order. To figure out these, we need to consider the higher order terms in the Taylor expansion for _g_ ( _Tn_ ) around _θ_ . Assume, in the sequel, that _g_<sup>_′_</sup> ( _θ_ ) = 0 and that _g_<sup>_′′_</sup> ( _θ_ ) _̸_ = 0.

_CHAPTER 3. THE CENTRAL LIMIT THEOREM_

102

In this case, we do a two term Taylor approximation:


As a result, we have


Now by the continuous mapping theorem:


and hence we have


Therefore when _g_<sup>_′_</sup> ( _θ_ ) = 0 and _g_<sup>_′′_</sup> ( _θ_ ) _̸_ = 0, the right scaling factor is _n_ and the limiting distribution is a scaled multiple of _χ_<sup>2</sup> 1<sup>(notethatthelimitisnotanormaldistribution).</sup>

**Example 3.10.1.** _Suppose X_ 1 _, X_ 2 _, . . . , Xn are i.i.d Ber_ ( _p_ ) _random variables. Suppose we want to estimate p_ (1 _−p_ ) _. The natural estimator is X_<sup>¯</sup> _n_ (1 _−X_<sup>¯</sup> _n_ ) _. What is the limiting behavior of this estimator?_

_This can be answered by the Delta method by taking g_ ( _θ_ ) = _θ_ (1 _− θ_ ) _. Note first that by the usual CLT,_


_For g_ ( _θ_ ) = _θ_ (1 _− θ_ ) _, note that_


_so that g_<sup>_′_</sup> ( _p_ ) _̸_ = 0 _when p̸_ = 1 _/_ 2 _. Thus when p̸_ = 1 _/_ 2 _, the Delta method gives_


_But when p_ = 1 _/_ 2 _, we have to use_ (3.20) _instead of_ (3.19) _and this gives (note that g_<sup>_′′_</sup> ( _p_ ) = _−_ 2 _)_


## **Chapter 4**

---

[← Conditioning](03-conditioning.md) · [Up: contents](index.md) · [Second Order Theory of Random Vectors →](05-second-order-theory-of-random-vectors.md)
