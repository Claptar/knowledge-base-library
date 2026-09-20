---
title: "15. The Moran Process and Fixation"
course: "MIT 8.591J 2014"
chapter: 15
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 15. The Moran Process and Fixation

## What this covers

This chapter builds the Moran process, the standard model for how a population of fixed size
evolves when new types arise one individual at a time, and uses it to answer two questions: how
fast do neutral (fitness-irrelevant) mutations spread and fix, and what determines whether a mutant
with a real fitness advantage takes over the population at all. It assumes basic probability
(conditional probability, expectation, a random walk with absorbing boundaries) and the
population-genetics notion of relative fitness; it does not assume familiarity with the
Wright-Fisher process, which is mentioned only for contrast, or with diffusion approximations.

## The Moran process: a population that never changes size

Populations of interest for evolution are often enormous — $10^9$ bacteria in a flask, say — and
yet stochastic effects are never negligible, because *every* new mutant, however large the
population, starts out as a single individual. Tracking what happens to that one individual is
irreducibly a question about randomness, no matter how large $N$ is.

The Moran process is the simplest model built to study this. It fixes population size at a constant
$N$ and considers an asexually reproducing population of two types, $A$ and $B$, differing (for now)
only in some trait already present — no new mutation happens during the process itself. Rather than
having all $N$ individuals reproduce at once in synchronized generations, as in the Wright-Fisher
process, the Moran process moves one birth at a time:

1. One individual is chosen to reproduce, with probability proportional to fitness.
2. Its offspring replaces one individual chosen uniformly at random from the *whole* population of
   $N$ — including, possibly, the parent itself.

This keeps $N$ fixed by construction: one birth, one death (or "replacement" — the two words mean
the same thing here). It is a reasonable theoretical stand-in for a turbidostat, a device that holds
population size constant by pulling out a random individual every time a cell divides, in contrast
to a chemostat, which fixes the dilution rate instead.

Write $i$ for the number of $A$ individuals, so there are $N-i$ individuals of type $B$. (The
letter $i$, rather than something more mnemonic, follows Nowak's *Evolutionary Dynamics*, chapter
6 — the assigned reading behind this lecture.)

## Neutral dynamics: a random walk that looks biased and isn't

Suppose $A$ and $B$ have equal fitness — the *neutral* case. Then the probability that an
individual is chosen to reproduce is just proportional to how many of that type there are: an $A$
is chosen to reproduce with probability $i/N$, a $B$ with probability $(N-i)/N$.

Going from $i$ to $i+1$ requires two things at once: an $A$ chosen to reproduce *and* a $B$ chosen
to be replaced:

$$P(i \to i+1) = \frac{i}{N}\cdot\frac{N-i}{N}.$$

Going from $i$ to $i-1$ requires the mirror event, a $B$ reproducing and an $A$ being replaced:

$$P(i \to i-1) = \frac{N-i}{N}\cdot\frac{i}{N}.$$

These are the same product written in the other order, so they are *exactly* equal for every value
of $i$ — even though the population need not be split evenly between $A$ and $B$. This is the kind
of fact that is easy to prove and hard to feel: if $i/N=1/3$, it still doesn't matter, because the
imbalance in who is likely to reproduce is exactly cancelled by the imbalance in who is likely to
be replaced. So $i$ performs an **unbiased random walk**, with two absorbing boundaries at $i=0$
(only $B$ left) and $i=N$ (only $A$ left): once the population hits either wall, it stays there.

