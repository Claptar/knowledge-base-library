---
title: "12. Three Views of Stochastic Kinetics"
course: "MIT 8.591J 2014"
chapter: 12
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 12. Three Views of Stochastic Kinetics

## What this covers

A single chemical species obeying a birth–death master equation, and its Poisson steady state, is
assumed from the previous lecture. This chapter asks how to describe a system with **two** coupled
species — mRNA and the protein it makes — and then compares three ways of actually getting numbers
out of a stochastic model: solving the master equation for how a whole probability distribution
evolves, running individual stochastic trajectories with the Gillespie algorithm, and approximating
the discrete process by a diffusion (Fokker–Planck) equation when copy numbers are moderately
large. The organizing question throughout is: does a simple model of gene expression produce
**protein bursts**, and if so, in which of these three pictures do you actually see them?

## A two-species master equation

Take the simplest possible model of gene expression: mRNA is made at a constant rate and degraded
at a rate proportional to how much of it there is, and protein is made from mRNA (translation) and
degraded the same way:

$$\dot m = K_m - \gamma_m m, \qquad \dot n = K_p m - \gamma_p n,$$

where $m$ is the mRNA copy number and $n$ is the protein copy number. There is no feedback of any
kind — mRNA drives protein, and that's it.

To write the master equation for this you need a joint probability $P_{m,n}(t)$ for *every* pair
$(m,n)$: not one infinite family of equations but, in effect, an infinite number of infinite
families — "infinity times infinity," except it is still only countably infinite, so the equation
still makes sense. The recipe for building it is mechanical: draw the state $(m,n)$ and its four
neighbours, write the rate on every arrow leaving each state, and read off

$$\frac{dP_{m,n}}{dt} = \big[\text{rate in}\big] - \big[\text{rate out}\big].$$

Because mRNA numbers don't depend on protein numbers (there's no feedback), the rates in the
$m$-direction are exactly the single-species birth–death rates from before, unaffected by $n$: a
constant production rate $K_m$, and a degradation rate that scales with how much mRNA is currently
there. In the $n$-direction, translation happens at a rate set by *how much mRNA is around*
($K_p m$, unaffected by the current protein number), and protein degradation scales with $n$.

<figure>
<svg viewBox="0 0 460 380" role="img" aria-label="Transition diagram for the joint mRNA-protein master equation, showing the rate on every arrow between a state and its four neighbours">
  <defs>
    <marker id="arrM" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0,0 7,3 0,6" fill="currentColor"/>
    </marker>
  </defs>
  <!-- horizontal edges: center-right, center-left -->
  <line x1="248" y1="182" x2="392" y2="182" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrM)"/>
  <line x1="392" y1="198" x2="248" y2="198" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrM)"/>
  <line x1="212" y1="182" x2="88" y2="182" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrM)"/>
  <line x1="88" y1="198" x2="212" y2="198" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrM)"/>
  <!-- vertical edges: center-top, center-bottom -->
  <line x1="222" y1="178" x2="222" y2="52" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrM)"/>
  <line x1="238" y1="52" x2="238" y2="178" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrM)"/>
  <line x1="222" y1="202" x2="222" y2="328" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrM)"/>
  <line x1="238" y1="328" x2="238" y2="202" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrM)"/>
  <!-- nodes -->
  <circle cx="230" cy="190" r="4" fill="currentColor"/>
  <circle cx="400" cy="190" r="4" fill="currentColor"/>
  <circle cx="80" cy="190" r="4" fill="currentColor"/>
  <circle cx="230" cy="40" r="4" fill="currentColor"/>
  <circle cx="230" cy="340" r="4" fill="currentColor"/>
  <!-- node labels -->
  <text x="252" y="168" font-size="12" fill="currentColor">M, N</text>
  <text x="400" y="215" text-anchor="middle" font-size="12" fill="currentColor">M+1, N</text>
  <text x="80" y="215" text-anchor="middle" font-size="12" fill="currentColor">M-1, N</text>
  <text x="230" y="20" text-anchor="middle" font-size="12" fill="currentColor">M, N+1</text>
  <text x="230" y="362" text-anchor="middle" font-size="12" fill="currentColor">M, N-1</text>
  <!-- rate labels -->
  <text x="320" y="176" text-anchor="middle" font-size="11" fill="currentColor">K_m</text>
  <text x="320" y="211" text-anchor="middle" font-size="11" fill="currentColor">γ_m(M+1)</text>
  <text x="150" y="176" text-anchor="middle" font-size="11" fill="currentColor">γ_m M</text>
  <text x="150" y="211" text-anchor="middle" font-size="11" fill="currentColor">K_m</text>
  <text x="195" y="113" text-anchor="end" font-size="11" fill="currentColor">K_p M</text>
  <text x="245" y="113" text-anchor="start" font-size="11" fill="currentColor">γ_p(N+1)</text>
  <text x="195" y="268" text-anchor="end" font-size="11" fill="currentColor">γ_p N</text>
  <text x="245" y="268" text-anchor="start" font-size="11" fill="currentColor">K_p M</text>
