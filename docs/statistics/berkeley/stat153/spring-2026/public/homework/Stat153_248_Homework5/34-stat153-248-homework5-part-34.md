---
title: Stat153 248 Homework5 Part 34 —
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat153_248_Homework5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Stat153 248 Homework5 Part 34 —

**Source:** [`public/homework/Stat153_248_Homework5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

### Question 8 (2 points)

You are designing a classifier for two different tasks. For each, state whether you would use a **1D CNN on the raw waveform**, a **2D CNN on a spectrogram**, or a **non-convolutional model** (e.g., logistic regression on hand-engineered features). Justify your choice in one or two sentences referencing specific properties of convolutional models.

**(a)** Detecting a single, fixed, known template (e.g., a specific epileptic spike waveform) in continuous time series brain data (EEG).

**(b)** Classifying spoken words from raw audio, where pronunciation varies across speakers and time.

**Your answer:**

(a)

(b)

### Question 9 (2 points)

A student trains two models on the same audio dataset with the same architecture and hyperparameters. The only difference is the train/test split:

- **Model A:** random 80/20 split of all recordings.
- **Model B:** held-out speaker where all recordings from one speaker are in the test set, none in the training set.

Model A achieves 95% test accuracy; Model B achieves 45% test accuracy.

**(a)** Explain the gap. What has Model A likely learned that Model B is failing to exploit?

**(b)** Which number better reflects how well the model will perform on a *new user* of the system, and why?

**Your answer:**

(a)

(b)

## Part 4: Recurrent neural networks

*We have not covered RNNs in lecture yet. This short section introduces the essentials and compares RNNs to the CNNs you just worked through.*

### Primer

A **recurrent neural network (RNN)** processes a sequence $x_1, x_2, \ldots, x_T$ one step at a time, maintaining a hidden state $h_t$ that summarizes everything seen so far and predicts $\hat{y}_t$. The simplest ("vanilla") RNN applies the same update equation at every timestep:

$$h_t = \tanh(W_h h_{t-1} + W_x x_t + b_h), \qquad \hat{y}_t = W_y h_t + b_y$$

Here $W_h \in \mathbb{R}^{H \times H}$, $W_x \in \mathbb{R}^{H \times d}$, $W_y \in \mathbb{R}^{k \times H}$, where $H$ is the hidden size, $d$ is the input dimension per timestep, and $k$ is the output dimension. The nonlinearity is usually $\tanh$ or ReLU.

We fit the following parameters:

* $W_x$, which maps the current input $x_t$ into the hidden space
* $W_h$, which maps the previous hidden state $h_{t-1}$ forward
* $b_h$, which is the bias term for the hidden update
* $W_y$, which maps the hidden state to the output
* $b_y$, the bias for the output

There are three important properties:

1. **Weight sharing across time**: The same $(W_h, W_x, W_y)$ are used at every timestep. This is analogous to a convolutional filter being applied at every spatial position.
2. **Unbounded context (in principle)**: The hidden state $h_t$ can depend on arbitrarily distant past inputs through the recurrence, unlike a CNN whose receptive field is fixed by architecture.
3. **Training is sequential**: To compute $h_t$ you need $h_{t-1}$, so forward and backward passes run step-by-step along the sequence. This is called backpropagation through time (BPTT). It means RNNs are harder to parallelize than CNNs, which compute all positions in a layer at once.

**Vanishing/exploding gradients.** When you backpropagate through many timesteps, the gradient is multiplied by $W_h$ repeatedly. If the eigenvalues of $W_h$ are less than 1 in magnitude, gradients shrink to zero over long sequences and the network cannot learn long-range dependencies. If greater than 1, gradients explode. **LSTM** and **GRU** cells are architectural modifications that add gating mechanisms to control information flow; they preserve gradients over much longer timescales and are what people actually use in practice. For this homework, "LSTM" and "GRU" can be treated as black-box drop-in replacements for the vanilla RNN that handle long sequences better.

Here are some rough rules of thumb for time series tasks:

| Property | CNN (1D) | RNN (LSTM/GRU) |
|---|---|---|
| Receptive field | fixed by architecture | unbounded (in principle) |
| Parallelism across time | yes | no |
| Training speed | fast | slow |
| Good for | local patterns, fixed-scale features | long-range dependencies, variable-length sequences |

Modern practice often combines the two, using a CNN frontend for efficient local feature extraction, followed by an RNN (or transformer) for long-range integration. This is the architecture behind models like wav2vec 2.0 mentioned in lecture 23.

### Question 10 (2 points): parameter counting for an RNN

Consider a vanilla RNN with input dimension $d = 10$, hidden size $H = 64$, and output dimension $k = 3$ (the output is produced at every timestep).

**(a)** Compute the total number of trainable parameters in the RNN (include biases: one bias vector for the hidden state update, one for the output). Show each term.

**(b)** Compare to a 1D CNN with the same input dimension ($d = 10$ channels), 64 output channels, and kernel size 3 (no bias, for simplicity). How many parameters does the CNN have? What does the comparison tell you?

**Your answer:**

(a)

(b)

### Question 11 (3 points): When to use a RNN vs. a CNN?

For each of the following time series tasks, state whether you would start with a **1D CNN**, an **RNN (LSTM/GRU)**, or a **hybrid (CNN frontend + RNN)**. Justify each answer in one or two sentences citing a specific property from the primer.

**(a)** Forecasting daily electricity demand 24 hours ahead, where the relevant patterns include weekly cycles (7 days) and annual cycles (365 days). You have one data point per hour.

**(b)** Detecting epilepsy related activity (also called interictal epileptiform discharges (IEDs)) in continuous intracranial EEG recordings from the brain. IEDs are stereotyped short (~100 ms) waveforms and the model should output a label per time window.

**(c)** Classifying full sentences of speech (variable length, several seconds, where word-level meaning depends on long-range context across the sentence) from audio waveforms.

**Your answer:**

(a)

(b)

(c)

---

[← fc weight: 6410 = 640, bias: 10 -> 650](33-fc-weight-6410-640-bias-10---650.md) · [Up: contents](index.md)
