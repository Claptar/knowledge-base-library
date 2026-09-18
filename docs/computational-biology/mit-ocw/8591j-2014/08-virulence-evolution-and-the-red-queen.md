---
title: "8. Virulence Evolution and the Red Queen"
course: "MIT 8.591J 2014"
chapter: 8
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 8. Virulence Evolution and the Red Queen

## What this covers

This chapter answers two separate questions that the lecture pairs deliberately. First: given a
simple compartmental model of infection, what determines whether a disease invades and persists,
and — the sharper question — what does natural selection actually maximize when two strains of a
parasite compete for the same host population? Second, and unrelated in mechanism but linked by
theme (both are about the population consequences of a parasite): why does sexual reproduction
persist at all, given that it costs a population a factor of two in growth rate? The chapter
assumes comfort with ODE fixed points and their stability, and reuses — without re-deriving it —
the geometric-distribution argument from the mRNA/protein burst-size problem earlier in the course.

## Microparasites and macroparasites

A parasite, in the broadest sense, is layered onto essentially every organism: humans carry viruses
and bacteria; bacteria are themselves preyed on by bacteriophage, viruses that have evolved
specifically to exploit a bacterial cell's machinery. Before writing down any model, it is worth
asking which details of this relationship are worth keeping and which are not — the choice is not
forced by the biology, and different choices suit different parasites.

The distinction the lecture opens with is between **microparasites** — viruses and bacteria, which
reproduce extremely fast inside a host and reach huge numbers there — and **macroparasites** —
things like tapeworms, which do not reproduce prolifically inside a single host and are more often
transmitted through the environment than by direct host-host contact. The consequence for modeling
is this: for a microparasite, the number of pathogen particles inside a given host is not the
useful state variable to track, both because it would be complicated and because, once a host is
infected, it typically becomes sick and infectious quickly and recovers (or dies) on a similar time
scale — there is a rough separation of time scales between "becoming infected" and "the details of
what happens inside." That licenses collapsing all of that internal state into a small number of
discrete classes per host: sensitive (uninfected), infected, and — later — resistant. Whether this
simplification is actually justified for a given disease is an empirical question, not something
the model can settle on its own; macroparasites, which don't blow up in numbers inside one host and
often transmit environmentally rather than host-to-host, are a case where the same collapse would
throw away exactly the information that matters, and need a different kind of model that this
lecture does not build.

*Aside on intra-host parasitism.* The phage-on-bacteria layer has its own parasite-of-a-parasite
story worth keeping in mind for later: when several phage particles infect the same bacterial cell,
a phage with a shorter genome that cannot replicate on its own can still spread by taking over the
replication machinery contributed by full-length, co-infecting phage — a "cheater" strategy. This
is a small piece of a much larger point that resurfaces below, when the virulence-evolution
discussion returns to what happens once more than one strain can share a host.

## A basic model of infection

Martin's model (the lecture works from chapter 11) divides the host population into sensitive
individuals, in number $x$, and infected individuals, in number $y$, and writes down the simplest
possible dynamics for how a host moves between the two classes — treating contact between the
classes the way a well-mixed chemical reaction treats collisions between two species:

$$\dot x = k - u\,x - \beta\,x y, \qquad \dot y = \beta\, x y - (u+v)\,y.$$

Reading off the terms: $k$ is a constant rate at which new sensitive individuals enter the
population (birth, immigration, whatever keeps the population from vanishing — see the caveat
below); $u$ is the death rate that applies regardless of infection; $\beta x y$ is the rate at which
sensitive individuals become infected, proportional to how often the two classes "collide," exactly
as in mass-action chemical kinetics; and $v$ is the **virulence** — the extra death rate an
infected individual suffers on top of the baseline $u$. Every individual leaving the sensitive class
through infection enters the infected class, which is why $\beta xy$ appears with opposite signs in
the two equations.

<figure>
<svg viewBox="0 0 380 190" role="img" aria-label="Flow diagram of the sensitive/infected compartmental model">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="40" y="60" width="90" height="50" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="85" y="90" text-anchor="middle" font-size="13" fill="currentColor">S  (x)</text>
  <rect x="250" y="60" width="90" height="50" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="295" y="90" text-anchor="middle" font-size="13" fill="currentColor">I  (y)</text>

  <line x1="0" y1="85" x2="38" y2="85" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="15" y="72" font-size="12" fill="currentColor">k</text>

  <line x1="132" y1="85" x2="248" y2="85" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="190" y="72" text-anchor="middle" font-size="12" fill="currentColor">&#946;xy</text>

  <line x1="85" y1="112" x2="85" y2="160" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="95" y="150" font-size="12" fill="currentColor">u</text>

  <line x1="295" y1="112" x2="295" y2="160" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="305" y="150" font-size="12" fill="currentColor">u+v</text>
