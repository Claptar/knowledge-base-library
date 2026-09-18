---
title: "5. Cost-Benefit Optimization and Statistical Evidence"
course: "MIT 8.591J 2014"
chapter: 5
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 5. Cost-Benefit Optimization and Statistical Evidence

## What this covers

This chapter works through one lecture built around a close reading of a single paper: Dekel &
Alon, "Optimality and evolutionary tuning of the expression level of a protein" (*Nature*, 2005),
which argues that the expression level of the lac operon in *E. coli* has evolved to balance the
metabolic cost of making the proteins against the benefit of digesting lactose. The lecture uses
that paper for two purposes at once: to work through the biology of measuring a cost and a benefit
for gene expression, and to build a general statistical toolkit for deciding how much a plotted
curve should convince you. The two threads are not separable in what follows, because the second
is what the lecture uses to interrogate the first. It assumes you already know what the lac operon
does — lacZ, lacY, the repressor, and lactose's role in inactivating it — and have seen a Gaussian
distribution before.

## Two views of "why does this protein have this expression level"

The paper opens with a sentence it is hard to disagree with: different proteins have different
expression levels. The question is why. One view treats expression levels as evolved solutions to
a cost-benefit optimization problem: over evolutionary time, in some ancestral environment we
cannot observe directly, a given level of expression won out because it balanced what the protein
cost the cell against what it bought. A second, more skeptical view grants that selection *could*
optimize such a thing, but doubts that we can ever reconstruct the ancestral environment well
enough to claim it did, for any particular protein. This is a real disagreement among people who
study this, and the lecture does not ask you to resolve it. It asks something narrower and more
answerable: given the specific evidence in this paper, how far should it move you toward the
optimization reading for this one operon?

For the lac operon specifically, cost and benefit have concrete referents. The cost is whatever
finite resource — energy, protein-synthesis machinery, anything the cell has only so much of — goes
into making LacZ ($\beta$-galactosidase, which cleaves the lactose disaccharide into its two
monosaccharides) and LacY (the membrane protein that actively imports lactose; the operon's third
gene, LacA, has no settled story attached to it and nobody in the field talks about it much). Making
these two proteins is a cost precisely because the same resources could have gone to making
something else. The benefit, when lactose is actually present, is the sugar the cell gets to eat
once it has been imported and cleaved.

## Isolating the cost: the IPTG trick

Measuring the cost alone, with no benefit mixed in, takes a specific experimental move. Left alone,
lactose itself controls expression: it inactivates the lac repressor, which then stops blocking the
lac promoter. To decouple the amount of protein made from the presence of any actual sugar to
metabolize, the experiment instead adds IPTG, a chemical that inactivates the repressor directly
without being a substrate for the pathway. Titrating the IPTG concentration titrates lac operon
expression continuously between zero and the maximum the wild-type promoter allows — and it does
this with **no lactose in the medium**, so any change in growth rate can only be a cost, never a
benefit.

But cells still need something to eat, so the medium carries a small amount of glycerol — a
second-rate carbon source that keeps the population alive without feeding it well. Two things make
glycerol the right choice rather than a strong carbon source like glucose. First, if glucose were
abundant, adding lactose later would show essentially no growth benefit, since the cells would
already be doing fine — you'd have destroyed your own ability to see a benefit in a later
experiment. Second, glucose triggers catabolite repression: a preferred carbon source represses
CRP-dependent alternative metabolic machinery wholesale, so you would need an additional mutation
just to unmask the effect you were trying to measure in the first place.

Plotting relative growth-rate deficit (roughly, percentage decrease in growth rate relative to an
uninduced cell) against lac expression level (normalized to the wild-type promoter's maximum,
induced with IPTG, at $1$) gives a **cost curve that is convex** — it grows faster than linearly.
At the wild-type maximum, the growth deficit is only about 4%. There is no data beyond expression
level $1$, because IPTG cannot push a fixed promoter sequence past what that promoter allows; going
further needs a *stronger* promoter, which is exactly what a later experiment in this chapter
supplies via evolution rather than titration.

## Reading an error bar

Before returning to that cost curve, the lecture takes a long detour through a question that
applies to reading almost any plotted curve in a paper: if you measure some quantity $y$ at several
values of $x$, plot the mean at each $x$ with an error bar, and there is some true underlying curve
$y(x)$ that you don't get to see directly, what fraction of your error bars should actually contain
that true curve?

