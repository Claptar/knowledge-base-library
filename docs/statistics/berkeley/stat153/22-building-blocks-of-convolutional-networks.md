---
title: "22. Building Blocks of Convolutional Networks"
course: "Berkeley Stat 153 Fall 2024"
chapter: 22
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 22. Building Blocks of Convolutional Networks

## What this covers

This is the second half of a two-part lecture on convolutional neural networks (CNNs). It asks
what a convolution's output value actually measures, why a convolution is always followed by a
nonlinearity, and what happens when the same operation is applied to a spectrogram-like time series
instead of an image. It then lays out the standard vocabulary of a CNN — convolution, activation,
pooling, flattening, dense layer — and works two small numerical examples (a template-matching
convolution and a pooling step) by hand. It assumes the definition of a 2D convolution, and of
padding and stride, from the first part of the lecture ("last time"), which this chapter does not
reproduce. The source slide deck for this lecture carries most of its content in images rather than
in extractable text (no transcript was available), so the figures described below are read directly
from the deck.

## Edge detection needs a nonlinearity

The lecture reopens with the two Sobel kernels used for edge detection, convolved with an image
$\mathbf{A}$ (a photo of a bike locked to a rack, in the slide's example):

$$\mathbf{G}_x = \begin{bmatrix} -1 & 0 & +1 \\ -2 & 0 & +2 \\ -1 & 0 & +1 \end{bmatrix} * \mathbf{A}
\qquad
\mathbf{G}_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ +1 & +2 & +1 \end{bmatrix} * \mathbf{A}$$

Applied to the photo, $\mathbf{G}_x$ (which differences across a row) lights up the vertical edges
— the vertical mortar lines between bricks, the bike's frame tubes — while $\mathbf{G}_y$
(differencing down a column) lights up the horizontal edges instead. Each kernel only finds edges
running in one direction.

Getting *all* the edges out of the two directional responses takes a **nonlinear** combination of
$\mathbf{G}_x$ and $\mathbf{G}_y$, not a linear one: an edge that gives a strongly negative response
in one filter and a strongly positive response in the other could cancel to near zero if the two
were simply added, even though there plainly is an edge there. The slide's combined image — edges
picked out in both directions at once, shown in white against black — is the result of such a
nonlinear combination. This is the same job a nonlinearity does inside a CNN generally: the
nonlinearity a CNN applies after (almost) every convolution is the **ReLU** (rectified linear unit),

$$\text{ReLU}(x) = \max(0, x),$$

flat at $0$ for negative input and the identity for non-negative input — it is what the slides list
as element 3 of a CNN, the "activation layer."

## Convolution as template matching

A convolution's output at one location is a single number: the elementwise product of the kernel
with the patch of the input it currently sits over, summed. Two of the deck's diagrams recall how
that sliding window interacts with the input's size: a $5\times 5$ input convolved with a $3\times
3$ kernel, no padding and stride $2$, produces a $3\times 3$ output; the same $5\times 5$ input with
"same" padding and stride $1$ produces a $5\times 5$ output — padding is chosen precisely so the
output matches the input's size when the stride is $1$.

What that single summed product *means* is shown with a worked arithmetic example. Take a $9\times
9$ input $X$ built from $\pm 1$ entries so that a diagonal "X" pattern runs through it, and a
$3\times 3$ kernel $K$ whose entries are $+1$ on the diagonal and $-1$ off it — the same pattern as
the top-left $3\times 3$ block of $X$. Lining $K$ up exactly over that block and taking the
elementwise product and sum gives

$$(+1)(+1) + (-1)(-1) + (-1)(-1) + (-1)(-1) + (+1)(+1) + (-1)(-1) + (-1)(-1) + (-1)(-1) + (+1)(+1) = 9,$$

the maximum possible score for a $\{-1,+1\}$ kernel and patch of this size, because every one of the
nine products comes out $+1$ — the kernel is a perfect match for the patch. Rotate the kernel by
$180°$ (anti-diagonal $+1$s instead of diagonal ones) and score it against the same patch, and only
one of the nine signs still agrees, giving a score of $+1$. A third kernel that agrees with the
patch everywhere except at the two off-diagonal corners scores $+5$, in between the other two. The
pattern is general: a convolution kernel is a *template*, and its output is large exactly where the
underlying patch matches the template's pattern of signs, and small or negative where it does not —
which is exactly why an edge-detecting kernel like $\mathbf{G}_x$ lights up at edges and stays quiet
elsewhere.

<figure>
<svg viewBox="0 0 460 210" role="img" aria-label="The same image patch scored against two kernels with the same nine plus-or-minus-one entries in different arrangements, giving a large score when the pattern matches and a small one when it does not">
  <rect x="10" y="10" width="66" height="66" fill="none" stroke="currentColor" stroke-width="1"/>
  <line x1="32" y1="10" x2="32" y2="76" stroke="currentColor" stroke-width="1"/>
  <line x1="54" y1="10" x2="54" y2="76" stroke="currentColor" stroke-width="1"/>
  <line x1="10" y1="32" x2="76" y2="32" stroke="currentColor" stroke-width="1"/>
  <line x1="10" y1="54" x2="76" y2="54" stroke="currentColor" stroke-width="1"/>
  <text x="21" y="25" text-anchor="middle" font-size="13" fill="currentColor">+</text>
  <text x="43" y="25" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="65" y="25" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="21" y="47" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="43" y="47" text-anchor="middle" font-size="13" fill="currentColor">+</text>
  <text x="65" y="47" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="21" y="69" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="43" y="69" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="65" y="69" text-anchor="middle" font-size="13" fill="currentColor">+</text>

  <text x="100" y="47" text-anchor="middle" font-size="18" fill="currentColor">&#215;</text>

  <rect x="140" y="10" width="66" height="66" fill="none" stroke="currentColor" stroke-width="1"/>
  <line x1="162" y1="10" x2="162" y2="76" stroke="currentColor" stroke-width="1"/>
  <line x1="184" y1="10" x2="184" y2="76" stroke="currentColor" stroke-width="1"/>
  <line x1="140" y1="32" x2="206" y2="32" stroke="currentColor" stroke-width="1"/>
  <line x1="140" y1="54" x2="206" y2="54" stroke="currentColor" stroke-width="1"/>
  <text x="151" y="25" text-anchor="middle" font-size="13" fill="currentColor">+</text>
  <text x="173" y="25" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="195" y="25" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="151" y="47" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="173" y="47" text-anchor="middle" font-size="13" fill="currentColor">+</text>
  <text x="195" y="47" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="151" y="69" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="173" y="69" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="195" y="69" text-anchor="middle" font-size="13" fill="currentColor">+</text>

  <text x="220" y="47" text-anchor="middle" font-size="18" fill="currentColor"≥</text>
  <text x="250" y="52" text-anchor="middle" font-size="20" fill="currentColor">9</text>
  <text x="285" y="47" text-anchor="start" font-size="12" fill="currentColor">aligned: large response</text>

  <rect x="10" y="120" width="66" height="66" fill="none" stroke="currentColor" stroke-width="1"/>
  <line x1="32" y1="120" x2="32" y2="186" stroke="currentColor" stroke-width="1"/>
  <line x1="54" y1="120" x2="54" y2="186" stroke="currentColor" stroke-width="1"/>
  <line x1="10" y1="142" x2="76" y2="142" stroke="currentColor" stroke-width="1"/>
  <line x1="10" y1="164" x2="76" y2="164" stroke="currentColor" stroke-width="1"/>
  <text x="21" y="135" text-anchor="middle" font-size="13" fill="currentColor">+</text>
  <text x="43" y="135" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="65" y="135" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="21" y="157" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="43" y="157" text-anchor="middle" font-size="13" fill="currentColor">+</text>
  <text x="65" y="157" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="21" y="179" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="43" y="179" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="65" y="179" text-anchor="middle" font-size="13" fill="currentColor">+</text>

  <text x="100" y="157" text-anchor="middle" font-size="18" fill="currentColor">&#215;</text>

  <rect x="140" y="120" width="66" height="66" fill="none" stroke="currentColor" stroke-width="1"/>
  <line x1="162" y1="120" x2="162" y2="186" stroke="currentColor" stroke-width="1"/>
  <line x1="184" y1="120" x2="184" y2="186" stroke="currentColor" stroke-width="1"/>
  <line x1="140" y1="142" x2="206" y2="142" stroke="currentColor" stroke-width="1"/>
  <line x1="140" y1="164" x2="206" y2="164" stroke="currentColor" stroke-width="1"/>
  <text x="151" y="135" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="173" y="135" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="195" y="135" text-anchor="middle" font-size="13" fill="currentColor">+</text>
  <text x="151" y="157" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="173" y="157" text-anchor="middle" font-size="13" fill="currentColor">+</text>
  <text x="195" y="157" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="151" y="179" text-anchor="middle" font-size="13" fill="currentColor">+</text>
  <text x="173" y="179" text-anchor="middle" font-size="13" fill="currentColor">-</text>
  <text x="195" y="179" text-anchor="middle" font-size="13" fill="currentColor">-</text>

  <text x="220" y="157" text-anchor="middle" font-size="18" fill="currentColor"≥</text>
  <text x="250" y="162" text-anchor="middle" font-size="20" fill="currentColor">1</text>
  <text x="285" y="157" text-anchor="start" font-size="12" fill="currentColor">rotated: weak response</text>
</svg>
<figcaption>The same 3×3 patch of ±1 entries scored against two kernels built from the same nine
entries in different arrangements. A convolution's output is an elementwise product summed to one
number, so it is large exactly when the kernel's sign pattern lines up with the patch's, and small
when it does not. Values from the lecture's worked example.</figcaption>
</figure>

## The same operation, applied to time: STRF and time-lagged regression

Convolution is not particular to images. The lecture makes this explicit with a figure from
auditory neuroscience: a **spectro-temporal receptive field** (STRF) is the set of coefficients
(the beta weights) of a *time-lagged regression* of a neuron's response onto a matrix of stimulus
features — and convolving that 2D STRF filter (time by feature) with the stimulus feature matrix is
exactly how the predicted response is produced. The figure shows this concretely: a top panel
plotting a neuron's actual response against the response predicted by convolving the STRF with the
stimulus over about 1.3 seconds, and a bottom panel showing the STRF itself as a heatmap over
phonetic features (plosive, fricative, nasal, voiced, and so on) against time, with a raster marking
when each phonetic feature actually occurred in the stimulus.

The point is that this is *the same computation* as the Sobel filter above, just running along a
different pair of axes — time and phonetic feature, rather than image row and column — which is why
time-lagged (distributed-lag) regression, covered earlier in the course, can be recast as a
convolution once it is written this way.

## The building blocks of a CNN

A convolutional neural network is built from a short, fixed list of layer types:

1. Input layer
2. Convolutional layer
3. Activation layer (introduces nonlinearity)
4. Pooling layer
5. Flattening
6. Fully connected (dense) layer
7. Output layer

The deck's canonical picture of this pipeline runs an image (a photo of a zebra, in the example)
through several rounds of convolution+ReLU followed by pooling; the small yellow square annotation
in the figure marks the same idea as the worked example above, that one entry of a feature map comes
from one kernel sitting over one patch of the layer below it. The diagram groups the stages into
three named blocks: **feature extraction** (the repeated convolution+ReLU+pooling rounds, which
produce the feature maps), **classification** (flattening the final feature maps into a vector and
passing them through fully connected layers), and a final **probabilistic distribution** — a softmax
layer turning the last layer's output into class probabilities (in the example, $0.2$ horse, $0.7$
zebra, $0.1$ dog).

