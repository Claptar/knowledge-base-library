---
title: "9. Adaptive Rejection Sampling for Gibbs Sampling"
course: "Berkeley Stat 243 Fall 2024"
chapter: 9
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 9. Adaptive Rejection Sampling for Gibbs Sampling

## What this covers

This chapter answers a narrow but consequential question: when a Gibbs sampler needs one draw from
each of many thousands of different, awkward, one-dimensional conditional densities, and evaluating
each density is expensive, how do you sample without repeatedly re-deriving an envelope by hand or
paying for an optimisation on every single draw? It assumes familiarity with ordinary rejection
sampling — an envelope function you can sample from, an accept/reject test comparing to the target —
and with the idea of a Gibbs sampler as an algorithm that cycles through a vector of parameters,
replacing each one in turn by a draw from its full conditional distribution given the others. The
chapter follows Gilks and Wild's 1992 paper introducing **adaptive rejection sampling (ARS)**, the
device built to make that repeated sampling cheap.

## Ordinary rejection sampling, and why it is not enough here

Standard rejection sampling draws from a density $f(x)$ known only up to a constant, $g(x) = cf(x)$,
by using an envelope function $g_u(x) \geqslant g(x)$ on the domain $D$ of $f$, and optionally a
squeezing function $g_l(x) \leqslant g(x)$. To generate one point: sample $x^*$ from $g_u$, sample
$w \sim \text{uniform}(0,1)$ independently, and

- if a squeeze is available and $w \leqslant g_l(x^*)/g_u(x^*)$, accept $x^*$ without ever
  evaluating $g$;
- otherwise evaluate $g(x^*)$ and accept if $w \leqslant g(x^*)/g_u(x^*)$;
- otherwise reject and try again.

This is only worth doing if sampling from $g_u$ and evaluating it are cheap relative to $g$. The
usual difficulty is finding $g_u$ at all: in practice this means locating the supremum of $g(x)$
over $D$ by a numerical optimisation, once, before sampling can start.

That cost is tolerable when you draw many points from one fixed density. It is not tolerable inside
a Gibbs sampler, where the pattern is the opposite: **one sample from each of many thousands of
different densities.** A non-conjugate Bayesian model can also make each individual evaluation of
the target density expensive — an example later in the chapter has a full conditional built as a
product of more than 150 terms. Re-optimising to find $g_u$ before every single draw, for thousands
of draws each from a different density, is exactly the situation to avoid.

## Log-concavity: the property that removes the optimisation step

Adaptive rejection sampling handles this by assuming $f(x)$ (equivalently $g(x)$, since they differ
only by a constant) is **log-concave**: writing $h(x) = \ln g(x)$, the domain $D$ is connected,
$h$ is continuous and differentiable on $D$, and $h'(x)$ decreases monotonically as $x$ increases —
so $h$ can contain straight segments and $h'$ can jump, but it never turns upward. This one
assumption buys two things at once. First, because a concave function lies below each of its
tangent lines, a piecewise-linear upper bound built from a handful of tangents to $h$ is guaranteed
to lie above $h$ everywhere, with no search for a global maximum required. Second, the same tangents
and the chords between them give a lower bound for free, which is what lets most candidate points be
accepted or rejected without ever touching $g$ itself.

Log-concavity is common rather than exotic. Among standard families, the normal, exponential,
gamma (shape $\geqslant 1$), Weibull (shape $\geqslant 1$), logistic and Gumbel densities are
log-concave in $x$; several others become log-concave after an obvious reparametrisation (e.g. the
Pareto and $\chi^2$ in $\log x$, the beta and binomial-type discrete families in $\mathrm{logit}$
scale). More generally, if $[x \mid \mu,\sigma] = \sigma^{-1} f\!\left(\frac{x-\mu}{\sigma}\right)$
for a location $\mu$ and scale $\sigma$, and $\ln f(z)$ is concave in $z$, then $\ln[x\mid\mu,\sigma]$
is automatically concave in $x$, in $\mu$, and in the precision $\tau = 1/\sigma$ — though not
necessarily in $\sigma$ itself.

