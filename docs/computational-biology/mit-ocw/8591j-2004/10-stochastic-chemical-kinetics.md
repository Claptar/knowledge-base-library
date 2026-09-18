---
title: "10. Stochastic Chemical Kinetics"
course: "MIT 8.591J 2004"
chapter: 10
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. Stochastic Chemical Kinetics

## What this covers

How should we describe a chemical reaction network when some of the reacting species are present
in only tens or hundreds of copies — too few for the deterministic rate equations of ordinary
chemical kinetics to be trusted? This chapter builds the probabilistic description from scratch:
the master equation that replaces a rate equation for discrete molecule counts, the two limits in
which it reduces to something familiar (the deterministic law for the mean, and a diffusion-like
Fokker–Planck equation for large-but-not-infinite numbers), and the simulation algorithm and
switching-time calculation that the master equation makes possible. It assumes the reader is
comfortable with ordinary first-order chemical kinetics ($dn/dt = k-\gamma n$), with means and
variances, and with solving simple ODEs.

## Why molecule number cannot be treated as continuous

Take the simplest possible reaction network: a molecule $X$ is created at a constant rate $k$ and
destroyed by a first-order reaction with rate $\gamma$. If the number of molecules $n$ is
enormous — Avogadro's number, about $10^{24}$, is the usual scale in a beaker — it costs nothing to
pretend $n$ is a continuous variable and write the ordinary rate equation

$$\frac{dn}{dt} = k - \gamma n \equiv f_n - g_n,$$

where $f_n = k$ is the creation rate and $g_n = \gamma n$ the destruction rate when there are $n$
molecules present.

Inside a living cell this approximation is far less innocent: a typical protein is present in
thousands of copies, a ribosome or an RNA polymerase in hundreds, an mRNA species in tens, and most
genes in one or two copies. So take discreteness seriously and ask what the *exact* trajectory
$n(t)$ looks like.

One tempting guess is that $n(t)$ still moves smoothly through the integers, with a creation event
exactly every $\Delta t = \Delta n/(k-\gamma n)$ for $\Delta n = 1$ — a "clockwork" version of the
same curve. This is not physically possible: it would require the system to keep track of the time
elapsed since the last event, the way a clock counts ticks, but there is no clock here, only
molecules colliding with each other. The system's future can depend only on its present state,
never on how it got there. (No memory of the past beyond the present state is the defining property
of a **Markov process**.)

What a memoryless system *can* do is have each possible reaction occur with some probability per
unit time, proportional to its rate. Run the same experiment twice from the same initial condition
and the two trajectories $n(t)$ will differ — the system is genuinely **stochastic**. Run it many
times and record $n$ at some fixed time, and the outcomes form a distribution rather than a single
value. The rest of the chapter is about that distribution.

## The master equation

### From a rate to a probability

If a given reaction fires at rate $r$, then over a long stretch of time $T$ it fires on average
$rT$ times. Split $T$ into $N$ equal slivers of length $dt = T/N$; the chance the reaction happens
in any one particular sliver is $rT/N = r\,dt$. So in the limit of small $dt$: the probability that
a reaction with rate $r$ occurs in a time interval $dt$ is $r\,dt$, and the chance of two
occurrences within the same sliver is negligible.

### Setting up an ensemble

Imagine many identical copies of the system, all started from the same initial condition, and let
$p_n(t)$ be the fraction of them that have exactly $n$ molecules of $X$ at time $t$. Four things
can change $p_n$ in a small interval $dt$:

- a system with $n-1$ molecules gains one, at rate $f_{n-1}$ — moving *into* the $n$-population;
- a system with $n+1$ molecules loses one, at rate $g_{n+1}$ — moving *into* the $n$-population;
- a system with $n$ molecules gains one, at rate $f_n$ — moving *out of* the $n$-population;
- a system with $n$ molecules loses one, at rate $g_n$ — moving *out of* the $n$-population.

