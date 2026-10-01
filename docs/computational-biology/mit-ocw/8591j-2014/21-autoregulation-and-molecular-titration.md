---
title: "21. Autoregulation and Molecular Titration"
course: "MIT 8.591J 2014"
chapter: 21
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 21. Autoregulation and Molecular Titration

## What this covers

This lecture answers two connected questions. First, a leftover from the previous class: besides
cooperative binding, what else can turn a graded input into a sharp, switch-like output — and
what does *molecular titration* (sequestering the input away with a decoy binding partner)
actually require of the binding affinities involved? Second, the bulk of the lecture: what does a
gene buy itself by regulating its own expression — the simplest possible network motif — and why
does negative autoregulation show up far more often in real transcription networks than positive
autoregulation does? It assumes you already have the basic kinetics of gene expression (a
production rate competing with a linear degradation/dilution rate), the Michaelis–Menten binding
curve, and the idea that cooperative binding sharpens a response (a Hill function).

## Two routes to an ultrasensitive response

Suppose $x$ activates $y$, and you would like the production rate of $y$, as a function of the
concentration of $x$, to look less like a gentle Michaelis–Menten curve and more like a digital
switch: essentially zero, then a sharp rise, then saturation at some maximal rate.

One way to get closer to that is **cooperativity**: if several copies of $x$ (say, a tetramer)
have to bind together to activate $y$, the response curve becomes steeper than the single-monomer
Michaelis–Menten curve — sharper, though not necessarily fully digital.

A second, independent route is **molecular titration**. Here $x$ does two things: it binds the
promoter of $y$ (activating expression, with dissociation constant $K_d$), and it also binds
reversibly to some other protein $w$, forming a complex $wx$ with dissociation constant $K_w$. The
protein $w$ acts as a decoy or "sponge" that soaks up $x$ before it ever reaches the promoter.

### Perfect sequestration

Take the idealized limit $K_w \to 0$: $w$ binds $x$ essentially irreversibly. As you slowly raise
the total amount of $x$ present, $x_T$, ask what the *free* (unbound) concentration of $x$ does.
While there is still free $w$ around, every new $x$ molecule you add gets grabbed by $w$
immediately, so free $x$ stays at zero. (The single promoter molecule binding a little of that $x$
is negligible against a pool of, say, a thousand copies of $w$ — it doesn't move the free-$x$
balance.) Once $x_T$ exceeds the total amount of $w$, $w_T$, there is no free $w$ left to grab
anything more, and every further increment of $x$ shows up directly as free $x$: free $x$ rises
with slope 1 in $x_T$.

The production rate of $y$ tracks the *free* $x$, not the total, through the ordinary
Michaelis–Menten form. So the production rate of $y$, plotted against $x_T$, stays at zero until
$x_T$ passes $w_T$, and only then rises — as a Michaelis–Menten curve in the free $x$ that has just
started to appear — reaching half its maximum when $x_T = w_T + K_d$.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Free x plotted against total x under strong sequestration: flat at zero, then a slope-one rise past the titration threshold">
  <line x1="40" y1="185" x2="310" y2="185" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="185" x2="40" y2="25" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="185" x2="160" y2="185" stroke="currentColor" stroke-width="2.5"/>
  <line x1="160" y1="185" x2="290" y2="50" stroke="currentColor" stroke-width="2.5"/>
  <line x1="160" y1="185" x2="160" y2="30" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="160" y="20" text-anchor="middle" font-size="12" fill="currentColor">w_T</text>
  <text x="300" y="205" text-anchor="middle" font-size="12" fill="currentColor">x_T</text>
  <text x="55" y="35" font-size="12" fill="currentColor">free x</text>
  <text x="220" y="95" font-size="12" fill="currentColor">slope 1</text>
</svg>
<figcaption>Strong sequestration: added x is absorbed by w until w is used up at $x_T = w_T$, then
free x rises one-for-one. The production rate of the target gene follows the same shape, but
softened into a Michaelis–Menten rise of width $K_d$ starting at $x_T \approx w_T$.</figcaption>
</figure>

### What the binding affinities need to satisfy

Real sequestration is never perfectly tight, so the class worked through what $K_d$, $K_w$ and
$w_T$ need to satisfy relative to each other for the switch to actually be sharp. Three conditions,
in the order the lecture built them up:

1. **$K_w \ll K_d$.** $x$ must bind the sequestering protein $w$ far more tightly than it binds the
   promoter, so that as $x$ is added it is captured by $w$ first, rather than leaking straight into
   activating $y$.
