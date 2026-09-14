---
title: Second Order Theory of Random Vectors
source: https://www.stat.berkeley.edu/~aditya/resources/FullLectureNotes201AFall2019.pdf
source_file: sources/berkeley-guntuboyina-notes/FullLectureNotes201AFall2019.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Second Order Theory of Random Vectors

**Source:** [`FullLectureNotes201AFall2019.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullLectureNotes201AFall2019.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Here we shall study random vectors and some of their properties which only involved their means and covariances. These include the notions of the best linear predictor and partial correlation and are known as second order properties.

### **4.1 Random Vectors**

In this section, we view a finite number of random variables as a random vector and go over some basic formulae for the mean and covariance of random vectors.

A random vector is a vector whose entries are random variables. Let _Y_ = ( _Y_ 1 _, . . . , Yn_ )<sup>_T_</sup> be a random vector. Its expectation E _Y_ is defined as a vector whose _i_ th entry is the expectation of _Yi_ i.e., E _Y_ = (E _Y_ 1 _,_ E _Y_ 2 _, . . . ,_ E _Yn_ )<sup>_T_</sup> . The covariance matrix of _Y_ , denoted by _Cov_ ( _Y_ ), is an _n × n_ matrix whose ( _i, j_ )th entry is the covariance between _Yi_ and _Yj_ . Two important but easy facts about _Cov_ ( _Y_ ) are:

1. The diagonal entries of _Cov_ ( _Y_ ) are the variances of _Y_ 1 _, . . . , Yn_ . More specifically the ( _i, i_ )th entry of the matrix _Cov_ ( _Y_ ) equals _var_ ( _Yi_ ).

2. _Cov_ ( _Y_ ) is a symmetric matrix i.e., the ( _i, j_ )th entry of _Cov_ ( _Y_ ) equals the ( _j, i_ ) entry. This follows because _Cov_ ( _Yi, Yj_ ) = _Cov_ ( _Yj, Yi_ ).

One can also check:

103

_CHAPTER 4. SECOND ORDER THEORY OF RANDOM VECTORS_

104

1. E( _AY_ + _c_ ) = _A_ E( _Y_ ) + _c_ for every deterministic matrix _A_ and every deterministic vector _c_ .

2. _Cov_ ( _AY_ + _c_ ) = _ACov_ ( _Y_ ) _A_<sup>_T_</sup> for every deterministic matrix _A_ and every deterministic vector _c_ . **Example 4.1.1** (White Noise) **.** _Random variables Z_ 1 _, . . . , Zp are said to form white noise if they have mean zero, variance one and if they are uncorrelated. Let Z be the random vector with components Z_ 1 _, . . . , Zp. Then it is clear that the components of Z are white noise if and only if_ E _Z_ = 0 _and Cov_ ( _Z_ ) = _Ip (here Ip is the p × p identity matrix)._

As a consequence of the second formula above, we saw that


Because variance is always nonnegative, this means that _Cov_ ( _Y_ ) satisfies the following property:


Now recall the following definition from linear algebra:

**Definition 4.1.2.** _Let_ Σ _denote a p × p symmetric matrix._

_1._ Σ _is said to be_ **_positive semi-definite_** _if a_<sup>_T_</sup> Σ _a ≥_ 0 _for every a ∈_ R<sup>_p_</sup> _._

_2._ Σ _is said to be_ **_positive definite_** _if a_<sup>_T_</sup> Σ _a >_ 0 _for every a ∈_ R<sup>_p_</sup> _with a̸_ = 0 _._

From this definition and the fact (4.1), it follows that **the covariance matrix** _Cov_ ( _Y_ ) **of every random vector** _Y_ **is symmetric and positive semi-definite** .

However _Cov_ ( _Y_ ) is not necessarily positive definite. To see this, just take _p_ = 2 and _Y_ = ( _Y_ 1 _, −Y_ 1)<sup>_T_</sup> for a random variable _Y_ 1. Then with _a_ = (1 _,_ 1), it is easy to see that _a_<sup>_T_</sup> _Cov_ ( _Y_ ) _a_ = _V ar_ ( _a_<sup>_T_</sup> _Y_ ) = _V ar_ ( _Y_ 1 + _Y_ 2) = 0.

But if _Cov_ ( _Y_ ) is not positive definite, then there exists _a̸_ = 0 such that _V ar_ ( _a_<sup>_T_</sup> _Y_ ) = _a_<sup>_T_</sup> _Cov_ ( _Y_ ) _a_ = 0. This must necessarily mean that _a_<sup>_T_</sup> ( _Y − µ_ ) = 0 where _µ_ = E( _Y_ ). In other words, the random variables _Y_ 1 _, . . . , Yn_ have to satisfy a linear equation. We can therefore say that: _Cov_ ( _Y_ ) **is positive definite if and only if the random variables** _Y_ 1 _, . . . , Yn_ **do not satisfy a linear equation** .

### **4.2 Detour – Spectral Theorem for Symmetric Matrices**

Since _Cov_ ( _Y_ ) is a symmetric and positive semi-definite matrix, some standard facts about such matrices are useful while working with covariance matrices. In particular, we shall make some use of the spectral theorem for symmetric matrices. Before looking at the spectral theorem, we need to recall the notion of an orthonormal basis.

_4.2. DETOUR – SPECTRAL THEOREM FOR SYMMETRIC MATRICES_

105

#### **4.2.1 Orthonormal Basis**

**Definition 4.2.1** (Orthonormal Basis) **.** _An orthonormal basis in_ R<sup>_p_</sup> _is a set of p vectors u_ 1 _, . . . , up in_ R<sup>_p_</sup> _having the following properties:_

_1. u_ 1 _, . . . , up are orthogonal i.e., ⟨ui, uj⟩_ := _ui_<sup>_Tuj_= 0</sup><sup>_fori̸_=</sup><sup>_j._</sup>

_2. Each ui has unit length i.e., ∥ui∥_ = 1 _for each i._

The simplest example of an orthonormal basis is _e_ 1 _, . . . , en_ where _ei_ is the vector that 1 in the _i_<sup>_th_</sup> position and 0 at all other positions.

Every orthonormal basis _u_ 1 _, . . . , up_ satisfies the following properties:

1. _u_ 1 _, . . . , up_ are linearly independent and therefore form a basis of R<sup>_p_</sup> (this explains the presence of the word “basis” in the definition of orthonormal basis).

To see why this is true, suppose that


Taking the dot product of both sides of the above equality with _uj_ (for a fixed _j_ ), we get


because _⟨uj, ui⟩_ is non-zero only when _i_ = _j_ and _⟨uj, uj⟩_ = 1. Thus (4.2) implies that _αj_ = 0 for every _j_ = 1 _, . . . , p_ and thus _u_ 1 _, . . . , up_ are linearly independent and consequently form a basis of R<sup>_p_</sup> .

2. The following formula holds for every vector _x ∈_ R<sup>_p_</sup> :


To see why this is true, note first that the previous property implies that _u_ 1 _, . . . , up_ form a basis of R<sup>_p_</sup> so that every _x ∈_ R<sup>_p_</sup> can be written as a linear combination


of _u_ 1 _, . . . , up_ . Now take dot product with _uj_ on both sides to prove that _βj_ = _⟨x, uj⟩_ .

3. The formula


holds where _Ip_ is the _p × p_ identity matrix. To see why this is true, note that (4.3) can be rewritten as


Since both sides of the above identity are equal for every _x_ , we must have (4.4).

_CHAPTER 4. SECOND ORDER THEORY OF RANDOM VECTORS_

106

4. Suppose _U_ is the _p × p_ matrix whose columns are the vectors _u_ 1 _, . . . , up_ . Then


To see why this is true, note that the ( _i, j_ )th entry of _U_<sup>_T_</sup> _U_ equals _u_<sup>_T_</sup> _i_<sup>_uj_which(bydefinition</sup> of orthonormal basis) is zero when _i̸_ = _j_ and 1 otherwise. On the other hand, the statement _UU_<sup>_T_</sup> = _Ip_ is the same as (4.4).

5. For every vector _x ∈_ R<sup>_p_</sup> , the formula


holds. To see why this is true, just write


#### **4.2.2 Spectral Theorem**

**Theorem 4.2.2** (Spectral Theorem) **.** _Suppose_ Σ _is a p × p symmetric matrix. Then there exists an orthonormal basis u_ 1 _, . . . , up and real numbers λ_ 1 _, . . . , λp such that_


The spectral theorem is also usually written in the following alternative form. Suppose _U_ is the _p × p_ matrix whose columns are the vectors _u_ 1 _, . . . , up_ . Also suppose that Λ is the _p × p_ diagonal matrix (a diagonal matrix is a matrix whose off-diagonal entries are all zero) whose diagonal entries are _λ_ 1 _, . . . , λp_ . Then (4.5) is equivalent to


Here are some straightforward consequences of the spectral theorem:

1. For every 1 _≤ j ≤ p_ , we have the identities


These follow directly from (4.5). The first identity above implies that each _λj_ is an eigenvalue of Σ with eigenvector _uj_ .

2. In the representation (4.5), the eigenvalues _λ_ 1 _, . . . , λp_ are unique while the eigenvectors _u_ 1 _, . . . , up_ are not necessarily unique (for every _uj_ can be replaced by _−uj_ and if _λ_ 1 = _λ_ 2, then _u_ 1 and _u_ 2 can be replaced by any pair _u_ ˜1 _,_ ˜ _u_ 2 of orthogonal unit norm vectors in the span of _u_ 1 and _u_ 2).

_4.2. DETOUR – SPECTRAL THEOREM FOR SYMMETRIC MATRICES_

107

3. The rank of Σ precisely equals the number of _λ_<sup>_′_</sup> _j_<sup>_s_thatarenon-zero.</sup>

4. If all of _λ_ 1 _, . . . , λp_ are non-zero, then Σ has full rank and is hence invertible. Moreover, we can then write


5. If Σ is positive semi-definite, then every _λj_ in (4.5) is nonnegative (this is a consequence of _λj_ = _u_<sup>_T_</sup> _j_<sup>Σ</sup><sup>_uj≥_0).</sup>

6. **Square Root of a Positive Semi-definite Matrix** : If Σ is positive semi-definite, then we can define a new matrix


It is easy to see that Σ<sup>1</sup><sup>_/_2</sup> is symmetric, positive semi-definite and satisfies (Σ<sup>1</sup><sup>_/_2</sup> )(Σ<sup>1</sup><sup>_/_2</sup> ) = Σ. We shall refer to Σ<sup>1</sup><sup>_/_2</sup> as the square root of Σ.

7. If Σ is positive definite, then every _λj_ in (4.5) is strictly positive (this is a consequence of _λj_ = _u_<sup>_T_</sup> _j_<sup>Σ</sup><sup>_uj>_0).</sup>

#### **4.2.3 Three Applications of the Spectral Theorem**

##### **Every symmetric positive semi-definite matrix is a Covariance Matrix**

We have seen previously that the covariance matrix _Cov_ ( _Y_ ) of every random vector _Y_ is symmetric and positive semi-definite. It turns out that the converse of this statement is also true i.e., it is also true that every symmetric and positive semi-definite matrix equals _Cov_ ( _Y_ ) for some random vector _Y_ . To see why this is true, suppose that Σ is an arbitrary _p × p_ symmetric and positive semi-definite matrix. Recall that, via the spectral theorem, we have defined Σ<sup>1</sup><sup>_/_2</sup> (square-root of Σ) which is a symmetric and nonnegative definite matrix such that Σ<sup>1</sup><sup>_/_2</sup> Σ<sup>1</sup><sup>_/_2</sup> = Σ.

Now suppose that _Z_ 1 _, . . . Zp_ are uncorrelated random variables all having unit variance and let _Z_ = ( _Z_ 1 _, . . . , Zp_ )<sup>_T_</sup> be the corresponding random vector. Because _Z_ 1 _, . . . , Zp_ are uncorrelated and have unit variance, it is easy to see that _Cov_ ( _Z_ ) = _Ip_ . Suppose now that _Y_ = Σ<sup>1</sup><sup>_/_2</sup> _Z_ . Then


We have thus started with an arbitrary positive semi-definite matrix Σ and proved that it equals _Cov_ ( _Y_ ) for some random vector _Y_ .

We can thus summarize the following properties of a covariance matrix.

1. The covariance matrix of every random vector is positive semi-definite definite.

2. Every positive semi-definite matrix equals the covariance matrix of some random vector.

_CHAPTER 4. SECOND ORDER THEORY OF RANDOM VECTORS_

108

3. Unless the random variables _Y_ 1 _, . . . , Yn_ satisfy an exact linear equation, their covariance matrix is positive definite.

##### **Whitening**

Given a _p ×_ 1 random vector _Y_ , how can we transform it into a _p ×_ 1 white noise vector _Z_ (recall that _Z_ is white noise means that E _Z_ = 0 and _Cov_ ( _Z_ ) = _Ip_ ). This transformation is known as Whitening. Whitening can be done if _Cov_ ( _Y_ ) is positive definite. Indeed suppose that Σ := _Cov_ ( _Y_ ) is positive definite with spectral representation:


The fact that Σ is positive definite implies that _λi >_ 0 for every _i_ = 1 _, . . . , p_ . In that case, it is easy to see that Σ<sup>1</sup><sup>_/_2</sup> is invertible and


Moreover it is easy to check that Σ<sup>_−_1</sup><sup>_/_2</sup> ΣΣ<sup>_−_1</sup><sup>_/_2</sup> = _Ip_ . Using this, it is straightforward to check that _Z_ = Σ<sup>_−_1</sup><sup>_/_2</sup> ( _Y −_ E _Y_ ) is white noise. Indeed E _Z_ = 0 and


Therefore the spectral theorem is used to define the matrix ( _Cov_ ( _Y_ ))<sup>_−_1</sup><sup>_/_2</sup> which can be used to whiten the given random vector _Y_ .

##### **First Prinicipal Component of a Random Vector**

Let _Y_ be a _p ×_ 1 vector. We say that a unit vector _a ∈_ R<sup>_p_</sup> (unit vectors are vectors with norm equal to one) is a **first principal component** of _Y_ if


In other words, the unit vector _a_ maximizes the variance of _b_<sup>_T_</sup> _Y_ over all unit vectors _b_ .

Suppose that Σ := _Cov_ ( _Y_ ) has the spectral representation (4.5). Assume, without loss of generality, that the eigenvalues _λ_ 1 _, . . . , λp_ appearing in (4.5) are arranged in decreasing order i.e.,


It then turns out that the vector _u_ 1 is a first principal component of _Y_ . To see this, simply note that


and that for every unit vector _b_ ,


_4.3. BEST LINEAR PREDICTOR_

109

Thus _u_ 1 is a first principal component of _Y_ . Note that first principal components are not unique. Indeed, _−u_ 1 is also a first principal component and if _λ_ 1 = _λ_ 2, then _u_ 2 and ( _u_ 1 + _u_ 2) _/√_ 2 are also first principal components.

### **4.3 Best Linear Predictor**

Consider random variables _Y, X_ 1 _, . . . , Xp_ that have finite variance. We want to predict _Y_ on the basis of _X_ 1 _, . . . , Xp_ . Given a predictor _g_ ( _X_ 1 _, . . . , Xp_ ) of _Y_ based on _X_ 1 _, . . . , Xp_ , we measure the accuracy of prediction by


We have seen in the last class that the best predictor (i.e., the function _g_<sup>_∗_</sup> which minimizes _R_ ( _g_ )) is given by the conditional expectation:


This conditional expectation is often quite a complicated quantity. For example, in practice to estimate it, one would need quite a lot of data on the variables _X_ 1 _, . . . , Xp, Y_ .

We now consider a related problem of predicting _Y_ based only on **linear** functions of _X_ 1 _, . . . , Xp_ . Specifically, we consider predictions of the form _β_ 0 + _β_ 1 _X_ 1 + _· · ·_ + _βpXp_ = _β_ 0 + _β_<sup>_T_</sup> _X_ (where _β_ := ( _β_ 1 _, . . . , βp_ )<sup>_T_</sup> and _X_ = ( _X_ 1 _, . . . , Xp_ )<sup>_T_</sup> ). The Best Linear Predictor (BLP) of _Y_ in terms of _X_ 1 _, . . . , Xp_ is the linear function


where _β_ 0<sup>_∗, . . . , β_</sup> _p_<sup>_∗_minimize</sup>


over _β_ 0 _, β_ 1 _, . . . , βp_ .

One can get an explicit formula for _β_ 0<sup>_∗_and</sup><sup>_β∗_by minimizing</sup><sup>_L_directly via calculus.Taking partial</sup> derivatives with respect to _β_ 0 _, β_ 1 _, . . . , βp_ and setting them equal to zero, we obtain the following equations:


and


The first equation above implies that _Y − β_ 0<sup>_∗−β_</sup> 1<sup>_∗X_1</sup><sup>_−· · · −β_</sup> _p_<sup>_∗Xp_isameanzerorandomvariable.</sup> Using this, we can rewrite the second equation as


110 _CHAPTER 4. SECOND ORDER THEORY OF RANDOM VECTORS_

which is same as


Rearranging the above, we obtain


In matrix notation, we can rewrite this as


Here _Cov_ ( _X, Y_ ) is the _p×_ 1 vector with entries _Cov_ ( _X_ 1 _, Y_ ) _, . . . , Cov_ ( _Xp, Y_ ). The above equation gives


assuming that _Cov_ ( _X_ ) is invertible. This equation determines _β_ 1<sup>_∗, . . . , β_</sup> _p_<sup>_∗_.Wecanthenuse(4.6)to</sup> write _β_ 0<sup>_∗_as</sup>


Note that the term _Cov_ ( _Y, X_ ) appearing above is the transpose of _Cov_ ( _X, Y_ ). More generally, given two random vectors _W_ = ( _W_ 1 _, . . . , Wp_ ) and _Z_ = ( _Z_ 1 _, . . . , Zq_ ), we define _Cov_ ( _W, Z_ ) to be the _p × q_ matrix whose ( _i, j_ )th entry is the covariance between _Wi_ and _Zj_ .

The Best Linear Predictor (BLP) of _Y_ in terms of _X_ 1 _, . . . , Xp_ then equals


Here are some important properties of the BLP:

1. The BLP solves equations (4.6) and (4.8). These equations are called **normal equations** .

2. If _Cov_ ( _X_ ) is invertible (equivalently, positive definite), then the BLP is uniquely given by (4.9).

3. _Y −BLP_ has mean zero (because of (4.6)) and _Y −BLP_ is uncorrelated with each _Xi, i_ = 1 _, . . . , p_ (because of (4.8)). In fact, this property characterizes the BLP (see next).

4. If _Cov_ ( _X_ ) is invertible, then it is clear from the form of the normal equations that the BLP is the unique linear combination of _X_ 1 _, . . . , Xp_ such that _Y − BLP_ has mean zero and is uncorrelated with _X_ 1 _, . . . , Xp_ .

**Example 4.3.1** (The case _p_ = 1) **.** _When p_ = 1 _, the random vector X has only element X_ 1 _so that Cov_ ( _X_ ) _is just equal to the number V ar_ ( _X_ 1) _. In that case, the BLP of Y in terms of X_ 1 _is given by_


_4.3. BEST LINEAR PREDICTOR_

111

_In other words, when p_ = 1 _,_


_In the further special case when V ar_ ( _Y_ ) = _V ar_ ( _X_ 1) _and_ E( _Y_ ) = E( _X_ 1) = 0 _, we have_


_so that the BLP is simply given by ρY,X_ 1 _X_ 1 _._

**Example 4.3.2.** _Suppose X_ 1 _, X_ 2 _, Z_ 3 _, . . . , Zn, Zn_ +1 _are uncorrelated random variables and mean zero random variables. Define random variables X_ 3 _, . . . , Xn_ +1 _as_


_What is the BLP of Xn_ +1 _in terms of X_ 1 _, . . . , Xn for n ≥_ 2 _?_

_By definition,_


_which means that Xn_ +1 _− φ_ 1 _Xn − φ_ 2 _Xn−_ 1 = _Zn_ +1 _. It is now easy to see that each Xt depends only on X_ 1 _, X_ 2 _, Z_ 3 _, . . . , Zt for t ≥_ 3 _which implies that Zn_ +1 _is uncorrelated with all of X_ 1 _, . . . , Xn._

_Therefore φ_ 1 _Xn_ + _φ_ 2 _Xn−_ 1 _is a linear combination of X_ 1 _, . . . , Xn such that Xn_ +1 _− φ_ 1 _Xn − φ_ 2 _Xn−_ 1 _is uncorrelated with each of X_ 1 _, . . . , Xn (it also has mean zero). We deduce therefore that the BLP of Xn_ +1 _in terms of X_ 1 _, . . . , Xn equals φ_ 1 _Xn_ + _φ_ 2 _Xn−_ 1 _._

As discussed in the chapter on conditioning, the Best Predictor (BP) of _Y_ in terms of _X_ 1 _, . . . Xp_ is the function _g_<sup>_∗_</sup> ( _X_ 1 _, . . . , Xp_ ) of _X_ 1 _, . . . , Xp_ which minimizes


over all functions _g_ and we have seen that


In other words, the best predictor is the conditional expectation. In general, the BP and BLP will differ and the BP will be a more accurate predictor of _Y_ compared to BLP. Note that the BLP only depends on the variances and covariances between the random variables _Y, X_ 1 _, . . . , Xp_ while the BP depends potentially on the entire joint distribution. As a result, the BLP is usually much easier to estimate based on data compared to the BP.

In general, we shall refer to any quantity involving the distribution of _Y, X_ 1 _, . . . , Xp_ that depends only on the mean, variances and covariances of _Y, X_ 1 _, . . . , Xp_ as a second order property. Note that the BLP is a second order quantity while the BP is not.

112

_CHAPTER 4. SECOND ORDER THEORY OF RANDOM VECTORS_

### **4.4 Residual**

The residual of a random variable _Y_ in terms of _X_ 1 _, . . . , Xp_ will be denoted by _rY |X_ 1 _,...,Xp_ and defined as the difference between _Y_ and the BLP of _Y_ in terms of _X_ 1 _, . . . , Xp_ . In other words,


Using the formula for the BLP, we can write down the following formula for the residual:


where _X_ is the _p ×_ 1 random vector with components _X_ 1 _, . . . , Xp_ .

The residual has mean zero and is uncorrelated with each of _X_ 1 _, . . . , Xp_ . This can be proved either directly from the formula (4.10) or from the properties of the BLP.

The variance of the residual can be calculated from the formula (4.10) as follows:


In other words, _V ar_ ( _rY |X_ 1 _,...,Xp_ ) equals the **Schur complement** (recalled next) of _V ar_ ( _Y_ ) in the covariance matrix:


of the ( _n_ + 1) _×_ 1 random vector ( _X_ 1 _, . . . , Xp, Y_ )<sup>_T_</sup> .

Note that the residual is also a second order quantity.

### **4.5 Detour: Schur Complements**

Consider an _n × n_ matrix _A_ that is partitioned into four blocks as


where _E_ is _p × p_ , _F_ is _p × q_ , _G_ is _q × p_ and _H_ is _q × q_ ( _p_ and _q_ are such that _p_ + _q_ = _n_ ).

We define


_4.6. PARTIAL CORRELATION_

113

assuming that _H_<sup>_−_1</sup> and _E_<sup>_−_1</sup> exist. We shall refer to _E_<sup>_S_</sup> and _H_<sup>_S_</sup> as the _Schur complements_ of _E_ and _H_ respectively ( **Warning** : This is not standard terminology; it is more common to refer to _E_<sup>_S_</sup> as the Schur complement of _H_ and to _H_<sup>_S_</sup> as the Schur complement of _E_ . I find it more natural to think of _E_<sup>_S_</sup> as the Schur complement of _E_ and _H_<sup>_S_</sup> as the Schur complement of _H_ ).

Note that both _E_ and _E_<sup>_S_</sup> are _p × p_ while both _H_ and _H_<sup>_S_</sup> are _q × q_ .

Schur complements have many interesting properties such as:

1. _det_ ( _A_ ) = _det_ ( _E_ ) _det_ ( _H_<sup>_S_</sup> ) = _det_ ( _H_ ) _det_ ( _E_<sup>_S_</sup> ).

2. If _A_ is positive definite, then _E, E_<sup>_S_</sup> _, H, H_<sup>_S_</sup> are all positive definite.

and many others. Feel free to see the monograph titled _Schur Complements and Statistics_ by Diane Ouellette for proofs and exposition of these facts (this is not really necessary for this course).

But one very important property of Schur Complements for our purpose is the fact that they arise naturally in inverses of partitioned matrices. A standard formula for the inverse of a partitioned matrix (see, for example, `https://en.wikipedia.org/wiki/Block_matrix#Block_matrix_inversion` ) is


It must be noted from this formula that **the first (or** (1 _,_ 1)<sup>_th_</sup> **) block of** _A_<sup>_−_1</sup> **equals the inverse of the Schur complement of the first block of** _A_ **. Similarly, the last (or** (2 _,_ 2)<sup>_th_</sup> **) block of** _A_<sup>_−_1</sup> **equals the inverse of the Schur complement of the last block of** _A_ .

We shall use the expression (4.11) for the inverse of the partitioned matrix _A_ but we will not see how to prove (4.11). You can find many proofs of this fact elsewhere (just google something like “inverse of partitioned matrices”).

### **4.6 Partial Correlation**

Given random variables _Y_ 1 _, Y_ 2 and _X_ 1 _, . . . , Xp_ , the partial correlation between _Y_ 1 and _Y_ 2 given _X_ 1 _, . . . , Xp_ is denoted by _ρY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ and defined as


In other words, _ρY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ is defined as the correlation between the residual of _Y_ 1 given _X_ 1 _, . . . , Xp_ and the residual of _Y_ 2 given _X_ 1 _, . . . , Xp_ .

_ρY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ is also termed the partial correlation of _Y_ 1 and _Y_ 2 after controlling for _X_ 1 _, . . . , Xp_ . Since residuals are second order quantities, it follows that the partial correlation is a second order

114

_CHAPTER 4. SECOND ORDER THEORY OF RANDOM VECTORS_

quantity as well. We shall now see how to explicitly write the partial correlation in terms of the covariances of _Y_ 1, _Y_ 2 and _X_ .

As


and


it can be checked (left as an exercise) that


This, along with the formula for the variance of the residuals from the previous subsections, gives the following formula for the partial correlation _ρY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ :


When _p_ = 1 so that _X_ equals the scalar random variable _X_ 1, the above formula simplifies to (check this):


It is instructive to put the variances of the residuals _rY_ 1 _|X_ 1 _,...,Xp_ and _ry_ 2 _|X_ 1 _,...,Xp_ and their covariance in a matrix. Recall first that:


and

_Cov_ ( _rY_ 1 _|X_ 1 _,...,Xp, rY_ 2 _|X_ 1 _,...,Xp_ ) = _Cov_ ( _Y_ 1 _, Y_ 2) _− Cov_ ( _Y_ 1 _, X_ )( _CovX_ )<sup>_−_1</sup> _Cov_ ( _X, Y_ 2) _._

Let _RY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ denote the 2 _×_ 1 random vector consisting of the residuals _rY_ 1 _|X_ 1 _,...,Xp_ and _rY_ 2 _|X_ 1 _,...,Xp_ . The formulae for the variances and covariances of the residuals allows us then to write the 2 _×_ 2 covariance matrix of _RY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ as


where


_4.7. PARTIAL CORRELATION AND INVERSE COVARIANCE_

115

The right hand side in the formula for _Cov_ ( _RY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ ) equals precisely the Schur complement of _Cov_ ( _Y_ ) in the matrix


Thus if Σ denotes the covariance matrix of the ( _p_ + 2) _×_ 1 random vector ( _X_ 1 _, . . . , Xp, Y_ 1 _, Y_ 2)<sup>_T_</sup> , then _Cov_ ( _RY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ ) equals precisely the Schur complement of _Cov_ ( _Y_ ) in Σ. We shall come back to this fact in the next class and use it to describe an expression for the partial correlation _ρY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ involving Σ<sup>_−_1</sup> .

### **4.7 Partial Correlation and Inverse Covariance**

We defined partial correlation in the last lecture. Given random variables _Y_ 1 _, Y_ 2 and _X_ 1 _, . . . , Xp_ , the partial correlation between _Y_ 1 and _Y_ 2 given _X_ 1 _, . . . , Xp_ is denoted by _ρY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ and defined as


In other words, _ρY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ is defined as the correlation between the residual of _Y_ 1 given _X_ 1 _, . . . , Xp_ and the residual of _Y_ 2 given _X_ 1 _, . . . , Xp_ .

Recall that the residuals _rY_ 1 _|X_ 1 _,...,Xp_ and _rY_ 2 _|X_ 1 _,...,Xp_ have the following expressions:


and


In the last class, we computed the variances of _rY_ 1 _|X_ 1 _,...,Xp_ and _rY_ 2 _|X_ 1 _,...,Xp_ as well as the covariance between them. This gave us the formulae:


and


We can put these expressions together to get the following formula for the partial correlation between _Y_ 1 and _Y_ 2 given _X_ 1 _, . . . , Xp_ :


We shall now describe the connection between partial correlations and the inverse of the Covariance matrix. Let _RY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ denote the 2 _×_ 1 random vector consisting of the residuals _rY_ 1 _|X_ 1 _,...,Xp_ and

_CHAPTER 4. SECOND ORDER THEORY OF RANDOM VECTORS_

116

_rY_ 2 _|X_ 1 _,...,Xp_ . The formulae for the variances and covariances of the residuals allows us then to write the 2 _×_ 2 covariance matrix of _RY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ as


= _Cov_ ( _Y_ ) _− Cov_ ( _Y, X_ )( _CovX_ )<sup>_−_1</sup> _Cov_ ( _X, Y_ )

where


The right hand side in the formula for _Cov_ ( _RY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ ) equals precisely the Schur complement of _Cov_ ( _Y_ ) in the matrix


Thus if Σ denotes the covariance matrix of the ( _p_ + 2) _×_ 1 random vector ( _X_ 1 _, . . . , Xp, Y_ 1 _, Y_ 2)<sup>_T_</sup> , then _Cov_ ( _RY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ ) equals precisely the Schur complement of _Cov_ ( _Y_ ) in Σ.

But we know if we invert Σ, then the last diagonal block (or the (2 _,_ 2)<sup>_th_</sup> block) of Σ<sup>_−_1</sup> equals the inverse of the Schur complement of the (2 _,_ 2)<sup>_th_</sup> block of Σ. This and the above connection between Schur complement and the covariance of _RY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ allows us to deduce that if


where _D_ is the determinant of _Cov_ ( _RY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ ).

From here it follows that the partial correlation _ρY_ 1 _,Y_ 2 _|X_ 1 _,...,Xp_ has the alternative expression:


This shows the connection between partial correlation and inverse covariance matrices.

_4.8. PARTIAL CORRELATION AND BEST LINEAR PREDICTOR_

117

More generally, if _Y_ 1 _, . . . , Yn_ are random variables (no distributional assumptions are needed here) with covariance matrix given by Σ. Then the partial correlation between _Yi_ and _Yj_ given _Yk, k̸_ = _i, k̸_ = _j_ can be written in terms of Σ<sup>_−_1</sup> as


This implies, in particular, that


Therefore (Σ<sup>_−_1</sup> )( _i, j_ ) = 0 is equivalent to the partial correlation between _Yi_ and _Yj_ given _Yk, k̸_ = _i, k̸_ = _j_ being zero.

Also


In other words, Σ<sup>_−_1</sup> ( _i, j_ ) being nonpositive is equivalent to the partial correlation between _Yi_ and _Yj_ given _Yk, k̸_ = _i, k̸_ = _j_ being nonnegative. Similarly, Σ<sup>_−_1</sup> ( _i, j_ ) being nonnegative is equivalent to the partial correlation between _Yi_ and _Yj_ given _Yk, k̸_ = _i, k̸_ = _j_ being nonpositive.

### **4.8 Partial Correlation and Best Linear Predictor**

Consider random variables _Y_ and _X_ 1 _, . . . , Xp_ . Let _β_ 0<sup>_∗_+</sup><sup>_β_</sup> 1<sup>_∗X_1+</sup><sup>_· · ·_+</sup><sup>_β_</sup> _p_<sup>_∗Xp_denotetheBLPof</sup><sup>_Y_in</sup> terms of _X_ 1 _, . . . , Xp_ .

We have seen before that If _p_ = 1, then _X_ is equal to the scalar random variable _X_ 1 and the BLP then has the expression:


In other words, when _p_ = 1, the slope coefficient of the BLP is given by


When _p ≥_ 1, we would have _p_ “slope” coefficients _X_ 1 _, . . . , Xp_ . In this case, one can write a formula analogous to (4.12) as follows:


In other words _βi_<sup>_∗_equalstheslopecoefficientofBLPof</sup><sup>_rY |X_</sup> _k_<sup>_,k̸_=</sup><sup>_i_intermsof</sup><sup>_rX_</sup> _i_<sup>_|X_</sup> _k_<sup>_,k̸_=</sup><sup>_i_.</sup>

We shall prove this fact now. We can assume without loss of generality _i_ = _p_ . The proof for other _i_ can be completed by rearranging _X_ 1 _, . . . , Xp_ so that _Xi_ appears at the last position. The formula for _β_<sup>_∗_</sup> = ( _β_ 1 _, . . . , βp_ )<sup>_∗_</sup> is


118

_CHAPTER 4. SECOND ORDER THEORY OF RANDOM VECTORS_

Let us write


where _X−p_ := ( _X_ 1 _, . . . , Xp−_ 1)<sup>_T_</sup> consists of all the _X_ ’s except _Xp_ . We can partition _Cov_ ( _X_ ) as


The formula for _β_<sup>_∗_</sup> then becomes


In order to derive an explicit formula for _βp_<sup>_∗_fromthisexpression,weneedtofigureoutthelastrowof</sup> ( _CovX_ )<sup>_−_1</sup> . A standard formula for the inverses of partitioned matrices states that


where _H_<sup>_S_</sup> := _H − GE_<sup>_−_1</sup> _F_ is the Schur complement of _H_ in _A_ . We shall apply this formula to

_E_ = _Cov_ ( _X−p_ ) _, F_ = _Cov_ ( _X−p, Xp_ ) _, G_ = _Cov_ ( _Xp, X−p_ ) _,_ and _H_ = _V ar_ ( _Xp_ )

so that _A_ equals _Cov_ ( _X_ ). In this case,


so that


We thus obtain


which proves the result for _i_ = _p_ . One can prove it for other _i_ by simply rearranging _X_ 1 _, . . . , Xp_ so that _Xi_ appears as the last variable.

An important consequence of (4.13) is:


In other words, the coefficient of _Xi_ in the BLP of _Y_ based on _X_ 1 _, . . . , Xp_ equals zero if and only if the partial correlation between _Y_ and _Xi_ given _Xk, k̸_ = _i_ equals 0.

_4.9. BLP WHEN Y IS A RANDOM VECTOR_

119

**Example 4.8.1.** _Suppose X_ 1 _, X_ 2 _, Z_ 3 _, . . . , Zn, Zn_ +1 _with n ≥_ 2 _are uncorrelated random variables having mean zero. Define random variables X_ 3 _, . . . , Xn_ +1 _as_


_We have seen in the last class that the BLP of Xn_ +1 _in terms of X_ 1 _, . . . , Xn equals φ_ 1 _Xn_ + _φ_ 2 _Xn−_ 1 _. This means that the coefficient of Xi in the BLP of Xn_ +1 _in terms of X_ 1 _, . . . , Xn equals 0 for i_ = 1 _, . . . , n −_ 2 _. As a consequence of_ (4.14) _, we then deduce that_


_Using the connection between partial correlation and inverse covariance, we can further deduce that if_ Σ _denotes the_ ( _n_ + 1) _×_ ( _n_ + 1) _covariance matrix of X_ 1 _, . . . , Xn_ +1 _, then_


### **4.9 BLP when** _Y_ **is a random vector**

Let us first quickly recap the BLP. Given random variables _Y_ and _X_ 1 _, . . . , Xp_ , a linear predictor of _Y_ in terms of _X_ 1 _, . . . , Xp_ is a random variable of the form _β_ 0 + _β_ 1 _X_ 1 + _· · ·_ + _βpXp_ . The BLP is then given by _β_ 0<sup>_∗_+</sup><sup>_β_</sup> 1<sup>_∗X_1+</sup><sup>_· · ·_+</sup><sup>_β_</sup> _p_<sup>_∗Xp_where</sup><sup>_β_</sup> 0<sup>_∗, . . . , β_</sup> _p_<sup>_∗_minimize:</sup>


over _β_ 0 _, . . . , βp_ . We have seen that _β_ 0<sup>_∗, . . . , β_</sup> _p_<sup>_∗_canbefiguredoutusingcalculusandthisgivesthe</sup> formula:


where _X_ stands for the _p ×_ 1 random vector with components _X_ 1 _, . . . , Xp_ . The residual _rY |X_ 1 _,...,Xp_ simply equals _Y − BLP_ and we have seen that the variance of _rY |X_ 1 _,...,Xp_ equals:


Now suppose that we have two random variables _Y_ 1 and _Y_ 2 with _Y_ denoting the 2 _×_ 1 random vector with components _Y_ 1 and _Y_ 2. Consider the problem of finding the BLP of _Y_ in terms of _X_ (where _X_ , as before, is the _p ×_ 1 random vector with components _X_ 1 _, . . . , Xp_ ). To formalize this, we first need to define what a linear predictor is (note that _Y_ is a 2 _×_ 1 random vector and not a scalar random variable). A linear predictor for _Y_ in terms of _X_ is given by


_CHAPTER 4. SECOND ORDER THEORY OF RANDOM VECTORS_

120

where _A_ is a 2 _× p_ matrix and _c_ is a 2 _×_ 1 vector. The accuracy of this linear predictor for predicting _Y_ can be measured by


The BLP is then given by _A_<sup>_∗_</sup> _Y_ + _c_<sup>_∗_</sup> where _A_<sup>_∗_</sup> and _c_<sup>_∗_</sup> minimize _L_ ( _A, c_ ) over all _A_ and _c_ . To solve this minimization, let us first write _A_ and _c_ as


so that


and


From here it is clear that to minimize the above with respect to _A_ and _c_ , we can minimize the first term over _a_ 11 _, a_ 12 _, . . . , a_ 1 _p, c_ 1 and then minimize the second term over _a_ 21 _, a_ 22 _, . . . , a_ 2 _p, c_ 2. From here, _Y_ 1 it is easy to see that the _BLP_ of _Y_ = in terms of _X_ is given by � _Y_ 2�


Thus the same formula E _Y_ + _Cov_ ( _Y, X_ )( _CovX_ )<sup>_−_1</sup> ( _X −_ E _X_ ) gives the BLP for _Y_ in terms of _X_ even when _Y_ is a 2 _×_ 1 random vector. It is straightforward now to see that this holds when _Y_ is a _k ×_ 1 random vector for every _k ≥_ 1 (not just _k_ = 1 or _k_ = 2). One can define the residual of _Y_ in terms of _X_ 1 _, . . . , Xp_ as


and this is exactly the vector whose _i_<sup>_th_</sup> component is the residual of _Yi_ in terms of _X_ 1 _, . . . , Xp_ . It is also straightforward to check that that covariance matrix of _RY |X_ is given by


which is exactly the Schur complement of _Cov_ ( _Y_ ) in the matrix


## **Chapter 5**

---

[← The Central Limit Theorem](04-the-central-limit-theorem.md) · [Up: contents](index.md) · [The Multivariate Normal Distribution →](06-the-multivariate-normal-distribution.md)