Two different quantities are easy to confuse here. The **standard deviation** of your measurements
at a given $x$ tells you how noisy an individual measurement is — how good an experimentalist you
are, essentially. What you actually want to know is how well you know the *true mean* at that $x$,
and that is the **standard error of the mean**,
$$\text{SEM} = \frac{\text{SD}}{\sqrt{n}},$$
where $n$ is the number of independent measurements averaged at that point (with the usual small
bookkeeping question of whether the sample SD itself divides by $n$ or by $n-1$). In the paper, each
growth-rate point comes from 48 independent cultures grown in a checkerboard layout on a microtiter
plate, and the error bars plotted are the SEM across those 48, not the raw spread — and the raw
spread, from the paper's own supplementary histograms, is large: a standard deviation of several
percent on a signal that is itself only a few percent.

Why does averaging help, and why is the result Gaussian even before you know the shape of the
underlying measurement noise? Because you are adding up many noisy measurements and dividing by
$n$: by the **central limit theorem**, the distribution of that sample mean tends toward a Gaussian
centered on the truth, with width shrinking as $\text{SD}/\sqrt{n}$, regardless of the exact shape
of the individual measurement errors.

That has a sharp, slightly counterintuitive consequence. If the noise really is Gaussian and there
is no hidden systematic bias, an error bar drawn at $\pm 1$ SEM should **miss the true value about
a third of the time** — that's just what "one sigma" means for a Gaussian. And this fraction does
not depend on $n$: as you take more measurements, the error bars shrink, but the sample mean also
gets closer to the truth, and the two effects cancel exactly, leaving the same roughly two-thirds
coverage regardless of how many measurements went into each point. So seeing a chunk of your error
bars fail to touch the plotted curve is not, by itself, evidence of sloppy measurement or a wrong
model — it is what a Gaussian is supposed to do.

## The peril of fitting

That whole argument assumed the plotted curve is the actual, God-given truth. Suppose instead the
curve is a **fit** to the very data whose error bars you're asking about. Now the picture changes,
because fitting — typically, minimizing the sum of squared deviations from the data — pulls the
curve *toward* the points by construction. Fewer than a third of the error bars will now typically
miss it, and how much fewer depends on how many free parameters the fit used.

Push this to the extreme and the danger becomes obvious: with as many free parameters as data
points, you get a **perfect fit** — the curve passes through every single point exactly, and no
error bar, however small, can possibly miss it. Concretely: measure 15 points and fit a 14-degree
polynomial (15 free coefficients), and it will thread through all 15 points precisely, not merely
within their error bars. That is not evidence the model is right. It is solving 15 equations in 15
unknowns, nothing more — and it is an easy trap to fall into without noticing, because a fit that
looked mediocre with two parameters can suddenly look spectacular with three or four, for reasons
that have nothing to do with whether the extra parameters mean anything. The general habit worth
building: whenever a fitted curve looks convincing, ask how many free parameters it used relative
to how many independent data points it was fit against. That ratio tells you how much of the
apparent success is structural rather than a discovery about the system.

This lands directly on the cost curve above. The paper compares a straight line against a
**quadratic** — one extra free parameter — and finds the quadratic fits better. That should not
surprise anyone: an extra parameter almost always fits at least as well, whether or not the true
relationship is really superlinear. Read honestly, the cost data argue for a superlinear cost
*rather weakly*: draw a straight line through the same four or five points and it looks basically
fine too.

## Back to the cost curve: two models, one range of data

The paper actually carries two different nonlinear cost curves, not one. Besides the quadratic —
a purely phenomenological curve with no mechanism attached — there is a second, mechanistic curve
built from the assumption that the cell has a **finite total amount** of some protein-making
resource; push expression high enough and that resource runs out, driving growth to zero. Over the
range where there is actual cost data (expression from $0$ to $1$, relative to the wild-type
maximum), the quadratic and the finite-resource curve are numerically almost indistinguishable —
which means the cost data alone cannot tell you which is right, only that both beat a straight line
by about the same small amount. The two curves diverge sharply only **outside** that range, for
expression levels above wild type — levels that IPTG titration cannot reach, because titrating an
existing promoter has a ceiling, but that a stronger, mutant promoter could, given enough
evolutionary time. That divergence, and not the cost data itself, is what a later experiment in
this chapter is actually built to test.

