---
title: "69. Autoregression and Yule's AR(2)"
course: "Berkeley Stat 153 Fall 2024"
chapter: 69
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 69. Autoregression and Yule's AR(2)

## What this covers

Every regression model built so far in the course — trend regression, broken-stick regression,
harmonic (sinusoidal) regression — predicts $y_t$ from functions of the *time index* $t$: the design
matrix $X$ is made of columns like $t$, $(t-c)_+$, $\cos 2\pi ft$. This chapter introduces
**autoregression (AR)**, where $X$ is instead made of the series' own **past values**: $y_{t-1}$,
$y_{t-2}$, and so on. It defines $AR(1)$, $AR(2)$ and the general $AR(p)$ model, shows that fitting
one is *still* ordinary least squares once the design matrix is relabelled, and works out how to
forecast several steps ahead by feeding earlier forecasts back in as if they were data. It then asks
where this idea came from: Udny Yule's 1927 attempt to model the 11-year sunspot cycle, which is
worked through in enough detail to see why a recursive model succeeds where a fixed sinusoid does
not. Assumes: linear regression by least squares and by maximum likelihood, and harmonic
(sinusoidal) regression $y_t = \beta_0+\beta_1\cos2\pi ft+\beta_2\sin2\pi ft+\varepsilon_t$.

## From regression on time to regression on the past

The family $ARIMA$ — **A**uto**R**egressive **I**ntegrated **M**oving **A**verage — names the three
ingredients this part of the course assembles: $AR$, $MA$ (moving average) and $I$ (integration,
i.e. differencing). This chapter is about the first one.

Every model considered up to now has the generic linear-regression shape
$$y = X\beta + \varepsilon,$$
for example a broken-stick trend $y_t = \beta_0+\beta_1 t+\beta_2(t-c)_++\varepsilon_t$, with
$$y = \begin{pmatrix} y_1\\ \vdots\\ y_n\end{pmatrix}, \qquad
X = \begin{bmatrix} 1 & t_1 & (t_1-c)_+ \\ \vdots & \vdots & \vdots \\ 1 & t_n & (t_n-c)_+\end{bmatrix}.$$
In every one of these, $X$ is built out of the time index $t$ (or functions of it, such as a
frequency). **Autoregression keeps exactly the same equation $y=X\beta+\varepsilon$ and only changes
what goes into $X$: its columns are the series' own past values**, $y_{t-1}, y_{t-2},\dots$, rather
than functions of $t$. That single change is the whole idea, and it is also why fitting an AR model
needs no new machinery: it is ordinary least squares on a differently-built $X$.

## The $AR(p)$ model

**$AR(1)$.** The simplest case regresses $y_t$ on the single preceding value:
$$y_t = \phi_0 + \phi_1 y_{t-1} + \varepsilon_t, \qquad \varepsilon_t \overset{\text{iid}}{\sim} N(0,\sigma^2), \qquad t=2,3,\dots,n.$$
The "$1$" is the **order**: the number of lags used. Writing it as $y=X\beta+\varepsilon$,
$$y = \begin{pmatrix} y_2\\ \vdots\\ y_n\end{pmatrix}, \qquad
X = \begin{bmatrix} 1 & y_1 \\ \vdots & \vdots \\ 1 & y_{n-1}\end{bmatrix}, \qquad
\beta = \begin{pmatrix} \phi_0\\ \phi_1\end{pmatrix}.$$
Notice the fitting sample starts at $t=2$: there is no $y_0$ to serve as a regressor for $y_1$, so
the first observation is used only as a predictor, never as a response.

**$AR(2)$** adds a second lag,
$$y_t = \phi_0+\phi_1y_{t-1}+\phi_2y_{t-2}+\varepsilon_t, \qquad t=3,4,\dots,n,$$
$$y=\begin{pmatrix} y_3\\ \vdots\\ y_n\end{pmatrix}, \qquad
X=\begin{bmatrix} 1 & y_2 & y_1\\ \vdots & \vdots & \vdots\\ 1 & y_{n-1} & y_{n-2}\end{bmatrix},$$
and now the sample loses its first *two* observations to the role of predictors.