<figure>
<svg viewBox="0 0 460 200" role="img" aria-label="The Moran process as a random walk on the number of A individuals, absorbed at 0 and N">
  <line x1="40" y1="140" x2="420" y2="140" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="40" cy="140" r="7" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="40" cy="140" r="3" fill="currentColor"/>
  <circle cx="420" cy="140" r="7" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="420" cy="140" r="3" fill="currentColor"/>
  <circle cx="230" cy="140" r="4" fill="currentColor"/>
  <text x="40" y="162" font-size="12" text-anchor="middle" fill="currentColor">0</text>
  <text x="420" y="162" font-size="12" text-anchor="middle" fill="currentColor">N</text>
  <text x="230" y="162" font-size="12" text-anchor="middle" fill="currentColor">i</text>
  <text x="40" y="120" font-size="11" text-anchor="middle" fill="currentColor">all B, absorbing</text>
  <text x="420" y="120" font-size="11" text-anchor="middle" fill="currentColor">all A, absorbing</text>
  <defs>
    <marker id="arrM" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <path d="M 246 132 Q 300 90 340 132" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrM)"/>
  <path d="M 214 132 Q 160 90 120 132" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrM)"/>
  <text x="320" y="78" font-size="11" text-anchor="middle" fill="currentColor">P(i→i+1) = (i/N)·((N−i)/N)</text>
  <text x="140" y="78" font-size="11" text-anchor="middle" fill="currentColor">P(i→i−1) = ((N−i)/N)·(i/N)</text>
  <text x="230" y="28" font-size="12" text-anchor="middle" fill="currentColor">same product both ways — exactly equal under neutrality</text>
</svg>
<figcaption>The two transition probabilities out of state i are the same product written in a
different order, so under equal fitness the count of A individuals is an unbiased random walk
between two absorbing states.</figcaption>
</figure>

## Fixation under neutrality: an argument that needs no algebra

Given that $i$ random-walks between two absorbing boundaries, what is the probability that $A$
eventually fixes (takes over the whole population), starting from $i$ copies?

The algebra is not needed for this one. Imagine tagging every individual with its own distinct
colour, rather than lumping them into just two types. Because $N$ is fixed forever, the lineage of
*some* individual will eventually fill the entire population — someone's descendants must
eventually occupy all $N$ slots, purely as a consequence of the random walk hitting a boundary. By
symmetry, since every individual is equally likely (under neutrality) to be that eventual ancestor,
each one has probability exactly $1/N$ of being it. Summing over the $i$ individuals that happen to
carry type $A$:

$$P(A \text{ fixes} \mid i) = \frac{i}{N}, \qquad P(B \text{ fixes} \mid i) = 1-\frac{i}{N} = \frac{N-i}{N}.$$

That the answer depends on $i/N$ so simply, when the underlying dynamics look symmetric in a
different way (recall the two transition probabilities above were equal, independent of $i$), is
exactly the kind of result that feels obvious and confusing at the same time — both things can be
true together.

This is the same style of argument behind why a single, non-recombining lineage — the Y-chromosome,
say, or mitochondrial DNA, neither of which recombines the way the rest of the genome does — is
expected to trace back to a single common ancestor (colloquially, "Adam" or "Eve"): with no
recombination shuffling lineages together, the population of gene copies along that line is exactly
this random walk, and one lineage has to win. (With recombination, many ancestors contribute to any
one descendant, and the argument no longer applies in the same form — sexually reproducing
populations need a different treatment, not covered here.)

## How much real time is one iteration?

