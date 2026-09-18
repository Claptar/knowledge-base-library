---
title: "23. Predator-Prey Cycles and Their Fragility"
course: "MIT 8.591J 2014"
chapter: 23
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 23. Predator-Prey Cycles and Their Fragility

## What this covers

This chapter asks why the standard textbook model of a predator and its prey — the Lotka–Volterra
equations — is, in a mathematical biologist's own words, "a bad model but profoundly important,"
and works through what that means in practice: which of its assumptions are doing the work, why its
oscillations are a fragile borderline case rather than a robust prediction, and what happens once
that fragility is repaired in two different directions. It then follows two places where a real
system's departure from the simple model turned out to be the interesting result rather than an
embarrassment: a laboratory rotifer–algae system whose cycles had the wrong period and the wrong
phase, and a demographic-noise effect that manufactures sustained oscillations out of a model that,
deterministically, has none. It assumes the reader can linearize a nonlinear system at a fixed
point and read stability off the Jacobian's eigenvalues, has met the chemical master equation as an
individual-based alternative to a differential equation, and knows the Poincaré–Bendixson theorem
by name.

## The Lotka–Volterra model and its four assumptions

The history, as told in lecture: in the mid-1920s the marine biologist Humberto D'Ancona had spent
about a decade (roughly 1912–1923) recording the composition of fish sold at markets across Italy.
He noticed that the fraction of *selachians* — sharks and shark-like, broadly predatory fish —
rose sharply during World War I and fell again afterward, and wanted a mechanistic explanation
rather than an appeal to "the general zeitgeist." He happened to be engaged to Luisa Volterra,
daughter of the mathematician Vito Volterra, and asked his future father-in-law about it. Volterra
wrote down a model and analyzed D'Ancona's data with it. Independently, Alfred Lotka had studied
essentially the same pair of equations some fifteen years earlier, first in the context of
autocatalytic chemical reactions and only later for population dynamics — hence the two names
attached to one model.

Writing $x$ for the prey and $y$ for the predator, the model is

$$\dot x = ax - bxy, \qquad \dot y = -cy + dxy,$$

with $a,b,c,d>0$. The lecture's own way of getting at what this equation actually says is to name
the assumptions that had to go in to write it down, rather than treat it as given:

1. **The interaction term is $xy$.** This is a *mass-action* assumption on the encounter rate
   between predator and prey, and it is worth keeping separate from "the population is well-mixed."
   A population can be spatially resolved — tracked as densities that vary with position, as in a
   reaction–diffusion or Turing-pattern model — and still have its *local* interaction rate written
   as $x(\mathbf{r})y(\mathbf{r})$ at each point. Conversely, being well-mixed does not by itself
   force the interaction term to be a product of the two densities. What is really being assumed
   here is that predator and prey encounter each other, and something happens, at a rate
   proportional to the product of their numbers or densities — nothing about saturation, and
   nothing about whether space is being tracked explicitly.
2. **The prey grows exponentially in the predator's absence** ($\dot x = ax$ when $y=0$). The rate
   $a$ is a *net* rate — births minus deaths — not a birth rate alone, so it is not quite right to
   say "the prey doesn't die without the predator"; only that its net growth rate is assumed
   positive.
3. **The predator dies exponentially in the prey's absence** ($\dot y = -cy$ when $x=0$), at rate
   $c$.
4. **Predation is one predator eating one prey at a time.** There is no group-hunting effect built
   in — nothing here would capture how a pack of wolves brings down a buffalo. This is bundled into
   the same $xy$ term as assumption 1, but it is a separate claim: assumption 1 is about how often
   predator and prey meet, this one is about what a single meeting does.

## Fixed points, and why "neutral" is a trap

The model has two fixed points. The origin is one, since $x$ appears in every term of the top
equation and $y$ in every term of the bottom one. Along the $y$-axis ($x=0$) the dynamics reduce to
$\dot y = -cy$, decaying to the origin — stable in that direction, since the predator dies out
without prey. Along the $x$-axis ($y=0$) the dynamics reduce to $\dot x = ax$, growing without
bound — unstable in that direction, since the prey grows freely without a predator. So the origin
is a saddle, with eigenvectors along the two axes.

The second, interior fixed point comes from solving $a-by=0$ and $-c+dx=0$ simultaneously:

$$x^* = \frac{c}{d}, \qquad y^* = \frac{a}{b}.$$

