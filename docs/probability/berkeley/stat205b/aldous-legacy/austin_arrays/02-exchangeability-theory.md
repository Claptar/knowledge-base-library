---
title: Exchangeability Theory
source: https://www.stat.berkeley.edu/~aldous/205B/austin_arrays.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/austin_arrays.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Exchangeability Theory

**Source:** [`austin_arrays.pdf`](https://www.stat.berkeley.edu/~aldous/205B/austin_arrays.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **1 Exchangeable sequences and arrays**

#### **Some notation**

- N := _{_ 1 _,_ 2 _, . . .}_ ;

- for _n ∈_ N, [ _n_ ] := _{_ 1 _,_ 2 _, . . . , n}_ ;

- Sym( _n_ ) is the group of all permutations of [ _n_ ] and Sym(N) is the group of all permutations of N;

- for any set _A_ and _k ≥_ 1, _A_<sup>(</sup><sup>_k_)</sup> is the set of subsets of _A_ of size _k_ , and _A_<sup>(</sup><sup>_≤k_)</sup> :=<sup>�</sup><sup>_k_</sup> _j_ =0<sup>_A_(</sup><sup>_j_).</sup>

- if _E_ is a standard Borel space<sup>1</sup> , then Pr _E_ is the space of all Borel probability measures on _E_ ;

- if _E_ and _E_<sup>_′_</sup> are measurable spaces, _µ_ is a probability measure on _E_ , and _f_ : _E −→ E_<sup>_′_</sup> is measurable, then _f∗µ_ denotes the pushforward measure:

   - _f∗µ_ ( _A_ ) := _µ_ ( _f_<sup>_−_1</sup> ( _A_ )) _∀A ⊆_ measurable _E_ ;

- a background probability space will be denoted by (Ω _, F,_ P), with expectation denoted E (although in keeping with convention among probabilists, Ω will usually be kept hidden in the background);

- if _X_ and _Y_ are r.v.s valued in the same space, then _X_ =<sup>d</sup> _Y_ if they have the same distribution.

#### **Objects of the theory**

Exchangeability theory is concerned with families of random variables whose joint distribution is unchanged when they are permuted by some group of permutations.

1Meaning it is isomorphic, as a measure space, to a Borel subset of a complete, separable metric space with the Borel _σ_ -algebra. This assumption is needed when working with conditional probabilities. It covers all ‘nice’ spaces that one meets in practice.

3

For particular groups of permutations, it seeks to describe all possible joint distributions that have this property. Of course, if the index set is a discrete group Γ, the random variables are indexed by Γ, and they are permuted by the regular representation, then this task encompasses the whole of ergodic theory. In that case a complete description is generally impossible. But in some other cases, in which the relevant group of permutations is ‘very large’ relative to the indexing set, one can deduce rather more complete results on the distributions of such families than in general ergodic theory.

Basic objects of the theory:

- **Exchangeable sequences:** Let _E_ be _{_ 0 _,_ 1 _}_ , R, or any other standard Borel space. A sequence of _E_ -valued random variables ( _Xn_ ) _n∈_ N is **exchangeable** if


Note that this is really an assertion about the measure _µ_ on _E_<sup>N</sup> which is the joint law of the r.v.s ( _Xn_ ): it is invariant under the action of Sym(N) on _E_<sup>N</sup> by the permutation of coordinates. When _E_ = _{_ 0 _,_ 1 _}_ these were studied by de Finetti in the 1930’s; for more general _E_ by Hewitt and Savage in the 1950’s.

- **Exchangeable arrays:** More generally, for any _k ≥_ 1 we can consider an array of _E_ -valued r.v.s ( _Xe_ ) _e∈_ N( _k_ ) indexed by size- _k_ subsets of N, and say it is **exchangeable** if ( _Xe_ ) _e_ =d ( _Xσ_ ( _e_ )) _e_ for any _σ ∈_ Sym(N), where if _e_ = _{n_ 1 _, . . . , nk}_ then _σ_ ( _e_ ) := _{σ_ ( _n_ 1) _, . . . , σ_ ( _nk_ ) _}_ . So now exchangeability is an assertion about the law _µ_ on _E_<sup>N(</sup><sup>_k_)</sup> . Exchangeable sequences are the case _k_ = 1. General arrays were studied by Hoover [Hoo79, Hoo82], Aldous [Ald81, Ald82, Ald85], Fremlin and Talagrand [FT85] and Kallenberg [Kal89, Kal92]. Important ideas were also suggested (though not published) by Kingman, who had previously studied random partitions with a similar symmetry and proved his related ‘paintbox’ theorem: see [Kin78b, Kin78a].

Recommended reading on basic exchangeability theory: the really essential reference is still [Ald85]. The recent textbook [Kal05] offers a more modern and definitive account (see Chapter 7 in particular). Three surveys with different emphases are [Aus08, DJ07, Ald]: the first two give special attention to the connection with limit objects for finite graphs.

4

#### **Why are these important?**

Exchangeable random structures are important because they are the natural output of sampling at random from discrete structures.

**Example 1** Most simply, for any _E_ and any probability measure _ν_ on _E_ , the product measure _ν_<sup>_⊗_N(</sup><sup>_k_)</sup> is always the law of an _E_ -valued exchangeable array.

**Example 2** Suppose now that _E_ is arbitrary and that _{ν_ 1 _, . . . , νm}_ is a finite set of probability measures on _E_ . Choose an _E_ -valued array ( _Xe_ ) _e∈_ N( _k_ ) as follows: first pick _ℓ ∈{_ 1 _,_ 2 _, . . . , m}_ uniformly at random, and then conditionally on this choose ( _Xe_ ) _e∈_ N( _k_ ) i.i.d. from _νℓ_ . (This clearly agrees with the previous example when _m_ = 1.)

**Example 3** Let _E_ = _{_ 0 _,_ 1 _}_ and let _G_ = ( _V, E_ ) be a finite graph, possibly with loops. Let ( _Vn_ ) _n∈_ N be a random sequence of vertices sampled independently from the uniform distribution on _V_ , and now define ( _Xe_ ) _e∈_ N(2) by letting


(so there is no additional randomness once the _Vn_ have been chosen). Note that in general the notation _ij_ stands for the unordered pair _{i, j}_ .

One can easily find ways to generalize these examples (for instance, how could Example 3 be made to give a random array with a different space _E_ ?). We will soon introduce a broad framework for discussing these. Remarkably, it turns out that once a suitably general notion of ‘sampling’ has been defined, it is the _only_ way one can produce an exchangeable sequence or array.

### **2 Statement of the Representation Theorem**

In order to generalize Examples 1–3 above, one must first observe that to construct a _k_ -set exchangeable random array, randomness can be introduced at any ‘level’ between 0 and _k_ . In order to make this formal, consider the **uniform random array** : this is a family of random variables ( _Ua_ ) _a⊆_ N _, |a|≤k_ which are i.i.d. U[0 _,_ 1]. Its law is simply the product of copies of Lebesgue measure on the space


5

Now consider also any measurable function


which is symmetric under the action of the permutation group Sym( _k_ ):

_f_ ( _x,_ ( _xi_ ) _i,_ ( _xij_ ) _ij, . . . , x_ [ _k_ ]) = _f_ ( _x,_ ( _xσ_ ( _i_ )) _i,_ ( _xσ_ ( _i_ ) _σ_ ( _j_ )) _ij, . . . , x_ [ _k_ ]) _∀σ ∈_ Sym( _k_ ) _._ Such a function will be referred to as **middle-symmetric** .

Then we may obtain an exchangeable random array as follows: let the _Ua_ for _a ⊂_ N, _|a| ≤ k_ be uniform i.i.d. as above, and set


This is well-defined owing to the middle-symmetry of _f_ .

**Definition 2.1** _This is the exchangeable random array_ **_directed by_** _f . We denote its law by_ Samp( _f_ ) _._

Let’s revisit the previous examples:

**Example 1** By abstract measure theory, any Borel probability measure _ν_ on _E_ is the pushforward of U[0 _,_ 1] under some measurable _f_ 0 : [0 _,_ 1] _−→ E_ : that is, law( _f_ 0) = _ν_ . So now let


This example is using only ‘level- _k_ randomness’.

**Example 2** Building on the above, let _fℓ_ : [0 _,_ 1] _−→ E_ be such that law( _fℓ_ ) = _νℓ_ for 1 _≤ ℓ ≤ m_ , and also let _P_ = ( _I_ 1 _, . . . , Im_ ) be a partition of [0 _,_ 1] into _m_ equal subintervals. Now let


This example is using the randomness from levels 0 and _k_ .

**Example 3** Finally, let _P_ = ( _Iv_ ) _v∈V_ be a partition of [0 _,_ 1] into _|V|_ -many equal subintervals, and now define


So this example (with _k_ = 2) is using the randomness from level 1.

6

**Theorem 2.2 (Representation Theorem for exchangeable arrays)** _Any exchangeable array_ ( _Xe_ ) _e∈_ N( _k_ ) _has law equal to_ Samp( _f_ ) _for some f as above._

This is due to de Finetti ( _k_ = 1, _E_ = _{_ 0 _,_ 1 _}_ ), Hewitt and Savage ( _k_ = 1), Hoover and separately Aldous ( _k_ = 2, different proofs), and Kallenberg (all _k_ ). (Aldous partly attributes his proof to Kingman.)

We will prove the cases _k_ = 1 and _k_ = 2. The latter already contains the main difficulties, except that the general case requires an induction on _k_ which needs some careful management. That will be left as an exercise, or see [Aus08].

### **3 A tool: the Noise-Outsourcing Lemma**

The following soft fact from measure theory provides a valuable tool for simplifying and clarifying the structures we will examine. It is treated in many standard probability texts; for instance, a more general version is given as Theorem 6.10 in Kallenberg [Kal02].

**Lemma 3.1 (Noise-Outsourcing lemma)** _If X, Y are r.v.s taking values in standard Borel spaces S and T , then (possibly after enlarging the background probability space) there are a r.v. U ∼_ U[0 _,_ 1] _and a Borel function f_ : _S ×_ [0 _,_ 1] _−→ T such that U is independent from X and_


In case _S_ is a one-point space, say _S_ = _{∗}_ , and _X_ is deterministic, this is just the assertion that any standard-Borel-valued r.v. has law equal to an image of U[0 _,_ 1]

### **4 Proof of de Finetti’s Theorem**

We will prove de Finetti’s Theorem in this section, and the Aldous-Hoover Theorem in the next.

7

Thus, suppose that _E_ is a standard Borel space and that ( _Xi_ ) _i_ is an exchangeable sequence of _E_ -valued r.v.s. We must find a Borel function _g_ : [0 _,_ 1] _×_ [0 _,_ 1] _−→ E_ such that


where _U_ and _Ui_ , _i ∈_ N, are i.i.d. U[0 _,_ 1].

**Obtaining conditional independence** The key to the proof is finding a coupling of ( _Xi_ ) _i_ to a new r.v. _Z_ (possibly after enlarging (Ω _, F,_ P)) such that:

(i) one still has exchangeability, now in the enhanced form


(so _Z_ is not moved by the permutation action);

(ii) the r.v.s _Xi_ are conditionally independent over _Z_ : this means that


for any finite _k_ and any _x_ 1, ..., _xk ∈ E_ . In terms of conditional expectations, this asserts that


for any bounded measurable functions _f_ 1 _, . . . , fk_ : _E −→_ R.

This coupling is obtained from a simple ‘duplication’ trick. Observe that exchangeability of ( _Xi_ ) _i_ implies also


whenever _γ_ : N _−→_ N is an _injection_ (not necessarily a permutation). This is because the distributions of these two arrays are determined by their finitedimensional marginals, and for any finite collection _i_ 1 _, i_ 2 _, . . . , im ∈_ N we can find a genuine permutation _σ_ : N _−→_ N such that _σ_ ( _ir_ ) = _γ_ ( _ir_ ) for all _r_ (but _σ_ and _γ_ differ elsewhere if necessary).

Now, of course, our previous choice of N as index set was rather arbitrary; we could have used, say, Z instead. But if we switch to indexing by Z, we now rediscover the original family ( _Xi_ ) _i∈_ N inside the new family ( _Xi_ ) _i∈_ Z, in the sense that

8

this sub-family has the same distribution as the N-indexed family that we started with. This is simply because we can let _γ_ : Z _−→_ Z be an injection with image equal to N and apply the reasoning above.

This completely trivial observation is important, because it provides a large collection of extra r.v.s ( _Xi_ ) _i∈_ Z _\_ N from which to synthesize the new r.v. _Z_ . Let N<sup>c</sup> := Z _\_ N. Letting _Z_ = ( _Xi_ ) _i∈_ Nc, a r.v. valued in _E_<sup>Nc</sup> , we will show that this has the desired properties.

To see property (i), observe that if _σ_ : N _−→_ N is any permutation, then we may define a permutation _σ_ ˜ : Z _−→_ Z to agree with _σ_ on N and to be the identity on N<sup>c</sup> , and now one has


where the equality of distributions in the middle follows from the exchangeability of the original sequence.

Property (ii) needs a deeper idea. By induction on _k_ it suffices to prove that


for any bounded measurable functions _f_ 1 _, . . . , fk_ : _E −→_ R, and this, in turn, is really asserting that


(i.e., if we condition _fk_ ( _Xk_ ) on _Z_ , _X_ 1,..., _Xk−_ 1, then no more information is retained about it than if we condition on _Z_ alone).

To prove this, let _F_ 1 be the _σ_ -algebra generated by _Z_ and _F_ 2 the _σ_ -algebra generated by ( _Z, X_ 1 _, . . . , Xk−_ 1). Then _F_ 1 _⊆F_ 2, and so the law of iterated conditional expectation gives


In particular, this implies that


9

with equality if and only if the functions themselves are equal. This is because, in Hilbert-space terms, conditional expectations are orthogonal projections.

Therefore we need only prove this equality of norms. However, recalling our definition of _Z_ , we have


Now let _τ_ : N _−→_ N be the injection


and observe that


Exchangeability applied to this _τ_ implies that


and hence


completing the proof of (ii).

**Finishing the proof** Now we need only the Noise-Outsourcing Lemma and some routine bookkeeping. That lemma gives a Borel function _g_<sup>_′_</sup> : [0 _,_ 1] _×_ [0 _,_ 1] _−→ E_ such that


for each _i_ , where the _Ui_ are i.i.d. U[0 _,_ 1], independent from _Z_ . The same function _g_<sup>_′_</sup> works for each _i_ , since exchangeability implies that all pairs ( _Z, Xi_ ) have the same distribution. Given this, the conditional independence over _Z_ proved in (ii) implies for the whole sequence that


Finally, another appeal to Lemma 3.1, this time in the simple case _|S|_ = 1, gives a Borel function _h_ : [0 _,_ 1] _−→ E_<sup>Nc</sup> such that _Z_ =<sup>d</sup> _h_ ( _U_ ) when _U ∼_ U[0 _,_ 1]. Substituting this into the above gives


10

where _U_ is independent from ( _Ui_ ) _i_ , and hence completes the proof with _g_ ( _x, y_ ) := _g_<sup>_′_</sup> ( _h_ ( _x_ ) _, y_ ). _2_

**Remark** Instead of constructing the new r.v. _Z_ as above, many proofs of de Finetti’s Theorem prove that the r.v.s _Xi_ ’s are conditionally independent over their own tail _σ_ -alegbra. Although possibly cleaner, this argument does not generalize so directly to the case of higher-dimensional arrays, so I have avoided it. _�_

#### **Finite sequences**

The analog of de Finetti’s Theorem does not hold for finite sequences. One can see that the proof given above makes important use of the infinitude of N, most obviously through the existence of injections _γ_ : N _−→_ N for which N _\ γ_ (N) is infinite.

A rather weaker characterization is possible for finite exchangeable sequences, however. Given a finite sequence **x** = ( _xi_ )<sup>_n_</sup> _i_ =1<sup>_∈En_, let</sup>


be its empirical distribution. Clearly _E_ is a Sym( _n_ )-invariant function _E_<sup>_n_</sup> _−→_ Pr _E_ . On the other hand, if _ν ∈_ Pr _E_ lies in the image of _E_ (meaning that it is a sum of _n_ equal-weight atoms, not necessarily distinct), then let _ν_<sup>(</sup><sup>_n_)</sup> be the uniform distribution on the finite set of sequences _E_<sup>_−_1</sup> _{ν}_ (that is, all sequences whose frequencies are given by _ν_ ).

**Proposition 4.1** _If µ is a_ Sym( _n_ ) _-invariant probability on E_<sup>_n_</sup> _, then_


_so µ is a mixture of the measures ν_<sup>(</sup><sup>_n_)</sup> _:_


This is an elementary calculation, and we omit the proof. However, it is worth knowing that this gives another approach to de Finetti’s Theorem. Given the finite exchangeable law


a fairly easy estimate can be used to compare it with the mixture of product measures


The difference between _ν_<sup>_⊗n_</sup> and _ν_<sup>(</sup><sup>_n_)</sup> is essentially that between sampling from a set of _n_ samples with and without replacement. (In the latter case, _ν_<sup>(</sup><sup>_n_)</sup> is the law of the classical **urn sequence** obtained by sampling without replacement from the set of atoms of _ν_ , possibly with some multiplicities.) For the first _k_ outcomes of this sample, this difference is small when the sample size _n_ is _≫ k_ . A simple quantitative estimate gives the following.

**Corollary 4.2** _If µ is a_ Sym( _n_ ) _-invariant probability on E_<sup>_n_</sup> _and µk is the marginal of µ on any k coordinates, then_


Letting _n −→∞_ and then _k −→∞_ yields another proof of de Finetti’s Theorem. See Section 1.2 of Kallenberg [Kal05] for more on these ideas, or Diaconis and Freedman [DF80] for better estimates that can be obtained given some extra restrictions on _E_ .

### **5 Proof of the Aldous-Hoover Theorem**

Now suppose ( _Xij_ ) _ij∈_ N(2) is an exchangeable random _E_ -valued array. Recall that for us _ij ∈_ N<sup>(2)</sup> implies _i̸_ = _j_ . We wish to show that there is a function _f_ : [0 _,_ 1] _×_ [0 _,_ 1]<sup>2</sup> _×_ [0 _,_ 1] _−→ E_ which is middle-symmetric and such that


where _U_ , _Ui_ , _Uj_ and _Uij_ for _i, j ∈_ N are all i.i.d. U[0 _,_ 1].

We will give the ‘classical’ proof, essentially following Aldous [Ald82, Ald85], which builds on de Finetti’s Theorem.

**Obtaining conditional independence** Similarly to the proof of de Finetti’s Theorem, the first step is to construct some new r.v.s coupled to ( _Xij_ ) _ij_ which give

12

some conditional independence. This time we will find a whole sequence of r.v.s ( _Yi_ ) _i_ , coupled to ( _Xij_ ) _ij_ and valued in some auxiliary standard Borel space, such that the following hold:

(i) The whole enlarged array ( _Yi, Xij_ ) _i,j_ is still exchangeable, i.e.


for any permutation _π_ : N _−→_ N. Note that this array, unlike ( _Xij_ ) _ij_ , is now indexed by _directed_ edges ( _i, j_ ).

- (ii) The r.v.s _Xij_ are conditionally independent over the r.v.s _Yi_ , in the following specific sense:


for any family of distinct pairs _irjr ∈_ N<sup>(2)</sup> , 1 _≤ r ≤ m_ and any bounded measurable functions _f_ 1 _, . . . , fm_ : _E −→_ R. To be precise, this amounts to conditional independence over ( _Yi_ ) _i_ , and also the assertion that when _Xi_ 1 _j_ 1 is conditioned on the whole sequence ( _Yi_ ) _i_ , it actually depends only on the two values _Yi_ 1 and _Yj_ 1.

Now, just as in the case of de Finetti’s Theorem, exchangeability of the family ( _Xij_ ) _ij∈_ N(2) implies that also


for any injection _γ_ : N _−→_ N. Just as before, it follows that we may assume ( _Xij_ ) _ij∈_ N(2) is actually a sub-array of a larger exchangeable array indexed by Z<sup>(2)</sup> .

The extra random variables _Xij_ , for which at least one of _i, j_ lies in N<sup>c</sup> , will be used to construct the _Yi_ . This time, we define the random variables _Yi_ for _i ∈_ N by


so these take values in the product space


Thus, for each _i ∈_ N, _Yi_ simply records _all_ of the values _Xi′j′_ where _i_<sup>_′_</sup> _j_<sup>_′_</sup> is either an edge in N<sup>c</sup> , or an edge that joins _i_ to N<sup>c</sup> .

13

The invariance property (i) of the family � _Yi, Xij_ � _i_ = _̸ j∈_ N _×_ N<sup>is now an immedi-</sup> ate consequence of the exchangeability of the whole Z<sup>(2)</sup> -indexed array, just as in the case of de Finetti’s Theorem.

It remains to prove (1). By induction on _m_ and the law of iterated conditional expectation, it suffices to show that


for any bounded measurable function _f_ : _E −→_ R.

Let _F_ 2 be the _σ_ -algebra generated by all the random variables _Xi_ 1 _j_ 1, ..., _Xim−_ 1 _jm−_ 1 and ( _Yi_ ) _i∈_ N, and _F_ 1 the _σ_ -algebra generated by just _Yim_ and _Yjm_ . Hence _F_ 1 _⊆F_ 2, and by another appeal to iterated conditional expectation we know that


We wish to show that E( _f_ ( _Ximjm_ ) _| F_ 1) = E( _f_ ( _Ximjm_ ) _| F_ 2), and once again the norm-contracting property of conditional expectation shows that


with equality of the functions if and only if their norms are equal.

We now perform the analog of the re-arrangement trick that proved de Finetti’s Theorem, but in this case it will require slightly more care. Let _T ⊂_ N<sup>c</sup> be a further subset such that _T_ and N<sup>c</sup> _\ T_ are both infinite. Given this infinitude, we may now choose an injection _γ_ : Z _−→_ Z with the following properties:


(so all indices except _im_ and _jm_ end up somewhere in N<sup>c</sup> ).

After applying this map to the indices, the r.v.s _Xirjr_ are sent to _Xγ_ ( _ir_ ) _γ_ ( _jr_ ), and the r.v.s _Yi_ are replaced by


(recall (2)), and the joint exchangeability of all our r.v.s promises that


14

Taking _L_<sup>2</sup> norms, this implies


where _F_ 3 is the _σ_ -algebra generated by _Xγ_ ( _i_ 1) _γ_ ( _j_ 1), ..., _Xγ_ ( _im−_ 1) _γ_ ( _jm−_ 1) and ( _Yγ_<sup>_′_</sup> ( _i_ )<sup>)</sup><sup>_i∈_N.</sup> (Note that in the case of de Finetti’s Theorem this third _σ_ -algebra was not needed; the difference is that in the present case we may be unable to find an injection _γ_ that converts _F_ 2 exactly into _F_ 1.)

Upon unraveling the definition of _γ_ , one sees that _F_ 3 is generated by some r.v.s of the form _Xi′j′_ where _i_<sup>_′_</sup> _j_<sup>_′_</sup> is either an edge in N<sup>c</sup> or is of the form _i_<sup>_′_</sup> _im_ or _i_<sup>_′_</sup> _jm_ for some _i_<sup>_′_</sup> _∈_ N<sup>_c_</sup> . This is because _γ_ (Z) = N<sup>c</sup> _∪{im, jm}_ , and the edge _imjm_ is distinct from _irjr_ for _r ≤ m−_ 1. This particular subcollection of the random variables _Xi′j′_ is determined by the various coordinates appearing in the definition (2) of _Yim_ and _Yjm_ . Therefore one has the inclusion _F_ 3 _⊆F_ 1, and hence


by using again the norm-contracting property of conditional expectation. Since this left-hand side is equal to _∥_ E( _f_ ( _Ximjm_ ) _| F_ 2) _∥_ 2, we deduce the desired equality of norms by sandwiching with the previous inequality.

**Completion of the proof: using de Finetti** By the Noise-Outsourcing Lemma, considering any given pair _ij ∈_ N<sup>(2)</sup> we can choose a Borel function _g_ : [0 _,_ 1]<sup>2</sup> _×_ [0 _,_ 1] _−→_ [0 _,_ 1] such that


where _U ∼_ U[0 _,_ 1] is independent from everything else, and since the left-hand distribution is symmetric in _i_ and _j_ we may choose _g_ to be symmetric in its first two arguments. Now by exchangeability, this same _g_ must work for every _ij_ .

However, in view of (1) this now implies that for the joint distribution of the whole process ( _Yi, Xij_ ) _i_ = _̸ j_ we have


where _Uij ∼_ U[0 _,_ 1] are i.i.d. and independent from everything else.

Finally, de Finetti’s Theorem applied to ( _Yi_ ) _i_ gives _h_ : [0 _,_ 1] _×_ [0 _,_ 1] _−→ E_<sup>¯</sup> such that ( _Yi_ ) _i_ = (d _h_ ( _U, Ui_ )) _i_ , and so combining with the above we have


15

where _U_ , _Ui_ , _Ui,j_ are from the full array of i.i.d. U[0 _,_ 1]. This implies the desired conclusion with the middle-symmetric function

_f_ ( _x, x_ 1 _, x_ 2 _, x_ 12) := _g_ ( _h_ ( _x, x_ 1) _, h_ ( _x, x_ 2) _, x_ 12) _._

_2_

**Remarks 1.** This proof looks rather like magic, because it’s hard to locate where we did anything nontrivial. Perhaps the first place one should point to is equality (3). The essence of this theorem is that conditioning _Ximjm_ on all the other random variables that gave rise to _F_ 2 is the same as conditioning on only _Yim_ and _Yjm_ . For the proof, the key realization is that this assertion can be made ‘quantitative’, in that it requires only the equality of the _L_<sup>2</sup> -norms appearing in (3).

**2.** Just as for de Finetti’s Theorem, the analog of the Aldous-Hoover Theorem fails for finite arrays. Once again there is an approximate version of the story instead, but here it is substantially more delicate than for sequences, requiring the study of general structural results for large dense graphs (in particular, a version of the famous Szemer´edi Regularity Lemma from graph theory). This is a part of the theory of ‘limit objects’ for sequences of dense graphs, which has recently been the subject of considerable study by combinatorists (see, for instance, Lov´asz and Szegedy [LS06]). We set that aside here; its connection to exchangeability is surveyed in [Aus08] and [DJ07]. _�_

### **6 Random partitions and mass partitions**

#### **The paintbox theorem**

As suggested previously, the importance of exchangeable random structures is their appearance as a result of infinite sampling. The general philosophy is nicely expressed by Aldous in Section 3 of [Ald]:

‘One way of examining a complex mathematical structure is to sample i.i.d. random points and look at some form of induced substructure relating the random points.’

Our first and most classical example is Kingman’s study of exchangeable random partitions. More recently this has become a central ingredient in the formulation and study of certain coagulation and fragmentation processes, but we will not

16

approach that subject here; see, for instance, Bertoin [Ber06], and Schweinsberg’s course at this workshop.

First, a **mass partition** is a measure on N of mass at most 1 and with atoms of non-increasing size; equivalently, it is a non-negative, non-increasing sequence ( _sk_ ) _k∈_ N such that<sup>�</sup> _k_<sup>_sk≤_1.Let</sup><sup>_P_mdenotethespaceofmasspartitions.Itis</sup> easily shown to be compact for the topology inherited from the product topology on [0 _,_ 1]<sup>N</sup> .

Next, let Ptn denote the space of all partitions of N. Given Π _∈_ Ptn and _A ⊆_ N, we write Π _|A_ for the restriction of Π to _A_ . The space Ptn is also easily seen to be a compact metrizable space by letting two partitions Π, Π<sup>_′_</sup> be close if Π _|_ [ _n_ ] = Π<sup>_′_</sup> _|_ [ _n_ ] for some large _n_ . Partitions Π are in bijective correspondence with equivalence relations on Π, where the associated relation _∼_ Π is defined by


There is a natural action of Sym(N) on Ptn coming from the action on N itself: _σ_ (Π) := _{σ_<sup>_−_1</sup> ( _A_ ) : _A ∈_ Π _}_ . A probability measure on Ptn is **exchangeable** if it is invariant for this action.

**Example** Random mass partitions give a simple construction of exchangeable random partitions. Suppose that _ν ∈_ Pr _P_ m, and now draw a random element of Ptn as follows. First, pick ( _sk_ ) _k ∼ ν_ at random. Having done so, pick a sequence ( _mn_ ) _n_ at random so that the _mn_ are i.i.d. elements of N _∪{∞}_ with law


Finally, let Π consist of the classes


for all _k ∈_ N, together with all the singletons _{n}_ for which _mn_ = _∞_ .

It is a simple calculation to check that this process is an exchangeable random partition, i.e. its law is a Sym(N)-invariant element of Pr(Ptn). We refer to this process as Samp( _ν_ ); it is also called the **paintbox** partition obtained from _ν_ . This name derives from the following intuitive picture. We think of N as a paintbox from which we choose a colour for each _n ∈_ N independently at random according to the probabilities ( _s_ 1 _, s_ 2 _, . . ._ ), or choose not to colour _n_ with probability 1 _−_<sup>�</sup> _k_<sup>_sk_.</sup> Then _m, n ∈_ N lie in the same cell of **Π** if and only if they have both been painted and are the same colour. _�_

17

Just as for sequences and arrays, the point here is that the ‘natural’ examples turn out to be the only ones.

**Theorem 6.1 (Kingman’s Paintbox Theorem)** _Every exchangeable random partition_ **Π** _has the same distribution as_ Samp( _ν_ ) _for some ν ∈_ Pr _P_ m _._

**Proof** This is a consequence of de Finetti’s Theorem. To make contact with that theorem, we construct a [0 _,_ 1]-valued process ( _Vn_ ) _n∈_ N as follows:

- first, choose a sample of the random partition **Π** ;

- then, for each cell _C ∈_ **Π** choose an independent U[0 _,_ 1] r.v. _VC_ ;

- finally, let _Vn_ := _VC_ where _C_ is the cell containing _n_ .

Observe that:

- (i) The r.v.s ( _Vn_ ) _n_ a.s. determine the partition **Π** , because a.s. we have that all _VC_ for different cells _C_ are distinct (since there are only countably many cells), and hence

_Vn_ = _Vm_ iff _n, m_ lie in the same cell of **Π** _._ (4)

- (ii) The sequence ( _Vn_ ) _n_ is exchangeable. Indeed, after fixing the sample **Π** , the process ( _Vn_ ) _n_ arises simply from independent choices of constant values within each cell of **Π** , and hence

law(( _Vσ_ ( _n_ )) _n∈_ N _| σ_ ( **Π** )) = law(( _Vn_ ) _n∈_ N _|_ **Π** ) _._

Since **Π** is exchangeable, i.e. _σ_ ( **Π** ) =<sup>d</sup> **Π** , averaging over the distribution of **Π** now gives that ( _Vn_ ) _n_ is exchangeable.

By de Finetti’s Theorem, there is some Borel _f_ : [0 _,_ 1] _×_ [0 _,_ 1] _−→_ [0 _,_ 1] such

that


Finally, let _θ_ ( _x_ ) _∈_ Pr[0 _,_ 1] be the law of _f_ ( _x, U_ ) when _U ∼_ U[0 _,_ 1], and let _s_ ( _x_ ) = ( _sn_ ( _x_ )) _n_ be the sequence of masses of the atoms of _θ_ ( _x_ ) arranged in non-increasing order. This defines a measurable function _s_ : [0 _,_ 1] _−→P_ m. Conditionally on _x ∈_ [0 _,_ 1], the rule (4) gives that if _m, n ∈_ N are distinct then they lie in the same cell of our random partition if and only if _f_ ( _x, Um_ ) and _f_ ( _x, Un_ ) land on the same atom of _θ_ ( _x_ ). This is clearly equivalent to the description in the example, so **Π** has law Samp( _ν_ ) with _ν_ the law of _s_ ( _U_ ). _2_

18

#### **The Chinese Restaurant and the Poisson-Dirichlet distributions**

Having introduced exchangeable random partitions, we take the chance to introduce also an important family of examples.

Fix a parameter 0 _< α <_ 1, and consider the measure _mα_ (d _x_ ) = _x_<sup>_−α−_1</sup> d _x_ on (0 _, ∞_ ). Simple calculus gives


using _α >_ 0 and _α <_ 1 respectively.

Now let Λ be a Poisson point process on (0 _, ∞_ ) with intensity measure _mα_ . This is a random countable subset of (0 _, ∞_ ), and the first inequality above translates into the fact that _|_ Λ _∩_ [ _ε, ∞_ ) _| < ∞_ a.s. for all _ε >_ 0. This means that we may enumerate the points of Λ in non-increasing order, say as ( _uk_ ) _k_ . In addition,


so these two facts together imply that<sup>�</sup> _k_<sup>_uk_is finite a.s.We may therefore con-</sup> sider the sequence


This is now a random element of _P_ m.

Thus we have constructed a family of probability measures on _P_ m indexed by _α ∈_ (0 _,_ 1). They are called the **Poisson-Dirichlet** distributions and are denoted by PD( _α,_ 0). (They are part of a larger two-parameter family PD( _α, θ_ ), whose others members will not concern us.) They were introduced by Pitman and Yor in [PY97], and have since shown up in a remarkable range of applications. We will meet them again later; at this point we simply record some basic facts about the associated paintbox random partitions.

To do so, first consider any random partition **Π** (not necessarily exchangeable). The law of **Π** is determined by the laws of all its finite restrictions **Π** _|_ [ _n_ ], and hence by the function


defined for any partition _{B_ 1 _, . . . , Bk}_ of a finite set [ _n_ ].

19

If this quantity depends only on _|B_ 1 _|_ , ..., _|Bk|_ then **Π** is said to be **weakly exchangeable** ; clearly this is implied by exchangeability. In this case _p_ is written as a function of these cardinalities and is called the **exchangeable partition probability function** (‘EPPF’).

In the case of Samp(PD( _α,_ 0)), some clever calculus (omitted here) now yields the **Pitman sampling formula** for the EPPF:


Using this, one can prove that the following remarkable construction also gives rise to the law Samp(PD( _α,_ 0)). Consider a restaurant with an infinite number of tables in a row, all of them infinitely large. Initially all tables are empty. At subsequent times, customers arrive and pick tables according to the following random process. The first customer simply sits at table 1. Now suppose that at time _n ≥_ 1, the first _k_ tables already have at least one customer. Then the ( _n_ + 1)<sup>th</sup> customer chooses to sit at the first unoccupied table with probability _kα/n_ , or chooses to sit at the _i_<sup>th</sup> occupied table with probability


For future reference, let us note an alternative way of writing this rule: it asserts that the probability of customer _n_ +1 choosing to sit at the same table as any given customer _m ∈{_ 1 _,_ 2 _, . . . , n}_ is given by


Over time, this process reveals a partition of N whose classes are the sets of customers sitting at each table. This is often referred to as the **Chinese Restaurant Process** , and was introduced in work of Dubins and Pitman; see [Pit95].

**Proposition 6.2** _The random partition_ **Π** _resulting from the Chinese Restaurant process is exchangeable with law_ Samp(PD( _α,_ 0)) _. 2_

This can be proved directly by computing the probabilities (5) for this partition by induction on _|B_ 1 _|_ + _· · ·_ + _|Bk|_ = _n_ , and verifying that they agree with (6). Without this calculation, it is not even obvious that the Chinese Restaurant Process gives a weakly exchangeable partition.

20

The Poisson-Dirichlet processes also arise naturally from a remarkable number of other discrete random structures: a nice overview is given in Section 11 of Aldous [Ald85].

### **7 Gram-de Finetti matrices and probabilities on Hilbert space**

Our next class of exchangeable structures is the following.

**Definition 7.1 (Gram-de Finetti matrices)** _A_ **_Gram-de Finetti matrix_** _is a symmetric exchangeable array_ ( _Ri,j_ )( _i,j_ ) _∈_ N2 _of_ R _-valued random variables such that the matrix_ ( _Ri,j_ ) _i,j is almost surely non-negative definite._

This time, the natural ‘sampling’ examples are the following.

**Examples** Suppose that **_µ_** is a random probability measure on a Hilbert space H, which will always be assumed real and separable, and construct a random array from it as follows. First, sample **_µ_** at random. Having chosen **_µ_** , now draw from it an i.i.d. sequence of vectors ( _ξi_ ) _i∈_ N, and finally set


the matrix of pairwise inner products in H. This defines a Gram-de Finetti matrix, whose law we denote by Samp( **_µ_** ).

To make this a little more general, suppose instead that **_µ_** is a random probability measure on H _×_ [0 _, ∞_ ), and modify the above construction as follows: after choosing **_µ_** at random, let ( _ξi, ai_ ) be an i.i.d. _∼_ **_µ_** sequence and set


where _δij_ is the Kronecker delta. This law will still be referred to as Samp( **_µ_** ). _�_

If we fix _M >_ 0, then the space of non-negative definite arrays with all entries bounded by _M_ is compact for the product topology, so we may naturally talk of vague (= weak<sup>_∗_</sup> ) convergence for probability measures on this space, and moreover a limit of exchangeable measures is easily seen to be still exchangeable. This will be important for applications later.

21

#### **The Dovbysh-Sudakov representation**

The crucial fact which makes Gram-de Finetti matrices useful is that, just as for other exchangeable arrays, they _all_ arise from sampling. This is the main result of this section.

**Theorem 7.2 (Dovbysh-Sudakov representation; [DS82, Hes86, Pan10])** _For any Gram-de Finetti matrix R there is a random probability measure_ **_µ_** _on ℓ_ 2 _×_ [0 _, ∞_ ) _such that_ law( _R_ ) = Samp( **_µ_** ) _._

A suitable choice of **_µ_** is called a **directing random measure** for _R_ ; in the next section we will address the issue of its uniqueness.

We will prove Theorem 7.2 only in the special case that _R_ takes values in [ _−_ 1 _,_ 1] and _Ri,i ≡_ 1. Both of these assumptions can be removed with just a little more work, but we leave that to the references for the sake of brevity; the special case is enough for our later applications to spin glasses. In this special case we will show that there is a random probability measure **_µ_** on the unit ball _B ⊂ ℓ_ 2 (rather than on _ℓ_ 2 _×_ [0 _, ∞_ )) such that


where ( _ξi_ ) _i_ is a conditionally i.i.d. sequence drawn from **_µ_** . The diagonal terms are then taken care of simply by setting


**Proof of special case, following [Pan10]**<sup>2</sup> Since ( _Ri,j_ ) _i_ = _̸ j_ is a symmetric exchangeable array, by the Aldous-Hoover Theorem we have


for some middle-symmetric _f_ : [0 _,_ 1] _×_ [0 _,_ 1]<sup>2</sup> _×_ [0 _,_ 1] _−→_ [ _−_ 1 _,_ 1].

Instead of the arbitrary measurable function _f_ , we want the richer geometric structure of sampling points from a random probability measure on _ℓ_ 2. The rest of the proof goes into synthesizing the latter from the former.

**Step 1:** Letting _fu_ := _f_ ( _u, ·, ·, ·_ ), it is easy to see that Samp( _f_ ) is a.s. nonnegative definite if and only if Samp( _fu_ ) is a.s. non-negative definite for a.e. _u_ .

> 2I think this is similar to the proof of [Hes86], but I haven’t been able to access that.

22

It therefore suffices to show that Samp( _fu_ ) must arise from sampling from some measure _µu_ on _B ⊂ ℓ_ 2 for a.e. _u_ , where the measure _µu_ is now non-random. From this, general measure theory gives a measurable selection _u �→ µu_ , which defines the desired random measure.

So suppose henceforth that _f_ is a function of only ( _u_ 1 _, u_ 2 _, u_ 12), and that Samp( _f_ ) is a.s. non-negative definite. We may also suppose that


(not just in law), simply by taking this as our new definition of ( _Ri,j_ ) _i_ = _̸ j_ . We still have _Ri,i ≡_ 1.

**Step 2:** Next we show that _f_ ( _u_ 1 _, u_ 2 _, u_ 12) cannot depend non-trivially on _u_ 12 without violating the a.s. non-negative definiteness of _R_ . To make use of the nonnegative definiteness, observe that for any _n ≥_ 1 and any bounded measurable functions _h_ 1 _, . . . , hn_ : [0 _,_ 1] _−→_ R one has


We will apply this with the following careful choice of functions. Let _n_ = 4 _m_ , let _A_ 1 _, A_ 2 _⊆_ [0 _,_ 1] be any measurable subsets, and let


Now consider


which is an average over the _ui_ (but not the _uij_ ) of an expression like (8). Taking the sum outside the integral, we may write this as


where _D_ contains the diagonal terms ( _i_ = _j_ ) and each _Ikℓ_ consists of those terms with _i̸_ = _j_ , ( _k −_ 1) _m_ + 1 _≤ i ≤ km_ and ( _ℓ −_ 1) _m_ + 1 _≤ j ≤ ℓm_ .

23

Since _|f | ≤_ 1, _D_ consists of an average of _n_ terms that are uniformly bounded by 1. On the other hand, each _Ikℓ_ is (1 _/n_ ) times a sum of terms of the form


with each of _A_ , _A_<sup>_′_</sup> equal to either _A_ 1 or _A_ 2. If _k̸_ = _ℓ_ there are _m_<sup>2</sup> of these terms in _Ikℓ_ , and if _k_ = _ℓ_ then there are _m_<sup>2</sup> _− m_ (because the diagonal terms are in _D_ instead). Also, as we vary _k_ and _ℓ_ the _±_ -signs almost exactly cancel, in that each integral � _A_ � _A_<sup>_′_appears in all of the</sup><sup>_Ik,ℓ_together the same number of times as</sup> _−_ � _A_ � _A_<sup>_′_, apart from a small correction owing to the diagonal terms.</sup>

However, each of these individual integrals appearing in one of the sums _Ikℓ_ depends on a different variable _uij_ . If their dependence on this variable is not trivial up to a negligible set, then a simple estimate using the Central Limit Theorem shows that these off-diagonal sums must have approximately a centred Gaussian distribution as functions of the uniform r.v.s ( _Uij_ ) _i,j≤n_ , with variance of order 1. In particular, there is some small positive probability in these uniform r.v.s that the sum _I_ 11 + _I_ 12 + _. . ._ + _I_ 44 will be negative and have absolute value much larger than _|D| ≤_ 1. This would make the whole sum _D_ + _I_ 11 + _I_ 12 + _. . ._ + _I_ 44 negative, and this would contradict non-negative definiteness.

So instead one must have that for every _A_ 1 _, A_ 2 _⊆_ [0 _,_ 1] the quantity


is independent of _w_ outside a Lebesgue-negligible set of _w_ . Since _f_ itself may be approximated by a linear combination of indicator functions of the form 1 _A_ 1 _×A_ 2, this implies that _f_ ( _u, v, w_ ) does not depend on _w_ outside of some negligible set, as required.

Henceforth we write _f_ as a function of only ( _u_ 1 _, u_ 2).

**Step 3:** Now consider the linear operator _A_ on _L_<sup>2</sup> [0 _,_ 1] defined by


Since _f_ is uniformly bounded by 1, this is a bounded operator, and moreover an easy exercise shows that it is compact. It is self-adjoint owing to the symmetry of _f_ .

Therefore the Spectral Theorem for compact self-adjoint operators provides a sequence of real eigenvalues _λi_ with _|λi| −→_ 0 and eigenfunctions _ϕi ∈ L_<sup>2</sup> [0 _,_ 1]

24

##### such that


where the series converges in _L_<sup>2</sup> ([0 _,_ 1]<sup>2</sup> ). (If you’re not familiar with this spectral theorem, then think of it as putting the ‘symmetric [0 _,_ 1] _×_ [0 _,_ 1] matrix _f_ ( _·, ·_ )’ into ‘diagonal form’; and see any standard book covering Hilbert space operators, such as Conway [Con90].)

**Step 4:** Another property of the operator _A_ is that it is non-negative definite for a.e. _u_ ; once again, this is necessary in order that _R_ be a.s. non-negative definite. To see this, simply observe that for any measurable function _h_ : [0 _,_ 1] _−→_ R, nonnegative definiteness and the Law of Large Numbers applied to the independent r.v.s _Ui ∼_ U[0 _,_ 1] give


as _n −→∞_ , where this denotes the inner product in _L_<sup>2</sup> [0 _,_ 1]. Therefore we also have _λi ≥_ 0 for all _i_ a.s.

**Step 5:** Now define a measurable function _F_ : [0 _,_ 1] _−→_ C<sup>N</sup> by


We will next argue that it takes values in _B ⊂ ℓ_ 2 a.s. To be specific, let _x ∈_ [0 _,_ 1] be a Lebesgue density point for every _ϕi_ simultaneously: that is,


These points are co-negligible in [0 _,_ 1] by the Lebesgue Differentiation Theorem, which applies since _ϕi ∈ L_<sup>2</sup> [0 _,_ 1] _⊂ L_<sup>1</sup> [0 _,_ 1].

Now we can compute that


and this is _≤_ 1 because _f_ is pointwise bounded by 1. Letting _δ −→_ 0 shows that


25

as required.

In terms of _F_ we now have the relation


where the right-hand side is the inner product in _ℓ_ 2. Let _µ_ be the distribution of _F_ ( _X_ ) on _B_ when _X ∼_ U[0 _,_ 1] (that is, the push-forward of Lebesgue measure under _F_ ).

**Step 6:** Lastly, recall that Samp( _f_ ) is the law of _R_ , and write this relation explicitly as


for any _N ≥_ 1 and any non-negative definite matrix ( _rij_ ) _i,j≤N_ . Finally, we recognize that


This is precisely the assertion that law( _R_ ) = Samp( _µ_ ), so the proof is complete. _2_

An important consequence of Theorem 7.2 is a sensible notion of convergence for random Hilbert space probability measures. If ( **_µ_** _n_ ) _n_ is a sequence of random probability measures on (possibly different) Hilbert spaces, then they **samplingconverge** if the resulting laws Samp( **_µ_** _n_ ) converge vaguely as probability measures on the space of non-negative definite matrices, and in this case their **limit object** is any choice of directing random measure for the limiting random matrix. If all these random probability measures have uniformly bounded support then the resulting Gram-de Finetti matrices will be uniformly bounded, and so there will always at least be subsequential limits.

This is worth comparing with the theory of limit objects for dense finite graphs [LS06, DJ07, Aus08], for which it is the direct analog of left-convergence of homomorphism densities. It is also very much in the spirit of the more general discussion of probability distributions on distance matrices that characterize a general metric probability space – see Sections 3 2<sup><u>1</u>.4through3</sup><sup><u>1</u></sup> 2<sup>.7inGromov[Gro99],andthe</sup> references given there to works of Vershik.

26

### **8 Some uniqueness results**

In the setting of the Structure Theorem 2.2, it is natural to ask which pairs of middle-symmetric functions _f_ , _f_<sup>_′_</sup> give Samp( _f_ ) = Samp( _f_<sup>_′_</sup> ). The necessary and sufficient condition is a little subtle, and is explained in detail in Chapter 7 of Kallenberg [Kal05]. However, in the settings of the Kingman and DovbyshSudakov Theorems it is easier to be precise, so here we will focus on these.

In the case of random partitions, the representation is unique.

**Proposition 8.1** _If ν, ν_<sup>_′_</sup> _∈P_ m _and_ Samp( _ν_ ) = Samp( _ν_<sup>_′_</sup> ) _, then ν_ = _ν_<sup>_′_</sup> _._

**Proof** Recall the construction of **Π** _∼_ Samp( _ν_ ): first one chooses ( _sk_ ) _k ∼ ν_ ; then one chooses _mn ∈_ N _∪{∞}_ i.i.d. from the distribution ( _s_ 1 _, s_ 2 _, . . . ,_ 1 _−_ � _k_<sup>_sk_); and finally one defines</sup><sup>_ℓ∼_</sup><sup>**Π**</sup><sup>_n_if and only if</sup><sup>_mℓ_=</sup><sup>_mn∈_N.</sup>

In this construction, after fixing the mass partition ( _sk_ ) _k_ , it follows from the Law of Large Numbers that for each _k ∈_ N one has


a.s. in the choice of the sequence ( _mn_ ) _n_ , where _Ck_ = _{n_ : _mn_ = _k}_ is the corresponding cell of **Π** . Therefore, it holds a.s. that the asymptotic frequency


exists for every cell _C ∈_ **Π** , and the set of positive asymptotic frequencies is equal to the set of values _sk_ which are positive, counted with multiplicities. Hence ( _sk_ ) _k_ is a.s. equal to ( _tk_ ( **Π** )) _k_ , defined to be the set of values


arranged in non-increasing order. It follows that _ν_ is equal to the law of the sequence ( _tk_ ( **Π** )) _k_ as a function of the random partition **Π** , and so the law of **Π** determines the law of ( _sk_ ) _k_ . _2_

The situation is not quite so simple for Gram-de Finetti matrices. For example, if _µ_ , _µ_<sup>_′_</sup> are probability measures on Hilbert spaces H, H<sup>_′_</sup> such that there is a linear isometry Φ : H _−→_ H<sup>_′_</sup> with _µ_<sup>_′_</sup> = Φ _∗µ_ , then one easily calculates that Samp( _µ_ ) = Samp( _µ_<sup>_′_</sup> ). However, it turns out that this kind of degeneracy, suitably generalized, is the only possibility.

27

To formulate this, we will use the following notation: if _µ_ is a probability measure on H _×_ [0 _, ∞_ ), we will write spt1 _µ_ for the projection of spt _µ ⊆_ H _×_ [0 _, ∞_ ) onto H (or, equivalently, the support of the projection of _µ_ onto H), and will write


for the closed subspace of H generated by spt1 _µ_ .

Before giving the main proposition, it is worth proving the following lemma separately.

**Lemma 8.2** _There are measurable functions_


_with the following property. Suppose that_ H _is a real Hilbert space and ξ_ 1 _, ξ_ 2 _, ...is a sequence of vectors in_ H _such that ∥ξi∥≤_ 1 _for all i and_


_Then the values_


_converge to ∥ξ_ 1 _∥._

**Proof** By enlarging H if necessary, we may assume that _e_ 1, _e_ 2, ...is an orthonormal sequence which is also orthogonal to every _ξi_ . Now let


so that _∥ζi∥_ = 1 and


Since _ξ_ 1 lies in <u>span(</u> _ξ_ 2 _, ξ_ 3 _, . . ._ ), it is equal to its projection onto that subspace. That, in turn, is equal to the projection of _ζ_ 1 onto <u>span(</u> _ζ_ 2 _, ζ_ 3 _, . . ._ ), since the vectors _ei_ are orthogonal to each other and to everything else.

However, for the _ζi_ s (unlike for the _ξi_ s) we know that all their lengths are equal to 1. Therefore, by implementing the Gram-Schmidt procedure and computing the resulting change of basis, for any _n ≥_ 2 the length of the projection of _ζ_ 1 onto span( _ζ_ 2 _, . . . , ζn_ ) is given by a measurable function _fn_ of the inner products


Letting _n −→∞_ gives the result. _2_

28

**Proposition 8.3** _Suppose that_ **_µ_** _and_ **_µ_**<sup>_′_</sup> _are random probability measures on the respective spaces_ H _×_ [0 _, ∞_ ) _and_ H<sup>_′_</sup> _×_ [0 _, ∞_ ) _such that_ Samp( **_µ_** ) = Samp( **_µ_**<sup>_′_</sup> ) _. Then there is a coupling of random variables_ ( **_µ_** _,_ **_µ_**<sup>**_′_**</sup> _,_ **Φ** ) _in which_

_•_ **Φ** _is almost surely a linear isometry_


As for the Dovbysh-Sudakov Theorem, for the proof we restrict to the special case _|Ri,j| ≤_ 1, _Ri,i ≡_ 1. Note that this does _not_ imply _ai_ = 0. The general case is treated in [Panar], but for the last step in the proof below I have taken a different route from Panchenko, using an idea of Vershik from the more general setting of exchangeable random metrics on N (see Section 3<sup><u>1</u></sup> 2<sup>.7 of Gromov [Gro99]).</sup>

**Proof in special case** Recall the definition of the process with law Samp( **_µ_** ): first one samples **_µ_** at random, and then one samples ( _ξi, ai_ ) _i∈_ N i.i.d. _∼_ **_µ_** and forms the matrix


If we retain all of the random choices made in this procedure, it actually defines a coupled collection of random variables


in which the _Ri,j_ s are determined by the ( _ξi, ai_ )s.

**Step 1:** First we show that under the joint distribution of these random data, the norms _∥ξi∥_ , _i ∈_ N, are a.s. determined by the matrix ( _Ri,j_ ) _i,j_ . In case _ai ≡_ 0 this is obvious, since then _∥ξi∥_<sup>2</sup> = _Ri,i_ , but in general we must instead make use of the off-diagonal terms of the matrix. The key observation is that almost surely one has


and given this it also holds almost surely that:

for every _i_ and every _ε >_ 0 there are infinitely many _j_ such that


Therefore


Now Lemma 8.2 shows that on this probability-1 event, each of the norms _∥ξi∥_ is equal to a limit of measurable functions of the off-diagonal inner products _ξi · ξj_ = _Ri,j_ for _j̸_ = _i_ , and hence the norm itself is a measurable function of these offdiagonal _R_ -entries.

Having shown this, it follows that _ai_ = _Ri,i −∥ξi∥_<sup>2</sup> is also a measurable function of the _R_ -entries.

**Step 2:** If one knows _Ri,j_ for all _i̸_ = _j_ and also _∥ξi∥_ for all _i_ , then these quantities determine the distances


Therefore, in the sextuple of random data


the matrix _R_ a.s. determines all the distances in the fourth and fifth entries and all the values in the sixth entry.

**Step 3:** Now suppose that **_µ_**<sup>_′_</sup> is another random measure giving Samp( **_µ_**<sup>_′_</sup> ) = Samp( **_µ_** ), and form also its collection of random data


in the same way. Our assumption is that ( _Ri,j_ ) _i,j_ = (d _Ri,j′_<sup>)</sup><sup>_i,j_, and so (using that we</sup> work on standard Borel spaces) there is a coupling of these random collections of data under which


Having formed this coupling, Step 2 implies that also


Therefore the random map


defined by **Φ**<sup>0</sup> (0) = 0 and **Φ**<sup>0</sup> ( _ξi_ ) = _ξi_<sup>_′_is almost surely an isometry.</sup>

30

On the other hand, by the Law of Large Numbers, another almost sure event is that the empirical distributions of the sequence ( _ξi, ai_ ) _i_ are tight and satisfy


in the vague topology, and similarly for the pairs ( _ξi_<sup>_′, a′_</sup> _i_<sup>) and the random measure</sup> **_µ_**<sup>_′_</sup> .

Finally, when these a.s. events both hold and the map **Φ**<sup>0</sup> is an isometry, that map may be extended uniquely to a linear isometry


(since an origin-preserving isometry between subsets of Hilbert spaces uniquely extends to a linear isometry of the subspaces they generate). Now applying **Φ** to the convergence of the empirical distributions gives


This completes the proof.

### **9 Comparison of random partitions and Gram-de Finetti matrices**

Although Kingman’s Paintbox Theorem is much simpler than Dovbysh-Sudakov, it is worth noting that the former is a special case of the latter. This is simply because if **Π** is an exchangeable random partition, then it defines a _{_ 0 _,_ 1 _}_ -valued Gram-de Finetti matrix by setting


(an easy exercise shows that this is non-negative definite).

Applying the Dovbysh-Sudakov Theorem to this _R_ gives a random measure **_µ_** on H _×_ [0 _, ∞_ ) such that


31

for an i.i.d.( **_µ_** ) sample ( _ξi, ai_ ) _i_ . Since _R_ is _{_ 0 _,_ 1 _}_ -valued, this implies that _ξ · ξ_<sup>_′_</sup> lies in _{_ 0 _,_ 1 _}_ almost surely when _ξ_ , _ξ_<sup>_′_</sup> are drawn independently from **_µ_** . By some simple analysis, this is possible only if the random set spt1 **_µ_** almost surely consists of either a finite or infinite orthonormal sequence, or an orthonormal sequence together with the origin, or just the origin.

In the third case one has _Ri,j_ = 0 whenever _i̸_ = _j_ , so this corresponds to the trivial partition of N into singletons. In either of the first two cases, let ( _ek_ ) _k_ be the orthonormal sequence ordered so that the weights _sk_ := **_µ_** _{ek}_ are non-increasing, and made infinite by including extra vectors if necessary. The support spt1 **_µ_** also contains 0 precisely when<sup>�</sup> _k_<sup>_sk<_1,inwhichcase</sup><sup>**_µ_**</sup><sup>_{_0</sup><sup>_}_=1</sup><sup>_−_�</sup> _k_<sup>_sk_.Re-</sup> writing the representation of _R_ as Samp( **_µ_** ) in terms of **Π** , we find that the random sequence of weights ( _sk_ ) _k_ is precisely the random mass partition that directs **Π** according to the paintbox construction.

Concerning the uniqueness results of the preceding section, one sees a closer parallel by choosing a slightly different formulation of paintbox processes. If one does not insist that mass partitions be non-increasing, then two mass partitions ( _sk_ ) _k_ , ( _s_<sup>_′_</sup> _k_<sup>)</sup><sup>_k_give the same paintbox process if and only if one is a re-ordering of</sup> the other. This is the analog of the redundancy that we found for Gram-de Finetti matrices driven by Hilbert space measures, except that the relevant symmetry group is Sym(N) rather than the orthogonal group of H. With this less restrictive notion of random mass partitions, two measures _ν, ν_<sup>_′_</sup> _∈_ Pr _P_ m give Samp( _ν_ ) = Samp( _ν_<sup>_′_</sup> ) if and only if there is a coupling _λ ∈_ Pr ( _P_ m _× P_ m) of _ν_ and _ν_<sup>_′_</sup> such that _λ_ is supported on the pairs (( _sk_ ) _k,_ ( _s_<sup>_′_</sup> _k_<sup>)</sup><sup>_k_)forwhich(</sup><sup>_s_</sup> _k_<sup>_′_)</sup><sup>_k_isare-orderingofthe</sup> sequence ( _sk_ ) _k_ .

### **10 Other symmetries for stochastic processes**

Several other symmetry principles for the laws of stochastic processes have been studied by methods more-or-less similar to those above, often using the basic Structure Theorem 2.2 to do the heavy lifting and then adding some refinements, as we did for partitions and Garm-de Finetti matrices.

Some well-known examples, with references, include:

- contractible sequences and arrays ([Ald85, Section 6] and [Kal05, Chapters 1 and 7]);

- separately (or ‘row-column’) exchangeable arrays ([Ald85, Section 14] and

32

[Kal05, Chapters 1 and 7]);

- notions of exchangeability for continuous-time processes ([Ald85, Section 10] and [Kal05, Section 1.3]);

- tree-indexed processes which have the symmetries of the tree [Ald85, Section 13];

- rotatable arrays ([Ald85, Subsection 15.7] and [Kal05, Chapter 8]);

- exchangeable random sets [Ald85, Section 17] and [Kal05, Chapter 6]);

- invariant point processes [Ald85, Subsection 21.2], and more generally symmetric random measures on rectangles in Euclidean spaces [Kal05, Chapter 9].

### **Part II**

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Spin glasses →](03-spin-glasses.md)
