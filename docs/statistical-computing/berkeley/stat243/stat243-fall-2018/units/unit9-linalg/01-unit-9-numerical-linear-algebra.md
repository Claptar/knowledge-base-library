---
title: 'Unit 9: Numerical linear algebra'
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit9-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit9-linalg.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 9: Numerical linear algebra

**Source:** [`units/unit9-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit9-linalg.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

October 26, 2018

References:

- Gentle: Numerical Linear Algebra for Applications in Statistics (my notes here are based primarily on this source) [Gentle-NLA]

   - Unfortunately, this is not in the UCB library system - I have a copy that you can take a look at.

- Gentle: Computational Statistics [Gentle-CS]

- Lange: Numerical Analysis for Statisticians

- Monahan: Numerical Methods of Statistics

In working through how to compute something or understanding an algorithm, it can be very helpful to depict the matrices and vectors graphically. We’ll see this on the board in class.

## **1 Preliminaries**

### **1.1 Context**

Many statistical and machine learning methods involve linear algebra of some sort - at the very least matrix multiplication and very often some sort of matrix decomposition to fit models and do analysis: linear regression, various more sophisticated forms of regression, deep neural networks, principle components analysis (PCA) and the wide varieties of generalizations and variations on PCA, etc., etc.

1

### **1.2 Goals**

Here’s what I’d like you to get out of this unit:

1. How to think about the computational order (number of computations involved) of a problem

2. How to choose a computational approach to a given linear algebra calculation you need to do.

3. An understanding of how issues with computer numbers (Unit 6) affect linear algebra calculations.

### **1.3 Key principle**

**The form of a mathematical expression and how it should be evaluated on a computer may be very different.** Better computational approaches can increase speed and improve the numerical properties of the calculation.

Example 1 (already seen in Unit 4): If _X_ and _Y_ are matrices and _z_ is a vector, we should compute _X_ ( _Y z_ ) rather than ( _XY_ ) _z_ ; the former is much more computationally efficient.

Example 2: We do not compute ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ by computing _X_<sup>_⊤_</sup> _X_ and finding its inverse. In fact, perhaps more surprisingly, we may never actually form _X_<sup>_⊤_</sup> _X_ in some implementations.

Example 3: Suppose I have a matrix _A_ , and I want to permute (switch) two rows. I can do this with a permutation matrix, _P_ , which is mostly zeroes. On a computer, in general I wouldn’t need to even change the values of _A_ in memory in some cases (e.g., if I were to calculate _PAB_ ). Why not?

### **1.4 Computational complexity**

We can assess the computational complexity of a linear algebra calculation by counting the number multiplys/divides and the number of adds/subtracts. Sidenote: addition is a bit faster than multiplication, so some algorithms attempt to trade multiplication for addition.

In general we do not try to count the actual number of calculations, but just their order, though in some cases in this unit we’ll actually get a more exact count. In general, we denote this as _O_ ( _f_ ( _n_ )) which means that the number of calculations approaches _cf_ ( _n_ ) as _n →∞_ (i.e., we know the calculation is approximately proportional to _f_ ( _n_ )). Consider matrix multiplication, _AB_ , with matrices of size _a × b_ and _b × c_ . Each column of the second matrix is multiplied by all the rows of the first. For any given inner product of a row by a column, we have _b_ multiplies. We repeat these operations for each column and then for each row, so we have _abc_ multiplies so _O_ ( _abc_ ) operations. We could count the additions as well, but there’s usually an addition for each multiply, so we can

2

usually just count the multiplys and then say there are such and such {multiply and add}s. This is Monahan’s approach, but you may see other counting approaches where one counts the multiplys and the adds separately.

For two symmetric, _n × n_ matrices, this is _O_ ( _n_<sup>3</sup> ). Similarly, matrix factorization (e.g., the Cholesky decomposition) is _O_ ( _n_<sup>3</sup> ) unless the matrix has special structure, such as being sparse. As matrices get large, the speed of calculations decreases drastically because of the scaling as _n_<sup>3</sup> and memory use increases drastically. In terms of memory use, to hold the result of the multiply indicated above, we need to hold _ab_ + _bc_ + _ac_ total elements, which for symmetric matrices sums to 3 _n_<sup>2</sup> . So for a matrix with _n_ = 10000, we have 3 _·_ 10000<sup>2</sup> _·_ 8 _/_ 1 _e_ 9 = 2 _._ 4Gb.

When we have _O_ ( _n_<sup>_q_</sup> ) this is known as polynomial time. Much worse is _O_ ( _b_<sup>_n_</sup> ) (exponential time), while much better is _O_ (log _n_ ) (log time). Computer scientists talk about NP-complete problems; these are essentially problems for which there is not a polynomial time algorithm - it turns out all such problems can be rewritten such that they are equivalent to one another.

In real calculations, it’s possible to have the actual time ordering of two approaches differ from what the order approximations tell us. For example, something that involves _n_<sup>2</sup> operations may be faster than one that involves 1000( _n_ log _n_ + _n_ ) even though the former is _O_ ( _n_<sup>2</sup> ) and the latter _O_ ( _n_ log _n_ ). The problem is that the constant, _c_ = 1000, can matter (depending on how big _n_ is), as can the extra calculations from the lower order term(s), in this case 1000 _n_ .

A note on terminology: _flops_ stands for both floating point operations (the number of operations required) and floating point operations per second, the speed of calculation.

### **1.5 Notation and dimensions**

I’ll try to use capital letters for matrices, _A_ , and lower-case for vectors, _x_ . Then _xi_ is the ith element of _x_ , _Aij_ is the _i_ th row, _j_ th column element, and _A·j_ is the _j_ th column and _Ai·_ the _i_ th row. By default, we’ll consider a vector, _x_ , to be a one-column matrix, and _x_<sup>_⊤_</sup> to be a one-row matrix. Some of the textbook resources also use _aij_ for _Aij_ and _aj_ for the _j_ th column.

Throughout, we’ll need to be careful that the matrices involved in an operation are conformable: for _A_ + _B_ both matrices need to be of the same dimension, while for _AB_ the number of columns of _A_ must match the number of rows of _B_ . Note that this allows for _B_ to be a column vector, with only one column, _Ab_ . Just checking dimensions is a good way to catch many errors. Example: is Cov( _Ax_ ) = _A_ Cov( _x_ ) _A_<sup>_⊤_</sup> or Cov( _Ax_ ) = _A_<sup>_⊤_</sup> Cov( _x_ ) _A_ ? Well, if _A_ is _m × n_ , it must be the former, as the latter is not conformable.

The **inner product** of two vectors is<sup>�</sup> _i_<sup>_x_</sup> _i_<sup>_y_</sup> _i_<sup>=</sup><sup>_x⊤y≡⟨x, y⟩≡x · y_.</sup>

The **outer product** is _xy_<sup>_⊤_</sup> , which comes from all pairwise products of the elements. When the indices of summation should be obvious, I’ll sometimes leave them implicit. Ask me

3

if it’s not clear.

### **1.6 Norms**

_∥x∥p_ = (<sup>�</sup> _i_<sup>_|x_</sup> _i_<sup>_|p_)1</sup><sup>_/p_andthestandard(Euclidean)normis</sup><sup>_∥x∥_</sup> 2<sup>=</sup> ~~�~~ <u>�</u> _x_ 2 _i_<sup>=</sup> _√x_<sup>_⊤_</sup> _x_ , just the length of the vector in Euclidean space, which we’ll refer to as _∥x∥_ , unless noted otherwise. One commonly used norm for a matrix is the Frobenius norm, _∥A∥F_ = (<sup>�</sup> _i,j_<sup>_a_2</sup> _ij_<sup>)1</sup><sup>_/_2.</sup>

In this Unit, we’ll make use of the **induced matrix norm** , which is defined relative to a corresponding vector norm, _∥· ∥_ , as:


So we have


A property of any legitimate matrix norm (including the induced norm) is that _∥AB∥≤∥A∥∥B∥_ . Recall that norms must obey the triangle inequality, _∥A_ + _B∥≤∥A∥_ + _∥B∥_ .

A normalized vector is one with “length”, i.e., Euclidean norm, of one. We can easily normalize a vector: _x_ ˜ = _x/∥x∥_

The angle between two vectors is


### **1.7 Orthogonality**

Two vectors are orthogonal if _x_<sup>_⊤_</sup> _y_ = 0, in which case we say _x ⊥ y_ . An **orthogonal matrix** is a matrix in which all of the columns are orthogonal to each other and normalized. Orthogonal matrices can be shown to have full rank. Furthermore if _A_ is orthogonal, _A_<sup>_⊤_</sup> _A_ = _I_ , so _A_<sup>_−_1</sup> = _A_<sup>_⊤_</sup> . Given all this, the determinant of orthogonal _A_ is either 1 or -1. Finally the product of two orthogonal matrices, _A_ and _B_ , is also orthogonal since ( _AB_ )<sup>_⊤_</sup> _AB_ = _B_<sup>_⊤_</sup> _A_<sup>_⊤_</sup> _AB_ = _B_<sup>_⊤_</sup> _B_ = _I_ .

**Permutations** Sometimes we make use of matrices that permute two rows (or two columns) of another matrix when multiplied. Such a matrix is known as an elementary permutation matrix and is an orthogonal matrix with a determinant of -1. You can multiply such matrices to get more general permutation matrices that are also orthogonal. If you premultiply by _P_ , you permute rows, and if you postmultiply by _P_ you permute columns. Note that on a computer, you wouldn’t need to actually do the multiply (and if you did, you should use a sparse matrix routine), but rather one can

4

often just rework index values that indicate where relevant pieces of the matrix are stored (more in the next section).

### **1.8 Some vector and matrix properties**

_AB̸_ = _BA_ but _A_ + _B_ = _B_ + _A_ and _A_ ( _BC_ ) = ( _AB_ ) _C_ . In R, recall the syntax is

A + B A %*% B _# matrix multiplication_ A * B _# Hadamard (direct) product_

You don’t need the spaces, but they’re nice for code readability.

### **1.9 Trace and determinant of square matrices**

The trace of a matrix is the sum of the diagonal elements. For square matrices, tr( _A_ + _B_ ) = tr( _A_ ) + tr( _B_ ), tr( _A_ ) = tr( _A_<sup>_⊤_</sup> ).

We also have tr( _ABC_ ) = tr( _CAB_ ) = tr( _BCA_ ) - basically you can move a matrix from the beginning to the end or end to beginning, provided they are conformable for this operation. This is helpful for a couple reasons:

1. We can find the ordering that reduces computation the most if the individual matrices are not square.

2. _x_<sup>_⊤_</sup> _Ax_ = tr( _x_<sup>_⊤_</sup> _Ax_ ) since the quadratic form, _x_<sup>_⊤_</sup> _Ax_ , is a scalar, and this is equal to tr( _xx_<sup>_⊤_</sup> _A_ ) where _xx_<sup>_⊤_</sup> _A_ is a matrix. It can be helpful to be able to go back and forth between a scalar and a trace in some statistical calculations.

For square matrices, the determinant exists and we have _|AB|_ = _|A||B|_ and therefore, _|A_<sup>_−_1</sup> _|_ = 1 _/|A|_ since _|I|_ = _|AA_<sup>_−_1</sup> _|_ = 1. Also _|A|_ = _|A_<sup>_⊤_</sup> _|_ , which can be seen using the QR decomposition for _A_ and understanding properties of determinants of triangular matrices (in this case _R_ ) and orthogonal matrices (in this case _Q_ ).

For square, invertible matrices, we have that ( _A_<sup>_−_1</sup> )<sup>_⊤_</sup> = ( _A_<sup>_⊤_</sup> )<sup>_−_1</sup> . Why? Since we have ( _AB_ )<sup>_⊤_</sup> = _B_<sup>_⊤_</sup> _A_<sup>_⊤_</sup> , we have:

_A_<sup>_⊤_</sup> ( _A_<sup>_−_1</sup> )<sup>_⊤_</sup> = ( _A_<sup>_−_1</sup> _A_ )<sup>_⊤_</sup> = _I_

so ( _A_<sup>_⊤_</sup> )<sup>_−_1</sup> = ( _A_<sup>_−_1</sup> )<sup>_⊤_</sup> .

5

**Other matrix multiplications** The Hadamard or direct product is simply multiplication of the correspoding elements of two matrices by each other. In R this is simply A * B. **Challenge** : How can I find tr( _AB_ ) without using A %*% B ?

The Kronecker product is the product of each element of one matrix with the entire other matrix”


The inverse of a Kronecker product is the Kronecker product of the inverses,


which is obviously quite a bit faster because the inverse (i.e., solving a system of equations) in this special case is _O_ ( _n_<sup>3</sup> + _m_<sup>3</sup> ) rather than the naive approach being _O_ (( _nm_ )<sup>3</sup> ).

### **1.10 Matrix decompositions**

A matrix decomposition is a re-expression of a matrix, _A_ , in terms of a product of two or three other, simpler matrices, where the decomposition shows structure or relationships present in the original matrix, _A_ . The “simpler” matrices may be simpler in various ways, including

- having fewer rows or columns;

- being diagonal, triangular or sparse in some way,

- being orthogonal matrices.

In addition, once you have a decomposition, computation is generally easier, because of the special structure of the simpler matrices.

We’ll see this in great detail in Section 3.

## **2 Statistical interpretations of matrix invertibility, rank, etc.**

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

_A_ positive definite _⇔A_ is a covariance matrix _⇔x_<sup>_⊤_</sup> _Ax >_ 0 _⇔λi >_ 0 (positive eigenvalues) _⇒|A| >_ 0 _⇔A_ is invertible _⇔A_ is non singular _⇔ A_ is full rank.

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

### **2.4 Generalized inverses**

Suppose I want to find _x_ such that _Ax_ = _b_ . Mathematically the answer (provided _A_ is invertible, i.e. of full rank) is _x_ = _A_<sup>_−_1</sup> _b_ .

Generalized inverses arise in solving equations when _A_ is not full rank. A generalized inverse is a matrix, _A_<sup>_−_</sup> s.t. _AA_<sup>_−_</sup> _A_ = _A_ . The Moore-Penrose inverse (the pseudo-inverse), _A_<sup>+</sup> , is a (unique) generalized inverse that also satisfies some additional properties. _x_ = _A_<sup>+</sup> _b_ is the solution to the linear system, _Ax_ = _b_ , that has the shortest length for _x_ .

We can find the pseudo-inverse based on an eigendecomposition (or an SVD) as ΓΛ<sup>+</sup> Γ<sup>_⊤_</sup> . We obtain Λ<sup>+</sup> from Λ as follows. For values _λi >_ 0, compute 1 _/λi_ . All other values are set to 0. Let’s interpret this statistically. Suppose we have a precision matrix with one or more zero eigenvalues and we want to find the covariance matrix. A zero eigenvalue means we have no precision, or infinite variance, for some linear combination (i.e., for some basis vector). We take the pseudoinverse and assign that linear combination zero variance.

Let’s consider a specific example. Autoregressive models are often used for smoothing (in time, in space, and in covariates). A first order autoregressive model for _y_ 1 _, y_ 2 _, . . . , yT_ has _E_ ( _yi|y−i_ ) = <u>12</u><sup>(</sup><sup>_yi−_1+</sup><sup>_yi_+1).Anotherwayofwritingthemodelisintime-order:</sup><sup>_yi_=</sup><sup>_yi−_1+</sup><sup>_ϵi_.Asecond</sup> order autoregressive model has _E_ ( _yi|y−i_ ) = 6<sup><u>1</u>(4</sup><sup>_yi−_1 + 4</sup><sup>_yi_+1</sup><sup>_−yi−_2</sup><sup>_−yi_+2).These constructions</sup> basically state that each value should be a smoothed version of its neighbors. One can figure out that the **precision** matrix for _y_ in the first order model is


9

and in the second order model is


If we look at the eigendecomposition of such matrices, we see that in the first order case, the eigenvalue corresponding to the constant eigenvector is zero.

precMat <- **matrix** ( **c** (1,-1,0,0,0,-1,2,-1,0,0,0,-1,2,-1, 0,0,0,-1,2,-1,0,0,0,-1,1), 5) e <- **eigen** (precMat) e$values

## [1] 3.618034 2.618034 1.381966 0.381966 0.000000 e$vectors[ , 5] ## [1] 0.4472136 0.4472136 0.4472136 0.4472136 0.4472136

This means we have no information about the overall level of _y_ . So how would we generate sample _y_ vectors? We can’t put infinite variance on the constant basis vector and still generate samples. Instead we use the pseudo-inverse and assign ZERO variance to the constant basis vector. This corresponds to generating realizations under the constraint that<sup>�</sup> _yi_ has no variation, i.e., � _yi_ = _y_ ¯ = 0 - you can see this by seeing that Var(Γ _⊤·i_<sup>_y_) = 0 when</sup><sup>_λi_= 0.</sup>

_# generate a realization_ e$values[1:4] <- 1 / e$values[1:4] y <- e$vec %*% ( **sqrt** (e$values) * **rnorm** (5)) **sum** (y) ## [1] 2.178813e-15

In the second order case, we have two non-identifiabilities: for the sum and for the linear component of the variation in _y_ (linear in the indices of _y_ ).

I could parameterize a statistical model as _µ_ + _y_ where _y_ has covariance that is the generalized inverse discussed above. Then I allow for both a non-zero mean and for smooth variation governed

10

by the autoregressive structure. In the second-order case, I would need to add a linear component as well, given the second non-identifiability.

### **2.5 Matrices arising in regression**

In regression, we work with _X_<sup>_⊤_</sup> _X_ . Some properties of this matrix are that it is symmetric and non-negative definite (hence our use of ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> in the OLS estimator). When is it not positive definite?

Fitted values are _Xβ_<sup>ˆ</sup> = _X_ ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ = _HY_ . The “hat” matrix, _H_ , projects _Y_ into the column space of _X_ . _H_ is idempotent: _HH_ = _H_ , which makes sense - once you’ve projected into the space, any subsequent projection just gives you the same thing back. _H_ is singular. Why? Also, under what special circumstance would it not be singular?

## **3 Computational issues**

### **3.1 Storing matrices**

We’ve discussed column-major and row-major storage of matrices. First, retrieval of matrix elements from memory is quickest when multiple elements are contiguous in memory. So in a column-major language (e.g., R, Fortran), it is best to work with values in a common column (or entire columns) while in a row-major language (e.g., Python, C) for values in a common row.

In some cases, one can save space (and potentially speed) by overwriting the output from a matrix calculation into the space occupied by an input. This occurs in some clever implementations of matrix factorizations.

### **3.2 Algorithms**

Good algorithms can change the efficiency of an algorithm by one or more orders of magnitude, and many of the improvements in computational speed over recent decades have been in algorithms rather than in computer speed.

Most matrix algebra calculations can be done in multiple ways. For example, we could compute _b_ = _Ax_ in either of the following ways, denoted here in pseudocode.

1. Stack the inner products of the rows of _A_ with _x_ .


11


2. Take the linear combination (based on _x_ ) of the columns of _A_


In this case the two approaches involve the same number of operations but the first might be better for row-major matrices (so might be how we would implement in C) and the second for columnmajor (so might be how we would implement in Fortran). **Challenge** : check whether the second approach is faster in R. (Write the code just doing the outer loop and doing the inner loop using vectorized calculation.)

**General computational issues** The same caveats we discussed in terms of computer arithmetic hold naturally for linear algebra, since this involves arithmetic with many elements. Good implementations of algorithms are aware of the danger of catastrophic cancellation and of the possibility of dividing by zero or by values that are near zero.

### **3.3 Ill-conditioned problems**

**Basics** A problem is ill-conditioned if small changes to values in the computation result in large changes in the result. This is quantified by something called the _condition number_ of a calculation. For different operations there are different condition numbers.

Ill-conditionedness arises most often in terms of matrix inversion, so the standard condition number is the “condition number with respect to inversion”, which when using the _L_ 2 norm is the

12

ratio of the absolute values of the largest to smallest eigenvalue. Here’s an example:


The solution of _Ax_ = _b_ for _b_ = (32 _,_ 23 _,_ 33 _,_ 31) is _x_ = (1 _,_ 1 _,_ 1 _,_ 1), while the solution for _b_ + _δb_ = (32 _._ 1 _,_ 22 _._ 9 _,_ 33 _._ 1 _,_ 30 _._ 9) is _x_ + _δx_ = (9 _._ 2 _, −_ 12 _._ 6 _,_ 4 _._ 5 _, −_ 1 _._ 1), where _δ_ is notation for a perturbation to the vector or matrix. What’s going on?

norm2 <- **function** (x) **sqrt** ( **sum** (x^2)) A <- **matrix** ( **c** (10,7,8,7,7,5,6,5,8,6,10,9,7,5,9,10),4) e <- **eigen** (A) b <- **c** (32, 23, 33, 31) bPerturbed <- **c** (32.1, 22.9, 33.1, 30.9) x <- **solve** (A, b) xPerturbed <- **solve** (A, bPerturbed) **norm2** (x - xPerturbed) _## delta x_ ## [1] 16.39695 **norm2** (b - bPerturbed) _## delta b_ ## [1] 0.2 **norm2** (x - xPerturbed)/ **norm2** (x) ## [1] 8.198475 (e$val[1]/e$val[4])* **norm2** (b - bPerturbed)/ **norm2** (b) ## [1] 9.942834

Some manipulations with inequalities involving the induced matrix norm (for any chosen vector norm, but we might as well just think about the Euclidean norm) (see Gentle-CS Sec. 5.1) give


where we define the condition number w.r.t. inversion as cond( _A_ ) _≡∥A∥∥A_<sup>_−_1</sup> _∥_ . We’ll generally

13

work with the _L_ 2 norm, and for a nonsingular square matrix the result is that the condition number is the ratio of the absolute values of the largest and smallest magnitude eigenvalues. This makes sense since _∥A∥_ 2 is the absolute value of the largest magnitude eigenvalue of _A_ and _∥A_<sup>_−_1</sup> _∥_ 2 that of the inverse of the absolute value of the smallest magnitude eigenvalue of _A_ . We see in the code above that the large disparity in eigenvalues of _A_ leads to an effect predictable from our inequality above, with the condition number helping us find an upper bound.

The main use of these ideas for our purposes is in thinking about the numerical accuracy of a linear system solution (Gentle-NLA Sec 3.4). On a computer we have the system


where the ’perturbation’ is from the inaccuracy of computer numbers. Our exploration of computer numbers tells us that


where _p_ = 16 for standard double precision floating points. Following Gentle, one gets the approximation


so if cond( _A_ ) _≈_ 10<sup>_t_</sup> , we have accuracy of order 10<sup>_t−p_</sup> instead of 10<sup>_−p_</sup> . (Gentle cautions that this holds only if 10<sup>_t−p_</sup> _≪_ 1). So we can think of the condition number as giving us the number of digits of accuracy lost during a computation relative to the precision of numbers on the computer. E.g., a condition number of 10<sup>8</sup> means we lose 8 digits of accuracy relative to our original 16 on standard systems. One issue is that estimating the condition number is itself subject to numerical error and requires computation of _A_<sup>_−_1</sup> (albeit not in the case of _L_ 2 norm with square, nonsingular _A_ ) but see Golub and van Loan (1996; p. 76-78) for an algorithm.

**Improving conditioning** Ill-conditioned problems in statistics often arise from collinearity of regressors. Often the best solution is not a numerical one, but re-thinking the modeling approach, as this generally indicates statistical issues beyond just the numerical difficulties.

A general comment on improving conditioning is that we want to avoid large differences in the magnitudes of numbers involved in a calculation. In some contexts such as regression, we can center and scale the columns to avoid such differences - this will improve the condition of the problem. E.g., in simple quadratic regression with _x_ = _{_ 1990 _, . . . ,_ 2010 _}_ (e.g., regressing on calendar years), we see that centering and scaling the matrix columns makes a huge difference on the condition number

14

x1 <- 1990:2010 x2 <- x1 - 2000 _# centered_ x3 <- x2/10 _# centered and scaled_ X1 <- **cbind** ( **rep** (1, 21), x1, x1^2) X2 <- **cbind** ( **rep** (1, 21), x2, x2^2) X3 <- **cbind** ( **rep** (1, 21), x3, x3^2) e1 <- **eigen** ( **crossprod** (X1)) e1$values ## [1] 3.360186e+14 7.699100e+02 -3.833498e-08 e2 <- **eigen** ( **crossprod** (X2)) e2$values ## [1] 50677.704275 770.000000 9.295725 e3 <- **eigen** ( **crossprod** (X3)) e3$values ## [1] 24.112935 7.700000 1.953665

The basic story is that simple strategies often solve the problem, and that you should be cognizant of the absolute and relative magnitudes involved in your calculations.

One rule of thumb is to try to work with numbers whose magnitude is around 1. We can often scale the values in our problem in order to do this. I.e., change the units of your variables. Instead of personal income in dollars, use personal income in thousands or hundreds of thousands of dollars.

## **4 Matrix factorizations (decompositions) and solving systems of linear equations**

Suppose we want to solve the following linear system:


15

Numerically, this is never done by finding the inverse and multiplying. Rather we solve the system using a matrix decomposition (or equivalent set of steps). One approach uses Gaussian elimination (equivalent to the LU decomposition), while another uses the Cholesky decomposition. There are also iterative methods that generate a sequence of approximations to the solution but reduce computation (provided they are stopped before the exact solution is found).

Gentle-CS has a nice table overviewing the various factorizations (Table 5.1, page 219). I’ve reproduced a variation on it here (sorry about the weird lines – L<sup>A</sup> TEX is being a pain for some reason).

_Table 1. Useful matrix factorizations for statistics._

|Name|Representation|Restrictions|Properties|Uses|
|---|---|---|---|---|
|LU|_Ann_ =_LnnUnn_|_A_generally<br>square|_L_upper triangular;_U_<br>lower triangular|solving equations;<br>inversion|
|QR|_Anm_ =_QnnRnm_||_Q_orthogonal;_R_upper<br>triangular|regression|
|Cholesky|_Ann_ =_U _<sup>_⊤_</sup><br>_nn_<sup>_Unn_</sup>|_A_positive<br>(semi-) definite|_U_ upper triangular|multivariate normal;<br>covariance; solving<br>equations; inversion|
|Eigen de-<br>composition|_Ann_ = Γ_nn_Λ_nn_Γ<sup>_⊤_</sup><br>_nn_|_A_square,<br>symmetric*|Γorthogonal;Λ<br>(non-negative) diagonal|principal components<br>analysis and related|
|SVD|_Anm_ =_UnnDnmV _<sup>_⊤_</sup><br>_mm_<sup>or</sup><br>_Anm_ =_UnkDkkV _<sup>_⊤_</sup><br>_mk_||_U, V_ orthogonal;_D_<br>(non-negative) diagonal|machine learning, topic<br>models|


*For the eigen decomposition, I assume _A_ is symmetric, though there is a decomposition for non-symmetric _A_ .

### **4.1 Triangular systems**

As a preface, let’s figure out how to solve _Ax_ = _b_ if _A_ is upper triangular. The basic algorithm proceeds from the bottom up (and therefore is called a ’backsolve’. We solve for _xn_ trivially, and then move upwards plugging in the known values of _x_ and solving for the remaining unknown in each row (each equation).


_bk−_<sup><u>�</u></sup><sup>_n_</sup> _<u>j</u>_ = _k_ <u>+1</u><sup>_xjAkj_</sup> 2. Now for _k < n_ , use the already computed _{xn, xn−_ 1 _, . . . , xk_ +1 _}_ to calculate _xk_ = _Akk_

3. Repeat for all rows.

How many multiplies and adds are done? Solving lower triangular systems is very similar and involves the same number of calculations.

In R, _backsolve()_ solves upper triangular systems and _forwardsolve()_ solves lower triangular systems:

16

n <- 20 X <- **crossprod** ( **matrix** ( **rnorm** (n^2), n)) b <- **rnorm** (n) U <- **chol** ( **crossprod** (X)) _# U is upper-triangular_ L <- **t** (U) _# L is lower-triangular_ out1 <- **backsolve** (U, b) out2 <- **forwardsolve** (L, b) **all.equal** (out1, **c** ( **solve** (U) %*% b)) ## [1] TRUE **all.equal** (out2, **c** ( **solve** (L) %*% b)) ## [1] TRUE

We can also solve ( _U_<sup>_⊤_</sup> )<sup>_−_1</sup> _b_ and ( _L_<sup>_⊤_</sup> )<sup>_−_1</sup> _b_ as **backsolve** (U, b, transpose = TRUE) **forwardsolve** (L, b, transpose = TRUE)

**To reiterate the distinction between matrix inversion and solving a system of equations, when we write** _U_<sup>_−_1</sup> _b_ **, what we mean on a computer is to carry out the above algorithm, not to find the inverse and then multiply.**

Here’s a good reason why.

n <- 5000 X <- **crossprod** ( **matrix** ( **rnorm** (n^2), n)) b <- **rnorm** (n) U <- **chol** ( **crossprod** (X)) _# U is upper-triangular_

**system.time** ( out1 <- **backsolve** (U, b) ) ## user system elapsed ## 0.02 0.00 0.02 **system.time** (

17

out2 <- **solve** (U) %*% b ) ## user system elapsed ## 13.036 0.148 13.189

That assumes you have _U_ , but we’ll see in a bit that even when one accounts for the creation of _U_ , you don’t want to invert matrices in order to solve systems of equations.

### **4.2 Gaussian elimination (LU decomposition)**

Gaussian elimination is a standard way of directly computing a solution for _Ax_ = _b_ . It is equivalent to the LU decomposition. LU is primarily done with square matrices, but not always. Also LU decompositions do exist for some singular matrices.

The idea of Gaussian elimination is to convert the problem to a triangular system. In class, we’ll walk through Gaussian elimination in detail and see how it relates to the LU decomposition. I’ll describe it more briefly here. Following what we learned in algebra when we have multiple equations, we preserve the solution, _x_ , when we add multiples of rows (i.e., add multiples of equations) together. This amounts to doing _L_ 1 _Ax_ = _L_ 1 _b_ for a lower-triangular matrix _L_ 1 that produces all zeroes in the first column of _L_ 1 _A_ except for the first row. We proceed to zero out values below the diagonal for the other columns of _A_ . The result is _Ln−_ 1 _· · · L_ 1 _Ax ≡ Ux_ = _Ln−_ 1 _· · · L_ 1 _b ≡ b_<sup>_∗_</sup> where _U_ is upper triangular. This is the forward reduction step of Gaussian elimination. Then the backward elimination step solves _Ux_ = _b_<sup>_∗_</sup> .

If we’re just looking for the solution of the system, we don’t need the lower-triangular factor _L_ = ( _Ln−_ 1 _· · · L_ 1)<sup>_−_1</sup> in _A_ = _LU_ , but it turns out to have a simple form that is computed as we go along, it is unit lower triangular and the values below the diagonal are the negative of the values below the diagonals in _L_ 1 _, . . . , Ln−_ 1 (note that each _Lj_ has non-zeroes below the diagonal only in the _j_ th column). As a side note related to storage, it turns out that as we proceed, we can store the elements of _L_ and _U_ in the original _A_ matrix, except for the implicit 1s on the diagonal of _L_ .

In class, we’ll work out the computational complexity of the LU and see that it is _O_ ( _n_<sup>3</sup> ).

If we look at _solve.default()_ in R, we see that it uses _dgesv_ . A Google search indicates that this is a Lapack routine that does the LU decomposition with partial pivoting and row interchanges (see below on what these are), so R is using the algorithm we’ve just discussed.

One additional complexity is that we want to avoid dividing by very small values to avoid introducing numerical inaccuracy (we would get large values that might overwhelm whatever they are being added to, and small errors in the divisor will have large effects on the result). This can be done on the fly by interchanging equations to use the equation (row) that produces the largest

18

value to divide by. For example in the first step, we would switch the first equation (first row) for whichever of the remaining equations has the largest value in the first column. This is called partial pivoting. The divisors are called pivots. Complete pivoting also considers interchanging columns, and while theoretically better, partial pivoting is generally sufficient and requires fewer computations. Partial pivoting can be expressed as multiplying along the way by permutation matrices, _P_ 1 _, . . . Pn−_ 1 that switch rows. One can show with some work that based on pivoting, we have _PA_ = _LU_ , where _P_ = _Pn−_ 1 _· · · P_ 1. In the demo code, we’ll see a toy example of the impact of pivoting.

Finally _|PA|_ = _|P ||A|_ = _|L||U |_ = _|U |_ (why?) so _|A|_ = _|U |/|P |_ and since the determinant of each permutation matrix, _Pj_ is -1 (except when _Pj_ = _I_ because we don’t need to switch rows), we just need to multiply by minus one if there is an odd number of permutations. Or if we know the matrix is non-negative definite, we just take the absolute value of _|U |_ . So Gaussian elimination provides a fast stable way to find the determinant.

### **4.3 Cholesky decomposition**

When _A_ is p.d., we can use the Cholesky decomposition to solve a system of equations. Positive definite matrices can be decomposed as _U_<sup>_⊤_</sup> _U_ = _A_ where _U_ is upper triangular. _U_ is called a square root matrix and is unique (apart from the sign, which we fix by requiring the diagonals to be positive). One algorithm for computing _U_ is:


We can then solve a system of equations as: _U_<sup>_−_1</sup> ( _U_<sup>_⊤−_1</sup> _b_ ), which in R can be done in either of the following ways:

**backsolve** (U, **backsolve** (U, b, transpose = TRUE)) **backsolve** (U, **forwardsolve** ( **t** (U), b)) _# equivalent but less efficient_

The Cholesky has some nice advantages over the LU: (1) while both are _O_ ( _n_<sup>3</sup> ), the Cholesky involves only half as many computations, _n_<sup>3</sup> _/_ 6 + _O_ ( _n_<sup>2</sup> ) and (2) the Cholesky factorization has only ( _n_<sup>2</sup> + _n_ ) _/_ 2 unique values compared to _n_<sup>2</sup> + _n_ for the LU. Of course the LU is more broadly

19

applicable. The Cholesky does require computation of square roots, but it turns out this is not too intensive. There is also a method for finding the Cholesky without square roots.

**Uses of the Cholesky** The standard algorithm for generating _y ∼N_ (0 _, A_ ) is:

U <- **chol** (A)

y <- **crossprod** (U, **rnorm** (n)) _# i.e., t(U)%*%rnorm(n), but much faster_

**Question** : where will most of the time in this two-step calculation be spent?

If a regression design matrix, _X_ , is full rank, then _X_<sup>_⊤_</sup> _X_ is positive definite, so we could find _β_ ˆ = ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ using either the Cholesky or Gaussian elimination. **Challenge** : write efficient R code to carry out the OLS solution using either LU or Cholesky factorization.

However, it turns out that the standard approach is to work with _X_ using the QR decomposition rather than working with _X_<sup>_⊤_</sup> _X_ ; working with _X_ is more numerically stable, though in most situations without extreme collinearity, either of the approaches will be fine.

#### **Numerical issues with eigendecompositions and Cholesky decompositions for positive definite**

**matrices** Monahan comments that in general Gaussian elimination and the Cholesky decomposition are very stable. However, in the Cholesky case, if the matrix is very ill-conditioned we can get _Aii −_<sup>�</sup> _k_<sup>_U_</sup> _ki_<sup>2being negative and then the algorithm stops when we try to take the square root. In</sup> this case, the Cholesky decomposition does not exist numerically although it exists mathematically. It’s not all that hard to produce such a matrix, particularly when working with high-dimensional covariance matrices with large correlations.

_# require(fields)_ locs <- **runif** (100) rho <- .1 C <- **exp** (- **rdist** (locs)^2/rho^2) e <- **eigen** (C) e$values[96:100]

## [1] -5.664370e-16 -7.246818e-16 -8.520257e-16 -1.121117e-15 -2.208819e-15 U <- **chol** (C)

**## Error in chol.default(C): the leading minor of order 36 is not positive definite**

20

vals <- **abs** (e$values) **max** (vals)/ **min** (vals)

## [1] 6.303212e+19 U <- **chol** (C, pivot = TRUE)

## Warning in chol.default(C, pivot = TRUE): the matrix is either rank-deficient or indefinite

We can think about the accuracy here as follows. Suppose we have a matrix whose diagonal elements (i.e., the variances) are order of magnitude 1 and that the true value of a _Uii_ is less than 1 _×_ 10<sup>_−_16</sup> . From the given _Aii_ we are subtracting<sup>�</sup> _k_<sup>_U_</sup> _ki_<sup>2andtryingtocalculatethisverysmall</sup> number but we know that we can only represent the values _Aii_ and<sup>�</sup> _k_<sup>_U_</sup> _ki_<sup>2accurately to 16 places,</sup> so the difference is garbage starting in the 17th position and could well be negative. Now realize that<sup>�</sup> _k_<sup>_U_</sup> _ki_<sup>2is the result of a potentially large set of arithmetic operations, and is likely represented</sup> accurately to fewer than 16 places. Now if the true value of _Uii_ is smaller than the accuracy to which<sup>�</sup> _k_<sup>_U_2</sup> _ki_<sup>is represented, we can get a difference that is negative.</sup>

Note that when the Cholesky fails, we can still compute an eigendecomposition, but we have negative numeric eigenvalues. Even if all the eigenvalues are numerically positive (or equivalently, we’re able to get the Cholesky), errors in small eigenvalues near machine precision could have large effects when we work with the inverse of the matrix. This is what happens when we have columns of the _X_ matrix nearly collinear. We cannot statistically distinguish the effect of two (or more) covariates, and this plays out numerically in terms of unstable results.

A strategy when working with mathematically but not numerically positive definite _A_ is to set eigenvalues or singular values to zero when they get very small, which amounts to using a pseudoinverse and setting to zero any linear combinations with very small variance. We can also use pivoting with the Cholesky and accumulate zeroes in the last _n − q_ rows (for cases where we try to take the square root of a negative number), corresponding to the columns of _A_ that are numerically linearly dependent. See the _pivot_ argument to R’s _chol()_ .

### **4.4 QR decomposition**

#### **4.4.1 Introduction**

The QR decomposition is available for any matrix, _X_ = _QR_ , with _Q_ orthogonal and _R_ upper triangular. If _X_ is non-square, _n × p_ with _n > p_ then the leading _p_ rows of _R_ provide an upper triangular matrix ( _R_ 1) and the remaining rows are 0. (I’m using _p_ because the QR is generally

21

applied to design matrices in regression). In this case we really only need the first _p_ columns of _Q_ , and we have _X_ = _Q_ 1 _R_ 1, the ’skinny’ QR (this is what R’s QR provides). For uniqueness, we can require the diagonals of _R_ to be nonnegative, and then _R_ will be the same as the upper-triangular Cholesky factor of _X_<sup>_⊤_</sup> _X_ :


There are three standard approaches for computing the QR, using (1) reflections (Householder transformations), (2) rotations (Givens transformations), or (3) Gram-Schmidt orthogonalization (see below for details).

For _n×n X_ , the QR (for the Householder approach) requires 2 _n_<sup>3</sup> _/_ 3 flops, so QR is less efficient than LU or Cholesky.

We can also obtain the pseudo-inverse of _X_ from the QR: _X_<sup>+</sup> = [ _R_ 1<sup>_−_10]</sup><sup>_Q⊤_.In the case that</sup> _X_ is not full-rank, there is a version of the QR that will work (involving pivoting) and we end up with some additional zeroes on the diagonal of _R_ 1.

#### **4.4.2 Regression and the QR**

Often QR is used to fit linear models, including in R. Consider the linear model in the form _Y_ = _Xβ_ + _ϵ_ , finding _β_<sup>ˆ</sup> = ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ . Let’s consider the skinny QR and note that _R_<sup>_⊤_</sup> is invertible. Therefore, we can express the normal equations as


and solving for _β_ is just a backsolve since _R_ is upper-triangular. Furthermore the standard regression quantities, such as the hat matrix, the SSE, the residuals, etc. can be easily expressed in terms of _Q_ and _R_ .

Why use the QR instead of the Cholesky on _X_<sup>_⊤_</sup> _X_ ? The condition number of _X_ is the square root of that of _X_<sup>_⊤_</sup> _X_ , and the _QR_ factorizes _X_ . Monahan has a discussion of the condition of the regression problem, but from a larger perspective, the situations where numerical accuracy is a concern are generally cases where the OLS estimators are not particularly helpful anyway (e.g., highly collinear predictors).

What about computational order of the different approaches to least squares? The Cholesky is _np_<sup>2</sup> + 3<sup><u>1</u></sup><sup>_p_3, an algorithm called sweeping is</sup><sup>_np_2+</sup><sup>_p_3 , the Householder method for QR is 2</sup><sup>_np_2</sup><sup>_−_</sup><sup><u>2</u></sup> 3<sup>_p_3,</sup>

22

and the modified Gram-Schmidt approach for QR is 2 _np_<sup>2</sup> . So if _n ≫ p_ then Cholesky (and sweeping) are faster than the QR approaches. According to Monahan, modified Gram-Schmidt is most numerically stable and sweeping least. In general, regression is pretty quick unless _p_ is large since it is linear in _n_ , so it may not be worth worrying too much about computational differences of the sort noted here.

#### **4.4.3 Regression and the QR in R**

Regression in R uses the QR decomposition via _qr()_ , which calls a Fortran function. _qr()_ (and the Fortran functions that are called) is specifically designed to output quantities useful in fitting linear models. Note that by default you get the skinny QR, namely only the first _p_ rows of _R_ and the first _p_ columns of _Q_ , where the latter form an orthonormal basis for the column space of _X_ . The remaining columns form an orthonormal basis for the null space of _X_ (the space orthogonal to the column space of _X_ ). The analogy in regression is that we get the basis vectors for the regression, while adding the remaining columns gives us the full _n_ -dimensional space of the observations.

_qr()_ returns the result as a list meant for use by other tools. R stores the _R_ matrix in the upper triangle of _$qr_ , while the lower triangle of _$qr_ and _$aux_ store the information for constructing _Q_ (this relates to the Householder-related vectors _u_ below). One can multiply by _Q_ using _qr.qy()_ and by _Q_<sup>_⊤_</sup> using _qr.qty()_ . If you want to extract _R_ and _Q_ , the following will work:

X.qr = **qr** (X) Q = **qr.Q** (X.qr) R = **qr.R** (X.qr)

As a side note, there are QR-based functions that provide regression-related quantities, such as _qr.resid()_ , _qr.fitted()_ and _qr.coef()_ . These functions (and their Fortran counterparts) exist because one can work through the various regression quantities of interest and find their expressions in terms of _Q_ and _R_ , with nice properties resulting from _Q_ being orthogonal and _R_ triangular.

#### **4.4.4 Computing the QR decomposition**

We’ll work through some of the details of the different approaches to the QR, in part because they involve some concepts that may be useful in other contexts.

One approach involves reflections of vectors and a second rotations of vectors. Reflections and rotations are transformations that are performed by orthogonal matrices. The determinant of a reflection matrix is -1 and the determinant of a rotation matrix is 1. We’ll see some of the details in the demo code.

23

**Reflections** If _u_ and _v_ are orthonormal vectors and _x_ is in the space spanned by _u_ and _v_ , _x_ = _c_ 1 _u_ + _c_ 2 _v_ , then _x_ ˜ = _−c_ 1 _u_ + _c_ 2 _v_ is a reflection (a _Householder_ reflection) along the _u_ dimension (since we are using the negative of that basis vector). We can think of this as reflecting across the plane perpendicular to _u_ . This extends simply to higher dimensions with orthonormal vectors, _u, v_ 1 _, v_ 2 _, . . ._

Suppose we want to formulate the reflection in terms of a “Householder” matrix, _Q_ . It turns out that


if _Q_ = _I −_ 2 _uu_<sup>_⊤_</sup> . _Q_ has the following properties: (1) _Qu_ = _−u_ , (2) _Qv_ = _v_ for _u_<sup>_⊤_</sup> _v_ = 0, (3) _Q_ is orthogonal and symmetric.

One way to create the QR decomposition is by a series of Householder transformations that create an upper triangular _R_ from _X_ :


where we make use of the symmetry in defining _Q_ .

Basically _Q_ 1 reflects the first column of _X_ with respect to a carefully chosen _u_ , so that the result is all zeroes except for the first element. We want _Q_ 1 _x_ = _x_ ˜ = ( _||x||,_ 0 _, . . . ,_ 0). This can be achieved with _u_ = _||xx−−xx_ ˜˜ _||_<sup>.Then</sup><sup>_Q_2 makes the last</sup><sup>_n −_2 rows of the second column equal to zero.</sup> We’ll work through this a bit in class.

In the regression context, as we work through the individual transformations, _Qj_ = _I −_ 2 _uju_<sup>_⊤_</sup> _j_<sup>,</sup> we apply them to _X_ and _Y_ to create _R_ (note this would not involve doing the full matrix multiplication - think about what calculations are actually needed) and _QY_ = _Q_<sup>_⊤_</sup> _Y_ , and then solve _Rβ_ = _Q_<sup>_⊤_</sup> _Y_ . To find Cov( _β_<sup>ˆ</sup> ) _∝_ ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> = ( _R_<sup>_⊤_</sup> _R_ )<sup>_−_1</sup> = _R_<sup>_−_1</sup> _R_<sup>_−⊤_</sup> we do need to invert _R_ , but it’s upper-triangular and of dimension _p × p_ . It turns out that _Q_<sup>_⊤_</sup> _Y_ can be partitioned into the first _p_ and the last _n − p_ elements, _z_<sup>(1)</sup> and _z_<sup>(2)</sup> . The SSR is _∥z_<sup>(1)</sup> _∥_<sup>2</sup> and SSE is _∥z_<sup>(2)</sup> _∥_<sup>2</sup> .

Final side note: if _X_ is square (so _n_ = _p_ ) you might wonder why we need _Qp_ since after _p −_ 1 reflections, we don’t need to zero anything else out (since the last column of _R_ has _n_ non-zero elements). It turns out that if we go back to thinking about a Householder reflection in general, there is a lack of uniqueness in choosing _x_ ˜. It could either be ( _||x||,_ 0 _, . . . ,_ 0) or ( _−||x||,_ 0 _, . . . ,_ 0). For better numerical stability, one chooses from the two of those such that _x_ 1 is of the opposite sign to _x_ ˜1, so that one avoids cancellation of numbers that may be of the same magnitude when doing _x − x_ ˜. The transformation _Qp_ is the last step of taking that approach of choosing the sign at each step. _Qp_ doesn’t zero anything out; it just basically just involves potentially setting _Rpp_ to be _−Rpp_ . (To be honest, I’m not clear on why one would bother to do that last step, but that seems to

24

be how it is presented in discussions of the Householder approach.) Of course in the case of _p < n_ , we definitely need _Qp_ so that the last _n − p_ rows of _R_ are zero and we can then discard them when just using the skinny QR.

**Rotations** A _Givens_ rotation matrix rotates a vector in a two-dimensional subspace to be axis oriented with respect to one of the two dimensions by changing the value of the other dimension. E.g. we can create _x_ ˜ = ( _x_ 1 _, . . . ,_ ˜ _xp, . . . ,_ 0 _, . . . xn_ ) from _x_ = ( _x_ 1 _, . . . , xp, . . . , xq, . . . , xn_ ) using a matrix multiplication: _x_ ˜ = _Qx_ . _Q_ is orthogonal but not symmetric.

We can use a series of Givens rotations to do the QR but unless it is done carefully, more computations are needed than with Householder reflections. The basic story is that we apply a series of Givens rotations to _X_ such that we zero out the lower triangular elements.


Note that we create the _n − p_ zero rows in _R_ (because the calculations affect the upper triangle of _R_ ), but we can then ignore those rows and the corresponding columns of _Q_ .

**Gram-Schmidt Orthogonalization** Gram-Schmidt involves finding a set of orthonormal vectors to span the same space as a set of LIN vectors, _x_ 1 _, . . . , xp_ . If we take the LIN vectors to be the columns of _X_ , so that we are discussing the column space of _X_ , then G-S yields the QR decomposition. Here’s the algorithm:


2. Orthogonalize the remaining vectors with respect to _x_ ˜1:

   - _x_ 2 _−x_ ˜<sup>_⊤_</sup> <u>1</u><sup>_x_2</sup><sup>_x_˜1</sup>

   - (a) _x_ ˜2 = _∥x_ 2 _−x_ ˜<sup>_⊤_</sup> 1<sup>_x_2</sup><sup>_x_˜1</sup><sup>_∥_,which orthogonalizes with respect to</sup><sup>_x_˜1and normalizes.Note that</sup>

   - _x_ ˜<sup>_⊤_</sup> 1<sup>_x_2</sup><sup>_x_˜1=</sup><sup>_⟨x_˜1</sup><sup>_, x_2</sup><sup>_⟩x_˜1.So we are finding a scaling,</sup><sup>_cx_˜1, where</sup><sup>_c_is based on the inner</sup> product, to remove the variation in the _x_ 1 direction from _x_ 2.

   - (b) For _k >_ 2, find interim vectors, _x_<sup>(2)</sup> _k_<sup>, by orthogonalizing with respect to</sup><sup>_x_˜1</sup>

3. Proceed for _k_ = 3 _, . . ._ , in turn orthogonalizing and normalizing the first of the remaining vectors w.r.t. _x_ ˜ _k−_ 1 and orthogonalizing the remaining vectors w.r.t. _x_ ˜ _k−_ 1 to get new interim vectors

Mathematically, we could instead orthogonalize _x_ 2 w.r.t. _x_ ˜1, then orthogonalize _x_ 3 w.r.t. _{x_ ˜1 _,_ ˜ _x_ 2 _}_ , etc. The algorithm above is the _modified_ G-S, and is known to be more numerically stable if the

25

columns of _X_ are close to collinear, giving vectors that are closer to orthogonal. The resulting _x_ ˜ vectors are the columns of _Q_ . The elements of _R_ are obtained as we proceed: the diagonal values are the the normalization values in the denominators, while the off-diagonals are the inner products with the already-computed columns of _Q_ that are computed as part of the numerators.

Another way to think about this is that _R_ = _Q_<sup>_⊤_</sup> _X_ , which is the same as regressing the columns of _X_ on _Q,_ since ( _Q_<sup>_⊤_</sup> _Q_ )<sup>_−_1</sup> _Q_<sup>_⊤_</sup> _X_ = _Q_<sup>_⊤_</sup> _X_ . By construction, the first column of _X_ is a scaling of the first column of _Q_ , the second column of _X_ is a linear combination of the first two columns of _Q_ , etc., so _R_ being upper triangular makes sense.

#### **4.4.5 The “tall-skinny” QR**

Suppose you have a very large regression problem, with _n_ very large, and _n ≫ p_ . There is a variant of the QR, called the tall-skinny QR (see http://arxiv.org/pdf/0808.2664v1.pdf for details) that allows us to find the decomposition in a parallel fashion. The basic idea is to do a nested set of QR decompositions on blocks of rows of _X_ :


followed by ’reduction’ steps (this can be done in a map-reduce context) that do the _QR_ of pairs of the _R_ factors:


and


The full decomposition is then


26

The computation can be done in parallel (in particular it can be done with map-reduce) and the _Q_ matrix for big problems would generally not be computed explicitly but would be stored in its constituent pieces.

Alternatively, there is a variant on the algorithm that processes the row-blocks of _X_ serially, allowing you to do QR on a large tall-skinny matrix that you can’t fit in memory (or possibly even on disk). First you do _QR_ on _X_ 0 to get _Q_ 0 _R_ 0. Then you stack _R_ 0 on top of _X_ 1 and do QR to get _R_ 01. Then stack _R_ 01 on top of _X_ 2 to get _R_ 012, etc.

### **4.5 Determinants**

The absolute value of the determinant of a square matrix can be found from the product of the diagonals of the triangular matrix in any factorization that gives a triangular (including diagonal) matrix times an orthogonal matrix (or matrices) since the determinant of an orthogonal matrix is either one or minus one.

_|A|_ = _|QR|_ = _|Q||R|_ = _±|R|_

_|A_<sup>_⊤_</sup> _A|_ = _|_ ( _QR_ )<sup>_⊤_</sup> _QR|_ = _|R_<sup>_⊤_</sup> _R|_ = _|R_ 1<sup>_⊤R_1</sup><sup>_|_=</sup><sup>_|R_1</sup><sup>_|_2</sup>

In R, the following will do it (on the log scale), since _R_ is stored in the upper triangle of the _$qr_ element.

myqr = **qr** (A) magn = **sum** ( **log** ( **abs** ( **diag** (myqr$qr))))

An alternative is the product of the diagonal elements of _D_ (the singular values) in the SVD factorization, _A_ = _UDV_<sup>_⊤_</sup> .

For non-negative definite matrices, we know the determinant is non-negative, so the uncertainty about the sign is not an issue. For positive definite matrices, a good approach is to use the product of the diagonal elements of the Cholesky decomposition.

One can also use the product of the eigenvalues: _|A|_ = _|_ ΓΛΓ<sup>_−_1</sup> _|_ = _|_ Γ _||_ Γ<sup>_−_1</sup> _||_ Λ _|_ = _|_ Λ _|_

**Computation** Computing from any of these diagonal or triangular matrices as the product of the diagonals is prone to overflow and underflow, so we **always** work on the log scale as the sum of the log of the values. When some of these may be negative, we can always keep track of the number of negative values and take the log of the absolute values.

Often we will have the factorization as a result of other parts of the computation, so we get the determinant for free.

R’s _determinant()_ uses the LU decomposition. Supposedly _det()_ just wraps _determinant()_ , but I can’t seem to pass the _logarithm_ argument into _det()_ , so _determinant()_ seems more useful.

27

## **5 Eigendecomposition and SVD**

### **5.1 Eigendecomposition**

The eigendecomposition (spectral decomposition) is useful in considering convergence of algorithms and of course for statistical decompositions such as PCA. We think of decomposing the components of variation into orthogonal patterns (the eigenvectors) with variances (eigenvalues) associated with each pattern.

Square symmetric matrices have real eigenvectors and eigenvalues, with the factorization into orthogonal Γ and diagonal Λ, _A_ = ΓΛΓ<sup>_⊤_</sup> , where the eigenvalues on the diagonal of Λ are ordered in decreasing value. Of course this is equivalent to the definition of an eigenvalue/eigenvector pair as a pair such that _Ax_ = _λx_ where _x_ is the eigenvector and _λ_ is a scalar, the eigenvalue. The inverse of the eigendecomposition is simply ΓΛ<sup>_−_1</sup> Γ<sup>_⊤_</sup> . On a similar note, we can create a square root matrix, ΓΛ<sup>1</sup><sup>_/_2</sup> , by taking the square roots of the eigenvalues.

The spectral radius of _A_ , denoted _ρ_ ( _A_ ), is the maximum of the absolute values of the eigenvalues. As we saw when talking about ill-conditionedness, for symmetric matrices, this maximum is the induced norm, so we have _ρ_ ( _A_ ) = _∥A∥_ 2. It turns out that _ρ_ ( _A_ ) _≤∥A∥_ for any induced matrix norm. The spectral radius comes up in determining the rate of convergence of some iterative algorithms.

**Computation** There are several methods for eigenvalues; a common one for doing the full eigendecomposition is the _QR algorithm_ . The first step is to reduce _A_ to upper Hessenburg form, which is an upper triangular matrix except that the first subdiagonal in the lower triangular part can be non-zero. For symmetric matrices, the result is actually tridiagonal. We can do the reduction using Householder reflections or Givens rotations. At this point the QR decomposition (using Givens rotations) is applied iteratively (to a version of the matrix in which the diagonals are shifted), and the result converges to a diagonal matrix, which provides the eigenvalues. It’s more work to get the eigenvectors, but they are obtained as a product of Householder matrices (required for the initial reduction) multiplied by the product of the _Q_ matrices from the successive QR decompositions.

We won’t go into the algorithm in detail, but note that it involves manipulations and ideas we’ve seen already.

If only the largest (or the first few largest) eigenvalues and their eigenvectors are needed, which can come up in time series and Markov chain contexts, the problem is easier and can be solved by the _power method_ . E.g., in a Markov chain context, steady state is reached through _xt_ = _A_<sup>_t_</sup> _x_ 0. One can find the largest eigenvector by multiplying by _A_ many times, normalizing at each step. _v_<sup>(</sup><sup>_k_)</sup> = _Az_<sup>(</sup><sup>_k−_1)</sup> and _z_<sup>(</sup><sup>_k_)</sup> = _v_<sup>(</sup><sup>_k_)</sup> _/∥v_<sup>(</sup><sup>_k_)</sup> _∥_ . There is an extension to find the _p_ largest eigenvalues and their vectors. See the demo code for an implementation.

28

### **5.2 Singular value decomposition**

Let’s consider an _n × m_ matrix, _A_ , with _n ≥ m_ (if _m > n_ , we can always work with _A_<sup>_⊤_</sup> ). This often is a matrix representing _m_ features of _n_ observations. We could have _n_ documents and _m_ words, or _n_ gene expression levels and _m_ experimental conditions, etc. _A_ can always be decomposed as


where _U_ and _V_ are matrices with orthonormal columns (left and right eigenvectors) and _D_ is diagonal with non-negative values (which correspond to eigenvalues in the case of square _A_ and to squared eigenvalues of _A_<sup>_⊤_</sup> _A_ ).

The SVD can be represented in more than one way. One representation is


where _uj_ and _vj_ are the columns of _U_ and _V_ and where _k_ is the rank of _A_ (which is at most the minimum of _n_ and _m_ of course). The diagonal elements of _D_ are the singular values.

If _A_ is positive semi-definite, the eigendecomposition is an SVD. Furthermore, _A_<sup>_⊤_</sup> _A_ = _V D_<sup>2</sup> _V_<sup>_⊤_</sup> and _AA_<sup>_⊤_</sup> = _UD_<sup>2</sup> _U_<sup>_⊤_</sup> , so we can find the eigendecomposition of such matrices using the SVD of _A_ (for _AA_<sup>_⊤_</sup> we need to fill out _U_ to have _n_ columns). Note that the squares of the singular values of _A_ are the eigenvalues of _A_<sup>_⊤_</sup> _A_ and _AA_<sup>_⊤_</sup> .

We can also fill out the matrices to get


where the added rows and columns of _D_ are zero with the upper left block the _Dk×k_ from above.

**Uses** The SVD is an excellent way to determine a matrix rank and to construct a pseudo-inverse ( _A_<sup>+</sup> = _V D_<sup>+</sup> _U_<sup>_⊤_</sup> ).

We can use the SVD to approximate _A_ by taking _A ≈ A_<sup>˜</sup> =<sup>�</sup><sup>_p_</sup> _j_ =1<sup>_Djjujv_</sup> _j_<sup>_⊤_for</sup><sup>_p<m_.This</sup> approximation holds in terms of the Frobenius norm for _A − A_<sup>˜</sup> . As an example if we have a large image of dimension _n × m_ , we could hold a compressed version by a rank- _p_ approximation using the SVD. The SVD is used a lot in clustering problems. For example, the Netflix prize was won based on a variant of SVD (in fact all of the top methods used variants on SVD, I believe).

**Computation** The basic algorithm (Golub-Reinsch) is similar to the QR method for the eigendecomposition. We use a series of Householder transformations on the left and right to reduce _A_

29

to an upper bidiagonal matrix, _A_<sup>(0)</sup> . The post-multiplications (the transformations on the right) generate the zeros in the upper triangle. (An upper bidiagonal matrix is one with non-zeroes only on the diagonal and first subdiagonal above the diagonal). Then the algorithm produces a series of upper bidiagonal matrices, _A_<sup>(0)</sup> , _A_<sup>(1)</sup> _,_ etc. that converge to a diagonal matrix, _D_ . Each step is carried out by a sequence of Givens transformations:


This eventually gives _A_<sup>(</sup><sup>_..._)</sup> = _D_ and by construction, _U_ (the product of the pre-multiplied Householder matrices and the _R_ matrices) and _V_ (the product of the post-multiplied Householder matrices and the _T_ matrices) are orthogonal. The result is then transformed by a diagonal matrix to make the elements of _D_ non-negative and by permutation matrices to order the elements of _D_ in nonincreasing order.

**Computation for large tall-skinny matrices** The SVD can also be generated from a QR decomposition. Take _X_ = _QR_ and then do an SVD on the _R_ matrix to get _X_ = _QUDV_<sup>_⊤_</sup> = _U_<sup>_∗_</sup> _DV_<sup>_⊤_</sup> . This is particularly helpful for the case when _X_ is tall and skinny (suppose _X_ is _n×p_ with _n ≫ p_ ), because we can do the tall-skinny QR, and the resulting SVD on _R_ is easy computationally if _p_ is manageable.

## **6 Computation**

### **6.1 Linear algebra in R**

Speedups and storage savings can be obtained by working with matrices stored in special formats when the matrices have special structure. E.g., we might store a symmetric matrix as a full matrix but only use the upper or lower triangle. Banded matrices and block diagonal matrices are other common formats. Banded matrices are all zero except for _Ai,i_ + _ck_ for some small number of integers, _ck_ . Viewed as an image, these have bands. The bands are known as co-diagonals.

Note that for many matrix decompositions, you can change whether all of the aspects of the decomposition are returned, or just some, which may speed calculations.

Some useful packages in R for matrices are _Matrix_ , _spam_ , and _bdsmatrix_ . _Matrix_ can represent a variety of rectangular matrices, including triangular, orthogonal, diagonal, etc. and provides methods for various matrix calculations that are specific to the matrix type. _spam_ handles general sparse matrices with fast matrix calculations, in particular a fast Cholesky decomposition.

30

_bdsmatrix_ focuses on block-diagonal matrices, which arise frequently in contexts where there is clustering that induces within-cluster correlation and cross-cluster independence.

In general, matrix operations in R go to compiled C or Fortran code without much intermediate R code, so they can actually be pretty efficient and are based on the best algorithms developed by numerical experts. The core libraries that are used are LAPACK and BLAS (the Linear Algebra PACKage and the Basic Linear Algebra Subroutines). As we’ve discussed in the parallelization unit, one way to speed up code that relies heavily on linear algebra is to make sure you have a BLAS library tuned to your machine. These include OpenBLAS (free; formerly called GotoBLAS), Intel’s MKL, AMD’s ACML, and Apple’s vecLib. These can be installed and R can be linked to the shared object library file ( _.so_ file or _.dylib_ on a Mac) for the fast BLAS. These BLAS libraries are also available in threaded versions that farm out the calculations across multiple cores or processors that share memory.

BLAS routines do vector operations (level 1), matrix-vector operations (level 2), and dense matrix-matrix operations (level 3). Often the name of the routine has as its first letter “d”, “s”, “c” to indicate the routine is double precision, single precision, or complex. LAPACK builds on BLAS to implement standard linear algebra routines such as eigendecomposition, solutions of linear systems, a variety of factorizations, etc.

### **6.2 Sparse matrices**

As an example of exploiting sparsity, here’s how the _spam_ package in R stores a sparse matrix. Consider the matrix to be row-major and store the non-zero elements in order in a vector called _value_ . Then create a vector called _rowptr_ that stores the position of the first element of each row. Finally, have a vector, _colindices_ that tells the column identity of each element. Here’s an example in the spam package in R:

**require** (spam) mat = **matrix** ( **c** (0,0,1,0,10,0,0,0,100,0, **rep** (0,5),1000, **rep** (0,4)), nrow mat = **as.spam** (mat) mat@entries ## [1] 1 10 100 1000 mat@rowpointers ## [1] 1 3 4 4 5 mat@colindices ## [1] 3 5 4 1

= 4, byrow

31

We can do a fast matrix multiply, _Ab_ , as follows in pseudo-code:

f o r ( i in 1: nrows (A) ) { x [ i ] = 0

---

[Up: contents](index.md) · [Unit 09 — linalg Part 02 — →](02-unit-09-linalg-part-02.md)
