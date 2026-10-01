---
title: "1. Statistics in the Scientific Method"
course: "GTPB Psls20"
chapter: 1
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 1. Statistics in the Scientific Method

## What this covers

This chapter opens the course with three real studies — a microbiome-transplant experiment on
smelly armpits, a repeated-sampling exercise using the NHANES cholesterol survey, and the 1954
Salk polio-vaccine trial — to introduce the ideas the rest of the course is built on: what a
sample can and cannot tell you about a population, why the same experiment gives a different
answer every time it is repeated, and how confounding can make a treatment look effective (or
ineffective) when it is not. It assumes only that the reader knows what a mean, a standard
deviation, a standard error and a p-value are; no other statistical machinery is assumed.

## The smelly armpit experiment

Smelly armpits are not caused by sweat itself. The smell comes from specific bacteria,
*Corynebacterium spp.*, that metabolise sweat into odorous compounds. A second group of bacteria
that is just as abundant on the skin, *Staphylococcus spp.*, does not produce the smell. A
research group at Ghent University proposed transplanting the armpit microbiome as a therapy for
people with smelly armpits: first remove the existing microbiome with antibiotics, then influence
its regrowth with a microbial transplant.

To test this, 20 subjects with smelly armpits were split into two groups: a placebo group
(antibiotics only) and a transplant group (antibiotics followed by a microbial transplant). Six
weeks after treatment, the armpit microbiome was sampled and analysed by DGGE (denaturing gradient
gel electrophoresis). The outcome measured was the relative abundance of *Staphylococcus spp.*
among *Corynebacterium spp.* plus *Staphylococcus spp.* — the idea being that a successful
transplant should shift this balance toward the harmless *Staphylococcus*.

## Why a barplot is not enough

Before any modelling, the data has to be looked at — data exploration is, in the lecturer's words,
"extremely important to get insight in the data" and "often underrated and overlooked." For the
armpit data, summarising each treatment group by its mean, standard deviation, number of
observations $n$ and standard error $se = s/\sqrt{n}$ is the obvious first step.

The natural way to *show* that summary is a barplot of the two group means, with the standard
error added as an error bar. But this plot is not informative, and it fails for reasons that
generalise well beyond this example:

- A barplot shows only a two-point summary of the data (mean and spread). A table would say the
  same thing in less space.
- It wastes most of its area — everything from zero up to somewhere near the smallest observed
  value — on a region where no data exist at all.
- It hides the shape of the distribution and the sample size entirely.

A boxplot is better, because it shows the distribution rather than a single summary: a box
spanning the 25th to 75th percentile with the median marked inside it, whiskers extending to the
most extreme observation still within $1.5\times$ the box's width (the interquartile range) of the
box, and any points beyond that plotted individually as outliers.

Even a boxplot is not the end of it, though, when the sample is small — and 10 observations per
group *is* small. The rule the lecture draws from this is a general one: **it is always better to
show the data as raw as possible.** The informative version of the plot is a boxplot with the
outlier markers turned off (they would just duplicate points already visible) and every individual
observation overlaid on top, jittered sideways slightly so that points do not stack exactly on top
of one another. That plot — box, whiskers, and every one of the 20 subjects visible as a point —
is the one that actually earns the description "informative."

## Random sampling and the scope of a study

Two questions the armpit example raises directly: why do we need more than one subject per group
at all, and what does it actually mean, and cost, to select subjects "at random"?

Compare two ways a research assistant might have recruited the 20 subjects:

1. Twenty male students with smelly armpits, recruited from the assistant's own faculty.
2. Twenty people with smelly armpits, recruited completely at random from the entire Belgian
   population.

The lecture illustrates the two designs with simulated versions of the same experiment: design 1
gives a sample with smaller variability, while design 2 gives a sample with larger variability and
a lower relative abundance of *Staphylococcus*. Neither design is unconditionally "better" — the
question the lecture leaves open is which is.