</svg>
<figcaption>The local structure of the joint master equation: production rates (K_m, K_p M) are the
same on the way in as on the way out, but degradation rates depend on which state you are leaving —
γ_m(M+1) leaving M+1 is larger than γ_m M leaving M, which is exactly what keeps the chain from
drifting away.</figcaption>
</figure>

Reading the diagram off gives the balance equation for every state:

$$\frac{dP_{m,n}}{dt} = K_m P_{m-1,n} + \gamma_m(m+1)P_{m+1,n} + K_p m\, P_{m,n-1} + \gamma_p(n+1)P_{m,n+1} - \big[K_m + \gamma_m m + K_p m + \gamma_p n\big]P_{m,n}.$$

This is exactly the bookkeeping exercise it looks like: incoming arrows raise $P_{m,n}$, outgoing
arrows lower it, and every rate has to be multiplied by the probability of being in the state the
arrow leaves *from* — a system that starts with all its probability piled up somewhere else still
obeys this equation everywhere.

## Does this model have protein bursts?

Whether this pair of reactions produces protein bursts depends entirely on which of two pictures
you use to simulate it:

- Treated as the **deterministic** pair of ODEs above, no: both variables are smooth, continuous
  functions of time, and nothing "pops."
- Treated as a **stochastic** system and simulated exactly (Gillespie, below), yes: in the right
  parameter regime you see the protein number jump up in a burst and then decay back down.

The two pictures are not in conflict. The deterministic curve is what you get by averaging over
many stochastic trajectories — a well-behaved mean can hide dramatic behaviour in every individual
realization.

Bursts of this kind appear when translation is fast compared with mRNA turnover, $K_p \gg \gamma_m$.
In that regime, each mRNA molecule — before it happens to be degraded — triggers a burst of protein
production whose size is geometrically distributed (a race, repeated each "turn," between the fast
rate $K_p$ producing another protein and the slow rate $\gamma_m$ destroying the mRNA). Whether
those bursts are *large* relative to the steady-state protein level is a separate question, one
that also brings in $K_p$ and $\gamma_p$.

At steady state:

- the **mRNA** number is Poisson distributed (the single-species result from the previous lecture);
- the **protein** number, when bursts are significant, is Gamma distributed, with two parameters set
  by the underlying rates.

It is worth being careful here: knowing the shape of one marginal distribution does not tell you
the shape of another. A model whose protein number is Gamma distributed can have an mRNA number
that is Poisson distributed at the very same time — they are different representations of the same
underlying process, and there is no contradiction in that.

## What the master equation actually tells you

A useful check on your own understanding: if you specify an initial condition — say, $m_0$ mRNA and
$n_0$ protein at $t=0$ — and solve the master equation numerically out to some time $T$, you get a
number, $P_1$, for the probability of being in a particular state $(m,n)$ at time $T$. If you run
the exact same calculation again, do you get $P_1$ again?

