---
title: "4. The Cohort Location Model"
course: "Berkeley Stat 243"
chapter: 4
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 4. The Cohort Location Model

## What this covers

STAT 243 (Fall 2021) assigns "A Cohort Location Model of household sorting in US metropolitan
regions" (Estiri and Krause, *Urban Studies*, 2016) as a reading for problem set 2, question 2(b):
students skim the paper's Method section, look at the authors' published code, and are asked to
judge how reproducible the analysis actually is. This chapter reconstructs the paper itself — the
question it answers, the model it builds, the data pipeline behind the results, and the paper's own
reproducibility statement — since that is the material the exercise is judged against. It assumes no
background in urban economics or demography; it does assume familiarity with linear regression and
LOESS smoothing, the two statistical tools the paper relies on throughout.

## Why households move within a metropolitan area

Household mobility is described as the "engine of change" in cities: between 2012 and 2013 more
than 35 million people in the US changed residence, and Current Population Survey data put about
75% of moves between 1999 and 2010 down to housing- or household-related reasons. The classic
explanation is a disequilibrium story — a household moves when there is a mismatch between its
*actual* and *desired* consumption of "housing services": not just square footage, but a bundle
that includes dwelling type, structure, and proximity to schools and amenities.

What drives that mismatch is mostly the household, not the neighbourhood: household- and
housing-related factors dominate over locational ones. Two examples from the paper are worth
keeping in mind because the rest of the argument leans on them:

- **Household size.** A larger family raises the chance of choosing a larger unit; for households
  already in crowded housing, the birth of a child can be enough to trigger dissatisfaction and a
  move. High mobility is therefore expected around small dwellings and around childbirth.
- **Tenure.** Homeownership substantially reduces mobility, so higher mobility rates cluster in
  markets with a large rental stock and a younger population.

Both point to the same underlying variable: a household's needs change fast (as it forms, has
children, ages), while the housing stock in a given location does not. Something has to give, and
the something is household location.

## From lifecycle stages to a continuous cohort model

If household needs drive relocation, and needs track family status, then age of the householder is
a natural proxy for where a household is in that process. This is the **lifecycle approach**,
standard in mobility research from the 1950s through the 1970s: households pass through discrete
stages — Abou-Lughod and Foley's four (pre-child, childbearing/childrearing, child-launching,
post-child) is one version — and it is the *transition* between stages, not steady socioeconomic
change, that triggers a move. Age is consistently found to be negatively associated with the
probability of moving; a synthesis by Simmons found roughly 20% of moves happen under age 10, 60%
between ages 10 and 40, and 20% after 40.

The lifecycle approach was eventually criticised as too deterministic and inconsistent about where
the stage boundaries actually fall, and it does not fit modern household forms well (single-parent
households, later marriage, and so on). It was largely displaced by the **lifecourse approach**,
which treats a household's history as a set of parallel, interacting transitions (marriage,
children, work, education) rather than a fixed sequence of stages.

A direct predecessor to this paper, the **phasic model** (Estiri et al. 2015), sits between the two:
it keeps age as the organising variable but tries to make the stages empirically grounded rather
than a priori. It splits households into three phases — phase one (ages 15–34): low housing
consumption, high mobility, tends to live near the city centre; phase two (ages 35–59): consumption
peaks, mobility is at its lowest; phase three (60+): consumption falls off slightly and mobility
ticks back up as households downsize. The phasic model's central finding is that phase-one
households cluster centrally and phase-two/three households cluster in the suburbs.

The paper in this chapter — the **Cohort Location Model (CLM)** — takes the phasic model's two
underlying assumptions (about housing consumption and about metropolitan land-use patterns) but
removes the phase boundaries. Age is treated as a continuous variable rather than being cut into
three bins chosen in advance, so any age-based pattern the data actually contain can show up at
whatever resolution the data allow, instead of being forced into three pre-specified groups.

## The Cohort Location Model

The CLM rests on two assumptions, stated explicitly in the paper:

