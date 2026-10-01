---
title: "11. Dynamic Instability of Microtubules"
course: "MIT 8.592J"
chapter: 11
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 11. Dynamic Instability of Microtubules

## What this covers

This chapter looks at one physical function carried out by the cell's cytoskeleton: the
oscillatory growth-and-shrinkage behaviour of microtubules known as *dynamic instability*, and two
models built for it in the lecture — a coarse two-state stochastic model of the whole filament tip,
and a finer model of the GTP-bound "cap" thought to control the switch between the two states. It
assumes familiarity with master equations for continuous-time Markov processes and with solving
linear PDEs by Fourier transform; the lecture points to a problem-set assignment for the latter
technique, which was not supplied with this lecture.

## Cell function and the cytoskeleton

Proteins carry out a wide range of cell functions: enzymatic activity (breaking down sugars),
transport (haemoglobin carrying oxygen), sensing and signalling (transcription factors), and
biophysical functions tied to force and motion — moving organelles, holding cell shape, producing
motion. This chapter is about the last kind, worked out through the example of microtubules and the
motors that ride them.

The interior of a cell is not a fluid bag: it holds specific shapes and carries out specific
mechanical tasks through the active dynamics of protein fibres, the cytoskeleton. These fibres
assemble from protein subunits much as polymers do, but are considerably stiffer because the
subunits themselves are larger.

- **Microfilaments**, the thinnest, are built from the monomer *actin* and are roughly 8 nm in
  diameter. They have a built-in directionality — a plus end and a minus end — and are typically
  held in a dynamic equilibrium in which monomers dissociate from the minus end while new monomers
  assemble at the plus end, a process called *treadmilling*.
- **Microtubules**, the subject of the rest of this chapter, are larger: 25 nm in diameter, built
  from dimers of $\alpha$- and $\beta$-tubulin. A microtubule is a hollow cylinder made of 13
  protofilaments stacked side by side, directional like actin filaments, and of variable length,
  growing up to about 25,000 nm.
- **Intermediate filaments**, 8–25 nm across, occur in a variety of cells — for example
  strengthening the long axons of neurons.

## Dynamic instability of microtubules

Discovered in the 1980s (Mitchison and Kirschner, 1984), *dynamic instability* is the phenomenon in
which a microtubule grows at a slow, steady rate and is then interrupted by a "catastrophe": a
sudden switch to rapid shortening, which persists until a "rescue" event restores the original slow
growth. The cycle repeats stochastically, on a timescale of minutes.

The behaviour depends on a constant influx of energy, as does the cytoskeleton generally, and here
that energy comes from hydrolysis of GTP (guanosine triphosphate) to GDP (guanosine diphosphate).
A tubulin dimer must be bound to GTP before it can be added to the growing end of a microtubule, so
the growing (plus) end is capped by GTP-bound tubulin. Further back from the tip, individual
subunits can spontaneously hydrolyse their bound GTP to GDP — and it is the fate of that GTP-bound
region, the *cap*, that turns out to control the transition between growing and shrinking.

## A two-state model of the filament tip

Dogterom and Leibler (1993) modelled the growth and switching of a microtubule at the coarsest
level that reproduces catastrophe and rescue: treat the tip as being in one of two states, growing
or shrinking, each with its own constant velocity, and let it switch between the states at fixed
rates.

<figure>
<svg viewBox="0 0 360 200" role="img" aria-label="Two-state model of a microtubule tip switching between a growing state and a shrinking state">
  <defs>
    <marker id="di11-arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="20" y="60" width="130" height="60" rx="8" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="85" y="85" text-anchor="middle" font-size="12" fill="currentColor">growing (+)</text>
  <text x="85" y="103" text-anchor="middle" font-size="12" fill="currentColor">tip speed v₊</text>

  <rect x="210" y="60" width="130" height="60" rx="8" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="275" y="85" text-anchor="middle" font-size="12" fill="currentColor">shrinking (–)</text>
  <text x="275" y="103" text-anchor="middle" font-size="12" fill="currentColor">tip speed v₋</text>

  <path d="M150 70 C 175 45, 185 45, 210 70" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#di11-arrow)"/>
  <text x="180" y="38" text-anchor="middle" font-size="12" fill="currentColor">f₊₋ (catastrophe)</text>

  <path d="M210 110 C 185 135, 175 135, 150 110" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#di11-arrow)"/>
  <text x="180" y="152" text-anchor="middle" font-size="12" fill="currentColor">f₋₊ (rescue)</text>