One iteration of the Moran process is one birth and one replacement — and only one individual out
of $N$ actually gets to reproduce in that step. So if a whole population is to have had roughly one
chance each to reproduce, that takes about $N$ iterations. Equivalently: with $N$ individuals each
independently "waiting" to be the one to divide, a $10\times$ larger population reaches its first
division $10\times$ faster. So the real time elapsed per iteration scales as $1/N$, and one
generation time (the typical interval between a cell's birth and its own division) corresponds to
about $N$ iterations of the model. This conversion is exactly what is needed to turn a target
real-time duration — say, 100 hours of bacteria growing in a turbidostat — into a number of
iterations to run in a simulation.

## The molecular clock: the rate of neutral substitution

Now allow mutation. Let $\mu$ be the probability that a birth event produces a mutant of a new,
selectively neutral type — a mutation probability *per birth*, equivalently *per generation*. Two
things must happen for a new neutral mutation to leave a permanent trace along a lineage: it must
*appear*, and it must *fix*.

- **Rate of appearance.** In one generation (about $N$ iterations, each with one birth), the
  expected number of new neutral mutants arising is $\mu N$ — linear in population size, since more
  individuals means more birth events.
- **Probability of fixation.** A new mutant starts out as a single copy, $i=1$, so by the neutral
  fixation result above its probability of eventually fixing is $1/N$.

Multiplying, the rate at which neutral mutations *fix* — the rate of neutral molecular evolution —
is

$$(\mu N)\cdot\frac{1}{N} = \mu,$$

independent of population size, measured in substitutions per generation. This cancellation is the
content of the (neutral) **molecular clock**: the two population-size dependences, one in how many
mutants appear and one in how likely each is to fix, exactly cancel, leaving a rate governed only
by the per-generation mutation rate. (The calculation implicitly assumes new mutants are rare enough
that they don't have to compete against each other while fixing — a "separation of time scales"
that breaks down once multiple lineages coexist, the subject of *clonal interference*, taken up
later in the course.)

The model is too simple in one respect worth flagging: it predicts a substitution rate constant
*per generation*, so organisms with the same $\mu$ but very different generation times — humans and
mice, say — should accumulate neutral substitutions at very different rates *per year*. That isn't
what is observed; real substitution rates look closer to constant per year across quite different
generation times. Something is missing from this simplest account, and the lecture flags it as a
question to return to rather than resolving it here.

## Reading the clock: how far back is that?

Treating the neutral substitution rate as roughly constant lets an observed count of neutral
differences between two lineages be converted into an estimate of how long ago they diverged — this
is the basis for molecular-clock dating. It helps to have a few memorized landmarks for the
resulting timescales, so a new number has something to be compared against: the universe is about
13 billion years old, the earth about 4.5 billion years, life appears roughly a billion years after
that, the dinosaurs disappear some 60-odd million years ago, agriculture begins about 12,000 years
ago — and the human/chimpanzee divergence, argued over but usually quoted within a factor of two of
$7\times10^6$ years, sits among these mid-scale numbers.

A sharper application: dating when humans started wearing clothes. Direct archaeological evidence
(needles, clothed figurines) only reaches back about 30,000 years, and body hair was apparently lost
around a million years ago — leaving a wide, otherwise unrecoverable gap. The trick that closes it:
a species of louse specializes in living in human clothing, distinct from the one that lives in
human hair, and it presumably could not have speciated before there *was* any clothing to colonize.
Sequencing the two louse lineages and counting accumulated neutral differences gives a
molecular-clock estimate for when they split — bounded, sensibly, between the archaeological floor
of 30,000 years and the human/chimpanzee divergence of about 7 million years. One early estimate (a
researcher at the Max Planck Institute) put it at about 70,000 years; a later study (a University of
Florida group) put it at about 170,000 years. The exact number is still debated, but the method —
turning a question with no physical record at all into a testable estimate, using nothing but DNA —
is the point.

## Beyond neutrality: the general fixation probability

Now suppose $A$ has a genuine fitness advantage, captured by a relative fitness $r=$ (fitness of
$A$)/(fitness of $B$): $r>1$ means $A$ is advantageous, $r<1$ deleterious. Only the *reproduction*
step is affected by $r$; replacement stays uniformly random. Nowak's book gives — without deriving
it here, since the derivation is the assigned reading behind this lecture and is not repeated in
it — the probability that $A$ eventually fixes, starting from $i$ copies out of $N$:

$$x_i = \frac{1-r^{-i}}{1-r^{-N}}.$$

The formula is compact but nearly opaque on sight. The standard remedy — and a habit worth adopting
for any formula derived by hand, not just this one — is to check it against every limit whose
answer is already known:

- **$i=0$:** no $A$ individuals at all should never fix, whatever $r$ is. Indeed $r^{-0}=1$, so the
  numerator is $0$.
- **$i=N$:** already fixed stays fixed. Indeed $r^{-N}$ cancels top and bottom, giving $x_N=1$.
- **$r\to\infty$:** an overwhelmingly fit mutant should fix for sure, given at least one copy.
  Indeed every $r^{-k}\to 0$ for $k>0$, so $x_i \to 1/1 = 1$.
- **$r\to 1$** (recovering the neutral case): substituting $r=1$ directly gives $0/0$. Applying
  L'Hopital's rule — differentiating numerator and denominator with respect to $r$, and only then
  taking the limit — gives $i\,r^{-i-1}$ over $N\,r^{-N-1}$, which at $r=1$ is $i/N$: exactly the
  neutral result derived above by the symmetry argument, recovered here as a special case of the
  general formula. The useful thing to notice is that this limit is *not* automatically small, even
  though naively plugging $r=1$ into the un-simplified expression looks like it gives $0$.

That every one of these checks passes is not a proof that the formula is right, but it is exactly
the kind of sanity check that catches a wrong formula quickly, and is worth running on any result
before trusting it.

## Weak selection: when is a mutation "nearly neutral"?

Real fitness advantages are usually small — a paper assigned for the next lecture reports selection
coefficients of order 1–3% for mutations that let bacteria do better in a new environment. Write the
relative fitness as $r=1+s$, where $s$ is the **selection coefficient**: $s>0$ beneficial, $s<0$
deleterious, and $|s|\ll 1$ is the case of interest. Take the fixation probability of a single new
mutant, $x_1$, and consider two regimes.

**Strong enough selection ($sN\gg1$).** If the population is large enough that $r^N\gg1$, the
denominator $1-r^{-N}$ is essentially $1$, so

$$x_1 \approx 1-\frac{1}{r} = 1-\frac{1}{1+s} \approx s.$$

A beneficial mutation with a 1–3% advantage therefore has only a 1–3% chance of ever fixing — most
copies of even a genuinely beneficial mutation are lost to chance while still rare. (The constant in
front of $s$ is model-dependent: other stochastic models of the same idea, such as branching-process
approximations, can give $2s$ instead. What's robust across models is that the fixation probability
is of order $s$, not of order $1$.)

**Weak relative to drift ($sN\ll1$, "nearly neutral").** Expanding the exact formula for small $s$
gives

$$x_1 \approx \frac{1}{N} + \frac{s}{2}.$$

A mutation whose fitness effect is small enough that $|s|N\ll1$ behaves, for practical purposes,
just like a truly neutral one — the population is too small, or the effect too weak, for selection
to move the fixation probability far from its neutral baseline $1/N$. This is the precise sense in
which "nearly neutral" is defined: not that $s$ is literally zero, but that $|s|N\ll1$.

<figure>
<svg viewBox="0 0 420 260" role="img" aria-label="Fixation probability of a single mutant as a function of its selection coefficient">
  <defs>
    <marker id="arrS" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="30" y1="220" x2="400" y2="220" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrS)"/>
  <line x1="210" y1="220" x2="210" y2="20" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrS)"/>
  <text x="400" y="238" font-size="12" text-anchor="middle" fill="currentColor">s</text>
  <text x="210" y="14" font-size="12" text-anchor="middle" fill="currentColor">x&#8321;</text>
  <line x1="210" y1="220" x2="390" y2="40" stroke="currentColor" stroke-width="1" stroke-dasharray="4 4"/>
  <text x="330" y="55" font-size="11" text-anchor="middle" fill="currentColor">x&#8321; ≈ s (sN ≫ 1)</text>
  <line x1="210" y1="220" x2="270" y2="196" stroke="currentColor" stroke-width="1" stroke-dasharray="2 3"/>
  <text x="255" y="180" font-size="11" text-anchor="start" fill="currentColor">slope s/2</text>
  <line x1="210" y1="215" x2="390" y2="215" stroke="currentColor" stroke-width="0.8" stroke-dasharray="1 3"/>
  <text x="195" y="212" font-size="11" text-anchor="end" fill="currentColor">1/N</text>
  <path d="M 30 219 C 100 218 160 217 210 215 C 260 212 330 140 390 45" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <circle cx="210" cy="215" r="3" fill="currentColor"/>
  <text x="90" y="235" font-size="11" text-anchor="middle" fill="currentColor">deleterious, |s|N ≫ 1: decays toward 0</text>
  <text x="330" y="252" font-size="11" text-anchor="middle" fill="currentColor">beneficial</text>
