---
title: 25 Lecture Twenty Five
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 25 Lecture Twenty Five

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **25.1 Recap: Last Class**

In the last lecture, we looked at the Central Limit Theorem:

**Theorem 25.1** (Central Limit Theorem) **.** _Suppose Xi, i_ = 1 _,_ 2 _, . . . are i.i.d with_ E( _Xi_ ) = _µ and var_ ( _Xi_ ) = _σ_<sup>2</sup> _< ∞. Then, with X_<sup>¯</sup> _n_ = ( _X_ 1 + _· · ·_ + _Xn_ ) _/n,_


_converges in distribution to N_ (0 _,_ 1) _. Convergence in distribution here means that_


We also discussed the usefulness of transforms for proving the CLT, and proved it using the Laplace Transform (MGF) by showing that


This proof suffers from the following two deficiencies:

1. It tacitly assumes that the moment generating function of _X_ 1 _, . . . , Xn_ exists for all _t_ . This is much stronger than the existence of the variance of _Xi_ (which is all the CLT needs). Indeed if _MX_ ( _t_ ) exists for all _t_ in any open interval containing zero, then moments of all orders (not just the variance) exist.


for _−∞≤ a < b ≤∞_ .

To fix these two deficiencies, the Fourier transform (or Characteristic Function) is used to prove the CLT.

128

### **25.2 CLT proof via the Fourier Transform**

Recall, from the last lecture, that the Fourier transform of a random variable _X_ is defined as the function:


for all _t ∈_ ( _−∞, ∞_ ). Here _i_ =<sup>_√_</sup> _−_ 1. The Fourier transform is defined for every random variable and it is finite for all _t ∈_ ( _−∞, ∞_ ). This is because cos( _tX_ ) and sin( _tX_ ) are always bounded by 1 so the expectation will obviously be finite. Just like the Laplace transform, the Fourier transform also factorizes for independent random variables. Specifically, if _X_ 1 _, . . . , Xn_ are independent, then


As a consequence, if _X_ 1 _, . . . , Xn_ are i.i.d,


A sketch of the proof of the CLT via the Fourier transform is provided below. I will skip some technical details and provide only the high level ideas. Full details can be found, for example, in Chapter 6 of the book _A Course in Probability Theory_ by Kai Lai Chung.

_Fourier Proof of CLT._ We have i.i.d random variables _X_ 1 _, X_ 2 _, . . ._ which have mean _µ_ and finite variance _σ_<sup>2</sup> . Let _Yn_ :=<sup>_√_</sup> _<u>n</u>_ <u>(</u> _X_<sup>¯</sup> _n − µ_ ) _/σ_ . We shall first prove that the Fourier transform of _Yn_ converges to that of _N_ (0 _,_ 1):


The Fourier transform of _N_ (0 _,_ 1) equals

We will show that

_ϕYn_ ( _t_ ) _→ e_<sup>_−t_2</sup><sup>_/_2</sup> for every _t._

Because


we can write,


where _ϕ_ ( _·_ ) is the Fourier transform of ( _X_ 1 _− µ_ ) _/σ_ . We now use Taylor’s theorem to expand _ϕ_ ( _tn_<sup>_−_1</sup><sup>_/_2</sup> ) up to a quadratic polynomial around 0:


It is easy to check that, for every random variable _R_ , we have _ϕR_ (0) = E _e_<sup>_i_(0)</sup><sup>_R_</sup> = 1. Also


129

Plugging in _t_ = 0, we get


Using _R_ = ( _X_ 1 _− µ_ ) _/σ_ (which has mean zero and unit variance) and _ϕ_ = _ϕR_ , we get


Therefore


as _n →∞_ . This proves that the Fourier transform of _Yn_ converges to that of _N_ (0 _,_ 1). From here, we now need to deduce that


This statement is equivalent to


where _I_ $$ _a,b_ $$( _x_ ) := _I{a ≤ x ≤ b}_ is the indicator function of the interval [ _a, b_ ]. How does this follow from the convergence of the Fourier transforms:


The idea is that Fourier analysis guarantees that the indicator function can be represented as a linear combination of the complex functions _e_<sup>_itx_</sup> . This representation is of the form:


for some function _g_ . From here, one can write


which proves (121). For a rigorous version of this argument, see Chapter 6 of the book _A Course in Probability Theory_ by Kai Lai Chung.

### **25.3 Closing Thoughts**

In this class, we took the view that probability is a general and principled method of reasoning under uncertainty. Here is a quote by Jaynes (from one of his papers in 1957): _the purpose of any application of probability theory is simply to help us in forming reasonable judgements_

130

_in situations where we do not have complete information_ . Hopefully, this course convinced you that probability theory applies to many problems that are commonly studied in the fields of statistics and machine learning (what is usually called “Bayesian Statistics” is just Probability Theory). I would like to leave you with a couple of quotes by Laplace (from the book _A Philosophical Essay on Probabilities_ by Pierre Simon Laplace) glorifying probability theory. Laplace was one of the founders of probability theory and Bayesian statistics:

1. _It is remarkable that a science, which commenced with a consideration of the games of chance, should be elevated to the rank of the most important subjects of human knowledge._

2. _If we consider_

   - _a) the analytical methods to which this theory has given birth;_

   - _b) the truth of the principles which serve as a basis;_

   - _c) the fine and delicate logic which their employment in the solution of problems requires;_

   - _d) the establishments of public utility which rest upon it;_

   - _e) the extension which it has received and which it can still receive by its application to the most important questions of natural philosophy and the moral science;_

_if we consider again_

- _a) that, even in the things which cannot be submitted to calculus, it gives the surest hints which can guide us in our judgements, and_

- _b) that it teaches us to avoid the illusions which offtimes confuse us,_

_then we shall see that there is no science more worthy of our meditations, and that no more useful one could be incorporated in the system of public instruction._

---

[← 24 Lecture Twenty Four](25-24-lecture-twenty-four.md) · [Up: contents](index.md) · [References →](27-references.md)
