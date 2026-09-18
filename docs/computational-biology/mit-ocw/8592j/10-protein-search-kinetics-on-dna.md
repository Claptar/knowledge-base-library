---
title: "10. Protein Search Kinetics on DNA"
course: "MIT 8.592J"
chapter: 10
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. Protein Search Kinetics on DNA

## What this covers

A repressor protein finds its one target sequence among millions of DNA base pairs fast enough to
shut off a gene within a fraction of a second. This chapter asks how, quantitatively. It starts
from the measured on-rate for a real protein-DNA pair, builds the classical diffusion-limited
theory of that rate, shows the theory is two orders of magnitude too slow, and then works through
the fix — a protein that alternates between sliding along the DNA and jumping through solution. It
assumes the diffusion equation, elementary mass-action kinetics, and the geometric and exponential
distributions.

## The kinetics of a protein-DNA complex

Consider a protein $P$ that can bind a specific site on a DNA molecule. The concentration of the
bound complex changes for two reasons: complexes form, at a rate proportional to how likely a free
site and a free protein are to be at the same place, and complexes break up, at a rate proportional
to how many there already are. At the low concentrations relevant to a cell, both proportionalities
are exact (this is ordinary mass-action kinetics), giving

$$\frac{d}{dt}[P{\cdot}\text{DNA}] = k_a [P][\text{DNA}] - k_d [P{\cdot}\text{DNA}],$$

where $k_a$ is the **on-rate** and $k_d$ the **off-rate**. For the *lac* repressor binding its
operator on *E. coli* DNA, *in vitro* measurements give $k_a \sim 10^{10}\ \text{M}^{-1}\text{s}^{-1}$.

**The question.** Suppose lactose is abundant, so the repressor sits inactive and no complexes have
formed. At $t = 0$ lactose vanishes, the repressor activates, and it must now find the operator to
switch the gene off. How long does that take?

There are only a handful of operator sequences per cell. Taking the cell volume as $1\ \mu\text{m}^3$
gives an operator number density of about $1/\mu\text{m}^3$, which converted to molar units
($1\ \text{M} = 6\times 10^{26}\ \text{m}^{-3}$) is $[\text{DNA}] \sim 10^{-9}\ \text{M}$. Because
this concentration barely changes while the search is still going on, the rate equation linearises
at early times:

$$\frac{d}{dt}[P{\cdot}\text{DNA}] \approx \big(k_a[\text{DNA}]\big)[P] = [P]/\tau, \qquad
\tau \equiv \frac{1}{k_a[\text{DNA}]}.$$

$\tau$ is the characteristic time for one free repressor to locate the operator. Plugging in the
measured $k_a$ and the estimated $[\text{DNA}]$ gives $\tau \sim 0.1\ \text{s}$: the repressor finds
its target in about a tenth of a second. The rest of the chapter asks where the number $k_a\sim
10^{10}\ \text{M}^{-1}\text{s}^{-1}$ that made this possible actually comes from.

## Diffusion-limited kinetics: the Debye-Smoluchowski rate

The classical answer is that binding is limited only by how fast diffusion can bring the two
partners together. Model the cell as a sphere of radius $R$ with the target site at the centre, and
let $C(\vec r, t)$ be the concentration field of free protein, obeying the diffusion equation
$\partial C/\partial t = D_3\nabla^2 C$ with $D_3$ the protein's diffusion constant in the cytoplasm.

