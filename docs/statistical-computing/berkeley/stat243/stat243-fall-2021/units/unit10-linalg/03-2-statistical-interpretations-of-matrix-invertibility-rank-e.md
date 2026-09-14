---
title: 2 Statistical interpretations of matrix invertibility, rank, etc.
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit10-linalg.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Statistical interpretations of matrix invertibility, rank, etc.

**Source:** [`units/unit10-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **2.1 Linear independence, rank, and basis vectors**

A set of vectors, _v_ 1 _, . . . vn_ , is linearly independent (LIN) when none of the vectors can be represented as a linear combination,<sup>�</sup> _civi_ , of the others for scalars, _c_ 1 _, . . . , cn_ . If we have vectors of

6

length _n_ , we can have at most _n_ linearly independent vectors. The rank of a matrix is the number of linearly independent rows (or columns - it’s the same), and is at most the minimum of the number of rows and number of columns. We’ll generally think about it in terms of the dimension of the column space - so we can just think about the number of linearly independent columns.

Any set of linearly independent vectors (say _v_ 1 _, . . . , vn_ ) span a space made up of all linear combinations of those vectors (<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_civi_).The spanning vectors are known as basis vectors.We</sup> can express a vector _y_ that is in the space with respect to (as a linear combination of) basis vectors as _y_ =<sup>�</sup> _i_<sup>_c_</sup> _i_<sup>_v_</sup> _i_<sup>, where if the basis vectors are normalized and orthogonal, we can find the weights</sup> as _ci_ = _⟨y, vi⟩_ .

Consider a regression context. We have _p_ covariates ( _p_ columns in the design matrix, _X_ ), of which _q ≤ p_ are linearly independent covariates. This means that _p−q_ of the vectors can be written as linear combos of the _q_ vectors. The space spanned by the covariate vectors is of dimension _q_ , rather than _p_ , and _X_<sup>_⊤_</sup> _X_ has _p − q_ eigenvalues that are zero. The _q_ LIN vectors are basis vectors for the space - we can represent any point in the space as a linear combination of the basis vectors. You can think of the basis vectors as being like the axes of the space, except that the basis vectors are not orthogonal. So it’s like denoting a point in _ℜ_<sup>_q_</sup> as a set of _q_ numbers telling us where on each of the axes we are - this is the same as a linear combination of axis-oriented vectors.

When fitting a regression, if _n_ = _p_ = _q_ , a vector of _n_ observations can be represented exactly as a linear combination of the _p_ basis vectors, so there is no residual and we have a single unique (and exact) solution (e.g., with _n_ = _p_ = 2, the observations fall exactly on the simple linear regression line). If _n < p_ , then we have at most _n_ linearly independent covariates (the rank is at most _n_ ). In this case we have multiple possible solutions and the system is ill-determined (under-determined). Similarly, if _q < p_ and _n ≥ p_ , the rank is again less than _p_ and we have multiple possible solutions. Of course we usually have _n > p_ , so the system is overdetermined - there is no exact solution, but regression is all about finding solutions that minimize some criterion about the differences between the observations and linear combinations of the columns of the _X_ matrix (such as least squares or penalized least squares). In standard regression, we project the observation vector onto the space spanned by the columns of the _X_ matrix, so we find the point in the space closest to the observation vector.

### **2.2 Invertibility, singularity, rank, and positive definiteness**

For square matrices, let’s consider how invertibility, singularity, rank and positive (or non-negative) definiteness relate.

Square matrices that are “regular” have an eigendecomposition, _A_ = ΓΛΓ<sup>_−_1</sup> where Γ is a matrix with the eigenvectors as the columns and Λ is a diagonal matrix of eigenvalues, Λ _ii_ = _λi_ .

7

Symmetric matrices and matrices with unique eigenvalues are regular, as are some other matrices. The number of non-zero eigenvalues is the same as the rank of the matrix. Square matrices that have an inverse are also called nonsingular, and this is equivalent to having full rank. If the matrix is symmetric, the eigenvectors and eigenvalues are real and Γ is orthogonal, so we have _A_ = ΓΛΓ<sup>_⊤_</sup> . The determinant of the matrix is the product of the eigenvalues (why?), which is zero if it is less than full rank. Note that if none of the eigenvalues are zero then _A_<sup>_−_1</sup> = ΓΛ<sup>_−_1</sup> Γ<sup>_⊤_</sup> .

Let’s focus on symmetric matrices. The symmetric matrices that tend to arise in statistics are either positive definite (p.d.) or non-negative definite (n.n.d.). If a matrix is positive definite, then by definition _x_<sup>_⊤_</sup> _Ax >_ 0 for any _x_ . Note that if Cov( _y_ ) = _A_ then _x_<sup>_⊤_</sup> _Ax_ = _x_<sup>_⊤_</sup> Cov( _y_ ) _x_ = Cov( _x_<sup>_⊤_</sup> _y_ ) = Var( _x_<sup>_⊤_</sup> _y_ ) if so positive definiteness amounts to having linear combinations of random variables (with the elements of _x_ here being the weights) having positive variance. So we must have that positive definite matrices are equivalent to variance-covariance matrices (I’ll just refer to this as a variance matrix or as a covariance matrix). If _A_ is p.d. then it has all positive eigenvalues and it must have an inverse, though as we’ll see, from a numerical perspective, we may not be able to compute it if some of the eigenvalues are very close to zero. In R, eigen(A)$vectors is Γ, with each column a vector, and eigen(A)$values contains the ordered eigenvalues.

To summarize, here are some of the various connections between mathematical and statistical properties of **positive definite** matrices:

_A_ positive definite _⇔A_ is a covariance matrix _⇔x_<sup>_⊤_</sup> _Ax >_ 0 _⇔λi >_ 0 (positive eigenvalues) _⇒|A| >_ 0 _⇒A_ is invertible _⇔A_ is non singular _⇔ A_ is full rank.

And here are connections for positive semi-definite matrices:

_A_ positive semi-definite _⇔A_ is a constrained covariance matrix _⇔x_<sup>_⊤_</sup> _Ax ≥_ 0 and equal to 0 for some _x ⇔λi ≥_ 0 (non-negative eigenvalues), with at least one zero _⇒|A|_ = 0 _⇔A_ is not invertible _⇔A_ is singular _⇔ A_ is not full rank.

### **2.3 Interpreting an eigendecomposition**

Let’s interpret the eigendecomposition in a generative context as a way of generating random vectors. We can generate _y_ s.t. Cov( _y_ ) = _A_ if we generate _y_ = ΓΛ<sup>1</sup><sup>_/_2</sup> _z_ where Cov( _z_ ) = _I_ and Λ<sup>1</sup><sup>_/_2</sup> is formed by taking the square roots of the eigenvalues. So<sup>_√_</sup> _λi_ is the standard deviation associated with the basis vector Γ _·i_ . That is, the _z_ ’s provide the weights on the basis vectors, with scaling based on the eigenvalues. So _y_ is produced as a linear combination of eigenvectors as basis vectors, with the variance attributable to the basis vectors determined by the eigenvalues.

If _x_<sup>_⊤_</sup> _Ax ≥_ 0 then _A_ is nonnegative definite (also called positive semi-definite). In this case one or more eigenvalues can be zero. Let’s interpret this a bit more in the context of generating random vectors based on non-negative definite matrices, _y_ = ΓΛ<sup>1</sup><sup>_/_2</sup> _z_ where Cov( _z_ ) = _I_ . Questions:

8

1. What does it mean when one or more eigenvalue (i.e., _λi_ = Λ _ii_ ) is zero?

2. Suppose I have an eigenvalue that is very small and I set it to zero? What will be the impact upon _y_ and Cov( _y_ )?

3. Now let’s consider the inverse of a covariance matrix, known as the precision matrix, _A_<sup>_−_1</sup> = ΓΛ<sup>_−_1</sup> Γ<sup>_⊤_</sup> . What does it mean if a (Λ<sup>_−_1</sup> ) _ii_ is very large? What if (Λ<sup>_−_1</sup> ) _ii_ is very small?

Consider an arbitrary _n × p_ matrix, _X_ . Any crossproduct or sum of squares matrix, such as _X_<sup>_⊤_</sup> _X_ is positive definite (non-negative definite if _p > n_ ). This makes sense as it’s just a scaling of an empirical covariance matrix.

### **2.4 Generalized inverses (optional)**

Suppose I want to find _x_ such that _Ax_ = _b_ . Mathematically the answer (provided _A_ is invertible, i.e. of full rank) is _x_ = _A_<sup>_−_1</sup> _b_ .

Generalized inverses arise in solving equations when _A_ is not full rank. A generalized inverse is a matrix, _A_<sup>_−_</sup> s.t. _AA_<sup>_−_</sup> _A_ = _A_ . The Moore-Penrose inverse (the pseudo-inverse), _A_<sup>+</sup> , is a (unique) generalized inverse that also satisfies some additional properties. _x_ = _A_<sup>+</sup> _b_ is the solution to the linear system, _Ax_ = _b_ , that has the shortest length for _x_ .

We can find the pseudo-inverse based on an eigendecomposition (or an SVD) as ΓΛ<sup>+</sup> Γ<sup>_⊤_</sup> . We obtain Λ<sup>+</sup> from Λ as follows. For values _λi >_ 0, compute 1 _/λi_ . All other values are set to 0. Let’s interpret this statistically. Suppose we have a precision matrix with one or more zero eigenvalues and we want to find the covariance matrix. A zero eigenvalue means we have no precision, or infinite variance, for some linear combination (i.e., for some basis vector). We take the pseudoinverse and assign that linear combination zero variance.

Let’s consider a specific example. Autoregressive models are often used for smoothing (in time, in space, and in covariates). A first order autoregressive model for _y_ 1 _, y_ 2 _, . . . , yT_ has _E_ ( _yi|y−i_ ) = <u>12</u><sup>(</sup><sup>_yi−_1+</sup><sup>_yi_+1).Anotherwayofwritingthemodelisintime-order:</sup><sup>_yi_=</sup><sup>_yi−_1+</sup><sup>_ϵi_.Asecond</sup> order autoregressive model has _E_ ( _yi|y−i_ ) = 6<sup><u>1</u>(4</sup><sup>_yi−_1 + 4</sup><sup>_yi_+1</sup><sup>_−yi−_2</sup><sup>_−yi_+2).These constructions</sup> basically state that each value should be a smoothed version of its neighbors. One can figure out that the **precision** matrix for _y_ in the first order model is


9

and in the second order model is


If we look at the eigendecomposition of such matrices, we see that in the first order case, the eigenvalue corresponding to the constant eigenvector is zero.

precMat <- **matrix** ( **c** (1,-1,0,0,0,-1,2,-1,0,0,0,-1,2,-1, 0,0,0,-1,2,-1,0,0,0,-1,1), 5) e <- **eigen** (precMat) e$values

---

[← 1 Preliminaries](02-1-preliminaries.md) · [Up: contents](index.md) · [Unit 10 — linalg Part 04 — →](04-unit-10-linalg-part-04.md)
