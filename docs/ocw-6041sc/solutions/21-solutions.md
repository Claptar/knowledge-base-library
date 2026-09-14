---
title: 21 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/21-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 21 solutions

**Source:** `solutions/21-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

Recitation 21 Solutions November 23, 2010


and the Markov inequality yields


(b) Using the Chebyshev inequality, we find that


(c) Finally, using the Central Limit Theorem, we find that


2. Check online solutions.

3. (a) If we interpret Xi as the number of arrivals in an interval of length 1 in a Poisson process of rate 1, then, Sn = X1 + · · · + Xn can be seen as the number of arrivals in an interval of length n in the Poisson process of rate 1. Therefore, Sn is a Poisson random variable with mean and variance equal to n.

   - (b) We use the random variables X1, . . . , Xn and the random variable Sn = X1 + · · · + Xn. Denoting by Z the standard normal, and applying the central limit theorem, we have for

1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

large n


where the first equation follows from the fact that Sn takes integer values, the first approx­ imation is suggested by the central limit theorem, and the second approximation uses the fundamental theorem of calculus (the value of a definite integral over a small interval is equal to the length of the interval times the integrand evaluated at some point within the interval). Since Sn is Poisson with mean n, we have


n and by combining the preceding relations, we see that n! ≈ n e<sup>−n√</sup> 2πn = √2πn � <u>ne</u><sup>�n</sup> . One may show that


so the relative error of the approximation tends to 0 as n →∞. A more precise estimate is that


where


However, one cannot derive these relations from the central limit theorem.

Note that the form of the approximation was first discovered by de Moivre in the form · n! ≈ n<sup>n+1/2</sup> e<sup>−n</sup> (constant), and gave a complicated expression for the constant. De Moivre’s friend Stirling subsequently showed that the constant has the simple form √2π.

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
