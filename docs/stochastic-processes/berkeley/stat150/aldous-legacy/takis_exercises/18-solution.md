---
title: Solution.
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution.

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

71.

How would you modify the formula we derived for Es<sup>Ta</sup> for a simple random walk starting from 0 in order to make it valid for all a, positive or negative? Here Ta is the first hitting time of a.

Solution. For a simple random walk Sn = ξ1 + · · · + ξn, with P (ξi = +1) = p, P (ξi = −1) = q, we found


60

where T1 is the first time that the RW hits 1 (starting from 0), and we use the notation ψ(p, s) just to denote this function as a function of p and s. We argued that when a > 0, the random variable Ta is the sum of a i.i.d. copies of T1 and so


Let us now look at T−1. Since the distribution of T−1 is the same as that of T1 but for a RW where the p and q are interchanged we have


Now, if −a < 0, the random variable T−a is the sum of a i.i.d. copies of T−1. Hence


72.

Consider a simple symmetric random walk starting from 0 and let Ta be the first time that state a will be visited. Find a formula for P (Ta = n), n ∈ Z.

Solution. Let us consider the case a > 0, the other being similar. We have


whence


We write power series for the right and left hand sides separately.


Equating powers of s in both sides, we see that we need a + m = 2n, i.e. m = 2n − a.


We conclude:


61

73.

Consider a simple symmetric random walk starting from 0 and let Ta be the first time that state a will be visited. Derive the formulæ for P (Ta < ∞) in detail.

---

[← Takis exercises Part 17 —](17-takis-exercises-part-17.md) · [Up: contents](index.md) · [Solution. We have →](19-solution-we-have.md)
