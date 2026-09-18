---
title: Lecture Three (153-248) (Sept 03)
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureThree153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/HandwrittenNotesLectureThree153248Fall2026.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureThree153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/HandwrittenNotesLectureThree153248Fall2026.pdf) — berkeley-stat153 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture Three (153-248) (Sept 03)

## Linear Regression Math

**Simple Question 1**: Suppose I have two numbers $a$ & $b$. I tell you that $a + b = 7$. What can you say about $a$?

**Simple Question 2**: I have two numbers $a$ & $b$. Suppose $b$ is small in magnitude. As before, $a + b = 7$. What can you say about $a$?

**Solution**: $a$ & $b$.

Assume independent:
- $a \sim \text{Unif}(-C, C)$ for a very large $C$.
- $b \sim N(0, \sigma^2)$, $\sigma^2 = 0.5$

Calculate $a \mid a + b = 7$

Let $y = a + b$.

$a \mid y = 7$

$$y = \underset{\text{Unif}(-C, C)}{a} + \underset{N(0, \sigma^2)}{b}$$

---

$$y \mid a \sim N(a, \sigma^2)$$

$$\begin{aligned}
f_{a \mid y = 7}(a) &= \frac{f_{y \mid a}(7) f_a(a)}{f_y(7)} \quad \text{Bayes Rule} \\
&\propto f_{y \mid a}(7) f_a(a) \\
&= \frac{1}{\sqrt{2\pi}\sigma} \exp\left\{ -\frac{(a-y)^2}{2\sigma^2} \right\} \frac{I\{-C < a < C\}}{2C} \\
&\propto \frac{1}{\sigma} \exp\left( -\frac{(a-7)^2}{2\sigma^2} \right) \quad [y=7]
\end{aligned}$$

$$a \mid a + b = 7 \sim N(7, \sigma^2)$$

**Answer**: $N(7, \sigma^2)$

---

**Question 3**: I have $a, b_1, b_2$.
$b_1$ & $b_2$ are small in magnitude.
$$a + b_1 = 7$$
$$a + b_2 = 10$$
What can you say about $a$?

**Solution**: Assume independent:
$$\begin{aligned}
a &\sim \text{Unif}(-C, C) \\
b_1, b_2 &\sim N(0, \sigma^2) \\
\log \sigma &\sim \text{Unif}(-C, C)
\end{aligned}$$

$$a \mid \begin{aligned} a + b_1 &= 7 \\ a + b_2 &= 10 \end{aligned} \qquad \begin{aligned} y_1 &= a + b_1 \\ y_2 &= a + b_2 \end{aligned}$$

$$a \mid y_1, y_2$$

$$a, \sigma \mid y_1, y_2$$

\$\$f_{a, \

---

[Up: contents](index.md)
