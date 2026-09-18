---
title: "12. Molecular Motors as Brownian Ratchets"
course: "MIT 8.592J"
chapter: 12
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 12. Molecular Motors as Brownian Ratchets

## What this covers

How does a molecular motor such as kinesin turn the chemical energy released by ATP hydrolysis into
directed mechanical motion, given that at its own scale the dominant force acting on it is random
thermal agitation? This chapter builds the minimal model that answers that question — the
*asymmetric hopping model* — and uses it to work out how fast the motor moves, how much force it
can generate, and why a purely passive ("equilibrium") ratchet could never do either. It assumes the
basic machinery of the course: master equations for a stochastic process, the continuum
(drift-diffusion) limit of a hopping process, detailed balance, and the Boltzmann distribution.

## Molecular motors and the ratchet problem

A *molecular motor* is a protein that converts chemical fuel — usually the hydrolysis of ATP to ADP
— into mechanical work: movement, transport of cargo, or packaging of material inside the cell.
*Myosin* walks along actin filaments, doing the work of muscle contraction; *kinesin* and *dynein*
walk along microtubules (MTs) in opposite directions, kinesin toward the microtubule's (+) end and
dynein toward its (−) end.

A macroscopic engine runs deterministically through its cycle. A molecular motor cannot: it is a
few nanometres across, immersed in water at room temperature, and is battered by thermal collisions
on exactly the same energy scale as the work it needs to do. Its operation is irreducibly
stochastic. Despite that, two features recur across essentially every such motor:

- **An asymmetry that sets the direction of travel.** For myosin this is the polarity of the actin
  filament; for kinesin and dynein it is built into which end of the microtubule each one walks
  toward.
- **A periodic, asymmetric potential along the track** — the motor's interaction with its track
  looks like a ratchet. But a *Brownian ratchet* — a particle sitting passively in a periodic
  asymmetric potential, agitated only by thermal noise — cannot extract net work from that noise: at
  thermal equilibrium there is no preferred direction, on pain of violating the second law. Getting
  net motion out of a ratchet potential requires an energy-consuming mechanism to rectify the
  fluctuations. The general scheme used by real motors is to give the motor several internal
  (chemical) states — e.g. bound to ATP, or to ADP and inorganic phosphate, or to ADP alone — each of
  which experiences a *different* ratchet potential. Cycling between internal states, driven by ATP
  hydrolysis, is what traps and rectifies the thermal fluctuations. That is the mechanism the rest
  of this chapter makes precise.

Before building the model, it is worth knowing the numbers involved. Kinesin's step size along a
microtubule is about $a \approx 8.2\text{ nm}$, and the free energy released by hydrolysing one ATP
molecule under physiological conditions is about $\Delta G_h = 12\,k_BT$. If that energy were used
with no loss whatsoever to produce a single mechanical step, the largest force the motor could
possibly generate would be

$$F_{\max} = \frac{\Delta G_h}{a} \approx 6.2\text{ pN}.$$

This is only a bound from energy conservation — it says nothing about the rates at which the motor
actually moves, and nothing about how much of $\Delta G_h$ is lost to dissipation. The rest of the
chapter is about computing the real velocity and the real force, and both come out below this bound.

## The asymmetric hopping model

Rather than track a particle in a continuous ratchet potential, the same physics is captured by a
much simpler *asymmetric hopping model*: the motor makes discrete jumps between sites spaced $a$
apart along its track, and at each site it can be in one of a small number of internal states. (A
motor with, say, four internal states per site — MT, MT+ATP, MT+ADP+P, MT+ADP — reproduces a full
chemical cycle; here we work through the simplest non-trivial version.)

Take two internal states, $T$ (motor bound to ATP) and $D$ (motor bound to ADP), at each site $n$.
Two kinds of transition are possible:

- an *internal* transition, in place at a fixed site, with rate $u$ ($D\to T$) or $d$ ($T\to D$);
- a *stepping* transition, which advances the motor by one site while also flipping its internal
  state, with rate $r$ (stepping right, $T\to D$) or $l$ (stepping left, $D\to T$).

