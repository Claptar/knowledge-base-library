---
title: "9. RNA Secondary Structure and Melting"
course: "MIT 8.592J"
chapter: 9
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 9. RNA Secondary Structure and Melting

## What this covers

This chapter asks two connected questions about RNA folding, treated as a statistical-mechanics
problem rather than a biochemistry one. First: given a sequence, how do you find, in reasonable
time, the pairing of bases with itself — its secondary structure — that minimises the energy?
Second: what happens statistically to an ensemble of such structures once thermal fluctuations are
strong enough to melt the native fold, and does a hairpin melt sharply at some temperature? It
assumes partition functions and Boltzmann weights, the central limit theorem applied to a sum of
many independent steps, and some prior acquaintance with the Poland–Scheraga model of DNA melting
and its loop-closure exponent, which the last section uses by direct analogy rather than
re-deriving.

## RNA as a self-pairing polymer

RNA is built from the same kind of nucleotide as DNA — a sugar, a phosphate and a base — but the
sugar is ribose rather than deoxyribose, and the base that pairs with adenine is uracil (U) rather
than thymine (T). The consequential difference, though, is that RNA is normally single-stranded.
Where two strands of DNA wrap around each other into a rigid double helix, a single strand of RNA
is flexible enough to loop back on itself, so that bases far apart along the chain can form the
same kind of Watson–Crick bond that holds the two strands of DNA together. This is what gives RNA
its structural range, from catalytic and scaffolding roles (the ribosome) to purely informational
ones (messenger RNA).

Three levels of description follow from this. The **primary structure** is the sequence of bases.
The **secondary structure** is the pattern of which bases pair with which — the list of internal
Watson–Crick bonds. The **tertiary structure** is the actual three-dimensional shape the connected
molecule settles into. This chapter is about predicting the secondary structure from the sequence
and about what happens to it as temperature is raised.

## Counting structures, and why planarity is the useful restriction

The direct question — of the many ways to pair up $N$ bases, which minimises the energy — is a
hard combinatorial problem before it is a physical one. The number of possible pairings of $N$
bases grows roughly as $(N-1)!!$, so checking every one is infeasible for any real molecule. The
rescue is physical rather than computational: not every pairing corresponds to a shape that can
actually be laid out in three dimensions without the backbone crossing itself, and almost every
real secondary structure belongs to a much smaller class — the *planar* pairings, in which the
backbone and every base-pair connection can be drawn in a plane with no two lines crossing. A
connection that would force a crossing produces a *pseudoknot*, and pseudoknots do occur in real
RNA but are rare. Restricting the search to planar structures is therefore a mild physical
approximation that buys a large computational one: planar structures can be enumerated, and
optimised, in polynomial time.

Three equivalent ways of writing down a planar pairing make this precise.

- **Arch diagram.** Stretch the backbone along a line and draw an arch over every paired pair of
  bases. Planarity is exactly the statement that two arches are either disjoint or one is nested
  entirely inside the other — arches never cross.
- **Parenthesis string.** Walk along the sequence from one end. Write an open parenthesis at the
  first base of a pair and close it at its partner; an unpaired base is a dot. A planar structure
  is exactly a grammatically well-formed string of parentheses, for example
  $$..(((..(((........)))..((((((.....)))))..))..)))$$
  — at every point along the string, every close has already been opened.
- **Mountain diagram.** Turn each character of the parenthesis string into a step: an open
  parenthesis is a step up, a close is a step down, a dot is a step that stays level. Planarity —
  no premature close — is exactly the condition that this walk never dips below the height it
  started at; the profile it traces looks like a mountain skyline sitting over the backbone.

