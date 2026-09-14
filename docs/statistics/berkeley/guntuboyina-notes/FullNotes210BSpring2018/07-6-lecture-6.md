---
title: 6 Lecture 6
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Lecture 6

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This lecture was delivered by Max Rabinovich. He made some changes to the notes (his modified notes are in the folder).

## **6.1 Proof of the Sauer-Shelah-Vapnik-Chevronenkis Lemma**

This section contains the proof of Lemma 5.6. The proof uses an idea called _downshifting_ .

Fix a Boolean class _F_ with VC dimension _D_ and also fix _n ≥_ 1 and _x_ 1 _, . . . , xn_ . To simplify notation, let us denote the set _F_ ( _x_ 1 _, . . . , xn_ ) by ∆. Observe first that the set ∆can be represented by a Boolean _n × N_ matrix where _N_ := _|_ ∆ _|_ . Indeed, every element of ∆is an element of _{_ 0 _,_ 1 _}_<sup>_n_</sup> ; so write this element as a column in a matrix; append all the columns corresponding to the different elements to form an _n × N_ matrix all of whose columns are distinct. In the proof of Lemma 5.6, we will use both these representations of ∆: as a subset of _{_ 0 _,_ 1 _}_<sup>_n_</sup> and also as a Boolean _n × N_ matrix.

For a subset _S_ of _{x_ 1 _, . . . , xn}_ , let ∆ _S_ denote the _|S| × N_ submatrix of ∆formed by taking only the rows of ∆corresponding to _S_ . For example, if _S_ := _{x_ 1 _, x_ 5 _, x_ 8 _}_ , then ∆ _S_ is the 3 _× N_ submatrix of ∆consisting of only the first, fifth and eighth rows of ∆.

28

Note that a subset _S_ of _{x_ 1 _, . . . , xn}_ is shattered by _F_ if and only if every element of _{_ 0 _,_ 1 _}_<sup>_|S|_</sup> appears as a column of ∆ _S_ . Because the VC dimension of _F_ is _D_ , the number of subsets of _{x_ 1 _, . . . , xn}_ that can be shattered by _F_ is clearly at most


We therefore have to show that the number of columns of ∆is atmost the number of subsets of _{x_ 1 _, . . . , xn}_ that are shattered by _F_ . We can isolate this into the following result which applies only to Boolean matrices.

**Result 6.1.** _Let_ ∆ _denote a n × N matrix with Boolean entries all of whose columns are distinct. Say that a subset S of {_ 1 _, . . . , n} is shattered by_ ∆ _if every element of {_ 0 _,_ 1 _}_<sup>_|S|_</sup> _appears as a column of_ ∆ _S (the empty set is always shattered). Let S_ (∆) _denote the number of subsets of {_ 1 _, . . . , n} that are shattered by_ ∆ _. Then_


_Proof of Result 6.1._ The proof follows an idea called _downshifting_ . Pick an arbitrary row of the matrix ∆, say the first row. Change each 1 in that row of ∆to 0 unless the change would create a column already present in ∆. This will create a new Boolean matrix, call it ∆<sup>_′_</sup> , all of whose columns are distinct. This operation is called downshifting. I claim that


This claim is the key component of the proof. Once this is established, the rest of the proof is immediate.

To prove (35), it is enough to show that whenever a subset _S_ of _{_ 1 _, . . . , n}_ is **not** shattered by ∆, it is not shattered by ∆<sup>_′_</sup> as well. This means that there will be fewer subsets shattered by ∆<sup>_′_</sup> compared to ∆ which implies (35). So let us fix a subset _S_ that is not shattered by ∆. _S_ is a subset of the rows of ∆. If _S_ does not contain the first row, then we have nothing to do because ∆<sup>_′_</sup> and ∆are identical in all rows except the first. So assume that 1 _∈ S_ . In fact, assume, purely for notational simplicity, that _S_ = _{_ 1 _,_ 2 _,_ 3 _,_ 4 _}_ .

Because _S_ is not shattered by ∆, there exists an element _u ∈{_ 0 _,_ 1 _}_<sup>4</sup> that is not present in ∆ _S_ . If _u_ 1 = 1, then it is clear that _u_ is not present in ∆<sup>_′_</sup> _S_<sup>aswellbecausethedownshiftingoperationwhichcreated∆</sup><sup>_′_from</sup> ∆cannot create new ones. So let us assume that _u_ 1 = 0 and write _u_ = (1 _, v_ ). The fact that _u_ is not in ∆ _S_ means that an element of the form (0 _, v_ ) is not present as a column in ∆ _S_ . This would then mean that (1 _, v_ ) is not present in ∆<sup>_′_</sup> _S_<sup>.Ifnot,then∆</sup><sup>_′_wouldincludeacolumnoftheform(1</sup><sup>_, v, x_).Butthen∆would</sup> have to include the column (1 _, v, x_ ) as well. But if ∆did have (1 _, v, x_ ), then it would have been converted to (0 _, v, x_ ) by the downshifting operation because (0 _, v, x_ ) is not alredy present as a column in ∆to prevent this shifting. This completes the proof of (35).

