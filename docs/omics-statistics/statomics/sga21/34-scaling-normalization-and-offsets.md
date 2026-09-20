---
title: "34. Scaling Normalization and Offsets"
course: "StatOmics Sga21"
chapter: 34
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 34. Scaling Normalization and Offsets

## What this covers

This chapter asks two connected questions about count data from sequencing experiments: why does
a gene's apparent differential expression depend on how deeply each sample was sequenced, and why
is the correction for that usually built into the model as an *offset*, rather than done by
rescaling the raw counts before fitting anything? It assumes you know what a sequencing count is,
can read a generalized linear model (GLM) with a log link, and know that a Poisson random variable
$Y \sim \text{Poisson}(\mu)$ has $E[Y] = Var(Y) = \mu$.

## A gene that looks differentially expressed until you account for depth

Take a single gene, measured in two groups of $n = 8$ samples each, with counts simulated so that
the true rate differs between groups:

$$
Y_i \sim \text{Poisson}(7) \text{ for group 1}, \qquad Y_i \sim \text{Poisson}(11) \text{ for group 2}.
$$

Fitting a plain Poisson GLM of the counts on group,

```r
m <- glm(y ~ factor(group), family = "poisson")
```

finds the gene "extremely significantly" differentially expressed (DE). That is the correct
conclusion here, because the two groups really were simulated with different rates. But now suppose
the two groups were also sequenced to different depths — group 2's libraries are on average half
again as large as group 1's:

$$
\text{libSize}_i \sim \text{Poisson}(10^5) \text{ for group 1}, \qquad \text{libSize}_i \sim \text{Poisson}(1.5 \times 10^5) \text{ for group 2}.
$$

Refitting with the library size folded in as an offset,

```r
m <- glm(y ~ factor(group) + offset(log(libSize)), family = "poisson")
```

the gene is *no longer* significant at the 5% level. The lesson stated directly in the material:
**not correcting for sequencing depth produces spurious results.** In this particular simulation
you can see why the correction removes so much of the apparent effect: the ratio of the true group
means, $11/7 \approx 1.6$, is close to the ratio of the average library sizes, $1.5$. Once the model
is told how much more deeply group 2 was sequenced, there is very little "extra" difference left
for the group effect to explain — most of what looked like differential expression was really a
depth difference.

## What the offset does

An offset is a term added to the linear predictor of a GLM with its coefficient fixed at $1$,
rather than estimated from the data. Writing the model with the offset out in full,

$$
\log(\mu_i) = \log(\text{libSize}_i) + \beta_0 + \beta_1 \cdot \text{group}_i
\quad\Longleftrightarrow\quad
\mu_i = \text{libSize}_i \cdot \exp(\beta_0 + \beta_1 \cdot \text{group}_i),
$$

so the model is really asking whether the count is proportional to library size, with $\beta_1$
picking up any *departure* from that proportionality between groups. Sequencing depth is a known,
observed technical quantity — not something to estimate a coefficient for — which is exactly what
an offset is for.

## Why not just rescale the counts instead?

An offset leaves the counts themselves untouched and only changes the fitted mean. The alternative
would be to normalize the counts directly — divide each gene's count by something proportional to
its library size before fitting anything — and then treat the rescaled numbers as ordinary Poisson
or negative-binomial counts. The next example is a demonstration of why that second route is not
innocuous: rescaling a count breaks the relationship between its mean and its variance that a count
distribution assumes.

## Count data has a mean-variance relationship — but not a naive one

For a Poisson random variable, variance and mean are the same quantity, $Var(Y) = E[Y]$, so a gene
with higher average expression has higher absolute variance. To see this relationship (and how
easily it is broken), simulate three variables at very different rates,

$$
Y_{1i} \sim \text{Poisson}(\mu_1 = 5), \qquad Y_{2i} \sim \text{Poisson}(\mu_2 = 50), \qquad Y_{3i} \sim \text{Poisson}(\mu_3 = 500),
$$

then rescale them to share a common mean of $50$ — multiply $Y_1$ by $10$, leave $Y_2$ alone, divide
$Y_3$ by $10$ — and plot the density of each:

```r
df <- data.frame(y = c(y1 * 10, y2, y3 / 10), gr = factor(rep(1:3, each = n)))
ggplot(df, aes(x = y)) + geom_density() + facet_wrap(. ~ gr) + geom_vline(xintercept = 50)
```

The three densities are drastically different, even though all three now have the same mean. That
looks like a contradiction of "variance grows with the mean" — but it isn't. Rescaling a random
variable by a constant $a$ multiplies its mean by $a$ but its *variance* by $a^2$:

$$
Var(Y_3) = 500, \qquad Var(Y_3 / 10) = \tfrac{1}{100} Var(Y_3) = 5, \qquad Var(Y_1 \times 10) = 100 \cdot Var(Y_1) = 500.
$$

