---
title: 25 Lecture 25
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 25 Lecture 25

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The next (and last) topic in this class is about minimax lower bounds. In this lecture, we shall mainly motivate the study of minimax lower bounds. We start with the basic decision-theoretic setting under which these are studied.

## **25.1 Decision Theoretic Framework**

Minimaxity can be studied in the general and abstract decision theoretic framework. This framework is described here. A classical reference for this is the book Ferguson [8, Chapter 1 and 2].

We have an unknown parameter _θ_ . _θ_ can be a real-number or a vector or a function or a matrix etc. We assume that _θ_ takes values in a known set Θ which we refer to as the Parameter Space.

The data will be generically be denoted by _X_ . Again _X_ can be a real-number, vector or function or matrix etc. We assume that _X_ takes values in a set _X_ which is referred to as the sample space.

The connection between _X_ and _θ_ is that the distribution of _X_ depends on _θ_ through a known probability measure _Pθ_ . The class of all probability measures _{Pθ, θ ∈_ Θ _}_ will be denoted by _P_ . We assume that each _Pθ_ has a density _pθ_ with respect to a single sigma finite measure _µ_ .

Next, we have an action space _A_ which corresponds to the actions that the statistician needs to take in the problem (for example, in estimation problems, _A_ will be equal to or larger than Θ, in testing problems with a null and an alternative hypothesis, _A_ will correspond to the two hypotheses etc. specific examples are given below).

The loss function _L_ is a nonnegative function defined on Θ _× A_ i.e., for every parameter _θ ∈_ Θ and action _a ∈A_ , there is associated a nonnegative loss _L_ ( _θ, a_ ).

A nonrandomized decision rule _d_ is a function from _X_ to _A_ . In other words, _d_ associates an action to every _x ∈X_ . The risk of a decision rule _d_ at a particular parameter value _θ_ is defined by


where the expectation above is taken with respect to _X ∼ Pθ_ .

The goal of a statistician in a decision problem is to choose a decision rule _d_ whose risk _R_ ( _θ, d_ ) is small. This statement of “small risk” needs to be qualified further however because the risk _R_ ( _θ, d_ ) depends on the unknown _θ_ . In other words, the risk of a decision rule _d_ depends on what the unknown parameter value (or state of nature) is. So when we say small risk, we need to specify if we mean uniformly small risk over _θ_ or small average risk or small worst case risk. We shall come back to this issue shortly after seeing some examples of decision-theoretic problems.

**Example 25.1.** _Consider the problem of estimating a vector θ ∈_ R<sup>_n_</sup> _from an observation Y ∼ Nn_ ( _θ, In_ ) _under squared error loss. Suppose it is known that θ is k-sparse i.e., the number of non-zero entries in θ is at most k. This can be be put in the decision theoretic framework outlined above by taking_ Θ _to be the set of all k-sparse vectors in_ R<sup>_n_</sup> _, X_ = R<sup>_n_</sup> _, A_ = Θ _or A_ = R<sup>_n_</sup> _(depending on whether we want our estimators to be k-sparse or not) and L_ ( _θ, a_ ) = _∥θ − a∥_<sup>2</sup> _. Also Pθ is the Nn_ ( _θ, In_ ) _distribution. Decision rules are simply estimators for θ and the risk of an estimator θ_<sup>ˆ</sup> _is given by_


**Example 25.2.** _Consider the same setting as the last problem but suppose now that we want to estimate the L_<sup>1</sup> _-norm of θ (and not the entire vector θ): ∥θ∥_ 1 := _|θ_ 1 _|_ + _· · ·_ + _|θn|. Then_ Θ _, X and Pθ remain the same as in the previous example but A_ = R _and the loss function is L_ ( _θ, a_ ) = ( _∥θ∥_ 1 _− a_ )<sup>2</sup> _._

134

