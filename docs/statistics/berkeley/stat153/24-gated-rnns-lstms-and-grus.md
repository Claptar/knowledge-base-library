---
title: "24. Gated RNNs: LSTMs and GRUs"
course: "Berkeley Stat 153"
chapter: 24
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 24. Gated RNNs: LSTMs and GRUs

## What this covers

This continues directly from the previous lecture's introduction to recurrent neural networks
(RNNs) and backpropagation through time (BPTT); it assumes you already have the basic recurrence
$h_t = f(x_t, h_{t-1})$ and the idea of unrolling it into a deep feedforward network for training.
The question here is: why does a plain RNN fail to learn dependence across long sequences, and
what structural change — gating — fixes it? The chapter works through the standard LSTM cell and
the simpler GRU, then follows the lecture to two places that change of subject was pointed at: what
the gates in a trained network end up representing, and where gated RNNs show up outside language
entirely, decoding brain signals into speech and text.

## The problem: why plain RNNs forget

Take a sentence a language model has to finish:

> *When she tried to print her **tickets**, she found that the printer was out of toner. She went
> to the stationery store to buy more toner. It was very overpriced. After installing the toner
> into the printer, she finally printed her* ________

The correct completion, *tickets*, was mentioned roughly 37 words earlier. Everything in between —
toner, printers, the price of toner — is a plausible-sounding distractor. A network that gets this
right has to carry the word "tickets" forward through about 37 steps of recurrence essentially
untouched, while not being derailed by 37 steps of topically related noise.

Plain RNNs are bad at exactly this. The failure has a name — **vanishing and exploding
gradients** — and it gets worse the longer the sequence backpropagation has to run across, which is
precisely why a simple RNN, trainable by BPTT, still has a real limit on how much temporal
dependence it can learn.

## Vanishing and exploding gradients, made explicit

Strip the recurrence down to one dimension to see why. Let $h_{t+1} = \sigma(wh_t)$ for a scalar
weight $w$ and nonlinearity $\sigma$ (tanh, sigmoid, maybe ReLU). Then

$$\frac{\partial h_{t+1}}{\partial h_t} = w\,\sigma'(wh_t).$$

Chaining this forward two steps,

$$\frac{\partial h_{t+2}}{\partial h_t} = w\sigma'(wh_{t+1})\cdot w\sigma'(wh_t),$$

and after $n$ steps,

$$\frac{\partial h_{t+n}}{\partial h_t} = w^n \prod_{j=0}^{n-1} \sigma'(wh_{t+j}).$$

This is the term backpropagation through time has to compute to let information 37 steps back
affect today's gradient, and it fails in two independent ways.

$w^n$ is, in the lecture's phrase, "really bad": if $|w|>1$ it grows exponentially in $n$
(illustrated on the slide with a plain exponential curve that runs into the hundreds within a
handful of steps); if $|w|<1$ it shrinks to zero just as fast. Either way the raw weight term alone
is enough to destabilize a long chain.

The product of derivatives is "also bad," independently of $w$. For the logistic sigmoid, the
derivative $\sigma'(x) = \sigma(x)(1-\sigma(x))$ is bounded above by $\tfrac14$, attained only at
$x=0$:

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="The logistic sigmoid and its derivative, showing the derivative never exceeds 0.25">
  <line x1="20" y1="170" x2="310" y2="170" stroke="currentColor" stroke-width="1"/>
  <polygon points="310,170 302,166 302,174" fill="currentColor"/>
  <text x="298" y="186" font-size="11" fill="currentColor">x</text>
  <line x1="20" y1="170" x2="20" y2="15" stroke="currentColor" stroke-width="1"/>
  <line x1="20" y1="132.5" x2="300" y2="132.5" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="205" y="128" font-size="11" fill="currentColor">max slope = 0.25</text>
  <polyline points="20,169.6 43.3,169.0 66.7,167.3 90,162.9 113.3,152.1 136.7,129.7 160,95 183.3,60.3 206.7,37.9 230,27.1 253.3,22.7 276.7,21.0 300,20.4" fill="none" stroke="currentColor" stroke-width="2"/>
  <polyline points="20,169.6 43.3,169.0 66.7,167.3 90,163.2 113.3,154.3 136.7,140.5 160,132.5 183.3,140.5 206.7,154.3 230,163.2 253.3,167.3 276.7,169.0 300,169.6" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="4,3"/>
  <text x="235" y="52" font-size="12" fill="currentColor">&#963;(x)</text>
  <text x="170" y="122" font-size="12" fill="currentColor">&#963;&#8242;(x)</text>
