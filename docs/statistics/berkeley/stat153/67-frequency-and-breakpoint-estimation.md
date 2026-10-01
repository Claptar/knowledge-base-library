---
title: "67. Frequency and Breakpoint Estimation"
course: "Berkeley Stat 153"
chapter: 67
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 67. Frequency and Breakpoint Estimation

## What this covers

This chapter answers a single question: how do you fit a regression model when one of its
parameters — the frequency of a hidden oscillation, or the location of a kink in a trend — enters
*nonlinearly*, and what goes wrong when you let a trend model have as many kinks as there are data
points? It assumes you are comfortable with ordinary least squares in matrix form, the sum-of-squares
decomposition $\sum_t (y_t-\bar y)^2 = \text{(explained)} + \text{RSS}$, and — carried over from an
earlier lecture in this course — the discrete Fourier transform and the periodogram of a time series.

## Profiling: separate the nonlinear parameter from the linear ones

Two examples drive the chapter, and they share one trick. In the first, the data are believed to
contain a hidden cycle of unknown frequency $f$:
$$y_t = \beta_0 + \beta_1 \cos 2\pi f t + \beta_2 \sin 2\pi f t + \varepsilon_t, \qquad \varepsilon_t \sim N(0,\sigma^2), \qquad t = 0,\dots,n-1.$$
In the second, the data are believed to follow a trend whose slope changes at an unknown time $c$:
$$y_t = \beta_0 + \beta_1 t + \beta_2 (t-c)_+ + \varepsilon_t, \qquad (x)_+ = \max(x,0).$$
In both models, once the nonlinear parameter ($f$, or $c$) is fixed at some candidate value, what
remains is an ordinary linear regression in the $\beta$'s. That suggests a two-stage recipe, called
**profiling**: for each candidate value of the nonlinear parameter, run the linear regression and
record its residual sum of squares — this gives a *profile* $RSS(f)$ or $RSS(c)$ — and then search
over the candidate values to minimize the profile. The parameters $\beta_0,\beta_1,\beta_2,\sigma$
are **nuisance parameters**: they have to be estimated to get $RSS$, but the object of interest is
the nonlinear parameter itself.

$$RSS(f) = \min_{\beta_0,\beta_1,\beta_2} \sum_{t=0}^{n-1}\left(y_t - \beta_0 - \beta_1\cos 2\pi ft - \beta_2 \sin 2\pi ft\right)^2, \qquad \hat f = \operatorname*{argmin}_f RSS(f).$$

The same idea gives a Bayesian answer instead of just a point estimate: integrating the Gaussian
likelihood over the nuisance parameters $\beta_0,\beta_1,\beta_2,\sigma$ produces a marginal
posterior for $f$ alone,
$$\text{posterior}(f) \;\propto\; \left(\frac{1}{RSS(f)}\right)^{\frac{n-3}{2}} \, \big|X_f^TX_f\big|^{-1/2}\, I\!\left(0<f<\tfrac12\right),$$
where $X_f$ is the $n\times 3$ design matrix with columns $1$, $\cos 2\pi ft$, $\sin 2\pi ft$. The
exponent $(n-3)/2$ counts $n$ observations against the $3$ linear coefficients that were profiled
out — the same pattern reappears with two sinusoids below, with $n-5$ in place of $n-3$ once there
are $5$ linear coefficients to profile out. The factor $|X_f^TX_f|^{-1/2}$ is an Occam-type
penalty: it depends on $f$ in general, and disfavors frequencies where the design is closer to
being non-identifiable (columns close to collinear). The restriction $0 < f < \tfrac12$ is the
usual one for data sampled at unit spacing — frequencies above one-half cycle per sample are not
distinguishable from lower ones (the Nyquist frequency).

Either way — minimizing $RSS(f)$ or maximizing the posterior — a workable estimate requires a list
of candidate frequencies at which to evaluate $RSS(f)$. There are two ways to build that list:

1. **A dense grid** of points across $(0, \tfrac12)$, evaluated by brute force: refit the regression
   at each candidate $f$.
