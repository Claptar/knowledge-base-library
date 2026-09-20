---
title: "5. Mathematical basis of stability analysis"
course: "MIT 8.591J 2004"
chapter: 5
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 5. Mathematical basis of stability analysis

## What this covers

This lecture does two things at once. First, it sets out a general recipe — nullclines,
linearization, and the trace/determinant test — for deciding whether a fixed point of a
two-variable system of nonlinear differential equations is stable. Second, it introduces the
system that recipe is about to be pointed at: chemotaxis in *Escherichia coli*, a signal
transduction pathway that has to act far faster than the genetic switches studied so far. The
chapter assumes the genetic-switch material from earlier lectures (the lysis–lysogeny decision
and the engineered toggle switch) and basic multivariable calculus — partial derivatives and
$2\times 2$ matrices. No transcript or exercise set was supplied for this lecture; the chapter is
built from the slides alone.

## Linear stability analysis for two-variable systems

Take a general system of two coupled, nonlinear ordinary differential equations,

$$\dot{x} = f(x,y), \qquad \dot{y} = g(x,y).$$

There is no general way to solve this exactly, but there is a standard way to ask a more modest
question: near a point where the system sits still, does a small perturbation die out or grow?
The answer only requires linear algebra, by the following six steps.

**Step 1 — nullclines and fixed points.** Set both derivatives to zero and solve simultaneously:

$$f(x_o,y_o) = 0, \qquad g(x_o,y_o) = 0.$$

Any $(x_o,y_o)$ solving both is a fixed point of the system.

**Step 2 — deviation variables.** Introduce the small displacement from the fixed point,

$$\tilde{x} \equiv x - x_o, \qquad \tilde{y} \equiv y - y_o.$$

**Step 3 — linearize.** Taylor-expand $f$ and $g$ around $(x_o,y_o)$ and keep only the linear
term (the fixed point itself contributes nothing, since $f=g=0$ there):

$$\dot{x} \approx \tilde{x}\left.\frac{\partial f}{\partial x}\right|_{(x_o,y_o)} + \tilde{y}\left.\frac{\partial f}{\partial y}\right|_{(x_o,y_o)} \equiv a\tilde{x} + b\tilde{y},$$
$$\dot{y} \approx \tilde{x}\left.\frac{\partial g}{\partial x}\right|_{(x_o,y_o)} + \tilde{y}\left.\frac{\partial g}{\partial y}\right|_{(x_o,y_o)} \equiv c\tilde{x} + d\tilde{y}.$$

**Step 4 — the Jacobian.** Collect the four partial derivatives into the matrix

$$A = \begin{bmatrix} a & b \\ c & d \end{bmatrix},$$

so that the linearized system is just $\dot{\tilde{x}} = A\tilde{x}$ (writing $\tilde{x}$ for the
vector $(\tilde{x},\tilde{y})$).

**Step 5 — trace and determinant.**

$$\tau = \operatorname{trace}(A) = a+d, \qquad \Delta = \det(A) = ad-bc.$$

**Step 6 — the stability test.** The fixed point $(x_o,y_o)$ is stable **only if**

$$\tau < 0 \quad \text{and} \quad \Delta > 0.$$

The lecture flags this explicitly as a two-dimensional fact only — it does not generalize to
three or more variables without more work.

### Why trace and determinant are enough

The test is a shortcut for a statement about eigenvalues, and it is worth seeing why. For a
$2\times 2$ matrix $A$ the two eigenvalues $\lambda_1,\lambda_2$ satisfy

$$\lambda_1+\lambda_2 = \tau, \qquad \lambda_1\lambda_2 = \Delta,$$

and the linearized fixed point is stable exactly when both eigenvalues have negative real part
(every solution of $\dot{\tilde x}=A\tilde x$ then decays). If $\Delta<0$ the eigenvalues are real
with opposite sign — one growing, one decaying direction, a saddle, unstable regardless of $\tau$.
If $\Delta>0$ the two eigenvalues are either both real with the *same* sign, or a complex
conjugate pair sharing one real part; either way that common sign is exactly the sign of their
sum $\tau$. So $\Delta>0$ together with $\tau<0$ forces both real parts negative, and stability
follows.

<figure>
<svg viewBox="0 0 320 240" role="img" aria-label="The trace-determinant plane with the stable region shaded where the trace is negative and the determinant is positive">
  <defs>
    <marker id="arrowA" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="20" y="20" width="140" height="100" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <line x1="20" y1="120" x2="300" y2="120" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowA)"/>
  <line x1="160" y1="220" x2="160" y2="20" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowA)"/>
  <text x="292" y="112" font-size="12" text-anchor="end" fill="currentColor">τ</text>
  <text x="168" y="30" font-size="12" fill="currentColor">Δ</text>
  <text x="35" y="45" font-size="12" fill="currentColor">stable</text>
  <text x="35" y="60" font-size="11" fill="currentColor">τ &#60; 0, Δ &#62; 0</text>