1. **Housing consumption rises over a household's housing career.** As a household ages
   (the paper's proxy for progress through that career), it consumes more housing services, and the
   paper describes this increase as roughly logarithmic in age — steep early, flattening later.
2. **Housing services increase with distance from the city centre.** Because of the predominantly
   low-density ("suburban") pattern of US metropolitan development, larger lots, larger homes, and
   more of the housing-service bundle are available farther from the central business district
   (CBD) than close to it. ("City centre" here covers both single-centre and multi-centre metro
   areas; the paper writes "CBD" throughout as shorthand for whichever applies.)

Put the two together and a prediction falls out: since younger households consume less housing and
older households consume more, and since more housing is on offer farther from the centre, younger
households should sort toward the CBD and older households toward the metropolitan fringe. The
paper works this prediction out further than "young near the centre, old far away" — it predicts
*where the ordering by age is sharp and where it blurs*, which is what makes the model testable
rather than just a plausible story.

<figure>
<svg viewBox="0 0 400 260" role="img" aria-label="Schematic of predicted location-quotient trend lines by age cohort, from city centre to metropolitan fringe">
  <line x1="40" y1="200" x2="370" y2="200" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="200" x2="40" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="115" x2="370" y2="115" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <text x="374" y="118" font-size="11" fill="currentColor">LQ = 1</text>
  <line x1="156" y1="200" x2="156" y2="30" stroke="currentColor" stroke-width="1" stroke-dasharray="2 4" opacity="0.5"/>
  <line x1="40" y1="70" x2="370" y2="198" stroke="currentColor" stroke-width="1.6"/>
  <line x1="40" y1="85" x2="370" y2="170" stroke="currentColor" stroke-width="1.6"/>
  <line x1="40" y1="124" x2="370" y2="98" stroke="currentColor" stroke-width="1.6"/>
  <line x1="40" y1="154" x2="370" y2="43" stroke="currentColor" stroke-width="1.6"/>
  <text x="12" y="73" font-size="11" fill="currentColor">15–24</text>
  <text x="12" y="88" font-size="11" fill="currentColor">25–34</text>
  <text x="8" y="127" font-size="11" fill="currentColor">45–54</text>
  <text x="8" y="157" font-size="11" fill="currentColor">75–84</text>
  <text x="40" y="215" font-size="12" text-anchor="start" fill="currentColor">CBD</text>
  <text x="156" y="215" font-size="12" text-anchor="middle" fill="currentColor">suburb</text>
  <text x="370" y="215" font-size="12" text-anchor="end" fill="currentColor">metro fringe</text>
  <text x="170" y="18" font-size="11" fill="currentColor">lines nearly cross here</text>
</svg>
<figcaption>The CLM's qualitative prediction (after the paper's own Figure 1): a location
quotient — the relative likelihood of a cohort living at a given distance from the centre — plotted
by distance for several age cohorts. Younger cohorts start highest and fall; older cohorts start
lowest and rise; the lines bunch together near the suburb, where age stops discriminating location,
then fan back out toward the fringe in the reverse order.</figcaption>
</figure>

The paper spells out three consequences of this crossing pattern that the CLM commits to in
advance, and that the results are then checked against:

- **Near the CBD**, the age ordering is sharpest at the extremes: it should be easier to tell a
  24-year-old householder from a 25-year-old than to tell a 42-year-old from a 43-year-old, because
  the youngest and oldest cohorts are most distinct there while the middle-aged cohorts overlap.
- **Near the suburb**, the trend lines converge — middle-aged households dominate this zone, and the
  model expects age to stop discriminating location around here.
- **Near the metropolitan fringe**, the pattern from the CBD reappears in reverse: the ordering is
  sharp again, but oldest-highest and youngest-lowest instead of the other way around.

Because the model is stated as a relationship between age (continuous) and distance (continuous),
it can be tested at whatever age resolution the data support — the paper settles for 10-year age
cohorts because that is what the 2010 Census provides, but nothing in the model requires that
particular bin width.

## Turning Census data into a testable claim

**Study area.** The analysis covers the 50 largest Core Based Statistical Areas (CBSAs) in the US
as of 2013 — 166 million people, 54% of the US population — chosen partly for coverage and partly
so the results are comparable to earlier studies using the same set of metro areas.

**Data.** Household counts by age of householder come from the 2010 Census SF1 dataset, question
P22, at the census-block level. P22 reports ten-year age cohorts (with the 55–59/60–64 break
merged back to a consistent 10-year scheme), and family/non-family status is collapsed since it
plays no role here, leaving eight age cohorts per block. This merged block-level table is called
the Household Location Data (HLD).

**Distance.** For every CBSA, the authors located the centre and any named subcentres by hand, via
Google Maps — the CBD is the first city named in the CBSA's official name (e.g. Phoenix in
"Phoenix-Mesa-Scottsdale"), subcentres are the others, and non-municipal names such as a county are
dropped since they have no single centroid. The great-circle distance from each block centroid to
its nearest centre or subcentre is then computed with the Haversine formula, and the minimum such
distance is attached to the block.

