---
title: "10. Single Molecules and Protein Bursts"
course: "MIT 8.591J 2014"
chapter: 10
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. Single Molecules and Protein Bursts

## What this covers

How do you watch a single protein molecule fluoresce inside a living cell, and how do you turn
that observation into a count of how many protein molecules a gene made in one go? The lecture
works through both questions using a single 2006 paper from Sunney Xie's lab, which was the first
to get single-molecule fluorescence measurements working *inside* live bacteria rather than in a
purified, in-vitro sample. It assumes you can already think in orders of magnitude, that you know
what a diffraction limit and a Stokes shift are, and that you have at least seen the exponential,
geometric and Poisson distributions before (they get a proper treatment the following lecture).

## Why live-cell single-molecule fluorescence was thought impossible

Before this paper, single-molecule biophysics — both fluorescence detection and mechanical
manipulation of single molecules — was almost exclusively an in-vitro technique: purified
components on a glass slide, not inside a living cell. That gave real insight into the dynamics of
molecular motors, transcription and translation, but doing the analogous experiment inside a living
cell was widely doubted to be possible at all. Two papers from the same lab, one in *Science* and
one in *Nature*, appeared within the same month in January 2006 and demonstrated two independent
ways of getting single-molecule dynamics out of living cells. The lecture works through one of
them in detail; the other used a microfluidic trap to enclose single cells in a small volume and
run a more conventional enzymatic assay inside it, and was shown to work in both *E. coli* and
yeast.

Four separate obstacles stand between "this works in a test tube" and "this works in a living
cell", and the paper's design is a response to each of them:

- **Photodamage.** Enough laser power kills the cell outright; the question is whether you can dial
  the power down far enough to still see something.
- **Many molecules.** A live cell contains many copies of most things, but a single-molecule
  measurement needs to isolate one at a time — either temporally or spatially.
- **Diffusion.** Molecules move on the timescale of the measurement.
- **Autofluorescence.** The cell itself is weakly fluorescent across a broad range of wavelengths,
  because it is full of many different molecules, each with its own absorption/emission profile.
  That broadband background — not the tightly-defined signal from an introduced fluorescent
  label — is the noise you are trying to detect a single molecule's signal above.

## The photon budget is not actually the bottleneck

A natural worry is that a single fluorescent molecule just does not emit enough light to detect.
It does not, in fact, run out: a single molecule can put out of order $10^4$ photons per second,
for anywhere from a few tenths of a second up to tens of seconds before it stops fluorescing
permanently (the paper's illumination conditions, deliberately intense, push this down to
around $250\ \text{ms}$; more on that below). Modern camera quantum efficiency — the fraction of
photons hitting the camera that get registered — is close to $0.9$, effectively $1$ for these
purposes. So the number of photons collectable from a single molecule is not small. The actual
problem is detecting that signal *against the autofluorescence background*, which the paper's
figures show is comparable in scale to the single-molecule signal itself.

## Localising a single molecule far below the diffraction limit

Start with scale. A typical globular protein — GFP-sized, say — is a few nanometers across.
Illuminate it and image it, and the spot you actually see on the camera is nothing like a few
nanometers wide: it is a **diffraction-limited spot**, a fundamental optical limit set by the
wavelength of the light, of order $\lambda/2$ (up to numerical-aperture factors). With excitation
at $514\ \text{nm}$ and fluorescence emission at a longer wavelength (emission is always redder
than excitation — the emitted photon carries less energy than the absorbed one, and energy goes as
$1/\lambda$), the resulting spot is of order $300\ \text{nm}$ across: roughly a hundred times the
size of the protein producing it.

That gap between the actual size of the object and the size of its image matters in two very
different ways, and it is easy to conflate them.

**Resolving two molecules apart** is genuinely limited by the spot size. If two molecules sit
closer together than about $\lambda/2$, their two diffraction-limited spots overlap almost
completely and the combined pattern looks like a single, slightly brighter spot — not obviously two
molecules. You need real spatial separation, on the order of the wavelength, before the sum of the
two spots visibly splits into two peaks.