<figure>
<svg viewBox="0 0 440 210" role="img" aria-label="Ladder diagram of the two-state asymmetric hopping model, showing a motor stepping between ATP-bound and ADP-bound states along its track">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 z" fill="currentColor"/>
    </marker>
  </defs>

  <text x="26" y="59" font-size="14" fill="currentColor">···</text>
  <text x="392" y="59" font-size="14" fill="currentColor">···</text>
  <text x="26" y="169" font-size="14" fill="currentColor">···</text>
  <text x="392" y="169" font-size="14" fill="currentColor">···</text>

  <text x="80" y="28" text-anchor="middle" font-size="12" fill="currentColor">n-1</text>
  <text x="220" y="28" text-anchor="middle" font-size="12" fill="currentColor">n</text>
  <text x="360" y="28" text-anchor="middle" font-size="12" fill="currentColor">n+1</text>

  <text x="12" y="59" font-size="12" fill="currentColor">T</text>
  <text x="12" y="169" font-size="12" fill="currentColor">D</text>

  <circle cx="80" cy="55" r="4" fill="currentColor"/>
  <circle cx="220" cy="55" r="4" fill="currentColor"/>
  <circle cx="360" cy="55" r="4" fill="currentColor"/>
  <circle cx="80" cy="165" r="4" fill="currentColor"/>
  <circle cx="220" cy="165" r="4" fill="currentColor"/>
  <circle cx="360" cy="165" r="4" fill="currentColor"/>

  <line x1="86" y1="60" x2="212" y2="160" stroke="currentColor" stroke-width="1" stroke-opacity="0.3" marker-end="url(#arrow)"/>
  <line x1="354" y1="160" x2="228" y2="60" stroke="currentColor" stroke-width="1" stroke-opacity="0.3" marker-end="url(#arrow)"/>

  <line x1="214" y1="63" x2="214" y2="157" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <line x1="226" y1="157" x2="226" y2="63" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <text x="196" y="115" text-anchor="middle" font-size="12" fill="currentColor">d</text>
  <text x="244" y="115" text-anchor="middle" font-size="12" fill="currentColor">u</text>

  <line x1="226" y1="60" x2="354" y2="160" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <text x="308" y="98" text-anchor="middle" font-size="12" fill="currentColor">r</text>

  <line x1="214" y1="160" x2="86" y2="60" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <text x="150" y="132" text-anchor="middle" font-size="12" fill="currentColor">l</text>

  <line x1="150" y1="195" x2="290" y2="195" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <text x="220" y="207" text-anchor="middle" font-size="11" fill="currentColor">net drift when ru &#62; ld</text>
</svg>
<figcaption>The two-state hopping model: at every site the motor flips in place between the
ATP-bound state $T$ and the ADP-bound state $D$ (rates $u$, $d$), or flips state while stepping one
site along the track (rate $r$ to the right, $l$ to the left). Faint diagonals show the same pattern
repeating at neighbouring sites. Detailed balance alone would make the two routes between $T$ and
$D$ thermodynamically equivalent; ATP hydrolysis breaks that equivalence and biases stepping to the
right.</figcaption>
</figure>

Writing $p_T(n,t)$ and $p_D(n,t)$ for the probability of being at site $n$ in state $T$ or $D$, the
transitions above give the master equations

$$\begin{aligned}
\frac{dp_D(n, t)}{dt} &= r\, p_T(n - 1) + d\, p_T(n) - (u + l)\, p_D(n) \\
\frac{dp_T(n, t)}{dt} &= l\, p_D(n + 1) + u\, p_D(n) - (d + r)\, p_T(n).
\end{aligned}$$

**Continuum limit.** If $p_T$ and $p_D$ vary slowly from one site to the next (on scales much larger
than $a$), each term like $p_T(n-1)$ can be Taylor-expanded in $a$: $p_T(n-1) \approx p_T(x) - a\,
\partial_x p_T + \tfrac{a^2}{2}\partial_x^2 p_T$. Doing this term by term turns the two master
equations into