</svg>
<figcaption>The tip is in one of two states, growing or shrinking, each with its own constant
velocity; it switches between them at rates f₊₋ and f₋₊.</figcaption>
</figure>

Let $P_+(z,t)$ and $P_-(z,t)$ be the probability that a growing, respectively shrinking, microtubule
has length $z$ at time $t$. Dropping diffusive spreading within a state (small compared to the
drift), the evolution is

$$\frac{\partial}{\partial t}P_+(z,t) = -f_{+-}P_+ + f_{-+}P_- - \frac{\partial}{\partial z}\big(v_+P_+\big)$$

$$\frac{\partial}{\partial t}P_-(z,t) = +f_{+-}P_+ - f_{-+}P_- + \frac{\partial}{\partial z}\big(v_-P_-\big)$$

The first two terms on each right-hand side are a birth–death process on the two-state label —
probability leaves the growing population at rate $f_{+-}$ and arrives from the shrinking population
at rate $f_{-+}$, and conversely — and the last term is transport of probability along $z$ at that
state's own drift velocity.

Because the rates and velocities do not depend on $z$ or $t$, the system is linear and
translation-invariant, so it is solved by Fourier modes $P_\pm(z,t)\propto e^{i(kz-\omega t)}$:
substituting $\partial_t\to-i\omega$, $\partial_z\to ik$ turns the pair of PDEs into a $2\times2$
linear algebraic system,

$$\begin{pmatrix} i\omega - f_{+-} - ikv_+ & f_{-+} \\ f_{+-} & i\omega - f_{-+} + ikv_- \end{pmatrix}
\begin{pmatrix} P_+(k,\omega) \\ P_-(k,\omega) \end{pmatrix} = 0.$$

A non-trivial mode exists only where the determinant vanishes; solving that condition for
$\omega(k)$ and expanding for small $k$ gives

$$\omega(k) = vk - Dk^2 + \cdots$$

The linear term is an effective net drift velocity $v$ of the tip once the fast switching between
the two ballistic states is averaged over; the quadratic term is an effective diffusion coefficient
$D$ that appears even though neither state is individually diffusive — it is generated purely by
the randomness of *when* the switches happen, the same mechanism that produces diffusive spreading
from a dichotomous (telegraph) process alternating between two constant velocities.

## The stabilizing cap: what sets the switching rate

The model above takes $f_{+-}$ and $f_{-+}$ as given constants. The question the lecture poses next
is where they come from: how does the transition between growing and shrinking actually happen, and
how should it depend on the concentration of free tubulin (and GTP) in solution?

Flyvbjerg, Holy and Leibler (1994) answered this by modelling the GTP cap directly. A microtubule
grows by adding tubulin-GTP dimers at its tip; behind the tip, individual subunits spontaneously
hydrolyse their bound GTP to GDP. Track two positions along the filament: $T$, the growing tip, and
$E$, the leading edge of hydrolysis — the point up to which some subunit has already converted to
GDP. The unbroken stretch of GTP-tubulin between $E$ and $T$ is the stabilizing cap, of length $x$.

<figure>
<svg viewBox="0 0 420 190" role="img" aria-label="The GTP cap at a microtubule tip, bounded by the growing tip T and the hydrolysis front E">
  <defs>
    <marker id="di12-arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="30" y="80" width="340" height="26" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <rect x="250" y="80" width="120" height="26" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <line x1="250" y1="80" x2="250" y2="106" stroke="currentColor" stroke-width="1.5"/>

  <text x="140" y="72" text-anchor="middle" font-size="12" fill="currentColor">GDP-tubulin lattice</text>
  <text x="310" y="72" text-anchor="middle" font-size="12" fill="currentColor">GTP cap (stable)</text>

  <line x1="250" y1="48" x2="250" y2="56" stroke="currentColor" stroke-width="1.5"/>
  <line x1="370" y1="48" x2="370" y2="56" stroke="currentColor" stroke-width="1.5"/>
  <line x1="250" y1="52" x2="370" y2="52" stroke="currentColor" stroke-width="1.5"/>
  <text x="310" y="40" text-anchor="middle" font-size="12" fill="currentColor">cap length x</text>

  <text x="250" y="124" text-anchor="middle" font-size="12" fill="currentColor">E</text>
  <text x="370" y="124" text-anchor="middle" font-size="12" fill="currentColor">T</text>

  <line x1="370" y1="93" x2="395" y2="93" stroke="currentColor" stroke-width="1.5" marker-end="url(#di12-arrow)"/>
  <text x="395" y="145" text-anchor="end" font-size="12" fill="currentColor">v_T: growth</text>

  <line x1="228" y1="93" x2="248" y2="93" stroke="currentColor" stroke-width="1.5" marker-end="url(#di12-arrow)"/>
  <text x="228" y="145" text-anchor="middle" font-size="12" fill="currentColor">v_E: hydrolysis front</text>