The resolution is that random sampling is inseparable from the *scope* of the study — the
population to which the researchers intend to generalise their conclusions. That scope has to be
fixed before the study starts, and it can be narrow ("male students") or broad ("all Belgians with
this condition"). Once the scope is fixed, a valid statistical analysis requires the subjects to
be selected **completely at random** from that population, which means two things jointly:

- every subject in the population has the same probability of being selected, and
- the selection of one subject is independent of the selection of every other subject.

A sample built this way is representative of its population precisely *because* it is random, not
in spite of it. This is also the trade-off behind the two designs above: recruiting only male
students at one faculty buys lower variability, but the conclusions only ever generalise back to
male students at that faculty; recruiting randomly from the whole population is noisier, but the
conclusions generalise to the population the study actually claims to be about.

## Sample-to-sample variability: the NHANES cholesterol example

The NHANES (National Health and Nutrition Examination Survey) has interviewed individuals of all
ages in their homes every year since 1960, with a health examination carried out in a mobile
examination centre. Because it is large, it stands in here for "the population" against which a
small experiment can be checked.

The question posed is whether direct cholesterol differs between men and women over 25.
Cholesterol concentrations are skewed — they cannot go below zero — so they are conventionally
log-transformed first, after which the two distributions look roughly bell-shaped. Restricting
NHANES to subjects over 25 with a recorded cholesterol value and adding a log-cholesterol column
gives a large reference dataset; its mean, standard deviation and standard error by sex are what
an experimenter would like to know but, in a real study, does not have direct access to.

Instead, suppose the budget only allows measuring 10 women and 10 men. Draw that sample at random
from the reference data, summarise it, and test for a sex difference with a two-sample t-test
(equal variances assumed):

$$
t = \frac{\bar{x}_{F} - \bar{x}_{M}}{s_p\sqrt{\tfrac{1}{n_F}+\tfrac{1}{n_M}}}, \qquad
s_p = \sqrt{\frac{(n_F-1)s_F^2 + (n_M-1)s_M^2}{n_F+n_M-2}}
$$

with a two-sided p-value from $T_{n_F+n_M-2}$. The sample mean already differs from the
large-dataset mean, simply because it is a sample. Repeating the exact same procedure — same
sample size, same random selection rule, same large dataset to draw from — gives a *different*
sample, different summary statistics, and a different t-test result each time. In one repetition
in the lecture, the sampled difference between the sexes even ran in the opposite direction from
the large-dataset comparison, which, taken as the only evidence, would have supported the wrong
conclusion about which sex has the higher level.

That every repetition of an identical design gives a different answer is the central point:
**conclusions drawn from a sample are themselves subject to uncertainty and can change from
sample to sample.** The lecture quantifies how often this goes wrong by repeating the same
10-versus-10 sampling procedure 20,000 times and, for each repetition, recording the sample mean
difference and its two-sided p-value. Tallying the 20,000 repetitions into three outcomes —
significant in the correct direction, not significant, significant in the wrong direction — shows
that a sizeable share come back *not significant* (the design has low power with only 10 subjects
per group), while reversals of the kind seen above, significant *and* in the wrong direction, are
very rare. A single small experiment can therefore easily be inconclusive, and can occasionally be
actively misleading, even though the great majority of repetitions of the same design point the
right way.

## Confounding: the Salk polio-vaccine study

In 1916 the US experienced its first large polio epidemic. In the early 1950s John Salk developed
a vaccine that showed promising results in the lab, and in 1954 the National Foundation for
Infantile Paralysis (NFIP) mounted a large field study of its effectiveness. Suppose the NFIP had
simply vaccinated a large number of children in 1954 and observed that polio incidence that year
was lower than in 1953 — could that alone have shown the vaccine worked?

The design actually run in 1954 was more careful than that, but still flawed. In school districts
with high polio incidence, second-graders whose parents consented were vaccinated (the *cases*);
first- and third-graders formed a comparison group that was not offered vaccination at all (the
*controls*); and second-graders whose parents did **not** consent formed a third group (*no
consent*).

| group | grade | vaccinated | total | polio cases | incidence per million |
|---|---|---|---|---|---|
| cases | 2nd | yes | 221,998 | 54 | 243 |
| control | 1st & 3rd | no | 725,173 | 391 | 539 |
| no consent | 2nd | no | 123,605 | 56 | 453 |

The puzzle is in the last row: the no-consent children were not vaccinated, exactly like the
controls, yet their incidence (453 per million) was noticeably lower than the controls' (539 per
million). Vaccination cannot explain that difference, since neither group was vaccinated.

The explanation is confounding. Consent to vaccinate was associated with socio-economic status,
and socio-economic status was itself associated with susceptibility to the disease — children of
lower socio-economic status turned out to be more resistant to polio. So the three groups differ
not only in vaccination status but also in age, socio-economic status and underlying
susceptibility, and these differences are entangled with each other.

