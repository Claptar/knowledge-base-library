---
title: "17. Binding, Kinetics, and Ultrasensitivity"
course: "MIT 8.591J 2014"
chapter: 17
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 17. Binding, Kinetics, and Ultrasensitivity

## What this covers

This chapter follows one lecture across four connected pieces: the equilibrium binding of two
molecules, what changes when the bound complex can also react (Michaelis–Menten kinetics), how an
inhibitor's effect on that kinetics gives away its mechanism, and the dynamics of a simple
transcription-factor-to-target gene circuit — ending with two distinct ways to make that circuit's
response ultrasensitive. It assumes only the definitions of a reaction rate and an equilibrium
constant, and enough calculus to solve $\dot Y = \beta - \alpha Y$.

## Binding equilibrium: two molecules, one complex

Two molecules $E$ and $S$ associate at rate $k_f$ and their complex $ES$ falls apart at rate $k_r$:
the forward flux is $k_f[E][S]$, the reverse flux is $k_r[ES]$. Their ratio defines the
dissociation constant,
$$K_d \equiv \frac{k_r}{k_f}.$$

A first thing worth being careful about: $k_f$ and $k_r$ look like the same kind of object — both
just "a $k$ with a subscript" — but they do not have the same units, because the forward rate
carries an extra factor of concentration that the reverse rate does not. It is $K_d$, the *ratio*,
that comes out with units of concentration, once the two rates are worked out consistently. This
is an easy point to lose track of later, precisely because the two symbols look so similar.

### Fraction bound, and four limits worth thinking through before any algebra

Define the fraction of $E$ that is in complex,
$$F_b \equiv \frac{[ES]}{[E] + [ES]},$$
on the assumption that free and bound are the only two states available to $E$. Before writing
down a formula for $F_b$, it pays to fix intuition against a few limits: if the algebra later
disagrees with the limit, one of the two — the intuition or the algebra — has to be wrong, and
finding out which is how you catch mistakes rather than just making them.

- **$S_{\text{total}} \to 0$.** Nothing to bind, so $F_b \to 0$.
- **$S_{\text{total}} \to \infty$.** Enough substrate saturates every enzyme molecule, so
  $F_b \to 1$.
- **$E_{\text{total}} \to 0$ at fixed $S$.** This is the subtle one. Written as a population
  fraction, $[ES]/([E]+[ES])$ looks like $0/0$ as both go to zero together, and one honest answer
  is that the ratio is genuinely ill-defined without more care. But there is a cleaner way to see
  it: stop thinking about a population and imagine being the one enzyme molecule in the tube. You
  bind a substrate molecule at some rate set by $[S]$, stay bound for a while, and fall apart again
  at rate $k_r$. $F_b$ is then the *time-average* fraction of your own life spent bound — a
  perfectly well-defined quantity for a single molecule, and it settles at
  $$F_b = \frac{S}{K_d + S}.$$
  This is the limit in which one enzyme does not deplete the pool of substrate it swims in, so the
  free concentration $S$ in that formula is safely the same as $S_{\text{total}}$.
- **$E_{\text{total}} \to \infty$ at fixed $S_{\text{total}}$.** Now there is so much enzyme that
  essentially all of the substrate ends up bound — but that substrate is spread across an
  ever-growing enzyme population, so $F_b = [ES]/E_{\text{total}} \to S_{\text{total}}/E_{\text{total}} \to 0$.
  Almost every enzyme molecule is free simply because there are so many of them chasing a fixed
  amount of substrate.

Setting $d[ES]/dt = k_f[E][S] - k_r[ES] = 0$ gives, in one line, the same formula found above,
$$F_b = \frac{S}{K_d + S}.$$

This expression is easy to misread. The $S$ in it is the *free* substrate concentration, not
$S_{\text{total}}$ — and free $S$ itself is a function of $S_{\text{total}}$, $E_{\text{total}}$,
and $K_d$ together. Treating $S \approx S_{\text{total}}$ is only safe in the limit where enzyme is
scarce relative to substrate (the $E_{\text{total}} \to 0$ limit above), which is exactly the
regime in which real enzyme–substrate systems are usually studied — and is the reason the
Michaelis–Menten curve below has this same shape.

Plotting $F_b$ against $E_{\text{total}}$ at some fixed $S_{\text{total}}$ comparable to $K_d$ is a
good way to check this understanding: the curve starts at $1/2$ as $E_{\text{total}} \to 0$ (from
the third limit above, with $S \approx S_{\text{total}} \approx K_d$), falls monotonically, and
goes to $0$ as $E_{\text{total}} \to \infty$ (the fourth limit) — with $K_d$, the only
concentration scale in the problem, setting where the curve bends.

