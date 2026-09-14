---
title: Homework5 Part 30 —
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf
source_file: sources/berkeley-stat153/spring-2026/public/homework/Homework5.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Homework5 Part 30 —

**Source:** [`public/homework/Homework5.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

```

### Question 8 (2 points)

You are designing a classifier for two different tasks. For each, state whether you would use a 1D CNN on the raw waveform, a 2D CNN on a spectrogram, or a nonconvolutional model (e.g., logistic regression on hand-engineered features). Justify your choice in one or two sentences referencing specific properties of convolutional models.

(a) Detecting a single, fixed, known template (e.g., a specific epileptic spike waveform) in continuous time series brain data (EEG).

(b) Classifying spoken words from raw audio, where pronunciation varies across speakers and time.

Your answer:

(a)

(b)

### Question 9 (2 points)

A student trains two models on the same audio dataset with the same architecture and hyperparameters. The only difference is the train/test split:

- Model A: random 80/20 split of all recordings.

- Model B: held-out speaker where all recordings from one speaker are in the test set, none in the training set.

Model A achieves 95% test accuracy; Model B achieves 45% test accuracy.

(a) Explain the gap. What has Model A likely learned that Model B is failing to exploit?

(b) Which number better reflects how well the model will perform on a new user of the system, and why?

Your answer:

(a)

(b)

## Part 4: Recurrent neural networks

We have not covered RNNs in lecture yet. This short section introduces the essentials and compares RNNs to the CNNs you just worked through.

### Primer

A recurrent neural network (RNN) processes a sequence x1, x2, … , xT one step at a time, maintaining a hidden state ht that summarizes everything seen so far and predicts y^t. The simplest ("vanilla") RNN applies the same update equation at every timestep:

ht = tanh(Whht−1 + Wxxt + bh), y^t = Wyht + by

Here Wh ∈ R<sup>H×H</sup> , Wx ∈ R<sup>H×d</sup> , Wy ∈ R<sup>k×H</sup> , where H is the hidden size, d is the input dimension per timestep, and k is the output dimension. The nonlinearity is usually tanh or ReLU.

We fit the following parameters:

- Wx, which maps the current input xt into the hidden space

- Wh, which maps the previous hidden state ht−1 forward

- bh, which is the bias term for the hidden update

- Wy, which maps the hidden state to the output by, the bias for the output

There are three important properties:

1. Weight sharing across time: The same (Wh, Wx, Wy) are used at every timestep. This is analogous to a convolutional filter being applied at every spatial position.

2. Unbounded context (in principle): The hidden state ht can depend on arbitrarily distant past inputs through the recurrence, unlike a CNN whose receptive field is fixed by architecture.

3. Training is sequential: To compute ht you need ht−1, so forward and backward passes run step-by-step along the sequence. This is called backpropagation through time (BPTT). It means RNNs are harder to parallelize than CNNs, which compute all positions in a layer at once.

Vanishing/exploding gradients. When you backpropagate through many timesteps, the gradient is multiplied by Wh repeatedly. If the eigenvalues of Wh are less than 1 in magnitude, gradients shrink to zero over long sequences and the network cannot learn long-range dependencies. If greater than 1, gradients explode. LSTM and GRU cells are architectural modifications that add gating mechanisms to control information flow; they preserve gradients over much longer timescales and are what people actually use in practice. For this homework, "LSTM" and "GRU" can be treated as black-box drop-in replacements for the vanilla RNN that handle long sequences better.

Here are some rough rules of thumb for time series tasks:

|Property|CNN(1D)|RNN(LSTM/GRU)|
|---|---|---|
|Receptive field|fixed by architecture|unbounded (in principle)|
|Parallelism across<br>time|yes|no|
|Training speed|fast|slow|
|Good for|local patterns, fixed-scale<br>features|long-range dependencies, variable-<br>length sequences|


Modern practice often combines the two, using a CNN frontend for efficient local feature extraction, followed by an RNN (or transformer) for long-range integration. This is the architecture behind models like wav2vec 2.0 mentioned in lecture 23.

### Question 10 (2 points): parameter counting for an RNN

Consider a vanilla RNN with input dimension d = 10, hidden size H = 64, and output dimension k = 3 (the output is produced at every timestep).

(a) Compute the total number of trainable parameters in the RNN (include biases: one bias vector for the hidden state update, one for the output). Show each term.

(b) Compare to a 1D CNN with the same input dimension (d = 10 channels), 64 output channels, and kernel size 3 (no bias, for simplicity). How many parameters does the CNN have? What does the comparison tell you?

Your answer:

(a)

(b)

### Question 11 (3 points): When to use a RNN vs. a CNN?

For each of the following time series tasks, state whether you would start with a 1D CNN, an RNN (LSTM/GRU), or a hybrid (CNN frontend + RNN). Justify each answer in one or two sentences citing a specific property from the primer.

(a) Forecasting daily electricity demand 24 hours ahead, where the relevant patterns include weekly cycles (7 days) and annual cycles (365 days). You have one data point per hour.

(b) Detecting epilepsy related activity (also called interictal epileptiform discharges (IEDs)) in continuous intracranial EEG recordings from the brain. IEDs are stereotyped short (~100 ms) waveforms and the model should output a label per time window.

(c) Classifying full sentences of speech (variable length, several seconds, where wordlevel meaning depends on long-range context across the sentence) from audio waveforms.

Your answer:

(a)

(b)

(c)

```
In [ ]:
```

---

[← fc weight: 6410 = 640, bias: 10 -> 650](29-fc-weight-6410-640-bias-10---650.md) · [Up: contents](index.md)
