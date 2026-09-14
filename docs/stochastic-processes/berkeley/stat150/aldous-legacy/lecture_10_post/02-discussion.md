---
title: Discussion.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_10_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_10_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Discussion.

**Source:** [`lecture_10_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_10_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- (a) There is a calculation which checks this _π_ does satisfy _π_ = _π_ **P** .

- (b) Because _π_ is the same for each choice of _b_ we have another formula


- (c) For an irreducible chain, the properties

   - E _i Ti_<sup>+</sup> _< ∞_ for some _i_ E _i Ti_<sup>+</sup> _< ∞_ for all _i_

are equivalent. When these hold we call the chain **positive-recurrent** . (d) The theorem implies that every finite-state irreducible chain is positive-recurrent. So every finite-state irreducible chain has a unique stationary distribution.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Limit theory for Markov chains combines this theorem with the next two theorems. The first is about convergence of **distributions** , the second is about convergence of **random variables** .

David Aldous

Lecture 10


Theorem _If the chain is irreducible, positive-recurrent and aperiodic, then for any initial distribution_ P( _X_ ( _t_ ) = _j_ ) _→ πj as t →∞ where π is the unique stationary distribution._


<!-- Start of picture text -->
Theorem<br>Write<br>t− 1<br>Ni ( t ) = � 11( X ( s )= i ) = number of visits to i before t.<br>s =0<br>If the chain is irreducible and positive-recurrent, then for any initial<br>distribution<br>t − 1 Ni ( t )  → πi a.s. as t →∞.<br>Note this implies but is stronger than previous fact<br>E[ t − 1 Ni ( t )]  → πi as t →∞.<br><!-- End of picture text -->

David Aldous Lecture 10


A final result is rather subtle. Note we only need this when the state space is infinite.

Proposition


_If irreducible, if there exists a probability distribution π satisfying π_ = _π_ **P** _, then the chain is positive-recurrent._


Then we can apply previous theorems and this _π_ is the unique stationary distribution.

See texts for proofs. I want to focus on what these results say, in our specific examples.

David Aldous

Lecture 10


Recall that for a doubly-stochastic chain the stationary distribution is the uniform distribution.

**Card-shuffling examples.** Theory implies that for any “non-stupid” random shuffle model, the distribution will eventually become closer and closer to uniform.

**Simple random walk on the n-by-n torus.** [board]

David Aldous Lecture 10

---

[← Ideas used in Lecture 9.](01-ideas-used-in-lecture-9.md) · [Up: contents](index.md) · [Example: Umbrellas. →](03-example-umbrellas.md)
