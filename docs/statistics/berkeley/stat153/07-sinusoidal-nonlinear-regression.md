---
title: "7. Sinusoidal Nonlinear Regression"
course: "Berkeley Stat 153"
chapter: 7
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 7. Sinusoidal Nonlinear Regression

## What this covers

This chapter asks what changes when a regression model is nonlinear in its parameters, using the
running example of a periodic signal of unknown frequency. It works out how a sinusoid's amplitude,
frequency and phase relate to the coefficients a computer actually fits, why sampling a continuous
signal at discrete times caps which frequencies can be recovered at all, and how the frequency is
estimated by least squares despite entering the model nonlinearly. It assumes multiple linear
regression — the normal equations, the design matrix, residual sum of squares — from the previous
lecture.

## From linear to nonlinear regression

Multiple linear regression models $y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots +
\beta_p x_{ip} + w_i$: a relationship that is linear *in the parameters* $\beta$. Many real series
are not. The lecture's example is the sunspot record: smoothed monthly sunspot counts do not settle
near a fixed level but oscillate with a very stable period, and no linear combination of a few
predictors captures that on its own.

The same shape of problem — recovering an unknown frequency from noisy data — recurs across fields:

* Climate data, e.g. El Niño / the Southern Oscillation Index.
* Astronomy: variable stars, whose brightness oscillates with a period $1/f$ that is related to the
  star's intrinsic luminosity, and hence to its distance. Edwin Hubble used exactly this relationship
  in the 1920s to estimate the distance to the Andromeda galaxy, showing it lay far outside the Milky
  Way — evidence that the Milky Way is only one galaxy among many.
* Signal processing: estimating the pitch and formants of a person's voice, part of automatic speech
  recognition.
* Economics, "but generally less stable."

The natural model for a periodic signal observed with noise is

$$y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t, \qquad \epsilon_t
\overset{\text{iid}}{\sim} N(0,\sigma^2).$$

If the frequency $f$ were known in advance, this would already be multiple linear regression.
Writing