Now, consider ∆<sup>_′_</sup> . Again, pick an arbitrary row and perform downshifting on ∆<sup>_′_</sup> . Repeat this procedure of picking an arbitrary row and performing downshifting until we get a matrix that cannot be altered by further downshifts. Call this matrix ∆<sup>_∗_</sup> . Repeated application of (35) will imply that _S_ (∆<sup>_∗_</sup> ) _≤S_ (∆). The proof will now be completed by showing that _N ≤S_ (∆<sup>_∗_</sup> ). To see this, consider the first column of ∆<sup>_∗_</sup> and let _S_ be the indices among _{_ 1 _, . . . , n}_ for which there is a 1 in the first column of _S_<sup>_∗_</sup> . I claim that _S_ is shattered by ∆<sup>_∗_</sup> . To see this, assume that _S_ is non-empty because empty sets are always shattered. For notational simplicity, assume that _S_ = _{_ 1 _,_ 2 _}_ . We need to show that all elements in _{_ 0 _,_ 1 _}_<sup>2</sup> appear as columns in ∆<sup>_∗_</sup> _S_<sup>.</sup> There are only four elements in _{_ 0 _,_ 1 _}_<sup>2</sup> : (1 _,_ 1) _,_ (1 _,_ 0) _,_ (0 _,_ 1) and (0 _,_ 0). Obviously (1 _,_ 1) appears in the first column of ∆<sup>_∗_</sup> _S_<sup>.(1</sup><sup>_,_0)shouldalsoappearsomewherebecauseotherwise,itshouldbepossibletoalter∆</sup><sup>_∗_by</sup> downshifting. Similarly for (0 _,_ 1) and (0 _,_ 0). The proof is complete.

As mentioned previously, Result 6.1 almost gives proves Lemma 5.6. The only thing remaining is to argue that


To see this, let _B_ have the Binomial distribution corresponding to _n_ tosses with probability of success 1 _/_ 2. Then the left hand side above equals


29

The function _I{B ≤ D}_ is bounded from above by ( _D/n_ )<sup>_B−D_</sup> which gives


because 1 + ( _D/n_ ) _≤ e_<sup>_D/n_</sup> . The proof of Lemma 5.6 is now complete.

## **6.2 Covering and Packing Numbers**

As mentioned before, chaining gives much better bounds for _Rn_ ( _F_ ( _x_ 1 _, . . . , xn_ )) compared to the simple bound of Proposition 5.2. In order to discuss chaining, we need to be familiar with the notions of covering and packing numbers.

Let _T_ be a set equipped with a pseudometric _d_ . A pseudometric satisfies (a) _d_ ( _x, x_ ) = 0 for all _x ∈ T_ , (b) _d_ ( _x, y_ ) = _d_ ( _y, x_ ), and (c) _d_ ( _x, z_ ) _≤ d_ ( _x, y_ ) + _d_ ( _y, z_ ) for all _x, y, z_ . If, in addition, it also satisfies _d_ ( _x, y_ ) _>_ 0 for _x̸_ = _y_ , then _d_ ( _·, ·_ ) becomes a metric. We shall need to work with pseudometrics because the function:


is usually not a metric over _F_ (because it only depends on the values of functions in _F_ at _x_ 1 _, . . . , xn_ ). But this is a valid pseudometric.

**Definition 6.2** (Covering Numbers) **.** _For a subset F of T and δ >_ 0 _, the δ-covering number of F is denoted by NT_ ( _δ, F, d_ ) _and is defined as the smallest number of closed δ-balls needed to cover F . In other words, NT_ ( _δ, F, d_ ) _is the smallest N for which there exist points t_ 1 _, . . . , tN ∈ T with_ min1 _≤i≤N d_ ( _t, ti_ ) _≤ δ for each t ∈ F . The set of centers {ti} is called a δ-net for F . The logarithm of NT_ ( _δ, F, d_ ) _is called the δ-metric entropy of F ._

**Remark 6.1.** _Note that the centers t_ 1 _, . . . , tN are not constrained to be in F . This is related to the presence of the subscript T in the definition NT_ ( _δ, F, d_ ) _of the covering numbers of F . If we regard F as a metric space in its own right, not just as a subset of T , then the covering numbers NF_ ( _δ, F, d_ ) _might be larger because the centers ti would then be forced to lie in F . It is an easy exercise to prove that NF_ (2 _δ, F, d_ ) _≤ NT_ ( _δ, F, d_ ) _and the extra factor of_ 2 _would usually be of little consequence._