</svg>
<figcaption>The two compartments of the basic model: entry into the sensitive class at rate $k$,
transmission from sensitive to infected at rate $\beta x y$, and death at rate $u$ (sensitive) or
$u+v$ (infected, carrying the extra mortality caused by the parasite).</figcaption>
</figure>

Without any infection at all, $\dot x = k - ux = 0$ gives an equilibrium number of sensitive
individuals $x_0 = k/u$ — this is the population the model settles to before a parasite is ever
introduced, and it reappears below inside $R_0$.

A caveat the lecture is explicit about: entry at a constant rate $k$ is a mathematical convenience,
not a claim about biology — it takes something else (parents, migrants) to produce those $k$
individuals per unit time, and treating that as a constant rather than, say, proportional to the
existing population is a simplification made purely to keep the population from certain,
uninteresting extinction (with no birth term, *everyone* dies eventually, infection or not, since
both classes have positive death rates and nothing replenishes them). Classic epidemiological
**SIR** models — the S here matches the sensitive class, but "I" and "R" stand for infected and
*resistant* — sidestep this by having infected individuals recover into a resistant class rather
than by inventing a birth term, and possibly cycle resistant individuals back to sensitive later.
The lecture does not derive the SIR equations in full (see Sources), only notes that the same
intuition about $R_0$ carries over, and the underlying conclusions turn out to be robust to which
of these bookkeeping choices you make.

## $R_0$: definition, distribution, and derivation

$R_0$, the **basic reproductive number**, is defined operationally: introduce one infected
individual into an otherwise fully sensitive population (at its infection-free equilibrium $x_0$),
and ask for the *expected* number of new infections that one individual causes over its lifetime.
It is a pure number, not a rate — a point worth being pedantic about, since "the expected number of
secondary infections from one case" has no time unit attached to it. Whether $R_0$ is greater or
less than 1 is the whole story near the infection-free state: above 1, a single introduced infection
grows in expectation (an exponentially branching process); below 1, it goes extinct in expectation.
At exactly $R_0=1$ the process is a critical branching process — neutrally stable in the mean, but
it will nonetheless die out with probability 1 purely from the randomness of who infects whom,
since a random walk with zero drift is recurrent to extinction.

$R_0>1$ does *not* mean the whole population is doomed to become infected. The exponential growth
of the infected class is a statement about the *early*, linearized dynamics near the infection-free
state; as more of the population becomes infected, the pool of remaining sensitive individuals
shrinks, which throttles the rate at which new infections can be generated. That feedback — not
visible in $R_0$ itself — is what can let the infected and sensitive classes settle into a
nontrivial (generally damped-oscillatory) coexistence equilibrium rather than driving $x$ to zero.

**What distribution governs the number of secondary infections?** Not Poisson: a Poisson count
would answer "how many people do I infect in the next ten days, given that I stay alive that long,"
which fixes the observation window rather than the individual's lifetime. The actual question is
how many times a randomly-chosen individual manages to transmit before leaving the infected class
altogether (by dying, at rate $u+v$), when transmission itself happens at rate $\beta x$. This is
exactly the same race-between-two-rates structure that produced a **geometric distribution** for
the number of times an mRNA is translated before it degrades, earlier in the course (production at
one rate, removal at another; count how many times you go around the "produce" loop before the
"remove" event fires). Here the loop is "infect one more person, at rate $\beta x$" versus "die, at
rate $u+v$," and the number of secondary infections before the infected individual leaves the
population is geometric with the corresponding success probability — even though every infected
individual in this model is identical. Summing many such geometric draws (say, from an initial
batch of 20 or 100 simultaneously-introduced infections) smooths the distribution into something
close to Gaussian, by the same logic as any sum of many i.i.d. random variables — a geometric total
for one seed does not make the total across many seeds geometric.

Real populations of infected individuals are not identical, and that matters: if individuals vary
in how infectious they are, the distribution of secondary cases becomes broader than geometric even
for a fixed mean $R_0$. A larger fraction of introductions then fizzle out immediately, while a
minority of highly infectious individuals produce disproportionately explosive outbreaks — the
canonical illustration being "Typhoid Mary," an individual whose case (as a cook, in the version
recalled in class) generated far more secondary infections than a typical carrier. This is the
subject of the supplementary reading by Lloyd-Smith on heterogeneity in individual infectiousness
(see Sources); it is not derived here.

