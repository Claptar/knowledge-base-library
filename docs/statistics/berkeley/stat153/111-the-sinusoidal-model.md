---
title: "111. The Sinusoidal Model"
course: "Berkeley Stat 153 Fall 2024"
chapter: 111
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 111. The Sinusoidal Model

## What this covers

This chapter defines a *sinusoid* as a regression function for periodic data, shows why sampling
it only at the integer times $t=1,\dots,n$ lets the frequency parameter be confined to $[0,1/2]$
without loss of generality, and covers the two ways the model's parameters — in particular the
frequency $f$ — get estimated once that reduction is made: a least-squares grid search, and a
Bayesian posterior for $f$. It assumes comfort with ordinary linear regression, the residual sum
of squares (RSS), and picks up the sinusoidal model mid-course, after it has already been
introduced and fit to data in an earlier lecture.

## The sinusoidal model

A sinusoid is the function of time

$$s(t) := \beta_0 + R\cos(2\pi f t + \phi).$$

The four constants each have a name:

- $R$, the **amplitude** — the height of the oscillation above and below its centre line $\beta_0$.
- $f$, the **frequency** — the number of oscillations per unit time. If $t$ is in seconds, $f$ is
  in Hertz.
- $1/f$, the **period** — the time to complete one full oscillation.
- $\phi$, the **phase** — with $\phi=0$ the wave is at its maximum at $t=0$; a nonzero $\phi$
  shifts it in time, capturing that two oscillations of the same frequency need not be
  "in step."
- $2\pi f$, the **angular frequency**, often written $\omega = 2\pi f$ — the rate of change of the
  angle inside the cosine.

For fitting purposes this parametrisation is awkward, because $R$ and $\phi$ enter $s(t)$
nonlinearly. The angle-addition identity $\cos(\alpha+\beta) = \cos\alpha\cos\beta -
\sin\alpha\sin\beta$ turns the sinusoid into an equivalent form that is linear in its unknown
coefficients:

$$s(t) = \beta_0 + \beta_1 \cos 2\pi f t + \beta_2 \sin 2\pi f t,$$

where $\beta_1 = R\cos\phi$ and $\beta_2 = R\sin\phi$ recover the amplitude and phase (amplitude
and phase are what you'd read off a picture of the wave; $\beta_1,\beta_2$ are what a regression
can estimate). The point of working in this second form is exactly that: once $f$ is treated as
fixed, $s(t)$ is a *linear* function of $(\beta_0,\beta_1,\beta_2)$, so ordinary least squares
applies directly to the coefficients — all the nonlinearity in the model is confined to $f$ alone.

Fitting the model to an observed series $y_1,\dots,y_n$ means adding noise,

$$y_t = \beta_0 + \beta_1\cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t, \qquad
\epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2),$$

and the quantity that ends up doing the work of inferring $f$ is $RSS(f)$, the residual sum of
squares left over after fitting $\beta_0,\beta_1,\beta_2$ by least squares *for a fixed value of*
$f$:

$$RSS(f) := \min_{\beta_0,\beta_1,\beta_2} \sum_{t=1}^n \big(y_t - \beta_0 - \beta_1\cos(2\pi f t)
- \beta_2 \sin(2\pi f t)\big)^2.$$

Everything below is about how $f$ is chosen using $RSS(f)$ — first by cutting down the range of
$f$ that needs to be searched, then by two different estimation procedures over that range.

## Discrete sampling folds every frequency into $[0,1/2]$

When the sinusoid is only ever observed at the integers $t=1,\dots,n$, frequencies outside
$[0,1/2]$ turn out to be redundant: for any $f$ whatsoever there is another frequency $f_0 \in
[0,1/2]$ whose sinusoid takes *exactly* the same values at every integer time, for a suitably
adjusted phase. This is worth stating carefully, because it is the reason the search for $f$ later
in the chapter only ever has to scan $[0,1/2]$.

**Fact.** For every $f \in (-\infty,\infty)$ and $\phi \in (-\infty,\infty)$ there exist $f_0 \in
[0,1/2]$ and $\phi_0$ such that

$$\beta_0 + R\cos(2\pi f t + \phi) = \beta_0 + R\cos(2\pi f_0 t + \phi_0) \quad \text{for all
integers } t = 1,\dots,n.$$

*Proof.* Three cases cover every $f$.