Yes. The master equation is a (linear) set of *deterministic* differential equations for how a
probability distribution changes over time. The stochasticity of the underlying physical process is
built into the fact that these are probabilities at all — not into the calculation itself. Solve it
twice from the same initial condition and you get the same distribution both times.

This is the opposite situation from a Gillespie run, described below: there, a single trajectory
*is* a random object, and running the simulation again from the same initial condition gives a
different sample path. The two pictures are connected by a consistency check that is worth
remembering: histogram many independent Gillespie trajectories at a fixed time $T$, and the result
should converge to the same distribution the master equation gives you at that time. If it doesn't,
something in the simulation is wrong.

The master equation is just as valid away from steady state as at it — you can start from any
distribution over states, including one concentrated entirely on a single state, and it tells you
how that distribution evolves for all later time. Steady state is simply what you get if you let it
run forever; it is a special case, not the only thing the equation is good for.

## Truncating an infinite system in practice

The master equation is, in principle, an infinite set of coupled differential equations — one for
every state. In practice you can only ever simulate finitely many of them, and deciding how many is
a real, practical question.

Take the mRNA numbers alone, with $\gamma_m = 0.5\ \mathrm{min}^{-1}$ (a roughly two-minute mRNA
lifetime) and $K_m = 50\ \mathrm{min}^{-1}$. At steady state the mean is

$$\langle m \rangle = \frac{K_m}{\gamma_m} = \frac{50}{0.5} = 100,$$

and since the steady-state distribution is Poisson, the variance equals the mean, so the standard
deviation is $\sqrt{100}=10$. The distribution sits at $100 \pm 10$ or so, decaying fast on either
side, so going out to a few standard deviations — say $130$–$150$ — comfortably covers it.

But you also have to cover wherever you *start*. If the simulation begins at $m_0=50$, well below
the mean, that state needs an equation too, and so does everywhere the system passes through on the
way to steady state. The relaxation there is a biased random walk: starting below the mean, you are
roughly twice as likely to step up (towards $100$) as down at each move, so the walk is unlikely to
wander much below where it started. A range from about $35$ to $134$ — on the order of $100$ states
— was judged in the lecture to be generous enough for full credit on the corresponding problem-set
question.

In practice, once you've picked a finite range, you enforce it with **reflecting boundary
conditions**: at the top and bottom states of your truncated range, you simply drop the arrows that
would carry probability further out, so probability that would have left instead stays where it is.
This keeps the truncated distribution normalized (it always sums to $1$), at the cost of being
formally wrong right at the two boundary states. That's fine as long as the probability sitting at
those boundary states stays negligible — check it directly (is it below, say, $10^{-3}$ or
$10^{-4}$?) and extend the range if it isn't.

## The Gillespie algorithm

Rather than propagate a whole probability distribution, you can generate individual stochastic
trajectories directly. In general, suppose there are $m$ chemical species, packaged into a state
vector $X$ (numbers or concentrations of proteins, mRNAs, small molecules — anything), and $n$
possible reactions, each with a rate $r_i(X)$ that depends on the current state (a system with $50$
species and $300$ reactions is not exotic).

