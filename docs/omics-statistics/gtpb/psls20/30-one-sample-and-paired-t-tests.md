---
title: "30. One-Sample and Paired t-Tests"
course: "GTPB Psls20"
chapter: 30
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 30. One-Sample and Paired t-Tests

## What this covers

This chapter works through two related questions about a single dataset — is a mean above a
fixed reference value, and did a treatment change a mean — to introduce the one-sample $t$-test
and the paired two-sample $t$-test. It assumes the reader already knows the captopril dataset from
the data-exploration tutorial (systolic blood pressure, SBP, measured in 15 patients before and
after treatment) and has some prior exposure to the general logic of a hypothesis test: stating a
null and alternative hypothesis, checking assumptions, then interpreting a test's output.

## The dataset and the two questions

The captopril data record, for 15 patients, systolic blood pressure (SBP) and diastolic blood
pressure, each measured twice: before treatment (SBPb) and after treatment (SBPa) with the drug
captopril. Two research questions drive the tutorial:

1. Is the average SBP **before** treatment (SBPb) higher than 149 mmHg?
2. Is the average SBP before treatment significantly **different** from the average SBP after
   treatment?

These look similar but call for different tests: the first compares one sample's mean to a fixed
number, the second compares two measurements taken on the *same* patients.

## Question 1: is SBPb above 149 mmHg?

### Where the threshold comes from

The value 149 is not arbitrary. In the earlier exploration of the NHANES dataset, a reference
interval was built — an interval expected to contain 95% of the SBP values of healthy
individuals — and it came out as $[93, 149]$ mmHg. To find patients who genuinely have elevated
blood pressure (candidates for a captopril trial), it is exactly the patients whose SBP sits above
the *upper* end of that healthy reference interval, 149 mmHg, that are of interest. So the question
"is SBPb higher than 149?" is really "are these patients, on average, outside the healthy range on
the high side?" — which is why the alternative hypothesis is one-sided rather than "different from".

### Setting up the test

This is a **one-sample $t$-test**: one sample of SBPb measurements is compared against a fixed,
hypothesized value $\mu_0 = 149$. The hypotheses are

$$H_0: \ \mu_{\text{SBPb}} = 149 \qquad \text{vs.} \qquad H_A: \ \mu_{\text{SBPb}} > 149.$$

The alternative is one-sided (greater than, not merely unequal) because the question being asked
is specifically whether the patients' blood pressure is elevated, not whether it merely differs
from 149 in either direction.

### Checking the assumptions first

A $t$-test is only valid if two conditions hold, and they must be checked *before* looking at the
test result, not after:

1. **Independence** — the 15 patients' measurements do not influence one another.
2. **Normality** — the SBPb values are (at least approximately) normally distributed.

Normality is not taken on faith; it is assessed graphically with a **quantile–quantile (QQ) plot**,
which plots the sample's sorted values against the quantiles a normal distribution would predict.
If the points fall close to a straight line, normality is a reasonable working assumption; a
systematic curve or heavy departure at the tails is evidence against it. Only once this plot has
been interpreted and judged acceptable does it make sense to proceed to the test itself.

## Question 2: did treatment change SBP?

### Why the two measurements cannot be treated as two independent samples

SBPb and SBPa are not two independent samples of blood pressure — they are two measurements on the
*same* 15 patients. A patient who starts with a high SBPb tends to still have a comparatively high
SBPa, treatment or not: the two values are correlated within a patient. A scatterplot of SBPa
against SBPb makes this visible directly, in the tutorial's own words: "if a patient's SBPb value
is high, its SBPa value will be comparatively high as well." Ignoring that correlation — treating
the before- and after-measurements as if they came from two unrelated groups of patients — would
throw away information and understate how tightly the two values move together.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Before and after SBP values for several patients, joined by a line to show within-patient pairing">
  <line x1="60" y1="20" x2="60" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="260" y1="20" x2="260" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <text x="60" y="205" text-anchor="middle" font-size="12" fill="currentColor">before (SBPb)</text>
  <text x="260" y="205" text-anchor="middle" font-size="12" fill="currentColor">after (SBPa)</text>
  <line x1="60" y1="40" x2="260" y2="60" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="70" x2="260" y2="95" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="95" x2="260" y2="120" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="120" x2="260" y2="140" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="150" x2="260" y2="165" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="170" x2="260" y2="180" stroke="currentColor" stroke-width="1"/>
  <circle cx="60" cy="40" r="3" fill="currentColor"/>
  <circle cx="60" cy="70" r="3" fill="currentColor"/>
  <circle cx="60" cy="95" r="3" fill="currentColor"/>
  <circle cx="60" cy="120" r="3" fill="currentColor"/>
  <circle cx="60" cy="150" r="3" fill="currentColor"/>
  <circle cx="60" cy="170" r="3" fill="currentColor"/>
  <circle cx="260" cy="60" r="3" fill="currentColor"/>
  <circle cx="260" cy="95" r="3" fill="currentColor"/>
  <circle cx="260" cy="120" r="3" fill="currentColor"/>
  <circle cx="260" cy="140" r="3" fill="currentColor"/>
  <circle cx="260" cy="165" r="3" fill="currentColor"/>
  <circle cx="260" cy="180" r="3" fill="currentColor"/>
