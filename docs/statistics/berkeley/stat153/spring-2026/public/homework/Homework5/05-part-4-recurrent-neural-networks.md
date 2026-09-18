---
title: 'Part 4: Recurrent neural networks'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf
source_file: sources/berkeley-stat153/spring-2026/public/homework/Homework5.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`public/homework/Homework5.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Part 4: Recurrent neural networks

*We have not covered RNNs in lecture yet. This short section introduces the essentials and compares RNNs to the CNNs you just worked through.*

### Primer

A recurrent neural network (RNN) processes a sequence $x_1, x_2, \dots, x_T$ one step at a time, maintaining a hidden state $h_t$ that summarizes everything seen so far and predicts $\hat{y}_t$. The simplest ("vanilla") RNN applies the same update equation at every timestep:

$$h_t = \tanh(W_h h_{t-1} + W_x x_t + b_h), \quad \hat{y}_t = W_y h_t + b_y$$

Here $W_h \in \mathbb{R}^{H \times H}$, $W_x \in \mathbb{R}^{H \times d}$, $W_y \in \mathbb{R}^{k \times H}$, where $H$ is the hidden size, $d$ is the input dimension per timestep, and $k$ is the output dimension. The nonlinearity is usually $\tanh$ or ReLU.

We fit the following parameters:

* $W_x$, which maps the current input $x_t$ into the hidden space
* $W_h$, which maps the previous hidden state $h_{t-1}$ forward
* $b_h$, which is the bias term for the hidden update
* $W_y$, which maps the hidden state to the output
* $b_y$, the bias for the output

There are three important properties:

1. **Weight sharing across time:** The same $(W_h, W_x, W_y)$ are used at every timestep. This is analogous to a convolutional filter being applied at every spatial position.
2. **Unbounded context (in principle):** The hidden state $h_t$ can depend on arbitrarily distant past inputs through the recurrence, unlike a CNN whose receptive field is fixed by architecture.
3. **Training is sequential:** To compute $h_t$ you need $h_{t-1}$, so forward and backward passes run step-by-step along the sequence. This is called backpropagation through time (BPTT). It means RNNs are harder to parallelize than CNNs, which compute all positions in a layer at once.

**Vanishing/exploding gradients.** When you backpropagate through many timesteps, the gradient is multiplied by $W_h$ repeatedly. If the eigenvalues of $W_h$ are less than 1 in magnitude, gradients shrink to zero over long sequences and the network cannot learn long-range dependencies. If greater than 1, gradients explode. **LSTM and GRU** cells are architectural modifications that add gating mechanisms to control information flow; they preserve gradients over much longer timescales and are what people actually use in practice. For this homework, "LSTM" and "GRU" can be treated as black-box drop-in replacements for the vanilla RNN that handle long sequences better.

Here are some rough rules of thumb for time series tasks:

| Property | CNN (1D) | RNN (LSTM/GRU) |
| :--- | :--- | :--- |
| Receptive field | fixed by architecture | unbounded (in principle) |
| Parallelism across time | yes | no |
| Training speed | fast | slow |
| Good for | local patterns, fixed-scale features | long-range dependencies, variable-length sequences |

Modern practice often combines the two, using a CNN frontend for efficient local feature extraction, followed by an RNN (or transformer) for long-range integration. This is the architecture behind models like wav2vec 2.0 mentioned in lecture 23.

## Question 10 (2 points): parameter counting for an RNN

Consider a vanilla RNN with input dimension $d = 10$, hidden size $H = 64$, and output dimension $k = 3$ (the output is produced at every timestep).

**(a)** Compute the total number of trainable parameters in the RNN (include biases: one bias vector for the hidden state update, one for the output). Show each term.

**(b)** Compare to a 1D CNN with the same input dimension ($d = 10$ channels), 64 output channels, and kernel size 3 (no bias, for simplicity). How many parameters does the CNN have? What does the comparison tell you?

### Your answer:

(a)

(b)

## Question 11 (3 points): When to use a RNN vs. a CNN?

For each of the following time series tasks, state whether you would start with a **1D CNN**, an **RNN (LSTM/GRU)**, or a **hybrid (CNN frontend + RNN)**. Justify each answer in one or two sentences citing a specific property from the primer.

**(a)** Forecasting daily electricity demand 24 hours ahead, where the relevant patterns include weekly cycles (7 days) and annual cycles (365 days). You have one data point per hour.

**(b)** Detecting epilepsy related activity (also called interictal epileptiform discharges (IEDs)) in continuous intracranial EEG recordings from the brain. IEDs are stereotyped short (~100 ms) waveforms and the model should output a label per time window.

**(c)** Classifying full sentences of speech (variable length, several seconds, where word-level meaning depends on long-range context across the sentence) from audio waveforms.

### Your answer:

(a)

(b)

(c)

```python

```

---

[← Question 7 (5 points): parameter counting](04-question-7-5-points-parameter-counting.md) · [Up: contents](index.md)