2. **$w_T \gg K_w$.** There has to be *enough* $w$, and it has to bind tightly, for the sponge to
   work well. In the sequestering regime ($x_T \ll w_T$), the free concentration of $x$ works out
   to approximately
   $$x_{\text{free}} \approx x_T \cdot \frac{K_w}{w_T},$$
   so free $x$ is suppressed by the factor $K_w/w_T$; you need $w_T/K_w \gg 1$ for that suppression
   to actually be strong. (This condition also follows logically from combining conditions 1 and
   3, though it is worth seeing directly: too little $w$ and the sponge saturates as soon as a
   little $x$ is added, and expression starts leaking on immediately.)
3. **$K_d \ll w_T$.** The width of the switching region in the production curve is set by $K_d$
   (it is a Michaelis–Menten rise of scale $K_d$), while the *location* of the switch is set by
   $w_T$. For the transition to look sharp — low, low, low, then up quickly — that width has to be
   small compared to where the switch happens.

A further condition is implicit: the cell has to be able to make *enough* $x$ to exceed $w_T$ in
the first place. If $w$ is so abundant that $x_T$ can never physically get past it, the curve is
ultrasensitive in principle but the switch is never reached.

**A trap worth recording explicitly.** Plotting free $x$ against $x_T$ on log–log axes, both
regimes — below and above $w_T$ — are straight lines of slope 1 (since free $x$ is linearly related
to $x_T$ in each regime; taking logs of a linear relationship changes only the intercept, not the
slope). It is tempting to look at "same slope in both regimes" and conclude nothing interesting is
happening. What actually carries the switch is the *vertical offset* between the two lines, i.e.
how much the sequestration suppresses free $x$ in the low regime relative to the high regime — a
feature invisible if you only compare slopes. The lesson generalizes: plot a result more than one
way before concluding what it shows.

## Autoregulation as a network motif

A gene that regulates its own expression is the simplest possible feedback loop in a regulatory
network, and often not even called a "motif" because it's so simple. There are two kinds:
**negative autoregulation**, where the protein represses its own expression, and **positive
autoregulation**, where it activates (upregulates) its own expression.

The question the lecture opens with is why this loop turns up so often. Take a transcription
network with $N$ genes (nodes) and $E$ regulatory interactions (directed edges, since regulation
has a direction). Counting all possible directed edges, including self-edges: you can start at any
of the $N$ nodes and end at any of the $N$ nodes, giving $N^2$ possible edges. (Equivalently: there
are $\tfrac12 N(N-1)$ unordered pairs of distinct nodes, each of which can carry an edge in either
direction — $N(N-1)$ — plus $N$ possible self-edges, and $N(N-1)+N = N^2$.)

The textbook's null model — referred to in the lecture only as "Uri's" — for asking whether a
motif is more common than chance is an **Erdős–Rényi random network**: place the same number of
edges $E$ uniformly at random among the $N^2$ possible slots, i.e. each possible edge is present
independently with probability $p = E/N^2$. Under that null model, the expected number of
self-edges is
$$N \cdot p = N \cdot \frac{E}{N^2} = \frac{E}{N}.$$

For the *E. coli* transcription network the lecture uses as an example — $N = 420$ genes, $E = 520$
edges — this predicts $E/N \approx 1.2$ expected self-loops, with a fluctuation of roughly
$\sqrt{1.2} \approx 1.1$ around it: you'd expect to see 0, 1, 2, maybe 3 autoregulatory genes by
chance. The actual count observed in that network was **40** — vastly more than the null model
predicts. That gap is what makes autoregulation a genuine network motif rather than a statistical
accident. Of those 40, the lecturer recalled (without having written it down, so treat this split
as approximate) something like 34 cases of negative autoregulation against 6 of positive — negative
autoregulation is the much stronger motif of the two.

A student pushed on whether Erdős–Rényi is the right null model at all, given that real
transcription networks have other structural constraints. The lecturer agreed this is a real issue
— he judged the autoregulation conclusion itself fairly insensitive to that choice, but flagged
that it becomes a much bigger issue for other motifs (the feed-forward loop, covered in a later
lecture not part of this transcript), where an Erdős–Rényi network turns out to be a poor
description of a real network altogether.