<figure>
<svg viewBox="0 0 340 170" role="img" aria-label="Three neighboring molecule-count states linked by birth rates f and death rates g">
  <defs>
    <marker id="me-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="60" cy="90" r="24" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="170" cy="90" r="24" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="280" cy="90" r="24" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="60" y="94" text-anchor="middle" font-size="12" fill="currentColor">n-1</text>
  <text x="170" y="94" text-anchor="middle" font-size="12" fill="currentColor">n</text>
  <text x="280" y="94" text-anchor="middle" font-size="12" fill="currentColor">n+1</text>
  <path d="M82,76 Q115,45 148,76" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#me-arrow)"/>
  <path d="M192,76 Q225,45 258,76" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#me-arrow)"/>
  <path d="M148,104 Q115,135 82,104" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#me-arrow)"/>
  <path d="M258,104 Q225,135 192,104" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#me-arrow)"/>
  <text x="115" y="38" text-anchor="middle" font-size="12" fill="currentColor">f(n-1)</text>
  <text x="225" y="38" text-anchor="middle" font-size="12" fill="currentColor">f(n)</text>
  <text x="115" y="154" text-anchor="middle" font-size="12" fill="currentColor">g(n)</text>
  <text x="225" y="154" text-anchor="middle" font-size="12" fill="currentColor">g(n+1)</text>
</svg>
<figcaption>Probability flows between neighboring molecule-count states: creation carries it forward
along the top arrows, destruction carries it back along the bottom arrows.</figcaption>
</figure>

Collecting all four fluxes gives the **master equation**:

$$\frac{dp_n}{dt} = -(f_n+g_n)\,p_n + f_{n-1}\,p_{n-1} + g_{n+1}\,p_{n+1}.$$

This is really an infinite family of coupled linear ODEs, one for every $n = 0,1,2,\dots$. Because
it is linear, it does not matter whether $p_n$ is a raw count of systems or a normalized
probability with $\sum_n p_n = 1$ — the second reading is the useful one: $p_n(t)$ is the
probability that a given system has exactly $n$ molecules at time $t$. Concretely, the ensemble
could be a population of cells and $p_n$ the fraction of cells carrying $n$ copies of some protein.

## The deterministic limit reappears in the mean

The master equation looks like a step backward — instead of one ODE for $n(t)$ there are now
infinitely many, for the whole distribution $p_n(t)$. But its moments can be extracted without ever
solving it. Take the mean number of molecules,

$$\langle n \rangle = \sum_n n\,p_n,$$

differentiate, substitute the master equation, and reindex the sums (using
$\sum_n h(n) = \sum_n h(n\pm1)$, valid whenever the sum runs over all integers). With the specific
rates $f_n = k$, $g_n = \gamma n$ of the birth–death example, every term but a boundary piece
cancels and what remains is

$$\frac{d}{dt}\langle n\rangle = k - \gamma\langle n\rangle.$$

The mean molecule number obeys exactly the deterministic rate equation, even though individual
systems fluctuate around it. This is not a special feature of this example: **the mean always obeys
the deterministic equation whenever the rates $f_n, g_n$ are linear functions of $n$.**

## The steady-state distribution: a Poisson

Set $dp_n/dt = 0$ in the master equation for the birth–death system:

$$0 = -(k+\gamma n)p_n + k\,p_{n-1} + \gamma(n+1)p_{n+1}.$$

Write $\bar n = k/\gamma$ (the deterministic steady state) and rearrange:

$$(n+1)p_{n+1} - \bar n\,p_n = n\,p_n - \bar n\,p_{n-1}.$$

The right-hand side evaluated at $n$ is exactly the left-hand side evaluated at $n-1$, so this
quantity is the *same number* for every $n$ — call it $C$. Normalizability forces $C = 0$: a
nonzero constant "current" between neighboring states cannot be sustained all the way out to
$n\to\infty$ by a distribution that sums to something finite. With $C=0$ the recursion collapses:

$$p_n = \frac{\bar n}{n}p_{n-1} = \frac{\bar n^2}{n(n-1)}p_{n-2} = \cdots = \frac{\bar n^n}{n!}p_0,$$

and normalizing (using $\sum_n \bar n^n/n! = e^{\bar n}$) fixes $p_0 = e^{-\bar n}$. The result is the
**Poisson distribution**:

$$p_n = \frac{\bar n^n}{n!}e^{-\bar n}, \qquad \bar n = \frac{k}{\gamma}.$$

The argument that forced $C=0$ will reappear, in a different guise, in the Fokker–Planck picture
below: a genuine steady state cannot sustain a constant nonzero probability current.

## How large is "large"?

For a Poisson distribution the mean and the variance coincide:

$$\langle n\rangle = \langle \delta n^2\rangle = \bar n,$$

so the relative size of the fluctuations is