<figure>
<svg viewBox="0 0 400 250" role="img" aria-label="A short pairing shown as nested arches, as a parenthesis string, and as the equivalent up-down-level walk">
  <text x="8" y="46" font-size="10" fill="currentColor">pairing</text>
  <text x="8" y="104" font-size="10" fill="currentColor">string</text>
  <text x="8" y="202" font-size="10" fill="currentColor">walk</text>

  <line x1="40" y1="60" x2="360" y2="60" stroke="currentColor" stroke-width="1.5"/>
  <path d="M60,60 Q200,15 340,60" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M140,60 Q200,35 260,60" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <g fill="currentColor">
    <circle cx="60" cy="60" r="3"/><circle cx="100" cy="60" r="3"/><circle cx="140" cy="60" r="3"/>
    <circle cx="180" cy="60" r="3"/><circle cx="220" cy="60" r="3"/><circle cx="260" cy="60" r="3"/>
    <circle cx="300" cy="60" r="3"/><circle cx="340" cy="60" r="3"/>
  </g>
  <g font-size="10" text-anchor="middle" fill="currentColor">
    <text x="60" y="76">1</text><text x="100" y="76">2</text><text x="140" y="76">3</text>
    <text x="180" y="76">4</text><text x="220" y="76">5</text><text x="260" y="76">6</text>
    <text x="300" y="76">7</text><text x="340" y="76">8</text>
  </g>

  <g font-size="14" text-anchor="middle" font-family="monospace" fill="currentColor">
    <text x="60" y="104">(</text><text x="100" y="104">.</text><text x="140" y="104">(</text>
    <text x="180" y="104">.</text><text x="220" y="104">.</text><text x="260" y="104">)</text>
    <text x="300" y="104">.</text><text x="340" y="104">)</text>
  </g>

  <polygon points="40,220 80,200 120,200 160,180 200,180 240,180 280,200 320,200 360,220"
           fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <polyline points="40,220 80,200 120,200 160,180 200,180 240,180 280,200 320,200 360,220"
            fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="220" x2="360" y2="220" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="365" y="224" font-size="10" fill="currentColor">h=0</text>
  <text x="200" y="242" font-size="11" text-anchor="middle" fill="currentColor">position along the chain</text>
</svg>
<figcaption>A six-base illustration of the pair (1,8) nesting the pair (3,6): the same planar
structure drawn as arches over the backbone, as a parenthesis string, and as the up/level/down
walk it traces — the walk never dips below its starting height, which is exactly the planarity
condition.</figcaption>
</figure>

## A recursion for the minimum-energy structure

Fix a simple model in which *all* pairings without pseudoknots are allowed, with no extra penalty
for bending or steric clash. For a configuration $C$, the energy is a sum over its bonded pairs,
$E[C] = \sum \varepsilon_{ij}$, where $\varepsilon_{ij}$ is the energy assigned to a bond between
bases $i$ and $j$, and the sum runs only over the pairs actually present in $C$.

The minimum-energy configuration can be built up recursively. Suppose the optimal energy is
already known for every sub-sequence of length $n$ or shorter. Consider a sub-sequence of length
$n+1$, running from site $i$ to $j = i+n+1$. In the optimal structure for this sub-sequence, either
$j$ is unpaired, or $j$ is paired with some site $k$ with $i \le k \le j-1$. In the latter case, the
arch between $k$ and $j$ splits the remaining sites into two segments — from $i$ to $k-1$, and from
$k+1$ to $j-1$ — and by planarity these two segments cannot interact, so each can be optimised
independently. Checking all $n+2$ possibilities (unpaired, or paired to one of the $n+1$ choices of
$k$) gives the recursion
$$E_{i,j} = \min\big[\,E_{i,j-1},\ \varepsilon_{kj} + E_{i,k-1} + E_{k+1,j-1}\,\big] \quad \text{for } i \le k \le j-1. \tag{2.96}$$
Starting from segments of length one, where $E_{i,i+1} = \varepsilon_{i\,i+1}$, this equation builds
up optimal energies for longer and longer segments, and the optimal structure itself is recovered
by tracing the choices back afterward.

## From ground state to partition function

The same recursive idea extends to finite temperature, where entropy competes with binding energy.
Assign each segment a partition function rather than just a ground-state energy, and the same
splitting argument that gave Eq. (2.96) gives a recursion for it:
$$Z_{i,j} = Z_{i,j-1} + \sum_{k=i}^{j-1} e^{-\beta \varepsilon_{kj}}\, Z_{i,k-1}\, Z_{k+1,j-1}. \tag{2.97}$$
The first term is the contribution from $j$ unpaired; each term in the sum is the contribution from
$j$ paired to $k$, weighted by the Boltzmann factor of that bond and by the (independent, by
planarity) partition functions of the two resulting segments.

## The molten state: RNA as a constrained random walk

Equation (2.97) can be used to follow how a native secondary structure denatures as temperature
rises, presumably vanishing at some melting temperature $T_m$ in favour of a molten state that
behaves like a branched polymer. The details of that melting depend strongly on the sequence and
on the native structure being melted — the case of a simple hairpin is worked out in the next
section. Here the question is about the molten phase itself: with the specific native structure
forgotten, what fraction of bases are typically paired at all?

