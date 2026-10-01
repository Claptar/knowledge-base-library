---
title: "5. The Charge Environment of the Cell"
course: "MIT 8.592J"
chapter: 5
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 5. The Charge Environment of the Cell

## What this covers

This is the opening lecture of the structural half of the course. It states why the physics of
charge, not just sequence, has to enter the story of a biomolecule, and it introduces the two
pictures the course builds on: the electrostatic environment inside a cell, and the geometry for
computing the field of a charged membrane. It assumes only elementary electrostatics — Coulomb's
law and the idea of a surface charge density. The material supplied for this lecture is short — one
slide of text and two hand-drawn figures — and this chapter says only what they contain.

## From sequence to structure

The information a living system needs to reproduce itself is carried in the sequence of its
macromolecules. But that sequence only does anything once it is turned into a physical structure —
a folded protein, a wound strand of DNA, a bounded cell — and the forces that do the turning are
physical forces. Identifying which forces matter, and how they act, is the subject of this half of
the course.

## Coulomb interactions as the relevant force

Of the fundamental interactions, only the electromagnetic one matters at the scale of a cell:
gravity is far too weak, and the nuclear interactions do not reach beyond the nucleus of an atom.
So every force that shapes a macromolecule of life is some manifestation of the Coulomb interaction
between electrons and nuclei — the strong covalent bonds that hold together the primary chain of a
molecule, and the weaker hydrogen bonds. The slide's text breaks off mid-sentence immediately after
naming hydrogen bonds, so whatever the lecture went on to list — presumably further electrostatic
effects such as interactions between charged side groups, or effects mediated by the solvent — is
not part of the material supplied for this chapter.

## The charge environment of the cell

The first figure, captioned "the 'charge environment' of the cell is quite complicated," makes the
electrostatic picture concrete. A cell, bounded by its membrane, contains large charged molecules —
macroions — such as DNA and folded proteins. The figure sorts macroions into two kinds: an "acid,"
a macroion such as DNA whose backbone has given up protons and so carries a fixed negative charge,
and a "polyampholyte," a macroion such as a protein whose different side groups can carry positive
or negative charge, so that the molecule as a whole is a mix of both. Around a charged macroion,
small mobile ions of the opposite sign accumulate; the figure labels this local screening layer a
"neutralizing cloud." The rest of the cell's interior is not empty either: it holds dissolved salt
(the figure lists the cations Na⁺, K⁺, Mg²⁺ and the anion Cl⁻), which dissociates into free ions
that can move to screen any charge in the cell. The point of the figure is that a macromolecule's
charge is never isolated — it always sits inside a bath of mobile counterions and salt.

<figure>
<svg viewBox="0 0 360 240" role="img" aria-label="A charged macroion (DNA) and a polyampholyte (protein) inside a cell, surrounded by counterions and dissolved salt, bounded by the membrane">
  <line x1="30" y1="15" x2="30" y2="225" stroke="currentColor" stroke-width="2"/>
  <text x="12" y="12" font-size="11" fill="currentColor">membrane</text>
  <circle cx="128" cy="118" r="58" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <path d="M100,35 C122,65 80,95 100,125 C122,155 80,185 100,210" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="96" y="30" font-size="11" fill="currentColor">DNA (acid)</text>
  <text x="94" y="55" font-size="12" fill="currentColor">-</text>
  <text x="80" y="95" font-size="12" fill="currentColor">-</text>
  <text x="94" y="145" font-size="12" fill="currentColor">-</text>
  <text x="80" y="185" font-size="12" fill="currentColor">-</text>
  <circle cx="145" cy="70" r="7" fill="none" stroke="currentColor"/>
  <text x="142" y="74" font-size="10" fill="currentColor">+</text>
  <circle cx="150" cy="115" r="7" fill="none" stroke="currentColor"/>
  <text x="147" y="119" font-size="10" fill="currentColor">+</text>
  <circle cx="145" cy="165" r="7" fill="none" stroke="currentColor"/>
  <text x="142" y="169" font-size="10" fill="currentColor">+</text>
  <text x="95" y="222" font-size="11" fill="currentColor">neutralizing cloud</text>
  <ellipse cx="270" cy="85" rx="38" ry="26" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="255" y="80" font-size="12" fill="currentColor">+</text>
  <text x="278" y="95" font-size="12" fill="currentColor">-</text>
  <text x="234" y="122" font-size="11" fill="currentColor">protein</text>
  <text x="222" y="135" font-size="11" fill="currentColor">(polyampholyte)</text>
  <circle cx="250" cy="180" r="6" fill="none" stroke="currentColor"/>
  <text x="247" y="184" font-size="9" fill="currentColor">+</text>
  <circle cx="272" cy="195" r="6" fill="none" stroke="currentColor"/>
  <text x="269" y="199" font-size="9" fill="currentColor">-</text>
  <text x="230" y="215" font-size="11" fill="currentColor">salt: Na+, K+, Mg2+ / Cl-</text>