</svg>
<figcaption>The stability test lives entirely in the upper-left quadrant of the trace–determinant
plane: negative trace and positive determinant together pin both eigenvalues to negative real
part.</figcaption>
</figure>

## From genetic switches to protein switches

The previous lectures built two examples of genetic switches: the naturally occurring
lysis–lysogeny decision, and the engineered genetic toggle switch. Switches of this kind are how
a cell makes binary decisions — what to become in development and differentiation, what to eat in
metabolism, what to synthesize when building amino acids or other small molecules.

But genetic regulation has a built-in speed limit: transcription and translation take on the
order of ten minutes to hours. That is far too slow for behaviors that have to respond
immediately — finding food, chasing prey, or signal transduction in general. Genetics, as the
lecture puts it, is too slow.

The fix is to move the switch down a level: a **protein switch**, in which an existing protein
flips between an active and an inactive conformation. The total amount of protein (active plus
inactive) stays fixed on the relevant timescale, so gene expression can be ignored entirely — the
switch is purely a fast chemical modification of protein already present. That buys a timescale
of milliseconds to minutes, and the chapter's running example of one is chemotaxis in
*Escherichia coli*.

## E. coli chemotaxis: run, tumble, and temporal sensing

*E. coli* is a small cell — roughly 1–2 $\mu$m long and 0.5 $\mu$m in diameter — that swims by
rotating flagella. Its behavior alternates between two states:

- **run** — flagella rotate counterclockwise, bundle together, and propel the cell roughly in a
  straight line;
- **tumble** — flagella rotate clockwise, the bundle flies apart, and the cell reorients
  randomly.

In the absence of a chemical attractant, the cell alternates run and tumble more or less at
random, producing an unbiased random walk. In the presence of an attractant, the cell biases this
walk: it suppresses tumbling (extends runs) when things are getting better, and does not when
they are not. Because the cell is small enough that it cannot compare concentration across its
own length, the gradient is sensed **temporally** — by comparing the concentration now against
the concentration a few seconds ago — rather than spatially.

## The chemotactic signal-transduction pathway

The receptor for chemotaxis is Tar (other receptors, and other periplasmic binding proteins,
detect other attractants — maltose, galactose, glucose, ribose, dipeptides, Ni(II); Tar itself
also responds directly to aspartate, serine and citrate). Tar is permanently bound to the
histidine kinase **CheA** through an adapter protein **CheW**, which has no known enzymatic
activity of its own — a pure scaffold holding the kinase at the receptor.

### Phosphorylation: CheA, CheY, CheZ

Three reactions carry a phosphoryl group from the receptor to the flagellar motor and back:

$$\text{CheA} + \text{ATP} \;\rightleftharpoons\; \text{CheA-P} + \text{ADP} \qquad \text{(autophosphorylation)}$$
$$\text{CheA-P} + \text{CheY} \;\rightleftharpoons\; \text{CheA} + \text{CheY-P} \qquad \text{(phosphotransfer)}$$
$$\text{CheY-P} + \text{CheZ} \;\rightleftharpoons\; \text{CheY} + \text{CheZ-P} \qquad \text{(dephosphorylation)}$$

CheA autophosphorylates one of its histidines using ATP. CheA-P is unstable and hands its
phosphoryl group to CheY, which is small and highly soluble and diffuses freely through the
cytoplasm to the flagellar motor. CheY-P binds the motor switch protein FliM and drives clockwise
rotation — a tumble. CheZ runs the reaction the other way, dephosphorylating CheY-P.

The logic of the pathway is then:

- high CheA activity $\rightarrow$ high [CheY-P] $\rightarrow$ frequent tumbling;
- low CheA activity $\rightarrow$ low [CheY-P] $\rightarrow$ smooth, sustained running;
- high CheZ activity $\rightarrow$ low [CheY-P] $\rightarrow$ smooth running, working against CheA.

Ligand binding feeds into this at the very top: **unoccupied** receptors stimulate CheA
autophosphorylation. So an attractant binding the receptor lowers CheA activity, lowers [CheY-P],
and immediately suppresses tumbling.