</svg>
<figcaption>The logistic sigmoid saturates at 0 and 1; its derivative peaks at $0.25$ at $x=0$ and is
smaller everywhere else. Every factor $\sigma'(wh_{t+j})$ in the chain-rule product is therefore at
most $0.25$, so the product over $n$ steps shrinks at least like $0.25^n$.</figcaption>
</figure>

So even in the best case, 37 such factors multiplied together are on the order of $4^{-37}$ —
indistinguishable from zero. The gradient that would tell the network "keep remembering *tickets*"
never arrives, so the weights that would let it happen never get a signal to become those weights.

## Fixing it: a highway for the cell state — the LSTM

The fix is architectural, not a better optimizer: give the recurrence a second, largely-linear
channel that state can travel along, and let the network learn, per time step, whether to keep,
overwrite, or read from it. This is the **long short-term memory** cell (LSTM), and the walkthrough
below follows the same diagrams as Christopher Olah's *Understanding LSTM Networks*, which the
lecture names as further reading.

Contrast the two repeating modules. A plain RNN's module is a single layer: concatenate $h_{t-1}$
and $x_t$, pass through one $\tanh$, and that is $h_t$. An LSTM's module has four interacting
layers, built around a **cell state** $C_t$ that runs alongside the hidden state. Reading the
diagram as equations, there are three sigmoid **gates** and one $\tanh$ **candidate**, each a
function of the same concatenated input $[h_{t-1}, x_t]$:

$$f_t = \sigma(W_f\cdot[h_{t-1},x_t]+b_f) \qquad\text{forget gate}$$

$$i_t = \sigma(W_i\cdot[h_{t-1},x_t]+b_i), \qquad \tilde C_t = \tanh(W_C\cdot[h_{t-1},x_t]+b_C) \qquad\text{input gate and candidate}$$

$$C_t = f_t \odot C_{t-1} + i_t \odot \tilde C_t \qquad\text{cell state update}$$

$$o_t = \sigma(W_o\cdot[h_{t-1},x_t]+b_o), \qquad h_t = o_t \odot \tanh(C_t) \qquad\text{output gate}$$

where $\odot$ is elementwise multiplication and each $\sigma$ output is a vector in $(0,1)$, one
entry per cell-state coordinate, acting as a per-coordinate switch. The forget gate decides how
much of the old cell state to erase; the input gate and candidate decide what new content to write
in; the output gate decides how much of the (squashed) cell state to expose as the hidden state.

The reason this fixes vanishing gradients is visible directly in the picture, not only in the
algebra: the update from $C_{t-1}$ to $C_t$ is one multiply and one add — no matrix multiply, no
squashing nonlinearity sitting on that path itself. A $\tanh$ appears only on the short side branch
that reads $C_t$ back out into $h_t$, once per step, not accumulated along the state:

<figure>
<svg viewBox="0 0 500 240" role="img" aria-label="The LSTM cell state as a highway modified only by pointwise gates">
  <defs>
    <marker id="lstm-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="40" y="42" width="415" height="16" fill="currentColor" fill-opacity="0.15"/>
  <line x1="40" y1="50" x2="455" y2="50" stroke="currentColor" stroke-width="2" marker-end="url(#lstm-arrow)"/>
  <text x="4" y="46" font-size="12" fill="currentColor">C(t-1)</text>
  <text x="462" y="46" font-size="12" fill="currentColor">C(t)</text>

  <circle cx="150" cy="50" r="9" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="145" y="54" font-size="11" fill="currentColor">&#215;</text>
  <line x1="150" y1="108" x2="150" y2="59" stroke="currentColor" stroke-width="1.5" marker-end="url(#lstm-arrow)"/>
  <rect x="128" y="86" width="44" height="22" fill="none" stroke="currentColor" stroke-width="1"/>
  <text x="136" y="101" font-size="11" fill="currentColor">f(t)</text>

  <circle cx="280" cy="50" r="9" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="275" y="54" font-size="12" fill="currentColor">+</text>
  <line x1="280" y1="108" x2="280" y2="59" stroke="currentColor" stroke-width="1.5" marker-end="url(#lstm-arrow)"/>
  <rect x="242" y="86" width="76" height="22" fill="none" stroke="currentColor" stroke-width="1"/>
  <text x="246" y="101" font-size="11" fill="currentColor">i(t) &#183; Ctilde</text>

  <line x1="380" y1="50" x2="380" y2="80" stroke="currentColor" stroke-width="1.5"/>
  <rect x="360" y="80" width="40" height="20" fill="none" stroke="currentColor" stroke-width="1"/>
  <text x="368" y="94" font-size="11" fill="currentColor">tanh</text>
  <line x1="380" y1="100" x2="380" y2="131" stroke="currentColor" stroke-width="1.5" marker-end="url(#lstm-arrow)"/>
  <circle cx="380" cy="140" r="9" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="375" y="144" font-size="11" fill="currentColor">&#215;</text>
  <line x1="418" y1="140" x2="391" y2="140" stroke="currentColor" stroke-width="1.5" marker-end="url(#lstm-arrow)"/>
  <rect x="418" y="129" width="40" height="22" fill="none" stroke="currentColor" stroke-width="1"/>
  <text x="428" y="144" font-size="11" fill="currentColor">o(t)</text>
  <line x1="380" y1="149" x2="380" y2="178" stroke="currentColor" stroke-width="1.5" marker-end="url(#lstm-arrow)"/>
  <text x="366" y="192" font-size="12" fill="currentColor">h(t)</text>

  <line x1="100" y1="215" x2="440" y2="215" stroke="currentColor" stroke-width="1"/>
  <text x="215" y="230" font-size="11" fill="currentColor">[h(t-1), x(t)]</text>
  <line x1="150" y1="215" x2="150" y2="108" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="280" y1="215" x2="280" y2="108" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="438" y1="215" x2="438" y2="151" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>
