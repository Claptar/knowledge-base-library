---
title: "78. ARMA and ARIMA Models"
course: "Berkeley Stat 153"
chapter: 78
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 78. ARMA and ARIMA Models

## What this covers

This chapter sets up the general $\mathrm{ARMA}(p,q)$ model, the backshift-operator notation used to
manipulate it, the condition under which it has a stationary "infinite moving-average" form, how the
sample ACF and PACF are used — and where they stop being useful — to guess $p$ and $q$, how the
parameters are actually fit, and how differencing extends the model to $\mathrm{ARIMA}(p,d,q)$ for a
series that carries a trend. It assumes the reader already knows the separate $\mathrm{AR}(p)$ and
$\mathrm{MA}(q)$ models, the backshift operator $B$, and what stationarity and the autocovariance/ACF
of a time series mean.

## Combining AR and MA: the ARMA(p, q) model

A time series $y_t$ is $\mathrm{ARMA}(p,q)$ if

$$
(y_t-\mu) - \phi_1(y_{t-1}-\mu) - \cdots - \phi_p(y_{t-p}-\mu) = \varepsilon_t + \theta_1\varepsilon_{t-1} + \cdots + \theta_q\varepsilon_{t-q},
$$

where $\varepsilon_t$ is white noise. Expanding the left side and collecting the constant term gives
the equivalent form actually used for fitting,

$$
y_t - \phi_0 - \phi_1y_{t-1} - \cdots - \phi_py_{t-p} = \varepsilon_t+\theta_1\varepsilon_{t-1}+\cdots+\theta_q\varepsilon_{t-q},
\qquad \phi_0 = \mu(1-\phi_1-\cdots-\phi_p),
$$

so that once $\phi_0,\phi_1,\dots,\phi_p$ are known, the mean recovers as
$\mu = \phi_0/(1-\phi_1-\cdots-\phi_p)$. Either way, writing $y_t=\mu+\eta_t$ splits the series into
its mean and a zero-mean $\mathrm{ARMA}(p,q)$ process $\eta_t$ carrying no $\mu$ or $\phi_0$ term — the
two parametrizations describe the same model.

$\mathrm{ARMA}(p,q)$ is "$\mathrm{AR}(p)$ with $\mathrm{MA}(q)$ errors": the autoregressive part
controls how $y_t$ depends on its own past, the moving-average part controls how today's noise
depends on the recent noise history. The two familiar models sit at the boundary of this family:

1. $q=0$: $\mathrm{ARMA}(p,0)=\mathrm{AR}(p)$.
2. $p=0$: $\mathrm{ARMA}(0,q)=\mathrm{MA}(q)$.

## Backshift notation

Write $B$ for the backshift (lag) operator, $By_t=y_{t-1}$ (some authors write $L$ instead). Collect
the autoregressive and moving-average coefficients into two polynomials,

$$
\phi(z) = 1-\phi_1z-\phi_2z^2-\cdots-\phi_pz^p, \qquad \theta(z) = 1+\theta_1z+\theta_2z^2+\cdots+\theta_qz^q,
$$

so the $\mathrm{ARMA}(p,q)$ equation compresses to

$$
\phi(B)(y_t-\mu) = \theta(B)\varepsilon_t.
$$

Formally "dividing" by $\phi(B)$ gives $y_t-\mu = \dfrac{\theta(B)}{\phi(B)}\varepsilon_t$ — whether
this division is well-defined is exactly the question of the next section.

## When ARMA has a causal, stationary form

Factor the autoregressive polynomial over its roots,
$$
\phi(z) = (1-a_1z)\cdots(1-a_pz),
$$
so the roots of $\phi$ sit at $1/a_1,\dots,1/a_p$. Substituting into $\theta(B)/\phi(B)$ and applying
the geometric series $\frac{1}{1-x}=1+x+x^2+\cdots$ to each factor,

$$
\frac{\theta(B)}{\phi(B)}\varepsilon_t = \theta(B)\big[1+a_1B+(a_1B)^2+\cdots\big]\cdots\big[1+a_pB+(a_pB)^2+\cdots\big]\varepsilon_t,
$$

and each bracket is a legitimate, convergent power series only when $|a_j|<1$ — equivalently, when
the corresponding root $1/a_j$ of $\phi$ has modulus greater than $1$. This is the causal-stationary
regime: **all roots of $\phi$ lie outside the unit circle**.

<figure>
<svg viewBox="0 0 300 260" role="img" aria-label="The unit circle in the complex plane, with the roots of phi required to lie outside it">
  <line x1="20" y1="130" x2="280" y2="130" stroke="currentColor" stroke-width="1"/>
  <line x1="150" y1="10" x2="150" y2="250" stroke="currentColor" stroke-width="1"/>
  <circle cx="150" cy="130" r="60" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <text x="150" y="62" text-anchor="middle" font-size="12" fill="currentColor">|z| = 1</text>
  <circle cx="230" cy="100" r="4" fill="currentColor"/>
  <text x="238" y="97" font-size="12" fill="currentColor">1/a&#8321;</text>
  <circle cx="100" cy="190" r="4" fill="currentColor"/>
  <text x="60" y="205" font-size="12" fill="currentColor">1/a&#8322;</text>
  <text x="275" y="145" text-anchor="end" font-size="11" fill="currentColor">Re</text>
  <text x="156" y="22" font-size="11" fill="currentColor">Im</text>