$$y = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}, \qquad X_f = \begin{pmatrix} 1 & \cos(2\pi
f(1)) & \sin(2\pi f(1)) \\ \vdots & \vdots & \vdots \\ 1 & \cos(2\pi f(n)) & \sin(2\pi f(n))
\end{pmatrix}, \qquad \beta = \begin{pmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \end{pmatrix},$$

the model reads $y = X_f \beta + \epsilon$ and ordinary least squares applies exactly as before.
What makes this a genuinely *nonlinear* regression problem is that $f$ is usually not known, and the
model is not linear in $f$: $\cos(2\pi f t)$ does not change linearly as $f$ varies. This particular
model is called a **sinusoid**, and it has properties worth pinning down before estimating anything.

## What a sinusoid's parameters mean

Write the same curve in amplitude–phase form:

$$s(t) := \beta_0 + R\cos(2\pi f t + \phi).$$

* $R$ — the **amplitude**: the height of the oscillation above (and below) the center line $\beta_0$.
* $f$ — the **frequency**: cycles per unit time. If $t$ is in seconds, $f$ is in Hertz.
* $1/f$ — the **period**: the time to complete one full oscillation.
* $\phi$ — the **phase**: shifts the whole oscillation left or right in time. At $\phi = 0$ the curve
  is at its maximum when $t = 0$.
* $\omega := 2\pi f$ — the **angular frequency**: the rate of change of the angle inside the cosine.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="A cosine curve with the baseline, amplitude, period and phase shift marked">
  <defs>
    <marker id="arr1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="10" y1="110" x2="390" y2="110" stroke="currentColor" stroke-width="1" stroke-dasharray="4,4" opacity="0.6"/>
  <text x="14" y="104" font-size="12" fill="currentColor">&#946;&#8320;</text>
  <polyline points="20.0,75.8 26.1,85.7 32.2,96.7 38.3,108.2 44.4,119.9 50.5,131.1 56.6,141.4 62.7,150.2 68.8,157.2 74.9,162.1 81.0,164.7 87.1,164.7 93.2,162.3 99.3,157.5 105.4,150.6 111.5,141.8 117.6,131.6 123.7,120.5 129.8,108.8 135.9,97.2 142.0,86.2 148.1,76.3 154.2,67.8 160.3,61.3 166.4,57.0 172.5,55.1 178.6,55.7 184.7,58.7 190.8,64.0 196.9,71.4 203.1,80.6 209.2,91.1 215.3,102.4 221.4,114.1 227.5,125.6 233.6,136.4 239.7,146.0 245.8,154.0 251.9,160.0 258.0,163.7 264.1,165.0 270.2,163.8 276.3,160.2 282.4,154.3 288.5,146.4 294.6,136.9 300.7,126.2 306.8,114.7 312.9,103.0 319.0,91.6 325.1,81.1 331.2,71.8 337.3,64.3 343.4,58.9 349.5,55.7 355.6,55.1 361.7,56.9 367.8,61.1 373.9,67.5 380.0,75.8" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <circle cx="20" cy="75.8" r="3" fill="currentColor"/>
  <circle cx="172.5" cy="55.1" r="3" fill="currentColor"/>
  <line x1="20" y1="35" x2="20" y2="75.8" stroke="currentColor" stroke-width="0.75" stroke-dasharray="3,3" opacity="0.5"/>
  <line x1="172.5" y1="35" x2="172.5" y2="55.1" stroke="currentColor" stroke-width="0.75" stroke-dasharray="3,3" opacity="0.5"/>
  <line x1="20" y1="35" x2="172.5" y2="35" stroke="currentColor" stroke-width="1.2" marker-start="url(#arr1)" marker-end="url(#arr1)"/>
  <text x="96" y="25" text-anchor="middle" font-size="12" fill="currentColor">phase &#966;</text>
  <line x1="355.6" y1="110" x2="355.6" y2="55.1" stroke="currentColor" stroke-width="1.2" marker-start="url(#arr1)" marker-end="url(#arr1)"/>
  <text x="362" y="84" font-size="12" fill="currentColor">R</text>
  <line x1="172.5" y1="55.1" x2="172.5" y2="195" stroke="currentColor" stroke-width="0.75" stroke-dasharray="3,3" opacity="0.5"/>
  <line x1="355.6" y1="55.1" x2="355.6" y2="195" stroke="currentColor" stroke-width="0.75" stroke-dasharray="3,3" opacity="0.5"/>
  <line x1="172.5" y1="195" x2="355.6" y2="195" stroke="currentColor" stroke-width="1.2" marker-start="url(#arr1)" marker-end="url(#arr1)"/>
  <text x="264" y="210" text-anchor="middle" font-size="12" fill="currentColor">period = 1/f</text>
  <text x="385" y="80" text-anchor="end" font-size="12" fill="currentColor">t</text>
</svg>
<figcaption>The sinusoid $s(t) = \beta_0 + R\cos(2\pi f t + \phi)$: $\beta_0$ sets the center line,
$R$ the height of the swings above it, $1/f$ the time between successive peaks, and $\phi$ how far
the first peak is shifted away from $t=0$.</figcaption>
</figure>

This doesn't look like $y_t = \beta_0 + \beta_1\cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t$
above, but it's the same model. Expand with the identity $\cos(a+b) = \cos a \cos b - \sin a \sin b$,
taking $a = 2\pi f t$ and $b = \phi$:

$$s(t) = \beta_0 + R\big(\cos(2\pi f t)\cos\phi - \sin(2\pi f t)\sin\phi\big) = \beta_0 + R\cos\phi
\cos(2\pi f t) - R\sin\phi \sin(2\pi f t).$$

Setting $\beta_1 = R\cos\phi$ and $\beta_2 = -R\sin\phi$ turns this into exactly $s(t) = \beta_0 +
\beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t)$. The map is invertible, so a fitted $(\hat\beta_1,
\hat\beta_2)$ always gives back the amplitude and phase:

$$R = \sqrt{\beta_1^2 + \beta_2^2}, \qquad \phi = \arctan\!\left(-\frac{\beta_2}{\beta_1}\right).$$

So $(\beta_1,\beta_2)$ and $(R,\phi)$ are two parameterizations of the same two degrees of freedom.
Regression estimates the first pair directly; the second is read off afterward.

## Sampling a continuous signal: the Nyquist limit

The sinusoid above is written in continuous time, but data are collected at discrete sampling times.
If the sampling rate is $f_s$ (samples per second), observations occur at $t_n = n/f_s$ for $n =
0,1,2,\dots$, so what is actually fit is

$$y_n = \beta_0 + R\cos\!\left(\frac{2\pi f n}{f_s} + \phi\right) + \epsilon_n.$$

The sampling rate fundamentally constrains which frequencies can be recovered. Frequencies up to
half the sampling rate,

$$f_{\max} = \frac{f_s}{2},$$

called the **Nyquist frequency**, can be reliably estimated. A true component at a higher frequency
$f > f_s/2$ does not vanish from the data — it produces **aliasing**: the frequency that shows up in
the fit is $|f - n f_s|$ for whichever integer $n$ brings that value down into range. Two different
continuous sinusoids can agree exactly at every sampling time while disagreeing everywhere between
them.