1. **$f<0$.** Cosine is even, so $\cos(2\pi f t + \phi) = \cos(-(2\pi f t + \phi)) = \cos(2\pi(-f)t
   - \phi)$, and $-f \ge 0$.
2. **$f \ge 1$.** Write $[f]$ for the integer part of $f$. Since $t$ is an integer, $2\pi[f]t$ is a
   multiple of $2\pi$, and cosine has period $2\pi$:
   $$\cos(2\pi f t + \phi) = \cos\big(2\pi[f]t + 2\pi(f-[f])t + \phi\big) = \cos\big(2\pi(f-[f])t +
   \phi\big),$$
   and $0 \le f - [f] < 1$.
3. **$f \in [1/2,1)$.** Using $\cos(2\pi t - x) = \cos x$ for integer $t$ (again periodicity),
   $$\cos(2\pi f t + \phi) = \cos\big(2\pi t - 2\pi(1-f)t + \phi\big) = \cos\big(2\pi(1-f)t -
   \phi\big),$$
   and $0 < 1-f \le 1/2$.

Case 2 (possibly followed by case 3) brings any $f$ down into $[0,1)$, and case 3 brings anything
in $[1/2,1)$ the rest of the way into $[0,1/2]$; case 1 handles negative $f$ first. In every case
the amplitude $R$ and the sample values at integer $t$ are unchanged — only the frequency and
phase are relabelled. $\blacksquare$

