---
title: "4. Describing and Relating Quantitative Data"
course: "GTPB Psls20"
chapter: 4
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 4. Describing and Relating Quantitative Data

## What this covers

Given a batch of measurements on one quantitative variable — a cholesterol level, a BMI, a height —
how do you look at its shape, summarise where it is centred and how spread out it is, and check
whether it behaves like a Normal distribution? And once there are two such variables measured on
the same subjects, how do you say whether they move together? This chapter works through those
questions with the NHANES health-survey data as the running example, and assumes you already know
what a probability density is and what the Normal distribution looks like.

## Looking at the shape: histogram and density

A histogram is the first look at a quantitative variable. Two choices make it usable rather than
just decorative:

- **Equal-width bins**, so that bar height is comparable across the plot; the number of bins can be
  tuned (the `bins` argument), and too few or too many bins hide or manufacture structure.
- **Relative frequency (density) rather than raw counts** on the $y$-axis, so that histograms of
  samples of different sizes — or a histogram against a fitted curve — can be compared directly.

When there are enough observations, a **kernel density estimate** can be overlaid: a smoothed
estimate of the underlying density $f(x)$ that does not depend on where the bin edges happen to
fall. The worked example throughout is `NHANES` filtered to females, plotting `DirectChol` (direct
cholesterol) as a histogram with a density overlay.

## The boxplot: quantiles, IQR, and outliers

A **quantile** $x_{a\%}$ is the value of the variable that cuts off a given probability from below:
$F(x_{a\%}) = P[X \le x_{a\%}] = a\%$. The median is the $50\%$ quantile; the first and third
quartiles, $Q_1$ and $Q_3$, are the $25\%$ and $75\%$ quantiles. Their spread,
$\mathrm{IQR} = Q_3 - Q_1$, is exactly the width of the box in a boxplot.

The whiskers are not the minimum and maximum of the data. They extend to the most extreme
observation that still lies within $1.5 \times \mathrm{IQR}$ of the nearest quartile; anything
beyond that fence is drawn as an individual point — an outlier.

<figure>
<svg viewBox="0 0 300 220" role="img" aria-label="Anatomy of a boxplot showing the box, whiskers, and an outlier beyond the fence">
  <line x1="130" y1="30" x2="130" y2="70" stroke="currentColor" stroke-width="1.5"/>
  <line x1="112" y1="30" x2="148" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <rect x="100" y="70" width="60" height="80" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <line x1="100" y1="110" x2="160" y2="110" stroke="currentColor" stroke-width="2"/>
  <line x1="130" y1="150" x2="130" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="112" y1="190" x2="148" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="130" cy="15" r="3" fill="currentColor"/>
  <text x="175" y="18" font-size="12" fill="currentColor">outlier</text>
  <text x="175" y="34" font-size="12" fill="currentColor">fence: 1.5×IQR</text>
  <text x="175" y="74" font-size="12" fill="currentColor">Q3 (75%)</text>
  <text x="175" y="113" font-size="12" fill="currentColor">median</text>
  <text x="175" y="153" font-size="12" fill="currentColor">Q1 (25%)</text>
  <text x="175" y="193" font-size="12" fill="currentColor">fence: 1.5×IQR</text>
</svg>
<figcaption>The box spans the interquartile range with the median marked inside; whiskers reach to
the most extreme point still within 1.5×IQR of the box, and anything beyond is plotted as a
separate outlier point.</figcaption>
</figure>

In `ggplot`, a boxplot always needs an `x` aesthetic. Giving it a single string (`x=""`) puts every
observation in one box; giving it a factor (a treatment group, say) produces one box per group,
which is how boxplots are normally used to compare groups. For small to moderate sample sizes the
raw data can be added on top with `geom_point(position="jitter")` — and since the outliers would
then be plotted twice, `geom_boxplot(outlier.shape=NA)` suppresses the boxplot's own outlier
markers. The running example for grouped boxplots is the armpit-microbiome transplant experiment:
relative abundance of *Staphylococcus* plotted by treatment, one box per treatment arm with the raw
points jittered underneath.

