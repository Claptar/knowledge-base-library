---
title: "68. Multiple Testing"
course: "Berkeley Stat 210A Fall 2024"
chapter: 68
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 68. Multiple Testing

## What this covers

This chapter answers: when you test many hypotheses at once, what does "an error" even mean, and
how do you control it? It moves from a single per-test significance level $\alpha$, through the
classical family-wise guarantee (no false rejections at all) and the general "deduce it from a
confidence region" trick, to the more permissive false discovery rate criterion and the
Benjamini–Hochberg procedure that controls it. The last section proves FDR control by treating the
discovery threshold as a stopping time for a martingale running backward in time, so it helps to
already be comfortable with p-values and confidence regions, and with filtrations, martingales and
optional stopping, from earlier in the course.

## The multiple-testing problem

Many experiments produce not one hypothesis to test but a whole family of them: a coefficient
$\beta_j$ in a linear regression for each of $d$ predictors, an association with a phenotype for
each of tens of thousands of SNPs, an effect on engagement for each of thousands of website tweaks.
In each case there is a single underlying model $X\sim P_\theta \in \mathcal P$ and a family of null
hypotheses

$$H_{0i}: \theta \in \Theta_i, \qquad i=1,\dots,m,$$

commonly of the form $H_{0i}:\theta_i=0$. A procedure returns an accept/reject decision for every
$i$; write

$$R=\{i: H_{0i}\text{ rejected}\},\qquad H_{0c}=\{i: H_{0i}\text{ true}\},\quad |H_{0c}|=m_0\le m.$$

The set $R\cap H_{0c}$ is the set of *false* rejections — nulls that were actually true but got
rejected anyway. The whole chapter is about controlling this set, in one sense or another.

### Why testing at level $\alpha$ per hypothesis is not enough

If each of the $m$ tests is simply run at level $\alpha$ on its own, and all $m$ nulls happen to be
true, the chance that *at least one* is rejected is already

$$\mathbb P(\text{any } H_{0i}\text{ rejected}) \le 1-(1-\alpha)^m \approx m\alpha,$$

which grows with $m$ and can be far larger than $\alpha$. Concretely, if $X_i\sim N(\theta_i,1)$
independently for $i=1,\dots,m$ and $H_{0i}:\theta_i=0$, then under the global null

$$\mathbb P_0(\text{any } H_{0i}\text{ rejected}) = 1-(1-\alpha)^m \approx m\alpha.$$

Whether this actually matters depends on what happens next: if attention will be focused entirely
on the rejections and none on the correct non-rejections, an inflated rate of spurious rejections is
exactly the failure mode worth guarding against.

## Family-wise error rate

The classical fix is to control the **family-wise error rate**,

$$\mathrm{FWER}(\theta) = \mathbb P_\theta(\text{any false rejections}) = \mathbb P_\theta(R\cap H_{0c}\neq\emptyset),$$

and to ask for $\sup_\theta \mathrm{FWER}(\theta)\le \alpha$. This is typically achieved not by
re-deriving a joint test from scratch but by correcting the *marginal* p-values
$p_1(X),\dots,p_m(X)$ — each satisfying $p_i\sim U(0,1)$ under $H_{0i}$ — so that rejecting on a
stricter individual threshold controls the family-wise rate.

### Bonferroni correction

The simplest correction needs no assumption about how the $p_i$ depend on one another. Reject
$H_{0i}$ iff $p_i\le \alpha/m$. Then, by the union bound,

$$\mathbb P_\theta(\text{any false rejections}) \le \sum_{i\in H_{0c}} \mathbb P_\theta(H_{0i}\text{ rejected}) \le \frac{m_0\alpha}{m}\le\alpha.$$

The first inequality only uses that a false rejection is in particular *some* rejection among the
true nulls; the second is the union bound over those $m_0$ tests, each rejected with probability at
most $\alpha/m$ under its own null; the last uses $m_0\le m$. No independence or any other
structure among the tests is used — this is why Bonferroni works under *arbitrary* dependence. For
a Gaussian example, the rule $\phi_i = \mathbf 1\{\alpha/(2m)^{-1}|X_i| > \Phi^{-1}(1-\alpha/(2m))\}$
applies exactly this idea test by test.

### Šidák correction, and why it barely helps

If the $p_i$ actually **are** independent, the union bound above is loose and can be tightened.
Reject $H_{0i}$ iff $p_i \le 1-(1-\alpha)^{1/m}$. Then

