---
title: "63. Multiple Testing and FWER"
course: "Berkeley Stat 210A Fall 2024"
chapter: 63
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 63. Multiple Testing and FWER

## What this covers

When many hypotheses are tested at once — one coefficient per predictor in a regression, one test
per SNP, one test per website tweak — testing each one at the usual level $\alpha$ no longer
controls the chance of a wrong conclusion. This chapter sets up the multiple testing problem,
defines the standard error criterion for it (the familywise error rate), and derives the two
classical corrections that control it: Bonferroni and Šidák. It assumes familiarity with p-values
and single-hypothesis testing at a fixed level.

## The multiple testing problem

The setting: an observation $X \sim P_\theta \in \mathcal{P}$, and $m$ null hypotheses
$H_{0i}: \theta \in \Theta_{0i}$ for $i = 1, \dots, m$ — commonly $H_{0i}: \theta_i = 0$. The goal is
to return an accept/reject decision for *each* $i$, not just one.

Write

$$\mathcal{R}(X) = \{i : H_{0i} \text{ rejected}\} \subseteq \{1, \dots, m\}, \qquad
\mathcal{H}_0(\theta) = \{i : H_{0i} \text{ true}\},$$

and let $R(X) = |\mathcal{R}(X)|$ and $m_0 = |\mathcal{H}_0|$ be the number of rejections and the
number of true nulls.

This is not a niche setup. The lecture's examples:

- testing $H_{0j}: \beta_j = 0$ for each of $j = 1, \dots, d$ coefficients in a linear regression,
- testing whether each of 2 million SNPs is associated with a phenotype (diabetes, schizophrenia),
- testing whether each of 2000 website tweaks affects user engagement.

In each case $m$ is large and a decision is wanted per hypothesis, not a single global verdict.

## Why testing each hypothesis at level $\alpha$ fails

The obvious procedure — reject $H_{0i}$ whenever its own p-value is at most $\alpha$ — controls the
error rate of *that one test*, but not of the collection.

**Example.** Let $X_i \overset{\text{ind.}}{\sim} \mathcal{N}(\theta_i, 1)$ for $i = 1, \dots, m$,
with $H_{0i}: \theta_i = 0$, and reject each $H_{0i}$ at its own level-$\alpha$ cutoff. If every
null is true,

$$\mathbb{P}_\theta(\text{any } H_{0i} \text{ rejected}) = 1 - (1-\alpha)^{m_0} \to 1
\quad \text{as } m_0 \to \infty.$$

However small $\alpha$ is, enough independent tests make a false rejection all but certain. Is that
a problem? The lecture's answer: yes, if attention ends up focused entirely on the (false)
rejections and none on the correct non-rejections — which in practice, with a list of "significant"
findings, it usually does.

## The familywise error rate

The classical fix is to control the probability of *any* false rejection at all, not the error rate
of each test separately. Define the **familywise error rate** (FWER):

$$\text{FWER}_\theta = \mathbb{P}_\theta(\text{any false rejections}) =
\mathbb{P}_\theta(\mathcal{R} \cap \mathcal{H}_0 \neq \emptyset).$$

The goal is a procedure with

$$\sup_{\theta \in \Theta} \text{FWER}_\theta \le \alpha,$$

i.e. control over every possible configuration of true and false nulls, not merely under the global
null $m_0 = m$.

FWER-controlling procedures are typically built by first computing a marginal p-value $p_i(X)$ for
each hypothesis — satisfying $p_i \overset{H_{0i}}{\gtrsim} \mathcal{U}[0,1]$, meaning
$\mathbb{P}_\theta(p_i \le t) \le t$ for $\theta \in \Theta_{0i}$ — and then "correcting" the
collection $p_1(X), \dots, p_m(X)$ into a joint rejection rule. (For the Gaussian example above, the
usual two-sided p-value is $p_i(X) = 2(1 - \Phi(|X_i|))$.)

## Bonferroni correction

**Procedure.** Reject $H_{0i}$ iff $p_i \le \alpha/m$.

**Why it controls FWER, for arbitrary dependence among the $p_i$:**

$$\begin{aligned}
\mathbb{P}_\theta(\text{any false rejections})
&= \mathbb{P}_\theta\Big(\bigcup_{i \in \mathcal{H}_0} \{H_{0i} \text{ rejected}\}\Big) \\
&\le \sum_{i \in \mathcal{H}_0} \mathbb{P}_\theta(H_{0i} \text{ rejected}) \\
&\le m_0 \cdot \frac{\alpha}{m} \le \alpha,
\end{aligned}$$

where the last inequality uses $m_0 \le m$. The only tool used is the union bound, so the guarantee
holds no matter how the $p_i$'s depend on each other. That generality is also the cost: the
threshold is divided by the *total* number of tests $m$, even though only $m_0 \le m$ of them are
actually null, so the correction is conservative whenever $m_0$ is much smaller than $m$.

## Šidák correction: using independence

If the p-values are independent, the threshold can be relaxed to

$$\tilde{\alpha}_m = 1 - (1-\alpha)^{1/m},$$

which is the value solving $(1 - \tilde\alpha_m)^m = 1 - \alpha$ — the exact threshold that would
make a single fixed-level test's chance of *no* false rejection equal $1-\alpha$ across $m$
independent nulls, mirroring the calculation in the worked example above. Since
$1 - (1-\alpha)^{1/m} \ge \alpha/m$, Šidák's threshold is never smaller than Bonferroni's, and is
strictly larger for $m > 1$ — it rejects (weakly) more often, at the price of requiring independence
that Bonferroni does not need.

The source material breaks off mid-derivation at the point of setting up
$\mathbb{P}_\theta(\text{no false rejections}) = \prod_{i \in \mathcal{H}_0}
\mathbb{P}_\theta(p_i > \tilde\alpha_m)$, using independence to turn the probability of avoiding
any false rejection into a product over the true nulls. The remaining step — bounding each factor
using $p_i \overset{H_{0i}}{\gtrsim} \mathcal{U}[0,1]$ and $m_0 \le m$ — is not recorded in the
supplied notes.

## Beyond this lecture

The lecture's own outline lists four further topics — stepdown multiple testing, simultaneous
intervals ("deduced inference"), false discovery rate control, and the Benjamini–Hochberg
procedure — as items 3 through 6. None of these is covered in the material supplied for this
chapter; only the multiple testing setup, the FWER criterion, and the Bonferroni and (partial)
Šidák corrections (items 1–2, into the start of 3) are present.

## Sources

- Handwritten lecture notes, "Lecture 26: Multiple testing" (outline slide and following pages),
  Berkeley STAT210A. The same scanned lecture appears twice in the supplied material — under both
  the fall-2025 and fall-2026 course directories — with identical content, so this chapter draws on
  one reading of it:
  `statistics/berkeley/stat210a/fall-2025/handwritten/lecture26-multipletesting.md` (and its
  fall-2026 duplicate). Both are machine reconstructions of a handwritten PDF with no text layer;
  the source page itself flags the prose as paraphrased in places and every equation as unverified,
  and the notes above should be checked against the original scan before being cited further.
- No slide deck, lecture transcript, or problem set was supplied alongside these notes.
- The lecture's own outline names "Stepdown multiple testing," "Simultaneous intervals / deduced
  inference," "False Discovery Rate control," and "Benjamini–Hochberg Procedure" as later sections;
  none of that material is present in what was supplied, so it is not covered here.

---

[← 62. The Nonparametric Bootstrap](62-the-nonparametric-bootstrap.md) · [Contents](index.md) · [64. Wald and Score Tests →](64-wald-and-score-tests.md)
