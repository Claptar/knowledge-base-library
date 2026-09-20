---
title: "24. Negative Autoregulation and the Repressilator"
course: "MIT 8.591J 2014"
chapter: 24
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 24. Negative Autoregulation and the Repressilator

## What this covers

Why does wiring up a gene that represses itself not automatically give you a biological clock, and
what does it actually take? This chapter works through the negative-autoregulation models used to
answer that question, the stability argument (Poincaré–Bendixson, linearization, eigenvalues) that
tells you when a set of ODEs can and cannot oscillate, and the Elowitz–Leibler repressilator as the
worked case where the argument was used to design a real circuit. It assumes you have already seen
linear stability analysis for a system of two linear ODEs (trace/determinant, eigenvalues) and know
what a Hill-function repression term looks like.

## Why build an oscillator at all

Oscillators matter, first, because they are the basis for time-keeping: a pendulum clock is just an
oscillation that lets a winding mechanism advance a little on every swing, and every modern clock,
however high its frequency, is still built on some oscillatory dynamic underneath. Oscillators are
also just interesting dynamically in their own right.

Biology already has an oscillator built from a gene network: the circadian clock, which keeps track
of the day/night cycle and is entrained by it. It is useful for an organism to know roughly where in
the day it is, independent of instantaneous light levels — a cloud crossing the sun is not a
reliable signal that night has fallen, and an organism that shut down on every cloud would be at a
real disadvantage. Circadian oscillators are not the subject of this lecture, but it is worth knowing
that in some systems the oscillation survives *in vitro*, with the gene-expression machinery removed
entirely — just the protein components cycling in a test tube. That was a genuinely surprising result
when it was first published.

## A single auto-repressing gene cannot oscillate

Start with the simplest possible negative feedback: one gene whose protein represses its own
expression. A verbal argument for oscillation is easy to construct: start with a lot of protein, so
expression is strongly repressed and the concentration falls; once it has fallen enough, repression
relaxes, expression resumes, and the concentration climbs back to where it started — and now you're
back at the beginning, so the cycle should repeat forever, with no decay in amplitude.

That argument should not be trusted. Just because you can tell a story in which something happens
does not mean a particular equation reproduces it — the value of writing an actual equation is that
it forces every assumption into the open, and then you can ask, of that specific equation, whether it
oscillates or not. The simplest non-dimensionalized model of a negative auto-regulatory loop is

$$\dot p = \frac{\alpha}{1+p^n} - p ,$$

where $\alpha$ bundles together the expression strength, the protein's lifetime, and the repressor's
binding affinity, and $n$ is the cooperativity (Hill coefficient) of the repression.

Without doing any analysis, this equation is already ruled out. For a fixed value of $p$, this
equation gives exactly one value of $\dot p$ — it is single-valued. But any oscillation has to pass
back and forth through the same concentration, with the derivative sometimes rising and sometimes
falling at that same point; that is a multi-valued relationship between $p$ and $\dot p$, which a
first-order autonomous ODE in one variable simply cannot produce. This is special to *differential*
equations with a *single* variable: a discrete-time difference equation can oscillate, and a
second-order equation — position and velocity, as in a mass on a spring — can too, because it has
two interacting dynamical variables. One variable, one derivative, no oscillation, regardless of what
function sits on the right-hand side.

## Adding the mRNA: a two-variable model

The one-variable argument does not survive once you make the model even slightly more realistic. A
gene is first transcribed into mRNA, and the mRNA is then translated into protein, so write $m$ for
mRNA concentration and $p$ for protein concentration:

$$\dot m = \frac{\alpha}{1+p^n} - m , \qquad \dot p = \beta(m-p).$$

The protein represses transcription of its own mRNA; the mRNA decays; the mRNA's translation makes
protein; the protein also decays, at a rate scaled by $\beta$. Two non-dimensionalization choices are
buried in this equation and are worth making explicit:

- **The unit of time is the mRNA lifetime** — that's why there is no coefficient in front of the
  $-m$ term. $\beta$ is then the *ratio of the mRNA lifetime to the protein lifetime*, introduced
  precisely because the two lifetimes are usually different. (The Elowitz–Leibler paper itself states
  this ratio backwards, as protein lifetime over mRNA lifetime — worth checking against the algebra
  rather than the caption if you go back to it.) Since proteins are typically far more stable than
  mRNA, $\beta$ is typically much less than 1.