$$\mathbb P_\theta(\text{no false rejections}) = \prod_{i\in H_{0c}} \mathbb P_\theta\big(p_i > 1-(1-\alpha)^{1/m}\big) \ge (1-\alpha)^{m_0/m}\ge 1-\alpha,$$

using independence to turn the probability of the intersection into a product. For small $\alpha$,
$1-(1-\alpha)^{1/m}\approx \alpha/m$, so Šidák's threshold is barely different from Bonferroni's: at
$\alpha=0.05$, $m=20$, Bonferroni rejects below $0.0025$ and Šidák below $0.00256$ — a negligible
improvement for having assumed independence.

## Testing under dependence

Since exploiting independence buys so little, it's natural to ask whether *dependence* — the thing
that made the naive per-test approach fail in the first place — can instead be turned to advantage.
It can, dramatically, when the dependence between the tests has enough structure.

### Scheffé's S-method

Suppose $X\sim N(\theta,I_d)$ and the hypotheses concern $m$ different linear combinations of the
same $d$-dimensional mean vector: $H_{0j}: a_j^\top\theta = 0$ for $j=1,\dots,m$, with $\|a_j\|=1$
(there can be far more hypotheses $m$ than dimensions $d$ — every direction $a_j$ gives one). Reject
$H_{0j}$ if

$$|a_j^\top X| > \sqrt{d\,F_{d,\infty,1-\alpha}}.$$

This controls the FWER exactly, and the reason is not a union bound at all: it is a single
probability statement about $X$,

$$\mathbb P\big(\|X-\theta\|^2 \le d\,F_{d,\infty,1-\alpha}\big) = 1-\alpha,$$

i.e. $\theta$ lies in the confidence ball $C(X)=\{\theta:\|X-\theta\|^2\le dF_{d,\infty,1-\alpha}\}$
with probability $1-\alpha$. By Cauchy–Schwarz, whenever $\theta\in C(X)$, every unit vector $a_j$
satisfies $|a_j^\top(X-\theta)|\le\|X-\theta\|\le\sqrt{dF_{d,\infty,1-\alpha}}$ — so a false rejection
of some true $H_{0j}$ (where $a_j^\top\theta=0$) can only happen when $\theta\notin C(X)$. One
confidence statement, deduced in $m$ different directions at once, however large $m$ is. That is
the general idea the next section makes precise.

## Deduced inference

**General principle.** Given any $(1-\alpha)$ confidence region $C(X)$ for $\theta$, once we commit
to treating $\theta\in C(X)$ as true, *every* logical consequence of that assumption can be asserted
freely, with no extra cost to the error rate:

$$\mathbb P_\theta(\text{any deduced inference is wrong}) \le \mathbb P_\theta(\theta\notin C(X)) \le \alpha.$$

This holds because "some deduced inference is wrong" can only happen when the premise
$\theta\in C(X)$ itself was wrong — deducing correctly from a true premise cannot produce a false
conclusion. This is a good paradigm specifically for producing **simultaneous confidence
intervals**: $C_1(X),\dots,C_m(X)$ are simultaneous $1-\alpha$ confidence intervals for
$g_1(\theta),\dots,g_m(\theta)$ if

$$\mathbb P_\theta\big(g_i(\theta)\in C_i(X)\text{ for all }i=1,\dots,m\big) \ge 1-\alpha.$$

Deducing them from a single joint region is easy but comes with a caveat worth having in view before
the example: intervals *deduced* from a region are only guaranteed to hit $1-\alpha$ or better, not
exactly $1-\alpha$ — in practice they typically overshoot.

### Example: simultaneous intervals for a multivariate Gaussian mean

Let $X\sim N_d(\theta,\Sigma)$ with $\Sigma$ known and $\Sigma_{ii}=1$, and let $t_\alpha$ be the
upper-$\alpha$ quantile of the Mahalanobis norm $\|X-\theta\|_\Sigma =
\sqrt{(X-\theta)^\top\Sigma^{-1}(X-\theta)}$ (when $\Sigma=I_d$ this is just
$t_\alpha=\sqrt{\chi^2_{d,1-\alpha}}$). Deduce, coordinate by coordinate,

$$C_i(X) = \big[\theta_i : |X_i-\theta_i|\le t_\alpha\sqrt{\Sigma_{ii}}\big].$$

