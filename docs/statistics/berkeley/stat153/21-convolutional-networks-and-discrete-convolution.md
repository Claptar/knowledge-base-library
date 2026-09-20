---
title: "21. Convolutional Networks and Discrete Convolution"
course: "Berkeley Stat 153 Fall 2024"
chapter: 21
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 21. Convolutional Networks and Discrete Convolution

## What this covers

This chapter opens the course's unit on convolutional neural networks (CNNs): what one is, why a
statistics course that has been doing time series would care, and the neuroscience and history that
motivated the architecture. It then works through the one piece of mathematics the lecture actually
defines precisely — the discrete convolution — including the worked numerical example from the
slides. It assumes familiarity with matrices and the idea of a feedforward neural network; nothing
here depends on having met a convolution before.

The lecture is labelled "Part 1", and it stops partway through explaining convolutional layers: the
outline promises pooling layers and "putting everything together" as well, but those belong to a
second lecture that was not supplied for this chapter. This chapter stops where the slides stop.

## Why a statistics course looks at convolutional networks

A CNN is a deep learning model built to process structured, grid-like data by learning a hierarchy
of spatial features rather than being handed hand-designed ones. The slides introduce it with a
standard picture of the whole pipeline: an image (a zebra, in the example) is passed through several
rounds of *convolution + ReLU* followed by *pooling*, each round producing a stack of smaller
"feature maps"; the last stack is flattened into a vector and fed to an ordinary fully connected
network, which ends in a softmax over the possible classes (in the example, probabilities of 0.2 for
horse, 0.7 for zebra, 0.1 for dog). The convolutional part is doing feature extraction; only the
fully connected part at the end is doing classification in the sense a plain neural network does.

Why does this belong in a time-series course? Convolutions capture regular patterns over an axis —
and that axis does not have to be space. It can be time. Convolutional layers scale well to long
sequences, and they are used as the front end of modern sequence models for audio (the slides name
WavLM, wav2vec 2.0, and HuBERT) before those sequences are handed to whatever comes next. The slides
also frame the underlying problem playfully as "Where's Waldo?": finding one small, fixed pattern
wherever it occurs in a much larger scene is exactly the problem a convolution is built to solve —
scan a small template across the whole input and record where it matches.

## The biological picture that motivates them

CNNs are explicitly modelled on an account of the visual system, and the lecture walks through it
before touching any mathematics.

**Orientation-selective cells.** Hubel and Wiesel's classic experiments (1968) recorded from single
neurons in visual cortex while showing a bar of light at different orientations. A given neuron
fires vigorously for a bar at one orientation and weakly or not at all as the bar is rotated away
from it — the cell is *orientation-selective*. That is the biological precedent for a convolutional
filter: a small, spatially localised template that responds strongly to one pattern and weakly to
others, checked against every position in the visual field rather than built specially for one.

**A hierarchy, not a single stage.** Rolls (2021) traces this idea up through the visual system:
from the retina and LGN, through V1, V2, V4, to TEO and TE. Two things change together as you move
up the hierarchy: the receptive field of a typical unit — how much of the visual field it responds
to — grows, and the representation moves from being tied to the exact retinal position and viewpoint
of a stimulus toward being *view-independent*. A companion diagram makes the mechanism for this
visible: at Layer 1 a wide, spatially distributed set of units is active; by Layer 4 that activity
has converged onto a much smaller, more localized set. Each layer pools the responses of many units
in the layer below into fewer, more abstract ones — which is exactly the pattern of alternating
convolution and pooling that a CNN uses to build up from raw pixels to something closer to "object
identity".

**What invariance buys you.** A further slide (citing Lipman et al., 2005) makes the target concrete
with photographs of a single carved wooden figure: the same object rotated, closely cropped versus
shown from further back, and lit warmly versus neutrally. Recognizing it as the same object across
all of these is the invariance the visual hierarchy is built to supply, and it is what weight-sharing
and pooling in a CNN are trying to buy back computationally: the same filter, reused at every spatial
position, and pooling that discards exactly where within a region a feature fired.

