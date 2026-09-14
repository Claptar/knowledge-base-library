---
title: 17 Lecture 17
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 17 Lecture 17

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We will study the prediction risk of the estimator:


in the linear regression model _Y_ = _Xθ_<sup>_∗_</sup> + _ϵ_ where _ϵ ∼ N_ (0 _, In_ ). Recall that this is the Hard Thresholding estimator when _X_ = _In_ . The following result will be true for _θ_<sup>ˆ</sup> _λ_<sup>BIC</sup> : If


for a sufficiently large _c_ 1, then


86

We shall not prove the expectation bound given above but we shall use the rate theorem which will imply that the loss ��� _X_ ˆ _θλ_ BIC _− Xθ_<sup>_∗_��</sup> � will be bounded by a constant multiple of � _k_ log( _ep_ ) with high probability. Before we proceed to this argument, let us recall first that in the last lecture, we proved


Note that this estimator _θ_<sup>ˆ(</sup><sup>_k_)</sup> can be viewed as a constrained version of _θ_<sup>ˆ</sup> _λ_<sup>BIC</sup> . In the process of proving (143), we derived that


We shall use this inequality in the sequel. Now let us proceed to analyze _λ_ ��� _X_ ˆ _θ_ BIC _− Xθ_<sup>_∗_��</sup> � via the rate theorem. Note first that _θ_<sup>ˆ</sup> _λ_<sup>BIC</sup> maximizes


So we shall apply the rate theorem with this _Mn_ ( _θ_ ) and _M_ ( _θ_ ) taken to be


Also _d_ ( _θ, θ_<sup>_∗_</sup> ) := _∥Xθ − Xθ_<sup>_∗_</sup> _∥_ . For applying the rate theorem, we would need to bound


from above and equate the resulting bound to _u_<sup>2</sup> . For this, note that


Let us denote the two terms above by Γ1 and Γ2 respectively. To bound Γ1, note that for every 1 _≤ s ≤ p_ , the map


is 2 _u_ -Lipschitz so by the Gaussian concentration inequality from last time, we have


for every _a >_ 0. As a result, we have


For bounding Γ2, we simply use inequality (144) to obtain


87

Thus by enlarging the constant _C_ appropriately, we have


We just maximize the above function in terms of _s_ by calculus. Setting _s_ to be such that


we obtain


Choosing _λ_ = _c_ 1 ~~�~~ log( _ep_ ), we obtain


Now if _c_ 1 = _C_<sup>2</sup> _/_ 2, then we obtain the equation


which gives


This, therefore, proves that ��� _X_ ˆ _θλ_ BIC _− Xθ_<sup>_∗_��</sup> � will be controlled by ~~�~~ _k_ log( _ep_ ) with high probability. This argument does not yield the expecation bound (142) which can be proved a modification of the above argument.

Here are two comments on (142):

1. It requires no assumptions on the design matrix _X_ .

2. If _λ_ is allowed to depend on _k_ , then it is possible to derive the bound ( _k/n_ ) log( _ep/k_ ) (i.e., log( _ep_ ) in (142) can be replaced by log( _ep/k_ )) (see, Johnstone [11, Chapter 11]).

## **17.2 Prediction Risk of** _θ_<sup>ˆLASSO</sup> _λ_

We now study the LASSO estimator:


We shall prove two bounds on the prediction error


The first bound involves _∥θ_<sup>_∗_</sup> _∥_ 1 (weak or approximate sparsity regime) and the second bound involves _∥θ_<sup>_∗_</sup> _∥_ 0 (strong or exact sparsity regime)

88

### **17.2.1 Weak Sparsity Bound**

Here we shall prove the following bound for the prediction risk of _θ_<sup>ˆ</sup> _λ_<sup>LASSO</sup> . Let _X_ 1 _, . . . , Xp ∈_ R<sup>_n_</sup> denote the _p_ columns of the _n × p_ design matrix _X_ . If


for a sufficiently large _c_ 1, then


for a constant _C_ ( _c_ 1) depending only on _c_ 1.

Note that this bound specializes to our earlier bound for soft thresholding if we take _X_ = _In_ . Usually, the scaling for the design matrix is chosen so that max1 _≤i≤p ∥Xi∥≤_<sup>_√_</sup> _<u>n</u>_ <u>.</u> Under this assumption, the choice of the tuning parameter becomes