<figure>
<svg viewBox="0 0 400 205" role="img" aria-label="A fast and a slow cosine curve that pass through exactly the same sample points">
  <circle cx="30" cy="15" r="3.5" fill="currentColor"/>
  <text x="40" y="19" font-size="11" fill="currentColor">samples common to both curves</text>
  <text x="140" y="40" text-anchor="middle" font-size="12" fill="currentColor">true signal: f = 0.9</text>
  <polyline points="20.0,55.0 22.4,55.8 24.8,58.2 27.2,62.1 29.7,67.4 32.1,73.8 34.5,81.1 36.9,89.2 39.3,97.6 41.7,106.1 44.2,114.4 46.6,122.2 49.0,129.2 51.4,135.1 53.8,139.8 56.2,143.1 58.7,144.8 61.1,144.8 63.5,143.3 65.9,140.2 68.3,135.7 70.7,129.9 73.2,123.0 75.6,115.3 78.0,107.1 80.4,98.6 82.8,90.1 85.2,82.0 87.7,74.6 90.1,68.0 92.5,62.6 94.9,58.6 97.3,56.0 99.7,55.0 102.1,55.6 104.6,57.9 107.0,61.6 109.4,66.7 111.8,73.0 114.2,80.3 116.6,88.3 119.1,96.7 121.5,105.2 123.9,113.5 126.3,121.4 128.7,128.5 131.1,134.5 133.6,139.4 136.0,142.8 138.4,144.6 140.8,144.9 143.2,143.6 145.6,140.7 148.1,136.3 150.5,130.6 152.9,123.9 155.3,116.2 157.7,108.0 160.1,99.5 162.6,91.0 165.0,82.9 167.4,75.3 169.8,68.7 172.2,63.2 174.6,58.9 177.0,56.2 179.5,55.0 181.9,55.5 184.3,57.5 186.7,61.1 189.1,66.1 191.5,72.3 194.0,79.4 196.4,87.4 198.8,95.7 201.2,104.3 203.6,112.6 206.0,120.6 208.5,127.7 210.9,133.9 213.3,138.9 215.7,142.5 218.1,144.5 220.5,145.0 223.0,143.8 225.4,141.1 227.8,136.8 230.2,131.3 232.6,124.7 235.0,117.1 237.4,109.0 239.9,100.5 242.3,92.0 244.7,83.8 247.1,76.1 249.5,69.4 251.9,63.7 254.4,59.3 256.8,56.4 259.2,55.1 261.6,55.4 264.0,57.2 266.4,60.6 268.9,65.5 271.3,71.5 273.7,78.6 276.1,86.5 278.5,94.8 280.9,103.3 283.4,111.7 285.8,119.7 288.2,127.0 290.6,133.3 293.0,138.4 295.4,142.1 297.9,144.4 300.3,145.0 302.7,144.0 305.1,141.4 307.5,137.4 309.9,132.0 312.3,125.4 314.8,118.0 317.2,109.9 319.6,101.4 322.0,92.9 324.4,84.7 326.8,77.0 329.3,70.1 331.7,64.3 334.1,59.8 336.5,56.7 338.9,55.2 341.3,55.2 343.8,56.9 346.2,60.2 348.6,64.9 351.0,70.8 353.4,77.8 355.8,85.6 358.3,93.9 360.7,102.4 363.1,110.8 365.5,118.9 367.9,126.2 370.3,132.6 372.8,137.9 375.2,141.8 377.6,144.2 380.0,145.0" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <polyline points="20.0,55.0 26.1,55.1 32.2,55.3 38.3,55.6 44.4,56.0 50.5,56.6 56.6,57.3 62.7,58.1 68.8,59.0 74.9,60.1 81.0,61.2 87.1,62.5 93.2,63.9 99.3,65.4 105.4,66.9 111.5,68.6 117.6,70.4 123.7,72.2 129.8,74.1 135.9,76.1 142.0,78.2 148.1,80.3 154.2,82.5 160.3,84.7 166.4,87.0 172.5,89.3 178.6,91.7 184.7,94.0 190.8,96.4 196.9,98.8 203.1,101.2 209.2,103.6 215.3,106.0 221.4,108.3 227.5,110.7 233.6,113.0 239.7,115.3 245.8,117.5 251.9,119.7 258.0,121.8 264.1,123.9 270.2,125.9 276.3,127.8 282.4,129.6 288.5,131.4 294.6,133.1 300.7,134.6 306.8,136.1 312.9,137.5 319.0,138.8 325.1,139.9 331.2,141.0 337.3,141.9 343.4,142.7 349.5,143.4 355.6,144.0 361.7,144.4 367.8,144.7 373.9,144.9 380.0,145.0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="6,4" opacity="0.7"/>
  <text x="300" y="158" text-anchor="middle" font-size="12" fill="currentColor">aliased estimate: |0.9 &#8722; 1| = 0.1</text>
  <circle cx="20.0" cy="55.0" r="3.5" fill="currentColor"/>
  <circle cx="92.0" cy="63.6" r="3.5" fill="currentColor"/>
  <circle cx="164.0" cy="86.1" r="3.5" fill="currentColor"/>
  <circle cx="236.0" cy="113.9" r="3.5" fill="currentColor"/>
  <circle cx="308.0" cy="136.4" r="3.5" fill="currentColor"/>
  <circle cx="380.0" cy="145.0" r="3.5" fill="currentColor"/>
  <line x1="10" y1="170" x2="390" y2="170" stroke="currentColor" stroke-width="1"/>
  <line x1="20" y1="170" x2="20" y2="176" stroke="currentColor" stroke-width="1"/>
  <line x1="92" y1="170" x2="92" y2="176" stroke="currentColor" stroke-width="1"/>
  <line x1="164" y1="170" x2="164" y2="176" stroke="currentColor" stroke-width="1"/>
  <line x1="236" y1="170" x2="236" y2="176" stroke="currentColor" stroke-width="1"/>
  <line x1="308" y1="170" x2="308" y2="176" stroke="currentColor" stroke-width="1"/>
  <line x1="380" y1="170" x2="380" y2="176" stroke="currentColor" stroke-width="1"/>
  <text x="20" y="188" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="92" y="188" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="164" y="188" text-anchor="middle" font-size="11" fill="currentColor">2</text>
  <text x="236" y="188" text-anchor="middle" font-size="11" fill="currentColor">3</text>
  <text x="308" y="188" text-anchor="middle" font-size="11" fill="currentColor">4</text>
  <text x="380" y="188" text-anchor="middle" font-size="11" fill="currentColor">5</text>
  <text x="200" y="201" text-anchor="middle" font-size="12" fill="currentColor">t, in samples (f_s = 1)</text>
