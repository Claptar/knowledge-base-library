---
title: "23. Recurrent Neural Networks"
course: "Berkeley Stat 153 Fall 2024"
chapter: 23
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 23. Recurrent Neural Networks

## What this covers

This chapter answers a specific design question: how do you build a model that predicts a value
$y_t$ from a history of inputs $x_t, x_{t-1}, x_{t-2}, \dots$ whose relevant length you don't know
in advance, without the number of parameters exploding as that history grows? The answer is the
recurrent neural network (RNN). It assumes the previous lecture's material on feed-forward and
convolutional networks, and ordinary backpropagation (forward pass, backward pass, chain rule).

## The problem: how far back does the input matter?

Take a concrete setting: you work at an investment bank and want to predict tomorrow's price of a
stock, $y_{t+1}$, from today's price $y_t$ and from other inputs $x_t$ you think are informative —
prices of other stocks, whether the company was in the news, and so on. The simplest model,
$y_t = f(x_t)$, uses only today's input. But you don't know, and don't want to commit in advance,
*when* an input matters: a move in another stock yesterday might affect today's price, or news
from two weeks ago might only matter once combined with news from yesterday. The honest model is

$$y_t = f(x_t, x_{t-1}, x_{t-2}, \dots),$$

an output that depends on an input history of unknown, and possibly unbounded, length. The question
of the lecture is how to express this as a neural network.

## Two fixes, and why both are unsatisfying

**Fix the window and go feed-forward.** If you believe there's a fixed horizon — say you only ever
need the last 20 days — you can concatenate the 21 vectors $\{x_{t-20}, \dots, x_t\}$ into one long
input vector and feed it to an ordinary feed-forward network. The problem is the weight count: if
each $x_t$ has length $n$, the first layer alone needs $21n \times m$ weights, where $m$ is the
width of that layer. If $n$ is large, this is already a disaster, and it only gets worse if you
decide the horizon should have been 40 days rather than 20.

**Use a 1D CNN instead.** Convolution cuts the weight count down a lot, because the same small
filter is reused at every position rather than learning a separate weight for every lag. But a
convolutional filter still has a fixed width, so you are still forced to commit to a window size —
and the amount of history that actually matters for a given sequence might be much longer, or might
vary from one part of the sequence to another.

Both fixes share the same flaw: they force you to decide, ahead of time, how far back to look.

## Recurrence

The fix is to stop trying to look back explicitly, and instead carry a summary of the past forward
one step at a time. Define a **hidden state** $h_t$ and write

$$h_t = g(x_t, h_{t-1}), \qquad y_t = f(h_t).$$

The output is a function of the hidden state; the hidden state is a function of the current input
and the hidden state from the previous time step. Unrolled across time, this looks like a deep
feed-forward network — in fact the lecture notes it looks like the state-space models seen earlier
in the course, with $h_t$ playing the role of the state — but with one crucial difference: **the
same weights are reused at every time step**, rather than each step (each unrolled "layer") getting
its own.

