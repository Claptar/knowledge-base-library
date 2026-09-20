---
title: "3. The Lambda Phage Bistable Switch"
course: "MIT 8.591J 2004"
chapter: 3
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 3. The Lambda Phage Bistable Switch

## What this covers

This chapter follows the second half of Lecture 3 of MIT 8.591J (2004): how the lysis/lysogeny
decision made by bacteriophage $\lambda$ is turned into a testable mass-action model, and how the
single equation that model produces can be read for stability directly off a picture, without
solving it. It assumes the reader already has mass-action kinetics and the idea of a stable versus
unstable fixed point of a first-order ODE; nothing about the phage biology is assumed beyond what
is stated here.

## From a genetic decision to a reaction scheme

Phage $\lambda$, on infecting *E. coli*, either lyses the cell right away or integrates and sits
dormant (lysogeny); UV light can later flip a dormant lysogen back into lysis. That is the
biological decision the lecture sets out to model, following Hasty *et al.*

The reaction scheme is six steps, and the slide itself splits them into two groups by timescale:

**Fast (binding equilibria):**

$$2\text{X} \rightleftharpoons \text{X}_2 \qquad (K_1)$$

$$\text{D} + \text{X}_2 \rightleftharpoons \text{DX}_2 \qquad (K_2)$$

$$\text{D} + \text{X}_2 \rightleftharpoons \text{DX}_2^{*} \qquad (K_3)$$

$$\text{DX}_2 + \text{X}_2 \rightleftharpoons \text{DX}_2\text{DX}_2 \qquad (K_4)$$

Here X is the free repressor monomer, X$_2$ its dimer, D the operator DNA, DX$_2$ the dimer bound
at one operator site (OR2), DX$_2^{*}$ the dimer bound at a competing site (OR3), and
DX$_2$DX$_2$ the state where a second dimer has bound and looped the two operator sites together.

**Slow (synthesis and decay):**

$$\text{DX}_2 + \text{P} \xrightarrow{k_t} \text{DX}_2 + \text{P} + n\text{X}$$

$$\text{X} \xrightarrow{k_d} \text{A}$$

Polymerase P transcribes $n$ new copies of the monomer from the OR2-bound state, and the monomer
degrades. The slide calls the fast/slow split itself "the most important step in modeling": because
the four binding reactions equilibrate far faster than transcription and degradation, they can be
replaced by their mass-action equilibrium relations, collapsing the whole scheme to one slow ODE
for the free monomer.

## One equation, in dimensionless form

Eliminating the fast variables this way gives a single equation for the monomer level $x$, already
written in dimensionless, relative variables:

$$\frac{dx}{dt} = \frac{\alpha x^2}{1+(1+\sigma_1)x^2+\sigma_2 x^4} - \gamma x + 1$$

where

$$\sigma_1 = \frac{K_3}{K_2}, \qquad \sigma_2 = \frac{K_4}{K_2}$$

are relative binding constants (OR3 relative to OR2, and the looped complex relative to OR2), and

$$\alpha = \frac{n k_t p_0 d_T}{r} \sim \text{synthesis rate}/\text{basal rate}, \qquad
\gamma = \frac{k_d}{r\sqrt{K_1 K_2}} \sim \text{degradation rate}/\text{basal rate}$$

for some basal rate $r$. The lecture's point is the move as much as the result: choosing elegant,
dimensionless, relative variables is what turns six reactions and six rate constants into one
equation with two shape parameters ($\sigma_1,\sigma_2$) and two rate parameters ($\alpha,\gamma$).

The $x^4$ in the denominator is not decorative: it means the synthesis term eventually loses to the
denominator as $x$ grows, so it rises and then falls rather than simply saturating — the signature
of the looped, doubly-bound state DX$_2$DX$_2$ shutting transcription back down once $X_2$ becomes
abundant.

## Reading stability off a picture