</svg>
<figcaption>With sampling rate $f_s=1$, a true frequency $f=0.9$ (solid) and the aliased frequency
$|0.9-1|=0.1$ (dashed) give identical values at every integer sampling time, even though the two
curves disagree everywhere between the samples.</figcaption>
</figure>

Because of this, searching for $f$ by least squares never needs to test frequencies above the
Nyquist limit: it suffices to search $f \in [0, 1/2]$ once frequency is expressed in units of the
sampling rate.

## Estimating the frequency by least squares

All five parameters $\beta_0, \beta_1, \beta_2, f, \sigma$ are fit by minimizing

$$S(\beta_0,\beta_1,\beta_2,f,\sigma) := \sum_{t=1}^n \Big(y_t - \beta_0 - \beta_1\cos(2\pi f t) -
\beta_2 \sin(2\pi f t)\Big)^2.$$

Minimizing over all five at once is a genuine nonlinear least squares problem. But for any *fixed*
value of $f$, this is ordinary linear regression on the design matrix $X_f$ from the second section
— $f$ enters only through the columns of $X_f$, not through $\beta_0,\beta_1,\beta_2$. That lets the
frequency be searched for separately from the linear coefficients:

1. Take a grid of candidate values of $f$ in $[0, 1/2]$.
2. For each $f$ on the grid, build $X_f$, regress $y$ on $X_f$, and record the residual sum of
   squares $\mathrm{RSS}(f)$.
3. Take $\hat f$ to be the grid value that minimizes $\mathrm{RSS}(f)$.
4. With $f$ fixed at $\hat f$, take $\hat\beta$ and $\hat\sigma$ to be the usual least-squares
   estimates from regressing $y$ on $X_{\hat f}$.

## Sources

* Lecture index: [`09_nonlinear_regression.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nonlinear_regression.md) — reading pointer (Shumway & Stoffer, Ch. 2 in part and Ch. 4.1) and a link to a Nyquist-limit demo, neither reproduced here.
* [`09-nonlinear_regression_notes/01-nonlinear-regression.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nonlinear_regression_notes.md) — multiple linear regression recap, the sunspots motivation, the list of application areas, and the sinusoidal model (including the design matrix $X_f$).
* [`09_nonlinear_regression_notes/02-about-sinusoids.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nonlinear_regression_notes.md) — the amplitude/frequency/period/phase parameterization and its derivation.
* [`09_nonlinear_regression_notes/03-a-note-on-dealing-with-sampling.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nonlinear_regression_notes.md) — discrete sampling, the Nyquist limit, aliasing, and the least-squares estimation procedure.
* Referred to but not contained in the supplied material: Shumway & Stoffer, *Time Series Analysis*, Chapter 2 and Chapter 4.1; the sunspots figure (`09_sunspots.png`) and the interactive [Nyquist limit demo](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/09_nyquist.html), both linked from the lecture page rather than included in it. No transcript, written notes or problem set were supplied for this lecture.

---

[← 6. Simple and Multiple Linear Regression](06-simple-and-multiple-linear-regression.md) · [Contents](index.md) · [8. Improving upon the linear model →](08-improving-upon-the-linear-model.md)