## Central location: mean, median, and the geometric mean

### Mean versus median

The mean uses every observation, but that is also its weakness: it is very sensitive to outliers.
A concrete illustration from a survey on desired number of sexual partners (Miller and Fishkin,
1997): the mean reported by men was 64.3 and by women 2.8 over a 30-year span — but the *median*
for both men and women was 1. A handful of very large reported values drag the mean far from where
most of the data actually sit; the median ignores them entirely.

### Geometric mean

$$\sqrt[n]{\prod_{i=1}^n x_i} = \exp\left\{\frac{1}{n} \sum_{i=1}^n \log(x_i)\right\}$$

The geometric mean sits closer to the median than the ordinary (arithmetic) mean does, because
taking logs before averaging removes skewness — a few very large values contribute much less once
they are compressed onto a log scale. That makes it, for many biological measurements, a more
useful measure of central location than either the mean or the median:

1. It uses all the observations, unlike the median, so it is more precise.
2. It **is** the ordinary mean computed on log-transformed data, so classical statistical machinery
   — hypothesis tests, confidence intervals — can be applied directly to it without modification.
3. It is naturally suited to quantities that cannot be negative, such as concentrations.
4. A difference on the log scale has a direct interpretation as a log fold change:
   $$\log(B) - \log(A) = \log\!\left(\frac{B}{A}\right) = \log(FC_{B \text{ vs } A})$$
   In genomics the $\log_2$ transform is the usual choice, so that a difference of 1 corresponds to
   a fold change of exactly 2.

Applied to the NHANES cholesterol data: the ordinary mean is pulled upward by the skew in the raw
values, while the geometric mean sits close to the median. Taking $\log_2$ of `DirectChol` makes
the distribution visibly more symmetric, and a Normal density fitted to the log-transformed data
(mean and sd on the log scale) tracks the histogram much better than a Normal fitted to the raw
scale would.

## Variability: variance, standard deviation, and reference intervals

Variability is not a nuisance to be summarised away — it is often the thing being asked about.
Biologists routinely want to know how spread out organisms are across a study region, and when
comparing groups, a treatment effect is only visible once it stands out against the variability
within groups. A large part of applied statistics is exactly this: deciding how much of the total
variability is explained by something measured (treatment, age, ...) and how much is left
unexplained.

**Sample variance** and **sample standard deviation**:

$$s_X^2 = \sum_{i=1}^n \frac{(X_i - \bar X)^2}{n-1}, \qquad s_X = \sqrt{s_X^2}$$

The variance is hard to interpret directly because it is in the square of the original units. The
standard deviation fixes that, and for data that are approximately Normally distributed it has a
direct reading:

- about 68% of observations fall in $\bar x - s_x$ to $\bar x + s_x$;
- about 95% of observations fall in $\bar x - 2s_x$ to $\bar x + 2s_x$.

These are called 68% and 95% **reference intervals** — but they are only valid under (approximate)
Normality. If the data are not Normally distributed, these intervals do not hold.

For skewed data the standard deviation is a poor summary of spread, for the same reason the mean is
a poor summary of centre: both are very sensitive to outliers. The robust alternative is the
**interquartile range**, $Q_3 - Q_1$ — precisely the width of the box in a boxplot.

## Checking Normality: QQ-plots

Whenever an analysis leans on an assumption that the data are Normally distributed, that assumption
needs to be checked, not asserted. The standard tool is the **QQ-plot** (quantile-quantile plot):
the observed quantiles of the sample are plotted against the quantiles the Normal distribution would
predict. If the data really are Normal, the two sets of quantiles line up and the points fall on a
straight line; systematic curvature away from the line is evidence against Normality.

