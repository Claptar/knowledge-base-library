---
title: 'Lecture 26: Recurrent neural networks part 2'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/26_RNNs_Part2.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/26_RNNs_Part2.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`public/lectures/26_RNNs_Part2.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/26_RNNs_Part2.pdf) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture 26: Recurrent neural networks part 2

Liberty Hamilton
April 30, 2026

---

## Announcements

- For Stat248 - Final Project Instructions are on bCourses
- For Stat153 - Final Exam will be May 14 - 7-10pm, in this classroom
- No class next week, but we will have a final review session on Tuesday
- I will have regular office hours (Tuesday after class)
- Homework 5 is now optional/extra credit (3%)
- We will also have a little on pytorch with RNNs + exam review in Lab this week

---

## Recap

- Recurrent neural networks (RNNs)
  - Appropriate for problems where data have sequential dependence
  - Trainable using backpropagation through time (BPTT)
    - This is like "unrolling" the recurrent network into a (very) deep feedforward network, and then applying backpropagation
  - RNNs are great for problems like language, which requires more sequential processing than vision

---

## Today

- Gated RNNs
  - LSTMs
  - GRUs

---

## More reading for today...

- The Unreasonable Effectiveness of Recurrent Neural Networks (Andrej Karpathy)
- Understanding LSTM Networks (Chris Olah)

---

## The trouble with RNNs

- Suppose we want to predict the last word:

  *When she tried to print her tickets, she found that the printer was out of toner. She went to the stationery store to buy more toner. It was very overpriced. After installing the toner into the printer, she finally printed her* ________

---

## The trouble with RNNs

- Suppose we want to predict the last word:

  *When she tried to print her **tickets**, she found that the printer was out of toner. She went to the stationery store to buy more toner. It was very overpriced. After installing the toner into the printer, she finally printed her* ________

  ~37 steps back!

---

## The trouble with RNNs

- RNNs suffer from the problems of **vanishing** and **exploding gradients**
- This problem is worse when backpropagating over a **long sequence**
  - Limits temporal dependence of functions that simple RNNs can learn

---

## The trouble with RNNs

- Simple 1-D example:

$$h_{t+1} = \sigma(wh_t) \qquad \frac{\partial h_{t+1}}{\partial h_t} = w\sigma'(wh_t)$$

nonlinearity (e.g. tanh, sigmoid, maaybe ReLu)

---

## The trouble with RNNs

- Simple 1-D example:

$$h_{t+1} = \sigma(wh_t) \qquad \frac{\partial h_{t+1}}{\partial h_t} = w\sigma'(wh_t)$$

$$\frac{\partial h_{t+2}}{\partial h_t} = w\sigma'(wh_{t+1})w\sigma'(wh_t)$$

---

## The trouble with RNNs

- Simple 1-D example:

$$h_{t+1} = \sigma(wh_t) \qquad \frac{\partial h_{t+1}}{\partial h_t} = w\sigma'(wh_t)$$

$$\frac{\partial h_{t+2}}{\partial h_t} = w\sigma'(wh_{t+1})w\sigma'(wh_t)$$

$$\frac{\partial h_{t+n}}{\partial h_t} = w^n \prod_{j=0}^{n-1} \sigma'(wh_{t+j})$$

---

## The trouble with RNNs

- Simple 1-D example:

$$h_{t+1} = \sigma(wh_t) \qquad \frac{\partial h_{t+1}}{\partial h_t} = w\sigma'(wh_t)$$

$$\frac{\partial h_{t+2}}{\partial h_t} = w\sigma'(wh_{t+1})w\sigma'(wh_t)$$

$$\frac{\partial h_{t+n}}{\partial h_t} = w^n \prod_{j=0}^{n-1} \sigma'(wh_{t+j})$$

$w^n$ : really bad
$\prod_{j=0}^{n-1} \sigma'(wh_{t+j})$ : also bad

---

[Up: contents](../../index.md)

## Figures

Extracted from the original PDF. They are listed by the page they came from rather
than placed in the text: the conversion does not record where on the page each one
sat.

![Figure from page 13 of the original](26_RNNs_Part2/figures/p013-1.png)

![Figure from page 14 of the original](26_RNNs_Part2/figures/p014-1.png)

![Figure from page 18 of the original](26_RNNs_Part2/figures/p018-1.png)

![Figure from page 19 of the original](26_RNNs_Part2/figures/p019-1.png)

![Figure from page 19 of the original](26_RNNs_Part2/figures/p019-2.png)

![Figure from page 20 of the original](26_RNNs_Part2/figures/p020-1.png)

![Figure from page 20 of the original](26_RNNs_Part2/figures/p020-2.png)

![Figure from page 21 of the original](26_RNNs_Part2/figures/p021-1.png)

![Figure from page 22 of the original](26_RNNs_Part2/figures/p022-1.png)

![Figure from page 23 of the original](26_RNNs_Part2/figures/p023-1.png)

![Figure from page 24 of the original](26_RNNs_Part2/figures/p024-1.png)

![Figure from page 26 of the original](26_RNNs_Part2/figures/p026-1.png)

![Figure from page 27 of the original](26_RNNs_Part2/figures/p027-1.png)

![Figure from page 28 of the original](26_RNNs_Part2/figures/p028-1.png)

![Figure from page 29 of the original](26_RNNs_Part2/figures/p029-1.png)

![Figure from page 30 of the original](26_RNNs_Part2/figures/p030-1.png)

![Figure from page 31 of the original](26_RNNs_Part2/figures/p031-1.png)

![Figure from page 32 of the original](26_RNNs_Part2/figures/p032-1.png)

![Figure from page 33 of the original](26_RNNs_Part2/figures/p033-1.png)

![Figure from page 34 of the original](26_RNNs_Part2/figures/p034-1.png)

![Figure from page 35 of the original](26_RNNs_Part2/figures/p035-1.png)

![Figure from page 36 of the original](26_RNNs_Part2/figures/p036-1.png)

![Figure from page 37 of the original](26_RNNs_Part2/figures/p037-1.png)

![Figure from page 41 of the original](26_RNNs_Part2/figures/p041-1.png)

![Figure from page 42 of the original](26_RNNs_Part2/figures/p042-1.png)

![Figure from page 43 of the original](26_RNNs_Part2/figures/p043-1.png)

![Figure from page 44 of the original](26_RNNs_Part2/figures/p044-1.png)

![Figure from page 44 of the original](26_RNNs_Part2/figures/p044-2.png)

![Figure from page 44 of the original](26_RNNs_Part2/figures/p044-3.png)

![Figure from page 45 of the original](26_RNNs_Part2/figures/p045-1.png)

![Figure from page 46 of the original](26_RNNs_Part2/figures/p046-1.png)

![Figure from page 47 of the original](26_RNNs_Part2/figures/p047-1.png)

![Figure from page 48 of the original](26_RNNs_Part2/figures/p048-1.png)

![Figure from page 48 of the original](26_RNNs_Part2/figures/p048-2.png)

![Figure from page 49 of the original](26_RNNs_Part2/figures/p049-1.png)

![Figure from page 49 of the original](26_RNNs_Part2/figures/p049-2.png)

![Figure from page 50 of the original](26_RNNs_Part2/figures/p050-1.jpeg)

