---
title: 14 Lecture 14
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 14 Lecture 14

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **14.1 Recap of the main rate theorem**

_θ_ ˆ _n_ maximizes a stochastic process _Mn_ ( _θ_ ) over _θ ∈_ Θ while _θ_ 0 maximizes a deterministic process _M_ ( _θ_ ) over _θ ∈_ Θ. Assume that _d_ ( _·, ·_ ) is such that


for all _θ ∈_ Θ. Let _φn_ ( _·_ ) be a function satisfying a mild condition (there exists _α <_ 2 such that _φn_ ( _cx_ ) _≤ c_<sup>_α_</sup> _φn_ ( _x_ )) such that


for all _u >_ 0. Then the random quantity _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) will be controlled by _δn_ for every _δn_ satisfying


Formally, we have


Here are some strengths and weaknesses of this theorem. Let us start with the strengths:

1. It rigorizes the heuristic argument well. Indeed, the heuristic argument starts with the basic inequality:


From here, it is easy to derive that _δ_<sup>ˆ</sup> _n_ := _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) satisfies


From here, it is reasonable to conjecture that the _d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) will be controlled by any _δn_ satisfying


The theorem basically proves this if the ≲ inequality above is changed to ≳. This also suggests that the rate obtained by solving _φn_ ( _δn_ ) _∼ δn_<sup>2shouldbethecorrectratefor</sup><sup>_d_(ˆ</sup><sup>_θn, θ_0).</sup>

71

2. It is very general. The theorem is quite general and applies to a variety of problems. We have already seen examples of this and we shall some more examples in the near future.

3. It is very simple to prove. The proof is only a few lines long and does not use any complicated machinery.

Here are some important weaknesses of the rate theorem.

1. The most important weakness is that, although the rate obtained is usually correct, the deviation inequaiity (115) is usually quite weak. To see this, observe that when _α_ = 1 (for example), inequality (115) becomes


from which it follows that


for all _t_ . This inequality is quite weak in the sense that it does not even imply that


The main reason for the looseness comes from the use of Markov’s inequality in the proof:


This inequality is quite loose. More sophisticated arguments (under more specialized settings) can be used in place of this and these give improved bounds for P _{d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) _> tδn}_ . We shall see some examples of such improved results later.

2. Calculating the rate via the theorem requires one to bound


Although there exist general techniques for this, getting good bounds in specific situations can still be quite hard.

We shall next apply the rate theorem for understanding the loss behavior of convex penalized least squares estimators in the Gaussian sequence model. Before that, let us first introduce the Gaussian sequence model.

## **14.2 The Gaussian Sequence Model**

The (finite) Gaussian Sequence Model is an important model for studying the theoretical performance of many commonly used statistical procedures. For a comprehensive treatment of estimation theory under the Gaussian sequence model, see Johnstone [11].

Suppose we observe real-valued observations _Y_ 1 _, . . . , Yn_ . Under the Gaussian sequence model, we model the observed data as


where _ϵ_ 1 _, . . . , ϵn_ are i.i.d _N_ (0 _,_ 1). In other words, _ϵ ∼ N_ (0 _, In_ ) and _Y ∼ N_ ( _θ_<sup>_∗_</sup> _, In_ ). The goal is to estimate _θ_ 1<sup>_∗, . . . , θ_</sup> _n_<sup>_∗_fromdata</sup><sup>_Y_1</sup><sup>_, . . . , Yn_underthelossfunction:</sup>


72

The _risk_ of an estimator _θ_<sup>ˆ</sup> will be defined as


Usually one imposes some additional structure on the unknown parameters _θ_ 1<sup>_∗, . . . , θ_</sup> _n_<sup>_∗_.Here are some standard</sup> examples of such additional structure:

1. **No Structure** : In this case, no information is available on _θ_ 1<sup>_∗, . . . , θ_</sup> _n_<sup>_∗_.Itisintuitivelyclearthenthat</sup> one cannot do much better than the simple estimator _θ_<sup>ˆ</sup> _i_ = _Yi, i_ = 1 _, . . . , n_ . The risk of this estimator clearly equals 1. It turns out that


