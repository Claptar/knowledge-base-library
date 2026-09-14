---
title: Unit 09 — linalg Part 08 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit9-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit9-linalg.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 09 — linalg Part 08 —

**Source:** [`units/unit9-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit9-linalg.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can think about the accuracy here as follows. Suppose we have a matrix whose diagonal elements (i.e., the variances) are order of magnitude 1 and that the true value of a _Uii_ is less than 1 _×_ 10<sup>_−_16</sup> . From the given _Aii_ we are subtracting<sup>�</sup> _k_<sup>_U_</sup> _ki_<sup>2andtryingtocalculatethisverysmall</sup> number but we know that we can only represent the values _Aii_ and<sup>�</sup> _k_<sup>_U_</sup> _ki_<sup>2accurately to 16 places,</sup> so the difference is garbage starting in the 17th position and could well be negative. Now realize that<sup>�</sup> _k_<sup>_U_</sup> _ki_<sup>2is the result of a potentially large set of arithmetic operations, and is likely represented</sup> accurately to fewer than 16 places. Now if the true value of _Uii_ is smaller than the accuracy to

18

which<sup>�</sup> _k_<sup>_U_2</sup> _ki_<sup>is represented, we can get a difference that is negative.</sup>

Note that when the Cholesky fails, we can still compute an eigendecomposition, but we have negative numeric eigenvalues. Even if all the eigenvalues are numerically positive (or equivalently, we’re able to get the Cholesky), errors in small eigenvalues near machine precision could have large effects when we work with the inverse of the matrix. This is what happens when we have columns of the _X_ matrix nearly collinear. We cannot statistically distinguish the effect of two (or more) covariates, and this plays out numerically in terms of unstable results.

A strategy when working with mathematically but not numerically positive definite _A_ is to set eigenvalues or singular values to zero when they get very small, which amounts to using a pseudoinverse and setting to zero any linear combinations with very small variance. We can also use pivoting with the Cholesky and accumulate zeroes in the last _n − q_ rows (for cases where we try to take the square root of a negative number), corresponding to the columns of _A_ that are numerically linearly dependent. See the _pivot_ argument to R’s _chol()_ .

### **3.4 QR decomposition**

#### **3.4.1 Introduction**

The QR decomposition is available for any matrix, _X_ = _QR_ , with _Q_ orthogonal and _R_ upper triangular. If _X_ is non-square, _n × p_ with _n > p_ then the leading _p_ rows of _R_ provide an upper triangular matrix ( _R_ 1) and the remaining rows are 0. (I’m using _p_ because the QR is generally applied to design matrices in regression). In this case we really only need the first _p_ columns of _Q_ , and we have _X_ = _Q_ 1 _R_ 1, the ’skinny’ QR (this is what R’s QR provides). For uniqueness, we can require the diagonals of _R_ to be nonnegative, and then _R_ will be the same as the upper-triangular Cholesky factor of _X_<sup>_⊤_</sup> _X_ :


There are three standard approaches for computing the QR, using (1) reflections (Householder transformations), (2) rotations (Givens transformations), or (3) Gram-Schmidt orthogonalization (see below for details).

For _n×n X_ , the QR (for the Householder approach) requires 2 _n_<sup>3</sup> _/_ 3 flops, so QR is less efficient than LU or Cholesky.

We can also obtain the pseudo-inverse of _X_ from the QR: _X_<sup>+</sup> = [ _R_ 1<sup>_−_10]</sup><sup>_Q⊤_.In the case that</sup> _X_ is not full-rank, there is a version of the QR that will work (involving pivoting) and we end up with some additional zeroes on the diagonal of _R_ 1.

19

#### **3.4.2 Regression and the QR**

Often QR is used to fit linear models, including in R. Consider the linear model in the form _Y_ = _Xβ_ + _ϵ_ , finding _β_<sup>ˆ</sup> = ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ . Let’s consider the skinny QR and note that _R_<sup>_⊤_</sup> is invertible. Therefore, we can express the normal equations as


and solving for _β_ is just a backsolve since _R_ is upper-triangular. Furthermore the standard regression quantities, such as the hat matrix, the SSE, the residuals, etc. can be easily expressed in terms of _Q_ and _R_ .

Why use the QR instead of the Cholesky on _X_<sup>_⊤_</sup> _X_ ? The condition number of _X_ is the square root of that of _X_<sup>_⊤_</sup> _X_ , and the _QR_ factorizes _X_ . Monahan has a discussion of the condition of the regression problem, but from a larger perspective, the situations where numerical accuracy is a concern are generally cases where the OLS estimators are not particularly helpful anyway (e.g., highly collinear predictors).

What about computational order of the different approaches to least squares? The Cholesky is _np_<sup>2</sup> +<sup><u>1</u></sup> 3<sup>_p_3, an algorithm called sweeping is</sup><sup>_np_2+</sup><sup>_p_3 , the Householder method for QR is 2</sup><sup>_np_2</sup><sup>_−_</sup><sup><u>2</u></sup> 3<sup>_p_3,</sup> and the modified Gram-Schmidt approach for QR is 2 _np_<sup>2</sup> . So if _n ≫ p_ then Cholesky (and sweeping) are faster than the QR approaches. According to Monahan, modified Gram-Schmidt is most numerically stable and sweeping least. In general, regression is pretty quick unless _p_ is large since it is linear in _n_ , so it may not be worth worrying too much about computational differences of the sort noted here.

#### **3.4.3 Regression and the QR in R**

Regression in R uses the QR decomposition via _qr()_ , which calls a Fortran function. _qr()_ (and the Fortran functions that are called) is specifically designed to output quantities useful in fitting linear models. Note that by default you get the skinny QR, namely only the first _p_ rows of _R_ and the first _p_ columns of _Q_ , where the latter form an orthonormal basis for the column space of _X_ . The remaining columns form an orthonormal basis for the null space of _X_ (the space orthogonal to the column space of _X_ ). The analogy in regression is that we get the basis vectors for the regression, while adding the remaining columns gives us the full _n_ -dimensional space of the observations.

_qr()_ returns the result as a list meant for use by other tools. R stores the _R_ matrix in the upper triangle of _$qr_ , while the lower triangle of _$qr_ and _$aux_ store the information for constructing _Q_

20

(this relates to the Householder-related vectors _u_ below). One can multiply by _Q_ using _qr.qy()_ and by _Q_<sup>_⊤_</sup> using _qr.qty()_ . If you want to extract _R_ and _Q_ , the following will work:

X.qr = **qr** (X) Q = **qr.Q** (X.qr) R = **qr.R** (X.qr)

As a side note, there are QR-based functions that provide regression-related quantities, such as _qr.resid()_ , _qr.fitted()_ and _qr.coef()_ . These functions (and their Fortran counterparts) exist because one can work through the various regression quantities of interest and find their expressions in terms of _Q_ and _R_ , with nice properties resulting from _Q_ being orthogonal and _R_ triangular.

#### **3.4.4 Computing the QR decomposition**

We’ll work through some of the details of the different approaches to the QR, in part because they involve some concepts that may be useful in other contexts.

One approach involves reflections of vectors and a second rotations of vectors. Reflections and rotations are transformations that are performed by orthogonal matrices. The determinant of a reflection matrix is -1 and the determinant of a rotation matrix is 1. We’ll see some of the details in the demo code.

**Reflections** If _u_ and _v_ are orthonormal vectors and _x_ is in the space spanned by _u_ and _v_ , _x_ = _c_ 1 _u_ + _c_ 2 _v_ , then _x_ ˜ = _−c_ 1 _u_ + _c_ 2 _v_ is a reflection (a _Householder_ reflection) along the _u_ dimension (since we are using the negative of that basis vector). We can think of this as reflecting across the plane perpendicular to _u_ . This extends simply to higher dimensions with orthonormal vectors, _u, v_ 1 _, v_ 2 _, . . ._

Suppose we want to formulate the reflection in terms of a “Householder” matrix, _Q_ . It turns out that


if _Q_ = _I −_ 2 _uu_<sup>_⊤_</sup> . _Q_ has the following properties: (1) _Qu_ = _−u_ , (2) _Qv_ = _v_ for _u_<sup>_⊤_</sup> _v_ = 0, (3) _Q_ is orthogonal and symmetric.

One way to create the QR decomposition is by a series of Householder transformations that create an upper triangular _R_ from _X_ :


21

where we make use of the symmetry in defining _Q_ .

Basically _Q_ 1 reflects the first column of _X_ with respect to a carefully chosen _u_ , so that the result is all zeroes except for the first element. We want _Q_ 1 _x_ = _x_ ˜ = ( _||x||,_ 0 _, . . . ,_ 0). This can be achieved with _u_ = _||xx−−xx_ ˜˜ _||_<sup>.Then</sup><sup>_Q_2 makes the last</sup><sup>_n −_2 rows of the second column equal to zero.</sup> We’ll work through this a bit in class.

In the regression context, as we work through the individual transformations, _Qj_ = _I −_ 2 _uju_<sup>_⊤_</sup> _j_<sup>,</sup> we apply them to _X_ and _Y_ to create _R_ (note this would not involve doing the full matrix multiplication - think about what calculations are actually needed) and _QY_ = _Q_<sup>_⊤_</sup> _Y_ , and then solve _Rβ_ = _Q_<sup>_⊤_</sup> _Y_ . To find Cov( _β_<sup>ˆ</sup> ) _∝_ ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> = ( _R_<sup>_⊤_</sup> _R_ )<sup>_−_1</sup> = _R_<sup>_−_1</sup> _R_<sup>_−⊤_</sup> we do need to invert _R_ , but it’s upper-triangular and of dimension _p × p_ . It turns out that _Q_<sup>_⊤_</sup> _Y_ can be partitioned into the first _p_ and the last _n − p_ elements, _z_<sup>(1)</sup> and _z_<sup>(2)</sup> . The SSR is _∥z_<sup>(1)</sup> _∥_<sup>2</sup> and SSE is _∥z_<sup>(2)</sup> _∥_<sup>2</sup> .

**Rotations** A _Givens_ rotation matrix rotates a vector in a two-dimensional subspace to be axis oriented with respect to one of the two dimensions by changing the value of the other dimension. E.g. we can create _x_ ˜ = ( _x_ 1 _, . . . ,_ ˜ _xp, . . . ,_ 0 _, . . . xn_ ) from _x_ = ( _x_ 1 _, . . . , xp, . . . , xq, . . . , xn_ ) using a matrix multiplication: _x_ ˜ = _Qx_ . _Q_ is orthogonal but not symmetric.

We can use a series of Givens rotations to do the QR but unless it is done carefully, more computations are needed than with Householder reflections. The basic story is that we apply a series of Givens rotations to _X_ such that we zero out the lower triangular elements.


Note that we create the _n − p_ zero rows in _R_ (because the calculations affect the upper triangle of _R_ ), but we can then ignore those rows and the corresponding columns of _Q_ .

**Gram-Schmidt Orthogonalization** Gram-Schmidt involves finding a set of orthonormal vectors to span the same space as a set of LIN vectors, _x_ 1 _, . . . , xp_ . If we take the LIN vectors to be the columns of _X_ , so that we are discussing the column space of _X_ , then G-S yields the QR decomposition. Here’s the algorithm:


2. Orthogonalize the remaining vectors with respect to _x_ ˜1:

> _x_ 2 _−x_ ˜<sup>_⊤_</sup> <u>1</u><sup>_x_2</sup><sup>_x_˜1</sup> (a) _x_ ˜2 = _∥x_ 2 _−x_ ˜<sup>_⊤_</sup> 1<sup>_x_2</sup><sup>_x_˜1</sup><sup>_∥_,which orthogonalizes with respect to</sup><sup>_x_˜1and normalizes.Note that</sup> _x_ ˜<sup>_⊤_</sup> 1<sup>_x_2</sup><sup>_x_˜1=</sup><sup>_⟨x_˜1</sup><sup>_, x_2</sup><sup>_⟩x_˜1.So we are finding a scaling,</sup><sup>_cx_˜1, where</sup><sup>_c_is based on the inner</sup> product, to remove the variation in the _x_ 1 direction from _x_ 2.

22

   - (b) For _k >_ 2, find interim vectors, _x_<sup>(2)</sup> _k_<sup>, by orthogonalizing with respect to</sup><sup>_x_˜1</sup>

3. Proceed for _k_ = 3 _, . . ._ , in turn orthogonalizing and normalizing the first of the remaining vectors w.r.t. _x_ ˜ _k−_ 1 and orthogonalizing the remaining vectors w.r.t. _x_ ˜ _k−_ 1 to get new interim vectors

Mathematically, we could instead orthogonalize _x_ 2 w.r.t. _x_ ˜1, then orthogonalize _x_ 3 w.r.t. _{x_ ˜1 _,_ ˜ _x_ 2 _}_ , etc. The algorithm above is the _modified_ G-S, and is known to be more numerically stable if the columns of _X_ are close to collinear, giving vectors that are closer to orthogonal. The resulting _x_ ˜ vectors are the columns of _Q_ . The elements of _R_ are obtained as we proceed: the diagonal values are the the normalization values in the denominators, while the off-diagonals are the inner products with the already-computed columns of _Q_ that are computed as part of the numerators.

Another way to think about this is that _R_ = _Q_<sup>_⊤_</sup> _X_ , which is the same as regressing the columns of _X_ on _Q,_ since ( _Q_<sup>_⊤_</sup> _Q_ )<sup>_−_1</sup> _Q_<sup>_⊤_</sup> _X_ = _Q_<sup>_⊤_</sup> _X_ . By construction, the first column of _X_ is a scaling of the first column of _Q_ , the second column of _X_ is a linear combination of the first two columns of _Q_ , etc., so _R_ being upper triangular makes sense.

#### **3.4.5 The “tall-skinny” QR**

Suppose you have a very large regression problem, with _n_ very large, and _n ≫ p_ . There is a variant of the QR, called the tall-skinny QR (see http://arxiv.org/pdf/0808.2664v1.pdf for details) that allows us to find the decomposition in a parallel fashion. The basic idea is to do a nested set of QR decompositions on blocks of rows of _X_ :


followed by ’reduction’ steps (this can be done in a map-reduce context) that do the _QR_ of pairs of the _R_ factors:

and


23

The full decomposition is then


The computation can be done in parallel (in particular it can be done with map-reduce) and the _Q_ matrix for big problems would generally not be computed explicitly but would be stored in its constituent pieces.

Alternatively, there is a variant on the algorithm that processes the row-blocks of _X_ serially, allowing you to do QR on a large tall-skinny matrix that you can’t fit in memory (or possibly even on disk). First you do _QR_ on _X_ 0 to get _Q_ 0 _R_ 0. Then you stack _R_ 0 on top of _X_ 1 and do QR to get _R_ 01. Then stack _R_ 01 on top of _X_ 2 to get _R_ 012, etc.

### **3.5 Determinants**

The absolute value of the determinant of a square matrix can be found from the product of the diagonals of the triangular matrix in any factorization that gives a triangular (including diagonal) matrix times an orthogonal matrix (or matrices) since the determinant of an orthogonal matrix is either one or minus one.

_|A|_ = _|QR|_ = _|Q||R|_ = _±|R|_


In R, the following will do it (on the log scale), since _R_ is stored in the upper triangle of the _$qr_ element.

myqr = **qr** (A) magn = **sum** ( **log** ( **abs** ( **diag** (myqr$qr))))

An alternative is the product of the diagonal elements of _D_ (the singular values) in the SVD factorization, _A_ = _UDV_<sup>_⊤_</sup> .

For non-negative definite matrices, we know the determinant is non-negative, so the uncertainty about the sign is not an issue. For positive definite matrices, a good approach is to use the product of the diagonal elements of the Cholesky decomposition.

One can also use the product of the eigenvalues: _|A|_ = _|_ ΓΛΓ<sup>_−_1</sup> _|_ = _|_ Γ _||_ Γ<sup>_−_1</sup> _||_ Λ _|_ = _|_ Λ _|_

**Computation** Computing from any of these diagonal or triangular matrices as the product of the diagonals is prone to overflow and underflow, so we **always** work on the log scale as the sum of the

24

log of the values. When some of these may be negative, we can always keep track of the number of negative values and take the log of the absolute values.

Often we will have the factorization as a result of other parts of the computation, so we get the determinant for free.

R’s _determinant()_ uses the LU decomposition. Supposedly _det()_ just wraps _determinant()_ , but I can’t seem to pass the _logarithm_ argument into _det()_ , so _determinant()_ seems more useful.

---

[← [1] 5.679501e+20 U <- chol (C, pivot = TRUE)](07-1-5-679501e-20-u---chol-c-pivot-true.md) · [Up: contents](index.md) · [4 Eigendecomposition and SVD →](09-4-eigendecomposition-and-svd.md)