2. **The Fourier frequencies**, $f \in \{\tfrac1n, \tfrac2n, \dots\} \cap (0,\tfrac12)$ — the
   frequencies that fit a whole number of cycles into the $n$ observations. On this particular grid,
   $RSS(f)$ can be computed for *all* candidates at once, extremely cheaply, using the FFT
   algorithm. That shortcut is the subject of the next section.

## The periodogram shortcut

Run the data through the discrete Fourier transform (DFT):
$$b_j = \sum_{t=0}^{n-1} y_t \, e^{-2\pi i jt/n}, \qquad j = 0, 1, \dots, n-1,$$
computed efficiently by the FFT algorithm. Its squared modulus, rescaled, is the **periodogram**:
$$I\!\left(\frac jn\right) = \frac{|b_j|^2}{n}.$$
$I(j/n)$ measures how much of the variation in $y$ lines up with an oscillation at frequency $j/n$
— a large peak in the periodogram is evidence of a real cycle at that frequency.

The reason the Fourier grid is special is an orthogonality fact from an earlier lecture: at a
Fourier frequency $f = j/n$ (with $0 < j/n < \tfrac12$), the three regressor columns $1$,
$\cos(2\pi ft)$, $\sin(2\pi ft)$ (evaluated at $t=0,\dots,n-1$) are exactly orthogonal to each other,
and
$$X_f^TX_f = \begin{pmatrix} n & 0 & 0 \\ 0 & n/2 & 0 \\ 0 & 0 & n/2\end{pmatrix},$$
a matrix that does **not depend on which Fourier frequency $f$ is**. Orthogonality makes the
least-squares fit split into three independent univariate regressions: $\hat\beta_0 = \bar y$, and
$$\hat\beta_1 = \frac2n\sum_t y_t \cos(2\pi ft), \qquad \hat\beta_2 = \frac2n \sum_t y_t \sin(2\pi ft).$$
The sum of squares the two sinusoid terms explain (beyond the mean) is then
$$\hat\beta_1^2 \cdot \frac n2 + \hat\beta_2^2\cdot\frac n2 = \frac2n\left[\Big(\sum_t y_t\cos 2\pi ft\Big)^2 + \Big(\sum_t y_t \sin 2\pi ft\Big)^2\right] = \frac2n |b_j|^2 = 2\,I\!\left(\frac jn\right),$$
because $b_j = \sum_t y_t\cos(2\pi ft) - i\sum_t y_t \sin(2\pi ft)$ has exactly that pair of sums as
its real and imaginary parts. Subtracting the explained sum of squares from the total gives the
boxed identity from the notes:
$$RSS\!\left(\frac jn\right) = \sum_{t=0}^{n-1}(y_t-\bar y)^2 \;-\; 2\,I\!\left(\frac jn\right).$$

Two things follow immediately. First, minimizing $RSS(j/n)$ over the Fourier grid is the same as
maximizing the periodogram $I(j/n)$ over that grid — so $\hat f = \hat\jmath/n$ where $\hat\jmath$
locates the tallest peak. Second, because $X_f^TX_f$ does not depend on $f$ on this grid, its
determinant $|X_f^TX_f| = n\cdot(n/2)\cdot(n/2)$ is a constant across all Fourier frequencies, so it
drops out of the posterior comparison entirely and
$$\text{posterior}\!\left(\frac jn\right) \propto \left(\frac{1}{RSS(j/n)}\right)^{\frac{n-3}{2}} I\!\left(0 < \frac jn < \tfrac12\right).$$
This simplification is specific to the Fourier grid: at an off-grid frequency the three columns are
not orthogonal, $X_f^TX_f$ genuinely depends on $f$, and no such shortcut is available — the
regression has to be refit from scratch at every candidate. The restriction to Fourier frequencies
is used **only for computational convenience** — nothing says the true cycle in the data actually
falls on that grid.

## Two sinusoids: reading frequencies off the periodogram