## Representation learning

The slides put a name on what all of this is doing: deep learning is fundamentally about
*representation learning*. A representation, in this sense, is a symbol that approximates the
entities and relations of the real world — and the reason a brain needs representations at all is
that it cannot literally contain the real world it is representing. A CNN's filters, on this view,
are not features an engineer chose; they are representations the network builds for itself.

## From handwritten digits to ImageNet: a short history

The lecture's history section is organized around one recurring theme: filters that used to be
designed by hand are learned instead, and once learned they often look like the biological ones
already described.

**Handwriting recognition.** The starting problem was mundane: collecting samples of handwriting —
digits and letters printed in boxes on a standard form — to train and test computer recognition of
hand-printed characters. This is the same underlying task LeNet was built for.

**LeNet (1998).** Developed by Yann LeCun at Bell Labs as an update of a 1989 network, LeNet-5 has
the following layer structure, alternating convolution ("C") with subsampling ("S"), and ending in
fully connected layers:

| Layer | What it is | Size |
| --- | --- | --- |
| Input | image | $32\times 32$ |
| C1 | convolution, 6 feature maps | $6@28\times 28$ |
| S2 | subsampling, 6 feature maps | $6@14\times 14$ |
| C3 | convolution, 16 feature maps | $16@10\times 10$ |
| S4 | subsampling, 16 feature maps | $16@5\times 5$ |
| C5 | full connection | 120 units |
| F6 | full connection | 84 units |
| Output | Gaussian connections | 10 units |

A *feature map* is "a set of units whose weights are constrained to be identical" — that is, the
same small filter is applied at every position of the layer below it, rather than each position
getting its own independently-trained weights. This weight-sharing is precisely the mechanism by
which a fixed pattern is recognized wherever it occurs, tying the architecture back to the invariance
argument above.

LeNet trained successfully with about 60,000 parameters and no GPU acceleration, was used to
automatically read zip codes on mail, and reached 0.8% error on MNIST (a set of handwritten digit
images) — near the state of the art at the time.

