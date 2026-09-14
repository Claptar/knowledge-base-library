---
title: 5 Eigendecomposition and SVD
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit10-linalg.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Eigendecomposition and SVD

**Source:** [`units/unit10-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **5.1 Eigendecomposition**

The eigendecomposition (spectral decomposition) is useful in considering convergence of algorithms and of course for statistical decompositions such as PCA. We think of decomposing the components of variation into orthogonal patterns (the eigenvectors) with variances (eigenvalues) associated with each pattern.

Square symmetric matrices have real eigenvectors and eigenvalues, with the factorization into orthogonal Γ and diagonal Λ, _A_ = ΓΛΓ<sup>_⊤_</sup> , where the eigenvalues on the diagonal of Λ are ordered in decreasing value. Of course this is equivalent to the definition of an eigenvalue/eigenvector pair as a pair such that _Ax_ = _λx_ where _x_ is the eigenvector and _λ_ is a scalar, the eigenvalue. The inverse of the eigendecomposition is simply ΓΛ<sup>_−_1</sup> Γ<sup>_⊤_</sup> . On a similar note, we can create a square root matrix, ΓΛ<sup>1</sup><sup>_/_2</sup> , by taking the square roots of the eigenvalues.

The spectral radius of _A_ , denoted _ρ_ ( _A_ ), is the maximum of the absolute values of the eigenvalues. As we saw when talking about ill-conditionedness, for symmetric matrices, this maximum is the induced norm, so we have _ρ_ ( _A_ ) = _∥A∥_ 2. It turns out that _ρ_ ( _A_ ) _≤∥A∥_ for any induced matrix norm. The spectral radius comes up in determining the rate of convergence of some iterative algorithms.

**Computation** There are several methods for eigenvalues; a common one for doing the full eigendecomposition is the _QR algorithm_ . The first step is to reduce _A_ to upper Hessenburg form, which is an upper triangular matrix except that the first subdiagonal in the lower triangular part can be non-zero. For symmetric matrices, the result is actually tridiagonal. We can do the reduction using Householder reflections or Givens rotations. At this point the QR decomposition (using Givens rotations) is applied iteratively (to a version of the matrix in which the diagonals are shifted), and the result converges to a diagonal matrix, which provides the eigenvalues. It’s more work to get the

28

eigenvectors, but they are obtained as a product of Householder matrices (required for the initial reduction) multiplied by the product of the _Q_ matrices from the successive QR decompositions.

We won’t go into the algorithm in detail, but note that it involves manipulations and ideas we’ve seen already.

If only the largest (or the first few largest) eigenvalues and their eigenvectors are needed, which can come up in time series and Markov chain contexts, the problem is easier and can be solved by the _power method_ . E.g., in a Markov chain context, steady state is reached through _xt_ = _A_<sup>_t_</sup> _x_ 0. One can find the largest eigenvector by multiplying by _A_ many times, normalizing at each step. _v_<sup>(</sup><sup>_k_)</sup> = _Az_<sup>(</sup><sup>_k−_1)</sup> and _z_<sup>(</sup><sup>_k_)</sup> = _v_<sup>(</sup><sup>_k_)</sup> _/∥v_<sup>(</sup><sup>_k_)</sup> _∥_ . There is an extension to find the _p_ largest eigenvalues and their vectors. See the demo code for an implementation.

### **5.2 Singular value decomposition**

Let’s consider an _n × m_ matrix, _A_ , with _n ≥ m_ (if _m > n_ , we can always work with _A_<sup>_⊤_</sup> ). This often is a matrix representing _m_ features of _n_ observations. We could have _n_ documents and _m_ words, or _n_ gene expression levels and _m_ experimental conditions, etc. _A_ can always be decomposed as


where _U_ and _V_ are matrices with orthonormal columns (left and right eigenvectors) and _D_ is diagonal with non-negative values (which correspond to eigenvalues in the case of square _A_ and to squared eigenvalues of _A_<sup>_⊤_</sup> _A_ ).

The SVD can be represented in more than one way. One representation is


where _uj_ and _vj_ are the columns of _U_ and _V_ and where _k_ is the rank of _A_ (which is at most the minimum of _n_ and _m_ of course). The diagonal elements of _D_ are the singular values.

If _A_ is positive semi-definite, the eigendecomposition is an SVD. Furthermore, _A_<sup>_⊤_</sup> _A_ = _V D_<sup>2</sup> _V_<sup>_⊤_</sup> and _AA_<sup>_⊤_</sup> = _UD_<sup>2</sup> _U_<sup>_⊤_</sup> , so we can find the eigendecomposition of such matrices using the SVD of _A_ (for _AA_<sup>_⊤_</sup> we need to fill out _U_ to have _n_ columns). Note that the squares of the singular values of _A_ are the eigenvalues of _A_<sup>_⊤_</sup> _A_ and _AA_<sup>_⊤_</sup> .

We can also fill out the matrices to get


where the added rows and columns of _D_ are zero with the upper left block the _Dk×k_ from above.

29

**Uses** The SVD is an excellent way to determine a matrix rank and to construct a pseudo-inverse ( _A_<sup>+</sup> = _V D_<sup>+</sup> _U_<sup>_⊤_</sup> ).

We can use the SVD to approximate _A_ by taking _A ≈ A_<sup>˜</sup> = � _pj_ =1<sup>_Djjujv_</sup> _j_<sup>_⊤_for</sup><sup>_p<m_.This</sup> approximation holds in terms of the Frobenius norm for _A − A_<sup>˜</sup> . As an example if we have a large image of dimension _n × m_ , we could hold a compressed version by a rank- _p_ approximation using the SVD. The SVD is used a lot in clustering problems. For example, the Netflix prize was won based on a variant of SVD (in fact all of the top methods used variants on SVD, I believe).

**Computation** The basic algorithm (Golub-Reinsch) is similar to the QR method for the eigendecomposition. We use a series of Householder transformations on the left and right to reduce _A_ to an upper bidiagonal matrix, _A_<sup>(0)</sup> . The post-multiplications (the transformations on the right) generate the zeros in the upper triangle. (An upper bidiagonal matrix is one with non-zeroes only on the diagonal and first subdiagonal above the diagonal). Then the algorithm produces a series of upper bidiagonal matrices, _A_<sup>(0)</sup> , _A_<sup>(1)</sup> _,_ etc. that converge to a diagonal matrix, _D_ . Each step is carried out by a sequence of Givens transformations:


This eventually gives _A_<sup>(</sup><sup>_..._)</sup> = _D_ and by construction, _U_ (the product of the pre-multiplied Householder matrices and the _R_ matrices) and _V_ (the product of the post-multiplied Householder matrices and the _T_ matrices) are orthogonal. The result is then transformed by a diagonal matrix to make the elements of _D_ non-negative and by permutation matrices to order the elements of _D_ in nonincreasing order.

**Computation for large tall-skinny matrices** The SVD can also be generated from a QR decomposition. Take _X_ = _QR_ and then do an SVD on the _R_ matrix to get _X_ = _QUDV_<sup>_⊤_</sup> = _U_<sup>_∗_</sup> _DV_<sup>_⊤_</sup> . This is particularly helpful for the case when _X_ is tall and skinny (suppose _X_ is _n×p_ with _n ≫ p_ ), because we can do the tall-skinny QR, and the resulting SVD on _R_ is easy computationally if _p_ is manageable.

30

---

[← Unit 10 — linalg Part 11 —](11-unit-10-linalg-part-11.md) · [Up: contents](index.md) · [6 Computation →](13-6-computation.md)