**The naive protocol.** Chop time into small steps $\Delta t$. At each step, ask whether reaction
$i$ fires, with probability $r_i \Delta t$ for each $i$ (small $\Delta t$ makes each waiting time
locally exponential, so this probability is accurate to leading order). If nothing fires, move on to
the next $\Delta t$; if something does, update the state. The problem is a genuine trade-off:
$\Delta t$ has to be small enough that it is *unlikely* anything happens in a given step (otherwise
you risk two reactions firing in the same step, which the algorithm can't represent), which means
most steps do nothing at all — computationally wasteful — and there is no way to make the
discretization error vanish without making the simulation arbitrarily slow.

**An exact but still slow alternative.** For each of the $n$ reaction channels, draw its own
waiting time $\tau_i$ from an exponential distribution with rate $r_i$, independently. Whichever
$\tau_i$ is smallest tells you which reaction fires first, and when; update the state and repeat.
This has no time discretization at all, so it is exact — but it costs $n$ independent random draws
per step, which is exactly the cost the naive method was trying to avoid, just moved somewhere else.

**The insight behind Gillespie's algorithm.** Ask for the probability that *none* of the $n$
reactions has occurred by time $t$. Since each reaction's waiting time is exponential and
independent of the others,

$$P(\text{no reaction by } t) = \prod_{i=1}^n e^{-r_i t} = \exp\Big(-t\sum_{i=1}^n r_i\Big).$$

This is itself an exponential decay, with rate equal to the *sum* of all the individual rates,
$R \equiv \sum_i r_i$. However different the individual $r_i$ are — some fast, some orders of
magnitude slower — the time to the very first reaction of any kind is exponentially distributed
with rate $R$. That single fact is the whole trick: it means you never need to draw $n$ separate
waiting times and take the minimum. You can draw one waiting time from the combined rate, directly.

**The algorithm.** At each step:

1. Compute the current rates $r_i(X)$ and their sum $R$.
2. Draw a single waiting time $\tau \sim \mathrm{Exp}(R)$ — this is when the next reaction happens.
3. Decide *which* reaction it was by drawing from the discrete distribution $p_i = r_i/R$ (a
   reaction with a larger rate contributes proportionally more of $R$, and so is proportionally more
   likely to be the one selected).
4. Update the state by that reaction's effect, advance the clock by $\tau$, recompute the rates, and
   repeat.

Two random draws per step — one exponential, one categorical — no matter how many reaction channels
there are. It is exact, in the sense that there is no discretization of time anywhere, provided the
rates themselves are an accurate description of the system. One practical wrinkle: the resulting
event times are not evenly spaced, so plotting or analysing the output has to keep track of the
actual (irregular) times, not just a step count.

A remark on what "sample from an exponential" means concretely: the exponential density is
$p(\tau) = r\, e^{-r\tau}$ — the leading factor of $r$ is needed for $p(\tau)$ to have units of
inverse time, so that $p(\tau)\,d\tau$ is a genuine dimensionless probability. Computationally, this
is generated from a uniform random variable by a change of variables (an exercise left for the
problem set, not carried out here). One thing worth noticing: the *most likely* single value to draw
is $\tau = 0$, where the density is largest, even though the *mean* waiting time is $1/r$ — a
reminder that "most probable outcome" and "typical/average outcome" are different questions once a
distribution is skewed.

## Where the burst actually comes from, mechanically

Every single reaction event in an exact Gillespie simulation changes exactly one species by exactly
$\pm 1$. So a literal jump of more than one protein in a single step of the algorithm never happens.
The "burst" seen in a plot of $n(t)$ is not one such jump; it is a rapid sequence of many individual
$+1$ translation events, fired back-to-back while one mRNA molecule happens to still be alive —
because with $K_p \gg \gamma_m$, that mRNA is far more likely to trigger *another* translation event
than to be degraded on any given turn. Once the mRNA is finally degraded, the proteins it produced
are removed only one at a time, at the comparatively slow rate $\gamma_p n$.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="A protein-number trajectory showing a fast staircase rise while one mRNA molecule is alive, followed by a slow staircase decline after it is degraded">
  <line x1="30" y1="170" x2="320" y2="170" stroke="currentColor" stroke-width="1.3"/>
  <line x1="30" y1="170" x2="30" y2="20" stroke="currentColor" stroke-width="1.3"/>
  <text x="320" y="185" text-anchor="end" font-size="12" fill="currentColor">t</text>
  <text x="14" y="30" font-size="12" fill="currentColor">n</text>
  <polyline points="30,155 90,155 90,140 98,140 98,120 106,120 106,105 114,105 114,90 122,90 122,75 130,75 130,60 138,60 138,45 175,45 175,60 215,60 215,80 255,80 255,105 300,105 300,130 320,130" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <text x="112" y="38" text-anchor="middle" font-size="11" fill="currentColor">burst: mRNA alive, many fast +1 steps</text>
  <text x="245" y="120" text-anchor="middle" font-size="11" fill="currentColor">decay: mRNA gone, slow −1 steps</text>
</svg>
<figcaption>A single protein burst as a Gillespie trajectory actually produces it: a fast staircase
of individual +1 translation events while the triggering mRNA molecule survives, then a much slower
staircase of individual −1 degradation events after it is gone.</figcaption>
</figure>

## The Fokker–Planck approximation

The third picture is useful when the copy number is large enough that you don't need to track every
discrete molecule, but not so large that fluctuations can be ignored altogether — an intermediate
regime. There, the birth–death process can be approximated by a continuous diffusion equation, and
its steady state written in a Boltzmann-like form. For a single species with production rate $f(n)$
and degradation rate $g(n)$ (so $\dot n = f(n)-g(n)$ deterministically),

$$P(n) \propto \frac{1}{f(n)+g(n)}\, e^{-\phi(n)}, \qquad \phi(n) = -\int^n \frac{f(n')-g(n')}{f(n')+g(n')}\, dn'.$$

$\phi(n)$ is an **effective potential**: probability concentrates where $\phi$ is small, exactly as
a Boltzmann factor concentrates probability at low potential energy, and it dominates the shape of
$P(n)$ because it sits in the exponent — the prefactor $1/(f+g)$ is a much weaker correction.

This works cleanly in one dimension. Once there are two coupled species (mRNA and protein together)
there is no guarantee you can still write the steady state as a gradient of a single scalar
potential — you would need something like a vector potential, and the physical intuition built for
a simple potential well doesn't transfer cleanly once you have the equivalent of magnetic-field-like
cross terms mixing the two directions.

**Why the well is quadratic near steady state.** At the steady state $n^*$, production and
degradation balance by definition, $f(n^*)=g(n^*)$, so $f-g$ vanishes there. Any smooth function
looks linear close to a point where it's smooth, so near $n^*$, $f(n)-g(n)$ grows approximately
linearly in $(n-n^*)$ — true even if $f$ and $g$ are not linear functions globally. Integrating
something that grows linearly gives something that grows quadratically, so $\phi(n)$ is
approximately a quadratic well near the steady state: $P(n)$ is approximately Gaussian there, as
you'd expect once numbers are large enough for the discreteness to wash out.

**Same mean, different noise.** The lecture worked through three cases, all sharing the same
steady-state mean but built from differently-shaped $f$ and $g$, to make the point that the location
of the crossing and the amount of spread around it are two separate questions.

<figure>
<svg viewBox="0 0 380 240" role="img" aria-label="Production and degradation rate curves for two cases sharing the same crossing point but different heights there">
  <line x1="40" y1="200" x2="340" y2="200" stroke="currentColor" stroke-width="1.3"/>
  <line x1="40" y1="200" x2="40" y2="20" stroke="currentColor" stroke-width="1.3"/>
  <text x="340" y="215" text-anchor="end" font-size="12" fill="currentColor">n</text>
  <text x="20" y="28" font-size="12" fill="currentColor">rate</text>
  <!-- case A: f = k constant, g = gamma n -->
  <line x1="40" y1="60" x2="340" y2="60" stroke="currentColor" stroke-width="1.4"/>
  <line x1="40" y1="200" x2="220" y2="60" stroke="currentColor" stroke-width="1.4"/>
  <!-- case B: f = k - 0.5 gamma n, g = 0.5 gamma n, dashed -->
  <line x1="40" y1="60" x2="220" y2="130" stroke="currentColor" stroke-width="1.4" stroke-dasharray="5 4"/>
  <line x1="40" y1="200" x2="220" y2="130" stroke="currentColor" stroke-width="1.4" stroke-dasharray="5 4"/>
  <!-- crossing marker -->
  <line x1="220" y1="20" x2="220" y2="200" stroke="currentColor" stroke-width="1" stroke-dasharray="2 3" opacity="0.5"/>
  <text x="220" y="215" text-anchor="middle" font-size="12" fill="currentColor">n*</text>
  <text x="345" y="63" font-size="11" fill="currentColor">f_A = k</text>
  <text x="345" y="50" font-size="11" fill="currentColor">(solid)</text>
  <text x="230" y="60" font-size="11" fill="currentColor">2k</text>
  <text x="230" y="133" font-size="11" fill="currentColor">k</text>
  <text x="112" y="150" text-anchor="middle" font-size="11" fill="currentColor">g_A = γn (solid)</text>
  <text x="70" y="115" text-anchor="middle" font-size="11" fill="currentColor">f_B, g_B (dashed)</text>
</svg>
<figcaption>Two pairs of rate curves crossing at the same mean n*, but at different heights: the sum
f+g there — 2k in the solid case, k in the dashed case — sets how steep the effective potential well
is, not the location of the crossing.</figcaption>
</figure>

| Case | $f(n)$ | $g(n)$ | $f+g$ at $n^*$ | Steady state | $\mathrm{Var}/\mathrm{Mean}$ |
|---|---|---|---|---|---|
| A — unregulated expression | $k$ (constant) | $\gamma n$ | $2k$ | Poisson | $1$ |
| B — same mean, curves pulled down together | $k - \tfrac12\gamma n$ | $\tfrac12\gamma n$ | $k$ | narrower Gaussian-like | $1/2$ |
| C — pushed to the extreme | $\to 0$ at $n^*$ | $\to 0$ at $n^*$ | $\to 0$ | essentially a spike at $n^*$ | $\to 0$ |

In case A, $f-g$ and $f+g$ combine to give exactly the Poisson result already known from the master
equation. In case B, the crossing point — and so the mean — hasn't moved, but $f+g$ at that point is
half what it was, while $f-g$ still grows at the same rate moving away from $n^*$; that makes the
effective potential steeper (a narrower well), and the variance-to-mean ratio drops to $1/2$. Pushed
to the limit in case C — very slow production and very slow degradation, still balanced at the same
$n^*$ — the ratio goes to $0$: the system climbs to $n^*$ and then essentially sits there, because
there is no longer any birth–death "noise" being injected once it arrives. (These three ratios were
given in the lecture as the qualitative payoff of the effective-potential picture; the integral
itself was left as something to work through, not carried out in class.)

The moral drawn from this: knowing that production and degradation rates are equal only tells you
*where* the steady state sits. It says nothing on its own about how much the system fluctuates
around it — that depends on how large $f$ and $g$ themselves are at that point, not merely on the
fact that they're equal there.

## Sources

- MIT 8.591J *Systems Biology* (OCW, Fall 2014), lecture recording `exbo08-78iu` (transcript only;
  everything drawn on the board — the transition-diagram sketch, the $f(n)$/$g(n)$ curve sketches —
  is not captured in the source and is reconstructed here from the spoken description; timestamps
  run from the start of the recording to about 1:21:30).
- Administrative content (a midterm-scheduling reminder) and the standard OCW donation notice are
  stripped.
- Referred to in the lecture but not supplied as source material for this chapter:
  - the previous lecture ("last time"/Thursday's class), which derived the single-species
    birth–death master equation and its Poisson steady state, assumed throughout here;
  - the assigned reading for this lecture, which the professor says works through the Fokker–Planck
    derivation in more detail than was given in class ("the notes do go over it");
  - a paper on protein bursts observed in single E. coli cells, referred to in class only as
    "Sunny's paper," which motivated the opening question about whether this model should show
    bursts;
  - a problem-set exercise on transforming a uniform random variable into an exponentially
    distributed one, referenced as the technique behind "sampling from an exponential" but not
    worked out in the lecture.

---

[← 11. Clonal Interference and Fitness Landscapes](11-clonal-interference-and-fitness-landscapes.md) · [Contents](index.md) · [13. From Genes to Ecosystems →](13-from-genes-to-ecosystems.md)