This manual step is worth flagging on its own, separately from the statistics: picking centre
coordinates by hand from Google Maps for 50 metro areas is not a scripted, re-runnable procedure in
the way the rest of the pipeline is. Two people repeating it could reasonably choose different
points for a subcentre, and the paper's reproducibility discussion (below) does not mention this
step at all — it is exactly the kind of soft spot a reproducibility check should look for.

**Standardising distance.** Because CBSAs differ enormously in size, raw miles are not comparable
across them. Blocks farther than 60 miles from any centre are dropped as effectively rural (a cutoff
chosen from a visible break in the data, not derived from a rule). Within each CBSA, every
remaining block's distance is then divided by the farthest remaining distance in that CBSA, so
distance runs from 0 (at a centre) to 1 (at the CBSA's own effective edge), rounded to two decimal
places.

## The location quotient

Raw household counts by age and distance are not directly comparable, because the eight age
cohorts are not equally sized to begin with. The paper instead computes a **location quotient**
for each cohort $i$ at each standardised distance $j$ (rounded to the nearest 0.01):

$$\mathrm{LQ}_{ij} = \frac{HH_{ij}/HH_j}{HH_i/HH}$$

where $HH$ is the total household count, $HH_i$ the count in cohort $i$ across the whole region,
$HH_j$ the count at distance $j$ across all cohorts, and $HH_{ij}$ the count in cohort $i$ at
distance $j$. The numerator is cohort $i$'s share of households at distance $j$; the denominator is
cohort $i$'s share of households overall. $\mathrm{LQ}=1$ means the cohort is exactly as common at
that distance as it is region-wide; $\mathrm{LQ}>1$ means over-represented there, $\mathrm{LQ}<1$
under-represented. This is the same device used in regional economics to ask whether an industry
is locally concentrated, applied here to age cohorts and distance instead of industries and
regions.

Because low household counts at some distances make the raw location quotients noisy, the paper
smooths each cohort's series with a **LOESS** (locally weighted regression) fit, using a smoothing
span of 0.1. Both the raw linear-regression trend and the LOESS-smoothed trend are reported, for
the pooled 50-CBSA dataset and for each CBSA separately.

## Results: reading the trend lines

Across the 50 CBSAs pooled together, the slope of the location-quotient trend flips from negative
to positive as age increases — moving from the youngest cohort (15–24) to the oldest (85+), the
probability of living farther from the centre rises. The sign change happens close to age 35, which
the paper notes lines up both with the phasic model's own phase-one cutoff and with independent
findings elsewhere that mobility stabilises around that age.

A few specific, quantitative findings from the smoothed and linear fits (Figures 3–5 in the
original — not reproduced here since the source conversion of this PDF only kept placeholder image
links for them; see the original paper for the actual plots):

- At the city centre, the 15–24 cohort has by far the highest location quotient, and the 25–34
  cohort is second; the gap between these two youngest cohorts and everyone else is statistically
  significant (via non-overlapping confidence intervals).
- Interestingly, the *oldest* cohort (85+) has a **higher** quotient at the centre than every
  cohort between 45 and 74 — even though its quotient there is still below 1 (under-represented
  overall). This is a genuine wrinkle in the "monotonic in age" story, not something the two
  assumptions alone predict.
- Confidence intervals overlap for all cohorts above 35 at the centre and largely overlap for
  cohorts above 35 in the suburbs, meaning the model's prediction that middle age stops
  discriminating location holds up statistically, not just visually.
- The linear-regression view groups the eight cohorts into **four** statistically distinguishable
  clusters at the city centre — {15–24, 25–34}, {35–44}, {45–54, 55–64}, {65+} — and **five**
  clusters at the metropolitan fringe, where the middle cohorts separate out more (35–44, 45–54,
  55–64 are each distinguishable there, while the two youngest and two oldest cohorts still pair
  up).
- At the metropolitan fringe the order is close to an exact reversal of the CBD order: 75–84 highest,
  then 65–74, 85+, 55–64, 45–54, 35–44, 15–24, 25–34 lowest — matching the model's third
  qualitative claim above.

## What the pattern does and does not explain

The paper reads these results as support for a **housing-based** explanation of age sorting: young
households cluster centrally because they consume less housing and because central locations in US
cities tend to offer a smaller bundle of housing services (plus other draws — non-residential land
uses, amenities); middle-aged households dominate the suburbs because that is where the housing
services they now need (space, schools) are available. It draws a direct policy implication:
zoning aimed at compact growth should target the housing needs of middle-aged households in city
centres, since that is the group the suburbs currently absorb almost by default.

Two limits are stated plainly rather than glossed over:

- **The second assumption is US-specific.** The claim that housing services rise with distance from
  the centre depends on the US's characteristic suburban development pattern; applying the CLM
  elsewhere would require re-deriving that assumption for the local land-use pattern, and the
  paper expects the resulting geometry (the shape drawn in Figure 1) to differ by region.
- **The behaviour of the oldest households is not well explained by the model's own machinery.** The
  paper's account for older households leans on "downsizing," which it explicitly notes is not a
  well-studied phenomenon and which the Census data cannot speak to directly — the actual triggers
  for older households' moves (health, widowhood, proximity to family) are not in the dataset at
  all. The 85+ anomaly at the centre noted above is a visible symptom of this gap.

## Reproducibility, and why a computing course assigned this paper

The paper closes with an explicit reproducibility statement: all code is published
(github.com/andykrause/hhLocation), with instructions to download and clean the raw Census data
from scratch, and a pre-cleaned copy of the Household Location Data is also deposited at Harvard's
Dataverse for anyone who wants to skip that step. The paper cites reproducible research as
associated with fewer errors, faster completion, and higher citation counts, and frames its own
release of code and data as satisfying that standard.

This is the reason the paper appears on a statistics-computing syllabus rather than a demography
one: problem set 2 asks students to skim the Method section, look at the actual code the authors
released, and weigh its reproducibility in practice — not from the paper's own self-description, but
from whether the pipeline described above (block-level data, hand-picked centre coordinates,
Haversine distances, the 60-mile cutoff, standardisation, location quotients, LOESS smoothing) can
actually be re-run and re-checked against the released code. The manual centre-picking step flagged
above is exactly the kind of thing that self-description misses and an actual code inspection would
catch.

## Sources

All content in this chapter comes from the 15-section conversion of *ps/clm.pdf* (Estiri H and
Krause A (2016) "A Cohort Location Model of household sorting in US metropolitan regions." *Urban
Studies*, DOI: 10.1177/0042098016668783), as assigned in Berkeley STAT 243, Fall 2021:

- Abstract and author/journal details — `01-abstract.md`
- Motivation and the CLM's two contributions — `02-introduction.md`
- Household- and housing-driven mobility, family size, tenure — `03-why-families-move.md`
- Lifecycle approach, Simmons' 20/60/20 synthesis, stage classifications — `04-the-lifecycle-approach-to-residential-mobility.md`
- The phasic model's three phases and predecessor findings — `05-application-of-a-lifecycle-inspired-approach-in-modelling-ho.md`
- Critique of the lifecycle approach, lifecourse alternative, motivation for relaxing phase boundaries — `06-relaxing-the-phasic-model.md`
- The CLM's two assumptions, Figure 1's qualitative description, study area and CBSA selection — `07-the-cohort-location-model-clm.md`
- Data sources, HLD construction, centre/subcentre geocoding, distance standardisation — `08-data-preparation.md`
- Location quotient formula and LOESS smoothing — `09-computation-of-the-location-quotient.md`
- Pooled results, slope sign change near age 35 — `10-results.md`
- Cluster structure at the CBD and fringe, the 85+ anomaly, confidence-interval comparisons — `11-differences-in-smoothed-pattern-lines.md`
- Linear-regression cluster counts (four at the CBD, five at the fringe) — `12-changes-and-differences-in-linear-patterns.md`
- Interpretation, US-specificity of the second assumption, downsizing and data limits, policy implications — `13-conclusion-and-discussion.md`
- The paper's own reproducibility statement and data/code release — `14-reproducing-this-work.md`
- Full reference list — `15-references.md`

For context on why this reading was assigned (not itself one of the supplied inputs for this
chapter): Berkeley STAT 243, Fall 2021, problem set 2, question 2(b)
(`ps/ps2/02-problems.md`), which asks students to evaluate the reproducibility of the authors'
released code against the Method section reconstructed here.

Not contained in the supplied material: the actual plots (Figures 1–5 of the original paper) are
referenced throughout but the PDF-to-markdown conversion only preserved placeholder links for them;
the code repository (github.com/andykrause/hhLocation) and the cleaned dataset on Harvard Dataverse
that the paper points to are named but not included; and the "Unit 4" reproducibility reading and
the *Practice of Reproducible Research* book that problem set 2 pairs with this paper are named in
the assignment but are separate readings, not part of this source.

---

[← 3. Regular Expressions and Testing](03-regular-expressions-and-testing.md) · [Contents](index.md) · [5. Code Review and Homework Habits →](05-code-review-and-homework-habits.md)