The same construction extends to a model with two hidden cycles:
$$y_t = \beta_0 + \beta_{11}\cos 2\pi f_1 t + \beta_{12}\sin 2\pi f_1 t + \beta_{21}\cos 2\pi f_2 t + \beta_{22}\sin 2\pi f_2 t + \varepsilon_t.$$
Profiling out the five linear coefficients gives $RSS(f_1,f_2)$, minimized jointly over
$(\hat f_1,\hat f_2)$, with a matching posterior
$$\text{posterior}(f_1,f_2) \propto \left(\frac{1}{RSS(f_1,f_2)}\right)^{\frac{n-5}{2}} \big|X_{f_1,f_2}^TX_{f_1,f_2}\big|^{-1/2} I(0<f_1,f_2<\tfrac12)$$
— the exponent is now $(n-5)/2$, matching the five linear coefficients $\beta_0,\beta_{11},\beta_{12},\beta_{21},\beta_{22}$ profiled out.

As before, two ways to search: restrict both $f_1$ and $f_2$ to Fourier frequencies, or use a
separate (possibly denser) grid for each and refit explicitly. On the Fourier grid, if $f_1 = j_1/n$
and $f_2 = j_2/n$ are **distinct** Fourier frequencies, the four sinusoid columns are pairwise
orthogonal by the same discrete-orthogonality fact, giving
$$X_{f_1,f_2}^TX_{f_1,f_2} = \operatorname{diag}\!\left(n, \tfrac n2, \tfrac n2, \tfrac n2, \tfrac n2\right)$$
(again independent of $f_1, f_2$), and, by the identical argument as before applied to each
sinusoid pair separately,
$$RSS(f_1,f_2) = \sum_{t=0}^{n-1}(y_t-\bar y)^2 - 2\,I(f_1) - 2\,I(f_2).$$
Minimizing $RSS(f_1,f_2)$ is therefore the same as maximizing $I(f_1) + I(f_2)$ — so the best pair
of Fourier frequencies is simply the **two largest peaks of a single periodogram**. A two-dimensional
nonlinear search collapses into reading two numbers off a one-dimensional plot. In the worked
example from the notes, the periodogram's two tallest peaks sit at $j=10$ and $j=8$, giving
$$\hat f_1 = \frac{10}{n}, \qquad \hat f_2 = \frac{8}{n}.$$

## Change-of-slope models: unknown breakpoints in a trend

The profiling idea is not specific to frequencies. A trend can instead be modeled as piecewise
linear, with an unknown location where the slope changes:
$$y_t = \beta_0 + \beta_1 t + \beta_2(t-c)_+ + \varepsilon_t.$$
Before $c$, the fitted slope is $\beta_1$; from $c$ onward the extra term adds $\beta_2$ to it, so
the slope becomes $\beta_1+\beta_2$. Exactly as with $f$, the breakpoint $c$ enters nonlinearly while
the $\beta$'s enter linearly for fixed $c$, so the same recipe applies: profile out the $\beta$'s to
get $RSS(c)$, then search over candidate breakpoints for $\hat c$.

Adding a second breakpoint gives a three-segment trend:
$$y_t = \beta_0 + \beta_1 t + \beta_2(t-c_1)_+ + \beta_3(t-c_2)_+ + \varepsilon_t,$$
with slope $\beta_1$ up to $c_1$, $\beta_1+\beta_2$ between $c_1$ and $c_2$, and
$\beta_1+\beta_2+\beta_3$ after $c_2$:

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="A trend line with two breakpoints, growing steeper after each one">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="30" y1="190" x2="380" y2="190" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="385" y="194" font-size="12" fill="currentColor">t</text>

  <polyline points="30,170 150,140 260,90 370,20" fill="none" stroke="currentColor" stroke-width="2"/>

  <line x1="150" y1="190" x2="150" y2="140" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="260" y1="190" x2="260" y2="90" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>

  <text x="150" y="205" text-anchor="middle" font-size="12" fill="currentColor">c1</text>
  <text x="260" y="205" text-anchor="middle" font-size="12" fill="currentColor">c2</text>

  <text x="85" y="150" text-anchor="middle" font-size="11" fill="currentColor">slope &#946;1</text>
  <text x="200" y="105" text-anchor="middle" font-size="11" fill="currentColor">&#946;1+&#946;2</text>
  <text x="320" y="45" text-anchor="middle" font-size="11" fill="currentColor">&#946;1+&#946;2+&#946;3</text>