This means that the simple estimator _Y_ is minimax optimal over R<sup>_n_</sup> (or equivalently, the worst case risk over _θ ∈_ R<sup>_n_</sup> of every other estimator is at least 1).

2. **Fixed Linear Subspace** : Here it is assumed that _θ_<sup>_∗_</sup> _∈ S_ for a known linear subspace _S_ . In this case, the most natural estimator is the projection of _Y_ onto _S_ . This estimator has risk _k/n_ where _k_ is the dimension of _S_ . The minimax risk over _S_ equals _k/n_ i.e.,


3. **Smoothness** : Suppose _θ_<sup>_∗_</sup> = ( _f_<sup>_∗_</sup> (1 _/n_ ) _, . . . , f_<sup>_∗_</sup> (1)) for some function _f_<sup>_∗_</sup> : [0 _,_ 1] _→_ [ _−_ 1 _,_ 1] which is 1- Lipschitz. In the last class, we saw that if we consider the estimator _θ_<sup>ˆ</sup> = ( _f_<sup>ˆ</sup> (1 _/n_ ) _, . . . , f_<sup>ˆ</sup> (1)) where _f_<sup>ˆ</sup> is any least squares estimator over the class of all 1-Lipschitz functions that are bounded by 1, then


It is possible to also prove that the above bound also holds in expectation i.e.,


It turns out that _n_<sup>_−_2</sup><sup>_/_3</sup> is actually the minimax risk over the class of all vectors ( _f_ (1 _/n_ ) _, . . . , f_ (1)) where _f_ : [0 _,_ 1] _→_ [ _−_ 1 _,_ 1] is 1-Lipschitz. We shall prove this later. The estimator _θ_<sup>ˆ</sup> is actually non-linear. However it is possible to achieve the risk _n_<sup>_−_2</sup><sup>_/_3</sup> also with a linear estimator based on local averaging of _Y_ 1 _, . . . , Yn_ .

4. **Sparsity** : Suppose the vector _θ_<sup>_∗_</sup> is sparse in the sense that only a few of its entries are non-zero. More precisely assume that _θ_<sup>_∗_</sup> _∈_ Θ _k_ where Θ _k_ is the class of all vectors in R<sup>_n_</sup> which have at most _k_ non-zero entries. Assume that _k_ is small compared to _n_ (specifically, assume that _k/n →_ 0 as _n →∞_ ). In this case, there exist estimators _θ_<sup>ˆ</sup> which satisfy


It can be proved that the minimax risk over Θ _k_ also equals the right hand side above (we shall prove this later). The estimator _θ_<sup>ˆ</sup> achieving (116) can be taken to be LASSO or soft-thresholding with an appropriate choice of the tuning parameter. This is an M-estimator that can be studied via the rate theorem. We shall do this later.

5. **Low Rank Structure** : Suppose _θ_<sup>_∗_</sup> is the vectorization of a _d × d_ matrix _A_<sup>_∗_</sup> with _n_ = _d_<sup>2</sup> . Suppose it is assumed that _A_<sup>_∗_</sup> is rank at most _r_ . Then a penalized estimator based on penalizing the nuclear norm (sum of singular values) can be shown to be minimax optimal.

73

## **14.3 Convex Penalized Estimators in the Gausssian Sequence Model**

In the Gaussian sequence model _Y_ = _θ_<sup>_∗_</sup> + _ϵ_ with _ϵ ∼ N_ (0 _, In_ ), a very standard class of estimators is given by estimators of the form:


where _f_ : R<sup>_n_</sup> _→_ R is a convex function and _λ >_ 0 is an appropriate tuning parameter. The function _f_ will be the _L_<sup>1</sup> norm of _θ_ when we believe that the true signal is sparse and will be the nuclear norm of the matrix corresponding to _θ_ under a low rank assumption. Other functions _f_ are also used (such as _f_ ( _θ_ ) :=<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_−_1</sup><sup>_|θi −θi−_1</sup><sup>_|_forpiecewiseconstantstructure).</sup>