The protein must find the *exact* target sequence, so represent the target as a small absorbing
sphere of radius $b\approx 0.34\ \text{nm}$ (one base pair) at the origin: whenever a diffusing
protein touches it, it disappears (it has become a bound complex). This is a good approximation as
long as the target is usually unoccupied. Hold the concentration fixed at $C_R$ on the outer
boundary, as if protein is constantly resupplied there. Under these conditions a time-independent
current of protein flows steadily inward, so instead of the full diffusion equation it is enough to
solve Laplace's equation, $\nabla^2 C = 0$, with $C(R) = C_R$ and $C(b) = 0$.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Concentric-sphere model of diffusion-limited binding, with a fixed concentration on the outer sphere and an absorbing target at the centre">
  <defs>
    <marker id="ds-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="160" cy="112" r="86" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="160" cy="112" r="15" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <line x1="160" y1="94" x2="160" y2="34" stroke="currentColor" stroke-width="1.5" marker-end="url(#ds-arrow)"/>
  <text x="168" y="65" font-size="12" fill="currentColor">I</text>
  <text x="196" y="34" font-size="12" fill="currentColor">radius R, fixed C_R</text>
  <text x="118" y="108" font-size="11" fill="currentColor" text-anchor="end">target, radius b</text>
  <line x1="118" y1="112" x2="145" y2="112" stroke="currentColor" stroke-width="1"/>
</svg>
<figcaption>The Debye-Smoluchowski setup: concentration is pinned at $C_R$ on the outer sphere of
radius $R$ and at zero on the absorbing target of radius $b$ at the centre. The steady state of
Laplace's equation carries a constant inward current $I$.</figcaption>
</figure>

The spherically symmetric solution is $C(r) = C_0[1 - b/r]$, with $C_0 = C_R/(1-b/R)\approx C_R$
since $b\ll R$. Fick's law gives the radially inward current density $J = -D_3\,\partial C/\partial r
= -D_3 b C_0/r^2$, and the total current through any sphere is

$$I = J(r)\cdot 4\pi r^2 = -4\pi D_3 b\, C_0.$$

The number of complexes forming per second — the left side of the linearised rate equation above —
must equal (minus) this incoming current, with $C_0$ identified as the bulk free-protein
concentration $[P]$. Matching the two gives the **Debye-Smoluchowski rate**:

$$k_a = 4\pi D_3 b.$$

Using the target size $b\approx 0.34\ \text{nm}$ and the measured diffusion constant of the *lac*
repressor in water, $D_3 \approx 3\times 10^{-11}\ \text{m}^2\text{s}^{-1}$, gives $k_a \approx
10^8\ \text{M}^{-1}\text{s}^{-1}$ — and the real value should if anything be smaller still, because
a protein also needs time to align itself with the target and because $D_3$ in the crowded
cytoplasm is lower than in water. Either way this is **two orders of magnitude below** the measured
$k_a \sim 10^{10}\ \text{M}^{-1}\text{s}^{-1}$. Plain three-dimensional diffusion cannot account for
how fast the repressor actually finds its target — something else must be speeding the search up.

## Facilitated diffusion: sliding and jumping (Berg-von Hippel theory)

Berg and von Hippel's proposal is that the protein does not diffuse only in three dimensions. It
can bind *any* site on the DNA, not just the specific one, and once bound it diffuses along the
DNA backbone (**sliding**, one-dimensional diffusion with constant $D_1$). Eventually it detaches
and diffuses freely in solution (a **jump**) until it lands on the DNA again, somewhere else, and
resumes sliding. It keeps alternating rounds of sliding and jumping until, purely by chance, a
sliding event carries it across the specific target — at which point it stays, because the specific
site binds far more strongly ($E_s \sim 20$–$25\,k_BT$) than a generic site does
($E_{ns} \sim 5$–$10\,k_BT$): non-specific binding is weak enough to let the protein keep exploring,
while the target is a deep trap.

<figure>
<svg viewBox="0 0 340 170" role="img" aria-label="Schematic of the 1D/3D search: thick segments are sliding along the DNA, dashed arcs are jumps through solution">
  <line x1="20" y1="120" x2="320" y2="120" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="120" x2="90" y2="120" stroke="currentColor" stroke-width="4"/>
  <path d="M90,120 Q120,60 150,120" fill="none" stroke="currentColor" stroke-width="1.25" stroke-dasharray="4,3"/>
  <line x1="150" y1="120" x2="180" y2="120" stroke="currentColor" stroke-width="4"/>
  <path d="M180,120 Q225,35 270,120" fill="none" stroke="currentColor" stroke-width="1.25" stroke-dasharray="4,3"/>
  <line x1="270" y1="120" x2="300" y2="120" stroke="currentColor" stroke-width="4"/>
  <circle cx="300" cy="120" r="4" fill="currentColor"/>
  <text x="65" y="140" font-size="11" fill="currentColor" text-anchor="middle">slide</text>
  <text x="120" y="55" font-size="11" fill="currentColor" text-anchor="middle">jump</text>
  <text x="300" y="140" font-size="11" fill="currentColor" text-anchor="middle">target</text>
</svg>
<figcaption>The protein alternates rounds of one-dimensional sliding along the DNA (thick segments)
with three-dimensional jumps through solution (dashed arcs), until a slide carries it across the
specific target site.</figcaption>
</figure>

**Why jumps can be treated as landing uniformly at random.** DNA is packed into a compact coil, so
two sites that are close together in real space can be very far apart along the sequence. It is
therefore reasonable to treat a jump as landing on a uniformly random site among the $M$ total
sites, independently of where the previous slide ended. Each sliding event then independently has
some probability $q = n/M$ of passing over the target, where $n$ is the number of sites visited
during that slide.

### A fixed sliding time, first

Suppose, unrealistically, that every slide takes the same time $\tau_1$ and visits the same number
of sites $n$. The number of rounds $N_R$ needed to hit the target is then geometric: the protein
misses in each of the first $N_R - 1$ rounds and hits on the $N_R$-th,

$$p(N_R) = q(1-q)^{N_R - 1}, \qquad \overline{N_R} = \sum_{N_R=1}^\infty N_R\, q(1-q)^{N_R-1} =
\frac{1}{q} = \frac{M}{n}.$$

Each round costs the sliding time plus the average jump time $\tau_3$, so the average search time
is

$$\overline{t_s} = \overline{N_R}(\tau_1 + \tau_3) = \frac{M}{n}(\tau_1+\tau_3).$$

### Sliding times are actually random

Real sliding events end when the protein happens to detach, at rate $k_d^{(ns)} = 1/\overline{\tau_1}$,
so the duration of a slide is exponentially distributed, $\rho(\tau_1) =
\exp(-\tau_1/\overline{\tau_1})/\overline{\tau_1}$.

The number of sites visited in a slide of duration $\tau_1$ now needs care. What matters is not
where the slide *ends* but every site it *passes over*, since the protein would be trapped the
instant it crossed the target during the slide, not only if it happened to stop there. The relevant
quantity is therefore the **range** of the one-dimensional random walk — the span between its
leftmost and rightmost visited site — rather than its end-to-end displacement:

$$n(\tau_1) = \sqrt{\frac{16 D_1 \tau_1}{\pi b^2}} \qquad \text{(range)}, \qquad \text{as opposed to}
\qquad \sqrt{\frac{2D_1\tau_1}{b^2}} \qquad \text{(end-to-end displacement)},$$

with $b$ the base-pair distance. The range is the larger of the two, which matters, since it is
what sets how quickly the protein actually explores new ground.

Averaging $n(\tau_1)$ over the exponential distribution of sliding times gives $\langle n\rangle =
2\sqrt{D_1\overline{\tau_1}}/b$. Because successive slides are still independent draws (each one's
outcome depends only on its own random duration), the same geometric-distribution argument applies
with $q$ replaced by its average $\langle q\rangle = \langle n\rangle /M$:

$$\langle N_R\rangle = \frac{1}{\langle q\rangle} = \frac{Mb}{2\sqrt{D_1\overline{\tau_1}}}.$$

Computing the average search time is more delicate, because a round that ends in success is, on
average, a longer round than one that fails — but working through the sum over rounds (weighting
each round's duration by the probability that the search ends exactly there) the correlation
cancels and the compact form survives:

$$\langle t_s\rangle = \langle N_R\rangle\left(\overline{\tau_1} + \tau_3\right) =
\frac{Mb}{2\sqrt{D_1\overline{\tau_1}}}\left(\overline{\tau_1}+\tau_3\right).$$

### The optimal sliding time

Treat $\overline{\tau_1}$ as a free parameter and minimise $\langle t_s\rangle$ over it:

$$0 = \frac{\partial \langle t_s\rangle}{\partial \overline{\tau_1}} =
\frac{Mb}{2\sqrt{D_1\overline{\tau_1}}}\left(\frac{1}{2} - \frac{\tau_3}{2\overline{\tau_1}}\right)
\quad\Longrightarrow\quad \overline{\tau_1}^{(\text{opt})} = \tau_3.$$

The search is fastest when the average time spent sliding equals the average time spent jumping. Slide
too long ($\overline{\tau_1} > \tau_3$) and the protein wastes time re-covering ground it has
already ruled out, since one-dimensional diffusion explores new sites only as $\sqrt{\text{time}}$;
jump too often ($\overline{\tau_1} < \tau_3$) and it wastes time in solution making no progress
along the sequence at all.

The sliding-off rate $k_d^{(ns)} = 1/\overline{\tau_1}$ depends strongly on the non-specific binding
energy $E_{ns}$, which in turn depends on the salt concentration in the cytoplasm, since the
non-specific interaction is predominantly electrostatic: more salt screens the interaction and
lowers $E_{ns}$. One might expect a cell to sit at the optimum, but at physiological salt
concentrations the measured sliding time for the *lac* repressor, $\overline{\tau_1}\sim
10^{-3}\ \text{s}$, is noticeably longer than the estimated jump time, $\tau_3\sim V/(D_3 L)\sim
10^{-4}\ \text{s}$ (using cell volume $V\sim 1\ \mu\text{m}^3$, DNA length $L = Mb \sim 1\ \text{mm}$,
and $D_3\approx 3\times 10^{-11}\ \text{m}^2\text{s}^{-1}$): real proteins slide somewhat longer than
the strict optimum. Feeding these numbers, together with $D_1\approx 5\times
10^{-14}\ \text{m}^2\text{s}^{-1}$, into the search-time formula gives

$$\langle t_s\rangle = \frac{L}{2\sqrt{D_1\overline{\tau_1}}}(\overline{\tau_1}+\tau_3) \sim
10\text{--}100\ \text{s}.$$

This is the search time for **one** repressor molecule doing facilitated diffusion — and it is far
longer than the $\sim 0.1\ \text{s}$ inferred at the very start of the chapter from the measured
on-rate. The gap is closed by noting that a cell does not search with only one copy.

## Many searchers: the fastest of $n_p$ proteins

Take the single-protein search time to be exponentially distributed, $\rho_1(t_s) =
\exp(-t_s/\langle t_s\rangle)/\langle t_s\rangle$. Gene expression shuts off as soon as the *first*
of $n_p$ independently searching copies binds the target, so what matters is the distribution of
the minimum of $n_p$ independent draws from $\rho_1$. That distribution is standard: the minimum
exceeds $t$ only if every one of the $n_p$ searches has not yet succeeded by time $t$, giving

$$\rho_{n_p}(t_s) = n_p\,\rho_1(t_s)\left(1 - \int_0^{t_s}\rho_1(t)\,dt\right)^{n_p - 1} =
\frac{n_p}{\langle t_s\rangle}\exp\!\left(-\frac{t_s\, n_p}{\langle t_s\rangle}\right),$$

itself exponential, with mean $\langle t_s\rangle/n_p$. With of order $n_p\sim 100$ copies of the
repressor typically present in the cell, this brings the effective search time down from
$10$–$100\ \text{s}$ for a lone protein to roughly $0.1$–$1\ \text{s}$ — matching, in order of
magnitude, the search time inferred from the measured on-rate at the start of the chapter. Searching
in parallel, not a faster mechanism per molecule, is what reconciles facilitated diffusion with the
observed switching speed.

## Exercises

1. The non-specific dissociation rate $k_d^{(ns)} = 1/\overline{\tau_1}$ depends on the non-specific
   binding energy $E_{ns}$. Work out this dependence, and explain why increasing the salt
   concentration in the cytoplasm — which screens the (electrostatic) non-specific interaction —
   changes $\overline{\tau_1}$, and hence the optimal balance between sliding and jumping.

## Sources

- Slides: `lectures/19-slides/01-1-1-reaction-kinetics.md` ("1.1 Reaction Kinetics"),
  `02-1-2-debye-smoluchowski-theory.md` ("1.2 Debye-Smoluchowski theory"), and
  `03-1-3-berg-von-hippel-theory.md` ("1.3 Berg-von Hippel theory"), from MIT OCW 8.592J/HST.452J
  *Statistical Physics in Biology*, Spring 2011, Lecture 22 (4/30/09). No transcript, written notes,
  or exercise sheet were supplied for this lecture; the one exercise above is the "(homework)" aside
  named explicitly in the Berg-von Hippel slide.
- The slides themselves note that the first two sections (reaction kinetics and Debye-Smoluchowski
  theory) closely follow R. F. Bruinsma, *Physica A* **313**, 211-237 (2002) — a paper the lecture
  points to but that was not itself supplied here.
- These slide files are flagged in their own front matter as a model's reconstruction of a PDF with
  no extractable text layer ("fidelity: reconstructed"), with every equation marked unverified. One
  apparent inconsistency was resolved silently for readability: the slide text defines $\tau \equiv
  1/(k_a[P{\cdot}\text{DNA}])$ immediately after deriving $d[P{\cdot}\text{DNA}]/dt \approx
  (k_a[\text{DNA}])[P]$, which is self-consistent only as $\tau = 1/(k_a[\text{DNA}])$; the latter
  is what is used here. Given the reconstruction caveat, the numbered equations in this chapter
  should be checked against the original PDF slides before being cited elsewhere.

---

[← 9. RNA Secondary Structure and Melting](09-rna-secondary-structure-and-melting.md) · [Contents](index.md) · [11. Dynamic Instability of Microtubules →](11-dynamic-instability-of-microtubules.md)