**Locating a single, known-to-be-single molecule** is a completely different question, and it is
*not* limited by the spot width in the same way. If you know there is exactly one molecule producing
that $300\ \text{nm}$ spot, the question is only: where is the *center* of that spot? And locating
the center of a measured distribution is a statistics problem, not an optics problem. If you sample
a distribution $N$ times, your uncertainty in its mean falls as

$$
\delta x \sim \frac{\sigma}{\sqrt{N}},
$$

where $\sigma$ is the width of the distribution — it does *not* go to zero as you take more samples,
but the uncertainty in *where the mean is* does. Here $N$ is the number of photons collected, and
$\sigma$ is the $\sim 300\ \text{nm}$ spot width. Collecting $N \sim 10^4$ photons — not an unusual
number, as established above — gives $\sqrt{N} \sim 100$, so

$$
\delta x \sim \frac{300\ \text{nm}}{100} \sim 3\ \text{nm}.
$$

A few thousand photons buy you nanometer-scale localization of a spot that is itself three hundred
nanometers wide. This is genuinely surprising the first time you see it, and it survives a check
that seems like it should break it: cameras do not record a continuous position, they bin light
into discrete pixels, and a $100\ \text{nm}$ pixel at the sample plane (a physical pixel of order
ten microns, divided by roughly $100\times$ magnification) is not small compared to the spot. Doing
the calculation carefully shows the pixelation costs you very little — you still land close to the
$1/\sqrt{N}$ estimate. (There is a further, genuinely technical wrinkle: in the presence of camera
read noise, *larger* pixels can sometimes be better than the naive argument suggests, for reasons
that trade off against each other in practice.)

This is exactly the trick behind "super-resolution" localization microscopy, and it long predates
the live-cell paper — it was popularized for single-molecule biophysics in work such as Ahmet
Yildiz's FIONA method (**f**luorescence **i**maging with **o**ne **n**anometer **a**ccuracy), which
attached single fluorophores to the heads of molecular motors and watched them step. The trick
only works this well while the molecule stays still during the exposure — those experiments slowed
the motors down (limiting ATP, so steps happened every second or ten) precisely so the assumption
"the molecule is not moving" would hold during each snapshot, at a cost of only collecting maybe
$10$–$15\%$ of the photons actually emitted (the rest go in directions the objective does not
catch).