## Building the envelope: upper and lower hulls

Suppose $h(x)$ and $h'(x)$ have been evaluated at $k$ points $x_1 \leqslant \dots \leqslant x_k$ in
$D$; call this set $T_k$. Two piecewise-linear functions of $x$ are built from these evaluations.

**The upper hull** $u_k(x)$ is formed from the tangent lines to $h$ at each $x_i$. Consecutive
tangents at $x_j$ and $x_{j+1}$ cross at

$$z_j = \frac{h(x_{j+1}) - h(x_j) - x_{j+1}h'(x_{j+1}) + x_j h'(x_j)}{h'(x_j) - h'(x_{j+1})},$$

and for $x \in [z_{j-1}, z_j]$,

$$u_k(x) = h(x_j) + (x-x_j)h'(x_j),$$

using the tangent whose point of contact $x_j$ is nearest, with $z_0$ and $z_k$ the boundaries of
$D$ (possibly infinite). Exponentiating gives a **piecewise-exponential rejection envelope**
$\exp u_k(x)$, and normalising it gives the density actually sampled from,

$$s_k(x) = \exp u_k(x) \Big/ \int_D \exp u_k(x')\,dx'.$$

**The lower hull** $l_k(x)$ is formed instead from the chords joining consecutive points: for
$x \in [x_j, x_{j+1}]$,

$$l_k(x) = \frac{(x_{j+1}-x)h(x_j) + (x-x_j)h(x_{j+1})}{x_{j+1}-x_j},$$

and $l_k(x) = -\infty$ outside $[x_1, x_k]$ — the squeeze offers no protection beyond the outermost
points sampled so far. Concavity of $h$ guarantees $l_k(x) \leqslant h(x) \leqslant u_k(x)$
everywhere on $D$, which is exactly the ordering rejection sampling needs.

<figure>
<svg viewBox="0 0 400 230" role="img" aria-label="A concave log-density h(x) with a piecewise-linear upper hull from tangents and a piecewise-linear lower hull from chords, at three abscissae">
  <line x1="30" y1="200" x2="375" y2="200" stroke="currentColor" stroke-width="1.2"/>
  <text x="380" y="204" font-size="12" fill="currentColor">x</text>
  <polyline points="40,124 70,102.25 110,80.25 155,65.06 200,60 245,65.06 290,80.25 330,102.25 360,124"
            fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="200" y="45" text-anchor="middle" font-size="12" fill="currentColor">h(x)</text>
  <polyline points="40,111.75 155,60 245,60 360,111.75"
            fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="6 4"/>
  <text x="60" y="98" font-size="11" fill="currentColor">upper hull u_k(x)</text>
  <polyline points="110,80.25 200,60 290,80.25"
            fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="1.5 3"/>
  <text x="205" y="88" font-size="11" fill="currentColor">lower hull l_k(x)</text>
  <line x1="110" y1="80.25" x2="110" y2="200" stroke="currentColor" stroke-width="0.7" stroke-dasharray="2 2"/>
  <line x1="200" y1="60" x2="200" y2="200" stroke="currentColor" stroke-width="0.7" stroke-dasharray="2 2"/>
  <line x1="290" y1="80.25" x2="290" y2="200" stroke="currentColor" stroke-width="0.7" stroke-dasharray="2 2"/>
  <text x="110" y="215" text-anchor="middle" font-size="12" fill="currentColor">x1</text>
  <text x="200" y="215" text-anchor="middle" font-size="12" fill="currentColor">x2</text>
  <text x="290" y="215" text-anchor="middle" font-size="12" fill="currentColor">x3</text>
  <circle cx="110" cy="80.25" r="2.5" fill="currentColor"/>
  <circle cx="200" cy="60" r="2.5" fill="currentColor"/>
  <circle cx="290" cy="80.25" r="2.5" fill="currentColor"/>
</svg>
<figcaption>Three evaluated points on a concave log-density h(x): the dashed piecewise-linear upper
hull is built from the tangents at each point, the dotted piecewise-linear lower hull from the
chords between them. The upper hull touches h(x) exactly at the abscissae and lies above it
everywhere else; the lower hull lies below h(x) between the outermost abscissae and is undefined
past them.</figcaption>
</figure>

## The algorithm

**Initialisation.** Choose starting abscissae $T_k$. If $D$ is unbounded on the left, pick $x_1$
with $h'(x_1) > 0$; if unbounded on the right, pick $x_k$ with $h'(x_k) < 0$ — this guarantees the
tangent lines eventually turn down on both sides, so $\exp u_k(x)$ is integrable. Compute
$u_k, s_k, l_k$.

**Sampling step.** Draw $x^*$ from $s_k(x)$ and $w \sim \text{uniform}(0,1)$ independently.

- **Squeeze test**: if $w \leqslant \exp\{l_k(x^*) - u_k(x^*)\}$, accept $x^*$ — no evaluation of
  $h$ or $h'$ needed.
- Otherwise evaluate $h(x^*)$, $h'(x^*)$, and run the **rejection test**: if
  $w \leqslant \exp\{h(x^*) - u_k(x^*)\}$, accept; otherwise reject and go back to sampling.

**Updating step.** Whenever $h(x^*)$ and $h'(x^*)$ were actually computed (i.e. the point failed
the squeeze test), fold $x^*$ into $T_k$ to get $T_{k+1}$, relabel in order, and rebuild
$u_{k+1}, s_{k+1}, l_{k+1}$ from the same formulas. This is the "adaptive" part: every rejected or
borderline point makes the envelope tighter, so later draws from the same density are cheaper than
earlier ones.