<figure>
<svg viewBox="0 0 340 260" role="img" aria-label="Benefit and cost plotted against expression level, and their difference showing an interior optimum">
  <line x1="40" y1="20" x2="40" y2="220" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="320" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <text x="180" y="245" text-anchor="middle" font-size="12" fill="currentColor">expression level x</text>
  <text x="18" y="120" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 18 120)">contribution to growth</text>

  <polyline points="40,190 72.5,161.1 105,140.4 137.5,125.6 170,114.9 202.5,107.2 235,101.8 267.5,97.9 300,95.1" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <text x="228" y="93" font-size="11" fill="currentColor">benefit(x)</text>

  <polyline points="40,190 72.5,187.45 105,179.8 137.5,167.05 170,149.2 202.5,126.25 235,98.2 267.5,65.05 300,26.8" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="5 3"/>
  <text x="238" y="60" font-size="11" fill="currentColor">cost(x)</text>

  <polyline points="40,190 72.5,163.65 105,150.56 137.5,148.52 170,155.66 202.5,170.96 235,193.57" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="196" y="212" font-size="11" fill="currentColor">net = benefit − cost</text>

  <line x1="137.5" y1="148.52" x2="137.5" y2="190" stroke="currentColor" stroke-width="1" stroke-dasharray="3 2"/>
  <circle cx="137.5" cy="148.52" r="4" fill="orange" stroke="none"/>
  <text x="137.5" y="235" text-anchor="middle" font-size="12" fill="currentColor">x*</text>
</svg>
<figcaption>A saturating benefit and an accelerating cost, subtracted, produce an interior optimum
at x*. Replace either curve with a straight line and the difference becomes monotonic — the
optimum can disappear entirely. That dependence on curvature, not on which specific curve you draw,
is the crux of the paper's argument and, as later sections show, its main point of weakness.</figcaption>
</figure>

## Measuring the benefit

The benefit side is measured differently, and less directly: relative growth rate is plotted
against **external lactose concentration**, not against expression level, because holding
expression level fixed while varying lactose independently is the harder experiment. At zero
lactose, induced cells sit at the same roughly 4-4.5% deficit found on the cost curve — paying the
cost, getting no benefit. As lactose concentration rises, growth rate climbs, crossing from deficit
to advantage and saturating by full induction at roughly a 10-11% advantage.

In the paper's model, that saturation comes from the import step obeying Michaelis-Menten kinetics:
$$\text{import rate} = V_{\max}\,\frac{[\text{lactose}]}{K + [\text{lactose}]},$$
which saturates in the lactose concentration. But this is a narrower claim than it looks: it is
saturation with respect to how much substrate is around, not with respect to how much LacY the
cell is making. Make more importer and $V_{\max}$ itself goes up — so a benefit curve that
saturates as a function of lactose concentration does not, by itself, pin down whether benefit
saturates as a function of expression level. Many different benefit-versus-expression shapes are
consistent with the lactose-concentration data actually shown; the data neither confirms nor rules
out a saturating benefit function.

That distinction matters because of the earlier fitting argument. Net growth is $b(x) - c(x)$,
benefit minus cost as a function of expression $x$. Two straight lines subtracted give another
straight line — no interior optimum, just a function pinned to one boundary or the other. An
interior optimum needs real curvature *somewhere*. If, as later, more direct measurements suggest,
cost is actually close to linear over the relevant range (see below), the paper's superlinear-cost
story stops being able to supply that curvature — which means whatever nonlinearity produces an
optimum has to live on the benefit side instead. A saturating benefit — diminishing returns as
expression rises, the first slice of pizza being better than the fifth — is a generic feature to
expect of almost any benefit function, not something special to lac.

## Why the cost curve may be the wrong place to look for the nonlinearity

Later, independent measurements complicate the paper's cost story directly. Other work (from Terry
Hwa's group) has measured relative growth rate as a function of expression of a variety of
deliberately **non-useful** proteins — $\beta$-galactosidase or $\beta$-lactamase expressed with no
matching substrate to act on — across many conditions, and finds this cost curve is close to
**linear** over a wide range, only becoming severe (growth driven toward zero) around something
like 30% of total cellular protein — much further out than anything the Dekel-Alon cost data
covers. This is one of a family of phenomenological "growth laws" that Hwa's group has documented
for *E. coli*, and it undercuts the superlinear-cost claim on its own terms: measured more directly
and over a wider range, cost looks like a line, not the accelerating curve the paper needed.

## The evolution experiment: what "500 generations" actually costs