The joint confidence *ellipsoid* $\{\theta:\|X-\theta\|_\Sigma\le t_\alpha\}$ has probability exactly
$1-\alpha$ by construction of $t_\alpha$, and it sits entirely inside the *box* $\prod_i C_i(X)$: a
point satisfying the quadratic constraint automatically satisfies each linear one, again by
Cauchy–Schwarz. So the deduced event "$\theta_i\in C_i(X)$ for every $i$" is guaranteed at least
$1-\alpha$ — but because the ellipsoid sits strictly inside the box, touching it only where the axes
cross it, the box actually has *more* than $1-\alpha$ probability. That is the price of deducing a
rectangle from an ellipse.

<figure>
<svg viewBox="0 0 240 240" role="img" aria-label="An ellipsoidal confidence region inscribed in the rectangle of per-coordinate deduced intervals">
  <rect x="30" y="60" width="180" height="120" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5 4"/>
  <ellipse cx="120" cy="120" rx="90" ry="60" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <line x1="120" y1="60" x2="120" y2="50" stroke="currentColor" stroke-width="1"/>
  <line x1="120" y1="180" x2="120" y2="190" stroke="currentColor" stroke-width="1"/>
  <line x1="30" y1="120" x2="20" y2="120" stroke="currentColor" stroke-width="1"/>
  <line x1="210" y1="120" x2="220" y2="120" stroke="currentColor" stroke-width="1"/>
  <text x="120" y="30" text-anchor="middle" font-size="12" fill="currentColor">rectangle: deduced intervals</text>
  <text x="120" y="123" text-anchor="middle" font-size="12" fill="currentColor">ellipsoid: exact 1-&#945; region</text>
  <text x="120" y="215" text-anchor="middle" font-size="12" fill="currentColor">tangent only on the axes</text>
</svg>
<figcaption>The rectangle of deduced per-coordinate intervals contains the exact $(1-\alpha)$
ellipsoid, touching it only on the axes, so the rectangle's true coverage is at least $1-\alpha$ and
generally more: it is conservative.</figcaption>
</figure>

Building the intervals the other way around — reporting the ellipsoid
$\{\theta:\|X-\theta\|_\Sigma^2\le\chi^2_{d,1-\alpha}\}$ as the confidence region itself, and only
then reading off a bounding box — is exactly the same construction and inherits the same
over-coverage.

### Example: simultaneous intervals in linear regression

The same idea applies with $n$ observations and $d$ predictors, $Y\sim N(X\beta,\sigma^2 I_n)$ with
design matrix $X\in\mathbb R^{n\times d}$. Write $\hat\beta = (X^\top X)^{-1}X^\top Y \sim
N(\beta,\sigma^2(X^\top X)^{-1})$, and $S^2 = \|Y-X\hat\beta\|^2/(n-d)$, $V = S^2(X^\top X)^{-1}$.
The distribution of $\hat\beta_j/\sqrt{V_{jj}}$ is fully known. Assuming without loss of generality
that $X^\top X = I_d$, let $t_\alpha$ be the upper-$\alpha$ quantile of
$\|\hat\beta-\beta\|/\sqrt{S^2}$ (computed by simulation, since it has no simple closed form). Then

$$C_j = \hat\beta_j \pm t_\alpha\sqrt{V_{jj}}, \qquad j=1,\dots,d$$

are simultaneous confidence intervals for all $d$ regression coefficients at once:
$\mathbb P(|\hat\beta_j-\beta_j|\le t_\alpha\sqrt{V_{jj}}\text{ for all }j)=1-\alpha$, by exactly the
same deduction from the joint distribution of $\hat\beta-\beta$.

## False discovery rate

FWER asks for *zero* false rejections with high probability, and that guarantee gets expensive fast
as $m$ grows. With 10,000 independent test statistics, all run at level $\alpha=0.001$, roughly 10
rejections are expected purely by chance under the global null. If the data instead produce 50
rejections, probably only around 20 of them are false discoveries — demanding zero false rejections,
as FWER does, throws away the rest of the signal along with the noise. Benjamini and Hochberg (1995)
proposed a more liberal criterion that tolerates some false rejections provided most rejections are
valid.

Write $R(X)=|R(X)|$ for the number of rejections ("discoveries") and $V(X)=|R(X)\cap H_{0c}|$ for
the number of false discoveries among them. The **false discovery proportion** is

$$\mathrm{FDP} = \begin{cases} V(X)/R(X) & R(X)>0\\ 0 & R(X)=0,\end{cases}$$