**On the logic of "it evolved for a reason" arguments.** A second exchange is worth recording
because it is about method, not mechanism. Finding that a motif occurs more than chance predicts
does not *prove* it was selected for; it is a hypothesis, and the value of a hypothesis is that it
tells you what to go measure. If you can point to a plausible advantage the motif confers, and then
go check experimentally whether that advantage actually shows up in real systems, you accumulate
evidence consistent with the evolutionary story — without ever strictly proving it, in the way
other fields prove things. That caveat governs everything that follows: the arguments below say
what negative and positive autoregulation *can do*, as candidate explanations for why they are so
common, not settled facts about why they evolved.

## Negative autoregulation I: it speeds turning on, not turning off

Some background needed to make sense of what follows, reviewed briefly in the lecture: for a gene
under **simple regulation** (no autoregulation, a signal simply switches expression on or off) with
a stable protein — one degraded only by dilution as the cell grows and divides, not by active
degradation — the time to reach half the distance between the old and new steady-state
concentration (call it the response time, $T_{1/2}$) is set purely by the cell's generation time.
That is true whether you're turning expression on, turning it off, or moving to any other target
level: with only dilution acting, the approach to any new value is a simple exponential relaxation
at the growth rate, regardless of direction or target. One way to speed this up is to add *active*
degradation — but that has a real cost: the cell has to keep manufacturing protein at a high rate
merely to keep chopping it back up, a futile cycle that speeds both turning on and turning off but
burns resources doing it.

Negative autoregulation offers a different route, without that cost. Model it with the crudest
possible "logic" approximation for autorepression: the production rate of $x$ is a step function of
$x$ itself — the maximal rate $\beta$ for $x$ below some repression threshold $K$, and zero once $x$
reaches $K$ — competing against a purely dilution-driven, linear loss $\alpha x$ (no active
degradation assumed). Because the production curve is flat at $\beta$ up to $K$ and then drops
straight to zero, and the degradation line $\alpha x$ crosses through exactly that drop (as long as
$\alpha K < \beta$), the system settles precisely at $x = K$: below $K$, production exceeds
degradation and $x$ climbs; above $K$, production is zero and dilution wins, pulling $x$ back down.

The gain in speed comes from being free to choose $\beta$ much larger than what simple regulation
would need for the same equilibrium — a strong promoter. With that large $\beta$, $x$ shoots up
quickly toward $K$; once it reaches $K$, autorepression turns expression off, right at the
equilibrium value, rather than only asymptotically approaching it from below the way an
unregulated gene would. **Turning on is faster than the timescale set by the cell generation
time.** And critically, this speedup costs nothing extra in protein made-and-discarded: because
there's no active degradation in this model, the amount of protein present at equilibrium is
exactly the same as it would be under simple regulation with the same target concentration — you
never overshoot and destroy the excess, you just get there faster by autorepressing right at the
target.

**Turning off is a different story.** Once a signal removes expression entirely, the only thing
removing existing protein is dilution — the same mechanism, at the same rate, as simple regulation.
Negative autoregulation contributes nothing extra here, because autorepression only matters while
the gene is still being transcribed; with expression already at zero, there's nothing left for
autorepression to act on. **So the response time goes down for turning on, and is unchanged for
turning off** — not both, and not neither, which is the answer that took the class several rounds
of discussion to converge on.

## Negative autoregulation II: the equilibrium concentration is robust

The second thing negative autoregulation buys is **robustness**: an equilibrium value that is
comparatively insensitive to *some* of the parameters governing it, even though it is not
insensitive to all of them. Robustness always needs a "robust to what" attached — here, robustness
of the equilibrium concentration $x_{eq}$ to small changes in the production rate $\beta$ and the
degradation/dilution rate $\alpha$.

Return to the logic-approximation picture: production is flat at $\beta$ up to the threshold $K$,
then drops to zero; degradation is the straight line $\alpha x$; equilibrium sits exactly at the
crossing, which — as long as the crossing stays on the vertical drop — is $x_{eq} = K$, independent
of $\alpha$ and $\beta$ individually.

- Changing $\alpha$ tilts the degradation line's slope, but the crossing point with the vertical
  drop at $K$ doesn't move — a small change in $\alpha$ produces (in this idealized limit) no
  change in $x_{eq}$, and for a real, smoothed-out version of the curve, less than a proportional
  change.
- Changing $\beta$ raises or lowers the flat part of the production curve, but again doesn't move
  where it crosses the drop at $K$ — no change in $x_{eq}$.
- Changing $K$ itself moves the crossing point one-to-one: a 10% change in $K$ is a 10% change in
  $x_{eq}$.

