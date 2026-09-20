---
title: "18. Genetic Switch in Phage Lambda"
course: "MIT 8.591J 2004"
chapter: 18
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 18. Genetic Switch in Phage Lambda

## What this covers

This chapter sets up a single case study: how the decision between lysis and lysogeny in
bacteriophage $\lambda$ is modelled, in Hasty, Pradines, Dolnik and Collins, *Noise-based switches
and amplifiers for gene expression*, PNAS **97**, 2075–2080 (2000), as a bistable switch built from
one gene regulating itself. It assumes the equilibrium-binding and mass-action machinery from
earlier in the course — dissociation constants, cooperative binding of a dimer to DNA. The surviving
material covers the biological setup and the reaction scheme; it stops before the rate equation the
lecture set out to derive (see Sources).

## The autoregulatory loop at $P_{RM}$

The decision between the two phage lifestyles is controlled by the promoter $P_{RM}$, which drives
a single gene, *cI*. The *cI* gene product is a repressor protein that dimerizes and then binds back
to the operator DNA in front of its own gene, so the protein controls the transcription of its own
message — the loop that makes a switch possible at all.

The wild-type $\lambda$ operator has three binding sites (OR1, OR2, OR3); the model considered here
keeps only two of them. Hasty *et al.* assume that:

- occupying **OR2** turns transcription **on**,
- occupying **OR3** turns transcription **off**.

## The binding and production scheme

Writing $X$ for the repressor monomer, $D$ for the operator DNA, and $P$ for RNA polymerase, the
lecture's reaction scheme (its equation [III.1]) is

$$2X \rightleftharpoons_{K_1} X_2$$
$$D + X_2 \rightleftharpoons_{K_2} DX_2$$
$$D + X_2 \rightleftharpoons_{K_3} DX_2^{*}$$
$$DX_2 + X_2 \rightleftharpoons_{K_4} DX_2X_2$$
$$DX_2 + P \xrightarrow{k_t} DX_2 + P + nX$$

Reading it as a set of promoter states: the repressor first dimerizes ($K_1$), and the dimer $X_2$
then competes for the two sites — binding OR2 gives $DX_2$ (the transcriptionally active state),
binding OR3 gives the distinct complex $DX_2^{*}$ (silent), and a second dimer can occupy the
remaining site on top of $DX_2$ to give $DX_2X_2$ (both sites occupied, also silent). Only the
$DX_2$ state produces protein: the last line says that, whenever the promoter is in that state, RNA
polymerase turns out $n$ new copies of $X$ per transcription event, without $DX_2$ or $P$ being
consumed. Because a dimer, not a monomer, has to bind before transcription switches on, the
production rate is a nonlinear (cooperative) function of the repressor concentration rather than a
linear one — this is the ingredient the rest of the argument turns on.

## Reading a switch off a creation/destruction diagram

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Sigmoidal creation rate and linear destruction rate crossing three times, giving two stable states separated by one unstable state">
  <line x1="40" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="170" y="205" text-anchor="middle" font-size="12" fill="currentColor">x  (repressor concentration)</text>
  <text x="18" y="100" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 18 100)">rate</text>
  <line x1="55" y1="165" x2="270" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <text x="255" y="45" font-size="12" fill="currentColor">destruction</text>
  <path d="M 55 168 C 100 165, 130 150, 160 95 C 185 55, 220 42, 270 40" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="215" y="72" font-size="12" fill="currentColor">creation</text>
  <circle cx="70" cy="160" r="4.5" fill="currentColor"/>
  <circle cx="145" cy="116" r="4.5" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="242" cy="45" r="4.5" fill="currentColor"/>
  <line x1="125" y1="140" x2="95" y2="150" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="165" y1="98" x2="205" y2="72" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
</svg>
<figcaption>Creation rate (sigmoidal, from cooperative dimer binding) against destruction rate
(a straight line) as functions of repressor concentration $x$. Where the curves cross, production
balances loss: a fixed point. The two filled points are stable — the arrows show nearby
concentrations moving toward them — and the open point between them is unstable, so it is the
threshold that decides which stable state the system settles into.</figcaption>
</figure>

The same picture, drawn for different destruction rates, gives the three regimes shown in the
lecture: with a high destruction rate the curves cross only once, at a low value, and the system has
a single low steady state; with a low destruction rate they cross once at a high value, giving a
single high steady state; in between, for a medium destruction rate, they cross three times, giving
two stable states separated by the unstable one drawn above. That middle regime is the switch: which
of the two stable states the system ends up in depends on which side of the unstable point it starts
on, not on any change in the reaction rates themselves.

## Sources

- Transcript: `recordings/l3-syllabus-transcript.md` (MIT OCW 8.591J, 2004), section III, "A Genetic
  Switch in Lambda Phage" — the autoregulatory loop, the OR2/OR3 roles, and reaction scheme [III.1]
  all come from this fragment. **The transcript is a model's reconstruction of a PDF with no text
  layer** (flagged `fidelity: reconstructed` in the file), so the equations are unverified against
  the original, and the extracted text stops mid-equation right after scheme [III.1] — the lecture's
  stated goal, deriving Hasty *et al.*'s kinetic equation [7], is not present in what survived.
- Figure: `recordings/l3-syllabus-transcript/figures/p006-1.jpeg`, extracted from page 6 of the same
  source PDF (labels and captions read directly off the image). The lecture's own Figure 5 — a
  schematic of the promoter's bound/unbound states — is referenced in the text but its image link in
  the source is a placeholder, not the actual figure, so it is not reproduced here; the state
  labelling in "The binding and production scheme" above is read off the reaction scheme and the
  OR2/OR3 description instead.
- No slides, written notes or exercises were supplied for this chapter.

---

[← 17. Michaelis-Menten Kinetics and Cooperativity](17-michaelis-menten-kinetics-and-cooperativity.md) · [Contents](index.md) · [19. Linear Stability of Fixed Points →](19-linear-stability-of-fixed-points.md)