So after rescaling, $Y_3/10$ has mean $50$ and variance $5$, while $Y_1 \times 10$ has the *same*
mean $50$ but variance $500$: multiplying counts by a constant moves the mean and variance apart in
a way the Poisson distribution itself never would, at a mean of $50$ a genuine Poisson variable has
variance $50$, not $5$ or $500$. Rescaling has torn the mean and the variance out of the
relationship the Poisson distribution ties them into.

<figure>
<svg viewBox="0 0 320 210" role="img" aria-label="Three densities rescaled to the same mean of 50 but with very different spreads">
  <line x1="30" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <text x="300" y="198" text-anchor="end" font-size="12" fill="currentColor">count</text>
  <path d="M 40,180 Q 165,140 290,180" fill="currentColor" fill-opacity="0.10" stroke="currentColor" stroke-width="1.5"/>
  <path d="M 90,180 Q 165,95 240,180" fill="currentColor" fill-opacity="0.10" stroke="currentColor" stroke-width="1.5" stroke-dasharray="6 3"/>
  <path d="M 140,180 Q 165,35 190,180" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5" stroke-dasharray="2 2"/>
  <line x1="165" y1="20" x2="165" y2="180" stroke="orangered" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="165" y="14" text-anchor="middle" font-size="12" fill="orangered">mean = 50</text>
  <text x="60" y="150" font-size="11" fill="currentColor">Y&#8321;&#215;10 (Var=500)</text>
  <text x="185" y="105" font-size="11" fill="currentColor">Y&#8322; (Var=50)</text>
  <text x="192" y="50" font-size="11" fill="currentColor">Y&#8323;/10 (Var=5)</text>
</svg>
<figcaption>Three Poisson variables rescaled to share the same mean of 50: the narrower and taller
the density, the smaller its variance after rescaling — multiplying counts by a constant does not
preserve the Poisson mean-variance relationship.</figcaption>
</figure>

## The coefficient of variation: relative certainty grows with the mean

The right way to compare "how noisy" variables are across very different means is the coefficient
of variation, $CV(Y) = SD(Y) / E[Y]$: the standard deviation as a fraction of the mean, i.e. the
relative rather than absolute spread. For a Poisson variable,

$$
CV(Y) = \frac{\sqrt{Var(Y)}}{E[Y]} = \frac{\sqrt{\mu}}{\mu} = \frac{1}{\sqrt{\mu}},
$$

which is a *decreasing* function of $\mu$, matching what the material states directly:

$$
CV(\mathbf{Y}_3) \le CV(\mathbf{Y}_2) \le CV(\mathbf{Y}_1),
$$

confirmed numerically by

```r
calcCV <- function(x) sd(x) / mean(x)
```

on the three simulated samples, and shown by plotting the sample mean against the sample CV for
each. So although the *absolute* variance of a Poisson count grows with its mean, the *relative*
uncertainty about that mean shrinks as the mean grows — highly expressed genes are noisier in
absolute terms but relatively more precisely measured than lowly expressed ones. This also explains
the density plot above without any contradiction: the coefficient of variation is unchanged by
multiplying a variable by a positive constant (both the standard deviation and the mean scale by
the same factor $a$, so the ratio is unaffected), so $Y_3/10$ still carries the low relative
variability of the original, high-mean $Y_3$, and $Y_1 \times 10$ still carries the high relative
variability of the original, low-mean $Y_1$ — rescaling changed the mean and the absolute variance,
but not the relative variability each variable inherited from its true, unscaled mean.

## Putting the two examples together

The two halves of this chapter are the same issue seen from opposite sides. Correcting for a
technical factor like sequencing depth by adding it as an *offset* in the GLM changes the fitted
mean but leaves the observed counts, and therefore their built-in Poisson (or negative-binomial)
mean-variance relationship, untouched — that is what made the offset fit in the first example
behave sensibly. Correcting for the same kind of technical factor by *scaling* — dividing or
multiplying the counts themselves by a size factor before modelling — is exactly the operation shown
in the second example to break that relationship: it moves the mean and the variance apart from
each other in a way no count distribution would produce on its own. That is the caution behind the
title "scaling versus offsets": normalizing by transforming the counts and normalizing by adding a
known term to the model are not interchangeable, and only the latter keeps the data looking like the
count data the downstream model assumes it is.

## Sources

- All content, both R examples and the mean-variance/coefficient-of-variation argument, from
  `sequencing_scalingNormalization.md` (statOmics SGA21, "Scaling normalization and offsets"),
  the sole source supplied for this chapter — no slides, transcript or exercises were provided.
- The material points to, but does not itself contain, a more formal justification: Appendix B1 of
  Ahlmann-Eltze & Huber (2021), *"Comparison of Transformations for Single-Cell RNA-Seq Data"*,
  bioRxiv 2021.06.24.449781.

---

[← 33. RNA-seq Differential Expression Pipeline](33-rna-seq-differential-expression-pipeline.md) · [Contents](index.md) · [35. Filtering, Aliasing, and limma-voom →](35-filtering-aliasing-and-limma-voom.md)