<figure>
<svg viewBox="0 0 260 220" role="img" aria-label="Socio-economic status confounds the association between vaccination consent and polio incidence">
  <defs>
    <marker id="arrowC" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="47.8" y1="163.3" x2="122.2" y2="51.7" stroke="darkorange" stroke-width="1.5" marker-end="url(#arrowC)"/>
  <line x1="54" y1="175" x2="206" y2="175" stroke="darkorange" stroke-width="1.5" marker-end="url(#arrowC)"/>
  <line x1="137.8" y1="51.7" x2="212.2" y2="163.3" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowC)"/>
  <circle cx="40" cy="175" r="14" fill="none" stroke="darkorange" stroke-width="1.5"/>
  <text x="40" y="179" text-anchor="middle" font-size="12" fill="darkorange">S</text>
  <text x="40" y="205" text-anchor="middle" font-size="11" fill="currentColor">socio-economic status</text>
  <circle cx="130" cy="40" r="14" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="130" y="44" text-anchor="middle" font-size="12" fill="currentColor">V</text>
  <text x="130" y="20" text-anchor="middle" font-size="11" fill="currentColor">consent to vaccinate</text>
  <circle cx="220" cy="175" r="14" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="220" y="179" text-anchor="middle" font-size="12" fill="currentColor">P</text>
  <text x="220" y="205" text-anchor="middle" font-size="11" fill="currentColor">polio incidence</text>
</svg>
<figcaption>Socio-economic status (S) drives both consent to vaccinate (V) and polio susceptibility
(P), so a raw comparison of consenting against non-consenting groups mixes the vaccine's effect
with the effect of who was willing and able to consent.</figcaption>
</figure>

A second study fixed this by randomising: after parental consent was obtained, children were
assigned **at random** to vaccine or to an indistinguishable placebo, and the trial was **double
blind** — neither the parents nor the caregivers assessing the children knew which had been given.

| group | treatment | total | polio cases | incidence per million |
|---|---|---|---|---|
| vaccine | vaccine | 200,745 | 57 | 284 |
| placebo | placebo | 201,229 | 142 | 706 |
| no consent | none | 338,778 | 157 | 463 |

Two things fall out of this table. First, once cases and controls are genuinely comparable — both
drawn from the same consenting population, differing only in the coin flip that assigned treatment
— the estimated effect of the vaccine is much larger (284 versus 706 per million) than the
original comparison suggested. Second, as an internal check, the no-consent group's incidence
barely moved between the two studies (453 versus 463 per million): its risk had nothing to do with
which trial was running, only with who those children were, which is exactly what should happen if
socio-economic status, not the vaccine, was driving that group's numbers all along.

## The scientific method

Empirical data is central to the life sciences, and research is largely driven by it. The lecture
frames the whole enterprise as a triangle linking a natural process, a theory about it, and the
data collected on it.

<figure>
<svg viewBox="0 0 320 240" role="img" aria-label="Triangle linking nature, a theory, and data through experiment and statistical inference">
  <polygon points="160,30 40,190 280,190" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="18" text-anchor="middle" font-size="13" fill="currentColor">Nature</text>
  <text x="40" y="208" text-anchor="middle" font-size="13" fill="currentColor">Model</text>
  <text x="280" y="208" text-anchor="middle" font-size="13" fill="currentColor">Data</text>
  <text x="72" y="103" text-anchor="end" font-size="12" fill="darkorange">theory</text>
  <text x="248" y="103" text-anchor="start" font-size="12" fill="darkorange">experiment</text>
  <text x="160" y="228" text-anchor="middle" font-size="12" fill="darkorange">statistical inference</text>
</svg>
<figcaption>The scientific-method triangle: a model deduces testable consequences (theory), an
experiment turns nature into data, and statistical inference bridges model and data — able only to
reject the model, never to prove it.</figcaption>
</figure>

Reading the three edges as the lecture defines them:

- **Theory** (Model–Nature edge): deduce the logical, testable consequences of a theory or
  hypothesis about the natural process.
- **Experiment** (Nature–Data edge): collect data on that process. Data are a manifestation of the
  real process, not the process itself, so the experiment has to be *representative* and
  *reproducible*, and it has to be designed so that it actually could challenge the theory — this
  is the job of experimental design.
- **Statistical inference** (Model–Data edge): the bridge that confronts the model or hypothesis
  with the data. This is called the cornerstone of the scientific method.

The **falsification principle** follows directly from this picture: data cannot be used to *prove*
a model or hypothesis, only to *reject* it. Data exploration and analysis, in turn, are typically
used to refine the theory and generate new hypotheses — closing the loop back to the model, ready
for another round of deduction.

## The role of statistics in the life sciences

Pulling the three case studies together, the same handful of lessons keeps recurring: the scope of
a study has to be specified carefully before the experiment (the armpit designs); sample size
matters (the cholesterol resampling); confounding has to be watched for, and a proper control is
required (the Salk study). Good experimental design is what all three demand. And because there is
real variability across a population, and any study can only sample a small part of it, every
result and every conclusion carries uncertainty — the cholesterol example showed this directly, by
repeating an identical design and getting a different answer every time.

This is the working definition of statistics the lecture settles on: the science of