**ImageNet.** The next jump in scale is the ImageNet ILSVRC challenge: roughly 1000 categories, 1.2
million training images, 50,000 validation and 100,000 test images, at variable resolution, with the
task of classifying each image into one of the categories. This is the benchmark that the modern,
much deeper CNNs (starting with Krizhevsky et al.'s AlexNet, 2012) were built and evaluated on.

**Learned filters versus biology.** The slides put Krizhevsky et al.'s (2012) first-layer filters
next to Hubel and Wiesel's (1968) results directly: a network trained only to classify images, with
no instruction about edges or orientation, ends up learning filters that look like oriented edge
detectors and colour blobs — the same qualitative structure found in real V1 simple and colour cells.
Nobody designed those filters; the network reinvented them from data.

**Decoding brain activity with CNN features.** Horikawa and Kamitani (2017) go the other direction:
they use the layer-by-layer features of a trained CNN (alongside classical vision features such as
SIFT-plus-bag-of-features, GIST, and HMAX) as a candidate model of what the visual system itself
represents. Their pipeline: show a subject an object (or have them imagine one), record fMRI
activity, decode a predicted feature pattern from that activity, and match the predicted pattern
against category-average patterns (for categories such as "jet", "turtle", "leopard", "skyscraper",
"dolphin", "ostrich") to identify what the subject saw or imagined. A companion figure visualizes
what the learned filters at increasing depth respond to: early layers show simple oriented edges and
dots, and deeper layers show increasingly complex, sometimes semi-recognizable fragments.

## Structured data as arrays

Before defining the convolution operation itself, the slides fix some vocabulary for the data it
acts on. Images, sound clips, and other structured data can be stored as multi-dimensional arrays.
Some axes of that array have an ordering that matters — width versus height in an image, or time in
an audio signal — and one axis, the *channel axis*, is used to hold different "views" of the same
underlying data at each position: the red/green/blue channels of a colour image, or the left/right
channels of stereo audio.

## The discrete convolution

For an input matrix $X$ and a (smaller) kernel matrix $K$,

$$X = \begin{bmatrix} x_{11} & x_{12} & x_{13} & x_{14} \\ x_{21} & x_{22} & x_{23} & x_{24} \\ x_{31} & x_{32} & x_{33} & x_{34} \\ x_{41} & x_{42} & x_{43} & x_{44} \end{bmatrix}, \quad K = \begin{bmatrix} k_{11} & k_{12} & k_{13} \\ k_{21} & k_{22} & k_{23} \\ k_{31} & k_{32} & k_{33} \end{bmatrix},$$

the discrete convolution slides the kernel over every position of the input where it fits entirely,
and at each position takes the elementwise product of the kernel with the underlying patch of $X$
and sums it to a single number. With a $4\times 4$ input and a $3\times 3$ kernel, no padding, and a
stride of one position at a time, the kernel fits in

$$(4-3+1)\times(4-3+1) = 2\times 2$$

positions, so the output $Y$ is $2\times 2$. In general,

$$Y_{ij} = \sum_{m=1}^{3}\sum_{n=1}^{3} X_{i+m-1,\, j+n-1}\, K_{mn}.$$

The lecture then works this out position by position. At $(1,1)$, the kernel is aligned with the
top-left $3\times 3$ patch of the input:

$$Y_{11} = x_{11}k_{11} + x_{12}k_{12} + x_{13}k_{13} + x_{21}k_{21} + x_{22}k_{22} + x_{23}k_{23} + x_{31}k_{31} + x_{32}k_{32} + x_{33}k_{33}.$$

Sliding one column to the right, at $(1,2)$:

$$Y_{12} = x_{12}k_{11} + x_{13}k_{12} + x_{14}k_{13} + x_{22}k_{21} + x_{23}k_{22} + x_{24}k_{23} + x_{32}k_{31} + x_{33}k_{32} + x_{34}k_{33}.$$

Moving to the left edge, one row down, at $(2,1)$, the slide begins

$$Y_{21} = x_{21}k_{11} + x_{22}k_{12} + x_{23}k_{13} + \cdots$$

and the source breaks off there — the remaining six terms, and the fourth output value $Y_{22}$, are
not in the material supplied for this chapter, though the pattern for producing them is exactly the
one already shown twice above.

A second, fully numerical version of the same idea appears a few slides later, reproduced from
Dumoulin and Visin's guide to convolution arithmetic. There the input is $5\times 5$, the kernel is
$3\times 3$ with entries $\begin{bmatrix}0&1&2\\2&2&0\\0&1&2\end{bmatrix}$, and the resulting
$3\times 3$ output is shown below.

<figure>
<svg viewBox="0 0 460 200" role="img" aria-label="A 3x3 kernel slides over a 5x5 input to produce a 3x3 output; the highlighted input patch and output cell correspond to the same position">
<defs>
  <marker id="arrow22ec" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
  </marker>
</defs>
<path d="M 108 60 C 220 40, 260 40, 336 60" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow22ec)"/>
<text x="85" y="20" text-anchor="middle" font-size="12" fill="currentColor">input (5&#215;5)</text>
<rect x="20" y="34" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="34.0" y="52.0" text-anchor="middle" font-size="12" fill="currentColor">3</text>
<rect x="48" y="34" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="62.0" y="52.0" text-anchor="middle" font-size="12" fill="currentColor">3</text>
<rect x="76" y="34" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="90.0" y="52.0" text-anchor="middle" font-size="12" fill="currentColor">2</text>
<rect x="104" y="34" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="118.0" y="52.0" text-anchor="middle" font-size="12" fill="currentColor">1</text>
<rect x="132" y="34" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="146.0" y="52.0" text-anchor="middle" font-size="12" fill="currentColor">0</text>
<rect x="20" y="62" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="34.0" y="80.0" text-anchor="middle" font-size="12" fill="currentColor">0</text>
<rect x="48" y="62" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="62.0" y="80.0" text-anchor="middle" font-size="12" fill="currentColor">0</text>
<rect x="76" y="62" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="90.0" y="80.0" text-anchor="middle" font-size="12" fill="currentColor">1</text>
<rect x="104" y="62" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="118.0" y="80.0" text-anchor="middle" font-size="12" fill="currentColor">3</text>
<rect x="132" y="62" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="146.0" y="80.0" text-anchor="middle" font-size="12" fill="currentColor">1</text>
<rect x="20" y="90" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="34.0" y="108.0" text-anchor="middle" font-size="12" fill="currentColor">3</text>
<rect x="48" y="90" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="62.0" y="108.0" text-anchor="middle" font-size="12" fill="currentColor">1</text>
<rect x="76" y="90" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="90.0" y="108.0" text-anchor="middle" font-size="12" fill="currentColor">2</text>
<rect x="104" y="90" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="118.0" y="108.0" text-anchor="middle" font-size="12" fill="currentColor">2</text>
<rect x="132" y="90" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="146.0" y="108.0" text-anchor="middle" font-size="12" fill="currentColor">3</text>
<rect x="20" y="118" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="34.0" y="136.0" text-anchor="middle" font-size="12" fill="currentColor">2</text>
<rect x="48" y="118" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="62.0" y="136.0" text-anchor="middle" font-size="12" fill="currentColor">0</text>
<rect x="76" y="118" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="90.0" y="136.0" text-anchor="middle" font-size="12" fill="currentColor">0</text>
<rect x="104" y="118" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="118.0" y="136.0" text-anchor="middle" font-size="12" fill="currentColor">2</text>
<rect x="132" y="118" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="146.0" y="136.0" text-anchor="middle" font-size="12" fill="currentColor">2</text>
<rect x="20" y="146" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="34.0" y="164.0" text-anchor="middle" font-size="12" fill="currentColor">2</text>
<rect x="48" y="146" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="62.0" y="164.0" text-anchor="middle" font-size="12" fill="currentColor">0</text>
<rect x="76" y="146" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="90.0" y="164.0" text-anchor="middle" font-size="12" fill="currentColor">0</text>
<rect x="104" y="146" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="118.0" y="164.0" text-anchor="middle" font-size="12" fill="currentColor">0</text>
<rect x="132" y="146" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="146.0" y="164.0" text-anchor="middle" font-size="12" fill="currentColor">1</text>
<rect x="20" y="34" width="84" height="84" fill="orange" fill-opacity="0.15" stroke="orange" stroke-width="2"/>
<text x="388" y="40" text-anchor="middle" font-size="12" fill="currentColor">output (3&#215;3)</text>
<rect x="340" y="54" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="356.0" y="74.0" text-anchor="middle" font-size="12" fill="currentColor">12</text>
<rect x="372" y="54" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="388.0" y="74.0" text-anchor="middle" font-size="12" fill="currentColor">12</text>
<rect x="404" y="54" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="420.0" y="74.0" text-anchor="middle" font-size="12" fill="currentColor">17</text>
<rect x="340" y="86" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="356.0" y="106.0" text-anchor="middle" font-size="12" fill="currentColor">10</text>
<rect x="372" y="86" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="388.0" y="106.0" text-anchor="middle" font-size="12" fill="currentColor">17</text>
<rect x="404" y="86" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="420.0" y="106.0" text-anchor="middle" font-size="12" fill="currentColor">19</text>
<rect x="340" y="118" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="356.0" y="138.0" text-anchor="middle" font-size="12" fill="currentColor">9</text>
<rect x="372" y="118" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="388.0" y="138.0" text-anchor="middle" font-size="12" fill="currentColor">6</text>
<rect x="404" y="118" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1"/>
<text x="420.0" y="138.0" text-anchor="middle" font-size="12" fill="currentColor">14</text>
<rect x="340" y="54" width="32" height="32" fill="orange" fill-opacity="0.15" stroke="orange" stroke-width="2"/>
<text x="222" y="185" text-anchor="middle" font-size="11" fill="currentColor">kernel dotted with the highlighted patch gives the highlighted output value</text>
</svg>
<figcaption>The kernel occupies one $3\times 3$ patch of the input at a time; the highlighted patch and the highlighted output cell are the same sliding step. Moving the kernel to each of the nine valid positions fills in the rest of the $3\times 3$ output. Numbers are the worked example from Dumoulin and Visin's convolution-arithmetic guide, as shown in the lecture.</figcaption>
</figure>

## Padding

Later slides — present in the source only as figures, without accompanying reconstructed text —
extend the computation above with *padding*: an extra border, drawn in the source's diagrams as a
dashed outline around the input, added before the kernel is slid across it. Padding lets the kernel
be evaluated at positions that would otherwise run off the edge of the unpadded input, which is how
a convolution can produce an output the same size as its input rather than always shrinking it by
the $(-K+1)$ amount the no-padding formula above gives. The source does not state a formula for the
padded output size, so none is given here.

## What does a convolution actually pick out?

Two further worked examples from the (image-only) later slides make the abstract sum above concrete.

The first is a small binary image built from a repeated diagonal-stroke pattern, together with a
$3\times 3$ filter that is $+1$ along one diagonal and $-1$ everywhere else. Sliding this filter
across the image, several different patches line up with the filter's own diagonal pattern: at each
of those locations every term in the sum has the same sign, so the terms reinforce rather than
cancel and the output is large. Away from those locations, positive and negative products mix and
largely cancel. The slide highlights three separate locations in the image where this happens — the
same filter, applied at every position with the same weights, picks out the same local feature
wherever it occurs. This is the invariance argument from the biological section above, made
mechanical: one small template, reused everywhere, rather than a different detector built for every
location.

The second example applies a real, hand-designed filter pair — the Sobel operator — to a photograph
(a bicycle locked to a rack against a brick wall):

$$G_x = \begin{bmatrix} -1 & 0 & +1 \\ -2 & 0 & +2 \\ -1 & 0 & +1 \end{bmatrix} * A, \qquad G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ +1 & +2 & +1 \end{bmatrix} * A.$$

Convolving the photograph $A$ with $G_x$ and with $G_y$ produces two different edge-highlighted
versions of it, each sensitive to a different orientation of edge. This is a hand-designed filter
doing exactly the kind of thing the AlexNet first layer above learned to do on its own from data:
before any learning is involved, a fixed $3\times 3$ kernel already picks out a specific, meaningful
structure in an image. A CNN's contribution is to stop designing that kernel by hand and let training
choose its numbers instead.

## Sources

- Slides: `23_CNNs_Part1.md` ("Lecture 23: Convolutional neural networks", Liberty Hamilton, Berkeley
  STAT 153, April 21, 2026; credited in the slides to NeuroMatch Academy, Alona Fyshe). This is a
  model's reconstruction of a PDF with no text layer; the text in the source markdown breaks off
  mid-slide during the "Step by step" convolution walkthrough, and everything from there through the
  end of the deck exists in the source only as extracted page images, not as transcribed text.
  Administrative announcements (homework deadlines, course evaluations) have been cut.
- The convolution walkthrough, the LeNet architecture table, the Dumoulin and Visin figure, the
  Sobel-filter photograph, the diagonal-pattern filter example, the Hubel and Wiesel orientation-
  tuning figure, the Rolls (2021) visual-hierarchy diagrams, the Lipman et al. (2005) invariance
  photographs, the Krizhevsky et al. (2012) learned-filter figure, and the Horikawa and Kamitani
  (2017) decoding figure were all read directly from the page images embedded in that same source
  file (`23_CNNs_Part1/figures/`), since the slide text itself does not describe their contents.
- No transcript, lecturer notes, or problem set were supplied for this lecture.
- Not supplied, and referred to only by the outline on the "Outline" slide: the "pooling layers" and
  "putting everything together" parts of the lecture, which the outline promises but which are not
  present in this file — presumably covered in a "Part 2" that was not part of the input.

---

[← 20. The Kalman Filter and Smoother](20-the-kalman-filter-and-smoother.md) · [Contents](index.md) · [22. Building Blocks of Convolutional Networks →](22-building-blocks-of-convolutional-networks.md)