$$\frac{\sqrt{\langle\delta n^2\rangle}}{\langle n\rangle} = \frac{1}{\sqrt{\langle n\rangle}}.$$

This is the precise sense in which molecule counts need to be "large" before the deterministic
equation can be trusted: the relative deviation from the deterministic trajectory shrinks only as
the inverse square root of the number of molecules. An ensemble of systems averaging 20 molecules
shows about a 22% spread around that value; one averaging 500 molecules shows only about 4%. The
two regimes look qualitatively different even though both obey the same equation for the mean.

## The Fokker–Planck equation: a continuum approximation

Solving the master equation exactly means tracking every $p_n$ for every $n$ — an infinite system.
There is a useful shortcut for **intermediate** molecule numbers: large enough that the step from
$n$ to $n\pm1$ is a small perturbation, but not so large that fluctuations can be ignored
altogether. Treat $n$ as continuous and write $h(n)$ for what was $h_n$. Any smooth function
Taylor-expands as

$$h(n+\Delta n) = h(n) + \frac{\partial h}{\partial n}\Delta n
+ \frac12\frac{\partial^2 h}{\partial n^2}\Delta n^2 + \cdots,$$

so expanding the two "neighbor" terms of the master equation around $n$ (here $\Delta n = \pm1$),

$$f(n-1)p(n-1) = f(n)p(n) - \frac{\partial}{\partial n}\big[f(n)p(n)\big]
+ \frac12\frac{\partial^2}{\partial n^2}\big[f(n)p(n)\big] - \cdots$$

$$g(n+1)p(n+1) = g(n)p(n) + \frac{\partial}{\partial n}\big[g(n)p(n)\big]
+ \frac12\frac{\partial^2}{\partial n^2}\big[g(n)p(n)\big] + \cdots$$

Substituting into the master equation and keeping terms through second order gives the
**Fokker–Planck equation**:

$$\frac{\partial p(n,t)}{\partial t}
= -\frac{\partial}{\partial n}\left[(f-g)p - \frac12\frac{\partial}{\partial n}(f+g)p\right]
\equiv -\frac{\partial J}{\partial n},$$

where $J$ is a probability flux. The equation is a diffusion equation in disguise: think of each
system in the ensemble as a particle whose position is its molecule number $n$, and $J$ as the
current of particles across a given value of $n$.

### The zero-flux argument, and a potential

In steady state $J$ must be constant in $n$ — otherwise probability would pile up without bound
somewhere. But the flux at $n=0$ has to vanish, since no system can flow into negative molecule
number, so $J \equiv 0$ everywhere, not just at that one boundary. Zero flux means

$$(f-g)p = \frac12\frac{\partial}{\partial n}\big[(f+g)p\big].$$

Substituting $q = (f+g)p$ turns this into a first-order linear ODE for $q$:

$$\frac{\partial}{\partial n}\ln q = 2\,\frac{f-g}{f+g}
\quad\Longrightarrow\quad
q = A\,\exp\!\left(\int 2\,\frac{f-g}{f+g}\,dn\right),$$

so that

$$p(n) = \frac{A}{f(n)+g(n)}\,e^{-\varphi(n)}, \qquad
\varphi(n) = -\int 2\,\frac{f(n)-g(n)}{f(n)+g(n)}\,dn'.$$

The steady-state probability is, up to the prefactor $1/(f+g)$, a Boltzmann-like weight
$e^{-\varphi(n)}$ for an effective potential $\varphi$ built entirely out of the reaction rates:
wherever $f>g$ (net production) $\varphi$ decreases, and wherever $g>f$ (net removal) it increases,
so $\varphi$ has minima exactly at the deterministic steady states.

## Example: a bistable genetic switch

Take the autocatalytic gene-regulatory system from problem set 1:

$$\frac{dx}{dt} = \underbrace{\frac{v_0+v_1K_1K_2x^2}{1+K_1K_2x^2}}_{f(x)} - \underbrace{\gamma x}_{g(x)}.$$

There $x$ was a concentration and the decay term came from dilution by cell growth. Here take the
cell volume fixed and let the decay instead be an active degradation process, so that $x$ can be
reinterpreted directly as a molecule number. With $\gamma=1$, $K_1K_2=10^{-4}$, $v_0=12.5$,
$v_1=200$, $(f-g)(x)$ crosses zero three times — two stable roots flanking one unstable root — so
the system is **bistable**.