The catch is that *some* deviation from the line is always present, purely from sampling
variability, even when the data genuinely are Normal — and learning to tell a systematic deviation
from a random one is the actual skill being taught here. Simulating nine independent samples of size
20 from a Normal distribution with $\mu = 18$, $\sigma = 9$ makes the point directly: both the
histograms and the QQ-plots of these nine perfectly-Normal samples show visible wiggle and mild
curvature, just from the noise of having only 20 points.

Contrast that with real data: BMI for females in NHANES. The histogram is visibly right-skewed, and
the QQ-plot shows a *systematic* pattern rather than random noise — the lower-tail quantiles sit
above the reference line (the lower tail is compressed relative to what Normality predicts) and the
upper-tail quantiles also sit above the line (the upper tail is stretched out, i.e. a long tail to
the right). Both tails deviating from the line in this coordinated way is the signature of skew, not
of sampling noise.

## Two continuous variables: covariance and correlation

Now suppose each subject contributes a *pair* of measurements, $(X_i, Y_i)$ — height and weight,
say. A scatterplot of NHANES height against weight (for females over 25) shows an association, but
also that weight itself is right-skewed; log-transforming weight makes it somewhat less skewed
(though still not fully Normal), which is worth checking with a histogram and a QQ-plot on the
variable before trying to summarise the *relationship* between the two.

**Covariance** measures how $X_i$ and $Y_i$ deviate from their respective means, together:

$$\mathrm{Cov}(X,Y) = E\big[(X - E[X])(Y - E[Y])\big]$$

**Correlation** standardises the covariance by the variability of each variable separately, which
is what makes it comparable across different pairs of variables:

$$\mathrm{Cor}(X,Y) = \frac{E\big[(X-E[X])(Y-E[Y])\big]}{\sqrt{E\big[(X-E[X])^2\big]}\,\sqrt{E\big[(Y-E[Y])^2\big]}}$$

The sign of the correlation is easiest to see by splitting the scatter at the two means:

<figure>
<svg viewBox="0 0 320 240" role="img" aria-label="Scatter of points split at the mean of each variable into four quadrants, marked with the sign each quadrant contributes to the covariance">
  <line x1="20" y1="120" x2="300" y2="120" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="160" y1="20" x2="160" y2="220" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="165" y="18" font-size="12" fill="currentColor">mean of x</text>
  <text x="230" y="130" font-size="12" fill="currentColor">mean of y</text>
  <text x="235" y="55" font-size="13" fill="currentColor">+</text>
  <text x="80" y="55" font-size="13" fill="currentColor">−</text>
  <text x="80" y="195" font-size="13" fill="currentColor">+</text>
  <text x="235" y="195" font-size="13" fill="currentColor">−</text>
  <circle cx="60" cy="185" r="3" fill="currentColor"/>
  <circle cx="80" cy="165" r="3" fill="currentColor"/>
  <circle cx="50" cy="200" r="3" fill="currentColor"/>
  <circle cx="100" cy="150" r="3" fill="currentColor"/>
  <circle cx="240" cy="60" r="3" fill="currentColor"/>
  <circle cx="260" cy="45" r="3" fill="currentColor"/>
  <circle cx="230" cy="75" r="3" fill="currentColor"/>
  <circle cx="270" cy="90" r="3" fill="currentColor"/>
  <circle cx="70" cy="70" r="3" fill="currentColor" fill-opacity="0.5"/>
  <circle cx="250" cy="185" r="3" fill="currentColor" fill-opacity="0.5"/>
</svg>
<figcaption>Splitting the cloud at the mean of each variable: points in the top-right or
bottom-left quadrant make $(X_i-\bar X)(Y_i-\bar Y)$ positive, points in the other two quadrants
make it negative. A cloud sitting mostly in the "+" quadrants, as here, has positive covariance
and positive correlation.</figcaption>
</figure>

### Pearson correlation

The sample version of this — the **Pearson correlation** — is

$$r = \frac{\sum_{i=1}^n (X_i - \bar X)(Y_i - \bar Y)}{(n-1)\, s_X s_Y}$$