</svg>
<figcaption>The two-breakpoint change-of-slope model: the trend's slope steps up at each unknown knot, $c_1$ then $c_2$.</figcaption>
</figure>

This is profiled the same way, giving $RSS(c_1,c_2)$ minimized over a two-dimensional grid of
candidate knot pairs. A third breakpoint gives $RSS(c_1,c_2,c_3)$, minimized over a
three-dimensional grid — each additional knot buys one more linear segment and one more coordinate
to search over.

## When every point is a knot

Push this to its limit: put a knot at *every* interior time point,
$$y_t = \beta_0 + \beta_1 t + \beta_2(t-2)_+ + \beta_3(t-3)_+ + \cdots + \beta_{n-1}\big(t-(n-1)\big)_+ + \varepsilon_t.$$
There is no longer a search over candidate knots — every possible knot location is already a term
in the model. But the model now has as many free coefficients, $\beta_0,\dots,\beta_{n-1}$, as there
are observations $y_0,\dots,y_{n-1}$: a **high-dimensional linear regression model**. Fitting it by
ordinary least squares lets the curve bend at every single data point, so it can pass exactly
through each one:
$$RSS = 0.$$
A fit with zero residual sum of squares has not found the trend — it has reproduced the noise along
with it, which is a sign that unconstrained least squares has stopped being the right tool for this
model. Two fixes are named for this:

1. **Regularized estimation**: minimize [least squares $+$ penalty] instead of least squares alone,
   so the fit is discouraged from using all $n$ coefficients freely.
2. **A shrinkage prior on the coefficients**, in the Bayesian version of the same idea:
   $\beta_0,\dots,\beta_{n-1} \overset{iid}\sim \text{Uniform}(-C,C)$, or the "more informative"
   $\text{Uniform}(-\tau,\tau)$ for a suitably chosen $\tau$ — pulling the coefficients toward zero
   and so limiting how many of the $n$ knots the fit can actually make use of.

Both are flagged in the notes as the way forward rather than worked out — the mechanics of
regularized and Bayesian shrinkage estimation belong to material beyond this lecture.

## Sources

- Handwritten lecture notes, Berkeley Stat 153, Fall 2025, "Lecture NINE": `01-introduction.md`
  (single-sinusoid regression, the periodogram identity, Fourier frequencies) and
  `02-more-nonlinear-regression-models.md` (two-sinusoid regression, change-of-slope models, the
  high-dimensional limit and regularization). No slide deck, transcript, or problem set was supplied
  for this lecture — the chapter is built entirely from these two note files.
- These notes are themselves a model's reconstruction of handwritten pages with no text layer (per
  their own front matter: "every equation is unverified"). The derivations given here for *why* the
  boxed identities hold (the orthogonality argument for $RSS(j/n) = \text{SST} - 2I(j/n)$, and its
  extension to two frequencies) are supplied in this chapter to make the stated results plausible;
  they are not spelled out in the notes themselves, which state the identities without proof.
- The notes explicitly refer to "Lecture 7" for the fact that $X_f^TX_f$ is diagonal and
  frequency-independent at Fourier frequencies. That lecture's material was not supplied and is not
  covered here — it is used as a given fact, as the notes use it.
- Regularized and Bayesian shrinkage estimation for the high-dimensional change-of-slope model are
  named at the end of the second note file but not developed; they are not part of this chapter for
  the same reason.

---

[← 66. Frequentist and Bayesian Regression Inference](66-frequentist-and-bayesian-regression-inference.md) · [Contents](index.md) · [68. Regression with an Unknown Changepoint →](68-regression-with-an-unknown-changepoint.md)