## From binding to catalysis: Michaelis–Menten kinetics

Add a third step to the scheme: the bound complex can also react forward, $ES \to E + P$, at rate
$k_{\text{cat}}$. From the standpoint of the enzyme, the complex $ES$ can now fall apart two ways —
back to $E + S$, or forward to $E + P$ — so its effective lifetime is shorter than before. The two
loss rates simply add, giving the Michaelis constant
$$K_m = \frac{k_r + k_{\text{cat}}}{k_f},$$
which plays exactly the role $K_d$ played above. The whole earlier discussion of fraction bound
carries over unchanged with $K_d$ replaced by $K_m$, and the reaction velocity (rate of product
formation) is
$$V = V_{\max}\,\frac{S}{K_m + S}, \qquad V_{\max} = k_{\text{cat}}[E]_{\text{total}},$$
valid, as before, once $[E]_{\text{total}}$ is small enough that $S \approx S_{\text{total}}$. Two
conditions have to hold for this steady-state formula to apply in practice: enough time must have
passed for the initial transient — building up the $ES$ pool from nothing — to have died away, but
not so much time that the substrate has been noticeably used up.

**A limitation worth stating precisely, not just noting.** As written, this scheme has no way back
from $P$ to $S$, so if it is allowed to run forever, all the substrate becomes product. That is not
just a detail missing from one particular model — it is a way of getting the physics of a catalyst
wrong in general. A catalyst does not change the equilibrium ratio between substrate and product;
it only speeds up the forward and reverse reactions equally. Drop invertase into a test tube of
sucrose and it will reach the same equilibrium between sucrose and its hydrolysis products that the
tube would reach on its own after being left for a million years — the enzyme just gets there many
orders of magnitude faster. The reason is thermodynamic: the enzyme itself is present, unchanged, on
both sides of the reaction (bound at the start, bound at the end), so from that standpoint it cannot
appear in the free-energy difference between substrate and product, and cannot shift where that
equilibrium sits. The one-way $E + S \to ES \to E + P$ scheme is therefore a good local
approximation while the reaction is far from its own equilibrium — which is usually the regime an
experiment is run in — but it is not a globally valid model of what an enzyme does.

## Reading a mechanism off $V_{\max}$ and $K_m$

Different inhibitors change the Michaelis–Menten curve differently, and this is the practical
payoff of having derived it carefully.

- An inhibitor $I$ that binds $E$ reversibly, forming an $EI$ complex that competes with $S$ for
  the enzyme, leaves $V_{\max}$ unchanged. At saturating substrate, there is enough $S$ to pull
  essentially every enzyme molecule away from $I$ and into $ES$ — you just need *more* substrate to
  get there than you would without the inhibitor. So this kind of inhibitor raises $K_m$ but does
  not touch $V_{\max}$.
- An inhibitor that instead binds the $ES$ complex itself, blocking it from turning over into
  product, does the opposite: it lowers $V_{\max}$ (some fraction of complexes are stuck, unable to
  react, no matter how much substrate is present) without changing $K_m$.

This is why titrating in a candidate inhibitor and measuring how it moves $V_{\max}$ and $K_m$ is a
standard way enzymologists diagnose which of these two mechanisms — competition for the enzyme, or
blocking of the catalytic step — a small molecule is actually using.

## Gene expression: separation of time scales and the dilution clock

Now consider a transcription factor $X$ that is activated by some signal into $X^*$, which binds a
promoter and drives expression of $Y$. Two of the steps here happen on very different time scales.
Activation of $X$ into $X^*$ — often something like an allosteric switch triggered by a small
molecule — can be extremely fast, well under a second; whatever is rate-limiting about the response
to an environmental change is usually getting the signal into the cell in the first place, not the
activation step itself. Equilibration of $X^*$ on the promoter is also fast on the time scale of
gene expression, though not quite as fast — more like seconds. Against those, transcription and
translation take minutes. So on the time scale that matters for $Y$, $X^*$ can be treated as
switching essentially instantaneously in response to the signal, and the real dynamics is all in
$Y$.

The dynamics is written
$$\dot Y = f(X^*) - \alpha Y,$$
where $\alpha$ is the sum of two physically distinct contributions: active degradation of the
protein, and dilution from cell growth. Even a protein that is never actively degraded still has
$\alpha > 0$, because a cell that is growing and dividing while holding its number of protein
copies fixed is diluting that protein's concentration. Real growth is not perfectly uniform across
the cell cycle, but averaged over it, a first-order dilution rate is a reasonable description.

