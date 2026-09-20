---
title: "8. The Poland-Scheraga Melting Model"
course: "MIT 8.592J"
chapter: 8
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 8. The Poland-Scheraga Melting Model

## What this covers

Why does a DNA molecule, packed into a cell many orders of magnitude smaller than its own contour
length, come apart smoothly when heated in some cases and snap apart in others? This chapter treats
DNA as a polymer subject to two competing statistical-mechanical effects — the pairing energy of
the Watson–Crick bonds and the entropy gained by letting a strand flop around once it is freed of
its partner — and asks how those two effects, together with the geometry of closing a loop, decide
whether "melting" the double helix is a gentle crossover or a sharp phase transition. It assumes
the polymer-physics vocabulary built up earlier in the course: a chain as a random walk with a
persistence length, radius of gyration scaling, and the excluded-volume (self-avoiding walk)
exponent $\nu$.

## DNA in the cell: scale and packaging

DNA spans an enormous range of length scales: a $\lambda$-phage genome is about 50,000 monomers,
the human genome is $6\times10^9$, and the lily genome runs to $9\times10^{10}$ nucleotides — which,
stretched out, would be around thirty metres long. Treated as a random, non-self-avoiding chain
with persistence length $\xi_p \approx 50\ \text{nm}$, a chain of contour length $L$ has a typical
size $R_g \sim \sqrt{L\,\xi_p}$; for the human genome this comes to roughly $0.2\ \text{mm}$, and
excluded-volume effects only push that further out. All of these sizes dwarf a cell, which is why
DNA cannot simply sit inside one as an unconstrained coil: eukaryotes compactify it by wrapping the
chain around histone proteins to form nucleosomes, which are then packed together in turn.

## Melting the double helix

At the microscopic level the two strands are held together by Watson–Crick base pairs: G–C pairs,
with a binding energy of around $4k_BT$, bind roughly twice as strongly as A–T pairs. That binding
energy competes with an entropy cost — separating the two strands frees them to explore many more
configurations than they have while braided together — and the competition is temperature-dependent
in the usual way: at around $80^\circ\text{C}$ the entropy term wins enough of the free energy that
the double strand starts to unravel, or **denature** ("melt"), opening into bubbles where the two
strands have come apart locally. Because A–T pairs are weaker, A–T-rich regions open up at lower
temperature than G–C-rich regions. This shows up experimentally in ultraviolet absorbance versus
temperature: a short DNA molecule, with only a few possible melting domains, shows distinct blips as
each domain opens in turn; a very long, compositionally heterogeneous molecule has so many
overlapping melting events that the same measurement looks like one continuous curve. Software
exists that predicts, for a given sequence, how it will unravel as temperature is raised, by
computing a free energy from a model of the pairing energies (for instance summing stacking
energies between successive base pairs) together with the entropy cost of opening a bubble of a
given size.

## Loop-closure entropy

That entropy cost is observed to depend on the length $l$ of a denatured segment as

$$S(l) \approx bl + c\log l + d, \qquad c \approx 1.8\,k_B. \tag{2.71}$$

The extensive term $bl$ is just the number of configurations a flexible single strand gains per
added monomer; the logarithmic correction is the interesting piece, and it comes from **loop
closure**: the two single strands of a bubble of length $l$ each must still meet the double helix at
the same point in space at both ends, so the pair of them behaves like a closed loop of total length
$2l$, and closing a loop costs more than just being a free chain.

This can be made quantitative by first working out $\Omega(l)$, the number of configurations of a
bubble, for a non-self-avoiding (Gaussian) chain in $d$ spatial dimensions. Split the loop into two
independent strands of length $l$ that must arrive at the same displacement $\vec r$ from where they
started. If $W(\vec r,l)$ is the number of $l$-step configurations ending at $\vec r$, the loop of
total length $2l$, closed at a definite point $\vec r$, is counted by the product of the two halves,

$$W(\vec r, 2l) = W(\vec r, l)^2 = g_1^{2l}\exp\left[-\frac{dr^2}{2l\xi_p}\right]
\frac{1}{(4\pi l\xi_p/d)^{d}}, \tag{2.72}$$

where $g_1$ counts the configurations available per monomer to one flexible strand. Since the
bubble can close at any point in space, integrating over all positions of that meeting point gives

$$\Omega(l) = \int d^dr\, W(\vec r, 2l) = \left(\frac{d}{8\pi\xi_p}\right)^{d/2}\frac{g^l}{l^{c}},
\qquad g = g_1^2,\quad c = \frac{d}{2}. \tag{2.73}$$