**General $AR(p)$**:
$$y_t = \phi_0+\phi_1y_{t-1}+\dots+\phi_py_{t-p}+\varepsilon_t, \qquad t=p+1,\dots,n,$$
$$y=\begin{pmatrix} y_{p+1}\\ \vdots\\ y_n\end{pmatrix}, \qquad
X=\begin{bmatrix} 1 & y_p & y_{p-1} & \dots & y_1\\ \vdots & \vdots & \vdots & & \vdots\\ 1 & y_{n-1} & y_{n-2} & \dots & y_{n-p}\end{bmatrix}.$$
Each row of $X$ holds the $p$ values immediately preceding the response in that row, oldest last;
the price of using $p$ lags is always the first $p$ observations, which appear only inside $X$ and
never as a $y$.

## Fitting: still least squares

The unknown parameters are $\phi_0,\phi_1,\dots,\phi_p$ and $\sigma$. Because $y=X\beta+\varepsilon$
is again an ordinary linear model with iid Gaussian errors, the same equivalence used for trend and
harmonic regression applies unchanged: maximizing the Gaussian likelihood over $\phi_0,\dots,\phi_p$
is the same problem as minimizing the residual sum of squares,
$$\min_{\phi_0,\dots,\phi_p} \sum_{t=p+1}^n \big(y_t-\phi_0-\phi_1y_{t-1}-\dots-\phi_py_{t-p}\big)^2,$$
so `sm.OLS(y, X).fit()` on the $y,X$ built above gives $\hat\phi_0,\dots,\hat\phi_p$ directly — no
new estimation method is needed, only a new design matrix. The MLE for the noise scale is the usual
plug-in formula,
$$\hat\sigma_{\text{MLE}} = \sqrt{\frac{1}{n-p}\sum_{t=p+1}^n\big(y_t-\hat\phi_0-\hat\phi_1y_{t-1}-\dots-\hat\phi_py_{t-p}\big)^2}.$$

## Forecasting: feed the predictions back in

Forecasting $y_{n+1},\dots,y_{n+k}$ from a fitted $AR(p)$ runs into a problem one step ahead: the
first forecast,
$$\hat y_{n+1} = \hat\phi_0+\hat\phi_1y_n+\hat\phi_2y_{n-1}+\dots+\hat\phi_py_{n+1-p},$$
only needs *observed* data, since every lag it calls on is at or before time $n$. The second,
$$\hat y_{n+2} = \hat\phi_0+\hat\phi_1\hat y_{n+1}+\hat\phi_2y_n+\dots+\hat\phi_py_{n+2-p},$$
already needs $\hat y_{n+1}$, which does not exist yet as data — so the model's own first forecast is
substituted in its place. Continuing this way, forecasting $i$ steps ahead uses
$$\boxed{\hat y_{n+i} = \hat\phi_0+\hat\phi_1\hat y_{n+i-1}+\dots+\hat\phi_p\hat y_{n+i-p}}, \qquad
\boxed{\hat y_j = y_j \text{ if } j\le n}, \qquad i=1,2,\dots$$
i.e. wherever a lag falls on or before time $n$, use the real observation; wherever it falls after
$n$, use the forecast already computed for it. This "plug the forecast back in as if it were data"
recursion is the only way to reach beyond one step ahead, since an $AR(p)$ model only ever knows how
to predict the very next value.

## Where $AR(2)$ came from: Yule and the sunspot cycle (1927)

The autoregressive idea was not introduced as an abstract generalization of regression — it was
invented to solve a specific problem. Udny Yule was trying to model the number of sunspots $y_t$
observed per year, which rises and falls in a cycle roughly $11$ years long but not on a fixed
schedule: the peaks are not evenly spaced and not of even height.

**The first attempt** was the harmonic regression already familiar from earlier in the course:
$$\text{Model ①:} \qquad y_t = \underbrace{\beta_0+\beta_1\cos2\pi ft+\beta_2\sin2\pi ft}_{s(t)} + \varepsilon_t, \qquad \varepsilon_t\overset{\text{iid}}{\sim}N(0,\sigma^2),$$
with unknowns $f,\beta_0,\beta_1,\beta_2,\sigma$ — the frequency $f$ would come out near $1/11$ per
year. This treats the sunspot count as a perfectly regular signal $s(t)$ plus independent noise on
top of it.