If $f(X^*)$ switches on to a constant $\beta$ at $t = 0$, the solution approaches $Y \to \beta/\alpha$
with characteristic time $1/\alpha$, and the time to reach the halfway point is $T_{1/2} = \ln 2/\alpha$.
For a stable protein — no active degradation, $\alpha$ entirely from dilution — $T_{1/2}$ is exactly
the cell division time.

**The relaxation is symmetric.** If the signal is switched off again, $Y$ decays back down on the
*same* characteristic time $1/\alpha$ that it took to rise — not faster, not slower. That is not
obvious in advance, but it follows directly from $\dot Y = \beta - \alpha Y$ being linear: the same
$\alpha$ governs the approach to any target, whether that target is $\beta/\alpha$, $0$, or any
other constant.

One consequence: since $1/\alpha$ sets the response time in both directions, the only way to make
the circuit genuinely faster — on or off — is to increase $\alpha$, i.e., to actively degrade $Y$.
That has a cost. Holding the same steady-state level $\beta/\alpha$ while raising $\alpha$ requires
raising $\beta$ to match, which means synthesizing more protein to sustain the same concentration.
This cost is smaller for a protein that is kept at low copy number to begin with — which is
precisely how many transcription factors are expressed, since they only need to be present in
amounts sufficient to occupy binding sites, not to build cellular structure. That combination —
needing a fast response, and being cheap to overexpress — is a plausible reason active degradation
of transcription factors is common, while it would be far more costly for a structural protein made
in bulk.

## Ultrasensitivity: making a small input change into a large output change

A default input–output relationship, with a single $X$ monomer binding the promoter, has exactly
the same hyperbolic shape derived above:
$$\text{rate of } Y \text{ expression} = \beta\,\frac{X}{K_d + X}.$$
This is never ultrasensitive: doubling $X$ always produces *less* than a doubling in the response,
because the curve is already bending over. The ideal ultrasensitive response would instead be a
step — nothing until $X$ reaches some threshold, then all of $\beta$ at once.

### Cooperative binding steepens the curve

One way to approach the step is cooperative binding — dimerization or multimerization of the
transcription factor before or during promoter binding, or cooperative interactions among multiple
binding sites at the promoter. Such curves are commonly summarized with a Hill function,
$$\text{rate} = \beta\,\frac{X^n}{K^n + X^n},$$
where $K$ is still the point of half-maximal response, but $n > 1$ makes the transition around $K$
sharper. As $n$ increases the curve becomes progressively more step-like.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Hill functions of increasing cooperativity, n = 1, 2, 4, all sharing the same half-point but becoming progressively more step-like">
  <line x1="40" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="205" text-anchor="middle" font-size="12" fill="currentColor">X</text>
  <text x="18" y="30" text-anchor="middle" font-size="12" fill="currentColor">&#946;</text>
  <line x1="170" y1="180" x2="170" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3" opacity="0.5"/>
  <text x="170" y="195" text-anchor="middle" font-size="11" fill="currentColor">K</text>
  <polyline points="40.0,180.0 45.2,174.2 50.4,168.9 55.6,163.9 60.8,159.3 66.0,155.0 71.2,151.0 76.4,147.2 81.6,143.6 86.8,140.3 92.0,137.1 97.2,134.2 102.4,131.4 107.6,128.7 112.8,126.2 118.0,123.8 123.2,121.5 128.4,119.3 133.6,117.2 138.8,115.2 144.0,113.3 149.2,111.5 154.4,109.8 159.6,108.1 164.8,106.5 170.0,105.0 175.2,103.5 180.4,102.1 185.6,100.8 190.8,99.4 196.0,98.2 201.2,97.0 206.4,95.8 211.6,94.7 216.8,93.6 222.0,92.5 227.2,91.5 232.4,90.5 237.6,89.5 242.8,88.6 248.0,87.7 253.2,86.8 258.4,86.0 263.6,85.1 268.8,84.3 274.0,83.6 279.2,82.8 284.4,82.1 289.6,81.4 294.8,80.7 300.0,80.0" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.45"/>
  <polyline points="40.0,180.0 45.2,179.8 50.4,179.0 55.6,177.9 60.8,176.3 66.0,174.2 71.2,171.8 76.4,169.1 81.6,166.1 86.8,162.8 92.0,159.3 97.2,155.7 102.4,151.9 107.6,148.1 112.8,144.2 118.0,140.3 123.2,136.4 128.4,132.6 133.6,128.8 138.8,125.1 144.0,121.5 149.2,117.9 154.4,114.5 159.6,111.2 164.8,108.1 170.0,105.0 175.2,102.1 180.4,99.2 185.6,96.5 190.8,93.9 196.0,91.5 201.2,89.1 206.4,86.9 211.6,84.7 216.8,82.6 222.0,80.7 227.2,78.8 232.4,77.0 237.6,75.3 242.8,73.7 248.0,72.1 253.2,70.7 258.4,69.2 263.6,67.9 268.8,66.6 274.0,65.4 279.2,64.2 284.4,63.1 289.6,62.0 294.8,61.0 300.0,60.0" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.7"/>
  <polyline points="40.0,180.0 45.2,180.0 50.4,180.0 55.6,180.0 60.8,179.9 66.0,179.8 71.2,179.5 76.4,179.1 81.6,178.4 86.8,177.5 92.0,176.3 97.2,174.6 102.4,172.4 107.6,169.8 112.8,166.6 118.0,162.8 123.2,158.4 128.4,153.6 133.6,148.2 138.8,142.5 144.0,136.4 149.2,130.1 154.4,123.8 159.6,117.4 164.8,111.1 170.0,105.0 175.2,99.1 180.4,93.5 185.6,88.3 190.8,83.4 196.0,78.8 201.2,74.6 206.4,70.7 211.6,67.2 216.8,63.9 222.0,61.0 227.2,58.3 232.4,55.9 237.6,53.7 242.8,51.7 248.0,49.9 253.2,48.2 258.4,46.7 263.6,45.4 268.8,44.2 274.0,43.0 279.2,42.0 284.4,41.1 289.6,40.3 294.8,39.5 300.0,38.8" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="255" y="88" font-size="11" fill="currentColor">n=1</text>
  <text x="255" y="66" font-size="11" fill="currentColor">n=2</text>
  <text x="255" y="42" font-size="11" fill="currentColor">n=4</text>
