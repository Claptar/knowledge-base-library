---
title: "9. Robustness in Bacterial Chemotaxis"
course: "MIT 8.591J 2014"
chapter: 9
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 9. Robustness in Bacterial Chemotaxis

## What this covers

Bacterial chemotaxis: how *E. coli* biases its random walk toward attractants and away from
repellents, and why the mechanism it uses is a striking example of the course's running theme of
robustness. The chapter assumes the previous lecture's discussion of swimming at low Reynolds
number, and the earlier lecture on robustness in negative-autoregulatory gene circuits, which is
used here for comparison. It answers: what physically limits how a bacterium moves, why a
one-micron cell can respond to attractant concentrations spanning five orders of magnitude, and
how a genetic network can be built so that a key output is *exactly* independent of the
concentrations of its own components rather than merely insensitive to them.

## The puzzle: five orders of magnitude

The naive picture of chemotaxis is that the tumbling frequency is simply some function of the
local attractant concentration: more attractant, less tumbling. That picture would let a cell
climb a gradient, but only over a narrow range of concentrations — it saturates. Experimentally,
*E. coli* can respond to attractant concentrations spanning about five orders of magnitude, which
is a serious engineering problem for a cell one micron across.

The trick the cell uses is, in engineering language, close to integral feedback: the *steady-state*
tumbling frequency shows **perfect adaptation** — held at a constant attractant concentration, it
settles back to the same value regardless of what that concentration is. Only a *change* in
concentration moves it, transiently. This is already a form of robustness: robustness of the
tumbling frequency against the background level of attractant. What makes the system genuinely
subtle is that this perfect adaptation is itself robust to changes in the concentrations of the
network's own proteins (CheR, in particular). It is robustness of a robustness, and that is what
makes the example both the most elegant and the most confusing one in the course.

## Runs, tumbles, and the flagellar motor

The random walk is built from **runs** (roughly straight swimming, lasting on the order of a
second) alternating with **tumbles** (roughly a tenth of a second, during which the cell's
orientation is randomized). What changes with the gradient is the *frequency* of tumbling, i.e.
how long the runs last.

Mechanically: each cell has several flagella, with motors distributed over the whole body rather
than concentrated at one end. The individual filaments come together behind the cell into a single
corkscrew-shaped bundle. When all the motors spin counterclockwise, the bundle stays together and
drives the cell forward — a run. When one motor reverses to spin clockwise, the bundle falls apart
and the flagella move chaotically, randomizing the cell's orientation — a tumble. Swimming speed is
of order 30 microns per second; the motors themselves spin at roughly 100 hertz.

## How hard does a bacterium have to pull?

It is worth getting a feel for the forces involved, by the same low-Reynolds-number reasoning as
the previous lecture, where drag force is proportional to velocity rather than velocity squared.

**Scale of a molecular motor.** Many molecular motors — kinesin and myosin walking along
microtubules or actin — are powered by ATP hydrolysis, one molecule per step. The maximum force
such a motor can exert is bounded by energetics: it cannot do more mechanical work per step than
the free energy released by hydrolyzing the ATP that powers that step, or it would be a perpetual
motion machine. So force is of order $\Delta G_{\text{ATP}}/\Delta L$, where $\Delta L$ is the step
size. For kinesin, $\Delta G_{\text{ATP}}$ is of order 80–100 piconewton-nanometres and the step
size is about 8 nanometres, giving a force scale of order 10 piconewtons — the typical scale for a
single molecular motor.