Linearizing about $(x^*,y^*)$ gives the Jacobian

$$J(x^*,y^*) = \begin{pmatrix} 0 & -bc/d \\ ad/b & 0 \end{pmatrix},$$

whose eigenvalues are $\lambda = \pm i\sqrt{ac}$ — purely imaginary. Near the fixed point this
looks like a *center*: trajectories trace closed loops rather than spiraling in or out, with an
approximate period $2\pi/\sqrt{ac}$. It is worth pausing on that period: it depends only on $a$ and
$c$, the two intrinsic growth/death rates, and not at all on $b$ or $d$, the two interaction rates —
which is not obvious just from staring at the equations.

But purely imaginary eigenvalues are a *borderline* case, and the lecture was explicit that this
matters: a linear analysis that returns a center at a nonlinear system's fixed point does **not**
by itself prove that the full nonlinear system actually has neutrally stable closed orbits away from
the fixed point. The nonlinear terms that the linearization threw away could just as easily turn the
picture into a stable spiral (orbits decaying to the fixed point) or a genuine limit cycle (orbits
converging onto one particular closed curve). For the Lotka–Volterra system specifically it happens
to be true that the orbits are neutrally stable — there is an exact quantity conserved along
trajectories, with a different value on each orbit, which is what pins every orbit in place rather
than letting nearby orbits drift into one another. That conservation law is left as an exercise
rather than derived in lecture. The orbits run counterclockwise around $(x^*,y^*)$, there are
infinitely many of them nested inside one another, and — a fact stated as something the reader
should be able to show, not proved in lecture — the time average of $x(t)$ and of $y(t)$ over one
circuit of *any* of these orbits comes out to exactly $x^*$ and $y^*$. That is what makes $x^*,y^*$
worth reasoning about even though the system, generically, never actually sits at that point.

## The paradox of hunting the predator, and D'Ancona's fish

Suppose a wildlife manager wants to help a struggling prey population by shooting the predator —
raising the predator's death rate, $c$. In this model that changes $x^* = c/d$ upward (more prey,
as intended) but leaves $y^* = a/b$ **completely unchanged**: the time-averaged predator population
is untouched by how hard you hunt it. And the effect on the prey is not permanent — stop hunting
and $c$ returns to its original value, and the prey population comes back down. A parallel case
raised in class: to reduce a predator population at equilibrium (framed, for fun, as thinning out
zombies) the model says you want to decrease $a$ — the predator's *supply* of new individuals via
$y^*=a/b$ — not increase the death rate $c$, which does nothing to $y^*$ at all. That inversion of
the naive intuition was offered with an explicit caution: it is worth checking whether a model's
assumptions are any good before turning it into public policy.

That fixed-point algebra is also Volterra's own explanation of D'Ancona's data. To first order, the
war's effect was not biological but economic: fewer fishermen went out. Less fishing removes fewer
prey fish, raising their net growth rate — $a$ goes up. Less fishing also removes fewer predator
fish, lowering their net death rate — $c$ goes down. By the formulas above, $y^*=a/b$ then rises
(more predatory fish) while $x^*=c/d$ falls (fewer prey fish) — exactly the shift D'Ancona saw in
the market data during the war. The class also raised, fairly, that this is not a controlled
experiment: an equally plausible story is that fishermen simply avoided the deeper waters where
predatory fish live, and confidence in the mechanistic story would really need many independent
"wars" to average over.

## Small changes, different endings

Because the neutral orbits sit on a nonhyperbolic borderline, almost any modification to the
model's assumptions can tip the outcome toward decay or toward a genuine, self-correcting cycle.
Two modifications from lecture:

**Logistic prey growth.** Replace $ax$ with $ax(1-x/K)$, leaving everything else the same:

$$\dot x = ax\left(1-\frac{x}{K}\right) - bxy, \qquad \dot y = -cy + dxy.$$

