---
title: "2. Cooperativity and the Lambda Switch"
course: "MIT 8.591J 2004"
chapter: 2
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 2. Cooperativity and the Lambda Switch

## What this covers

Lecture 2 built a general toolkit for equilibrium binding — the Adair equation, detailed
balance, and a vocabulary for cooperativity ($\beta$, the Hill number). This lecture opens by
finishing that toolkit and then spends it immediately on a real switch: the decision, inside a
newly infected bacterium, between the phage lysing its host and lying dormant as a lysogen. The
question the second half answers is deliberately the one on the lecturer's own slide — *how do
you build a mathematical model that captures the essence of the switch?* — and the binding
machinery from the first half is exactly what that model is made of. The chapter assumes the
Michaelis–Menten scheme and the idea of a quasi-steady state are already familiar; both are
recapped only as far as needed to reuse them.

## Michaelis–Menten kinetics: the three regimes

The enzyme scheme is the usual reversible binding step followed by irreversible product release,

$$E + S \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} ES \xrightarrow{k_2} E + P,$$

with mass-action kinetics for each species and enzyme conserved, $E_o = [E] + [ES]$:

$$\frac{d[S]}{dt} = -k_1 E_o[S] + (k_1[S] + k_{-1})[ES], \qquad
\frac{d[ES]}{dt} = k_1 E_o[S] - (k_1[S] + k_{-1} + k_2)[ES],$$

started from $[S] = S_o$, $[E]=E_o$, $[ES]=[P]=0$. Plotted against time, the concentrations pass
through three regimes: a brief **transient** in which $[ES]$ builds up from zero; a **quasi-steady
state** in which $[ES]$ has equilibrated on the timescale of $[S]$'s slower decay, so
$d[ES]/dt \approx 0$ while $[S]$ is still changing; and, once enough substrate is consumed,
**substrate depletion**, where $[ES]$ and $v$ fall away as $[S]\to 0$.

The quasi-steady-state assumption is what makes the scheme tractable: setting $d[ES]/dt = 0$ in
the equation above gives $k_1 E_o[S] = (k_1[S] + k_{-1} + k_2)[ES]$, so

$$[ES] = \frac{E_o[S]}{[S] + K_m}, \qquad K_m \equiv \frac{k_{-1}+k_2}{k_1},$$

and the initial velocity $v_0 = k_2[ES]$ becomes the familiar

$$v_0 = \frac{V_{\max} S_o}{K_m + S_o}, \qquad V_{\max} = k_2 E_o.$$

This is a *good* approximation only when $S_o \gg E_o$: the quasi-steady state has to be reached
while almost none of the substrate has yet been consumed, so that $[S]$ at the start of that
regime is still essentially $S_o$. If enzyme and substrate are comparable in concentration, the
transient and the steady state overlap and the formula is no longer trustworthy.

## Equilibrium binding: the Adair equation and detailed balance

The second topic is a ligand $S$ binding a protein with $n$ sites, one at a time,

$$S + P_{j-1} \leftrightharpoons P_j, \qquad j = 1,\dots,n,$$

where $P_j$ is the species with $j$ ligands bound. The **macroscopic association constant**
$K_j = [P_j]/([P_{j-1}][S])$ describes the step from $j-1$ to $j$ ligands bound, without saying
anything about which of the $n$ sites is occupied. The average number of ligands bound per
protein, $r$, is the ligand-weighted average over all $n+1$ species, which gives the **Adair
equation**:

$$r = \frac{K_1[S] + 2K_1K_2[S]^2 + 3K_1K_2K_3[S]^3 + \dots + nK_1K_2\cdots K_n[S]^n}
{1 + K_1[S] + K_1K_2[S]^2 + \dots + K_1K_2\cdots K_n[S]^n}.$$

Why $K_j$ can be read off directly from rate constants — $K_j = k_{+j}/k_{-j}$ — is a **detailed
balance** argument, not an assumption. Write the chain of binding steps

$$P_o \underset{k_{-1}}{\overset{k_{+1}}{\rightleftharpoons}} P_1 \underset{k_{-2}}{\overset{k_{+2}}{\rightleftharpoons}} P_2 \ \cdots\ P_{n-1}\underset{k_{-n}}{\overset{k_{+n}}{\rightleftharpoons}} P_n,$$