<figure>
<svg viewBox="0 0 460 200" role="img" aria-label="An RNN unrolled across three consecutive time steps, showing the hidden state passed forward and the same weights reused at every step">
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
</marker>
</defs>
<rect x="55" y="80" width="70" height="40" fill="none" stroke="currentColor"/>
<text x="90" y="104" text-anchor="middle" font-size="12" fill="currentColor">h(t-1)</text>
<rect x="195" y="80" width="70" height="40" fill="none" stroke="currentColor"/>
<text x="230" y="104" text-anchor="middle" font-size="12" fill="currentColor">h(t)</text>
<rect x="335" y="80" width="70" height="40" fill="none" stroke="currentColor"/>
<text x="370" y="104" text-anchor="middle" font-size="12" fill="currentColor">h(t+1)</text>
<text x="20" y="104" font-size="14" fill="currentColor">...</text>
<text x="430" y="104" font-size="14" fill="currentColor">...</text>
<line x1="30" y1="100" x2="53" y2="100" stroke="currentColor" marker-end="url(#arrow)"/>
<line x1="125" y1="100" x2="193" y2="100" stroke="currentColor" marker-end="url(#arrow)"/>
<text x="159" y="92" text-anchor="middle" font-size="11" fill="currentColor">W_h</text>
<line x1="265" y1="100" x2="333" y2="100" stroke="currentColor" marker-end="url(#arrow)"/>
<line x1="405" y1="100" x2="428" y2="100" stroke="currentColor" marker-end="url(#arrow)"/>
<line x1="90" y1="165" x2="90" y2="122" stroke="currentColor" marker-end="url(#arrow)"/>
<text x="90" y="180" text-anchor="middle" font-size="12" fill="currentColor">x(t-1)</text>
<line x1="230" y1="165" x2="230" y2="122" stroke="currentColor" marker-end="url(#arrow)"/>
<text x="230" y="180" text-anchor="middle" font-size="12" fill="currentColor">x(t)</text>
<text x="255" y="150" font-size="11" fill="currentColor">W_x</text>
<line x1="370" y1="165" x2="370" y2="122" stroke="currentColor" marker-end="url(#arrow)"/>
<text x="370" y="180" text-anchor="middle" font-size="12" fill="currentColor">x(t+1)</text>
<line x1="90" y1="78" x2="90" y2="35" stroke="currentColor" marker-end="url(#arrow)"/>
<text x="90" y="25" text-anchor="middle" font-size="12" fill="currentColor">ŷ(t-1)</text>
<line x1="230" y1="78" x2="230" y2="35" stroke="currentColor" marker-end="url(#arrow)"/>
<text x="230" y="25" text-anchor="middle" font-size="12" fill="currentColor">ŷ(t)</text>
<text x="255" y="55" font-size="11" fill="currentColor">W_y</text>
<line x1="370" y1="78" x2="370" y2="35" stroke="currentColor" marker-end="url(#arrow)"/>
<text x="370" y="25" text-anchor="middle" font-size="12" fill="currentColor">ŷ(t+1)</text>
</svg>
<figcaption>Unrolling the recurrence in time: the same weight matrices $W_h$, $W_x$, $W_y$ are
reused at every step, and only the hidden state $h_t$ carries a summary of the past forward.</figcaption>
</figure>

Because one set of weights is reused at every step, an RNN processes its input one time step at a
time rather than all at once — unlike a feed-forward or convolutional network — and it can in
principle carry information from arbitrarily far back, stored in $h_t$, rather than only from
within a fixed window.

## The vanilla RNN

The standard RNN — also called the **vanilla RNN** or the **Elman network** — instantiates $g$ and
$f$ as

$$h_t = \tanh(W_h h_{t-1} + W_x x_t + b_h), \qquad \hat{y}_t = W_y h_t + b_y,$$

with $W_h \in \mathbb{R}^{H \times H}$, $W_x \in \mathbb{R}^{H \times d}$, and
$W_y \in \mathbb{R}^{k \times H}$, where $H$ is the size of the hidden state, $d$ is the dimension
of the input at each time step, and $k$ is the dimension of the output. Note that the weight count
no longer depends on the length of the sequence at all — only on $H$, $d$, and $k$ — which is the
whole point relative to the concatenated feed-forward model above.

The example here uses a $\tanh$ nonlinearity. A sigmoid is also used sometimes; a ReLU, standard in
CNNs, is rare in RNNs.

## Training an RNN: backpropagation through time

**Ordinary backpropagation first.** A feed-forward network with $L$ layers is a composition of
differentiable functions, $h_\ell = f_\ell(h_{\ell-1}; W_\ell)$, ending in a loss
$\mathcal{L} = \text{Loss}(\hat{y}, y)$. Training by gradient descent needs
$\partial \mathcal{L}/\partial W_\ell$ for every layer $\ell$, and this is computed in two passes:

- **Forward pass:** compute and cache $h_1, h_2, \dots, \hat{y}$, then the loss.
- **Backward pass:** starting from $\partial \mathcal{L}/\partial \hat{y}$, walk backward through
  the layers, applying the chain rule at each one:
  $$\frac{\partial \mathcal{L}}{\partial W_\ell} = \frac{\partial \mathcal{L}}{\partial h_\ell} \cdot \frac{\partial h_\ell}{\partial W_\ell}, \qquad \frac{\partial \mathcal{L}}{\partial h_{\ell-1}} = \frac{\partial \mathcal{L}}{\partial h_\ell} \cdot \frac{\partial h_\ell}{\partial h_{\ell-1}}.$$
  The first term is the gradient used to update $W_\ell$; the second is the upstream gradient
  passed on to the previous layer.