- **The unit of protein concentration is $K$**, the dissociation constant — the protein concentration
  that gives half-maximal repression, so $p=1$ means half repression by definition. The unit of mRNA
  concentration is more subtle: it is fixed by the requirement that the $p-m$ term above carry no
  extra coefficient, and that requirement turns out to depend on three things — the translation
  efficiency (how much protein one mRNA molecule produces per unit time), $\beta$, and $K$ itself.
  This is a good example of why a clean non-dimensional equation is not the same as an equation whose
  terms you can interpret at a glance: mathematically simple, biologically you have to be careful
  about what "$m=1$" is actually saying.

**Fixed points.** The origin is not a fixed point: with no protein present there is no repression, so
mRNA is still being made ($\alpha/(1+0)=\alpha\neq 0$). Setting both derivatives to zero gives
$m_{\mathrm{eq}}=p_{\mathrm{eq}}$, and — writing $p_0$ for this common value, to avoid presupposing
whether it is a stable equilibrium or just a fixed point —

$$p_0 = \frac{\alpha}{1+p_0^{\,n}} .$$

For example, with $\alpha=10$ and $n=2$, $p_0=2$ solves this exactly: $10/(1+2^2)=10/5=2$.

## When can a two-variable system oscillate? Poincaré–Bendixson

Whether this system oscillates is no longer decidable "for free" the way the one-variable case was —
you actually have to compute something. But there is still a clean criterion available in two
dimensions, the **Poincaré–Bendixson** criterion. Suppose you can draw a bounded region in the
$(m,p)$ plane that every trajectory enters and never leaves — here that's true, because trajectories
can't cross the axes (some mRNA generates protein, some protein generates mRNA, so neither species
alone can stay pinned at the boundary) and can't run off to infinity (once both concentrations are
large enough, degradation dominates and pulls them back in). Given such a trapping region containing
a *single* interior fixed point, the question "does the system oscillate?" collapses to the question
"is that fixed point stable?" A stable fixed point means every trajectory spirals in and settles
there — no sustained oscillation. An unstable fixed point pushes trajectories away from it, while the
outer boundary of the trapping region pushes trajectories in from outside; because two-dimensional
trajectories can never cross each other (crossing would mean two different values of $\dot m,\dot p$
at the same point — the same single-valuedness argument as before, just in two dimensions), the flow
has nowhere to go except to settle onto a closed loop sandwiched between the two — a **limit cycle**.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="An unstable fixed point drives trajectories outward while a trapping boundary pushes them inward, so the flow settles onto a closed limit-cycle orbit in between">
  <defs>
    <marker id="arrow1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="20" y="15" width="280" height="190" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <line x1="160" y1="15" x2="160" y2="34" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow1)"/>
  <line x1="160" y1="205" x2="160" y2="186" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow1)"/>
  <line x1="20" y1="110" x2="39" y2="110" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow1)"/>
  <line x1="300" y1="110" x2="281" y2="110" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow1)"/>
  <ellipse cx="160" cy="110" rx="64" ry="42" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <circle cx="160" cy="110" r="3" fill="currentColor"/>
  <path d="M164.8,110.9 L165.2,112.4 L164.3,114.1 L162.1,115.7 L158.6,116.7 L154.4,116.8 L149.9,115.8 L145.9,113.7 L143.2,110.5 L142.6,106.7 L144.3,102.6 L148.5,99.0 L155.0,96.3 L163.0,95.2 L171.7,95.9 L179.9,98.6 L186.3,103.1 L190.0,109.1 L190.1,115.8 L186.3,122.4 L178.7,127.9 L168.0,131.7 L155.3,133.0 L142.2,131.4 L130.4,127.0 L121.5,120.0 L116.8,111.3 L117.2,101.8 L123.2,92.7 L134.2,85.1 L149.1,80.3 L166.3,78.9 L183.8,81.3 L199.3,87.4 L210.7,96.8 L216.5,108.3 L215.4,120.6" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow1)"/>
  <line x1="160" y1="38" x2="160" y2="95" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
  <text x="160" y="30" text-anchor="middle" font-size="11" fill="currentColor">unstable fixed point</text>
  <line x1="160" y1="166" x2="160" y2="153" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
  <text x="160" y="178" text-anchor="middle" font-size="12" fill="currentColor">limit cycle</text>