</svg>
<figcaption>The fixation probability x₁ of a single new mutant, against its selection coefficient
s. Near s=0 it sits at the neutral baseline 1/N with a shallow local slope of s/2; for sN ≫ 1 it
rises to meet the line x₁ ≈ s; for deleterious s with |s|N ≫ 1 it decays toward 0 — small, but
never quite zero.</figcaption>
</figure>

Plotting $x_1$ against $s$ makes the comparison visible at once: near $s=0$ the curve sits at height
$1/N$ with a shallow local slope of $s/2$ — half as steep as the line $x_1=s$ it eventually
approaches — and on the deleterious side it bends down and decays toward $0$ once $|s|N\gg1$, but
does not reach it instantly. That last point — a deleterious mutation's fixation probability shrinks
but never vanishes — is the content of the next section.

## Deleterious mutations can fix too: Muller's ratchet

The formula above says a deleterious mutation ($s<0$) has small fixation probability when
$|s|N\gg1$, but *not zero* — and it is not even small once $|s|N$ is only of order $1$ or below,
which happens whenever the population is small enough. Small populations are worse "filters" for
selection: a mildly harmful mutation that a huge population would reliably purge can drift to
fixation in a small one.

This is exploited deliberately in a **mutation accumulation assay**: grow a population of bacteria
(so ordinary selection is acting — faster dividers are, in general, outcompeting slower ones), then
plate it out into colonies, each founded by a single cell. Pick one colony at random, grow it up,
and repeat. Because the colony propagated at each step is chosen at random rather than by how well
it grew, the effect of selection is essentially removed across steps — a colony carrying a
fitness-reducing mutation is just as likely to be picked as any other. Passing a population through
this kind of single-cell bottleneck at every step drives its **effective population size**,
$N_{\text{effective}}$, down toward $1$, regardless of how large the population grows in between
bottlenecks — a fluctuating population's effective size, for questions about drift, is generally
dominated by its smallest point, not its average. With $N_{\text{effective}}$ this small,
$|s|N_{\text{effective}}$ is small for essentially any deleterious mutation, and deleterious
mutations accumulate steadily rather than being filtered out.

