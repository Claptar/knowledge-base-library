---
title: 11 Lecture 11
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 11 Lecture 11

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For Boolean function classes _F_ , we have seen that the VC dimension gives useful upper bounds on covering numbers:


What happens for function classes that are not Boolean? We shall see today that there exist two notions of combinatorial dimension for general function classes which allow control of covering numbers via bounds similar to (83). These are the notions of _VC subgraph dimension_ and _fat shattering dimension_ which we shall go over today.

## **11.1 VC Subgraph Dimension**

The VC subgraph dimension of _F_ is simply the VC dimension of the Boolean class obtained by taking the indicators of the subgraphs of functions in _F_ . To formally define this, let us first define the notion of subgraph of a function.

**Definition 11.1** (Subgraph) **.** _For a function f_ : _X →_ R _, its subgraph sg_ ( _f_ ) _is a subset of X ×_ R _that is defined as_


_In other words, sg_ ( _f_ ) _consists of all points that lie below the graph of the function f ._

We can now define the VC subgraph dimension of _F_ as:

**Definition 11.2** (VC Subgraph Dimension) **.** _The VC subgraph dimension of F is defined as the VC dimension of the Boolean class {Isg_ ( _f_ ) : _f ∈F}. We shall denote this by just V C_ ( _F_ ) _._

The VC subgraph dimension can be related to covering numbers in the same way as (83). This is done in the following result.

**Theorem 11.3.** _Suppose F is a class of functions with envelope F . Let the VC-subgraph dimension of F be equal to D. Then_


_where c_ 1 _and c_ 2 _are universal positive constants._

_Proof._ The idea is to relate the _L_<sup>2</sup> ( _Q_ ) norm between two functions in _F_ to an _L_<sup>2</sup> norm between their subgraphs. Fix _f, g ∈F_ and write


where we used the fact that _|f_ ( _x_ ) _− g_ ( _x_ ) _| ≤_ 2 _F_ ( _x_ ) (this is true because _F_ is the envelope of _F_ ). We now use the fact that for every two real numbers _a_ and _b_ , we have the identity


56

This gives


We have thus proved that


where _Q_<sup>_′_</sup> is the probability measure on _X ×_ R whose density with respect to _Q × Leb_ is proportional to


It is routine to deduce from (85) that


To bound the right hand side, we simply use the earlier result for Boolean classes (see (83)). This completes the proof of Theorem 11.3.

The following is an immediate corollary of Theorem 11.3 and our main bound on the Expected suprema of empirical processes.

**Corollary 11.4.** _If F has envelope F and VC subgraph dimnension D, then_


_Proof._ Our main bound on the expected suprema of empirical processes gives


and we bound _J_ ( _F, F_ ) (using Theorem 11.3) as


which completes the proof of Corollary 11.4.

57

**Example 11.5.** _In the last lecture, I remarked that_


_where mθ_ ( _x_ ) := _I{θ −_ 1 _≤ x ≤ θ_ + 1 _}. I gave a partial proof of this fact in the last class. Complete this proof by proving that the function-class_


_has finite VC subgraph dimension (≤_ 3 _??)._

Let us now look at a reformulation of the VC subgraph dimension. This defines the dimension directly in terms of the class _F_ without going to subgraphs. This reformulation will also make clear the connection to fat shattering dimension.

We say that a subset _{x_ 1 _, . . . , xn}_ of _X_ is subgraph-shattered by _F_ if there exist real numbers _t_ 1 _, . . . , tn_ such that for every subset _S ⊆{_ 1 _, . . . , n}_ , there exists _f ∈F_ with


Note that (86) is equivalent to


In words, we say that _{x_ 1 _, . . . , xn}_ is subgraph-shattered by _F_ if there exist _levels t_ 1 _, . . . , tn_ such that for every subset _S ⊆{_ 1 _, . . . , n}_ , there exists a function _f_ which goes **under** the level for each _xs, s ∈ S_ and **strictly over** the level for _xs, s ∈/ S_ .

The VC subgraph dimension _V C_ ( _F_ ) is defined as the maximum cardinality of a finite subset of _X_ that is subgraph shattered by _F_ .