The paper's strongest evidence is not the cost curve at all — it is a laboratory evolution
experiment. Populations were grown continuously for about **500 generations** at several different
fixed external lactose concentrations, and the operon's evolved expression level was measured
against the lactose concentration of its environment. Here the finite-resource cost model's
prediction tracks the data, while the straight-line and quadratic cost models predict a much larger
response at high lactose — expression evolving out to several times the wild-type level — that is
not observed. This match is real evidence, because it operates exactly in the regime (expression
above wild type) where the cost models genuinely diverge, unlike the cost data itself.

How long should such an experiment take? Naively, at a roughly 20-minute doubling time, $E.\ coli$
manages something like 75 generations a day, which would put 500 generations at under a week. That
is not what happens, because populations are grown by **daily batch dilution**: each day the
saturated culture is diluted 100-fold into fresh medium, grown back up to saturation, and diluted
again the next day. A hundred-fold dilution corresponds to only about 6.6 generations per day
(since $2^{6.6} \approx 100$), not 75, and the reason is that most of the day is not spent dividing
at all.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Population size on a log scale across repeated days of dilution, showing lag, exponential growth and a long saturated phase">
  <line x1="40" y1="20" x2="40" y2="185" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="185" x2="320" y2="185" stroke="currentColor" stroke-width="1.5"/>
  <text x="180" y="198" text-anchor="middle" font-size="12" fill="currentColor">time (days)</text>
  <text x="12" y="100" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 12 100)">log N</text>

  <line x1="40" y1="60" x2="320" y2="60" stroke="currentColor" stroke-width="0.75" stroke-dasharray="2 2"/>
  <text x="245" y="55" font-size="10" fill="currentColor">N max</text>
  <line x1="40" y1="170" x2="320" y2="170" stroke="currentColor" stroke-width="0.75" stroke-dasharray="2 2"/>
  <text x="230" y="181" font-size="10" fill="currentColor">N max / 100</text>

  <polyline points="40,170 48,170 68,60 140,60" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <line x1="140" y1="60" x2="140" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <polyline points="140,170 148,170 168,60 240,60" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <line x1="240" y1="60" x2="240" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <polyline points="240,170 248,170 268,60 300,60" fill="none" stroke="currentColor" stroke-width="1.8"/>

  <text x="47" y="181" font-size="9" fill="currentColor">lag</text>
  <text x="90" y="55" font-size="9" fill="currentColor">exponential growth</text>
  <text x="185" y="75" font-size="9" fill="currentColor">saturated, not dividing</text>
</svg>
<figcaption>One day of the dilution protocol: an hour or two of lag after the 100-fold dilution,
then a few hours of exponential growth back up to N max, then most of the day spent saturated
before the next dilution resets the cycle. Only the middle stretch produces generations, which is
why 500 generations took about three months rather than the week a bare doubling time suggests.</figcaption>
</figure>

The point matters beyond the arithmetic, because whatever is under selection in this protocol need
not be division rate alone. A mutation could spread by shortening the lag phase (dividing sooner
after dilution, so a genotype gets a head start on its neighbours), or by doing specifically well
during the long saturated stretch — the "growth advantage in stationary phase" (GASP) phenotype,
where surviving cells can consume the contents of others that lyse during that stretch — or simply
by dying more slowly while saturated. Richard Lenski's long-running *E. coli* evolution experiment
(running since the late 1980s, now tens of thousands of generations) has documented several of
these, lag-time reduction among the earliest.

## What evolved, and what didn't

Two results from the evolved lines are worth holding onto separately, because they point in
opposite directions.

**What did not change**: the intrinsic catalytic efficiency of LacZ — its activity normalized by
the amount of LacZ protein actually present — showed no significant improvement across 500
generations. Read one way, this is consistent with the enzyme having already been optimized for
lactose cleavage over millions of years of prior evolution, leaving little for a few hundred more
generations in the lab to improve. But the argument carries a real caveat: *E. coli*'s natural
habitat for eating lactose is the gut, whose conditions (pH, and much else) differ from a lab flask,
so "already optimal" risks conflating optimal-for-the-ancestral-environment with optimal-here — an
easy story to tell after the fact and a hard one to have predicted beforehand.

