---
title: "16. Mass Spectrometry Basics for Proteomics"
course: "StatOmics Sga21"
chapter: 16
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 16. Mass Spectrometry Basics for Proteomics

## What this covers

This chapter is drawn from a guest lecture on mass-spectrometry (MS) based proteomics — the
physical measurement underlying the "-omics" data the rest of this course analyses statistically.
It answers two questions: how does a mass spectrometer turn a mixture of peptides into a spectrum,
and why is the intensity it reports a noisy, non-linear stand-in for "how much peptide was there"?
It closes by introducing peptide fragmentation and the naming convention used to read a sequence
back out of a fragment spectrum. It assumes only that a protein is a chain of amino-acid residues
joined end to end; no prior mass-spectrometry knowledge is assumed.

## Why look past the sequence at all

Genome sequencing gives a protein's primary structure — its sequence of residues (the lecture's
example: `...YSFVATAER...`) — but the sequence alone does not fix what the molecule does in a cell.
Proteomics is framed here as filling in the layers a sequence cannot show: secondary structure
(local structural elements), tertiary structure (the folded 3D shape), and two further layers that
are dynamic rather than fixed by the gene — modifications such as phosphorylation, which switch
function on and off, and processing: proteolytic events that target or activate a protein,
illustrated with trypsin and with platelet activity. Measuring the protein directly, at the level
mass spectrometry operates on, is how these layers become visible.

## Amino acids and the peptide bond

Amino acids differ considerably in their physico-chemical properties — size, charge,
hydrophobicity — and a protein backbone is built by joining them one at a time, losing a water
molecule between the amino group of one residue and the carboxyl group of the next:

$$\text{amino group} + \text{carboxyl group} \rightarrow \text{peptide bond} + \text{H}_2\text{O}$$

Repeating this reaction gives a chain with a free amino group at one end (the **N-terminus**) and a
free carboxyl group at the other (the **C-terminus**), with each residue's distinguishing side
chain ($R_1, R_2, \dots$) hanging off the backbone:

$$\text{H}_2\text{N}-\text{CH}(\text{R}_1)-\text{CO}-\text{NH}-\text{CH}(\text{R}_2)-\text{CO}-\dots-\text{COOH}$$

This directionality — a chain with a chemically distinct start and end — is what later lets a
fragment ion be labelled by *which* end of the peptide it came from.

## Anatomy of a mass spectrometer

A mass spectrometer is described as three functional parts plus a digitizer:

<figure>
<svg viewBox="0 0 620 180" role="img" aria-label="The four stages a sample passes through inside a mass spectrometer, from ion source to digitized spectrum">
  <defs>
    <marker id="arrow1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="5" y1="90" x2="35" y2="90" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow1)"/>
  <text x="20" y="80" text-anchor="middle" font-size="11" fill="currentColor">sample</text>

  <rect x="40" y="60" width="110" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="95" y="94" text-anchor="middle" font-size="12" fill="currentColor">ion source</text>
  <line x1="150" y1="90" x2="185" y2="90" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow1)"/>

  <rect x="190" y="60" width="120" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="250" y="86" text-anchor="middle" font-size="12" fill="currentColor">mass</text>
  <text x="250" y="100" text-anchor="middle" font-size="12" fill="currentColor">analyzer(s)</text>
  <line x1="310" y1="90" x2="345" y2="90" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow1)"/>

  <rect x="350" y="60" width="100" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="400" y="94" text-anchor="middle" font-size="12" fill="currentColor">detector</text>
  <line x1="450" y1="90" x2="485" y2="90" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow1)"/>

  <rect x="490" y="60" width="110" height="60" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="545" y="94" text-anchor="middle" font-size="12" fill="currentColor">digitizer</text>
</svg>
<figcaption>The generalized mass spectrometer: a sample is ionized, its ions are separated by
mass-to-charge ratio, arriving ions are recorded, and the analog detector signal is digitized into
the spectrum that gets plotted, with m/z on the x-axis and ion intensity (absolute or relative) on
the y-axis.</figcaption>
</figure>