**Example 25.3.** _Consider the problem of estimating a Lipschitz function f_ : [0 _,_ 1] _→_ R _from independent observations Y_ 1 _, . . . , Yn with Yi ∼ N_ ( _f_ ( _i/n_ ) _,_ 1) _for i_ = 1 _, . . . , n. In this problem, we can take_ Θ _to be the class of all Lipschitz functions from_ [0 _,_ 1] _to_ R _. For f ∈_ Θ _, the probability measure Pf is the multivariate normal distribution with mean_ ( _f_ (1 _/n_ ) _, . . . , f_ ( _n/n_ )) _and covariance matrix In. The action space can be taken to be the space of all real-valued functions on_ [0 _,_ 1] _and the loss function can be either:_


**Example 25.4.** _Consider the problem of testing H_ 0 : _θ_ = 0 _against H_ 1 : _θ_ = 1 _from n independent observations X_ 1 _, . . . , Xn drawn from N_ ( _θ,_ 1) _. Because we are testing θ_ = 0 _against θ_ = 1 _, we believe that only these two values are possible so we take_ Θ = _{_ 0 _,_ 1 _}. The action space is then also A_ = _{_ 0 _,_ 1 _}. A natural loss function is L_ ( _θ, a_ ) = _I{θ̸_ = _a}. Given a decision rule d (test), its risk is given by_


_Note that if θ_ = 0 _, then the risk is given by R_ (0 _, d_ ) = _P_ 0 _{d_ ( _X_ ) = 1 _} which is the usual Type I error. When θ_ = 1 _, the risk is given by R_ (1 _, d_ ) = _P_ 1 _{d_ ( _X_ ) = 0 _} which is the Type II error._

**Example 25.5.** _Consider the problem of testing the hypothesis H_ 0 : _θ ∈_ Θ0 _against H_ 1 : _θ ∈_ Θ1 _on the basis of n i.i.d observations X_ 1 _, . . . , Xn from the N_ ( _θ,_ 1) _distribution. In this case,_ Θ = Θ0 _∪_ Θ1 _, A_ = _{_ 0 _,_ 1 _} and_


_The risk of a decision rule (test) d is given by R_ ( _θ, d_ ) = _Pθ{d_ ( _X_ ) = 1 _} if θ ∈_ Θ0 _and R_ ( _θ, d_ ) = _Pθ{d_ ( _X_ ) = 0 _} if θ ∈_ Θ1 _. These can again be treated as type I and type II errors respectively. Note that these depend on θ (i.e., there is a family of type I errors for each θ ∈_ Θ0 _and a family of type II errors for each θ ∈_ Θ1 _)._

## **25.2 How to evaluate decision rules**

As mentioned earlier, the risk _R_ ( _θ, d_ ) of a decision rule _d_ depends on _θ_ . It turns out that usually it is impossible to find a single decision rule _d_<sup>_∗_</sup> such that


For example, in an estimation problem with Θ = _A ⊆_ R<sup>_k_</sup> and _L_ ( _θ, a_ ) = _∥θ − a∥_<sup>2</sup> . Consider the estimator _d_ 0( _X_ ) = _θ_ 0 for a fixed _θ_ 0 _∈_ Θ. This estimator clearly has risk equal to 0 at _θ_ = _θ_ 0 (i.e., _R_ ( _θ_ 0 _, d_ 0) = 0). Thus if there existed a decision rule _d_<sup>_∗_</sup> which satisfies (234), then _R_ ( _θ_ 0 _, d_<sup>_∗_</sup> ) _≤ R_ ( _θ_ 0 _, d_ 0) = 0. Since _θ_ 0 _∈_ Θ is arbitrary here, this must mean that


for every _θ ∈_ Θ. This implies that _d_<sup>_∗_</sup> ( _X_ ) = _θ_ almost surely under _Pθ_ for every _θ ∈_ Θ. This obviously cannot happen for general classes _{Pθ, θ ∈ θ}_ .

Therefore we cannot hope for an optimal decision rule _d_<sup>_∗_</sup> in the strong sense (234). There are three common ways of getting a relaxed notion of optimality:

1. The first way involves restricting to a subclass of all decision rules. For example, in parametric estimation problems, it is common to restrict attention to unbiased or equivariant estimators. In parametric testing problems, it is natural to restrict attention to level _α_ tests or unbiased level _α_ tests. This approach was taken in STAT 210A and we will not pursue it here.

2. Bayes approach

3. Minimax approach

We will study the Bayes and Minimax approaches in detail here.

135

## **25.3 Bayes Approach**

Here we fix a probability measure _w_ on Θ and evaluate decision rules by their average risk (where the averaging is done with respect to _w_ ). In other words, we evaluate decision rules _d_ by their average risk:


with respect to the probability measure _w_ . The probability measure _w_ is also referred to as a proper prior or simply prior. The smallest achievable average risk is called the Bayes risk with respect to _w_ and is denoted by


and the estimator _d_ which minimizes (235) is known as the Bayes estimator with respect to _w_ .

The obvious problem with this approach of evaluating decision rules is its dependence on the prior _w_ and, in many situations, it is not clear what a reasonable choice of the prior is. For example, in the Lipschitz regression problem of Example 25.3, one would need to choose a prior on the class of all Lipschitz functions on [0 _,_ 1] and it is not clear how one can do this.

The above issue notwithstanding, the Bayes approach has the important advantage in that finding the Bayes rule (the rule which minimizes (235)) is, in principle, tractable. Indeed, we can write (235) as


We now interchange the order of integration above (this is allowed because the loss function is nonnegative) to get


From the simple inequality

which holds for every _x ∈X_ , it should be clear that the rule which minimizes (235) is given by


The density


is simply the posterior density of _θ_ given _X_ = _x_ in the model _X|θ ∼ pθ_ and _θ ∼ w_ . We thus obtain the well-known fact that Bayes rule minimizes the posterior expectation of the Loss function. For example, in the case of the squared error loss _L_ ( _θ, a_ ) = _∥θ − a∥_<sup>2</sup> , the Bayes rule is simply the expectation of the posterior distribution.

The above calculation also gives an exact expression for the Bayes risk with respect to _w_ :


136

## **25.4 Minimax Approach**

In the minimax approach, we evaluate decision rules by their worst case (supremum) risk over _θ ∈_ Θ. In other words, we aim to select a decision rule _d_ for which sup _θ∈_ Θ _R_ ( _θ, d_ ) is small. The advantage with this approach is that one does not need to select a specific prior distribution. The disadvantage is that it focuses on worst case behavior and might be regarded as too pessimistic. Nevertheless, this is most widely used optimality criterion currently.

The minimax risk is defined as


where the infimum is taken over all decision rules _d_ . A decision rule _d_<sup>_∗_</sup> is said to be minimax if


Finding minimax estimators is quite difficult in many problems so one is often with approximate minimaxity. There are two commonly used notions of approximate minimaxity. These are defined in terms of a “sample size” or “dimension” parameter _n_ that is present in most decision problems. Specifically, we assume that possibly all the ingredients of the decision problem (i.e., Θ, _A_ , _L_ ( _θ, a_ ) and _Pθ_ ) depend on a sample size or dimension parameter _n_ and we are interested in the problem only for large values of _n_ . In this context, we have the following two definitions:

1. **Sharp Asymptotically Minimaxity** : We say that a decision rule _d_<sup>_∗_</sup> is sharp asymptotically minimax if


as _n →∞_ . This is equivalent to


2. **Rate Minimaxity** : We say that a decision rule _d_<sup>_∗_</sup> is rate minimax if


for a constant _C_ that does not depend on _n_ . This is equivalent to saying that


Consider now the following situation. Suppose we have a decision rule _d_<sup>_∗_</sup> which we have constructed (say by some _M_ -estimation method) and we have a good understanding of its performance in the sense that we have an upper bound _un_ on its supremum risk over Θ i.e., we know that


How then would we show that _d_<sup>_∗_</sup> is minimax (in one of the above senses: minimax, sharp asympotically minimax or rate minimax)? It is obvious that in order to do this we need to bound _R_ Minimax from below. Indeed, if we prove the minimax lower bound:


then we can assert

137

1. minimaxity if _ℓn_ = _un_ for every _n_ .

2. sharp asymptotic minimaxity if _un/ℓn →_ 1 as _n →∞_ .

3. rate minimaxity if _un/ℓn_ = _O_ (1) as _n →∞_ .

Of course the key to doing this is to be able to prove minimax lower bounds (i.e., bounds of the form (237)) which we shall study now.

## **25.5 Minimax Lower Bounds**

There is basically only one technique for proving lower bounds on the minimax risk. This involves bounding the minimax risk from below by a Bayes risk. Indeed


As we indicated earlier, the Bayes risk _R_ Bayes( _w_ ) is a much more tractable object (compared to _R_ Minimax) and it has the exact expression (236).

Inequality (238) can be rewritten as


where the supremum is taken over all probability measures _w_ on Θ. On the other hand, it is easy to see that the minimax risk satisfies:


We thus have


Suppose now that


then we would have _R_ Minimax = sup _w R_ Bayes( _w_ ) which would imply that the only way to bound the minimax risk from below is via a Bayes risk for an appropriate prior _w_ . An infimum and a supremum obviously cannot always be interchanged; for example,


However, under some conditions, they can be interchanged. Theorems which guarantee the interchange are known as minimax theorems. There exist a variety of such minimax theorems in the literature one example of which is the following (known sometime as Kneser’s minimax theorem):

**Theorem 25.6.** _Let K be a convex subset of a vector space X and let L be a compact convex subset of a Hausdorff Topological Vector Space Y. Suppose f_ : _K × L →_ R _is a function such that_

_1. x �→ f_ ( _x, y_ ) _is convex for each fixed y ∈ L._

_2. y �→ f_ ( _x, y_ ) _is concave and continuous for each fixed x ∈ K._

_Then_


138

Potentially this theorem can be applied to verify (25.5). For this, we can take _K_ to be the class of all decision rules _d_ and _L_ to be the set of all probability measures _w_ on Θ. We would then need


to be convex in _d_ for each fixed _w_ and concave in _w_ for each fixed _d_ . The concavity in _w_ is alright but in order to ensure convexity in _d_ , we need to switch to randomized decision rules and extend the notion of risk to randomized decision rules. In order to verify the compactness assumptions, one needs to put a topology on the space of all probability measures on Θ. These can be done in quite some generality but the details are quite involved. You can see Le Cam and Yang [15] or Le Cam [14] for full details.

To summarize this section, the inequality (238) is always true. Also usually, _R_ Minimax = sup _w R_ Bayes( _w_ ) so (238) is really the only way of obtaining minimax lower bounds. Because of the exact expression (236) for the Bayes risk, we have


We shall see many examples of (239) in the sequel. A simple example is the following where we can use (239) to prove exact minimaxity.

**Example 25.7** (Multivariate Normal Model) **.** _Consider the problem of estimating θ ∈_ R<sup>_n_</sup> _from X ∼ Nn_ ( _θ, In_ ) _under loss_


_In this case, the parameter space is_ Θ = R<sup>_n_</sup> _. The estimator d_ ( _X_ ) = _X has risk equal to 1. It turns out that this is the minimax risk over_ Θ _. To see this, let w to be the normal distribution on_ R<sup>_n_</sup> _with mean vector µ and covariance matrix τ_<sup>2</sup> _In. The Bayes risk R_ Bayes( _w_ ) _can then be explicitly calculated. To see this, note that the posterior distribution is given by_


_so that_


_This gives_


_Letting τ →∞, we obtain R_ Minimax _≥_ 1 _. Because the supremum risk of X over_ R<sup>_n_</sup> _is at most_ 1 _, this proves that X is minimax._

---

[← 24 Lecture 24](25-24-lecture-24.md) · [Up: contents](index.md) · [26 Lecture 26 →](27-26-lecture-26.md)
