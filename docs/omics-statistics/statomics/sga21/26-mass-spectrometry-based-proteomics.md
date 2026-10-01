---
title: "26. Mass Spectrometry-Based Proteomics"
course: "StatOmics Sga21"
chapter: 26
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 26. Mass Spectrometry-Based Proteomics

## What this covers

Mass spectrometry (MS) is the instrument behind essentially every large-scale protein measurement,
and before any statistics can be applied to proteomics data it helps to know what the machine
actually measures, and where its numbers already go wrong before a statistician sees them. This
chapter follows a peptide from the sample tube to a spectrum: how a mass spectrometer turns
molecules into a signal, why that signal is not a simple readout of abundance, and how a second
round of fragmentation ("MS/MS") turns a peptide's mass into information about its sequence. It
assumes only the ordinary chemistry of amino acids and peptide bonds — no statistics background is
needed, since the point of the chapter is to hand the statistics that follow a target worth being
careful about.

The lecture's own outline promises more after this: how a fragment spectrum is matched against a
protein database, how that search is done efficiently, how decoys are used to control a false
discovery rate, and the problem of inferring which protein a shared peptide came from. The material
supplied for this chapter stops at the end of fragmentation, before the database search; that
continuation is flagged in the Sources section rather than invented here.

## Proteins as sequences a spectrometer can read

A protein's behaviour is usually explained through a hierarchy of structure: the **primary
structure** is just the amino acid sequence (e.g. `...YSFVATAER...`); the **secondary** and
**tertiary structure** are the local and global folds that sequence produces; on top of that,
**modifications** (such as phosphorylation) and **processing** (proteolytic cleavage by an enzyme
such as trypsin, which activates or targets a protein — e.g. in platelet activity) change what the
protein does dynamically, without changing the underlying gene. Mass spectrometry-based proteomics
works by reading out sequence, modifications and processing directly from the physical mass of the
molecule, which is why it sits differently in "the central paradigm of biology" than a sequencing
readout of DNA or RNA: it measures the molecule that actually does the work, after everything that
happened to it since translation.

Twenty-odd amino acids are strung together into peptide backbones through **amide (peptide) bonds**:
an amino group on one residue reacts with the carboxyl group of the next, releasing water,

$$\text{amino group} + \text{carboxyl group} \rightarrow \text{peptide bond} + \text{H}_2\text{O},$$

giving a chain with a free amino terminus at one end and a free carboxyl terminus at the other,

$$\text{H}_2\text{N} - \text{CH}(\text{R}_1) - \text{CO} - \text{NH} - \text{CH}(\text{R}_2) - \text{CO} - \dots - \text{COOH},$$

where each residue contributes a side chain ($\text{R}_1, \text{R}_2, \dots$). The side chains vary
considerably in their physico-chemical properties — a fact worth holding on to, because it resurfaces
later: peptides built from different side chains do not behave identically once they reach the mass
spectrometer, and in particular they do not ionise equally well.

## Turning a peptide into a signal

A generalised mass spectrometer has three functional stages plus a digitiser: an **ion source**,
one or more **mass analysers**, and a **detector**, followed by a **digitiser** (an analog-to-digital
converter) that turns the detector's continuous analog signal into a discretised spectrum. The
mass analysers use electromagnetic fields to manipulate gas-phase ions and separate them; the result
is plotted with mass-over-charge ($m/z$) on the x-axis and ion intensity (absolute counts or
relative) on the y-axis. Two things have to happen before any of that can work: the sample has to be
**ionised** and brought into the gas phase, which is the job of the ion source, and the resulting ions
have to be **detected** as they arrive.

Two ion sources dominate proteomics, and they hand the analyser very different populations of ions:

- **MALDI** (matrix-assisted laser desorption/ionisation) fires a pulsed UV laser ($\lambda =
  337\,\text{nm}$, typically nitrogen) at a mixture of analyte and matrix molecules, triggering
  desorption and proton transfer into the gas phase under high vacuum. Ionisation between competing
  analyte molecules is competitive, and MALDI typically produces **singly charged** peptide ions. The
  term was coined by Karas and Hillenkamp (*Anal. Chem.*, 1985); Koichi Tanaka received the 2002 Nobel
  Prize in Chemistry for demonstrating MALDI ionisation of biological macromolecules (*Rapid Commun.
  Mass Spectrom.*, 1988).
- **ESI** (electrospray ionisation) nebulises the sample through a needle held at 3–5 kV, often
  heated to 40–100°C to help nebulisation and evaporation; droplets shrink until charge-driven fission
  or ion expulsion releases gas-phase ions, which pass through a barrier into the analyser inlet. ESI
  typically produces **multiply charged** peptide ions (2+, 3+, 4+). John Fenn received the 2002 Nobel
  Prize in Chemistry for demonstrating ESI ionisation of biological macromolecules (*Science*, 1989)
  — electrospray is also used, unrelated to biology, in the fine-control ion thrusters on satellites
  and interstellar probes.