This looks like a modest, purely local repair of assumption 2 above (real prey populations
saturate, they don't grow to infinity), and for large $K$ the dynamics near the fixed point are
barely changed. But its effect on the long-run picture is not modest at all: the neutral orbits are
destroyed, and every trajectory now spirals into $(x^*,y^*)$ — damped oscillations rather than
sustained ones. The decay timescale grows as $K$ grows, and in the limit $K\to\infty$ that timescale
diverges, recovering the original neutrally stable orbits as a degenerate limiting case.

**Saturating predation.** Replace the linear $xy$ predation term with one that saturates in $x$
(a Michaelis–Menten-type functional response, so a predator's rate of eating doesn't grow without
limit as prey become abundant). With this change the interior fixed point becomes *unstable*, while
trajectories far from it are still driven inward — with no food at all, neither population can
sustain itself, so a large enough region of the $(x,y)$ plane has trajectories entering but none
leaving. The Poincaré–Bendixson theorem then applies: a bounded trapping region containing no fixed
point other than a single unstable one must contain at least one periodic orbit. That guarantees a
genuine limit cycle — a single closed orbit with its own characteristic amplitude and period,
attracting trajectories from both inside and outside.

A more general statement, named but not derived in lecture: writing a predator–prey pair through
its *per-capita* growth rates, $\dot x = x f(x,y)$ and $\dot y = y g(x,y)$, Kolmogorov gave a set of
four conditions on the partial derivatives of $f$ and $g$ with respect to $x$ and $y$ — holding at
least in certain limits — under which a stable limit cycle is guaranteed. The lecture pointed to
the assigned reading for the precise statement rather than stating it.

One question from the room was left open rather than answered: could the Poincaré–Bendixson
argument above be evaded by *semi-stable* limit cycles — orbits attracting from one side and
repelling from the other — nested so that trajectories are still trapped without any single orbit
being fully stable? The lecturer agreed the picture could apparently be drawn, noted that
semi-stable orbits are not robust to any amount of noise anyway (a real, noisy system only ever
"sees" the fully-stable cycles), but did not resolve on the spot whether this specific construction
is actually consistent with the usual statement of the theorem, and said he would check.

<figure>
<svg viewBox="0 0 480 200" role="img" aria-label="Three phase portraits sharing the same interior fixed point: nested neutral orbits, a spiral decaying to the fixed point, and a single stable limit cycle.">
  <defs>
    <marker id="arrowhead" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <!-- Panel A: unchanged Lotka-Volterra -->
  <g transform="translate(0,0)">
    <line x1="20" y1="170" x2="20" y2="20" stroke="currentColor" stroke-width="1" opacity="0.5"/>
    <line x1="20" y1="170" x2="140" y2="170" stroke="currentColor" stroke-width="1" opacity="0.5"/>
    <text x="10" y="15" font-size="11" fill="currentColor">y</text>
    <text x="142" y="182" font-size="11" fill="currentColor">x</text>
    <ellipse cx="80" cy="95" rx="18" ry="13" fill="none" stroke="currentColor" stroke-width="1.2"/>
    <ellipse cx="80" cy="95" rx="32" ry="23" fill="none" stroke="currentColor" stroke-width="1.2"/>
    <ellipse cx="80" cy="95" rx="46" ry="33" fill="none" stroke="currentColor" stroke-width="1.2"/>
    <circle cx="80" cy="95" r="2.5" fill="currentColor"/>
    <path d="M98,64 Q90,58 82,60" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrowhead)"/>
    <text x="80" y="195" text-anchor="middle" font-size="11" fill="currentColor">unchanged: neutral orbits</text>
  </g>

  <!-- Panel B: logistic prey growth -->
  <g transform="translate(165,0)">
    <line x1="20" y1="170" x2="20" y2="20" stroke="currentColor" stroke-width="1" opacity="0.5"/>
    <line x1="20" y1="170" x2="140" y2="170" stroke="currentColor" stroke-width="1" opacity="0.5"/>
    <ellipse cx="80" cy="95" rx="46" ry="33" fill="none" stroke="currentColor" stroke-width="1.1" stroke-dasharray="4 3"/>
    <ellipse cx="80" cy="95" rx="30" ry="21" fill="none" stroke="currentColor" stroke-width="1.2"/>
    <ellipse cx="80" cy="95" rx="14" ry="10" fill="none" stroke="currentColor" stroke-width="1.2"/>
    <circle cx="80" cy="95" r="2.5" fill="currentColor"/>
    <path d="M112,80 L98,86" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrowhead)"/>
    <text x="80" y="195" text-anchor="middle" font-size="11" fill="currentColor">+ logistic prey: damped spiral</text>
  </g>

  <!-- Panel C: saturating predation -->
  <g transform="translate(330,0)">
    <line x1="20" y1="170" x2="20" y2="20" stroke="currentColor" stroke-width="1" opacity="0.5"/>
    <line x1="20" y1="170" x2="140" y2="170" stroke="currentColor" stroke-width="1" opacity="0.5"/>
    <ellipse cx="80" cy="95" rx="46" ry="33" fill="none" stroke="currentColor" stroke-width="1.1" stroke-dasharray="4 3"/>
    <ellipse cx="80" cy="95" rx="30" ry="21" fill="none" stroke="currentColor" stroke-width="2"/>
    <circle cx="80" cy="95" r="2.5" fill="currentColor"/>
    <path d="M80,95 L92,89" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrowhead)"/>
    <path d="M120,76 L106,83" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrowhead)"/>
    <text x="80" y="195" text-anchor="middle" font-size="11" fill="currentColor">+ saturating predation: limit cycle</text>
  </g>