This is why, from here on, $f$ is always taken to range over $[0,1/2]$ when the model is fit to
data at integer times. The figure below shows the phenomenon directly: a frequency $f=1.2$,
sampled only at integers, is indistinguishable from its reduced frequency $f_0 = f - [f] = 0.2$,
even though the two curves disagree almost everywhere in between.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="A slow cosine of frequency 0.2 and a fast cosine of frequency 1.2 agreeing at every integer sample point">
  <line x1="20" y1="105" x2="320" y2="105" stroke="currentColor" stroke-width="1"/>
  <text x="325" y="109" font-size="12" fill="currentColor">t</text>
  <g stroke="currentColor" stroke-width="1">
    <line x1="30" y1="100" x2="30" y2="110"/>
    <line x1="86" y1="100" x2="86" y2="110"/>
    <line x1="142" y1="100" x2="142" y2="110"/>
    <line x1="198" y1="100" x2="198" y2="110"/>
    <line x1="254" y1="100" x2="254" y2="110"/>
    <line x1="310" y1="100" x2="310" y2="110"/>
  </g>
  <g font-size="11" fill="currentColor" text-anchor="middle">
    <text x="30" y="122">0</text>
    <text x="86" y="122">1</text>
    <text x="142" y="122">2</text>
    <text x="198" y="122">3</text>
    <text x="254" y="122">4</text>
    <text x="310" y="122">5</text>
  </g>
  <path d="M 30.00 35.43 L 32.00 35.50 L 34.00 35.71 L 36.00 36.06 L 38.00 36.55 L 40.00 37.18 L 42.00 37.94 L 44.00 38.84 L 46.00 39.87 L 48.00 41.03 L 50.00 42.32 L 52.00 43.74 L 54.00 45.28 L 56.00 46.94 L 58.00 48.72 L 60.00 50.61 L 62.00 52.61 L 64.00 54.72 L 66.00 56.93 L 68.00 59.23 L 70.00 61.63 L 72.00 64.11 L 74.00 66.68 L 76.00 69.32 L 78.00 72.04 L 80.00 74.82 L 82.00 77.66 L 84.00 80.56 L 86.00 83.50 L 88.00 86.49 L 90.00 89.52 L 92.00 92.58 L 94.00 95.66 L 96.00 98.76 L 98.00 101.88 L 100.00 105.00 L 102.00 108.12 L 104.00 111.24 L 106.00 114.34 L 108.00 117.42 L 110.00 120.48 L 112.00 123.51 L 114.00 126.50 L 116.00 129.44 L 118.00 132.34 L 120.00 135.18 L 122.00 137.96 L 124.00 140.68 L 126.00 143.32 L 128.00 145.89 L 130.00 148.37 L 132.00 150.77 L 134.00 153.07 L 136.00 155.28 L 138.00 157.39 L 140.00 159.39 L 142.00 161.28 L 144.00 163.06 L 146.00 164.72 L 148.00 166.26 L 150.00 167.68 L 152.00 168.97 L 154.00 170.13 L 156.00 171.16 L 158.00 172.06 L 160.00 172.82 L 162.00 173.45 L 164.00 173.94 L 166.00 174.29 L 168.00 174.50 L 170.00 174.57 L 172.00 174.50 L 174.00 174.29 L 176.00 173.94 L 178.00 173.45 L 180.00 172.82 L 182.00 172.06 L 184.00 171.16 L 186.00 170.13 L 188.00 168.97 L 190.00 167.68 L 192.00 166.26 L 194.00 164.72 L 196.00 163.06 L 198.00 161.28 L 200.00 159.39 L 202.00 157.39 L 204.00 155.28 L 206.00 153.07 L 208.00 150.77 L 210.00 148.37 L 212.00 145.89 L 214.00 143.32 L 216.00 140.68 L 218.00 137.96 L 220.00 135.18 L 222.00 132.34 L 224.00 129.44 L 226.00 126.50 L 228.00 123.51 L 230.00 120.48 L 232.00 117.42 L 234.00 114.34 L 236.00 111.24 L 238.00 108.12 L 240.00 105.00 L 242.00 101.88 L 244.00 98.76 L 246.00 95.66 L 248.00 92.58 L 250.00 89.52 L 252.00 86.49 L 254.00 83.50 L 256.00 80.56 L 258.00 77.66 L 260.00 74.82 L 262.00 72.04 L 264.00 69.32 L 266.00 66.68 L 268.00 64.11 L 270.00 61.63 L 272.00 59.23 L 274.00 56.93 L 276.00 54.72 L 278.00 52.61 L 280.00 50.61 L 282.00 48.72 L 284.00 46.94 L 286.00 45.28 L 288.00 43.74 L 290.00 42.32 L 292.00 41.03 L 294.00 39.87 L 296.00 38.84 L 298.00 37.94 L 300.00 37.18 L 302.00 36.55 L 304.00 36.06 L 306.00 35.71 L 308.00 35.50 L 310.00 35.43" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M 30.00 35.43 L 32.00 37.94 L 34.00 45.28 L 36.00 56.93 L 38.00 72.04 L 40.00 89.52 L 42.00 108.12 L 44.00 126.50 L 46.00 143.32 L 48.00 157.39 L 50.00 167.68 L 52.00 173.45 L 54.00 174.29 L 56.00 170.13 L 58.00 161.28 L 60.00 148.37 L 62.00 132.34 L 64.00 114.34 L 66.00 95.66 L 68.00 77.66 L 70.00 61.63 L 72.00 48.72 L 74.00 39.87 L 76.00 35.71 L 78.00 36.55 L 80.00 42.32 L 82.00 52.61 L 84.00 66.68 L 86.00 83.50 L 88.00 101.88 L 90.00 120.48 L 92.00 137.96 L 94.00 153.07 L 96.00 164.72 L 98.00 172.06 L 100.00 174.57 L 102.00 172.06 L 104.00 164.72 L 106.00 153.07 L 108.00 137.96 L 110.00 120.48 L 112.00 101.88 L 114.00 83.50 L 116.00 66.68 L 118.00 52.61 L 120.00 42.32 L 122.00 36.55 L 124.00 35.71 L 126.00 39.87 L 128.00 48.72 L 130.00 61.63 L 132.00 77.66 L 134.00 95.66 L 136.00 114.34 L 138.00 132.34 L 140.00 148.37 L 142.00 161.28 L 144.00 170.13 L 146.00 174.29 L 148.00 173.45 L 150.00 167.68 L 152.00 157.39 L 154.00 143.32 L 156.00 126.50 L 158.00 108.12 L 160.00 89.52 L 162.00 72.04 L 164.00 56.93 L 166.00 45.28 L 168.00 37.94 L 170.00 35.43 L 172.00 37.94 L 174.00 45.28 L 176.00 56.93 L 178.00 72.04 L 180.00 89.52 L 182.00 108.12 L 184.00 126.50 L 186.00 143.32 L 188.00 157.39 L 190.00 167.68 L 192.00 173.45 L 194.00 174.29 L 196.00 170.13 L 198.00 161.28 L 200.00 148.37 L 202.00 132.34 L 204.00 114.34 L 206.00 95.66 L 208.00 77.66 L 210.00 61.63 L 212.00 48.72 L 214.00 39.87 L 216.00 35.71 L 218.00 36.55 L 220.00 42.32 L 222.00 52.61 L 224.00 66.68 L 226.00 83.50 L 228.00 101.88 L 230.00 120.48 L 232.00 137.96 L 234.00 153.07 L 236.00 164.72 L 238.00 172.06 L 240.00 174.57 L 242.00 172.06 L 244.00 164.72 L 246.00 153.07 L 248.00 137.96 L 250.00 120.48 L 252.00 101.88 L 254.00 83.50 L 256.00 66.68 L 258.00 52.61 L 260.00 42.32 L 262.00 36.55 L 264.00 35.71 L 266.00 39.87 L 268.00 48.72 L 270.00 61.63 L 272.00 77.66 L 274.00 95.66 L 276.00 114.34 L 278.00 132.34 L 280.00 148.37 L 282.00 161.28 L 284.00 170.13 L 286.00 174.29 L 288.00 173.45 L 290.00 167.68 L 292.00 157.39 L 294.00 143.32 L 296.00 126.50 L 298.00 108.12 L 300.00 89.52 L 302.00 72.04 L 304.00 56.93 L 306.00 45.28 L 308.00 37.94 L 310.00 35.43" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.55"/>
  <g fill="orange" stroke="currentColor" stroke-width="0.5">
    <circle cx="30.00" cy="35.43" r="3.2"/>
    <circle cx="86.00" cy="83.50" r="3.2"/>
    <circle cx="142.00" cy="161.28" r="3.2"/>
    <circle cx="198.00" cy="161.28" r="3.2"/>
    <circle cx="254.00" cy="83.50" r="3.2"/>
    <circle cx="310.00" cy="35.43" r="3.2"/>
  </g>