**Turning the signal into a recursion.** The signal $s(t)$ satisfies a second-order differential
equation: differentiating twice,
$$s''(t) = -(2\pi f)^2\big[\beta_1\cos2\pi ft+\beta_2\sin2\pi ft\big] = -(2\pi f)^2\big(s(t)-\beta_0\big),$$
using $s(t)-\beta_0=\beta_1\cos2\pi ft+\beta_2\sin2\pi ft$. This is the equation of a simple harmonic
oscillator: the "acceleration" of $s$ is always pulling it back toward $\beta_0$, proportional to its
current displacement.

The discrete analogue of this — replacing the second derivative by a second difference — turns out
to hold *exactly*, not just approximately, for any sinusoid at frequency $f$:
$$\big(s_t-s_{t-1}\big)-\big(s_{t-1}-s_{t-2}\big) = 2\big[\cos2\pi f-1\big]\big(s_{t-1}-\beta_0\big) \iff s_t = \beta_0+\beta_1\cos2\pi ft+\beta_2\sin2\pi ft.$$
Adding the observation noise back in (a sinusoid observed with error induces noise $\eta_t$ in this
recursion too) gives
$$\big(y_t-y_{t-1}\big)-\big(y_{t-1}-y_{t-2}\big) = 2\big(\cos2\pi f-1\big)\big(y_{t-1}-\beta_0\big)+\eta_t,$$
which rearranges into
$$y_t = \phi_0+\phi_1y_{t-1}-y_{t-2}+\eta_t.$$
This is **a special case of $AR(2)$** — special because the coefficient on $y_{t-2}$ is forced to be
exactly $-1$ by the sinusoid identity it came from. Letting that coefficient be a free parameter
$\phi_2$ instead of fixing it at $-1$ gives the general model
$$\text{Model ②:} \qquad y_t = \phi_0+\phi_1y_{t-1}+\phi_2y_{t-2}+\varepsilon_t,$$
which is the $AR(2)$ model proper.

**Why the recursion, and not just the sinusoid.** Models ① and ② look like alternative routes to the
same curve, but they describe very different kinds of irregularity, and a physical analogy makes the
difference concrete. Picture a mass on a spring, obeying Hooke's law
$$s''(t) = -\tfrac{k}{m}\big(s(t)-\beta_0\big),$$
a clean oscillation around the rest position $\beta_0$ with a fixed period set by the spring constant
$k$ and the mass $m$. Now introduce randomness by throwing stones at it, in one of two ways:

- **Scenario 1** (matching Model ①): the spring swings exactly as the equation says, and the
  randomness is *measurement* noise added afterward, $y_t = s(t)+\varepsilon_t$. Removing the noise
  would reveal a perfectly regular, unchanging oscillation.
- **Scenario 2** (matching Model ②, in continuous time): the stones hit the object itself, so the
  noise enters the equation of motion, $y''(t) = -k\big(y(t)-\beta_0\big)+\eta_t$. Now $y(t)$ is
  smooth — it still solves a differential equation, so it cannot jump — but every impact nudges its
  future trajectory, so its amplitude and effective period keep drifting rather than repeating
  exactly.

Sunspot activity looks like Scenario 2, not Scenario 1: the 11-year cycle wanders in height and
timing rather than repeating a fixed waveform. That is the reason Yule reached for the recursive
model rather than stopping at the harmonic regression he started with.