</svg>
<figcaption>Hill functions with the same half-maximal point K but growing cooperativity n: the curve
does not move, it steepens, approaching the ideal step response as n increases.</figcaption>
</figure>

For many real genes, measured input–output curves are reasonably well described by such a curve
with $n$ somewhere between $1$ and $4$ — moderate cooperativity is common, extreme cooperativity is
not.

### Molecular titration: sliding the curve instead of steepening it

A second route to ultrasensitivity needs no cooperativity at all. Suppose $X$ still binds the
promoter to activate $Y$ with dissociation constant $K_d$, but there is also some other protein $W$
that binds $X$ reversibly, with dissociation constant $K_w$, forming an inert complex $XW$. $W$ acts
as a sponge or decoy: while $W$ is present in excess, most of $X$ is siphoned off into $XW$ and
essentially none is free to activate the promoter, so expression stays near zero. Only once
$X_{\text{total}}$ exceeds $W_{\text{total}}$ does free $X$ start to rise substantially, and
expression switches on. The effect on the curve is different in kind from cooperative binding — the
response does not steepen in place, the whole curve slides sideways so that essentially nothing
happens until $X_{\text{total}}$ passes $W_{\text{total}}$.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Molecular titration shifts the response threshold sideways to W total, rather than steepening it in place">
  <line x1="40" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="205" text-anchor="middle" font-size="12" fill="currentColor">X total</text>
  <text x="18" y="30" text-anchor="middle" font-size="12" fill="currentColor">&#946;</text>
  <line x1="230" y1="180" x2="230" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3" opacity="0.5"/>
  <text x="230" y="195" text-anchor="middle" font-size="11" fill="currentColor">W total</text>
  <polyline points="40.0,180.0 45.2,175.6 50.4,163.9 55.6,148.1 60.8,131.3 66.0,115.7 71.2,102.1 76.4,90.7 81.6,81.3 86.8,73.7 92.0,67.5 97.2,62.4 102.4,58.2 107.6,54.7 112.8,51.8 118.0,49.3 123.2,47.3 128.4,45.5 133.6,44.0 138.8,42.7 144.0,41.5 149.2,40.5 154.4,39.7 159.6,38.9 164.8,38.2 170.0,37.6 175.2,37.0 180.4,36.5 185.6,36.1 190.8,35.7 196.0,35.3 201.2,35.0 206.4,34.7 211.6,34.4 216.8,34.2 222.0,34.0 227.2,33.8 232.4,33.6 237.6,33.4 242.8,33.2 248.0,33.1 253.2,32.9 258.4,32.8 263.6,32.7 268.8,32.5 274.0,32.4 279.2,32.3 284.4,32.2 289.6,32.1 294.8,32.1 300.0,32.0" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.45"/>
  <polyline points="40.0,180.0 45.2,180.0 50.4,180.0 55.6,180.0 60.8,180.0 66.0,180.0 71.2,180.0 76.4,180.0 81.6,180.0 86.8,180.0 92.0,179.9 97.2,179.9 102.4,179.8 107.6,179.7 112.8,179.5 118.0,179.3 123.2,178.9 128.4,178.5 133.6,177.9 138.8,177.1 144.0,176.1 149.2,174.8 154.4,173.2 159.6,171.2 164.8,168.8 170.0,166.0 175.2,162.8 180.4,159.0 185.6,154.7 190.8,150.0 196.0,144.8 201.2,139.3 206.4,133.4 211.6,127.2 216.8,121.0 222.0,114.6 227.2,108.3 232.4,102.2 237.6,96.2 242.8,90.5 248.0,85.1 253.2,80.1 258.4,75.4 263.6,71.0 268.8,67.0 274.0,63.4 279.2,60.1 284.4,57.1 289.6,54.4 294.8,52.0 300.0,49.8" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="95" y="55" font-size="11" fill="currentColor">no W</text>
  <text x="240" y="120" font-size="11" fill="currentColor">with W</text>