**Backpropagation through time (BPTT)** is mostly the same recipe applied to the unrolled RNN,
which is, after all, a deep feed-forward network — but with two twists. First, the same parameters
$W_h$ and $W_x$ are reused at every time step, so the total gradient with respect to $W_h$ is a sum
over all the places it was used:

$$\frac{\partial \mathcal{L}}{\partial W_h} = \sum_{t=1}^T \frac{\partial \mathcal{L}_t}{\partial W_h}.$$

Second, each term in that sum requires propagating the gradient back through every earlier time
step, via repeated multiplication by $\partial h_t / \partial h_{t-1}$. This raises a question that
an ordinary feed-forward network never has to answer: where do you stop? A fixed network has a
fixed number of layers to backpropagate through; an RNN's history is, in principle, unbounded.

The practical answer is **truncated BPTT**: instead of propagating gradients back forever, fix a
BPTT length $k$ and only back-propagate $k$ time steps. This is so much the default that it is
rarely even called "truncated BPTT" — in practice, people just call it BPTT.

## Why recurrence instead of convolution

Set against the CNN from the previous lecture, the RNN's distinguishing features are:

- it allows a **variable-length context**, rather than a context fixed by a filter width;
- it assumes **order matters** — the opposite assumption from a CNN, which is built around
  translation invariance in time;
- it processes **one time step at a time**, which is a more natural fit for online inference, where
  inputs arrive one at a time and a prediction is wanted immediately.

## RNN variants: going deeper and looking both ways

**Stacked RNNs.** If the relationship between $x_t$ and $y_t$ is complicated, a single hidden
recurrence may not be expressive enough — the same problem a single-layer feed-forward network has
against a three-layer one. The fix is the same: stack recurrent layers, feeding the hidden state of
one into the next:

$$h_t^1 = g(x_t, h_{t-1}^1), \qquad h_t^2 = g(h_t^1, h_{t-1}^2), \qquad y_t = f(h_t^2).$$

**A worked example: part-of-speech tagging.** Consider tagging the words of "It was a stray puppy"
with their part of speech, reading left to right with a single (possibly stacked) RNN. The tagger
gets "It / Pro", "was / VB", "a / Det" right, but tags "stray" as a noun (NN) — reading only from
the left, "a stray" looks like a determiner followed by a noun, and the model has not yet seen
"puppy". That is wrong: "stray" is an adjective (JJ) modifying "puppy".

The missing information is *later* in the sentence. A **bidirectional RNN** runs a second RNN over
the sequence in reverse and concatenates the forward and backward hidden states at each position
before producing a tag. With the backward pass supplying the context of "puppy", the tag for
"stray" is corrected to JJ.

