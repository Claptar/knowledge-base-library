---
title: 17 Law of Total Variance
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/02-exam-quiz02-revi.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 17 Law of Total Variance

**Source:** `exams/02-exam-quiz02-revi.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Var(X|Y ) is a random variable that is a function of Y (the variance is taken with respect to X). To compute Var(X|Y ), first express Var(X|Y = y) = E[(X − E[X|Y = y])<sup>2</sup> |Y = y] as a function of y. Law of conditional variances: Var(X) = E[Var(X|Y )] + Var(E[X|Y ]) (equality between two real numbers)

21

19 Covariance and Correlation = Cov(X, Y ) E[(X − E[X])(Y − E[Y ])] = E[XY ] − E[X]E[Y ]

- By definition, X, Y are uncorrelated ⇔ Cov(X, Y ) = 0.

- If X, Y independent ⇒ X and Y are uncorrelated. (the converse is not true)

18 Sum of a random number of iid RVs

N discrete RV, Xi i.i.d and independent of N . Y = X1 + . . . + XN . Then: = E[Y ] E[X]E[N ] = Var(Y ) E[N ]Var(X) + (E[X])<sup>2</sup> Var(N )

22

Correlation Coefficient: (dimensionless) Cov(X, Y ) ρ = ∈ [−1, 1] σX σY ρ = 0 ⇔ X and Y are uncorrelated. |ρ| = 1 ⇔ X − E[X] = c[Y − E[Y ]] (linearly related)

- In general, Var(X+Y)= Var(X)+ Var(Y)+ 2 Cov(X,Y)

- If X and Y are uncorrelated, Cov(X,Y)=0 and Var(X+Y)= Var(X)+Var(Y)

24

23

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 16 Law of iterated expectations](11-16-law-of-iterated-expectations.md) · [Up: contents](index.md)
