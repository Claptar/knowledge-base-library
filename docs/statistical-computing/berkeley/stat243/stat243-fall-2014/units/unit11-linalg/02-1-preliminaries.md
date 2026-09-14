---
title: 1 Preliminaries
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit11-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit11-linalg.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Preliminaries

**Source:** [`units/unit11-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit11-linalg.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **1.1 Goals**

Here’s what I’d like you to get out of this unit:

1. How to think about the computational order (number of computations involved) of a problem

2. How to choose a computational approach to a given linear algebra calculation you need to do.

3. An understanding of how issues with computer numbers (Unit 7) play out in terms of linear algebra.

1

### **1.2 Key principle**

**The form of a mathematical expression and how it should be evaluated on a computer may be very different.** Better computational approaches can increase speed and improve the numerical properties of the calculation.

Example 1: We do not compute ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ by computing _X_<sup>_⊤_</sup> _X_ and finding its inverse. In fact, perhaps more surprisingly, we may never actually form _X_<sup>_⊤_</sup> _X_ in some implementations.

Example 2: Suppose I have a matrix _A_ , and I want to permute (switch) two rows. I can do this with a permutation matrix, _P_ , which is mostly zeroes. On a computer, in general I wouldn’t need to even change the values of _A_ in memory in some cases (e.g., if I were to calculate _PAB_ ). Why not?

### **1.3 Computational complexity**

We can assess the computational complexity of a linear algebra calculation by counting the number multiplys/divides and the number of adds/subtracts. Sidenote: addition is a bit faster than multiplication, so some algorithms attempt to trade multiplication for addition.

In general we do not try to count the actual number of calculations, but just their order, though in some cases in this unit we’ll actually get a more exact count. In general, we denote this as _O_ ( _f_ ( _n_ )) which means that the number of calculations approaches _cf_ ( _n_ ) as _n →∞_ (i.e., we know the calculation is approximately proportional to _f_ ( _n_ )). Consider matrix multiplication, _AB_ , with matrices of size _a × b_ and _b × c_ . Each column of the second matrix is multiplied by all the rows of the first. For any given inner product of a row by a column, we have _b_ multiplies. We repeat these operations for each column and then for each row, so we have _abc_ multiplies so _O_ ( _abc_ ) operations. We could count the additions as well, but there’s usually an addition for each multiply, so we can usually just count the multiplys and then say there are such and such {multiply and add}s. This is Monahan’s approach, but you may see other counting approaches where one counts the multiplys and the adds separately.

For two symmetric, _n × n_ matrices, this is _O_ ( _n_<sup>3</sup> ). Similarly, matrix factorization (e.g., the Cholesky decomposition) is _O_ ( _n_<sup>3</sup> ) unless the matrix has special structure, such as being sparse. As matrices get large, the speed of calculations decreases drastically because of the scaling as _n_<sup>3</sup> and memory use increases drastically. In terms of memory use, to hold the result of the multiply indicated above, we need to hold _ab_ + _bc_ + _ac_ total elements, which for symmetric matrices sums to 3 _n_<sup>2</sup> . So for a matrix with _n_ = 10000, we have 3 _·_ 10000<sup>2</sup> _·_ 8 _/_ 1 _e_ 9 = 2 _._ 4Gb.

When we have _O_ ( _n_<sup>_q_</sup> ) this is known as polynomial time. Much worse is _O_ ( _b_<sup>_n_</sup> ) (exponential time), while much better is _O_ (log _n_ ) (log time). Computer scientists talk about NP-complete problems; these are essentially problems for which there is not a polynomial time algorithm - it turns

2

out all such problems can be rewritten such that they are equivalent to one another.

In real calculations, it’s possible to have the actual time ordering of two approaches differ from what the order approximations tell us. For example, something that involves _n_<sup>2</sup> operations may be faster than one that involves 1000( _n_ log _n_ + _n_ ) even though the former is _O_ ( _n_<sup>2</sup> ) and the latter _O_ ( _n_ log _n_ ). The problem is that the constant, _c_ = 1000, can matter (depending on how big _n_ is), as can the extra calculations from the lower order term(s), in this case 1000 _n_ .

A note on terminology: _flops_ stands for both floating point operations (the number of operations required) and floating point operations per second, the speed of calculation.

### **1.4 Notation and dimensions**

I’ll try to use capital letters for matrices, _A_ , and lower-case for vectors, _x_ . Then _xi_ is the ith element of _x_ , _Aij_ is the _i_ th row, _j_ th column element, and _A·j_ is the _j_ th column and _Ai·_ the _i_ th row. By default, we’ll consider a vector, _x_ , to be a one-column matrix, and _x_<sup>_⊤_</sup> to be a one-row matrix. Some of the textbook resources also use _aij_ for _Aij_ and _aj_ for the _j_ th column.

Throughout, we’ll need to be careful that the matrices involved in an operation are conformable: for _A_ + _B_ both matrices need to be of the same dimension, while for _AB_ the number of columns of _A_ must match the number of rows of _B_ . Note that this allows for _B_ to be a column vector, with only one column, _Ab_ . Just checking dimensions is a good way to catch many errors. Example: is Cov( _Ax_ ) = _A_ Cov( _x_ ) _A_<sup>_⊤_</sup> or Cov( _Ax_ ) = _A_<sup>_⊤_</sup> Cov( _x_ ) _A_ ? Well, if _A_ is _m × n_ , it must be the former, as the latter is not conformable.

The inner product of two vectors is<sup>�</sup> _i_<sup>_x_</sup> _i_<sup>_y_</sup> _i_<sup>=</sup><sup>_x⊤y≡⟨x, y⟩≡x · y_.The outer product is</sup><sup>_xy⊤_,</sup> which comes from all pairwise products of the elements.

When the indices of summation should be obvious, I’ll sometimes leave them implicit. Ask me if it’s not clear.

### **1.5 Norms**

_∥x∥p_ = (� _i_<sup>_|x_</sup> _i_<sup>_|p_)1</sup><sup>_/p_andthestandard(Euclidean)normis</sup><sup>_∥x∥_</sup> 2<sup>=</sup> ~~�~~ <u>�</u> _x_ 2 _i_<sup>=</sup> _√x_<sup>_⊤_</sup> _x_ , just the length of the vector in Euclidean space, which we’ll refer to as _∥x∥_ , unless noted otherwise. The standard norm for a matrix is the Frobenius norm, _∥A∥F_ = (<sup>�</sup> _i,j_<sup>_a_2</sup> _ij_<sup>)1</sup><sup>_/_2.There is also the induced</sup> matrix norm, corresponding to any chosen vector norm,


3

So we have


A property of any legitimate matrix norm (including the induced norm) is that _∥AB∥≤∥A∥∥B∥_ . Recall that norms must obey the triangle inequality, _∥A_ + _B∥≤∥A∥_ + _∥B∥_ .

A normalized vector is one with “length”, i.e., Euclidean norm, of one. We can easily normalize a vector: _x_ ˜ = _x/∥x∥_

The angle between two vectors is


### **1.6 Orthogonality**

Two vectors are orthogonal if _x_<sup>_⊤_</sup> _y_ = 0, in which case we say _x ⊥ y_ . An orthogonal matrix is a matrix in which all of the columns are orthogonal to each other and normalized. Orthogonal matrices can be shown to have full rank. Furthermore if _A_ is orthogonal, _A_<sup>_⊤_</sup> _A_ = _I_ , so _A_<sup>_−_1</sup> = _A_<sup>_⊤_</sup> . Given all this, the determinant of orthogonal _A_ is either 1 or -1. Finally the product of two orthogonal matrices, _A_ and _B_ , is also orthogonal since ( _AB_ )<sup>_⊤_</sup> _AB_ = _B_<sup>_⊤_</sup> _A_<sup>_⊤_</sup> _AB_ = _B_<sup>_⊤_</sup> _B_ = _I_ .

**Permutations** Sometimes we make use of matrices that permute two rows (or two columns) of another matrix when multiplied. Such a matrix is known as an elementary permutation matrix and is an orthogonal matrix with a determinant of -1. You can multiply such matrices to get more general permutation matrices that are also orthogonal. If you premultiply by _P_ , you permute rows, and if you postmultiply by _P_ you permute columns. Note that on a computer, you wouldn’t need to actually do the multiply (and if you did, you should use a sparse matrix routine), but rather one can often just rework index values that indicate where relevant pieces of the matrix are stored (more in the next section).

### **1.7 Some vector and matrix properties**

_AB̸_ = _BA_ but _A_ + _B_ = _B_ + _A_ and _A_ ( _BC_ ) = ( _AB_ ) _C_ . In R, recall the syntax is

A + B A %*% B

You don’t need the spaces, but they’re nice for code readability.

4

### **1.8 Trace and determinant of square matrices**

The trace of a matrix is the sum of the diagonal elements. For square matrices, tr( _A_ + _B_ ) = tr( _A_ ) + tr( _B_ ), tr( _A_ ) = tr( _A_<sup>_⊤_</sup> ).

We also have tr( _ABC_ ) = tr( _CAB_ ) = tr( _BCA_ ) - basically you can move a matrix from the beginning to the end or end to beginning, provided they are conformable for this operation. This is helpful for a couple reasons:

1. We can find the ordering that reduces computation the most if the individual matrices are not square.

2. _x_<sup>_⊤_</sup> _Ax_ = tr( _x_<sup>_⊤_</sup> _Ax_ ) since the quadratic form, _x_<sup>_⊤_</sup> _Ax_ , is a scalar, and this is equal to tr( _xx_<sup>_⊤_</sup> _A_ ) where _xx_<sup>_⊤_</sup> _A_ is a matrix. It can be helpful to be able to go back and forth between a scalar and a trace in some statistical calculations.

For square matrices, the determinant exists and we have _|AB|_ = _|A||B|_ and therefore, _|A_<sup>_−_1</sup> _|_ = 1 _/|A|_ since _|I|_ = _|AA_<sup>_−_1</sup> _|_ = 1. Also _|A|_ = _|A_<sup>_⊤_</sup> _|_ .

**Other matrix multiplications** The Hadamard or direct product is simply multiplication of the correspoding elements of two matrices by each other. In R this is simply A * B. **Challenge** : How can I find tr( _AB_ ) without using A %*% B ?

The Kronecker product is the product of each element of one matrix with the entire other matrix”


The inverse of a Kronecker product is the Kronecker product of the inverses,


which is obviously quite a bit faster because the inverse (i.e., solving a system of equations) in this special case is _O_ ( _n_<sup>3</sup> + _m_<sup>3</sup> ) rather than the naive approach being _O_ (( _nm_ )<sup>3</sup> ).

### **1.9 Linear independence, rank, and basis vectors**

A set of vectors, _v_ 1 _, . . . vn_ , is linearly independent (LIN) when none of the vectors can be represented as a linear combination,<sup>�</sup> _civi_ , of the others for scalars, _c_ 1 _, . . . , cn_ . If we have vectors of

5

length _n_ , we can have at most _n_ linearly independent vectors. The rank of a matrix is the number of linearly independent rows (or columns - it’s the same), and is at most the minimum of the number of rows and number of columns. We’ll generally think about it in terms of the dimension of the column space - so we can just think about the number of linearly independent columns.

Any set of linearly independent vectors (say _v_ 1 _, . . . , vn_ ) span a space made up of all linear combinations of those vectors (<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_civi_).The spanning vectors are known as basis vectors.We</sup> can express a vector _x_ that is in the space with respect to (as a linear combination of) basis vectors as _x_ =<sup>�</sup> _i_<sup>_c_</sup> _i_<sup>_v_</sup> _i_<sup>, where if the basis vectors are normalized and orthogonal, we can find the weights</sup> as _ci_ = _⟨x, vi⟩_ .

Consider a regression context. We have _p_ covariates ( _p_ columns in the design matrix, _X_ ), of which _q_ are linearly independent covariates. This means that _p − q_ of the vectors can be written as linear combos of the _q_ vectors. The space spanned by the covariate vectors is of dimension _q_ , rather than _p_ , and _X_<sup>_⊤_</sup> _X_ has _p − q_ eigenvalues that are zero. The _q_ LIN vectors are basis vectors for the space - we can represent any point in the space as a linear combination of the basis vectors. You can think of the basis vectors as being like the axes of the space, except that the basis vectors are not orthogonal. So it’s like denoting a point in _ℜ_<sup>_q_</sup> as a set of _q_ numbers telling us where on each of the axes we are - this is the same as a linear combination of axis-oriented vectors. When we have _n ≤ q_ , a vector of _n_ observations can be represented exactly as a linear combination of the _q_ basis vectors, so there is no residual. If _n_ = _q_ , then we have a single unique solution, while if _n < q_ we have multiple possible solutions and the system is ill-determined (under-determined). Of course we usually have _n > q_ , so the system is overdetermined - there is no exact solution, but regression is all about finding solutions that minimize some criterion about the differences between the observations and linear combinations of the columns of the _X_ matrix (such as least squares or penalized least squares). In standard regression, we project the observation vector onto the space spanned by the columns of the _X_ matrix, so we find the point in the space closest to the observation vector.

### **1.10 Invertibility, singularity, rank, and positive definiteness**

For square matrices, let’s consider how invertibility, singularity, rank and positive (or non-negative) definiteness relate.

Square matrices that are “regular” have an eigendecomposition, _A_ = ΓΛΓ<sup>_−_1</sup> where Γ is a matrix with the eigenvectors as the columns and Λ is a diagonal matrix of eigenvalues, Λ _ii_ = _λi_ . Symmetric matrices and matrices with unique eigenvalues are regular, as are some other matrices. The number of non-zero eigenvalues is the same as the rank of the matrix. Square matrices that have an inverse are also called nonsingular, and this is equivalent to having full rank. If the matrix is

6

symmetric, the eigenvectors and eigenvalues are real and Γ is orthogonal, so we have _A_ = ΓΛΓ<sup>_⊤_</sup> . The determinant of the matrix is the product of the eigenvalues (why?), which is zero if it is less than full rank. Note that if none of the eigenvalues are zero then _A_<sup>_−_1</sup> = ΓΛ<sup>_−_1</sup> Γ<sup>_⊤_</sup> .

Let’s focus on symmetric matrices. The symmetric matrices that tend to arise in statistics are either positive definite (p.d.) or non-negative definite (n.n.d.). If a matrix is positive definite, then by definition _x_<sup>_⊤_</sup> _Ax >_ 0 for any _x_ . Note that if Cov( _y_ ) = _A_ then _x_<sup>_⊤_</sup> _Ax_ = _x_<sup>_⊤_</sup> Cov( _y_ ) _x_ = Cov( _x_<sup>_⊤_</sup> _y_ ) = Var( _x_<sup>_⊤_</sup> _y_ ) if so positive definiteness amounts to having linear combinations of random variables having positive variance. So we must have that positive definite matrices are equivalent to variance-covariance matrices (I’ll just refer to this as a variance matrix or as a covariance matrix). If _A_ is p.d. then it has all positive eigenvalues and it must have an inverse, though as we’ll see, from a numerical perspective, we may not be able to compute it if some of the eigenvalues are very close to zero. In R, eigen(A)$vectors is Γ, with each column a vector, and eigen(A)$values contains the ordered eigenvalues.

Let’s interpret the eigendecomposition in a generative context as a way of generating random vectors. We can generate _y_ s.t. Cov( _y_ ) = _A_ if we generate _y_ = ΓΛ<sup>1</sup><sup>_/_2</sup> _z_ where Cov( _z_ ) = _I_ and Λ<sup>1</sup><sup>_/_2</sup> is formed by taking the square roots of the eigenvalues. So<sup>_√_</sup> _λi_ is the standard deviation associated with the basis vector Γ _·i_ . That is, the _z_ ’s provide the weights on the basis vectors, with scaling based on the eigenvalues. So _y_ is produced as a linear combination of eigenvectors as basis vectors, with the variance attributable to the basis vectors determined by the eigenvalues.

If _x_<sup>_⊤_</sup> _Ax ≥_ 0 then _A_ is nonnegative definite (also called positive semi-definite). In this case one or more eigenvalues can be zero. Let’s interpret this a bit more in the context of generating random vectors based on non-negative definite matrices, _y_ = ΓΛ<sup>1</sup><sup>_/_2</sup> _z_ where Cov( _z_ ) = _I_ . Questions:

1. What does it mean when one or more eigenvalue (i.e., _λi_ = Λ _ii_ ) is zero?

2. Suppose I have an eigenvalue that is very small and I set it to zero? What will be the impact upon _y_ and Cov( _y_ )?

3. Now let’s consider the inverse of a covariance matrix, known as the precision matrix, _A_<sup>_−_1</sup> = ΓΛ<sup>_−_1</sup> Γ<sup>_⊤_</sup> . What does it mean if a (Λ<sup>_−_1</sup> ) _ii_ is very large? What if (Λ<sup>_−_1</sup> ) _ii_ is very small?

Consider an arbitrary _n × p_ matrix, _X_ . Any crossproduct or sum of squares matrix, such as _X_<sup>_⊤_</sup> _X_ is positive definite (non-negative definite if _p > n_ ). This makes sense as it’s just a scaling of an empirical covariance matrix.

### **1.11 Generalized inverses**

Suppose I want to find _x_ such that _Ax_ = _b_ . Mathematically the answer (provided _A_ is invertible, i.e. of full rank) is _x_ = _A_<sup>_−_1</sup> _b_ .

7

Generalized inverses arise in solving equations when _A_ is not full rank. A generalized inverse is a matrix, _A_<sup>_−_</sup> s.t. _AA_<sup>_−_</sup> _A_ = _A_ . The Moore-Penrose inverse (the pseudo-inverse), _A_<sup>+</sup> , is a (unique) generalized inverse that also satisfies some additional properties. _x_ = _A_<sup>+</sup> _b_ is the solution to the linear system, _Ax_ = _b_ , that has the shortest length for _x_ .

We can find the pseudo-inverse based on an eigendecomposition (or an SVD) as ΓΛ<sup>+</sup> Γ<sup>_⊤_</sup> . We obtain Λ<sup>+</sup> from Λ as follows. For values _λi >_ 0, compute 1 _/λi_ . All other values are set to 0. Let’s interpret this statistically. Suppose we have a precision matrix with one or more zero eigenvalues and we want to find the covariance matrix. A zero eigenvalue means we have no precision, or infinite variance, for some linear combination (i.e., for some basis vector). We take the pseudoinverse and assign that linear combination zero variance.

Let’s consider a specific example. Autoregressive models are often used for smoothing (in time, in space, and in covariates). A first order autoregressive model for _y_ 1 _, y_ 2 _, . . . , yT_ has _E_ ( _yi|y−i_ ) = <u>12</u><sup>(</sup><sup>_yi−_1+</sup><sup>_yi_+1).Anotherwayofwritingthemodelisintime-order:</sup><sup>_yi_=</sup><sup>_yi−_1+</sup><sup>_ϵi_.Asecond</sup> order autoregressive model has _E_ ( _yi|y−i_ ) = 6<sup><u>1</u>(4</sup><sup>_yi−_1 + 4</sup><sup>_yi_+1</sup><sup>_−yi−_2</sup><sup>_−yi_+2).These constructions</sup> basically state that each value should be a smoothed version of its neighbors. One can figure out that the **precision** matrix for _y_ in the first order model is


and in the second order model is


If we look at the eigendecomposition of such matrices, we see that in the first order case, the eigenvalue corresponding to the constant eigenvector is zero.

precMat <- **matrix** ( **c** (1,-1,0,0,0,-1,2,-1,0,0,0,-1,2,-1, 0,0,0,-1,2,-1,0,0,0,-1,1), 5)

e <- **eigen** (precMat)

8

e$values ## [1] 3.618034 2.618034 1.381966 0.381966 0.000000 e$vectors[ , 5]

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Unit 11 — linalg Part 03 — →](03-unit-11-linalg-part-03.md)