## Pooling: summarizing a window with one number

A pooling layer reduces a feature map's spatial size by replacing each window of it — set by a
filter size and a stride — with one summary number. The deck computes both standard versions of
this by hand, on the same $4\times 4$ input, a $2\times 2$ filter, and stride $(2,2)$:

$$X = \begin{bmatrix} 2 & 2 & 7 & 3 \\ 9 & 4 & 6 & 1 \\ 8 & 5 & 2 & 4 \\ 3 & 1 & 2 & 6 \end{bmatrix}$$

**Max pooling** keeps the largest entry in each $2\times 2$ block:

$$\begin{bmatrix} 9 & 7 \\ 8 & 6 \end{bmatrix}$$

**Average pooling** keeps the mean of each block instead:

$$\begin{bmatrix} 4.25 & 4.25 \\ 4.25 & 3.5 \end{bmatrix}$$

(check the bottom-right block, $\{2,4,2,6\}$: its max is $6$ and its mean is $3.5$, matching both
matrices above.)

## Combining multiple filters, and from images to signals

Little text survives on the deck's "Combining multiple filters" slides beyond the heading, but the
pipeline figure already answers the question: a convolutional layer is not limited to one kernel. It
applies several in parallel, and each one produces its own feature map — which is why the stack of
feature maps in the pipeline diagram gets *deeper* (more maps) each time it goes through another
convolutional layer, even as each individual map keeps shrinking under pooling. Each map in the
stack is the output of a different learned template, in the sense worked out above; a layer with
many kernels is a layer that can respond to many different local patterns at once, rather than being
limited to the one pattern a single kernel matches.

