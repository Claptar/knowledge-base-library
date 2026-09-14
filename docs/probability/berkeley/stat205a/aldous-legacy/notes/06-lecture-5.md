---
title: Lecture 5.
source: https://www.stat.berkeley.edu/~aldous/205A/notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 5.

**Source:** [`notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Topics. Conditional expectations, conditional probabilities and regular conditional distributions (r.c.d.’s). Conditioning and independence. Conditional independence (see homework for definition).

Let’s record two lemmas.

**Lemma 10** If E(X|G) is a.s. equal to some D-measurable r.v., and if D ⊂ G, then E(X|D) = E(X|G).

**Lemma 11** If X and Y are conditionally independent given G, and if V is G-measurable, then X and (Y, V ) are conditionally independent given G.

Also record basic property of r.c.d.’s. If Q is a r.c.d. for Z given U then


**Lecture 6.** Measure-theory set-up for Markov chains.

This material is presented somewhat differently in Durrett 5.1 and 5.2. I want to emphasize the conditional independence aspects. The first result (I call it the splice lemma) gives the “conditionally independent” analog of product measure.

**Lemma 12** Let S1, S2, S3 be nice spaces. Let µ12 be a p.m. on S1 × S2 and µ23 be a p.m. on S2 × S3 such that the marginals on S2 coincide. Then there exists a unique probability measure µ on S1 ×S2 ×S3 such that, writing µ = dist(X1, X2, X3),

(i) dist(X1, X2) = µ12 and dist(X2, X3) = µ23

(ii) X1 and X3 are conditionally independent given X2.

Proof. We can specify µ on S1 × S2 × S3 by specifying a marginal p.m. on S1 × S2 and a kernel Q from S1 × S2 to S3. So let the marginal be µ12 and let the kernel be


where Q23 is the kernel from S2 to S3 associated with µ23. Property (i) is easy. For (ii),


9

---

[← Lecture 4.](05-lecture-4.md) · [Up: contents](index.md)