$$\begin{aligned}
\frac{\partial p_D}{\partial t} &= (r + d)\,p_T - (u + l)\,p_D - a r\,\partial_x p_T + \tfrac{a^2 r}{2}\,\partial_x^2 p_T \\
\frac{\partial p_T}{\partial t} &= (l + u)\,p_D - (d + r)\,p_T + a l\,\partial_x p_D + \tfrac{a^2 l}{2}\,\partial_x^2 p_D.
\end{aligned}$$

**Reducing two fields to one.** The internal-state transitions ($u$, $d$) equilibrate locally much
faster than the motor moves along the track, so at each $x$ the ratio of $p_T$ to $p_D$ settles to
the value that makes the internal-transition terms cancel:

$$(r + d)\,p_T(x) = (u + l)\,p_D(x).$$

Writing $p(x) = p_T(x) + p_D(x)$ for the total probability of being at $x$ regardless of internal
state, this local-equilibrium condition fixes the split,

$$p_T(x) = \frac{u+l}{u+d+r+l}\,p(x), \qquad p_D(x) = \frac{d+r}{u+d+r+l}\,p(x).$$

Adding the two continuum equations and substituting these expressions collapses the pair to a single
*drift–diffusion equation* for $p(x,t)$ — the same equation that describes an ordinary diffusing
particle with a constant drift — with drift velocity

$$v = a\,\frac{ru - ld}{u+d+r+l},$$

and diffusion coefficient

$$D = \frac{a^2}{2}\,\frac{ru + ld + 2lr}{u+d+r+l}.$$

So a motor with four rates per site, on scales longer than a step, looks exactly like a particle
drifting at speed $v$ and diffusing with coefficient $D$ — the problem of "how does the motor move"
has been reduced to working out $v$ and $D$ from the microscopic rates.

## Detailed balance, and where the net motion comes from

The rates $u,d,r,l$ are not free: if the system were isolated, with no fuel supplied, it would have
to relax to thermal equilibrium, and that forces the forward and backward rate of every transition
into a fixed ratio set by the energy it crosses. Call $\Delta U_a$ the activation energy separating
the two internal states, and $\Delta U_s$ the energy difference for a step along the track. Detailed
balance then requires

$$\frac{u}{d} = e^{-\beta \Delta U_a}, \qquad \frac{l}{r} = e^{-\beta \Delta U_s}.$$

Substituting these into the drift velocity above gives

$$v = a\,\frac{lu}{u+d+r+l}\left(e^{\beta \Delta U_s} - e^{\beta \Delta U_a}\right).$$

There are two routes between the $T$ and $D$ states at a given point: the direct internal flip, and
the round trip of stepping out and stepping back. If no energy is being fed into the system, these
two routes must be thermodynamically equivalent — $\Delta U_a = \Delta U_s$ — and $v = 0$. That is
the precise statement of "a Brownian ratchet cannot extract work from thermal noise alone": however
asymmetric the potential looks, detailed balance forces the two energy differences to match and the
average velocity to vanish.

ATP hydrolysis is what breaks the equivalence. It supplies

$$\Delta U_s = \Delta U_a + \Delta G_h,$$

i.e. the route that also advances the motor releases the hydrolysis free energy in addition to
crossing the activation barrier. That extra energy tilts $e^{\beta \Delta U_s}$ above $e^{\beta
\Delta U_a}$, so $v > 0$: the motor moves to the right on average, fuelled by, and only by, the
chemical energy it consumes.

## Measuring the force of a Brownian motor

Knowing $v$ tells us how the motor moves but not how efficiently it converts $\Delta G_h$ into
mechanical work, which requires knowing the force it exerts over each step. That force cannot be
measured directly — there is no way to isolate every dissipative and frictional force acting on a
single protein — so two indirect procedures are used instead.