**Deriving $R_0$ for this model.** $R_0$ factors into two pieces:

$$R_0 = (\text{rate of causing new infections}) \times (\text{expected lifetime as an infected individual}).$$

The expected lifetime as infected is $1/(u+v)$, the reciprocal of the death rate in that class. The
rate of causing new infections is $\beta x$, evaluated at the sensitive population *before* any
infection is introduced, i.e. at $x = x_0 = k/u$. So

$$R_0 = \frac{\beta k}{u\,(u+v)}.$$

## Vaccination and eradication

Because $R_0$ is exactly the quantity that must exceed 1 for a disease to become endemic, it also
tells you how hard it is to eliminate a disease by vaccination: vaccinating a fraction $p$ of the
population effectively removes those individuals from the pool of sensitives available to be
infected, which lowers the effective reproductive number below 1 once

$$p > 1 - \frac{1}{R_0}.$$

As $R_0$ grows, this threshold approaches 1, meaning you have to vaccinate essentially everyone —
which you can never fully achieve — and that is exactly why high-$R_0$ diseases are hard to
eradicate. The classic childhood diseases (measles, whooping cough, German measles, chickenpox,
diphtheria, scarlet fever, mumps, poliomyelitis) have estimated $R_0$s roughly in the range 5–15,
so vaccinating, e.g., 80% of the population is needed for $R_0=5$. Smallpox, by contrast, has an
estimated $R_0$ around 3–5 — smaller than most of that list — which the lecture connects directly
to why smallpox vaccination campaigns succeeded in eradicating it where campaigns against the
higher-$R_0$ diseases have not. A class discussion of Ebola arrived (from an audience member's
recollection, not from anything the professor asserted as fact) at an estimated $R_0$ around 2 for
the 2014 West Africa outbreak, which would put the eradication threshold near 50%.

The important caveat is that $R_0$ is not an intrinsic constant of a pathogen — it depends on the
environment and behavior of the population it is measured in. A returning healthcare worker who
knows to self-monitor and report a fever immediately has a very different (lower) local $R_0$ than
an outbreak in a setting without that surveillance; public health measures are, among other things,
a way of directly pushing $R_0$ down.

## Two strains, no super-infection, and what selection maximizes

$R_0$ tells you whether a single strain, on its own, can become endemic. It does not by itself tell
you what a parasite is selected to do — that requires comparing *two* strains competing for the
same hosts, which is the second model the lecture builds (still following Martin, but a simpler
model than the "super-infection" framework covered later in that chapter).

The critical assumption is **no super-infection**: a host carries at most one strain at a time.
Given that, the two strains can differ from each other in exactly two parameters: their
transmissibility $\beta_i$ and their virulence $v_i$ (the extra mortality each strain imposes).
Higher $\beta$, all else equal, is intuitively good for a strain; what happens as $v$ varies is the
less obvious question, and it is exactly what the rest of this section is for.

Each strain, alone, has its own single-strain equilibrium $E_i = (x_i^*, y_i^*)$ found by setting
$\dot y_i = 0$ at nonzero $y_i$:

$$\beta_i x_i^* - (u+v_i) = 0 \quad\Longrightarrow\quad x_i^* = \frac{u+v_i}{\beta_i}.$$

Suppose the population sits at $E_1$ (strain 1 alone, endemic, so $R_1>1$), and a single individual
infected with strain 2 is introduced. Does strain 2 invade? The natural criterion is the sign of
$\dot y_2$ evaluated at $E_1$ as $y_2$ is perturbed away from zero — i.e., the derivative of $\dot
y_2 = \beta_2 x y_2 - (u+v_2) y_2$ with respect to $y_2$, evaluated at $x=x_1^*$:

$$\beta_2 x_1^* - (u+v_2) > 0.$$

Substituting $x_1^* = (u+v_1)/\beta_1$:

$$\beta_2\,\frac{u+v_1}{\beta_1} > u+v_2 \quad\Longrightarrow\quad \frac{\beta_2}{u+v_2} > \frac{\beta_1}{u+v_1}.$$

Multiplying both sides by $k/u$ turns each side into exactly the $R_0$ expression derived above:

$$R_2 > R_1.$$

