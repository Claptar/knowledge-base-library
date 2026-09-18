---
title: 2 Statistical interpretations of matrix invertibility, rank, etc.
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit10-linalg.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit10-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Statistical interpretations of matrix invertibility, rank, etc.

## 2.1 Linear independence, rank, and basis vectors

A set of vectors, $v_1, \dots v_n$, is linearly independent (LIN) when none of the vectors can be represented as a linear combination, $\sum c_i v_i$, of the others for scalars, $c_1, \dots, c_n$. If we have vectors of length $n$, we can have at most $n$ linearly independent vectors. The rank of a matrix is the number of linearly independent rows (or columns - it's the same), and is at most the minimum of the number of rows and number of columns. We'll generally think about it in terms of the dimension of the column space - so we can just think about the number of linearly independent columns.

Any set of linearly independent vectors (say $v_1, \dots, v_n$) span a space made up of all linear combinations of those vectors ($\sum_{i=1}^n c_i v_i$). The spanning vectors are known as basis vectors. We can express a vector $y$ that is in the space with respect to (as a linear combination of) basis vectors as $y = \sum_i c_i v_i$, where if the basis vectors are normalized and orthogonal, we can find the weights as $c_i = \langle y, v_i \rangle$.

Consider a regression context. We have $p$ covariates ($p$ columns in the design matrix, $X$), of which $q \leq p$ are linearly independent covariates. This means that $p-q$ of the vectors can be written as linear combos of the $q$ vectors. The space spanned by the covariate vectors is of dimension $q$, rather than $p$, and $X^T X$ has $p - q$ eigenvalues that are zero. The $q$ LIN vectors are basis vectors for the space - we can represent any point in the space as a linear combination of the basis vectors. You can think of the basis vectors as being like the axes of the space, except that the basis vectors are not orthogonal. So it's like denoting a point in $\mathbb{R}^q$ as a set of $q$ numbers telling us where on each of the axes we are - this is the same as a linear combination of axis-oriented vectors.

When fitting a regression, if $n = p = q$, a vector of $n$ observations can be represented exactly as a linear combination of the $p$ basis vectors, so there is no residual and we have a single unique (and exact) solution (e.g., with $n = p = 2$, the observations fall exactly on the simple linear regression line). If $n < p$, then we have at most $n$ linearly independent covariates (the rank is at most $n$). In this case we have multiple possible solutions and the system is ill-

---

[← 1 Preliminaries](01-1-preliminaries.md) · [Up: contents](index.md)