- The **ion source** gets (some of) the sample's molecules into the gas phase and charged — without
  a charge, an analyte has no $m/z$ for the instrument to measure at all.
- One or more **mass analyzers** manipulate these gas-phase ions with electromagnetic fields to
  separate them by mass-to-charge ratio, $m/z$.
- The **detector** records the arrival of ions.
- The **digitizer** (analog-to-digital converter) turns the detector's continuous analog signal
  into the discrete, plotted spectrum.

## Ionizing peptides: MALDI and ESI

Two ion sources dominate proteomics, and they hand the mass analyzer very different populations of
ions.

**MALDI** (Matrix-Assisted Laser Desorption/Ionization) mixes the analyte with a light-absorbing
matrix and fires a pulsed UV laser at it (typically nitrogen, $\nu = 337\text{ nm}$); the resulting
desorption and proton transfer from matrix to analyte produce ions in the gas phase under high
vacuum. Peptides ionised this way are typically singly charged, and different analytes compete for
the available charge — competitive ionisation, part of why intensity is not simply proportional to
amount (see below). The name was coined by Karas and Hillenkamp (*Anal. Chem.*, 1985); Koichi
Tanaka received the 2002 Nobel Prize in Chemistry for demonstrating that MALDI could ionise
biological macromolecules (*Rapid Commun. Mass Spectrom.*, 1988).

**ESI** (Electrospray Ionization) instead nebulises the sample from a needle held at 3–5 kV and
heated to roughly $40$–$100^{\circ}\text{C}$; the resulting charged droplets evaporate, and either
undergo charge-driven fission or expel ions directly toward the analyzer inlet. ESI typically
produces multiply charged peptide ions ($2^+$, $3^+$, $4^+$). John Fenn shared the 2002 Nobel Prize
in Chemistry for demonstrating ESI on biological macromolecules (*Science*, 1989); the lecture adds
that the same physical process is used in fine-control thrusters on satellites and interstellar
probes.

## Resolving and detecting ions

**Resolution** is defined as the width of a peak at a given height — most often the width at 50% of
peak height, the *full width at half maximum* (FWHM); an alternative definition uses the
percent-valley height between two neighbouring peaks instead. Resolving power matters because a
peptide does not produce a single peak: its isotopes spread the signal over several peaks close in
$m/z$, so the same peptide has both a *monoisotopic mass* and a (slightly higher) *average mass*
depending on how much of that isotope envelope the instrument can resolve into distinct peaks
versus blur into one.