Let us now describe a potential problem with using the VC subgraph dimension to control covering numbers. Let _M_ denote the class of all nondecreasing functions _f_ : R _→_ [ _−_ 1 _,_ 1] i.e., _M_ consists of all nondecreasing functions on R that are bounded by 1. It turns out then that


It is also easy to see that the VC-subgraph dimension of _M_ equals _∞_ (i.e., for every _n ≥_ 1, there exists a finite subset of R that is subgraph shattered by _M_ ). Therefore, the notion of VC-subgraph dimension is not useful here and Theorem 11.3 does not give anything meaningful for this class _M_ . It is actually possible to prove (88) using the notion of fat shattering dimension which is discussed next.

## **11.2 Fat Shattering Dimension**

Fat Shattering is a scale sensitive notion of dimension. Specifically, fat shattering dimension is actually a function on (0 _, ∞_ ) i.e., it is defined for each _ϵ >_ 0. We shall denote this by fat _F_ ( _ϵ_ ) and is defined in the following way.

**Definition 11.6** ( _ϵ_ -shattering) **.** _We say that a subset {x_ 1 _, . . . , xn} of X is ϵ-shattered by F if there exist real numbers t_ 1 _, . . . , tn such that for every S ⊆{_ 1 _, . . . , n}, there exists a function f ∈F such that_


58

In words, we say that _{x_ 1 _, . . . , xn}_ is subgraph-shattered by _F_ if there exist _levels t_ 1 _, . . . , tn_ such that for every subset _S ⊆{_ 1 _, . . . , n}_ , there exists a function _f_ which goes **under** the level for each _xs, s ∈ S_ and **exceeds by** _ϵ_ the level for _xs, s ∈/ S_ . Note that the only difference between the notion of _ϵ_ -shattering and the notion of subgraph-shattering from the previous subsection is that the words “strictly over” are replaced by “exceeds by _ϵ_ ”.

**Definition 11.7** (Fat Shattering Dimension) **.** _For ϵ >_ 0 _, the fat shattering dimension_ fat _F_ ( _ϵ_ ) _is defined as the maximum cardinality of a finite subset of X that is ϵ-shattered by F._

It is clear that fat _F_ ( _ϵ_ ) is a decreasing function of _ϵ_ . In fact, it can be shown (exercise) that


where _V C_ ( _F_ ) above refers to VC subgraph dimension. This inequality means, in particular, that fat _F_ ( _ϵ_ ) is always bounded from above by _V C_ ( _F_ ). Another easy fact is that when _F_ is Boolean, then fat _F_ ( _ϵ_ ) equals _V C_ ( _F_ ) for every 0 _< ϵ ≤_ 1.

Recall now the class _M_ from the last subsection consisting of all nondecreasing functions _f_ : R _→_ [ _−_ 1 _,_ 1]. It was mentioned before that the VC subgraph dimension of _M_ is infinity. We shall show now that fat _M_ ( _ϵ_ ) is finite for every _ϵ >_ 0 and in fact


In fact, the above fat shattering dimension bound holds for the larger class of all functions _f_ : R _→_ R whose variation is bounded by 2. This is proved in the following result. Recall that the variation of a function _f_ : R _→_ R is defined by


**Lemma 11.8.** _Fix V >_ 0 _and let F denote the class of all functions f_ : R _→_ R _with ∥f ∥T V ≤ V . Then_


_Proof._ Fix _ϵ >_ 0. Let us first prove that


For this, _{x_ 1 _, . . . , xn}_ be _ϵ_ -shattered by _F_ . We shall show then that _n_ cannot be larger than the right hand side of (90) which will prove (90). Note first that because _{x_ 1 _, . . . , xn}_ are _ϵ_ -shattered, there exist real numbers _t_ 1 _, . . . , tn_ which satisfy the condition in the definition of _ϵ_ -shattering. This means, in particular, that there exist two functions _f_ 1 and _f_ 2 in _F_ which satisfy the following:


and


Now let _f_ = ( _f_ 1 _− f_ 2) _/_ 2. The conditions above imply together that


59

which immediately implies that


On the other hand,


Combining the above two inequalities, we obtain ( _n −_ 1) _ϵ ≤ V_ which implies (90) (note that _n_ has to be an integer which allows us to put integer part around _V/ϵ_ ).