</svg>
<figcaption>Without the titrating protein W, Y turns on near X = 0 (faint curve). With W present in
excess, expression is suppressed until X total exceeds W total, then rises — the response threshold
moves to sit at W total rather than the curve becoming steeper where it already was.</figcaption>
</figure>

This mechanism was motivated in the lecture by work from Nick Buchler, who helped work out how
molecular titration produces ultrasensitivity in this kind of setting. The precise relationship
required among $K_d$, $K_w$, and $W_{\text{total}}$ for the curve to behave this sharply was left
as the opening problem for the next lecture, rather than derived here.

## Exercises

These are the two questions the lecture itself raised and left open, rather than problems from a
separate problem set.

1. For the simple binding equilibrium $F_b = S/(K_d+S)$, work out $F_b$ exactly in the case
   $E_{\text{total}} = K_d$ (with, as usual, $S_{\text{total}}$ comparable to $K_d$ so the answer
   is not trivial). The lecture only guessed at the value ("around a third or a fifth") without
   computing it.
2. For the molecular titration scheme — $X$ binding the promoter with dissociation constant $K_d$,
   and binding a decoy protein $W$ with dissociation constant $K_w$ — determine what relationship
   between $K_d$, $K_w$, and $W_{\text{total}}$ is needed to get a genuinely ultrasensitive
   response (expression staying near zero until $X_{\text{total}}$ exceeds $W_{\text{total}}$, then
   rising sharply), as opposed to a gradual one.

## Sources

- Transcript of the lecture: `recordings/lly1u2aghiq.md`.
  - Binding equilibrium, units of $K_d$, and the four limits of $F_b$: 00:00–35:40.
  - Michaelis–Menten kinetics, $K_m$, and the thermodynamic limitation of the one-way scheme:
    35:40–48:00.
  - Competitive vs. catalytic-step inhibitors and reading mechanism off $V_{\max}$/$K_m$:
    48:00–57:28.
  - Separation of time scales, the dilution/degradation rate $\alpha$, and the symmetry of
    relaxation: 57:28–1:10:17.
  - Ultrasensitivity via cooperative (Hill) binding and via molecular titration: 1:10:17–1:17:34.
- This is a transcript-only source: whatever the lecturer drew on the board (the actual curves for
  $F_b$, the Michaelis–Menten plot, the Hill functions, the titration curve, and the time-course of
  $X$, $X^*$, and $Y$) was not captured. The shapes reconstructed here — the two figures above, and
  the qualitative descriptions elsewhere — follow only what was said about them out loud.
- Referred to but not supplied: Uri Alon's textbook (called "Uri's book" in the lecture, on the
  separation-of-time-scales argument for gene expression and on typical measured Hill coefficients
  in real promoters), and unpublished conversation with Nick Buchler on the mechanism of molecular
  titration. Homework on Michaelis–Menten kinetics and on inhibitor mechanisms was mentioned as
  upcoming but was not part of this task's inputs.

---

[← 16. Tipping Points and Species Competition](16-tipping-points-and-species-competition.md) · [Contents](index.md) · [18. Neutral Theory of Species Abundance →](18-neutral-theory-of-species-abundance.md)