and set $d[P_o]/dt = 0$ at equilibrium: $-k_{+1}[P_o][S] + k_{-1}[P_1] = 0$, so
$K_1 = k_{+1}/k_{-1} = [P_1]/([P_o][S])$ immediately. Substituting that into $d[P_1]/dt = 0$
cancels the two terms already balanced by the first equation, leaving
$-k_{+2}[P_1][S] + k_{-2}[P_2] = 0$ on its own — the second step balances independently of the
first. The pattern repeats down the chain: each step is separately at equilibrium, and each
$K_j$ is exactly the ratio of its own forward and backward rate constants, with no cross terms
from neighbouring steps.

## Three toy models for two-site binding

Three small cases show what the Adair equation does with a specific mechanism plugged in, and
they are the ones reused later on the phage operator.

**I. Identical, independent sites.** Two identical sites, each with intrinsic constant
$K = k_+/k_-$. Statistics alone changes the macroscopic constants: there are two ways to bind the
first ligand but only one way to lose it from a singly-bound protein, so $K_1 = 2K$; conversely
there is only one empty site left for the second ligand but two ways to vacate a doubly-bound
protein, so $K_2 = K/2$. The Adair equation collapses to

$$r = \frac{2K[S] + 2K^2[S]^2}{1 + 2K[S] + K^2[S]^2} = \frac{2K[S]}{1+K[S]},$$

which is exactly the hyperbolic isotherm of a single site, scaled by two — independence is what
lets it factor cleanly.

**II. Non-identical, independent sites.** Two distinct sites with their own constants $K$ and
$K^*$, still not interacting, simply add:

$$r = \frac{K[S]}{1+K[S]} + \frac{K^*[S]}{1+K^*[S]}.$$

**III. Identical, interacting sites.** Now the two sites are chemically identical but the
occupancy of one changes the affinity of the other: $K_1 = 2K$ as before, but the second step
carries a different intrinsic constant $K^* = k_+^*/k_-^*$, so $K_2 = K^*/2$. The Adair equation
becomes

$$r = \frac{2K[S] + 2KK^*[S]^2}{1 + 2K[S] + KK^*[S]^2}.$$

<figure>
<svg viewBox="0 0 420 150" role="img" aria-label="Three occupancy states of a two-site protein, with the macroscopic rate constants linking them.">
  <circle cx="60" cy="80" r="30" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="60" y="84" text-anchor="middle" font-size="12" fill="currentColor">0 bound</text>
  <circle cx="215" cy="80" r="30" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="215" y="84" text-anchor="middle" font-size="12" fill="currentColor">1 bound</text>
  <circle cx="370" cy="80" r="30" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="370" y="84" text-anchor="middle" font-size="12" fill="currentColor">2 bound</text>
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="92" y1="72" x2="183" y2="72" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr)"/>
  <text x="137" y="60" text-anchor="middle" font-size="12" fill="currentColor">K1 = 2K</text>
  <line x1="247" y1="72" x2="338" y2="72" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr)"/>
  <text x="292" y="60" text-anchor="middle" font-size="12" fill="currentColor">K2 = K*/2</text>
</svg>
<figcaption>The two-site interacting model (case III): the second binding step carries its own
intrinsic constant K*, so the ratio K2/K1, or equivalently β = K*/K, measures whether the second
ligand binds more or less readily once the first is already there.</figcaption>
</figure>

## Reading cooperativity off the isotherm

Case III is the one that matters, because it is the minimal model with cooperativity in it.
Writing $r$ as a fractional saturation $Y = r/2$ (out of a maximum of two sites), substituting
$x = K[S]$ and $\beta = K^*/K$, and using $KK^*[S]^2 = (K[S])(K^*[S]) = \beta x^2$ collapses the
case-III expression to

$$Y = \frac{x(1+\beta x)}{1 + 2x + \beta x^2}.$$

$\beta$ is the whole story of cooperativity here: $\beta > 1$ means the second ligand binds more
readily once the first is bound (**positive cooperativity**), $\beta < 1$ means it binds less
readily (**negative cooperativity**), and $\beta = 1$ recovers the independent case. The
curvature of $Y(x)$ tracks this: differentiating twice shows the sign of $Y''$ at $x=0$ is the
sign of $\beta - 2$. For $\beta \le 2$ the curve is concave for every $x \ge 0$ — a plain
saturating hyperbola. For $\beta > 2$, $Y$ is convex near $x=0$ and concave for large $x$, which
forces an inflection point in between: that inflection is what makes the curve **sigmoidal**, and
$\beta = 2$ is exactly the threshold at which it first appears. The slide's plot of the effective
Hill number $n_H(x)$ for $\beta = 1, 2, 10, 100$ traces the same fact from a different angle: at
$\beta=1$, $n_H\equiv 1$ everywhere (no cooperativity to detect); as $\beta$ grows, $n_H$ rises
above 1 near the midpoint of the transition and the isotherm sharpens, approaching — without
reaching, for a real, finite dimer — the ideal step-function response of a perfectly cooperative
site.

