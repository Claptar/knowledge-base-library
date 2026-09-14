---
title: 2. When should you buy every Lotto combination?
source: https://www.stat.berkeley.edu/~aldous/150/lecture_1_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_1_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. When should you buy every Lotto combination?

**Source:** [`lecture_1_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_1_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Simplifying some real-world issues, assume Ticket cost 1 dollar. _N_ combinations of numbers


”hold over” _A_ dollars from previous drawing (no winner) _M_ other tickets sold for this drawing


50% of ticket price goes to “pool” of prize money.

We want a formula for E(gain) – when does this work out to be _>_ 0?

David Aldous Lecture 1


If you buy all _N_ combinations

pool of prize money = _A_ + ( _M_ + _N_ ) _/_ 2 _._

You have a winning ticket but so do some random number _X_ of other people; so your winnings are 1+1 _X_<sup>_×_[</sup><sup>_A_+ (</sup><sup>_M_+</sup><sup>_N_)</sup><sup>_/_2]andyour</sup> gain = 1+1 _X_<sup>_×_[</sup><sup>_A_+ (</sup><sup>_M_+</sup><sup>_N_)</sup><sup>_/_2]</sup><sup>_−N._</sup>

A rough model is that _X_ has Poisson( _λ_ = _M/N_ ) distribution. We need to calculate E 1+1 _X_<sup>;recallthegeneralformula:</sup>


This is a bit complicated but we end with explicit formula


David Aldous Lecture 1


Bottom line: need “hold over” amount _A_ to be large, and the number of other tickets _M_ to be small; but this doesn’t happen because a large “hold over” encourages other people to buy tickets. Recall terminology about gambling – also apply to stock market investment, insurance etc.


You end with a random “gain” , taking your costs into account. A loss is a negative gain.

A bet is called


**fair** if E(gain) = 0 **favorable** if E(gain) _>_ 0 **unfavorable** if E(gain) _<_ 0

Using expectation as a criterion is not always appropriate. If potential gains/losses are large then issues of **utility** arise. Here is another case – imagining stock market investment as a favorable game.

David Aldous

Lecture 1

---

[← 1. A famous hypothetical example.](02-1-a-famous-hypothetical-example.md) · [Up: contents](index.md) · [3. Gambling on a favorable game. →](04-3-gambling-on-a-favorable-game.md)