So **strain 2 invades an equilibrium held by strain 1 if and only if $R_2 > R_1$** — and the same
argument run the other way shows strain 1 can likewise invade strain 2's equilibrium only if
$R_1>R_2$. Together, these say that whichever strain has the larger $R_0$ wins outright and drives
the other extinct; there is no stable coexistence except in the non-generic (measure-zero) case
$R_1=R_2$, and even then, coexistence is fragile in the same way nearly-neutral mutations are —
sorting between two strains with nearly equal $R_0$ just takes correspondingly longer. This is the
sense in which **selection maximizes $R_0$**: two strains compete on nothing but the size of a
single number, however many different combinations of $\beta$ and $v$ produced it. The lecture
flags this as more surprising than it first sounds — the invasion condition was derived from a
statement about competitive dynamics between two circulating strains, yet it collapses exactly onto
$R_0$, a quantity originally defined from a completely different scenario (one infected individual
entering a population of sensitives).

## What virulence evolves to depends on what it trades off against

Knowing that selection maximizes $R_0 = \beta k /[u(u+v)]$ tells you nothing about where virulence
ends up until you specify how $\beta$ (transmissibility) depends on $v$ (virulence) — because $v$
appears in the denominator, more virulence is *always* bad for $R_0$ on its own; whether it is
worth it depends entirely on what it buys in transmissibility. The lecture works through three
assumptions Martin considers.

**1. $\beta$ independent of $v$.** If a parasite's ability to spread does not depend at all on how
much damage it does to the host, then $R_0$ is strictly decreasing in $v$, and selection drives $v
\to 0$. This is the formal version of the folk claim that *a well-adapted parasite does not harm its
host*: if killing the host buys nothing, the only effect of virulence is to shorten the window in
which the host can spread the infection further, so lower virulence is strictly better. The lecture
is careful to flag this as a conclusion of a very particular (and probably not generally true)
assumption, not an empirical law — Martin's own counterexample is malaria, which has coexisted with
humans for a very long time and remains highly virulent.

**2. $\beta$ proportional to $v$** (e.g. $\beta = av$ — imagine viral load inside the host driving
both how sick you get and how infectious you are). Then

$$R_0(v) = \frac{a k}{u}\cdot\frac{v}{u+v},$$

which is monotonically increasing in $v$ and has the Michaelis–Menten shape: linear for small $v$,
saturating toward a finite ceiling as $v$ grows. Because it is monotonic with no interior peak, the
value that maximizes $R_0$ is $v\to\infty$ — virulence evolves to be arbitrarily large.

**3. $\beta$ itself saturates in $v$** (e.g. $\beta = av/(c+v)$ — past some point, extra viral load
no longer buys extra transmissibility; the lecture's example is that once you reliably infect
everyone you sneeze on, having still more virus in you does not raise the infection rate further).
Now $R_0(v)$ can have an interior maximum, and virulence evolves to some finite, intermediate $v^*$.
As the saturation constant $c \to \infty$, this case reduces to case 2 (transmission is
approximately linear in $v$ over the relevant range), and correspondingly the evolved virulence
grows without bound as $c$ grows.

<figure>
<svg viewBox="0 0 340 230" role="img" aria-label="Three possible shapes of R0 as a function of virulence, depending on the transmission trade-off">
  <line x1="35" y1="200" x2="320" y2="200" stroke="currentColor" stroke-width="1.5"/>
  <line x1="35" y1="200" x2="35" y2="15" stroke="currentColor" stroke-width="1.5"/>
  <text x="320" y="215" text-anchor="middle" font-size="12" fill="currentColor">virulence, v</text>
  <text x="20" y="15" text-anchor="middle" font-size="12" fill="currentColor">R&#8320;</text>

  <!-- Curve A: beta independent of v, strictly decreasing, optimum at v=0 -->
  <path d="M 40 40 C 90 90, 140 140, 300 185" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <circle cx="40" cy="40" r="3.5" fill="currentColor"/>
  <text x="55" y="35" font-size="11" fill="currentColor">A: &#946; fixed &#8212; max at v=0</text>

  <!-- Curve B: beta = a v, monotonic increasing, saturating -->
  <path d="M 40 195 C 100 150, 150 90, 320 65" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="7,4"/>
  <text x="180" y="82" font-size="11" fill="currentColor">B: &#946;&#8733;v &#8212; argmax v&#8594;&#8734;</text>

  <!-- Curve C: beta saturates in v, interior maximum -->
  <path d="M 40 198 C 100 120, 150 100, 190 105 C 230 110, 270 160, 300 195" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="2,3"/>
  <circle cx="190" cy="105" r="3.5" fill="currentColor"/>
  <text x="192" y="95" font-size="11" fill="currentColor">C: &#946; saturates &#8212; max at interior v*</text>