<figure>
<svg viewBox="0 0 320 210" role="img" aria-label="A regular sinusoid with scattered measurement noise compared with an AR(2) path whose cycle length and amplitude wander">
  <text x="160" y="12" text-anchor="middle" font-size="12" fill="currentColor">Model &#9312;: fixed sinusoid + independent noise on each point</text>
  <polyline points="20.0,45.0 21.4,43.9 22.8,42.7 24.2,41.6 25.6,40.5 27.0,39.4 28.4,38.3 29.8,37.3 31.3,36.3 32.7,35.3 34.1,34.4 35.5,33.5 36.9,32.6 38.3,31.8 39.7,31.1 41.1,30.4 42.5,29.8 43.9,29.2 45.3,28.7 46.7,28.2 48.1,27.8 49.5,27.5 51.0,27.3 52.4,27.1 53.8,27.0 55.2,27.0 56.6,27.0 58.0,27.2 59.4,27.3 60.8,27.6 62.2,27.9 63.6,28.3 65.0,28.8 66.4,29.3 67.8,29.9 69.2,30.6 70.7,31.3 72.1,32.0 73.5,32.8 74.9,33.7 76.3,34.6 77.7,35.6 79.1,36.5 80.5,37.6 81.9,38.6 83.3,39.7 84.7,40.8 86.1,41.9 87.5,43.0 88.9,44.1 90.4,45.3 91.8,46.4 93.2,47.5 94.6,48.7 96.0,49.8 97.4,50.9 98.8,51.9 100.2,53.0 101.6,54.0 103.0,54.9 104.4,55.9 105.8,56.7 107.2,57.6 108.6,58.4 110.1,59.1 111.5,59.8 112.9,60.4 114.3,61.0 115.7,61.4 117.1,61.9 118.5,62.2 119.9,62.5 121.3,62.8 122.7,62.9 124.1,63.0 125.5,63.0 126.9,62.9 128.3,62.8 129.7,62.6 131.2,62.3 132.6,62.0 134.0,61.6 135.4,61.1 136.8,60.5 138.2,59.9 139.6,59.3 141.0,58.6 142.4,57.8 143.8,57.0 145.2,56.1 146.6,55.2 148.0,54.2 149.4,53.2 150.9,52.2 152.3,51.1 153.7,50.0 155.1,48.9 156.5,47.8 157.9,46.7 159.3,45.6 160.7,44.4 162.1,43.3 163.5,42.2 164.9,41.1 166.3,40.0 167.7,38.9 169.1,37.8 170.6,36.8 172.0,35.8 173.4,34.8 174.8,33.9 176.2,33.0 177.6,32.2 179.0,31.4 180.4,30.7 181.8,30.1 183.2,29.5 184.6,28.9 186.0,28.4 187.4,28.0 188.8,27.7 190.3,27.4 191.7,27.2 193.1,27.1 194.5,27.0 195.9,27.0 197.3,27.1 198.7,27.2 200.1,27.5 201.5,27.8 202.9,28.1 204.3,28.6 205.7,29.0 207.1,29.6 208.5,30.2 209.9,30.9 211.4,31.6 212.8,32.4 214.2,33.3 215.6,34.1 217.0,35.1 218.4,36.0 219.8,37.0 221.2,38.1 222.6,39.1 224.0,40.2 225.4,41.3 226.8,42.5 228.2,43.6 229.6,44.7 231.1,45.9 232.5,47.0 233.9,48.1 235.3,49.2 236.7,50.3 238.1,51.4 239.5,52.4 240.9,53.5 242.3,54.4 243.7,55.4 245.1,56.3 246.5,57.2 247.9,58.0 249.3,58.7 250.8,59.4 252.2,60.1 253.6,60.7 255.0,61.2 256.4,61.7 257.8,62.1 259.2,62.4 260.6,62.7 262.0,62.8 263.4,63.0 264.8,63.0 266.2,63.0 267.6,62.9 269.0,62.7 270.5,62.5 271.9,62.2 273.3,61.8 274.7,61.3 276.1,60.8 277.5,60.2 278.9,59.6 280.3,58.9 281.7,58.2 283.1,57.4 284.5,56.5 285.9,55.6 287.3,54.7 288.7,53.7 290.2,52.7 291.6,51.7 293.0,50.6 294.4,49.5 295.8,48.4 297.2,47.3 298.6,46.1 300.0,45.0" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="27.0" cy="40.0" r="2" fill="currentColor"/>
  <circle cx="48.1" cy="35.3" r="2" fill="currentColor"/>
  <circle cx="67.8" cy="24.3" r="2" fill="currentColor"/>
  <circle cx="88.9" cy="50.1" r="2" fill="currentColor"/>
  <circle cx="108.6" cy="56.8" r="2" fill="currentColor"/>
  <circle cx="129.7" cy="61.0" r="2" fill="currentColor"/>
  <circle cx="150.9" cy="63.6" r="2" fill="currentColor"/>
  <circle cx="170.6" cy="37.7" r="2" fill="currentColor"/>
  <circle cx="191.7" cy="26.9" r="2" fill="currentColor"/>
  <circle cx="212.8" cy="36.8" r="2" fill="currentColor"/>
  <circle cx="232.5" cy="53.7" r="2" fill="currentColor"/>
  <circle cx="253.6" cy="60.5" r="2" fill="currentColor"/>
  <circle cx="273.3" cy="65.3" r="2" fill="currentColor"/>
  <circle cx="294.4" cy="43.7" r="2" fill="currentColor"/>
  <line x1="20" y1="75" x2="300" y2="75" stroke="currentColor" stroke-width="1" stroke-opacity="0.4"/>
  <text x="160" y="123" text-anchor="middle" font-size="12" fill="currentColor">Model &#9313;: noise perturbs the dynamics (Yule's AR(2))</text>
  <polyline points="20.0,148.9 21.4,148.0 22.8,148.4 24.2,149.0 25.6,150.8 27.0,151.1 28.4,153.7 29.8,157.0 31.3,157.2 32.7,156.8 34.1,157.8 35.5,156.0 36.9,151.3 38.3,149.2 39.7,151.5 41.1,154.7 42.5,157.7 43.9,160.2 45.3,158.3 46.7,157.8 48.1,154.2 49.5,153.9 51.0,155.5 52.4,155.4 53.8,153.0 55.2,149.8 56.6,147.6 58.0,147.4 59.4,148.7 60.8,150.3 62.2,153.2 63.6,155.5 65.0,156.2 66.4,156.5 67.8,154.9 69.2,152.4 70.7,146.9 72.1,143.6 73.5,144.5 74.9,148.7 76.3,153.8 77.7,156.6 79.1,159.3 80.5,159.7 81.9,155.2 83.3,156.5 84.7,159.4 86.1,160.3 87.5,159.0 88.9,156.3 90.4,154.6 91.8,152.0 93.2,149.9 94.6,150.5 96.0,147.2 97.4,145.7 98.8,147.8 100.2,151.6 101.6,156.2 103.0,159.8 104.4,167.2 105.8,171.4 107.2,168.8 108.6,165.5 110.1,160.2 111.5,152.5 112.9,144.9 114.3,137.9 115.7,139.7 117.1,145.7 118.5,153.9 119.9,159.8 121.3,161.5 122.7,166.6 124.1,165.9 125.5,165.5 126.9,161.1 128.3,158.9 129.7,155.6 131.2,150.3 132.6,147.3 134.0,146.3 135.4,146.0 136.8,147.7 138.2,151.2 139.6,152.0 141.0,151.4 142.4,152.4 143.8,148.4 145.2,148.9 146.6,149.1 148.0,151.2 149.4,153.7 150.9,154.8 152.3,155.3 153.7,154.4 155.1,156.8 156.5,161.4 157.9,162.5 159.3,163.5 160.7,164.2 162.1,165.5 163.5,161.4 164.9,154.9 166.3,146.4 167.7,143.2 169.1,143.4 170.6,148.8 172.0,153.4 173.4,154.5 174.8,157.4 176.2,156.1 177.6,152.8 179.0,150.8 180.4,154.2 181.8,154.4 183.2,155.0 184.6,156.6 186.0,156.8 187.4,155.7 188.8,151.6 190.3,151.0 191.7,149.2 193.1,146.2 194.5,142.9 195.9,143.5 197.3,148.4 198.7,152.1 200.1,155.8 201.5,158.5 202.9,157.1 204.3,155.9 205.7,159.2 207.1,161.8 208.5,165.9 209.9,165.1 211.4,161.3 212.8,157.6 214.2,153.9 215.6,149.4 217.0,146.7 218.4,143.9 219.8,144.4 221.2,145.4 222.6,145.7 224.0,145.0 225.4,148.3 226.8,151.0 228.2,158.0 229.6,165.4 231.1,173.0 232.5,172.8 233.9,170.7 235.3,164.9 236.7,158.0 238.1,151.4 239.5,147.8 240.9,146.2 242.3,143.4 243.7,143.8 245.1,145.9 246.5,148.0 247.9,151.9 249.3,158.5 250.8,164.3 252.2,164.8 253.6,166.1 255.0,165.5 256.4,160.5 257.8,153.2 259.2,147.4 260.6,142.8 262.0,141.6 263.4,146.3 264.8,155.6 266.2,164.6 267.6,168.0 269.0,168.8 270.5,167.8 271.9,165.3 273.3,163.7 274.7,160.3 276.1,158.5 277.5,155.4 278.9,157.3 280.3,157.7 281.7,158.7 283.1,162.4 284.5,162.3 285.9,161.0 287.3,162.7 288.7,164.1 290.2,162.4 291.6,160.0 293.0,155.1 294.4,149.5 295.8,144.8 297.2,142.7 298.6,141.3 300.0,142.2" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="20" y1="188" x2="300" y2="188" stroke="currentColor" stroke-width="1" stroke-opacity="0.4"/>
  <text x="160" y="203" text-anchor="middle" font-size="12" fill="currentColor">time &#8594;</text>