<figure>
<svg viewBox="0 0 480 200" role="img" aria-label="The phosphoryl group moving from the receptor complex to the motor, and being removed again by CheZ">
  <defs>
    <marker id="arrowB" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="10" y="70" width="105" height="50" rx="6" fill="none" stroke="currentColor"/>
  <text x="62" y="90" font-size="11" text-anchor="middle" fill="currentColor">Tar receptor</text>
  <text x="62" y="106" font-size="11" text-anchor="middle" fill="currentColor">+ ligand</text>

  <rect x="155" y="70" width="105" height="50" rx="6" fill="none" stroke="currentColor"/>
  <text x="207" y="90" font-size="11" text-anchor="middle" fill="currentColor">CheA / CheA-P</text>
  <text x="207" y="106" font-size="9" text-anchor="middle" fill="currentColor">(CheW scaffold)</text>

  <rect x="300" y="70" width="100" height="50" rx="6" fill="none" stroke="currentColor"/>
  <text x="350" y="95" font-size="11" text-anchor="middle" fill="currentColor">CheY / CheY-P</text>

  <rect x="425" y="70" width="50" height="50" rx="6" fill="none" stroke="currentColor"/>
  <text x="450" y="90" font-size="10" text-anchor="middle" fill="currentColor">Motor</text>
  <text x="450" y="104" font-size="9" text-anchor="middle" fill="currentColor">tumble</text>

  <line x1="115" y1="95" x2="155" y2="95" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowB)"/>
  <text x="135" y="85" font-size="8" text-anchor="middle" fill="currentColor">sets rate</text>

  <line x1="260" y1="95" x2="300" y2="95" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowB)"/>
  <text x="280" y="85" font-size="8" text-anchor="middle" fill="currentColor">transfer</text>

  <line x1="400" y1="95" x2="425" y2="95" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowB)"/>
  <text x="412" y="85" font-size="7" text-anchor="middle" fill="currentColor">binds FliM</text>

  <rect x="300" y="150" width="100" height="35" rx="6" fill="none" stroke="currentColor"/>
  <text x="350" y="172" font-size="11" text-anchor="middle" fill="currentColor">CheZ</text>
  <line x1="350" y1="150" x2="350" y2="120" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowB)"/>
  <text x="378" y="138" font-size="8" text-anchor="middle" fill="currentColor">dephosphorylates</text>
</svg>
<figcaption>Occupied receptors slow CheA autophosphorylation; the phosphoryl group that does form
passes to CheY, whose phosphorylated form triggers a tumble at the motor, and CheZ removes it
again to reset the pathway.</figcaption>
</figure>

### Methylation: CheR, CheB, and its coupling to phosphorylation

A second, slower modification runs alongside phosphorylation: methylation of the receptor.
**CheR** constitutively adds methyl groups to Tar; **CheB-P**, the phosphorylated form of CheB,
removes them. Crucially, CheB's phosphorylation state is itself set by CheA — CheB is phosphorylated
by phosphotransfer from CheA-P, exactly as CheY is. So the same CheA activity that raises [CheY-P]
and drives tumbling also raises [CheB-P] and drives demethylation, coupling the fast
phosphorylation response to a slower methylation response running on the same input.

## What a quantitative model of chemotaxis has to reproduce

*E. coli* chemotaxis has been studied for roughly a century, but the lecture turns to a handful of
more recent, quantitative experiments as the target a mathematical model needs to hit: Alon et al.
(*Nature* 397, 168, 1999), Cluzel et al. (*Science* 287, 1652, 2000), and two papers by Sourjik and
Berg (*PNAS* 99, 123, 2002; *PNAS* 99, 12669, 2002). Between them they establish several facts a
model has to be built to match.

**Dynamic range and sensitivity.** *E. coli* senses aspartate over roughly five orders of
magnitude (10 nM to 1 mM) and can detect a change in concentration as small as 0.1%.

**An ultrasensitive motor switch.** Using a CheY–GFP fusion under an inducible promoter in a
strain lacking native CheY, CheZ and CheB — so that essentially all CheY present is phosphorylated
— the correlation between [CheY-P] and the motor's clockwise bias (its tumbling tendency) is
steep: a Hill coefficient of about 10. The switch itself is a sharp, ultrasensitive function of
its input.

**Direct measurement of the CheY–CheZ interaction.** A FRET (fluorescence resonance energy
transfer) assay between CheY-YFP and CheZ-CFP reports bound versus unbound CheY, since CheZ binds
only CheY-P. Adding attractant produces an immediate drop in the CheY-P–CheZ complex — i.e. an
immediate drop in [CheY-P] — and correspondingly less tumbling, tracking the phosphorylation logic
above directly.

**Large gain.** Receptor sensitivity measurements give an amplification of about 35 between
receptor occupancy and [CheY-P], and a further amplification of about 10 between [CheY-P] and the
motor response, for a total gain of roughly 350. A tiny fractional change in receptor occupancy is
turned into a large behavioral change, and a model of the pathway has to reproduce this gain — the
lecture flags receptor clustering as the likely mechanism, though it is not modeled here.