**What did change, and how far**: the experiment kept IPTG present throughout, which decouples the
amount expressed from the repressor's own response to lactose and lets expression level itself sit
under direct selection at each fixed lactose concentration. Lines evolved at higher lactose
concentrations evolved somewhat higher LacZ activity; a line at an intermediate concentration
barely moved; a line evolved with no lactose at all saw expression drop substantially. But across
every line, evolved activity never rose above roughly 1.2-1.3 times the wild-type level, even under
sustained selection pressure for more. Something is genuinely constraining upward evolution of
expression beyond wild type — consistent with, though not by itself proof of, a real nonlinearity
somewhere in cost or benefit.

A separate comparison sharpens why cost matters even when it's small. Consider a population grown
for 500 generations with **neither** lactose **nor** IPTG: the operon is never transcribed, so
there is essentially no growth cost to carrying it — only the marginal cost of replicating that
stretch of DNA each division, which is tiny. Even so, in that lineage the operon was actually
**deleted** — close to a kilobase of DNA, including the promoter, was lost, leaving cells unable to
grow on lactose even if it were added back later. Contrast that with the IPTG-selected lines, where
the operon really was costing about 5% of growth rate whenever expressed, so a mutant that lost the
ability to express it had a genuine ~5% advantage and could sweep the population outright. Both
outcomes are selection against an unused gene; the difference is how much advantage was on offer,
and in both cases it was apparently enough.

## Where the paper's argument stands

Put together, the picture is more mixed than the paper's headline suggests. The hypothesis is a
good one, and the laboratory evolution data are real: expression really does track the lactose
concentration a population was evolved in, roughly as the finite-resource model predicts, and that
match is genuine evidence, because it lands in the one regime where the candidate cost models
actually disagree. But the cost curve itself — the piece meant to justify *which* cost model to
trust in the first place — is weak evidence on its own terms: a quadratic beating a line is exactly
what an extra free parameter buys you regardless of the truth, and the two nonlinear candidates the
paper compares are nearly indistinguishable over the range they actually measured. Independent,
more direct measurements of cost (Hwa's growth laws) subsequently found cost to be close to linear
over a much wider range than this paper probed, which removes the curvature the paper leaned on.
If cost really is close to linear, the interior optimum this whole framework needs has to come from
curvature in the benefit function instead — plausible on general grounds (diminishing returns are
generic), but not something the paper's own benefit data, measured against lactose concentration
rather than expression level, actually establishes. None of this makes the evolution experiments
wrong; it specifically undermines the mechanistic cost-function story used to explain and, above
all, to extrapolate them outside the range where data exist.

## Sources

- MIT OpenCourseWare, 8.591J Systems Biology (Fall 2014), lecture recording transcript
  `9ygxpwvwydy` (`docs/computational-biology/mit-ocw/8591j-2014/recordings/recordings/9ygxpwvwydy.md`).
  No slides accompanied this recording in the supplied material; the whole chapter is built from
  spoken content, 00:00 through 1:19:29.
  - The cost-benefit framing, the IPTG protocol, glycerol/glucose choice, and the cost curve
    (00:00-16:00).
  - The standard-error-of-the-mean and error-bar digression (16:00-32:05).
  - The curve-fitting and overfitting digression (32:05-41:00).
  - Returning to the two nonlinear cost models and their range of agreement (41:00-48:00).
  - The benefit curve and Michaelis-Menten import saturation (48:00-1:01:00).
  - The evolution protocol, daily batch dilution, and what else might be under selection
    (1:01:00-1:13:21).
  - Evolved lacZ activity by lactose concentration, the deletion result, and the closing critique
    (1:13:21-1:19:29).
- Referred to in the lecture but not contained in the supplied material, and not reproduced here
  beyond the professor's verbal description:
  - U. Dekel and U. Alon, "Optimality and evolutionary tuning of the expression level of a
    protein," *Nature* 436, 588-592 (2005) — the paper itself, including its Figure 2A (the cost
    curve and its three fitted models) and Figure 4 (evolved lacZ activity vs. lactose
    concentration), and its supplementary growth-rate histograms.
  - Unnamed work from Terry Hwa's group on phenomenological bacterial growth laws, cited for the
    finding that the cost of non-useful protein expression is close to linear up to roughly 30% of
    total protein.
  - Richard Lenski's long-term *E. coli* evolution experiment (Michigan State, running since the
    late 1980s), cited for lag-time reduction and other stationary-phase adaptations.

---

[← 4. When Does Clonal Interference Matter](04-when-does-clonal-interference-matter.md) · [Contents](index.md) · [6. Evolutionary Paths and Game Theory →](06-evolutionary-paths-and-game-theory.md)