So for an ideal chain the loop-closure exponent is simply $c=d/2$ — in three dimensions, $c=1.5$.

Real single strands are not ideal chains: they cannot cross themselves, so the relevant walk is
self-avoiding. Scaling arguments replace the Gaussian form with

$$W(\vec r, 2l) = \frac{g^l}{R^d}\,\Phi\!\left(\frac{\vec r}{R}\right), \qquad R\sim l^{\nu},
\qquad \Omega(l) = \frac{g^l}{l^{d\nu}}, \tag{2.74}$$

so that now $c = d\nu$. The exponent has an intuitive reading: with no closure constraint the free
end could sit anywhere in a volume $\sim R^d \propto l^{d\nu}$, and demanding that it come back to
meet the other end removes exactly that many choices, which is why $\Omega(l)$ picks up a factor of
$1/l^{d\nu}$ on top of the per-monomer weight $g^l$. In three dimensions, with the self-avoiding
exponent $\nu\approx0.588$, this gives $c=d\nu\approx1.76$ — close to the $c\approx1.8$ quoted from
melting-curve measurements above, which is a sign that a melted DNA strand behaves like a
self-avoiding chain rather than an ideal one, consistent with the excluded-volume effects already
mentioned. The ideal-chain result is the special case $\nu=1/2$.

<figure>
<svg viewBox="0 0 480 190" role="img" aria-label="A DNA chain drawn as alternating double-stranded rods and single-stranded melted bubbles">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="20" y1="90" x2="120" y2="90" stroke="currentColor" stroke-width="2"/>
  <line x1="30" y1="83" x2="30" y2="97" stroke="currentColor" stroke-width="1"/>
  <line x1="50" y1="83" x2="50" y2="97" stroke="currentColor" stroke-width="1"/>
  <line x1="70" y1="83" x2="70" y2="97" stroke="currentColor" stroke-width="1"/>
  <line x1="90" y1="83" x2="90" y2="97" stroke="currentColor" stroke-width="1"/>
  <line x1="110" y1="83" x2="110" y2="97" stroke="currentColor" stroke-width="1"/>
  <path d="M120,90 Q160,55 200,90" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M120,90 Q160,125 200,90" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="200" y1="90" x2="300" y2="90" stroke="currentColor" stroke-width="2"/>
  <line x1="210" y1="83" x2="210" y2="97" stroke="currentColor" stroke-width="1"/>
  <line x1="230" y1="83" x2="230" y2="97" stroke="currentColor" stroke-width="1"/>
  <line x1="250" y1="83" x2="250" y2="97" stroke="currentColor" stroke-width="1"/>
  <line x1="270" y1="83" x2="270" y2="97" stroke="currentColor" stroke-width="1"/>
  <line x1="290" y1="83" x2="290" y2="97" stroke="currentColor" stroke-width="1"/>
  <path d="M300,90 Q355,50 410,90" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M300,90 Q355,130 410,90" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="410" y1="90" x2="460" y2="90" stroke="currentColor" stroke-width="2"/>
  <line x1="420" y1="83" x2="420" y2="97" stroke="currentColor" stroke-width="1"/>
  <line x1="440" y1="83" x2="440" y2="97" stroke="currentColor" stroke-width="1"/>
  <line x1="22" y1="150" x2="118" y2="150" stroke="currentColor" stroke-width="1" marker-start="url(#arrow)" marker-end="url(#arrow)"/>
  <text x="70" y="168" text-anchor="middle" font-size="12" fill="currentColor">l1 (rod)</text>
  <line x1="122" y1="150" x2="198" y2="150" stroke="currentColor" stroke-width="1" marker-start="url(#arrow)" marker-end="url(#arrow)"/>
  <text x="160" y="168" text-anchor="middle" font-size="12" fill="currentColor">l2 (bubble)</text>
  <line x1="202" y1="150" x2="298" y2="150" stroke="currentColor" stroke-width="1" marker-start="url(#arrow)" marker-end="url(#arrow)"/>
  <text x="250" y="168" text-anchor="middle" font-size="12" fill="currentColor">l3 (rod)</text>
  <line x1="302" y1="150" x2="408" y2="150" stroke="currentColor" stroke-width="1" marker-start="url(#arrow)" marker-end="url(#arrow)"/>
  <text x="355" y="168" text-anchor="middle" font-size="12" fill="currentColor">l4 (bubble)</text>
  <line x1="412" y1="150" x2="458" y2="150" stroke="currentColor" stroke-width="1" marker-start="url(#arrow)" marker-end="url(#arrow)"/>
  <text x="435" y="168" text-anchor="middle" font-size="12" fill="currentColor">l5</text>