If _NT_ ( _δ, T, d_ ) _< ∞_ for every _δ >_ 0, we say that _T_ is totally bounded.

The notion of covering numbers is closely related to that of packing numbers which are defined next.

**Definition 6.3.** _For δ >_ 0 _, the δ-packing number of F is defined as the largest N for which there exist points t_ 1 _, . . . , tN ∈ F with d_ ( _ti, tj_ ) _> δ for every i̸_ = _j (these points t_ 1 _, . . . , tN are said to be δ-separated). The δ-packing number will be denoted by M_ ( _δ, F, d_ ) _. x_

The following result shows that covering and packing numbers are closely related to each other.

**Lemma 6.4.** _For every δ >_ 0 _, we have_


_Proof._ For the first inequality in (43), let _t_ 1 _, . . . , tM ∈ F_ be maximal set of _δ_ -separated points in _F_ with _M_ = _M_ ( _δ, F, d_ ). Because of the maximality, every other point of _F_ is within _δ_ of one of the points _t_ 1 _, . . . , tM_ . This means that _t_ 1 _, . . . , tM_ is a _δ_ -net for _F_ so that _NF_ ( _δ, F, d_ ) _≤ M_ and this proves the first inequality in (43).

For the second inequality, again let _t_ 1 _, . . . , tM ∈ F_ be maximal set of _δ_ -separated points in _F_ with _M_ = _M_ ( _δ, F, d_ ). Now if one tries to cover _F_ by closed balls of radius _δ/_ 2, it is clear that each ball can at

30

most contain one of the points _t_ 1 _, . . . , tM_ . This because the distance between any two points _ti_ and _tj_ is strictly larger than _δ_ while the diameter of a _δ/_ 2 ball is at most _δ_ . Therefore the number of closed _δ/_ 2-balls required to cover _F_ is at least _M_ which proves the second inequality.

The third inequality is trivial.

Below we see some examples where explicit bounds for covering/packing numbers are possible.

**Proposition 6.5.** _Suppose ∥·∥ denotes any norm in_ R<sup>_k_</sup> _. For example, it might be the usual Euclidean norm or the ℓn norm, ∥x∥_ 1 :=<sup>�</sup><sup>_k_</sup> _i_ =1<sup>_|xi|.Let_</sup>


_Then, for every ϵ >_ 0 _, we have_


_where d denotes the metric corresponding to the norm ∥·∥._

_Proof._ Let _x_ 1 _, . . . , xN_ denote any set of points in _BR_ that is _ϵR_ -separated i.e., _∥xi − xj∥ > ϵR_ for all _i̸_ = _j_ . Then the closed balls


for _i_ = 1 _, . . . , N_ are disjoint. Moreover, all these balls _B_ ( _xi, ϵR/_ 2) are contained in _BR_ + _ϵR/_ 2 (the ball of radius _R_ + _ϵR/_ 2 centered at the origin). As a result,


where Vol denotes volume (Lebesgue measure). If we let Λ denote the volume of the unit ball _B_ 1, then the above inequality becomes


which immediately proves (37).

The argument used above to prove (37) is known as the **volumetric** argument because it is based on a volume comparison.

We shall consider covering/packing numbers of some function classes. Loosely, function classes can be categorized into two groups: parametric classes and nonparametric classes. The _ϵ_ -covering numbers of parametric classes will be of the order _ϵ_<sup>_−k_</sup> for some integer _k_ while the _ϵ_ -covering numbers of nonparametric classes will be of the form exp( _∼ ϵ_<sup>_−k_</sup> ) for some _k_ . This reflects the fact that the nonparametric classes will be much larger compared to parametric classes.

The following proposition gives an example of a parametric class of functions. Note that when _D_ and _∥_ Γ _∥Q_ below are constants, the covering number bound given by the result below is of the form _ϵ_<sup>_−k_</sup> .

**Proposition 6.6.** _Let_ Θ _⊆_ R<sup>_k_</sup> _be a non-empty bounded subset with Euclidean diameter D and let F_ := _{fθ_ : _θ ∈_ Θ _} be a class of functions on X indexed by_ Θ _such that for some nonnegative function_ Γ : _X →_ R _, we have_


_for all x ∈X and θ_ 1 _, θ_ 2 _∈_ Θ _. Here ∥·∥ denotes the usual Euclidean norm on_ R<sup>_k_</sup> _._

31

_Fix a probability measure Q on X and let d denote the pseudometric on F defined by_


_Then, for every ϵ >_ 0 _,_


_Proof._ The condition (46) implies that for every _θ_ 1 _, θ_ 2 _∈_ Θ, we have


