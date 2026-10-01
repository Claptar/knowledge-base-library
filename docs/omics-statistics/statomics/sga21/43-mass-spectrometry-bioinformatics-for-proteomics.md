---
title: "43. Mass Spectrometry & Bioinformatics for Proteomics"
course: "StatOmics Sga21"
chapter: 43
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 43. Mass Spectrometry & Bioinformatics for Proteomics

## What this covers

This unit of the course is not itself a lecture: it is a pointer the course inserts into the
syllabus, sending the reader to a seven-part external video series that carries the actual
mass-spectrometry content needed for the proteomics part of the course. No slides, transcript, or
lecturer's notes for that video series were supplied alongside this pointer — only the list of
titles, durations, and links below. So this chapter records the roadmap the course lays out
rather than the mass-spectrometry material itself, and says plainly where that material actually
lives. It assumes nothing beyond what a reader arriving at this point in the syllabus would
already have (the course's general proteomics framing) and exists so that a reader can see, before
clicking through, what order the seven videos build in and what each one is meant to establish.

## Why this chapter is a roadmap, not an exposition

The source document consists of a title and seven linked videos, nothing else — no worked
examples, no equations, no figures, no accompanying prose. Writing out the mechanics of ion
sources, mass analysers, detectors, or collision-induced dissociation here would mean inventing
that content rather than reporting it, since none of it was in what was supplied. The honest
version of this chapter is therefore the structure the course itself chose: which sub-topic comes
first, which comes last, and how long the course expects each to take. The actual teaching —
definitions, mechanisms, derivations — is in the videos themselves, linked below.

## The sequence the course sets out

The seven parts are presented in this order, under the shared heading "Lecture mass spectrometry
basics":

1. **Amino Acids and Proteins** (30:46) — the biochemical starting point: what is being measured
   before any instrument is introduced.
2. **Mass Spectrometry: Concepts and Components. Ion Sources** (39:30) — the general architecture
   of a mass spectrometer, then the first stage of it: how a sample is turned into ions.
3. **Mass Spectrometry: Analysers** (34:10) — the stage after ionisation, where ions are separated.
4. **Mass Spectrometry: Detectors** (19:01) — the stage after separation, where ions are counted.
5. **Mass Spectrometry: FT-IR and Orbitrap** (12:55) — two named instruments, presumably worked
   examples of the analyser/detector combination just introduced.
6. **Tandem Mass Spectrometry** (24:54) — a second round of mass analysis, layered on the single-
   stage instrument covered in parts 2–5.
7. **A CID Fragmentation Primer** (25:37) — the chemistry of collision-induced dissociation, the
   fragmentation step that tandem mass spectrometry depends on.

Read as a whole, the sequence moves from the biological substance being analysed (part 1), through
the successive physical stages a sample passes through inside a single mass spectrometer —
ionisation, separation, detection (parts 2–4) — to two concrete instruments built from those stages
(part 5), and finally to the two-stage, fragmentation-based version of the technique that
underlies most proteomics workflows (parts 6–7). That last pairing is the one the course's
bioinformatics material is built on top of: tandem MS and CID fragmentation are what produce the
spectra that downstream proteomics data analysis has to interpret.

## Sources

- `docs/omics-statistics/statomics/sga21/techvid.md` (converted from `techvid.Rmd`, statOmics
  SGA21, CC BY-NC-SA 4.0) — the titles, durations, and links for all seven parts listed above, and
  nothing else. No slides, transcript, or written notes for the video content were supplied.
- The lecture content itself lives only in the seven linked videos, external to this course's
  supplied material:
  - [Part 1 — Amino Acids and Proteins](https://www.youtube.com/watch?v=bS78rIYvFBE)
  - [Part 2 — Concepts and Components. Ion Sources](https://www.youtube.com/watch?v=vXsotPtOdRY)
  - [Part 3 — Analysers](https://www.youtube.com/watch?v=NKXhyjsgT1I)
  - [Part 4 — Detectors](https://www.youtube.com/watch?v=lxtPIyFnzGk)
  - [Part 5 — FT-IR and Orbitrap](https://www.youtube.com/watch?v=rLmpfFjNJd4)
  - [Part 6 — Tandem Mass Spectrometry](https://www.youtube.com/watch?v=Wy1SwrMzhYk)
  - [Part 7 — A CID Fragmentation Primer](https://www.youtube.com/watch?v=JBt_9hBnXcQ)

---

[← 42. Testing for Differential Protein Abundance](42-testing-for-differential-protein-abundance.md) · [Contents](index.md)