**Resolution** matters for both identification and quantification: it is usually defined as the width
of a peak at a given height, most commonly at 50% of peak height (full width at half maximum, FWHM;
an alternative definition uses percent valley height instead). Resolution is what lets an instrument
tell the **average mass** of an ion population apart from its **monoisotopic mass** — the mass of the
single isotopic form built entirely from the lightest, most abundant isotopes (Eidhammer, Flikka,
Martens & Mikalsen, Wiley, 2007).

The most common **detector** in proteomics is the **electron multiplier**: a single incident ion
strikes a first dynode and knocks loose electrons, which are accelerated by rising voltages across a
chain of further dynodes (roughly 20 V, 40 V, 60 V, ... up to 120 V in the lecture's example), each
stage multiplying the electron count, until a single ion in produces on the order of $10^6$ electrons
out — a signal large enough to record.

## Why raw intensity is not a stable currency

The basic logic of MS-based **quantification** is that detector signal relates to quantity: make each
sample distinguishable (by introducing a mass difference between samples, or by running each sample
through the instrument separately), measure the intensity of each analyte in each sample, and then
statistically process the resulting numbers. That last step is where a statistics course earns its
keep, because the signal is not a clean, linear readout of abundance. Several things get in the way.

First, **not all peptides ionise equally**, so raw signal cannot be compared across different peptides
— only across the *same* peptide measured in different samples. A protein is inferred from its
constituent peptides' MS1 signal, but two different peptides from two different proteins are not
comparable just because their intensities can be read off the same axis.

Second, even for a fixed peptide compared to itself, the **detector response is non-linear at
extreme intensities**: plotting the measured $\log_2$ ratio between two conditions against the
expected $\log_2$ ratio, the measured values level off ("compress") as the true ratio moves away from
1:1 (Gevaert, *Proteomics*, 2007). At the same time, the **measurement error grows** as the ratio
departs from 1:1 (Vaudel, *Proteomics*, 2010), and both effects are still clearly visible even on
modern, high-resolution instruments such as the Orbitrap.

Third, **raw peak detection ("peak picking") is itself imprecise**. This step needs mass-spectrometer-
specific processing, it sets the lower limit of the instrument's usable dynamic range (via the
signal-to-noise ratio), and typical peak pickers introduce 5–10% error in the final reported ratios.
The size of the mass window used to fit a peak's shape matters too — using a peak-shape model that
does not match the true peak (a "non-adapted shape") can by itself add another 10% error (Vaudel,
*Proteomics*, 2010). Different software tools and libraries (e.g. Decon2LS) use different peak models,
and a peak in practice carries more information than a single $m/z$ value — its shape and profile can
be inspected directly in visualisation tools such as OpenMS's TOPPView.

Fourth, the sample itself is not stable before it ever reaches the instrument. **Serum proteins
degrade over time even in the best available sampling tubes** (Yi, *J. Prot. Res.*, 2007), and
**post-translational modifications are pervasive** enough to be a genuine identification problem, not
a rare exception. Re-analysing a public dataset (Kim et al., *Nature*, 2014) with the open
modification search engine *ionbot*, just six abundant glycolytic enzymes carried between 111 and 166
distinct modifications each, spread across 50 to 278 distinct peptides — including carbamylation,
carbamidomethylation, formylation, acetylation, oxidation, methylation, deamidation-type losses,
succinylation, and more.

All four effects point the same way: the number a mass spectrometer reports for a peptide is a
noisy, non-linear, sample-history-dependent proxy for the quantity a biologist actually wants, which
is exactly the gap that statistical modelling of proteomics data has to close.

## Reading the sequence back out: fragmentation and MS/MS

Identifying *which* peptide produced a signal, rather than just quantifying it, relies on
**fragmentation**. Tandem MS ("MS/MS") uses two mass analysers in series — or a single ion trap
performing the same two roles one after another — to do this: the first analyser acts as an **ion
selector**, letting through only ions of one chosen $m/z$ (the precursor); that selected ion is then
fragmented; and the second analyser separates the resulting fragment ions by mass, which the detector
records as the MS/MS spectrum.