</svg>
<figcaption>The cell state runs left to right through only two pointwise operations per step —
multiply by the forget gate $f_t$, add the input gate's contribution $i_t\odot\tilde C_t$ — so a
gradient can cross many steps without passing through a squashing nonlinearity. The nonlinear
$\tanh$ only appears on the short side branch that reads $C_t$ out into $h_t$, gated by
$o_t$.</figcaption>
</figure>

Gradient with respect to $C_{t-1}$ only has to survive multiplication by $f_t$ at each step, and the
network can *learn* $f_t \approx 1$ for coordinates it needs to preserve — there is no forced
$\sigma'(\cdot)\le\tfrac14$ penalty sitting on that path the way there was for the plain recurrence.
This is the "constant error carousel" idea: a channel the gradient can ride across many steps
essentially unattenuated, with the gates deciding locally, at each step, whether to interrupt it.

## What the gates actually learn

Gating gives the network many independent memory slots — one per coordinate of $C_t$ — each with
its own learned read/write policy. Trained on raw character sequences, some of those slots turn out
to track something a person can name. The lecture's examples, from Andrej Karpathy's character-level
RNN visualizations:

- a cell **sensitive to position in a line** of text, firing in a pattern that tracks how far along
  the current line the network is, regardless of content;
- a cell that **turns on inside quotation marks** and off outside them;
- a cell, trained on C source code, that **robustly activates inside `if` statements**;
- but, the lecture is careful to add, **a large portion of cells are not easily interpretable** — a
  typical cell's activation pattern on the same text looks like noise to a human reader.

The moral: gating does not guarantee that memory is organized the way a person would organize it.
It guarantees only that the network *can* preserve a coordinate across many steps if doing so
reduces loss; some of the coordinates it ends up preserving happen to line up with concepts we
recognize, and most do not.

## GRUs: a leaner gate

The **gated recurrent unit** (GRU) is a simplification: it drops the separate cell state and merges
the forget and input gates into a single **update gate**, leaving one fewer interacting layer than
the LSTM's four.

$$r_t = \sigma(W_r\cdot[h_{t-1},x_t]) \qquad\text{reset gate}$$

$$z_t = \sigma(W_z\cdot[h_{t-1},x_t]) \qquad\text{update gate}$$

$$\tilde h_t = \tanh\bigl(W\cdot[r_t\odot h_{t-1},\,x_t]\bigr) \qquad\text{candidate}$$

$$h_t = (1-z_t)\odot h_{t-1} + z_t\odot \tilde h_t \qquad\text{new state}$$

The reset gate $r_t$ controls how much of the old hidden state is used when forming the candidate
$\tilde h_t$; the update gate $z_t$ then interpolates between keeping the old state outright
($z_t\approx 0$) and replacing it with the candidate ($z_t\approx 1$). That interpolation plays the
same role the forget/input pair played for the LSTM's cell state: the old state survives by a
controlled, elementwise, non-squashed combination rather than by surviving a full nonlinear
transform every step.

## From text to brain signals: gated RNNs as neural decoders

