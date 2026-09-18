---
title: History (How AR models were invented)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureSixteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureSixteen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureSixteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureSixteen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# History (How AR models were invented)

(Yule 1927)

[Sunspots data]
$y_t$ : sunspots data

$$
\boxed{y_t = \beta_0 + \beta_1 \cos 2\pi ft + \beta_2 \sin 2\pi ft + \varepsilon_t} \qquad \varepsilon_t \overset{iid}{\sim} N(0, \sigma^2)
$$

$$\boxed{f, \beta_0, \beta_1, \beta_2, \sigma}$$
$$\downarrow$$
$$\frac{1}{11}$$

$$s(t) = \beta_0 + \beta_1 \cos 2\pi ft + \beta_2 \sin 2\pi ft$$

$$\text{Model 1}: \quad \boxed{y_t = s_t + \varepsilon_t} \qquad t = 1, 2, \dots$$

$$s(t) = \boxed{\beta_0 + \beta_1 \cos 2\pi ft + \beta_2 \sin 2\pi ft}$$

$$s''(t) = -(2\pi f)^2 [\beta_1 \cos 2\pi ft + \beta_2 \sin 2\pi ft]$$

$$\boxed{s''(t) = -(2\pi f)^2 (s(t) - \beta_0)}$$

---

$$\boxed{\begin{aligned} (s_t - s_{t-1}) - (s_{t-1} - s_{t-2}) \\ = 2[\cos(2\pi f) - 1] (s_{t-1} - \beta_0) \end{aligned}} \iff \begin{aligned} s_t = \beta_0 &+ \beta_1 \cos 2\pi f t \\ &+ \beta_2 \sin 2\pi f t \end{aligned}$$

$$\boxed{\begin{aligned} (y_t - y_{t-1}) - (y_{t-1} - y_{t-2}) \\ = 2(\cos 2\pi f - 1)(y_{t-1} - \beta_0) + \eta_t \end{aligned}}$$

$$\Updownarrow$$

$$y_t = \phi_0 + \phi_1 y_{t-1} \boxed{-} y_{t-2} + \eta_t$$
$$\downarrow$$
$$+ \phi_2 \qquad \text{special case of AR(2)}$$

$$\text{① } \boxed{y_t = \beta_0 + \beta_1 \cos 2\pi f t + \beta_2 \sin 2\pi f t + \varepsilon_t}$$

$$\text{② } \boxed{y_t = \phi_0 + \phi_1 y_{t-1} - y_{t-2} + \eta_t}$$

$s(t)$ : position of the object at time $t$.

$$s''(t) = -\frac{k}{m} (s(t) - \beta_0) \quad \text{+ random noise due to stone throwing}$$
$$\uparrow$$
$$\text{spring}$$

---

$$s''(t) = -\frac{k}{m}(s(t) - \beta_0)$$
$$\uparrow$$
$$\text{spring constant}$$

$$\text{Scenario 1}: \quad y_t = s(t) + \varepsilon_t, \quad \varepsilon_t \overset{iid}{\sim} N(0, \sigma^2)$$

$$\text{Scenario 2}: \quad \boxed{y''(t) = -k(y(t) - \beta_0) + \eta_t}$$
$$\downarrow$$
$$y(t) = \text{will be smooth.}$$

## YULE MODEL:

$$\boxed{y_t = \phi_0 + \phi_1 y_{t-1} - y_{t-2} + \varepsilon_t}$$
$$\boxed{\phi_1 = 2 \cos 2\pi f}$$

$$y_t + y_{t-2} = \phi_0 + \phi_1 y_{t-1} + \varepsilon_t$$

---

[← AR($p$)](02-ar.md) · [Up: contents](index.md)