</svg>
<figcaption>Three assumptions about how transmissibility &#946; trades off against virulence v give
three different evolutionary outcomes for R&#8320;(v): virulence driven to zero, driven to infinity,
or settling at an intermediate value.</figcaption>
</figure>

The lecture's own assessment is that real data suggest infectivity does increase with virulence but
sub-linearly (saturating) — case 3's shape — though how strong a claim that supports is disputed.
And there is a further complication once **super-infection** is allowed (multiple strains sharing a
host, which the two-strain model above ruled out by assumption): a strain that shares a host with a
rival must out-compete that rival *inside* the host as well as transmit onward, and a strategy of
high virulence — burn through the host fast and move on — avoids paying the cost of a rival strain
exploiting a host kept alive for the long haul. In that setting, low virulence functions like a
cooperative strategy (conserving host resources to maximize the transmission window), and it is
exploitable by "cheater" high-virulence strains in exactly the sense that the earlier phage-cheater
example illustrated: a strategy that does the patient thing is vulnerable to a rival that does not.
Super-infection therefore tends to select for *higher* virulence than the single-strain-per-host
model predicts.

## The puzzle: why sex, given its cost?

Switching topics entirely (the shared thread is only that parasites reappear as the driving force):
obligate, biparental sexual reproduction is astonishingly widespread among animals, despite what
looks, on its face, like a severe cost. The clearest version of the cost is the **twofold cost of
males**: compare a population that reproduces sexually, with separate males and females each
producing two offspring per generation (holding population size constant), against a population
that reproduces asexually — parthenogenetically or hermaphroditically — where every individual can
produce offspring. Two asexual females, each having (say) two offspring, both of which can
themselves reproduce, grow the population at twice the exponential rate of a sexual population that
has to "spend" half of every generation producing males, who do not themselves bear young. Whenever
a mutation arises in a sexual population that switches an individual to parthenogenetic
reproduction, that lineage should, in principle, spread rapidly — and this is not purely
hypothetical: sharks kept in captivity for years without access to a male have been documented to
give birth via parthenogenesis ("virgin birth").

The cost is not unique to full biparental sex with distinct sexes — it is the most extreme point on
a spectrum whose underlying theme is *sharing DNA*. Bacterial horizontal gene transfer carries a
milder version of the same cost: a bacterium such as *B. subtilis* entering a competence state to
take up external DNA has to stop dividing while it does so, and risks taking up DNA that is
actively harmful. So the question is general: what selective advantage from recombination could be
large enough to outweigh even the mildest version of this cost, let alone the twofold cost of
males?

## The Red Queen hypothesis

The paper the lecture discusses ("Running with the Red Queen," read for this session) argues for
recombination's advantage via genetic diversity, in a specific form. In a purely asexual (clonal)
population, two independently-arising beneficial mutations in different lineages cannot both reach
fixation together — only the fitter of the two genotypes wins, and the population has to wait for
the second mutation to arise again, this time in the winning background, before it can also spread.
This is **clonal interference**, covered earlier in the course. Recombination breaks that
constraint: a beneficial allele can spread through the population *as a gene*, moving across
different genetic backgrounds by outcrossing, rather than being permanently tied to the one
individual in which it first arose. A sexually-reproducing population can therefore adapt faster
when adaptation requires combining multiple beneficial changes.

That advantage only matters if the environment changes enough, and often enough, to keep rewarding
new combinations — and a genuinely fixed abiotic environment may not change fast or dramatically
enough on its own to make this worth the twofold cost. The **Red Queen hypothesis** (the name is
from the Red Queen in Lewis Carroll's *Through the Looking-Glass*, who has to keep running just to
stay in the same place) proposes a specific, reliable source of that constant change: coevolving
**parasites**. A parasite population is under selection to target whichever host genotype is
currently common, because that is where it can spread most easily; the host population is, in
effect, continually being "chased" away from whatever genotype the parasites have most recently
adapted to. Both populations are then locked in a moving target dynamic — a treadmill of mutual
adaptation — that keeps generating exactly the kind of environmental change that favors
recombination.