and the prediction risk bound (147) becomes


We shall now prove (147). Note first that _θ_<sup>ˆ</sup> _λ_<sup>LASSO</sup> maximizes _Mn_ ( _θ_ ) over _θ ∈_ R<sup>_p_</sup> where


It is also easy to see that _θ_<sup>_∗_</sup> maximizes _M_ ( _θ_ ) _, θ ∈_ R<sup>_p_</sup> where


The basic inequality therefore is


which becomes

We shall bound the term involving _ϵ_ on the right hand side above via

which gives

Triangle inequality:

now gives

Therefore if _λ_ is chosen so that

then we would obtain

When the tuning parameter _λ_ is chosen as in (146), it is easy to see that (149) holds with high probability and then inequality (147) follows from the above inequality (rigorize this argument and complete the proof of (147)).

89

### **17.2.2 Strong Sparsity Bound**

We shall now attempt to bound the prediction error in terms of _∥θ_<sup>_∗_</sup> _∥_ 0 = _k_ . Before proceeding further, let us introduce the following notation. Let _S_ denote the set of indices _i_ among 1 _, . . . , p_ where _θi_<sup>_∗_</sup> _̸_<sup>=0.Then</sup> _|S|_ = _k_ . For a vector _θ ∈_ R<sup>_n_</sup> , let _θS ∈_ R<sup>_n_</sup> denote the vector whose _i_<sup>_th_</sup> entry equals _θi_ if _i ∈ S_ and equals 0 if _i ∈/ S_ . We analogously define _θSc_ . Let us start with inequality (148) (where, for simplicity of notation, we write _θ_<sup>ˆ</sup> for _θ_<sup>ˆ</sup> _λ_<sup>LASSO</sup> )


We rewrite the right hand side above as

Because _θS_<sup>_∗c_= 0,wecansimplifythisas</sup>

Rearranging terms, we deduce

The last two terms can be bounded by triangle inequality as


and so we obtain

Suppose now that we assume that the regularization parameter _λ_ satisfies (149) as before. We can then cancel the terms _λ_ ��� _θ_ ˆ _Sc_ ���1<sup>and</sup> �� _X T ϵ_ �� _∞_ ��� _θ_ ˆ _Sc_ ���1<sup>frombothsidesoftheinequalityabovetoobtain</sup>


Applying the Cauchy-Schwarz inequality on the right hand side, we get


Further

This gives (from (151))


90

Cancelling one ��� _X_ ˆ _θ − Xθ∗_ ���, we obtain


We can now take _λ_ to be as in (146) which ensures (149) with high probability (if _c_ 1 is sufficiently large) which implies that


with high probability (expecation bound can be derived as well). When _X_ = _In_ , this is a weaker form of our earlier soft-thresholding risk bound for exact sparsity. However, a major problem of this bound is that it depends on _λ_ min( _X_<sup>_T_</sup> _X/n_ ). When _p > n_ , we necessarily have _λ_ min( _X_<sup>_T_</sup> _X/n_ ) = 0 so that the above bound is vacuous. It is however to replace _λ_ min( _X_<sup>_T_</sup> _X/n_ ) by a smaller quantity by a slight tweak on the above argument with _λ_ chosen to be 2 �� _X T ϵ_ �� _∞_<sup>.</sup>

Indeed, if _λ ≥_ 2 �� _X T ϵ_ �� _∞_<sup>,thenonecanfirstobservefrom(150)theinequality:</sup>

which is identical to


In other words, the vector _θ_<sup>ˆ</sup> _− θ_<sup>_∗_</sup> belongs to the cone:


Using this observation, one can replace the bound


by


Note that the only difference between the above two bounds is that in the latter the supremum is over ∆ _∈C_ while, in the former, the supremum is over all ∆ _∈_ R<sup>_p_</sup> . As we shall see in the next lecture, this improvement gives results that potentially work even when _p > n_ .

---

[← 16 Lecture 16](17-16-lecture-16.md) · [Up: contents](index.md) · [18 Lecture 18 →](19-18-lecture-18.md)