<figure>
<svg viewBox="0 0 400 210" role="img" aria-label="A bidirectional RNN reading a sentence forward and backward and concatenating both hidden states at each word to tag it">
<defs>
<marker id="arrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
</marker>
</defs>
<text x="40" y="15" text-anchor="middle" font-size="12" fill="currentColor">It</text>
<text x="120" y="15" text-anchor="middle" font-size="12" fill="currentColor">was</text>
<text x="200" y="15" text-anchor="middle" font-size="12" fill="currentColor">a</text>
<text x="280" y="15" text-anchor="middle" font-size="12" fill="currentColor">stray</text>
<text x="360" y="15" text-anchor="middle" font-size="12" fill="currentColor">puppy</text>
<circle cx="40" cy="50" r="12" fill="none" stroke="currentColor"/>
<circle cx="120" cy="50" r="12" fill="none" stroke="currentColor"/>
<circle cx="200" cy="50" r="12" fill="none" stroke="currentColor"/>
<circle cx="280" cy="50" r="12" fill="none" stroke="#d9782d" stroke-width="2"/>
<circle cx="360" cy="50" r="12" fill="none" stroke="currentColor"/>
<line x1="52" y1="50" x2="108" y2="50" stroke="currentColor" marker-end="url(#arrow2)"/>
<line x1="132" y1="50" x2="188" y2="50" stroke="currentColor" marker-end="url(#arrow2)"/>
<line x1="212" y1="50" x2="268" y2="50" stroke="currentColor" marker-end="url(#arrow2)"/>
<line x1="292" y1="50" x2="348" y2="50" stroke="currentColor" marker-end="url(#arrow2)"/>
<text x="200" y="40" text-anchor="middle" font-size="11" fill="currentColor">forward RNN</text>
<circle cx="40" cy="130" r="12" fill="none" stroke="currentColor"/>
<circle cx="120" cy="130" r="12" fill="none" stroke="currentColor"/>
<circle cx="200" cy="130" r="12" fill="none" stroke="currentColor"/>
<circle cx="280" cy="130" r="12" fill="none" stroke="#d9782d" stroke-width="2"/>
<circle cx="360" cy="130" r="12" fill="none" stroke="currentColor"/>
<line x1="108" y1="130" x2="52" y2="130" stroke="currentColor" marker-end="url(#arrow2)"/>
<line x1="188" y1="130" x2="132" y2="130" stroke="currentColor" marker-end="url(#arrow2)"/>
<line x1="268" y1="130" x2="212" y2="130" stroke="currentColor" marker-end="url(#arrow2)"/>
<line x1="348" y1="130" x2="292" y2="130" stroke="currentColor" marker-end="url(#arrow2)"/>
<text x="200" y="150" text-anchor="middle" font-size="11" fill="currentColor">backward RNN</text>
<line x1="40" y1="62" x2="40" y2="118" stroke="currentColor" stroke-dasharray="2,2"/>
<line x1="120" y1="62" x2="120" y2="118" stroke="currentColor" stroke-dasharray="2,2"/>
<line x1="200" y1="62" x2="200" y2="118" stroke="currentColor" stroke-dasharray="2,2"/>
<line x1="280" y1="62" x2="280" y2="118" stroke="#d9782d" stroke-width="2" stroke-dasharray="2,2"/>
<line x1="360" y1="62" x2="360" y2="118" stroke="currentColor" stroke-dasharray="2,2"/>
<text x="40" y="195" text-anchor="middle" font-size="12" fill="currentColor">Pro</text>
<text x="120" y="195" text-anchor="middle" font-size="12" fill="currentColor">VB</text>
<text x="200" y="195" text-anchor="middle" font-size="12" fill="currentColor">Det</text>
<text x="280" y="195" text-anchor="middle" font-size="12" fill="#d9782d" font-weight="bold">JJ</text>
<text x="360" y="195" text-anchor="middle" font-size="12" fill="currentColor">NN</text>
</svg>
<figcaption>Tagging "It was a stray puppy": a forward-only reader has not yet seen "puppy" when it
tags "stray", and calls it a noun (NN). Concatenating in the backward hidden state, which has
already seen "puppy", corrects the tag to an adjective (JJ).</figcaption>
</figure>

**Gated RNNs** are a third variant — the lecture flags them as next time's topic and does not
cover them in this one.

## Sources

- Slides: `statistics/berkeley/stat153/spring-2026/public/lectures/25_RNNs_Part1.md` (Lecture 25,
  "Recurrent neural networks", Liberty Hamilton, April 28 2026), all sections — "Time Series
  Prediction" through "RNN Variants". This file is itself a model's reconstruction of a PDF slide
  deck with no extractable text layer (`route: llm`, `fidelity: reconstructed`); its own banner
  warns that the prose is paraphrased in places and every equation is unverified against the
  original slides, so the equations above should be checked against the source PDF
  (`25_RNNs_Part1.pdf`) before being relied on for anything graded.
- No transcript, written notes, or exercises were supplied for this lecture, so there is no
  worked derivation, motivating aside, or problem set to draw on beyond what the slides state
  directly, and no `## Exercises` section is included.
- The lecture explicitly defers **gated RNNs** to the following lecture; that material is not in
  this chapter's source and is not covered here.
- The slides' images (`25_RNNs_Part1/figures/*.png`) are decorative background-colour extracts
  from the PDF conversion, not diagrams with content, and were not used as a source for this
  chapter; the figures here were constructed from the slides' prose and equations instead.

---

[← 22. Building Blocks of Convolutional Networks](22-building-blocks-of-convolutional-networks.md) · [Contents](index.md) · [24. Gated RNNs: LSTMs and GRUs →](24-gated-rnns-lstms-and-grus.md)