**Force needed to swim.** How hard would you have to pull a bacterium to make it go 30 microns per
second through water? Using Stokes drag, $F = 6\pi\eta a v$ (the sphere result, with $a$ the
longest linear dimension and a shape-dependent prefactor for anything that isn't a sphere), and
plugging in water's viscosity, a cell radius of about a micron, and a speed of 30 microns per
second, the answer comes out well under one piconewton — the class's Fermi-estimate votes clustered
around far larger numbers before the calculation was done.

The punchline is the same one that "Life at Low Reynolds Numbers" makes about swimming at this
scale generally: moving through water a micron at a time costs almost nothing in force, so even a
motor that is very inefficient at converting chemical energy to work — Purcell's comparison, in
that reading, was to a fuel-guzzling car — is not a problem, because so little force is needed in
the first place. A single motor, or even a fraction of one, has force to spare. (Left genuinely
open in the lecture: how several independently spinning flagella, each forming a corkscrew, manage
not to tangle with each other as they come together into one bundle. It is not resolved by the
motors turning at the same rate, and no explanation offered in class was considered fully
satisfying — it was flagged as something the lecturer does not have a clean answer for.)

## Rotary motors in biology

The flagellar motor is powered by a proton gradient across the membrane and is, as far as is
known, the first rotary motor discovered in any living thing — and rotary motors remain rare in
biology generally, in sharp contrast to human engineering, where they are everywhere. The obvious
reason is mechanical: anything rigidly connected across a continuously rotating joint gets tangled.
Human engineering avoids this by never connecting anything solid across the rotation axis (a wheel
does not have a rod running through its own rim). Biology's version of this trick shows up only at
the molecular scale, where a rotor need not be joined to anything by a covalent bond running across
its axis of rotation — it can just be forced to rotate by the gradient acting on it directly.

The second well-known example is **$F_0F_1$ ATP synthase**: a ring embedded in the membrane that
rotates in response to a proton gradient, driving rotation of a separate part of the protein,
$F_1$, which then synthesizes ATP. The motor is reversible — the cell can also burn ATP to drive
rotation and pump protons the other way. This has been demonstrated directly in single-molecule
experiments: attaching a magnetic particle to $F_1$ and forcibly rotating it drives ATP synthesis
(with fairly low efficiency, since a macroscopic magnet is being spun to make individual ATP
molecules).

Other well-studied molecular motors — kinesin and the myosins, and, in a looser sense, DNA and RNA
polymerase — are not rotary at all: they walk along one-dimensional tracks (microtubules, actin, or
the template strand), converting chemical energy into linear steps rather than continuous rotation.

## Three ways to watch chemotaxis

Beyond simply applying a spatial gradient (a pipette of attractant or repellent) and watching cells
swim toward or away from it — qualitatively convincing, but hard to quantify — two other assays
give more controlled data:

- **Tethering a cell to a slide**, typically by the flagellar hook. Whatever the motor is doing
  (spinning clockwise or counterclockwise) is now directly visible, because the whole cell body
  rotates with it. The cell is simultaneously the thing sensing and processing the signal and the
  marker for the motor's state, giving high time resolution with straightforward image analysis.
- **A temporally, rather than spatially, varying stimulus.** Instead of a spatial gradient, simply
  add attractant and mix it uniformly, removing any spatial pattern the cells could respond to. A
  population's tumbling frequency can then be tracked over time without following individual
  cells. These two assays are typically combined: tethered cells subjected to a stimulus applied
  uniformly and suddenly in time.

Doing this and plotting tumbling frequency against time is what produces the classic
perfect-adaptation curve: starting from a steady-state frequency, adding attractant drops the
tumbling frequency sharply and quickly (cells behave as though they are moving up the gradient),
and then, over a much longer timescale — on the order of ten minutes, though this varies — the
frequency climbs back to exactly where it started. Adding a repellent does the mirror image: a
sharp rise in tumbling frequency followed by slow recovery back down. The feature the rest of the
chapter is about is that recovery: the dashed line the frequency returns to is identical to where
it began.

## The chemotaxis network

The protein names all begin with **Che** (chemotaxis) and were identified by genetics — screens for
mutants defective at chemotaxis. The lecture folds two of them together: **CheW** and **CheA**,
together with the membrane receptor itself, are referred to jointly as **X**. This receptor complex
sits in the membrane with a ligand-binding pocket facing outward, able to bind attractants or
repellents (there are several receptor variants tuned to different ligands). Binding an attractant
or repellent changes the receptor's **methylation state**. In reality a receptor can carry four or
five methylation sites; this lecture simplifies to just two states, unmethylated ($X$) and
methylated ($X_m$).

The core signalling reaction is that **X phosphorylates CheY**, and phosphorylated CheY (CheY-P) is
what increases tumbling frequency — it acts directly on the flagellar motor to favour clockwise
rotation. But CheY-P is not simply produced and left alone: it is constantly dephosphorylated by
**CheZ**. Likewise, X methylates and demethylates on its own constant cycle: **CheR** adds methyl
groups, and phosphorylated **CheB** (CheB-P) removes them. Both cycles — CheY phosphorylation and X
methylation — run continuously in both directions, which is metabolically wasteful (a "futile
cycle" in each case), and the lecture's implicit point is that this waste is the price of a signal
that can be reset quickly rather than only slowly built up from scratch.

## The fast response: an attractant lowers activity

"Activity" of X means the rate at which it phosphorylates both CheB and CheY. Tracing through the
logic: an attractant binds, activity of X goes down, so less CheY-P is made, so tumbling frequency
drops, so the cell keeps swimming in the same direction — consistent with having sensed that things
are getting better. A repellent does the reverse, transiently.

**What sets the timescale of this fast response is not chemistry but diffusion.** Phosphorylation,
binding, and unbinding between these proteins happen quickly — on the order of a tenth of a second
or faster. The receptors themselves are clustered at the pole (or poles) of the cell — clustering
that is believed, from both experiment and Ising-type cooperative models of the receptor array, to
increase sensitivity, though that is not developed further here. So CheY-P is made at the pole, but
the flagellar motors are spread around the whole cell body, and only one motor needs to switch to
trigger a tumble. The rate-limiting step for a cell that suddenly finds itself in a bad environment
to start tumbling is therefore **diffusion of CheY-P from the pole to a motor** — and diffusion of a
protein-sized object across a bacterial cell takes on the order of a tenth of a second, matching
the observed fast response time.

This is also why the ten-minute recovery timescale is *not* explained by new protein synthesis. New
protein synthesis (or active degradation) sets the characteristic timescale in transcriptional
networks — roughly the cell generation time — but the adaptation model here works even holding all
protein *concentrations* fixed. What changes over those ten minutes is not how much CheR or CheB
there is, but the covalent modification state of the receptor: how much of it is methylated versus
unmethylated. That state is what the rest of this chapter is about.

## Perfect adaptation as a flux-balance argument

Write $X$ for unmethylated receptor and $X_m$ for methylated receptor. CheR methylates X, and it is
assumed to act **at saturation**: the rate at which CheR adds methyl groups does not depend on how
much unmethylated X is present (no Michaelis–Menten term for the substrate), only on how much CheR
there is — equivalent to saying the unmethylated substrate concentration is far above CheR's
Michaelis constant. CheB-P demethylates $X_m$, and this reaction *is* written with an explicit
Michaelis–Menten dependence on $X_m$ — CheB is not saturated.

<figure>
<svg viewBox="0 0 420 230" role="img" aria-label="Cycle between unmethylated and methylated receptor, showing the flux imbalance behind perfect adaptation">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="95" cy="115" r="48" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="95" y="110" text-anchor="middle" font-size="13" fill="currentColor">X</text>
  <text x="95" y="128" text-anchor="middle" font-size="11" fill="currentColor">unmethylated</text>
  <circle cx="325" cy="115" r="48" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="325" y="110" text-anchor="middle" font-size="13" fill="currentColor">Xm</text>
  <text x="325" y="128" text-anchor="middle" font-size="11" fill="currentColor">methylated, active</text>
  <path d="M 128 78 C 200 40, 220 40, 292 78" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#arr)"/>
  <text x="210" y="35" text-anchor="middle" font-size="12" fill="currentColor">CheR — saturated, ~fixed rate</text>
  <path d="M 292 155 C 220 195, 200 195, 128 155" fill="none" stroke="currentColor" stroke-width="1.6" marker-end="url(#arr)"/>
  <text x="210" y="212" text-anchor="middle" font-size="12" fill="currentColor">CheB-P — rate proportional to activity</text>
</svg>
<figcaption>An attractant lowers the receptor's activity, which lowers the CheB-P-driven flux back
to X (bottom) while CheR's saturated flux (top) stays fixed. The resulting net drift toward Xm
raises the active fraction, and hence activity, until the two fluxes balance again — that return
to balance is perfect adaptation.</figcaption>
</figure>

An attractant lowers X's activity — and, crucially, the *same* activity phosphorylates both CheY
and CheB. So the moment an attractant binds, both CheY-P (driving the fast response) and CheB-P
drop together. Less CheB-P means less flux flowing from $X_m$ back to $X$ (the bottom arrow), while
CheR's flux from $X$ to $X_m$ (the top arrow, saturated, so essentially unaffected by any of this)
stays the same. The two fluxes, which were balanced at steady state, are now unbalanced, and
$X_m$ accumulates. In this simplified model only the methylated receptor carries any activity, so
as $X_m$ builds up, activity rises back toward its earlier level — this build-up is the slow,
roughly ten-minute recovery.

Coming back up, however, is not the same as coming back up to *exactly* the same value — perfect
adaptation is a much stronger claim than mere recovery, and getting it requires more than what has
been said so far.

## Two models: fine-tuned versus robust

**The fine-tuned model** is the version just described, with no further assumption: CheB-P acts on
the methylated pool via ordinary Michaelis–Menten kinetics. This model *can* be made to show
perfect adaptation, but only for particular, matched values of all the relevant rate constants and
protein concentrations (CheR, CheB, and so on). The problem is inherent to fine-tuning: get the
parameters right for one set of concentrations, and adaptation is exact; change any one of them —
CheR's concentration, say — and the balance point moves, and the system is no longer tuned for the
new concentrations. It was only ever fine-tuned for the world it was built in.

**The robust model** changes one assumption, and the change looks almost too simple to matter: it
supposes the methylated receptor is rapidly flipping, on a timescale far faster than anything else
in the network (microseconds), between an "active" conformation and an "inactive" one, and that
**CheB-P only demethylates the active conformation**. Binding an attractant or repellent works by
shifting this fast conformational equilibrium — the fraction of time spent active — and that active
fraction *is* what "activity" means throughout. The demethylation rate is now proportional to
activity itself, not merely to the total amount of methylated receptor.

This one change is equivalent to integral feedback and gives *exact* perfect adaptation for any
values of the rate constants, not just matched ones: at steady state, the (activity-proportional)
demethylation flux must balance the (saturated, essentially fixed) methylation flux, and that
balance condition pins down the steady-state activity to a single value that never involves the
background attractant concentration at all. Change CheR's concentration and the fluxes both change,
but the balance point — hence the qualitative property of returning exactly to where it started —
does not depend on having gotten CheR's concentration "right."

The lecture is honest about the cost of this move: positing a rapid, largely unobservable
conformational switch between active and inactive methylated states is not something you can prove
directly, since it is happening on a timescale where individual molecular fluctuations are hard to
resolve experimentally. What can be shown is that the *rate of demethylation tracks activity*, which
is consistent with the model without nailing it down completely.

## Testing the robust model

Barkai and Leibler, in a 1997 *Nature* paper (Barkai was a postdoc in Stan Leibler's lab at the
time), argued theoretically — guided by earlier observations rather than new experiments — that a
robust perfect-adaptation model needs exactly this feature. Two years later, Uri Alon, also a
postdoc in Leibler's lab, tested the prediction directly: he put CheR under an inducible promoter
and used IPTG to control its mean concentration across a population, then measured how three things
depended on it — the steady-state tumbling frequency, the adaptation time, and the degree to which
adaptation was exact.

The results matched the robust model's predictions. More CheR drives both fluxes around the
methylation cycle faster, which does two things: it raises the steady-state activity (more CheY-P,
so a higher baseline tumbling frequency), and it shortens the adaptation time, since a faster cycle
reaches its new balance point sooner. Both the baseline frequency and the adaptation time therefore
*do* depend on CheR concentration — they are not robust. But the perfect adaptation itself — the
fact that, whatever the baseline was, the system returns exactly to it — held regardless of CheR
concentration. The model made a sharp, falsifiable prediction about which things should be robust
and which should not, and going and making the strains to test it is a genuine case of a model
driving new measurements rather than explaining old ones after the fact.

## A simpler robustness example, for comparison

An earlier lecture's example is worth returning to whenever chemotaxis's robustness gets confusing,
because it isolates the same idea with far less machinery: a protein $x$ that negatively
autoregulates its own production. Degradation is linear, $\alpha x$; in the limit of very sharp
negative autoregulation, production is close to a step function of height $\beta$ that falls to
zero once $x$ passes some threshold $k$. The steady-state concentration — where production and
degradation curves cross — sits at $x^* \approx k$.

This steady state is **robust to $\alpha$** (which only sets the slope of the degradation line, not
where it crosses the step) and **robust to $\beta$** (which only sets the height of the production
step, and in the sharp limit barely moves the crossing point), but it is **not robust to $k$**
(which sets the location of the step directly, so the crossing point tracks it). The general lesson
this is meant to illustrate: a robust quantity is never robust to everything, and it is worth being
precise about which perturbations a network is built to absorb and which one it necessarily still
tracks.

## Non-genetic individuality

Even a population of genetically identical *E. coli* does not show one tumbling frequency: measure
$f_1, f_2, \dots, f_n$ across $n$ clonal cells and they differ. The reason is the same flux-balance
picture, run on cell-to-cell variation rather than an experimenter's titration: protein copy numbers
fluctuate naturally, and CheR is present at only around 100 copies per cell — a small enough number
that the relative fluctuations are large. That variation propagates, exactly as the CheR-titration
experiment showed, into variation in baseline tumbling frequency and in adaptation time — but not
into whether adaptation is perfect, since each cell still returns to its own baseline exactly.

This was observed as early as 1976, in a paper by Jim Spudich and Dan Koshland in *Nature*, "Non-
genetic individuality: chance in the single cell." Some cells were "twitchy" — higher tumbling
frequency, shorter runs, changing their minds often — while nominally identical cells were more
"relaxed," with much longer runs. The timescale over which an individual cell's "personality"
should persist is roughly the **cell generation time**, since it tracks protein numbers such as
CheR that are themselves inherited, imperfectly, from a mother cell to its daughters — not unlike a
parent passing on some, but not all, of a personality to a child.

## Sources

- MIT 8.591J (Fall 2014), lecture recording `ct855rpx8bc` (Jeff Gore), transcript only — no slides,
  written notes, or problems were supplied for this lecture. Timestamps below refer to that
  transcript.
  - Puzzle of five-orders-of-magnitude sensing and perfect adaptation: 00:00–03:28.
  - Runs, tumbles, flagellar mechanics: 03:28–08:16.
  - Force-scale estimate for molecular motors and for swimming: 08:16–18:24.
  - Rotary motors, flagellar motor, ATP synthase: 18:24–27:22.
  - Assays for studying chemotaxis (spatial, tethered, temporal): 27:22–33:37.
  - Network components and naming (CheA/B/R/W/Y/Z), fast response, rate-limiting diffusion step:
    33:37–50:00.
  - Fine-tuned model, saturation assumption, flux-balance derivation: 50:00–1:00:14.
  - Robust model (active/inactive conformational switch), CheR titration experiment: 1:00:14–1:11:17.
  - Non-genetic individuality: 1:11:17–1:15:45.
  - Negative-autoregulation robustness recap: 1:15:45–1:18:04.
- **Referred to but not contained in this transcript:**
  - The previous lecture ("Thursday") on "Life at Low Reynolds Numbers," including the Purcell
    reading and its comparison of an inefficient swimmer to a fuel-hungry car in an oil-rich
    country — used here only by reference, for the point about force and efficiency at this scale.
  - The course textbook ("Uri's book" / "your book"), for its worked fine-tuned-model example, its
    discussion of what is rate-limiting in the network, and its EM reconstruction of the flagellar
    motor structure — none of these are reproduced in the transcript.
  - Barkai, N. and Leibler, S., *Nature* (1997) — theoretical proposal of the robust adaptation
    condition.
  - Alon, U. (and colleagues, in Leibler's lab, roughly two years after the 1997 paper) — the CheR-
    titration experiment testing the robust model's predictions.
  - Spudich, J. and Koshland, D., "Non-genetic individuality: chance in the single cell," *Nature*
    (1976).
  - Ising-type cooperative models of receptor clustering at the cell pole, mentioned as existing
    work on why clustering increases sensitivity, not developed in this lecture.
  - A whiteboard diagram of the full chemotaxis network (labelled with R, B, Z, Y, W, A) that the
    lecture refers to throughout as "up on the board" — its content is described in prose above but
    the diagram itself was not captured.

---

[← 8. Virulence Evolution and the Red Queen](08-virulence-evolution-and-the-red-queen.md) · [Contents](index.md) · [10. Single Molecules and Protein Bursts →](10-single-molecules-and-protein-bursts.md)