The deck then reruns exactly this vocabulary on a input that is a signal in time rather than in
space: a raw audio waveform. One figure shows such a waveform directly; a second (labelled panel
"(a)" in the deck, without further attribution in the extracted material) lays out the full
architecture applied to it, using the same terms as above but now on a length-$32{,}000$ input:

- **Convolutional layer** — receptive field (kernel length) $80$, $256$ feature maps, output length
  $8{,}000$
- **Max pooling** — pooling length $4$, output length $2{,}000$
- **Convolutional layer** — receptive field $3$, $256$ feature maps, output length still $2{,}000$
- **Max pooling** — pooling length $4$, output length $500$
- **Global average pooling** — one summary number per feature map, output length $1$
- **Softmax** — $10$ classes

"Receptive field" here plays the same role as kernel size did for the 2D image kernels earlier, and
$256$ feature maps is the "combining multiple filters" idea above, scaled up: 256 different
length-$80$ (then length-$3$) templates run over the waveform in parallel at each layer.

## Sources

- Slide deck: *Lecture 24: Convolutional neural networks part 2*, Liberty Hamilton, Statistics 153
  (UC Berkeley, Spring 2026), April 23 2026 — `24_CNNs_Part2.pdf`, converted at
  `statistics/berkeley/stat153/spring-2026/public/lectures/24_CNNs_Part2.md`. The slide credits
  NeuroMatch Academy (Alona Fyshe) for some of the material.
- The PDF's text layer could not be recovered in conversion, so most of this chapter's content —
  the Sobel edge-detection images, the STRF figure, the CNN pipeline diagram, the pooling and
  template-matching worked examples, and the 1D audio architecture — is read directly from the
  slide deck's embedded figures (pages 2–4, 6–9, 13, and 28–33 of the source PDF) rather than from
  extracted text.
- No transcript, lecture notes, or problem set were supplied for this lecture; there is no
  Exercises section as a result.
- The "Example convolution operations (from last time)" slide, and the definitions of padding and
  stride it assumes, refer to the first part of this lecture ("Convolutional neural networks part
  1"), which is not among the supplied material.
- The panel-(a) architecture diagram for classifying a raw audio waveform is not identified further
  in the extracted material; it is presented here only as it is labelled in the deck.

---

[← 21. Convolutional Networks and Discrete Convolution](21-convolutional-networks-and-discrete-convolution.md) · [Contents](index.md) · [23. Recurrent Neural Networks →](23-recurrent-neural-networks.md)