To isolate this, strip out sequence dependence by setting every bond energy to a common value,
$\varepsilon_{ij} = \varepsilon$, with Boltzmann weight $q \equiv e^{-\beta\varepsilon} \ge 1$ (so
$q$ is large at low temperature, where pairing is favoured, and $q \to 1$ at high temperature).
The partition function of Eq. (2.97) then depends only on segment length, $Z_{i,j} = Z_m(|j-i|+1)$,
and the recursion becomes
$$Z_m(N+1) = Z_m(N) + q\sum_{k=1}^{N} Z_m(k-1)\, Z_m(N-k), \qquad Z_m(0) = 1. \tag{2.98}$$

This recursion can be solved directly, but the more informative route is through the mountain
picture introduced above. Give each step of the walk a weight: a factor of $1$ for a level step
(an unpaired base) and a factor of $\sqrt{q}$ for a vertical step, up or down (a base opening or
closing a pair) — so that the two steps belonging to one bond together contribute $\sqrt{q}\cdot
\sqrt{q} = q$, the correct Boltzmann weight for that bond. Each secondary structure is then a
Markovian random walk with these three step weights, required never to dip below its starting
height.

Ignore that requirement for a moment. The total weight of all $N$-step walks from the origin,
summing over the three choices at every step, is $(1+2\sqrt{q})^N$. Since up and down carry equal
weight $\sqrt q$ and level carries weight $1$, the mean displacement per step is zero by symmetry
and the variance per step is the weighted average of (displacement)$^2$,
$\big(\sqrt{q}\cdot 1 + \sqrt{q}\cdot 1 + 1\cdot 0\big)/(1+2\sqrt{q}) = 2\sqrt{q}/(1+2\sqrt{q})$, so
after $N$ independent steps $\sigma^2 = N\cdot 2\sqrt{q}/(1+2\sqrt{q})$. Appealing to the central
limit theorem for large $N$, the total weight of walks ending at height $h$ after $N$ steps is
Gaussian,
$$W(N,h) = (1+2\sqrt{q})^N \exp\!\left[-\frac{(1+2\sqrt{q})h^2}{4\sqrt{q}N}\right] \sqrt{\frac{1+2\sqrt{q}}{4\pi\sqrt{q}N}}. \tag{2.99}$$

Asking what fraction of *all* walks return to the origin ($h=0$) gives the ordinary
one-dimensional random-walk result, $\Omega(N) \propto g^N/N^{c}$ with loop-closure exponent
$c = 1/2$. But counting planar structures needs only the walks that return to $h=0$ *without ever
going below it* — the unrestricted count in Eq. (2.99) has to be corrected for the walks that
violate this.

## Enforcing the constraint: the method of images

The requirement that the walk never dip below its starting height $h=0$ is the same as forbidding
it from ever reaching $h=-1$ — one step below the start. This is a random walk with an absorbing
barrier, and it can be solved by an argument closely related to the method of images in
electrostatics (the solution is due to Chandrasekhar, *Rev. Mod. Phys.* **15**, 1 (1943)).

Reflect the starting point $h=0$ through the forbidden level $h=-1$ to get an image point at
$h=-2$. Consider the ensemble $W^*$ of walks that start at this image point and end at $h=0$: every
such walk must cross the level $h=-1$ at least once, since it starts below it and ends above it.
Now build a second ensemble $W'$ from $W^*$: take each walk in $W^*$, and reflect the portion of it
before its *first* crossing of $h=-1$ across that level (so it now starts at $h=0$ instead of
$h=-2$), then let it continue exactly as $W^*$ did afterward. The walks in $W'$ start and end at
$h=0$, by construction touch the forbidden level $h=-1$ at some point, and are in one-to-one
correspondence with $W^*$ — so $W'$ is precisely the set of illegitimate walks that needs to be
subtracted from the unconstrained count. Since $W^*$ runs from $h=-2$ to $h=0$, an excursion of
size $2$, this is the weight $W(N,2)$ already computed in Eq. (2.99), and
$$Z_m(N+1) = W(N,0) - W(N,2) = (1+2\sqrt{q})^N\left[1-\exp\!\left(-\frac{1+2\sqrt{q}}{\sqrt{q}N}\right)\right] \sqrt{\frac{1+2\sqrt{q}}{4\pi\sqrt{q}N}}. \tag{2.100}$$
Expanding the bracket for large $N$ (where the Gaussian approximation is valid) gives the clean
asymptotic form
$$Z_m(N+1) = A(q)\,\frac{g(q)^N}{N^{c}}, \quad A(q) = \left(\frac{1+2\sqrt{q}}{64\pi^3\sqrt{q}}\right)^{3/2},\ \ g(q) = 1+2\sqrt{q},\ \ c = \tfrac{3}{2}. \tag{2.101}$$