The general phenomenon — that deleterious mutations can accumulate and fix in an asexual lineage,
degrading its fitness over time, especially in small or bottlenecked populations — is called
**Muller's ratchet**. It matters beyond the laboratory assay: it is one of the proposed explanations
for why sexual reproduction persists despite its steep cost (an asexual population can, in
principle, grow about twice as fast as a sexual one, since in the sexual case only half the
population — the females — gives birth). The idea is that recombination in a sexual population can
separate a beneficial mutation from a deleterious one that happened to arise on the same lineage,
letting selection act on each independently — something a purely asexual population, whose lineages
cannot exchange material, cannot do. The lecture flags this as an open question the field argues
about, to be developed more quantitatively later in the course.

## Sources

- Recording: `recordings/klrpm-beeoi-captions.srt`, converted to
  `docs/computational-biology/mit-ocw/8591j-2014/recordings/recordings/klrpm-beeoi.md` — MIT 8.591J
  *Systems Biology*, Fall 2014, transcript timestamps [00:00]–[1:20:13]. This lecture is
  transcript-only: nothing written on the board survives in the source, so the fixation-probability
  formula, both figures, and the human-history timeline are reconstructed here from what the
  lecturer said about them, not copied from a slide or board.
- Assigned reading referred to throughout but not supplied to this chapter: Martin Nowak,
  *Evolutionary Dynamics*, chapter 6 — the source of the Moran-process fixation formula
  $x_i=(1-r^{-i})/(1-r^{-N})$ and of its derivation, which the lecture explicitly declines to
  repeat ([58:32]).
- A paper assigned for the following lecture, on selection coefficients of 1–3% in bacterial
  adaptation to a new environment, referred to at [1:06:32] but not identified further or supplied.
- Two lice-genomics studies used as a molecular-clock worked example ([54:00]–[57:28]): one from a
  researcher at the Max Planck Institute (~70,000 years), one from a University of Florida group
  (~170,000 years). Neither is identified by author or full citation in the transcript.
- Topics named as coming later in the course and not developed here: clonal interference
  ([41:48]), and the quantitative treatment of Muller's ratchet and the evolution of sex
  ([1:19:06]–[1:20:13]).

---

[← 14. Toggle Switches and Stability Analysis](14-toggle-switches-and-stability-analysis.md) · [Contents](index.md) · [16. Tipping Points and Species Competition →](16-tipping-points-and-species-competition.md)