So the equilibrium concentration under negative autoregulation is robust to fluctuations in both
the production rate and the degradation/dilution rate — quantities that are affected by all sorts
of things going on in the cell, including the growth/division rate itself — but *not* robust to
changes in the repression threshold $K$, which is set by the binding kinetics of $x$ to its own
promoter (itself not perfectly insensitive to things like intracellular pH, but plausibly subject
to smaller swings than $\alpha$ or $\beta$ are).

This robustness is not unconditional: it only holds over some range of $\alpha$, $\beta$ and $K$ —
specifically the regime in which the degradation line still crosses the production curve on its
vertical drop rather than on its flat part. Push $K$ too high relative to $\beta/\alpha$ and the
robustness disappears. The lecture leaves the exact boundary of that range as an open question for
the reader to work out rather than deriving it in class.

Between the speed argument and the robustness argument, the lecturer was explicit that reasonable
people can disagree about which one matters more in a given case — likely both play a role to
varying degrees in different real circuits.

## Positive autoregulation: bistability and memory

Positive autoregulation trades away both of those advantages (it does not speed anything up and
does not confer this kind of robustness) but buys something qualitatively different: the
possibility of two distinct stable states at the same parameter values, which is the dynamical
basis for **memory**.

Model a gene that activates itself cooperatively:
$$\dot x = \beta_0 + \beta_1 \cdot (\text{cooperative self-activation of } x, \text{ Hill order } n)
\;-\; \alpha x,$$
with $n$ typically 2, 3 or 4. Plotted against $x$, the production side ($\beta_0$ plus the
sigmoidal, cooperative term) is an S-shaped curve, while the degradation side is the straight line
$\alpha x$. An S-curve and a straight line can cross up to three times. Where they cross defines
the fixed points of the system, and the stability of each is read off from which side has the
larger slope locally: at the two outer crossings, moving away from the fixed point brings you back
(production exceeds degradation just below, falls short just above, or the reverse) — **stable**;
at the middle crossing, a small departure grows — **unstable**. Three fixed points, two stable and
one unstable in between, is **bistability**.

Bistability becomes memory once you let a parameter — say $\alpha$, which tracks the cell's
division/growth rate — vary. Track the steady-state production rate as $\alpha$ is swept:

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Steady-state production rate against the degradation rate alpha, showing two stable branches joined by an unstable branch over a bistable window">
  <rect x="110" y="20" width="110" height="170" fill="currentColor" fill-opacity="0.15"/>
  <line x1="30" y1="190" x2="310" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="190" x2="30" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <path d="M30,45 L220,90" fill="none" stroke="currentColor" stroke-width="2.5"/>
  <path d="M220,90 L110,150" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5 4"/>
  <path d="M110,150 L310,175" fill="none" stroke="currentColor" stroke-width="2.5"/>
  <line x1="110" y1="190" x2="110" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="220" y1="190" x2="220" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="110" y="205" text-anchor="middle" font-size="12" fill="currentColor">alpha_1</text>
  <text x="220" y="205" text-anchor="middle" font-size="12" fill="currentColor">alpha_2</text>
  <text x="300" y="205" text-anchor="middle" font-size="12" fill="currentColor">alpha</text>
  <text x="165" y="35" text-anchor="middle" font-size="12" fill="currentColor">bistable</text>
</svg>
<figcaption>Solid curves are stable steady states, dashed is unstable. For alpha outside
[alpha_1, alpha_2] only one branch exists. Inside that window the same alpha admits two different
long-run states; which one the system occupies depends on where alpha has been before, not just
where it is now — that dependence on history is the memory.</figcaption>
</figure>

For large $\alpha$ (fast dilution), only the low branch survives, with steady-state production
approaching the basal rate $\beta_0$ alone — dilution outpaces even the fully activated
self-reinforcing term. For small $\alpha$, only the high branch survives, near the saturated rate
set by $\beta_0+\beta_1$. In between lies a window, $[\alpha_1, \alpha_2]$, where both a high and a
low branch are stable simultaneously, separated by the unstable branch. This whole picture — two
solid branches joined by a dashed one, folding back on itself at $\alpha_1$ and $\alpha_2$ — is
the bifurcation diagram for the system, and the folds are the points at which one of the stable
branches disappears.

**Memory works like this.** Suppose the cell currently sits at some "normal" $\alpha$ inside the
bistable window. Whether it's on the high branch or the low branch is a record of its past: it got
onto the high branch, for instance, by passing through a period of low $\alpha$ (which leaves only
the high branch available), and it will *stay* on the high branch even after $\alpha$ returns to
the normal, bistable value — because inside the window both branches are locally stable, so nothing
pushes it off the one it's already on. To reset the memory, you have to push $\alpha$ past a fold
(out of the bistable window entirely) and back, which forces the system onto the single surviving
branch and then lets it settle wherever that branch sits when bistability returns. In the (probably
unrealistic) limit of low noise, this is a genuine memory module: the same current parameter value,
two different states, depending on trajectory.

