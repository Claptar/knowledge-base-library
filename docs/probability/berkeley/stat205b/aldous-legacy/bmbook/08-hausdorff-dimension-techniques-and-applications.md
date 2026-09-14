---
title: 'Hausdorff dimension: Techniques and applications'
source: https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/bmbook.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Hausdorff dimension: Techniques and applications

**Source:** [`bmbook.pdf`](https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Dimensions are a tool to measure the size of mathematical objects on a crude scale. For example, in classical geometry one can use dimension to see that a line segment (a one-dimensional object) is smaller than the surface of a ball (a two-dimensional object), but there is no difference between line-segments of different lengths. It may therefore come as a surprise that dimension is able to distinguish the size of so many objects in probability theory.

In this chapter we first introduce a suitably general notion of dimension, the Hausdorff dimension. We then describe general techniques to calculate the Hausdorff dimension of arbitrary subsets of R<sup>_d_</sup> , and apply these techniques to the graph and zero set of Brownian motion in dimension one, and to the range of higher dimensional Brownian motion. Lots of further examples will follow in subsequent chapters.

### **1. Minkowski and Hausdorff dimension**

**1.1. The Minkowski dimension.** How can we capture the dimension of a geometric object? One requirement for a useful definition of dimension is that it should be _intrinsic_ . This means that it should be independent of an embedding of the object in an ambient space like R<sup>_d_</sup> . Intrinsic notions of dimension can be defined in arbitrary metric spaces.

Suppose _E_ is a bounded metric space with metric _ρ_ . Here bounded means that the diameter _|E|_ = sup _{ρ_ ( _x, y_ ) : _x, y ∈ E}_ of _E_ is finite. The example we have in mind is a bounded subset of R<sup>_d_</sup> . The definition of Minkowski dimension is based on the notion of a _covering_ of the metric space _E_ . A **covering** of _E_ is a finite or countable collection of sets


Define, for _ε >_ 0,


where _|A|_ is the diameter of a set _A ⊂ E_ . Intuitively, when _E_ has dimension _s_ the number _M_ ( _E, ε_ ) should be of order _ε_<sup>_−s_</sup> . This can be verified in simple cases like line segments, planar squares, etc. This intuition motivates the definition of _Minkowski dimension_ .

Definition 4.1. _For a bounded metric space E we define the_ **lower Minkowski dimension** _as_


97

_and the_ **upper Minkowski dimension** _as_


_We always have_ <u>dim</u> _~~M~~_<sup>_E≤_</sup> dim _M E, but equality need not hold. If it holds we write_


Remark 4.2. If _E_ is a subset of the unit cube [0 _,_ 1]<sup>_d_</sup> _⊂_ R<sup>_d_</sup> then let


be the number of dyadic cubes of sidelength 2<sup>_−n_</sup> which hit _E_ . Then there exists a constant _C_ ( _d_ ) _>_ 0 depending only on the dimension, such that _M_<sup>˜</sup> _n_ ( _E_ ) _≥ M_ ( _E, √d_ 2<sup>_−n_</sup> ) _≥ C_ ( _d_ ) _M_<sup>˜</sup> _n_ ( _E_ ). Hence


Example 4.3. In Exercise 4.1, we calculate the Minkowski dimension of a deterministic ‘fractal’, the (ternary) Cantor set,


This set is obtained from the unit interval [0 _,_ 1] by first removing the middle third, and the successively the middle third out of each remaining interval ad infinitum, see Figure 1 for the first three stages of the construction. _⋄_


<!-- Start of picture text -->
1<br>1/9 1/3 1/9<br><!-- End of picture text -->

Figure 1. The ternary Cantor set is obtained by removing the middle third from each interval. The figure shows the first three steps of the infinite procedure.

98

Remark 4.4. There is an unpleasant limitation of Minkowski dimension: Observe that singletons _S_ = _{x}_ have Minkowski dimension 0, but we shall see in Exercise 4.2 that the set


has positive dimension. Hence the Minkowski dimension does not have the **countable stability property**


This is one of the properties we expect from a reasonable concept of dimension. There are two ways out of this problem.

- (i) One can use a notion of dimension taking variations of the size in the different sets in a covering into account. This captures finer details of the set and leads to the notion of _Hausdorff dimension_ .

- (ii) One can enforce the countable stability property by subdividing every set in countably many bounded pieces and taking the maximal dimension of them. The infimum over the numbers such obtained leads to the notion of _packing dimension_ .

We follow the first route now, but come back to the second route later in the book.


**1.2. The Hausdorff dimension.** The Hausdorff dimension and Hausdorff measure were introduced by Felix Hausdorff in 1919. Like the Minkowski dimension, Hausdorff dimension can be based on the notion of a covering of the metric space _E_ . For the definition of the Minkowski dimension we have evaluated coverings crudely by counting the number of sets in the covering. Now we also allow infinite coverings and take the size of the covering sets, measured by their diameter, into account.

Looking back at the example of Exercise 4.2 one can see that the set _E_ = _{_ 1 _/n_ : _n ≥_ 1 _} ∪{_ 0 _}_ can be covered much more effectively, if we decrease the size of the balls as we move from right to left. In this example there is a big difference between evaluations of the covering which take into account that we use small sets in the covering, and the evaluation based on just counting the number of sets used to cover.

A very useful evaluation is the _α_ **-value** of a covering. For every _α ≥_ 0 and covering _E_ 1 _, E_ 2 _, . . ._ we say that the _α_ **-value** of the covering is


The terminology of the _α_ -values of a covering allows to formulate a concept of dimension, which is sensitive to the effect that the fine features of this set occur in different scales at different places.

Definition 4.5. _For every α ≥_ 0 _the α_ **-Hausdorff content** _of a metric space E is defined as_


99


<!-- Start of picture text -->
informally speaking the α-value of the most efficient covering. If 0  ≤ α ≤ β, and H∞ α ( E ) = 0 ,<br>then also H∞ β ( E ) = 0 . Thus we can define<br><!-- End of picture text -->


Remark 4.6. The Hausdorff dimension may, of course, be infinite. But it is easy to see that subsets of R<sup>_d_</sup> have Hausdorff dimension no larger than _d_ . Moreover, in Exercise 4.3 we show that for every bounded metric space, the Hausdorff dimension is bounded from above by the lower Minkowski dimension. Finally, in Exercise 4.4 we check that Hausdorff dimension has the countable stability property. _⋄_


<!-- Start of picture text -->
⋄<br><!-- End of picture text -->


<!-- Start of picture text -->
�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� 1<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>�� �� �� �� �� �� �� �� �� �� �� �� �� �� �� ��<br>1 1<br><!-- End of picture text -->

Figure 2. The ball, sphere and line segment pictured here all have 1-Hausdorff content equal to one.

The concept of the _α_ -Hausdorff content plays an important part in the definition of the Hausdorff dimension. However, it does not help distinguish the size of sets of the same dimension. For example, the three sets sketched in Figure 2 all have the same 1-Hausdorff content: the ball and the sphere on the left can be covered by a ball of diameter one, so that their 1-Hausdorff content is at most one, but the line segment on the right also does not permit a more effective covering and its 1-Hausdorff content is also 1. Therefore, one considers a refined concept, the _Hausdorff measure_ . Here the idea is to consider only coverings by _small_ sets.

Definition 4.7. _Let X be a metric space and E ⊂ X. For every α ≥_ 0 _and δ >_ 0 _define_


_i.e. we are considering coverings of E by sets of diameter no more than δ. Then_


_is the α_ **-Hausdorff measure** _of the set E._


100

Remark 4.8. The _α_ -Hausdorff measure has two obvious properties which, together with _H_<sup>_α_</sup> ( _∅_ ) = 0, make it an _outer measure_ . These are _countable subadditivity_ ,


and _monotonicity_ ,


One can express the Hausdorff dimension in terms of the Hausdorff measure.

Proposition 4.9. _For every metric space E we have_


**Proof.** We focus on the first equality, all the other arguments are similar. Suppose dim _E > α_ . Then, for all _β ≤ α_ , _c_ := _H∞_<sup>_β_(</sup><sup>_E_)</sup><sup>_>_0,andclearlywehave</sup><sup>_H_</sup> _δ_<sup>_β_(</sup><sup>_E_)</sup><sup>_≥c>_0for</sup> all _δ >_ 0. Hence, _H_<sup>_β_</sup> ( _E_ ) _≥ c >_ 0 and this implies _H_<sup>_β_</sup> ( _E_ ) _>_ 0 for all _β ≤ α_ . We infer that inf _{β_ : _H_<sup>_β_</sup> ( _E_ ) = 0 _} ≥ α_ . Conversely, if dim _E < α_ , then _H∞_<sup>_α_(</sup><sup>_E_) = 0 and hence, for every</sup><sup>_δ>_0, there exists a covering by</sup> sets _E_ 1 _, E_ 2 _, . . ._ with<sup>�</sup><sup>_∞_</sup> _k_ =1<sup>_|Ek|α< δ_.These sets have diameter less than</sup><sup>_δ_1</sup><sup>_/α_, hence</sup><sup>_H_</sup> _δ_<sup>_α_1</sup><sup>_/α_(</sup><sup>_E_)</sup><sup>_<_</sup> _δ_ and letting _δ ↓_ 0 yields _H_<sup>_α_</sup> ( _E_ ) = 0. This proves inf _{β_ : _H_<sup>_β_</sup> ( _E_ ) = 0 _} ≤ α_ .

Remark 4.10. As Lipschitz maps increase the diameter of sets by at most a constant, the image of any set _A ⊂ E_ under a Lipschitz map has at most the Hausdorff dimension of _A_ . This observation is particularly useful for projections. _⋄_


A natural generalisation of the last remark arises when we look at the effect of H¨older continuous maps on the Hausdorff dimension.

Definition 4.11. _A function f_ : ( _E_ 1 _, ρ_ 1) _→_ ( _E_ 2 _, ρ_ 2) _between metric spaces is called α-H¨older continuous if there exists a (global) constant C >_ 0 _such that_


_The constant C is sometimes called the_ **H¨older constant** _. ⋄_

Remark 4.12. H¨older continuous maps allow some control on the Hausdorff measure of images: We show in Exercise 4.6 that, if _f_ : ( _E_ 1 _, ρ_ 1) _→_ ( _E_ 2 _, ρ_ 2) is surjective and _α_ -H¨older continuous with constant _C_ , then for any _β ≥_ 0,


and therefore dim( _E_ 2) _≤ α_<sup><u>1</u>dim(</sup><sup>_E_1).</sup>


101

**1.3. Upper bounds on the Hausdorff dimension.** We now give general upper bounds for the dimension of graph and range of functions, which are based on H¨older continuity.

Definition 4.13. _For a function f_ : _A →_ R<sup>_d_</sup> _, for A ⊂_ [0 _, ∞_ ) _, we define the_ **graph** _to be_ Graph _f_ = �( _t, f_ ( _t_ )) : _t ∈ A_ � _⊂_ R<sup>_d_+1</sup> _,_

_and the_ **range** _or_ **path** _to be_


Proposition 4.14. _Suppose f_ : [0 _,_ 1] _→_ R<sup>_d_</sup> _is an α-H¨older continuous function. Then_

**(a)** dim(Graph _f_ ) _≤_ 1 + (1 _− α_ ) � _d ∧ α_<sup><u>1</u></sup> � _,_ **(b)** _and, for any A ⊂_ [0 _,_ 1] _, we have_ dim _f_ ( _A_ ) _≤_<sup><u>dim</u></sup> _α_<sup>_<u>A.</u>_</sup>

**Proof of (a).** Since _f_ is _α_ -H¨older continuous, there exists a constant _C_ such that, if _s, t ∈_ [0 _,_ 1] with _|t − s| ≤ ε_ , then _|f_ ( _t_ ) _− f_ ( _s_ ) _| ≤ Cε_<sup>_α_</sup> . Cover [0 _,_ 1] by no more than _⌈_ 1 _/ε⌉_ intervals of length _ε_ . The image of each such interval is then contained in a ball of diameter _Cε_<sup>_α_</sup> . One can now _• either_ cover each such ball by no more than a constant multiple of _ε_<sup>_dα−d_</sup> balls of diameter _ε_ ,

- _or_ use the fact that subintervals of length ( _ε/C_ )<sup>1</sup><sup>_/α_</sup> in the domain are mapped into balls of diameter _ε_ to cover the image inside the ball by a constant multiple of _ε_<sup>1</sup><sup>_−_1</sup><sup>_/α_</sup> balls of radius _ε_ .

In both cases, look at the cover of the graph consisting of the product of intervals and corresponding balls in [0 _,_ 1] _×_ R<sup>_d_</sup> of diameter _ε_ . The first construction needs a constant multiple of _ε_<sup>_dα−d−_1</sup> product sets, the second uses _ε_<sup>_−_1</sup><sup>_/α_</sup> product sets, all of which have diameter of order _ε_ . These coverings give the required upper bounds.

**Proof of (b).** Suppose that dim( _A_ ) _< β < ∞_ . Then there exists a covering _A_ 1 _, A_ 2 _, A_ 3 _, . . ._ such that _A ⊂_<sup>�</sup> _j_<sup>_Aj_and�</sup> _j_<sup>_|Aj|β<ε_.Then</sup><sup>_f_(</sup><sup>_A_1)</sup><sup>_, f_(</sup><sup>_A_2)</sup><sup>_, . . ._isacoveringof</sup><sup>_f_(</sup><sup>_A_),and</sup> _|f_ ( _Aj_ ) _| ≤ C|Aj|_<sup>_α_</sup> , where _C_ is the H¨older constant. Thus,


as _ε ↓_ 0, and hence dim _f_ ( _A_ ) _≤ β/α._

Remark 4.15. By countable stability of Hausdorff dimension, the statements of Proposi- _⋄_ tion 4.14 remain true if we assume that _f_ : [0 _, ∞_ ) _→_ R<sup>_d_</sup> is _locally α_ -H¨older continuous.

102

We now take a first look at dimensional properties of Brownian motion and harvest the results from our general discussion so far. We have shown in Corollary 1.20 that linear Brownian motion is everywhere locally _α_ -H¨older for any _α <_ 1 _/_ 2, almost surely. This extends obviously to _d_ -dimensional Brownian motion, and this allows us to get an upper bound on the Hausdorff dimension of its range and graph.

Corollary 4.16. _The graph of a d-dimensional Brownian motion satisfies, almost surely,_


_For any fixed set A ⊂_ [0 _, ∞_ ) _, almost surely_


Remark 4.17. The corresponding _lower bounds_ for the Hausdorff dimension of Graph and Range are more subtle and will be discussed in Section 4.3, when we have more sophisticated tools at our disposal. Our upper bounds also hold for the Minkowski dimension, see Exercise 4.7, and corresponding lower bounds are easier than in the Hausdorff case and obtainable at this stage, see Exercise 4.10. _⋄_

Corollary 4.16 does not make any statement about the 2-Hausdorff measure of the range, and any such statement requires more information than the H¨older exponent alone can provide, see for example Exercise 4.9. It is however not difficult to show that


Indeed, for any _n ∈_ N, we look at the covering of _B_ ([0 _,_ 1]) by the closure of the balls


By the uniform continuity of Brownian motion on the unit interval, the maximal diameter in these coverings goes to zero, as _n →∞_ . Moreover, we have


using Brownian scaling. The expectation on the right is finite by Theorem 2.39. Hence the expected 2-value of the _n_ th covering is bounded from above by


which implies, by Fatou’s lemma, that


Hence the liminf is almost surely finite, which proves (1.1).

103

The next theorem improves upon (1.1) by showing that the 2-dimensional Hausdorff measure of the range of _d_ -dimensional Brownian motion is zero for any _d ≥_ 2. The proof is considerably more involved and may be skipped on first reading. It makes use of the fact that we have a ‘natural’ measure on Range at our disposal, which we can use as a tool to pick a good cover by cubes. The idea of using a natural measure supported by the ‘fractal’ for comparison purposes will also turn out to be crucial for the lower bounds for Hausdorff dimension, which we discuss in the next section.

Theorem* 4.18. _Let {B_ ( _t_ ): _t ≥_ 0 _} be a Brownian motion in dimension d ≥_ 2 _. Then_


**Proof.** It is sufficient to show that _H_<sup>2</sup> (Range) = 0 for _d ≥_ 3, as 2-dimensional Brownian motion is the projection of 3-dimensional Brownian motion, and projections cannot increase the Hausdorff measure of a set. Moreover it suffices to prove _H_<sup>2</sup> (Range _∩_ Cube) = 0 almost surely, for any half-open cube Cube _⊂_ R<sup>_d_</sup> of sidelength one at positive distance from the starting point of the Brownian motion. Without loss of generality we may assume that this cube is the unit cube Cube = [0 _,_ 1)<sup>_d_</sup> , and our Brownian motion is started at some _x̸ ∈_ Cube.

So let _d ≥_ 3, and recall the definition of the (locally finite) occupation measure _µ_ , defined by


Let D _k_ be the collection of all cubes<sup>�</sup><sup>_d_</sup> _i_ =1<sup>[</sup><sup>_ni_2</sup><sup>_−k,_(</sup><sup>_ni_+1)2</sup><sup>_−k_) where</sup><sup>_n_1</sup><sup>_, . . . , nd∈{_0</sup><sup>_, . . . ,_2</sup><sup>_k −_1</sup><sup>_}_.</sup> We fix a threshold _m ∈_ N and let _M > m_ . We call _D ∈_ D _k_ with _k ≥ m_ a _big_ cube if


The collection E( _M_ ) consists of all maximal big cubes _D ∈_ D _k_ , _m ≤ k < M_ , i.e. all those which are not contained in another big cube, together with all cubes _D ∈_ D _M_ which are not contained in a big cube, but intersect Range. Obviously E( _M_ ) is a cover of Range _∩_ Cube by sets of diameter smaller than _√d_ 2<sup>_−m_</sup> .

To find the expected 2-value of this cover, first look at a cube _D ∈_ D _M_ . We denote by _D_ = _DM ⊂ DM −_ 1 _⊂· · · ⊂ Dm_ with _Dk ∈_ D _k_ the ascending sequence of cubes containing _D_ . Let _Dk_<sup>_∗_bethecubewiththesamecentreas</sup><sup>_Dk_and3</sup><sup>_/_2itssidelength,seeFigure3.</sup> Let _τ_ ( _D_ ) be the first hitting time of the cube _D_ and _τk_ = inf _{t > τ_ ( _D_ ) : _B_ ( _t_ ) _̸ ∈ Dk_<sup>_∗}_bethe</sup> first exit time from _Dk_<sup>_∗_for</sup><sup>_M>k≥m_.ForthecubesCube=[0</sup><sup>_,_1)</sup><sup>_d_andChild=[0</sup><sup>_,_</sup><sup><u>1</u></sup> 2<sup>)</sup><sup>_d_we</sup> also define the expanded cubes Cube<sup>_∗_</sup> and Child<sup>_∗_</sup> and the stopping time _τ_ = inf _{t >_ 0 : _B_ ( _t_ ) _̸ ∈_ Cube<sup>_∗_</sup> _}_ . Let


104


<!-- Start of picture text -->
Dm<br>D * M D*m<br>DM<br><!-- End of picture text -->

Figure 3. Nested systems of cubes, cubes _Dk_<sup>_∗_indicatedbydashed,</sup><sup>_Dk_bysolidboundaries.</sup>

By the strong Markov property applied to the stopping times _τM < . . . < τm_ +1 and Brownian scaling,


where _τ_ ˜ _k_ is the first exit time of the Brownian motion from _Dk_<sup>_∗_andthelastinequalityfollows</sup> from Brownian scaling. Recall from Theorem 3.17 that P _x{τ_ ( _D_ ) _< ∞} ≤ c_ 2<sup>_−M_(</sup><sup>_d−_2)</sup> , for a constant _c >_ 0 depending only on the dimension _d_ and the fixed distance of _x_ from the unit cube. Hence the probability that any given cube _D ∈_ D _M_ is in our cover is P _x_ � _µ_ ( _Dk_ ) _≤_<sup><u>1</u></sup> _ε_<sup>2</sup><sup>_−_2</sup><sup>_k_forall</sup><sup>_M> k≥m,τ_(</sup><sup>_D_)</sup><sup>_< ∞_</sup> � _≤ c_ 2<sup>_−M_(</sup><sup>_d−_2)</sup> _q_<sup>_M−m_</sup> _._ Hence the expected 2-value from the cubes in E( _M_ ) _∩_ D _M_ is (1.2) _d_ 2<sup>_dM_</sup> 2<sup>_−_2</sup><sup>_M_</sup> P _x_ � _µ_ ( _Dk_ ) _≤_<sup><u>1</u></sup> _ε_<sup>2</sup><sup>_−_2</sup><sup>_k_forall</sup><sup>_M> k≥m,τ_(</sup><sup>_D_)</sup><sup>_< ∞_</sup> � _≤ cd q_<sup>_M−m_</sup> _._ The 2-value from the cubes in E( _M_ ) _∩_<sup>�</sup><sup>_m_</sup> _k_ = _M_ +1<sup>D</sup><sup>_k_isboundedby</sup>


As E _µ_ (Cube) _< ∞_ by Theorem 3.26, we infer from (1.2) and (1.3) that the expected 2-value of our cover converges to zero for _ε ↓_ 0 and a suitable choice _M_ = _M_ ( _ε_ ). Hence a subsequence converges to zero almost surely, and, as _m_ was arbitrary, this ensures that _H_<sup>2</sup> (Range) = 0 almost surely.

105

### **2. The mass distribution principle**

From the definition of the Hausdorff dimension it is plausible that in many cases it is relatively easy to give an upper bound on the dimension: just find an efficient cover of the set and find an upper bound to its _α_ -value. However it looks more difficult to give lower bounds, as we must obtain a lower bound on _α_ -values of _all_ covers of the set.

The mass distribution principle is a way around this problem, which is based on the existence of a nontrivial measure on the set. The basic idea is that, if this measure distributes a positive amount of mass on a set _E_ in such a manner that its local concentration is bounded from above, then the set must be large in a suitable sense. For the purpose of this method we call a measure _µ_ on the Borel sets of a metric space _E_ a **mass distribution** on _E_ , if


The intuition here is that a positive and finite mass is spread over the space _E_ .

Theorem 4.19 (Mass distribution principle). _Suppose E is a metric space and α ≥_ 0 _. If there is a mass distribution µ on E and constants C >_ 0 _and δ >_ 0 _such that_


_for all closed sets V with diameter |V | ≤ δ, then_


_and hence_ dim _E ≥ α._

**Proof.** Suppose that _U_ 1 _, U_ 2 _, . . ._ is a cover of _E_ by arbitrary sets with _|Ui| ≤ δ_ . Let _Vi_ be the closure of _Ui_ and note that _|Ui|_ = _|Vi|_ . We have


Passing to the infimum over all such covers, and letting _δ ↓_ 0 gives the statement.

We now apply this technique to find the Hausdorff dimension of the zero set of a linear Brownian motion. Recall that this is an uncountable set with no isolated points.

At first it is not clear what measure on Zero would be suitable to apply the mass distribution principle. Here L´evy’s theorem, see Theorem 2.31, comes to our rescue: Recall the definition of the maximum process _{M_ ( _t_ ): _t ≥_ 0 _}_ associated with a Brownian motion from Chapter 2.3.

Definition 4.20. _Let {B_ ( _t_ ): _t ≥_ 0 _} be a linear Brownian motion and {M_ ( _t_ ): _t ≥_ 0 _} the associated maximum process. A time t ≥_ 0 _is a_ **record time** _for the Brownian motion if ⋄ M_ ( _t_ ) = _B_ ( _t_ ) _and the set of all record times for the Brownian motion is denoted by_ Rec _._

Note that the record times are the zeros of the process _{Y_ ( _t_ ): _t ≥_ 0 _}_ given by

_Y_ ( _t_ ) = _M_ ( _t_ ) _− B_ ( _t_ ) _._

106

By Theorem 2.31 this process is a reflected Brownian motion, and hence its zero set and the zero set of _{B_ ( _t_ ) : _t ≥_ 0 _}_ have the same distribution. A natural measure on Rec is given by the distribution function _{M_ ( _t_ ) : _t ≥_ 0 _}_ , which allows us to get a lower bound for the Hausdorff dimension of Rec via the mass distribution principle.

Lemma 4.21. _Almost surely,_ dim(Zero _∩_ [0 _,_ 1]) = dim(Rec _∩_ [0 _,_ 1]) _≥_ 1 _/_ 2 _._

**Proof.** The first equality follows from Theorem 2.31, so that we can focus in this proof on the record set. Since _t �→ M_ ( _t_ ) is an increasing and continuous function, we can regard it as a distribution function of a positive measure _µ_ , with _µ_ ( _a, b_ ] = _M_ ( _b_ ) _− M_ ( _a_ ) _._ This measure is obviously supported on the (closed) set Rec of record times. We know that, with probability one, the Brownian motion is locally H¨older continuous with any exponent _α <_ 1 _/_ 2. Thus there exists a (random) constant _Cα_ , such that, almost surely,


for all _a, b ∈_ [0 _,_ 1]. By the mass distribution principle, we get that, almost surely,


Letting _α ↑_<sup><u>1</u></sup> 2<sup>finishestheproof.</sup>

To get an upper bound on the Hausdorff dimension of Zero we use a covering consisting of intervals. Define the collection D _k_ of intervals [ _j_ 2<sup>_−k_</sup> _,_ ( _j_ + 1)2<sup>_−k_</sup> ) for _j_ = 0 _, . . . ,_ 2<sup>_k_</sup> _−_ 1, and let _Z_ ( _I_ ) = 1 if there exists _t ∈ I_ with _B_ ( _t_ ) = 0. To estimate the dimension of the zero set we need an estimate for the probability that _Z_ ( _I_ ) = 1, i.e. for the probability that a given interval contains a zero of Brownian motion.

Lemma 4.22. _There is an absolute constant C such that, for any a, ε >_ 0 _,_


**Proof.** Consider the event _A_ = _{|B_ ( _a_ + _ε_ ) _| ≤_<sup>_√_</sup> _<u>ε}</u>_ . By the scaling property of Brownian motion, we can give the upper bound


Knowing that Brownian motion has a zero in ( _a, a_ + _ε_ ) makes the event _A_ very likely. Indeed, applying the strong Markov property at the stopping time _T_ = inf _{t ≥ a_ : _B_ ( _t_ ) = 0 _}_ , we have P( _A_ ) _≥_ P� _A ∩{_ 0 _∈ B_ [ _a, a_ + _ε_ ] _}_ � _≥_ P _{T ≤ a_ + _ε} a≤_ min _t≤a_ + _ε_<sup>P</sup><sup>_{B_(</sup><sup>_a_+</sup><sup>_ε_)</sup><sup>_≤√_</sup> _ε | B_ ( _t_ ) = 0 _}._

Clearly the minimum is achieved at _t_ = _a_ and, using the scaling property of Brownian motion, we have P _{B_ ( _a_ + _ε_ ) _≤_<sup>_√_</sup> _<u>ε | B</u>_ ( _a_ ) = 0 _}_ = P _{|B_ (1) _| ≤_ 1 _}_ =: _c >_ 0. Hence,


and this completes the proof.

107

Remark 4.23. This is only very crude information about the position of the zeros of a linear Brownian motion. Much more precise information is available, for example in the form of the arcsine law for the last sign-change, which we prove in the next section, and which (after a _⋄_ simple scaling) yields the precise value of the probability in Lemma 4.22.

We have thus shown that, for any _ε >_ 0 and sufficiently large integer _k_ , we have


for some constant _c_ 1 _>_ 0. Hence the covering of the set _{t ∈_ ( _ε,_ 1 _− ε_ ) : _B_ ( _t_ ) = 0 _}_ by all _I ∈_ D _k_ with _I ∩_ ( _ε,_ 1 _− ε_ ) _̸_ = _∅_ and _Z_ ( _I_ ) = 1 has an expected<sup><u>1</u></sup> 2<sup>-valueof</sup>


We thus get, from Fatou’s lemma,


Hence the liminf is almost surely finite, which means that there exists a family of coverings with maximal diameter going to zero and bounded<sup><u>1</u></sup> 2<sup>-value.Thisimpliesthat,almostsurely,</sup>


and, in particular, that dim(Zero _∩_ ( _ε,_ 1 _− ε_ )) _≤_<sup><u>1</u></sup> 2<sup>.As</sup><sup>_ε >_0wasarbitrary,weobtainthesame</sup> bound for the full zero set. Combining this estimate with Lemma 4.21 we have verified the following result.

Theorem 4.24. _Let {B_ ( _t_ ): 0 _≤ t ≤_ 1 _} be a linear Brownian motion. Then, with probability one, we have_


Remark 4.25. As in the case of the Brownian path, the Hausdorff measure is itself _not_ a nontrivial measure on the zero set, see Exercise 4.13. In Chapter 6 we shall construct such a measure, the local time at zero. Until then, L´evy’s identity will remain the crucial tool. _⋄_

### **3. The energy method**

The energy method is a technique to find a lower bound for the Hausdorff dimension, which is particularly interesting in applications to random fractals. It replaces the condition on the mass of all closed sets in the mass distribution principle by finiteness of an energy.

108

Definition 4.26. _Suppose µ is a mass distribution on a metric space_ ( _E, ρ_ ) _and α ≥_ 0 _. The α_ **-potential** _of a point x ∈ E with respect to µ is defined as_


_In the case E_ = R<sup>3</sup> _and α_ = 1 _, this is the Newton gravitational potential of the mass µ. The α_ **-energy** _of µ is_


The simple idea of the energy method is the following: Mass distributions with _Iα_ ( _µ_ ) _< ∞_ spread the mass so that at each place the concentration is sufficiently small to overcome the singularity of the integrand. This is only possible on sets which are large in a suitable sense.

Theorem 4.27 (Energy method). _Let α ≥_ 0 _and µ be a mass distribution on a metric space E. Then, for every ε >_ 0 _, we have_


_Hence, if Iα_ ( _µ_ ) _< ∞ then H_<sup>_α_</sup> ( _E_ ) = _∞ and, in particular,_ dim _E ≥ α._

Remark 4.28. To get a lower bound on the dimension from this method it suffices to show finiteness of a single integral. In particular, in order to show for a random set _E_ that dim _E ≥ α ⋄_ almost surely, it suffices to show that E _Iα_ ( _µ_ ) _< ∞_ for a (random) measure on _E_ .

**Proof.** Suppose that _{An_ : _n_ = 1 _,_ 2 _, . . .}_ is a pairwise disjoint covering of _E_ by sets of diameter _< ε_ . Then


Moreover, using the Cauchy-Schwarz inequality,


Dividing both sides by the integral gives the stated inequality. If E _Iα_ ( _µ_ ) _< ∞_ the integral converges to zero, so that _Hε_<sup>_α_(</sup><sup>_E_)divergestoinfinity.</sup>

We now apply the energy method to resolve questions left open in the first section of this chapter, namely the lower bounds for the Hausdorff dimension of the graph and range of Brownian motion.

109

The nowhere differentiability of linear Brownian motion established in the first chapter suggests that its graph may have dimension greater than one. For dimensions _d ≥_ 2, it is interesting to look at the range of Brownian motion. We have seen that planar Brownian motion is neighbourhood recurrent, that is, it visits every neighbourhood in the plane infinitely often. In this sense, the range of planar Brownian motion is comparable to the plane itself and one can ask whether this is also true in the sense of dimension.

Theorem 4.29 (Taylor 1953). _Let {B_ ( _t_ ): _t ≥_ 0 _} be d-dimensional Brownian motion._

- (a) _If d_ = 1 _, then_ dim Graph = 3 _/_ 2 _almost surely._

- (b) _If d ≥_ 2 _, then_ dim Range = dim Graph = 2 _almost surely._

Recall that we already know the upper bounds from Corollaries 4.16 and 4.16. We now look at lower bounds for the range of Brownian motion in _d ≥_ 2.

**Proof of Theorem 4.29(b).** A natural measure on Range is the occupation measure _µB_ defined by _µB_ ( _A_ ) = _L_ ( _B_<sup>_−_1</sup> ( _A_ ) _∩_ [0 _,_ 1]), for all Borel sets _A ⊂_ R<sup>_d_</sup> , or, equivalently,


for all bounded measurable functions _f_ . We want to show that for any 0 _< α <_ 2,

Let us evaluate the expectation


The integral can be evaluated using polar coordinates, but all we need is that it is a finite constant _c_ depending on _d_ and _α_ only. Substituting this expression into (3.1) and using Fubini’s theorem we get


Therefore _Iα_ ( _µB_ ) _< ∞_ and hence dim Range _> α_ , almost surely. The lower bound on the range follows by letting _α ↑_ 2. We also obtain a lower bound for the dimension of the graph: As the graph of a function can be projected onto the path, the dimension of the graph is at least the dimension of the path by Remark 4.10. Hence, if _d ≥_ 2, almost surely dim Graph _≥_ 2.

Now let us turn to linear Brownian motion and prove the first half of Taylor’s theorem.

**Proof of Theorem 4.29(a).** Again we use the energy method for a sharp lower bound. Recall that we have shown in Corollary 4.16 that dim Graph _≤_ 3 _/_ 2 _._ Let _α <_ 3 _/_ 2 and define a measure _µ_ on the graph by

_µ_ ( _A_ ) = _L_ 1( _{_ 0 _≤ t ≤_ 1 : ( _t, B_ ( _t_ )) _∈ A}_ ) for _A ⊂_ [0 _, ∞_ ) _×_ R Borel.

110

Changing variables, the _α_ -energy of _µ_ can be written as


Bounding the integrand, taking expectations, and applying Fubini we get that


Let p( _z_ ) = _√_ 2 _π_ _~~−~~_ 1 exp( _−z_ 2 _/_ 2) denote the standard normal density. By scaling, the expectation above can be written as


Comparing the size of the summands in the integration suggests separating _z ≤_ _~~√~~ t_ from _z > √t_ . Then we can bound (3.4) above by twice


Furthermore, we separate the last integral at 1. We get


The latter integral is of order _t_<sup>(1</sup><sup>_−α_)</sup><sup>_/_2</sup> . Substituting these results into (3.3), we see that the expected energy is finite when _α <_ 3 _/_ 2. The claim now follows from the energy method.

### **4. Frostman’s lemma and capacity**

In this section we provide a converse to the mass distribution principle, i.e. starting from a lower bound on the Hausdorff measure we construct a mass distribution on a set. This is often useful, for example if one wants to relate the Hausdorff dimension of a set and its image under some transformation.

Theorem 4.30 (Frostman’s lemma). _If A ⊂_ R<sup>_d_</sup> _is a closed set such that H_<sup>_α_</sup> ( _A_ ) _>_ 0 _, then there exists a Borel probability measure µ supported on A and a constant C >_ 0 _such that µ_ ( _D_ ) _≤ C|D|_<sup>_α_</sup> _for all Borel sets D._

We now give a proof of Frostman’s lemma, which is based on a tree representation of Euclidean space and a famous result from graph theory, the _max-flow min-cut theorem_ . The proof given here is based on the representation of compact subsets of R<sup>_d_</sup> by trees, an idea that we will encounter again in Chapter 9.

111

Definition 4.31. _A_ **tree** _T_ = ( _V, E_ ) _is a connected graph described by a finite or countable set V of_ **vertices** _, which includes a distinguished vertex ϱ designated as the root, and a set E ⊂ V × V of ordered_ **edges** _, such that_

- _for every vertex v ∈ V the set {w ∈ V_ : ( _w, v_ ) _∈ E} consists of exactly one element_ _~~v,~~ the_ **parent** _, except for the_ **root** _ϱ ∈ V , which has no parent;_

- _for every vertex v there is a unique self-avoiding path from the root to v and the number of edges in this path is the_ **order** _or_ **generation** _|v| of the vertex v ∈ V ;_

- _for every v ∈ V , the set of_ **offspring** _or_ **children** _of {w ∈ V_ : ( _v, w_ ) _∈ E} is finite. ⋄_

Notation 4.32. Suppose _T_ = ( _V, E_ ) is a tree. For any _v, w ∈ V_ we denote by _v ∧ w_ the element on the intersection of the paths from the root to _v_ , respectively _w_ with maximal order, i.e. the last common ancestor of _v_ and _w_ . The order _|e|_ of an edge _e_ = ( _u, v_ ) is the order of its end-vertex _v_ . Every infinite self-avoiding path started in the root is called a **ray** . The set of rays is denoted _∂T_ , the **boundary** of _T_ . For any two rays _ξ_ and _η_ we define _ξ ∧ η_ the vertex in the intersection of the rays, which maximises the order. Note that _|ξ ∧ η|_ is the number of edges that two rays _ξ_ and _η_ have in common. The distance between two rays _ξ_ and _η_ is defined _⋄_ to be _|ξ − η|_ := 2<sup>_−|ξ∧η|_</sup> , and this definition makes the boundary _∂T_ a metric space. Remark 4.33. The boundary _∂T_ of a tree is an interesting fractal in its own right. Its Hausdorff dimension is log2(br _T_ ) where br _T_ is a suitably defined average offspring number. This, together _⋄_ with other interesting probabilistic aspects of trees, is discussed in depth in [ **LP05** ].

Definition 4.34. _Suppose_ capacities _are assigned to the edges of a tree T , i.e. there is a mapping C_ : _E →_ [0 _, ∞_ ) _. A_ **flow** _of strength c >_ 0 _through a tree with capacities C is a mapping θ_ : _E →_ [0 _, c_ ] _such that_


_i.e. the flow into and out of each vertex other than the root is conserved._

_• θ_ ( _e_ ) _≤ C_ ( _e_ ) _, i.e. the flow through the edge e is bounded by its capacity. A set_ Π _of edges is called a_ **cutset** _if every ray includes an edge from_ Π _. ⋄_

The key to the mass distribution principle is a famous result of graph theory, the _max-flow min-cut theorem_ of Ford and Fulkerson [ **FF56** ], which we prove in Section 4 of Appendix II.

112

Theorem 4.35 (Max-flow min-cut theorem).


**Proof of Frostman’s lemma.** We may assume _A ⊂_ [0 _,_ 1]<sup>_d_</sup> . Any compact cube in R<sup>_d_</sup> of sidelength _s_ can be split into 2<sup>_d_</sup> nonoverlapping compact cubes of side length _s/_ 2. We first create a tree with a root that we associate with the cube [0 _,_ 1]<sup>_d_</sup> . Every vertex in the tree has 2<sup>_d_</sup> edges emanating from it, each leading to a vertex that is associated with one of the 2<sup>_d_</sup> subcubes with half the sidelength of the original cube. We then erase the edges ending in vertices associated with subcubes that do not intersect _A_ . In this way we construct a tree _T_ = ( _V, E_ ) such that the rays in _∂T_ correspond to sequences of nested compact cubes, see Figure 4.


<!-- Start of picture text -->
A<br><!-- End of picture text -->

Figure 4. The first two stages in the construction of the tree associated with the shaded set _A ⊂_ [0 _,_ 1]<sup>2</sup> . Dotted edges in the tree are erased.

There is a canonical mapping Φ: _∂T → A_ , which maps sequences of nested cubes to their intersection. Note that if _x ∈ A_ , then there is an infinite path emanating from the root, all of whose vertices are associated with cubes that contain _x_ and thus intersect _A_ . Hence Φ is surjective.

For any edge _e_ at level _n_ define the capacity _C_ ( _e_ ) = 2<sup>_−nα_</sup> . We now associate to every cutset Π a covering of _A_ , consisting of those cubes associated with the initial vertices of the edges in the cutset. To see that the resulting collection of cubes is indeed a covering, let _ξ_ be a ray. As Π is a cutset, it contains one of the edges in this ray, and the cube associated with the initial vertex of this edge contains the point Φ( _ξ_ ). Hence we indeed cover the entire set Φ( _∂T_ ) = _A_ . This implies that


and as _H∞_<sup>_α_(</sup><sup>_A_)</sup><sup>_>_0thisisboundedfromzero.Thus,bythemax-flowmin-cuttheorem,there</sup> exists a flow _θ_ : _E →_ [0 _, ∞_ ) of positive strength such that _θ_ ( _e_ ) _≤ C_ ( _e_ ) for all edges _e ∈ E_ .

113

We now show how to define a suitable measure on the space of infinite paths. Given an edge _e ∈ E_ we associate a set _T_ ( _e_ ) _⊂ ∂T_ consisting of all rays containing the edge _e_ . Define


It is easily checked that the collection _C_ ( _∂T_ ) of subsets _T_ ( _v_ ) _⊂ ∂T_ for all _v ∈ T_ is a semialgebra on _∂T_ . Recall that this means that if _A, B ∈C_ ( _∂T_ ), then _A ∩ B ∈C_ ( _∂T_ ) and _A_<sup>_c_</sup> is a finite disjoint union of sets in _C_ ( _∂T_ ). Because the flow through any vertex is preserved, _ν_ � is countably additive. Thus, using a measure extension theorem such as, for example [ **Du95** , A.1(1.3)], we can extend _ν_ � to a measure _ν_ on the _σ_ -algebra generated by _C_ ( _∂T_ ). We can now define a Borel measure _µ_ = _ν ◦_ Φ<sup>_−_1</sup> on _A_ , which satisfies _µ_ ( _C_ ) = _θ_ ( _e_ ), where _C_ is the cube associated with the initial vertex of the edge _e_ . Suppose now that _D_ is a Borel subset of R<sup>_d_</sup> and _n_ is the integer such that 2<sup>_−n_</sup> _< |D ∩_ [0 _,_ 1]<sup>_d_</sup> _| ≤_ 2<sup>_−_(</sup><sup>_n−_1)</sup> . Then _D ∩_ [0 _,_ 1]<sup>_d_</sup> can be covered with 3<sup>_d_</sup> of the cubes in the above construction having side length 2<sup>_−n_</sup> . Using the bound, we have


so we have a finite measure _µ_ satisfying the requirement of the lemma. Normalising _µ_ to get a probability measure completes the proof.

We define the **(Riesz)** _α_ **-capacity** of a metric space ( _E, ρ_ ) as


Theorem 4.27 states that a set of positive _α_ -capacity has dimension at least _α_ . We now show that, in this formulation the method is sharp. Our proof of this fact relies on Frostman’s lemma and hence refers to closed subsets of Euclidean space.

Theorem 4.36. _For any closed set A ⊂_ R<sup>_d_</sup> _,_


**Proof.** It only remains to show _≤_ , and for this purpose it suffices to show that if dim _A > α_ , then there exists a Borel probability measure _µ_ on _A_ such that


By our assumption for some sufficiently small _β > α_ we have _H_<sup>_β_</sup> ( _A_ ) _>_ 0. By Frostman’s lemma, there exists a nonzero Borel probability measure _µ_ on _A_ and a constant _C_ such that _µ_ ( _D_ ) _≤ C|D|_<sup>_β_</sup> for all Borel sets _D_ . By restricting _µ_ to a smaller set if necessary, we can make the support of _µ_ have diameter less than one. Fix _x ∈ A_ , and for _k ≥_ 1 let _Sk_ ( _x_ ) = _{y_ : 2<sup>_−k_</sup> _< | x − y| ≤_ 2<sup>1</sup><sup>_−k_</sup> _}_ . Since _µ_ has no atoms, we have


114

where the equality follows from the monotone convergence theorem and the inequality holds by the definition of the _Sk_ . Also,


where _C_<sup>_′_</sup> = 2<sup>2</sup><sup>_β_</sup> _C_ . Since _β > α_ , we have


which proves the theorem.

In Corollary 4.16 we have seen that the image of a set _A ⊂_ [0 _, ∞_ ) under Brownian motion has at most twice the Hausdorff dimension of _A_ . Naturally, the question arises whether this is a sharp estimate. The following result of McKean shows that, if _d ≥_ 2, this is sharp for _any_ set _A_ , while in _d_ = 1 it is sharp as long as dim _A ≤_<sup><u>1</u></sup> 2<sup>.</sup>

Theorem 4.37 (McKean 1955). _Let A ⊂_ [0 _, ∞_ ) _be a closed subset and {B_ ( _t_ ) : _t ≥_ 0 _} a d-dimensional Brownian motion. Then, almost surely,_


**Proof.** The upper bound was verified in Corollary 4.16. For the lower bound let _α <_ dim( _A_ ) _∧_ ( _d/_ 2). By Theorem 4.36, there exists a Borel probability measure _µ_ on _A_ such that _Iα_ ( _µ_ ) _< ∞_ . Denote by _µB_ the measure defined by


for all Borel sets _D ⊂_ R<sup>_d_</sup> . Then


where the second equality can be verified by a change of variables. Note that the denominator on the right hand side has the same distribution as _|t − s|_<sup>_α_</sup> _|Z|_<sup>2</sup><sup>_α_</sup> , where _Z_ is a _d_ -dimensional standard normal random variable. Since 2 _α < d_ , we have that


Hence, using Fubini’s theorem,


Thus, E[ _I_ 2 _α_ ( _µB_ )] _< ∞_ , and hence _I_ 2 _α_ ( _µB_ ) _< ∞_ almost surely. Moreover, _µB_ is supported on _B_ ( _A_ ) because _µ_ is supported on _A_ . It follows from Theorem 4.27 that dim _B_ ( _A_ ) _≥_ 2 _α_ almost surely. By letting _α ↑_ dim( _A_ ) _∧ d/_ 2, we see that dim( _B_ ( _A_ )) _≥_ 2 dim( _A_ ) _∧ d_ almost surely. This completes the proof of Theorem 4.37.

115

Remark 4.38. We have indeed shown that, if Cap _α_ ( _A_ ) _>_ 0, then Cap2 _α_ ( _B_ ( _A_ )) _>_ 0 almost surely. The converse of this statement is also true and will be discussed later, see Theorem 9.36. _⋄_

Remark 4.39. Later in the book, we shall be able to significantly improve McKean’s theorem and show that for Brownian motion in dimension _d ≥_ 2, almost surely, for any _A ⊂_ [0 _, ∞_ ), we have dim _B_ ( _A_ ) = 2 dim( _A_ ). This result is Kaufman’s theorem, see Theorem 9.28. Note the difference between the results of McKean and Kaufman: In Theorem 4.37, the null probability set depends on _A_ , while Kaufman’s theorem has a much stronger claim: it states dimension doubling simultaneously for _all_ sets. This allows us to plug in random sets _A_ , which may depend completely arbitrarily on the Brownian motion. For Kaufman’s theorem, _d ≥_ 2 is a necessary condition: we have seen that the zero set of one dimensional Brownian motion has _⋄_ dimension 1 _/_ 2, while its image is a single point.

116

### **Exercises**

Exercise 4.1 ( _∗_ ). Show that for the ternary Cantor set _C_ , we have dim _M C_ =<sup>lo</sup> log 3<sup><u>g 2</u></sup><sup>_._</sup>

Exercise 4.2 ( _∗_ ). Let _E_ := _{_ 1 _/n_ : _n ∈_ N _} ∪{_ 0 _}_ . Then dim _M E_ =<sup><u>1</u></sup> 2<sup>_._</sup>

Exercise 4.3 ( _∗_ ). Show that, for every bounded metric space, the Hausdorff dimension is bounded from above by the lower Minkowski dimension.

Exercise 4.4 ( _∗_ ). Show that Hausdorff dimension has the countable stability property.

Exercise 4.5. Show that, for the ternary Cantor set _C_ we have dim _C_ =<sup>log 2</sup> log 3<sup>.</sup>

Exercise 4.6 ( _∗_ ). If _f_ : ( _E_ 1 _, ρ_ 1) _→_ ( _E_ 2 _, ρ_ 2) is surjective and _α_ -H¨older continuous with constant _C_ , then for any _β ≥_ 0,

_H_<sup>_β_</sup> ( _E_ 2) _≤ C_<sup>_β_</sup> _H_<sup>_αβ_</sup> ( _E_ 1) _,_ and therefore dim( _E_ 2) _≤ α_<sup><u>1</u>dim(</sup><sup>_E_1).</sup>

Exercise 4.7. Suppose _f_ : [0 _,_ 1] _→_ R<sup>_d_</sup> is an _α_ -H¨older continuous function. Then

**(a)** dimM(Graph _f_ ) _≤_ 1 + (1 _− α_ ) � _d ∧ α_<sup><u>1</u></sup> <u>�, dimM</u> _A ._ **(b)** and, for any _A ⊂_ [0 _,_ 1], we have dimM _f_ ( _A_ ) _≤ α_

Exercise 4.8 ( _∗_ ). For any integer _d ≥_ 1 and 0 _< α < d_ construct a compact set _A ⊂_ R<sup>_d_</sup> such that dim _A_ = _α_ .

117

Exercise 4.9. Construct a function _f_ : [0 _,_ 1] _→_ R<sup>_d_</sup> which is _α_ -H¨older continuous for any _α < β_ , but has _H_<sup>_β_</sup> ( _f_ [0 _,_ 1]) = _∞_ .

Exercise 4.10. A function _f_ : [0 _,_ 1] _→_ R is called **reverse** _β_ **-H¨older** for some 0 _< β <_ 1 if there exists a constant _C >_ 0 such that for any interval [ _t, s_ ], there is a subinterval [ _t_ 1 _, s_ 1] _⊂_ [ _t, s_ ], such that _|f_ ( _t_ 1) _− f_ ( _s_ 1) _| ≥ C|t − s|_<sup>_β_</sup> . Let _f_ : [0 _,_ 1] _→_ R be reverse _β_ -H¨older. Then dimM(Graph _f_ ) _≥_ 2 _− β_ .

Exercise 4.11. Show that for _{B_ ( _t_ ) : 0 _≤ t ≤_ 1 _}_ we have dim _M_ Graph = 23<sup>if</sup><sup>_d_=1,and</sup> dimM Graph = dim _M B_ [0 _,_ 1] = 2 if _d ≥_ 2, almost surely.

Exercise 4.12. Show that dimM _{_ 0 _≤ t ≤_ 1 : _B_ ( _t_ ) = 0 _}_ =<sup><u>1</u></sup> 2<sup>,almostsurely.</sup>

Exercise 4.13 ( _∗_ ). Show that _H_<sup>1</sup><sup>_/_2</sup> (Zero) = 0, almost surely.

118

### **Notes and Comments**

Felix Hausdorff introduced the Hausdorff measure in his seminal paper [ **Ha19** ]. Credit should also be given to Carath´eodory [ **Ca14** ] who introduced a general construction in which Hausdorff measure can be naturally embedded. The Hausdorff measure indeed defines a measure on the Borel sets, proofs can be found in [ **Ma95** ] and [ **Ro99** ]. If _X_ = R<sup>_d_</sup> and _α_ = _d_ the Hausdorff measure _H_<sup>_α_</sup> is a constant multiple of Lebesgue measure _Ld_ , moreover if _α_ is an integer and _X_ an embedded _α_ -submanifold, then _H_<sup>_α_</sup> is the surface measure. This idea can also be used to develop vector analysis on sets with much less smoothness than a differentiable manifold. For more about Hausdorff dimension and geometric questions related to it we strongly recommend Mattila [ **Ma95** ]. The classic text of Rogers [ **Ro99** ], which first appeared in 1970, is a thorough discussion of Hausdorff measures. Falconer [ **Fa97a, Fa97b** ] covers a range of applications and current developments, but with more focus on deterministic fractals.

The results on the Hausdorff dimension of graph and range of a Brownian motion are due to S.J. Taylor [ **Ta53, Ta55** ] and independently to L´evy [ **Le51** ] though the latter paper does not contain full proofs. Taylor also proved in [ **Ta55** ] that the dimension of the zero set of a Brownian motion in dimension one is 1 _/_ 2. Stronger results show that, almost surely, the Hausdorff dimension of _all_ nontrivial level sets is 1 _/_ 2. For this and much finer results see [ **Pe81** ]. A classical survey, which inspired a lot of activity in the area of Hausdorff dimension and stochastic processes is [ **Ta86** ] and a modern survey is [ **Xi04** ].

The energy method and Frostman’s lemma all stem from Otto Frostman’s famous 1935 thesis [ **Fr35** ], which lays the foundations of modern potential theory. The elegant quantitative proof of the energy method given here is due to Oded Schramm. Frostman’s lemma was generalised to complete, separable metric spaces by Howroyd [ **Ho95** ] using a functional-analytic approach. The main difficulty arising in the proof is that, if _H_<sup>_α_</sup> ( _E_ ) = _∞_ , one has to find a subset _A ⊂ E_ with 0 _< H_<sup>_α_</sup> ( _A_ ) _< ∞_ , which is tricky to do in abstract metric spaces. Frostman’s original proof uses, in a way, the same idea as the proof presented here, though the transfer to the tree setup is not done explicitly. Probability using trees became fashionable in the 1990s and indeed, this is the right way to look at many problems of Hausdorff dimension and fractal geometry. Survey articles are [ **Pe95** ] and [ **Ly96** ], more information can be found in [ **Pe99** ] and [ **LP05** ].

McKean’s theorem is due to H.P. McKean jr. [ **McK55** ]. Its surprising extension by Kaufman is not as hard as one might think considering the wide applicability of the result. The original source is [ **Ka69** ], we discuss the result in depth in Chapter 9.

The concept of ‘reverse H¨older’ mappings only partially extends from Minkowski to Hausdorff dimension. If _f_ : [0 _,_ 1] _→_ R is both _β_ -H¨older and reverse _β_ -H¨older for some 0 _< β <_ 1, it satisfies dim(Graph _f_ ) _>_ 1, see Przytycki and Urba´nski [ **PU89** ]. For example, the Weierstrass nowhere differentiable function, defined by _W_ ( _t_ ) =<sup>�</sup><sup>_∞_</sup> _n_ =0<sup>_an_cos(</sup><sup>_bnt_)</sup><sup>_,_for</sup><sup>_ab>_1,0</sup><sup>_<a<_1is</sup> _β_ -H¨older and reverse _β_ -H¨older for some 0 _< β <_ 1. The Hausdorff dimension of its graph is, however, not rigorously known in general.

119

There is a natural refinement of the notions of Hausdorff dimension and Hausdorff measure, which is based on evaluating sets by applying an arbitrary ‘gauge’ function _ϕ_ to the diameter, rather than taking a power. Measuring sets using a gauge function not only allows much finer results, it also turns out that the natural measures on graph and range of Brownian paths, which we have encountered in this chapter, turn out to be Hausdorff measures for suitable gauge functions. Results in this direction are [ **CT62, Ra63a, Ta64** ] and we include elements of this discussion in Chapter 6, where the zero set of Brownian motion is considered.

120

### CHAPTER 5

---

[← Harmonic functions, transience and recurrence](07-harmonic-functions-transience-and-recurrence.md) · [Up: contents](index.md) · [Brownian motion and random walk →](09-brownian-motion-and-random-walk.md)