The general strategy behind localizing *two or more* molecules that sit within a single
diffraction-limited spot — the various "super-resolution" schemes — is to force the fluorophores
to turn on and off one at a time, localize each one separately while it is the only one lit, and
then assemble the individual localizations. The differences between named methods (STORM, from
Xiaowei Zhuang's lab; PALM, from Eric Betzig; FIONA and its playful cousins) are essentially all
about the mechanism used to get molecules to blink on and off one at a time; the localization
argument once only one is on is the same argument as above.

## Diffusion sets the real limit on exposure time

Locating a single molecule this precisely assumed it stayed put during the exposure. Inside a cell
it does not, and a back-of-the-envelope calculation shows why this is a serious constraint rather
than a minor correction.

At the scale of a protein moving through a viscous fluid, inertial forces are negligible — this is
the low-Reynolds-number regime (developed further later in the course, in the context of how
bacteria swim), and the object's response to a pushing force is not Newton's second law but
something closer to Aristotelian physics: velocity proportional to force, not acceleration
proportional to force. The relevant relation is the Stokes–Einstein one,

$$
D = \frac{kT}{\gamma},
$$

where $kT$ is thermal energy (about $4.1\ \text{pN·nm}$ at room temperature) and $\gamma$ is a drag
coefficient that scales with the size of the object. For a protein-sized object in the cytoplasm —
whose effective viscosity is taken to be roughly ten times that of water, since it is packed with
other macromolecules — this gives $D \sim 10\ \mu\text{m}^2/\text{s}$. The characteristic distance
travelled by diffusion in time $t$ is

$$
\ell \sim \sqrt{2Dt}.
$$

The paper's camera exposure was $\Delta t = 0.1\ \text{s}$. Plugging in gives $\ell$ of order one
micron — comparable to the entire length of an *E. coli* cell. In other words, over the course of a
single exposure, an untethered protein would be expected to explore a large fraction of the cell's
volume, and any attempt to localize it as a single sharp spot would simply fail.

Shortening the exposure does not obviously help: the number of photons collected scales linearly
with exposure time, so cutting the exposure by a factor of ten also cuts the signal by a factor of
ten, and the signal was already only barely clear of the autofluorescence background (this is
visible directly in the paper's Figure 1). There is also a hard floor on how fast you can pump more
photons out by raising the laser intensity, set by the finite cycling time of the excitation–
emission process itself. The solution actually used was not to fight diffusion optically but to
remove it physically: anchor the fluorescent protein to the cell membrane, which slows its motion
enough that it stays effectively put during a $0.1\ \text{s}$ exposure. In the paper this was done
by fusing the fluorescent protein (Venus, chosen for faster maturation than ordinary GFP) not
directly into the membrane, but onto Tsr, a membrane protein (the same one that appears later in
the course as part of the *E. coli* chemotaxis receptor system) — a fusion the authors checked did
not itself change the amount of fluorescence produced, ruling out the confound that some other
membrane-targeting sequences introduced.

## How do you know you are looking at one molecule?

Everything above assumed you could tell a single-molecule spot from a many-molecule spot in the
first place. A diffraction-limited spot of $300\ \text{nm}$ could in principle contain one molecule
or a thousand — $10\times10\times10$ molecules packed into a $30\ \text{nm}$ cube is still far
smaller than the spot — so spot size alone tells you nothing. The evidence has to come from the
*dynamics* of the spot's intensity over time.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="Fluorescence intensity versus time for a single bleaching molecule compared with many molecules bleaching together">
  <line x1="40" y1="20" x2="40" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="380" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <text x="210" y="210" text-anchor="middle" font-size="12" fill="currentColor">time</text>
  <text x="14" y="105" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 14 105)">intensity</text>
  <path d="M 40 60 H 190 L 191 190 H 380" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="70" y="48" font-size="12" fill="currentColor">single molecule</text>
  <path d="M 40 60 C 120 62, 160 90, 200 120 C 260 155, 320 178, 380 187" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="5 4"/>
  <text x="230" y="145" font-size="12" fill="currentColor">many molecules</text>
</svg>
<figcaption>A single fluorophore holds a roughly constant intensity and then bleaches in one abrupt
step. A collection of independently-bleaching fluorophores instead gives a smoothly decaying
intensity trace, exactly as a population of independently-decaying radioactive nuclei decays
exponentially rather than dropping to zero all at once.</figcaption>
</figure>

A single fluorescent molecule eventually **bleaches**: some side reaction (with oxygen, for
example) irreversibly knocks it out of the excitation–emission cycle for good. Each cycle carries
some small, roughly constant probability — of order $1$ in $10^5$ — of triggering that irreversible
step, which means the *time* to bleach is exponentially distributed, with some characteristic
lifetime $\tau$. For a single molecule this shows up as intensity holding roughly steady and then
dropping to background in a single step. For many independent molecules bleaching in the same spot,
the population-level intensity instead decays smoothly, because at any moment a roughly constant
*fraction* of the surviving molecules bleach — the same logic as radioactive decay of a bulk sample.
**A single abrupt bleaching step, rather than a gradual exponential decay, is treated as the gold
standard for having isolated a single molecule.** A weaker, secondary piece of evidence used in the
paper was that the intensity of the spot matched what had been measured for isolated Venus molecules
on a slide — weaker because the same molecule can genuinely fluoresce at different intensities in
different environments, so a match is supporting rather than decisive.

(Bleaching, in this irreversible sense, should be kept separate from **blinking**, where a
fluorophore drops into a dark state temporarily and later recovers — a different, reversible
phenomenon not part of this argument.)

## The imaging cycle: deliberately bleaching to create a clean baseline

The measured bleaching lifetime under the paper's illumination was $\tau = 250\ \text{ms}$ — short,
reflecting fairly intense laser illumination. This short, controllable bleaching time is put to
direct use in the experimental design. Every three minutes, the cell is illuminated for a total of
$1.2\ \text{s}$, but only the *first* $0.1\ \text{s}$ of that window is the actual image used for
analysis. The remaining second-plus of illumination is a deliberate, intentional bleaching step,
whose purpose is to guarantee that essentially nothing fluorescent from this round survives into the
next one.

How good is that guarantee? The probability that a fluorophore present at the start of the
$1.2\ \text{s}$ illumination is still unbleached at the end of it is the exponential survival
probability

$$
P(\text{survive to } t) = e^{-t/\tau}, \qquad t = 1.2\ \text{s},\ \tau = 0.25\ \text{s},
$$

$$
P = e^{-4.8} \approx 0.8\% \approx 1\%.
$$

So after each three-minute cycle's illumination, on the order of $1\%$ of whatever fluorescence was
there survives — close enough to zero that any spot seen in the *next* cycle's $0.1\ \text{s}$
snapshot can be attributed with confidence to Venus molecules that matured since the previous
snapshot, rather than to leftover molecules from before. This is what turns "count the spots you
see" into "count the *new* protein molecules produced in the last three minutes."

## What counts as a "burst"

The paper reports the number of protein molecules produced in each **burst** of gene expression,
and getting from the raw three-minute snapshots to a burst size is a small but easy-to-get-wrong
step. Consider a worked example, reading off the zoomed-in trace of new molecules over time
(Figure 3B in the paper): at one sampling instant the count is $0$; three minutes later, one new
molecule has appeared; three minutes after *that*, two more new molecules appear; only after that
does the count of new molecules return to $0$.

The size of the first burst here is not $1$ — the count at the first nonzero sample — because that
sample could simply have caught the process in the middle. It is not obviously $2$ either. The
correct reading is that a burst is the *run* of consecutive nonzero samples between two zero
readings, summed together: $1 + 2 = 3$ molecules made up this one burst. Some bursts recorded this
way run as large as $10$–$15$ molecules.

This matters because bursts are not instantaneous: a typical burst lasts on the order of five to
seven minutes, while bursts under these repressed conditions occur at a rate of roughly one per
cell cycle (the cell cycle itself measured at $55$ minutes). Comparing a burst's duration to the
typical spacing between bursts gives a rough estimate that around $15\%$ of the events counted as
a single burst could actually be two bursts that overlapped in time and were merged by the counting
procedure.

## What a burst is made of

The paper argues for a specific mechanistic picture behind each burst. The promoter sits under Lac
repressor control; the repressor occasionally falls off the operator, and while it is off, RNA
polymerase can bind and transcribe. The claim, supported by the data, is that **each burst
typically corresponds to exactly one mRNA transcript** — one repressor-unbinding event usually
yields one round of transcription, which is then translated repeatedly (with a **geometrically
distributed** number of protein molecules per burst) before the mRNA itself degrades.

Establishing "typically one mRNA per burst" did not come from directly counting mRNA molecules
one at a time; it came from combining two separately measured quantities. RT-PCR (reverse
transcribing the mRNA to DNA and amplifying it) gave the average number of mRNA copies per cell.
That average is related to the burst-level quantities by

$$
\langle \text{mRNA per cell} \rangle = (\text{mRNA per burst}) \times (\text{bursts per unit time}) \times \tau_{\text{mRNA}},
$$

with an extra factor to convert the burst rate (naturally measured per cell cycle) into the same
time units as the mRNA lifetime — i.e. using the $55$-minute cell-cycle length as the unit
conversion. Solving this relation for "mRNA per burst" using the measured average mRNA copy number
gives an answer consistent with $1$. This is also why occasional bursts genuinely produced by *two*
close-together transcription events are hard to distinguish from single-mRNA bursts: the mRNA
lifetime here is short (about $1.5$ minutes), so two mRNAs made within that short a window would
be essentially indistinguishable from one in the data, but this happens rarely enough (few bursts
per hour) not to change the "typically one mRNA per burst" conclusion.

The number of bursts observed per cell cycle was found to fit a **Poisson distribution** with mean
around $\lambda \approx 1.2$,

$$
p(n) = \frac{\lambda^n e^{-\lambda}}{n!},
$$

and the number of protein molecules within a single burst was found to fit a **geometric
distribution**. Both of these are exactly the distributions predicted by the simplest possible
kinetic model of gene expression — constant-rate mRNA production and degradation, constant-rate
translation and protein degradation — which the course develops in the following lecture. The
point made explicitly in the lecture is that this agreement is worth checking rather than assuming:
"even things that we assume to be true, we should still check to see if they are." Here, the
simple model's prediction and the single-molecule measurement agreed.

## Sources

All material in this chapter is drawn from the transcript of a single MIT 8.591J (Fall 2014)
lecture: `docs/computational-biology/mit-ocw/8591j-2014/recordings/recordings/dp4nqipuh6w.md`
(converted from `dp4nqipuh6w-captions.srt`; timestamps below refer to this transcript). No slides,
written notes or problem set were supplied for this lecture, and there was no board content
captured — anything drawn or written on the board during the lecture (the bleaching-curve sketches,
the diffusion and localization scratch work, the illumination-cycle timeline) has been
reconstructed here from the spoken description only.

- Overview of live-cell single-molecule fluorescence and the two January-2006 papers from Sunney
  Xie's lab: [00:00]–[03:32]. The paper analyzed in the rest of the lecture is referred to
  throughout but its authors are inaudible in the recording (`[INAUDIBLE]`); the companion paper
  using a microfluidic trap in *E. coli* and yeast is likewise not named in the audio. Neither
  paper was supplied as a source file — a reader wanting the primary text should locate both via
  the OCW course page linked in this transcript's front matter.
- The four challenges (photodamage, many molecules, diffusion, autofluorescence) and the photon
  budget: [03:32]–[12:42].
- Diffraction limit, localization precision, the standard-error argument, CCD pixelation: [12:42]–
  [30:25]. FIONA is attributed to Ahmet Yildiz's group; that paper is referred to but not supplied.
- Super-resolution naming aside (STORM/Xiaowei Zhuang, PALM/Eric Betzig, FIONA and related
  acronyms): [30:25]–[35:56]. These are named in passing, not treated in technical depth, and no
  paper for them was supplied.
- Diffusion back-of-envelope calculation and the membrane-anchoring solution (Venus–Tsr fusion):
  [35:56]–[45:06].
- Single-step bleaching as evidence for a single molecule, and the bleaching mechanism: [45:06]–
  [51:55].
- The illumination/bleach/image cycle and the survival-probability calculation: [51:55]–[1:03:46].
- Defining a "burst" from Figure 3B, and the mRNA-per-burst and Poisson/geometric burst statistics:
  [1:03:46]–[1:19:54]. Figure references (Figure 1, Figure 3B) are to the paper's own figures, not
  reproduced here.

---

[← 9. Robustness in Bacterial Chemotaxis](09-robustness-in-bacterial-chemotaxis.md) · [Contents](index.md) · [11. Clonal Interference and Fitness Landscapes →](11-clonal-interference-and-fitness-landscapes.md)