</svg>
<figcaption>The Poland–Scheraga picture: a chain as an alternating sequence of paired double-helix
rods, each contributing a weight $w^{l}$ per unit length, and open single-stranded bubbles, each
contributing $\Omega(l)\propto g^{l}/l^{c}$.</figcaption>
</figure>

## The Poland–Scheraga model

The Poland–Scheraga model treats a partly-melted DNA molecule exactly as the picture above suggests:
a sequence of alternating rods (still-paired double helix) and bubbles (open single strands), each
segment contributing its own statistical weight. A rod of length $l$ is energetically favoured and
has little entropy of its own, so it contributes a Boltzmann weight

$$w^l, \qquad w = e^{-\beta\epsilon} > 1 \quad (\epsilon < 0),$$

where $\epsilon$ is the (negative) pairing energy per base pair. A bubble of length $l$ is
entropically favoured instead, contributing the weight worked out above,

$$\Omega(l) \propto \frac{g^l}{l^{c}}, \qquad g>1,$$

with $g$ counting the configurations available to the flexible open strands and $c$ the
loop-closure exponent. The full partition function of an $N$-monomer chain is built by threading
these two kinds of segment along the contour in every possible way their lengths can sum to $N$ —
a renewal-type sum that is naturally handled with a generating function in a fugacity $z$ conjugate
to segment length. That algebra is not part of the material available for this chapter (see
Sources); what follows is the result it leads to.

## The order of the melting transition

The rod weight $w^l$, summed over $l$, has its own generating-function singularity at $z=1/w$; the
bubble weight, summed as $\Sigma(z) = \sum_l (gz)^l/l^{c}$, is controlled by the fixed point
$z=1/g$. As temperature rises, $\beta$ falls and so $w=e^{-\beta\epsilon}$ falls toward $1$, meaning
$1/w$ *rises* toward $1/g$. Whichever singularity sits closer to the origin dominates the chain's
free energy: below the temperature where $w=g$ the rod dominates and the chain is mostly paired;
above it the bubble sector takes over and the chain unravels. Whether the handover at $w=g$ is a
smooth crossover, a continuous transition, or an abrupt jump depends entirely on how $\Sigma(z)$
behaves as $z\to(1/g)^-$ — which is exactly the question of whether $\sum_l l^{-c}$ converges, i.e.
on the value of the loop exponent $c$:

- **$c\le1$.** $\Sigma(z)\to\infty$ as $z\to1/g$ (the harmonic-type sum diverges), so the bubble
  sector never "runs out" of weight to hand over gradually. There is no genuine singularity in the
  free energy at all — melting is a smooth crossover with no sharp temperature.
- **$1<c<2$.** $\Sigma(1/g)=\zeta(c)$ is now finite (the sum converges), but its derivative in $z$
  still diverges. The notes mark $\zeta(3/2)\approx2.612$ — the same constant that sets the
  condensation threshold of an ideal Bose gas, the same mathematics appearing here for the same
  reason: a sum over a power law that just barely converges. This is enough for a genuine,
  continuous phase transition at a melting temperature $T_m$ (given by $w(T_m)=g$), with the
  fraction of still-paired bases $\theta$ vanishing as
  $$\theta \propto (T_m - T)^{\beta}, \qquad \beta = \frac{2-c}{c-1}.$$
  The exponent is non-universal: it depends continuously on $c$ rather than being fixed once and
  for all.
- **$c>2$.** Now even $\sum_l l^{-(c-1)}$ converges, so $\Sigma(z)$ and its derivative are both
  finite at $z=1/g$ — nothing in the bubble sector is singular anywhere near the transition. With no
  singular behaviour available to soften the handover, the transition is forced to be first order:
  $\theta$ drops discontinuously at $T_m$.