1. **collecting** data (experimental design),
2. **exploring** data (data exploration and descriptive statistics), and
3. **learning** from data and generalising what is observed in a sample to the population, while
   quantifying, controlling and reporting variability and uncertainty (statistical modelling and
   inference).

<figure>
<svg viewBox="0 0 320 275" role="img" aria-label="Experimental design draws a sample from the population; estimation and inference carry conclusions back">
  <defs>
    <marker id="arrowP" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="20" y="10" width="280" height="90" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="30" y="26" font-size="12" fill="currentColor">population</text>
  <g fill="currentColor">
    <circle cx="55" cy="55" r="3"/><circle cx="80" cy="70" r="3"/><circle cx="105" cy="50" r="3"/>
    <circle cx="130" cy="75" r="3"/><circle cx="155" cy="55" r="3"/><circle cx="180" cy="80" r="3"/>
    <circle cx="205" cy="60" r="3"/><circle cx="230" cy="78" r="3"/><circle cx="255" cy="52" r="3"/>
    <circle cx="275" cy="70" r="3"/><circle cx="115" cy="88" r="3"/><circle cx="200" cy="42" r="3"/>
  </g>
  <text x="160" y="93" text-anchor="middle" font-size="10" fill="currentColor">cholesterol in the population</text>

  <line x1="70" y1="103" x2="70" y2="162" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowP)"/>
  <text x="70" y="122" text-anchor="middle" font-size="10" fill="currentColor">1 experimental</text>
  <text x="70" y="134" text-anchor="middle" font-size="10" fill="currentColor">design</text>

  <line x1="250" y1="162" x2="250" y2="103" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowP)"/>
  <text x="250" y="122" text-anchor="middle" font-size="10" fill="currentColor">3 estimation</text>
  <text x="250" y="134" text-anchor="middle" font-size="10" fill="currentColor">&#38; inference</text>

  <rect x="20" y="165" width="280" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="30" y="181" font-size="12" fill="currentColor">sample</text>
  <g fill="currentColor">
    <circle cx="100" cy="200" r="3"/><circle cx="130" cy="200" r="3"/><circle cx="160" cy="200" r="3"/>
    <circle cx="190" cy="200" r="3"/><circle cx="220" cy="200" r="3"/>
  </g>
  <text x="160" y="218" text-anchor="middle" font-size="10" fill="currentColor">cholesterol in the sample</text>

  <text x="160" y="245" text-anchor="middle" font-size="10" fill="currentColor">2 data exploration &#38;</text>
  <text x="160" y="257" text-anchor="middle" font-size="10" fill="currentColor">descriptive statistics</text>
</svg>
<figcaption>The full cycle: experimental design draws a sample from the population, data
exploration summarises what is in the sample, and estimation and inference carry that summary back
to a statement about the population.</figcaption>
</figure>

Because it plays this role in collecting, exploring and learning from data, statistics is not a
side tool but a load-bearing part of almost every science — the lecture points to the "Points of
Significance" column that Nature Methods runs for exactly this reason.

## Exercises

1. The 20,000-repetition simulation of the cholesterol experiment (10 women and 10 men sampled at
   random from the NHANES data, compared with a two-sample t-test at the 5% level) sorts its
   outcomes into three bins: significant in the correct direction, not significant, and
   significant in the wrong direction. Redo the simulation with a sample size of 50 per group
   instead of 10. What changes about the balance between the three bins, and why?

## Sources

All material in this chapter comes from the introductory lecture ("`theory/01-intro.Rmd`") of the
GTPB PSLS20 course *Practical Statistics for the Life Sciences*, converted to markdown (CC BY 4.0)
in the knowledge-base-library:

- [Smelly armpit example](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/01-intro.Rmd) — the experiment, descriptive statistics, barplot/boxplot comparison, and
  the two hypothetical recruitment designs.
- Sample to sample variability — the NHANES cholesterol example, the repeated 10-vs-10 sampling
  experiments, and the 20,000-repetition simulation and its embedded assignment.
- Salk Study — the NFIP 1954 field trial, its confounding, and the randomised double-blind
  follow-up.
- Scientific Method — the nature/theory/data triangle and the falsification principle.
- Role of Statistics in the Life Sciences — the definition of statistics and the
  population/sample/inference cycle.

No lecture transcript, slide deck or separate problem set was supplied for this session; the five
files above are the complete raw material, each carrying live R code that was run during the
lecture. Numeric incidence-per-million figures in the Salk-study tables are computed directly from
the case counts given in that source, using the same formula (`polio / total * 1e6`, rounded) shown
in its code.

---

[Contents](index.md) · [2. Population, Sample, and Random Variables →](02-population-sample-and-random-variables.md)