</svg>
<figcaption>The cell's charge environment: fixed negative charge on a macroion such as DNA (an
"acid"), a mixed-charge macroion such as a protein (a "polyampholyte"), each screened by a
neutralizing cloud of mobile counterions, all bathed in dissociated salt.</figcaption>
</figure>

## Setting up: a charged membrane

The second figure turns from this qualitative picture to a specific calculation. It is headed
"Solution for a membrane with a uniform surface charge," and gives the surface charge density as

$$\sigma = -\frac{e}{d^2},$$

a single electronic charge $-e$ spread over an area $d^2$. Above the plane it places a charge

$$q = Ze \equiv +e,$$

i.e. a singly-charged cation, at some height along a $y$-axis perpendicular to the membrane. This is
as far as the supplied material goes: the figure establishes the geometry — a uniformly charged
plane and a point charge held above it along $y$ — but the field or potential that the heading
promises is not part of the text or figure supplied for this lecture.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="A point charge held above a membrane carrying uniform surface charge density sigma">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <polygon points="40,150 280,150 250,172 10,172" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <text x="120" y="192" font-size="12" fill="currentColor">sigma = -e / d^2</text>
  <line x1="60" y1="150" x2="60" y2="25" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="66" y="30" font-size="12" fill="currentColor">y</text>
  <circle cx="150" cy="75" r="7" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="162" y="70" font-size="12" fill="currentColor">q = Ze = +e</text>
  <line x1="150" y1="82" x2="150" y2="150" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
</svg>
<figcaption>The geometry the source sets up: a plane carrying uniform surface charge density
sigma = -e/d^2, with a test charge q = Ze = +e held at height y above it. No field or potential is
given in the supplied material.</figcaption>
</figure>

## Sources

- Slides: `computational-biology/mit-ocw/8592j/lectures/09-slides.md`, "2 Structure", section
  2.1 "Coulomb interactions", together with both figures extracted from the same slide deck
  (`09-slides/figures/p002-1.png`, the cell's charge environment; `09-slides/figures/p005-1.png`,
  the charged-membrane geometry). This markdown is itself a model's reconstruction of a PDF slide
  deck that has no text layer, and its own banner flags that "every equation is unverified" and
  that the prose is a paraphrase in places; the running text is quoted here as supplied, and it
  breaks off mid-sentence after "...the weaker hydrogen bonds (" — the original lecture evidently
  continued past this point, but that content was not part of the material supplied for this
  chapter.
- No transcript, written notes, or exercises were supplied for this lecture.
- Course: MIT OpenCourseWare 8.592J, *Statistical Physics in Biology* (Spring 2011).

---

[← 4. Statistical Significance of Sequence Alignments](04-statistical-significance-of-sequence-alignments.md) · [Contents](index.md) · [6. Fluctuating and Interacting Polymers →](06-fluctuating-and-interacting-polymers.md)