**The stall force.** Pull the motor backward with an optical tweezer, applying an external force
$F$ that the motor must now work against as it climbs the potential over each step. This shifts the
detailed-balance ratio for stepping to $r/l = e^{\beta(\Delta U_s - Fa)}$, and correspondingly the
velocity becomes

$$v = a\,\frac{lu}{u+d+r+l}\left(e^{\beta(\Delta U_a + \Delta G_h - Fa)} - e^{\beta \Delta U_a}\right).$$

The motor stalls, $v=0$, exactly when $F = F_s = \Delta G_h/a = F_{\max}$ — the same bound written
down informally at the start of the chapter. That is not a coincidence: a stalled motor is
stationary, so there is no dissipation to account for, and all of the free energy released by
hydrolysis goes into mechanical work against the external force.

**The Einstein force.** A second, independent estimate comes from the motor's own fluctuations
rather than from applying an external force at all. An ordinary Brownian particle in solution obeys
$v = \mu F$ for an applied force $F$, where $\mu$ is its mobility, and in the absence of any force it
diffuses with coefficient $D$; thermal equilibrium ties the two together through the *Einstein
relation*, $D = \mu k_BT$. Carrying the same relation over to the motor — using its own $v$ and $D$
from the hopping model, rather than those of a passive particle — defines an effective force

$$F_E = k_BT\,\frac{v}{D} = \frac{2k_BT}{a}\,\frac{ru - ld}{ru+ld+2lr} = \frac{2k_BT}{a}\,\frac{\frac{ru}{ld}-1}{\frac{ru}{ld}+1+2\frac{r}{d}}.$$

Since $ru/ld = e^{\beta \Delta G_h}$, this expression has two clean limits. Close to equilibrium
($\beta \Delta G_h \to 0$),

$$F_E \approx \frac{F_{\max}}{1 + r/d},$$

which is strictly less than $F_{\max}$ whenever there is any chance of stepping backward. Far from
equilibrium ($\beta \Delta G_h \gg 1$), $F_E \to 2k_BT/a$ — a force set purely by thermal energy and
step size, independent of how much free energy is actually available. In both limits $F_E <
F_{\max}$: the Einstein force, built from the motor's actual diffusion and drift, is always below
the naive bound from energy conservation alone, because thermal fluctuations dissipate part of
$\Delta G_h$ that the stall-force argument — with the motor held motionless throughout — never has
to spend.

## Sources

- Slides: `21-slides/01-introduction.md` (§3.2 Molecular Motors — motor examples, the ratchet
  argument, step size and $\Delta G_h$, the naive $F_{\max}$); `21-slides/02-3-2-1-asymmetric-hopping.md`
  (§3.2.1 — two-state hopping model, master equations (3.23), continuum limit (3.24), local
  equilibrium (3.25)–(3.26), drift and diffusion (3.27)–(3.28), detailed balance (3.29), velocity
  under hydrolysis (3.30)); `21-slides/03-3-2-2-force-of-a-brownian-motor.md` (§3.2.2 — stall force
  (3.31), Einstein relation and Einstein force (3.32)). All three are from MIT OCW 8.592J/HST.452J
  *Statistical Physics in Biology* (Spring 2011), CC BY-NC-SA.
- No transcript, notes, or exercises were supplied for this lecture; the chapter is built from the
  slides alone, so there is no "Exercises" section.
- The slides were reconstructed from a PDF with no text layer by a model, and their own header
  flags every equation as unverified — treat the equations reproduced here with the same caution,
  and check them against the original PDF before relying on them.
- The asymmetric hopping model is credited on the slides to M. E. Fisher and A. B. Kolomeisky,
  *PNAS* 96, 6597 (1999) — a paper the lecture cites but does not reproduce.

---

[← 11. Dynamic Instability of Microtubules](11-dynamic-instability-of-microtubules.md) · [Contents](index.md) · [13. Fixed Points and Hopfield Networks →](13-fixed-points-and-hopfield-networks.md)