</svg>
<figcaption>Left to right in each panel is time. Model &#9312; measures a perfectly regular sinusoid with
independent noise on each observation, so the underlying cycle never changes. Model &#9313; is an
AR(2) recursion in which fresh noise enters the recursion itself every step, so it stays smooth but
its cycle length and amplitude drift &#8212; the behaviour Yule needed to match the sunspot record.</figcaption>
</figure>

**The Yule model**, as originally written, keeps the link to the frequency $f$ that motivated it:
$$y_t = \phi_0+\phi_1y_{t-1}-y_{t-2}+\varepsilon_t, \qquad \phi_1 = 2\cos2\pi f,$$
or, moving the lag-2 term to the left,
$$y_t+y_{t-2} = \phi_0+\phi_1y_{t-1}+\varepsilon_t.$$
The fitted coefficient $\phi_1$ can be read back as an implied cycle frequency $f=\tfrac{1}{2\pi}\arccos(\phi_1/2)$ — the trace of the sinusoid the recursion grew out of, even though the general
$AR(2)$ no longer requires the coefficient on $y_{t-2}$ to be exactly $-1$.

## Sources

- Handwritten lecture notes (fall 2025), reconstructed by a model from a PDF with no text layer —
  every equation there is flagged unverified in the source and has been cross-checked here where
  possible (the sinusoid difference-equation identity in the history section was independently
  verified against the trigonometric sum formula):
  [`01-lagged-regression.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureSixteen153248Fall2025.pdf)
  (the "From regression on time to regression on the past" and "$AR(1)$/$AR(2)$" sections),
  [`02-ar.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureSixteen153248Fall2025.pdf)
  (general $AR(p)$, estimation, and the forecasting recursion), and
  [`03-history-how-ar-models-were-invented.md`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureSixteen153248Fall2025.pdf)
  (Yule 1927 and the spring analogy) — all from `berkeley-stat153/fall-2025`,
  `HandwrittenNotesLectureSixteen153248Fall2025.pdf`, CC BY 4.0.
- No slide deck, transcript, or problem set was supplied for this lecture, so none is drawn on here.
- The notes' opening agenda lists "Neural Networks (RNN, LSTM)" as the lecture's second topic; the
  supplied material contains no content on it, so it is not covered in this chapter.
- Not contained in the supplied material: the original Yule (1927) paper itself, and any numerical
  fit of the sunspot series (no data or fitted coefficients appear in the notes).

---

[← 68. Regression with an Unknown Changepoint](68-regression-with-an-unknown-changepoint.md) · [Contents](index.md) · [70. Bayesian Shrinkage and Variance Models →](70-bayesian-shrinkage-and-variance-models.md)