## From binding polynomials to a genetic switch

That machinery is the whole content of Lecture 2. This lecture puts it to work on a specific
molecular decision: bacteriophage $\lambda$, a virus with a $48{,}512$-base-pair genome, injects
its DNA into *E. coli* and then has to choose between two fates. Immediately after injection,
phage genes are transcribed and translated using the host's own machinery; **which set of phage
proteins gets expressed decides the outcome** — lysis (the phage replicates and kills the host
cell) or lysogeny (the phage genome is retained, quiescent, inside the host chromosome). A
lysogen is immune to a second infection: repressor dimers already present bind the incoming
phage's DNA and shut its genes off, and it is a high, steady concentration of repressor that
keeps the cell in the lysogenic state. (Source: Ptashne, *A Genetic Switch: Phage Lambda*, 3rd
ed., Cold Spring Harbor Laboratory Press, 2004 — the images the lecture showed here are not
reproduced in the converted slides.)

## The operator OR: three sites, three control logics

The decision is written into a short stretch of DNA, the right operator $O_R$, which contains
three repressor-binding sites — $O_{R}3$, $O_{R}2$, $O_{R}1$ — sandwiched between two promoters
that run in opposite directions: $P_{RM}$ (leftward, transcribing the repressor gene $cI$) and
$P_R$ (rightward, transcribing $cro$). The key physical fact is that **only one RNA polymerase
fits over this region at a time** — repressor and polymerase compete for overlapping or adjacent
space, so a repressor dimer parked on one site can block, or in one case help, polymerase at a
promoter several base pairs away.

<figure>
<svg viewBox="0 0 460 170" role="img" aria-label="The lambda right operator: three repressor-binding sites between two promoters running in opposite directions.">
  <text x="55" y="30" text-anchor="middle" font-size="12" fill="currentColor">cI</text>
  <line x1="20" y1="55" x2="80" y2="55" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr2)"/>
  <text x="90" y="58" font-size="11" fill="currentColor">P_RM</text>
  <defs>
    <marker id="arr2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M10,0 L0,5 L10,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="150" y="90" width="50" height="34" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="175" y="111" text-anchor="middle" font-size="12" fill="currentColor">OR3</text>
  <rect x="205" y="90" width="50" height="34" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="230" y="111" text-anchor="middle" font-size="12" fill="currentColor">OR2</text>
  <rect x="260" y="90" width="50" height="34" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="285" y="111" text-anchor="middle" font-size="12" fill="currentColor">OR1</text>
  <text x="380" y="58" font-size="11" fill="currentColor">P_R</text>
  <line x1="360" y1="55" x2="420" y2="55" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr3)"/>
  <defs>
    <marker id="arr3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <text x="420" y="30" text-anchor="middle" font-size="12" fill="currentColor">cro</text>
  <text x="230" y="150" text-anchor="middle" font-size="11" fill="currentColor">only room for one RNA polymerase</text>
</svg>
<figcaption>The right operator OR sits between the two promoters it controls: repressor bound
here can block RNAp at P_R, block or help RNAp at P_RM, depending on which of the three sites it
occupies.</figcaption>
</figure>

With a single repressor dimer bound, the slides give three cases, one per site:

- **Dimer at $O_{R}2$**: *negative* control of $P_R$ (blocks RNAp from transcribing $cro$) and
  *positive* control of $P_{RM}$ (a dimer here actually helps RNAp bind and transcribe $cI$).
- **Dimer at $O_{R}1$**: *negative* control of $P_R$, and — on its own — a weak negative effect on
  $P_{RM}$ too, since $O_{R}1$ is too far from $P_{RM}$ for a lone dimer there to help it directly.