</svg>
<figcaption>Solid: $\cos(2\pi \cdot 0.2\, t)$. Dashed: $\cos(2\pi \cdot 1.2\, t)$. The two curves
disagree almost everywhere, but the marked points — the only ones a sample at integer $t$ ever
sees — coincide exactly, because $1.2 - [1.2] = 0.2$.</figcaption>
</figure>

The two boundary frequencies behave in recognisably different ways. At $f=0$ the sinusoid is
simply the constant $\beta_0 + R\cos\phi$ — no oscillation at all. At $f=1/2$,

$$s(t) = \beta_0 + R\cos(\pi t + \phi) = \beta_0 + R(\cos\phi)\cos(\pi t) = \beta_0 + R(-1)^t
\cos\phi,$$

which alternates between $\beta_0 + R\cos\phi$ and $\beta_0 - R\cos\phi$ at every step — the
fastest oscillation a sample at integer times can register at all. So $[0,1/2]$ is exactly the
range from "no oscillation" to "oscillation as fast as discrete sampling can resolve," and no
frequency outside it adds anything a sample of the series could not already show.

## Least squares estimation of $\beta, f, \sigma$

With $f$ confined to $[0,1/2]$, the same strategy used earlier in the course for the change-of-slope
model applies here: since $s(t)$ is linear in $\beta$ once $f$ is fixed, sweep over candidate values
of $f$, and for each one solve an ordinary linear regression.

1. Take a grid of candidate values of $f$ in $[0,1/2]$.
2. For each grid value $f$, form the design matrix $X_f$ (columns $1$, $\cos(2\pi f t)$, $\sin(2\pi
   f t)$, evaluated at $t=1,\dots,n$), regress $y$ on $X_f$, and record the residual sum of squares
   $RSS(f)$.
3. Let $\hat f$ be the grid value minimising $RSS(f)$.
4. Take $\hat\beta$ and $\hat\sigma$ to be the usual least-squares regression estimates from
   regressing $y$ on $X_{\hat f}$.

The only new ingredient relative to an ordinary linear regression is that $f$ itself is not linear
in the model, so it cannot be estimated by the same normal equations that give $\hat\beta$ — it has
to be searched over, with $RSS(f)$ as the criterion to minimise at each candidate value.

## The Bayesian posterior for $f$

A Bayesian treatment needs priors on $\beta,\sigma,f$. As in the earlier change-of-slope model, flat
priors are put on $\beta_0,\beta_1,\beta_2$ and on $\log\sigma$:

$$\beta_0,\beta_1,\beta_2,\log\sigma \overset{\text{i.i.d.}}{\sim} \text{Unif}(-C,C),$$

and, because Fact 3.1 already justifies restricting $f$ there without loss of generality,

$$f \sim \text{Unif}[0,1/2].$$

The same calculation that produced the posterior for the breakpoint $c$ in the change-of-slope
model goes through unchanged here, with $c$ replaced by $f$ and the indicator $I\{1<c<n\}$ replaced
by $I\{0 \le f \le 1/2\}$: writing the joint posterior of $\beta,\sigma,f$ and integrating out
$\beta$ and $\sigma$ leaves a posterior for $f$ alone,

$$\text{posterior}(f) \;\propto\; I\{0 \le f \le 1/2\}\, \big|X_f^\top X_f\big|^{-1/2}
\left(\frac{1}{RSS(f)}\right)^{(n-p)/2},$$

to be evaluated numerically over a grid of $f \in [0,1/2]$, exactly as $RSS(f)$ was in the
least-squares approach. Here $p=3$ is the number of columns of $X_f$ (one each for $\beta_0,
\beta_1,\beta_2$).

One subtlety: the factor $|X_f^\top X_f|^{-1/2}$ blows up whenever $|X_f^\top X_f| = 0$, i.e.
whenever $X_f$ fails to have full column rank — and this happens exactly at the two endpoints
$f=0$ and $f=1/2$, where $\sin(2\pi f t)$ vanishes identically (at $f=0$) or the column is a
constant multiple of $\cos(\pi t)$, making the three columns of $X_f$ collinear. Those two edge
cases are therefore excluded when the posterior is actually computed:

$$\text{posterior}(f) \;\propto\; I\{0 < f < 1/2\}\, \big|X_f^\top X_f\big|^{-1/2}
\left(\frac{1}{RSS(f)}\right)^{(n-p)/2}.$$

## Sources

- Definition of the sinusoid, its four parameters, and the linear reparametrisation
  $\beta_1=R\cos\phi,\ \beta_2=R\sin\phi$: `02-2-the-sinusoid.md` (Fall 2025, Lecture Seven,
  §2 "The Sinusoid").
- The noise model $y_t = \beta_0+\beta_1\cos(2\pi ft)+\beta_2\sin(2\pi ft)+\epsilon_t$ and the
  definition of $RSS(f)$ as the minimised sum of squares over $\beta$ at fixed $f$: the "Recap
  from last lecture" section of `LectureSeven153248Spring2025.md` (Spring 2025, Lecture Seven,
  §1). This source file is truncated mid-sentence in the conversion and contains nothing beyond
  that recap; the rest of the Spring 2025 lecture is not available here.
- Fact 3.1 (restricting $f$ to $[0,1/2]$ under integer-time sampling) and its three-case proof, and
  the behaviour of $s(t)$ at $f=0$ and $f=1/2$: `03-3-discrete-sampling-and-restricting-to.md`
  (Fall 2025, Lecture Seven, §3).
- The least-squares grid-search algorithm for $\hat f, \hat\beta, \hat\sigma$: same file, §4
  ("Least Squares Estimation of $\beta,f,\sigma$"). The source calls this "exactly the same method"
  used for a change-of-slope model in an earlier lecture; that earlier lecture is referenced but
  not supplied here.
- The priors on $\beta,\sigma,f$ and the marginal posterior for $f$, including the edge-case
  exclusion at $f=0,1/2$: `04-5-bayesian-posterior.md` (Fall 2025, Lecture Seven, §5 "Bayesian
  Posterior"). This section explicitly derives the posterior for $f$ by analogy with the posterior
  for the breakpoint $c$ in the change-of-slope model, again from an earlier lecture not supplied
  here.
- Not supplied, and referenced only in passing by the source material: §1 "The Sinusoidal Model"
  (the section immediately preceding this one) and §6 "Efficient Computation of $RSS(f)$" (the
  section immediately following it).
- All four source files are machine reconstructions of PDFs with no extractable text layer; each
  carries the note that "every equation is unverified." Equations are reproduced here as given in
  those files.

---

[← 110. Introduction to Time Series Analysis](110-introduction-to-time-series-analysis.md) · [Contents](index.md) · [112. Parameter Estimation in AR(1) →](112-parameter-estimation-in-ar-1.md)