Rather than solving the ODE, plot its two terms separately against $x$: "creation"
($\alpha x^2/(1+(1+\sigma_1)x^2+\sigma_2x^4) + 1$, the leaky synthesis term) and "destruction"
($\gamma x$, a straight line through the origin). Fixed points are the crossings, and their
stability follows from the direction of crossing alone: where creation falls from above the
destruction line to below it as $x$ increases, a perturbation is pulled back — stable. Where the
crossing runs the other way, a perturbation is pushed further away — unstable.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Creation curve and destruction line crossing three times, giving two stable states separated by one unstable state">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="45" y1="190" x2="315" y2="190" stroke="currentColor" stroke-width="1"/>
  <line x1="45" y1="190" x2="45" y2="20" stroke="currentColor" stroke-width="1"/>
  <text x="322" y="194" font-size="12" fill="currentColor">x</text>
  <text x="15" y="22" font-size="12" fill="currentColor">rate</text>

  <line x1="50" y1="190" x2="300" y2="40" stroke="currentColor" stroke-width="1.3"/>
  <text x="252" y="68" font-size="12" fill="currentColor">destruction</text>

  <polyline points="50,178 90,166 120,160 160,130 175,115 190,95 230,70 260,64 290,60 300,65"
            fill="none" stroke="currentColor" stroke-width="1.6"/>
  <text x="182" y="43" font-size="12" fill="currentColor">creation</text>

  <circle cx="90" cy="166" r="4" fill="currentColor"/>
  <circle cx="175" cy="115" r="4" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="260" cy="64" r="4" fill="currentColor"/>

  <line x1="163" y1="141" x2="122" y2="150" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>
  <line x1="187" y1="99" x2="228" y2="80" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow)"/>

  <text x="62" y="206" font-size="11" fill="currentColor">low x</text>
  <text x="266" y="206" font-size="11" fill="currentColor">high x</text>
</svg>
<figcaption>Medium degradation rate: creation and destruction cross three times. The two filled
points are stable; the open point between them is unstable, and the flow runs away from it toward
whichever stable state is nearer. Steepening the destruction line (raising the degradation rate)
leaves only the low crossing; flattening it leaves only the high crossing.</figcaption>
</figure>

Because $\gamma$ sets the slope of the destruction line, sweeping it sweeps the number of crossings:

- **High $\gamma$** (steep line): one crossing, at low $x$ — one stable low state.
- **Medium $\gamma$**: three crossings — two stable states separated by one unstable one. This is
  the bistable switch.
- **Low $\gamma$** (shallow line): one crossing, at high $x$ — one stable high state.

This is lysis versus lysogeny restated as a dynamical fact: bistability of $x$ (repressor level) is
the mathematical form of "the same phage genome can commit to two different fates," and $\gamma$ —
the degradation rate relative to synthesis — is the single parameter that moves the system between
the three regimes.

## Testing the model against something built, not found

The slide's own next question is how to check this against biology rather than just the algebra.
Its answer is synthetic biology: build the designed circuit from scratch in a cell, rather than
working only with the naturally occurring switch, and see whether it behaves as the model predicts.
It cites two examples of this done for related genetic switches:

- Isaacs *et al.*, "Prediction and measurement of an autoregulatory genetic module," *PNAS* **100**,
  7714 (2003).
- Gardner *et al.*, "Construction of a genetic toggle switch in *Escherichia coli*," *Nature*
  **403**, 399 (2000).

From there the slide turns to what building such a circuit requires, listing the toolbox of the
genetic engineer — restriction enzymes, plasmids, PCR, and fluorescent proteins — as the opening of
the next topic, without saying more about any of them.

## Sources

- Slides only: *MIT 8.591J Systems Biology* (Fall 2004), Lecture 3 summary,
  `computational-biology/mit-ocw/8591j-2004/lectures/04-notes.md`. No transcript, written notes, or
  exercises were supplied for this lecture.
- That file is itself a model-reconstructed conversion of a PDF with no text layer
  (`fidelity: reconstructed`); its own header warns that the prose is a paraphrase and every
  equation is unverified against the original slide. This chapter reproduces the reaction scheme,
  the governing ODE, and the graphical-stability discussion exactly as given there, and the diagram
  above redraws the stability-analysis figure on that same slide (three panels: high, medium, and
  low degradation rate) as a single medium-rate case, in the notation the slide uses ($\alpha$,
  $\gamma$, $\sigma_1$, $\sigma_2$).
- The two citations at the end (Isaacs *et al.* 2003; Gardner *et al.* 2000) are given on the slide
  itself and are not expanded on beyond the citation.
- The slide's closing list — restriction enzymes, plasmids, PCR, fluorescent proteins — is the
  start of the next lecture's material and is not developed further in this source.

---

[← 2. Cooperativity and the Lambda Switch](02-cooperativity-and-the-lambda-switch.md) · [Contents](index.md) · [4. Molecular vs Systems Biology →](04-molecular-vs-systems-biology.md)