and the **false discovery rate** is $\mathrm{FDR}=\mathbb E[\mathrm{FDP}]$ — the expected fraction of
rejections that are wrong, rather than the probability of making any wrong rejection at all.

### The Benjamini–Hochberg procedure

Order the p-values $p_{(1)}\le p_{(2)}\le\cdots\le p_{(m)}$, and let

$$R(X) = \max\{r : p_{(r)} \le \alpha r/m\},$$

rejecting $H_{0(1)},\dots,H_{0(R)}$ — a **step-up** procedure, since it looks for the *largest*
index satisfying an increasingly lenient threshold, unlike Bonferroni's single fixed threshold
$\alpha/m$. It is correspondingly far more liberal: at $\alpha=0.05$, BH rejects at least $r$
p-values as soon as $p_{(r)}\le 0.05\,r/m$, a much easier bar to clear for large $r$ than
Bonferroni's fixed $\alpha/m$.

**As an empirical-Bayes rule.** Let $R(t)=\#\{i:p_i\le t\}$ and $\hat F(t)=R(t)/m$, the empirical CDF
of the p-values. BH rejects $H_i$ whenever $p_i \le T(X) := \max\{t : \hat F(t)\ge t/\alpha\}$. When
$\hat F$ increases continuously between its upward jumps (the usual case with no ties), $T(X)$ is
exactly the point where $\hat F(T(X)) = T(X)/\alpha$: the threshold is the **last crossing** of the
step function $\hat F(t)$ by the line $t/\alpha$, reading from $t=1$ down to $t=0$.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="The empirical CDF of p-values crossing the line t over alpha, marking the Benjamini-Hochberg threshold">
  <line x1="40" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="300" y="197" text-anchor="end" font-size="12" fill="currentColor">t</text>
  <text x="34" y="26" text-anchor="end" font-size="12" fill="currentColor">1</text>
  <path d="M40,180 L53,180 L53,148 L71,148 L71,116 L97,116 L97,84 L170,84 L170,52 L248,52 L248,20 L300,20"
        fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="40" y1="180" x2="144" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="150" y="18" font-size="12" fill="currentColor">t/&#945;</text>
  <line x1="97" y1="84" x2="97" y2="180" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="97" y="196" text-anchor="middle" font-size="12" fill="currentColor">T</text>
  <rect x="40" y="20" width="57" height="160" fill="currentColor" fill-opacity="0.12" stroke="none"/>
  <text x="180" y="70" font-size="12" fill="currentColor">reject region</text>
  <text x="46" y="35" font-size="12" fill="currentColor">F&#770;(t)</text>
</svg>
<figcaption>The step function is the empirical CDF of the p-values, $\hat F(t)=R(t)/m$; the straight
line is $t/\alpha$. BH's threshold $T$ is the last point, scanning from $t=1$ down, where the step
function is still at or above the line — every $p_i\le T$ is rejected.</figcaption>
</figure>

Only the p-values themselves matter as candidate thresholds: the crossing condition
$\hat F(t)\ge t/\alpha$ can only newly hold or fail exactly where $\hat F$ jumps, i.e. at
$t=p_{(i)}$, where it reduces to $\alpha i/m \ge p_{(i)}$, the criterion above.

## Proving FDR control

The proof below, due to Storey, Taylor and Siegmund (2002), is elegant but fragile — it needs
precise assumptions that the remarks at the end relax. Assume the $m_0=\#\{i: H_{0i}\text{ true}\}$
null p-values are independent and exactly $U[0,1]$ under $H_{0i}$.

**Setting up the process.** For a fixed threshold $t\in(0,1]$, let

$$V(t) = \#\{i\in H_{0c}: p_i\le t\}$$

be the number of *false* rejections a threshold $t$ would produce, and define $Q(t) = V(t)/(mt)$.

**$Q$ is a martingale run backward in time.** Think of $t$ decreasing from $1$ to $0$, and let
$\mathcal F_t$ record everything about which p-values lie below each level $s\ge t$ — so *smaller*
$t$ means *more* information. For a true null $i$ and $s<t$: conditional on $p_i\le t$, $p_i$ is
uniform on $[0,t]$ (having started uniform on $[0,1]$), so $\mathbb P(p_i\le s\mid p_i\le t)=s/t$;
conditional on $p_i>t$, $\mathbb P(p_i\le s\mid p_i>t)=0$ since $s<t$. Either way,