We now show that fat _F_ ( _ϵ_ ) is larger than or equal to the right hand side of (90). For this, let _d_ = _⌊V/ϵ⌋_ . Consider any set of _d_ points _y_ 1 _< · · · < yd_ . These form _d_ + 1 intervals _Ij_ := [ _yj, yj_ +1) for _j_ = 1 _, . . . , d −_ 1 and _I_ 0 := ( _−∞, y_ 1] and _Id_ := [ _yd, ∞_ ). Let _G_ consist of the 2<sup>_d_+1</sup> functions from R to _{_ 0 _, ϵ}_ that are piecewise constant on each of the intervals _I_ 0 _, . . . , Id_ . Let _{x_ 1 _, . . . , xd_ +1 _}_ be any finite set obtained by picking one point from each of the _d_ + 1 intervals _I_ 0 _, . . . , Id_ . It is then clear that _{x_ 1 _, . . . , xd_ +1 _}_ is _ϵ_ -shattered by _G_ . Further, the variation of every function in _G_ is atmost _dϵ_ = _ϵ⌊V/ϵ⌋≤ V_ . Thus _F_ shatters _{x_ 1 _, . . . , xd_ +1 _}_ which means


This completes the proof of Lemma 11.8.

Let us now describe a result which bound covering numbers in terms of the fat-shattering dimension fat _F_ ( _ϵ_ ) _, ϵ >_ 0. This is the following theorem due to Mendelson and Vershynin [16].

**Theorem 11.9** (Mendelson-Vershynin) **.** _Suppose F is a class of functions that are uniformly bounded by_ 1 _. Then there exist a universal positive constant C ≥_ 1 _such that_


Let us see what this result gives for class _M_ of all nondecreasing functions _f_ : R _→_ [ _−_ 1 _,_ 1]. Every function in this class has variation at most 2 and thus Lemma 11.8 implies that


This, together with Theorem 11.9, allows us to deduce that


Note that this result is weaker compared to (88) by a factor of log(2 _/ϵ_ ) in the exponent. We can now ask if it is possible to derive (88) via the fat shattering dimension. This is possible if the bound (91) can be improved to exp( _C_ fat _F_ ( _ϵ/C_ )). Note that this cannot be done in general. For example, when _F_ is Boolean with finite VC dimension, then fat _F_ ( _ϵ_ ) = _V C_ ( _F_ ) for every 0 _< ϵ ≤_ 1 and in this case, one obviously cannot replace 2 _/ϵ_ by a constant in (91). However, Rudelson and Vershynin [21] have showed that under a technical regularity assumption on fat _F_ ( _ϵ_ ) (which rules out the case when _F_ is Boolean with finite VC dimension), it is indeed possible to improve Theorem 11.9. This result is given below.

**Theorem 11.10** (Rudelson-Vershynin) **.** _Suppose F is a class of functions. Suppose a >_ 2 _and a decreasing function v_ : (0 _, ∞_ ) _→_ (0 _, ∞_ ) _are such that_


_for all ϵ >_ 0 _. Then_


_for every ϵ >_ 0 _. C as usual is a universal constant._

60

Note that the regularity condition (93) rules out situations such as the case when _v_ ( _ϵ_ ) is constant. Also notice that there is no explicit boundedness assumption on the functions in _F_ ; this is hidden in the regularity condition.

Let us now show that Theorem 11.10 does indeed imply the result (88) for the class _M_ of nondecreasing functions that are constrained to take values in [ _−_ 1 _,_ 1]. Indeed, for this class we first have (92). Also because the functions in _M_ are constrained to take values in [ _−_ 1 _,_ 1], the fat shattering dimension will be zero for large _ϵ_ . In fact, it is easy to see that fat _M_ ( _ϵ_ ) = 0 for _ϵ ≥_ 3. This, along with (92), implies that


We can therefore apply Theorem 11.10 with _v_ ( _ϵ_ ) := 5 _/ϵ_ . The condition _v_ ( _aϵ_ ) _≤ v_ ( _ϵ_ ) _/_ 2 is easily seen to be satisfied with _a_ = 3. It is straightforward then to show that inequality (88) is a consequence of (94).

---

[← 10 Lecture 10](11-10-lecture-10.md) · [Up: contents](index.md) · [12 Lecture 12 →](13-12-lecture-12.md)