<figure>
<svg viewBox="0 0 640 170" role="img" aria-label="Pipeline of tandem mass spectrometry from precursor ion selection through fragmentation to the MS/MS spectrum">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <g fill="none" stroke="currentColor" stroke-width="1.2">
    <rect x="10" y="52" width="108" height="60" rx="6"/>
    <rect x="140" y="52" width="112" height="60" rx="6"/>
    <rect x="274" y="52" width="100" height="60" rx="6"/>
    <rect x="396" y="52" width="120" height="60" rx="6"/>
    <rect x="538" y="52" width="96" height="60" rx="6"/>
  </g>
  <g font-size="10.5" fill="currentColor" text-anchor="middle">
    <text x="64" y="78">precursor</text>
    <text x="64" y="92">ions</text>
    <text x="196" y="78">1st analyser:</text>
    <text x="196" y="92">selects one m/z</text>
    <text x="324" y="82">fragmentation</text>
    <text x="456" y="78">2nd analyser:</text>
    <text x="456" y="92">sorts fragments</text>
    <text x="586" y="78">detector:</text>
    <text x="586" y="92">MS/MS spectrum</text>
  </g>
  <g stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)">
    <line x1="118" y1="82" x2="138" y2="82"/>
    <line x1="252" y1="82" x2="272" y2="82"/>
    <line x1="374" y1="82" x2="394" y2="82"/>
    <line x1="516" y1="82" x2="536" y2="82"/>
  </g>
</svg>
<figcaption>Tandem MS: the first mass analyser isolates a single precursor ion by m/z; fragmentation
breaks that precursor apart; the second analyser measures the resulting pieces, and the detector
records their masses as the MS/MS spectrum used for identification.</figcaption>
</figure>

Breaking the peptide backbone at different points produces two families of fragment ions, named for
which terminus they retain: ions that keep the **N-terminus** are called $a, b, c$ (numbered by how
many residues they contain, counting from the N-terminus: $a_1, b_1, c_1, a_2, b_2, c_2, \dots$), and
ions that keep the **C-terminus** are called $x, y, z$ (numbered from the C-terminus: $x_3, y_3, z_3,
\dots, x_1, y_1, z_1$) — a mnemonic link to the Roman alphabet, early letters for the N-terminal
series, late letters for the C-terminal one. This is the **Biemann nomenclature**, coined by
Roepstorff and Fohlmann (*Biomed. Mass Spec.*, 1984) and Klaus Biemann (*Biomed. Environ. Mass Spec.*,
1988). Other ion types exist, as do **internal fragments** — pieces that retain neither terminus —
which are harder to use for **ladder sequencing** (reading the amino acid sequence directly off the
regular mass differences between consecutive ions in one series) but can still be interpreted. In an
ideal case a peptide's fragment spectrum produces exactly such a directly interpretable ion ladder;
in practice, how well that ideal is met is what the rest of the identification pipeline — the
database search, decoys and protein inference promised by the lecture's outline — has to deal with.

## Sources

- Lecture notes: `docs/omics-statistics/statomics/sga21/docs/proteomics_data_analysis.md`, a
  model-reconstructed transcription of Lennart Martens's slide deck *"MS-based proteomics data
  analysis"* (talk title "Science meets life"), from the statOmics SGA21 course
  (`proteomics_data_analysis.pdf`, licensed CC BY-NC-SA 4.0). No separate slide file, transcript or
  problem set was supplied for this chapter — the note file *is* the reconstructed slide deck, produced
  by a model reading page images of a PDF with no extractable text layer. Its own header flags every
  equation as unverified and the prose as a paraphrase in places; that caveat carries over to the
  restatement here, which stays close to the wording and examples the file gives.
- The lecture's own outline slide (repeated twice in the source) lists three further topics not
  present in the supplied material and therefore not covered in this chapter: how a fragment spectrum
  is matched against a sequence database ("database search algorithms in three phases" and
  "sequential search algorithms"), how decoys are used to estimate a false discovery rate, and the
  problem of inferring a protein's identity from shared peptides ("protein inference: bad, ugly, and
  not so good"). The supplied file ends mid-way through the fragmentation section, at the slide
  captioned "in an ideal world, the peptide sequence will produce directly interpretable ion ladders."
- Specific results and images cited on the slides, attributed as the lecture attributes them: Karas &
  Hillenkamp, *Anal. Chem.* (1985); Tanaka, *Rapid Commun. Mass Spectrom.* (1988); Fenn, *Science*
  (1989); Eidhammer, Flikka, Martens & Mikalsen, Wiley (2007); Gevaert, *Proteomics* (2007); Yi, *J.
  Prot. Res.* (2007); Vaudel, *Proteomics* (2010); Roepstorff & Fohlmann, *Biomed. Mass Spec.* (1984);
  Biemann, *Biomed. Environ. Mass Spec.* (1988); Kim et al., *Nature* (2014), reanalysed with the
  *ionbot* search engine (`ionbot.cloud`); and a central-paradigm figure adapted from the NCBI Science
  Primer.

---

[← 25. Case-Study Datasets for msqrob2](25-case-study-datasets-for-msqrob2.md) · [Contents](index.md) · [27. Recap: The General Linear Model →](27-recap-the-general-linear-model.md)