</svg>
<figcaption>Three outcomes of the same predator&#8211;prey skeleton, all sharing the interior fixed
point (the dot). Left: the bare Lotka&#8211;Volterra model, where every orbit is neutrally stable
and which one you are on depends only on where you started. Middle: adding a carrying capacity for
the prey turns every orbit into a spiral that decays onto the fixed point. Right: adding a
saturating (Michaelis&#8211;Menten) predation term makes the fixed point unstable and produces one
genuine limit cycle, attracting trajectories from both inside and outside.</figcaption>
</figure>

## Rapid evolution and long, out-of-phase cycles: the Yoshida experiments

The lecture turned next to a laboratory system where the simple model's failure was the interesting
result: Yoshida et al., "Rapid Evolution Drives Ecological Dynamics in a Predator-Prey System,"
*Nature* (2003), studying a rotifer feeding on algae in a chemostat.

An earlier paper from the same group had varied the chemostat's dilution rate and watched the
system cross a Hopf bifurcation: at low dilution, a stable coexistence fixed point; at intermediate
dilution, sustained oscillations; at high dilution, collapse of the predator–prey pair. That
matched a simple model reasonably well, with the dilution rate essentially setting $c$ (the rotifer
barely dies on its own, so its death rate is set by being washed out of the chemostat) and $a$ set
by the algal growth rate at that dilution minus the dilution rate itself.

Two features of the oscillations that this simple picture did not explain:

1. **Much longer period than predicted** — five to ten times longer than expected from the measured
   rates, which mattered practically, since it meant runs had to last around six months to see even
   a couple of cycles.
2. **The wrong phase.** Any two-variable differential-equation predator–prey model generically
   predicts the predator peaking a quarter-cycle (90°) after the prey — that is simply what going
   around a closed orbit in the $(x,y)$ plane near a spiral or center looks like. Experimentally the
   lag was often closer to 180°: predator and prey nearly anti-correlated rather than a quarter-cycle
   apart.

Follow-up modeling found that letting the prey population itself be heterogeneous — more than one
algal type present at once, differing in traits — reproduced both anomalies. The lecture was careful
about the word "evolution" here: what is meant is not new mutants arising and spreading over the
course of the experiment, which is what an experimental microbial-evolution researcher might expect
the word to imply, but a shift in the relative frequencies of prey variants that may already be
present — which is evolution by the textbook definition (a change in allele frequency over time)
even without new mutation on the timescale of a run. Ecologist and evolutionary biologist frame the
same mechanism differently — "ecological dynamics between fixed types" versus "evolution of a
variable population" — and which label is reached for is, in the lecturer's words, largely a matter
of taste.

Direct confirmation came from a controlled version of the experiment: starting from an isogenic
(clonal) prey population rather than a natural mixture made both anomalies disappear — the period
returned to what the measured rates predicted, and the phase lag returned to the generic 90°. That
is strong evidence that heterogeneity within the prey population, rather than some overlooked
physiological detail, was the cause.

A later paper from the same research program (an *Ecology Letters* paper from a few years before
this lecture) made the underlying trade-off concrete. Two algal types were tracked alongside the
rotifer: one divided rapidly but existed as free single cells; the other divided more slowly but
grew in clumps that were harder for the rotifer to eat. All three sub-populations — fast singles,
slow clumps, and rotifer — were followed simultaneously and shown to oscillate together, giving a
direct picture of the growth-versus-defense trade-off that the earlier modeling had only inferred.

## Demographic noise can manufacture oscillations

The closing topic, picked up in the following problem set, was guided by McKane and Newman,
*Physical Review Letters* (2005). Start from the model with logistic prey growth from earlier in
the chapter — deterministically, this has no sustained oscillations, only a spiral decaying to the
fixed point. Ask what happens once predators and prey are treated as discrete individuals, born,
dying and eating each other at random times, rather than as smooth continuous densities.

There are two different ways to introduce "noise" into this picture, with very different
consequences:

- **Add a noise term directly onto the differential equations** — for example a term proportional
  to $x$ tacked onto the $\dot x$ equation and one proportional to $y$ onto the $\dot y$ equation.
  This produces only a noisy version of the same spiral: a jittery path in toward the fixed point.
- **Start instead from an individual-based description** — a master equation, in the same style
  used earlier in the course for chemical reaction networks, in which birth, death and predation
  events happen stochastically to discrete individuals. Solved this way, the *same* underlying
  deterministic skeleton (a damped spiral) produces sustained, surprisingly large-amplitude
  oscillations that do not decay away.

The mechanism: demographic noise excites the system at every frequency, but the linearized
dynamics near the fixed point has one preferred frequency, set by the (now complex, decaying)
eigenvalues of the spiral. That frequency is selectively, resonantly amplified — what would
otherwise be a spiral collapsing onto the fixed point instead gets continually kicked back outward
at its own natural frequency, producing an oscillation that, over any short stretch, looks much
like a genuine limit cycle even though nothing in the deterministic equations calls for one.

Because the noise is demographic, its size relative to the mean population falls off like
$1/\sqrt{N}$ for a system of order $N$ individuals, so the effect is relatively weaker at larger
population sizes. But the lecture stressed that the absolute effect can still be surprisingly large
even for populations of order a thousand individuals — which is what the following problem set's
simulations were built to demonstrate. In passing, the lecture noted that the same demographic-noise
mechanism has since been used to produce noise-induced *pattern formation* in space, without giving
further detail.

## Sources

Transcript-only lecture: recording `wtesorg5h-a` (8.591J, Systems Biology, MIT OpenCourseWare),
timestamps [00:00]–[1:20:15]. No slides, notes or exercises were supplied with this lecture, and
nothing was written on a captured board — the phase portraits, the D'Ancona time-series sketch, and
the Jacobian matrix reproduced above are reconstructed from the spoken description and the algebra,
not from the original drawings.

- History, the four assumptions, the equations, fixed points, linearization and eigenvalues,
  hunting-the-predator, the zombie aside, and the World War I explanation: [03:21]–[49:30].
- Logistic prey growth, saturating predation, the Poincaré–Bendixson argument, the class's
  semi-stable-limit-cycle question, and Kolmogorov's conditions: [50:38]–[1:00:18].
- The Yoshida rotifer–algae experiments: [1:00:18]–[1:15:52].
- Noise-induced oscillations (McKane and Newman): [1:15:52]–[1:20:15].

Referred to in the lecture but not contained in this recording, and not supplied alongside it:

- Mark Kot, *Elements of Theoretical Ecology* — apparent source of the "bad model but profoundly
  important" framing, and presumably of the historical D'Ancona/Volterra/Lotka account as told.
- Yoshida, Jones, Ellner, Fussmann and Hairston, "Rapid Evolution Drives Ecological Dynamics in a
  Predator-Prey System," *Nature* (2003) — discussed at length, but its figures and full model are
  not shown here.
- The same group's earlier paper crossing a Hopf bifurcation in a chemostat predator–prey system,
  referred to only informally in the recording, without a full citation.
- A later *Ecology Letters* paper from the same research program tracking two algal morphotypes
  alongside the rotifer — exact citation not given in the recording.
- Kolmogorov's four conditions for a stable limit cycle in a general predator–prey system — named,
  not stated, with the assigned reading pointed to for the precise statement.
- McKane and Newman, *Physical Review Letters* (2005), on noise-induced oscillations in
  predator–prey systems, including the simulation plots the lecturer displayed but which are not
  captured in a transcript.
- The following problem set built on the McKane–Newman model, referred to repeatedly but not
  supplied with this lecture.

---

[← 22. Diffusion, Uptake, and Bacterial Chemotaxis](22-diffusion-uptake-and-bacterial-chemotaxis.md) · [Contents](index.md) · [24. Negative Autoregulation and the Repressilator →](24-negative-autoregulation-and-the-repressilator.md)