</svg>
<figcaption>The stable cap is the unbroken stretch of GTP-tubulin between the hydrolysis front E and
the growing tip T. T advances by addition of tubulin-GTP; E advances because hydrolysis converts
GTP to GDP somewhere within the cap. A catastrophe is the event that E catches T.</figcaption>
</figure>

The rules of the model:

- $T$ advances at a growth rate that depends on the concentration of tubulin-GTP in solution: more
  subunits available, faster growth.
- $E$ advances because hydrolysis, occurring spontaneously anywhere within the cap, converts some
  GTP-bound subunit to GDP; the position of $E$ is set by the frontmost such conversion.
- A **catastrophe** is the event that $E$ catches $T$: the cap length reaches zero, no GTP-bound
  subunits remain to stabilize the tip, and the microtubule switches into rapid shrinkage.

This picture is supported by the observation that catastrophes are rarer when growth is faster, at
high tubulin concentration — a fast-advancing $T$ stays ahead of a hydrolysis front $E$ whose speed
does not depend on tubulin concentration, keeping the cap long. The lecture also poses, without
resolving in the material at hand, a puzzle for the model to answer: if a microtubule that had been
growing is suddenly transferred to a tubulin-poor solution, the time until catastrophe is observed
to depend little on the concentration it had been growing in beforehand.

Writing $p(x,t)$ for the probability that the cap has length $x$ at time $t$, Flyvbjerg, Holy and
Leibler propose the master equation

$$\partial_t p(x,t) = -v\,\partial_x p + D\,\partial_x^2 p - r\,x\,p + r\int_x^\infty dy\, p(y,t),$$

with $v \equiv v_T - v_E$ and $D \equiv D_T + D_E$. Reading it term by term:

- $-v\,\partial_x p$: drift of the cap length at the net rate $v$, tip growth minus the advance of
  the hydrolysis front.
- $D\,\partial_x^2 p$: diffusion of the cap length, with $D_T$ and $D_E$ adding because the two
  boundaries move independently and each contributes its own fluctuations.
- $-r\,x\,p$: loss — hydrolysis can strike at random at any of the $x$ subunits currently in the
  cap, each at rate $r$, so a cap of length $x$ is destroyed (cut down to something shorter) at
  total rate proportional to its own length.
- $r\int_x^\infty dy\,p(y,t)$: gain — a cap of length $x$ is created whenever a *longer* cap, of
  length $y>x$, suffers a hydrolysis event exactly a distance $x$ behind its own tip, cutting it
  down to length $x$. Summing over all longer caps $y$ replenishes the population at $x$, matching
  the loss term above.

## Sources

- Lecture slides (paraphrased text for §§3, 3.1, 3.1.1, cell function, cytoskeletal filaments,
  dynamic instability): `computational-biology/mit-ocw/8592j/lectures/20-slides.md`, MIT 8.592J
  (Statistical Physics in Biology), from `sources/ocw-8592j/lectures/20-slides.pdf`.
- The two-state model, its master equations, the Fourier-transform solution, and the
  Flyvbjerg–Holy–Leibler cap model and its master equation are read directly from the lecture's
  handwritten slide images, dated 4/11/07 and marked "Lec. 17": `20-slides/figures/p002-1.jpeg`
  ("Dynamic Instability of Microtubules", citing Mitchison and Kirschner (1984) and Dogterom and
  Leibler (1993)) and `20-slides/figures/p004-1.jpeg` (citing Flyvbjerg, Holy and Leibler (1994)).
  The auto-generated slide text breaks off mid-sentence before reaching this material, which is why
  the images rather than the paraphrase are cited for it.
- Referenced by the lecture but not supplied with it: "Assignment 7", pointed to for the
  Fourier-transform method used to solve the coupled linear master equations.
- No transcript, written notes, or exercise set was supplied for this lecture.

---

[← 10. Protein Search Kinetics on DNA](10-protein-search-kinetics-on-dna.md) · [Contents](index.md) · [12. Molecular Motors as Brownian Ratchets →](12-molecular-motors-as-brownian-ratchets.md)