- **Dimer at $O_{R}3$**: *negative* control of $P_{RM}$ (blocks the repressor's own gene) and
  *positive* control of $P_R$ (a dimer here actually allows RNAp to transcribe $cro$).

## Cooperative binding makes the two genes take turns

The three-toy-model section is not incidental background: repressor's binding across $O_{R}1$,
$O_{R}2$, $O_{R}3$ is exactly case III, generalized to three sites. The intrinsic constants for
repressor decrease roughly tenfold from site to site, $K_{O_R1} \sim 10\,K_{O_R2} \sim
10\,K_{O_R3}$ — $O_R1$ is bound first on affinity alone — but the cooperative constant for the
second step is far larger than the intrinsic one, $K^*_{O_R2} \gg K_{O_R2}$: once a dimer sits at
$O_R1$, a second dimer at the adjacent $O_R2$ is strongly favoured by direct protein–protein
contact between the two dimers. At the low repressor concentrations that hold in a stable
lysogen, $O_R1$ and $O_R2$ are effectively filled together — turning $P_R$ off and $P_{RM}$ on —
while $O_R3$ stays empty. Only once repressor accumulates further does it also occupy $O_R3$,
which shuts down $P_{RM}$: the repressor gene turns off its own promoter, capping how much
repressor gets made. That is the **negative feedback** the slides point to for keeping
$[\text{repressor}]$ at a steady level in the lysogenic state, and it is disturbed when the
switch is thrown by UV damage.

Cro, the protein whose accumulation drives the cell toward lysis, binds the same three sites
non-cooperatively and with the *opposite* preference: $K_{O_R3} \sim 10\,K_{O_R2} \sim
10\,K_{O_R1}$, so Cro fills $O_R3$ first (case II's independent-sites picture, not case III) —
shutting off $P_{RM}$ and repressor synthesis directly, without needing the cooperative assist
that repressor relies on to reach $O_R2$.

## Why cooperativity: a sharp, all-or-nothing decision

The slides compare percent repression against repressor concentration for a single, isolated
operator versus the full $\lambda$ $O_R$ system, and separately compare an isotherm with Hill
number $n_H=1$ against one with $n_H=3$: the cooperative system switches over a much narrower
range of repressor concentration than a single non-cooperative site would. The lecture's own
gloss on why is that the switch stacks **several layers of cooperativity** on top of one another
— repressor first has to dimerize (itself a cooperative step, two monomers to one active binding
unit), and the dimers then bind $O_R1$–$O_R2$ cooperatively as above. Each layer sharpens the
response further, which is what turns a graded, analog binding curve into something closer to a
genuine switch: a cell is pushed toward one committed fate rather than settling on some
intermediate mixture of both.

## Where the model goes next

The lecture closes by posing, without yet answering, the question that motivates building an
actual dynamical model of this switch: *how do you turn this binding picture into a model that
predicts which fate a given cell takes?* It points to the mechanism of that model rather than
building it here, citing Arkin, Ross, and McAdams, "Stochastic kinetic analysis of developmental
pathway bifurcation in phage $\lambda$-infected *Escherichia coli* cells," *Genetics* 149(4)
(1998): 1633–48 — a full stochastic treatment of exactly this decision, left as a pointer for
where the course goes next rather than material covered in this lecture.

## Sources

- Slides: `01-review-lecture-2.md` (Michaelis–Menten kinetics; Adair equation; detailed balance;
  the three two-site binding models; cooperativity and the Hill number; introduction to phage
  biology and the lysis–lysogeny decision) and `02-the-lysis-lysogeny-decision-is-a-genetic-switch.md`
  (the $O_R$ operator, the three single-dimer cases, repressor and Cro binding cooperativity,
  and the closing pointer to a mathematical model), both from *8.591J Systems Biology* (MIT OCW,
  Fall 2004), lecture 3 notes.
- No transcript, written notes, or exercise set was supplied for this lecture; the exposition
  above is built from the slides alone. Both slide files are a model's reconstruction of a PDF
  with no extractable text layer, and each carries its own fidelity note flagging every displayed
  equation as unverified against the original — treat the equations here as a faithful-effort
  transcription rather than a checked source.
- Named but not contained in the slides: Ptashne, *A Genetic Switch: Phage Lambda*, 3rd ed. (Cold
  Spring Harbor Laboratory Press, 2004), the source of the phage and operator diagrams the images
  were removed from; and Arkin, Ross & McAdams, *Genetics* 149(4) (1998): 1633–48, cited as where
  a full model of the switch is built.

---

[← 1. Introduction to Systems Biology](01-introduction-to-systems-biology.md) · [Contents](index.md) · [3. The Lambda Phage Bistable Switch →](03-the-lambda-phage-bistable-switch.md)