One loose end raised in class: bacteria and other microbes also carry parasites (phage, plasmids)
and also exchange genes horizontally, yet full obligate sex with two distinct sexes is overwhelmingly
a feature of large, multicellular organisms. The professor's own tentative answer (offered as a
guess, not as settled) is that body size and generation time are correlated, and generation time
sets the pace at which a population can itself evolve: large organisms, with long generation times,
evolve slowly relative to their much-faster-reproducing parasites, and are therefore precisely the
organisms most in need of a mechanism — recombination — that speeds up their own rate of adaptation
without waiting on new mutations one at a time.

## The C. elegans / Serratia coevolution experiment

The paper's central experiment tests the Red Queen prediction directly, using the millimeter-scale
nematode *C. elegans* and its bacterial pathogen *Serratia marcescens*. The worm side of the
experiment used three mating regimes:

- **wild type** — able to self-fertilize or outcross with males, as normal;
- **obligate outcrossing** — forced to mate with males every generation;
- **obligate selfing** — forced to self-fertilize, with outcrossing prevented.

Each was challenged with three bacterial regimes:

- **coevolution** — the bacteria surviving each round of infection were propagated forward, so the
  pathogen population evolves alongside the host population;
- **no evolution** — worms were repeatedly challenged with the same, unevolving ancestral bacterial
  strain;
- **control** — no bacterial challenge at all.

Two results stood out. First, under coevolving bacteria, the **obligate-selfing** worm population
was driven extinct — a purely clonal host population could not keep pace with a pathogen population
that kept adapting to it. Second, tracking the **outcrossing rate** (the fraction of matings
involving males) in the wild-type population over time gave a striking contrast between the two
bacterial regimes: against coevolving bacteria, the outcrossing rate rose from roughly 20% to as
high as 80% and *stayed elevated*; against the fixed ancestral strain, the outcrossing rate also
rose at first but then fell back down once the population had adapted to that unchanging challenge.
In other words, sex was favored specifically by a moving target, not by a fixed one — exactly the
Red Queen prediction.

The paper's own closing sentence, which the lecture singles out as remarkable in its honesty: "sex
can facilitate adaptation to novel environments, but the long-term maintenance of sex requires that
the novelty does not wear off." That is, this experiment supports sex as a response to ongoing
coevolutionary novelty, but does not by itself explain why that novelty would be sustained
indefinitely in nature — an open question the lecture leaves standing rather than resolving.

## Sources

- MIT 8.591J (Systems Biology), Fall 2014 — lecture recording `cn5k8r8ceii` (transcript only; no
  slides or board images were supplied). Timestamps below refer to that transcript.
  - Microparasite/macroparasite distinction, ubiquity of parasites, phage-cheater aside: 00:00–10:25.
  - The $x,y$ infection model, $R_0$ definition, the geometric-distribution argument, and the
    $R_0=\beta k/[u(u+v)]$ derivation: 11:42–29:25.
  - Vaccination threshold and the disease/$R_0$ table (values beyond the "5–15" and "3–5" ranges
    quoted verbally were on a physical handout the professor held up in class and are not in the
    transcript): 29:25–1:02:56.
  - Two-strain model, no-super-infection assumption, the $R_2>R_1$ invasion derivation: 31:37–46:00.
  - Trade-off cases for $\beta(v)$ and the evolution of virulence, including the super-infection
    caveat: 47:06–57:34.
  - Evolution of sex, twofold cost of males, Red Queen hypothesis, body-size aside: 1:02:56–1:14:17.
  - The *C. elegans*/*Serratia* experiment and its results: 1:14:17–1:17:39.
- **Referred to but not contained in the transcript**: chapter 11 of Martin Nowak's book on
  evolutionary dynamics (the primary source for both the basic infection model and the two-strain
  virulence model — the super-infection extension of that chapter, covering more than two
  co-circulating strains, was mentioned but explicitly not covered in this lecture); the assigned
  paper "Running with the Red Queen" (source of the *C. elegans*/*Serratia* experiment and its
  closing sentence, quoted from memory in class); the optional supplementary paper by Jamie
  Lloyd-Smith on individual heterogeneity in infectiousness and superspreading; a classic paper by
  Lin Chao on cheater phage strategies under multiple infection; the standard SIR epidemic model
  (pointed at as "just Google SIR," not derived in class, and left to the course's problem set); and
  a card-based in-class polling exercise used to build up the $R_0$ formula and the virulence-vote,
  neither of which is recoverable from audio alone.

---

[← 7. Anticipatory Regulation and Bet Hedging](07-anticipatory-regulation-and-bet-hedging.md) · [Contents](index.md) · [9. Robustness in Bacterial Chemotaxis →](09-robustness-in-bacterial-chemotaxis.md)
