---
title: 3. Gambling on a favorable game.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_1_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_1_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Gambling on a favorable game.

**Source:** [`lecture_1_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_1_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Hypothetical setting: events _A_ 1 _, A_ 2 _, . . ._ independent, P( _Ai_ ) = _p >_ 1 _/_ 2. Imagine _p_ = 0 _._ 51. But you can make bets at even odds (as if _p_ were 1 _/_ 2). What is the best way to exploit this favorable game, if you have an initial “fortune” _x_ 0 and can only work with your winnings, not with extra money?

Common sense suggests a strategy: choose 0 _< α <_ 1 and, at each step, bet a proportion _α_ of your current fortune. If you use this strategy, what happens in the long run?

Students often find it hard to get started on this question. It’s helpful to remember the **indicator r.v.** _I_ ( _A_ ). We want to study

_Xn_ = your fortune after _n_ bets

and we can relate _Xn_ to _Xn−_ 1 as follows.

David Aldous Lecture 1


Then


By the law of large numbers we have


Now saying _n_<sup><u>1</u>log</sup><sup>_Xn→b_isroughlysayingthat</sup><sup>_Xn_behavesasexp(</sup><sup>_bn_),</sup> so our “long-run optimality” criterion is to maximize this long run growth rate _b_ = E log _V_ 1.

David Aldous Lecture 1


Rewrite


So the long run growth rate is


In this question, _δ_ is given, but we can choose _α_ to maximize this expression. So we choose _α_ = 2 _δ_ and get a long run growth rate _≈_ 2 _δ_<sup>2</sup> . This is called the **Kelly strategy** – see popular books such as _Fortune’s Formula_ (William Poundstone) or _Red-Blooded Risk: The Secret History of Wall Street_ (Aaron Brown), who describes it as “getting rich exponentially slowly”. A conceptual point is that this strategy is quite different from “maximize E(gain) on each step”, which would make you bet all your fortune on each bet, and therefore likely lose all your money quickly.

David Aldous Lecture 1

---

[← 2. When should you buy every Lotto combination?](03-2-when-should-you-buy-every-lotto-combination.md) · [Up: contents](index.md)
