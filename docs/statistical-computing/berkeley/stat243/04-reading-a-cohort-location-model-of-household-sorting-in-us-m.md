---
title: "4. Reading: A Cohort Location Model of household sorting in US metropolitan regions"
course: "Berkeley Stat 243"
chapter: 4
source: "https://doi.org/10.1177/0042098016668783"
licence: "summary only \u2014 the paper is not reproduced"
written: "2026-10-01"
---

> **Summary of a paper.** Estiri, H. and Krause, A. (2016). A Cohort Location Model of household sorting in US metropolitan regions. Urban Studies (OnlineFirst), pp. 1-20. ([original](https://doi.org/10.1177/0042098016668783)). The paper is © its rights holder and is not reproduced here: this is a short account of it in our own words, standing in for it in the reading of Berkeley Stat 243.

# 4. Reading: A Cohort Location Model of household sorting in US metropolitan regions

## What this covers

A household-sorting model for US metropolitan regions: whether the age of a household's
householder predicts how far from the city centre that household is likely to live, across the
50 largest US metropolitan areas.

## The question

Research on residential mobility had long used a household's position in the lifecycle (newly
formed, child-rearing, empty-nest, and so on) as a predictor of when and why households move, but
that account was increasingly criticised as too rigid: it forces households into discrete stages
and does not fit the more varied trajectories of modern households. A companion paper by the same
first author had proposed a "phasic" model that grouped households into three lifecycle phases and
showed each phase settles at a different distance from the city centre. This paper asks whether
that spatial sorting effect survives when the artificial phase boundaries are removed and a
household's age is instead treated as a continuous variable — and, if so, what the shape of the
sorting pattern actually looks like across the country's largest metropolitan regions.

## The approach

The authors build a Cohort Location Model (CLM) from two assumptions. First, a household's housing
consumption grows over its housing career, approximated using the age of the householder as a
proxy for that career stage. Second, in the prevailing US pattern of low-density suburban
development, the overall bundle of housing services on offer (space, structure, access to
schools and amenities) increases with distance from the city centre or centres. Combining the two
predicts a systematic age gradient in residential location: younger households, with lower housing
consumption, cluster near the centre, while older households are drawn toward the urban fringe
where more housing services are on offer — with middle-aged households expected to be the hardest
group to tell apart spatially, since their housing consumption is changing most slowly.

To test this, they combine 2010 Census block-level population data with block geography for the 50
largest US Core Based Statistical Areas (a combined 2010 population of over 166 million, more than
half the US total). For each metropolitan area they located the city centre and any subcentres,
computed the great-circle distance from every census block to its nearest one, and standardised
that distance to a 0–1 scale (dropping blocks more than 60 miles out as effectively rural). Ages
were grouped into eight 10-year cohorts, the finest grouping the Census data allow. For each cohort
at each distance band they computed a location quotient — the share of that cohort's households
found at that distance, divided by the share of all households found there — so that an age group
that is simply larger or smaller overall does not distort the comparison. Location quotients were
summarised both with a LOESS-smoothed trend and a linear regression trend, each with confidence
intervals, pooling across all 50 metropolitan areas.

## What it found

The predicted gradient appears clearly. As householder age rises, the trend line's slope moves
from negative (over-represented near the centre) to positive (over-represented toward the fringe),
with the sign change occurring around age 35 — matching the threshold the earlier phasic model had
used to separate its first lifecycle phase. The 15-to-24 cohort has by far the highest location
quotient at the centre of any group, and is statistically distinguishable there from every other
cohort, including the next-youngest (25-to-34). At the metropolitan fringe the order is close to a
mirror image, with the 75-to-84 cohort showing the highest location quotient, though the very
oldest group (85 and over) is, perhaps surprisingly, somewhat more centrally located than the
cohorts just younger than it, while still being less central than the two youngest cohorts.

Away from the two extremes, the picture is less sharp. The four cohorts spanning ages 35 to 64
account for most of the suburban population, but their location-quotient trend lines overlap
enough, once confidence intervals are taken into account, that the model cannot statistically
tell them apart from one another in the suburbs — even though collectively they clearly dominate
that part of the metropolitan region. The authors read this as consistent with their model, which
predicts housing consumption (and therefore location) changes slowly across these middle years.
Overall they identify four statistically distinct clusters of cohorts near the centre and five
near the fringe.

## Limits and context

The authors are explicit that census data cannot observe why an older household relocates — in
particular "downsizing," a residential adjustment they build into their account of the oldest
cohorts, which they note is not a well-studied phenomenon and is likely driven by multiple factors
the Census does not record. They also distinguish the generality of their two assumptions: housing
consumption rising over a household's life span is argued to hold globally, but the second
assumption — that housing services increase with distance from the centre — reflects a
specifically American pattern of suburban development, and the model's geometry would need to be
adjusted for metropolitan regions elsewhere. The cohort resolution is limited to 10-year age bands
by the granularity of the Census data used, and blocks more than 60 miles from a centre were
excluded as likely rural rather than genuinely metropolitan. The full analysis code and a cleaned
version of the underlying dataset were released publicly so the results could be reproduced.

## Sources

Read from the publisher PDF: `sources/berkeley-stat243/stat243-fall-2021/ps/clm.pdf`.

## Citation

Estiri, H. and Krause, A. (2016). "A Cohort Location Model of household sorting in US metropolitan
regions." *Urban Studies* (OnlineFirst), pp. 1–20. The paper's own first page gives only the page
range 1–20 and a 2016 copyright date; no volume or issue number is printed on it, consistent with
an OnlineFirst publication ahead of print assignment. DOI: https://doi.org/10.1177/0042098016668783

---

[← 3. Regular Expressions and Testing](03-regular-expressions-and-testing.md) · [Contents](index.md) · [5. Code Review and Homework Habits →](05-code-review-and-homework-habits.md)