</svg>
<figcaption>Trajectories cannot cross in two dimensions. An unstable fixed point pushes the flow
outward (spiral) while the trapping boundary of a Poincaré–Bendixson region pushes it inward; the
only place left for the flow to go is a closed orbit between the two — the limit cycle.</figcaption>
</figure>

It matters that this is a *two*-dimensional argument. The no-crossing property of trajectories holds
in any dimension, but in two dimensions it is an extremely strong constraint — a trajectory that
can't cross itself or any other trajectory has very little room to move. In three or more dimensions
there is a whole extra direction for trajectories to use to avoid each other, which is essentially why
chaotic behaviour in differential equations needs at least three dimensions.

## Linearizing around the fixed point

To find the stability of $p_0$, linearize. Write $\tilde m = m-m_0$, $\tilde p = p-p_0$ for small
deviations from the fixed point (with $m_0=p_0$), and take the Jacobian of $(\dot m,\dot p) =
(f(m,p),g(m,p))$ at that point:

$$A=\begin{pmatrix}\partial f/\partial m & \partial f/\partial p\\ \partial g/\partial m & \partial g/\partial p\end{pmatrix}_{(m_0,p_0)} = \begin{pmatrix}-1 & x\\ \beta & -\beta\end{pmatrix},\qquad x = \left.\frac{\partial}{\partial p}\!\left(\frac{\alpha}{1+p^n}\right)\right|_{p_0} = -\,\frac{n\alpha\,p_0^{\,n-1}}{(1+p_0^{\,n})^2} .$$

Note $x<0$ — repression is, well, repressive.

For a $2\times2$ system, the fixed point is stable exactly when the trace of $A$ is negative and the
determinant is positive (this trace/determinant shortcut is special to two dimensions; the general
rule, needed below, is that *every* eigenvalue must have negative real part). Here:

$$\operatorname{tr}A = -1-\beta < 0 \quad\text{always, since } \beta>0,$$
$$\det A = \beta - x\beta = \beta(1-x) > 0 \quad\text{always, since } x<0 \text{ makes } 1-x>1.$$

Both conditions hold for *every* choice of $\alpha$, $n$, $\beta>0$ — there is no parameter regime in
which this fixed point is unstable. So the two-variable (mRNA + protein) negative-autoregulation
model can never sustain a limit-cycle oscillation, for any parameters. That's a stronger statement
than the one-variable case, and unlike the one-variable case it required an actual calculation to see
— it isn't visible "for free." (Stability doesn't mean the approach to the fixed point is monotonic:
the eigenvalues could still be complex, giving a decaying, ringing approach. What's ruled out is a
*sustained* oscillation.)

## Limit cycles versus neutrally stable orbits

A limit cycle has a characteristic amplitude and period that don't depend on where you start — in
that sense it behaves like a stable fixed point, just for an orbit instead of a point, and this is
what makes limit-cycle oscillations the mathematically robust, "nice" kind. Contrast this with a
**neutrally stable orbit**, which shows up when the linearization gives purely imaginary eigenvalues:
the orbits then form closed loops around the fixed point whose *size depends on the initial
condition* — there's a whole family of them, not one preferred amplitude. These are considered less
interesting biologically because they are fragile: a small change to the model's parameters typically
turns them into decaying spirals, growing spirals, or genuine limit cycles. This is exactly the
character of the oscillations in the Lotka–Volterra predator–prey model, revisited later in the
course — not limit cycles, but neutrally stable orbits.

## What negative autoregulation needs in order to oscillate

None of this means negative autoregulation can never produce oscillations, experimentally or
computationally — only that the bare two-variable model above cannot. What's missing is delay. Two
ways to add it:

- **An explicit time lag** — make repression depend on the mRNA or protein level from some time in
  the past rather than the instantaneous level, reflecting the real time it takes to transcribe,
  translate, and fold a protein.
- **More intermediate steps** — mRNA is made, then a peptide chain, then the chain folds, then the
  folded proteins have to multimerize before they can repress. Writing all of these steps down
  explicitly raises the dimension of the system, and for reasonable parameters that alone can produce
  oscillations from nothing but negative autoregulation.