$$\mathbb E[\mathbf 1\{p_i\le s\}\mid \mathcal F_t] = \frac{s}{t}\,\mathbf 1\{p_i\le t\},$$

and summing over the true nulls gives $\mathbb E[V(s)\mid \mathcal F_t] = (s/t)\,V(t)$, i.e.

$$\mathbb E[Q(s)\mid\mathcal F_t] = Q(t), \qquad s<t:$$

exactly the martingale property, with time running from $t=1$ down to $t=0$.

**$T$ is a stopping time for this reverse filtration.** The BH threshold $T=T(X)$ is defined from
$R(s)=\#\{i:p_i\le s\}$ for all $s$ — total rejection counts, which are actually observable, unlike
$V$. Whether $T\ge t$ (whether the backward search has not yet stopped by "time" $t$) is determined
entirely by $\{R(s): s\ge t\}$, i.e. by $\mathcal F_t$ — exactly the condition a reverse-time
stopping time must satisfy.

**Combining them.** Optional stopping for the reverse martingale gives

$$\mathbb E[Q(T)] = \mathbb E[Q(1)] = \frac{V(1)}{m} = \frac{m_0}{m},$$

since every null p-value satisfies $p_i\le 1$ trivially, so $V(1)=m_0$. At the BH crossing point,
$\hat F(T) = R(T)/m = T/\alpha$ exactly (the defining property of $T$ from the empirical-Bayes
description above), so $R(T) = mT/\alpha$, and therefore

$$\mathrm{FDP} = \frac{V(T)}{R(T)} = \frac{V(T)\,\alpha}{mT} = \alpha\,Q(T).$$

Taking expectations,

$$\mathrm{FDR} = \mathbb E[\mathrm{FDP}] = \alpha\,\mathbb E[Q(T)] = \alpha\,\mathbb E[Q(1)] = \alpha\,\frac{m_0}{m} \le \alpha.$$

So BH controls FDR at level $\alpha$ — in fact at the sharper level $\alpha m_0/m$, since only the
$m_0$ true nulls can ever contribute a false discovery.

### Remarks, and how fragile the assumptions are

- The proof as given needs the null p-values to be **independent** and **exactly** uniform, not
  merely stochastically at least as large as uniform.
- A more robust version of the proof still gives FDR control when the null p-values are
  *conservative* (stochastically $\ge U(0,1)$) rather than exactly uniform.
- The result extends to certain kinds of **positive dependence** among the p-values.
- Under **arbitrary** dependence, FDR is still controlled if the BH levels are shrunk using the
  harmonic-sum correction $c_m=\sum_{i=1}^m 1/i \approx \log m + 0.577$ in place of $m$.

## Exercises

No problem set was supplied with this material.

## Sources

- All of this chapter is drawn from the course reader chapter *Multiple Testing* for Berkeley
  STAT 210A, converted to markdown as `01-multiple-testing.md` / `02-deduced-inference.md` /
  `03-fdr-control.md` (and, in the fall-2025 numbering, `01-introduction.md` /
  `02-5-deduced-inference.md` / `03-8-fdr-control.md`). The same reader text appears, essentially
  verbatim, in the copies used together here: `fall-2024/reader/multiple-testing/` (source `.qmd`,
  commit `812543b`), `fall-2025/reader/multiple-testing/` and its duplicate under
  `fall-2025/units/reader/multiple-testing/` (source `.html`, commit `5eb849a`, whose header is
  dated "Published November 30, 2023"), and `fall-2026/reader/multiple-testing/` (source `.qmd`,
  commit `7dc8f80`) — all licensed CC BY 4.0.
- No slide deck, lecture transcript, or problem set was supplied for this lecture, only the written
  reader. The reader itself twice notes "[Insert graph showing $\hat F(t)$ vs $t/\alpha$]" — once in
  the Benjamini–Hochberg-as-empirical-Bayes discussion, once in the FDR-control proof — marking a
  figure the lecture showed that is not present in the converted text. The empirical-CDF-crossing
  diagram in this chapter reconstructs what that description implies, rather than reproducing an
  image that was never captured.
- The ellipsoid-in-a-rectangle diagram illustrating conservative simultaneous intervals is this
  chapter's own rendering of the geometric relationship stated in the reader's "Deduced Inference"
  section, in its multivariate-Gaussian example and the remark immediately following it.

---

[← 67. Least Favorable Priors](67-least-favorable-priors.md) · [Contents](index.md) · [69. Old Exams Archive →](69-old-exams-archive.md)