Detection in most instruments is by **electron multiplier**: a single incident ion striking the
first of several increasingly-charged dynodes triggers a cascade, each dynode boosting the electron
count (the lecture's example steps dynode voltages from $20\,\text{V}$ up to $120\,\text{V}$) until
a single incoming ion produces on the order of $10^6$ electrons out.

## Why an intensity is not an amount

The quantification principle is simple to state: detector signal relates to the quantity of analyte
present. Turning that into a usable number means, first, making each sample distinguishable —
either by introducing a mass difference between samples so they can be run together, or by running
each sample through the instrument as a separate experiment — then measuring, for each analyte, the
intensity of its signal in each sample, and finally processing the resulting numbers statistically.
The lecture illustrates this with mixtures combined at known ratios, such as $1{:}2$, $1{:}1$ and
$2{:}1$ — exactly the kind of comparison behind the error sources below.

Several things make the middle step, measuring intensity, harder than it sounds.

**Intensity is not comparable across peptides.** Different peptides ionise with different
efficiency, so one peptide's MS1 intensity says nothing about another's abundance; a given
peptide's intensity is informative only relative to that *same* peptide's intensity in another run
or sample.

**The detector response saturates.** Plotting the measured $\log_2$ ratio between two mixed samples
against the ratio they were actually mixed at (the expected $\log_2$ ratio), the response is linear
near $1{:}1$ but levels off as the true ratio becomes more extreme: the detector stops faithfully
tracking intensity once it is far enough from the middle of its dynamic range (Gevaert,
*Proteomics*, 2007).

**Error grows with the ratio.** Separately from that saturation, the percentage error on a measured
ratio between two peaks increases the further the ratio departs from $1{:}1$ (Vaudel, *Proteomics*,
2010) — and both effects, the lecture notes, remain clearly visible on modern Orbitrap instruments,
not only older ones.

**Peak-picking adds its own error.** Before a "peak" exists as a number at all, the raw digitized
signal has to be converted into a list of ($m/z$, intensity) values — a step that is
instrument-specific, sets the practical lower limit of the dynamic range (the signal-to-noise
ratio), and by itself often contributes a 5–10% error to the final ratios. That conversion has to
assume a peak shape: comparing peak-picking under three different mass windows ($0.02$, $0.04$,
$0.08\ \text{Da}$) against a mismatched, "non-adapted" shape model shows the wrong shape alone
adding on the order of another 10% error (Vaudel, *Proteomics*, 2010). Several software tools exist
for this step (the lecture names Decon2LS), and — its own phrase — "there's actually more to a peak
than just $m/z$", illustrated with the OpenMS TOPPView viewer, though the slide does not spell out
what that additional information is.

**The sample degrades before it is even measured.** Serum proteins continue to be degraded over
time after collection, regardless of the sampling tube used (Yi, *J. Proteome Res.*, 2007) — a
reminder that pre-analytical handling, not just instrument physics, is a source of error.

**Modifications are more pervasive than expected.** An open modification search (`ionbot`,
re-analysing the data behind Kim et al., *Nature*, 2014) finds a striking number of modified forms
even among six well-studied, highly abundant glycolytic enzymes — between 50 and 278 distinct
modified peptides per protein, and well over 100 distinct modifications on several of them
(glyceraldehyde-3-phosphate dehydrogenase, 166; pyruvate kinase PKM, 139; fructose-bisphosphate
aldolase A, 122; alpha-enolase, 121; triosephosphate isomerase, 117; phosphoglycerate kinase, 111),
spanning modification types from carbamylation and oxidation to succinylation and ammonia loss. A
search that only looks for the handful of modifications it was told to expect will miss most of
this.

## From spectrum to sequence: MS/MS and fragment ions

Identifying which peptide produced a spectrum relies on fragmenting it and reading the fragment
masses. **Tandem MS** does this with two mass analyzers used one after another (a single ion trap
can also do the whole job by itself): the first analyzer acts as an **ion selector**, passing only
ions at one chosen $m/z$ — the precursor; fragmentation is then triggered; and the second analyzer
records the $m/z$ of the resulting fragments, which the detector reads out as before. The pipeline
from the earlier figure gains an extra stage: source, then ion selector, then fragmentation, then
fragment mass analyzer, then detector.

Because the peptide backbone has a definite direction — N-terminus to C-terminus, from the section
above — a fragment ion is named by which terminus it retained and by how many residues it carries
from that terminus: fragments that keep the N-terminus are called $a$, $b$ or $c$ ions, and
fragments that keep the C-terminus are called $x$, $y$ or $z$ ions.

<figure>
<svg viewBox="0 0 480 170" role="img" aria-label="A single cleavage site along a peptide backbone, showing how the resulting N-terminal and C-terminal fragments are named">
  <text x="18" y="64" font-size="13" fill="currentColor">N</text>
  <text x="450" y="64" font-size="13" fill="currentColor">C</text>
  <line x1="40" y1="60" x2="400" y2="60" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="60" cy="60" r="4" fill="currentColor"/>
  <circle cx="120" cy="60" r="4" fill="currentColor"/>
  <circle cx="180" cy="60" r="4" fill="currentColor"/>
  <circle cx="240" cy="60" r="4" fill="currentColor"/>
  <circle cx="300" cy="60" r="4" fill="currentColor"/>
  <circle cx="360" cy="60" r="4" fill="currentColor"/>
  <line x1="270" y1="30" x2="270" y2="90" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <line x1="50" y1="95" x2="250" y2="95" stroke="currentColor" stroke-width="1.5"/>
  <text x="150" y="115" text-anchor="middle" font-size="12" fill="currentColor">a4, b4, c4</text>
  <line x1="290" y1="95" x2="370" y2="95" stroke="currentColor" stroke-width="1.5"/>
  <text x="330" y="115" text-anchor="middle" font-size="12" fill="currentColor">x2, y2, z2</text>
  <text x="270" y="145" text-anchor="middle" font-size="11" fill="currentColor">cleavage site</text>
</svg>
<figcaption>One cleavage site along a six-residue peptide backbone, splitting it into an
N-terminal fragment of four residues and a C-terminal fragment of two. The N-terminal fragment is
named a, b or c and indexed by how many residues it retains from the N-terminus; the C-terminal
fragment is named x, y or z and indexed from the C-terminus (Biemann nomenclature). A cleavage at
every other backbone position produces the rest of the ion ladder.</figcaption>
</figure>

Internal fragments — pieces that have lost both termini — can also appear and be interpreted, but
they don't fit this ladder scheme and are harder to use for reading a sequence directly off the
spectrum. This naming was introduced by Roepstorff and Fohlmann (*Biomed. Mass Spectrom.*, 1984)
and by Klaus Biemann (*Biomed. Environ. Mass Spectrom.*, 1988), and is commonly called the
**Biemann nomenclature** — the choice of letters deliberately follows the Roman alphabet in each
direction. In the ideal case, a full series of these ions — a complete ion ladder — lets the
peptide sequence be read directly off the gaps between consecutive peaks, each gap being the mass
of one residue.

The lecture's own material breaks off at exactly this point: the next slide promises to show what
that ideal ladder looks like, but only a single extracted label ("L") survives from it, and the
topics the deck's own table of contents promises after this one — database search algorithms,
sequential search algorithms, decoys and false discovery rate calculation, and protein inference —
are not present in the text this chapter was built from (see Sources).

## Sources

All of this chapter's content comes from a single guest lecture, "Science meets life: MS-based
proteomics data analysis" by Lennart Martens (Compomics, Ghent University / VIB), delivered within
the statOmics SGA21 course:
`docs/omics-statistics/statomics/sga21/docs/martens_proteomics_bioinformatics.md`, converted from
`martens_proteomics_bioinformatics.pdf` (statOmics/SGA21 repository, commit
`0ad787d4cc2bb2f4636440840a8a923cf6c09839`), licensed CC BY-NC-SA 4.0.

The source PDF had no extractable text layer, so it was reconstructed by a model reading the pages;
its own banner flags the prose as a paraphrase in places and every equation as unverified — the
same caveat carries over to the two chemical equations reproduced here (the peptide-bond reaction
and the backbone formula). No slide deck, transcript or exercise set was supplied separately for
this lecture — the reconstructed markdown is the entirety of the source material, and every section
above follows its slide-by-slide ordering. Figures extracted from the PDF are collected at the end
of the source file by page number, without captions tying them to a topic, and are not reproduced
here.

Named sources whose own content is not part of this chapter's material, only the claim they were
cited for:

- the NCBI Science Primer, for the levels-of-structure framing;
- Karas and Hillenkamp, *Anal. Chem.* (1985), and Tanaka, *Rapid Commun. Mass Spectrom.* (1988), for
  MALDI;
- Fenn, *Science* (1989), for ESI;
- Eidhammer, Flikka, Martens and Mikalsen (Wiley, 2007), for mass resolution;
- Roepstorff and Fohlmann, *Biomed. Mass Spectrom.* (1984), and Biemann, *Biomed. Environ. Mass
  Spectrom.* (1988), for fragment-ion nomenclature;
- Gevaert, *Proteomics* (2007), and Vaudel, *Proteomics* (2010), for the quantification-error
  figures;
- Yi, *J. Proteome Res.* (2007), for serum protein degradation; and
- Kim et al., *Nature* (2014), as the dataset behind the `ionbot` (https://ionbot.cloud) open
  modification search.

---

[← 15. Experimental design](15-experimental-design.md) · [Contents](index.md) · [17. Multiple Regression with Interactions →](17-multiple-regression-with-interactions.md)
