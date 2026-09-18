---
title: Lecture Twenty - Five
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwentyFive153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureTwentyFive153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureTwentyFive153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwentyFive153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture Twenty - Five

(1) AR & Nonlinear AR
(2) RNN
(3) GRU
(4) LSTM

---

## AR & NAR

$$y_1, \dots, y_n$$

$$y_t, \quad x_t = (y_{t-1}, y_{t-2}, \dots, y_{t-p})$$
$$t = p+1, \dots, n$$

**AR:**
$$\to \mu_t = \beta_0 + \beta^T x_t$$

$$\text{Loss}: \sum (y_t - \mu_t)^2$$

$$y_t = \mu_t + \varepsilon_t$$
$$\varepsilon_t \overset{iid}{\sim} N(0, \sigma^2)$$

**Qn:** How to make AR nonlinear?

$p=1$
$$x_t = y_{t-1}$$
$$\mu_t = \beta_0 + \beta_1 (y_{t-1})_+ + \beta_2 (y_{t-1} - c_1)_+ + \dots + \beta_{k+1} (y_{t-1} - c_k)_+$$
$$c_1, \dots, c_k$$
$$\beta_0, \beta_1, \beta_2, \dots, \beta_{k+1}$$

\$\$y_{t

---

[Up: contents](index.md)