**Perfect adaptation.** A step change in attractant produces a fast excitation (a change in
tumbling within seconds, via phosphorylation) followed by a slow return to the pre-stimulus
tumbling frequency (via methylation), regardless of the new steady attractant level — the cell
adapts perfectly to a sustained stimulus and only transiently reports a change. This qualitative
property is **robust** to changes in the concentrations of the Che proteins themselves, even
though not every parameter of the response is; robustness of the adaptive behavior, specifically,
is what Alon et al. establish.

## Where this is heading: assumptions for the model to come

The next lecture builds a detailed kinetic model along the lines of Spiro, Parkinson and Othmer,
"A model of excitation and adaptation in bacterial chemotaxis" (*PNAS* 94, 7263–7268, 1997), whose
key unit is the ternary Tar–CheA–CheW complex, tracked through combinations of ligand occupancy,
methylation level, and phosphorylation state. To keep that state space manageable, the model
adopts a set of simplifying assumptions:

1. Tar is the only receptor type considered, and CheW and CheA are always bound to Tar — the
   receptor–kinase complex never falls apart.
2. Methylation sites are modified in a specific, fixed order.
3. Only the three highest methylation states are kept explicitly; lower states are neglected.
4. Only CheB-P (not unphosphorylated CheB) demethylates the receptor.
5. Phosphorylation of CheA does not affect ligand binding or unbinding.
6. CheR binding to the receptor does not affect ligand binding/unbinding or CheA phosphorylation.
7. CheZ is not itself regulated — its activity is taken as constant.
8. Phosphotransfer from the receptor complex to CheY or to CheB does not depend on the receptor's
   ligand-occupancy or methylation state.

Two further modeling facts sit alongside this list: ligand-bound receptor states generally have
*lower* autophosphorylation rates (consistent with the "unoccupied receptors stimulate CheA"
logic above), and CheR methylates ligand-bound states *more* rapidly. The transitions among the
model's states are also sorted into three speed classes — fast, intermediate, and slow — which is
what will let the coming model be reduced to a smaller, tractable set of dominant states. Once
that system of equations is written down, it is exactly the kind of two-variable (or reducible)
nonlinear system the six-step stability recipe at the top of this chapter was built to analyze.

## Sources

- Six-step stability-analysis recipe (nullclines, deviation variables, linearization, Jacobian,
  trace/determinant, the $\tau<0,\Delta>0$ test and its two-dimensional caveat): slide 1,
  `lectures/07-notes/01-mathematical-basis-of-stability-analysis.md`.
- Genetic-switch recap, the genetics-is-too-slow argument, and the protein-switch motivation
  (timescales, active/inactive states): same slide file.
- *E. coli* chemotaxis biology — cell dimensions, run/tumble, temporal sensing, the receptor and
  Che-protein pathway (CheA/CheW/CheY/CheZ phosphorylation, CheR/CheB methylation, role of ligand
  occupancy): slide 1, with the pathway diagram repeated on slide 2,
  `lectures/07-notes/02-chemotactic-pathway-in-e-coli.md`.
- Experimental section — methylation/tumbling correlation, sensing range and sensitivity, the
  CheY-GFP single-cell Hill-coefficient experiment, the CheY–CheZ FRET measurements, the gain
  figures (~35, ~10, ~350), and perfect adaptation and its robustness — slide 2, citing Alon et
  al. (*Nature* 397, 168, 1999), Cluzel, Surette and Leibler (*Science* 287, 1652, 2000), and
  Sourjik and Berg (*PNAS* 99, 123, 2002; *PNAS* 99, 12669, 2002).
- Modeling assumptions and the Tar–CheA–CheW complex as the model's basic unit: slide 3,
  `lectures/07-notes/03-assumptions.md`, drawing on Spiro, Parkinson and Othmer, "A model of
  excitation and adaptation in bacterial chemotaxis," *PNAS* 94, 7263–7268 (1997).
- No transcript, written notes, or exercise set was supplied for this lecture. The slide files
  themselves are model reconstructions of a PDF with no text layer (route: llm, fidelity:
  reconstructed); their prose is paraphrase and their equations are flagged by the source as
  unverified, so the reactions and formulas above should be checked against the original PDF or
  the cited papers before being treated as exact.
- Referred to but not contained in the slides: Alberts et al., *Molecular Biology of the Cell*,
  4th ed., ch. 13, cited as background reading on *E. coli* chemotaxis; and Falke, Bass, Butler,
  Chervitz and Danielson, "The two-component signaling pathway of bacterial chemotaxis," *Annu Rev
  Cell Dev Biol* 13, 457–512 (1997), the source of the pathway diagram reproduced in the slides.

---

[← 4. Molecular vs Systems Biology](04-molecular-vs-systems-biology.md) · [Contents](index.md) · [6. Excitation and Adaptation in Chemotaxis →](06-excitation-and-adaptation-in-chemotaxis.md)