## Why the accepted points are exact draws from $f$

Let $x^*_r$ be the $r$th proposed point (accepted or not) and record
$\delta_r \in \{0,1,2\}$ for squeeze-accept / rejection-test-accept / reject. Let $H_r$ be the
history up to point $r$, which determines the current hulls. Then

$$\left[(x^*_{r+1}=x)\cap(\delta_{r+1}\neq2) \mid H_r\right] = \exp h(x) \Big/ \int_D \exp u_k(x')\,dx',$$

so conditioning on acceptance,

$$\left[x^*_{r+1}=x \mid H_r \cap (\delta_{r+1}\neq2)\right] = \exp h(x) \Big/ \int_D \exp h(x')\,dx' = f(x),$$

independent of $H_r$. Every accepted point is an exact, independent draw from $f$ no matter how
much the envelope has adapted — the accept/reject step always corrects for the *current* envelope,
so there is no bias from having built it out of previously accepted data.

## Why it is cheap

Conditional on a point not being squeeze-accepted, the chance a given $x$ is proposed and needs a
fresh evaluation of $h$ is proportional to $\exp u_k(x) - \exp l_k(x)$ — the gap between the two
hulls. New evaluations are therefore concentrated exactly where the bounds disagree most, so the
envelope tightens where it is loosest rather than uniformly, which is close to the optimal way to
place a fixed number of evaluation points.

Two evaluations to start ($k=2$) are, empirically, necessary and sufficient: adding more starting
abscissae or spacing them very widely costs little in extra evaluations, and there is a broad
optimum (around $\pm 1$ for a standard normal target). For that target, drawing 100 points needs
about 15 evaluations of $h$ and $h'$ in total, and 1000 points about 30 — the number of evaluations
needed grows roughly as $n^{1/3}$, not linearly in the number of points drawn, because the envelope
built for earlier draws is reused for later ones.

## Using it inside a Gibbs sampler

A Gibbs sampler updates a hierarchical model built from **submodels**: each parameter $\beta_m$ has
a *model conditional* $[\beta_m \mid \{\beta_i : i \in S_m\}]$ given the parameters it directly
depends on. The *full conditional* needed for a Gibbs update — $\beta_m$ given every other
parameter — combines the model conditional for $\beta_m$ with the model conditional of every other
submodel that itself depends on $\beta_m$:

$$[\beta_m \mid\ ] \propto [\beta_m \mid \{\beta_i:i\in S_m\}] \prod_{\{j:\,m\in S_j\}} [\beta_j\mid\{\beta_i:i\in S_j\}].$$

Unless every factor is conjugate to every other, this product has no closed form and no standard
name — and it can have very many factors (the example below has over 150; the paper notes
applications with several thousand). Taking logs,

$$h(\beta_m) = \ln[\beta_m\mid\{\beta_i:i\in S_m\}] + \sum_{\{j:m\in S_j\}} \ln[\beta_j\mid\{\beta_i:i\in S_j\}],$$

and if every term on the right is log-concave in $\beta_m$ — true whenever every model conditional
in the hierarchy is drawn from a log-concave family, per the previous section — then $h(\beta_m)$
is concave as a sum of concave functions, and adaptive rejection sampling applies directly. Only
each *model conditional's* log-concavity in $\beta_m$ is needed, not that of the full conditional
in isolation, and a factor $[\beta_j \mid \cdot]$ can even be a discrete distribution of $\beta_j$
as long as it is log-concave in $\beta_m$.

**Multivariate parameters.** ARS as described only samples a scalar. If $\beta_m$ is a vector, the
fix is componentwise: for each element $\beta_{mk}$, the univariate conditional
$[\beta_{mk}\mid\ ]$ is proportional (as a function of $\beta_{mk}$ alone) to the multivariate full
conditional $[\beta_m\mid\ ]$, so if the latter is log-concave in $\beta_m$ then the former is
log-concave in $\beta_{mk}$, and the Gibbs sampler updates each component of $\beta_m$ in turn by
ARS with $h(\beta_{mk}) = \ln[\beta_m\mid\ ]$.

## Worked example: monoclonal antibody reactivity

The paper's motivating application: 13 monoclonal antibodies were tested against 15 human cell
types for reactivity with the neural cell adhesion molecule (NCAM), reported as a percentage
$y_{ijr}$ (antibody $i$, cell type $j$, replicate $r$), rounded to the nearest integer. Because many
recorded values sit exactly at $0$ or $100$ — and the rounding matters, not just as a nuisance — the
model does not use $\mathrm{logit}(y_{ijr}/100)$ directly; instead $y_{ijr}$ is treated as an
interval observation of an underlying logistic variable with location $\mu_{ij}$ and scale
$\tau_y$:

$$[y_{ijr}\mid\mu_{ij},\tau_y] = \frac{1}{1+\exp\{-\tau_y(b_{ijr}-\mu_{ij})\}} - \frac{1}{1+\exp\{-\tau_y(a_{ijr}-\mu_{ij})\}},$$

where $a_{ijr}, b_{ijr}$ are the logit-transformed rounding bounds around $y_{ijr}$ (with
$a_{ijr}=-\infty$ when $y_{ijr}=0$ and $b_{ijr}=+\infty$ when $y_{ijr}=100$). The location is
decomposed as

$$\mu_{ij} = \beta_0 + \beta_{1j} + \beta_{2i}:$$

a baseline pattern of reactivity across cell types ($\beta_0+\beta_{1j}$), adjusted for each
antibody's individual affinity ($\beta_{2i}$). Priors are $\beta_0 \sim N(\alpha_0,\tau_0^{-1})$,
$\beta_{1j}\sim N(0,\tau_1^{-1})$, $\beta_{2i}\sim N(0,\tau_2^{-1})$, $\tau_y\sim G(\rho_y,\lambda_y)$,
with fixed, fairly flat hyperparameters for $\beta_0$ and $\tau_y$, and further gamma hyperpriors
$\tau_k \sim G(\rho_k,\lambda_k)$, $k=1,2$, left free — since **how much variability there is in
$\tau_1$ (across cell types) versus $\tau_2$ (across antibodies) is the question the analysis is
for.**

Each factor in the full conditional for $\beta_0$ (a normal prior term times a product over every
data point of the interval-logistic likelihood above) is log-concave in $\beta_0$, and so are the
corresponding conditionals for $\beta_{1j}$, $\beta_{2i}$, and $\tau_y$: none of them simplifies to
a standard form, and the product can run over more than 150 terms, but ARS handles them all as one
routine. The full conditionals for the hyperparameters $\tau_1,\tau_2$, by contrast, are conjugate
gammas, e.g. $[\tau_1\mid\ ] \sim G\!\left(\rho_1+\tfrac12 J,\ \lambda_1+\tfrac12\sum_j\beta_{1j}^2\right)$,
and need no rejection sampling at all — a reminder that ARS is reached for exactly where conjugacy
fails, not used as a universal replacement for it.

Running 1000 Gibbs iterations, and reusing the 15th and 85th centiles of the previous iteration's
sampling density $s_k(x)$ as the two starting abscissae for the next, each ARS draw needed on
average only three evaluations of $h$ (two of them the starting ones), and more than four only 5%
of the time. The chain converged within about 10 iterations; posterior summaries from iterations
11–1100 showed substantial variability in $\tau_1^{-1}$ (reactivity differs a lot across cell
types) but comparatively little in $\tau_2^{-1}$ (antibodies to the same antigen behave similarly),
with one exception — antibody 12's 90% interval for $\beta_{2,12}$ excluded 0, suggesting unusually
low NCAM affinity.

## Practical notes

Conceptually ARS is simple, but the paper flags that a naive implementation can misbehave
numerically on densities that are extremely peaked or skewed — care is needed in how the hulls are
computed and integrated. It also works unmodified on **truncated** distributions, since truncation
is just a restriction of $D$ and does not disturb log-concavity.

## Sources

All material in this chapter is drawn from the Berkeley STAT 243 (Fall 2024) project reading,
Gilks, W. R. and Wild, P. (1992), *Adaptive Rejection Sampling for Gibbs Sampling*, *J. R. Statist.
Soc.* B, **41**, 337–348, as converted to markdown in this library:

- Summary and framing — `01-adaptive-rejection-sampling-for-gibbs-sampling.md`.
- Motivation, relation to Devroye (1986), and the role of Gibbs sampling —
  `02-1-introduction.md`.
- Non-adaptive rejection sampling, the hull construction, the algorithm, the exactness proof, and
  the efficiency discussion (including Table 1) — `03-2-adaptive-rejection-sampling.md`.
- Gibbs sampling, the model-conditional decomposition, log-concavity of standard families
  (Table 2), and the multivariate extension — `04-3-adaptive-rejection-sampling-and-gibbs-sampling.md`.
- The monoclonal antibody model, priors, full conditionals, and results (Table 3) —
  `05-4-application-to-monoclonal-antibody-reactivity.md`.
- Conclusions and implementation caveats — `06-5-conclusions.md`.
- Full reference list, not reproduced here — `07-references.md`.

No slide deck, lecture transcript, or exercise set was supplied for this item; the source is the
paper itself, distributed as a course reading. The markdown files are machine reconstructions of a
PDF with no extractable text layer (`fidelity: reconstructed`, CC BY 4.0) — the prose is a
paraphrase in places and every displayed equation is unverified against the original typesetting,
so anyone checking a derivation to the letter should confirm it against the original paper. The
paper's own Figure 1 (a concave log-density with upper and lower hulls) is described in the source
but not reproduced as an image; the diagram in this chapter is redrawn from that description, not
copied from the original figure. Devroye, L. (1986), *Non-uniform Random Variate Generation*, is
discussed as related but non-adaptive prior work and was not itself supplied as a source.

---

[← 8. Infovis vs. Statistical Graphics](08-infovis-vs-statistical-graphics.md) · [Contents](index.md) · [10. Installing Git →](10-installing-git.md)
