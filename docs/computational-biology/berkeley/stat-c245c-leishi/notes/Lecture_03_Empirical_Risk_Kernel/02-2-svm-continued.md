---
title: 2 SVM-continued
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_03_Empirical_Risk_Kernel.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_03_Empirical_Risk_Kernel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 SVM-continued

**Source:** [`notes/Lecture_03_Empirical_Risk_Kernel.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_03_Empirical_Risk_Kernel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **2.1 Dual problem of SVM**

Let’s now circle back to the (primal) SVM optimization problem defined in last class:


Borrowing the notation from the previous section, the inequality constraints are


Since there is no equality constraint in the problem (3), the Lagrangian for our optimization problem is


By checking the conditions listed in the previous section, there is no duality gap between the primal problem (3) and its dual. To get the dual problem of (3), we following the steps introduced in the last section:

1. Find the Lagrange dual function associated with (3):


To to do, we take derivative with respect to w and _a_ :


constraint _gi_ are (strictly) feasible–meaning that there exists some w such that _gi_ (w) _<_ 0 for all _i_ . Note there are many different sets of sufficient conditions can be found in the literature.

3

2. We now take the definition of w in (5) and plug it back into the equation (4):


3. **SVM dual problem** : Dual problem associated with the primal problem (3) is thus


4. **Primal and dual relationship** : Suppose we can solve the dual problem (for now) and the optimal solution is _ν_<sup>_∗_</sup> , then we can obtain the primal solution from (5)


how about the intercept _a_<sup>_∗_</sup> ?

We want to resolves several issues in SVM by working out the dual formulation: First, what does _νi_<sup>_∗_= 0tellus?RecallfromtheKKTcondition,wemusthave(thisspecificconditionis</sup> also called KKT dual complementarity condition)


It says that if _νi_<sup>_∗>_0,then</sup><sup>_Yi_(</sup><sup>_a_+ w</sup><sup>_′Xi_)</sup><sup>_−_1 = 0,meaning that</sup><sup>_i_th data point is a support vector.Whenever</sup> _νi_<sup>_∗_= 0,wehavethesamplepair(</sup><sup>_Yi, Xi_)doesnotliveonthedecisionboundary.</sup>

Second, when we make prediction at a new data point _x ∈_ R<sup>_d_</sup> , we would then calculate w<sup>_∗′_</sup> _x_ + _a_<sup>_∗_</sup> and then predict


Notice that the quantity w<sup>_∗′_</sup> _x_ + _a_<sup>_∗_</sup> can be rewritten as


4

Now we can see that decision made from SVM is also quite intuitive: if the new data point _x_ is more “similar” to the support vectors labelled as one–hence there is a higher “chance” that<sup>�</sup> _i_ : _νi̸_ =0<sup>**1**(</sup><sup>_Y_</sup> _i_<sup>=1)</sup><sup>_X_</sup> _i_<sup>_′x >_</sup> � _i_ : _νi̸_ =0<sup>**1**(</sup><sup>_Y_</sup> _i_<sup>=</sup><sup>_−_1)</sup><sup>_X_</sup> _i_<sup>_′x_–therebyitclassifies</sup><sup>_x_as1.Canthismotivateyoutoclassifysampleinadifferent</sup> way?

By examining the dual form of the optimization problem, we gained significant insight into the structure of the problem, and were also able to write the entire algorithm in terms of only inner products between input feature vectors. In the next section, we will exploit this property to apply the kernels to our classification problem. The resulting algorithm, support vector machines, will be able to efficiently learn in very high dimensional spaces.

### **2.2 Kernel SVM**

From our drug dosage example, we can transform our original input _attributes_ to new _features_ as in Figure 1.


Figure 1: Can SVM be used to predict the drug-effective outcome? Yes!

Let’s formalize this transformation. Let _φ_ denote the _feature mapping_ , which maps from the attributes to the features. For instance, in our example, we use


Rather than applying SVMs using the original input attributes _x_ , we may instead want to learn using some features _φ_ ( _x_ ). To do so, we simply need to go over our previous algorithm, and replace _Xi_ everywhere in it with _φ_ ( _Xi_ ).

Since the SVM dual problem (7) solely works with the inner products _⟨Xi, Xj⟩_ , this means that we would replace all those inner products with _⟨φ_ ( _Xi_ ) _, φ_ ( _Xj_ ) _⟩_ . More specifically, given a feature mapping _φ_ , we define its corresponding _Kernel_ to be


Then, everywhere we previously had _⟨Xi, Xj⟩_ , we could simply replace it with _K_ ( _Xi, Xj_ ) and our algorithm would now be learning using the feature mapping _φ_ .

5

Suppose _x, z ∈X ⊆_ R<sup>_d_</sup> , given a feature mapping _φ_ , we could easily compute _K_ ( _x, z_ ) by finding _φ_ ( _x_ ), _φ_ ( _z_ ) and taking their inner product. But what’s more interesting is that, very often, _K_ ( _x, z_ ) is very inexpensive to calculate, even though _φ_ ( _x_ ) itself may be very expensive to calculate. In such setting, kernel SVM incorporates easy-to-compute kernel function _K_ ( _x, z_ ), and hence can learn in high-dimensional feature space (given by _φ_ ) without having to explicitly find or represent _φ_ ( _x_ ).

**Example 1** (Degree- _p_ polynomials kernel) **.** _For two input attributes defined in the attribute space X , x, z ∈ X ⊆_ R<sup>_d_</sup> _, we consider a Kernel_


_When p_ = 2 _, we have_


_This means if we direct work with the original feature mapping, we have to work with a long feature vector. Take d_ = 3 _for example:_


More broadly speaking, the degree- _p_ kernel _K_ ( _x, z_ ) = ( _x_<sup>_′_</sup> _z_ + _c_ )<sup>_p_</sup> corresponds to a feature mapping to an � _p_ + _d d_ � _−_ dimensional feature space. Such a feature space is spanned by all monomials of the _xi_ 1 _, . . . xik_ that are up to order _p_ – thus this is a space of order _d_<sup>_p_</sup> . Nevertheless, computing _K_ ( _x, z_ ) takes only _O_ ( _d_ ) time. Hence, we never need to explicitly represent feature vector in this very high-dimensional feature space.

Although the above description sounds mathematically complex, the kernel function is essentially measuring the similarity between two input attributes _x_ and _z_ . As long as you come up with some function _K_ ( _x, z_ ) that you think might be a reasonable measure of how similar _x_ and _z_ are, it would be a reasonable kernel. Another popular choice is the Gaussian Kernel:

**Example 2** (Gaussian Kernel) **.** _For two input attributes defined in the attribute space X , x, z ∈X ⊆_ R<sup>_d_</sup> _, we consider a Kernel_


6

This Gaussian kernel corresponds to an infinite dimensional feature mapping _φ_ . But think about more broadly, given some random function _K_ , how can we tell if it is a valid kernel? In other words, can we tell if there exist a feature mapping _φ_ so that _K_ ( _x, z_ ) = _φ_ ( _x_ )<sup>_′_</sup> _φ_ ( _z_ ) for all _x, z_ ? This requires us to understand the Mercer’s Theorem. If you are interested, you can take a look at Chapter 14.2 in Murphy (2012).

Keep in mind however that the idea of kernels has significantly broader applicability than SVMs. Specifically, if you have any learning algorithm that you can write in terms of only inner products _⟨x, z⟩_ between input attribute vectors, then by replacing this with _K_ ( _x, z_ ) where _K_ is a kernel, you can “magically” allow your algorithm to work efficiently in the high dimensional feature space corresponding to _K_ .

Lastly, to end this section on the support vector machines, we summarize its primal and dual problems:


and the dual problem


where _K_ ( _Xi, Xj_ ) = _⟨φ_ ( _Xi_ ) _, φ_ ( _Xj_ ) _⟩_ . The primal and dual solution can be linked by


### **2.3 A short story of SVM**

The very first paper on the support vector machines with kernels is published in 1992; see Boser et al. (1992). You can read a short story on this webpage.

---

[← 1 Lagrange duality](01-1-lagrange-duality.md) · [Up: contents](index.md) · [3 Empirical Risk Minimization →](03-3-empirical-risk-minimization.md)