Feeding this $f$ and $g$ into $\varphi(x) = -\int 2\,(f-g)/(f+g)\,dx'$ produces a double-well
potential, with the two stable states sitting in the wells and the unstable state at the barrier
between them. The corresponding steady-state distribution $p(x) = \frac{A}{f+g}e^{-\varphi(x)}$ is
bimodal: peaked in each well, and vanishingly small at the barrier.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="A double-well potential with a bimodal steady-state probability distribution concentrated in the two wells">
  <line x1="30" y1="190" x2="335" y2="190" stroke="currentColor" stroke-width="1.2"/>
  <text x="345" y="194" font-size="12" fill="currentColor">x</text>
  <path d="M40,60 C70,60 80,150 110,150 C140,150 155,80 185,80 C215,80 230,150 260,150 C290,150 300,60 330,60"
        fill="none" stroke="currentColor" stroke-width="1.6"/>
  <path d="M40,190 L70,190 C90,190 95,140 110,140 C125,140 130,190 150,190 L215,190
           C230,190 235,140 260,140 C280,140 290,190 320,190 L330,190 Z"
        fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  <text x="90" y="167" text-anchor="middle" font-size="11" fill="currentColor">stable state</text>
  <text x="260" y="167" text-anchor="middle" font-size="11" fill="currentColor">stable state</text>
  <text x="185" y="72" text-anchor="middle" font-size="11" fill="currentColor">barrier</text>
  <text x="335" y="65" font-size="12" fill="currentColor">&#966;(x)</text>
  <text x="335" y="150" font-size="12" fill="currentColor">p(x)</text>
</svg>
<figcaption>The potential φ(x) built from the bistable rates f(x)-g(x) has two wells separated by a
barrier; the shaded steady-state distribution p(x) concentrates in the wells and is nearly zero at
the barrier.</figcaption>
</figure>

This is the picture the rest of the chapter builds toward: a population of otherwise identical
cells running this network splits into two subpopulations sitting in the two wells, with individual
cells occasionally hopping between them.

## How long between reactions? The waiting-time distribution

The master equation and its continuum relative describe the *distribution* $p_n(t)$, but to
actually simulate one system's trajectory — rather than the whole ensemble — it helps to know the
distribution of the time until the next reaction, for a reaction firing at constant rate $r$.

Let $P(\tau)\,d\tau$ be the probability that the next occurrence falls between $\tau$ and
$\tau+d\tau$. This factors as "does not happen before $\tau$" times "happens in the next $d\tau$":

$$P(\tau) = Q(\tau)\cdot r\,d\tau, \qquad Q(\tau) \equiv \wp(\text{no occurrence before } \tau).$$

$Q$ satisfies its own recursion, since not occurring before $\tau$ means not occurring before
$\tau - d\tau$ *and* not occurring in the last sliver:

$$Q(\tau) = Q(\tau-d\tau)\,(1-r\,d\tau)
\;\Longrightarrow\; \frac{d\ln Q}{d\tau} = -r
\;\Longrightarrow\; Q(\tau) = e^{-r\tau}$$

(using $Q(0)=1$). So

$$P(\tau) = r\,e^{-r\tau}\,d\tau:$$

the waiting time between successive firings of a constant-rate reaction is **exponentially
distributed**, with mean $\langle\tau\rangle = 1/r$ and variance $\langle\delta\tau^2\rangle =
1/r^2$. This is the same memorylessness that made $n(t)$ a Markov process in the first place: the
exponential is the only distribution for which how long you have already waited carries no
information about how much longer you will wait.

## Simulating a reaction network: the Gillespie recipe

The exponential waiting-time law is exactly what is needed to simulate individual stochastic
trajectories numerically, rather than solve for the whole distribution $p_n(t)$.

**Sampling trick.** If $u$ is drawn uniformly from $(0,1)$, then

$$\theta = \frac{1}{r}\ln\!\left(\frac{1}{u}\right)$$

is distributed exactly as the waiting time $\tau$ above — exponential with rate $r$. (This is the
standard inverse-transform trick: it turns a uniform random-number generator into a generator for
any distribution whose cumulative distribution function can be inverted.)

**The algorithm.** Suppose the network has $m$ possible reaction channels — $m=2$ for the
birth–death system, creation and destruction — each currently firing at rate $r_i$:

1. Draw $m$ independent putative waiting times $\theta_i$ from the recipe above, one per channel.
2. Let the channel with the *smallest* $\theta_i$ be the one that actually fires next; advance the
   clock by that $\theta_i$.
3. Update the state accordingly — e.g. $n \to n+1$ for a creation event, $n \to n-1$ for a
   destruction event.
4. Recompute all the rates $r_i$ at the new state, and repeat from step 1.

Running this once generates one noisy trajectory $n(t)$ of the kind sketched at the start of the
chapter. Running it many times — 2,500 repeats, in the case worked through here — and recording
only the final state at some fixed time reproduces the distribution of outcomes across the
ensemble. This procedure is a slight simplification of the full **Gillespie algorithm**.

## Spontaneous switching in a bistable system

Apply the simulation recipe to the bistable network above. A single cell does not sit permanently
in one well: its trajectory $x(t)$ occasionally jumps from one stable state to the other, driven by
a run of fluctuations large enough to carry it over the barrier. Across a population, this produces
exactly the bimodal histogram of the steady-state distribution derived from the Fokker–Planck
potential — most cells sit in one well or the other, in proportions set by $p(x)$, with rare
individuals caught mid-transition.

The natural quantity to ask for is the **lifetime** of a state: the average time a cell spends in
one well before escaping to the other. Simulation shows that this lifetime grows rapidly with the
average number of $X$ molecules in that state, and diverges as that number gets large — a second,
independent way of seeing the crossover to deterministic behavior: with enough molecules, a state
that was only *metastable* becomes, for all practical purposes, permanently stable.

This is not a purely academic question. Reading the switch (with time measured in units of the
degradation time of $X$, typically of order a cell lifetime) as a toy model of the phage-$\lambda$
lysis/lysogeny decision, the induced state corresponds to lysogeny and an escape event to
spontaneous lysis. Measured lysogens undergo spontaneous lysis at a rate of about $10^{-8}$ per
cell per generation — an extremely stable switch. Matching that stability in the simple model above
requires roughly 1,000 molecules, consistent with measured repressor concentrations in the real
system. Stability can also be bought by means other than raw molecule number: higher cooperativity
in the regulatory interactions, or stabilizing feedback loops, both deepen the wells and steepen
the barrier without needing more molecules.

## Sources

All of this chapter comes from the lecture-outline handout for Lecture 12 of *7.81/8.591/9.531
Systems Biology* (A. van Oudenaarden and M. Thattai, MIT, Fall 2004; MIT OpenCourseWare, CC
BY-NC-SA), sections 1–10, split across six converted files in `lecture-outlines/12-outline/`:

- `01-1-introduction.md` — §1, the discreteness/Markov motivation (source Fig. 1).
- `02-2-probabilistic-formulation-of-reaction-kinetics-the-master.md` — §2 (master equation, source
  Fig. 2), §3 (deterministic limit for the mean), §4 (Poisson steady state), §5 (large-number
  limit, source Fig. 3).
- `03-6-the-fokker-planck-equation.md` — §6 (Fokker–Planck equation) and §7 (bistable-switch
  example, source Fig. 4).
- `04-8-waiting-times-between-reaction-events.md` — §8 (exponential waiting-time distribution).
- `05-9-stochastic-simulation-of-chemical-reactions.md` — §9 (Gillespie-style simulation recipe).
- `06-10-spontaneous-switching-rates-in-a-bistable-system.md` — §10 (escape times, source Fig. 5,
  phage-λ discussion).

No transcript, written notes or problem set were supplied for this lecture; the two diagrams in
this chapter (the master-equation flux diagram and the double-well potential) are original
renderings of what the source describes as its Figs. 2 and 4, not reproductions of the original
figures, which were not available. The bistable network's rate function $f(x)$ is stated in the
source to come from "problem set 1" of the course, which was not among the supplied material and is
not reproduced here. The source files themselves are flagged as model-reconstructed from a PDF with
no text layer (`sources/ocw-8591j-2004/lecture-outlines/12-outline.pdf`), with every equation
marked unverified in that conversion — the equations above should be checked against the original
PDF before being cited as a primary source.

---

[← 9. Genetic Toggle Switch and Oscillator](09-genetic-toggle-switch-and-oscillator.md) · [Contents](index.md) · [11. The Turing Instability Condition →](11-the-turing-instability-condition.md)