$\alpha$ itself is a slightly unnatural knob for this, since it's a *global* parameter that would
disturb every other process in the cell at the same time. The same bistable structure appears more
usefully as a function of some specific external small molecule — e.g. a sugar such as galactose in
the growth medium — acting as the input instead. A memory module built on a specific environmental
signal like that can retain a record of one particular past encounter independently of everything
else going on in the cell, which a shared global parameter like $\alpha$ cannot.

Finally, real cellular memory modules are often not literally one protein activating its own
promoter, but a small network doing the same job — most simply, a repressor repressing another
repressor, since two negations compose to a net positive feedback ("two negatives is a positive,
just like two lefts is a right").

## Closing thread

This lecture is meant as the first worked example of a theme that recurs through the course:
**robustness** as a design principle, with a "robust to what" that has to be stated explicitly
each time. Negative autoregulation's robustness of equilibrium concentration to production and
degradation rate is the cleanest version of the idea, because the thing that is robust and the
thing it's robust *against* are both simple and separate. A later application — perfect adaptation
in bacterial chemotaxis, not covered in this lecture — is more subtle precisely because there the
phenomenon being explained is itself a form of robustness, which the lecturer flagged as a reason
to make sure the concept is pinned down clearly here first.

## Sources

- Transcript: `recordings/sj7p2auoyla.md` (MIT OCW 8.591J, Systems Biology, Fall 2014), full
  lecture.
  - [00:00]–[19:25]: quick review of ultrasensitivity via cooperativity, then molecular titration —
    the perfect-sequestration limit, the resulting switch in the production rate of $y$.
  - [19:25]–[33:39]: the three conditions on $K_d$, $K_w$, $w_T$ for the titration switch to be
    sharp, the approximate free-$x$ formula, and the log–log slope trap.
  - [33:39]–[45:11]: autoregulation introduced as a network motif; the $N$/$E$/$N^2$ edge-counting
    argument, the Erdős–Rényi null model, the *E. coli* self-loop count (420 nodes, 520 edges,
    1.2 expected vs. 40 observed, ~34 negative/~6 positive recalled approximately), and the
    discussion of what an "it evolved for a reason" argument can and can't establish.
  - [45:11]–[57:02]: negative autoregulation and response time — the simple-regulation review
    (cell-generation-time response, the degradation-rate speed-up and its cost), the logic
    approximation for autorepression, and the on-time/off-time conclusion.
  - [57:02]–[1:07:02]: negative autoregulation and robustness of the equilibrium concentration.
  - [1:07:02]–[1:18:34]: positive autoregulation, the three-fixed-point/bistability argument, the
    bifurcation diagram in $\alpha$, memory, and the closing remarks tying back to robustness as a
    theme.
- **Referred to but not supplied:**
  - "Uri's book" and "his paper," cited repeatedly for the network-motif framework, the
    Erdős–Rényi null model, and the *E. coli* motif counts — almost certainly Uri Alon's textbook
    *An Introduction to Systems Biology: Design Principles of Biological Circuits* and the
    associated network-motif paper from the Alon lab, but neither is named precisely in the
    transcript and neither was supplied.
  - The assigned reading on autoregulation ("this is something... you guys just read about" /
    "did we read the chapter?"), presumably the corresponding chapter of the same book.
  - The prior lecture ("Tuesday"), which first introduced molecular titration and derived the
    cell-generation-time response-time result for simple regulation that this lecture builds on.
  - A forthcoming lecture on the feed-forward loop, where the choice of null model for network
    motifs is revisited in more depth.
  - A later topic, perfect adaptation in bacterial chemotaxis, referenced only as a forward pointer
    for where robustness reappears.
  - The problem set mentioned at the close of the lecture.
  - No slides, written notes or exercises were supplied for this lecture; everything on the board
    (the exact drawn curves, the classroom clicker-question wording) is not in the transcript and
    has been reconstructed here only as the mathematics and reasoning that were spoken aloud.

---

[← 20. Diffusion and Pattern Formation](20-diffusion-and-pattern-formation.md) · [Contents](index.md) · [22. Diffusion, Uptake, and Bacterial Chemotaxis →](22-diffusion-uptake-and-bacterial-chemotaxis.md)