</svg>
<figcaption>Each line joins one patient's before- and after-treatment SBP. Patients who start high
tend to stay comparatively high after treatment — the two columns are not independent samples, they
are the same 15 patients measured twice.</figcaption>
</figure>

### Setting up the test

Because the data are paired, the appropriate test is a **paired two-sample $t$-test**, which,
before being applied, again requires its assumptions to be checked and the diagnostic plots
examined — as with the one-sample test above.

### The paired test is a one-sample test on the differences

The tutorial makes explicit a fact that is easy to miss when only reading the software's output:
a paired two-sample $t$-test *is* a one-sample $t$-test, run on the within-patient differences
$d_i = \text{SBPb}_i - \text{SBPa}_i$. Rather than comparing two columns of numbers, it collapses
each patient down to a single difference and then asks whether the mean of those differences is
zero:

$$H_0: \ \mu_d = 0 \qquad \text{vs.} \qquad H_A: \ \mu_d \neq 0.$$

That this is exactly what is happening internally is visible in the statistical software's own
wording: the alternative hypothesis reported by the paired test literally reads "the true
difference in means is not equal to 0" — the same statement a one-sample test on the differences
would produce. Running the two calculations side by side gives identical output, which is the
point: pairing is not a different kind of test so much as a different kind of data-reduction step
that turns two correlated samples back into the single-sample situation already handled in
Question 1.

## Exercises

Both exercises use the captopril dataset (15 patients, SBP measured before and after treatment).

1. Test whether the mean systolic blood pressure before captopril treatment (SBPb) is greater
   than 149 mmHg. State the null and alternative hypotheses, check whatever assumptions the test
   requires (including the relevant diagnostic plot), carry out the appropriate test, and write a
   conclusion that is precise, concise, and answers the original research question — not just
   "reject $H_0$" or "$p < 0.05$".

2. Test whether the mean SBP before treatment differs from the mean SBP after treatment. First
   argue, using a plot, why the two measurements should not be treated as independent samples.
   State and check the assumptions for the appropriate paired test, carry it out, and write a
   conclusion. Then verify that computing the within-patient differences and running a one-sample
   test on them gives the same result as the paired test, and explain why that has to be so.

## Sources

Both sections are drawn from the exercise script *Hypothesis testing: captopril* (GTPB PSLS20,
"05 Statistical Inference" tutorial), split into two parts in the converted material:

- Question 1 — one-sample $t$-test setup, the NHANES reference interval, the QQ-plot assumption
  check: `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half/01-question-1.md`.
- Question 2 — paired two-sample $t$-test, the scatterplot argument for pairing, and the
  equivalence to a one-sample test on the differences:
  `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half/02-question-2.md`.

No slide deck or lecture transcript was supplied for this session — the exercise script is the
only source. The script itself refers to, but does not contain, the data-exploration tutorial from
the previous day (where the captopril dataset and the NHANES reference interval were first built)
and the actual R output of running `t.test()` on the data, since the code cells are left as blanks
for the student to complete.

---

[← 29. Checking t-test Assumptions](29-checking-t-test-assumptions.md) · [Contents](index.md) · [31. Hypothesis Testing on the Cuckoo Data →](31-hypothesis-testing-on-the-cuckoo-data.md)