As a result, every _ϵ_ -separated subset _F_ in the metric _d_ is automatically an _ϵ/ ∥_ Γ _∥Q_ separated subset of Θ. Consequently


To bound the Euclidean packing number, we shall use the assumption that Θ has diameter _≤ D_ so that Θ is contained in _B_ ( _a, D_ ) := _{x ∈_ R<sup>_k_</sup> : _∥x − a∥≤ D}_ for every _a ∈_ Θ. As a result


To bound the right hand side above, we use Proposition 7.6 (note that we can _a_ = 0 above because balls of the same radius will have the same packing numbers regardless of their center). This gives


which finishes the proof of Proposition 7.8.

The most standard examples of nonparametric function classes are smoothness classes. These will have covering numbers that are exponential in 1 _/ϵ_ . We shall first introduce smoothness classes and describe their covering numbers in one dimension and then generalize to multiple dimensions. For proofs of the covering number results, see Dudley [6, Chapter 8].

Fix _α >_ 0. Let _β_ denote the largest integer that is **strictly** smaller than _α_ . For example, if _α_ = 5, then _β_ = 4 and if _α_ = 5 _._ 2, then _β_ = 5.

The class _Sα_ is defined to consist of functions _f_ on [0 _,_ 1] that satisfy all the following properties:

1. _f_ is continuous on [0 _,_ 1].

2. _f_ is differentiable _β_ times on (0 _,_ 1).

3. _|f_<sup>(</sup><sup>_k_)</sup> ( _x_ ) _| ≤_ 1 for all _k_ = 0 _, . . . , β_ and _x ∈_ [0 _,_ 1] where _f_<sup>(0)</sup> ( _x_ ) := _f_ ( _x_ ).

4. _|f_<sup>(</sup><sup>_β_)</sup> ( _x_ ) _− f_<sup>(</sup><sup>_β_)</sup> ( _y_ ) _| ≤|x − y|_<sup>_α−β_</sup> for all _x, y ∈_ (0 _,_ 1).

Let _ρ_ denote the supremum metric on _Sα_ defined by


32

**Theorem 6.7.** _There exist positive constants ϵ_ 0 _, C_ 1 _and C_ 2 _denpending on α alone such that for all ϵ >_ 0 _, we have_


Thus the _ϵ_ -metric entropy (logarithm of the _ϵ_ -covering number) of the smoothness class _Sα_ in one dimension grows as _ϵ_<sup>_−_1</sup><sup>_/α_</sup> . Here _α_ denotes the degree of smoothness (the higher _α_ is, the smoother the functions in _Sα_ ). When _α_ = 1, the class _Sα_ consists of all bounded 1-Lipschitz functions on [0 _,_ 1].

This result has a direct generalization to multidimensions. As before, _α >_ 0 and _β_ is the largest integer that is strictly smaller than _α_ .

For a vector _p_ = ( _p_ 1 _, . . . , pd_ ) consisting of nonnegative integers _p_ 1 _, . . . , pd_ , let _⟨p⟩_ := _p_ 1 + _· · ·_ + _pd_ . Let


The class _Sα,d_ is defined to consist of all functions _f_ on [0 _,_ 1]<sup>_d_</sup> that satisfy:

1. _f_ is continuous on [0 _,_ 1]<sup>_d_</sup> .

2. All partial derivatives _D_<sup>_p_</sup> of _f_ exist on (0 _,_ 1)<sup>_d_</sup> for _⟨p⟩≤ β_ .

3. _|D_<sup>_p_</sup> ( _x_ ) _| ≤_ 1 for all _p_ with _⟨p⟩≤ β_ and _x ∈_ [0 _,_ 1]<sup>_d_</sup> .

4. _|D_<sup>_p_</sup> _f_ ( _x_ ) _− D_<sup>_p_</sup> _f_ ( _y_ ) _| ≤|x − y|_<sup>_α−β_</sup> for all _p_ with _⟨p⟩_ = _β_ and _x, y ∈_ (0 _,_ 1)<sup>_d_</sup> .

Once again, we consider the supremum metric defined by _ρ_ ( _f, g_ ) := sup _x∈_ [0 _,_ 1] _d |f_ ( _x_ ) _− g_ ( _x_ ) _|_ .

**Theorem 6.8.** _There exist positive constants C_ 1 _and C_ 2 _depending only on α and the dimension d such that for all ϵ >_ 0 _, we have_


Thus the metric entropy of a smoothness class of functions with smoothness _α_ and dimension _d_ scales as _ϵ_<sup>_−d/α_</sup> . This grows as _d_ increases and goes down as _α_ increases.

---

[← 5 Lecture 5](06-5-lecture-5.md) · [Up: contents](index.md) · [7 Lecture 7 →](08-7-lecture-7.md)