Jeff Hasty's group (UC San Diego) has spent roughly the last decade building exactly this kind of
delay-based single-gene oscillator in *E. coli*, moving back and forth between models and cells. One
thing modeling gets right immediately: **leakage** — residual expression even while the gene is
supposedly repressed — actively works against oscillation, so a good design uses especially tight
promoters with low leaky expression.

## The repressilator: Elowitz and Leibler's design

Elowitz and Leibler's question was whether you could actually *build* an oscillator by wiring
together components that had no history of working together, rather than repurposing something like
the circadian clock. Their design was a ring of three mutual repressors — call them $x$, $y$, $z$ —
with $x$ repressing $y$, $y$ repressing $z$, and $z$ repressing $x$. Before building it, they built a
model to guide the design: a week of thinking is cheaper than a year of experimental biology.

Two lessons the modeling gave them, both consistent with the discussion above:

1. **Match the lifetimes of mRNA and protein.** This plays the same role as the delay elements
   discussed above — if one species decays much faster than the other, the faster process effectively
   drops out of the dynamics. It's hard to lengthen an mRNA's lifetime much in bacteria, so instead
   they shortened the *protein* lifetime, by tagging the $x,y,z$ transcription factors for faster
   degradation.
2. **Minimize leakage.** They used synthetic promoters engineered for a large ratio of "on" expression
   to "off" (repressed) expression, since leakage inhibits oscillation.

**Bulk experiment.** They synchronized a population of cells with a pulse of IPTG and tracked
fluorescence from one of the three proteins. The population signal showed a single damped-looking
cycle rather than sustained oscillation. The explanation is desynchronization: individual cells'
oscillators start roughly in phase after the pulse, but random noise causes their phases to drift
apart over time, so an average over many out-of-phase single-cell oscillators looks like a damped
signal even if every individual cell keeps oscillating.

**Single-cell experiment.** Plating cells on an agar pad and imaging them individually as they
oscillated and divided settled the question: the cells really do oscillate — the first demonstration
that you could assemble unrelated regulatory parts into a working oscillator. But the oscillation was
far from clean: only about 40% of the cells showed clear oscillation, and even those had substantial
noise in period and amplitude. The paper attributes some of this to the low copy numbers of the
relevant genes and proteins, which makes the system intrinsically noisy (a stochastic effect that a
deterministic ODE model cannot capture). This observation is plausibly what pushed Elowitz toward a
later, more influential paper specifically about noise in gene networks — not required reading for
this course, but worth knowing it exists.

## The symmetric protein-only repressilator model

The full model — three mRNAs and three proteins — is a six-dimensional system, too large to work
through by hand in one sitting. Following the intuition-building move Elowitz himself used, simplify
to a **symmetric, protein-only** model: assume the three genes are identical (same $\alpha$, $n$, $K$),
even though in the real construct the three synthetic promoters differ.

$$\dot p_1 = \frac{\alpha}{1+p_3^{\,n}} - p_1,\qquad \dot p_2 = \frac{\alpha}{1+p_1^{\,n}} - p_2,\qquad \dot p_3 = \frac{\alpha}{1+p_2^{\,n}} - p_3 .$$

By symmetry the interior fixed point again has $p_1=p_2=p_3=p_0$ with $p_0=\alpha/(1+p_0^{\,n})$, the
same equation as before.

One caution before linearizing: with three variables there is no Poincaré–Bendixson theorem to fall
back on. The no-crossing argument that pinned two-dimensional flows down so tightly no longer applies
once there's a third direction available, so "the interior fixed point is unstable" does not
automatically imply "the system has a limit cycle" the way it did in two dimensions — that has to be
checked (e.g. by simulation), not assumed. It turns out to be true for this particular model, but that
is a fact about this model, not a general theorem.

The Jacobian, thanks to the cyclic symmetry, is the circulant matrix

$$A = \begin{pmatrix}-1 & 0 & x\\ x & -1 & 0\\ 0 & x & -1\end{pmatrix},\qquad x = -\,\frac{n\alpha\,p_0^{\,n-1}}{(1+p_0^{\,n})^2}$$

— the same $x$ as before, now coupling each protein to its repressor around the ring. Stability in
three dimensions requires every eigenvalue of $A$ to have negative real part (the trace/determinant
shortcut used earlier does not generalize). Expanding $\det(A-\lambda I)=0$ for this matrix, most of
the terms vanish and it collapses to the remarkably simple