<figure>
<svg viewBox="0 0 420 260" role="img" aria-label="Schematic order parameter theta versus temperature for the three ranges of the loop exponent c">
  <line x1="50" y1="220" x2="380" y2="220" stroke="currentColor" stroke-width="1.5"/>
  <line x1="50" y1="220" x2="50" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="388" y="230" font-size="12" fill="currentColor">T</text>
  <text x="30" y="22" font-size="12" fill="currentColor">&#952;</text>
  <line x1="45" y1="45" x2="50" y2="45" stroke="currentColor" stroke-width="1"/>
  <text x="30" y="49" font-size="11" fill="currentColor">1</text>
  <path d="M60,45 C 150,50 260,110 370,205" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="300" y="150" font-size="12" fill="currentColor">c &#8804; 1</text>
  <path d="M60,42 C 160,46 210,120 250,218" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="6 3"/>
  <line x1="250" y1="220" x2="250" y2="232" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
  <text x="225" y="245" font-size="11" fill="currentColor">Tm</text>
  <text x="130" y="185" font-size="12" fill="currentColor">1 &#60; c &#60; 2</text>
  <path d="M60,38 C 140,40 190,70 220,100" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="2 2"/>
  <circle cx="220" cy="100" r="3" fill="currentColor"/>
  <line x1="220" y1="103" x2="220" y2="220" stroke="currentColor" stroke-width="1" stroke-dasharray="2 2"/>
  <circle cx="220" cy="220" r="3" fill="none" stroke="currentColor"/>
  <text x="130" y="80" font-size="12" fill="currentColor">c &#62; 2</text>
  <text x="222" y="245" font-size="11" fill="currentColor">Tm&#8242;</text>
</svg>
<figcaption>How the paired-base fraction &#952; falls with temperature depends on the loop exponent
c: a smooth crossover for c &#8804; 1, a continuous transition &#952; &#8733; (T_m &#8722; T)^&#946;
for 1 &#60; c &#60; 2, and a discontinuous jump for c &#62; 2.</figcaption>
</figure>

Putting a number on this with the values already in hand: the marked example $c=3/2$ (the ideal,
non-self-avoiding value in three dimensions) gives $\beta=(2-1.5)/(1.5-1)=1$, a transition that
vanishes linearly. The measured, self-avoiding value $c\approx1.8$ instead gives
$\beta=(2-1.8)/(1.8-1)=0.25$ — still, strictly, a continuous transition, but a much steeper one,
close to the $c=2$ boundary beyond which it would become a discontinuous jump. Real DNA melting
therefore sits in the continuous regime, but only just, which is part of why melting curves for long
DNA can look almost as sharp as a true first-order transition even though they are not one.

## Sources

- Body text, Eqs. (2.71)–(2.74), and the section heading "2.4.1 The Poland–Scheraga model for DNA
  Denaturation" are from `lectures/16-slides.md` (course `computational-biology/mit-ocw/8592j`,
  lecture 16 slide file, "2.4 DNA structure" — MIT OCW 8.592J, *Statistical Physics in Biology*,
  Spring 2011, CC BY-NC-SA 4.0). That file is itself a model's reconstruction of a scanned PDF with
  no text layer and carries its own warning that the prose is paraphrase and every equation is
  unverified; the extracted text breaks off mid-sentence ("In practice, the crossover in behavior
  occurs") right after the Poland–Scheraga heading.
- The physical picture of alternating rods and bubbles, the statistical weights $w^l$ and
  $\Omega(l)\propto g^l/l^c$, and the definitions $g=g_1^2$, and the re-derivation of $c=d/2$
  (ideal) and $c=d\nu$ (self-avoiding), are read from the hand-written page
  `16-slides/figures/p002-1.png` — a scan headed "8.592, 3/21/07, Lec. 13 (1)" — cross-checked
  against Eqs. (2.72)–(2.74) in the slide text, which they match.
- The three-regime classification of the melting transition (smooth crossover for $c\le1$,
  continuous transition with $\beta=(2-c)/(c-1)$ for $1<c<2$, discontinuous jump for $c>2$), the
  marked constant $\zeta(3/2)\approx2.612$, and the comparison of $T_m$ at $c=1.8$ against $c=3/2$,
  are read from the hand-written page headed "Lec. 13 (4)", extracted twice as identical images
  `16-slides/figures/p005-1.png` and `16-slides/figures/p006-1.png`.
- The intermediate pages of that same hand-written derivation — the generating-function sum over
  rod and bubble segments that connects the weights on page (1) to the graphical results on page
  (4), which the lecture presumably worked through on pages (2)–(3) — were not extracted into the
  supplied file and so are not reconstructed here.
- No transcript, written notes, or exercises were supplied for this lecture.

---

[← 7. Coil-Globule Transition and Folding](07-coil-globule-transition-and-folding.md) · [Contents](index.md) · [9. RNA Secondary Structure and Melting →](09-rna-secondary-structure-and-melting.md)