The estimator (117) is obviously an _M_ -estimator so we can use our general rate theorem to study:


For this, we first write (using _Y_ = _θ_<sup>_∗_</sup> + _ϵ_ ),


Therefore, we can write


We can therefore apply the rate theorem with Θ = R<sup>_n_</sup> and


Note that _M_ ( _θ_ ) is maximized at _θ_<sup>_∗_</sup> and the condition


is trivially satisfied when


We can therefore apply the rate theorem which will require us to bound the expectation of


We now bound this term in the following way. Because _f_ is convex, for every subgradient _s_ of _f_ at _θ_<sup>_∗_</sup> , we have


As a result,


74

where, in the last inequality above, we used the Cauchy-Schwarz inequality. Note that the above is true for every subgradient _s_ of _f_ at _θ_<sup>_∗_</sup> . The set of all subgradients of _f_ at _θ_<sup>_∗_</sup> is called the subdifferential of _f_ at _θ_<sup>_∗_</sup> and is denoted by _∂f_ ( _θ_<sup>_∗_</sup> ). Because the above chain of inequalities is true for every _s ∈ ∂f_ ( _θ_<sup>_∗_</sup> ), we can take an infimum over _s ∈ ∂f_ ( _θ_<sup>_∗_</sup> ) which allows us to deduce that


and thus


The rate theorem therefore implies that ��� _θ_ ˆ _λ,f − θ∗_ ��� is controlled by _δn_ which solves


which means that we can take


The precise inequality given by the rate theorem for bounding ��� _θ_ ˆ _λ,f − θ∗_ ��� via _δn_ is slightly weak (as mentioned earlier, this happens in quite a few situations). However, in this context, it can be proved (see Oymak and Hassibi [17]) that


I will include a sketch of the proof of this inequality in the homework. Inequality (118) implies that if _∂f_ ( _θ_<sup>_∗_</sup> ) is a large set in R<sup>_n_</sup> , then the risk of _θ_<sup>ˆ</sup> _λ,f_ will be small. Note that inequality (118) holds for every convex function _f_ so it is applicable in a variety of situations. In the next section, we shall demonstrate its use for studying risks in sparse signal estimation.

### **14.3.1 Application of inequality** (118) **for sparse signal estimation**

We shall now apply the inequality (118) to the case when _f_ ( _θ_ ) = _|θ_ 1 _|_ + _· · ·_ + _|θn|_ is the _L_<sup>1</sup> norm of _θ_ . For a fixed _λ_ , we need to bound the squared expected distance of a standard Gaussian vector _ϵ_ to _λ∂f_ ( _θ_<sup>_∗_</sup> ). The first step is to obtain a characterization of _∂f_ ( _θ_<sup>_∗_</sup> ). It is straightforward to see that _∂f_ ( _θ_<sup>_∗_</sup> ) consists of all vectors ( _v_ 1 _, . . . , vn_ ) _∈_ R<sup>_n_</sup> such that


As a result, _λ∂f_ ( _θ_<sup>_∗_</sup> ) consists of all vectors ( _v_ 1 _, . . . , vn_ ) _∈_ R<sup>_n_</sup> such that


As a result,


75

where _pλ_ ( _ϵi_ ) is the point in the interval [ _−λ, λ_ ] that is closest to _ϵi_ . It is now easy to see that


This function above has a name and it is called the soft thresholding of _ϵi_ with level _λ_ . We thus have


We have thus obtained:


where _k_ is the number of non-zero entries in _θ_<sup>_∗_</sup> . To proceed further, we need to compute E [soft _λ_ ( _ϵ_ 1)]<sup>2</sup> which we shall do in the next class.

---

[← 13 Lecture 13](14-13-lecture-13.md) · [Up: contents](index.md) · [15 Lecture 15 →](16-15-lecture-15.md)
