---
title: Unit 10 — linalg Part 07 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit10-linalg.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 10 — linalg Part 07 —

**Source:** [`units/unit10-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The main use of these ideas for our purposes is in thinking about the numerical accuracy of a linear system solution (Gentle-NLA Sec 3.4). On a computer we have the system


where the ’perturbation’ is from the inaccuracy of computer numbers. Our exploration of computer numbers tells us that


where _p_ = 16 for standard double precision floating points. Following Gentle, one gets the approximation


so if cond( _A_ ) _≈_ 10<sup>_t_</sup> , we have accuracy of order 10<sup>_t−p_</sup> instead of 10<sup>_−p_</sup> . (Gentle cautions that this holds only if 10<sup>_t−p_</sup> _≪_ 1). So we can think of the condition number as giving us the number of digits of accuracy lost during a computation relative to the precision of numbers on the computer. E.g., a condition number of 10<sup>8</sup> means we lose 8 digits of accuracy relative to our original 16 on standard systems. One issue is that estimating the condition number is itself subject to numerical error and requires computation of _A_<sup>_−_1</sup> (albeit not in the case of _L_ 2 norm with square, nonsingular _A_ ) but see Golub and van Loan (1996; p. 76-78) for an algorithm.

**Improving conditioning** Ill-conditioned problems in statistics often arise from collinearity of regressors. Often the best solution is not a numerical one, but re-thinking the modeling approach, as this generally indicates statistical issues beyond just the numerical difficulties.

A general comment on improving conditioning is that we want to avoid large differences in the magnitudes of numbers involved in a calculation. In some contexts such as regression, we can center and scale the columns to avoid such differences - this will improve the condition of

14

the problem. E.g., in simple quadratic regression with _x_ = _{_ 1990 _, . . . ,_ 2010 _}_ (e.g., regressing on calendar years), we see that centering and scaling the matrix columns makes a huge difference on the condition number

t1 <- 1990:2010 _# naive covariate_ X1 <- **cbind** ( **rep** (1, 21), t1, t1^2) e1 <- **eigen** ( **crossprod** (X1)) e1$values ## [1] 3.360186e+14 7.699100e+02 -3.833498e-08 t2 <- t1 - 2000 _# centered_ X2 <- **cbind** ( **rep** (1, 21), t2, t2^2) e2 <- **eigen** ( **crossprod** (X2)) e2$values ## [1] 50677.704275 770.000000 9.295725 t3 <- t2/10 _# centered and scaled_ X3 <- **cbind** ( **rep** (1, 21), t3, t3^2) e3 <- **eigen** ( **crossprod** (X3)) e3$values ## [1] 24.112935 7.700000 1.953665

The basic story is that simple strategies often solve the problem, and that you should be cognizant of the absolute and relative magnitudes involved in your calculations.

One rule of thumb is to try to work with numbers whose magnitude is around 1. We can often scale the values in our problem in order to do this. I.e., change the units of your variables. Instead of personal income in dollars, use personal income in thousands or hundreds of thousands of dollars.

---

[← 3 Computational issues](06-3-computational-issues.md) · [Up: contents](index.md) · [4 Matrix factorizations (decompositions) and solving systems of linear equations →](08-4-matrix-factorizations-decompositions-and-solving-systems-o.md)