</svg>
<figcaption>Roots of &#966;(z), such as 1/a&#8321; and 1/a&#8322;, must all lie outside the unit circle
&#8212; equivalently each |a&#8271;| &#60; 1 &#8212; for the geometric series 1/(1&#8722;a&#8271;B) to
converge, giving the causal, stationary MA(&#8734;) form. A root landing inside the shaded disk
breaks convergence.</figcaption>
</figure>

When it holds, everything multiplies out into a single power series in $B$,

$$
y_t - \mu = \psi_0\varepsilon_t + \psi_1\varepsilon_{t-1}+\psi_2\varepsilon_{t-2}+\cdots = \sum_{j=0}^\infty \psi_j\varepsilon_{t-j}, \qquad \sum_j|\psi_j| < \infty,
$$

i.e. every stationary, causal $\mathrm{ARMA}(p,q)$ process is an $\mathrm{MA}(\infty)$ in disguise,
with absolutely summable weights $\psi_j$. Writing $\psi(z)=\theta(z)/\phi(z)=\psi_0+\psi_1z+\psi_2z^2+\cdots$
and clearing the denominator gives $\theta(z)=\psi(z)\phi(z)$, which turns into a recursion for the
$\psi_j$ by matching powers of $z$ on both sides:

$$
1 = \psi_0, \qquad \theta_1 = \psi_1-\phi_1\psi_0, \qquad \theta_2 = \psi_2 - \phi_1\psi_1 - \phi_2\psi_0, \ \ldots
$$

(taking $\theta_j=0$ once $j>q$). Each new $\psi_j$ is solved for from the previous ones and the
$\mathrm{ARMA}$ coefficients by matching one more power of $z$ — this is the standard route from an
$\mathrm{ARMA}$ model to its $\mathrm{MA}(\infty)$ form.

## Identifying p and q: ACF and PACF

For a stationary series $\{y_t\}$ and $h\ge0$, define
$$
\mathrm{ACF}(h) = \text{correlation between } y_t \text{ and } y_{t+h},
$$
$$
\mathrm{PACF}(h) = \text{partial correlation between } y_t \text{ and } y_{t+h}\text{, after removing the effect of } y_{t+1},\dots,y_{t+h-1}.
$$

Two facts make these directly useful for reading the order of a *pure* $\mathrm{AR}$ or $\mathrm{MA}$
model off a plot:

1. $\mathrm{MA}(q)$: $\mathrm{ACF}(h)=0$ for $|h|>q$.
2. $\mathrm{AR}(p)$: $\mathrm{PACF}(h)=0$ for $|h|>p$.

Given data $y_1,\dots,y_n$, one computes the sample $\mathrm{ACF}(h)$ and sample $\mathrm{PACF}(h)$
and reads off the lag past which each is (statistically) zero to identify $q$ and $p$ respectively.
But that trick is specific to the pure cases:

4. For a genuine $\mathrm{ARMA}(p,q)$ with both $p,q>0$, **neither** the ACF nor the PACF cuts off at
   a finite lag — both tail off gradually, so the correlogram no longer pins down $p$ and $q$ by
   inspection.

The practical fix is to stop trying to read $(p,q)$ off the plot and instead search: fix upper bounds
$p\le p_{\max}$, $q\le q_{\max}$, fit $\mathrm{ARMA}(p,q)$ for every combination in that range, and let
a model-selection criterion such as AIC or BIC choose automatically among them.

## Fitting the parameters

In practice the fit is done by a routine such as `ARIMA(data, order=(p, d, q))` (e.g. in
`statsmodels`), which estimates the mean $\mu$, the moving-average coefficients
$\theta_1,\dots,\theta_q$, the autoregressive coefficients $\phi_1,\dots,\phi_p$, and the innovation
variance $\sigma^2$ — $p+q+2$ parameters in total. Estimation writes down the likelihood of the data
under the model and maximizes the log-likelihood over these parameters. Even the simplest case with a
moving-average term, $\mathrm{MA}(1)$, has no simple closed-form likelihood, so the software builds
the log-likelihood using a Kalman filter recursion.

### AIC and BIC

Having fit several candidate $(p,q)$ pairs, two standard criteria trade fit against complexity:

$$
\mathrm{AIC} = -2\times(\text{maximized log-likelihood}) + 2\times(\#\text{ parameters}),
$$
$$
\mathrm{BIC} = -2\times(\text{maximized log-likelihood}) + (\log n)\times(\#\text{ parameters}),
$$

the Akaike and Bayesian information criteria respectively. Both penalize adding parameters; BIC's
penalty grows with $\log n$ rather than staying fixed at $2$, so for large samples it punishes extra
parameters more severely than AIC does.

### From forecasts of differences back to forecasts of levels

A model is often fit not to $y_t$ itself but to a difference of it, e.g. an $\mathrm{AR}(2)$ fit to
$\log y_t - \log y_{t-1}$, $t=2,\dots,n$. Forecasting this differenced series out to
$\log y_{n+1}-\log y_n,\ \log y_{n+2}-\log y_{n+1},\ \dots,\ \log y_{n+100}-\log y_{n+99}$ only gives
forecasts of successive changes. Recovering forecasts of the level itself, relative to the last
observation, means summing them up (telescoping):

$$
\log y_{n+1}-\log y_n,\quad \log y_{n+2}-\log y_n,\quad \log y_{n+3}-\log y_n,\ \dots,\quad \log y_{n+100}-\log y_n.
$$

This "difference, model, then re-sum" pattern is exactly the mechanism that $\mathrm{ARIMA}$ makes
systematic.

## ARIMA(p, d, q): differencing away a trend

$y_t$ is $\mathrm{ARIMA}(p,d,q)$ if its $d$-th difference $(I-B)^dy_t$ is $\mathrm{ARMA}(p,q)$, i.e.

$$
\phi(B)\{(I-B)^dy_t - \mu\} = \theta(B)\varepsilon_t.
$$

Write $\nabla y_t = y_t-y_{t-1} = (I-B)y_t$ for the first difference. The second difference can be
computed two equivalent ways — directly expanding the operator,
$$
(I-B)^2y_t = (I-2B+B^2)y_t = y_t - 2y_{t-1}+y_{t-2},
$$
or by differencing twice in a row,
$$
(I-B)\big((I-B)y_t\big) = (I-B)(y_t-y_{t-1}) = (y_t-y_{t-1})-(y_{t-1}-y_{t-2}),
$$
which is the same expression.

**Worked case.** Take $y_t$ to be a GNP series. Its log, $\log y_t$, is not stationary, but the once
differenced log series $(I-B)(\log y_t)$ can be modeled as an $\mathrm{AR}(2)$. That statement is the
same as fitting $\mathrm{ARIMA}(2,1,0)$ directly to $\log y_t$ — a call such as
`arima(log(y_t), order=(2, 1, 0), trend='t')` performs the differencing and the AR fit together.

### The d = 1 case in detail

With $d=1$, the model reads $\phi(B)(\nabla y_t-\mu)=\theta(B)\varepsilon_t$, i.e.
$\nabla y_t = \mu+\eta_t$ with $\eta_t\sim\mathrm{ARMA}(p,q)$ of mean zero. Writing this out for each
$t$ and summing telescopes:
$$
y_1-y_0=\mu+\eta_1,\quad y_2-y_1=\mu+\eta_2,\ \dots,\quad y_n-y_{n-1}=\mu+\eta_n
$$
$$
\Rightarrow\quad y_t = y_0 + t\mu + (\eta_1+\cdots+\eta_t) = y_0+t\mu+\gamma_t,
$$
where $\nabla\gamma_t$ is a zero-mean $\mathrm{ARMA}(p,q)$. A nonzero drift $\mu$ in the *differenced*
series is therefore exactly a **linear-in-$t$ trend** $t\mu$ added to the *level* — this is the
`trend='t'` model. The alternative, `trend='c'`, is the default once $d\ge1$: it sets $\mu=0$, giving
$y_t = y_0+\gamma_t$ with no added linear trend.

The source material closes by naming $\mathrm{SARIMA}$ — the seasonal extension of $\mathrm{ARIMA}$ —
as the next topic, without developing it.

## Sources

- Berkeley STAT 153/248, Fall 2025, handwritten lecture notes ("Lecture 22"), a single PDF split
  into two converted files: `01-arma.md` covers the $\mathrm{ARMA}(p,q)$ definition, backshift
  notation, the causal $\mathrm{MA}(\infty)$ representation, ACF/PACF-based order identification,
  AIC/BIC, and parameter estimation; `02-arima-models.md` covers the differencing operator, the GNP
  worked example, and the $d=1$ trend derivation.
- No slides, transcript, or exercise set were supplied for this lecture; the chapter is built
  entirely from these two note files.
- Both source files carry a fidelity note worth repeating: the original PDF is a scan with no text
  layer, converted by a model reading the handwritten pages, and every equation in the source is
  marked **unverified**. It is reproduced here as given, without independent checking against the
  original scan.
- $\mathrm{SARIMA}$ (seasonal $\mathrm{ARIMA}$) is named at the end of the source material as the
  next topic but is not developed there, and so is not covered here either.

---

[← 77. Multiplicative Seasonal ARIMA Models](77-multiplicative-seasonal-arima-models.md) · [Contents](index.md) · [79. Homework Assignments Index →](79-homework-assignments-index.md)