Positive correlation means $x \nearrow \Rightarrow y \nearrow$; negative correlation means
$x \nearrow \Rightarrow y \searrow$; and $r$ is always between $-1$ and $1$. On the NHANES data,
computing the correlation matrix of `Weight`, `Height`, and `log2(Weight)` shows the correlation
between height and weight is *lower* when weight is left untransformed than when it is put on the
log scale — a direct consequence of the two limitations below.

**It is sensitive to outliers.** Simulating $x \sim N(0,1)$ and $y = 2x + \text{noise}$ gives a
clean, fairly strong positive correlation. Adding a *single* additional point far from the trend
(at $(2,-4)$, well below where the line would predict) noticeably changes the computed correlation
— one point, out of twenty-one, is enough to move it. This is the same sensitivity the mean and the
standard deviation have, for the same reason: all three are built from sums, and a single large
term dominates a sum.

**It only captures *linear* association.** Simulating $x \sim N(0,1)$ and $y = x^2 + \text{noise}$
— a textbook nonlinear relationship, $y$ clearly determined by $x$ — gives a Pearson correlation
close to zero, because the positive and negative deviations of $x$ from its mean correspond to the
*same* sign of deviation in $y$ (both up), and they cancel in the sum that defines $r$. A
correlation near zero here does not mean "no relationship"; it means "no *linear* relationship."
This is why a scatterplot should always be looked at, not just the correlation number.

Repeating the height/weight-style scatter with different amounts of added noise (and then with the
sign flipped) shows how the *magnitude* of $r$ tracks how tightly the cloud hugs a line, while
flipping the sign of $y$ simply mirrors the cloud and flips the sign of $r$ without changing how
tightly it hugs the line.

### Spearman correlation

The **Spearman correlation** is defined as the Pearson correlation computed after replacing every
observation with its rank. It is less sensitive to outliers than the Pearson correlation, because an
extreme value only ever contributes an extreme *rank* — the largest or smallest available — no
matter how far out it actually sits; the raw magnitude of the outlier is discarded. This can be
checked directly: computing the Pearson correlation on the ranked data by hand gives exactly the
same number as calling the Spearman method directly, confirming that "Spearman" is nothing more
than "Pearson, after ranking."

Because of this robustness, Spearman correlation is the better default for skewed data or data with
outliers — such as the raw (untransformed) NHANES weight and height — where the Pearson correlation
can be pulled around by the skew or by a handful of extreme points.

## Sources

- Histogram, boxplot (quantiles, IQR, outlier fence), mean vs. median, geometric mean and log fold
  change, sample variance/standard deviation and reference intervals, and interquartile range:
  [`02-univariate-exploration-of-quantitative-variables.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/04-dataExploration.Rmd),
  GTPB PSLS20, theory unit 4 ("Data exploration"), CC BY 4.0.
- QQ-plots, the simulated-Normal-data illustration, and the NHANES BMI example:
  [`03-normale-approximation.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/04-dataExploration.Rmd),
  same unit.
- Covariance, correlation, Pearson correlation (including the outlier and nonlinearity examples)
  and Spearman correlation:
  [`04-two-continuous-variables-correlation.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/04-dataExploration.Rmd),
  same unit.

All three files are converted course notes (CC BY 4.0) rather than a slide/transcript pair; no
separate transcript or problem set was supplied for this chapter, so none is used or exercised here.
The notes point forward to "chapter 5" for the hypothesis tests and confidence intervals that the
log-transformed (geometric-mean) data enable, which is not part of this chapter's material. The
worked examples throughout use the `NHANES` R package and the course's armpit-microbiome transplant
data set (`data/armpit.csv`), both external to these notes.

---

[← 3. Experimental Design and Randomization](03-experimental-design-and-randomization.md) · [Contents](index.md) · [5. Data Exploration Case Studies →](05-data-exploration-case-studies.md)