$$(1+\lambda)^3 = x^3 .$$

Writing $\mu = 1+\lambda$, this equation has exactly three roots, equally spaced by $120°$ around a
circle of radius $|x|$ in the complex plane: since $x$ is real and negative, one root is $\mu=x$
itself, sitting on the negative real axis, and the other two form a complex-conjugate pair $120°$ away
from it on either side.

<figure>
<svg viewBox="0 0 360 260" role="img" aria-label="The three roots of (1+lambda) cubed equals x cubed sit 120 degrees apart on a circle, and stability depends on whether the complex pair lies left of the line Re(1+lambda) equals 1">
  <rect x="20" y="15" width="200" height="230" fill="currentColor" fill-opacity="0.12" stroke="none"/>
  <line x1="20" y1="130" x2="345" y2="130" stroke="currentColor" stroke-width="1.2"/>
  <text x="340" y="122" font-size="12" fill="currentColor">Re</text>
  <line x1="180" y1="15" x2="180" y2="248" stroke="currentColor" stroke-width="1.2"/>
  <text x="184" y="24" font-size="12" fill="currentColor">Im</text>
  <line x1="220" y1="15" x2="220" y2="248" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 3"/>
  <text x="224" y="30" font-size="11" fill="currentColor">Re(1+&#955;) = 1</text>
  <text x="224" y="44" font-size="11" fill="currentColor">(i.e. Re &#955; = 0)</text>
  <circle cx="180" cy="130" r="52" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="2 3" opacity="0.7"/>
  <line x1="180" y1="130" x2="128" y2="130" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
  <line x1="180" y1="130" x2="206" y2="85" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
  <line x1="180" y1="130" x2="206" y2="175" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
  <line x1="206" y1="85" x2="206" y2="130" stroke="currentColor" stroke-width="1" stroke-dasharray="1 2"/>
  <line x1="206" y1="175" x2="206" y2="130" stroke="currentColor" stroke-width="1" stroke-dasharray="1 2"/>
  <text x="212" y="60" font-size="11" fill="currentColor">Re = |x|/2</text>
  <circle cx="128" cy="130" r="3.5" fill="currentColor"/>
  <text x="128" y="148" text-anchor="middle" font-size="12" fill="currentColor">x</text>
  <circle cx="206" cy="85" r="3.5" fill="currentColor"/>
  <text x="212" y="82" font-size="12" fill="currentColor">x&#969;</text>
  <circle cx="206" cy="175" r="3.5" fill="currentColor"/>
  <text x="212" y="182" font-size="12" fill="currentColor">x&#969;&#178;</text>
</svg>
<figcaption>The shaded region is where the eigenvalue λ has negative real part. The real root µ=x
always lands in it; the complex pair sits at real part |x|/2, which crosses the stability line
Re(1+λ)=1 exactly when |x|=2 — the whole stability question for the ring reduces to this one number.</figcaption>
</figure>

To recover $\lambda$ itself, shift every point one unit to the left: $\lambda=\mu-1$. Stability needs
every $\mu$ to have real part less than 1. The real root $\mu=x$ is negative, so it's never a problem.
The complex pair sits at real part $|x|\cos 60° = |x|/2$ (the short side of a 30-60-90 triangle whose
hypotenuse is $|x|$). So the entire stability question comes down to comparing $|x|/2$ with $1$:

$$\text{stable (no oscillation)} \iff |x|<2, \qquad \text{unstable (oscillation)} \iff |x|>2 .$$

**Strong-expression limit ($\alpha\gg1$).** The fixed point condition $p_0(1+p_0^{\,n})=\alpha$ gives
$p_0^{\,n+1}\approx\alpha$. Substituting,

$$|x| = \frac{n\alpha\,p_0^{\,n-1}}{(1+p_0^{\,n})^2} \approx \frac{n\alpha\,p_0^{\,n-1}}{p_0^{\,2n}} = \frac{n\alpha}{p_0^{\,n+1}} \approx \frac{n\alpha}{\alpha} = n .$$

So $|x|\to n$ as $\alpha\to\infty$, and the stability condition $|x|<2$ collapses to $n<2$: **however
strong the expression, oscillation still requires cooperativity $n>2$.** This is not obviously
intuitive — one might expect strong enough expression on its own to be enough, and it isn't; raw
expression strength cannot substitute for cooperative repression. (There isn't a fully satisfying
intuitive explanation for this beyond it being a statement about the slopes of the repression curves
near the fixed point.)

**A concrete case, $\alpha=2$.** Here $p_0(1+p_0^{\,n})=2$ is solved by $p_0=1$ for *every* $n$, since
$1\cdot(1+1)=2$ regardless of $n$. At $p_0=1$, $x=-n\alpha/(1+1)^2=-n/2$, so $|x|=n/2$, and the
stability condition $|x|<2$ becomes $n<4$: with weaker maximal expression, oscillation now requires a
more strongly cooperative repressor, $n>4$.

## A trap: "any ring of repressors has to oscillate"

There's an appealing Boolean argument that seems to settle the question for free. Represent each gene
as simply on or off. Start at $(0,1,0)$: $y$ is on, repressing $z$ (already off); once $y$'s target
relaxes and $x$ turns on, you get $(1,1,0)$, and now $x$ starts repressing $y$, giving $(1,0,0)$ — and
tracking this through, the "on" state visibly marches around the ring forever. It looks like any three
mutually repressing genes are structurally guaranteed to oscillate.

The stability analysis above shows this is false. Without enough cooperativity — $n$ below the
threshold set by $|x|<2$ — the continuous system just relaxes to the symmetric interior fixed point
and stays there; no oscillation at all. Simply wiring up three mutual repressors is not sufficient. You
need transcription factors that actually multimerize and repress cooperatively, with a large enough
Hill coefficient, to have a real chance of getting the ring to oscillate.

## A methodological note: true, but not the mechanism

A natural follow-up question: doesn't cooperativity (multimerization) itself introduce a hidden delay,
since dimerizing takes some extra time after the monomer proteins are made? That may well be true of
real cells — but it is not what produces instability in *this* model, because the model as written
contains no time delay of any kind. Cooperativity here changes only the steepness of the repression
curve (how sharply the Hill function turns on), not any time lag. It's worth holding on to the general
point: a statement can be true of a real system and still not be the mechanism actually doing the
explanatory work in a specific piece of analysis. It is easy — and common — to conflate the two.

## Sources

- MIT 8.591J *Systems Biology* (Fall 2014), lecture recording transcript
  `computational-biology/mit-ocw/8591j-2014/recordings/recordings/xnnxlsy-f-s.md` (CC BY-NC-SA 4.0).
  Transcript-only source — no slides or board images were supplied, so every equation and figure
  above is reconstructed from what was said aloud (timestamps below), not copied from a board.
  - Motivation for oscillators, circadian aside: 00:00–03:32.
  - One-variable auto-repression model and the single-valuedness argument: 03:32–12:43.
  - Two-variable (mRNA + protein) model, non-dimensionalization, $\beta$: 12:43–22:31.
  - Poincaré–Bendixson, direction of rotation, noise-induced-oscillation aside: 22:31–24:56.
  - Fixed point, linearization, trace/determinant, stability result: 24:56–43:40.
  - Limit cycles vs. neutrally stable orbits, Lotka–Volterra aside, delay/leakage discussion: 43:40–47:22.
  - Repressilator design rationale and experiments (bulk and single-cell): 47:22–54:08.
  - Symmetric protein-only repressilator model, eigenvalues, complex-plane argument: 54:08–1:14:32.
  - Boolean-logic trap and the cooperativity/delay methodological aside: 1:14:32–1:21:09.
- **Named but not supplied as source material**, so not reproduced here beyond what was said about
  them: M.B. Elowitz and S. Leibler's repressilator paper (the paper under discussion throughout,
  including its stated design rationale, its own — reversed — definition of $\beta$, and its remark
  that "more realistic models may exhibit other complex types of dynamic behavior"); a later Elowitz
  paper on noise in gene networks (named as optional reading); Jeff Hasty's papers on delay-based
  single-gene oscillators in *E. coli*; the circadian-oscillator literature referenced in passing; the
  Lotka–Volterra predator–prey model (a forward reference to later in the course); the
  Poincaré–Bendixson theorem itself (used, but not cited to a text).

---

[← 23. Predator-Prey Cycles and Their Fragility](23-predator-prey-cycles-and-their-fragility.md) · [Contents](index.md)
