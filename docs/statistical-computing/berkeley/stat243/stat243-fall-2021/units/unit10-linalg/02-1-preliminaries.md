---
title: 1 Preliminaries
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit10-linalg.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Preliminaries

**Source:** [`units/unit10-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **1.1 Context**

Many statistical and machine learning methods involve linear algebra of some sort - at the very least matrix multiplication and very often some sort of matrix decomposition to fit models and do analysis: linear regression, various more sophisticated forms of regression, deep neural networks, principle components analysis (PCA) and the wide varieties of generalizations and variations on PCA, etc., etc.

### **1.2 Goals**

Here’s what I’d like you to get out of this unit:

1

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

In general we do not try to count the actual number of calculations, but just their order, though in some cases in this unit we’ll actually get a more exact count. In general, we denote this as _O_ ( _f_ ( _n_ )) which means that the number of calculations approaches _cf_ ( _n_ ) as _n →∞_ (i.e., we know the calculation is approximately proportional to _f_ ( _n_ )). Consider matrix multiplication, _AB_ , with matrices of size _a × b_ and _b × c_ . Each column of the second matrix is multiplied by all the rows of the first. For any given inner product of a row by a column, we have _b_ multiplies. We repeat these operations for each column and then for each row, so we have _abc_ multiplies so _O_ ( _abc_ ) operations. We could count the additions as well, but there’s usually an addition for each multiply, so we can usually just count the multiplys and then say there are such and such {multiply and add}s. This is Monahan’s approach, but you may see other counting approaches where one counts the multiplys and the adds separately.

2

For two symmetric, _n × n_ matrices, this is _O_ ( _n_<sup>3</sup> ). Similarly, matrix factorization (e.g., the Cholesky decomposition) is _O_ ( _n_<sup>3</sup> ) unless the matrix has special structure, such as being sparse. As matrices get large, the speed of calculations decreases drastically because of the scaling as _n_<sup>3</sup> and memory use increases drastically. In terms of memory use, to hold the result of the multiply indicated above, we need to hold _ab_ + _bc_ + _ac_ total elements, which for symmetric matrices sums to 3 _n_<sup>2</sup> . So for a matrix with _n_ = 10000, we have 3 _·_ 10000<sup>2</sup> _·_ 8 _/_ 1 _e_ 9 = 2 _._ 4Gb.

When we have _O_ ( _n_<sup>_q_</sup> ) this is known as polynomial time. Much worse is _O_ ( _b_<sup>_n_</sup> ) (exponential time), while much better is _O_ (log _n_ ) (log time). Computer scientists talk about NP-complete problems; these are essentially problems for which there is not a polynomial time algorithm - it turns out all such problems can be rewritten such that they are equivalent to one another.

In real calculations, it’s possible to have the actual time ordering of two approaches differ from what the order approximations tell us. For example, something that involves _n_<sup>2</sup> operations may be faster than one that involves 1000( _n_ log _n_ + _n_ ) even though the former is _O_ ( _n_<sup>2</sup> ) and the latter _O_ ( _n_ log _n_ ). The problem is that the constant, _c_ = 1000, can matter (depending on how big _n_ is), as can the extra calculations from the lower order term(s), in this case 1000 _n_ .

A note on terminology: _flops_ stands for both floating point operations (the number of operations required) and floating point operations per second, the speed of calculation.

### **1.5 Notation and dimensions**

I’ll try to use capital letters for matrices, _A_ , and lower-case for vectors, _x_ . Then _xi_ is the ith element of _x_ , _Aij_ is the _i_ th row, _j_ th column element, and _A·j_ is the _j_ th column and _Ai·_ the _i_ th row. By default, we’ll consider a vector, _x_ , to be a one-column matrix, and _x_<sup>_⊤_</sup> to be a one-row matrix. Some of the textbook resources also use _aij_ for _Aij_ and _aj_ for the _j_ th column.

Throughout, we’ll need to be careful that the matrices involved in an operation are conformable: for _A_ + _B_ both matrices need to be of the same dimension, while for _AB_ the number of columns of _A_ must match the number of rows of _B_ . Note that this allows for _B_ to be a column vector, with only one column, _Ab_ . Just checking dimensions is a good way to catch many errors. Example: is Cov( _Ax_ ) = _A_ Cov( _x_ ) _A_<sup>_⊤_</sup> or Cov( _Ax_ ) = _A_<sup>_⊤_</sup> Cov( _x_ ) _A_ ? Well, if _A_ is _m × n_ , it must be the former, as the latter is not conformable.

The **inner product** of two vectors is<sup>�</sup> _i_<sup>_x_</sup> _i_<sup>_y_</sup> _i_<sup>=</sup><sup>_x⊤y≡⟨x, y⟩≡x · y_.</sup>

The **outer product** is _xy_<sup>_⊤_</sup> , which comes from all pairwise products of the elements.

When the indices of summation should be obvious, I’ll sometimes leave them implicit. Ask me if it’s not clear.

3

### **1.6 Norms**

_∥x∥p_ = (<sup>�</sup> _i_<sup>_|x_</sup> _i_<sup>_|p_)1</sup><sup>_/p_andthestandard(Euclidean)normis</sup><sup>_∥x∥_</sup> 2<sup>=</sup> ~~�~~ <u>�</u> _x_ 2 _i_<sup>=</sup> _√x_<sup>_⊤_</sup> _x_ , just the length of the vector in Euclidean space, which we’ll refer to as _∥x∥_ , unless noted otherwise. One commonly used norm for a matrix is the Frobenius norm, _∥A∥F_ = (� _i,j_<sup>_a_2</sup> _ij_<sup>)1</sup><sup>_/_2.</sup>

In this Unit, we’ll make use of the **induced matrix norm** , which is defined relative to a corresponding vector norm, _∥· ∥_ , as:


So we have


If you’re not familiar with the supremum (“sup” above), you can just think of it as taking the maximum.

A property of any legitimate matrix norm (including the induced norm) is that _∥AB∥≤ ∥A∥∥B∥_ . Recall that norms must obey the triangle inequality, _∥A_ + _B∥≤∥A∥_ + _∥B∥_ .

A normalized vector is one with “length”, i.e., Euclidean norm, of one. We can easily normalize a vector: _x_ ˜ = _x/∥x∥_

The angle between two vectors is


### **1.7 Orthogonality**

Two vectors are orthogonal if _x_<sup>_⊤_</sup> _y_ = 0, in which case we say _x ⊥ y_ . An **orthogonal matrix** is a matrix in which all of the columns are orthogonal to each other and normalized. Orthogonal matrices can be shown to have full rank. Furthermore if _A_ is orthogonal, _A_<sup>_⊤_</sup> _A_ = _I_ , so _A_<sup>_−_1</sup> = _A_<sup>_⊤_</sup> . Given all this, the determinant of orthogonal _A_ is either 1 or -1. Finally the product of two orthogonal matrices, _A_ and _B_ , is also orthogonal since ( _AB_ )<sup>_⊤_</sup> _AB_ = _B_<sup>_⊤_</sup> _A_<sup>_⊤_</sup> _AB_ = _B_<sup>_⊤_</sup> _B_ = _I_ .

**Permutations** Sometimes we make use of matrices that permute two rows (or two columns) of another matrix when multiplied. Such a matrix is known as an elementary permutation matrix and is an orthogonal matrix with a determinant of -1. You can multiply such matrices to get more general permutation matrices that are also orthogonal. If you premultiply by _P_ , you permute rows, and if you postmultiply by _P_ you permute columns. Note that on a computer, you wouldn’t need to actually do the multiply (and if you did, you should use a sparse matrix routine), but rather one can often just rework index values that indicate where relevant pieces of the matrix are stored (more in

4

the next section).

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

For square, invertible matrices, we have that ( _A_<sup>_−_1</sup> )<sup>_⊤_</sup> = ( _A_<sup>_⊤_</sup> )<sup>_−_1</sup> . Why? Since we have ( _AB_ )<sup>_⊤_</sup> = _B_<sup>_⊤_</sup> _A_<sup>_⊤_</sup> , we have: _A_<sup>_⊤_</sup> ( _A_<sup>_−_1</sup> )<sup>_⊤_</sup> = ( _A_<sup>_−_1</sup> _A_ )<sup>_⊤_</sup> = _I_

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

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Statistical interpretations of matrix invertibility, rank, etc. →](03-2-statistical-interpretations-of-matrix-invertibility-rank-e.md)