The lecture closes by pointing gated RNNs at a problem far from language modeling: reconstructing
intended speech or handwriting directly from recorded brain activity, in people who have lost the
ability to speak or write. All three examples shown are from work associated with the Chang lab at
UCSF, and all use a recurrent decoder for the same structural reason a language model does — the
signal is a long, noisy sequence, and what it means at each moment depends on context accumulated
over many previous moments.

- Anumanchipalli, Chartier & Chang, *"Speech synthesis from neural decoding of spoken sentences"*
  (*Nature* 568, 2019): an RNN decodes electrocorticography (ECoG) recordings taken while a
  participant spoke, and the decoded output drives a speech synthesizer.
- Willett, Avansino, Hochberg, Henderson & Shenoy, *"High-performance brain-to-text communication
  via handwriting"* (*Nature* 593, 2021): a participant attempts to handwrite, an intracortical
  array records motor cortex activity, and an RNN converts threshold-crossing features directly
  into a stream of character probabilities. Thresholding those probabilities online gives a fast
  but noisy character stream — the slide's example, prompted with *"you must be the change you
  wish to see in the world,"* comes back online as `you>must>be>the>change>you>wish>to>see>in>the>world`.
  Running the same probabilities offline through a Viterbi search against a language model corrects
  most of the remaining errors: character error rate fell across trial days from roughly 13% to a
  few percent raw, and to well under 1% with the offline language model, while typing speed rose
  from about 65 to about 95 characters per minute — well above the roughly 40 characters-per-minute
  benchmark of earlier intracortical BCIs marked as a reference line on the same plot.
- Littlejohn et al., *"A streaming brain-to-voice neuroprosthesis to restore naturalistic
  communication"* (*Nature Neuroscience* 28, 2025): in a participant with anarthria from a
  brainstem stroke, a single continuously-streaming decoder consumes 80 ms chunks of ECoG and
  drives both a streaming text language model and a streaming speech language model in parallel,
  producing text and synthesized speech together, chunk by chunk, as the neural activity arrives.
  The lecture's own diagram of this decoder is drawn as a chain of repeating recurrent modules —
  visually the same picture used earlier in the lecture to explain the LSTM.

A further demonstration, captioned only *"A high-performance neuroprosthesis for speech decoding
and avatar control"* (UCSF), was shown as a video in the lecture without an accompanying citation
slide in the source material.

The point of ending here: the architectural fix for vanishing gradients was motivated by language,
but nothing about gating is specific to language. Any sufficiently long, sufficiently noisy
sequential signal with the same "relevant information can be far in the past" structure is a
candidate for the same tool.

## Sources

- Slide deck: `26_RNNs_Part2.md` (Berkeley Stat153, Spring 2026, Lecture 26, Liberty Hamilton,
  30 April 2026), converted by a model from a PDF with no text layer (`route: llm`,
  `fidelity: reconstructed`). Text bullets on pp. 1–14 supply the recap, the day's topics, the
  further-reading list, the "trouble with RNNs" example, and the vanishing/exploding-gradient
  derivation. No transcript, notes, problem set, or exercises were supplied for this lecture (all
  empty in the task manifest), so there is no Exercises section here.
- The LSTM and GRU equations in this chapter are not present as text in the converted file — the
  PDF's text layer did not survive conversion for these slides. They are read directly off the
  labelled diagrams extracted as images, `26_RNNs_Part2/figures/p018-1.png` through `p044-2.png`,
  which reproduce the standard walkthrough from Christopher Olah's *Understanding LSTM Networks* —
  named on the slide's reading list but not itself supplied as an input file.
- The cell-interpretability examples (the line-position cell, the quote-detecting cell, the
  if-statement cell, and the "not easily interpretable" example) are reproduced from
  `p042-1.png`/`p043-1.png`, matching Andrej Karpathy's *The Unreasonable Effectiveness of
  Recurrent Neural Networks* — also named on the reading list, not itself supplied.
- The closing applications are the figures and citation cards on pp. 45–50 of the same file:
  the 2019 speech-synthesis citation on `p045`–`p047`; the handwriting decoding-pipeline figure on
  `p048-1.png` beside its citation on `p048-2.png`; the streaming brain-to-voice figure on
  `p049-1.png` beside its citation on `p049-2.png`; and the uncited avatar-control video still on
  `p050-1.jpeg`.
- Administrative announcements in the source (final exam date, office hours, Homework 5 policy,
  the lab schedule) are lecture logistics and are omitted here.

---

[← 23. Recurrent Neural Networks](23-recurrent-neural-networks.md) · [Contents](index.md) · [26. From Sinusoid to AR(2) →](26-from-sinusoid-to-ar-2.md)