The one-step-below barrier changes nothing about the exponential growth rate $g(q)$, but it changes
the loop-closure exponent from $c=1/2$, for an unconstrained walk, to $c=3/2$ once the walk is
forbidden from crossing into negative territory. That shift is the single most important
consequence of the non-crossing (no pseudoknot) constraint.

Because a bound pair corresponds to a vertical step and an unpaired base to a level one, the
fraction of bases that are paired in the molten phase is simply the probability that a given step
of the walk is vertical rather than level:
$$\frac{\langle N_B\rangle}{N} = \frac{2\sqrt{q}}{1+2\sqrt{q}}. \tag{2.102}$$
This goes to $1$ at low temperature ($q$ large, pairing strongly favoured) and, notably, only down
to $2/3$ — not to $0$ — as $q \to 1$ at high temperature: even with no energetic preference for
pairing at all, two-thirds of the bases remain paired in the molten phase, purely as a consequence
of the planarity constraint itself.

## Melting of a hairpin

A hairpin is the simplest native RNA structure: base $k$ pairs with base $2N-k+1$ for every $k$,
folding the chain back on itself along its whole length. For long hairpins, the transition from
this fully native fold to the molten state can be worked out analytically using a Gō model, in
which intermediate configurations consist of alternating segments — some still holding their
original native bonds, others fully melted.

Summing over all such partially melted configurations, and neglecting any interaction between the
segments, gives a partition function of the form
$$Z_n(N) = \sum_{l_1,l_2,l_3,\dots}{}' R(l_1)\,Z_m(2l_2+1)\,R(l_3)\,Z_m(2l_4+1)\cdots, \tag{2.103}$$
with the segment lengths constrained by $l_1+l_2+l_3+\cdots = N$. The molten segments contribute
through $Z_m$ from Eq. (2.101); the native segments contribute through $R(l)$, built from a
separate, stronger Boltzmann weight $\overline{q} = e^{-\beta\overline{\varepsilon}} > q$ for each
native bond, reflecting that the native bond energy $\overline{\varepsilon}$ is more favourable than
the generic bulk pairing energy $\varepsilon$ used for the molten phase.

With this structure, the hairpin melting problem becomes identical to the Poland–Scheraga model of
DNA melting, with $w=\overline{q}$, $g=1+2\sqrt{q}$ and $c=3/2$. Carrying that identification
through gives a genuine melting transition at a finite temperature, at which the native fraction
vanishes continuously, and linearly — order-parameter exponent $\beta = 1$.

## Sources

- Definitions of RNA structure, the counting problem, planarity, pseudoknots, and the three
  representations (arch, parenthesis, mountain): `01-introduction.md` (section "2.5 RNA
  structure"), including the recursions for minimum energy, Eq. (2.96), and the finite-temperature
  partition function, Eq. (2.97).
- The molten-phase calculation — uniform bond energy, the mountain-walk mapping, the unconstrained
  Gaussian weight Eq. (2.99), the loop-closure exponent, the method-of-images argument, Eqs. (2.100)–(2.102):
  `02-2-5-1-free-energy-of-molten-rna.md` (section "2.5.1 Free energy of molten RNA").
- The hairpin Gō model, Eq. (2.103), and the identification with the Poland–Scheraga model:
  `03-2-5-2-melting-of-a-hairpin.md` (section "2.5.2 Melting of a hairpin").
- No transcript, written notes or exercises were supplied for this lecture; the chapter is built
  from the slide markdown alone.
- The slide files themselves are model reconstructions of a PDF with no extractable text layer
  (course 8.592J/HST.452J, MIT OpenCourseWare, Spring 2011, CC BY-NC-SA 4.0), and each carries the
  caveat that every equation in it is unverified against the original — Eqs. (2.96)–(2.103) above
  should be checked against the original slide PDF before being relied on as exact.
- The lecture refers to, but the supplied material does not contain: S. Chandrasekhar's solution of
  the absorbing-barrier random walk (*Rev. Mod. Phys.* **15**, 1 (1943)); R. Bundschuh and T. Hwa's
  Gō-model treatment of hairpin melting (*Phys. Rev. Lett.* **83**, 1479 (1999)); and the earlier
  treatment of the Poland–Scheraga model itself (its Eq. (2.79) for the partition function and Eq.
  (2.94) for the order-parameter exponent $\beta$), which this chapter's last section relies on
  without re-deriving.

---

[← 8. The Poland-Scheraga Melting Model](08-the-poland-scheraga-melting-model.md) · [Contents](index.md) · [10. Protein Search Kinetics on DNA →](10-protein-search-kinetics-on-dna.md)
