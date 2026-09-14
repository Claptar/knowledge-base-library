---
title: Sequence alignment with generalized gap penalties
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Sequence alignment with generalized gap penalties

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• **Implementing a generalized gap penalty function F(gap_length)**


<!-- Start of picture text -->
Initialization: same<br>Iteration:<br>F(i-1, j-1) + s(xi, yj)<br>F (i,j)  F(i, j)   = max maxk=0…i-1F(k,j) – (i-k)<br>maxk=0…j-1F(i,k) – (j-k)<br>Termination: same<br><!-- End of picture text -->

**<u>Running Time:</u>** O(N<sup>2</sup> M) (cubic) **<u>Space:</u>** O(NM)

**Do we have to be so general?**

16

##### **Algorithmic trade-offs of varying gap penalty functions**

 (n)


Linear gap penalty:  w(k) = k*p

- State: Current index tells if in a gap or not

- Achievable using quadratic algorithm (even w/ linear space)


<!-- Start of picture text -->
 (n)<br><!-- End of picture text -->


Quadratic:  w(k) = p+q*k+rk<sup>2</sup> .

- State:  needs to encode the length of the gap, which can be O(n)

- To encode it we need O(log n) bits of information.  Not feasible


<!-- Start of picture text -->
 (n)<br>e<br>d<br><!-- End of picture text -->

- Affine gap penalty:  w(k) = p + q*k, where q<p – State:  add binary value for each sequence:  starting a gap or not

- Implementation:  add second matrix for already-in-gap (recitation)


<!-- Start of picture text -->
 (n)<br><!-- End of picture text -->


- Length (mod 3) gap penalty for protein-coding regions – Gaps of length divisible by 3 are penalized less: conserve frame

- This is feasible, but requires more possible states

- Possible states are:  starting, mod 3=1, mod 3=2, mod 3=0

17

---

[← More variations on the theme: semi-global alignment](13-more-variations-on-the-theme-semi-global-alignment.md) · [Up: contents](index.md) · [Today’s Goal: Diving deeper into alignments →](15-today-s-goal-diving-deeper-into-alignments.md)
